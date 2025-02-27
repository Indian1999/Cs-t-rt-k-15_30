from random import randint, randrange
import math
import numpy as np  # terminálba: pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
from matplotlib.colors import LinearSegmentedColormap

def random_module():
    print("Ez itt egy random szám:", randint(1000, 9999))
    print(randrange(1,10))
    print(math.pi)
    print(math.e)
    print(math.inf)
    print(math.sqrt(2))
def math_module():
    sugár = float(input("Add meg egy kör sugarát!\n"))
    print(f"A kör kerülete: {2 * sugár * math.pi}")
    print(f"A kör területe: {sugár ** 2 * math.pi}")
    print(f"A kör átmérője: {2 * sugár}")
    print("Kevésbé pontos pi értékkel:")
    print(f"A kör kerülete: {2 * sugár * 3.14}")
    print(f"A kör területe: {sugár ** 2 * 3.14}")
    print(f"A kör átmérője: {2 * sugár}")
def numpy_module():
    numpy_array = np.array([5,3,2,7,1]) # tömb
    print(numpy_array)
    print(type(numpy_array))
    linear = np.linspace(-5, 4.9, 100)
    print(linear)
    print(linear.shape)
    linear = linear.reshape(5, 5, 4)
    print(linear)
    print(linear.shape)
    linear = linear.reshape(20, -1)
    print(linear)
    print(linear.shape)
def myFunction(x):
    return 0.1 * x
def sinus_graph():
    x = np.linspace(-2 * math.pi, 2*math.pi, 200)
    y = np.sin(x)
    y2 = myFunction(x)
    
    plt.plot(x, y, label = "Szinusz")
    plt.plot(x, y2, label = "Lineáris")
    #plt.axis("equal")
    plt.grid(True)
    plt.xlim([-2*math.pi, 2*math.pi])
    plt.ylim(bottom = -1.5, top = 1.5)
    plt.title("Szinusz függvény")
    plt.xlabel("x tengely")
    plt.ylabel("y tengely")
    plt.legend() # felirat
    #plt.show()  
    plt.savefig("sinus_vs_linear.png")  
def generate_image():
    mtx = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,1,1,0,0,1,1,0],
        [0,1,1,0,0,1,1,0],
        [0,0,0,1,1,0,0,0],
        [0,0,1,1,1,1,0,0],
        [0,0,1,1,1,1,0,0],
        [0,0,1,0,0,1,0,0]
    ]
    mtx = np.array(mtx)
    my_cmap = LinearSegmentedColormap.from_list("custom", ["green", "black"])
    plt.imshow(mtx, cmap = my_cmap)
    plt.axis("off")
    plt.savefig("creeper_face.png")
def pie_chart():
    labels = ["Nutellás", "Lekváros", "Túrós", "Kakaós"]
    sizes = [40, 10, 20, 30] # összege: 100
    
    plt.pie(sizes, labels = labels, explode = (0, 0.1, 0, 0), autopct="%1.1f%%")
    plt.title("Palacsinták kördiagrammja")
    plt.savefig("piechart.png")

def histogramm():
    data = np.random.randint(1, 11, size = 100)
    plt.hist(data)
    plt.show()
    
histogramm()
generate_image()
    
