import requests
from werkzeug import Response, Request

from diapretty.html import PrettyDiagnosis


class DiagnoseServer:
    diagnose_host: str = "http://localhost:4566"
    diagnose_endpoint: str = "/_localstack/diagnose"

    def __init__(self):
        self.wsgi = Request.application(self.serve)

    def serve(self, request: Request) -> Response:
        diagnose_response = requests.get(self.diagnose_host + self.diagnose_endpoint)

        doc = diagnose_response.json()

        return Response(PrettyDiagnosis(doc).full_html, mimetype="text/html")
