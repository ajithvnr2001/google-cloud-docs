---
url: https://docs.cloud.google.com/recaptcha/docs/express-standalone/
title: Set up reCAPTCHA express on application servers \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:58.649042+00:00
---

# Set up reCAPTCHA express on application servers  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/express-standalone/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Set up reCAPTCHA express on application servers Stay organized with collections  Save and categorize content based on your preferences. 

reCAPTCHA express can be set up on an application server when a client-side integration with the reCAPTCHA JavaScript or mobile SDK is not feasible, for example, for protection of API endpoints.

reCAPTCHA express is a feature that lets you create assessments without a client-side integration or client-side signals. reCAPTCHA express uses only backend signals to generate a reCAPTCHA risk score. You can use this risk score to decide whether to serve the request, redirect to a challenge page, or log it for later analysis.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

Record your Google Cloud project ID for later use.
  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the reCAPTCHA Enterprise API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recaptchaenterprise.googleapis.com)

  4. Create an API key for authentication:

     1. In the Google Cloud console, go to the **Credentials** page.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

     2. Click add **Create credentials** , and then select **API key**.

     3. Record the API key for later use.




## Create a reCAPTCHA express key

To implement reCAPTCHA express, create a reCAPTCHA express key.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. ### gcloud

To create reCAPTCHA keys, use the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command.

Before using any of the command data below, make the following replacements: 

     * INTEGRATION_TYPE: Type of integration. Specify `score`. 
     * DISPLAY_NAME: Name for the key. Typically a site name. 

Execute the [gcloud recaptcha keys create](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/create) command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud recaptcha keys create \
    --express \
    --display-name=DISPLAY_NAME

#### Windows (PowerShell)
    
    gcloud recaptcha keys create `
    --express `
    --display-name=DISPLAY_NAME

#### Windows (cmd.exe)
    
    gcloud recaptcha keys create ^
    --express ^
    --display-name=DISPLAY_NAME

The response contains the newly created reCAPTCHA key. 

### REST

For API reference information about key types and integration types, see [Key](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#resource:-key) and [Integration type](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.keys#integrationtype). 

Before using any of the request data, make the following replacements: 

     * INTEGRATION_TYPE: Type of integration. Specify `score`. 
     * DISPLAY_NAME: Name for the key. Typically a site name. 
     * DEFAULT_SCORE_THRESHOLD: For policy-based challenge keys, this defines the universal challenge threshold for the key when a custom score threshold is not defined. This is in [preview](https://cloud.google.com/products#product-launch-stages).
     * ACTION_SCORE_THRESHOLDS: For policy-based challenge keys, this specifies the action and the corresponding threshold score between 0.0 and 1.0. For example, `login='{"scoreThreshold": "0.3"}',signup='{"scoreThreshold": "0.1"}'`. This is in [preview](https://cloud.google.com/products#product-launch-stages). **Note:** Only the final scores that are computed after any challenges are returned in assessments. The initial score computed by reCAPTCHA is compared with the threshold. 

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/keys

Request JSON body: 
    
    {
      "displayName": "DISPLAY_NAME",
      "expressSettings": {}
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
      "name": "projects/project-id/keys/7Ldqgs0UBBBBBIn4k7YxEB-LwEh5S9-Gv6QQIWB8m",
    "displayName": "DISPLAY_NAME,
    "expressSettings": {
    }
    }
    
    




Record your express key for later use.

## Create an assessment

To make a request from your application server to reCAPTCHA, create an assessment using the [`projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method.

Before using any of the request data, make the following replacements: 

  * API_KEY: The API key that you created for the authentication.
  * EXPRESS_KEY: reCAPTCHA express key that you created for your application.
  * USER_IP_ADDRESS: The IP address in the request from the user's device related to this event.
  * HEADER_INFO: Optional. The HTTP headers that the client sent to your application server. It is a string array that contains request headers in the `[key:value]` format. For example, `[key:value, key:value,...]`. We recommend that you share as many headers as possible in the required order. Ensure that the order of the headers is consistent across all requests in the same session. 
  * JA4_FINGERPRINT: Optional. JA4 is a fingerprint of certain fields of the TLS Client Hello packet. For more information, see [JA4+™ Network Fingerprinting](https://github.com/FoxIO-LLC/ja4).
  * URI_NAME: Optional. The URI that is being accessed by the user.
  * USER_AGENT: Optional. The user agent that is present in the request from the user's device related to this event.
  * ACCOUNT_ID: Optional. A unique and persistent identifier for the user's account, such as a hashed account name.



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments?key=API_KEY

Request JSON body: 
    
    
    
    {
      "event": {
        "siteKey": "EXPRESS_KEY",
        "express": true,
        "userIpAddress": "USER_IP_ADDRESS",
        "headers": ["HEADER_INFO"],
        "ja4": "JA4_FINGERPRINT",
        "requestedUri": "URI_NAME",
        "userAgent": "USER_AGENT",
        "user_info": {
          "account_id": "ACCOUNT_ID"
        }
      }
    }
    
    

To send your request, choose one of these options:

#### curl

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments?key=API_KEY"

#### PowerShell

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments?key=API_KEY" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/123456789/assessments/abcdef1234000000",
      "event": {
        "token": "",
        "siteKey": "6L...",
        "userAgent": "Mozilla/5.0 (X11; CrOS x86_64 13816.55.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.86 Safari/537.36",
        "userIpAddress": "1.2.3.4",
        "express": true,
        "requestedUri": "https://example.com/",
        "user_info": {
          "account_id": "123456789"
        },
        "headers": [ "Origin: https://example.com", "Referer: https://example.com.login"],
      },
      "riskAnalysis": {
        "score": 0.7,
        "reasons": []
      }
    }
    

## Interpret scores

reCAPTCHA express returns only two scores: `0.3` and `0.7`. `0.3` indicates that the user interaction poses more risk and is likely fraudulent, and `0.7` indicates that the user interaction poses low risk and is likely legitimate.

If there are lack of signals, then reCAPTCHA express returns `0.7` by default.

## What's next

  * [Learn about how to interpret risk scores](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment).
  * [Learn about how to use reCAPTCHA express at the WAF layer](https://docs.cloud.google.com/recaptcha/docs/features-ca).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
