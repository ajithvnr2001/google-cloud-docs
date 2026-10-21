---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-react/
title: React Native for Android \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:45:47.292528+00:00
---

# React Native for Android  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-react/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  React Native for Android Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides integration with mobile applications using a number of methods including React. This document explains how to integrate React Native for Android.

Before following these Android-specific instructions, complete the instructions at [React Native for Mobile SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobileSDK-overview#mobile-sdk-react).

## Integrate the SDK into Android

To integrate the SDK into Android, follow these steps:

  1. Add the following code inside `<application>` of the `AndroidManifest.xml` file:
         
         <application>
           <activity
             android:name="co.ujet.android.activity.UjetActivity"
             android:exported="true">
             <intent-filter>
               <action android:name="android.intent.action.VIEW"/>
               <category android:name="android.intent.category.DEF```AULT"/>
               <category android:name="android.intent.category.BROWSABLE"/>
               <data
                 android:host="com.sampleapp"
                 android:path="/smartchannel"
                 android:scheme="ujet" />
             </intent-filter>
           </activity>
         
           <meta-data
                 android:name="co.ujet.android.companyKey"
                 android:value="@string/ujet_company_key"/>
           <meta-data
               android:name="co.ujet.android.companyName"
               android:value="@string/ujet_company_name"/>
           <meta-data
               android:name="co.ujet.android.subdomain"
               android:value="@string/ujet_subdomain"/>
           <meta-data
               android:name="co.ujet.android.companyUrl"
               android:value="@string/ujet_company_url"/>
         </application>
         

  2. Update `android/build.gradle`.
         
         allprojects {
           repositories {
             google()
             mavenCentral()
             maven {
               url "https://sdk.ujet.co/android/"
             }
           }
         }
         

  3. Update `android/app/build.gradle`.
         
         def ujetSdkVersion = "x.y.z"
           implementation "co.ujet.android:ujet-android:$ujetSdkVersion"
           implementation "co.ujet.android:cobrowse:$ujetSdkVersion"
         }
         

  4. Run `res/values/strings.xml`.
         
         <resources>
           <string name="ujet_company_key">YOUR_COMPANY_KEY</string>
           <string name="ujet_company_name">YOUR_COMPANY_NAME</string>
         
           <!-- If your tenant / portal url ends with "ujet.co" then set ujet_subdomain string only (ignore
               ujet_company_url), otherwise set ujet_company_url only (ignore ujet_subdomain) following below instructions. -->
           <!-- To get subdomain, extract string content between 'https://' and first '.' of your tenant/portal URL. 
               Example, If your tenant url is https://XXX.YYY.ZZZ/ then subdomain will be XXX -->
           <string name="ujet_subdomain">YOUR_SUBDOMAIN</string>
         
           <!-- Use tenant url as company url here, it should be in format of https://XXX.YYY.ZZZ/api/v2
               (here XXX should match with your subdomain) -->
           <string name="ujet_company_url">YOUR_COMPANY_URL</string>
         </resources>
         

  5. Download the `google-service.json` file and put it inside of your project at the following location: `/android/app/google-services.json`




## Register the module

For more information about registering modules, see [Register the Module (Android Specific)](https://reactnative.dev/docs/native-modules-android#register-the-module-android-specific).

  1. Open ReactApplication and update the `getPackages` function.
         
         override fun getPackages(): List<ReactPackage> {
           return PackageList(this).packages.apply {
             add(MyAppPackage())
           }
         }
         

  2. Create `MyAppPackage`.
         
         import android.view.View
         import com.facebook.react.ReactPackage
         import com.facebook.react.bridge.NativeModule
         import com.facebook.react.bridge.ReactApplicationContext
         import com.facebook.react.uimanager.ReactShadowNode
         import com.facebook.react.uimanager.ViewManager
         
         class MyAppPackage: ReactPackage {
           override fun createViewManagers(
             reactContext: ReactApplicationContext
           ): MutableList<ViewManager<View, ReactShadowNode<*>>> = mutableListOf()
         
           override fun createNativeModules(
             reactContext: ReactApplicationContext
           ): MutableList<NativeModule> = listOf(
             UJETModule(reactContext)
           ).toMutableList()
         }
         


**Note:** If you already implemented ReactPackage, then add `UJETModule` in the `createNativeModules` function.

## Implement Callback

Implement `UjetRequestListener` and `ReactInstanceEventListener` from your application.
    
    
    class YourApplication: Application(), ReactApplication, UjetRequestListener, ReactInstanceEventListener {
      private var reactContext: ReactContext? = null
    
      override fun onCreate() {
        super.onCreate()
    
        Ujet.init(this)
    
        reactNativeHost.reactInstanceManager.addReactInstanceEventListener(this)
      }
    
      override fun onReactContextInitialized(reactContext: ReactContext?) {
        this.reactContext = reactContext
      }
    
      override fun onSignPayloadRequest(
        payload: MutableMap<String, Any?>,
        ujetPayloadType: UjetPayloadType,
        callback: UjetTokenCallback
      ) {
        if (reactContext == null) {
          callback.onError()
          return
        }
    
        when (ujetPayloadType) {
          UjetPayloadType.AuthToken -> {
            UJETModule.authTokenCallback = callback
            createMapAndSendEvent("authToken", payload)
          }
          UjetPayloadType.CustomData -> {
            UJETModule.customDataCallback = callback
            createMapAndSendEvent("customData", payload)
          }
          else -> callback.onError()
        }
      }
    
      override fun onRequestPushToken(): String? {
        sendEvent(reactContext ?: return, "onRequestAndroidPushToken", null)
      }
    
      private fun sendEvent(reactContext: ReactContext, eventName: String, params: WritableMap?) {
        reactContext
          .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter::class.java)
          .emit(eventName, params)
      }
    
      private fun createMapAndSendEvent(typeName: String, payload: Map<String, Any?>) {
        val writableMap = Arguments.createMap()
        for ((key, value) in payload) {
          writableMap.putString(key, value.toString())
        }
    
        val params = Arguments.createMap()
        params.putString("type", typeName)
        params.putMap("data", writableMap)
        sendEvent(reactContext ?: return, "onSignPayloadRequest", params)
      }
    }
    

## Set up push notifications

To integrate push notifications natively, follow these steps:

  1. Create `MyFirebaseMessagingService` that implements `FirebaseMessagingService`.
         
         import android.util.Log
         import co.ujet.android.Ujet
         import com.google.firebase.messaging.FirebaseMessagingService
         import com.google.firebase.messaging.RemoteMessage
         
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
         

  2. Update `AndroidManifest.xml`.
         
         <application>
           <service
             android:name=".firebase.MyFirebaseMessagingService"
             android:exported="false">
             <intent-filter>
               <action android:name="com.google.firebase.MESSAGING_EVENT" />
             </intent-filter>
           </service>
         </application>
         

  3. Create `FirebaseTokenManager`.
         
         import android.content.Context
         import com.google.android.gms.tasks.Task
         import com.google.firebase.messaging.FirebaseMessaging
         
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
         

  4. Update `android/build.gradle`.
         
         buildscript {
           dependencies {
             classpath("com.google.gms:google-services:4.4.1")
           }
         }
         

  5. Update `android/app/build.gradle`.
         
         apply plugin: 'com.google.gms.google-services'
         
         dependencies {
           implementation platform("com.google.firebase:firebase-bom:32.7.3")
           implementation 'com.google.firebase:firebase-messaging'
         }
         

  6. Initialize Firebase in `Application.onCreate`.
         
         class YourApplication: Application(), ReactApplication {
           override fun onCreate() {
             super.onCreate()
         
             firebaseTokenManager = FirebaseTokenManager(this)
           }
         }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
