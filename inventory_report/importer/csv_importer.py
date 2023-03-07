from inventory_report.inventory.inventory import Inventory
from .importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        return Inventory.read_csv(path)
