import csv
import os


class CSVReader:

    @staticmethod
    def read_data():

        file_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            "test_data.csv"
        )

        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            return list(reader)