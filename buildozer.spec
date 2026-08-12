[app]
title = MX
package.name = mxapp
package.domain = org.mxapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3==3.11.9,kivy==2.2.1,pyjnius==1.4.1
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
