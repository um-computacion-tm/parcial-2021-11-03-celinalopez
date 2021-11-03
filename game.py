from buscaminas import Buscaminas

if __name__ == '__main__':
    movs = ['flag', 'uncover']
    buscaminas = Buscaminas(rows=8, cols=8, bombs=10)
    print('Juego')
    buscaminas.show()
    # jugar
    while not buscaminas.win():
        try:
            mov, row, col = buscaminas.question(movs)
            buscaminas.play(mov, row, col)
            print('Juego')
            buscaminas.show()
        except:
            print('Movimiento ilegal')
    if buscaminas.win():
        print('Ganaste')
    else:
        print('Perdiste')
