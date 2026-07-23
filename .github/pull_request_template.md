[pull_request_template.md](https://github.com/user-attachments/files/30311856/pull_request_template.md)
## Descripción del cambio

> Explique qué se modificó y por qué. Sea específico: ¿qué problema resuelve? ¿qué comportamiento cambia?

---

## CTQ relacionado

| Campo | Valor |
|---|---|
| CTQ-ID | CTQ-___ |
| Issue relacionado | #___ |
| Prioridad | Must / Should / Could |

---

## Checklist DoD

> Marque cada ítem. Si alguno no aplica, indíquelo con `N/A` y justifique brevemente.

### Historia de usuario
- [ ] Criterios de aceptación claros y verificables definidos
- [ ] CTQ asociado documentado (si aplica)
- [ ] Código implementado en rama de trabajo (no en `main`)
- [ ] Casos de prueba cubriendo escenarios normales y borde

### Pull Request
- [ ] PR vinculado al issue del backlog (`Closes #N` o `Refs CTQ-00X`)
- [ ] Quality Gate de GitHub Actions ejecutado con resultado visible
- [ ] Cero errores críticos de linter (flake8 E9/F63/F7/F82)
- [ ] README.md o documentación actualizada (si aplica)
- [ ] Al menos un integrante del equipo revisó este PR

### Documentación
- [ ] `docs/quality/CTQ.md` refleja el estado actual
- [ ] `docs/quality/QualityGate.md` actualizado con enlace a esta ejecución

---

## Evidencia

> Agregue el enlace al resultado de GitHub Actions y cualquier captura relevante.

| Tipo | Enlace / Descripción |
|---|---|
| GitHub Actions run | _[Agregar enlace]_ |
| Resultado pytest | ✅ X passed / ❌ X failed |
| Resultado flake8 | ✅ 0 errores / ❌ N errores |

---

## Observaciones adicionales

> Si el gate falló o algún criterio DoD no se cumple, documente aquí la causa y la justificación.
