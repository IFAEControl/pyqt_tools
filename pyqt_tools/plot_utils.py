import numpy as np

from .plots import Plot


def show_last(num, curve):
    x, y = curve.get_data()

    if num >= len(y):
        return x, y

    x = list(reversed(x))
    y = list(reversed(y))
    new_y = []
    new_x = []

    for i in range(num):
        new_y.append(y[i])
        new_x.append(x[i])

    return new_x, new_y


class Curve:

    def __init__(self, c):
        self._c = c

    def append(self, x_val, y_val, show_last=-1):
        if show_last == -1:
            x, y = self._c.get_data()
            x = np.append(x, x_val)
            y = np.append(y, y_val)
        else:
            x, y = show_last(show_last, self._c)

        self._c.set_data(x, y)


def generate_styles(num_curves):
    from guiqwt.styles import style_generator

    styles = style_generator()
    return [next(styles) for _ in range(num_curves)]


def make_curves(styles, names):
    from guiqwt.builder import make

    curves = []
    for s, n in zip(styles, names):
        c = make.curve([], [], color=s[0], linestyle=s[1:], title=n)
        curves.append(c)

    return curves


def create_styled_curves(names):
    styles = generate_styles(len(names))
    return make_curves(styles, names)


def add_curves_to_plot(plot, curves):
    for c in curves:
        plot.add(c)


def build_plot(widget, title, ylabel, xlabel, yunit, xunit, curve_names):
        curves = create_styled_curves(curve_names)
        plot = Plot(widget, title, ylabel, xlabel, yunit, xunit)

        add_curves_to_plot(plot, curves)

        wrapped_curves = [Curve(c) for c in curves]

        return plot, wrapped_curves
