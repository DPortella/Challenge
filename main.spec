# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py', 'infos_to_file.py', 'rosto_em_imagem.py', 'texto_em_docs.py', 'texto_em_imagem.py', 'texto_em_xlsx.py', 'valid_cpf.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
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
    icon=['C:\\Users\\marci\\Documents\\Challenge\\bigico.ico'],
)
