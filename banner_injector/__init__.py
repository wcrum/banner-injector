import click
import glob
import os
import pkg_resources

from jinja2 import Template


defaults = {
    "themes": {
        "background-color": "#f0f0f0",
        "text-color": "black"
    },
    "header": {
        "text": "An official website of the United States government",
        "icon": "us_flag_small.png",
        "font-size": ".74rem"
    },
    "content": {
        "left": {
            "text": "<strong>Official websites use .gov</strong><br>A .gov website belongs to an official government organization in the United States.",
        },
        "right": {
            "text": "<strong>Secure .gov websites use HTTPS</strong><br> A lock (🔒) or https:// means you've safely connected to the .gov website. Share sensitive information only on official, secure websites."
        },
        "font-size": ".94rem"
    }
}

from jinja2 import Template
with open('uswds_template.html') as file_:
    template = Template(file_.read())
template.stream(**defaults).dump("out.html")


@click.group()
def main():
    pass

@main.command()
@click.option('--config', help='Specify Configuration File')
@click.option('--recursive/--not-recursive', help='Disabled Recursive Search', default=True)
@click.argument('path', type=click.Path(exists=True))
def inject(path, *args, **kwgs):
    """Injects Banner in Specified Path"""
    running_path = os.getcwd()
    os.chdir(path)
    searching_path = os.getcwd()

    absoulte_files = []

    # set recursive flag option
    if not kwgs['recursive']:
        files = glob.glob('*.html', recursive = False)
    else:
        files = glob.glob('**/*.html', recursive = True)

    # add all file absolute file paths
    for f in files:
        click.echo(f)
        absoulte_files.append("{}\\{}".format(searching_path, f))


    click.echo(click.style('WARNING! You are about to modify {} files.'.format(len(files)), fg='red'))
    click.confirm('Do you want to continue?', abort=True)

@main.command()
def init():
    """Generates Banner Injector Configuration Files."""
    click.echo('Syncing')

if __name__ == '__main__':
    main()