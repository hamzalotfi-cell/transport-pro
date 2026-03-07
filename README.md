# 🚛 TransportPro — MVP

Outil de gestion financière pour les petits transporteurs routiers.

## Démarrage rapide

### Option 1 : En local (si Python est installé)
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Option 2 : GitHub Codespaces (recommandé si pas de Python en local)
1. Push ce dossier sur un repo GitHub
2. Ouvre un Codespace depuis le repo
3. Dans le terminal du Codespace :
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   ```

### Option 3 : Déploiement Streamlit Cloud
1. Push ce dossier sur GitHub
2. Va sur [share.streamlit.io](https://share.streamlit.io)
3. Connecte ton repo GitHub
4. Sélectionne `app.py` comme fichier principal
5. Déploie — c'est en ligne !

## Structure du projet
```
transport-pro/
├── app.py                     # Point d'entrée principal
├── requirements.txt           # Dépendances Python
├── .streamlit/
│   └── config.toml           # Thème et configuration
├── modules/
│   ├── calculateur.py        # Module 1 — Calculateur coût/km (GRATUIT)
│   ├── rentabilite.py        # Module 2 — Rentabilité tournées (PAYANT)
│   └── dashboard.py          # Module 3 — Dashboard financier (PAYANT)
├── utils/
│   ├── formules.py           # Moteur de calcul (toutes les formules)
│   └── charts.py             # Graphiques Plotly
└── assets/                    # Images, logo, etc.
```

## Prochaines étapes
- [ ] Intégration Supabase (base de données)
- [ ] Authentification utilisateurs
- [ ] Module 2 complet (tournées)
- [ ] Module 3 complet (dashboard financier)
- [ ] Intégration Stripe (paiements)
- [ ] Landing page SEO
