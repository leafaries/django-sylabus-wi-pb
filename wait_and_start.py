import psycopg2, os, time, subprocess, sys

print("Waiting for database...")
while True:
    try:
        psycopg2.connect(
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"]
        )
        break
    except Exception as e:
        print(f"DB not ready, retrying in 2s... ({e})")
        time.sleep(2)

print("Database is ready!")
subprocess.run([sys.executable, "manage.py", "migrate"])
os.execvp(sys.executable, [sys.executable, "manage.py", "runserver", "0.0.0.0:8000"])
