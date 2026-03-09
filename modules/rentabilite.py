"""
TransportCost Pro - Module 2 : Rentabilite par Tournee
Avec sauvegarde Supabase
"""
import streamlit as st
import pandas as pd
from utils.formules import Tournee, calculer_rentabilite_tournee, calculer_seuil_rentabilite
from utils.charts import jauge_marge

def afficher_rentabilite():
    st.markdown('<div style="padding:0.5rem 0 0.3rem;"><div style="font-size:1.5rem;font-weight:700;color:#e2e8f0;">Rentabilite par Tournee</div><div style="font-size:0.88rem;color:#64748b;margin-top:0.3rem;">Analysez la rentabilite de chaque tournee.</div></div>', unsafe_allow_html=True)
    st.divider()

    if "resultat_km" not in st.session_state:
        st.warning("Calculez d abord votre cout kilometrique dans le Calculateur.")
        return

    r_km = st.session_state["resultat_km"]
    user = st.session_state.get("user")

    # Charger historique depuis Supabase si connecte
    if "historique_tournees" not in st.session_state:
        st.session_state["historique_tournees"] = []
        if user:
            try:
                from utils.database import get_tournees
                tournees_db = get_tournees(user["id"])
                for t in tournees_db:
                    st.session_state["historique_tournees"].append({
                        "id": t["id"], "date": t.get("date_tournee", ""),
                        "depart": t.get("depart", ""), "arrivee": t.get("arrivee", ""),
                        "client": t.get("client", ""), "km": float(t.get("km_total", 0)),
                        "prix_facture": float(t.get("prix_facture", 0)),
                        "cout": float(t.get("cout_calcule", 0)),
                        "marge": float(t.get("marge_brute", 0)),
                        "taux_marge": float(t.get("taux_marge", 0)),
                        "indicateur": "🟢" if float(t.get("taux_marge", 0)) > 15 else ("🟡" if float(t.get("taux_marge", 0)) > 5 else ("🟠" if float(t.get("taux_marge", 0)) > 0 else "🔴")),
                        "label": "Tres rentable" if float(t.get("taux_marge", 0)) > 15 else ("Rentable" if float(t.get("taux_marge", 0)) > 5 else ("Seuil critique" if float(t.get("taux_marge", 0)) > 0 else "Non rentable")),
                    })
            except Exception:
                pass

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("CK actif", f"{r_km.ck:.4f} EUR/km")
    with col2:
        st.metric("CC actif", f"{r_km.cc:.2f} EUR/h")
    with col3:
        st.metric("CJ actif", f"{r_km.cj:.2f} EUR/jour")

    st.divider()
    st.markdown('<div class="section-label">Nouvelle tournee</div>', unsafe_allow_html=True)

    with st.form("form_tournee"):
        col1, col2 = st.columns(2)
        with col1:
            date_t = st.date_input("Date")
            depart = st.text_input("Depart", value="Paris")
            arrivee = st.text_input("Arrivee", value="Lyon")
            client = st.text_input("Client", value="")
        with col2:
            km_total = st.number_input("Km total", min_value=1, value=500, step=10)
            km_charge = st.number_input("Km en charge", min_value=1, value=450, step=10)
            nb_heures = st.number_input("Heures de service", min_value=1.0, value=8.0, step=0.5)
            nb_jours = st.number_input("Jours", min_value=1.0, value=1.0, step=0.5)

        col1, col2, col3 = st.columns(3)
        with col1:
            prix_facture = st.number_input("Prix facture (EUR HT)", min_value=0.0, value=800.0, step=50.0)
        with col2:
            peages_t = st.number_input("Peages (EUR)", min_value=0.0, value=50.0, step=5.0)
        with col3:
            frais_dep = st.number_input("Frais deplacement (EUR)", min_value=0.0, value=30.0, step=5.0)

        submitted = st.form_submit_button("Analyser cette tournee", use_container_width=True, type="primary")

    if submitted:
        tournee = Tournee(
            date_tournee=str(date_t), depart=depart, arrivee=arrivee,
            km_total=km_total, km_en_charge=km_charge,
            nb_heures=nb_heures, nb_jours=nb_jours,
            prix_facture=prix_facture, peages=peages_t,
            frais_deplacement=frais_dep, client=client,
        )
        res = calculer_rentabilite_tournee(tournee, r_km)

        entry = {
            "date": str(date_t), "depart": depart, "arrivee": arrivee,
            "client": client, "km": km_total, "prix_facture": prix_facture,
            "cout": round(res.cout_tournee, 2), "marge": round(res.marge_brute, 2),
            "taux_marge": round(res.taux_marge, 1), "indicateur": res.indicateur,
            "label": res.label,
        }

        # Sauvegarder dans Supabase
        if user:
            try:
                from utils.database import sauvegarder_tournee
                saved = sauvegarder_tournee(user["id"], None, tournee, res)
                if saved:
                    entry["id"] = saved["id"]
                st.toast("Tournee sauvegardee !", icon="✅")
            except Exception as e:
                st.toast(f"Erreur: {e}", icon="⚠️")

        st.session_state["historique_tournees"].append(entry)

        st.divider()
        st.markdown('<div class="section-label">Resultat de la tournee</div>', unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Cout de la tournee", f"{res.cout_tournee:,.2f} EUR")
        with col2:
            st.metric("Marge brute", f"{res.marge_brute:,.2f} EUR")
        with col3:
            st.metric("Taux de marge", f"{res.taux_marge:.1f} %")
        with col4:
            color_map = {"Tres rentable": "#2ecc71", "Rentable": "#f1c40f", "Seuil critique": "#e67e22", "Non rentable": "#e74c3c"}
            c = color_map.get(res.label, "#94a3b8")
            st.markdown(f'<div style="text-align:center;padding-top:0.5rem;"><div style="font-size:2rem;">{res.indicateur}</div><div style="font-size:0.85rem;color:{c};font-weight:600;">{res.label}</div></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Revenu par km", f"{res.revenu_par_km:.3f} EUR/km")
        with col2:
            st.metric("Cout par km", f"{res.cout_par_km:.3f} EUR/km")
        with col3:
            st.metric("Marge par km", f"{res.marge_par_km:.3f} EUR/km")

        with st.expander("Detail du calcul"):
            cout_ck = r_km.ck * km_total
            cout_cc = r_km.cc * nb_heures
            cout_cj = r_km.cj * nb_jours
            st.markdown(f"""
| Poste | Calcul | Montant |
|:------|:-------|--------:|
| CK x km | {r_km.ck:.4f} x {km_total} | {cout_ck:,.2f} EUR |
| CC x heures | {r_km.cc:.2f} x {nb_heures} | {cout_cc:,.2f} EUR |
| CJ x jours | {r_km.cj:.2f} x {nb_jours} | {cout_cj:,.2f} EUR |
| Peages | | {peages_t:,.2f} EUR |
| Frais deplacement | | {frais_dep:,.2f} EUR |
| **Cout total** | | **{res.cout_tournee:,.2f} EUR** |
| **Marge** | | **{res.marge_brute:,.2f} EUR** |
            """)

    if st.session_state["historique_tournees"]:
        st.divider()
        st.markdown('<div class="section-label">Historique des tournees</div>', unsafe_allow_html=True)
        df = pd.DataFrame(st.session_state["historique_tournees"])
        nb = len(df)
        marge_moy = df["taux_marge"].mean()
        marge_tot = df["marge"].sum()
        ca_tot = df["prix_facture"].sum()

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Tournees", nb)
        with col2:
            st.metric("Marge moyenne", f"{marge_moy:.1f} %")
        with col3:
            st.metric("Marge totale", f"{marge_tot:,.2f} EUR")
        with col4:
            st.metric("CA total", f"{ca_tot:,.2f} EUR")

        display_df = df[["date", "depart", "arrivee", "client", "km", "prix_facture", "cout", "marge", "taux_marge", "indicateur"]].copy()
        display_df.columns = ["Date", "Depart", "Arrivee", "Client", "Km", "Facture", "Cout", "Marge", "Marge %", "Status"]
        st.dataframe(display_df, use_container_width=True, hide_index=True)

        st.divider()
        st.markdown('<div class="section-label">Seuil de rentabilite</div>', unsafe_allow_html=True)
        resultats_list = []
        prix_list = []
        for h in st.session_state["historique_tournees"]:
            t = Tournee(km_total=h["km"], km_en_charge=h["km"], nb_heures=8, nb_jours=1, prix_facture=h["prix_facture"])
            res_t = calculer_rentabilite_tournee(t, r_km)
            resultats_list.append(res_t)
            prix_list.append(h["prix_facture"])

        seuil = calculer_seuil_rentabilite(r_km.total_couts_fixes, resultats_list, prix_list)
        col1, col2 = st.columns(2)
        with col1:
            val = seuil["nb_tournees_seuil_mensuel"]
            st.metric("Tournees minimum / mois", f"{val:.0f}" if val != float('inf') else "N/A")
        with col2:
            val2 = seuil["ca_seuil_annuel"]
            st.metric("CA seuil annuel", f"{val2:,.0f} EUR" if val2 != float('inf') else "N/A")

        if st.button("Reinitialiser l historique"):
            st.session_state["historique_tournees"] = []
            st.rerun()
