# C4-LU642D HDMI Matrix

Custom Home Assistant integration for the Control4 C4-LU642D HDMI matrix switch.

## Author

Created by **timcloud**

## Features

- Control 6x6 HDMI input/output routes
- Switch-friendly labels like `Input 1 → Output 2`
- Configurable via UI (no YAML needed)
- Entities are grouped under one device

## Installation

1. Copy the `c4_lu642d/` folder into `config/custom_components/` in your Home Assistant configuration directory.

2. Restart Home Assistant.

3. Go to **Settings > Devices & Services > Add Integration** and search for **C4-LU642D HDMI Matrix**.

4. Enter your matrix's IP address and login credentials.

5. You will now see all `Input → Output` switches under a single device.

## Example Use

Use `switch.input1_output3` in automations, scenes, or dashboards.

## Notes

- Only one input can be routed to each output at a time
- Turning on a switch will auto-route input to output
- Turning off a switch disables that output

## License

MIT
