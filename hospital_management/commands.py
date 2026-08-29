import click
import frappe

@click.command("hello-app")
def hello_app():
    """Print a greeting from the custom app."""
    print("Hello from custom command!")

commands = [
    hello_app
]
