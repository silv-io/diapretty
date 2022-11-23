FULL = """<!DOCTYPE html>
<link rel="stylesheet" href="https://fonts.xz.style/serve/inter.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@exampledev/new.css@1.1.2/new.min.css">
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="max-width: 1200px">
<header>
    <h1>LocalStack Diagnosis - {{ creation_date }}</h1>
</header>
<h2>Version</h2>
<table>
    {% for section, table_data in diagnosis["version"].items() %}
        <tr>
            <td>{{ section }}</td>
            <td>
                <table>
                    {% for key, value in table_data.items() %}
                        <tr>
                            <td> {{ key }}</td>
                            <td> {{ value }}</td>
                        </tr>
                    {% endfor %}
                </table>
            </td>
        </tr>
    {% endfor %}
</table>
<h2>Common environment configurations</h2>
<h3>HostConfig.Binds</h3>
<table>
    {% for bind in diagnosis["docker-inspect"]["HostConfig"]["Binds"] %}
        <tr>
            <td>{{ bind }}</td>
        </tr>
    {% endfor %}
</table>
<h3>PortBindings</h3>
{% if "PortBindings" in diagnosis["docker-inspect"] %}
    <table>
        <tr>
            <th>Container</th>
            <th>Host</th>
        </tr>
        {% for client, host in diagnosis["docker-inspect"]["PortBindings"].items() %}
            <tr>
                <td>{{ client }}</td>
                <td>{{ host["HostIp"] }}:{{ host["HostPort"] }}</td>
            </tr>
        {% endfor %}
    </table>
{% else %}
    <b>NONE</b>
{% endif %}
<h3>Config.Env</h3>
<table>
    {% for env in diagnosis["docker-inspect"]["Config"]["Env"] %}
        {% set split = env.split("=") %}
        <tr>
            <td>{{ split[0] }}</td>
            <td>{{ split[1] }}</td>
        </tr>
    {% endfor %}
</table>
<h3>NetworkSettings.Networks</h3>
{% for network_key, network_data in diagnosis["docker-inspect"]["NetworkSettings"]["Networks"].items() %}
    <h4>{{ network_key }}</h4>
    <table>
        {% for key, value in network_data.items() %}
            <tr>
                <td>{{ key }}</td>
                <td>{{ value }}</td>
            </tr>
        {% endfor %}
    </table>
{% endfor %}
<h2>Advanced configuration</h2>
<details>
    <summary>Running services</summary>
    <table>
        {% for service, available in diagnosis["services"].items() %}
            <tr>
                <td>{{ service }}</td>
                <td>{{ available }}</td>
            </tr>
        {% endfor %}
    </table>
</details>
<details>
    <summary>Config</summary>
    <table>
        {% for key, value in diagnosis["config"].items() %}
            <tr>
                <td style="min-width: 250px">{{ key }}</td>
                <td>
                    {% if value is mapping %}
                        <table>
                            {% for inner_key, inner_value in value.items() %}
                                <tr>
                                    <td>{{ inner_key }}</td>
                                    <td>{{ inner_value }}</td>
                                </tr>
                            {% endfor %}
                        </table>
                    {% else %}
                        {{ value }}
                    {% endif %}
                </td>
            </tr>
        {% endfor %}
    </table>
</details>

</body>
</html>
"""