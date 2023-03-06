from inventory_report.inventory.product import Product
from datetime import datetime as dt

start_date = dt.now().date()

if start_date.month == 3 and start_date.day == 29:
    end_date = start_date.replace(start_date.year + 1, 3, start_date.day - 1)
else:
    end_date = start_date.replace(start_date.year + 1)


def test_cria_produto():
    new_product = Product(
        1,
        "Barabam",
        "Xablau industries",
        start_date,
        end_date,
        "126547853156589",
        "The way you want to",
    )

    assert new_product.id == 1
    assert new_product.nome_do_produto == "Barabam"
    assert new_product.nome_da_empresa == "Xablau industries"
    assert new_product.data_de_fabricacao == str(start_date)
    assert new_product.data_de_validade == str(end_date)
    assert new_product.numero_de_serie == "126547853156589"
    assert new_product.instrucoes_de_armazenamento == "The way you want to"
