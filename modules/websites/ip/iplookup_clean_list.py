#ip lookup using python and ipwhois
from ipwhois import IPWhois as whois
import json

options_results = []
network_results = []
network_remarks_results = []
basic_result = []
network_result = []

def get_info(address):# get info about an ip address and return it
    
    # print("="*27,"\nBASIC INFO:\n"+"="*27+"\n")
    firstscan = whois(address)
    result = firstscan.lookup_rdap()

    for _, element in enumerate(result):
        options_results.append(element)

    for option in options_results:
        if option == 'network' or option == 'entities' or option == 'objects':
            continue
        e1 = (
            option+": ",
            result[str(option)] 
        )
        basic_result.append(e1)
##########################################################       !!!NOTE FOR EVERYONE!!!
#FOR EVERYONE, comment this print, if in main.py doesnt need.
    for tupla in basic_result:
        key, value = tupla
        # print(
        #     key,
        #     ": ",
        #     value
        # )
########################################################## 

    network_info = result.get('network')
    # print("\n"+"="*27,"\nNETWORK INFO:\n"+"="*27+"\n") 
    for _, value in enumerate(network_info):
        network_results.append(value)

    for element in network_results:
        if element == 'links' or element == 'notices' or element == 'events' or element == 'remarks':
            continue
        e2 = (
            element+": ",
            network_info[element]
        )

############################################################        !!!NOTE FOR EVERYONE!!!
##FOR EVERYONE, comment this print, if in main.py doesnt need.
        network_result.append(e2)
    for tupla in network_result:
        key, value = tupla
        # print(
        #     key,
        #     ": ",
        #     value
            
        # )
######################################################
    
    print("="*27+"\n")
    return basic_result, network_result 

def ip_whois(ip_address): ##START FUNCTION

    basicinfo, networkinfo = get_info(ip_address)
    data_info, data_info_network = json.dumps(basicinfo), json.dumps(networkinfo) 

    data_result = data_info.replace("[", "").replace("]", '\n').replace(",", "").replace('"', "")
    network_result = data_info_network.replace("[", "").replace("]", '\n').replace(",", "").replace('"', "")

    return data_result, network_result #the first is basic infos about the ip address, the second, the network infos about it.

#cleaned_list = [re.sub(r'[,"\\:\[\]]', '', item) for item in b]
