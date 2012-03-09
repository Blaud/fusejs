srcdir = "."
blddir = "build"
APPNAME = "node-fuse"
VERSION = "0.0.1"

def set_options(ctx):
  ctx.add_option('--exe', action='store_true', default=False)
  ctx.recurse('src')

def configure(ctx):
  ctx.env.CFLAGS = ['-g']
  ctx.recurse('src')

def build(ctx):
  ctx.recurse('src')

