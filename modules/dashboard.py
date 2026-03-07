"""
TransportPro - Module 3 : Dashboard Financier
Version accessible pour les transporteurs sans formation finance.
"""
import streamlit as st
from utils.formules import BilanSimplif, analyser_bilan
from utils.charts import waterfall_equilibre


def badge(text, color):
    bg = {"vert": "rgba(46,204,113,0.15)", "orange": "rgba(230,126,34,0.15)", "rouge": "rgba(231,76,60,0.15)"}
    fg = {"vert": "#2ecc71", "orange": "#e67e22", "rouge": "#e74c3c"}
    border = {"vert": "rgba(46,204,113,0.3)", "orange": "rgba(230,126,34,0.3)", "rouge": "rgba(231,76,60,0.3)"}
    return f'<span style="display:inline-block;padding:0.2rem 0.6rem;border-radius:4px;font-size:0.75rem;font-weight:600;font-family:DM Sans,sans-serif;background:{bg[color]};color:{fg[color]};border:1px solid {border[color]};">{text}</span>'


def indicateur_card(titre, valeur, explication, couleur, conseil=""):
    colors = {"vert": "#2ecc71", "orange": "#e67e22", "rouge": "#e74c3c"}
    border_colors = {"vert": "rgba(46,204,113,0.4)", "orange": "rgba(230,126,34,0.4)", "rouge": "rgba(231,76,60,0.4)"}
    bg = {"vert": "rgba(46,204,113,0.05)", "orange": "rgba(230,126,34,0.05)", "rouge": "rgba(231,76,60,0.05)"}
    icone = {"vert": "&#10003;", "orange": "&#9888;", "rouge": "&#10007;"}
    conseil_html = f'<div style="font-size:0.78rem;color:{colors[couleur]};margin-top:0.5rem;font-weight:500;">&#10140; {conseil}</div>' if conseil else ""

    st.markdown(f"""
    <div style="border:1px solid {border_colors[couleur]};border-left:4px solid {colors[couleur]};border-radius:8px;padding:1.2rem;background:{bg[couleur]};margin-bottom:0.8rem;">
        <div style="display:flex;justify-content:space-between;align-items:center;">
            <div style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;color:#94a3b8;font-weight:600;">{titre}</div>
            <div style="font-size:1rem;color:{colors[couleur]};">{icone[couleur]}</div>
        </div>
        <div style="font-family:JetBrains Mono,monospace;font-size:1.5rem;font-weight:700;color:#e2e8f0;margin:0.4rem 0;">{valeur}</div>
        <div style="font-size:0.82rem;color:#94a3b8;line-height:1.5;">{explication}</div>
        {conseil_html}
    </div>
    """, unsafe_allow_html=True)


def afficher_dashboard():
    st.markdown('<div style="padding:0.5rem 0 0.3rem;"><div style="font-size:1.5rem;font-weight:700;color:#e2e8f0;">Dashboard Financier</div><div style="font-size:0.88rem;color:#64748b;margin-top:0.3rem;">La sante financiere de votre entreprise, expliquee simplement.</div></div>', unsafe_allow_html=True)
    st.divider()

    # GUIDE
    with st.expander("Comment remplir ce formulaire ?"):
        st.markdown("""
**Pas de panique, c est plus simple qu il n y parait !**

Prenez votre dernier bilan comptable (celui que votre expert-comptable vous a remis) et reportez les chiffres dans les cases ci-dessous.

- **Immobilisations nettes** = la valeur actuelle de vos camions et equipements (apres amortissement)
- **Stocks** = pieces de rechange, pneus en stock, etc.
- **Creances clients** = les factures que vous avez envoyees mais pas encore encaissees
- **Tresorerie** = ce que vous avez sur votre compte en banque
- **Capitaux propres** = votre apport + les benefices accumules depuis la creation
- **Dettes long terme** = vos credits vehicules, emprunts bancaires
- **Dettes fournisseurs** = ce que vous devez a vos fournisseurs (gazole, garage, etc.)
- **Dettes fiscales/sociales** = ce que vous devez aux impots et a l URSSAF

*Si vous ne connaissez pas un chiffre, laissez la valeur par defaut et ajustez plus tard.*
        """)

    with st.form("form_bilan"):
        st.markdown('<div class="section-label">Ce que vous possedez (Actif)</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            immo = st.number_input("Vehicules et equipements (EUR)", min_value=0, value=200000, step=5000, help="Valeur nette apres amortissement de vos camions")
        with col2:
            stocks = st.number_input("Stocks pieces/pneus (EUR)", min_value=0, value=5000, step=500)
        with col3:
            creances = st.number_input("Factures non payees par clients (EUR)", min_value=0, value=45000, step=1000)
        with col4:
            treso_actif = st.number_input("Argent en banque (EUR)", min_value=0, value=15000, step=1000)

        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Ce que vous devez (Passif)</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            cp = st.number_input("Capital de l entreprise (EUR)", min_value=0, value=80000, step=5000, help="Capital + benefices accumules")
        with col2:
            dettes_lt = st.number_input("Credits vehicules/emprunts (EUR)", min_value=0, value=150000, step=5000)
        with col3:
            dettes_fourn = st.number_input("Dettes fournisseurs (EUR)", min_value=0, value=20000, step=1000)
        with col4:
            dettes_fs = st.number_input("Dettes impots/URSSAF (EUR)", min_value=0, value=12000, step=1000)

        decouverts = st.number_input("Decouvert bancaire (EUR)", min_value=0, value=0, step=500)

        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Votre activite cette annee</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            ca = st.number_input("Total facture cette annee (EUR)", min_value=0, value=500000, step=10000, help="Votre chiffre d affaires annuel")
            charges = st.number_input("Total des depenses (EUR)", min_value=0, value=475000, step=10000)
        with col2:
            res_exploit = st.number_input("Benefice d exploitation (EUR)", value=25000, step=1000, help="Ce qui reste apres toutes les charges sauf les interets")
            charges_fi = st.number_input("Interets des credits (EUR)", min_value=0, value=8000, step=500)
        with col3:
            res_net = st.number_input("Benefice net final (EUR)", value=17000, step=1000, help="Ce qui reste vraiment dans votre poche")
            dot_amort = st.number_input("Amortissement vehicules (EUR)", min_value=0, value=30000, step=1000, help="La perte de valeur annuelle de vos camions")

        st.markdown("<div style='height:0.5rem;'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Votre flotte</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            nb_camions = st.number_input("Nombre de camions", min_value=1, value=5, step=1)
        with col2:
            km_flotte = st.number_input("Km parcourus cette annee (toute la flotte)", min_value=0, value=500000, step=10000)
        with col3:
            jours_roules = st.number_input("Jours roules (toute la flotte)", min_value=0, value=1000, step=50)

        submitted = st.form_submit_button("Voir mon diagnostic financier", use_container_width=True, type="primary")

    if submitted:
        bilan = BilanSimplif(
            immobilisations_nettes=immo, stocks=stocks, creances_clients=creances,
            tresorerie_actif=treso_actif, capitaux_propres=cp, dettes_lt=dettes_lt,
            dettes_fournisseurs=dettes_fourn, dettes_fiscales_sociales=dettes_fs,
            decouverts_bancaires=decouverts, chiffre_affaires=ca,
            charges_exploitation=charges, resultat_exploitation=res_exploit,
            charges_financieres=charges_fi, resultat_net=res_net,
            dotations_amortissements=dot_amort, nombre_camions=nb_camions,
            km_total_flotte=km_flotte, jours_roules=jours_roules,
        )
        r = analyser_bilan(bilan)
        afficher_resultats_financiers(r, bilan)


def afficher_resultats_financiers(r, bilan):
    st.divider()
    st.markdown('<div style="text-align:center;margin-bottom:1.5rem;"><div style="font-size:1.2rem;font-weight:700;color:#e2e8f0;">Votre Diagnostic Financier</div><div style="font-size:0.85rem;color:#64748b;margin-top:0.3rem;">Chaque indicateur est explique en langage simple.</div></div>', unsafe_allow_html=True)

    # ===== TRESORERIE =====
    st.markdown('<div class="section-label">Votre tresorerie - Est-ce que vous avez assez d argent ?</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if r.tresorerie_nette >= 0:
            indicateur_card(
                "Tresorerie nette", f"{r.tresorerie_nette:,.0f} EUR",
                "C est l argent reellement disponible apres avoir paye toutes vos dettes a court terme. Vous etes dans le vert, vous pouvez dormir tranquille.",
                "vert"
            )
        elif r.tresorerie_nette > -10000:
            indicateur_card(
                "Tresorerie nette", f"{r.tresorerie_nette:,.0f} EUR",
                "Votre tresorerie est legerement negative. Ca veut dire que vous utilisez un peu votre decouvert pour financer votre activite. C est pas dramatique mais il faut surveiller.",
                "orange",
                "Essayez de relancer vos clients qui n ont pas paye leurs factures."
            )
        else:
            indicateur_card(
                "Tresorerie nette", f"{r.tresorerie_nette:,.0f} EUR",
                "Alerte ! Votre tresorerie est bien negative. Vous dependez de votre decouvert bancaire. Si la banque coupe le decouvert, vous etes en difficulte.",
                "rouge",
                "Action urgente : relancez vos factures impayees et negociez des delais avec vos fournisseurs."
            )
    with col2:
        if r.frng >= 0:
            indicateur_card(
                "Fonds de roulement (FRNG)", f"{r.frng:,.0f} EUR",
                "Vos financements long terme (capital + emprunts) couvrent bien vos vehicules. C est la base d une entreprise solide.",
                "vert"
            )
        else:
            indicateur_card(
                "Fonds de roulement (FRNG)", f"{r.frng:,.0f} EUR",
                "Vos financements long terme ne couvrent pas vos vehicules. En clair, vous financez des camions avec du court terme, c est dangereux.",
                "rouge",
                "Parlez a votre banquier pour restructurer vos financements."
            )

    st.plotly_chart(waterfall_equilibre(r.frng, r.bfr, r.tresorerie_nette), use_container_width=True)

    st.divider()

    # ===== RENTABILITE =====
    st.markdown('<div class="section-label">Votre rentabilite - Est-ce que vous gagnez de l argent ?</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if r.marge_exploitation_pct >= 5:
            indicateur_card(
                "Marge d exploitation", f"{r.marge_exploitation_pct:.1f} %",
                "Pour chaque 100 EUR factures, il vous reste {:.1f} EUR apres toutes les charges. C est bien au-dessus de la moyenne du transport (2-3%).".format(r.marge_exploitation_pct),
                "vert"
            )
        elif r.marge_exploitation_pct >= 2:
            indicateur_card(
                "Marge d exploitation", f"{r.marge_exploitation_pct:.1f} %",
                "Pour chaque 100 EUR factures, il vous reste {:.1f} EUR. C est dans la moyenne du secteur transport (2-3%), mais il y a peu de marge de manoeuvre.".format(r.marge_exploitation_pct),
                "orange",
                "Revoyez vos tarifs a la hausse ou reduisez vos couts pour gagner 1-2 points de marge."
            )
        else:
            indicateur_card(
                "Marge d exploitation", f"{r.marge_exploitation_pct:.1f} %",
                "Pour chaque 100 EUR factures, il ne vous reste que {:.1f} EUR. C est sous la moyenne du secteur. Votre activite ne degage pas assez de benefice.".format(r.marge_exploitation_pct),
                "rouge",
                "Il faut augmenter vos prix ou eliminer les tournees non rentables."
            )
    with col2:
        if res_net_val := r.rentabilite_nette_pct:
            couleur_rn = "vert" if res_net_val > 3 else ("orange" if res_net_val > 0 else "rouge")
            indicateur_card(
                "Benefice net", f"{res_net_val:.1f} %",
                "C est ce qui reste vraiment apres avoir tout paye, y compris les interets de vos credits. C est votre vrai gain.",
                couleur_rn
            )
    with col3:
        indicateur_card(
            "Benefice par camion", f"{r.marge_par_camion:,.0f} EUR / an",
            "Chaque camion de votre flotte vous rapporte en moyenne cette somme par an, apres deduction de toutes les charges.",
            "vert" if r.marge_par_camion > 5000 else ("orange" if r.marge_par_camion > 0 else "rouge"),
            "" if r.marge_par_camion > 0 else "Un camion qui ne rapporte rien doit etre vendu ou mieux utilise."
        )

    st.divider()

    # ===== DELAIS DE PAIEMENT =====
    st.markdown('<div class="section-label">Delais de paiement - Est-ce qu on vous paie a temps ?</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if r.dso <= 30:
            indicateur_card(
                "Vos clients vous paient en", f"{r.dso:.0f} jours",
                "C est conforme a la loi Gayssot qui impose un delai maximum de 30 jours dans le transport. Vos clients jouent le jeu.",
                "vert"
            )
        elif r.dso <= 45:
            indicateur_card(
                "Vos clients vous paient en", f"{r.dso:.0f} jours",
                "Attention, la loi Gayssot impose un maximum de 30 jours dans le transport. Vos clients depassent le delai legal.",
                "orange",
                "Relancez vos clients et rappelez-leur la reglementation. Vous pouvez demander des penalites de retard."
            )
        else:
            indicateur_card(
                "Vos clients vous paient en", f"{r.dso:.0f} jours",
                "C est beaucoup trop long ! La loi impose 30 jours max. Pendant ce temps, c est vous qui financez l activite de vos clients.",
                "rouge",
                "Mettez en place des relances automatiques et appliquez les penalites de retard. C est votre droit."
            )
    with col2:
        indicateur_card(
            "Vous payez vos fournisseurs en", f"{r.dpo:.0f} jours",
            "C est le temps que vous prenez pour payer vos factures (gazole, garage, etc.). Ni trop vite ni trop lent, c est un levier de tresorerie.",
            "vert" if r.dpo >= 15 else "orange"
        )

    st.divider()

    # ===== ENDETTEMENT =====
    st.markdown('<div class="section-label">Votre endettement - Est-ce que vous devez trop d argent ?</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if r.ratio_endettement < 1:
            indicateur_card(
                "Ratio d endettement", f"{r.ratio_endettement:.2f}",
                "Vos dettes long terme sont inferieures a votre capital. Vous etes peu endette, c est solide. Les banques aiment ca.",
                "vert"
            )
        elif r.ratio_endettement < 2:
            indicateur_card(
                "Ratio d endettement", f"{r.ratio_endettement:.2f}",
                "Vos dettes sont entre 1x et 2x votre capital. C est modere, mais faites attention avant de reprendre un nouveau credit.",
                "orange",
                "Attendez d avoir rembourse un credit avant d en reprendre un autre."
            )
        else:
            indicateur_card(
                "Ratio d endettement", f"{r.ratio_endettement:.2f}",
                "Vos dettes depassent 2x votre capital. Vous etes tres endette. Si l activite baisse, ca peut devenir critique.",
                "rouge",
                "Priorite au remboursement. Evitez tout nouvel emprunt."
            )
    with col2:
        couleur_liq = "vert" if r.ratio_liquidite_generale > 1.5 else ("orange" if r.ratio_liquidite_generale > 1 else "rouge")
        if couleur_liq == "vert":
            expl_liq = "Vous avez largement de quoi payer vos dettes a court terme. Situation confortable."
        elif couleur_liq == "orange":
            expl_liq = "Vous pouvez payer vos dettes, mais c est juste. Un impaye client pourrait vous mettre en difficulte."
        else:
            expl_liq = "Vous n avez pas assez pour payer vos dettes court terme. Risque de cessation de paiement."
        indicateur_card("Capacite a payer vos dettes", f"{r.ratio_liquidite_generale:.2f}", expl_liq, couleur_liq)

    with col3:
        indicateur_card(
            "Autofinancement annuel", f"{r.caf:,.0f} EUR",
            "C est l argent que votre entreprise genere chaque annee pour se developper : acheter un nouveau camion, rembourser un credit, ou constituer une reserve.",
            "vert" if r.caf > 20000 else ("orange" if r.caf > 0 else "rouge")
        )

    st.divider()

    # ===== PERFORMANCE FLOTTE =====
    st.markdown('<div class="section-label">Performance de votre flotte</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("CA par camion", f"{r.ca_par_camion:,.0f} EUR")
        st.caption("Chiffre d affaires moyen par vehicule")
    with col2:
        st.metric("Cout par camion", f"{r.cout_par_camion:,.0f} EUR")
        st.caption("Charges moyennes par vehicule")
    with col3:
        st.metric("CA par km", f"{r.ca_par_km:.3f} EUR")
        st.caption("Ce que chaque km vous rapporte")
    with col4:
        couleur_util = "vert" if r.taux_utilisation_flotte_pct > 85 else ("orange" if r.taux_utilisation_flotte_pct > 70 else "rouge")
        indicateur_card(
            "Utilisation flotte", f"{r.taux_utilisation_flotte_pct:.0f} %",
            "Pourcentage de jours ou vos camions roulent. Plus c est haut, mieux c est.",
            couleur_util,
            "" if r.taux_utilisation_flotte_pct > 85 else "Cherchez a remplir les creux : bourse de fret, nouveaux clients."
        )
