import tkinter as tk

# Pencereyi ve canvas'ı oluştur
window = tk.Tk()
window.title("Kaleye Gol Atma Oyunu")
canvas = tk.Canvas(window, width=600, height=400, bg="green")
canvas.pack()

# Kaleyi çiz
goal_posts = canvas.create_rectangle(250, 300, 350, 400, outline="white", width=2)

# Topu çiz
ball = canvas.create_oval(290, 370, 310, 390, fill="white")

# Oyuncuyu çiz (çubuk şeklinde)
player = canvas.create_line(300, 350, 300, 390, fill="black", width=5)

# Oyuncu ve topun hareket yönünü sakla
direction = {'x': 0, 'y': 0}


# Topu hareket ettirme fonksiyonu
def kick_ball(event):
    # Topun hızını belirle
    speed = 20
    # Topu hareket ettir
    canvas.move(ball, direction['x'] * speed, direction['y'] * speed)


# Oyuncuyu ve topu hareket ettirme fonksiyonu
def move_player_and_ball(event):
    # Hareket miktarını belirle
    move_x, move_y = 0, 0
    if event.keysym == 'Up':
        move_y = -10
    elif event.keysym == 'Down':
        move_y = 10
    elif event.keysym == 'Left':
        move_x = -10
    elif event.keysym == 'Right':
        move_x = 10

    # Oyuncu ve topun hareket yönünü güncelle
    direction['x'], direction['y'] = move_x, move_y

    # Oyuncuyu ve topu hareket ettir
    canvas.move(player, move_x, move_y)
    canvas.move(ball, move_x, move_y)


# Klavye olaylarını bağla
window.bind('<KeyPress-Up>', move_player_and_ball)
window.bind('<KeyPress-Down>', move_player_and_ball)
window.bind('<KeyPress-Left>', move_player_and_ball)
window.bind('<KeyPress-Right>', move_player_and_ball)
window.bind('<KeyPress-space>', kick_ball)

# Oyunu başlat
window.mainloop()
