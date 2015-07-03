# -*- mode: python -*-
a = Analysis(['IIPLCompressor.py'],
             pathex=['C:\\Users\\huzhp\\Desktop\\IIPL'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break
a.datas += [('res/iipl.ico','C:\\Users\\huzhp\\Desktop\\IIPL\\res\\iipl.ico','DATA')]
a.binaries += [('res/optipng.exe','C:\\Users\\huzhp\\Desktop\\IIPL\\res\\optipng.exe','BINARY')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='IIPLCompressor.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='res\\iipl.ico')
