# waf build script
# vim: ft=python

def configure(cctx):
    cctx.find_program('git')
    cctx.exec_command('git submodule update --init')


def slides(ctx):
    ctx.exec_command(
        'ipython nbconvert intro_to_fmri_analysis.ipynb --to slides '
        '--reveal-prefix="reveal"')
