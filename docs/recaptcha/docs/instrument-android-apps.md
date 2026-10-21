---
url: https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps/
title: Integrate Google Cloud Fraud Defense with Android apps \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:02:10.596175+00:00
---

# Integrate Google Cloud Fraud Defense with Android apps  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Integrate Google Cloud Fraud Defense with Android apps Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to integrate Google Cloud Fraud Defense in your Android app.

The SDK uses reflection and dynamic code to allow modification and refinement of the detection system in the existing deployed applications/SDKs. The set of classes that are available in the system are restricted to a controlled list to avoid interference with the application.

**Important:** Take note of the [deprecation and shutdown policy](https://docs.cloud.google.com/recaptcha/docs/deprecation-policy-mobile) and plan to upgrade the SDK on a regular basis.

## Before you begin

  1. [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 

  2. [Create a reCAPTCHA Key](https://cloud.google.com/recaptcha/docs/create-key-mobile) for the Android app platform.

Alternatively, you can copy the ID of an existing reCAPTCHA key for Android by performing one of the following steps:

     * To copy the ID of an existing key from the **Google Cloud console** , do the following:

       1. Go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

       2. Select the **Keys** tab.
       3. In the reCAPTCHA keys list, find the key you want to copy, and then click  content_copy . 
     * To copy the ID of an existing key using the **REST API** , use the [projects.keys.list](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys/list) method. 
     * To copy the ID of an existing key using the **gcloud CLI** , use the [gcloud recaptcha keys list](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/list) command. 



## Prepare your Android environment

**Warning:** Don't migrate to Android SDK 18.2.0, because it might make your app non-functional due to some internal errors. To avoid these problems, migrate directly to Android SDK 18.2.1 or later. For details, see the [issue report on GitHub](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/52).

### Native Android

  1. Prepare your development environment by downloading and installing [the latest version of Android Studio](https://developer.android.com/studio).

  2. Ensure that you have an app with the minimum Android SDK value set to **API 23: Android 6.0 (Marshmallow)**.

  3. If you are creating a new mobile app, create a test application by starting a new Android Studio project:

     1. Select **Empty Activity**. If you want to use [Jetpack Compose](https://developer.android.com/jetpack/compose) on your app choose **Empty Compose Activity**.
     2. Set the language to **kotlin**.
     3. Set the minimum SDK value to **API 23: Android 6.0 (Marshmallow)**.
  4. Ensure that Google's Maven repository `google()` is in the list of repositories in the project-level `build.gradle` file as shown in the following snippet:
         
         allprojects {
             repositories {
                 google()
             }
         }
         

For more information, see [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven).

  5. To add the reCAPTCHA API dependency, add the following build rule to the `dependencies` section of your app-level `build.gradle` file.
         
         implementation 'com.google.android.recaptcha:recaptcha:18.9.3'
         

For more information about adding dependencies in Android apps, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

  6. Add internet permission between the first `<manifest>` tag and the first `<application>` tag in your application's manifest (for example, `AndroidManifest.xml`). This permission is required because the reCAPTCHA API involves network operations.
         
         <manifest ...>
         
             <uses-permission android:name="android.permission.INTERNET" />
         
             <application ...>
             ...
           </application>
         </manifest>
         

  7. If you want to use `AndroidX` libraries in your new project, compile the SDK to Android 9.0 or higher and add the following code snippet to your `gradle.properties`.
         
         android.useAndroidX=true
         android.enableJetifier=true
         

For more information, see [Migrating to AndroidX](https://developer.android.com/jetpack/androidx/migrate).




### Flutter

For detailed instructions about using reCAPTCHA through Flutter, see the [Flutter documentation](https://pub.dev/packages/recaptcha_enterprise_flutter).

### React Native

For detailed instructions about using reCAPTCHA through React Native, see the [React Native documentation](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-react-native).

## Integrate reCAPTCHA with your Android app

  1. Instantiate a client by using the reCAPTCHA key (KEY_ID) that you created for your Android app.

**Note:** You must use the reCAPTCHA client only once during the lifetime of your app.

### Kotlin with `fetchClient`

The `fetchClient` method returns a client immediately and starts initializing the SDK in the background. It retries the communication with the reCAPTCHA server on network failures.
         
         class CustomApplication : Application() {
         
             private lateinit var recaptchaClient: RecaptchaClient
             // we recommend initializing in a ViewModel
             private val recaptchaScope = CoroutineScope(Dispatchers.IO)
         
             override fun onCreate() {
               super.onCreate()
               initializeRecaptchaClient()
             }
         
             private fun initializeRecaptchaClient() {
               recaptchaScope.launch {
                 try {
                   recaptchaClient = Recaptcha.fetchClient(this@CustomApplication, "KEY_ID")
                 } catch(e: RecaptchaException) {
                   // Handle errors ...
                   // See "Handle errors" section
                 }
               }
             }
         }
         

### Java with `fetchClient`
         
         public final class CustomApplication extends Application {
           @Nullable private RecaptchaTasksClient recaptchaTasksClient = null;
         
           @Override
           public void onCreate() {
             super.onCreate();
             initializeRecaptchaClient();
           }
         
           private void initializeRecaptchaClient() {
             Recaptcha
               .fetchTaskClient(this, "KEY_ID")
               .addOnSuccessListener(
                   this,
                   new OnSuccessListener<RecaptchaTasksClient>() {
                     @Override
                     public void onSuccess(RecaptchaTasksClient client) {
                       CustomApplication.this.recaptchaTasksClient = client;
                     }
                   })
               .addOnFailureListener(
                   this,
                   new OnFailureListener() {
                     @Override
                     public void onFailure(@NonNull Exception e) {
                       // Handle errors ...
                       // See "Handle errors" section
                     }
                   });
           }
         }
         

Initialization of the SDK can take several seconds to complete. To mitigate this latency, initialize the client as early as possible, such as during the `onCreate()` call of a custom `Application` class. You shouldn't make UI elements block on the reCAPTCHA SDK.

**Note:** If the API passes an instance of `ApiException` into `onFailure()`, you must handle each possible status code that you can retrieve using `getStatusCode()`. For more information, see Handle errors.
  2. For each action of your app that is protected using reCAPTCHA, call the `execute` method passing a [RecaptchaAction](https://cloud.google.com/recaptcha/docs/reference/android/com/google/android/recaptcha/RecaptchaAction). The reCAPTCHA library provides a built-in set of actions and if necessary, you can create custom actions.

The following code snippet shows how to use `execute` to protect a `LOGIN` action.

### Kotlin
         
         private fun executeLoginAction() {
           recaptchaScope.launch {
             recaptchaClient
               .execute(RecaptchaAction.LOGIN)
               .onSuccess { token ->
                 // Handle success ...
                 // See "What's next" section for instructions
                 // about handling tokens.
               }
               .onFailure { exception ->
                 // Handle errors ...
               }
           }
         }
         

### Java
         
         private void executeLoginAction(View v) {
           assert recaptchaTasksClient != null;
           recaptchaTasksClient
             .executeTask(RecaptchaAction.LOGIN)
             .addOnSuccessListener(
                 this,
                 new OnSuccessListener<String>() {
                   @Override
                   public void onSuccess(String token) {
                     // Handle success ...
                     // See "What's next" section for instructions
                     // about handling tokens.
                   }
                 })
             .addOnFailureListener(
                 this,
                 new OnFailureListener() {
                   @Override
                   public void onFailure(@NonNull Exception e) {
                     // Handle errors ...
                   }
                 });
         }
         


**Note:** Google Play Store requires you to fill out Google Play's data safety form before uploading your app to the Play Store. Review [Google Play's data disclosure requirements](https://docs.cloud.google.com/recaptcha/docs/disclosure-requirements-android) to find the information you need about the reCAPTCHA Android SDK to fill out the data safety form.

## Migrate from getClient method to fetchClient method

The `fetchClient` method returns a [RecaptchaClient](https://docs.cloud.google.com/recaptcha/docs/reference/android/com/google/android/recaptcha/RecaptchaClient) that retries initialization over network failures. If the app doesn't have network access when the client is created, the client keeps retrying and successfully initializes when a network is acquired.

If you call `execute(timeout)` and the client is not yet ready, it tries to initialize before returning a token or a [RecaptchaErrorCode](https://docs.cloud.google.com/recaptcha/docs/reference/android/com/google/android/recaptcha/RecaptchaErrorCode).

The following example shows how to migrate from `getClient` to `fetchClient`.

### Kotlin
    
    
    // Migrate from getClient
    private fun initializeWithGetClient() {
      recaptchaScope.launch {
        Recaptcha.getClient(application, "KEY_ID")
          .onSuccess { client ->
            recaptchaClient = client
          }
          .onFailure { exception ->
            // Handle errors ...
          }
      }
    }
    
     // Migrate to fetchClient
    private fun initializeWithFetchClient() {
      recaptchaScope.launch {
        try {
          recaptchaClient = Recaptcha.fetchClient(application, "KEY_ID")
        } catch(e: RecaptchaException){
          // Handle errors ...
        }
      }
    }
    

### Java
    
    
      // Migrate from getTasksClient
      private void initializeWithGetTasksClient() {
        Recaptcha
          .getTasksClient(getApplication(), "KEY_ID")
          .addOnSuccessListener(
              this,
              new OnSuccessListener<RecaptchaTasksClient>() {
                @Override
                public void onSuccess(RecaptchaTasksClient client) {
                  recaptchaTasksClient = client;
                }
              })
          .addOnFailureListener(
              this,
              new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                  // Handle errors ...
                }
              });
      }
    
      // Migrate to fetchTaskClient
      private void initializeWithFetchTaskClient() {
        Recaptcha
          .fetchTaskClient(getApplication(), "KEY_ID")
          .addOnSuccessListener(
              this,
              new OnSuccessListener<RecaptchaTasksClient>() {
                @Override
                public void onSuccess(RecaptchaTasksClient client) {
                  recaptchaTasksClient = client;
                }
              })
          .addOnFailureListener(
              this,
              new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                  // Handle errors ...
                }
              });
      }
    

## Set a timeout for API calls

You can specify a timeout value for the `execute` APIs by using the `withTimeout` property.

### Kotlin

  * Set timeout when calling `execute`.
        
        recaptchaScope.launch {
              recaptchaClient
                .execute(RecaptchaAction.LOGIN, timeout = 10000L)
                .onSuccess { token ->
                  // Handle success ...
                  // See "What's next" section for instructions
                  // about handling tokens.
                }
                .onFailure { exception ->
                  // Handle errors ...
                  // See "Handle errors" section
                }
            }
        

This code snippet sets the timeout of `execute` to 10 seconds.




### Java

  * Set timeout when calling `execute`.
        
        recaptchaTasksClient
            .executeTask(RecaptchaAction.custom("redeem"), 10000L)
            .addOnSuccessListener(
                this,
                new OnSuccessListener<String>() {
                  @Override
                  public void onSuccess(String token) {
                    // Handle success ...
                    // See "What's next" section for instructions
                    // about handling tokens.
                  }
                })
            .addOnFailureListener(
                this,
                new OnFailureListener() {
                  @Override
                  public void onFailure(@NonNull Exception e) {
                    // Handle errors ...
                    // See "Handle errors" section
                  }
                });
        

This code snippet sets the timeout of `execute` to 10 seconds.




## Handle errors

If your app cannot communicate with the reCAPTCHA service successfully, it might be because the API encountered an error. You must add logic in your app to gracefully handle such errors.

For more details about mitigations for common API errors, see [RecaptchaErrorCode](https://cloud.google.com/recaptcha/docs/reference/android/com/google/android/recaptcha/RecaptchaErrorCode).

## API reference

For a complete reference of the reCAPTCHA API for Android, see [`com.google.android.recaptcha`](https://cloud.google.com/recaptcha/docs/reference/android/com/google/android/recaptcha/package-summary).

## What's next

  * To assess the reCAPTCHA response token, [create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment-mobile).

**Note:** reCAPTCHA response tokens are assessed and annotated from your backend server, not from the mobile device.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
