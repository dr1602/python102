import random as rd

print('Este es el juego de piedra, papel o tijera.');

game_options = ('piedra', 'papel', 'tijera');

rondas = 0

user_victories = 0
computer_victories = 0

while True:
    
    rondas += 1
    
    print('*' * 12)
    print(f'Ronda {rondas}')
    print('*' * 12)
    
    user_option = input('Elige piedra, papel o tijera: ').lower();


    if user_option in game_options:
        
        computer_option = rd.choice(game_options)
        
        print(f'Has escogido {user_option}')
        print(f'La computadora ha escogido {computer_option}')
        
        if user_option == computer_option:
            print('Esto es un empate, seleccionaron la misma opcion');
            
            print('*' * 12)
            print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
        elif user_option == 'piedra':
            if computer_option == 'tijera':
                print('Piedra gana a tijera');
                print('El o la usuario ha ganado.');
                user_victories += 1;
                
                print('*' * 12)
                print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
            else:
                print('Papel gana a piedra');
                print('La computadora ha ganado.');
                computer_victories += 1;
                
                print('*' * 12)
                print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
        elif user_option == 'papel':
            if computer_option == 'tijera':
                print('Tijera gana a papel');
                print('La computadora ha ganado.');
                computer_victories += 1;
                
                print('*' * 12)
                print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
            else:
                print('Papel gana a piedra');
                print('El o la usuario ha ganado.');
                user_victories += 1;
                
                print('*' * 12)
                print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
        elif user_option == 'tijera':
            if computer_option == 'papel':
                print('Tijera gana a papel');
                print('El o la usuario ha ganado.');
                user_victories += 1;
                
                print('*' * 12)
                print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
            else:
                print('Piedra gana a tijera');
                print('La computadora ha ganado.');
                computer_victories += 1;
                
                print('*' * 12)
                print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
                
        if user_victories == 2:
            print('Una maravillosa vicotria de la o el usuario.');
            break
        
        if computer_victories == 2:
            print('Una maravillosa vicotria de la compu.');
            break
        
    else:
        
        print('Esa opción no es valida, escoge de nuevo (tienes 2 oportunidades más).')
        
        i = 0
        while i < 2:
            i += 1
            user_option = input('Elige piedra, papel o tijera: ').lower();
            
            if user_option in game_options:
                break
            
        if user_option in game_options:
            computer_option = rd.choice(game_options)
        
            print(f'Has escogido {user_option}')
            print(f'La computadora ha escogido {computer_option}')
            
            if user_option == computer_option:
                print('Esto es un empate, seleccionaron la misma opcion');
                
                print('*' * 12)
                print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
            elif user_option == 'piedra':
                if computer_option == 'tijera':
                    print('Piedra gana a tijera');
                    print('El o la usuario ha ganado.');
                    user_victories += 1;
                    
                    print('*' * 12)
                    print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
                else:
                    print('Papel gana a piedra');
                    print('La computadora ha ganado.');
                    computer_victories += 1;
                    
                    print('*' * 12)
                    print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
            elif user_option == 'papel':
                if computer_option == 'tijera':
                    print('Tijera gana a papel');
                    print('La computadora ha ganado.');
                    computer_victories += 1;
                    
                    print('*' * 12)
                    print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
                else:
                    print('Papel gana a piedra');
                    print('El o la usuario ha ganado.');
                    user_victories += 1;
                    
                    print('*' * 12)
                    print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
            elif user_option == 'tijera':
                if computer_option == 'papel':
                    print('Tijera gana a papel');
                    print('El o la usuario ha ganado.');
                    user_victories += 1;
                    
                    print('*' * 12)
                    print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
                else:
                    print('Piedra gana a tijera');
                    print('La computadora ha ganado.');
                    computer_victories += 1;
                    
                    print('*' * 12)
                    print(f'El marcador es {user_victories} punto(s) a favor del usario y {computer_victories} punto(s) a favor de la compu.')
        else:
            print('Gracias por jugar.')
    
        if user_victories == 2:
            print('Una maravillosa vicotria de la o el usuario.');
            break
        
        if computer_victories == 2:
            print('Una maravillosa vicotria de la compu.');
            break