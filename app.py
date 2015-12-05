from flask import Flask, redirect, render_template, url_for

# Initiate Flask
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('test'))

# SNMP dashboard method
@app.route("/test")
def snmp_dashboard():
    return render_template('test.html') # os_info=os_info, ip_interfaces=ip_interfaces)#, url_for=url_for())

# Run the server
if __name__ == "__main__":
    app.run()