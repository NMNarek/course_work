from datetime import datetime


class Operation:
    def __init__(
            self,
            state: str,
            date: str,
            amount: str,
            currency_name: str,
            description: str,
            from_: str | None,
            to: str,
    ):
        self.state = state
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_ if from_ is not None else ""
        self.to = to

    def convert_date(self) -> str:
        """
        конвертируем дату в нужный формат
        :return:
        """
        iso_date = datetime.fromisoformat(self.date)
        return iso_date.strftime("%d.%m.%Y")
