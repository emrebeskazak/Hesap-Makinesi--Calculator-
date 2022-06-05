# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['hesap_makinesi.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['PyQt5.QtBluetooth', 'PyQt5.QtDBus', 'PyQt5.QtHelp', 'PyQt5.QtLocation', 'PyQt5.QtMultimedia', 'PyQt5.QtMultimediaWidgets', 'PyQt5.QtNetwork', 'PyQt5.QtNfc', 'PyQt5.QtOpenGL', 'PyQt5.QtPositioning', 'PyQt5.QtPrintSupport', 'PyQt5.QtQml', 'PyQt5.QtQuick', 'PyQt5.QtQuick3D', 'PyQt5.QtQuickWidgets', 'PyQt5.QtRemoteObjects', 'PyQt5.QtSensors', 'PyQt5.QtSerialPort', 'PyQt5.QtSql', 'PyQt5.QtSvg', 'PyQt5.QtTest', 'PyQt5.QtTextToSpeech', 'PyQt5.QtWebChannel', 'PyQt5.QtWebSockets', 'PyQt5.QtWinExtras', 'PyQt5.QtXml', 'PyQt5.QtXmlPatterns', 'Tkinter' ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('icon.ico', 'C:\\Users\\emre\\Documents\\Python_Projeleri\\PyQt\\Designer\\hesap\\icon.ico', 'DATA')]	
a.datas += [('icon.png', 'C:\\Users\\emre\\Documents\\Python_Projeleri\\PyQt\\Designer\\hesap\\icon.png', 'DATA')]			 
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='hesap_makinesi',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None, 
		  icon='C:\\Users\\emre\\Documents\\Python_Projeleri\\PyQt\\Designer\\hesap\\icon.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='hesap_makinesi')
