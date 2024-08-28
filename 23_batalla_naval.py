# 3 barcos con tamanos diferentes en matriz
# 2 jugadores, cada uno con su matriz
# se atacan uno a otro adivinando las posiciones
# gana el jugador que adivine las posiciones del oponente

# Bienvenido al juego de bataal Naval
# Jugador 1 coloca sus barcos
# Jugador 1 coloca su destructor de tamano 2

# Fila Inicial

import random

class Ship:
    def __init__(self, initial_position_x, initial_position_y, orientation):
        self.initial_position_x = initial_position_x
        self.initial_position_y = initial_position_y
        self.orientation = orientation
        
    def check_place(self):
        print(f'La posicion inicial del barco es {self.initial_position_x} en x, {self.initial_position_y} en y, con orientación {self.orientation}')
        
class Portaaviones(Ship):
    def __init__(self, initial_position_x, initial_position_y, orientation ):
        super().__init__(initial_position_x, initial_position_y, orientation)
        self.name = 'Portaaviones'
        self.id = 'P'
        self.hits_taken = 0
        self.lenght = 4
    
    def ship_status(self):
        print(f'Las vidas predeterminadas de tu {self.name} son: {self.lenght}, las vidas actuales que tiene son: {self.lenght-self.hits_taken}')
        
    def hit_ship(self):
        self.hits_taken = self.hits_taken + 1
        print(f'La nave ha sido golpeada, su vida actual es {self.lenght - self.hits_taken}')
        
class Submarino(Ship):
    def __init__(self, initial_position_x, initial_position_y, orientation ):
        super().__init__(initial_position_x, initial_position_y, orientation)
        self.name = 'Submarino'
        self.id = 'S'
        self.hits_taken = 0
        self.lenght = 3
    
    def ship_status(self):
        print(f'Las vidas predeterminadas de tu {self.name} son: {self.lenght}, las vidas actuales que tiene son: {self.lenght-self.hits_taken}')
        
    def hit_ship(self):
        self.hits_taken = self.hits_taken + 1
        print(f'La nave ha sido golpeada, su vida actual es {self.lenght - self.hits_taken}')
        
class Destructor(Ship):
    def __init__(self, initial_position_x, initial_position_y, orientation ):
        super().__init__(initial_position_x, initial_position_y, orientation)
        self.name = 'Destructor'
        self.id = 'D'
        self.hits_taken = 0
        self.lenght = 2
    
    def ship_status(self):
        print(f'Las vidas predeterminadas de tu {self.name} son: {self.lenght}, las vidas actuales que tiene son: {self.lenght-self.hits_taken}')
        
    def hit_ship(self):
        self.hits_taken = self.hits_taken + 1
        print(f'La nave ha sido golpeada, su vida actual es {self.lenght - self.hits_taken}')
        
class Fragata(Ship):
    def __init__(self, initial_position_x, initial_position_y, orientation ):
        super().__init__(initial_position_x, initial_position_y, orientation)
        self.name = 'Fragata'
        self.id = 'F'
        self.hits_taken = 0
        self.lenght = 1
    
    def ship_status(self):
        print(f'Las vidas predeterminadas de tu {self.name} son: {self.lenght}, las vidas actuales que tiene son: {self.lenght-self.hits_taken}')
        
    def hit_ship(self):
        self.hits_taken = self.hits_taken + 1
        print(f'La nave ha sido golpeada, su vida actual es {self.lenght - self.hits_taken}')
        
class Player:
    def __init__(self, name):
        self.name = name
        
class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.ships = []
        
    def check_user_name(self):
        print(f'Bienvenida o bienvenido: {self.name}')
        
    def set_ships(self, ship):
        self.ships.append(ship)
        print(f'Acabas de agregar la nave: {ship.name}, coordenadas {ship.initial_position_x} en x y {ship.initial_position_x} en y')
        
    def disparar(self, x, y):
        coord_x = int(x)
        coord_y = int(y)
        print(f'Acabas de dispirar en la coordenada {coord_x} en x y {coord_y} en y')
        
class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        
        ships_array = []
        
        opciones = [
            'Vertical',
            'Horizontal',
        ]
        
        PortaavionesComputer = Portaaviones(int(random.random() * 10),int(random.random() * 10),opciones[int(round(random.random(),0)*1)])
        SubmarinoComputer = Submarino(int(random.random() * 10),int(random.random() * 10),opciones[int(round(random.random(),0)*1)])
        DestructorComputer = Destructor(int(random.random() * 10),int(random.random() * 10),opciones[int(round(random.random(),0)*1)])
        FragataComputer = Fragata(int(random.random() * 10),int(random.random() * 10),opciones[int(round(random.random(),0)*1)])
        
        ships_array.append(PortaavionesComputer)
        ships_array.append(SubmarinoComputer)
        ships_array.append(DestructorComputer)
        ships_array.append(FragataComputer)
        
        self.ships = ships_array[:]
        
    def check_user_name(self):
        print(f'Soy {self.name}, tu oponente')
        
    def set_ships(self, ship):
        
        self.ships.append(ship)
        print(f'Ahora tengo la nave: {ship.name}')
    
    def disparar(self):
        x = int(random.random() * 10)
        y = int(random.random() * 10)
        print(f'Acabas de dispirar en la coordenada {x} en x y {y} en y')
        
class Board:
    def __init__(self):
        board_x = []
        
        x = 0
        while x < 10:
            board_y = []
            y = 0
            while y < 10:
                board_y.append('.')
                y += 1
            board_x.append(board_y)
            x += 1
            
        self.board = board_x
        
    def show(self):
        i = 1
        while i < 11 :
            print(f'{self.board[i-1:i]}')
            
            i += 1
            
class Player_Board(Board):
    def __init__(self, player):
        super().__init__()
        self.player = player
        
        i = 0
        while i < len(player.ships):
            
            n = 0
            while n < player.ships[i].lenght:
                if player.ships[i].orientation == 'Horizontal':
                    self.board[player.ships[i].initial_position_y - 1][player.ships[i].initial_position_x - 1 + n] = str(player.ships[i].id)
                elif player.ships[i].orientation == 'Vertical':
                    self.board[player.ships[i].initial_position_y - 1 + n][player.ships[i].initial_position_x - 1] = str(player.ships[i].id)
                n += 1
            i += 1
    
    def show_player_board(self):                   
        print(f'Est es el tablero de {self.player.name}')
        self.show()
        
    def attack(self):
        x = int(random.random() * 10)
        y = int(random.random() * 10)
        attacked_item = self.board[y-1][x-1]

        # Busca el barco correspondiente basado en su id
        for ship in self.player.ships:
            if ship.id == attacked_item:  # Esto encuentra el barco correcto
                ship.hits_taken += 1
                remaining_lifes = ship.lenght - ship.hits_taken
                if remaining_lifes == 0:
                    print(f'El barco {ship.name} ha sido hundido')
                    self.player.ships.remove(ship)  # Remueve el barco hundido
                break

        self.board[y-1][x-1] = 'X'
        print(f'Han atacado atacado al tablero de {self.player.name}')
        self.show()

class Computer_Board(Board):
    def __init__(self, player):
        super().__init__()
        self.player = player
        board_x = []
        
        x = 0
        while x < 10:
            board_y = []
            y = 0
            while y < 10:
                board_y.append('-')
                y += 1
            board_x.append(board_y)
            x += 1
            
        i = 0
        while i < len(player.ships):
            
            n = 0
            while n < player.ships[i].lenght:
                if player.ships[i].orientation == 'Horizontal':
                    self.board[player.ships[i].initial_position_y - 1][player.ships[i].initial_position_x - 1 + n] = str(player.ships[i].id)
                elif player.ships[i].orientation == 'Vertical':
                    self.board[player.ships[i].initial_position_y - 1 + n][player.ships[i].initial_position_x - 1] = str(player.ships[i].id)
                n += 1
            i += 1
            
        self.hidden_ships = board_x
    
    def show_player_board(self):                   
        print(f'Est es el tablero de {self.player.name}')
        self.show()  
    
    def attack(self, x, y):
        attacked_item = self.board[y-1][x-1]

        # Busca el barco correspondiente basado en su id
        for ship in self.player.ships:
            if ship.id == attacked_item:  # Esto encuentra el barco correcto
                ship.hits_taken += 1
                remaining_lifes = ship.lenght - ship.hits_taken
                if remaining_lifes == 0:
                    print(f'El barco {ship.name} ha sido hundido')
                    self.player.ships.remove(ship)  # Remueve el barco hundido
                break

            self.board[y-1][x-1] = 'X'
        print(f'Han atacado atacado al tablero de {self.player.name}')
        self.show()

def juego():
    print('Vamos a jugar Batalla Naval')
    print('Si en algún momento el juego te marca error, para el juego con CTRL + C y vuelve a correr la funcion juego(), empezarás de cero pero podrás jugar.')
    
    opcion = str(input('¿Quieres jugar un juego de configuración rápida? (Escribe S para o N para no ): '))
    
    if opcion == 'S' or opcion == 's' or opcion == 'Si' or opcion == 'si' or opcion == 'Sí' or opcion == 'sí':
        human_name = 'Fulane'
        human = Human(human_name)
        
        computer_name = 'Computina'
        computer = Computer(computer_name)
        
        
        PortaavionesX = 1
        PortaavionesY = 1
        PortaavionesOrientacion = 'Horizontal'
        human.set_ships(Portaaviones(PortaavionesX,PortaavionesY,PortaavionesOrientacion))
        
        SubmarinoX = 2
        SubmarinoY = 2
        SubmarinoOrientacion = 'Horizontal'
        human.set_ships(Submarino(SubmarinoX,SubmarinoY,SubmarinoOrientacion))
        
        DestructorX = 3
        DestructorY = 3
        DestructorOrientacion = 'Horizontal'
        human.set_ships(Destructor(DestructorX,DestructorY,DestructorOrientacion))
        
        FragataX = 4
        FragataY = 4
        FragataOrientacion = 'Horizontal'
        human.set_ships(Fragata(FragataX,FragataY,FragataOrientacion))    
            
        player_board = Player_Board(human)
        player_board.show_player_board()

        computer_board = Computer_Board(computer)
        computer_board.show_player_board()

        x = 0
        while x < 15:
            print('¡Vamos a atacar!')
            atack_x_axis = int(input('Escoge la coordenada en x que quieres atacar del 1 al 10 (números enteros): '))
            atack_y_axis = int(input('Escoge la coordenada en x que quieres atacar del 1 al 10 (números enteros): '))
            computer_board.attack(atack_x_axis,atack_y_axis)   
            if int(len(computer.ships)) == 0:
                print('A lo computadora no le quedan naves, has GANADO.')
                break
            else:
                print(f'Aun le quedan a la computadora {int(len(computer.ships))} naves')
            
            print('¡Le toca a la computadora atacar!')
            player_board.attack()
            if int(len(human.ships)) == 0:
                print('No te quedan naves, has perdido.')
                break
            else:
                print(f'Aun te quedan {int(len(human.ships))} naves')
        
    else:
        human_name = str(input('¿Cuál es tu nombre?: '))
        human = Human(human_name)
        
        computer_name = str(input('¿Cuál es el nombre de tu rival?: '))
        computer = Computer(computer_name)
        
        
        PortaavionesX = int(input('Ingresa las coordenadas x de tu Portaaviones: '))
        PortaavionesY = int(input('Ingresa las coordenadas x de tu Portaaviones: '))
        PortaavionesOrientacion = str(input('Ingresa la orientación de tu Portaaviones (Horizontal o Vertical): '))
        human.set_ships(Portaaviones(PortaavionesX,PortaavionesY,PortaavionesOrientacion))
        
        SubmarinoX = int(input('Ingresa las coordenadas x de tu Submarino: '))
        SubmarinoY = int(input('Ingresa las coordenadas x de tu Submarino: '))
        SubmarinoOrientacion = str(input('Ingresa la orientación de tu Submarino (Horizontal o Vertical): '))
        human.set_ships(Submarino(SubmarinoX,SubmarinoY,SubmarinoOrientacion))
        
        DestructorX = int(input('Ingresa las coordenadas x de tu Destructor: '))
        DestructorY = int(input('Ingresa las coordenadas x de tu Destructor: '))
        DestructorOrientacion = str(input('Ingresa la orientación de tu Destructor (Horizontal o Vertical): '))
        human.set_ships(Destructor(DestructorX,DestructorY,DestructorOrientacion))
        
        FragataX = int(input('Ingresa las coordenadas x de tu Fragata: '))
        FragataY = int(input('Ingresa las coordenadas x de tu Fragata: '))
        FragataOrientacion = str(input('Ingresa la orientación de tu Fragata (Horizontal o Vertical): '))
        human.set_ships(Fragata(FragataX,FragataY,FragataOrientacion))    
            
        player_board = Player_Board(human)
        player_board.show_player_board()

        computer_board = Computer_Board(computer)
        computer_board.show_player_board()
    
        x = 0
        while x < 15:
            print('¡Vamos a atacar!')
            atack_x_axis = int(input('Escoge la coordenada en x que quiers atacar del 1 al 10 (números enteros): '))
            atack_y_axis = int(input('Escoge la coordenada en x que quiers atacar del 1 al 10 (números enteros): '))
            computer_board.attack(atack_x_axis,atack_y_axis)
            print(f'Aun le quedan a la computadora {int(len(computer.ships))} naves')
            if int(len(computer.ships)) == 0:
                'A lo computadora no le quedan naves, has GANADO.'
                break
            
            print('¡Le toca a la computadora atacar!')
            player_board.attack()
            print(f'Aun te quedan {int(len(human.ships))} naves')
            if int(len(human.ships)) == 0:
                'No te quedan naves, has perdido.'
                break

juego()