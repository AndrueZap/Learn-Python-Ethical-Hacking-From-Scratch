# Dette er fra leksjon 18

import subprocess
import optparse
from pip._vendor.distlib.compat import raw_input


# Mitt første objekt
parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Navnet på grensesnittet som skal forandre MAC adresse")
parser.parse_args()

interface = raw_input("interface >  ")
new_mac = raw_input("New MAC  >  ")

print(" [+] Forandrer MAC addressen for " +interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


˝