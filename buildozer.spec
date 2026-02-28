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

[buildozer]
log_level = 2
warn_on_root = 1

[requirements]
# Gunakan API level 31 (lebih stabil dari 30)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 30

[android]
permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.gradle_dependencies = androidx.core:core:1.7.0
android.arch = arm64-v8a
android.accept_sdk_license = True

# Tambahkan ini untuk stabilitas
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk

[app]
author = JUN.AI
author_email = your@email.com
description = Aplikasi Rekap Data Ruijie Pro
