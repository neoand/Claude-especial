#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tech Scanner - Auto-Detection de Tecnologias
Analisa projetos e identifica tecnologias automaticamente
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Set
from dataclasses import dataclass

@dataclass
class TechDetection:
    """Resultado da detecção de tecnologia"""
    name: str
    category: str
    confidence: float  # 0.0 a 1.0
    evidence: List[str]  # Arquivos/padrões encontrados
    version: str = "unknown"
    patterns: List[str] = None

class TechScanner:
    """Scanner automático de tecnologias em projetos"""

    def __init__(self):
        self.tech_patterns = self._load_tech_patterns()
        self.detection_rules = self._load_detection_rules()

    def _load_tech_patterns(self) -> Dict[str, Dict]:
        """Carrega patterns de detecção para cada tecnologia"""
        return {
            # Backend Frameworks
            "nodejs": {
                "category": "backend",
                "files": ["package.json", "package-lock.json", "yarn.lock"],
                "patterns": [r"node\s+v?(\d+\.\d+)", r'"engines":\s*{\s*"node":'],
                "dependencies": ["express", "fastify", "koa", "nest"],
                "confidence_threshold": 0.8
            },
            "python": {
                "category": "backend",
                "files": ["requirements.txt", "pyproject.toml", "Pipfile", "setup.py"],
                "patterns": [r"python\s*(\d+\.\d+)", r"version\s*=\s*[\"\'](\d+\.\d+)"],
                "dependencies": ["django", "flask", "fastapi", "celery", "sqlalchemy"],
                "confidence_threshold": 0.8
            },
            "django": {
                "category": "backend",
                "files": ["manage.py", "settings.py", "wsgi.py"],
                "patterns": [r"from django", r"Django\s+(\d+\.\d+)"],
                "dependencies": ["django", "djangorestframework"],
                "confidence_threshold": 0.9
            },
            "fastapi": {
                "category": "backend",
                "files": ["main.py", "app.py"],
                "patterns": [r"from fastapi", r"FastAPI\s*\("],
                "dependencies": ["fastapi", "uvicorn"],
                "confidence_threshold": 0.9
            },

            # Frontend Frameworks
            "react": {
                "category": "frontend",
                "files": ["package.json"],
                "patterns": [r"react\s+(\d+\.\d+)", r"import.*React", r"React\."],
                "dependencies": ["react", "react-dom"],
                "file_extensions": [".jsx", ".tsx"],
                "confidence_threshold": 0.8
            },
            "nextjs": {
                "category": "frontend",
                "files": ["next.config.js", "next.config.mjs"],
                "patterns": [r"next\s+(\d+\.\d+)", r"from 'next'"],
                "directories": ["pages", "app"],
                "dependencies": ["next", "react"],
                "confidence_threshold": 0.9
            },
            "vue": {
                "category": "frontend",
                "files": ["vue.config.js", "vite.config.ts"],
                "patterns": [r"vue\s+(\d+\.\d+)", r"<template>", r"export default\s*\{"],
                "file_extensions": [".vue"],
                "dependencies": ["vue"],
                "confidence_threshold": 0.9
            },

            # Databases
            "postgresql": {
                "category": "database",
                "files": ["postgresql.conf", "pg_hba.conf"],
                "patterns": [r"postgresql", r"pg_"],
                "dependencies": ["psycopg2", "pg", "@libsql/client"],
                "connection_strings": [r"postgresql://", r"postgres://"],
                "confidence_threshold": 0.8
            },
            "mongodb": {
                "category": "database",
                "files": ["mongod.conf"],
                "patterns": [r"mongodb://", r"mongoose"],
                "dependencies": ["mongodb", "mongoose"],
                "confidence_threshold": 0.9
            },
            "redis": {
                "category": "database",
                "files": ["redis.conf"],
                "patterns": [r"redis://", r"Redis"],
                "dependencies": ["redis", "ioredis"],
                "confidence_threshold": 0.8
            },

            # Infrastructure
            "docker": {
                "category": "infrastructure",
                "files": ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"],
                "patterns": [r"FROM\s+\w+", r"version:\s*[\'\"]3\.[78]"],
                "confidence_threshold": 0.9
            },
            "kubernetes": {
                "category": "infrastructure",
                "files": ["k8s/", "kubernetes/", "*.yaml", "*.yml"],
                "patterns": [r"apiVersion:\s*v1", r"kind:\s*(Deployment|Pod|Service)"],
                "directories": ["deployments", "services", "configmaps"],
                "confidence_threshold": 0.9
            },

            # Odoo Specific
            "odoo": {
                "category": "odoo",
                "files": ["__manifest__.py", "odoo.conf", "__openerp__.py"],
                "patterns": [r"odoo\.", r"_inherit\s*=\s*[\'\"].*[\'\"]", r"odoo-bin"],
                "directories": ["models", "views", "controllers"],
                "file_extensions": [".xml"],
                "confidence_threshold": 0.9
            },

            # Communication
            "websockets": {
                "category": "communication",
                "files": ["*.js", "*.ts", "*.py"],
                "patterns": [r"WebSocket", r"socket\.io", r"ws://"],
                "dependencies": ["ws", "socket.io", "websockets"],
                "confidence_threshold": 0.8
            },

            # Security
            "jwt": {
                "category": "security",
                "patterns": [r"jwt", r"JSON Web Token"],
                "dependencies": ["jsonwebtoken", "PyJWT", "jose"],
                "confidence_threshold": 0.9
            }
        }

    def scan_project(self, project_path: str) -> List[TechDetection]:
        """
        Escaneia um projeto e detecta tecnologias usadas

        Args:
            project_path: Caminho para o projeto

        Returns:
            Lista de tecnologias detectadas
        """
        project_path = Path(project_path)
        detections = []

        for tech_name, patterns in self.tech_patterns.items():
            detection = self._detect_technology(project_path, tech_name, patterns)
            if detection and detection.confidence >= patterns["confidence_threshold"]:
                detections.append(detection)

        return sorted(detections, key=lambda x: x.confidence, reverse=True)

    def _detect_technology(self, project_path: Path, tech_name: str, patterns: Dict) -> TechDetection:
        """Detecta uma tecnologia específica no projeto"""
        evidence = []
        confidence = 0.0
        version = "unknown"

        # 1. Check files
        for file_pattern in patterns.get("files", []):
            found_files = list(project_path.rglob(file_pattern))
            if found_files:
                evidence.append(f"Found {file_pattern}")
                confidence += 0.3

                # Extract version from package files
                if file_pattern in ["package.json", "requirements.txt", "pyproject.toml"]:
                    version = self._extract_version_from_file(found_files[0], tech_name)

        # 2. Check directories
        for directory in patterns.get("directories", []):
            if (project_path / directory).exists():
                evidence.append(f"Found directory: {directory}")
                confidence += 0.2

        # 3. Check file extensions
        for ext in patterns.get("file_extensions", []):
            if list(project_path.rglob(f"*{ext}")):
                evidence.append(f"Found {ext} files")
                confidence += 0.2

        # 4. Search for patterns in files
        for pattern in patterns.get("patterns", []):
            matches = self._search_pattern_in_files(project_path, pattern)
            if matches:
                evidence.extend(matches[:3])  # Limit to 3 matches
                confidence += 0.3

        # 5. Check dependencies
        dependencies = patterns.get("dependencies", [])
        if dependencies:
            found_deps = self._check_dependencies(project_path, dependencies)
            if found_deps:
                evidence.append(f"Found dependencies: {', '.join(found_deps)}")
                confidence += 0.4

        # 6. Check connection strings
        for conn_pattern in patterns.get("connection_strings", []):
            if self._search_pattern_in_files(project_path, conn_pattern):
                evidence.append(f"Found connection pattern")
                confidence += 0.5

        # Calculate final confidence
        confidence = min(confidence, 1.0)

        if confidence >= patterns["confidence_threshold"]:
            return TechDetection(
                name=tech_name,
                category=patterns["category"],
                confidence=confidence,
                evidence=evidence,
                version=version
            )

        return None

    def _search_pattern_in_files(self, project_path: Path, pattern: str) -> List[str]:
        """Busca por padrão em todos os arquivos do projeto"""
        matches = []

        # Files to search (limit to common file types)
        file_types = [".py", ".js", ".ts", ".json", ".yml", ".yaml", ".md", ".txt", ".conf", ".xml"]

        for file_path in project_path.rglob("*"):
            if file_path.is_file() and file_path.suffix in file_types:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if re.search(pattern, content, re.IGNORECASE):
                            matches.append(f"Pattern in {file_path.relative_to(project_path)}")
                            if len(matches) >= 5:  # Limit matches
                                break
                except Exception:
                    continue

        return matches

    def _check_dependencies(self, project_path: Path, dependencies: List[str]) -> List[str]:
        """Verifica se dependências específicas estão presentes"""
        found_deps = []

        # Check package.json
        package_json = project_path / "package.json"
        if package_json.exists():
            try:
                with open(package_json) as f:
                    pkg_data = json.load(f)
                    all_deps = list(pkg_data.get("dependencies", {}).keys())
                    all_deps.extend(pkg_data.get("devDependencies", {}).keys())

                    for dep in dependencies:
                        if dep in all_deps:
                            found_deps.append(dep)
            except Exception:
                pass

        # Check requirements.txt
        requirements_txt = project_path / "requirements.txt"
        if requirements_txt.exists():
            try:
                with open(requirements_txt) as f:
                    content = f.read()
                    for dep in dependencies:
                        if re.search(rf"^{re.escape(dep)}", content, re.MULTILINE):
                            found_deps.append(dep)
            except Exception:
                pass

        return found_deps

    def _extract_version_from_file(self, file_path: Path, tech_name: str) -> str:
        """Extrai versão da tecnologia de arquivos de configuração"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if file_path.name == "package.json":
                data = json.loads(content)
                return data.get("dependencies", {}).get(tech_name, "unknown")
            elif file_path.name == "requirements.txt":
                # Procura por tech_name==version
                pattern = rf"{re.escape(tech_name)}[=<>!]+([0-9\.]+)"
                match = re.search(pattern, content)
                return match.group(1) if match else "unknown"

        except Exception:
            pass

        return "unknown"

    def generate_tech_report(self, detections: List[TechDetection]) -> str:
        """Gera relatório de tecnologias detectadas"""
        if not detections:
            return "No technologies detected."

        report = "# 🔍 Technology Detection Report\n\n"
        report += f"**{len(detections)} technologies detected**\n\n"

        # Group by category
        by_category = {}
        for detection in detections:
            category = detection.category
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(detection)

        for category, techs in by_category.items():
            report += f"## {category.title()}\n\n"

            for tech in sorted(techs, key=lambda x: x.confidence, reverse=True):
                confidence_pct = int(tech.confidence * 100)
                report += f"### 📦 {tech.name.title()}\n"
                report += f"- **Confidence:** {confidence_pct}%\n"
                if tech.version != "unknown":
                    report += f"- **Version:** {tech.version}\n"
                report += f"- **Evidence:** {', '.join(tech.evidence[:3])}\n"
                report += "\n"

        return report

def main():
    """Função principal para CLI"""
    import argparse

    parser = argparse.ArgumentParser(description="Scan project for technologies")
    parser.add_argument("path", help="Path to project directory")
    parser.add_argument("--output", "-o", help="Output file for report")
    parser.add_argument("--json", action="store_true", help="Output JSON format")

    args = parser.parse_args()

    scanner = TechScanner()
    detections = scanner.scan_project(args.path)

    if args.json:
        result = {
            "project_path": args.path,
            "timestamp": "2025-11-18T16:30:00Z",
            "technologies": [
                {
                    "name": d.name,
                    "category": d.category,
                    "confidence": d.confidence,
                    "version": d.version,
                    "evidence": d.evidence
                }
                for d in detections
            ]
        }
        print(json.dumps(result, indent=2))
    else:
        report = scanner.generate_tech_report(detections)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to {args.output}")
        else:
            print(report)

if __name__ == "__main__":
    main()