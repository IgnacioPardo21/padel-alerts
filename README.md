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

1. Busca partidos en directo en la web de **Premier Padel**
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

```
Web Premier Padel
        │
        ▼
Web Scraping
(BeautifulSoup)
        │
        ▼
Detección de parejas
        │
        ▼
Sistema de estado
(alert_state.json)
        │
        ▼
Alertas por email
(SMTP)
        │
        ▼
Actualización de matches.json
        │
        ▼
Mini web con partidos detectados
```

---

# 🔎 Cómo funciona paso a paso

## 1️⃣ Consulta de la web

El script accede a la web donde se muestran los **partidos en directo de Premier Padel**.

Utiliza **requests + BeautifulSoup** para obtener el contenido de la página.

---

## 2️⃣ Detección de jugadores

El sistema analiza el texto de la página y busca los nombres de los jugadores definidos.

Ejemplo de detección:

```
coello
tapia
chingotto
galan
```

Si aparecen ambos jugadores de una pareja en el texto:

```
se detecta que el partido está en juego
```

---

## 3️⃣ Gestión del estado del partido

Para evitar enviar múltiples correos, el sistema guarda el estado en:

```
alert_state.json
```

Este archivo almacena:

- pareja detectada
- momento en el que se detectó
- si ya se envió alerta previa

---

## 4️⃣ Alerta de inicio de partido

Cuando se detecta un nuevo partido:

```
🎾 Partido detectado
```

Se envía un email notificando que esa pareja está jugando.

---

## 5️⃣ Alerta previa al partido

Después de un tiempo configurado (por ejemplo **10 minutos**), el sistema puede enviar un aviso adicional indicando que el partido está próximo a comenzar.

---

## 6️⃣ Alerta de final de partido

Si el sistema deja de detectar a esa pareja en la web:

```
🏁 Partido terminado
```

Se envía un segundo email indicando que el partido ha finalizado.

---

## 7️⃣ Registro de partidos

Cada partido detectado se guarda en:

```
docs/matches.json
```

Esto permite:

- mantener un historial
- alimentar una mini web
- visualizar los partidos del día

Ejemplo:

```
[
  {
    "pair": "coello / tapia",
    "date": "2026-03-10"
  },
  {
    "pair": "chingotto / galan",
    "date": "2026-03-10"
  }
]
```

---

# 🌐 Mini web de partidos

El proyecto incluye una **mini página web** que muestra los partidos detectados durante el día.

La web lee automáticamente:

```
docs/matches.json
```

Esto permite ver rápidamente:

- qué parejas han jugado hoy
- qué partidos se han detectado

La página se actualiza automáticamente cada vez que el workflow hace commit.

---

# 🕒 Automatización

La ejecución automática se realiza con **GitHub Actions**.

El workflow se ejecuta cada **5 minutos**.

```
schedule:
  - cron: "*/5 * * * *"
```

Esto permite detectar partidos prácticamente **en tiempo real**.

También puede ejecutarse manualmente desde:

```
GitHub → Actions → Run workflow
```

---

# 🔐 Variables necesarias

Debes configurar estos **Secrets en GitHub**:

```
Repository → Settings → Secrets → Actions
```

Variables necesarias:

```
EMAIL_USER
EMAIL_PASS
EMAIL_DEST
```

---

# 📄 Descripción de variables

### EMAIL_USER

Correo desde el que se envían las alertas.

---

### EMAIL_PASS

Contraseña de aplicación del correo.

Ejemplo para Gmail:

```
Google → Seguridad → Contraseñas de aplicaciones
```

---

### EMAIL_DEST

Correo donde se reciben las alertas de partidos.

---

# 📂 Estructura del proyecto

```
padel-alerts

padel_alert.py
alert_state.json

docs/
   matches.json

.github/workflows/
   padel-alert.yml
```

---

# 📜 Dependencias

El proyecto utiliza **Python**.

Librerías principales:

```
requests
beautifulsoup4
smtplib
```

En GitHub Actions se instalan con:

```
pip install requests beautifulsoup4
```

---

# 📬 Ejemplo de alertas

### Inicio de partido

```
🎾 Partido detectado

Coello / Tapia están jugando ahora mismo.
```

---

### Aviso previo

```
🎾 En breve empieza el partido

Coello / Tapia están en pista.
```

---

### Fin de partido

```
🏁 Partido terminado

El partido de Coello / Tapia ha finalizado.
```

---

# 🔮 Posibles mejoras futuras

Este proyecto puede evolucionar hacia:

- 🎾 seguimiento de **todas las parejas del circuito**
- 📊 estadísticas de partidos detectados
- 📱 notificaciones push en móvil
- 🌐 dashboard web con calendario de partidos
- 🧠 predicción de partidos mediante IA
- 📈 análisis de actividad del circuito

---

# 🧠 Objetivo del proyecto

Este proyecto demuestra cómo combinar:

- agregación de información
- web scraping
- automatización
- infraestructura cloud ligera

para construir un **sistema automático de monitorización de eventos deportivos** que detecta partidos y envía alertas sin intervención manual.

---

⭐ Si te gusta el proyecto, puedes ampliarlo para seguir más jugadores, torneos o incluso otros deportes.
