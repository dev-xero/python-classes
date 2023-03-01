from time import sleep


class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer: str, bank: str, acnt: str, limit: int):
        """

        Create a new credit card instance

        The initial balance is zero

        [customer]  the name of the customer  (e.g., Takeshi Matsuno)
        [bank]      the name of the bank  (e.g., Bank of Japan)
        [acnt]      the account identifier  (e.g., 5408 3412 5580 5912)
        [limit]     credit limit  (measured in dollars)
        [tax]       tax applied to transactions

        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0
        self._tax = 0.15

    def get_customer(self) -> str:
        """Return the name of the customer"""
        return self._customer

    def get_bank(self) -> str:
        """Return bank's name"""
        return self._bank

    def get_account(self) -> str:
        """Return card identifying number"""
        return self._acnt

    def get_balance(self) -> int:
        """Return current balance"""
        return self._balance

    def get_limit(self) -> int:
        """Return the current credit limit"""
        return self._limit

    def charge(self, price: int) -> bool:
        """

        Charge given price to the card assuming sufficient credit limit

        return True if charge was process else return False

        """

        if (price + self._balance) > self._limit:  # if charge will exceed limit
            return False  # cannot accept charge

        else:
            self._balance += price
            return True  # accept charge

    def credit_account(self, amount: int) -> str:
        """Credit the account if the transaction does not exceed limits"""
        return f"Your account has been credited with ${amount}\n\tCurrent Balance: ${cc.get_balance()}" \
            if self.charge(amount) \
            else \
            "Cannot credit your account, the transaction exceeds your account limit."

    def make_payment(self, amount: int) -> str:
        """

        Process customer payment that reduces balance

        [amount]       amount to be charged from this card
        [payment_tax]  tax to be applied on this transaction

        """

        payment_tax = amount * self._tax
        self._balance -= (amount + payment_tax)

        return f"\n--- Transaction successful ---" \
               f"\n\tAmount Charged: ${amount}" \
               f"\n\tTax: ${payment_tax}" \
               f"\n\tCurrent Balance: {self._balance}"


if __name__ == "__main__":
    cc = CreditCard(
        acnt="1234 6789 9921 1330",
        bank="Xero AI Bank",
        customer="Xero",
        limit=900_000_000
    )

    credit = 320_000

    times = 10

    while times > 0:
        print(cc.credit_account(credit))
        times -= 1
        sleep(1)

    print(cc.make_payment(2_400))
