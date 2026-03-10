# 🎾 Padel Match Alert

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions-black)
![Web Scraping](https://img.shields.io/badge/Data-Web%20Scraping-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

Sistema automatizado que **detecta partidos en directo de pádel profesional** y envía **alertas por email cuando empiezan o terminan**.

El sistema monitoriza continuamente la web oficial de **Premier Padel** y te avisa cuando juegan las **parejas que quieras seguir**.

Todo funciona **automáticamente en la nube mediante GitHub Actions**, sin necesidad de tener el ordenador encendido.

---

# 🚀 Qué hace este proyecto

El sistema:

1. Consulta periódicamente la web de **Premier Padel**
2. Detecta si están jugando determinadas parejas
3. Envía una alerta por email cuando empieza el partido
4. Envía otra alerta cuando el partido termina
5. Guarda los partidos detectados en un archivo JSON
6. Actualiza automáticamente una mini web con los partidos del día

Todo esto se ejecuta **automáticamente cada 5 minutos** mediante **GitHub Actions**.

---

# 🎾 Parejas monitorizadas

Actualmente el sistema está configurado para detectar partidos de:

- Arturo **Coello / Tapia**
- Federico **Chingotto / Galán**

El sistema puede ampliarse fácilmente para incluir **más jugadores o parejas**.

---

# ⚙️ Arquitectura del sistema

El flujo del sistema es el siguiente:
