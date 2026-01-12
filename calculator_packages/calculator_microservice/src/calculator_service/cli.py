import typer

from calculator_service.calculator import (
    add,
    subtract,
    multiply,
    divide,
)
from calculator_service.logger import get_logger

app = typer.Typer()
logger = get_logger("calculator-cli")


@app.command()
def add_cmd(a: float, b: float):
    result = add(a, b)
    logger.info(f"{a} + {b} = {result}")
    typer.echo(result)


@app.command()
def subtract_cmd(a: float, b: float):
    result = subtract(a, b)
    logger.info(f"{a} - {b} = {result}")
    typer.echo(result)


@app.command()
def multiply_cmd(a: float, b: float):
    result = multiply(a, b)
    logger.info(f"{a} * {b} = {result}")
    typer.echo(result)


@app.command()
def divide_cmd(a: float, b: float):
    try:
        result = divide(a, b)
        logger.info(f"{a} / {b} = {result}")
        typer.echo(result)
    except ValueError as exc:
        logger.error(str(exc))
        raise typer.Exit(code=1)


def main():
    app()


if __name__ == "__main__":
    main()
