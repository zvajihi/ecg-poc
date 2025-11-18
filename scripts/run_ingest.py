# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 15:38:28 2025

@author: zvaj2620
"""

from pathlib import Path

from ecg_poc.data_ingest.ingest_ecg import ingest_muse


def main():
    # Default config path; can later be overridden by CLI args
    config_path = Path("configs/ingest_muse.yaml")
    manifest_path = ingest_muse(config_path)
    print(f"[main] Ingestion finished. Manifest saved at: {manifest_path}")


if __name__ == "__main__":
    main()
