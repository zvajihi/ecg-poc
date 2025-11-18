# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 15:38:28 2025

@author: zvaj2620
"""

from pathlib import Path
from ecg_poc.data_ingest.ingest_ecg import ingest_muse

def main():
    # Always resolve paths relative to the project root
    ROOT = Path(__file__).resolve().parents[1]
    config_path = ROOT / "configs" / "ingest_muse.yaml"
    
    manifest_path = ingest_muse(config_path)
    print(f"[main] Ingestion finished. Manifest saved at: {manifest_path}")


if __name__ == "__main__":
    main()
