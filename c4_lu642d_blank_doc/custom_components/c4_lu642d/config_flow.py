from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Control4 C4-LU642D", data=user_input)

        data_schema = vol.Schema({
            vol.Required("host"): str,
            vol.Optional("username", default="admin"): str,
            vol.Optional("password", default="admin"): str,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)
