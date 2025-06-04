let userData = { objetivos: [], habitos: [] };

function showLogin() {
  document.getElementById("registerScreen").classList.add("hidden");
  document.getElementById("loginScreen").classList.remove("hidden");
}

function showRegister() {
  document.getElementById("loginScreen").classList.add("hidden");
  document.getElementById("registerScreen").classList.remove("hidden");
}

function login() {
  document.getElementById("loginScreen").classList.add("hidden");
  document.getElementById("mainApp").classList.remove("hidden");
  carregarAnotacoes();
  updateAll();
}

function register() {
  alert("Cadastro realizado!");
  showLogin();
}

function logout() {
  location.reload();
}

function showTab(tab) {
  document.querySelectorAll(".tab").forEach(el => el.classList.add("hidden"));
  document.getElementById(tab).classList.remove("hidden");
}

function addItem(tipo) {
  const input = document.getElementById(tipo === 'objetivos' ? 'novoObjetivo' : 'novoHabito');
  const texto = input.value.trim();
  if (!texto) return;
  userData[tipo].push({ texto, progresso: 0 });
  input.value = "";
  renderList(tipo);
  updateSelo();
  notificar("Novo item adicionado com sucesso!");
}

function renderList(tipo) {
  const lista = document.getElementById(tipo === 'objetivos' ? 'listaObjetivos' : 'listaHabitos');
  lista.innerHTML = "";

  userData[tipo].forEach((item, index) => {
    const div = document.createElement("div");
    div.className = "card";
    div.innerHTML = `
      <strong>${item.texto}</strong><br/>
      <input type="range" min="0" max="100" value="${item.progresso}" onchange="updateProgresso('${tipo}', ${index}, this.value)" />
      <div class="progress"><div class="progress-bar" style="width:${item.progresso}%"></div></div>
      <button onclick="removeItem('${tipo}', ${index})">❌ Excluir</button>
    `;
    lista.appendChild(div);
  });
}

function removeItem(tipo, index) {
  userData[tipo].splice(index, 1);
  renderList(tipo);
  updateSelo();
  notificar("Item removido.");
}

function updateProgresso(tipo, index, valor) {
  userData[tipo][index].progresso = parseInt(valor);
  renderList(tipo);
  updateSelo();
}

function updateSelo() {
  const all = [...userData.objetivos, ...userData.habitos];
  const total = all.length * 100;
  const done = all.reduce((sum, item) => sum + item.progresso, 0);
  const pct = total === 0 ? 0 : (done / total) * 100;
  let selo = "Bronze";
  if (pct > 25) selo = "Prata";
  if (pct > 50) selo = "Ouro";
  if (pct > 75) selo = "Diamante";
  if (pct === 100) selo = "Mestre";
  document.getElementById("seloAtual").innerText = `🏅 Selo: ${selo}`;
}

function updateAll() {
  renderList("objetivos");
  renderList("habitos");
  updateSelo();
}

function salvarAnotacoes() {
  const texto = document.getElementById("anotacoesTexto").value.trim();
  if (texto) {
    localStorage.setItem("anotacoes", texto);
    notificar("Anotações salvas com sucesso!");
  }
}

function carregarAnotacoes() {
  const anotacoes = localStorage.getItem("anotacoes");
  if (anotacoes) {
    document.getElementById("anotacoesTexto").value = anotacoes;
  }
}

function enviarFeedback() {
  const texto = document.getElementById("feedbackTexto").value.trim();
  if (texto) {
    alert("Obrigado pelo seu feedback!");
    document.getElementById("feedbackTexto").value = "";
  }
}

function notificar(mensagem) {
  const box = document.getElementById("notificacao");
  box.innerText = mensagem;
  box.style.display = "block";
  setTimeout(() => {
    box.style.display = "none";
  }, 3000);
}