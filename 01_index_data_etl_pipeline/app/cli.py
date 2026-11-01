import argparse
from app.config import settings
from app.logging_config import configure_logging
from app.pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("--input", required=True)
    run.add_argument("--output", default="output")
    args = parser.parse_args()
    configure_logging(settings.log_level)
    if args.command == "run":
        result = run_pipeline(args.input, args.output)
        print(result.to_string(index=False))
if __name__ == "__main__": main()
