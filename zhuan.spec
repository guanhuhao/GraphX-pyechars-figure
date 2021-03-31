# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['zhuan.py','untitled.py'],
             pathex=['C:\\Users\\guan\\Desktop\\zhuan'],
             binaries=[],
             datas=[("data.txt","data.txt"),
					("template.html","template.html"),
					("template2.html","template2.html"),
					("echarts.min.js","echarts.min.js"),
					("run.png","run.png"),
					("icon.png","icon.png"),
					],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='zhuan',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
