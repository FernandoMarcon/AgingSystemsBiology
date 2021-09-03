# Untitled

### 3.7. Detecção de Pontos de Mudanças em Módulos Relacionados à Idade <a id="docs-internal-guid-c02ca417-7fff-b57f-4771-7c14a58a5279"></a>

Para analisar o comportamento dos dos processos identificados neste trabalho, aplicou-se uma transformação por média móvel com janela de 5 anos à cada transcrito do ageCollapsed. Em seguida, foi calculado o perfil de expressão de cada classe de AgingGenes e sub-módulos da AgingNet através da mediana dos valores de expressão de seus transcritos por idade, obtendo-se uma série temporal de expressão condensada para cada classe/sub-módulo. Posteriormente, realizou-se uma análise de detecção de pontos sobre o perfil de expressão de cada módulo para identificar mudanças importantes em seu comportamento ao longo da vida. Esse teste foi feito através do pacote cpm [\(MATTHEWS; FOULKES, 2015\)](http://f1000.com/work/citation?ids=5964037&pre=&suf=&sa=0) do R, com o método de Cramer-von-Mises no qual detecta mudanças estatisticamente significativas \(p-valor &lt; 0.01\) tanto na média quanto na variância entre fases temporais.

