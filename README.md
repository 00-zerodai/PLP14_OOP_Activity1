# PLP 14: Airline Ticket Booking System (OOP in Python)

This repository contains the solution for *Activity 1: Passenger booking a ticket* for Peer Learning Project (PLP) Group 14. 

The project is an interactive Command Line Interface (CLI) application built in Python that demonstrates core Object-Oriented Programming (OOP) concepts such as Inheritance, Polymorphism, and Encapsulation.

## 👥 Group Members & Roles

Our group actively collaborated to build this system. Below is the breakdown of our contributions:

*   *Bruno*: Driver - Project Setup & Base Passenger Class
*   *Sacha*: Driver - EconomyPassenger Child Class
*   *Janson*: Driver - BusinessPassenger Child Class (with luggage override)
*   *Steve*: Driver - FirstClassPassenger Child Class (with chauffeur logic)
*   *Frank*: Navigator - Input Validation & Error Handling Helpers
*   *Blaise*: Navigator & Presenter - Interactive CLI Workflow & Integration
*   Absent Members: None

## ✨ Features

*   *Inheritance*: Uses a base Passenger class to handle common attributes (name, route, date) shared by all ticket tiers.
*   *Polymorphism*: Child classes override the get_passenger_info() and get_weight_allowance() methods to provide tier-specific perks and baggage limits.
*   *Dynamic CLI*: Prompts the user only for details relevant to their selected ticket class.
*   *Error Handling*: Validates user inputs to prevent crashes from empty strings or invalid menu selections.

## 🚀 How to Run the Application

### Prerequisites
*   Python 3.x installed on your machine.

### Execution Steps
1. Clone this repository or download the source code file.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the following command:
   bash
   python PLP14_OOP_Activity1.py
   
5. Follow the on-screen prompts to book a ticket!

## 📁 Submission Deliverables

*   PLP14_OOP_Activity1.py: The complete, runnable Python source code.
*   PLP14_OOP_Activity1_Video.mp4: A 5-10 minute live walkthrough and code explanation (uploaded to Canvas).
*   *Proof of Collaboration*: Visible via our Git commit history (or attached Live Share screenshots on Canvas).
