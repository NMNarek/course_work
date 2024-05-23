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

    def mask_payment_info(self, payment_info: str) -> str:
        """
        замена приватных данных на ***
        :param payment_info:
        :return:
        """
        user_payment_info: list[str] = payment_info.split(" ")
        number_card = user_payment_info.pop(-1)
        if payment_info.startswith("Счет"):
            number_card = "**" + number_card[-4:]
        elif not payment_info:
            number_card = ""
        else:
            number_card = number_card[:6] + "******" + number_card[-4:]
        number_card = "".join([number_card[i:i + 4] for i in range(0, len(number_card),4)])
        user_payment_info.append(number_card)
        return " ".join(user_payment_info)

    def __lt__(self, other):
        return self.date < other.date

    def __gt__(self, other):
        return self.date > other.date

    def __str__(self):
        from_ = self.mask_payment_info(self.from_)
        delimiter = " -> " if from_ else ""
        return (
            f"{self.convert_date()} {self.description}\n"
            f"{from_}{delimiter}{self.mask_payment_info(self.to)}\n"
            f"{self.amount} {self.currency_name}"
        )

