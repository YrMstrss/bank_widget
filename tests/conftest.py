import pytest
import os


@pytest.fixture
def file():
    return os.path.join(os.path.dirname(__file__), 'test.json')


@pytest.fixture
def data():
    return  [{
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
      "amount": "56883.54",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  },
  {
    "id": 596171168,
    "state": "EXECUTED",
    "date": "2018-07-11T02:26:18.671407",
    "operationAmount": {
      "amount": "79931.03",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 72082042523231456215"
  },
  {
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
    "operationAmount": {
      "amount": "40701.91",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 5999414228426353",
    "to": "Счет 72731966109147704472"
  },
  {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
      "description": "Перевод организации",
      "from": "Visa Platinum 1246377376343588",
      "to": "Счет 14211924144426031657"
  }]
