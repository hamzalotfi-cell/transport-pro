"""
TransportPro — Module 1 : Calculateur de Coût Kilométrique
Outil gratuit permettant de calculer le coût réel au km d'un véhicule.
"""

import streamlit as st
from utils.formules import ProfilVehicule, calculer_cout_km
from utils.charts import (
    camembert_couts,
    barres_detail_couts,
    graphique_trinome,
)


# Valeurs par défaut selon le type de véhicule
DEFAULTS = {
    "Fourgon (3.5T)": {
        "prix_achat": 35000, "duree_amort": 5, "val_residuelle": 8000,
        "km_annuel": 60000, "conso": 12.0,
        "assurance": 2500, "taxe_essieu": 0, "ct": 200,
        "pneus": 800, "entretien": 2000,
    },
    "Porteur (19T)": {
        "prix_achat": 80000, "duree_amort": 7, "val_residuelle": 15000,
        "km_annuel": 80000, "conso": 25.0,
        "assurance": 4500, "taxe_essieu": 300, "ct": 350,
        "pneus": 2500, "entretien": 5000,
    },
    "Semi-remorque (40T)": {
        "prix_achat": 120000, "duree_amort": 8, "val_residuelle": 20000,
        "km_annuel": 120000, "conso": 33.0,
        "assurance": 6000, "taxe_essieu": 600, "ct": 500,
        "pneus": 4500, "entretien": 8000,
    },
    "Personnalisé": {
        "prix_achat": 0, "duree_amort": 5, "val_residuelle": 0,
        "km_annuel": 100000, "conso": 30.0,
        "assurance": 0, "taxe_essieu": 0, "ct": 0,
        "pneus": 0, "entretien": 0,
    },
}


def afficher_calculateur():
    """Affiche l'interface complète du calculateur de coût/km."""

    st.markdown(
        """
        <div style="text-align: center; padding: 1rem 0;">
            <h1 style="color: #1B6EC2; margin-bottom: 0.2rem;">
                🚛 Calculateur de Coût Kilométrique
            </h1>
            <p style="color: #aaa; font-size: 1.1rem;">
                Calculez votre coût réel au km et le prix minimum à facturer
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ------- Choix du type de véhicule -------
    type_vehicule = st.selectbox(
        "Type de véhicule",
        list(DEFAULTS.keys()),
        index=2,
        help="Sélectionnez un type pour pré-remplir les valeurs par défaut, ou 'Personnalisé' pour tout saisir.",
    )
    d = DEFAULTS[type_vehicule]

    # ------- Formulaire de saisie -------
    with st.form("form_calculateur"):

        # --- Section 1 : Données véhicule ---
        st.subheader("🚚 Données du véhicule")
        col1, col2, col3 = st.columns(3)
        with col1:
            prix_achat = st.number_input(
                "Prix d'achat (€)", min_value=0, value=d["prix_achat"], step=1000
            )
            duree_amort = st.number_input(
                "Durée d'amortissement (années)", min_value=1, max_value=20, value=d["duree_amort"]
            )
        with col2:
            val_residuelle = st.number_input(
                "Valeur résiduelle (€)", min_value=0, value=d["val_residuelle"], step=500
            )
            km_annuel = st.number_input(
                "Kilométrage annuel (km)", min_value=1000, value=d["km_annuel"], step=5000
            )
        with col3:
            conso = st.number_input(
                "Consommation (L/100km)", min_value=1.0, value=d["conso"], step=0.5
            )
            prix_carburant = st.number_input(
                "Prix du gazole (€/L)", min_value=0.50, value=1.55, step=0.05
            )

        st.divider()

        # --- Section 2 : Coûts fixes ---
        st.subheader("📌 Coûts fixes annuels")
        col1, col2, col3 = st.columns(3)
        with col1:
            assurance = st.number_input(
                "Assurance (€/an)", min_value=0, value=d["assurance"], step=100
            )
            taxe_essieu = st.number_input(
                "Taxe à l'essieu (€/an)", min_value=0, value=d["taxe_essieu"], step=50
            )
            ct = st.number_input(
                "Contrôle technique (€/an)", min_value=0, value=d["ct"], step=50
            )
        with col2:
            parking = st.number_input(
                "Parking / Stationnement (€/an)", min_value=0, value=0, step=100
            )
            credit = st.number_input(
                "Mensualité crédit / leasing (€/mois)", min_value=0, value=0, step=50
            )
            frais_structure = st.number_input(
                "Frais de structure (€/an)",
                min_value=0, value=0, step=500,
                help="Loyer bureau, comptable, téléphone, etc. (quote-part par véhicule)"
            )
        with col3:
            salaire_brut = st.number_input(
                "Salaire conducteur brut (€/mois)", min_value=0, value=2200, step=100
            )
            charges_sociales = st.number_input(
                "Charges sociales patronales (%)", min_value=0.0, value=45.0, step=1.0
            )

        st.divider()

        # --- Section 3 : Coûts variables ---
        st.subheader("🔧 Coûts variables annuels")
        col1, col2, col3 = st.columns(3)
        with col1:
            pneus = st.number_input(
                "Pneumatiques (€/an)", min_value=0, value=d["pneus"], step=100
            )
        with col2:
            entretien = st.number_input(
                "Entretien / Réparation (€/an)", min_value=0, value=d["entretien"], step=500
            )
        with col3:
            peages = st.number_input(
                "Péages (€/an)", min_value=0, value=12000, step=500
            )

        st.divider()

        # --- Section 4 : Paramètres d'exploitation ---
        st.subheader("⚙️ Paramètres d'exploitation")
        col1, col2, col3 = st.columns(3)
        with col1:
            jours_exploit = st.number_input(
                "Jours d'exploitation / an", min_value=50, max_value=365, value=220
            )
        with col2:
            heures_jour = st.number_input(
                "Heures de conduite / jour", min_value=1.0, max_value=15.0, value=8.0, step=0.5
            )
        with col3:
            taux_vide = st.number_input(
                "Taux de retour à vide (%)", min_value=0.0, max_value=80.0, value=20.0, step=1.0
            )

        marge = st.slider(
            "Marge bénéficiaire souhaitée (%)", min_value=0, max_value=50, value=10
        )

        submitted = st.form_submit_button(
            "📊 Calculer mon coût kilométrique",
            use_container_width=True,
            type="primary",
        )

    # ------- Calcul et affichage des résultats -------
    if submitted:
        profil = ProfilVehicule(
            nom=type_vehicule,
            type_vehicule=type_vehicule,
            prix_achat=prix_achat,
            duree_amortissement=duree_amort,
            valeur_residuelle=val_residuelle,
            km_annuel=km_annuel,
            assurance=assurance,
            taxe_essieu=taxe_essieu,
            controle_technique=ct,
            parking_stationnement=parking,
            credit_mensualite=credit,
            salaire_conducteur_brut=salaire_brut,
            charges_sociales_pct=charges_sociales,
            frais_structure=frais_structure,
            conso_carburant=conso,
            prix_carburant=prix_carburant,
            cout_pneumatiques=pneus,
            cout_entretien_reparation=entretien,
            cout_peages_annuel=peages,
            jours_exploitation=jours_exploit,
            heures_conduite_jour=heures_jour,
            taux_retour_vide=taux_vide,
            marge_souhaitee=marge,
        )

        # Stocker le profil et le résultat en session
        resultat = calculer_cout_km(profil)
        st.session_state["profil_vehicule"] = profil
        st.session_state["resultat_km"] = resultat

        afficher_resultats(resultat, profil)


def afficher_resultats(r, profil):
    """Affiche les résultats du calcul."""

    st.markdown("---")
    st.markdown(
        "<h2 style='text-align: center; color: #1B6EC2;'>📊 Résultats</h2>",
        unsafe_allow_html=True,
    )

    # --- KPIs principaux ---
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Coût brut / km",
            value=f"{r.cout_km_brut:.3f} €",
            help="Coût total annuel divisé par le kilométrage annuel",
        )
    with col2:
        st.metric(
            label="Coût réel / km",
            value=f"{r.cout_km_reel:.3f} €",
            delta=f"+{((r.cout_km_reel / r.cout_km_brut - 1) * 100):.0f}% (retours à vide)" if r.cout_km_brut > 0 else None,
            delta_color="inverse",
            help=f"Corrigé avec {profil.taux_retour_vide:.0f}% de retours à vide",
        )
    with col3:
        st.metric(
            label="💰 Prix minimum / km",
            value=f"{r.prix_min_km:.3f} €",
            help=f"Avec {profil.marge_souhaitee:.0f}% de marge incluse",
        )
    with col4:
        st.metric(
            label="Coût journalier",
            value=f"{r.cout_journalier:.0f} €",
            help="Coût total annuel divisé par le nombre de jours d'exploitation",
        )

    st.markdown("")

    # --- Deuxième ligne : totaux ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Coûts fixes annuels", f"{r.total_couts_fixes:,.0f} €")
    with col2:
        st.metric("Coûts variables annuels", f"{r.total_couts_variables:,.0f} €")
    with col3:
        st.metric("🏷️ Coût total annuel", f"{r.cout_total_annuel:,.0f} €")

    st.markdown("---")

    # --- Graphiques ---
    col_left, col_right = st.columns(2)

    with col_left:
        fig_pie = camembert_couts(r.detail_fixes, r.detail_variables)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_right:
        fig_trinome = graphique_trinome(r.ck, r.cc, r.cj)
        st.plotly_chart(fig_trinome, use_container_width=True)

    # --- Barres détaillées ---
    fig_bars = barres_detail_couts(r.detail_fixes, r.detail_variables)
    st.plotly_chart(fig_bars, use_container_width=True)

    # --- Trinôme CNR texte ---
    st.markdown("---")
    st.subheader("📐 Formule Trinôme CNR")
    st.markdown(
        f"""
        La méthode officielle du **Comité National Routier** décompose le coût en 3 termes :

        > **Prix transport = CK × km + CC × heures + CJ × jours**

        | Composante | Valeur | Description |
        |:-----------|-------:|:------------|
        | **CK** (Coût Kilométrique) | **{r.ck:.4f} €/km** | Carburant, pneus, entretien, péages |
        | **CC** (Coût Conducteur) | **{r.cc:.2f} €/h** | Salaire + charges par heure |
        | **CJ** (Coût Journalier) | **{r.cj:.2f} €/jour** | Amortissement, assurance, structure |

        **Exemple** : une tournée de 500 km, 8 heures, 1 jour =
        **{r.ck * 500 + r.cc * 8 + r.cj * 1:,.2f} €** de coût.
        """
    )

    # --- Simulateur rapide ---
    st.markdown("---")
    st.subheader("🧮 Simulateur rapide de tournée")
    st.markdown("*Utilisez la formule trinôme pour estimer rapidement le coût d'une tournée.*")

    col1, col2, col3 = st.columns(3)
    with col1:
        sim_km = st.number_input("Kilomètres", min_value=1, value=500, step=50, key="sim_km")
    with col2:
        sim_heures = st.number_input("Heures de service", min_value=1.0, value=8.0, step=0.5, key="sim_h")
    with col3:
        sim_jours = st.number_input("Jours", min_value=1.0, value=1.0, step=0.5, key="sim_j")

    cout_sim = r.ck * sim_km + r.cc * sim_heures + r.cj * sim_jours
    prix_min_sim = cout_sim * (1 + profil.marge_souhaitee / 100)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Coût estimé de la tournée", f"{cout_sim:,.2f} €")
    with col2:
        st.metric(
            f"Prix minimum à facturer ({profil.marge_souhaitee:.0f}% marge)",
            f"{prix_min_sim:,.2f} €",
        )
