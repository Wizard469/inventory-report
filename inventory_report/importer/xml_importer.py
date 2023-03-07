from inventory_report.inventory.inventory import Inventory
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        return Inventory.read_xml(path)
