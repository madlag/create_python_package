import jinja2
import os
import click
import sh

def rec_split(s):
  rest, tail = os.path.split(s)
  if rest in ('', os.path.sep):
    return tail,
  return rec_split(rest) + (tail,)

  

  
def copy_directory(source, dest, dir_names, variables, git):
  """
  Copy directory source to dest, renaming directory names using dir_names, and applying jinja2 templates
  using the variables.
  If a path 
  """
  for root, directories, files in os.walk(source):
    rel_d = rec_split(os.path.relpath(root, source))
    rel_d = os.path.join(*map(lambda x : dir_names.get(x, x), rel_d))
    
    for f in files:
      src_filename = os.path.join(root, f)
      dest_filename = os.path.join(dest, rel_d, f)
      t = jinja2.Template(open(src_filename).read())
      
      if not os.path.exists(os.path.dirname(dest_filename)):
        os.makedirs(os.path.dirname(dest_filename))
              
      content = t.render(variables)
      dest_file = open(dest_filename, "w")
      dest_file.write(content)
      dest_file.close()
      if git:
        gitadd = sh.git("add", "-v", dest_filename).stdout.decode("utf-8")
        click.echo("git " + gitadd, nl=False)


      
@click.command()
@click.option('--git', '-g', is_flag=True)
@click.argument('name')
@click.argument('dest', default = '')
def run(git, name, dest):
  if dest is '':
    dest = name
  variables = {"package_name":name}
  dir_names = {"package_name":name}
  copy_directory(os.path.join(os.path.dirname(__file__), "template"), 
                 dest,
                 dir_names,
                 variables,
                 git)
  
