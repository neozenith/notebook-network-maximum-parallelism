from invoke import task


@task
def tidy(c):
    """Run formatter tasks."""
    c.run("ruff format .")
    c.run("black --ipynb notebooks/")


@task
def ci(c):
    """Run all quality checks."""
    c.run("ruff check .")


@task
def dev(c):
    """Run development loop."""
    c.run("jupyter lab")
