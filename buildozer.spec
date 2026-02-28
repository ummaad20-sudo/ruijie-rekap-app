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
# Android API level yang stabil
android.api = 30
android.minapi = 21
android.ndk = 23b
android.sdk = 30

[android]
permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.gradle_dependencies = androidx.core:core:1.7.0
android.arch = arm64-v8a
android.accept_sdk_license = True
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r23b
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk

# Paksa untuk menggunakan versi tertentu
p4a.branch = master
p4a.local_recipes = /home/runner/work/ruijie-rekap-app/ruijie-rekap-app/.buildozer/android/platform/python-for-android

# Metadata tambahan
android.manifest = <manifest xmlns:android="http://schemas.android.com/apk/res/android" package="org.junai.ruijierekap" android:versionCode="1" android:versionName="0.1">
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <application android:label="Ruijie Rekap Pro" android:icon="@drawable/icon" android:allowBackup="true">
        <activity android:name="org.kivy.android.PythonActivity" android:label="Ruijie Rekap Pro" android:configChanges="keyboardHidden|orientation|screenSize" android:exported="true"/>
    </application>
</manifest>
