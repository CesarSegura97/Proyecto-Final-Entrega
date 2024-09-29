import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos desde el repositorio de GitHub
url = "https://raw.githubusercontent.com/CesarSegura97/Proyecto-Final-Entrega/refs/heads/main/Datos%20Limpios%20proyecto.csv"
data = pd.read_csv(url)

# Título de la aplicación
st.title("Proyecto César Segura")
st.title("Visualización de Ratios Financieros")

st.title("Ratio de Liquidez")
# Filtro por Country para la primera gráfica
countries = data['Country'].unique()
selected_country_current = st.selectbox("Selecciona un país para graficar el Ratio de Liquidez por Industria", options=countries)

# Filtrar los datos según la selección de país
filtered_data_current = data[data['Country'] == selected_country_current]

# Gráfica de barras para el promedio del Current Ratio
if not filtered_data_current.empty:
    avg_current_ratio = filtered_data_current.groupby('Industry')['Current_Ratio'].mean().reset_index()

    st.subheader(f'Promedio del Ratio de Liquidez por Industria en {selected_country_current}')

    # Justificación: El Current Ratio es un indicador clave de liquidez que muestra la capacidad de una empresa para cubrir sus obligaciones a corto plazo. 
    # Esta gráfica ayuda a comparar la eficiencia de diferentes industrias en la gestión de sus activos y pasivos.

    plt.figure(figsize=(10, 6))

    # Generar colores únicos para cada industria
    colors = plt.cm.viridis(np.linspace(0, 1, len(avg_current_ratio)))

    plt.bar(avg_current_ratio['Industry'], avg_current_ratio['Current_Ratio'], color=colors)
    plt.xlabel('Industria')
    plt.ylabel('Promedio del Current Ratio')
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write("No hay datos que mostrar para el país seleccionado.")

#Segunda Gráfica
st.title("Ratio de Deuda a Patrimonio")

# Filtro por Country para la segunda gráfica
selected_country_debt = st.selectbox("Selecciona un país para graficar Ratio de Deuda a Patrimonio", options=countries)

# Filtrar los datos según la selección de país
filtered_data_debt = data[data['Country'] == selected_country_debt]

# Gráfica de pastel para el promedio del Debt to Equity Ratio
if not filtered_data_debt.empty:
    industries = filtered_data_debt['Industry'].unique()
    selected_industry_debt = st.selectbox("Selecciona la Industria", options=industries)

    filtered_data_debt_industry = filtered_data_debt[filtered_data_debt['Industry'] == selected_industry_debt]

    if not filtered_data_debt_industry.empty:
        avg_debt_equity_ratio = filtered_data_debt_industry.groupby('Company_Size')['Debt_to_Equity_Ratio'].mean().reset_index()

        st.subheader(f'Comportamiento del Promedio del Ratio de Deuda a Patrimonio por Tamaño de Empresa en {selected_country_debt} - {selected_industry_debt}')

        # Justificación: El Debt to Equity Ratio es una medida de la proporción de deuda en comparación con el capital propio de una empresa. 
        # Esta gráfica permite visualizar cómo se distribuye la deuda entre diferentes tamaños de empresas en la industria específica, ayudando a entender su estructura de capital.

        plt.figure(figsize=(8, 8))
        plt.pie(avg_debt_equity_ratio['Debt_to_Equity_Ratio'], labels=avg_debt_equity_ratio['Company_Size'], autopct='%1.1f%%', startangle=140)
        plt.title('Distribución del Promedio')
        st.pyplot(plt)
    else:
        st.write("No hay datos que mostrar para la industria seleccionada.")
else:
    st.write("No hay datos que mostrar para el país seleccionado.")


st.title("Cobertura de Gastos Financieros")

# Gráfica de líneas para el Interest Coverage Ratio
selected_country_interest = st.selectbox("Selecciona un país para graficar Cobertura de Gastos Financieros", options=countries)

# Filtrar los datos según la selección de país
filtered_data_interest = data[data['Country'] == selected_country_interest]

if not filtered_data_interest.empty:
    avg_interest_coverage = filtered_data_interest.groupby('Industry')['Interest_Coverage_Ratio'].mean().reset_index()

    st.subheader(f'Promedio de la Cobertura de Gastos Financieros por Industria en {selected_country_interest}')

    # Justificación: El Interest Coverage Ratio indica la capacidad de una empresa para cubrir sus gastos de interés con sus ganancias. 
    # Esta gráfica de líneas permite observar las diferencias entre industrias y su capacidad para manejar su deuda, lo que es crucial para la sostenibilidad financiera.

    plt.figure(figsize=(10, 6))
    plt.plot(avg_interest_coverage['Industry'], avg_interest_coverage['Interest_Coverage_Ratio'], marker='o', color='green', linewidth=3)
    plt.xlabel('Industria')
    plt.ylabel('Promedio del Interest Coverage Ratio')
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write("No hay datos que mostrar para el país seleccionado.")

