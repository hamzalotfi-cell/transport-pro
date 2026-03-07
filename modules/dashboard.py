"""
TransportPro — Module 3 : Tableau de Bord Financier
Module payant : vision consolidée de la santé financière.
"""

import streamlit as st


def afficher_dashboard():
    """Affiche l'interface du tableau de bord financier."""

    st.markdown(
        """
        <div style="text-align: center; padding: 1rem 0;">
            <h1 style="color: #1B6EC2; margin-bottom: 0.2rem;">
                💼 Tableau de Bord Financier
            </h1>
            <p style="color: #aaa; font-size: 1.1rem;">
                Vision complète de la santé financière de votre entreprise
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.info(
        "🔒 **Module Pro** — Ce module sera disponible avec l'abonnement Pro (49€/mois). "
        "Il vous offrira :\n\n"
        "- **FRNG, BFR, Trésorerie nette** — L'équilibre financier en un coup d'œil\n"
        "- **Ratios de rentabilité** — Marge d'exploitation, rentabilité nette, ROE\n"
        "- **Ratios de structure** — Endettement, autonomie financière\n"
        "- **Ratios de liquidité** — Capacité à payer vos dettes court terme\n"
        "- **DSO / DPO** — Délais de paiement clients et fournisseurs\n"
        "- **CAF** — Capacité d'autofinancement\n"
        "- **KPIs par camion** — CA, coût et marge par véhicule\n"
        "- **Alertes automatiques** — Notifications quand un indicateur est dans le rouge"
    )

    # Preview visuelle
    st.markdown("---")
    st.subheader("🔍 Aperçu des indicateurs")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Trésorerie Nette", "— €", help="Disponible avec l'abonnement Pro")
    with col2:
        st.metric("Marge d'exploitation", "— %", help="Benchmark secteur : 2-3%")
    with col3:
        st.metric("DSO (délai paiement)", "— jours", help="Légal : 30 jours max")
    with col4:
        st.metric("Seuil de rentabilité", "⏳", help="Progression vers le point mort")

    st.markdown(
        """
        ---
        *Le secteur du transport routier opère avec des marges de 2-3%.
        Ce tableau de bord vous permet de piloter votre entreprise avec la même
        rigueur financière que les grands groupes, mais adapté à votre taille.*
        """
    )
