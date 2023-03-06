from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, type):
        report_list = Inventory.read_csv(path)

        if type == "simples":
            return SimpleReport.generate(report_list)
        elif type == "completo":
            return CompleteReport.generate(report_list)

    def read_csv(path):
        report_list = []
        with open(path, encoding="utf-8-sig") as f:
            reports = csv.DictReader(f)
            for report in reports:
                report_list.append(report)
        return report_list
