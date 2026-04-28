# Guide de contribution — Courses

Merci de contribuer à ce projet ! Ce document décrit les règles à suivre pour maintenir une collaboration claire et cohérente.

---

## Table des matières

1. [Workflow Git](#workflow-git)
2. [Convention de commits](#convention-de-commits)
3. [Ouvrir une issue](#ouvrir-une-issue)
4. [Soumettre une Pull Request](#soumettre-une-pull-request)
5. [Qualité du code](#qualité-du-code)

---

## Workflow Git

Ce projet suit le modèle **GitHub Flow** :

```
main  ←  feat/ajout-chapitre-kubernetes
      ←  fix/correction-diagramme-mermaid
      ←  docs/mise-a-jour-readme
```

1. Créer une branche depuis `main` avec un nom explicite
2. Effectuer les modifications en respectant la convention de commits
3. Ouvrir une Pull Request vers `main`
4. Attendre la revue avant de merger

### Nommage des branches

| Type | Exemple |
|------|---------|
| Nouvelle leçon / contenu | `feat/linux-chapitre-13-kubernetes` |
| Correction d'erreur | `fix/mongodb-label-mermaid` |
| Documentation | `docs/mise-a-jour-contributing` |
| Refactoring | `refactor/pyspark-notebook-03` |
| CI / scripts | `ci/migration-workflow-unifie` |

---

## Convention de commits

Voir [COMMIT_CONVENTION.md](COMMIT_CONVENTION.md) pour le détail complet.

En résumé, format Conventional Commits :

```
<type>(<scope>): <description courte>
```

Exemples :

```
feat(linux): ajouter diagrammes mermaid chapitres 1-4
fix(mongodb): corriger label mermaid section replica set
docs(readme): mettre à jour les liens vers la documentation
```

---

## Ouvrir une issue

Avant d'ouvrir une issue :

- Vérifier qu'elle n'existe pas déjà
- Utiliser le bon template (Bug ou Contenu)
- Fournir un titre clair au format `[type] description courte`

Types : `[bug]`, `[contenu]`, `[question]`, `[amélioration]`

---

## Soumettre une Pull Request

- Une PR = un objectif précis
- Le titre doit suivre la convention de commits : `type(scope): description`
- Remplir entièrement le template de PR
- La CI (lint) doit passer avant le merge

---

## Qualité du code

Pour les fichiers Python (`.py`) et notebooks (`.ipynb`) :

```bash
# Vérifier localement avant de pousser
sh utils/ci.sh
```

- Linter : `ruff` (via `nbqa` pour les notebooks)
- Pas de secrets ou credentials dans le code
- Commentaires en français
