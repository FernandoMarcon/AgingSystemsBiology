# Overall Methodology

Microarray transcriptomics data from the blood of healthy individuals were obtained from public databases and pre-processed using the R and Bash programming languages. All platforms have been re-annotated to the most current versions of the human genome and non-coding RNA database. Then, all samples were used to create a new dataset consisting of representative samples of each age and transcribed in common to all platforms. Each transcript was treated as a time series in the following analyses, with each time point representing an age.

‌ First, highly age-correlated transcripts \(AgingGenes\) were identified. Each transcript was classified according to its type of correlation, which could be positive linear, negative or non-linear. Then, a co-expression analysis was performed to build a network \(AgingNet\) in which its nodes are represented by transcripts and their relationships are represented by the similarity between their expression profiles. Once the network was built, subgroups of genes with similar expression profiles over the ages were identified.

‌ All AgingGenes classes, as well as the AgingNet modules, were submitted to a pathway enrichment analysis, to elucidate the possible molecular mechanisms they would be representing. In addition, a Change-point Detection analysis was performed to identify at which times during life such molecular programs present changes in their transcriptional behaviour.



![Figura 3.1. Fluxograma de an&#xE1;lise. Resumo dos processos e an&#xE1;lises realizadas no trabalho.](https://lh6.googleusercontent.com/HZnng09X-jFxk0b17fWYvjtrMqCqHH-emS6AntyXjKAiEXrisbIdt19UCA90QQ7UNtjDHQQiLwvtkJvQtunrhHvRgCpnsfL2ukd3f4Mrs3PSMOuBhK_1z1jOhWXBKFA9RgcoZ3w0=s0)



  
  


 

