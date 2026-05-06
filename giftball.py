from enum import Enum, auto


class State(Enum):
    NO_TOKEN = auto()
    HAS_TOKEN = auto()
    OUT_OF_BALLS = auto()


class GiftBall: # Classe pour representer une machine a balles surprise
    def __init__(self, balls=3, tokens=3): # Constructeur pour initialiser la machine avec un nombre de balles et de pieces
        self.balls = balls
        self.tokens = tokens
        self.current_state = State.NO_TOKEN

        if self.balls == 0:
            self.current_state = State.OUT_OF_BALLS

    def insert_token(self): # Methode pour inserer une piece dans la machine
        if self.current_state == State.OUT_OF_BALLS:
            print("Impossible : il n'y a plus de balles.")
        elif self.current_state == State.HAS_TOKEN:
            print("Une piece est deja inseree.")
        elif self.tokens == 0:
            print("Impossible : vous n'avez plus de pieces.")
        else:
            self.tokens -= 1
            self.current_state = State.HAS_TOKEN
            print("Piece inseree.")

    def eject_token(self): # Methode pour ejecter une piece si elle a ete inseree
        if self.current_state == State.HAS_TOKEN:
            self.tokens += 1
            self.current_state = State.NO_TOKEN
            print("Piece rendue.")
        else:
            print("Aucune piece a rendre.")

    def turn_crank(self): # Methode pour tourner la manivelle et distribuer une balle
        if self.current_state == State.OUT_OF_BALLS:
            print("Impossible : la machine est vide.")
        elif self.current_state == State.NO_TOKEN:
            print("Inserez une piece avant de tourner la manivelle.")
        else:
            self.balls -= 1
            print("Une balle surprise est distribuee.")

            if self.balls == 0:
                self.current_state = State.OUT_OF_BALLS
            else:
                self.current_state = State.NO_TOKEN

    def refill(self, balls): # Methode pour recharger la machine avec des balles
        self.balls += balls
        if self.balls > 0 and self.current_state == State.OUT_OF_BALLS:
            self.current_state = State.NO_TOKEN
        print("La machine a ete rechargee.")

    def show_status(self):
        print(f"Etat : {self.current_state.name}")
        print(f"Balles restantes : {self.balls}")
        print(f"Pieces restantes : {self.tokens}")


if __name__ == "__main__":
    machine = GiftBall(balls=3, tokens=2)

    machine.show_status()
    machine.insert_token()
    machine.turn_crank()
    machine.insert_token()
    machine.eject_token()
    machine.turn_crank()
    machine.insert_token()
    machine.turn_crank()
    machine.insert_token()
    machine.turn_crank()
    machine.insert_token()
    machine.show_status()
    
