const form = document.getElementById("form");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const dados = {
        nome: document.getElementById("nome").value,
        altura: Number(document.getElementById("altura").value),
        peso: Number(document.getElementById("peso").value)
    };

    try {
        const response = await fetch("/api/usuarios", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(dados)
        });

        if (!response.ok) {
            alert("Erro ao salvar os dados");
            return;
        }

        const result = await response.json();
        alert(result.mensagem); // 👈 campo correto
        form.reset();

    } catch (error) {
        alert("Erro ao conectar com a API");
        console.error(error);
    }
});
