import pathlib
p = pathlib.Path('templates/store/home.html')
p.write_text('', encoding='utf-8')
def add(txt):
    with open(p, 'a', encoding='utf-8') as out:
        out.write(txt)
