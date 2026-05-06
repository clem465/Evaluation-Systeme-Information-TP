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

Entite : `Distributeur`

- id_distributeur
- etat
- nombre_balles
- nombre_pieces

## MLD

Distributeur(id_distributeur, etat, nombre_balles, nombre_pieces)

## MPD

```sql
CREATE TABLE distributeur (
    id_distributeur INTEGER PRIMARY KEY,
    etat VARCHAR(30) NOT NULL,
    nombre_balles INTEGER NOT NULL,
    nombre_pieces INTEGER NOT NULL
);
```
