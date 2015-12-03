from snmp_client import SNMPClient
from flask import Flask, redirect, render_template, url_for

# Initiate Flask
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('cim_dashboard'))

# SNMP dashboard method
@app.route("/snmp")
def snmp_dashboard():
    snmp = SNMPClient()

    try:
        os_info = snmp.getOs()
    except:
        os_info = "Host not availible"
    
    try:
        ip_interfaces = snmp.getNetwork()
    except:
        ip_interfaces = [] 
    
    return render_template('snmp.html',
        os_info=os_info, ip_interfaces=ip_interfaces)#, url_for=url_for())

# Run the server
if __name__ == "__main__":
    app.run()