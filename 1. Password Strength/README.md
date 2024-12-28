# Password Strength Checker

## Project Description
The **Password Strength Checker** is a simple program that evaluates the strength of a given password. It checks whether the password meets basic security requirements and provides feedback and suggestions for improvement.

---

## Features
- Checks the following criteria:
  - Minimum length of 8 characters.
  - Contains uppercase and lowercase letters.
  - Includes at least one number.
  - Includes at least one special character (e.g., `!@#$%^&*`).
- Suggests a strong password if the input password is weak.
- Simple to use and customizable.

---

## Technologies Used
- **Programming Language:** Python

> No additional libraries are required; the program uses basic Python functions and the `string` module.

---

## How It Works
1. The user inputs a password.
2. The program evaluates the password based on predefined security rules.
3. The program outputs the password's strength:
   - **Strong:** Meets all criteria.
   - **Moderate:** Partially meets the criteria.
   - **Weak:** Fails to meet most criteria.
4. If the password is weak, the program generates and suggests a stronger password.

---

## Usage
1. Clone or download the project files.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. Enter a password 
4. If the password is weak, use the suggested password.
---

## Example
**Input:**
```
Enter a password: 123456
```

**Output:**
```
Password strength: Weak
Suggestion: A$g7@Kd#9r2Q
```
---

## License
This project is open-source and available under the MIT License.

## Author:
> Created By: Harsh Gharsandiya
