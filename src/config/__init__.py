import json
from pathlib import Path


CONFIG_OPTS = {
    "applicationId": str,
    "appName": str,
    "authUrl": str,
    "cardFileDirectory": str,
    "cardSchemaVersion": str,
    "channelIds": list,
    "clientId": str,
    "clientSecretId": str,
    "clientSecretValue": str,
    "debug": bool,
    "graphUrl": str,
    "host": str,
    "logLevel": str,
    "logFile": str,
    "logFormat": str,
    "logDatefmt": str,
    "objectId": str,
    "port": int,
    "redirectUri": str,
    "scopes": str,
    "serviceAccount": str,
    "state": str,
    "tenantId": str,
    "tokenUrl": str
}

CURRENT_SESSIONS = {
    "cards": dict
}


def _prepare_config():
    if not Path("config/config.json").exists():
        raise FileNotFoundError("Config file not found")

    with open("config/config.json", "r") as f:
        config = json.load(f)

        if isinstance(config, dict):
            for key, value in config.items():
                if key in CONFIG_OPTS:
                    if key == "scopes":
                        CONFIG_OPTS['scopes'] = ','.join(value)

                    elif not isinstance(config[key], CONFIG_OPTS[key]):
                        raise TypeError(f"Config key {key} must be of type {CONFIG_OPTS[key]}")
                    
                    else:
                        CONFIG_OPTS[key] = value
        else:
            raise TypeError("Config must be a dict")

