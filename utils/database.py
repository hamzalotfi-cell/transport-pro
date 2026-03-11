"""
TransportCost Pro - Connexion Supabase
"""
from supabase import create_client
import streamlit as st

SUPABASE_URL = "https://onobjgsjugssiqbslomf.supabase.co"
SUPABASE_KEY = "sb_publishable_3a99zTGiHN_Hft2VBI8G8w_9aOYFj4l"

@st.cache_resource
def get_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def creer_utilisateur(email, nom_entreprise=""):
    sb = get_supabase()
    data = sb.table("users").insert({"email": email, "nom_entreprise": nom_entreprise, "plan": "free"}).execute()
    return data.data[0] if data.data else None

def get_utilisateur(email):
    sb = get_supabase()
    data = sb.table("users").select("*").eq("email", email).execute()
    return data.data[0] if data.data else None

def get_ou_creer_utilisateur(email, nom_entreprise=""):
    user = get_utilisateur(email)
    if not user:
        user = creer_utilisateur(email, nom_entreprise)
    return user

def sauvegarder_vehicule(user_id, profil, immatriculation=""):
    sb = get_supabase()
    data = sb.table("vehicules").insert({
        "user_id": user_id, "nom": profil.nom, "type_vehicule": profil.type_vehicule,
        "immatriculation": immatriculation,
        "prix_achat": profil.prix_achat, "duree_amortissement": profil.duree_amortissement,
        "valeur_residuelle": profil.valeur_residuelle, "km_annuel": profil.km_annuel,
        "conso_carburant": profil.conso_carburant, "prix_carburant": profil.prix_carburant,
        "assurance": profil.assurance, "taxe_essieu": profil.taxe_essieu,
        "controle_technique": profil.controle_technique, "parking": profil.parking_stationnement,
        "credit_mensualite": profil.credit_mensualite, "salaire_brut": profil.salaire_conducteur_brut,
        "charges_sociales_pct": profil.charges_sociales_pct, "frais_structure": profil.frais_structure,
        "pneus": profil.cout_pneumatiques, "entretien": profil.cout_entretien_reparation,
        "peages": profil.cout_peages_annuel, "jours_exploitation": profil.jours_exploitation,
        "heures_conduite": profil.heures_conduite_jour, "taux_retour_vide": profil.taux_retour_vide,
        "marge_souhaitee": profil.marge_souhaitee,
    }).execute()
    return data.data[0] if data.data else None

def get_vehicules(user_id):
    sb = get_supabase()
    data = sb.table("vehicules").select("*").eq("user_id", user_id).execute()
    return data.data

def supprimer_vehicule(vehicule_id):
    sb = get_supabase()
    sb.table("vehicules").delete().eq("id", vehicule_id).execute()

def sauvegarder_tournee(user_id, vehicule_id, tournee, resultat):
    sb = get_supabase()
    data = sb.table("tournees").insert({
        "user_id": user_id, "vehicule_id": vehicule_id,
        "date_tournee": tournee.date_tournee, "depart": tournee.depart,
        "arrivee": tournee.arrivee, "km_total": tournee.km_total,
        "km_en_charge": tournee.km_en_charge, "nb_heures": tournee.nb_heures,
        "nb_jours": tournee.nb_jours, "prix_facture": tournee.prix_facture,
        "peages": tournee.peages, "frais_deplacement": tournee.frais_deplacement,
        "client": tournee.client, "cout_calcule": resultat.cout_tournee,
        "marge_brute": resultat.marge_brute, "taux_marge": resultat.taux_marge,
    }).execute()
    return data.data[0] if data.data else None

def get_tournees(user_id):
    sb = get_supabase()
    data = sb.table("tournees").select("*").eq("user_id", user_id).order("date_tournee", desc=True).execute()
    return data.data

def supprimer_tournee(tournee_id):
    sb = get_supabase()
    sb.table("tournees").delete().eq("id", tournee_id).execute()
