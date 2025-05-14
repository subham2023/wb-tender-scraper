import pandas as pd
from datetime import datetime

class ExportTool:
    def __init__(self):
        self.output_dir = "data"

    def export_to_csv(self, data):
        df = pd.DataFrame(data)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{self.output_dir}/structured_tenders_{timestamp}.csv"
        df.to_csv(output_file, index=False)
        return output_file 