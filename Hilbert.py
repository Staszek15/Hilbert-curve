from turtle import *

def hilbert(num, angle, step):
    """Argumenty(3): num - rząd krzywej, agle - kąt krzywej, step - rozmiar jednego kroku
    Funkcja rysuje krzywą Hilberta rekurencyjnie. Zwraca błąd jeśli num nie jest liczbą całkowitą lub jest mniejsze od zera."""
    if num<0 or not (float(num)).is_integer():  ## is_integer() działa dla float, zadziała np. dla 5.0
        raise IndexError("Variable n should be an integer higher than 0.")
    
    if num == 0:
        return

    # obrót w prawo
    right(angle)
    hilbert(num-1, - angle, step)
    dot("red")

    # krok i obrót w lewo
    forward(step)
    left(angle)
    hilbert(num-1, angle, step)
    dot("blue")

    forward(step)
    hilbert(num-1, angle, step)

    left(angle)
    forward(step)
    hilbert(num-1, -angle, step)
    
    right(angle)

def draw(num):
    """Argumenty(1): num - rząd krzywej
    Funkcja rysuje krzywą Hilberta rekurencyjnie z wykorzystaniem powyższej funkcji hilbert. 
    Przekazuje do niej rozmiar, pozycję początkową żółwia oraz kąt na 90 stopni."""
    size = 200
    penup()
    goto(-size // 2, size // 2)
    pendown()
    hilbert(num, 90, size//(2*num+1))       
    done()

if __name__ == "__main__":
    draw(4)
