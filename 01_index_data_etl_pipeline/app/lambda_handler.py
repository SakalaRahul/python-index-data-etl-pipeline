import os, tempfile
from app.pipeline import run_pipeline
from app.s3_io import download_s3_object, upload_file

def handler(event, context):
    # Expected event: {"input_key":"incoming/prices.csv","output_prefix":"processed/"}
    input_key = event.get("input_key") or os.environ.get("S3_INPUT_KEY")
    if not input_key:
        raise ValueError("input_key is required")
    with tempfile.TemporaryDirectory() as tmp:
        source = f"{tmp}/prices.csv"
        download_s3_object(input_key, source)
        run_pipeline(source, f"{tmp}/output")
        upload_file(f"{tmp}/output/index_snapshots.csv",
                    f"{event.get('output_prefix', 'processed/') }index_snapshots.csv")
    return {"statusCode": 200, "body": "Index pipeline completed"}
