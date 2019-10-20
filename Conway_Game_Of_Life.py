import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.animation as animation

w = 15
h = 15
first = 20
generations = 100
def updateMat(matrix):
    mat = np.zeros((w, h))
    popCount = 0
    for i in range(w):
        for j in range(h):

            if matrix[i][j] == 0:
                if i == 0 and j == 0:
                    if matrix[0][1] == 1 and matrix[1][0] == 1 and matrix[1][1] == 1: mat[0][0] = 1
                elif i == w-1 and j == 0:
                    if matrix[w-2][0] == 1 and matrix[w-2][1] == 1 and matrix[w-1][1] == 1: mat[w-1][0] = 1
                elif i == w-1 and j == h-1:
                    if matrix[w-2][h-1] == 1 and matrix[w-2][h-2] == 1 and matrix[w-1][h-2] == 1: mat[w-1][h-1] = 1
                elif i == 0 and j == h-1:
                    if matrix[0][h-2] == 1 and matrix[1][h-2] == 1 and matrix[1][h-1] == 1: mat[0][h-1] = 1
                elif i == 0:
                    cnt = matrix[0][j-1] + matrix[1][j-1] + matrix[1][j] + matrix[1][j+1] + matrix[0][j+1]
                    if cnt == 3: mat[i][j] = 1
                elif j == 0:
                    cnt = matrix[i-1][0] + matrix[i-1][1] + matrix[i][1] + matrix[i+1][1] + matrix[i+1][0]
                    if cnt == 3: mat[i][j] = 1
                elif i == w-1:
                    cnt = matrix[w-1][j - 1] + matrix[w-2][j - 1] + matrix[w-2][j] + matrix[w-2][j + 1] + matrix[w-1][j + 1]
                    if cnt == 3: mat[i][j] = 1
                elif j == h-1:
                    cnt = matrix[i - 1][h-1] + matrix[i - 1][h-2] + matrix[i][h-2] + matrix[i + 1][h-2] + matrix[i + 1][h-1]
                    if cnt == 3: mat[i][j] = 1
                else:
                    cnt = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + matrix[i][j-1] + matrix[i][j+1] + matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]
                    if cnt == 3: mat[i][j] = 1

            else:
                if i == 0 and j == 0:
                    cnt = matrix[0][1] + matrix[1][0] + matrix[1][1]
                    if cnt < 2: mat[0][0] = 0
                    else:
                        mat[i][j] = 1
                elif i == w - 1 and j == 0:
                    cnt =  matrix[w - 2][0] + matrix[w - 2][1] + matrix[w - 1][1]
                    if cnt < 2: mat[w - 1][0] = 0
                    else:
                        mat[i][j] = 1
                elif i == w - 1 and j == h - 1:
                    cnt =  matrix[w - 2][h - 1] + matrix[w - 2][h - 2] + matrix[w - 1][h - 2]
                    if cnt < 2: mat[w - 1][h - 1] = 0
                    else:
                        mat[i][j] = 1
                elif i == 0 and j == h - 1:
                    cnt = matrix[0][h - 2] + matrix[1][h - 2] + matrix[1][h - 1]
                    if cnt < 2: mat[0][h - 1] = 0
                    else:
                        mat[i][j] = 1
                elif i == 0:
                    cnt = matrix[0][j - 1] + matrix[1][j - 1] + matrix[1][j] + matrix[1][j + 1] + matrix[0][j + 1]
                    if cnt < 2 or cnt > 3: mat[i][j] = 0
                    else:
                        mat[i][j] = 1
                elif j == 0:
                    cnt = matrix[i - 1][0] + matrix[i - 1][1] + matrix[i][1] + matrix[i + 1][1] + matrix[i + 1][0]
                    if cnt < 2 or cnt > 3: mat[i][j] = 0
                    else:
                        mat[i][j] = 1
                elif i == w - 1:
                    cnt = matrix[w - 1][j - 1] + matrix[w - 2][j - 1] + matrix[w - 2][j] + matrix[w - 2][j + 1] + \
                           matrix[w - 1][j + 1]
                    if cnt < 2 or cnt > 3: mat[i][j] = 0
                    else:
                        mat[i][j] = 1
                elif j == h - 1:
                    cnt = matrix[i - 1][h - 1] + matrix[i - 1][h - 2] + matrix[i][h - 2] + matrix[i + 1][h - 2] + \
                           matrix[i + 1][h - 1]
                    if cnt < 2 or cnt > 3: mat[i][j] = 0
                    else:
                        mat[i][j] = 1
                else:
                    cnt = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i][j - 1] + \
                           matrix[i][j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
                    if cnt < 2 or cnt > 3: mat[i][j] = 0
                    else: mat[i][j] = 1
                popCount += cnt

    return mat, popCount

#def hinton(matrix, max_weight=None, ax=None):
def gameOfLife(matrix):

    fig, axes = plt.subplots(nrows=1, ncols=2)
    ax, ax1 = axes.flatten()

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    fig.suptitle('Game Of Life', fontsize=16)
#    if not max_weight:
#        max_weight = 2 ** np.ceil(np.log(np.abs(matrix).max()) / np.log(2))

    ax.patch.set_facecolor('gray')
    ax.set_title('Arena')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())

    ax1.patch.set_facecolor('lightgray')
    ax1.set_title('Population v/s Time')
    ax1.set_aspect('equal', 'box')
    ax1.set_xlabel('time')
    ax1.set_ylabel('population size')

    popcnt = first
    ims = []
    i = 0
    xdata = []
    ydata = []
    line = plt.plot([],[],'-r')
    while i<=generations:
        im = ax.imshow(matrix)
        ydata.append(i)
        xdata.append(popcnt)
        im2, = plt.plot(xdata, ydata, 'ro-')
        ims.append([im, im2])
        matrix, popcnt = updateMat(matrix)
        i+=1

    ani = animation.ArtistAnimation(fig, ims, blit = True, interval = 150, repeat = False)

    ax.autoscale_view()
    ax1.autoscale_view()
    ax.invert_yaxis()

def submit(event):
    global w, h, first, generations
    w = int(sY.val)
    h = int(sX.val)
    first = int(sNum.val)
    generations = int(sGen.val)
    plt.close()

def initMat():
    global first
    matrix = np.zeros((w, h))
    x = np.random.rand(first) * w
    y = np.random.rand(first) * h
    for (i,j) in zip(x,y):
        matrix[int(i)][int(j)] = 1

    return matrix

if __name__ == '__main__':
    np.random.seed(19680801)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axis('off')

    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()

    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    plt.title('Game Of Life')

    axcolor = 'lightgoldenrodyellow'
    sliderWidth = 0.35
    sliderHeight = 0.03
    axY = plt.axes([0.5 - sliderWidth/2, 0.7, sliderWidth, sliderHeight], facecolor=axcolor)
    axX = plt.axes([0.5 - sliderWidth/2, 0.6, sliderWidth, sliderHeight], facecolor=axcolor)
    axNum = plt.axes([0.5 - sliderWidth / 2, 0.5, sliderWidth, sliderHeight], facecolor=axcolor)
    axGen = plt.axes([0.5 - sliderWidth / 2, 0.4, sliderWidth, sliderHeight], facecolor=axcolor)
    sY = Slider(axY, 'Slider Y', 1, 40, valinit=w)
    sX = Slider(axX, 'Slider X', 1, 40, valinit=h)
    sNum = Slider(axNum, 'First Generation', 1, 700, valinit=first)
    sGen = Slider(axGen, 'Total Generations', 1, 700, valinit=generations)

    buttonHeight = 0.04
    buttonWidth = 0.1
    submitax = plt.axes([0.5 - buttonWidth/2, 0.3, buttonWidth, buttonHeight])
    button = Button(submitax, 'Submit', color=axcolor, hovercolor='0.975')

    button.on_clicked(submit)
    plt.show()

    print(w, h)
    matrix = initMat()
    gameOfLife(matrix)
    plt.show()