from locust import HttpUser, task, between

class JogadorEsportsUser(HttpUser):
    """
    Simula a busca pelo perfil dos jogadores profissionais no campeonato de E-sports.
    O wait_time é sorteado dinamicamente entre 2 e 4 segundos a cada requisição.
    """
    wait_time = between(2, 4)

    @task
    def buscar_perfil_jogadores(self):
        # Executa requisição GET na rota /users
        with self.client.get("/users", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Erro na requisição. Status: {response.status_code}")