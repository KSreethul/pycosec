# 🚀 pycosec – Python Library for COSEC Biometric Devices

[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-LGPL--3.0-green)](https://www.gnu.org/licenses/lgpl-3.0.html)
![PyPI Downloads](https://img.shields.io/pypi/dm/pycosec)
![GitHub stars](https://img.shields.io/github/stars/KSreethul/pycosec)

Stop dealing with raw XML and complex COSEC APIs.

**pycosec** is a simple, production-ready Python library that lets you integrate COSEC biometric devices in minutes — not hours.

✔ No manual API calls
✔ No XML parsing
✔ Clean Python interface
✔ Works out of the box

Perfect for **HRMS systems, attendance tracking, and biometric integrations**.

---

## ⚡ Quick Start (2 Minutes)

```python
from pycosec import COSECBiometric

device = COSECBiometric(
    machine_ip="192.168.1.100",
    port=80,
    username="admin",
    password="password"
)

# Fetch attendance logs
events = device.get_attendance_events(no_of_events=10)
print(events)
```

That’s it. No complex setup.

---

## 📦 Installation

Install from PyPI:

```bash
pip install pycosec
```

Or install locally:

```bash
git clone https://github.com/KSreethul/pycosec.git
cd pycosec
pip install .
```

---

## ❓ Why pycosec?

Working directly with COSEC APIs is painful:

* XML responses are hard to parse
* API parameters are not intuitive
* Authentication handling is repetitive
* Every project ends up rewriting the same code

**pycosec solves this by:**

* 🔄 Converting XML → Python dictionaries
* 🔐 Handling authentication automatically
* ⚙️ Providing simple, readable methods
* ✅ Validating arguments before sending requests

So you can focus on building your application—not debugging device APIs.

---

## ✨ Features

* 👤 User Management (Add / Update / Delete users)
* 📊 Attendance Fetching (Punch logs, events)
* ⚙️ Device Configuration (Time, access control, alarms)
* 🔐 Credential Management (Fingerprint, card, face, palm)
* ⚡ Automatic XML Parsing → Python dict
* ✅ Argument validation before API calls
* 🔌 Works with COSEC HTTP API (Basic Auth)

---

## 🛠 Real-World Usage

This library is used in production systems to:

* Sync biometric attendance with HRMS
* Manage employee data on devices
* Handle large volumes of attendance logs efficiently

Tested with real COSEC devices in live environments.

---

## 🔌 Common Use Cases

* HRMS / Employee Management Systems
* Attendance Tracking Systems
* Access Control Automation
* Biometric Data Sync Services

---

## 📄 Example Usage

### Get total users

```python
user_count = device.get_user_count()
print(user_count)
```

### Add / Update user

```python
device.set_cosec_user(
    user_id="1001",
    ref_user_id=1,
    name="John Doe",
    user_active=True,
    card1="1234567890",
    enable_fr=True
)
```

### Get attendance events

```python
events = device.get_attendance_events(no_of_events=50)
print(events)
```

---

## 📄 Example Response

```json
{
  "user-id": "1001",
  "event-id": "101",
  "date": "2026-04-21",
  "time": "09:12:33",
  "message": "Successful"
}
```

---

## 📚 API Coverage

### Device Configuration

* `basic_config()`
* `finger_reader_parameter_configuration()`
* `enrollment_configuration()`
* `access_settings_configuration()`
* `alarm_configuration()`
* `date_and_time_configuration()`
* `door_features_configuration()`
* `system_timer_configuration()`
* `special_function_configuration()`
* `wiegand_interface()`
* `smart_card_format()`

### User Management

* `get_cosec_user()`
* `set_cosec_user()`
* `delete_cosec_user()`
* `enable_user_face_recognition()`
* `get_user_credential()`
* `get_user_credential_count()`
* `delete_cosec_user_credential()`

### Attendance

* `get_attendance_events()`

---

## 🚧 Roadmap

* [ ] Async support
* [ ] More API endpoint wrappers
* [ ] Webhook/event-based sync
* [ ] Improved error handling

---

## 🤝 Contributing

Contributions are welcome!

You can help with:

* Adding new API endpoints
* Improving documentation
* Writing examples

### Steps:

1. Fork the repository
2. Create a branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push: `git push origin feature-name`
5. Open a Pull Request

Check issues labeled **good first issue** to get started.

---

## 📄 License

This project is licensed under the **LGPL-3.0 License**
👉 [https://www.gnu.org/licenses/lgpl-3.0.html](https://www.gnu.org/licenses/lgpl-3.0.html)

---

## 🔗 Links

* GitHub: [https://github.com/KSreethul/pycosec](https://github.com/KSreethul/pycosec)
* Issues: [https://github.com/KSreethul/pycosec/issues](https://github.com/KSreethul/pycosec/issues)
* PyPI: [https://pypi.org/project/pycosec/](https://pypi.org/project/pycosec/)

---

## ⭐ Support

If this project helped you:

* ⭐ Star the repo
* 🐛 Report issues
* 🔁 Share with others

---

# 🎯 Final Note

This library was built to solve real-world biometric integration problems.

If you're working with COSEC devices, **pycosec will save you hours of work**.
