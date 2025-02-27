"""
Archivo que contiene la información de los agentes de Valorant.
Esta información se usará para mostrar detalles en la aplicación web.
"""

AGENT_DATA = {
    "Astra": {
        "role": "Controlador",
        "image": "static/images/astra.jpg",
        "abilities": [
            "Nova Pulsar: Coloca estrellas que detonan como concusión",
            "Nebula / Disipador: Coloca estrellas que se transforman en humo",
            "Pozo Gravitacional: Coloca estrellas que succionan jugadores",
            "ULTIMATE - Fisura Cósmica: Coloca una pared que bloquea balas y sonido"
        ]
    },
    "Breach": {
        "role": "Iniciador",
        "image": "static/images/breach.jpg",
        "abilities": [
            "Carga Cegadora: Dispara un flash a través de paredes",
            "Falla Tectónica: Crea un temblor que aturde",
            "Postimpacto: Dispara una carga explosiva a través de paredes",
            "ULTIMATE - Fragor Rodante: Desata ondas sísmicas masivas"
        ]
    },
    "Brimstone": {
        "role": "Controlador",
        "image": "static/images/brimstone.jpg",
        "abilities": [
            "Incendiario: Lanza una granada incendiaria",
            "Cortina de Humo: Despliega humo en ubicaciones marcadas",
            "Baliza Estimulante: Coloca una baliza que aumenta la velocidad de disparo",
            "ULTIMATE - Golpe Orbital: Marca un área para un ataque láser masivo"
        ]
    },
    "Chamber": {
        "role": "Centinela",
        "image": "static/images/chamber.jpg",
        "abilities": [
            "Cazador de Cabezas: Pistola pesada de alta precisión",
            "Rendez-Vous: Coloca dos anclajes de teletransporte",
            "Marca Registrada: Coloca una trampa que revela enemigos",
            "ULTIMATE - Tour de Force: Rifle de francotirador potente"
        ]
    },
    "Cypher": {
        "role": "Centinela",
        "image": "static/images/cypher.jpg",
        "abilities": [
            "Trampa Cibernética: Coloca trampas invisibles",
            "Cámara Espía: Lanza una cámara para vigilar",
            "Cable Trampa: Cable que revela y ralentiza enemigos",
            "ULTIMATE - Robo Neural: Revela la posición de enemigos vivos"
        ]
    },
    "Jett": {
        "role": "Duelista",
        "image": "static/images/jett.jpg",
        "abilities": [
            "Updraft: Impulso vertical",
            "Tailwind: Dash rápido en la dirección de movimiento",
            "Cloudburst: Lanza bombas de humo",
            "ULTIMATE - Blade Storm: Conjunto de cuchillos precisos"
        ]
    },
    "KAY/O": {
        "role": "Iniciador",
        "image": "static/images/kayo.jpg",
        "abilities": [
            "FLASH/drive: Granada cegadora",
            "ZERO/point: Cuchillo que suprime habilidades enemigas",
            "FRAG/ment: Granada explosiva que daña repetidamente",
            "ULTIMATE - NULL/cmd: Pulso que suprime a todos los enemigos"
        ]
    },
    "Killjoy": {
        "role": "Centinela",
        "image": "static/images/killjoy.jpg",
        "abilities": [
            "Alarmbot: Robot que persigue enemigos",
            "Torreta: Torreta automática",
            "Nanoswarm: Granada de nanorobots oculta",
            "ULTIMATE - Lockdown: Dispositivo que captura enemigos en el área"
        ]
    },
    "Omen": {
        "role": "Controlador",
        "image": "static/images/omen.jpg",
        "abilities": [
            "Paranoia: Dispara sombra que ciega",
            "Dark Cover: Lanza orbe de sombra",
            "Shrouded Step: Se teletransporta a corta distancia",
            "ULTIMATE - From the Shadows: Se teletransporta a cualquier lugar del mapa"
        ]
    },
    "Phoenix": {
        "role": "Duelista",
        "image": "static/images/phoenix.jpg",
        "abilities": [
            "Curveball: Bola de fuego que ciega",
            "Hot Hands: Bola de fuego que daña",
            "Blaze: Muro de fuego",
            "ULTIMATE - Run it Back: Marca una ubicación para revivir después de morir"
        ]
    },
    "Raze": {
        "role": "Duelista",
        "image": "static/images/raze.jpg",
        "abilities": [
            "Blast Pack: Carga explosiva",
            "Paint Shells: Clúster de granadas",
            "Boom Bot: Robot explosivo",
            "ULTIMATE - Showstopper: Lanzacohetes con gran daño"
        ]
    },
    "Reyna": {
        "role": "Duelista",
        "image": "static/images/reyna.jpg",
        "abilities": [
            "Devour: Consume orbes para curarse",
            "Dismiss: Consume orbes para volverse intangible",
            "Leer: Ojo que ciega a los enemigos que lo miran",
            "ULTIMATE - Empress: Aumenta cadencia de disparo y crea orbes automáticamente"
        ]
    },
    "Sage": {
        "role":"Centinela",
        "image": "static/images/sage.jpg",
        "abilities": [
            "Slow Orb: Orbe que ralentiza enemigos",
            "Healing Orb: Cura aliados",
            "Barrier Orb: Crea una pared de hielo",
            "ULTIMATE - Resurrection: Revive a un aliado caído"
        ]
    },
    "Skye": {
        "role": "Iniciador",
        "image": "static/images/skye.jpg",
        "abilities": [
            "Trailblazer: Controla un tigre que salta sobre enemigos",
            "Guiding Light: Halcón que ciega enemigos",
            "Regrowth: Cura aliados en área",
            "ULTIMATE - Seekers: Envía buscadores que encuentran enemigos"
        ]
    },
    "Sova": {
        "role": "Iniciador",
        "image": "static/images/sova.jpg",
        "abilities": [
            "Shock Bolt: Flecha que causa daño",
            "Recon Bolt: Flecha que revela enemigos",
            "Owl Drone: Drone que marca enemigos",
            "ULTIMATE - Hunter's Fury: Dispara rayos de energía a través de paredes"
        ]
    },
    "Viper": {
        "role": "Controlador",
        "image": "static/images/viper.jpg",
        "abilities": [
            "Poison Cloud: Emisor de gas venenoso",
            "Toxic Screen: Muro de gas tóxico",
            "Snake Bite: Granada que crea charco corrosivo",
            "ULTIMATE - Viper's Pit: Nube de toxinas masiva"
        ]
    },
    "Yoru": {
        "role": "Duelista",
        "image": "static/images/yoru.jpg",
        "abilities": [
            "Blindside: Flashbang que rebota",
            "Gatecrash: Coloca anclaje de teletransporte",
            "Fakeout: Crea pasos falsos",
            "ULTIMATE - Dimensional Drift: Se vuelve invisible y se mueve entre dimensiones"
        ]
    }
}

# Mapeo de valores del formulario a valores del modelo (Estos no son parte de AGENT_DATA)
MAP_MAPPING = {
    "ascent": "Ascent",
    "bind": "Bind",
    "breeze": "Breeze",
    "fracture": "Fracture",
    "haven": "Haven",
    "icebox": "Icebox",
    "split": "Split"
}

ROLE_MAPPING = {
    "centinela": "Centinela",
    "controlador": "Controlador",
    "duelista": "Duelista",
    "iniciador": "Iniciador"
}

DIFFICULTY_MAPPING = {
    "facil": "Baja",
    "media": "Media",
    "dificil": "Alta"
}