---
url: https://docs.cloud.google.com/recaptcha/docs/sms-fraud-detection/
title: Detect and prevent SMS fraud \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:20.292799+00:00
---

# Detect and prevent SMS fraud  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/sms-fraud-detection/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Detect and prevent SMS fraud Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use SMS defense to detect and prevent SMS pumping attacks in businesses that rely on SMS for two-factor authentication (2FA) or phone verification, which is a potential target for SMS toll fraud.

SMS-based authentication (2FA and login) is an industry standard for login and signup security, but it doesn't provide protection against SMS toll fraud or SMS pumping fraud. Before you send an SMS, SMS defense provides you with a risk score that indicates the likelihood of that phone number committing SMS toll fraud. Based on this score, you can allow or block fraudulent SMS messages before they are sent to your SMS provider.

The SMS defense risk score works inversely in comparison to the reCAPTCHA global score. A SMS defense risk score of 0.0 shows low confidence of SMS toll fraud occurring; a risk score of 1.0 shows high confidence of SMS toll fraud occurring. For more information about reCAPTCHA scores, see [Interpret assessments for websites](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website#interpret_scores). If you're using Firebase Authentication or Identity Platform, see the [Identity Platform documentation](https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp).

For additional information, see the [SMS defense blog](https://www.googlecloudcommunity.com/gc/Community-Blog/Introducing-reCAPTCHA-SMS-toll-fraud-protection-now-in-public/ba-p/768724).

## Before you begin

Depending on whether you are an existing user of reCAPTCHA or new to reCAPTCHA, follow the instructions in the appropriate tab:

### Existing reCAPTCHA user

If you are an existing user of reCAPTCHA, then enable SMS defense on your Google Cloud project:

  1. In the Google Cloud console, go to the reCAPTCHA page.

[Go to reCAPTCHA](https://console.cloud.google.com/security/recaptcha)

  2. Verify that the name of your project appears in the resource selector.

If you don't see the name of your project, click the resource selector, and then select your project.

  3. Click **settings Settings**.

  4. In the **SMS defense** pane, click **Configure**.

  5. Click the **Enable** toggle, and click **Save**.

It might take a few minutes for the SMS defense enablement to propagate to our systems. After the feature enablement is propagated to our systems, you should start receiving responses related to SMS defense as part of the assessments.




### New reCAPTCHA user

If you are new to reCAPTCHA, do the following:

  1. Depending on whether you want to use SMS defense on a website or mobile application, follow these steps to integrate reCAPTCHA:

### Website

     1. [Create a score-based key for your website](https://docs.cloud.google.com/recaptcha/docs/create-key-website).
     2. [Install the score-based key on web pages](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages).

### Mobile application

     1. [Create a score-based key for your mobile application](https://docs.cloud.google.com/recaptcha/docs/create-key-mobile).
     2. Integrate reCAPTCHA with an [iOS app](https://docs.cloud.google.com/recaptcha/docs/instrument-ios-apps) or an [Android app](https://docs.cloud.google.com/recaptcha/docs/instrument-android-apps)

  2. Enable SMS defense on your Google Cloud project: 
     1. In the Google Cloud console, go to the reCAPTCHA page.

[Go to reCAPTCHA](https://console.cloud.google.com/security/recaptcha)

     2. Verify that the name of your project appears in the resource selector.

If you don't see the name of your project, click the resource selector, and then select your project.

     3. Click **settings Settings**.

     4. In the **SMS defense** pane, click **Configure**.

     5. Click the **Enable** toggle, and click **Save**.

It might take a few minutes for the SMS defense enablement to propagate to our systems. After the feature enablement is propagated to our systems, you should start receiving responses related to SMS defense as part of the assessments.




## Create an assessment with the phone number

For SMS defense, create assessments with the token that is generated by the `execute()` function and the phone number, by using either the reCAPTCHA Client Libraries or the REST API from your backend.

This document shows how to create an assessment using the REST API. To learn how to create an assessment using Client Libraries, see [Create assessments](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website#create-assessment-request).

Before you create an assessment, do the following:

  * Set up authentication to Fraud Defense. 

The authentication method you choose depends on the environment where Fraud Defense is set up. The following table helps you choose the appropriate authentication method and the supported interface to set up authentication:

Environment | Interface | Authentication method  
---|---|---  
Google Cloud | 
    * REST
    * Client libraries
| Use [attached service accounts](https://docs.cloud.google.com/recaptcha/docs/authentication#on-gcp).  
On-premises or a different cloud provider | REST | Use [API keys](https://docs.cloud.google.com/docs/authentication/api-keys) or [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises). If you want to use API keys, then we recommend securing the API keys by [applying API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).  
Client libraries | Use the following:
    * For Python or Java, use [API keys](https://docs.cloud.google.com/docs/authentication/api-keys) or [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises). If you want to use API keys, then we recommend securing the API keys by [applying API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).
    * For other languages, use [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises).  
  * Choose a stable account identifier `accountId` that is not often changed by the user and provide it to the assessment in the [ `projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method. This stable account identifier should have the same value for all the events related to the same user. You can provide the following as the account identifier:

### User identifiers

If every account can be uniquely associated with a stable username, email address, or phone number, you can use it as the `accountId`. When you provide such cross-site identifiers (identifiers that can be reused across sites), Fraud Defense uses this information to improve protection for your user accounts based on cross-site models by flagging abusive account identifiers and using knowledge of cross-site abuse patterns related to these identifiers.

Alternatively, if you have an internal user ID uniquely associated with each account, you can provide it as the `accountId`.

### Hashed or encrypted

If you do not have an internal user ID uniquely associated with each account, you can turn any stable identifier into an opaque, site-specific account identifier. This identifier is still needed for Fraud Defense account defender to understand user activity patterns and detect anomalous behaviour, but it is not shared across other sites.

Pick any stable account identifier and make it opaque before sending to Fraud Defense by using encryption or hashing:

    * encryption (recommended): encrypt the account identifier using a deterministic encryption method that produces a stable ciphertext. For detailed instructions, see [encrypt data deterministically](https://developers.google.com/tink/deterministic-encryption). When you choose symmetric encryption over hashing, you don't need to keep a mapping between your user identifiers and the corresponding opaque user identifiers. Decrypt the opaque identifiers that are returned by Fraud Defense to turn them into the user identifier.

    * hashing: we recommend hashing the account identifier using the SHA256-HMAC method with a custom salt of your choice. Because hashes are one-way only, you need to keep a mapping between the generated hashes and your user identifiers so that you can map the hashed account identifier that are returned back to the original accounts.




Add the `accountId` parameter and the phone number in the E.164 format as the `UserId` to verify in the assessment in the [`projects.assessments.create`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/create) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID.
  * TOKEN: token returned from the `grecaptcha.enterprise.execute()` call.
  * KEY_ID: the score-based key that you installed on your website.
  * ACCOUNT_ID: an identifier for a user account that is unique to your website.
  * PHONE_NUMBER: the phone number that needs to be checked for maliciousness. The phone number must be in the E.164 format and it should not be hashed or encrypted.



HTTP method and URL: 
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments

Request JSON body: 
    
    
    
    {
      "event": {
        "token": "TOKEN",
        "siteKey": "KEY_ID",
        "userInfo": {
          "accountId": "ACCOUNT_ID",
          "userIds": [
            {
              "phoneNumber": "PHONE_NUMBER"
            }
          ]
        }
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
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments"

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
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "event": {
         …
      },
      "name": "ASSESSMENT_ID",
      "phoneFraudAssessment": {
        "smsTollFraudVerdict": {
          "risk": 0.3
        }
      }
    }
    

The response you receive includes the `risk` score in the [`phoneFraudAssessment.smsTollFraudVerdict`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#smstollfraudverdict) field . The higher the score, the more likely the phone number is risky; the lower the score, the more likely the phone number is legitimate.

You are responsible for the actions that you take based on the assessment. For the simplest integration, you can set thresholds on `phoneFraudAssessment.smsTollFraudVerdict.risk` to contribute to your decision.

## Annotate the assessment

To keep track of the SMS traffic and to improve the fraud detection, you must annotate the assessments within 10 minutes after the SMS is sent or after the phone number is successfully verified.

You annotate an assessment by sending a request to the [`projects.assessments.annotate`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate) method with the assessment ID. In the body of that request, include the phone number in E.164 format in the `phoneAuthenticationEvent` field.

To annotate an assessment, do the following:

  1. Determine the information and labels to add in the request JSON body depending on your use case.

The following table lists the labels and values that you can use to annotate events:

Label | Description | Request example  
---|---|---  
`reasons` | Required. A label to support your assessments. Provide real-time event details in the `reasons` label in a few seconds or minutes after the event because they influence real-time detection. Possible values:
     * `INITIATED_TWO_FACTOR`: a verification code through SMS is sent.
     * `PASSED_TWO_FACTOR`: the verification code is successfully verified.
     * `FAILED_TWO_FACTOR`: the verification code is invalid.
| 
    
    {
          "reasons": ["INITIATED_TWO_FACTOR"],
          "phoneAuthenticationEvent": {
            "phoneNumber": "+18005550175"
          }
        }
          
  
`annotation` | Optional. A label to indicate the legitimacy of assessments. Provide facts about login and registration events to validate or correct your risk assessments in the `annotation` label. Possible values: `LEGITIMATE` or `FRAUDULENT`. We recommend sending this information in a few seconds or minutes after the event because it influences real-time detection. | 
    
    {
       "annotation": "LEGITIMATE"
      }
        
  
  2. Create an annotate request with the appropriate labels. 

Before using any of the request data, make the following replacements: 

     * ASSESSMENT_ID: value of the `name` field returned from the `projects.assessments.create` call.
     * ANNOTATION: Optional. A label to indicate whether the assessment is legitimate or fraudulent.
     * REASONS: reasons that support your annotation. For the list of possible values, see [reasons values](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate#reason).
     * PHONE_NUMBER: the phone number that was assessed. The phone number must be in the E.164 format and it should not be hashed or encrypted.

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/ASSESSMENT_ID:annotate

Request JSON body: 
    
    {
      "annotation": ANNOTATION,
      "reasons": REASONS,
      "phoneAuthenticationEvent": {
        "phoneNumber": "PHONE_NUMBER"
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
         "https://recaptchaenterprise.googleapis.com/v1/ASSESSMENT_ID:annotate"

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
        -Uri "https://recaptchaenterprise.googleapis.com/v1/ASSESSMENT_ID:annotate" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




## What's next

  * Learn about the [user accounts protection features of reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/protect-accounts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
