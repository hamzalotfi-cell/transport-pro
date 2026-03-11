"""
TransportCost Pro - Landing Page navy/gold
"""
import streamlit as st

def afficher_landing():
    st.markdown("""
    <style>
        .hero-section {
            text-align: center; padding: 4rem 2rem 3rem;
            background: linear-gradient(135deg, #1e3a5f 0%, #1e293b 40%, #1a2744 100%);
            border-radius: 14px; margin-bottom: 2rem;
            border: 1px solid rgba(245,158,11,0.1);
            position: relative; overflow: hidden;
        }
        .hero-section::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(ellipse at 20% 50%, rgba(59,130,246,0.1) 0%, transparent 50%),
                        radial-gradient(ellipse at 80% 50%, rgba(245,158,11,0.06) 0%, transparent 50%);
            pointer-events: none;
        }
        .hero-title { font-family: 'DM Sans', sans-serif; font-size: 2.5rem; font-weight: 700; color: #f1f5f9; line-height: 1.2; letter-spacing: -0.03em; position: relative; }
        .hero-title span { color: #f59e0b; }
        .hero-subtitle { font-size: 1.05rem; color: #94a3b8; max-width: 580px; margin: 1rem auto 0; line-height: 1.7; position: relative; }
        .hero-badge { display: inline-block; padding: 0.3rem 1rem; background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.2); border-radius: 20px; font-size: 0.75rem; color: #f59e0b; font-weight: 600; letter-spacing: 0.05em; margin-bottom: 1.5rem; position: relative; }

        .feature-card {
            border: 1px solid rgba(59,130,246,0.1); border-radius: 12px; padding: 2rem 1.5rem;
            background: rgba(30,41,59,0.5); text-align: center; height: 100%;
            transition: all 0.3s ease;
        }
        .feature-card:hover { border-color: rgba(59,130,246,0.25); transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0,0,0,0.15); }
        .feature-icon { width: 52px; height: 52px; border-radius: 12px; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.2rem; }
        .feature-card h3 { font-family: 'DM Sans', sans-serif; font-size: 1rem; font-weight: 600; color: #f1f5f9; margin-bottom: 0.6rem; }
        .feature-card p { font-size: 0.85rem; color: #94a3b8; line-height: 1.6; margin: 0; }

        .img-card { border-radius: 12px; overflow: hidden; position: relative; height: 230px; background-size: cover; background-position: center; border: 1px solid rgba(59,130,246,0.1); }
        .img-card:hover { box-shadow: 0 8px 25px rgba(0,0,0,0.2); }
        .img-card-overlay { position: absolute; bottom: 0; left: 0; right: 0; padding: 1.5rem; background: linear-gradient(transparent, rgba(15,23,42,0.95)); }
        .img-card-overlay h3 { font-size: 1.05rem; font-weight: 600; color: #f1f5f9; margin: 0 0 0.3rem; }
        .img-card-overlay p { font-size: 0.82rem; color: #94a3b8; margin: 0; }

        .why-title { font-family: 'DM Sans', sans-serif; font-size: 1.5rem; font-weight: 700; color: #f1f5f9; text-align: center; }
        .why-subtitle { font-size: 0.9rem; color: #94a3b8; text-align: center; margin-bottom: 2rem; }
        .why-item { display: flex; align-items: flex-start; gap: 0.8rem; padding: 0.7rem 0; }
        .why-check { width: 22px; height: 22px; border-radius: 6px; background: rgba(245,158,11,0.1); border: 1px solid rgba(245,158,11,0.25); display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; color: #f59e0b; font-size: 0.65rem; font-weight: 700; }
        .why-text { font-size: 0.88rem; color: #cbd5e1; line-height: 1.5; }
        .why-text strong { color: #f1f5f9; }

        .stat-box { text-align: center; padding: 1.5rem; border: 1px solid rgba(59,130,246,0.1); border-radius: 12px; background: rgba(30,41,59,0.4); }
        .stat-number { font-family: 'JetBrains Mono', monospace; font-size: 2rem; font-weight: 700; color: #f59e0b; }
        .stat-label { font-size: 0.8rem; color: #94a3b8; margin-top: 0.3rem; }

        .pricing-card { border: 1px solid rgba(59,130,246,0.1); border-radius: 12px; padding: 2rem 1.5rem; background: rgba(30,41,59,0.4); text-align: center; }
        .pricing-card.featured { border-color: rgba(245,158,11,0.3); background: rgba(30,41,59,0.6); box-shadow: 0 0 30px rgba(245,158,11,0.05); }
        .pricing-tier { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.12em; font-weight: 600; margin-bottom: 0.8rem; }
        .pricing-name { font-size: 1.15rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.5rem; }
        .pricing-price { font-family: 'JetBrains Mono', monospace; font-size: 2rem; font-weight: 700; color: #f1f5f9; margin-bottom: 0.3rem; }
        .pricing-price span { font-size: 0.9rem; color: #94a3b8; font-weight: 400; }
        .pricing-feature { font-size: 0.85rem; color: #94a3b8; padding: 0.4rem 0; border-bottom: 1px solid rgba(59,130,246,0.06); }
        .pricing-feature:last-child { border: none; }
    </style>

    <div class="hero-section">
        <div class="hero-badge">Concu pour les transporteurs routiers</div>
        <div class="hero-title">Maitrisez votre cout au kilometre.<br><span>Decidez rentable.</span></div>
        <div class="hero-subtitle">L'outil professionnel qui vous donne votre vrai cout au km, analyse la rentabilite de chaque tournee et pilote votre sante financiere.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Calculer mon cout maintenant", use_container_width=True, type="primary"):
            st.session_state["nav_page"] = "Calculateur Cout/km"
            st.rerun()

    st.markdown("<div style='height:1.5rem;'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown('<div class="feature-card"><div class="feature-icon" style="background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.2);"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2"><rect x="1" y="3" width="15" height="13" rx="2"/><path d="M16 8h4l3 3v5a2 2 0 01-2 2h-1"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg></div><h3>Special transport routier</h3><p>Methode trinome CNR integree. Concu exclusivement pour les transporteurs.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="feature-card"><div class="feature-icon" style="background:rgba(245,158,11,0.1);border:1px solid rgba(245,158,11,0.2);"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg></div><h3>Evitez les tournees a perte</h3><p>Identifiez immediatement si une mission est rentable ou non.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="feature-card"><div class="feature-icon" style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg></div><h3>Pilotez votre rentabilite</h3><p>Dashboard financier complet avec alertes automatiques.</p></div>', unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown('<div class="img-card" style="background-image:url(\'https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?w=800&q=80\');"><div class="img-card-overlay"><h3>Analysez chaque tournee</h3><p>Marge, cout, rentabilite en un coup d oeil</p></div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="img-card" style="background-image:url(\'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80\');"><div class="img-card-overlay"><h3>Pilotez votre flotte</h3><p>Performance financiere par vehicule</p></div></div>', unsafe_allow_html=True)

    st.divider()
    st.markdown('<div style="padding:2rem 0 0;"><div class="why-title">Pourquoi connaitre son cout au km ?</div><div class="why-subtitle">Une mauvaise tarification peut couter des milliers d euros par an.</div></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""<div style="padding:0.5rem 0;">
        <div class="why-item"><div class="why-check">&#10003;</div><div class="why-text"><strong>Negociez mieux vos contrats</strong> avec des chiffres precis et verifiables</div></div>
        <div class="why-item"><div class="why-check">&#10003;</div><div class="why-text"><strong>Refusez les missions a perte</strong> en connaissant votre prix plancher</div></div>
        <div class="why-item"><div class="why-check">&#10003;</div><div class="why-text"><strong>Identifiez vos postes de cout</strong> les plus lourds pour les optimiser</div></div>
        <div class="why-item"><div class="why-check">&#10003;</div><div class="why-text"><strong>Securisez votre tresorerie</strong> et anticipez vos besoins financiers</div></div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div style="padding:0.5rem 0;"><div class="stat-box" style="margin-bottom:1rem;"><div class="stat-number">2-3 %</div><div class="stat-label">Marge moyenne du transport routier</div></div>
        <div class="stat-box" style="margin-bottom:1rem;"><div class="stat-number">37 000</div><div class="stat-label">Transporteurs en France</div></div>
        <div class="stat-box"><div class="stat-number">83 %</div><div class="stat-label">N ont pas d outil de pilotage adapte</div></div></div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown('<div style="text-align:center;padding:1.5rem 0 0.5rem;"><div class="why-title">Tarifs transparents</div><div class="why-subtitle">Commencez gratuitement. Sans engagement.</div></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown('<div class="pricing-card"><div class="pricing-tier" style="color:#10b981;">Gratuit</div><div class="pricing-name">Calculateur</div><div class="pricing-price">0 EUR</div><div style="height:1rem;"></div><div class="pricing-feature">Cout au kilometre</div><div class="pricing-feature">Methode trinome CNR</div><div class="pricing-feature">Simulateur rapide</div><div class="pricing-feature">1 vehicule</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="pricing-card featured"><div class="pricing-tier" style="color:#f59e0b;">Essentiel</div><div class="pricing-name">Rentabilite</div><div class="pricing-price">29 EUR <span>/ mois</span></div><div style="height:1rem;"></div><div class="pricing-feature">Tout du Gratuit</div><div class="pricing-feature">Analyse par tournee</div><div class="pricing-feature">Seuil de rentabilite</div><div class="pricing-feature">5 vehicules</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="pricing-card"><div class="pricing-tier" style="color:#3b82f6;">Pro</div><div class="pricing-name">Dashboard complet</div><div class="pricing-price">49 EUR <span>/ mois</span></div><div style="height:1rem;"></div><div class="pricing-feature">Tout de l Essentiel</div><div class="pricing-feature">Dashboard financier</div><div class="pricing-feature">Alertes automatiques</div><div class="pricing-feature">Vehicules illimites</div></div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align:center;padding:3rem 0 1rem;border-top:1px solid rgba(59,130,246,0.08);margin-top:2rem;"><div class="brand-name" style="font-size:1.2rem;">Transport<span>Cost</span> Pro</div><div style="font-size:0.75rem;color:#64748b;margin-top:0.5rem;">L outil financier des transporteurs routiers</div></div>', unsafe_allow_html=True)
