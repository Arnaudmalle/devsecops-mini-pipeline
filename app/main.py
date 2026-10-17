"""API FastAPI VOLONTAIREMENT vulnérable (projet d'apprentissage DevSecOps).

Ne jamais déployer. Toutes les données et tous les secrets sont factices.
"""

import sqlite3
from contextlib import asynccontextmanager

import jwt
from fastapi import FastAPI, Header, HTTPException

# VULN-1 : clé API en dur dans le code source (factice)
api_key = "vOUKpCQBotxnReg2akR0zhuakUH3BGKDIFH6LA81"

USERS = [
    ("alice", "alice@example.invalid"),
    ("bob", "bob@example.invalid"),
    ("carol", "carol@example.invalid"),
]

db: sqlite3.Connection


@asynccontextmanager
async def lifespan(_: FastAPI):
    global db
    db = sqlite3.connect(":memory:", check_same_thread=False)
    db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT)")
    db.executemany("INSERT INTO users (username, email) VALUES (?, ?)", USERS)
    db.commit()
    yield
    db.close()


app = FastAPI(title="devsecops-mini-pipeline", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users/{username}")
def get_user(username: str):
    # VULN-2 : injection SQL, entrée utilisateur interpolée dans la requête (f-string)
    rows = db.execute(f"SELECT id, username, email FROM users WHERE username = '{username}'").fetchall()
    if not rows:
        raise HTTPException(status_code=404, detail="user not found")
    return [{"id": r[0], "username": r[1], "email": r[2]} for r in rows]


@app.get("/token")
def get_token(x_api_key: str = Header(default="")):
    if x_api_key != api_key:
        raise HTTPException(status_code=401, detail="invalid api key")
    return {"token": jwt.encode({"sub": "admin"}, api_key, algorithm="HS256")}
