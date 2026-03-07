"""
TransportPro — Fonctions graphiques
Graphiques Plotly pour les dashboards.
"""

import plotly.graph_objects as go
import plotly.express as px


# Palette de couleurs cohérente
COLORS = {
    "bleu": "#1B6EC2",
    "bleu_clair": "#4DA3FF",
    "vert": "#2ECC71",
    "jaune": "#F1C40F",
    "orange": "#E67E22",
    "rouge": "#E74C3C",
    "gris": "#7F8C8D",
    "fond": "#0E1117",
    "carte": "#1A1F2B",
    "texte": "#FAFAFA",
}

LAYOUT_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color=COLORS["texte"], family="Arial"),
    margin=dict(l=40, r=40, t=50, b=40),
)


def camembert_couts(detail_fixes: dict, detail_variables: dict) -> go.Figure:
    """Camembert répartition coûts fixes vs variables."""

    total_fixes = sum(detail_fixes.values())
    total_variables = sum(detail_variables.values())

    fig = go.Figure(data=[
        go.Pie(
            labels=["Coûts fixes", "Coûts variables"],
            values=[total_fixes, total_variables],
            marker=dict(colors=[COLORS["bleu"], COLORS["orange"]]),
            hole=0.55,
            textinfo="label+percent",
            textfont=dict(size=14),
            hovertemplate="<b>%{label}</b><br>%{value:,.0f} €<br>%{percent}<extra></extra>",
        )
    ])

    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Répartition Coûts Fixes / Variables", font=dict(size=16)),
        showlegend=False,
        height=350,
    )

    # Annotation au centre
    total = total_fixes + total_variables
    fig.add_annotation(
        text=f"<b>{total:,.0f} €</b><br>Total annuel",
        x=0.5, y=0.5, showarrow=False,
        font=dict(size=16, color=COLORS["texte"]),
    )

    return fig


def barres_detail_couts(detail_fixes: dict, detail_variables: dict) -> go.Figure:
    """Barres horizontales détaillées de chaque poste de coût."""

    # Fusionner et trier
    tous_couts = {}
    for k, v in detail_fixes.items():
        if v > 0:
            tous_couts[k] = v
    for k, v in detail_variables.items():
        if v > 0:
            tous_couts[k] = v

    # Trier par valeur
    sorted_items = sorted(tous_couts.items(), key=lambda x: x[1])
    labels = [item[0] for item in sorted_items]
    values = [item[1] for item in sorted_items]
    colors = [
        COLORS["bleu"] if label in detail_fixes else COLORS["orange"]
        for label in labels
    ]

    fig = go.Figure(data=[
        go.Bar(
            y=labels,
            x=values,
            orientation="h",
            marker_color=colors,
            text=[f"{v:,.0f} €" for v in values],
            textposition="outside",
            textfont=dict(size=12),
            hovertemplate="<b>%{y}</b><br>%{x:,.0f} €<extra></extra>",
        )
    ])

    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Détail des postes de coût (annuel)", font=dict(size=16)),
        xaxis=dict(
            title="Montant annuel (€)",
            gridcolor="rgba(255,255,255,0.1)",
            showgrid=True,
        ),
        yaxis=dict(showgrid=False),
        height=max(350, len(labels) * 45 + 100),
    )

    return fig


def jauge_marge(taux_marge: float, label: str = "Marge") -> go.Figure:
    """Jauge de marge avec zones de couleur."""

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=taux_marge,
        number=dict(suffix="%", font=dict(size=32)),
        title=dict(text=label, font=dict(size=16)),
        gauge=dict(
            axis=dict(range=[-10, 30], ticksuffix="%"),
            bar=dict(color=COLORS["bleu"]),
            bgcolor="rgba(0,0,0,0)",
            steps=[
                dict(range=[-10, 0], color="rgba(231,76,60,0.3)"),
                dict(range=[0, 5], color="rgba(230,126,34,0.3)"),
                dict(range=[5, 15], color="rgba(241,196,15,0.3)"),
                dict(range=[15, 30], color="rgba(46,204,113,0.3)"),
            ],
            threshold=dict(
                line=dict(color=COLORS["rouge"], width=3),
                thickness=0.8,
                value=0,
            ),
        ),
    ))

    fig.update_layout(
        **LAYOUT_BASE,
        height=280,
    )

    return fig


def graphique_trinome(ck: float, cc: float, cj: float) -> go.Figure:
    """Visualisation de la décomposition trinôme CNR."""

    categories = [
        "CK<br>(Coût kilométrique)",
        "CC<br>(Coût conducteur/h)",
        "CJ<br>(Coût journalier)",
    ]
    values = [ck, cc, cj]
    colors_list = [COLORS["orange"], COLORS["bleu"], COLORS["bleu_clair"]]

    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=values,
            marker_color=colors_list,
            text=[f"{v:.2f} €" for v in values],
            textposition="outside",
            textfont=dict(size=14),
        )
    ])

    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Décomposition Trinôme CNR", font=dict(size=16)),
        yaxis=dict(
            title="€",
            gridcolor="rgba(255,255,255,0.1)",
            showgrid=True,
        ),
        xaxis=dict(showgrid=False),
        height=350,
    )

    return fig


def waterfall_equilibre(frng: float, bfr: float, tn: float) -> go.Figure:
    """Graphique en cascade FRNG → BFR → Trésorerie nette."""

    fig = go.Figure(go.Waterfall(
        name="Équilibre financier",
        orientation="v",
        measure=["absolute", "relative", "total"],
        x=["FRNG", "BFR", "Trésorerie Nette"],
        y=[frng, -bfr, tn],
        text=[f"{frng:,.0f} €", f"-{bfr:,.0f} €", f"{tn:,.0f} €"],
        textposition="outside",
        connector=dict(line=dict(color="rgba(255,255,255,0.3)")),
        increasing=dict(marker=dict(color=COLORS["vert"])),
        decreasing=dict(marker=dict(color=COLORS["rouge"])),
        totals=dict(marker=dict(
            color=COLORS["vert"] if tn >= 0 else COLORS["rouge"]
        )),
    ))

    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="Équilibre Financier", font=dict(size=16)),
        yaxis=dict(
            title="€",
            gridcolor="rgba(255,255,255,0.1)",
            showgrid=True,
        ),
        height=400,
        showlegend=False,
    )

    return fig
