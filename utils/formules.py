"""
TransportPro — Moteur de calcul financier
Toutes les formules de coût kilométrique, rentabilité et analyse financière.
"""

from dataclasses import dataclass, field
from typing import Optional


# ============================================================
# MODULE 1 — Calculateur de Coût Kilométrique
# ============================================================

@dataclass
class ProfilVehicule:
    """Profil complet d'un véhicule avec tous ses coûts."""
    # Données véhicule
    nom: str = ""
    type_vehicule: str = "Semi-remorque 40T"
    prix_achat: float = 0.0
    duree_amortissement: int = 5
    valeur_residuelle: float = 0.0
    km_annuel: int = 100000

    # Coûts fixes annuels
    assurance: float = 0.0
    taxe_essieu: float = 0.0
    controle_technique: float = 0.0
    parking_stationnement: float = 0.0
    credit_mensualite: float = 0.0
    salaire_conducteur_brut: float = 0.0
    charges_sociales_pct: float = 45.0
    frais_structure: float = 0.0

    # Coûts variables
    conso_carburant: float = 33.0  # L/100km
    prix_carburant: float = 1.55   # €/L
    cout_pneumatiques: float = 0.0
    cout_entretien_reparation: float = 0.0
    cout_peages_annuel: float = 0.0

    # Paramètres d'exploitation
    jours_exploitation: int = 220
    heures_conduite_jour: float = 8.0
    taux_retour_vide: float = 20.0
    marge_souhaitee: float = 10.0


@dataclass
class ResultatCoutKm:
    """Résultats du calcul de coût kilométrique."""
    # Coûts fixes
    amortissement_annuel: float = 0.0
    cout_conducteur_annuel: float = 0.0
    credit_annuel: float = 0.0
    total_couts_fixes: float = 0.0

    # Coûts variables
    cout_carburant_annuel: float = 0.0
    total_couts_variables: float = 0.0

    # Coût total
    cout_total_annuel: float = 0.0

    # Coûts au km
    cout_km_brut: float = 0.0
    cout_km_reel: float = 0.0
    km_facturable: float = 0.0

    # Prix minimum
    prix_min_km: float = 0.0

    # Méthode trinôme CNR
    ck: float = 0.0  # Coût kilométrique
    cc: float = 0.0  # Coût conducteur horaire
    cj: float = 0.0  # Coût journalier structure

    # Coût journalier
    cout_journalier: float = 0.0

    # Détails pour graphiques
    detail_fixes: dict = field(default_factory=dict)
    detail_variables: dict = field(default_factory=dict)


def calculer_cout_km(profil: ProfilVehicule) -> ResultatCoutKm:
    """Calcule le coût kilométrique complet d'un véhicule."""

    r = ResultatCoutKm()

    # --- Coûts fixes ---
    r.amortissement_annuel = (
        (profil.prix_achat - profil.valeur_residuelle)
        / max(profil.duree_amortissement, 1)
    )

    r.cout_conducteur_annuel = (
        profil.salaire_conducteur_brut * 12
        * (1 + profil.charges_sociales_pct / 100)
    )

    r.credit_annuel = profil.credit_mensualite * 12

    r.total_couts_fixes = (
        r.amortissement_annuel
        + profil.assurance
        + profil.taxe_essieu
        + profil.controle_technique
        + profil.parking_stationnement
        + r.credit_annuel
        + r.cout_conducteur_annuel
        + profil.frais_structure
    )

    r.detail_fixes = {
        "Amortissement": r.amortissement_annuel,
        "Conducteur (salaire + charges)": r.cout_conducteur_annuel,
        "Crédit / Leasing": r.credit_annuel,
        "Assurance": profil.assurance,
        "Taxe à l'essieu": profil.taxe_essieu,
        "Contrôle technique": profil.controle_technique,
        "Parking / Stationnement": profil.parking_stationnement,
        "Frais de structure": profil.frais_structure,
    }

    # --- Coûts variables ---
    r.cout_carburant_annuel = (
        (profil.conso_carburant / 100)
        * profil.km_annuel
        * profil.prix_carburant
    )

    r.total_couts_variables = (
        r.cout_carburant_annuel
        + profil.cout_pneumatiques
        + profil.cout_entretien_reparation
        + profil.cout_peages_annuel
    )

    r.detail_variables = {
        "Carburant": r.cout_carburant_annuel,
        "Pneumatiques": profil.cout_pneumatiques,
        "Entretien / Réparation": profil.cout_entretien_reparation,
        "Péages": profil.cout_peages_annuel,
    }

    # --- Totaux ---
    r.cout_total_annuel = r.total_couts_fixes + r.total_couts_variables

    # --- Coût au km ---
    km = max(profil.km_annuel, 1)
    r.cout_km_brut = r.cout_total_annuel / km

    r.km_facturable = km * (1 - profil.taux_retour_vide / 100)
    r.cout_km_reel = r.cout_total_annuel / max(r.km_facturable, 1)

    # --- Prix minimum ---
    r.prix_min_km = r.cout_km_reel * (1 + profil.marge_souhaitee / 100)

    # --- Méthode trinôme CNR ---
    r.ck = r.total_couts_variables / km
    heures_annuelles = profil.jours_exploitation * profil.heures_conduite_jour
    r.cc = r.cout_conducteur_annuel / max(heures_annuelles, 1)
    r.cj = (r.total_couts_fixes - r.cout_conducteur_annuel) / max(profil.jours_exploitation, 1)

    # --- Coût journalier ---
    r.cout_journalier = r.cout_total_annuel / max(profil.jours_exploitation, 1)

    return r


# ============================================================
# MODULE 2 — Rentabilité par Tournée
# ============================================================

@dataclass
class Tournee:
    """Données d'une tournée."""
    date_tournee: str = ""
    depart: str = ""
    arrivee: str = ""
    km_total: float = 0.0
    km_en_charge: float = 0.0
    nb_heures: float = 0.0
    nb_jours: float = 1.0
    prix_facture: float = 0.0
    peages: float = 0.0
    frais_deplacement: float = 0.0
    client: str = ""
    type_marchandise: str = ""


@dataclass
class ResultatTournee:
    """Résultats de l'analyse de rentabilité d'une tournée."""
    cout_tournee: float = 0.0
    marge_brute: float = 0.0
    taux_marge: float = 0.0
    revenu_par_km: float = 0.0
    cout_par_km: float = 0.0
    marge_par_km: float = 0.0
    indicateur: str = ""    # 🟢 🟡 🟠 🔴
    label: str = ""         # Texte descriptif


def calculer_rentabilite_tournee(
    tournee: Tournee,
    resultat_km: ResultatCoutKm
) -> ResultatTournee:
    """Calcule la rentabilité d'une tournée individuelle."""

    r = ResultatTournee()

    # Coût de la tournée (méthode trinôme)
    r.cout_tournee = (
        resultat_km.ck * tournee.km_total
        + resultat_km.cc * tournee.nb_heures
        + resultat_km.cj * tournee.nb_jours
        + tournee.peages
        + tournee.frais_deplacement
    )

    # Marge
    r.marge_brute = tournee.prix_facture - r.cout_tournee
    r.taux_marge = (
        (r.marge_brute / tournee.prix_facture * 100)
        if tournee.prix_facture > 0 else 0
    )

    # Par km
    km_charge = max(tournee.km_en_charge, 1)
    km_total = max(tournee.km_total, 1)
    r.revenu_par_km = tournee.prix_facture / km_charge
    r.cout_par_km = r.cout_tournee / km_total
    r.marge_par_km = r.revenu_par_km - r.cout_par_km

    # Indicateur
    if r.taux_marge > 15:
        r.indicateur = "🟢"
        r.label = "Très rentable"
    elif r.taux_marge > 5:
        r.indicateur = "🟡"
        r.label = "Rentable"
    elif r.taux_marge > 0:
        r.indicateur = "🟠"
        r.label = "Seuil critique"
    else:
        r.indicateur = "🔴"
        r.label = "Non rentable"

    return r


def calculer_seuil_rentabilite(
    cf_annuel: float,
    tournees_resultats: list[ResultatTournee],
    tournees_prix: list[float],
) -> dict:
    """Calcule le seuil de rentabilité (point mort)."""

    if not tournees_resultats:
        return {
            "nb_tournees_seuil_mensuel": 0,
            "ca_seuil_annuel": 0,
            "marge_moyenne": 0,
            "taux_marge_moyen": 0,
        }

    cf_mensuel = cf_annuel / 12
    marge_moyenne = sum(r.marge_brute for r in tournees_resultats) / len(tournees_resultats)
    taux_marge_moyen = sum(r.taux_marge for r in tournees_resultats) / len(tournees_resultats)

    nb_tournees_seuil = cf_mensuel / marge_moyenne if marge_moyenne > 0 else float('inf')
    ca_seuil = cf_annuel / (taux_marge_moyen / 100) if taux_marge_moyen > 0 else float('inf')

    return {
        "nb_tournees_seuil_mensuel": round(nb_tournees_seuil, 1),
        "ca_seuil_annuel": round(ca_seuil, 2),
        "marge_moyenne": round(marge_moyenne, 2),
        "taux_marge_moyen": round(taux_marge_moyen, 2),
    }


# ============================================================
# MODULE 3 — Analyse Financière
# ============================================================

@dataclass
class BilanSimplif:
    """Bilan simplifié du transporteur."""
    immobilisations_nettes: float = 0.0
    stocks: float = 0.0
    creances_clients: float = 0.0
    tresorerie_actif: float = 0.0
    capitaux_propres: float = 0.0
    dettes_lt: float = 0.0
    dettes_fournisseurs: float = 0.0
    dettes_fiscales_sociales: float = 0.0
    decouverts_bancaires: float = 0.0
    # Compte de résultat
    chiffre_affaires: float = 0.0
    charges_exploitation: float = 0.0
    resultat_exploitation: float = 0.0
    charges_financieres: float = 0.0
    resultat_net: float = 0.0
    dotations_amortissements: float = 0.0
    nombre_camions: int = 1
    km_total_flotte: float = 0.0
    jours_roules: int = 0
    jours_exploitation: int = 220


@dataclass
class ResultatFinancier:
    """Résultats de l'analyse financière complète."""
    # Équilibre financier
    frng: float = 0.0
    bfr: float = 0.0
    tresorerie_nette: float = 0.0
    # Rentabilité
    marge_exploitation_pct: float = 0.0
    rentabilite_nette_pct: float = 0.0
    rentabilite_cp_pct: float = 0.0
    # Structure
    ratio_endettement: float = 0.0
    ratio_autonomie_pct: float = 0.0
    # Liquidité
    ratio_liquidite_generale: float = 0.0
    ratio_liquidite_immediate: float = 0.0
    # Délais
    dso: float = 0.0
    dpo: float = 0.0
    # CAF
    caf: float = 0.0
    # KPIs transport
    ca_par_camion: float = 0.0
    cout_par_camion: float = 0.0
    marge_par_camion: float = 0.0
    ca_par_km: float = 0.0
    taux_utilisation_flotte_pct: float = 0.0
    # Alertes
    alertes: list = field(default_factory=list)


def analyser_bilan(bilan: BilanSimplif) -> ResultatFinancier:
    """Analyse financière complète à partir du bilan simplifié."""

    r = ResultatFinancier()

    # --- Équilibre financier ---
    ressources_stables = bilan.capitaux_propres + bilan.dettes_lt
    emplois_stables = bilan.immobilisations_nettes
    r.frng = ressources_stables - emplois_stables

    actif_circulant = bilan.stocks + bilan.creances_clients
    passif_circulant = bilan.dettes_fournisseurs + bilan.dettes_fiscales_sociales
    r.bfr = actif_circulant - passif_circulant

    r.tresorerie_nette = r.frng - r.bfr

    # --- Rentabilité ---
    ca = max(bilan.chiffre_affaires, 1)
    r.marge_exploitation_pct = (bilan.resultat_exploitation / ca) * 100
    r.rentabilite_nette_pct = (bilan.resultat_net / ca) * 100
    cp = max(bilan.capitaux_propres, 1)
    r.rentabilite_cp_pct = (bilan.resultat_net / cp) * 100

    # --- Structure ---
    r.ratio_endettement = bilan.dettes_lt / cp if bilan.capitaux_propres > 0 else float('inf')
    total_passif_stable = bilan.capitaux_propres + bilan.dettes_lt
    r.ratio_autonomie_pct = (
        (bilan.capitaux_propres / total_passif_stable * 100)
        if total_passif_stable > 0 else 0
    )

    # --- Liquidité ---
    dettes_ct = (
        bilan.dettes_fournisseurs
        + bilan.dettes_fiscales_sociales
        + bilan.decouverts_bancaires
    )
    if dettes_ct > 0:
        r.ratio_liquidite_generale = (
            (bilan.stocks + bilan.creances_clients + bilan.tresorerie_actif)
            / dettes_ct
        )
        r.ratio_liquidite_immediate = bilan.tresorerie_actif / dettes_ct
    else:
        r.ratio_liquidite_generale = float('inf')
        r.ratio_liquidite_immediate = float('inf')

    # --- Délais ---
    r.dso = (bilan.creances_clients / ca) * 365 if ca > 0 else 0
    charges = max(bilan.charges_exploitation, 1)
    r.dpo = (bilan.dettes_fournisseurs / charges) * 365

    # --- CAF ---
    r.caf = bilan.resultat_net + bilan.dotations_amortissements

    # --- KPIs transport ---
    nb = max(bilan.nombre_camions, 1)
    r.ca_par_camion = bilan.chiffre_affaires / nb
    r.cout_par_camion = bilan.charges_exploitation / nb
    r.marge_par_camion = r.ca_par_camion - r.cout_par_camion
    r.ca_par_km = bilan.chiffre_affaires / max(bilan.km_total_flotte, 1)
    r.taux_utilisation_flotte_pct = (
        bilan.jours_roules
        / max(nb * bilan.jours_exploitation, 1)
        * 100
    )

    # --- Alertes ---
    if r.tresorerie_nette < 0:
        r.alertes.append(("🔴", "Trésorerie nette négative — risque de tension de trésorerie"))
    if r.dso > 30:
        r.alertes.append(("🔴", f"DSO de {r.dso:.0f} jours — non-conformité loi Gayssot (max 30j)"))
    if r.ratio_endettement > 2:
        r.alertes.append(("🟠", f"Ratio d'endettement à {r.ratio_endettement:.1f} — vigilance"))
    if r.marge_exploitation_pct < 2:
        r.alertes.append(("🟠", f"Marge d'exploitation à {r.marge_exploitation_pct:.1f}% — sous la moyenne secteur (2-3%)"))
    if r.ratio_liquidite_generale < 1:
        r.alertes.append(("🔴", "Ratio de liquidité < 1 — risque de cessation de paiement"))
    if r.frng < 0:
        r.alertes.append(("🔴", "FRNG négatif — insuffisance de financement stable"))

    if not r.alertes:
        r.alertes.append(("🟢", "Tous les indicateurs sont au vert"))

    return r
