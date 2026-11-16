# OSWork v5 — edição 40+ leigo

Curso estático INEMA.CLUB PRO sobre organizar o próprio ambiente de IA.
Repositório independente: a edição v2 (público técnico) vive em `../oswork` e **não**
compartilha código, conteúdo nem estado com este.

- **Conta e autoria:** `inematds <inematds@gmail.com>`, author e committer.
- **Formato:** `formato-curso-v5` (página única, dark editorial, contrato pedagógico 40+).
  Motor em `assets/curso.js` + `assets/aula.css`, copiados da skill sem alteração.
- **Público e descoberta:** registrados no topo de `curso.html` e em `context/curriculo.md`.
  Profissões-alvo: **gestora** e **professor**. Nenhum exemplo usa outra.

## Estrutura

- `curso.html` — página única com a trilha e as 7 aulas. **Artefato montado**, não edite
  as aulas 2–7 diretamente aqui.
- `aulas/aula-N.html` — fragmento fonte de cada aula (2–7). É onde se edita.
  A Aula 1 é a referência do formato e vive dentro do próprio `curso.html`.
- `landing.html` / `index.html` — landing auto-contida e redirecionamento.
- `context/curriculo.md` — currículo travado: promessas, tipos, dosagem, ganchos.
- `scripts/build.py` — remonta `curso.html` a partir de `aulas/`. Idempotente.
- `scripts/validate.py` — o portão mecânico. Roda sobre `curso.html` ou sobre um fragmento.

## Fluxo de trabalho

```bash
python3 scripts/build.py        # monta curso.html a partir de aulas/
python3 scripts/validate.py     # portão: 0 falhas é obrigatório
```

Editar uma aula = editar `aulas/aula-N.html`, remontar e revalidar. Nunca editar a view
já montada dentro de `curso.html` — `build.py` sobrescreve.

## Regras de conteúdo que o portão cobra

- Jargão-sentinela proibido no texto do aluno: terminal, instalar, script, servidor,
  repositório, commit, branch, Git, JSON, pipeline, "arquivo de configuração", API,
  deploy, CLI, diretório, plugin, encoding. Use *pasta*, nunca *diretório*.
- Exemplo por profissão (`<p data-ex="gestora|professor">`) em 100% dos steps.
- Apoio visual legendado (`data-cap`) em 100% dos steps; `.herofig` é metáfora do mundo
  real, `.fig` do trilho é diagrama de mecanismo — nunca trocados.
- Densidade: no máximo 1 quadro funcional a cada 2 steps, nunca em steps adjacentes.
- Cartões nunca repetem ≥6 palavras seguidas do `.recap-autor`, e toda frente é pergunta.
- Manifesto de completude em cada aula, 13 linhas, zero `[AUSENTE]`. O marcador
  `teste-se-FUND` reflete a **obrigação**: `[OK]` só em aula FUNDAMENTO, `[N/A]` nas demais.
- Zero emoji, zero exclamação dupla, zero gamificação.

## Publicação

Por git, GitHub Pages na raiz de `main`. Não usar Vercel. Publicar = commit + push;
o deploy não é responsabilidade deste repo.

## Idiomas (EN e ES) — a partir de 22/09/2026

PT na raiz, inglês em `en/`, espanhol em `es/`. Progresso e cartões **isolados por
idioma** (`oswork5-en` / `oswork5-es`): os cartões guardam o texto no estado do aluno.

```bash
python3 scripts/build.py             # PT primeiro (monta curso.html)
python3 scripts/i18n_extract.py      # 810 unidades, ~12.850 palavras
python3 scripts/i18n_translate.py    # OpenRouter + gpt-5.4-nano, cache em i18n/
python3 scripts/i18n_repair.py       # espaço de borda e markup inventado
python3 scripts/build_locales.py     # monta en/ e es/ e insere o seletor nas 6 páginas
python3 scripts/validate-locales.py  # paridade com o PT + jargão traduzido + seletor
node scripts/browser-locales.cjs     # navegador nos dois idiomas
```

**A ordem importa:** `build_locales.py` roda **depois** de `build.py`, porque `build.py`
reescreve `curso.html` inteiro e apagaria o seletor de idioma. Os dois são idempotentes.

Quatro superfícies traduzidas, não uma: HTML · rótulos do motor (recortados por
deslocamento, cópia local por idioma em `<lang>/assets/curso.js`) · rótulos gerados por
`content:` no CSS (`<lang>/assets/i18n.css`) · texto dentro dos SVG.
