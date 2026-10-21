---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/creating-client-ids/
title: Creating client IDs \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:19.536525+00:00
---

# Creating client IDs  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/creating-client-ids/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Creating client IDs Stay organized with collections  Save and categorize content based on your preferences. 

If you want to require authentication to access your API backend, you must obtain the required client IDs and supply them to the backend by using the proper API annotation attribute. 

### Android

To create the OAuth 2.0 Android client ID, you need to have a certificate key fingerprint. If you use Android Studio, a debug keystore and a debug key are created automatically. You can use the debug key for testing purposes, but you must use a release key for production. 

Note that the default debug keystore password is `android`, and the key alias is `androiddebugkey`. The default location for Linux and macOS is `~/.android/debug.keystore`. 

**Warning:** When you create a release key, don't use `android` as your release key or keystore password. 

  1. If you don't already have one, generate a debug or release key for your Android application. If you use Android Studio, it automatically generates a debug key in the debug keystore the first time you build an Android project. 
  2. In a Linux or macOS terminal window, you can get the fingerprint of the key by using the `keytool` included with the Java SDK as follows: 
         
         keytool -exportcert -alias androiddebugkey -keystore path-to-debug-or-production-keystore -list -v

The output displays a fingerprint similar to the following: `DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09`
  3. Copy and save the key fingerprint that is displayed after your run the preceding `keytool` command. You need to supply the fingerprint to generate the Android client ID in the Google Cloud console. 
  4. In the Google Cloud console, go to the **Credentials** page. 

[Go to the Credentials page](https://console.cloud.google.com/apis/credentials)

  5. From the projects list, select the project containing your API. 
  6. If this is your first time creating a client ID in this project, use the sub-steps to go to the **OAuth consent** page; otherwise, skip to the next step. 
     1. Click **OAuth consent screen**.
     2. Enter a name in the **Application name** field.
     3. Fill out the rest of the fields as needed.
     4. Click **Save**. 
  7. In the **Create credentials** drop-down list, select **OAuth client ID**. 
  8. Select **Android** as the application type. 
  9. In **Name** , enter a name for your client ID. 
  10. In **Signing-certificate fingerprint** , enter the fingerprint you obtained previously. 
  11. In **Package name** , enter the Android application package name, as specified in your `AndroidManifest.xml` file. 
  12. Click **Create**. 

You use the generated client ID in your API backend and in your client application. 




### Web client

  1. In the Google Cloud console, go to the **Credentials** page. 

[Go to the Credentials page](https://console.cloud.google.com/apis/credentials)

  2. From the projects list, select the project containing your API. 
  3. If this is your first time creating a client ID in this project, use the sub-steps to go to the **OAuth consent** page; otherwise, skip to the next step. 
     1. Click **OAuth consent screen**.
     2. Enter a name in the **Application name** field.
     3. Fill out the rest of the fields as needed.
     4. Click **Save**. 
  4. In the **Create credentials** drop-down list, select **OAuth client ID**. 
  5. Select **Web application** as the application type. 
  6. In **Name** , enter a name for your client ID. 
  7. In **Authorized JavaScript origins** , enter one of the following: 
     * `http://localhost:8080` if you are [ testing the backend locally](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy#running_and_testing_api_backends_locally). 
     * `https://YOUR_PROJECT_ID.appspot.com`, replacing `YOUR_PROJECT_ID` with your App Engine project ID if you are deploying your backend API to your production App Engine. 

**Important:** You must specify the site or host name under **Authorized JavaScript origins** using `https` for this to work with Cloud Endpoints, unless you are testing with `localhost`, in which case you must use `http`. 
  8. Click **Create**. 

You use the generated client ID in your API backend and in your client application. 




## What's next

For information about how to support authentication in your Android or JavaScript application, see the following:

  * [Authenticating users](https://docs.cloud.google.com/endpoints/docs/frameworks/java/authenticating-users)
  * [Making authenticated calls from an Android client](https://docs.cloud.google.com/endpoints/docs/frameworks/java/calling-from-android#making_authenticated_calls)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
