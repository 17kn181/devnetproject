from netmiko import ConnectHandler

# Paramètres de connexion
cisco1 = {
    "device_type": "cisco_nxos",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
}

# Connexion au routeur
try:
    net_connect = ConnectHandler(**cisco1)
    print("Connexion réussie !")

    # Afficher le nom du routeur, sa version du OS et le modèle du routeur
    output = net_connect.send_command("show version")
    print(output)

    # Afficher la liste des interfaces Up
    output = net_connect.send_command("show ip interface brief | include up")
    print(output)

    # Afficher la liste des interfaces Down
    output = net_connect.send_command("show ip interface brief | include down")
    print(output)

    # Compter le nombre d'interfaces Fast Ethernet et Gigabit Ethernet
    output = net_connect.send_command("show ip interface brief | include FastEthernet|GigabitEthernet")
    interfaces = output.splitlines()
    fast_eth_count = sum("FastEthernet" in intf for intf in interfaces)
    gig_eth_count = sum("GigabitEthernet" in intf for intf in interfaces)
    print(f"Nombre d'interfaces Fast Ethernet : {fast_eth_count}")
    print(f"Nombre d'interfaces Gigabit Ethernet : {gig_eth_count}")

    # Afficher la liste des réseaux accessibles via le routeur
    output = net_connect.send_command("show ip route")
    print(output)

    # Déconnexion
    net_connect.disconnect()

except Exception as e:
    print(f"Erreur lors de la connexion : {str(e)}")
