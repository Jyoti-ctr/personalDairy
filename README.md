## Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Jyoti-ctr/personalDairy.git
    cd personalDairy
    ```

2.  **Install Dependencies:**
    Make sure you have Python installed, then run:
    ```bash
    pip install flask
    ```

3.  **Run the Application:**
    ```bash
    python app.py
    ```

4.  **Access the App:**
    Open your browser and navigate to `http://127.0.0.1:5000`

---

## 📊 Database Schema (SQL)

The project uses a single table named `journal` to manage the diary entries:

| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Primary Key (Auto-increment) |
| `date` | TEXT | Unique date for the entry (YYYY-MM-DD) |
| `title` | TEXT | The headline of your diary entry |
| `content` | TEXT | The full body text of your thoughts |

---

## 👤 Author

**Jyoti Sharma**  
*Computer Science Engineering Student*  
[GitHub Profile](https://github.com/Jyoti-ctr)

---

# 📔 Personal Diary Web Application

A sleek, private digital journal that allows users to record their daily thoughts and experiences. This project features a dynamic **Calendar View** and uses a **SQL database** to ensure all entries are stored securely and persistently.

---

## Features

*   **Interactive Calendar:** View and manage your entries through a clean, monthly calendar interface.
*   **Persistent Storage:** All journal entries are saved in a SQLite database, ensuring data isn't lost when the server restarts.
*   **CRUD Functionality:** Create, Read, and Update your daily notes by simply clicking on a date.
*   **Responsive UI:** A modern, user-friendly interface built with CSS and JavaScript.

---

## Tech Stack

*   **Backend:** Python (Flask Framework)
*   **Database:** SQLite (SQL)
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Libraries:** FullCalendar API

---

## 📂 Project Structure
```text
personal_diary/
│
├── app.py              # Flask Backend & SQL API logic
├── database.db         # SQLite database file (auto-generated)
└── templates/
    └── index.html      # Frontend Calendar interface
