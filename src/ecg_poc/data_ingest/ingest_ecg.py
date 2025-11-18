# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:34:43 2025

@author: zvaj2620
"""

from pathlib import Path

import pandas as pd
import yaml

from ecg_poc.data_ingest.muse_loader import load_muse_directory


def load_config(config_path: str | Path) -> dict:
    config_path = Path(config_path)
    with config_path.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return cfg


def ingest_muse(config_path: str | Path) -> Path:
    """
    Main ingestion entry point for MUSE ECG data.
    - Reads config
    - Loads raw files
    - Writes an interim manifest
    Returns path to the manifest file.
    """
    cfg = load_config(config_path)

    raw_dir = Path(cfg["paths"]["raw_dir"])
    interim_dir = Path(cfg["paths"]["interim_dir"])
    interim_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = interim_dir / cfg["paths"]["manifest_name"]

    print(f"[ingest] Loading MUSE ECG files from: {raw_dir}")
    df = load_muse_directory(raw_dir)

    print(f"[ingest] Found {len(df)} ECG files.")
    print(f"[ingest] Saving manifest to: {manifest_path}")

    # Save as Parquet (preferred) or CSV
    if manifest_path.suffix == ".parquet":
        df.to_parquet(manifest_path, index=False)
    else:
        df.to_csv(manifest_path, index=False)

    return manifest_path
