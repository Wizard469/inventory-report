from inventory_report.reports.simple_report import SimpleReport
from collections import Counter

class CompleteReport(SimpleReport):
    @staticmethod
    def generate(report):
        simple_report = SimpleReport.generate(report)

        companies = Counter(product["nome_da_empresa"] for product in report)

        format = ["Produtos estocados por empresa:\n"]

        for company in companies:
            format.append(f"- {company}: {companies[company]}\n")

        formatted = "".join(format)

        return (
            f"{simple_report}\n"
            f"{formatted}"
        )
