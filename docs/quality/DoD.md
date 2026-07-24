# Definition of Done (DoD)
## Proyecto: QA Student Tracker

> El DoD establece criterios objetivos y verificables que determinan cuándo un elemento de trabajo está realmente completado. Ningún ítem puede considerarse "Done" si algún criterio obligatorio no se cumple.

---

## DoD para Historia de Usuario

Una historia de usuario está **Done** cuando:

- [x] Los criterios de aceptación están redactados de forma clara y son verificables (no "funciona bien", sino "retorna `estado: aprobado` cuando nota >= 61 y en_tiempo es True").
- [x] Existe al menos un CTQ asociado cuando la historia impacta calidad observable.
- [x] El código está implementado en una rama de trabajo (`feature/...`), nunca directamente en `main`.
- [x] Existen pruebas unitarias o funcionales que cubren los casos normales y los casos borde.
- [x] Las pruebas se ejecutan sin errores (`pytest` retorna exit code 0).
- [x] La evidencia de pruebas está registrada en el issue correspondiente.

---

## DoD para Pull Request

Un Pull Request está **Done** cuando:

- [x] El PR está vinculado a al menos un issue del backlog mediante referencia (`Refs CTQ-001, CTQ-002, CTQ-003`).
- [x] El Quality Gate de GitHub Actions se ejecutó y produjo resultado visible.
- [x] No existen errores críticos abiertos relacionados con el cambio (flake8 retorna 0 errores E9/F63/F7/F82).
- [x] El README.md o la documentación en `docs/quality/` fue actualizada si el cambio modifica comportamiento o estructura.
- [x] Al menos un integrante del equipo revisó y aprobó el PR (AndreaChk).
- [x] El checklist de la plantilla de PR está completo y no tiene ítems sin marcar sin justificación.

---

## DoD para Sprint / Release

Un sprint o release está **Done** cuando:

- [x] Todos los CTQs con prioridad **Must** están completados o tienen justificación documentada de por qué se posponen.
- [x] La deuda técnica identificada durante el sprint está registrada como issues en el backlog con etiqueta `deuda-tecnica`.
- [x] Las evidencias de ejecución del Quality Gate están consolidadas en `docs/quality/QualityGate.md`.
- [ ] La versión está etiquetada en GitHub (`git tag vX.Y`) o existe una release note en GitHub Releases.
- [x] El tablero de GitHub Project muestra todos los ítems del sprint en estado **Done** o con justificación en **Backlog**.

---

## Criterios de excepción documentada

Si un criterio no puede cumplirse, el equipo debe:

1. Registrar la excepción en el issue o PR afectado.
2. Describir la causa raíz (limitación técnica, tiempo, dependencia externa).
3. Crear un issue de seguimiento etiquetado como `excepcion-dod`.
4. Obtener aprobación explícita de otro integrante antes de fusionar.
