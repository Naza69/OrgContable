class VotingSystem:
    def __init__(self):
        self.candidates = {}
        self.votes = {}

    def add_candidate(self, name):
        if name in self.candidates:
            print(f"El candidato '{name}' ya existe.")
        else:
            self.candidates[name] = 0
            print(f"Candidato '{name}' agregado.")

    def vote(self, voter_id, candidate_name):
        if voter_id in self.votes:
            print(f"El votante '{voter_id}' ya ha votado.")
            return

        if candidate_name not in self.candidates:
            print(f"El candidato '{candidate_name}' no existe.")
            return

        self.candidates[candidate_name] += 1
        self.votes[voter_id] = candidate_name
        print(f"Voto registrado: {voter_id} votó por '{candidate_name}'.")

    def get_results(self):
        print("\nResultados de la votación:")
        for candidate, vote_count in self.candidates.items():
            print(f"{candidate}: {vote_count} votos")
        print()

    def reset(self):
        self.candidates.clear()
        self.votes.clear()
        print("Sistema de votación reiniciado.")


def main():
    voting_system = VotingSystem()

    # Agregar candidatos
    voting_system.add_candidate("Alice")
    voting_system.add_candidate("Bob")

    # Realizar votaciones
    voting_system.vote("votante 1", "Alice")
    voting_system.vote("votante 2", "Bob")
    voting_system.vote("votante 3", "Alice")
    voting_system.vote("votante 4", "Bob")  

    # Obtener resultados
    voting_system.get_results()

    # Reiniciar el sistema de votación
    voting_system.reset()

if __name__ == "__main__":
    main()
