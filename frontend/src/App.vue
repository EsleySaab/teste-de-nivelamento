<template>
  <div class="container">
    <div class="header">
      <h1>Operadoras de Saúde</h1>

      <div class="search-container">
        <input
          v-model="searchQuery"
          placeholder="Digite o nome da operadora..."
        />
        <button @click="fetchData">Buscar</button>
      </div>
    </div>

    <div v-if="posts.length > 0" class="result-container">
      <ul>
        <li v-for="(post, index) in posts" :key="index" class="card">
          <p><strong>Registro ANS:</strong> {{ post.registro_ans }}</p>
          <p><strong>CNPJ:</strong> {{ post.cnpj }}</p>
          <p><strong>Razão Social:</strong> {{ post.razao_social }}</p>
          <p>
            <strong>Nome Fantasia:</strong>
            {{ post.nome_fantasia || "Não informado" }}
          </p>
          <p><strong>Modalidade:</strong> {{ post.modalidade }}</p>
          <p><strong>Localização:</strong> {{ post.cidade }}, {{ post.uf }}</p>
        </li>
      </ul>
    </div>

    <p v-else class="search">Nenhum resultado encontrado...</p>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      posts: [],
      searchQuery: "",
    }
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get(
          `http://127.0.0.1:5000/search?query=${this.searchQuery}`
        )
        this.posts = response.data
      } catch (error) {
        console.error("Erro ao buscar dados:", error)
      }
    },
  },
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  margin: 20px;
  text-align: center;
  font-family: Arial, sans-serif;
}

.header {
  justify-content: center;
  gap: 20px;
}

h1 {
  font-size: 2rem;
  color: whitesmoke;
  margin-bottom: 20px;
}

.search-container {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

input {
  width: 450px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

button {
  padding: 10px 15px;
  border: none;
  background-color: #007bff;
  color: white;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.result-container {
  margin: 10px auto;
  text-align: left;
}

ul {
  list-style: none;
  padding: 0;
}

.card {
  width: 800px;
  background: wheat;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  border-left: 5px solid #007bff;
}

.card p {
  margin: 5px 0;
  color: #444;
}

.search {
  font-size: 18px;
  color: #777;
  margin-top: 20px;
}
</style>
