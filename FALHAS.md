# Falhas — OSWork v5

Uma linha por falha real: data, o que quebrou, a menor correção, e se era PROMPT ou INFRA.
Mais recente no topo.

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-09-22 | "role para estudar" traduzido como "role to study": em PT é o verbo rolar a página, em EN virou o substantivo função | corrigido e posto no glossário dos dois repos | prompt |
| 2026-09-22 | "roteiro de laboratório" traduzido como "lab script" — `script` está na lista que o curso promete não usar | glossário fixa roteiro → worksheet / guía nos dois repos | prompt |
| 2026-09-22 | browser-locales.cjs trazido do Quick com a chave de estado `osworkq` escrita no código, reprovava o v5 | o teste lê a chave do `<meta name="curso">` do próprio PT | prompt |
| 2026-09-21 | traços das figuras invisíveis nos temas papel e sépia: fundo da caixa de figura é escuro nos 3 temas, mas currentColor segue --ink e vira escuro no claro (contraste medido 1,10 e 1,36) | token `--figink` claro aplicado a `.figstage`, `.colfig` e `.mobfig` | infra |
| 2026-09-21 | browser-test media contraste só do texto do corpo, então não pegou a falha acima | novo grupo de verificação: contraste do traço da figura nos 3 temas | prompt |
| 2026-09-21 | tema sépia com contraste 6,52:1 no corpo (AAA exige 7:1) — defeito herdado do aula.css da skill | usar `--ink` no lugar de `--ink-soft` só no sépia; token existente, nenhuma cor nova | infra |
| 2026-09-21 | browser-test media contraste no meio da `transition:background .3s` do body e lia o blend como cor do tema | esperar 700ms após trocar `data-theme` antes de medir | prompt |
| 2026-09-21 | browser-test calculava luminância sem linearização sRGB, dando razões de contraste erradas | aplicar a fórmula WCAG (gama) em vez da média direta dos canais | prompt |
| 2026-09-21 | cliques do browser-test bloqueados pelo scrim do onboarding na primeira visita | helper `fecharPaineis()` removendo `.on` de painéis e scrim após cada carga | prompt |
| 2026-09-21 | Aula 1 repetia metáfora, `why` e enquadramento "três partes" do curso ia-do-zero (clone estrutural) | trocar metáfora para ordem de serviço, reescrever o why e as duas cenas da gestora | prompt |
| 2026-09-21 | persona "Marta" da Aula 2 é a mesma gestora de RH de agi-ready e ia-do-zero | renomear para Sílvia (inédita nos cursos anteriores) | prompt |
| 2026-09-21 | validate.py acusou "figura sem legenda" e ".termdemo presente" na Aula 1, ambos falsos positivos | regex `fig` casava `figstage` → ancorar em `class="fig"\|"fig on"`; varredura de termdemo ignorando comentários HTML | prompt |
