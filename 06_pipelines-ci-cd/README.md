# MÓDULO: PIPELINES DE CI E CD

#### Código
Todo código desenvolvido precisa ser armazenado, rastreável, disponibilizado de forma que diversas pessoas possam contribuir para que o ciclo de vida seja o mais longo possível e a manutenção possa acontecer de forma facilitada.

#### Organização de repositórios
Controladores de versão com GIT, SVN são úteis  nesse processo, onde também podemos usar ferramentas na nuvem para armazenar os códigos desenvolvidos de forma visual e integrada com os protocolos mais famosos.

#### Termos importantes
**Build:** Construir artefatos com suas dependências, a partir de código desenvolvido.
**Steps:** Divisão de processos por tipo - exemplo: Checkout.
**Jobs:** Tarefas que podem ser executadas para complementar o processo de construção, entre outros.
**Environments:** Divisão de ambientes por contexto, como produção, desenvolvimento.
**Test:** Processo de validação e checagem de saúde do código.
**Deploy:** Processo de implantação do código após a parte de integração.

#### Pipelines
Pipelines são como esteiras de código, tal qual uma linha de montagem com diversos steps, processos de checagem para garantir a qualidade do nosso produto: **o Código Produtivo**.
Esteiras com diversos passos que geram artefatos.

#### Ferramentas de integração contínua
Jenkins, GitLab CI, GitHub Actions, Argocd, CircleCI...

#### Integração contínua
Uma forma de gerar código produtivo de forma automatizada.

#### Build automatizado
Podemos construir artefatos sem precisarmos de um time especializado parra isso através de ferramentas.
Cada artefato possui uma identificação que facilita o desenvolvimento e controle de versões a cada incremento de software, podemos voltar ou avançar versões conforme necessário.

#### Rollback
Processo que consiste em voltar para versões anteriores de forma a manter a saúde do seu ecossistema de aplicações e serviços.

#### Entrega contínua
Processo de implantação dó código após ter passado por uma esteira de testes, validações e outros processos que criam versões prontas para estarem disponíveis em abientes produtivos. Isso facilita que possamos lançar novas funções e melhorar a experiência do usuário de forma controlada.

