import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Menu Scolastico Gianelli", layout="centered")

st.title("Menu Scuola 'Gianelli'")
st.markdown("### La Valle Agordina (BL)")
st.write("Controlla con un solo clic cosa mangiano i bambini oggi e domani!")

menu_primavera_estate = {
    1: {
        "Monday": ["Risotto allo zafferano", "Prosciutto cotto", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Tuesday": ["Gnocchi al pomodoro", "Formaggio", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Wednesday": ["Pasta alle verdure", "Frittata con parmigiano", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Thursday": ["Pasta all'olio (o burro)", "Arrosto di tacchino", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Friday": ["Pasta al pesto", "Polpette di pesce", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Saturday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""],
        "Sunday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""]
    },
    2: {
        "Monday": ["Gnocchi alla romana", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Tuesday": ["Pasta alle verdure", "Coscette di pollo", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Wednesday": ["Insalata di riso", "Formaggio", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Thursday": ["Pasta con ricotta", "Scaloppine di pollo al limone", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Friday": ["Pasta pomodoro", "Filetti di pesce al limone", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Saturday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""],
        "Sunday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""]
    },
    3: {
        "Monday": ["Pasta al pesto", "Formaggio fresco", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Tuesday": ["Risotto con verdure", "Polpette di carne al forno", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Wednesday": ["Pasta con lenticchie", "Frittata", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Thursday": ["Pasta al pomodoro", "Polpette di pesce e patate", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Friday": ["Gnocchi al ragu", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Saturday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""],
        "Sunday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""]
    },
    4: {
        "Monday": ["Pasta all'olio (o burro)", "Crocchette di legumi", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Tuesday": ["Tacchino al forno con patate", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Wednesday": ["Pizza margherita", "Prosciutto cotto", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Thursday": ["Pasta al pomodoro", "Halibut alla pizzaiola", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Friday": ["Spaetzle alla salvia", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Saturday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""],
        "Sunday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""]
    }
}

menu_autunno_inverno = {
    1: {
        "Monday": ["Risotto con verdure", "Prosciutto cotto", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Tuesday": ["Polenta", "Spezzatino di vitello e maiale", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Wednesday": ["Pasta al pomodoro", "Frittata con parmigiano", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Thursday": ["Pasta all'olio", "Arrosto di tacchino", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Friday": ["Pasta al pesto", "Polpette di pesce", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Saturday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""],
        "Sunday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""]
    },
    2: {
        "Monday": ["Gnocchi alla romana", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Tuesday": ["Pasta alle verdure", "Coscette di pollo", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Wednesday": ["Passato di verdure", "Formaggio", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Thursday": ["Pasta con ricotta", "Scaloppine di pollo al limone", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Friday": ["Pasta pomodoro", "Filetti di pesce al limone", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Saturday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""],
        "Sunday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""]
    },
    3: {
        "Monday": ["Minestrina in brodo", "Formaggio fresco con pure", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Tuesday": ["Risotto con verdure", "Polpette di carne al forno", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Wednesday": ["Zuppa di lenticchie", "Frittata", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Thursday": ["Pasta al pomodoro", "Polpette di pesce e patate", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Friday": ["Gnocchi al ragu", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Saturday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""],
        "Sunday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""]
    },
    4: {
        "Monday": ["Pasta al burro", "Crocchette di legumi", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Tuesday": ["Minestrina in brodo vegetale", "Tacchino al forno con patate", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Wednesday": ["Pizza margherita", "Prosciutto cotto", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Thursday": ["Pasta al pomodoro", "Halibut alla pizzaiola", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Friday": ["Spaetzle alla salvia", "Verdura cruda e cotta", "Pane", "Frutta"],
        "Saturday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""],
        "Sunday": ["Scuola chiusa", "Nessun menu scolastico", "", "", ""]
    }
}

st.sidebar.header("Impostazioni Menu")
stagione = st.sidebar.selectbox("Seleziona la Stagione:", ["Primavera/Estate", "Autunno/Inverno"], index=0)

# Calcolo automatico della settimana basato sul fatto che ieri era il lunedi della seconda settimana del menu estivo
ref_date = date(2026, 10, 5) # Ieri (lunedi della seconda settimana)
oggi = date.today()
delta_days = (oggi - ref_date).days
weeks_passed = delta_days // 7
settimana_calcolata = ((1 + weeks_passed) % 4) + 1

settimana_corrente = st.sidebar.selectbox("Seleziona la settimana del menu (1-4):", [1, 2, 3, 4], index=settimana_calcolata-1)

giorni_traduzione = {
    "Monday": "Lunedi",
    "Tuesday": "Martedi",
    "Wednesday": "Mercoledi",
    "Thursday": "Giovedi",
    "Friday": "Venerdi",
    "Saturday": "Sabato",
    "Sunday": "Domenica"
}

if st.button("Mostra Menu di Oggi e Domani", type="primary"):
    domani = oggi + timedelta(days=1)
    
    giorno_oggi_en = oggi.strftime("%A")
    giorno_domani_en = domani.strftime("%A")
    
    menu_selezionato = menu_autunno_inverno if stagione == "Autunno/Inverno" else menu_primavera_estate
    
    piatti_oggi = menu_selezionato[settimana_corrente].get(giorno_oggi_en, ["Nessun menu"])
    piatti_domani = menu_selezionato[settimana_corrente].get(giorno_domani_en, ["Nessun menu"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"OGGI\n\n{giorni_traduzione.get(giorno_oggi_en, giorno_oggi_en)} {oggi.strftime('%d/%m/%Y')}")
        if giorno_oggi_en in ["Saturday", "Sunday"]:
            st.write("Weekend! Nessun servizio mensa scolastica.")
        else:
            for piatto in piatti_oggi:
                if piatto:
                    st.write(f"- {piatto}")
                    
    with col2:
        st.warning(f"DOMANI\n\n{giorni_traduzione.get(giorno_domani_en, giorno_domani_en)} {domani.strftime('%d/%m/%Y')}")
        if giorno_domani_en in ["Saturday", "Sunday"]:
            st.write("Weekend! Nessun servizio mensa scolastica.")
        else:
            for piatto in piatti_domani:
                if piatto:
                    st.write(f"- {piatto}")

st.markdown("---")
st.caption("Nota: Ricordati di aggiornare la settimana di riferimento in base al calendario scolastico effettivo.")
