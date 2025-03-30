import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  test: {
    environment: "jsdom", // Simula o ambiente de navegador (necessário para testes de UI)
    globals: true, // Habilita as funções globais como `describe`, `test`, `expect`, etc.
  },
})
