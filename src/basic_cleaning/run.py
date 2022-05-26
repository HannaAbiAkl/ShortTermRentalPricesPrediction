#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    # Initialize WANDB

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact.

    artifact_local_path = wandb.use_artifact("sample.csv:latest").file()
    logger.info(f"Input File: {args.input_artifact}")
    df = pd.read_csv(artifact_local_path)

    # Drop outliers
    
    min_price = args.min_price
    max_price = args.max_price
    logger.info(f"Min: {min_price}")
    logger.info(f'Max: {max_price}')

    # Ensure price is between minimum and maximum values

    idx = df['price'].between(min_price, max_price)
    df = df[idx].copy()

    # Convert last_review to datetime

    df['last_review'] = pd.to_datetime(df['last_review'])
    logger.info('Successfully converted last_review to datetime')

    # Fig geolocation bug

    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()

    # Save results to CSV
    
    df.to_csv("clean_sample.csv", index=False)

    # Upload CSV artifact to WANDB
    
    artifact = wandb.Artifact(
     args.output_artifact,
     type=args.output_type,
     description=args.output_description,
    )
    
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help='input_artifact',
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help='output_artifact',
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help='output_type',
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help='output_description',
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help='min_price',
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help='max_price',
        required=True
    )


    args = parser.parse_args()

    go(args)
