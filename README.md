# ✈ SkyBooker — Flight Booking System

> COMP2090 Group 108 Course Project

[![License: Anti 996](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![pywebview](https://img.shields.io/badge/GUI-pywebview-orange.svg)](https://pywebview.flowrl.com/)

**SkyBooker** is a modern desktop flight booking system built with Python and [pywebview](https://pywebview.flowrl.com/). It features a sleek single-page-application (SPA) style UI rendered inside a native window, with a full-featured backend for flight management, user authentication, and booking operations.

---

## ✨ Features

### For Passengers
- 🔍 **Search Flights** — Search by flight number, origin, or destination
- 🎫 **Book Flights** — One-click booking with real-time seat availability
- ❌ **Cancel Bookings** — Easily cancel existing reservations
- 👤 **Account Management** — Register and log in securely

### For Admins
- 📊 **Dashboard** — Overview of all flights and available seats
- ➕ **Add Flights** — Create new flight entries with full details
- ✏️ **Edit Flight Time** — Update departure time for existing flights
- 🗑️ **Remove Flights** — Delete flights from the system
- 👥 **View Passengers** — See the passenger list for any flight

### Security & Architecture
- 🔒 **Password Hashing** — Uses `bcrypt` via `passlib` for secure credential storage
- 🏗️ **OOP Design** — Abstract base class (`Person`) with `Passenger` and `Admin` subclasses demonstrating **inheritance**, **polymorphism**, and **encapsulation**
- 🎨 **Modern UI** — CSS-variable-driven responsive design with toast notifications, modals, and smooth animations

---

## 🏛️ Architecture

```
┌──────────────────────────────────────────────┐
│                  gui.py                       │
│  ┌────────────┐    ┌───────────────────────┐  │
│  │  Api class  │◄──│  HTML / CSS / JS SPA  │  │
│  │  (Bridge)   │──►│  (Embedded Frontend)  │  │
│  └─────┬──────┘    └───────────────────────┘  │
│        │           pywebview js_api bridge     │
├────────┼─────────────────────────────────────┤
│        ▼                                      │
│  ┌──────────────┐                             │
│  │ flight_system│  Core booking logic         │
│  │   System     │                             │
│  └──┬───┬───┬───┘                             │
│     │   │   │                                 │
│     ▼   ▼   ▼                                 │
│  flights.py  person.py  passenger.py admin.py │
│  (Flight)    (Person▲)  (Passenger)  (Admin)  │
│              ABC base    ▲ extends    ▲ extends│
└──────────────────────────────────────────────┘
```

| File | Description |
|------|-------------|
| `gui.py` | Application entry-point, API bridge, and embedded HTML/CSS/JS frontend |
| `flight_system.py` | Core `System` class — manages flights, users, and booking logic |
| `flights.py` | `Flight` data model with capacity and passenger management |
| `person.py` | Abstract `Person` base class with bcrypt password hashing |
| `passenger.py` | `Passenger` subclass — search, book, and cancel flights |
| `admin.py` | `Admin` subclass — level-based permissions for flight management |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10** or higher
- **pip** (Python package manager)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/justinfromhkg/2600_COMP2090_GRP108.git
cd 2600_COMP2090_GRP108
```

2. **Create a virtual environment** *(recommended)*

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python gui.py
```

A native window will open with the SkyBooker UI. Use the **demo account** to explore:

| Role | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |

Or register a new **Passenger** / **Admin** account from the login screen.

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| [pywebview](https://pywebview.flowrl.com/) | ≥ 5.0 | Native GUI window with embedded web content |
| [passlib](https://passlib.readthedocs.io/) | ≥ 1.7.4 | Password hashing utilities |
| [bcrypt](https://github.com/pyca/bcrypt) | ≥ 4.0.0, < 5.0.0 | Bcrypt hashing backend for passlib |

---

## 🧑‍💻 OOP Concepts Demonstrated

This project showcases key Object-Oriented Programming principles:

| Concept | Implementation |
|---------|---------------|
| **Abstraction** | `Person` is an abstract base class (`ABC`) with abstract methods `__str__` and `display_role` |
| **Encapsulation** | Private attributes (e.g. `self.__password`, `self._username`) with getter/setter methods |
| **Inheritance** | `Passenger` and `Admin` both inherit from `Person` |
| **Polymorphism** | `display_role()` returns different values depending on the subclass |

---

## 📁 Project Structure

```
2600_COMP2090_GRP108/
├── gui.py              # Main entry-point & embedded SPA frontend
├── flight_system.py    # Core system logic (flights, users, bookings)
├── flights.py          # Flight model
├── person.py           # Abstract Person base class
├── passenger.py        # Passenger subclass
├── admin.py            # Admin subclass
├── requirements.txt    # Python dependencies
├── LICENSE             # Anti-996 License
└── README.md           # This file
```

---

## 📄 License

This project is licensed under the [Anti-996 License](LICENSE).

[![Badge](https://img.shields.io/badge/link-996.ICU-%23FF4D5B.svg?style=flat-square)](https://996.icu/#/en_US)

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👥 Team

**COMP2090 — Group 108**

---

<p align="center">Made with LIAO Junming, XIE Jiayan and CHEN Jiawen by Group 108</p>
