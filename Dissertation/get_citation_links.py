citations = """Control of senescence by CXCR2 and its ligands
A practical tool for maximal information coefficient analysis
Non-specific immunity in aging: deficiency of monocyte and polymorphonuclear cell-mediated functions
Naturally occurring p16 Ink4a -positive cells shorten healthy lifespan
A novel B cell population revealed by a CD38/CD24 gating strategy: CD38 - CD24 - B cells in centenarian offspring and elderly people
Carvalho-Bürguer, M - Análise Transcricional de RNAs Não Codificadores Longos em Pacientes com Dengue
Density-Based Clustering Based on Hierarchical Density Estimates
Cellular senescence: when bad things happen to good cells
B cell immunosenescence in the elderly and in centenarians
Senescence-associated secretory phenotypes reveal cell-nonautonomous functions of oncogenic RAS and the p53 tumor suppressor
The senescence-associated secretory phenotype: the dark side of tumor suppression
CRAN - Package TTR
Gene Time E{chi}pression Warper: a tool for alignment, template matching and visualization of gene expression time series
Reactome: a database of reactions, pathways and biological processes
Senescent cells as a source of inflammatory factors for tumor progression
GEOquery: a bridge between the Gene Expression Omnibus GEO and BioConductor
DE MAGALHÃ P
Density Based Clustering of Applications with Noise DBSCAN and Related Algorithms \R package dbscan version 1
TGF-beta signaling is required for the function of insulin-reactive T regulatory cells
Gene Expression Omnibus: NCBI gene expression and hybridization array data repository
Wnt antagonist SFRP1 functions as a secreted mediator of senescence
TNF receptor 2 and disease: autoimmunity and regenerative medicine
A new definition of aging? Frontiers in 3, p
Inflammatory networks during cellular senescence: causes and consequences
Immunosenescence and Inflamm-Aging As Two Sides of the Same Coin: Friends or Foes? Frontiers in 8, p
Immunosenescence and infectious diseases
Oncogene-induced senescence: the bright and dark side of the response
A sudden decline in active membrane-bound TGF-beta impairs both T regulatory cell function and protection against autoimmune diabetes
The free radical theory of aging: effect of age on serum copper levels
GENCODE: the reference human genome annotation for The ENCODE Project
CD4 T cell memory derived from young naive cells functions well into old age, but memory generated from aged naive cells functions poorly
Health and Economic Costs of Chronic Disease \| About Chronic Disease \| Chronic Disease Prevention and Health Promotion \| CDC
Cutting edge: TGF-beta signaling is required for the in vivo expansion and immunosuppressive capacity of regulatory CD4+CD25+ T cells
IBGE: Instituto Brasileiro de Geografia e Estatística
Age gene expression and coexpression progressive signatures in peripheral blood leukocytes
Minimum prediction residual principle applied to speech recognition
The landscape of long noncoding RNAs in the human transcriptome
Adjusting batch effects in microarray expression data using empirical Bayes methods
Systems biology: a brief overview
ArrayExpress update--simplifying data submissions
The essence of senescence
Enrichr: a comprehensive gene set enrichment analysis web server 2016 update
Functional regulatory T cells accumulate in aged hosts and promote chronic infectious disease reactivation
The hallmarks of aging
Interleukin-6 in aging and chronic disease: a magnificent pathway
Survival after the age of 80 in the United States, Sweden, France, England, and Japan
Tumour-associated macrophages as a prototypic type II polarised phagocyte population: role in tumour progression
MixMAP: AnR Package for Mixed Modeling of Meta-AnalysisValues in Genetic Association Studies
Local and systemic immune response in nursing-home elderly following intranasal or intramuscular immunization with inactivated influenza vaccine
Cell contact-dependent immunosuppression by CD4 + CD25 + regulatory T cells is mediated by cell surface-bound transforming growth factor beta
The twilight of immunity: emerging concepts in aging of the immune system
Aging and impairment of innate immunity
PI3K/AKT signaling and systemic autoimmunity
Multiplatform single-sample estimates of transcriptional activation
Impaired secretion of interferons by dendritic cells from aged subjects to influenza: role of histone modifications
Plasma cell numbers decrease in bone marrow of old patients
p53 acetylation: regulation and consequences
The origin of the 1918 pandemic influenza virus: a continuing enigma
Detecting novel associations in large data sets
DTW-MIC Coexpression Networks from Time-Course Data
Four faces of cellular senescence
Age is an important determinant in humoral and T cell responses to immunization with hepatitis B surface antigen
IL-4-producing CD8+ T cells with a CD62L++ bright phenotype accumulate in a subgroup of older adults and are associated with the maintenance of intact humoral immunity in old age
Evolution of the immune system in humans from infancy to old age
Cell therapy strategies to combat immunosenescence
STRING v10: protein-protein interaction networks, integrated over the tree of life
Signalling through the high-affinity IgE receptor FcεRI
World population ageing 2015 highlights
CD28 extinction in human T cells: altered functions and the program of T-cell senescence
The role of senescent cells in ageing
Evaluation of IgA1-IgA2 levels in serum and saliva of young and elderly people
visNetwork: Network Visualization using “vis
LNCipedia: a database for annotated human lncRNA transcript sequences and structures
The aging of the immune system
The effect of age on the B-cell repertoire
An immune risk phenotype, cognitive impairment, and survival in very late life: impact of allostatic load in Swedish octogenarian and nonagenarian humans
Senescence and tumour clearance is triggered by p53 restoration in murine liver carcinomas
A general framework for weighted gene co-expression network analysis"""

from time import sleep
import mechanize
url = 'https://scholar.google.com.br/scholar?hl=en&as_sdt=0%2C5&q='

links = {}
for j in range(0,len(citations)):
    title = citations.split('\n')[j]
    page = '+'.join(title.split(' '))

    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent','Firefox')]

    browser.open(url+page)
    assert browser.viewing_html()
    # links = browser.find_link()
    links[title] = browser.links()
    print(links[title])
    print('Remaining: '+str(len(citations)-j))
    sleep(3)

j = 1
title = citations.split('\n')[j]
links[title]

page_link = links[title]
names = ['absolute_url','attrs','base_url','tag','text','url']
set([l.base_url for l in page_link])
