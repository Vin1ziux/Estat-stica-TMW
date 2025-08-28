Git Cheat Sheet 

🔧 Inicialização



git init → Inicia um repositório Git.



git clone <url> → Clona um repositório remoto.



📌 Status e acompanhamento



git status → Mostra status dos arquivos.



git log → Histórico de commits.



git log --oneline --graph --all → Histórico simplificado em árvore.



git diff → Mostra alterações não commitadas.



➕ Adicionar arquivos



git add <arquivo> → Adiciona arquivo ao stage.



git add . → Adiciona todas as alterações ao stage.



💾 Commit



git commit -m "mensagem" → Cria commit.



git commit --amend → Edita o último commit (mensagem/arquivos).



🌐 Repositório remoto



git remote -v → Lista repositórios remotos configurados.



git remote add origin <url> → Conecta a um repositório remoto.



git push -u origin main → Envia commits para branch main do remoto.



git pull → Atualiza local com mudanças do remoto.



git fetch → Baixa alterações sem mesclar.



🌱 Branches



git branch → Lista branches.



git branch <nome> → Cria nova branch.



git checkout -b <nome> → Cria e muda para branch.



git checkout <nome> → Muda de branch.



git merge <branch> → Mescla branch na atual.



git branch -d <nome> → Apaga branch local.



🔄 Reverter / Corrigir



git restore <arquivo> → Descarta mudanças em arquivo.



git reset <arquivo> → Remove arquivo do stage.



git reset --soft HEAD~1 → Desfaz último commit (mantém alterações no stage).



git reset --hard HEAD~1 → Apaga último commit e alterações ⚠️.



git revert <commit> → Desfaz commit criando um novo.



📦 Extras úteis



.gitignore → Define arquivos/pastas ignorados.



git stash → Salva alterações temporariamente.



git stash pop → Restaura alterações salvas.



git tag <nome> → Marca commits (ex: versões).

