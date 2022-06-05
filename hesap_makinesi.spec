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
             excludes=['QtBluetooth.pyd', 'QtDBus.pyd', 'QtHelp.pyd', 'QtLocation.pyd', 'QtMultimedia.pyd', 'QtMultimediaWidgets.pyd', 'QtNetwork.pyd', 'QtNfc.pyd', 'QtOpenGL.pyd', 'QtPositioning.pyd', 'QtPrintSupport.pyd', 'QtQml.pyd', 'QtQuick.pyd', 'QtQuick3D.pyd', 'QtQuickWidgets.pyd', 'QtRemoteObjects.pyd', 'QtSensors.pyd', 'QtSerialPort.pyd', 'QtSql.pyd', 'QtSvg.pyd', 'QtTest.pyd', 'QtTextToSpeech.pyd', 'QtWebChannel.pyd', 'QtWebSockets.pyd', 'QtWinExtras.pyd', 'QtXml.pyd', 'QtXmlPatterns.pyd' ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
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
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='hesap_makinesi')
