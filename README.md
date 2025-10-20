# pycosec

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-LGPL--2.1+-green)](https://www.gnu.org/licenses/lgpl-2.1.html)  

**pycosec** is a Python library that provides an easy interface to interact with COSEC biometric devices. It allows you to manage users, configure device settings, retrieve attendance events, and handle credentials programmatically.

---

## Features

- Configure device settings such as IP, time, and access control.
- Manage users (add, update, delete).
- Enable/disable face recognition and other special features.
- Retrieve attendance events (punch-in/punch-out).
- Manage user credentials (fingerprint, card, palm, face templates/images).
- Support for alarms, door features, and system timers.
- Works with COSEC API using HTTP Basic authentication.

---

## Installation

Install via pip:

```
pip install pycosec
````

Or clone the repository and install locally:

```bash
git clone https://github.com/KSreethul/pycosec.git
cd pycosec
pip install .
```

---

## Requirements

* Python 3.10+
* `requests` library (>=2.0)

---

## Usage

```python
from pycosec import COSECBiometric

# Initialize device connection
device = COSECBiometric(
    machine_ip="192.168.1.100",
    port=80,
    username="admin",
    password="password"
)

# Retrieve total number of users
user_count = device.get_user_count()
print("Total Users:", user_count)

# Add or update a user
response = device.set_cosec_user(
    user_id="1001",
    ref_user_id=1,
    name="John Doe",
    user_active=True,
    card1="1234567890",
    enable_fr=True
)
print(response)

# Retrieve attendance events
events = device.get_attendance_events(no_of_events=50)
print(events)
```

---

## Documentation

The library provides methods to configure and interact with:

* **Device Settings**

  * `basic_config()`, `finger_reader_parameter_configuration()`, `enrollment_configuration()`, `access_settings_configuration()`, `alarm_configuration()`, `date_and_time_configuration()`, `door_features_configuration()`, `system_timer_configuration()`, `special_function_configuration()`, `wiegand_interface()`, `smart_card_format()`
* **User Management**

  * `get_cosec_user()`, `set_cosec_user()`, `delete_cosec_user()`, `enable_user_face_recognition()`, `get_user_credential()`, `get_user_credential_count()`, `delete_cosec_user_credential()`
* **Attendance**

  * `get_attendance_events()`

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m "Add feature"`.
4. Push to your branch: `git push origin feature-name`.
5. Create a Pull Request.

---

## License

This project is licensed under the **LGPL 3.0** license. See [[LICENSE](https://www.gnu.org/licenses/lgpl-3.0.html)](https://www.gnu.org/licenses/lgpl-3.0.html) for details.

---

## Links

* **Homepage:** [https://github.com/KSreethul/pycosec](https://github.com/KSreethul/pycosec)
* **Bug Tracker:** [https://github.com/KSreethul/pycosec/issues](https://github.com/KSreethul/pycosec/issues)