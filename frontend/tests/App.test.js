import { render, fireEvent, screen } from "@testing-library/vue"
import { expect, describe, test, vi } from "vitest"
import App from "../src/App.vue"
import axios from "axios"

vi.mock("axios")

describe("App.vue", () => {
  test("Renderiza o campo de busca corretamente", () => {
    render(App)

    const input = screen.getByPlaceholderText("Digite o nome da operadora...")
    expect(input).not.toBeNull()

    const button = screen.getByText("Buscar")
    expect(button).not.toBeNull()
  })

  test("Realiza uma busca e exibe resultados", async () => {
    axios.get.mockResolvedValue({
      data: [
        {
          registro_ans: "317144",
          cnpj: "05868278000107",
          razao_social:
            "UNIMED DE FORTALEZA SOCIEDADE COOPERATIVA MÉDICA LTDA.",
          nome_fantasia: "UNIMED DE FORTALEZA",
          modalidade: "Cooperativa Médica",
          cidade: "Fortaleza",
          uf: "CE",
        },
      ],
    })

    render(App)

    const input = screen.getByPlaceholderText("Digite o nome da operadora...")
    await fireEvent.update(input, "UNIMED DE FORTALEZA")

    const button = screen.getByText("Buscar")
    await fireEvent.click(button)

    expect(await screen.findByText(/317144/)).not.toBeNull()
    expect(await screen.findByText(/05868278000107/)).not.toBeNull()
    expect(
      await screen.findByText(
        /UNIMED DE FORTALEZA SOCIEDADE COOPERATIVA MÉDICA LTDA./
      )
    ).not.toBeNull()
    expect(
      await screen.findByText(
        /UNIMED DE FORTALEZA SOCIEDADE COOPERATIVA MÉDICA/
      )
    ).not.toBeNull()
    expect(await screen.findByText(/Cooperativa Médica/)).not.toBeNull()
    expect(await screen.findByText(/Fortaleza, CE/)).not.toBeNull()
  })
})
