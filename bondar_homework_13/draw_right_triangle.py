import tkinter
from bondar_homework_13 import create_right_triangle


tri_coords = create_right_triangle((100, 100), area=10000)

root = tkinter.Tk()
root.title("Triangular")
root.geometry('500x500')


my_canvas = tkinter.Canvas(root, width=500, height=500, bg='lightgrey')
my_canvas.create_polygon([tri_coords[0][0], tri_coords[0][1]], [tri_coords[1][0], tri_coords[1][1]], [tri_coords[2][0], tri_coords[2][1]], fill='blue', outline='black')
my_canvas.create_text(tri_coords[0][0]+10, tri_coords[0][1]+10, text='p.1', fill='black')
my_canvas.create_text(tri_coords[1][0]+10, tri_coords[1][1]+10, text='p.2', fill='black')
my_canvas.create_text(tri_coords[2][0]+10, tri_coords[2][1]+10, text='p.3', fill='black')
my_canvas.create_text(200, 380, text=f'(x1={round(tri_coords[0][0], 2)}, y1={round(tri_coords[0][1], 2)}), (x2={round(tri_coords[1][0], 2)}, y2={round(tri_coords[1][1], 2)}), (x3={round(tri_coords[2][0], 2)}, y3={round(tri_coords[2][1], 2)})')


my_canvas.pack()

root.mainloop()