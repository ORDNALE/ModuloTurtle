from turtle import Turtle
# iniciando
t = Turtle()
t.speed(1)


def direcao_do_movimento():
    movimento = int(input(
        'quantos pixels quer movimentar?: '))
    return movimento


def rotacionar_turtle(turtle):
    curva = input(f'Deseja rotacionar?, d:Direira; e:esquerda; n:não!')
    if curva == 'd':
        rotacionar_direita(turtle)
    elif curva == 'e':
        rotacionar_esquerda(turtle)


def rotacionar_esquerda(turtle):
    angulo = int(input('quantos pixels quer movimentar?: '))
    t.left(angulo)


def rotacionar_direita(turtle):
    angulo = int(input('quantos pixels quer movimentar?: '))
    t.right(angulo)


# corpo do codigo
while True:
    direcao = input('digite a direção para movimentar: f:frente, t:trás !')
    if direcao == 'f':
        distancia = direcao_do_movimento()
        rotacionar_turtle(t)
        t.forward(distancia)

    elif direcao == 't':
        distancia = direcao_do_movimento()
        rotacionar_turtle(t)
        t.backward(distancia)

        continuar = input('Deseja fazer novamente?')
        if continuar not in ('s', 'sim'):
            break
        # FIM
