import datetime
import gzip
import json
from typing import Dict

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader("diapretty", "templates"), autoescape=True)
full = env.get_template("template.html.jinja2")


class PrettyDiagnosis:
    diagnosis: Dict[str, object]

    def __init__(self, diagnosis_path: str):
        if diagnosis_path.endswith(".gz"):
            with gzip.open(diagnosis_path) as f:
                self.diagnosis = json.load(f)
        elif diagnosis_path.endswith(".json"):
            with open(diagnosis_path) as f:
                self.diagnosis = json.load(f)

    @property
    def full_html(self):
        return full.render(
            diagnosis=self.diagnosis,
            creation_date=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        )
