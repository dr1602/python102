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
        
        PortaavionesComputer = Portaaviones(int(random.random() * 10),int(random.random() * 10),'Vertical')
        SubmarinoComputer = Submarino(int(random.random() * 10),int(random.random() * 10),'Vertical')
        DestructorComputer = Destructor(int(random.random() * 10),int(random.random() * 10),'Vertical')
        FragataComputer = Fragata(int(random.random() * 10),int(random.random() * 10),'Vertical')
        
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
    def __init__(self):
        super().__init__()
    
    def show_player_board(self):
        self.show()
    
    def add_ship(self, player):
        i = 0
        while i < len(player.ships):
            
            n = 0
            while n < player.ships[i].lenght:
                if player.ships[i].lenght == 'Vertical':
                    self.board[player.ships[i].initial_position_y - 1][player.ships[i].initial_position_x - 1 + n] = str(player.ships[i].id)
                else:
                    self.board[player.ships[i].initial_position_y - 1 + n][player.ships[i].initial_position_x - 1] = str(player.ships[i].id)
                n += 1
            i += 1
                    
        print(f'Est es el tablero de {player.name}')
        self.show()

class Computer_Board(Board):
    def __init__(self):
        super().__init__()
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
            
        self.hidden_ships = board_x
    
    def show_player_board(self):
        self.show()
    
    def add_ship(self, player):
        i = 0
        while i < len(player.ships):
            
            n = 0
            while n < player.ships[i].lenght:
                if player.ships[i].lenght == 'Vertical':
                    self.board[player.ships[i].initial_position_y - 1][player.ships[i].initial_position_x - 1 + n] = str(player.ships[i].id)
                else:
                    self.board[player.ships[i].initial_position_y - 1 + n][player.ships[i].initial_position_x - 1] = str(player.ships[i].id)
                n += 1
            i += 1

        y = 1

                    
        print(f'Est es el tablero de {player.name}')
        self.show()
        
        print(f'Est es el tablero escondido de {player.name}')
        while y < 11 :
            print(f'{self.hidden_ships[y-1:y]}')
            
            y += 1
    

        
PortaavionesHuman = Portaaviones(1,2,'Vertical')
SubmarinoHuman = Submarino(2,2,'Vertical')
DestructorHuman = Destructor(3,2,'Vertical')
FragataHuman = Fragata(4,2,'Vertical')

human = Human('Marcelo')
human.set_ships(PortaavionesHuman)
human.set_ships(SubmarinoHuman)
human.set_ships(DestructorHuman)
human.set_ships(FragataHuman)


computer = Computer('Computina')

player_board = Player_Board()
player_board.add_ship(human)

computer_board = Computer_Board()
computer_board.add_ship(computer)

