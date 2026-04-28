# Convention de commits — Conventional Commits

Ce projet suit le standard [Conventional Commits 1.0.0](https://www.conventionalcommits.org/fr/).

---

## Format

```
<type>(<scope>): <description>

[corps optionnel]

[footer optionnel]
```

- **type** : obligatoire — catégorie de la modification
- **scope** : optionnel — composant concerné entre parenthèses
- **description** : obligatoire — résumé en minuscules, sans point final, max 72 caractères
- **corps** : optionnel — contexte supplémentaire (séparé par une ligne vide)
- **footer** : optionnel — références à des issues (`Closes #12`, `Fixes #8`)

---

## Types autorisés

| Type | Usage |
|------|-------|
| `feat` | Nouvelle leçon, section ou ressource pédagogique |
| `fix` | Correction d'une erreur dans le contenu ou le code |
| `docs` | Modification de la documentation uniquement |
| `style` | Mise en forme, diagrammes, images — sans changement de contenu |
| `refactor` | Restructuration sans ajout ni suppression de contenu |
| `perf` | Optimisation (scripts, notebooks) |
| `test` | Ajout ou correction de tests |
| `chore` | Maintenance : dépendances, configuration, scripts |
| `ci` | Configuration des workflows GitHub Actions |
| `revert` | Annulation d'un commit précédent |

---

## Scopes suggérés

| Scope | Description |
|-------|-------------|
| `linux` | Cours Linux |
| `mongodb` | Cours MongoDB |
| `docker` | Cours Docker |
| `pyspark` | Cours pySpark |
| `python` | Cours Python |
| `git` | Cours Git |
| `cloud` | Cours Cloud |
| `sql` | Cours SQL |
| `airflow` | Cours Airflow |
| `utils` | Scripts utilitaires |
| `ci` | Workflows GitHub Actions |
| `docs` | Documentation générale |
| `readme` | Fichier README |

---

## Exemples

```
feat(linux): ajouter diagrammes mermaid chapitres 1-4

fix(mongodb): corriger label mermaid section replica set

docs(readme): mettre à jour les liens vers la documentation

style(docker): reformater les tableaux de commandes

chore(ci): migrer vers ci.yml unifié

feat(pyspark): ajouter badge Colab notebooks 01-04
```

---

## Référencer des issues

```
fix(linux): corriger le diagramme permissions utilisateurs

Closes #8
```

---

## Règles à respecter

- Toujours en minuscules
- Pas de point `.` en fin de description
- Description en français
- Un commit = une modification logique (ne pas mélanger `fix` et `feat`)
- Éviter les commits vagues : `fix stuff`, `wip`, `update`
