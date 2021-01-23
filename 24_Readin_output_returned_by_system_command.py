#!/usr/bin/python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",help="Navnet på grensesnittet som skal forandre MAC adresse")
    parser.add_option("-m", "--mac", dest="new_mac",help="Skriv in den nye MAC adressen")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Spesifiser et grensesnitt, bruk --help for mer info")
    elif not options.new_mac
        parser.error("[-] Spesifiser en my MAC adresse, bruk --help for mer info")
    return options

def change_mac (interface, new_mac):
    print("[+] Forandrer MAC adresse til " +interface+ " til " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
# change_mac(options.interface, options.new_mac)