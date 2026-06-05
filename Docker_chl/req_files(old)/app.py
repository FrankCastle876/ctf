from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Internal DNS Diagnostics</h2>

    <p>Lookup a hostname:</p>

    <form action="/lookup">
        <input name="host" placeholder="example.com">
        <input type="submit">
    </form>
    """

@app.route("/lookup")
def lookup():
    host = request.args.get("host", "")

    try:
        result = subprocess.check_output(
            f"nslookup {host}",
            shell=True,
            stderr=subprocess.STDOUT,
            timeout=5
        )

        return f"<pre>{result.decode()}</pre>"

    except subprocess.CalledProcessError as e:
        return f"<pre>{e.output.decode()}</pre>"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
