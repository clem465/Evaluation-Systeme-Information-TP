class State:
    def insert_token(self, machine):
        pass

    def eject_token(self, machine):
        pass

    def turn_crank(self, machine):
        pass

    def refill(self, machine, balls):
        pass


class NoTokenState(State):
    def insert_token(self, machine):
        if machine.tokens == 0:
            print("Impossible : vous n'avez plus de pieces.")
        else:
            machine.tokens -= 1
            machine.current_state = machine.has_token_state
            print("Piece inseree.")

    def eject_token(self, machine):
        print("Aucune piece a rendre.")

    def turn_crank(self, machine):
        print("Inserez une piece avant de tourner la manivelle.")

    def refill(self, machine, balls):
        machine.balls += balls
        print("La machine a ete rechargee.")


class HasTokenState(State):
    def insert_token(self, machine):
        print("Une piece est deja inseree.")

    def eject_token(self, machine):
        machine.tokens += 1
        machine.current_state = machine.no_token_state
        print("Piece rendue.")

    def turn_crank(self, machine):
        machine.balls -= 1
        print("Une balle surprise est distribuee.")

        if machine.balls == 0:
            machine.current_state = machine.out_of_balls_state
        else:
            machine.current_state = machine.no_token_state

    def refill(self, machine, balls):
        machine.balls += balls
        print("La machine a ete rechargee.")


class OutOfBallsState(State):
    def insert_token(self, machine):
        print("Impossible : il n'y a plus de balles.")

    def eject_token(self, machine):
        print("Aucune piece a rendre.")

    def turn_crank(self, machine):
        print("Impossible : la machine est vide.")

    def refill(self, machine, balls):
        machine.balls += balls

        if machine.balls > 0:
            machine.current_state = machine.no_token_state

        print("La machine a ete rechargee.")


class GiftBall:
    def __init__(self, balls=3, tokens=3):
        self.balls = balls
        self.tokens = tokens

        self.no_token_state = NoTokenState()
        self.has_token_state = HasTokenState()
        self.out_of_balls_state = OutOfBallsState()

        if self.balls == 0:
            self.current_state = self.out_of_balls_state
        else:
            self.current_state = self.no_token_state

    def insert_token(self):
        self.current_state.insert_token(self)

    def eject_token(self):
        self.current_state.eject_token(self)

    def turn_crank(self):
        self.current_state.turn_crank(self)

    def refill(self, balls):
        self.current_state.refill(self, balls)

    def show_status(self):
        print(f"Etat : {self.current_state.__class__.__name__}")
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
