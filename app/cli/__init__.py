from .seed import seed


def register_cli(app):
    app.cli.add_command(seed)
