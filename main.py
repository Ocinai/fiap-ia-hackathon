import argparse
from pathlib import Path

from src.diagram_parser.parser import DiagramParser
from src.stride_report.report import STRIDEReportGenerator
from src.vulnerabilities.lookup import VulnerabilityLookup

def main() -> None:
    parser = argparse.ArgumentParser(description="Gera relatório STRIDE a partir de diagrama de arquitetura.")
    parser.add_argument("--image", type=Path, help="Caminho da imagem do diagrama")
    parser.add_argument("--output", type=Path, default=Path("report.md"), help="Caminho do relatório de saída")
    args = parser.parse_args()

    if not args.image or not args.image.exists():
        print("Forneça uma imagem válida com --image path/to/diagram.png")
        return

    diagram_parser = DiagramParser()
    components = diagram_parser.parse(args.image)
    
    vuln_lookup = VulnerabilityLookup()
    report_gen = STRIDEReportGenerator(vulnerabilities_source=vuln_lookup)
    
    report_gen.generate(components, output_path=args.output)
    print(f"Relatório salvo em {args.output}")


if __name__ == "__main__":
    main()
