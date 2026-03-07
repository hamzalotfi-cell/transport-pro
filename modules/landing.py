"""
TransportCost Pro - Landing Page
"""
import streamlit as st


def afficher_landing():

    st.markdown("""
    <style>
        .hero-section {
            text-align: center;
            padding: 4rem 2rem 3rem;
            background: linear-gradient(135deg, #0f2744 0%, #163a5f 50%, #1a4a7a 100%);
            border-radius: 12px;
            margin-bottom: 2rem;
            border: 1px solid rgba(77, 163, 255, 0.2);
            position: relative;
            overflow: hidden;
        }
        .hero-section::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: radial-gradient(circle at 30% 40%, rgba(77,163,255,0.15) 0%, transparent 60%),
                        radial-gradient(circle at 80% 70%, rgba(46,204,113,0.08) 0%, transparent 50%);
            pointer-events: none;
        }
        .hero-title {
            font-family: 'DM Sans', sans-serif;
            font-size: 2.6rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.2;
            letter-spacing: -0.03em;
            margin-bottom: 0.5rem;
            position: relative;
        }
        .hero-title span { color: #5cb8ff; }
        .hero-subtitle {
            font-size: 1.05rem;
            color: #b0c4de;
            max-width: 580px;
            margin: 1rem auto 2rem;
            line-height: 1.7;
        }
        .hero-badge {
            display: inline-block;
            padding: 0.3rem 0.9rem;
            background: rgba(46,204,113,0.15);
            border: 1px solid rgba(46,204,113,0.3);
            border-radius: 20px;
            font-size: 0.75rem;
            color: #2ecc71;
            font-weight: 500;
            letter-spacing: 0.05em;
            margin-bottom: 1.5rem;
        }
        .feature-card {
            border: 1px solid rgba(77,163,255,0.15);
            border-radius: 10px;
            padding: 2rem 1.5rem;
            background: linear-gradient(135deg, rgba(15,39,68,0.7) 0%, rgba(22,58,95,0.5) 100%);
            text-align: center;
            height: 100%;
            transition: all 0.3s ease;
        }
        .feature-card:hover {
            border-color: rgba(77,163,255,0.35);
            transform: translateY(-2px);
        }
        .feature-icon {
            width: 50px; height: 50px;
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            margin: 0 auto 1.2rem;
        }
        .feature-card h3 {
            font-family: 'DM Sans', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            color: #e2e8f0;
            margin-bottom: 0.6rem;
        }
        .feature-card p {
            font-size: 0.85rem;
            color: #94a3b8;
            line-height: 1.6;
            margin: 0;
        }
        .img-card {
            border-radius: 10px;
            overflow: hidden;
            position: relative;
            height: 230px;
            background-size: cover;
            background-position: center;
            border: 1px solid rgba(77,163,255,0.15);
            transition: all 0.3s ease;
        }
        .img-card:hover { border-color: rgba(77,163,255,0.35); }
        .img-card-overlay {
            position: absolute;
            bottom: 0; left: 0; right: 0;
            padding: 1.5rem;
            background: linear-gradient(transparent, rgba(10,20,40,0.95));
        }
        .img-card-overlay h3 {
            font-family: 'DM Sans', sans-serif;
            font-size: 1.05rem; font-weight: 600; color: #e2e8f0; margin: 0 0 0.3rem;
        }
        .img-card-overlay p { font-size: 0.82rem; color: #94a3b8; margin: 0; }
        .why-title {
            font-family: 'DM Sans', sans-serif;
            font-size: 1.5rem; font-weight: 700; color: #e2e8f0;
            text-align: center; margin-bottom: 0.5rem;
        }
        .why-subtitle {
            font-size: 0.9rem; color: #94a3b8;
            text-align: center; margin-bottom: 2rem;
        }
        .why-item {
            display: flex; align-items: flex-start; gap: 0.8rem; padding: 0.8rem 0;
        }
        .why-check {
            width: 24px; height: 24px; border-radius: 50%;
            background: rgba(46,204,113,0.15);
            border: 1px solid rgba(46,204,113,0.3);
            display: flex; align-items: center; justify-content: center;
            flex-shrink: 0; margin-top: 2px;
            color: #2ecc71; font-size: 0.7rem;
        }
        .why-text {
            font-size: 0.9rem; color: #cbd5e1; line-height: 1.5;
        }
        .why-text strong { color: #e2e8f0; }
        .stat-box {
            text-align: center; padding: 1.5rem;
            border: 1px solid rgba(77,163,255,0.15);
            border-radius: 10px;
            background: linear-gradient(135deg, rgba(15,39,68,0.5) 0%, rgba(22,58,95,0.3) 100%);
        }
        .stat-number {
            font-family: 'JetBrains Mono', monospace;
            font-size: 2rem; font-weight: 700; color: #5cb8ff;
        }
        .stat-label { font-size: 0.8rem; color: #94a3b8; margin-top: 0.3rem; }
        .pricing-card {
            border: 1px solid rgba(77,163,255,0.15);
            border-radius: 10px; padding: 2rem 1.5rem;
            background: linear-gradient(135deg, rgba(15,39,68,0.5) 0%, rgba(22,58,95,0.3) 100%);
            text-align: center;
        }
        .pricing-card.featured {
            border-color: rgba(77,163,255,0.4);
            background: linear-gradient(135deg, rgba(15,39,68,0.8) 0%, rgba(27,110,194,0.15) 100%);
        }
        .pricing-tier {
            font-size: 0.72rem; text-transform: uppercase;
            letter-spacing: 0.12em; font-weight: 600; margin-bottom: 0.8rem;
        }
        .pricing-name {
            font-size: 1.15rem; font-weight: 700; color: #e2e8f0; margin-bottom: 0.5rem;
        }
        .pricing-price {
            font-family: 'JetBrains Mono', monospace;
            font-size: 2rem; font-weight: 700; color: #e2e8f0; margin-bottom: 0.3rem;
        }
        .pricing-price span { font-size: 0.9rem; color: #94a3b8; font-weight: 400; }
        .pricing-feature {
            font-size: 0.85rem; color: #94a3b8; padding: 0.4rem 0;
            border-bottom: 1px solid rgba(30,58,95,0.2);
        }
        .pricing-feature:last-child { border: none; }
    </style>

    <div class="hero-section">
        <div class="hero-badge">Concu pour les transporteurs routiers francais</div>
        <div class="hero-title">
            Maitrisez votre cout au kilometre.<br>
            <span>Decidez rentable.</span>
        </div>
        <div class="hero-subtitle">
            L'outil professionnel qui vous donne votre vrai cout au km,
            analyse la rentabilite de chaque tournee et pilote la sante financiere de votre entreprise.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Bouton CTA qui marche
    col_left, col_center, col_right = st.columns([1, 1, 1])
    with col_center:
        if st.button("Calculer mon cout maintenant", use_container_width=True, type="primary"):
            st.session_state["nav_page"] = "Calculateur Cout/km"
            st.rerun()

    st.markdown("<div style='height:1.5rem;'></div>", unsafe_allow_html=True)

    # FEATURES
    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background:rgba(77,163,255,0.12);border:1px solid rgba(77,163,255,0.25);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#5cb8ff" stroke-width="2"><rect x="1" y="3" width="15" height="13" rx="2"/><path d="M16 8h4l3 3v5a2 2 0 01-2 2h-1"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>
            </div>
            <h3>Special transport routier</h3>
            <p>Outil concu exclusivement pour les transporteurs. Methode trinome CNR integree.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background:rgba(46,204,113,0.12);border:1px solid rgba(46,204,113,0.25);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2ecc71" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>
            </div>
            <h3>Evitez les tournees a perte</h3>
            <p>Identifiez immediatement si une mission genere un benefice ou une perte.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon" style="background:rgba(230,126,34,0.12);border:1px solid rgba(230,126,34,0.25);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#e67e22" stroke-width="2"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
            </div>
            <h3>Decisions basees sur vos chiffres</h3>
            <p>Calculs bases sur vos charges reelles. Pas des estimations generiques.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem;'></div>", unsafe_allow_html=True)

    # IMAGE CARDS
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("""
        <div class="img-card" style="background-image:url('https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?w=800&q=80');">
            <div class="img-card-overlay">
                <h3>Analysez la rentabilite de chaque tournee</h3>
                <p>Indicateurs financiers clairs avec code couleur</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="img-card" style="background-image:url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80');">
            <div class="img-card-overlay">
                <h3>Pilotez votre flotte avec precision</h3>
                <p>Dashboard financier complet et accessible</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    st.divider()

    # WHY SECTION
    st.markdown("""
    <div style="padding:2rem 0 0;">
        <div class="why-title">Pourquoi analyser son cout kilometrique ?</div>
        <div class="why-subtitle">Beaucoup de transporteurs acceptent des tournees sans connaitre leur veritable cout.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown("""
        <div style="padding:1rem 0;">
            <div style="font-size:0.9rem;color:#94a3b8;line-height:1.7;margin-bottom:1.5rem;">
                Une mauvaise estimation peut generer <strong style="color:#e2e8f0;">plusieurs milliers d'euros de perte par an</strong>.
                Connaitre votre cout reel vous permet de :
            </div>
            <div class="why-item">
                <div class="why-check">&#10003;</div>
                <div class="why-text"><strong>Negocier correctement vos contrats</strong> avec des chiffres precis</div>
            </div>
            <div class="why-item">
                <div class="why-check">&#10003;</div>
                <div class="why-text"><strong>Refuser les missions a perte</strong> en sachant exactement votre seuil</div>
            </div>
            <div class="why-item">
                <div class="why-check">&#10003;</div>
                <div class="why-text"><strong>Ameliorer votre marge</strong> en identifiant vos postes de cout les plus lourds</div>
            </div>
            <div class="why-item">
                <div class="why-check">&#10003;</div>
                <div class="why-text"><strong>Securiser votre tresorerie</strong> et anticiper vos besoins financiers</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="padding:1rem 0;">
            <div class="stat-box" style="margin-bottom:1rem;">
                <div class="stat-number">2-3 %</div>
                <div class="stat-label">Marge moyenne du secteur transport en France</div>
            </div>
            <div class="stat-box" style="margin-bottom:1rem;">
                <div class="stat-number">37 000</div>
                <div class="stat-label">Entreprises de transport routier en France</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">83 %</div>
                <div class="stat-label">Sont des micro-entreprises sans outils adaptes</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # PRICING
    st.markdown("""
    <div style="text-align:center;padding:1.5rem 0 0.5rem;">
        <div class="why-title">Tarifs simples, sans engagement</div>
        <div class="why-subtitle">Commencez gratuitement. Evoluez quand vous etes pret.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown("""
        <div class="pricing-card">
            <div class="pricing-tier" style="color:#2ecc71;">Gratuit</div>
            <div class="pricing-name">Calculateur</div>
            <div class="pricing-price">0 EUR</div>
            <div style="height:1rem;"></div>
            <div class="pricing-feature">Cout au kilometre</div>
            <div class="pricing-feature">Methode trinome CNR</div>
            <div class="pricing-feature">Simulateur de tournee</div>
            <div class="pricing-feature">1 vehicule</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="pricing-card featured">
            <div class="pricing-tier" style="color:#5cb8ff;">Essentiel</div>
            <div class="pricing-name">Rentabilite</div>
            <div class="pricing-price">29 EUR <span>/ mois</span></div>
            <div style="height:1rem;"></div>
            <div class="pricing-feature">Tout du plan Gratuit</div>
            <div class="pricing-feature">Analyse par tournee</div>
            <div class="pricing-feature">Seuil de rentabilite</div>
            <div class="pricing-feature">Jusqu a 5 vehicules</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="pricing-card">
            <div class="pricing-tier" style="color:#e67e22;">Pro</div>
            <div class="pricing-name">Dashboard complet</div>
            <div class="pricing-price">49 EUR <span>/ mois</span></div>
            <div style="height:1rem;"></div>
            <div class="pricing-feature">Tout du plan Essentiel</div>
            <div class="pricing-feature">Dashboard financier</div>
            <div class="pricing-feature">Ratios et alertes</div>
            <div class="pricing-feature">Vehicules illimites</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center;padding:3rem 0 1rem;border-top:1px solid rgba(30,58,95,0.3);margin-top:2rem;">
        <div class="brand-name" style="font-size:1.2rem;">Transport<span style="color:#5cb8ff;">Cost</span> Pro</div>
        <div style="font-size:0.78rem;color:#475569;margin-top:0.5rem;">L'outil financier des transporteurs routiers.</div>
    </div>
    """, unsafe_allow_html=True)
