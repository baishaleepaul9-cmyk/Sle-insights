import pandas as pd
import re

# ==========================================================
# LOAD A SINGLE KEGG EXCEL FILE
# ==========================================================

def load_kegg(filepath):
    """
    Load one KEGG enrichment Excel file.
    """
    return pd.read_excel(filepath)


# ==========================================================
# FIND ALL PATHWAYS CONTAINING A GENE
# ==========================================================

def get_gene_pathways(df, gene):

    results = []

    gene = gene.upper().strip()

    for _, row in df.iterrows():

        genes = str(row["Genes"]).upper()

        # Works with ; , / or whitespace separated genes
        genes = [
            g.strip()
            for g in re.split(r"[;,/\s]+", genes)
            if g.strip()
        ]

        if gene in genes:

            results.append({

                "Pathway": row["Term"],

                "Adjusted P-value": row["Adjusted P-value"],

                "Odds Ratio": row["Odds Ratio"],

                "Combined Score": row["Combined Score"]

            })

    return pd.DataFrame(results)


# ==========================================================
# SEARCH ACROSS ALL THREE KEGG DATASETS
# ==========================================================

def search_gene_all_kegg(gene):

    files = {

        "Diagnostic Biomarkers":
            "data/kegg_excel/Final_Significant_SHAP_KEGG.xlsx",

        "Disease Activity":
            "data/kegg_excel/top20_severity_genes_KEGG_results.xlsx",

        "Overlapping Biomarkers":
            "data/kegg_excel/Final_Significant_Overlap_KEGG.xlsx"

    }

    output = {}

    for dataset, filepath in files.items():

        df = load_kegg(filepath)

        pathways = get_gene_pathways(df, gene)

        if not pathways.empty:
            output[dataset] = pathways

    return output

