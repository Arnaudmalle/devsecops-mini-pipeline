# Projet d'apprentissage DevSecOps — « casser, détecter, corriger »

## Contexte
API FastAPI VOLONTAIREMENT vulnérable, jetable. Aucune donnée réelle, tous les secrets sont factices.
L'objectif est que j'apprenne : je dois comprendre chaque changement.

## Règles de collaboration
- Explique ce que tu vas faire et pourquoi AVANT de modifier un fichier.
- Un changement à la fois, rien « au passage ».
- Ne corrige jamais un défaut planté sans demande explicite.
- Workflow CI et corrections : c'est moi qui code. Tu relis et tu poses des questions, sans donner la solution d'emblée.
- Interdit pour « faire passer » le pipeline : désactiver une règle, relever un seuil, ajouter une exception (nosemgrep, .gitleaksignore, .trivyignore). Seule exception : un faux positif que j'ai documenté et justifié.

## Défauts plantés (repérés par des commentaires VULN-n)
1. Clé API factice en dur → gitleaks
2. Injection SQL par concaténation → Semgrep
3. Dépendance avec CVE HIGH/CRITICAL → Trivy fs / pip-audit
4. Dockerfile : image `latest`, exécution en root → Hadolint, Trivy

## Conventions
- Conventional Commits. Une correction = un commit : `fix(<secrets|sast|sca|docker>): <quoi> (<outil> <règle>)`.
- Versions épinglées partout (dépendances, images, actions GitHub par SHA). Toute version doit être vérifiée en ligne sur la source officielle. Si tu ne peux pas vérifier, dis-le au lieu de supposer.
- Seuil de blocage : HIGH/CRITICAL, ou l'équivalent propre à chaque outil.
- Secrets factices au format générique, sans préfixe réel (AKIA, sk_live_, ghp_…).

## Commandes
(à compléter après la génération)