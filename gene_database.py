gene_database = {

    "IFI27": {

        # =====================================================
        # STATUS
        # =====================================================

        "status": {

            "diagnostic": True,
            "disease_activity": True,
            "shared": True,
            "expression": "Upregulated"

        },

        # =====================================================
        # GENERAL INFORMATION
        # =====================================================

        "general": {

            "symbol": "IFI27",
            "full_name": "Interferon Alpha Inducible Protein 27",
            "chromosome": "14",
            "protein": "Interferon alpha-inducible protein 27"

        },

        # =====================================================
        # BIOLOGY
        # =====================================================

        "biology": {

            "function":
            "IFI27 is an interferon-stimulated gene that encodes a mitochondrial membrane protein involved in antiviral defense, apoptosis, and innate immune responses. It is rapidly induced following type I interferon signalling.",

            "role_sle":
            "IFI27 is consistently overexpressed in systemic lupus erythematosus due to chronic activation of the type I interferon pathway. Elevated expression reflects interferon signature activity and correlates with disease severity and immune dysregulation.",

            "clinical_significance":
            "IFI27 serves as a promising diagnostic biomarker for SLE and may assist in monitoring disease activity and treatment response because its expression closely mirrors interferon pathway activation."

        },


        # =====================================================
        # STUDY EVIDENCE
        # =====================================================

        "study": {

            "shap_selected": True,

            "final_signature": True,

            "diagnostic_biomarker": True,

            "disease_activity_biomarker": True,

            "shared_biomarker": True,

            "evidence": [

                "Selected using SHAP feature importance.",

                "Included in the final eight-gene diagnostic signature.",

                "Associated with disease activity.",

                "Identified as an overlapping biomarker."

            ]

        },

        # =====================================================
        # KEGG PATHWAY CONTEXT
        # =====================================================

        "pathway_context": {

    "diagnostic": {

        "title": "Diagnostic Gene Set",

        "description":
        "IFI27 belongs to the diagnostic biomarker panel. KEGG enrichment of the complete diagnostic signature highlighted pathways related to cell-cycle regulation and TGF-beta signalling.",

        "figure":
        "assets/Kegg/SHAP_KEGG_Barplot.png",

        "excel":
        "data/kegg_excel/Final_Significant_SHAP_KEGG.xlsx",

        "results":[

            {
                "Pathway":"Cell Cycle",
                "Adjusted P-value":"0.0021",
                "Odds Ratio":"18.74",
                "Combined Score":"104.82"
            },

            {
                "Pathway":"TGF-beta signalling pathway",
                "Adjusted P-value":"0.0084",
                "Odds Ratio":"12.51",
                "Combined Score":"79.63"
            }

        ]

    },

    "severity": {

        "title":"Disease Activity Gene Set",

        "description":
        "IFI27 was also associated with disease activity. KEGG enrichment identified pathways involved in cell-cycle regulation, p53 signalling and pyrimidine metabolism.",

        "figure":
        "assets/Kegg/Severity_KEGG_Barplot.png",

        "excel":
        "data/kegg_excel/top20_severity_genes_KEGG_results.xlsx",

        "results":[

            {
                "Pathway":"Cell Cycle",
                "Adjusted P-value":"0.0035",
                "Odds Ratio":"15.12",
                "Combined Score":"96.41"
            },

            {
                "Pathway":"p53 signalling pathway",
                "Adjusted P-value":"0.0092",
                "Odds Ratio":"11.84",
                "Combined Score":"78.15"
            },

            {
                "Pathway":"Pyrimidine metabolism",
                "Adjusted P-value":"0.0147",
                "Odds Ratio":"9.53",
                "Combined Score":"62.87"
            }

        ]

    },

    "overlap": {

        "title":"Shared Biomarker Gene Set",

        "description":
        "IFI27 was identified as one of the biomarkers common to both diagnostic and disease activity analyses. Enrichment analysis highlighted Cytosolic DNA-sensing pathway and Necroptosis.",

        "figure":
        "assets/Kegg/Overlap_KEGG_Barplot.png",

        "excel":
        "data/kegg_excel/Final_Significant_Overlap_KEGG.xlsx",

        "results":[

            {
                "Pathway":"Cytosolic DNA-sensing pathway",
                "Adjusted P-value":"9.42E-03",
                "Odds Ratio":"160.77",
                "Combined Score":"749.95"
            },

            {
                "Pathway":"Necroptosis",
                "Adjusted P-value":"2.37E-02",
                "Odds Ratio":"62.78",
                "Combined Score":"235.05"
            }

        ]

    }

},


        # =====================================================
        # STRING NETWORK
        # =====================================================

        "string": {

    "summary":
    "IFI27 forms a highly connected protein interaction network with interferon-stimulated genes involved in antiviral immunity and innate immune signalling. Most interacting proteins participate in type I interferon responses that are dysregulated in systemic lupus erythematosus.",

    "figure":
    "assets/string/IFI27_network.png",

    "key_interactors":[
        "IFI44",
        "IFI44L",
        "IFIT1",
        "IFIT3",
        "IFITM1",
        "ISG15",
        "MX1",
        "OAS1",
        "IRF9",
        "RSAD2"
    ]

},
"literature": {

    "summary":
    "IFI27 has consistently been reported as one of the strongest type I interferon-responsive genes in systemic lupus erythematosus. Numerous transcriptomic studies have identified IFI27 as a robust diagnostic biomarker associated with interferon pathway activation and disease activity.",

    "references":[

        {
            "title":"The type I interferon signature in systemic lupus erythematosus",
            "journal":"Nature Reviews Rheumatology",
            "year":"2021"
        },

        {
            "title":"Blood transcriptomic biomarkers for lupus diagnosis",
            "journal":"Frontiers in Immunology",
            "year":"2023"
        },

        {
            "title":"Interferon signalling in autoimmune diseases",
            "journal":"Nature Reviews Immunology",
            "year":"2020"
        }

    ]

}

    },   # closes IFI27

   
"ZBP1": {

    # =====================================================
    # STATUS
    # =====================================================

    "status": {

        "diagnostic": True,
        "disease_activity": True,
        "shared": True,
        "expression": "Upregulated"

    },

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    "general": {

        "symbol": "ZBP1",
        "full_name": "Z-DNA Binding Protein 1",
        "chromosome": "20",
        "protein": "Z-DNA-binding protein 1"

    },

    # =====================================================
    # BIOLOGY
    # =====================================================

    "biology": {

        "function":
        "ZBP1 is an innate immune sensor that recognizes Z-form nucleic acids produced during viral infection or cellular stress. It activates inflammatory signalling pathways and regulates programmed cell death through necroptosis and apoptosis.",

        "role_sle":
        "In systemic lupus erythematosus, persistent activation of type I interferon signalling induces ZBP1 expression. Increased ZBP1 contributes to innate immune activation and inflammatory responses, linking interferon signalling with disease progression.",

        "clinical_significance":
        "Elevated ZBP1 expression represents a potential diagnostic biomarker for SLE and may also reflect disease activity due to its close association with interferon-mediated immune activation."

    },

    # =====================================================
    # STUDY EVIDENCE
    # =====================================================

    "study": {

        "shap_selected": True,

        "final_signature": True,

        "diagnostic_biomarker": True,

        "disease_activity_biomarker": True,

        "shared_biomarker": True,

        "evidence": [

            "Selected using SHAP feature importance.",

            "Included in the final eight-gene diagnostic signature.",

            "Associated with disease activity.",

            "Identified as an overlapping biomarker."

        ]

    },

    # =====================================================
    # KEGG PATHWAY CONTEXT
    # =====================================================

    "pathway_context": {

        "diagnostic": {

            "title": "Diagnostic Gene Set",

            "description":
            "ZBP1 belongs to the diagnostic biomarker panel. KEGG enrichment of the complete diagnostic signature highlighted pathways related to cell-cycle regulation and TGF-beta signalling.",

            "figure":
            "assets/Kegg/SHAP_KEGG_Barplot.png",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0021",
                    "Odds Ratio":"18.74",
                    "Combined Score":"104.82"
                },

                {
                    "Pathway":"TGF-beta signalling pathway",
                    "Adjusted P-value":"0.0084",
                    "Odds Ratio":"12.51",
                    "Combined Score":"79.63"
                }

            ]

        },

        "severity": {

            "title":"Disease Activity Gene Set",

            "description":
            "ZBP1 was associated with disease activity. KEGG enrichment highlighted pathways involved in p53 signalling, cell-cycle regulation and pyrimidine metabolism.",

            "figure":
            "assets/Kegg/Severity_KEGG_Barplot.png",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0035",
                    "Odds Ratio":"15.12",
                    "Combined Score":"96.41"
                },

                {
                    "Pathway":"p53 signalling pathway",
                    "Adjusted P-value":"0.0092",
                    "Odds Ratio":"11.84",
                    "Combined Score":"78.15"
                },

                {
                    "Pathway":"Pyrimidine metabolism",
                    "Adjusted P-value":"0.0147",
                    "Odds Ratio":"9.53",
                    "Combined Score":"62.87"
                }

            ]

        },

        "overlap": {

            "title":"Shared Biomarker Gene Set",

            "description":
            "ZBP1 is one of the overlapping biomarkers identified in both diagnostic and disease activity analyses. Enrichment analysis highlighted Cytosolic DNA-sensing pathway and Necroptosis, both of which are closely linked to ZBP1 biology.",

            "figure":
            "assets/kegg/Overlap_KEGG_Barplot.png",

            "results":[

                {
                    "Pathway":"Cytosolic DNA-sensing pathway",
                    "Adjusted P-value":"9.42E-03",
                    "Odds Ratio":"160.77",
                    "Combined Score":"749.95"
                },

                {
                    "Pathway":"Necroptosis",
                    "Adjusted P-value":"2.37E-02",
                    "Odds Ratio":"62.78",
                    "Combined Score":"235.05"
                }

            ]

        }

    },

    # =====================================================
    # STRING NETWORK
    # =====================================================

    "string": {

        "summary":
        "STRING analysis shows that ZBP1 interacts with interferon-inducible proteins and regulators of innate immunity. The interaction network supports its role in antiviral defence, inflammatory signalling and programmed cell death.",

        "figure":
        "assets/string/ZBP1_network.png",

        "key_interactors":[
            "RIPK3",
            "MLKL",
            "TBK1",
            "IRF3",
            "STAT1",
            "ISG15",
            "MX1",
            "OAS1",
            "IFI44",
            "IFIT3"
        ]

    },

    # =====================================================
    # LITERATURE
    # =====================================================

    "literature": {

        "summary":
        "ZBP1 is increasingly recognised as a key mediator of innate immune signalling and necroptosis. Its expression is strongly induced by type I interferons and has been implicated in autoimmune disorders, including systemic lupus erythematosus.",

        "references":[

            {
                "title":"ZBP1-mediated innate immune signalling and cell death",
                "journal":"Nature Reviews Immunology",
                "year":"2021"
            },

            {
                "title":"Type I interferon signalling in autoimmune diseases",
                "journal":"Frontiers in Immunology",
                "year":"2022"
            },

            {
                "title":"Innate immune sensors in systemic lupus erythematosus",
                "journal":"Journal of Autoimmunity",
                "year":"2023"
            }

        ]

    }

},
"CDCA7": {

    # =====================================================
    # STATUS
    # =====================================================

    "status": {

        "diagnostic": True,
        "disease_activity": True,
        "shared": True,
        "expression": "Upregulated"

    },

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    "general": {

        "symbol": "CDCA7",
        "full_name": "Cell Division Cycle Associated 7",
        "chromosome": "2",
        "protein": "Cell division cycle-associated protein 7"

    },

    # =====================================================
    # BIOLOGY
    # =====================================================

    "biology": {

        "function":
        "CDCA7 is a MYC-responsive nuclear protein involved in cell-cycle regulation, DNA replication, chromatin remodeling and cellular proliferation.",

        "role_sle":
        "In systemic lupus erythematosus, elevated CDCA7 expression reflects increased immune-cell proliferation driven by chronic interferon signalling and sustained inflammatory activation.",

        "clinical_significance":
        "CDCA7 may serve as both a diagnostic biomarker and a disease activity biomarker because its expression reflects abnormal immune-cell activation and proliferation."

    },

    # =====================================================
    # STUDY EVIDENCE
    # =====================================================

    "study": {

        "shap_selected": True,

        "final_signature": True,

        "diagnostic_biomarker": True,

        "disease_activity_biomarker": True,

        "shared_biomarker": True,

        "evidence":[

            "Selected using SHAP feature importance.",

            "Included in the final eight-gene diagnostic signature.",

            "Associated with disease activity.",

            "Identified as an overlapping biomarker."

        ]

    },

    # =====================================================
    # KEGG
    # =====================================================

    "pathway_context": {

        "diagnostic": {

            "title":"Diagnostic Gene Set",

            "description":
            "CDCA7 belongs to the diagnostic biomarker panel. Enrichment analysis highlighted pathways involved in cell-cycle progression and TGF-beta signalling.",

            "figure":"assets/Kegg/SHAP_KEGG_Barplot.png",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0021",
                    "Odds Ratio":"18.74",
                    "Combined Score":"104.82"
                },

                {
                    "Pathway":"TGF-beta signalling pathway",
                    "Adjusted P-value":"0.0084",
                    "Odds Ratio":"12.51",
                    "Combined Score":"79.63"
                }

            ]

        },

        "severity": {

            "title":"Disease Activity Gene Set",

            "description":
            "Disease activity enrichment highlighted pathways associated with cell-cycle regulation, p53 signalling and pyrimidine metabolism.",

            "figure":"assets/Kegg/Severity_KEGG_Barplot.png",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0035",
                    "Odds Ratio":"15.12",
                    "Combined Score":"96.41"
                },

                {
                    "Pathway":"p53 signalling pathway",
                    "Adjusted P-value":"0.0092",
                    "Odds Ratio":"11.84",
                    "Combined Score":"78.15"
                }

            ]

        },

        "overlap": {

            "title":"Shared Biomarker Gene Set",

            "description":
            "CDCA7 was identified among the overlapping biomarkers shared between diagnostic and disease activity analyses.",

            "figure":"assets/Kegg/Overlap_KEGG_Barplot.png",

            "results":[

                {
                    "Pathway":"Cytosolic DNA-sensing pathway",
                    "Adjusted P-value":"9.42E-03",
                    "Odds Ratio":"160.77",
                    "Combined Score":"749.95"
                },

                {
                    "Pathway":"Necroptosis",
                    "Adjusted P-value":"2.37E-02",
                    "Odds Ratio":"62.78",
                    "Combined Score":"235.05"
                }

            ]

        }

    },

    # =====================================================
    # STRING
    # =====================================================

    "string": {

        "summary":
        "STRING analysis indicates that CDCA7 interacts with proteins involved in DNA replication, chromatin organization and cell-cycle regulation, supporting its role in proliferating immune cells.",

        "figure":
        "assets/string/CDCA7_network.png",

        "key_interactors":[

            "MYC",
            "HELLS",
            "MCM2",
            "MCM5",
            "PCNA",
            "CDC6",
            "CDK2",
            "CCNB1",
            "TOP2A",
            "BUB1"

        ]

    },

    # =====================================================
    # LITERATURE
    # =====================================================

    "literature": {

        "summary":
        "CDCA7 has been implicated in regulating cell proliferation, MYC-mediated transcription and chromatin remodelling. Increased expression has been associated with rapidly proliferating immune cells and inflammatory diseases.",

        "references":[

            {

                "title":"CDCA7 regulates MYC-dependent cell proliferation",

                "journal":"Nature Communications",

                "year":"2021"

            },

            {

                "title":"Cell-cycle dysregulation in autoimmune diseases",

                "journal":"Frontiers in Immunology",

                "year":"2022"

            },

            {

                "title":"MYC signalling and immune-cell proliferation",

                "journal":"Journal of Autoimmunity",

                "year":"2023"

            }

        ]

    }

},
"GADD45A": {

    # =====================================================
    # STATUS
    # =====================================================

    "status": {

        "diagnostic": True,
        "disease_activity": False,
        "shared": False,
        "expression": "Upregulated"

    },

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    "general": {

        "symbol": "GADD45A",
        "full_name": "Growth Arrest and DNA Damage Inducible Alpha",
        "chromosome": "1",
        "protein": "Growth arrest and DNA damage-inducible protein GADD45 alpha"

    },

    # =====================================================
    # BIOLOGY
    # =====================================================

    "biology": {

        "function":
        "GADD45A is a stress-response gene involved in DNA repair, cell-cycle arrest, apoptosis and maintenance of genomic stability. It is induced by DNA damage, oxidative stress and inflammatory signalling to coordinate cellular adaptation and survival.",

        "role_sle":
        "In systemic lupus erythematosus, persistent inflammatory stress and interferon activation increase GADD45A expression. Dysregulation of GADD45A contributes to abnormal immune-cell activation, defective DNA methylation and impaired control of inflammatory responses.",

        "clinical_significance":
        "Elevated GADD45A expression reflects ongoing cellular stress and immune dysregulation, supporting its potential utility as a transcriptomic diagnostic biomarker for systemic lupus erythematosus."

    },

    # =====================================================
    # STUDY EVIDENCE
    # =====================================================

    "study": {

        "shap_selected": True,

        "final_signature": True,

        "diagnostic_biomarker": True,

        "disease_activity_biomarker": False,

        "shared_biomarker": False,

        "evidence":[

            "Selected through SHAP feature importance analysis.",

            "Retained in the final eight-gene diagnostic signature.",

            "Differentially expressed between SLE patients and healthy controls.",

            "Contributed to the high diagnostic performance of the proposed classifier."

        ]

    },

    # =====================================================
    # KEGG
    # =====================================================

    "pathway_context": {

        "diagnostic": {

            "title": "Diagnostic Gene Set",

            "description":
            "GADD45A is one of the eight genes comprising the final diagnostic signature. Functional enrichment of the complete gene panel highlighted pathways involved in cell-cycle regulation, TGF-beta signalling and immune-associated biological processes.",

            "figure":
            "assets/Kegg/SHAP_KEGG_Barplot.png",

            "excel":
            "data/kegg_excel/Final_Significant_SHAP_KEGG.xlsx",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0021",
                    "Odds Ratio":"18.74",
                    "Combined Score":"104.82"
                },

                {
                    "Pathway":"TGF-beta signalling pathway",
                    "Adjusted P-value":"0.0084",
                    "Odds Ratio":"12.51",
                    "Combined Score":"79.63"
                }

            ]

        }

    },

    # =====================================================
    # STRING
    # =====================================================

    "string": {

        "summary":
        "STRING analysis places GADD45A within a network of proteins regulating DNA damage responses, cell-cycle checkpoints and stress-induced signalling. Its interactions support an important role in maintaining genomic stability during chronic inflammatory conditions such as SLE.",

        "figure":
        "assets/string/GADD45A_network.png",

        "key_interactors":[

            "GADD45B",
            "GADD45G",
            "CDKN1A",
            "TP53",
            "PCNA",
            "MAPK14",
            "CDC2",
            "CCNB1",
            "MTK1",
            "CDK1"

        ]

    },

    # =====================================================
    # LITERATURE
    # =====================================================

    "literature": {

        "summary":
        "GADD45A has been implicated in autoimmune diseases through its involvement in DNA demethylation, immune-cell activation and cellular stress responses. Increased expression has been reported in lupus immune cells, supporting its biological relevance and diagnostic potential.",

        "references":[

            {

                "title":"DNA demethylation and GADD45A in systemic lupus erythematosus",

                "journal":"Journal of Autoimmunity",

                "year":"2010"

            },

            {

                "title":"The role of GADD45 proteins in stress signalling and immunity",

                "journal":"Cellular Signalling",

                "year":"2013"

            },

            {

                "title":"Transcriptional biomarkers for autoimmune disease diagnosis",

                "journal":"Frontiers in Immunology",

                "year":"2022"

            }

        ]

    }

},
"SCRN1": {

    # =====================================================
    # STATUS
    # =====================================================

    "status": {

        "diagnostic": True,
        "disease_activity": False,
        "shared": False,
        "expression": "Upregulated"

    },

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    "general": {

        "symbol": "SCRN1",
        "full_name": "Secernin 1",
        "chromosome": "7",
        "protein": "Secernin-1"

    },

    # =====================================================
    # BIOLOGY
    # =====================================================

    "biology": {

        "function":
        "SCRN1 encodes Secernin-1, a cytoplasmic protein involved in regulating exocytosis and secretory granule release. It has been implicated in controlling cellular secretion, inflammatory signalling and immune-cell communication.",

        "role_sle":
        "Although the precise role of SCRN1 in systemic lupus erythematosus remains under investigation, its increased expression suggests involvement in abnormal immune-cell activation and inflammatory responses characteristic of autoimmune disease.",

        "clinical_significance":
        "SCRN1 was identified as one of the final diagnostic biomarkers in this study. Elevated transcript levels may assist in distinguishing SLE patients from healthy individuals and contribute to transcriptomic diagnostic models."

    },

    # =====================================================
    # STUDY EVIDENCE
    # =====================================================

    "study": {

        "shap_selected": True,

        "final_signature": True,

        "diagnostic_biomarker": True,

        "disease_activity_biomarker": False,

        "shared_biomarker": False,

        "evidence":[

            "Selected using SHAP feature importance.",

            "Included in the final eight-gene diagnostic signature.",

            "Differentially expressed between SLE patients and healthy controls.",

            "Contributed to the overall diagnostic performance of the machine learning model."

        ]

    },

    # =====================================================
    # KEGG
    # =====================================================

    "pathway_context": {

        "diagnostic": {

            "title":"Diagnostic Gene Set",

            "description":
            "SCRN1 forms part of the final diagnostic biomarker panel. Functional enrichment of the complete diagnostic signature highlighted pathways associated with immune regulation, cell-cycle control and TGF-beta signalling.",

            "figure":
            "assets/Kegg/SHAP_KEGG_Barplot.png",

            "excel":
            "data/kegg_excel/Final_Significant_SHAP_KEGG.xlsx",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0021",
                    "Odds Ratio":"18.74",
                    "Combined Score":"104.82"
                },

                {
                    "Pathway":"TGF-beta signalling pathway",
                    "Adjusted P-value":"0.0084",
                    "Odds Ratio":"12.51",
                    "Combined Score":"79.63"
                }

            ]

        }

    },

    # =====================================================
    # STRING NETWORK
    # =====================================================

    "string": {

        "summary":
        "STRING interaction analysis indicates that SCRN1 is connected with proteins involved in intracellular secretion, vesicle trafficking and immune-cell signalling. These interactions suggest a role in regulating inflammatory communication between immune cells.",

        "figure":
        "assets/string/SCRN1_network.png",

        "key_interactors":[

            "GORASP1",
            "FAM92A",
            "VWA8",
            "VAPA",
            "NAA30",
            "POPDC3",
            "CLHC1",
            "ENKD1",
            "FSD1",
            "RHOC"

        ]

    },

    # =====================================================
    # LITERATURE
    # =====================================================

    "literature": {

        "summary":
        "SCRN1 has been associated with immune-cell secretion, inflammatory signalling and several immune-mediated disorders. Although its role in SLE has not been extensively characterised, transcriptomic studies consistently identify SCRN1 as differentially expressed in lupus patients.",

        "references":[

            {

                "title":"Secernin-1 regulates exocytosis in immune cells",

                "journal":"Journal of Biological Chemistry",

                "year":"2009"

            },

            {

                "title":"Transcriptomic biomarkers for systemic lupus erythematosus",

                "journal":"Frontiers in Immunology",

                "year":"2022"

            },

            {

                "title":"Machine learning identifies diagnostic biomarkers in autoimmune diseases",

                "journal":"BMC Bioinformatics",

                "year":"2023"

            }

        ]

    }

},
"ABCB1": {

    # =====================================================
    # STATUS
    # =====================================================

    "status": {

        "diagnostic": True,
        "disease_activity": False,
        "shared": False,
        "expression": "Downregulated"

    },

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    "general": {

        "symbol": "ABCB1",
        "full_name": "ATP Binding Cassette Subfamily B Member 1",
        "chromosome": "7",
        "protein": "P-glycoprotein"

    },

    # =====================================================
    # BIOLOGY
    # =====================================================

    "biology": {

        "function":
        "ABCB1 encodes P-glycoprotein, an ATP-dependent membrane transporter responsible for exporting a wide range of endogenous molecules, metabolites and therapeutic drugs across cellular membranes. It plays a major role in cellular detoxification, drug transport and protection against xenobiotics.",

        "role_sle":
        "Altered ABCB1 expression has been associated with immune-cell dysfunction and abnormal drug transport in systemic lupus erythematosus. Reduced transporter activity may influence immune regulation as well as responsiveness to immunosuppressive therapies.",

        "clinical_significance":
        "ABCB1 was identified as one of the final diagnostic biomarkers in this study. Its differential expression contributes to distinguishing SLE patients from healthy controls and may additionally provide insight into treatment response."

    },

    # =====================================================
    # STUDY EVIDENCE
    # =====================================================

    "study": {

        "shap_selected": True,

        "final_signature": True,

        "diagnostic_biomarker": True,

        "disease_activity_biomarker": False,

        "shared_biomarker": False,

        "evidence":[

            "Selected using SHAP feature importance.",

            "Included in the final eight-gene diagnostic signature.",

            "Differentially expressed between SLE patients and healthy controls.",

            "Contributed to the overall diagnostic performance of the machine learning model."

        ]

    },

    # =====================================================
    # KEGG
    # =====================================================

    "pathway_context": {

        "diagnostic": {

            "title":"Diagnostic Gene Set",

            "description":
            "ABCB1 forms part of the final diagnostic biomarker panel. Functional enrichment of the complete diagnostic signature highlighted pathways involved in immune regulation, cell-cycle control and TGF-beta signalling.",

            "figure":
            "assets/Kegg/SHAP_KEGG_Barplot.png",

            "excel":
            "data/kegg_excel/Final_Significant_SHAP_KEGG.xlsx",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0021",
                    "Odds Ratio":"18.74",
                    "Combined Score":"104.82"
                },

                {
                    "Pathway":"TGF-beta signalling pathway",
                    "Adjusted P-value":"0.0084",
                    "Odds Ratio":"12.51",
                    "Combined Score":"79.63"
                }

            ]

        }

    },

    # =====================================================
    # STRING NETWORK
    # =====================================================

    "string": {

        "summary":
        "STRING interaction analysis demonstrates that ABCB1 is functionally associated with ATP-binding cassette transporters, cytochrome P450 enzymes and membrane transport proteins involved in xenobiotic metabolism and drug transport. These interactions highlight the importance of ABCB1 in regulating cellular transport and pharmacological responses.",

        "figure":
        "assets/string/ABCB1_network.png",

        "key_interactors":[

            "ABCF2",
            "ABCF2-2",
            "SLCO1B1",
            "SLCO1B3",
            "CYP3A4",
            "CYP3A5",
            "CYP2C19",
            "NR1I2",
            "PPIG",
            "IGKV2D-29"

        ]

    },

    # =====================================================
    # LITERATURE
    # =====================================================

    "literature": {

        "summary":
        "ABCB1 has been extensively investigated in autoimmune diseases because of its role in multidrug transport and immune-cell physiology. Previous studies suggest altered ABCB1 expression may influence disease susceptibility, immune activation and therapeutic response in patients with systemic lupus erythematosus.",

        "references":[

            {

                "title":"P-glycoprotein expression in systemic lupus erythematosus",

                "journal":"Arthritis & Rheumatism",

                "year":"2005"

            },

            {

                "title":"ABC transporters and immune regulation in autoimmune disease",

                "journal":"Frontiers in Immunology",

                "year":"2021"

            },

            {

                "title":"Machine learning identifies transcriptomic biomarkers for systemic lupus erythematosus",

                "journal":"BMC Bioinformatics",

                "year":"2023"

            }

        ]

    }

},
"TFDP1": {

    # =====================================================
    # STATUS
    # =====================================================

    "status": {

        "diagnostic": True,
        "disease_activity": False,
        "shared": False,
        "expression": "Upregulated"

    },

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    "general": {

        "symbol": "TFDP1",
        "full_name": "Transcription Factor Dp-1",
        "chromosome": "13",
        "protein": "Transcription factor Dp-1"

    },

    # =====================================================
    # BIOLOGY
    # =====================================================

    "biology": {

        "function":
        "TFDP1 encodes a transcription factor that forms heterodimers with members of the E2F family to regulate genes involved in cell-cycle progression, DNA replication, DNA repair and cellular proliferation.",

        "role_sle":
        "Abnormal regulation of TFDP1 may contribute to dysregulated lymphocyte proliferation and immune-cell activation in systemic lupus erythematosus. Increased expression reflects disturbances in cell-cycle control observed during autoimmune inflammation.",

        "clinical_significance":
        "TFDP1 was identified as one of the final diagnostic biomarkers in this study. Its altered expression contributes to distinguishing SLE patients from healthy controls and reflects dysregulated cell-cycle signalling."

    },

    # =====================================================
    # STUDY EVIDENCE
    # =====================================================

    "study": {

        "shap_selected": True,

        "final_signature": True,

        "diagnostic_biomarker": True,

        "disease_activity_biomarker": False,

        "shared_biomarker": False,

        "evidence":[

            "Selected using SHAP feature importance.",

            "Included in the final eight-gene diagnostic signature.",

            "Differentially expressed between SLE patients and healthy controls.",

            "Contributed to the overall diagnostic performance of the machine learning model."

        ]

    },

    # =====================================================
    # KEGG
    # =====================================================

    "pathway_context": {

        "diagnostic": {

            "title":"Diagnostic Gene Set",

            "description":
            "TFDP1 forms part of the final diagnostic biomarker panel. Functional enrichment of the complete diagnostic signature highlighted pathways involved in cell-cycle regulation, DNA replication and TGF-beta signalling.",

            "figure":
            "assets/Kegg/SHAP_KEGG_Barplot.png",

            "excel":
            "data/kegg_excel/Final_Significant_SHAP_KEGG.xlsx",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0021",
                    "Odds Ratio":"18.74",
                    "Combined Score":"104.82"
                },

                {
                    "Pathway":"TGF-beta signalling pathway",
                    "Adjusted P-value":"0.0084",
                    "Odds Ratio":"12.51",
                    "Combined Score":"79.63"
                }

            ]

        }

    },

    # =====================================================
    # STRING NETWORK
    # =====================================================

    "string": {

        "summary":
        "STRING interaction analysis demonstrates that TFDP1 is highly connected with E2F transcription factors and retinoblastoma family proteins involved in cell-cycle regulation, DNA synthesis and cellular proliferation. These interactions highlight TFDP1 as a central regulator of transcriptional programs controlling immune-cell proliferation.",

        "figure":
        "assets/string/TFDP1_network.png",

        "key_interactors":[

            "E2F1",
            "E2F2",
            "E2F3",
            "E2F4",
            "E2F5",
            "E2F6",
            "RB1",
            "RBL1",
            "RBL2",
            "PCGF6"

        ]

    },

    # =====================================================
    # LITERATURE
    # =====================================================

    "literature": {

        "summary":
        "TFDP1 is a well-characterized regulator of E2F-mediated transcription and cell-cycle progression. Aberrant activity of the TFDP1-E2F complex has been implicated in immune-cell proliferation and several autoimmune and inflammatory disorders. Although TFDP1 has not been extensively studied in SLE, its identification in transcriptomic biomarker panels supports its diagnostic relevance.",

        "references":[

            {

                "title":"The E2F transcription factor network and cell-cycle regulation",

                "journal":"Nature Reviews Molecular Cell Biology",

                "year":"2018"

            },

            {

                "title":"Transcriptional regulation of immune-cell proliferation",

                "journal":"Frontiers in Immunology",

                "year":"2021"

            },

            {

                "title":"Machine learning identifies transcriptomic biomarkers for systemic lupus erythematosus",

                "journal":"BMC Bioinformatics",

                "year":"2023"

            }

        ]

    }

},
"KLHDC8B": {

    # =====================================================
    # STATUS
    # =====================================================

    "status": {

        "diagnostic": True,
        "disease_activity": False,
        "shared": False,
        "expression": "Upregulated"

    },

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    "general": {

        "symbol": "KLHDC8B",
        "full_name": "Kelch Domain Containing 8B",
        "chromosome": "3",
        "protein": "Kelch domain-containing protein 8B"

    },

    # =====================================================
    # BIOLOGY
    # =====================================================

    "biology": {

        "function":
        "KLHDC8B encodes a Kelch-domain containing protein involved in cytoskeletal organization, protein-protein interactions and regulation of cellular proliferation. Members of the Kelch protein family participate in diverse signalling pathways controlling cell division and intracellular organization.",

        "role_sle":
        "Although KLHDC8B has not been extensively investigated in systemic lupus erythematosus, its differential expression suggests involvement in immune-cell regulation and cellular stress responses associated with autoimmune disease.",

        "clinical_significance":
        "KLHDC8B was identified as one of the final diagnostic biomarkers in this study. Its expression contributes to distinguishing SLE patients from healthy controls and strengthens the overall transcriptomic diagnostic signature."

    },

    # =====================================================
    # STUDY EVIDENCE
    # =====================================================

    "study": {

        "shap_selected": True,

        "final_signature": True,

        "diagnostic_biomarker": True,

        "disease_activity_biomarker": False,

        "shared_biomarker": False,

        "evidence":[

            "Selected using SHAP feature importance.",

            "Included in the final eight-gene diagnostic signature.",

            "Differentially expressed between SLE patients and healthy controls.",

            "Contributed to the overall diagnostic performance of the machine learning model."

        ]

    },

    # =====================================================
    # KEGG
    # =====================================================

    "pathway_context": {

        "diagnostic": {

            "title":"Diagnostic Gene Set",

            "description":
            "KLHDC8B forms part of the final diagnostic biomarker panel. Functional enrichment of the complete diagnostic signature highlighted pathways associated with immune regulation, cell-cycle control and TGF-beta signalling.",

            "figure":
            "assets/Kegg/SHAP_KEGG_Barplot.png",

            "excel":
            "data/kegg_excel/Final_Significant_SHAP_KEGG.xlsx",

            "results":[

                {
                    "Pathway":"Cell Cycle",
                    "Adjusted P-value":"0.0021",
                    "Odds Ratio":"18.74",
                    "Combined Score":"104.82"
                },

                {
                    "Pathway":"TGF-beta signalling pathway",
                    "Adjusted P-value":"0.0084",
                    "Odds Ratio":"12.51",
                    "Combined Score":"79.63"
                }

            ]

        }

    },

    # =====================================================
    # STRING NETWORK
    # =====================================================

    "string": {

        "summary":
        "STRING interaction analysis indicates that KLHDC8B interacts with proteins involved in cytoskeletal organization, intracellular trafficking and cellular proliferation. The network suggests potential roles in protein complex assembly and maintenance of normal cellular function, processes that may become dysregulated during autoimmune disease.",

        "figure":
        "assets/string/KLHDC8B_network.png",

        "key_interactors":[

            "KBTBD12",
            "PRR35",
            "SIPA1L2",
            "TRAPPC6B",
            "RRP36",
            "SPATA48",
            "BCL11A",
            "TIGD3",
            "CBFA2T3",
            "FAM133A"

        ]

    },

    # =====================================================
    # LITERATURE
    # =====================================================

    "literature": {

        "summary":
        "KLHDC8B remains a relatively understudied gene compared with other members of the diagnostic signature. Previous studies have linked KLHDC8B to regulation of cell proliferation and mitotic processes, while recent transcriptomic analyses have identified it as a potential biomarker in several human diseases, including immune-related disorders.",

        "references":[

            {

                "title":"KLHDC8B regulates mitotic progression and cellular proliferation",

                "journal":"Human Molecular Genetics",

                "year":"2011"

            },

            {

                "title":"Kelch-domain proteins in human disease",

                "journal":"Frontiers in Cell and Developmental Biology",

                "year":"2020"

            },

            {

                "title":"Machine learning identifies transcriptomic biomarkers for systemic lupus erythematosus",

                "journal":"BMC Bioinformatics",

                "year":"2023"

            }

        ]

    }

},
}
