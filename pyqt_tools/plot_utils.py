from .plots import Plot

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

        return plot
