"""
Geração do relatório STRIDE a partir dos componentes identificados no diagrama.
STRIDE: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.
"""

from pathlib import Path
from typing import List, Optional

from src.vulnerabilities.lookup import VulnerabilityLookup
from .threat_definitions import THREAT_DEFINITIONS

# Componente: {"type": str, "label": str, "bbox": ...}


STRIDE_CATEGORIES = [
    "Spoofing",
    "Tampering",
    "Repudiation",
    "Information Disclosure",
    "Denial of Service",
    "Elevation of Privilege",
]


class STRIDEReportGenerator:
    """
    Gera relatório de ameaças STRIDE por componente.
    """

    def __init__(self, vulnerabilities_source: Optional[VulnerabilityLookup] = None):
        self.vulnerabilities_source = vulnerabilities_source if vulnerabilities_source else VulnerabilityLookup()

    def generate(self, components: List[dict], ai_threats: Optional[str] = None, output_path: Optional[Path] = None) -> str:
        """
        Gera o relatório (texto ou HTML) a partir da lista de componentes.
        Se output_path for informado, salva o relatório no arquivo.
        """
        report_lines = [
            "# Relatório de Modelagem de Ameaças (STRIDE)",
            "",
            "## Componentes identificados",
            "",
        ]
        for i, comp in enumerate(components, 1):
            report_lines.append(f"{i}. **{comp.get('label', 'N/A')}** ({comp.get('type', 'N/A')})")
        report_lines.append("")
        report_lines.append("## Ameaças por categoria STRIDE (Análise Tradicional)")
        report_lines.append("")
        for cat in STRIDE_CATEGORIES:
            report_lines.append(f"### {cat}")
            for comp in components:
                comp_type = comp.get("type", "default")
                
                threats = self.vulnerabilities_source.get_threats(comp_type, cat)
                countermeasures = self.vulnerabilities_source.get_countermeasures(comp_type, cat)
                
                if threats:
                    report_lines.append(f"#### Componente: {comp.get('label', 'N/A')}")
                    for threat in threats:
                        report_lines.append(f"- **Ameaça:** {threat}")
                    if countermeasures:
                        for countermeasure in countermeasures:
                            report_lines.append(f"  - **Contramedida:** {countermeasure}")
            report_lines.append("")
        
        if ai_threats:
            report_lines.append("## Ameaças Identificadas pela IA")
            report_lines.append("")
            report_lines.append(ai_threats)

        report = "\n".join(report_lines)
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(report, encoding="utf-8")
        return report
