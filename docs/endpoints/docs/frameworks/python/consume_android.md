---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/consume_android/
title: Calling backend APIs from an Android client \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:22.576233+00:00
---

# Calling backend APIs from an Android client  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/consume_android/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Calling backend APIs from an Android client Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how an Android client calls a backend API built with Cloud Endpoints Frameworks for App Engine.

**Note:** These instructions assume familiarity with Android development and concepts including project setup, Activities and AsyncTasks classes, shared preferences, Android permissions, and Intents. If you want to learn more about these concepts, refer to the [Android documentation and examples](http://developer.android.com).**Note:** For information and sample code showing how to access a backend API from a Python client, see [Accessing backend APIs from Python clients](https://docs.cloud.google.com/endpoints/docs/frameworks/python/access_from_python).

## Generating the client library

Your Android client requires the client library generated from the backend API your client is using. If you don't have the client library yet, see [Generating a client library](https://docs.cloud.google.com/endpoints/docs/frameworks/python/gen_clients) for details. There are steps in this document that explain how you add the client library to the Android client project.

## Setting up the project

In these instructions, you use [Android Studio](http://developer.android.com/sdk/installing/studio.html). If you haven't already done so, you need to set up Android Studio to support a client that uses the frameworks.

## Configuring the project

In Android Studio, your project uses the `build.gradle` file for dependencies and other settings. By default, Android Studio creates a parent project-level `build.gradle` file and an Android app-specific one in the Android module. These instructions are for the app-specific `build.gradle` in the Android module.

To configure `build.gradle`:

  1. Double-click **`build.gradle`** to open it.

  2. Edit this file so it contains the following lines:
         
         buildscript {
             repositories {
                 mavenCentral()
             }
             dependencies {
                 classpath 'com.android.tools.build:gradle:1.0.0'
             }
         }
         apply plugin: 'com.android.application'
         
         repositories {
             mavenCentral()
             mavenLocal()
         }
         
         android {
             compileSdkVersion 26
         
             defaultConfig {
                 applicationId "com.mycompany.myapp"
                 minSdkVersion 17
                 targetSdkVersion 26
                 versionCode 1
                 versionName "1.0"
             }
             buildTypes {
                 release {
                     minifyEnabled false
                     proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
                 }
             }
             packagingOptions {
                 exclude 'META-INF/DEPENDENCIES'
             }
         }
         
         dependencies {
             implementation 'com.android.support:appcompat-v7:26.1.0'
             implementation 'com.android.support.constraint:constraint-layout:1.1.3'
             // BEGIN Google APIs
             // Play Services will validate the application prior to allowing OAuth2 access.
             implementation 'com.google.android.gms:play-services-auth:16.0.0'
             implementation 'com.google.android.gms:play-services-identity:16.0.0'
             // The following lines implement maven imports as defined at:
             // https://github.com/googleapis/google-api-java-client/wiki/Setup-Instructions
             // Add the Google API client library.
             implementation('com.google.api-client:google-api-client:1.28.0') {
                 // Exclude artifacts that the Android SDK/Runtime provides.
                 exclude(group: 'xpp3', module: 'xpp3')
                 exclude(group: 'org.apache.httpcomponents', module: 'httpclient')
                 exclude(group: 'junit', module: 'junit')
                 exclude(group: 'com.google.android', module: 'android')
             }
             // Add the Android extensions for the Google API client library.
             // This will automatically include play services as long as you have download that library
             // from the Android SDK manager.
             // Add the Android extensions for the Google API client library.
             implementation(group: 'com.google.api-client', name: 'google-api-client-android', version: '1.25.0') {
                        // Exclude play services, since we're not using this yet.
                       exclude(group: 'com.google.android.gms:play-services', module: 'google-play-services')
             }
             // END Google APIs
             // The following client libraries make HTTP/JSON on Android easier.
             // Android extensions for Google HTTP Client.
             implementation('com.google.http-client:google-http-client-android:1.21.0') {
                 exclude(group: 'com.google.android', module: 'android')
             }
             implementation 'com.google.http-client:google-http-client-gson:1.21.0'
             // This is used by the Google HTTP client library.
             implementation 'com.google.guava:guava:18.0+'
             implementation files('libs/echo-v1-1.25.0-SNAPSHOT.jar')
         }
         
         

Replace `com.mycompany.myapp` with your own values.

  3. Click **File** > **Save All** and then exit Android Studio and restart it.




## Adding the client library to the project

To add the client library to the Android project:

  1. Add a `/libs` directory to your project if it doesn't already have one. It is a peer to the `/src` directory.

  2. Copy the client library generated from the backend API into `/libs`.

  3. Right-click the library you just added, and then select **Add As Library** to your project.




## Creating the service object

In your project code, you must use a service object to make requests to the backend API. For _unauthenticated_ requests, construct the service object as follows:
    
    
    BACKEND_API_NAME.Builder builder = new BACKEND_API_NAME.Builder(
        NetHttpTransport(), new GsonFactory(), null);
    service = builder.build();
    

Replace `BACKEND_API_NAME` with the name of your backend API.

**Important:** For authenticated calls, you need to supply credentials to the service object, as described in Making authenticated calls.

## Calling the backend API

In your project, call the API using the service object. For example:
    
    
    ScoreCollection scores = service.scores().list().execute();
    

In this snippet, you are requesting a list of all `Score` objects on the server. If `list` required parameters, or a request body, you provide them in the command. Android Studio provides code completion to identity available method calls, and their required parameters.

It is important to note that because API calls result in requests over the network, you are required to make requests in their own thread. (This requirement was added to recent versions of Android, but it is a best practice even in older versions.) To do this, you use a `Thread` or `AsyncTask`. For example:
    
    
    private class QueryScoresTask extends AsyncTask<Void, Void, ScoreCollection>{
      Context context;
    
      public QueryScoresTask(Context context) {
        this.context = context;
      }
    
      protected Scores doInBackground(Void... unused) {
        ScoreCollection scores = null;
        try {
          scores = service.scores().list().execute();
        } catch (IOException e) {
          Log.d("TicTacToe", e.getMessage(), e);
        }
        return scores;
      }
    
      protected void onPostExecute(ScoreCollection scores) {
        // Do something with the result.
      }
    }
    

## Making authenticated calls

**Important:** For information on authentication from the perspective of keeping the backend secure, see the blog post [Verifying backend calls from Android apps](https://android-developers.blogspot.com/2013/01/verifying-back-end-calls-from-android.html). These instructions cover only the client coding you need to add. They assume that you have already added the Endpoints Frameworks support for authentication as described in [Authenticating users](https://docs.cloud.google.com/endpoints/docs/frameworks/python/authenticating-users). 

If your Android client is making calls to an endpoint that requires authentication, you must:

  * Configure your Android Client to provide credentials to the service object.
  * Use the account picker to support user choice of login accounts.



The following sections provide details.

### Configuring your Android client to provide credentials

To support requests to a backend API that requires authentication, your Android client needs to get user credentials and pass them to the service object. 

Getting the user credentials and using the account picker requires you to have the following Android permissions:
    
    
    <uses-permission android:name="android.permission.GET_ACCOUNTS" />
    <uses-permission android:name="android.permission.USE_CREDENTIALS" />
    

To get the user credentials, you call `GoogleAccountCredential.usingAudience` as follows:
    
    
    // Inside your Activity class onCreate method
    settings = getSharedPreferences(
        "TicTacToeSample", 0);
    credential = GoogleAccountCredential.usingAudience(this,
        "server:client_id:1-web-app.apps.googleusercontent.com");
    

Where the second parameter to the call is the prefix `server:client_id` prepended to the web client ID of the backend API.

#### Sample code: getting credentials for the service object

The following code shows how to get credentials and pass it to the service object:
    
    
    // Inside your Activity class onCreate method
    settings = getSharedPreferences("TicTacToeSample", 0);
    credential = GoogleAccountCredential.usingAudience(this,
        "server:client_id:1-web-app.apps.googleusercontent.com");
    setSelectedAccountName(settings.getString(PREF_ACCOUNT_NAME, null));
    
    Tictactoe.Builder builder = new Tictactoe.Builder(
        NetHttpTransport(), new GsonFactory(),
        credential);
    service = builder.build();
    
    if (credential.getSelectedAccountName() != null) {
      // Already signed in, begin app!
    } else {
      // Not signed in, show login window or request an account.
    }
    
    // setSelectedAccountName definition
    private void setSelectedAccountName(String accountName) {
      SharedPreferences.Editor editor = settings.edit();
      editor.putString(PREF_ACCOUNT_NAME, accountName);
      editor.commit();
      credential.setSelectedAccountName(accountName);
      this.accountName = accountName;
    }
    

The preceding sample code looks up any shared preferences stored by the Android app and attempts to find the name of the account the user wants to use to authenticate to your application. If successful, the code creates a credentials object and passes it into your service object. These credentials let your Android app pass the appropriate token to your backend.

Notice that the code sample checks to see whether or not the Android app already knows which account to use. If it does, the logical flow can continue on and run the Android app. If the app doesn't know which account to use, the app displays a login screen or prompt the user to pick an account.

Finally, the sample creates a credentials object and passes it into the service object. These credentials let your Android app pass the appropriate token to your App Engine web app.

### Using the account picker

Android provides an intent to select a user account. You can invoke this as follows:
    
    
    static final int REQUEST_ACCOUNT_PICKER = 2;
    
    void chooseAccount() {
      startActivityForResult(credential.newChooseAccountIntent(),
          REQUEST_ACCOUNT_PICKER);
    }
    

A handler for interpreting the result of this intent is shown here:
    
    
    @Override
    protected void onActivityResult(int requestCode, int resultCode,
       Intent data) {
     super.onActivityResult(requestCode, resultCode, data);
     switch (requestCode) {
       case REQUEST_ACCOUNT_PICKER:
         if (data != null && data.getExtras() != null) {
           String accountName =
               data.getExtras().getString(
                   AccountManager.KEY_ACCOUNT_NAME);
           if (accountName != null) {
             setSelectedAccountName(accountName);
             SharedPreferences.Editor editor = settings.edit();
             editor.putString(PREF_ACCOUNT_NAME, accountName);
             editor.commit();
             // User is authorized.
           }
         }
         break;
      }
    }
    

## Testing an Android client against a local development server

You can test your client against a backend API running in production App Engine at any time without making any changes. However, if you want to test your client against a backend API running on the local development server, you need to change tne line of code in the client to point to the IP address of the machine running the local development server.

**Note:** You can use either an Android Virtual Device (AVD) emulator, or a physical device. However, physical devices must use the same Wi-Fi as the system running the local development server.

To make the required changes and test using the local development server:

  1. Make a note of the IP address of the machine that is running the local development server because you need it when you add code to the Android client.

  2. Start the local development server, as described in [Testing an API locally](https://docs.cloud.google.com/endpoints/docs/frameworks/python/test-deploy#testing_an_api_locally). 

  3. In your Android Studio client project, locate the code that gets the handle to the backend API service. Typically, this code uses a `Builder` to set up the API request.

  4. Override the root URL on the `Builder` object (this is the URL the Android client connects to in the backend API call) by adding the line:
         
         yourBuilderObject.setRootUrl("http://YOUR_MACHINE_IP_ADDRESS:8080/_ah/api");
         

For example:
         
         public static Helloworld getApiServiceHandle(@Nullable GoogleAccountCredential credential) {
           // Use a builder to help formulate the API request.
           Helloworld.Builder helloWorld = new Helloworld.Builder(AppConstants.HTTP_TRANSPORT,
               AppConstants.JSON_FACTORY,credential);
         
           helloWorld.setRootUrl("http://YOUR_MACHINE_IP_ADDRESS:8080/_ah/api");
           return helloWorld.build();
         }
         

Replace `YOUR_MACHINE_IP_ADDRESS` with your system's IP address.

  5. Rebuild your Android client project.

  6. If you want to run your client app on an AVD emulator:

     1. In Android Studio, go to **Tools** > **Android** > **AVD Manager** and start an existing AVD if you have one, otherwise create one, and then start it.
     2. Go to **Run** > **Debug` YOUR_PROJECT_NAME`** where `YOUR_PROJECT_NAME` represents the name of your Google Cloud project.
     3. When prompted to choose a device, select your AVD.
     4. Test your client.
  7. If you want to run your client app on a physical Android device:

     1. Make sure your Android device is [enabled for debugging](http://developer.android.com/tools/device.html#setting-up).
     2. In Android Studio, go to **Run** > **Debug` YOUR_PROJECT_NAME`**.
     3. When prompted to choose a device, select your physical Android device.
     4. Test your client.

**Important:** If the backend API is Auth-protected, your client must provide support as described in Adding authentication support with OAuth 2.0. However, when running against the local development server, no credentials page is displayed in response to a user's attempt to sign in. Instead, the sign-on simply occurs, granting the user access to the protected API, _and the user returned is always`example@example.com`_.

## Sample client source code

For sample code, see the [Android Cloud Endpoints v2.0 example](https://github.com/GoogleCloudPlatform/android-docs-samples/tree/master/endpoints-frameworks/v2).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
