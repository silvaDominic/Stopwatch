# template for "Stopwatch: The Game"

# define global variables
import simplegui

interval = 100
current_time = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global current_time
    string_time = str(current_time)
    A = t / 600
    
    D = t % 10
    t /= 10
    t %= 60

    C = t % 10
    B = t / 10
    
    A = str(A)
    B = str(B)
    C = str(C)
    D = str(D)
    
    return A + ":" + B + C + "." + D

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    timer.start()
    
def stop_timer():
    timer.stop()

def reset_timer():
    global current_time
    timer.stop()
    current_time = 0

# define event handler for timer with 0.1 sec interval
def increment_time():
    global current_time
    current_time += 1
    print current_time

# define draw handler
def draw(canvas):
    canvas.draw_text(format(current_time), [80, 110], 24, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch Game", 300, 200, 200)

# register event handlers
timer = simplegui.create_timer(interval, increment_time)
button1 = frame.add_button("Start", start_timer, 50)
button2 = frame.add_button("Stop", stop_timer, 50)
button3 = frame.add_button("Reset", reset_timer, 50)
frame.set_draw_handler(draw)

# start frame
frame.start()
