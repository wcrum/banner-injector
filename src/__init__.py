import click
import glob
import os
import pkg_resources
import yaml
from bs4 import BeautifulSoup
from jinja2 import Template

@click.group()
def main():
    pass

@main.command()
@click.option('--config', '-c', default="banner-config.yml", help='Specify Configuration File')
@click.option('--recursive/--not-recursive', help='Disabled Recursive Search', default=True)
@click.option('--force', '-f', help='Force Modification', is_flag=True, default=False)
@click.argument('path', type=click.Path(exists=True))
def uswds(path, *args, **kwgs):
    """Injects Banner in Specified Path"""

    with open(kwgs["config"]) as conf:
        config = yaml.load(conf, yaml.Loader)


    with open(pkg_resources.resource_filename(__name__, 'assets/uswds_template.html')) as file:
        template = Template(file.read())

    template = "".join(template.stream(**config))

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
        absoulte_files.append("{}/{}".format(searching_path, f))

    if not kwgs['force']:
        click.echo(click.style('WARNING! You are about to modify {} files.'.format(len(files)), fg='red'))
        click.confirm('Do you want to continue?', abort=True)

    for f in absoulte_files:
        with open(f, "r", encoding='latin-1') as _html:
            soup = BeautifulSoup(_html, "html.parser")
            try:
                soup.body.insert(
                    0,
                    BeautifulSoup(template, "html.parser") 
                )
            except:
                click.echo(click.style('Error! No body. {}'.format(f), fg='red'))
                pass            
        with open(f, "w", encoding='utf-8') as _html:
            _html.write(str(soup))

        click.echo(click.style('{}'.format(f), fg='green'))


@main.command()
def init():
    """Generates Banner Injector Configuration Files."""
    click.echo('Syncing')

if __name__ == '__main__':
    main()