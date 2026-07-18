from app.services.database import db
import hashlib


# -------------------------
# Users Table
# -------------------------

def create_user_table():

    db.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT

    )
    """)


# -------------------------
# Documents Table
# -------------------------

def create_documents_table():

    db.execute("""
    CREATE TABLE IF NOT EXISTS documents(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        filename TEXT,

        uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


# -------------------------
# HR Reports Table
# -------------------------

def create_hr_table():

    db.execute("""
    CREATE TABLE IF NOT EXISTS hr_reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        candidate_name TEXT,

        ats_score INTEGER,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


# -------------------------
# Research Reports Table
# -------------------------

def create_research_table():

    db.execute("""
    CREATE TABLE IF NOT EXISTS research_reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        topic TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


# -------------------------
# Activity Logs
# -------------------------

def create_activity_table():

    db.execute("""
    CREATE TABLE IF NOT EXISTS activity_logs(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        module TEXT,

        activity TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)


# -------------------------
# Password Hash
# -------------------------

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# -------------------------
# Register User
# -------------------------

def register_user(username, password):

    username = username.strip().lower()

    try:

        db.execute(

            "INSERT INTO users(username,password) VALUES(?,?)",

            (

                username,

                hash_password(password)

            )

        )

        return True

    except:

        return False


# -------------------------
# Login User
# -------------------------

def login_user(username, password):

    username = username.strip().lower()

    db.execute(

        "SELECT * FROM users WHERE username=? AND password=?",

        (

            username,

            hash_password(password)

        )

    )

    return db.fetchone()


# -------------------------
# Automation Table
# -------------------------

def create_automation_table():

    db.execute("""

    CREATE TABLE IF NOT EXISTS automation_workflows(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        trigger_name TEXT,

        action_name TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)