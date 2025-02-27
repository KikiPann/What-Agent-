import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from catboost import CatBoostClassifier

# Cargar el dataset
# Se asume que el archivo CSV contiene las características y la variable objetivo ('Agent')
data = pd.read_csv("Data/Balanceado-Con-los-Datos-Deep.csv")

# Separar características (X) y variable objetivo (y)
X = data.drop('Agent', axis=1)  # Todas las columnas excepto 'Agent' son características
y = data['Agent']  # 'Agent' es la variable objetivo

# Dividir los datos en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Identificar las columnas categóricas por su índice en el dataframe
categorical_features_indices = [X.columns.get_loc(col) for col in ['Map', 'Role', 'Difficulty']]

# Crear y configurar el modelo CatBoostClassifier
cat_model = CatBoostClassifier(
    random_state=42,      # Fijar la semilla para reproducibilidad
    iterations=100,       # Número de árboles en el ensamble
    learning_rate=0.1,    # Tasa de aprendizaje
    depth=6,              # Profundidad máxima de los árboles de decisión
    loss_function='MultiClass',  # Función de pérdida para clasificación multiclase
    verbose=0             # Silenciar la salida de entrenamiento
)

# Entrenar el modelo con las características categóricas especificadas
cat_model.fit(X_train, y_train, cat_features=categorical_features_indices)

# Realizar predicciones en el conjunto de prueba
y_pred = cat_model.predict(X_test)

# Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy:.2f}')

# Mostrar matriz de confusión
def plot_confusion_matrix(y_test, y_pred, model):
    """
    Genera y muestra una matriz de confusión con etiquetas correspondientes.
    """
    conf_matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues",
                xticklabels=model.classes_, yticklabels=model.classes_)
    plt.xlabel('Predicción')
    plt.ylabel('Valor Real')
    plt.title('Matriz de Confusión')
    plt.show()

# Graficar la matriz de confusión
plot_confusion_matrix(y_test, y_pred, cat_model)

# Imprimir reporte de clasificación
print('Reporte de clasificación:')
print(classification_report(y_test, y_pred))

# Función para recomendar el mejor agente según el mapa, rol y dificultad
def recommend_agent(role_name, map_name, difficulty, trained_model):
    """
    Recomienda el mejor agente basado en el rol, mapa y dificultad.

    Parámetros:
    - role_name (str): Rol del agente (Ej. 'Duelista', 'Controlador').
    - map_name (str): Mapa de juego (Ej. 'Ascent', 'Bind').
    - difficulty (str): Dificultad del agente (Ej. 'Baja', 'Media', 'Alta').
    - trained_model (CatBoostClassifier): Modelo CatBoost entrenado.

    Retorna:
    - Nombre del agente recomendado.
    """
    # Crear un DataFrame con los valores de entrada y valores numéricos ficticios
    input_data = pd.DataFrame([[map_name, role_name, difficulty, 0, 0, 0, 0, 0]],
                              columns=['Map', 'Role', 'Difficulty', 'ACS', 'Kills', 'Assists', 'Deaths', 'ADR'])

    # Predecir probabilidades de cada agente
    probabilities = trained_model.predict_proba(input_data)

    # Obtener el índice de la clase con la mayor probabilidad
    best_agent_index = np.argmax(probabilities)
    best_agent = trained_model.classes_[best_agent_index]  # Obtener el nombre del agente

    print(f"El agente recomendado para el rol '{role_name}' en el mapa '{map_name}' con dificultad '{difficulty}' es: {best_agent}")
    return best_agent

# Ejemplo de uso de la función de recomendación
recommend_agent('Duelista', 'Fracture', 'Media', cat_model)

from sklearn.model_selection import GridSearchCV

# Definir la cuadrícula de hiperparámetros
param_grid = {
    'iterations': [100, 200, 300],
    'learning_rate': [0.01, 0.1, 0.2],
    'depth': [4, 6, 8]
}

# Crear el modelo base
cat_model = CatBoostClassifier(random_state=42, verbose=0)

# Configurar GridSearchCV
grid_search = GridSearchCV(estimator=cat_model, param_grid=param_grid, cv=3, scoring='accuracy', n_jobs=-1)

# Entrenar GridSearchCV
grid_search.fit(X_train, y_train, cat_features=categorical_features_indices)

# Mostrar los mejores hiperparámetros
print("Mejores hiperparámetros:", grid_search.best_params_)

# Evaluar el mejor modelo
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del mejor modelo: {accuracy:.2f}')