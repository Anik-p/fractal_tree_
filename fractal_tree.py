from turtle import goto, pu, pd, color, begin_fill, end_fill, done, tracer, hideturtle

COLORS = ['#f1c40f', '#27ae60', '#8e44ad', '#e67e22', '#3498db']

def draw_fractal_tree(left_x: int | float,
                      left_y: int | float,
                      right_x: int | float,
                      right_y: int | float,
                      depth=0) -> None:

    if depth > 0:
        dx, dy = right_x - left_x, left_y - right_y
        x3, y3 = right_x + dy, right_y + dx
        x4, y4 = left_x + dy, left_y + dx
        x5, y5 = x4 + (dx + dy) / 2, y4 + (dx - dy) / 2
        color('black', COLORS[depth % len(COLORS)])
        goto(left_x, left_y)
        begin_fill()
        pd()
        for x, y in ((right_x, right_y), (x3, y3), (x4, y4), (left_x, left_y)):
            goto(x, y)
        pu()
        end_fill()
        draw_fractal_tree(x4, y4, x5, y5, depth - 1)
        draw_fractal_tree(x5, y5, x3, y3, depth - 1)

if __name__ == '__main__':
    tracer(1)
    hideturtle()
    pu()
    draw_fractal_tree(-100, -300, 100, -300, depth=8)
    done()