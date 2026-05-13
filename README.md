# Multilevel_Multiple_inheritance_task
This repository demonstrates the implementation of core Object-Oriented Programming (OOP) concepts in Python, specifically focusing on different types of Class Inheritance.

## 📌 Project Overview
The goal of this task is to model real-world relationships using Python classes to show how data and behaviors can be passed down or combined from multiple sources.

## 🧬 Key Concepts Implemented
1. Multilevel Inheritance :  In this pattern, a class is derived from a child class, creating a "grandparent-parent-child" relationship.

- Logic: Data flows through a linear chain.

- Use Case: Modeling levels of specialization (e.g., General User → Employee → Manager).

2. Multiple Inheritance : This occurs when a single class inherits features from more than one base class.

- Logic: A child class combines attributes and methods from multiple independent parents.

- Use Case: Combining different skill sets or categories into one entity (e.g., a "Smartphone" inheriting from both "Camera" and "Phone" classes).

## 🛠️ Features

- Method Resolution Order (MRO): Demonstrates how Python determines which class to use when multiple parents have methods with the same name.

- Super() Function: Proper use of super().__init__() to ensure all parent classes are initialized correctly.

- Business Logic: Implementation of specific methods (like premium calculations or status updates) based on inherited attributes.

## 🚀 How to Run
Clone the repository with Bash:

`git glose https://github.com/Sayali-hatwar/Multilevel_Multiple_inheritance_task.git`

Navigate to the directory:

`cd Multilevel_Multiple_inheritance_task`

Run the script:

`python main.py`

📂 File Structure

main.py: Contains the primary implementation of the inheritance models.

README.md: Project documentation and overview.
