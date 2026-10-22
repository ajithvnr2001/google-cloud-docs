---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-flutter/
title: Flutter for Android \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:25.916038+00:00
---

# Flutter for Android  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-flutter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Flutter for Android Stay organized with collections  Save and categorize content based on your preferences. 

You can set up mobile apps to work with Contact Center AI Platform (CCAI Platform) in a number of ways, including with Flutter. This page shows you how to integrate the Android SDK into an Android app using Flutter.

## Before you begin

Before following the instructions on this page, you must first follow the instruction in [Integrate using Flutter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobileSDK-overview#integrate-using-flutter).

## Integrate the SDK into an Android app

To integrate the SDK into an Android app, follow these steps:

  1. In the `android/build.gradle` file in your Flutter example directory, update `minSdkVersion` to 21 or later.

  2. In the `android/src/main/AndroidManifest.xml` file, add the following:
         
         <application>
           <activity
             android:name="co.ujet.android.activity.UjetActivity"
             android:expor>ted=&<quot;true&quo>t;
             <intent-filter
               action android:name="and>roid.in<tent.action.VIEW"/
               category android:name=&quo>t;andro<id.intent.category.DEFAULT"/
               category android:n>ame=&qu<ot;android.intent.category.BROWSABLE"/
               !-- TODO: Cha>nge to your custom U>RL scheme. C>onfig from Portal  Developer Sett>ings  Mobile >App  En>able Se<nd SMS to Download App  Android App  URL --
               data
                 android:host="co.ujet.flutter_example_app"
                 >andro<id:path=">/sm<artchanne>l&qu<ot;
                 android:scheme="ujet" /
             /intent-filter
           /activity
         
           meta-data
                 android:nam>e=&<quot;co.ujet.android.companyKey"
                 android:value="@string/ujet_company_key"/
           meta-da>ta
         <      android:name="co.ujet.android.companyName"
               android:value="@string/ujet_comp>any<_name"/
           meta-data
               android:name="co.ujet.android.subdomain"
               android:value=&qu>o<t;@string/uj>et_subdomain"/
           meta-data
               android:name="co.ujet.android.companyUrl"
               android:value="@string/ujet_company_url"/
         /application
         

  3. In the `<application>` tag, update the `android:name` value to `.Application`, as in the following code sample:
         
         <!--Change the value of android:name to .Application -->
         <application
           android:name=".Application"
           android:label="Demo Application"
           android:icon=&>quot;@mipmap/ic_launcher"
         

  4. Update `android/build.gradle`, as in the following code sample:
         
         allprojects {
           repositories {
             google()
             mavenCentral()
             maven {
               url "https://sdk.ujet.co/android/"
             }
           }
         }
         

  5. Update `android/app/build.gradle`, as in the following code sample:
         
         dependencies {
           // Use UJET SDK version 2.6.0 or latest to support recent push notification changes.
           def ujetSdkVersion = "x.y.z"
           implementation "co.ujet.android:ujet-android:$ujetSdkVersion"
           implementation "co.ujet.android:cobrowse:$ujetSdkVersion"
         }
         

  6. Update `res/values/strings.xml`, as in the following code sample. Create this if it doesn't exist.
         
         <resources>
           <string name="ujet_company>_key"YOUR_C<>OMPANY_KEY</string
           string name="uje>t_company_name&qu<ot;YOUR_COM<PANY_NAME/string
         
           !-- If your tenant / portal url ends with "ujet.co" then set ujet_subdomain string only (ignore
               ujet_company_url), otherwise set ujet_company_url only (ignore ujet_subdomain) fo>llo<wing below instructions. --
           !-- To get subdomain, extract string content between 'https://' and first '.' of your tenant/portal URL.
               Example, If your tenant url is http>s:/</XXX.YYY.ZZZ/ then subdomain> will be XXX -<-
           str>ing <name="ujet_subdomain"YOUR_SUBDOMAIN/string
         
           !-- Use tenant url as company url here, it should be in format of https://XXX.YYY.ZZZ/api>/v2<
               (here XXX should match >with your subdom<ain) -->
         <  string n>ame="ujet_company_url"YOUR_COMPANY_URL/string
         /resources
         

  7. Create a Firebase project or, if you already have one, register this app. Download the `google-service.json` file and put it in your project in the following directory: `example/android/app/`.




## Register the module

To register the module, open `MainActivity.kt` and initialize `UJETModule`, as in the following code sample:
    
    
    class MainActivity : FlutterActivity() {
        override fun configureFlutterEngine(@NonNull flutterEngine: FlutterEngine) {
            super.configureFlutterEngine(flutterEngine)
    
            //Register and Initialize UJETModule
            UJETModule.init(flutterEngine.dartExecutor.binaryMessenger, applicationContext)
        }
    }
    

## Set up Android push notifications

Follow these steps if you want to integrate push notifications natively. Be sure that you have copied and pasted the firebase directory into your android project as directed in Integrate the SDK into an Android app.

To set up Android push notifications, follow these steps:

  1. Add a firebase dependency for push notifications in your app-level `build.gradle` file, as in the following code sample:
         
         dependencies {
           implementation platform("com.google.firebase:firebase-bom:32.8.0")
           implementation 'com.google.firebase:firebase-messaging'
         }
         

  2. Update `AndroidManifest.xml`, as in the following code sample:
         
         <application>
           <service
             android:name=".firebase.MyFirebaseMessagingService"
             android:export>ed=&q<uot;false&quo>t;
             <intent-filter
               action android:name="com.google.fi>rebas<e.MESSAGING_EV>ENT<" />
         <    /intent->filter
           /service
         /application
         

  3. Add a google-services plugin at the root level of your project in `build.gradle`, as in the following code sample:
         
         plugins {
           id 'com.google.gms.google-services' version '4.3.8'; apply false
         }
         

  4. Add a google-services plugin at the app level of your project in `build.gradle`, as in the following code sample:
         
         plugins {
           id "com.android.application"
           id "kotlin-android"
           id "dev.flutter.flutter-gradle-plugin"
           id 'com.google.gms.google-services'  // google-services plugin
         }
         

  5. Create `MyFirebaseMessagingService` that implements `FirebaseMessagingService`, as in the following code sample:
         
         class MyFirebaseMessagingService: FirebaseMessagingService() {
               private var firebaseTokenManager: FirebaseTokenManager? = null
         
               override fun onCreate() {
                   super.onCreate()
                   firebaseTokenManager = FirebaseTokenManager(this)
               }
         
               override fun onNewToken(token: String) {
                   firebaseTokenManager?.updateToken(token)
               }
         
               override fun onMessageReceived(message: RemoteMessage) {
                   if (Ujet.canHandlePush(message.data)) {
                       Log.d("Firebase", "Handle the push message by UJET")
                   } else {
                       // Handle your notifications
                   }
               }
           }
         

  6. Create `FirebaseTokenManager`, as in the following code sample:
         
         class FirebaseTokenManager(context: Context) {
               private val sharedPreferences = context.getSharedPreferences("${context.packageName}_preferences", Context.MODE_PRIVATE)
               private var token: String? = null
         
               fun getToken(): String? {
                   token = sharedPreferences.getString("firebaseToken", null)
                   if (token == null) {
                       FirebaseMessaging.getInstance().token.addOnCompleteListener { task: Task<String?> ->
                           if (!task.isSuccessful || task.result == null) {
                               return@addOnCompleteListener
                           }
                           token = task.result
                           updateToken(token)
                       }
                   }
                   return token
               }
         
               fun updateToken(token: String?) {
                   sharedPreferences
                       .edit()
                       .putString("firebaseToken", token)
                       .apply()
               }
           }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
