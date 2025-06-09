
import logging
import requests
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = entry.data
    host = data.get("host")
    username = data.get("username", "admin")
    password = data.get("password", "admin")

    switches = []

    for input_ in range(1, 7):
        for output in range(1, 7):
            name = f"Input {input_} → Output {output}"
            switches.append(Control4HDMISwitch(name, input_, output, host, username, password))

    async_add_entities(switches)

class Control4HDMISwitch(SwitchEntity):
    def __init__(self, name, input_num, output_num, host, username, password):
        self._name = name
        self.input = input_num
        self.output = output_num
        self.host = host
        self.username = username
        self.password = password
        self._is_on = False
        self._attr_unique_id = f"control4_input{input_num}_output{output_num}"
        self._attr_entity_id = f"switch.control4_input{input_num}_output{output_num}"

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    @property
    def unique_id(self):
        return self._attr_unique_id

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, "c4_lu642d")},
            "name": "Control4 C4-LU642D HDMI Matrix",
            "manufacturer": "Control4",
            "model": "C4-LU642D"
        }

    def turn_on(self, **kwargs):
        self._send_command(f"LEAF[48,{self.input:02},{self.output - 1:02}]")
        self._is_on = True

    def turn_off(self, **kwargs):
        self._send_command(f"LEAF[47,00,{self.output - 1:02}]")
        self._is_on = False

    def _send_command(self, query):
        try:
            url = f"http://{self.host}/cgi-bin/CGI_MAIN.cgi"
            response = requests.post(
                url,
                data={"query": query},
                auth=(self.username, self.password),
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=5,
            )
            response.raise_for_status()
            _LOGGER.info("Command sent: %s", query)
        except Exception as e:
            _LOGGER.error("Failed to send command to %s: %s", self.host, e)
