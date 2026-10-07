import streamlit as st
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
from html import escape

st.set_page_config(page_title="Menù Scuola dell'infanzia GIANELLI", page_icon="🍽️",
                   layout="centered", initial_sidebar_state="collapsed")

# ==================== CONFIGURAZIONE ====================
TZ = ZoneInfo("Europe/Rome")             # data sempre italiana (anche su server UTC)
DATA_RIFERIMENTO = date(2026, 10, 5)     # un lunedì noto...
SETTIMANA_RIFERIMENTO = 2                # ...e la sua settimana di menu (1-4)
INIZIO_AUTUNNO_INVERNO = (9, 1)          # (mese, giorno) -> da regolare col calendario scolastico
INIZIO_PRIMAVERA_ESTATE = (4, 1)
CONTORNI = ["Verdura cruda e cotta", "Pane", "Frutta"]

GIORNI = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]

TEMI = {
    "Primavera/Estate": {"icona": "🌸☀️", "c1": "#1b7a4b", "c2": "#4cb87a", "accento": "#1b7a4b"},
    "Autunno/Inverno":  {"icona": "🍂❄️", "c1": "#8e3b16", "c2": "#d9822b", "accento": "#b8541c"},
}

# Solo i piatti principali (lun-ven); i contorni si aggiungono in automatico
MENU = {
    "Primavera/Estate": {
        1: [["Risotto allo zafferano", "Prosciutto cotto"],
            ["Gnocchi al pomodoro", "Formaggio"],
            ["Pasta alle verdure", "Frittata con parmigiano"],
            ["Pasta all'olio (o burro)", "Arrosto di tacchino"],
            ["Pasta al pesto", "Polpette di pesce"]],
        2: [["Gnocchi alla romana"],
            ["Pasta alle verdure", "Coscette di pollo"],
            ["Insalata di riso", "Formaggio"],
            ["Pasta con ricotta", "Scaloppine di pollo al limone"],
            ["Pasta pomodoro", "Filetti di pesce al limone"]],
        3: [["Pasta al pesto", "Formaggio fresco"],
            ["Risotto con verdure", "Polpette di carne al forno"],
            ["Pasta con lenticchie", "Frittata"],
            ["Pasta al pomodoro", "Polpette di pesce e patate"],
            ["Gnocchi al ragù"]],
        4: [["Pasta all'olio (o burro)", "Crocchette di legumi"],
            ["Tacchino al forno con patate"],
            ["Pizza margherita", "Prosciutto cotto"],
            ["Pasta al pomodoro", "Halibut alla pizzaiola"],
            ["Spaetzle alla salvia"]],
    },
    "Autunno/Inverno": {
        1: [["Risotto con verdure", "Prosciutto cotto"],
            ["Polenta", "Spezzatino di vitello e maiale"],
            ["Pasta al pomodoro", "Frittata con parmigiano"],
            ["Pasta all'olio", "Arrosto di tacchino"],
            ["Pasta al pesto", "Polpette di pesce"]],
        2: [["Gnocchi alla romana"],
            ["Pasta alle verdure", "Coscette di pollo"],
            ["Passato di verdure", "Formaggio"],
            ["Pasta con ricotta", "Scaloppine di pollo al limone"],
            ["Pasta pomodoro", "Filetti di pesce al limone"]],
        3: [["Minestrina in brodo", "Formaggio fresco con purè"],
            ["Risotto con verdure", "Polpette di carne al forno"],
            ["Zuppa di lenticchie", "Frittata"],
            ["Pasta al pomodoro", "Polpette di pesce e patate"],
            ["Gnocchi al ragù"]],
        4: [["Pasta al burro", "Crocchette di legumi"],
            ["Minestrina in brodo vegetale", "Tacchino al forno con patate"],
            ["Pizza margherita", "Prosciutto cotto"],
            ["Pasta al pomodoro", "Halibut alla pizzaiola"],
            ["Spaetzle alla salvia"]],
    },
}

# ==================== LOGICA ====================
def lunedi_di(d: date) -> date:
    return d - timedelta(days=d.weekday())

def settimana_menu(d: date) -> int:
    """Rotazione continua 1-4 calcolata dal lunedì di riferimento."""
    settimane = (lunedi_di(d) - lunedi_di(DATA_RIFERIMENTO)).days // 7
    return (SETTIMANA_RIFERIMENTO - 1 + settimane) % 4 + 1

def stagione_di(d: date) -> str:
    if INIZIO_PRIMAVERA_ESTATE <= (d.month, d.day) < INIZIO_AUTUNNO_INVERNO:
        return "Primavera/Estate"
    return "Autunno/Inverno"

def piatti_di(d: date):
    if d.weekday() >= 5:
        return None
    return MENU[stagione_di(d)][settimana_menu(d)][d.weekday()]

def prossimo_giorno_mensa(d: date) -> date:
    n = d + timedelta(days=1)
    while n.weekday() >= 5:
        n += timedelta(days=1)
    return n

def prossimo_cambio_stagione(d: date):
    candidati = []
    for anno in (d.year, d.year + 1):
        for m, g in (INIZIO_AUTUNNO_INVERNO, INIZIO_PRIMAVERA_ESTATE):
            x = date(anno, m, g)
            if x > d:
                candidati.append(x)
    x = min(candidati)
    return x, stagione_di(x)

def data_estesa(d: date) -> str:
    return f"{GIORNI[d.weekday()]} {d.day} {MESI[d.month - 1]}"

# ==================== GRAFICA ====================
oggi = datetime.now(TZ).date()
stagione = stagione_di(oggi)
tema = TEMI[stagione]

st.markdown(f"""<style>
#MainMenu, footer, header {{visibility: hidden;}}
.block-container {{padding-top: 1.2rem; max-width: 780px;}}
.hero {{background: linear-gradient(135deg, {tema['c1']}, {tema['c2']}); border-radius: 22px; padding: 22px 26px; color: #fff; box-shadow: 0 8px 24px rgba(0,0,0,.15); margin-bottom: 18px;}}
.hero h1 {{margin: 0; padding: 0; font-size: 1.7rem; color: #fff;}}
.hero .sub {{opacity: .9; margin-top: 2px;}}
.badges {{display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px;}}
.badge {{background: rgba(255,255,255,.22); padding: 5px 12px; border-radius: 999px; font-size: .85rem; font-weight: 600;}}
.duo {{display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 10px;}}
.card {{background: #fff; border-radius: 18px; padding: 16px 18px; box-shadow: 0 4px 16px rgba(0,0,0,.08); border-top: 6px solid var(--c);}}
.lbl {{font-size: .72rem; letter-spacing: .14em; text-transform: uppercase; font-weight: 800; color: var(--c);}}
.dt {{font-size: 1.1rem; font-weight: 700; color: #222; margin: 2px 0 10px;}}
.dish {{font-weight: 700; color: #333; padding: 7px 0; border-bottom: 1px dashed #e5e5e5;}}
.sides {{color: #777; font-size: .85rem; margin-top: 9px;}}
.closed {{color: #999; font-style: italic; padding: 10px 0;}}
.week {{display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px;}}
.day {{background: #fafafa; border-radius: 12px; padding: 10px; font-size: .8rem; color: #333; border: 2px solid transparent;}}
.day.today {{background: #fff; border-color: {tema['accento']}; box-shadow: 0 3px 10px rgba(0,0,0,.08);}}
.day .dn {{font-weight: 800; color: {tema['accento']}; margin-bottom: 4px;}}
.day .it {{padding: 2px 0;}}
.foot {{text-align: center; color: #999; font-size: .78rem; margin-top: 18px;}}
@media (max-width: 640px) {{ .duo, .week {{grid-template-columns: 1fr;}} }}
</style>""", unsafe_allow_html=True)

cambio, nuova_stagione = prossimo_cambio_stagione(oggi)
st.markdown(
    f'<div class="hero"><h1>🍽️ Menù Scuola dell\'infanzia "GIANELLI"</h1>'
    f'<div class="sub">La Valle Agordina (BL)</div>'
    f'<div class="badges">'
    f'<span class="badge">📅 {data_estesa(oggi)} {oggi.year}</span>'
    f'<span class="badge">{tema["icona"]} {stagione}</span>'
    f'<span class="badge">🔁 Settimana {settimana_menu(oggi if oggi.weekday() < 5 else prossimo_giorno_mensa(oggi))} di 4</span>'
    f'</div></div>', unsafe_allow_html=True)

def card(etichetta: str, d: date, colore: str) -> str:
    piatti = piatti_di(d)
    if piatti is None:
        corpo = '<div class="closed">🏖️ Weekend – mensa chiusa</div>'
    else:
        corpo = "".join(f'<div class="dish">🍴 {escape(p)}</div>' for p in piatti)
        corpo += f'<div class="sides">🥗 {CONTORNI[0]} · 🍞 {CONTORNI[1]} · 🍎 {CONTORNI[2]}</div>'
    return (f'<div class="card" style="--c:{colore}"><div class="lbl">{etichetta}</div>'
            f'<div class="dt">{data_estesa(d)}</div>{corpo}</div>')

prossimo = prossimo_giorno_mensa(oggi)
etichetta_prossimo = "Domani" if prossimo == oggi + timedelta(days=1) else "Prossima mensa"
st.markdown(f'<div class="duo">{card("Oggi", oggi, tema["accento"])}'
            f'{card(etichetta_prossimo, prossimo, "#5c6bc0")}</div>', unsafe_allow_html=True)

def griglia_settimana(lun: date) -> str:
    celle = []
    for i in range(5):
        d = lun + timedelta(days=i)
        voci = "".join(f'<div class="it">• {escape(p)}</div>' for p in piatti_di(d))
        classe = "day today" if d == oggi else "day"
        celle.append(f'<div class="{classe}"><div class="dn">{GIORNI[i][:3]} {d.day:02d}/{d.month:02d}</div>{voci}</div>')
    return f'<div class="week">{"".join(celle)}</div>'

st.markdown("#### 📆 Menù settimanale")
lun_base = lunedi_di(oggi if oggi.weekday() < 5 else prossimo)
tab1, tab2 = st.tabs([f"Questa settimana (Sett. {settimana_menu(lun_base)})",
                      f"Prossima settimana (Sett. {settimana_menu(lun_base + timedelta(days=7))})"])
with tab1:
    st.markdown(griglia_settimana(lun_base), unsafe_allow_html=True)
with tab2:
    st.markdown(griglia_settimana(lun_base + timedelta(days=7)), unsafe_allow_html=True)

st.markdown(f'<div class="foot">Contorni ogni giorno: {", ".join(CONTORNI).lower()} · '
            f'Cambio menù → {nuova_stagione} dal {cambio.day} {MESI[cambio.month - 1]} {cambio.year}</div>',
            unsafe_allow_html=True)
