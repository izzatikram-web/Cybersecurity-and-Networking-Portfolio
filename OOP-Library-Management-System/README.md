# OOP Term Project — Library Management System

**Course:** Object-Oriented Programming  
**Contributors:** Izzat Ikram, Ayman Sohail, Gehad Mohamed  
**Date:** Summer 2025  

---

###  Overview
The **Library Management System** is a Python-based program that helps manage library books — borrowing, returning, tracking availability, and calculating overdue penalties.  
It demonstrates **core OOP principles** such as inheritance, encapsulation, and modular design.  

Users can:
- View available books  
- Borrow or return books  
- See borrowed books and overdue fines  
Librarians can:
- Add or remove books from the system  

---

###  Class Structure
| Class | Description |
|:--|:--|
| **UserAccount** | Manages user data and borrowed books. |
| **Librarian** | Inherits from `UserAccount`; adds/removes books. |
| **ManageBookLending** | Handles CSV file storage, lending, and availability. |
| **ReturnsAndOverduePenalties** | Calculates overdue fines and records returns. |

 *See the UML diagram (`UML_Diagram.pdf`) for class relationships.*

---

###  How to Run
1. Requires **Python 3.6+**  
2. No external libraries needed — uses built-in modules `csv`, `os`, and `datetime`  
3. Run from a terminal:  
   ```bash
   python OOP_Term_Project.py
