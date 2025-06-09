 Home Assistant Control4 C4-LU642D HDMI Matrix Integration
A custom Home Assistant integration for the Control4 C4-LU642D 6x6 HDMI Matrix Switch.

✨ Features
Seamless routing for up to 36 input/output combinations (6 inputs × 6 outputs)

Auto-creation of switch entities for each route

Clean, friendly entity names (e.g., switch.control4_input1_output4)

All routes grouped under one device for easy dashboard management

Full configuration via the Home Assistant UI

📦 Installation
Copy files to: config/custom_components/c4_lu642d/

Restart Home Assistant

Add via Settings > Devices & Services > Add Integration

Select “C4-LU642D HDMI Matrix”, enter IP & credentials

All switch entities will be automatically created

🧠 Usage Tips
Each entity maps one input to one output

Turning off a switch disables the output

Outputs support only one input at a time

Perfect for automations, scripts, and dashboards
🧪 Example
Input 3 → Output 2
Entity: switch.control4_input3_output2

Automation Example:

yaml
Copy
Edit
alias: Watch Xbox in Living Room
trigger:
  platform: state
  entity_id: input_boolean.xbox_mode
  to: "on"
action:
  service: switch.turn_on
  target:
    entity_id: switch.control4_input2_output1
🛠️ Configuration
No YAML required

Fully UI-managed (stored in .storage)

👨‍💻 Created by
timcloud

📄 License
MIT License
