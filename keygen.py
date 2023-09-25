from argparse import ArgumentParser
from keys import OEMKey, RetailKey, OfficeKey


def main() -> None:
    if args.oem:
        print(f"OEM key: {OEMKey.generate()}")
    elif args.retail:
        print(f"Retail key: {RetailKey.generate()}")
    elif args.office:
        print(f"Office 97 key: {OfficeKey.generate()}")
    elif args.key:
        if OEMKey.validate(args.key):
            print("OEM key is valid")
        elif RetailKey.validate(args.key):
            print("Retail key is valid")
        elif OfficeKey.validate(args.key):
            print("Office 97 key is valid")
        else:
            print("Key is invalid")
    else:
        print(f"OEM key: {OEMKey.generate()}")
        print(f"Retail key: {RetailKey.generate()}")
        print(f"Office 97 key: {OfficeKey.generate()}")


if __name__ == "__main__":
    parser = ArgumentParser(description="win95-keygen - Windows 95 & Office 97 key generator/validator")
    parser.add_argument(
        "-o", "--oem",
        action="store_true",
        help="generate an OEM key"
    )
    parser.add_argument(
        "-r", "--retail",
        action="store_true",
        help="generate a retail key"
    )
    parser.add_argument(
        "-f", "--office",
        action="store_true",
        help="generate an Office 97 key"
    )
    parser.add_argument(
        "key",
        nargs="?",
        help="key to validate"
    )
    args = parser.parse_args()

    main()
