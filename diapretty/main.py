import tempfile
import webbrowser

import click

from diapretty.html import PrettyDiagnosis


@click.command()
@click.argument("diagnose_path")
def main(diagnose_path):
    diagnosis = PrettyDiagnosis.from_diagnose_file(diagnose_path)

    name: str
    with tempfile.NamedTemporaryFile(prefix="diagnosis_", suffix=".html", delete=False) as f:
        f.write(bytes(diagnosis.full_html, "utf-8"))
        f.close()
        name = f.name

    webbrowser.open_new_tab(name)


if __name__ == "__main__":
    main()
