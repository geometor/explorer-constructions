import sympy as sp
import matplotlib.pyplot as plt
from matplotlib import rc
import tempfile
import os

#  rc('text', usetex=True)

def latex_render_to_png(expr, filename, figsize=(1920/80, 1080/80), dpi=80, padding=100):
    # Convert the expression to LaTeX code
    latex_expr = sp.latex(expr)

    width_limit = figsize[0] * 80 - 2 * padding
    height_limit = figsize[1] * 80 - 2 * padding
    print(f'{width_limit=}')
    print(f'{height_limit=}')
    

    # Create a new figure and axis
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    font_size = 48
    # Create the text element with initial font size
    t = ax.text(0.5, 0.5, f'${latex_expr}$', fontsize=font_size,
                horizontalalignment='center', verticalalignment='center',
                backgroundcolor='#CCC')

    bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
    print(bb)
    print(f'{bb.width=}')
    print(f'{bb.height=}')

    # Find the right font size to fit the expression with the desired padding
    while True:
        # Update the font size of the text element
        t.set_fontsize(font_size)

        # Get the bounding box of the expression

        bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
        print(bb)
        print(f'{bb.width=}')
        print(f'{bb.height=}')

        # Check if the bounding box fits within the desired padding
        if bb.width > width_limit / 2 or bb.height > height_limit / 2:
            print(f'{font_size=}')
            break

        font_size += 6

    # Remove the axis and set the background color to white
    ax.axis('off')
    fig.patch.set_facecolor('white')

    plt.savefig(filename, dpi=dpi, pad_inches=0)

    plt.show()

    # Save the figure as a PNG

    plt.close(fig)

if __name__ == "__main__":
    # Example expression
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    expr = sp.sin(x) * sp.exp(-y**2)

    expr = x**2 - x - 1
    # Save the expression as a PNG
    latex_render_to_png(expr, 'output.png', padding=100)
    latex_render_to_png(sp.solve(expr), 'output.png', padding=100)

