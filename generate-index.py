#!/usr/bin/env python3
import json, os

pkgs = []
for f in os.listdir('repo'):
    if f.endswith('.pkg.tar.zst') and '-debug-' not in f:
        size = os.path.getsize(os.path.join('repo', f))
        pkgs.append({'name': f, 'size': size})

pkgs.sort(key=lambda p: p['name'])

rows = ''
for p in pkgs:
    size_mb = p['size'] / 1024 / 1024
    rows += f'''          <tr>
            <td><a href="{p['name']}">{p['name']}</a></td>
            <td>{size_mb:.1f} MB</td>
          </tr>
'''

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>antergos-pkgs</title>
  <style>
    body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; background: #0e0e18; color: #e4e4f0; }}
    h1 {{ color: #e08a3c; }}
    a {{ color: #7a8cff; text-decoration: none; }}
    a:hover {{ color: #e08a3c; }}
    table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
    th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #1e1e30; }}
    th {{ color: #6a6a8a; text-transform: uppercase; font-size: 0.8em; letter-spacing: 0.1em; }}
    tr:hover {{ background: #141420; }}
    .usage {{ background: #141420; border: 1px solid #1e1e30; border-radius: 8px; padding: 16px; margin: 20px 0; }}
    code {{ background: #08080e; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }}
    pre {{ background: #08080e; border: 1px solid #1e1e30; padding: 12px; border-radius: 6px; overflow-x: auto; }}
    footer {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #1e1e30; color: #4a4a66; font-size: 0.85em; }}
  </style>
</head>
<body>
  <h1>antergos-pkgs</h1>
  <p>AUR package repository for Antergos NeXT</p>

  <div class="usage">
    <strong>Add to /etc/pacman.conf</strong>
    <pre>[antergos-pkgs]
SigLevel = Optional TrustAll
Server = https://Antergos-NeXT.github.io/antergos-pkgs/$repo/os/$arch
Server = https://Antergos-NeXT.github.io/antergos-pkgs</pre>
  </div>

  <table>
    <tr><th>Package</th><th>Size</th></tr>
{rows}  </table>

  <footer>Antergos NeXT &mdash; <a href="https://github.com/Antergos-NeXT">github.com/Antergos-NeXT</a></footer>
</body>
</html>'''

with open('repo/index.html', 'w') as fp:
    fp.write(html)

with open('repo/pkglist.json', 'w') as fp:
    json.dump([{'name': p['name'], 'size': p['size']} for p in pkgs], fp, indent=2)
    fp.write('\n')
