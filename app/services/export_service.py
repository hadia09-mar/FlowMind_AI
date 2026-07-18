import pandas as pd


class ExportService:

    @staticmethod
    def export_csv(data, filename):

        df = pd.DataFrame(data)

        df.to_csv(filename, index=False)

        return filename