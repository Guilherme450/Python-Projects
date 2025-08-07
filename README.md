# Python Implementations of Data Structures, Algorithms, and Electronics Analysis

This repository contains a collection of Python scripts that implement various data structures, algorithms, and perform analysis on electronic components. Each script is a standalone project with a specific focus.

## Data Structures

This section covers classic data structures implemented in Python.

### Linked Lists

*   **`LinkedListStudy.py`**: A simple implementation of a singly linked list with basic operations like `push`, `pop`, `search`, and `show`.
*   **`linked_list_implementation.py`**: A more practical application of a linked list that simulates a user database, where each node stores a user's name and cash. It includes a command-line interface to interact with the data.

### Queue

*   **`Queue_implementation/`**: This directory contains a project that simulates an order processing system using a queue data structure.
    *   `queue_structure.py`: Defines the queue implementation using a linked list.
    *   `queue_project.py`: Uses the queue to manage and process a series of orders in a FIFO (First-In, First-Out) manner.

### Stack

*   **`stack_data_structure.py`**: A basic implementation of a stack (LIFO - Last-In, First-Out) using a linked list.
*   **`stack_implementation.py`**: A practical example of a stack used to manage a music playlist.

### Usage
To run the scripts:
```bash
python LinkedListStudy.py
python linked_list_implementation.py
python Queue_implementation/queue_project.py
python stack_data_structure.py
python stack_implementation.py
```

## Algorithms

### Rational Root Theorem

*   **`RationalRootsAlgorithm.py`**: This script implements the Rational Root Theorem to find the possible rational roots of a polynomial. It then uses the Briot-Ruffini method (synthetic division) to test these possible roots.

    **Usage:**
    ```bash
    python RationalRootsAlgorithm.py
    ```
    The script will prompt you to enter the number of coefficients in your polynomial and then the coefficients themselves.

## Electronics Analysis

This section contains scripts for analyzing electronic components.

### NTC Thermistor Analysis

*   **`NTC_Resistor_Program.py`**: This script calculates and plots the resistance of an NTC (Negative Temperature Coefficient) thermistor as a function of temperature.

### Capacitor Analysis

*   **`capacitors_analysis.py`**: This script analyzes the charging and discharging of a capacitor in an RC circuit. It plots the voltage and current over time for both charging and discharging phases.

### Dependencies

To run the electronics analysis scripts, you need to install the following Python libraries:

*   `numpy`
*   `matplotlib`
*   `seaborn`
*   `scipy`
*   `pandas`

You can install them using pip:
```bash
pip install numpy matplotlib seaborn scipy pandas
```

### Usage
To run the scripts:
```bash
python NTC_Resistor_Program.py
python capacitors_analysis.py
```
