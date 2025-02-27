document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const recommendationForm = document.getElementById('recommendation-form');
    const runModelButton = document.getElementById('run-model');
    const resultSection = document.querySelector('.result');
    const mapSelect = document.getElementById('map');
    const roleSelect = document.getElementById('role');
    const difficultySelect = document.getElementById('difficulty');
    const agentNameEl = document.getElementById('agent-name');
    const agentRoleEl = document.getElementById('agent-role');
    const agentImageEl = document.getElementById('agent-image');
    const agentAbilitiesEl = document.getElementById('agent-abilities');
    const agentRecommendationEl = document.getElementById('agent-recommendation');

    // Añadir eventos a los selectores para efecto visual
    const selects = document.querySelectorAll('select');
    selects.forEach(select => {
        select.addEventListener('change', function() {
            this.style.animation = 'none';
            setTimeout(() => {
                this.style.animation = 'fadeIn 0.5s';
            }, 10);
        });
    });

    // Evento de clic en el botón para obtener recomendación
    runModelButton.addEventListener('click', async function(e) {
        e.preventDefault(); // Evitar recarga de la página

        // Obtener valores seleccionados
        const map = mapSelect.value;
        const role = roleSelect.value;
        const difficulty = difficultySelect.value;

        // Mostrar la sección de resultados con animación
        resultSection.classList.remove('hidden');
        agentNameEl.innerHTML = "<span class='loading'>Analizando preferencias...</span>";
        resultSection.scrollIntoView({ behavior: 'smooth' });

        try {
            // Crear FormData para enviar los datos al servidor
            const formData = new FormData();
            formData.append('map', map);
            formData.append('role', role);
            formData.append('difficulty', difficulty);

            // Realizar petición al API para obtener recomendación
            const response = await fetch('/api/recomendar-agente', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error('Error en la solicitud al servidor: ' + response.status);
            }

            const data = await response.json();

            // Log para depuración
            console.log('Datos recibidos del servidor:', data);

            showAgentInfo(data);

        } catch (error) {
            console.error('Error al obtener recomendación:', error);

            // Mostrar mensaje de error
            agentNameEl.innerText = 'Error en la recomendación';
            agentRoleEl.innerText = 'Error';
            agentRoleEl.style.backgroundColor = '#bd3944';
            agentImageEl.src = '/static/images/default.jpg';  // Ruta corregida
            agentImageEl.alt = 'Error al cargar imagen';
            agentAbilitiesEl.innerHTML =
                '<li>No se pudo cargar la información del agente. Por favor, intenta nuevamente.</li>';
            agentRecommendationEl.innerText = 'Ocurrió un error al procesar tu solicitud. Verifica tu conexión e intenta de nuevo.';
        }
    });

    // Función para mostrar la información del agente recomendado
    function showAgentInfo(data) {
        // Actualizar información básica del agente
        agentNameEl.innerText = data.agente;
        agentRoleEl.innerText = data.rol || 'Rol no especificado';

        // Asegurar que la ruta de la imagen sea correcta (MUY IMPORTANTE)
        if (data.imagen) {
            agentImageEl.src = `/static/images/${data.imagen}`;  // Construye la ruta correctamente
            console.log('Ruta de imagen desde API: ', agentImageEl.src); //Ver ruta en consola
        } else {
            agentImageEl.src = `/static/images/default.jpg`;
            console.log('Ruta de imagen generada: ', agentImageEl.src); //Ver ruta en consola
        }
        agentImageEl.alt = `Imagen de ${data.agente}`;

        // Restaurar estilos si hubo un error previo
        agentRoleEl.style.backgroundColor = '';

        // Mostrar habilidades
        agentAbilitiesEl.innerHTML = '';
        if (data.habilidades && Array.isArray(data.habilidades)) {
            data.habilidades.forEach(habilidad => {
                const li = document.createElement('li');
                li.textContent = habilidad;
                agentAbilitiesEl.appendChild(li);
            });
        } else {
            const li = document.createElement('li');
            li.textContent = 'Información de habilidades no disponible';
            agentAbilitiesEl.appendChild(li);
        }

        // Construir mensaje de recomendación
        let selectedMap = mapSelect.options[mapSelect.selectedIndex].text;
        if (mapSelect.value === 'Aleatorio') {
            selectedMap = data.mapa;
        }

        let recomendacionTexto = `${data.agente} es una excelente elección para el mapa ${selectedMap}.`;

        if (roleSelect.value !== 'Aleatorio') {
            recomendacionTexto += ` Como ${data.rol}, puede controlar eficazmente el campo de batalla.`;
        }

        if (difficultySelect.value !== 'Aleatorio') {
            if (difficultySelect.value === 'facil') {
                recomendacionTexto += ' Sus habilidades son intuitivas y fáciles de dominar.';
            } else if (difficultySelect.value === 'media') {
                recomendacionTexto += ' Con un poco de práctica, podrás aprovechar todo su potencial.';
            } else {
                recomendacionTexto += ' Dominar sus habilidades requiere tiempo, pero los resultados son excepcionales.';
            }
        }

        agentRecommendationEl.innerText = recomendacionTexto;
    }
});