from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, type):
        if path.endswith(".csv"):
            report_list = Inventory.read_csv(path)
        elif path.endswith(".json"):
            report_list = Inventory.read_json(path)
        elif path.endswith(".xml"):
            report_list = Inventory.read_xml(path)

        if type == "simples":
            return SimpleReport.generate(report_list)
        elif type == "completo":
            return CompleteReport.generate(report_list)

    def read_csv(path):
        report_list = []
        with open(path) as f:
            reports = csv.DictReader(f)
            for report in reports:
                report_list.append(report)
        return report_list

    def read_json(path):
        with open(path) as f:
            return json.load(f)

    def read_xml(path):
        with open(path) as f:
            return xmltodict.parse(f.read())["dataset"]["record"]
