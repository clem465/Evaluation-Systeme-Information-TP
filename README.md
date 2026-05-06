# Systeme-Information-TP

## Version 1

Le programme contient une classe `GiftBall` qui represente un distributeur de
balles surprise.

### Etats possibles

- `NO_TOKEN` : aucune piece n'est inseree.
- `HAS_TOKEN` : une piece est inseree.
- `OUT_OF_BALLS` : la machine n'a plus de balles.

### Actions possibles

- `insert_token()` : insere une piece.
- `eject_token()` : rend la piece si elle est presente.
- `turn_crank()` : tourne la manivelle et distribue une balle si possible.
- `refill(balls)` : recharge la machine.
- `show_status()` : affiche l'etat de la machine.

## MCD

Entite : `Machine`

- id_machine

Entite : `Token`

- id_token
- utilise
- id_machine

Entite : `Operation`

- etat

Entite : `Balle`

- id_balle
- distribuee
- id_machine

Relations :

- Une `Operation` utilise 0 ou 1 `Token`.
- Un `Token` est utilisé dans une `Operation`.
- Une `Machine` donne 0 ou plusieurs `Balle`.
- Une `Balle` est donne par une seule `Machine`.
- Une `Operation` est effectue par 0 ou 1 `Machine`
- Une `Machine` effectue 0 ou 1 `Operation`

## MLD

Machine(id_machine, etat)

Token(id_token, utilise, id_machine)

Ball(id_ball, distribuee, id_machine)

## MPD

```sql
CREATE TABLE machine (
    id_machine INTEGER PRIMARY KEY,
    etat VARCHAR(30) NOT NULL
);

CREATE TABLE token (
    id_token INTEGER PRIMARY KEY,
    utilise BOOLEAN NOT NULL,
    id_machine INTEGER NOT NULL,
    FOREIGN KEY (id_machine) REFERENCES machine(id_machine)
);

CREATE TABLE ball (
    id_ball INTEGER PRIMARY KEY,
    distribuee BOOLEAN NOT NULL,
    id_machine INTEGER NOT NULL,
    FOREIGN KEY (id_machine) REFERENCES machine(id_machine)
);
```

Exemple de calcul :

```sql
-- Nombre de pieces restantes
SELECT COUNT(*)
FROM token
WHERE id_machine = 1
AND utilise = FALSE;

-- Nombre de balles restantes
SELECT COUNT(*)
FROM ball
WHERE id_machine = 1
AND distribuee = FALSE;
```

## Version 2

### Probleme constate

Dans la version 1, les actions contiennent beaucoup de conditions comme :

```python
if self.current_state == ...
```

Le probleme est que chaque nouvel etat oblige a modifier plusieurs methodes de la
classe `GiftBall`. Le code devient donc plus long, plus difficile a maintenir et plus
risque a modifier.

Pour corriger cela, la version 2 utilise le patron de conception `State`.
Chaque etat devient une classe separee qui sait comment reagir aux actions.

### Diagramme de classe

```text
                 <<interface>>
                    State
                      |
    ---------------------------------------
    |                  |                  |
NoTokenState     HasTokenState     OutOfBallsState

State
- insert_token(machine)
- eject_token(machine)
- turn_crank(machine)
- refill(machine, balls)

GiftBall
- balls
- tokens
- current_state
- no_token_state
- has_token_state
- out_of_balls_state
+ insert_token()
+ eject_token()
+ turn_crank()
+ refill(balls)
+ show_status()

GiftBall utilise State
NoTokenState implemente State
HasTokenState implemente State
OutOfBallsState implemente State
```
