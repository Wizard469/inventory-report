from datetime import datetime as dt
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(report):
        oldest_date = min(product["data_de_fabricacao"] for product in report)

        expiration_date = min(
            product["data_de_validade"]
            for product in report
            if dt.strptime(product["data_de_validade"], "%Y-%m-%d")
            >= dt.today()
        )

        count_company_products = Counter(
            product["nome_da_empresa"] for product in report
        )

        company = max(count_company_products, key=count_company_products.get)

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {company}"
        )
