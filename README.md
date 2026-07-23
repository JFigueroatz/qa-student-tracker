# 📚 QA Student Tracker

> Sistema minimalista de validación de entregas académicas, desarrollado como proyecto base para la actividad de Aseguramiento de la Calidad del Software.

## 👥 Integrantes

| Nombre | Rol |
|---|---|
| Jefferson Alejandro Tzib Figueroa | QA Lead / DevOps |
| Ericka Andrea Chacon Kress | Developer |
| Manuel Ronaldinho Maquin Zuñiga | Documentación |

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.12
- **Testing:** pytest
- **Linter:** flake8
- **CI/CD:** GitHub Actions

## 🔗 Enlaces del Proyecto

| Recurso | Enlace |
|---|---|
| 📊 GitHub Project | [Ver Project](https://github.com/users/JFigueroatz/projects/1) |
| 🔀 Pull Request de validación | [PR #1](https://github.com/JFigueroatz/qa-student-tracker/pull/1) |
| 📄 Matriz CTQ | [docs/quality/CTQ.md](docs/quality/CTQ.md) |
| ✅ Definition of Done | [docs/quality/DoD.md](docs/quality/DoD.md) |
| ⚙️ Quality Gate Workflow | [.github/workflows/quality-gate.yml](.github/workflows/quality-gate.yml) |
| 🧪 Evidencias | [docs/quality/QualityGate.md](docs/quality/QualityGate.md) |

## ⚙️ Quality Gate

El workflow se ejecuta automáticamente en cada PR hacia `main` y valida:

1. ✅ Existencia de documentación obligatoria
2. ✅ Contenido mínimo de documentos de calidad
3. ✅ Linter sin errores críticos (flake8)
4. ✅ Pruebas unitarias pasando (pytest — 16 passed)

## 🚀 Cómo ejecutar

```bash
pip install pytest flake8
pytest src/test_tracker.py -v
flake8 src/ --max-line-length=100
```

## 📌 Limitaciones conocidas

La regla de protección de rama en `main` requiere cuenta GitHub Team. Con cuenta gratuita, la ejecución del gate es visible en GitHub Actions pero no bloquea automáticamente el merge. Limitación documentada en `docs/quality/QualityGate.md`.
