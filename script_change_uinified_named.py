import os
import sys

from mongodb import Database

TOP_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, os.path.join(TOP_DIR, './'))

VENUS_TOKEN = [
    "0x595e9DDfEbd47B54b996c839Ef3Dd97db3ED19bA",
    "0x49fADE95f94e5EC7C1f4AE13a6d6f9ca18B2F430",
    "0xf6C14D4DFE45C132822Ce28c646753C54994E59C",
    "0xfD36E2c2a6789Db23113685031d7F16329158384",
    "0x004065D34C6b18cE4370ced1CeBDE94865DbFAFE",
    "0x793ff22b882665CA492843962aD945cAf5440F3c",
    "0xf9f48874050264664bf3d383C7289a0a5BD98896",
    "0x47BEAd2563dCBf3bF2c9407fEa4dC236fAbA485A",
    "0x4BD17003473389A42DAF6a0a729f6Fdb328BbBd7",
    "0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d",
    "0x55d398326f99059fF775485246999027B3197955",
    "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
    "0xcF6BB5389c92Bdda8a3747Ddb454cB7a64626C63",
    "0x7130d2A12B9BCbFAe4f2634d864A1Ee1Ce3Ead9c",
    "0x2170Ed0880ac9A755fd29B2688956BD959F933F8",
    "0x4338665CBB7B2485A8855A139b75D5e34AB0DB94",
    "0x1D2F0da169ceB9fC7B3144628dB156f3F6c60dBE",
    "0xecA88125a5ADbe82614ffC12D0DB554E2e2867C8",
    "0xfD5840Cd36d94D7229439859C0112a4185BC0255",
    "0x95c78222B3D6e262426483D42CfA53685A67Ab9D",
    "0x2fF3d0F6990a40261c66E1ff2017aCBc282EB6d0",
    "0xA07c5b74C9B40447a954e1466938b865b6BBea36",
    "0x151B1e2635A717bcDc836ECd6FbB62B674FE3E1D",
    "0x882C173bC7Ff3b7786CA16dfeD3DFFfb9Ee7847B",
    "0xf508fCD89b8bd15579dc79A6827cB4686A3592c8",
    "0x57A5297F2cB2c0AaC9D554660acd6D385Ab50c6B",
    "0xB248a295732e0225acd3337607cc01068e3b9c10",
    "0x939bD8d64c0A9583A7Dcea9933f7b21697ab6396",
    "0x406f48f47D25E9caa29f17e7Cfbd1dc6878F078f",
    "0x516c18DC440f107f12619a6d2cc320622807d0eE"
]

mongodb = Database()

for token in VENUS_TOKEN:
    collection = token.lower()
    print(collection)
    type_ = "token_transfer"
    transfers = mongodb.get_event(collection, type_)
    for transfer in transfers:
        transfer["type"] = "Transfer"
        print(transfer)
        mongodb.update_event(collection, transfer)

    type_ = "event"
    events = mongodb.get_event(collection, type_)
    for event in events:
        event["type"] = event.pop("event_type")
        print(event)
        mongodb.update_event(collection, event)

    type_ = "Transfer"
    transfers = mongodb.get_event(collection, type_)
    for transfer in transfers:
        address = transfer.get("token_address")
        if address:
            transfer["contract_address"] = transfer.pop("token_address")
        print(transfer)
        mongodb.update_event(collection, transfer)
