from inventory_report.inventory.inventory import Inventory
from .importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        return Inventory.read_json(path)
