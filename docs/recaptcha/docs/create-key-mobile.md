---
url: https://docs.cloud.google.com/recaptcha/docs/create-key-mobile/
title: Create reCAPTCHA keys for mobile applications \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:58.405276+00:00
---

# Create reCAPTCHA keys for mobile applications  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/create-key-mobile/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Create reCAPTCHA keys for mobile applications Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create reCAPTCHA keys to verify user interactions on your mobile applications.

reCAPTCHA keys represent how reCAPTCHA is configured for a mobile application.

## Before you begin

  * [Prepare your environment for Google Cloud Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/prepare-environment). 
  * Ensure that you have the following Identity and Access Management role: reCAPTCHA Enterprise Admin (`roles/recaptchaenterprise.admin`).



## Create a reCAPTCHA key

You can create only score-based keys for mobile applications.

We recommend the following when creating reCAPTCHA keys for mobile applications:

  * Create one reCAPTCHA key for each mobile application.
  * For Android, create separate keys for the following scenarios:

    * Android package is only available on the Google Play Store.
    * Android package is only available on non-Google Play Store app stores.
  * Create separate reCAPTCHA keys for staging and production environments. Otherwise, you risk polluting reCAPTCHA risk analysis with data from your test environment.




The simplest way to create a reCAPTCHA key is through the Google Cloud console. Alternatively, you can use the reCAPTCHA Enterprise API or the Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project.

  3. Select the **Keys** tab.
  4. Click **Create key**. 
  5. In the **Display name** field, enter a display name for the key.
  6. Depending on the type of reCAPTCHA key you want to create for your mobile application, perform the appropriate action:

#### Create reCAPTCHA keys for iOS applications

We recommend creating one reCAPTCHA key per iOS application. 

     1. For the **Application type** , select **iOS**. 
        1. In the **iOS bundle ID list** section, click **Add iOS bundle ID**. 
        2. In the **Bundle ID** field, enter the name of your iOS bundle ID.

        3. Optional: To add an additional bundle ID, click **Add iOS bundle ID** and enter the name of your iOS bundle ID in the **Bundle ID** field. 
        4. To protect the reCAPTCHA key for your bundle IDs, ensure that the **Disable bundle ID verification** toggle is turned off. If you disable bundle ID verification, you must verify the `[tokenProperties.iosBundleId](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties)` field in the assessments you create.
        5. Optional: Provide **Apple Developer settings**.

We recommend providing this data because it allows Fraud Defense to provide more accurate risk scores for your traffic. 

Enter the following information: 

           * **Private key (.p8)** : This is generated in the Apple Developer Center under Certificates, Identifiers & Profiles.
           * **Key identifier** : The Apple developer key identifier (10-character string).
           * **Team ID** : The Apple team ID (10-character string) owning the provisioning profile that is used to build your application.
        6. Optional: Click **Next Step (optional)**.
           1. For your non-production environment, if you want to specify a score that you want the key to return when any assessments are created for it, do the following: 

              1. In **Additional settings** , click the **Are you creating this key for testing purposes only?** toggle.
              2. Use the **Set score** slider to specify a score between 0 to 1.0.
        7. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.

#### Create reCAPTCHA keys for Android applications

     1. For the **Application type** , select **Android**.  

     2. In the **Android package list** section, click **Add Android package**.
     3. In the **Android package** field, enter the name of your Android package. 
     4. Optional: To add an additional package, click **Add Android package** and enter the name of another Android package in the **Android package** field.
     5. To enforce that reCAPTCHA key is only used within your app, turn off the **Disable package name verification** toggle. If you disable package name verification, you must verify the `[tokenProperties.androidPackageName](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties)` field in the assessments you create. 
     6. If you want to create a key for an application that is available on other app stores in addition to the Google Play Store, turn on **Support applications distributed outside of the Google Play Store**. 
     7. Optional: Click **Next Step (optional)**.
        1. For your non-production environment, if you want to specify a score that you want the key to return when any assessments are created for it, do the following: 

           1. In **Additional settings** , click the **Are you creating this key for testing purposes only?** toggle.
           2. Use the **Set score** slider to specify a score between 0 to 1.0.
     8. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.




### gcloud (iOS)

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

Before using any of the command data below, make the following replacements: 

  * DISPLAY_NAME: Name for the key. Typically a site name.
  * BUNDLE_IDs: iOS bundle ids of apps allowed to use the key. Specify multiple bundle IDs as a comma-separated list.



Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud recaptcha keys create \
    --display-name=DISPLAY_NAME  \
    --ios --bundle-ids=BUNDLE_IDs

#### Windows (PowerShell)
    
    
    gcloud recaptcha keys create `
    --display-name=DISPLAY_NAME  `
    --ios --bundle-ids=BUNDLE_IDs

#### Windows (cmd.exe)
    
    
    gcloud recaptcha keys create ^
    --display-name=DISPLAY_NAME  ^
    --ios --bundle-ids=BUNDLE_IDs

The response contains the newly created reCAPTCHA key. 

### gcloud (Android)

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

Before using any of the command data below, make the following replacements: 

  * DISPLAY_NAME: Name for the key. Typically a site name.
  * PACKAGE_NAMES: Android package names of apps allowed to use the key. Specify multiple package names as a comma-separated list.



Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud recaptcha keys create \
    --display-name=DISPLAY_NAME  \
    --android --package-names=PACKAGE_NAMES

#### Windows (PowerShell)
    
    
    gcloud recaptcha keys create `
    --display-name=DISPLAY_NAME  `
    --android --package-names=PACKAGE_NAMES

#### Windows (cmd.exe)
    
    
    gcloud recaptcha keys create ^
    --display-name=DISPLAY_NAME  ^
    --android --package-names=PACKAGE_NAMES

The response contains the newly created reCAPTCHA key. 

### REST (iOS)

Before using any of the request data, make the following replacements: 

  * DISPLAY_NAME: Name for the key. Typically an app name.
  * BUNDLE_IDs: iOS bundle ids of apps allowed to use the key. Specify multiple bundle IDs as a comma-separated list.



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME",
      "iosSettings": {
       "allowedBundleIds":"BUNDLE_IDs"
    
      }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "projects/project-id/keys/6LfhtywnAAAAABY3sCS2duZ6A55kmDXz-PNEgKgT",
      "displayName": "DISPLAY_NAME",
      "iosSettings": {
        "allowAllBundleIds": false,
        "allowedBundleIds": [
            BUNDLE_IDS
        ]
      },
      "labels": {},
    }
    
    

### REST (Android)

Before using any of the request data, make the following replacements: 

  * DISPLAY_NAME: Name for the key. Typically an app name.
  * PACKAGE_NAMES: Android package names of apps allowed to use the key. Specify multiple package names as a comma-separated list.



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    
    
    {
      "displayName": "DISPLAY_NAME",
      "androidSettings": {
      "allowedPackageNames":"PACKAGE_NAMES"
      }
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "projects/project-id/keys/6LcioSknAAAAABrjlMuZv2fjIGYMqwaAFC9izhoy",
      "displayName": "DISPLAY_NAME",
      "androidSettings": {
          "allowAllPackageNames": false,
          "allowedPackageNames": [
              PACKAGE_NAMES
          ],
          "supportNonGoogleAppStoreDistribution": false
      },
      "labels": {},
    }
    
    

**Note:** After creating reCAPTCHA keys, you can edit or delete them. You cannot recover deleted keys. Also, you cannot migrate reCAPTCHA keys from one Google Cloud project to another.

## What's next

  * [Install keys on iOS](https://docs.cloud.google.com/recaptcha/docs/instrument-ios-apps).
  * [Install keys on Android](https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
