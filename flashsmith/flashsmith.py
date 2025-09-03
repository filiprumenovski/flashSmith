import argparse
from .validator import load_and_validate_csv
from .builder import build_package_grouped

def main():
    parser = argparse.ArgumentParser(description="Build Anki deck from CSV")
    parser.add_argument("csv", help="Path to input CSV")
    parser.add_argument("--out", required=True, help="Output folder for .apkg")
    parser.add_argument("--dry-run", action="store_true", help="Validate only")
    args = parser.parse_args()

    rows = load_and_validate_csv(args.csv)
    build_package_grouped(rows, out_dir=args.out, dry_run=args.dry_run)

if __name__ == "__main__":
    raise SystemExit(main())
