"""
TransportCost Pro - Graphiques navy/gold
"""
import plotly.graph_objects as go

C = {"bleu": "#3b82f6", "bleu2": "#60a5fa", "or": "#f59e0b", "or2": "#fbbf24", "vert": "#10b981", "rouge": "#ef4444", "orange": "#f97316", "texte": "#f1f5f9", "sec": "#94a3b8", "grille": "rgba(148,163,184,0.08)"}
L = dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color=C["texte"], family="DM Sans", size=13), margin=dict(l=50, r=30, t=55, b=40))

def camembert_couts(df, dv):
    tf, tv = sum(df.values()), sum(dv.values())
    fig = go.Figure(data=[go.Pie(labels=["Couts fixes", "Couts variables"], values=[tf, tv], marker=dict(colors=[C["bleu"], C["or"]]), hole=0.6, textinfo="label+percent", textfont=dict(size=13))])
    fig.update_layout(**L, title=dict(text="REPARTITION DES COUTS", font=dict(size=13, color=C["sec"]), x=0.5, xanchor="center"), showlegend=False, height=340)
    fig.add_annotation(text=f"<b>{tf+tv:,.0f} EUR</b><br><span style='font-size:11px;color:{C['sec']}'>Total annuel</span>", x=0.5, y=0.5, showarrow=False, font=dict(size=18, color=C["texte"], family="JetBrains Mono"))
    return fig

def barres_detail_couts(df, dv):
    tc = {}
    for k, v in df.items():
        if v > 0: tc[k] = ("f", v)
    for k, v in dv.items():
        if v > 0: tc[k] = ("v", v)
    si = sorted(tc.items(), key=lambda x: x[1][1])
    fig = go.Figure(data=[go.Bar(y=[i[0] for i in si], x=[i[1][1] for i in si], orientation="h", marker_color=[C["bleu"] if i[1][0]=="f" else C["or"] for i in si], text=[f"{i[1][1]:,.0f} EUR" for i in si], textposition="outside", textfont=dict(size=12, family="JetBrains Mono", color=C["texte"]))])
    fig.update_layout(**L, title=dict(text="DETAIL PAR POSTE", font=dict(size=13, color=C["sec"]), x=0.5, xanchor="center"), xaxis=dict(gridcolor=C["grille"], showgrid=True, zeroline=False), yaxis=dict(showgrid=False), height=max(340, len(si)*42+100))
    return fig

def graphique_trinome(ck, cc, cj):
    fig = go.Figure(data=[go.Bar(x=["CK Kilometrique", "CC Conducteur/h", "CJ Journalier"], y=[ck, cc, cj], marker_color=[C["or"], C["bleu"], C["bleu2"]], text=[f"{v:.2f} EUR" for v in [ck, cc, cj]], textposition="outside", textfont=dict(size=13, family="JetBrains Mono", color=C["texte"]), width=0.5)])
    fig.update_layout(**L, title=dict(text="TRINOME CNR", font=dict(size=13, color=C["sec"]), x=0.5, xanchor="center"), yaxis=dict(gridcolor=C["grille"], showgrid=True, zeroline=False), xaxis=dict(showgrid=False), height=340)
    return fig

def jauge_marge(tm, label="Marge"):
    fig = go.Figure(go.Indicator(mode="gauge+number", value=tm, number=dict(suffix="%", font=dict(size=36, family="JetBrains Mono", color=C["texte"])), gauge=dict(axis=dict(range=[-10, 30], ticksuffix="%"), bar=dict(color=C["bleu"]), bgcolor="rgba(0,0,0,0)", steps=[dict(range=[-10, 0], color="rgba(239,68,68,0.15)"), dict(range=[0, 5], color="rgba(249,115,22,0.1)"), dict(range=[5, 15], color="rgba(245,158,11,0.08)"), dict(range=[15, 30], color="rgba(16,185,129,0.1)")])))
    fig.update_layout(**L, height=260)
    return fig

def waterfall_equilibre(frng, bfr, tn):
    fig = go.Figure(go.Waterfall(orientation="v", measure=["absolute", "relative", "total"], x=["FRNG", "BFR", "Tresorerie"], y=[frng, -bfr, tn], text=[f"{frng:,.0f}", f"-{bfr:,.0f}", f"{tn:,.0f}"], textposition="outside", textfont=dict(family="JetBrains Mono", size=12, color=C["texte"]), connector=dict(line=dict(color=C["grille"])), increasing=dict(marker=dict(color=C["vert"])), decreasing=dict(marker=dict(color=C["rouge"])), totals=dict(marker=dict(color=C["vert"] if tn>=0 else C["rouge"]))))
    fig.update_layout(**L, title=dict(text="EQUILIBRE FINANCIER", font=dict(size=13, color=C["sec"]), x=0.5, xanchor="center"), yaxis=dict(gridcolor=C["grille"], showgrid=True), height=380, showlegend=False)
    return fig
