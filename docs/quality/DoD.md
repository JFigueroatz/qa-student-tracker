# Definition of Done (DoD)
## Proyecto: QA Student Tracker

> El DoD establece criterios objetivos y verificables que determinan cuándo un elemento de trabajo está realmente completado. Ningún ítem puede considerarse "Done" si algún criterio obligatorio no se cumple.

---

## DoD para Historia de Usuario

Una historia de usuario está **Done** cuando:

- [ ] Los criterios de aceptación están redactados de forma clara y son verificables (no "funciona bien", sino "retorna `estado: aprobado` cuando nota >= 61 y en_tiempo es True").
- [ ] Existe al menos un CTQ asociado cuando la historia impacta calidad observable.
- [ ] El código está implementado en una rama de trabajo (`feature/...`), nunca directamente en `main`.
- [ ] Existen pruebas unitarias o funcionales que cubren los casos normales y los casos borde.
- [ ] Las pruebas se ejecutan sin errores (`pytest` retorna exit code 0).
- [ ] La evidencia de pruebas está registrada en el issue correspondiente.

---

## DoD para Pull Request

Un Pull Request está **Done** cuando:

- [ ] El PR está vinculado a al menos un issue del backlog mediante referencia (`Closes #N` o `Refs CTQ-00X`).
- [ ] El Quality Gate de GitHub Actions se ejecutó y produjo resultado visible.
- [ ] No existen errores críticos abiertos relacionados con el cambio (flake8 retorna 0 errores E9/F63/F7/F82).
- [ ] El README.md o la documentación en `docs/quality/` fue actualizada si el cambio modifica comportamiento o estructura.
- [ ] Al menos un integrante del equipo revisó y aprobó el PR.
- [ ] El checklist de la plantilla de PR está completo y no tiene ítems sin marcar sin justificación.

---

## DoD para Sprint / Release

Un sprint o release está **Done** cuando:

- [ ] Todos los CTQs con prioridad **Must** están completados o tienen justificación documentada de por qué se posponen.
- [ ] La deuda técnica identificada durante el sprint está registrada como issues en el backlog con etiqueta `deuda-tecnica`.
- [ ] Las evidencias de ejecución del Quality Gate están consolidadas en `docs/quality/QualityGate.md`.
- [ ] La versión está etiquetada en GitHub (`git tag vX.Y`) o existe una release note en GitHub Releases.
- [ ] El tablero de GitHub Project muestra todos los ítems del sprint en estado **Done** o con justificación en **Backlog**.

---

## Criterios de excepción documentada

Si un criterio no puede cumplirse, el equipo debe:

1. Registrar la excepción en el issue o PR afectado.
2. Describir la causa raíz (limitación técnica, tiempo, dependencia externa).
3. Crear un issue de seguimiento etiquetado como `excepcion-dod`.
4. Obtener aprobación explícita de otro integrante antes de fusionar.
