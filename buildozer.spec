[app]
title = Ruijie Rekap Pro
package.name = ruijierekap
package.domain = org.junai
version = 0.1
version.code = 1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
requirements = python3,kivy==2.1.0,openpyxl
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.1.0
fullscreen = 0
author = JUN.AI
author_email = your@email.com
description = Aplikasi Rekap Data Ruijie Pro

[buildozer]
log_level = 2
warn_on_root = 1

[requirements]
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

[android]
permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.gradle_dependencies = androidx.core:core:1.7.0
android.arch = arm64-v8a
android.accept_sdk_license = True
android.build_tools_version = 30.0.0

# Path ke Android SDK
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
