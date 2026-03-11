"""
TransportCost Pro - Module 1 : Calculateur
Avec immatriculation + sauvegarde Supabase
"""
import streamlit as st
from utils.formules import ProfilVehicule, calculer_cout_km
from utils.charts import camembert_couts, barres_detail_couts, graphique_trinome

DEFAULTS = {
    "Fourgon (3.5T)": {"prix_achat": 35000, "duree_amort": 5, "val_residuelle": 8000, "km_annuel": 60000, "conso": 12.0, "assurance": 2500, "taxe_essieu": 0, "ct": 200, "pneus": 800, "entretien": 2000},
    "Porteur (19T)": {"prix_achat": 80000, "duree_amort": 7, "val_residuelle": 15000, "km_annuel": 80000, "conso": 25.0, "assurance": 4500, "taxe_essieu": 300, "ct": 350, "pneus": 2500, "entretien": 5000},
    "Semi-remorque (40T)": {"prix_achat": 120000, "duree_amort": 8, "val_residuelle": 20000, "km_annuel": 120000, "conso": 33.0, "assurance": 6000, "taxe_essieu": 600, "ct": 500, "pneus": 4500, "entretien": 8000},
    "Personnalise": {"prix_achat": 0, "duree_amort": 5, "val_residuelle": 0, "km_annuel": 100000, "conso": 30.0, "assurance": 0, "taxe_essieu": 0, "ct": 0, "pneus": 0, "entretien": 0},
}

def afficher_calculateur():
    st.markdown('<div style="padding:0.5rem 0 0.3rem;"><div style="font-size:1.5rem;font-weight:700;color:#f1f5f9;">Calculateur de Cout Kilometrique</div><div style="font-size:0.88rem;color:#94a3b8;margin-top:0.3rem;">Calculez votre cout reel au km et le prix minimum a facturer.</div></div>', unsafe_allow_html=True)
    st.divider()

    user = st.session_state.get("user")
    if user:
        try:
            from utils.database import get_vehicules
            vehicules_sauv = get_vehicules(user["id"])
            if vehicules_sauv:
                st.markdown('<div class="section-label">Vos vehicules sauvegardes</div>', unsafe_allow_html=True)
                for v in vehicules_sauv:
                    col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
                    with col1:
                        immat = v.get("immatriculation", "")
                        nom = v.get("nom", "Vehicule")
                        st.markdown(f'<div style="font-size:0.9rem;color:#f1f5f9;font-weight:600;">{nom}</div>', unsafe_allow_html=True)
                    with col2:
                        if immat:
                            st.markdown(f'<div style="font-family:JetBrains Mono,monospace;font-size:0.85rem;color:#f59e0b;font-weight:600;background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.2);border-radius:6px;padding:0.2rem 0.6rem;display:inline-block;">{immat}</div>', unsafe_allow_html=True)
                    with col3:
                        st.markdown(f'<div style="font-size:0.82rem;color:#94a3b8;">{v.get("km_annuel", 0):,} km/an</div>', unsafe_allow_html=True)
                    with col4:
                        if st.button("Charger", key=f'load_{v["id"]}'):
                            charger_vehicule(v)
                            st.rerun()
                st.divider()
        except Exception:
            pass

    type_vehicule = st.selectbox("Type de vehicule", list(DEFAULTS.keys()), index=2)
    d = DEFAULTS[type_vehicule]

    with st.form("form_calculateur"):
        st.markdown('<div class="section-label">Identification du vehicule</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            nom_vehicule = st.text_input("Nom du vehicule", value=type_vehicule, help="Ex: Camion 1, Renault T480...")
        with col2:
            immatriculation = st.text_input("Plaque d immatriculation", value="", placeholder="AA-123-BB", help="Pour identifier facilement ce vehicule")

        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Donnees du vehicule</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            prix_achat = st.number_input("Prix d achat (EUR)", min_value=0, value=d["prix_achat"], step=1000)
            duree_amort = st.number_input("Amortissement (annees)", min_value=1, max_value=20, value=d["duree_amort"])
        with col2:
            val_residuelle = st.number_input("Valeur residuelle (EUR)", min_value=0, value=d["val_residuelle"], step=500)
            km_annuel = st.number_input("Kilometrage annuel (km)", min_value=1000, value=d["km_annuel"], step=5000)
        with col3:
            conso = st.number_input("Consommation (L/100km)", min_value=1.0, value=d["conso"], step=0.5)
            prix_carburant = st.number_input("Prix gazole (EUR/L)", min_value=0.50, value=1.55, step=0.05)

        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Couts fixes annuels</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            assurance = st.number_input("Assurance (EUR/an)", min_value=0, value=d["assurance"], step=100)
            taxe_essieu = st.number_input("Taxe a l essieu (EUR/an)", min_value=0, value=d["taxe_essieu"], step=50)
        with col2:
            ct = st.number_input("Controle technique (EUR/an)", min_value=0, value=d["ct"], step=50)
            parking = st.number_input("Parking (EUR/an)", min_value=0, value=0, step=100)
        with col3:
            credit = st.number_input("Credit / leasing (EUR/mois)", min_value=0, value=0, step=50)
            salaire_brut = st.number_input("Salaire conducteur brut (EUR/mois)", min_value=0, value=2200, step=100)
        charges_sociales = st.number_input("Charges sociales (%)", min_value=0.0, value=45.0, step=1.0)

        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Frais de structure</div>', unsafe_allow_html=True)
        mode_structure = st.radio("Mode de saisie", ["Montant global", "Saisie detaillee"], horizontal=True)
        if mode_structure == "Montant global":
            frais_structure = st.number_input("Frais de structure (EUR/an)", min_value=0, value=0, step=500)
        else:
            col1, col2 = st.columns(2)
            with col1:
                fs_loyer = st.number_input("Loyer (EUR/an)", min_value=0, value=0, step=100, key="fs1")
                fs_comptable = st.number_input("Comptable (EUR/an)", min_value=0, value=0, step=100, key="fs2")
                fs_tel = st.number_input("Telephone (EUR/an)", min_value=0, value=0, step=50, key="fs3")
                fs_log = st.number_input("Logiciels (EUR/an)", min_value=0, value=0, step=50, key="fs4")
            with col2:
                fs_rc = st.number_input("RC pro (EUR/an)", min_value=0, value=0, step=100, key="fs5")
                fs_four = st.number_input("Fournitures (EUR/an)", min_value=0, value=0, step=50, key="fs6")
                fs_form = st.number_input("Formation FIMO (EUR/an)", min_value=0, value=0, step=100, key="fs7")
                fs_div = st.number_input("Divers (EUR/an)", min_value=0, value=0, step=50, key="fs8")
            frais_structure = fs_loyer + fs_comptable + fs_tel + fs_log + fs_rc + fs_four + fs_form + fs_div

        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Couts variables annuels</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            pneus = st.number_input("Pneumatiques (EUR/an)", min_value=0, value=d["pneus"], step=100)
        with col2:
            entretien = st.number_input("Entretien (EUR/an)", min_value=0, value=d["entretien"], step=500)
        with col3:
            peages = st.number_input("Peages (EUR/an)", min_value=0, value=12000, step=500)

        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Parametres d exploitation</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            jours_exploit = st.number_input("Jours / an", min_value=50, max_value=365, value=220)
        with col2:
            heures_jour = st.number_input("Heures / jour", min_value=1.0, max_value=15.0, value=8.0, step=0.5)
        with col3:
            taux_vide = st.number_input("Retours a vide (%)", min_value=0.0, max_value=80.0, value=20.0, step=1.0)
        marge = st.slider("Marge souhaitee (%)", min_value=0, max_value=50, value=10)

        submitted = st.form_submit_button("Calculer le cout kilometrique", use_container_width=True, type="primary")

    if submitted:
        profil = ProfilVehicule(
            nom=nom_vehicule, type_vehicule=type_vehicule,
            prix_achat=prix_achat, duree_amortissement=duree_amort,
            valeur_residuelle=val_residuelle, km_annuel=km_annuel,
            assurance=assurance, taxe_essieu=taxe_essieu,
            controle_technique=ct, parking_stationnement=parking,
            credit_mensualite=credit, salaire_conducteur_brut=salaire_brut,
            charges_sociales_pct=charges_sociales, frais_structure=frais_structure,
            conso_carburant=conso, prix_carburant=prix_carburant,
            cout_pneumatiques=pneus, cout_entretien_reparation=entretien,
            cout_peages_annuel=peages, jours_exploitation=jours_exploit,
            heures_conduite_jour=heures_jour, taux_retour_vide=taux_vide,
            marge_souhaitee=marge,
        )
        resultat = calculer_cout_km(profil)
        st.session_state["profil_vehicule"] = profil
        st.session_state["resultat_km"] = resultat
        st.session_state["immatriculation"] = immatriculation

        if user:
            try:
                from utils.database import sauvegarder_vehicule
                sauvegarder_vehicule(user["id"], profil, immatriculation)
                st.toast("Vehicule sauvegarde !", icon="✅")
            except Exception as e:
                st.toast(f"Erreur: {e}", icon="⚠️")

        afficher_resultats(resultat, profil, immatriculation)


def charger_vehicule(v):
    profil = ProfilVehicule(
        nom=v.get("nom", ""), type_vehicule=v.get("type_vehicule", ""),
        prix_achat=float(v.get("prix_achat", 0)), duree_amortissement=int(v.get("duree_amortissement", 5)),
        valeur_residuelle=float(v.get("valeur_residuelle", 0)), km_annuel=int(v.get("km_annuel", 100000)),
        assurance=float(v.get("assurance", 0)), taxe_essieu=float(v.get("taxe_essieu", 0)),
        controle_technique=float(v.get("controle_technique", 0)), parking_stationnement=float(v.get("parking", 0)),
        credit_mensualite=float(v.get("credit_mensualite", 0)), salaire_conducteur_brut=float(v.get("salaire_brut", 0)),
        charges_sociales_pct=float(v.get("charges_sociales_pct", 45)), frais_structure=float(v.get("frais_structure", 0)),
        conso_carburant=float(v.get("conso_carburant", 33)), prix_carburant=float(v.get("prix_carburant", 1.55)),
        cout_pneumatiques=float(v.get("pneus", 0)), cout_entretien_reparation=float(v.get("entretien", 0)),
        cout_peages_annuel=float(v.get("peages", 0)), jours_exploitation=int(v.get("jours_exploitation", 220)),
        heures_conduite_jour=float(v.get("heures_conduite", 8)), taux_retour_vide=float(v.get("taux_retour_vide", 20)),
        marge_souhaitee=float(v.get("marge_souhaitee", 10)),
    )
    resultat = calculer_cout_km(profil)
    st.session_state["profil_vehicule"] = profil
    st.session_state["resultat_km"] = resultat
    st.session_state["immatriculation"] = v.get("immatriculation", "")


def afficher_resultats(r, profil, immat=""):
    st.divider()
    titre = f"{profil.nom}"
    if immat:
        titre += f" — {immat}"
    st.markdown(f'<div style="text-align:center;margin-bottom:1rem;"><div style="font-size:0.72rem;text-transform:uppercase;letter-spacing:0.12em;color:#94a3b8;font-weight:600;">Resultats</div><div style="font-family:JetBrains Mono,monospace;font-size:0.95rem;color:#f59e0b;margin-top:0.3rem;">{titre}</div></div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Cout brut / km", f"{r.cout_km_brut:.3f} EUR")
    with col2:
        delta_pct = ((r.cout_km_reel / r.cout_km_brut - 1) * 100) if r.cout_km_brut > 0 else 0
        st.metric("Cout reel / km", f"{r.cout_km_reel:.3f} EUR", delta=f"+{delta_pct:.0f}% retours a vide", delta_color="inverse")
    with col3:
        st.metric("Prix min. / km", f"{r.prix_min_km:.3f} EUR")
    with col4:
        st.metric("Cout journalier", f"{r.cout_journalier:.0f} EUR")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Couts fixes", f"{r.total_couts_fixes:,.0f} EUR")
    with col2:
        st.metric("Couts variables", f"{r.total_couts_variables:,.0f} EUR")
    with col3:
        st.metric("Cout total annuel", f"{r.cout_total_annuel:,.0f} EUR")

    st.divider()
    col_left, col_right = st.columns(2)
    with col_left:
        st.plotly_chart(camembert_couts(r.detail_fixes, r.detail_variables), use_container_width=True)
    with col_right:
        st.plotly_chart(graphique_trinome(r.ck, r.cc, r.cj), use_container_width=True)
    st.plotly_chart(barres_detail_couts(r.detail_fixes, r.detail_variables), use_container_width=True)

    st.divider()
    st.markdown('<div class="section-label">Formule Trinome CNR</div>', unsafe_allow_html=True)
    st.markdown(f'<div style="background:rgba(30,41,59,0.5);border:1px solid rgba(59,130,246,0.1);border-radius:10px;padding:1.5rem;"><div style="font-family:JetBrains Mono,monospace;font-size:0.95rem;color:#f1f5f9;text-align:center;margin-bottom:1.2rem;">Prix = CK x km + CC x heures + CJ x jours</div><div style="display:flex;justify-content:space-around;text-align:center;"><div><div style="font-size:0.7rem;color:#94a3b8;text-transform:uppercase;">CK</div><div style="font-family:JetBrains Mono,monospace;font-size:1.3rem;color:#f59e0b;font-weight:600;">{r.ck:.4f} EUR/km</div></div><div><div style="font-size:0.7rem;color:#94a3b8;text-transform:uppercase;">CC</div><div style="font-family:JetBrains Mono,monospace;font-size:1.3rem;color:#3b82f6;font-weight:600;">{r.cc:.2f} EUR/h</div></div><div><div style="font-size:0.7rem;color:#94a3b8;text-transform:uppercase;">CJ</div><div style="font-family:JetBrains Mono,monospace;font-size:1.3rem;color:#60a5fa;font-weight:600;">{r.cj:.2f} EUR/jour</div></div></div></div>', unsafe_allow_html=True)

    st.divider()
    st.markdown('<div class="section-label">Simulateur rapide</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        sim_km = st.number_input("Kilometres", min_value=1, value=500, step=50, key="sim_km")
    with col2:
        sim_h = st.number_input("Heures", min_value=1.0, value=8.0, step=0.5, key="sim_h")
    with col3:
        sim_j = st.number_input("Jours", min_value=1.0, value=1.0, step=0.5, key="sim_j")
    cout_sim = r.ck * sim_km + r.cc * sim_h + r.cj * sim_j
    prix_sim = cout_sim * (1 + profil.marge_souhaitee / 100)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Cout estime", f"{cout_sim:,.2f} EUR")
    with col2:
        st.metric(f"Prix min. ({profil.marge_souhaitee:.0f}% marge)", f"{prix_sim:,.2f} EUR")
