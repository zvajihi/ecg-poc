# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 14:34:43 2025

@author: zvaj2620
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List

import pandas as pd


@dataclass
class ECGRecord:
    """Internal representation of one ECG recording (metadata-level)."""
    ecg_id: str
    file_path: Path
    patient_id: str | None = None
    visit_id: str | None = None
    recording_time: str | None = None  # you can later use datetime


def find_muse_files(raw_dir: Path, extension: str = ".xml") -> List[Path]:
    """
    Find all MUSE ECG files under raw_dir with given extension.
    For now we assume XML; you can adjust later.
    """
    return sorted(raw_dir.rglob(f"*{extension}"))


def load_muse_directory(raw_dir: Path) -> pd.DataFrame:
    """
    Scan a directory of MUSE ECG files and return a DataFrame
    with basic metadata. Parsing of ECG signals will come later.
    """
    raw_dir = Path(raw_dir)
    files = find_muse_files(raw_dir)

    records: list[ECGRecord] = []

    for f in files:
        ecg_id = f.stem  # filename without extension

        # TODO: Later parse patient_id, visit_id, time from XML content.
        record = ECGRecord(
            ecg_id=ecg_id,
            file_path=f,
            patient_id=None,
            visit_id=None,
            recording_time=None,
        )
        records.append(record)

    # Convert list of ECGRecord to DataFrame
    df = pd.DataFrame(
        [
            {
                "ecg_id": r.ecg_id,
                "file_path": str(r.file_path),
                "patient_id": r.patient_id,
                "visit_id": r.visit_id,
                "recording_time": r.recording_time,
            }
            for r in records
        ]
    )

    return df
