# devsecops-mini-pipeline

> ⚠️ **Application VOLONTAIREMENT vulnérable**, destinée à l'apprentissage DevSecOps (« casser, détecter, corriger »).
> Ne jamais la déployer ni l'exposer. Toutes les données et tous les secrets sont factices.
> Les défauts plantés sont repérés par des commentaires `VULN-n` et décrits dans [CLAUDE.md](CLAUDE.md).

## Routes

| Méthode | Route | Description |
|---|---|---|
| GET | `/health` | État de l'API |
| GET | `/users/{username}` | Recherche d'un utilisateur (SQLite en mémoire, 3 utilisateurs fictifs : alice, bob, carol) |
| GET | `/token` | Renvoie un JWT si l'en-tête `X-API-Key` est valide |

## Lancer en local (Python 3.14+)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1      # Linux/macOS : source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Puis : <http://127.0.0.1:8000/health> ou <http://127.0.0.1:8000/docs>.

## Lancer avec Docker

```bash
docker build -t devsecops-mini:dev .
docker run --rm -p 8000:8000 devsecops-mini:dev
```
