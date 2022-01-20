from urllib import request
import requests
from phue import Bridge


def load_bridge(ip_address=None):
    """
    Connect to a bridge given it's IP Address
    or try to find it on the network
    """
    if ip_address is None:
        try:
            bridges = requests.get("https://discovery.meethue.com/").json()
            ip_address = bridges[0]["internalipaddress"]
        except Exception:
            raise Exception("No Bridge Found")

    try:
        bridge = Bridge(ip_address)
    except Exception as error:
        print(error)
    return bridge


def turn_on(bridge: Bridge, light_names: list[str]):
    """turn on all of the named lights"""
    # TODO: Error handling for missing light
    lights = bridge.get_light_objects("name")
    for light in light_names:
        lights[light].on = True


def turn_off(bridge: Bridge, light_names: list[str]):
    """turn off all of the named lights"""
    # TODO: Error handling for missing light
    lights = bridge.get_light_objects("name")
    for light in light_names:
        lights[light].on = False
