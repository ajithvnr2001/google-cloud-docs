---
url: https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca-mobile/
title: Integrate with Google Cloud Armor for mobile applications \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:15.551141+00:00
---

# Integrate with Google Cloud Armor for mobile applications  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca-mobile/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Integrate with Google Cloud Armor for mobile applications Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to integrate the features of Google Cloud Fraud Defense with Cloud Armor on mobile applications.

To complete the integration, you must implement one or more features of reCAPTCHA and configure Cloud Armor security policies. However, you can implement only reCAPTCHA action-tokens for integrating with Cloud Armor on mobile applications.

## Before you begin

  1. Enable the reCAPTCHA Enterprise API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recaptchaenterprise.googleapis.com&redirect=https%3A//console.cloud.google.com)

  2. Identify the actions that you want to protect.




## Implement reCAPTCHA action-tokens

You must have reCAPTCHA running on your mobile application to generate action-tokens. After reCAPTCHA generates an action-token, you attach the action-token to a predefined request header wherever you need to protect any user action, such as `checkout`. By default, action-tokens are valid for 30 minutes, but can vary depending on the traffic. You must attach the action-token to a predefined request header before the token expires, so that the Cloud Armor can evaluate the token attributes. 

To implement a reCAPTCHA action-token, do the following:

  1. Create an action-token key for your mobile application.

### Console

     1. In the Google Cloud console, go to the **Google Cloud Fraud Defense** page.

[Go to Google Cloud Fraud Defense](https://console.cloud.google.com/security/recaptcha)

     2. Verify that the name of your project appears in the resource selector at the top of the page.

If you don't see the name of your project, click the resource selector, then select your project.

     3. Select the **Keys** tab.
     4. Click **Create key**. 
     5. In the **Display name** field, enter a display name for the key.
     6. Depending on the type of application for which you want to create the reCAPTCHA keys for WAF, perform the appropriate action:
**Note:** You can create only action-token keys for mobile applications. 

#### Create reCAPTCHA keys for WAF for iOS applications

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
              1. To create a reCAPTCHA key for WAF, do the following: 
                 1. In **Additional settings** , turn on the 
                 2. In **Additional settings** , turn on the **Will you deploy this key in a Web Application Firewall (WAF)?** toggle.
                 3. From the **Service** options, select **Cloud Armor.**
                 4. From the **Feature** options, select **Action**.
              2. For your non-production environment, if you want to specify a score that you want the key to return when any assessments are created for it, do the following: 

                 1. In **Additional settings** , click the **Are you creating this key for testing purposes only?** toggle.
                 2. Use the **Set score** slider to specify a score between 0 to 1.0.
           7. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.

#### Create reCAPTCHA keys for WAF for Android applications

        1. For the **Application type** , select **Android**.  

        2. In the **Android package list** section, click **Add Android package**.
        3. In the **Android package** field, enter the name of your Android package. 
        4. Optional: To add an additional package, click **Add Android package** and enter the name of another Android package in the **Android package** field.
        5. To enforce that reCAPTCHA key is only used within your app, turn off the **Disable package name verification** toggle. If you disable package name verification, you must verify the `[tokenProperties.androidPackageName](https://docs.cloud.google.com/recaptcha/docs/reference/rpc/google.cloud.recaptchaenterprise.v1#tokenproperties)` field in the assessments you create. 
        6. If you want to create a key for an application that is available on other app stores in addition to the Google Play Store, turn on **Support applications distributed outside of the Google Play Store**. 
        7. Optional: Click **Next Step (optional)**.
           1. To create a reCAPTCHA key for WAF, do the following: 
              1. In **Additional settings** , turn on the 
              2. In **Additional settings** , turn on the **Will you deploy this key in a Web Application Firewall (WAF)?** toggle.
              3. From the **Service** options, select **Cloud Armor.**
              4. From the **Feature** options, select **Action**.
           2. For your non-production environment, if you want to specify a score that you want the key to return when any assessments are created for it, do the following: 

              1. In **Additional settings** , click the **Are you creating this key for testing purposes only?** toggle.
              2. Use the **Set score** slider to specify a score between 0 to 1.0.
        8. Click **Create key**.

The newly created key is listed on the **reCAPTCHA keys** page.

### gcloud (iOS)

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

**Note:** Creating reCAPTCHA keys for WAF on mobile applications is supported only for integration with Cloud Armor. For this integration, you can create only action-token keys for mobile applications. 

Before using any of the command data below, make the following replacements: 

     * DISPLAY_NAME: Name for the key. Typically a site name.
     * BUNDLE_IDs: iOS bundle ids of apps allowed to use the key. Specify multiple bundle IDs as a comma-separated list.
     * WAF_FEATURE: Name of the WAF feature. Specify `action-token`. 
     * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 

Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud recaptcha keys create \
    --display-name=DISPLAY_NAME  \
    --ios --bundle-ids=BUNDLE_IDs \
    --waf-feature=WAF_FEATURE \
    --waf-service=WAF_SERVICE 

#### Windows (PowerShell)
    
    gcloud recaptcha keys create `
    --display-name=DISPLAY_NAME  `
    --ios --bundle-ids=BUNDLE_IDs `
    --waf-feature=WAF_FEATURE `
    --waf-service=WAF_SERVICE 

#### Windows (cmd.exe)
    
    gcloud recaptcha keys create ^
    --display-name=DISPLAY_NAME  ^
    --ios --bundle-ids=BUNDLE_IDs ^
    --waf-feature=WAF_FEATURE ^
    --waf-service=WAF_SERVICE 

The response contains the newly created reCAPTCHA key. 

### gcloud (Android)

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

**Note:** Creating reCAPTCHA keys for WAF on mobile applications is supported only for integration with Cloud Armor. For this integration, you can create only action-token keys for mobile applications. 

Before using any of the command data below, make the following replacements: 

     * DISPLAY_NAME: Name for the key. Typically a site name.
     * PACKAGE_NAMES: Android package names of apps allowed to use the key. Specify multiple package names as a comma-separated list.
     * WAF_FEATURE: Name of the WAF feature. Specify `action-token`. 
     * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 

Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud recaptcha keys create \
    --display-name=DISPLAY_NAME  \
    --android --package-names=PACKAGE_NAMES \
    --waf-feature=WAF_FEATURE \
    --waf-service=WAF_SERVICE 

#### Windows (PowerShell)
    
    gcloud recaptcha keys create `
    --display-name=DISPLAY_NAME  `
    --android --package-names=PACKAGE_NAMES `
    --waf-feature=WAF_FEATURE `
    --waf-service=WAF_SERVICE 

#### Windows (cmd.exe)
    
    gcloud recaptcha keys create ^
    --display-name=DISPLAY_NAME  ^
    --android --package-names=PACKAGE_NAMES ^
    --waf-feature=WAF_FEATURE ^
    --waf-service=WAF_SERVICE 

The response contains the newly created reCAPTCHA key. 

### REST (iOS)

**Note:** Creating reCAPTCHA keys for WAF on mobile applications is supported only for integration with Cloud Armor. For this integration, you can create only action-token keys for mobile applications. 

Before using any of the request data, make the following replacements: 

     * DISPLAY_NAME: Name for the key. Typically an app name.
     * BUNDLE_IDs: iOS bundle ids of apps allowed to use the key. Specify multiple bundle IDs as a comma-separated list.
     * WAF_FEATURE: Name of the WAF feature. Specify `action-token`. 
     * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    {
      "displayName": "DISPLAY_NAME",
      "iosSettings": {
     "allowedBundleIds": "BUNDLE_IDS"
     },
       'wafSettings': "  {
           "wafService": "CA",
     "wafFeature": "ACTION_TOKEN"
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
      "wafSettings": {
          "wafService": "CA",
          "wafFeature": "ACTION_TOKEN"
      }
    }
    
    

### REST (Android)

**Note:** Creating reCAPTCHA keys for WAF on mobile applications is supported only for integration with Cloud Armor. For this integration, you can create only action-token keys for mobile applications. 

Before using any of the request data, make the following replacements: 

     * DISPLAY_NAME: Name for the key. Typically an app name.
     * PACKAGE_NAMES: Android package names of apps allowed to use the key. Specify multiple package names as a comma-separated list.
     * WAF_FEATURE: Name of the WAF feature. Specify `action-token`. 
     * WAF_SERVICE: Name of the WAF service provider. Specify `CA` for Cloud Armor. 

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    {
      "displayName": "DISPLAY_NAME",
      "androidSettings": {
      "allowedPackageNames":"PACKAGE_NAMES"
     },
       'wafSettings': "  {
           "wafService": "CA",
     "wafFeature": "ACTION_TOKEN"
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
      "wafSettings": {
          "wafService": "CA",
          "wafFeature": "ACTION_TOKEN"
      }
    }
    
    

  2. Integrate reCAPTCHA mobile SDK on your mobile applications with the action-token key that you created. For instructions, refer to the document that corresponds with the type of your mobile application. 

     * For Android, see [Integrate Google Cloud Fraud Defense with Android apps](https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps).
     * For iOS, see [Integrate Google Cloud Fraud Defense with iOS apps](https://docs.cloud.google.com/recaptcha/docs/instrument-ios-apps).
  3. After you receive the token, attach the token to a predefined request header in the following format:
         
         X-Recaptcha-Token: value-of-your-action-token
         

The following sample code shows how to attach the token:

### Android

Sample code in Java
         
         // This example shows how to send an HTTP request to the backend server
         // attached with the reCAPTCHA token in the header.
         //
         // @param serverUrl: the URL of the backend server.
         // @param rceToken: reCAPTCHA token that is attached to the header of the
         // HTTP request.
         
         public static void sendRequestToServerWithRceToken(
             String serverUrl, String rceToken) throws JSONException, IOException {
          URL url = new URL(String.format("http://%s/decryptcaptchacookie/accesswafserver", serverUrl));
          HttpURLConnection connection = (HttpURLConnection) url.openConnection();
          connection.setRequestProperty("X-Recaptcha-Token", rceToken);
         
          try {
             String requestBody = "['']";
             sendRequest(connection, requestBody, "AccessWithRceToken", "GET");
          } finally {
             connection.disconnect();
          }
         }
         
         private static void sendRequest(
             HttpURLConnection connection, String requestString, String requestName, String action)
             throws IOException {
          connection.setConnectTimeout(HTTP_CONNECT_TIMEOUT_MS);
          connection.setReadTimeout(HTTP_READ_TIMEOUT_MS);
          connection.setRequestProperty("Content-type", CONTENT_TYPE);
          connection.setRequestProperty(
             "Content-Length", Integer.toString(Utf8.encodedLength(requestString)));
          connection.setRequestMethod(action);
          connection.setDoOutput(true);
          connection.connect();
          try (OutputStream postStream = connection.getOutputStream()) {
             postStream.write(requestString.getBytes(UTF_8));
          }
         
          int responseCode = connection.getResponseCode();
          String response = connection.getResponseMessage();
          if (responseCode != HttpURLConnection.HTTP_OK) {
             throw new IOException(
                String.format(
                   "Failed to complete request.\nResponse code:%s\nError Detail:\n%s",
                   responseCode, response));
          }
         }

### iOS

Sample code in Swift
         
         // This example shows how to send an HTTP request to the backend server
         // attached with the reCAPTCHA token in the header.
         // @param serverUrl: the URL of the backend server.
         // @param rceToken: reCAPTCHA token that is attached to the header of
         // the HTTP request.
         
          public static func accessWafServer(rceToken: String, serverUrl: String)
             async throws -> String
          {
             let requestURL = try HttpHelper.createRequestURL(endpoint: serverUrl)
             var request = try HttpHelper.createRequest(requestURL: requestURL, action: "GET")
             request.setValue(rceToken, forHTTPHeaderField: "X-Recaptcha-Token")
         
             let data = try await HttpHelper.getDataFromServer(request)
         
             return String(decoding: data, as: UTF8.self)
          }




## Configure Cloud Armor security policies

After implementing the features of Fraud Defense for WAF, you must configure Cloud Armor security policies that evaluate reCAPTCHA tokens for bot management.

To learn how to configure Cloud Armor security policies and use the action-token keys with your security policies, see [Configure rules for bot management](https://docs.cloud.google.com/armor/docs/configure-bot-management).

## Get reCAPTCHA scores

For reCAPTCHA action-tokens, you can get reCAPTCHA scores from the `X-Recaptcha-Wafdata` header. Based on these scores, you can configure any custom action that needs to be taken for user requests.

The following example shows a sample `X-Recaptcha-Wafdata` header:
    
    
    X-Recaptcha-Wafdata: waf_service="Google Cloud Armor", action_token;score=0.9\r\n
    

You can also view reCAPTCHA scores in the [Google Cloud Armor logs](https://docs.cloud.google.com/armor/docs/request-logging#requests).

## What's next

  * [Configure rules for bot management](https://docs.cloud.google.com/armor/docs/configure-bot-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
