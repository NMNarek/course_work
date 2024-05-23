import pytest

from src.classes import Operation


@pytest.fixture
def operation():
    return Operation(
        state="EXECUTED",
        from_=None,
        date="2019-07-12T20:41:47.882230",
        amount="51463.70",
        currency_name="USD",
        description="Перевод с карты на счет",
        to="Счет 96527012349577388612"
    )


@pytest.fixture
def operations():
    return [Operation(
        state="EXECUTED",
        from_=None,
        date="2019-07-12T20:41:47.882230",
        amount="51463.70",
        currency_name="USD",
        description="Перевод с карты на счет",
        to="Счет 96527012349577388612"
    ),
        Operation(
            state="EXECUTED",
            from_=None,
            date="2018-07-12T20:41:47.882230",
            amount="51463.70",
            currency_name="USD",
            description="Перевод с карты на счет",
            to="Счет 96527012349577388612"
        ),
        Operation(
            state="EXECUTED",
            from_=None,
            date="2017-07-12T20:41:47.882230",
            amount="51463.70",
            currency_name="USD",
            description="Перевод с карты на счет",
            to="Счет 96527012349577388612"
        ),
        Operation(
            state="EXECUTED",
            from_=None,
            date="2024-07-12T20:41:47.882230",
            amount="51463.70",
            currency_name="USD",
            description="Перевод с карты на счет",
            to="Счет 96527012349577388612"
        )
    ]


@pytest.fixture
def list_with_dicts():
    return [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
    ]
