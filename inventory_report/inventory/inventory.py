from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path, type):
        if path.endswith(".csv"):
            product_list = Inventory.read_csv(path)
        elif path.endswith(".json"):
            product_list = Inventory.read_json(path)
        elif path.endswith(".xml"):
            product_list = Inventory.read_xml(path)

        return Inventory.select_type(product_list, type)

    def select_type(product_list, type):
        if type == "simples":
            return SimpleReport.generate(product_list)
        elif type == "completo":
            return CompleteReport.generate(product_list)

    def read_csv(path):
        product_list = []
        with open(path) as f:
            products = csv.DictReader(f)
            for product in products:
                product_list.append(product)
        return product_list

    def read_json(path):
        with open(path) as f:
            return json.load(f)

    def read_xml(path):
        with open(path) as f:
            return xmltodict.parse(f.read())["dataset"]["record"]
