def test_operation_init(operation):
    assert operation.from_ == ""


def test_operation_convert_date(operation):
    assert isinstance(operation.convert_date(), str)
    assert operation.convert_date() == "12.07.2019"


def test_operation_str(operation):
    assert str(operation) == ("12.07.2019 Перевод с карты на счет\n"
                              "Счет **8612\n"
                              "51463.70 USD")


def test_operation_mask_payment_info(operation):
    assert operation.mask_payment_info("96527012349577388612") == "965270******8612"
