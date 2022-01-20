import json

CONFIG_TEMPLATE = {
    "bridge_ip_address": "192.168.xxx.xxx",
    "light_names": ["Light 1", "Light 2"],
    "scan_frequency_seconds": 3,
}


def create_config(path: str) -> str:
    with open(path, "w+") as config_file:
        config_file.write(json.dumps(CONFIG_TEMPLATE, indent=2))
    return path


def load_config(path: str) -> dict:
    with open(path) as config_file:
        return json.load(config_file)
