# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['retoolgui.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Marc\\Documents\\1G1R\\Balrog Toolkit\\retool\\images', 'images'), ('C:\\Users\\Marc\\Documents\\1G1R\\Balrog Toolkit\\retool\\config', 'config'), ('C:\\Users\\Marc\\Documents\\1G1R\\Balrog Toolkit\\retool\\clonelists', 'clonelists'), ('C:\\Users\\Marc\\Documents\\1G1R\\Balrog Toolkit\\retool\\metadata', 'metadata'), ('C:\\Users\\Marc\\Documents\\1G1R\\Balrog Toolkit\\retool\\mias', 'mias'), ('C:\\Users\\Marc\\Documents\\1G1R\\Balrog Toolkit\\retool\\retroachievements', 'retroachievements')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Retool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Marc\\Documents\\1G1R\\Balrog Toolkit\\retool\\images\\retool.ico'],
)
