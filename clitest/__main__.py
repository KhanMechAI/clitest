import argparse
import logging


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Script with positional and optional arguments"
    )
    parser.add_argument("positional_arg", help="A positional argument")
    parser.add_argument("--optional_arg1", help="An optional argument 1")
    parser.add_argument("--optional_arg2", help="An optional argument 2")
    return parser


def process_args(args: argparse.Namespace) -> None:
    logging.info("Positional argument provided: %s", args.positional_arg)
    if args.optional_arg1:
        logging.info("Optional argument 1 provided: %s", args.optional_arg1)
    else:
        logging.info("Optional argument 1 not provided")
    if args.optional_arg2:
        logging.info("Optional argument 2 provided: %s", args.optional_arg2)
    else:
        logging.info("Optional argument 2 not provided")


def main() -> None:
    setup_logging()
    parser = cli()
    args = parser.parse_args()
    process_args(args)


if __name__ == "__main__":
    main()
