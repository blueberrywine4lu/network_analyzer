import subprocess
import datetime
import os

ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def esegui(comando):
    risultato = subprocess.run(comando, capture_output=True, text=True)
    return risultato.stdout.strip()

ip_privato = esegui(["ip","addr","show"])
gateway = esegui(["ip","route","show"])
porte = esegui(["ss","-tuln"])
dns = esegui(["dig","+short","google.com"])

report = f"""
=== NETWORK ANALYZER ===
Generato il: {ora}

--- IP E INTERFACCE ---
{ip_privato}

--- GATEWAY ---
{gateway}

--- PORTE APERTE ---
{porte}

--- DNS GOOGLE ---
{dns}
"""

print (report)

with open("network_report.txt","w") as f:
    f.write(report)

print ("Report salvato in Network_report.txt")
