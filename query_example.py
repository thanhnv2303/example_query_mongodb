import os
import sys

from mongodb import Database

TOP_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(TOP_DIR, './'))


def example():
    mongodb = Database()

    from_address = "0xef575087f1e7bec54046f98119c8c392a37c51dd"
    wallet = mongodb.get_wallet(from_address)
    transactions = mongodb.get_transactions_transfer_from(from_address)

    print("-------------------------------------------------------")
    print("wallet info:")
    print(wallet)
    print("-------------------------------------------------------")
    print("transactions from address :", from_address)
    for transaction in transactions:
        print(transaction)


if __name__ == '__main__':
    example()
