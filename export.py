"""
export.py
Export utilities for SignalDecoder
"""

import json
import csv
from pathlib import Path

import pandas as pd


class Exporter:
    """
    Export analysis results in different formats.
    """

    @staticmethod
    def export_json(data, filename):
        filename = Path(filename)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        return filename

    @staticmethod
    def export_csv(data, filename):
        filename = Path(filename)

        if isinstance(data, pd.DataFrame):
            data.to_csv(filename, index=False)
            return filename

        if isinstance(data, list):
            if len(data) == 0:
                return filename

            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)

                if isinstance(data[0], dict):
                    writer.writerow(data[0].keys())

                    for row in data:
                        writer.writerow(row.values())
                else:
                    for row in data:
                        if isinstance(row, (list, tuple)):
                            writer.writerow(row)
                        else:
                            writer.writerow([row])

        elif isinstance(data, dict):
            pd.DataFrame([data]).to_csv(filename, index=False)

        return filename

    @staticmethod
    def export_txt(data, filename):
        filename = Path(filename)

        with open(filename, "w", encoding="utf-8") as f:
            if isinstance(data, dict):
                for key, value in data.items():
                    f.write(f"{key}: {value}\n")

            elif isinstance(data, list):
                for item in data:
                    f.write(f"{item}\n")

            else:
                f.write(str(data))

        return filename

    @staticmethod
    def export_all(data, basename="result"):
        """
        Export data to JSON, CSV and TXT simultaneously.
        """

        Exporter.export_json(data, f"{basename}.json")
        Exporter.export_csv(data, f"{basename}.csv")
        Exporter.export_txt(data, f"{basename}.txt")

        print("Export completed.")


if __name__ == "__main__":

    sample = {
        "frames": 12,
        "errors": 0,
        "snr": 18.7,
        "decoded": "HELLO"
    }

    Exporter.export_all(sample)
