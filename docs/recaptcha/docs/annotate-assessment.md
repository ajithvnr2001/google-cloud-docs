---
url: https://docs.cloud.google.com/recaptcha/docs/annotate-assessment/
title: Annotate assessments \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:01.019174+00:00
---

# Annotate assessments  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/annotate-assessment/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Annotate assessments Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can provide feedback on the accuracy of the assessments created by Google Cloud Fraud Defense. With this information, Fraud Defense can tune your site-specific model and provide improved performance for your site over time.

## When to annotate assessments

Fraud Defense provides a score when creating an assessment that helps you understand the level of risk user interactions pose. Later, when your site has more information about user interactions to determine if the interaction was legitimate or fraudulent, you can confirm or correct reCAPTCHA's assessment. To do this, you send the reCAPTCHA assessment IDs back to Google labeled as `LEGITIMATE` or `FRAUDULENT`. Confirming or correcting reCAPTCHA's assessment improves the performance of Fraud Defense for your site.

To improve the performance of Fraud Defense, you can confirm the annotations for **true positives** and **true negatives** in addition to the annotations for potential assessment errors. For example, for a user who successfully authenticated using a 2-factor-authentication method and received a high reCAPTCHA score, you can annotate the assessment as `LEGITIMATE`. Alternatively, if the Google Cloud Fraud Defense score was low and your site determined that the interaction was fraudulent or abusive, you can annotate the assessment as `FRAUDULENT`.

The following list shows additional information about some sample user interactions that indicate whether a user interaction is legitimate or fraudulent:

  * Credit card chargebacks or other concrete evidence of fraud indicate that an earlier financial transaction was fraudulent.
  * A new account that sends messages that are flagged as spam by other users might indicate that the account creation was fraudulent.
  * A support case filed if a user has difficulty logging in to their account might indicate that the login attempt is legitimate.
  * A purchase or booking on a site that uses Fraud Defense to defend against scraping might indicate that the user is legitimate.



## Before you begin

  * Ensure that you have the following Identity and Access Management role: [reCAPTCHA Enterprise Agent (`roles/recaptchaenterprise.agent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.agent).

  * Depending on where you have set up Fraud Defense, complete the appropriate step:

    * [Create an assessment for your website](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).
    * [Create an assessment for your mobile application](https://docs.cloud.google.com/recaptcha/docs/create-assessment-mobile).
    * [Set up your WAF integration](https://docs.cloud.google.com/recaptcha/docs/setup-overview-ca).



## Retrieve the assessment ID

To annotate an assessment, retrieve the unique assessment ID in the following ways:

  * For web and mobile integrations, you can retrieve the unique assessment ID from the assessment response.

After you create an assessment, you receive a JSON response as shown in the following example.

Retrieve the unique assessment ID from the `name` field in the JSON response.
        
        {
        'tokenProperties': {
          'valid': True,
          'hostname': 'www.google.com',
          'action': 'homepage',
          'createTime': u'2019-03-28T12:24:17.894Z'
        },
        'riskAnalysis': {
          'score': 0.1,
          'reasons': ['AUTOMATION']
        },
        'event': {
          'token': 'RESPONSE_TOKEN',
          'siteKey': 'KEY_ID'
        },
        **'name' : 'ASSESSMENT_ID'**
        }

  * For WAF integrations, you can retrieve the unique assessment ID from the reCAPTCHA token. The unique assessment ID is the unique alphanumeric string of 16 characters that appears at the end of the reCAPTCHA token after `:U=`. For example, if the reCAPTCHA token is `.................U=6ZZZZe73fZZZZZZ0`, then the assessment ID is `6ZZZZe73fZZZZZZ0`.




## Annotate an assessment

  1. Determine the information and labels to add in the request JSON body depending on your use case.

The following table lists the labels and values that you can use to annotate events:

Label | Description | Request example  
---|---|---  
`reasons` | Optional. A label to support your assessments. Provide real-time event details in the `reasons` label in a few seconds or minutes after the event because they influence real-time detection. For the list of possible values, see [reasons values](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate#reason). Example: To detect account takeovers, annotate if the entered password was correct with `CORRECT_PASSWORD` or `INCORRECT_PASSWORD` values. If you deployed your own MFA, you can add the following values: `INITIATED_TWO_FACTOR`, and `PASSED_TWO_FACTOR` or `FAILED_TWO_FACTOR`.  | 
         
         {
               "reasons": ["INCORRECT_PASSWORD"]
               }
               
  
`annotation` | Optional. A label to indicate the legitimacy of assessments. Provide facts about login and registration events to validate or correct your risk assessments in the `annotation` label. Possible values: `LEGITIMATE` or `FRAUDULENT`. You can send this information at any time or as part of a batch job. However, we recommend sending this information in a few seconds or minutes after the event because they influence real-time detection. | 
         
         {
                "annotation": "LEGITIMATE"
               }
         
             
  
  2. Annotate an assessment using the [`projects.assessments.annotate`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate) method with the gcloud CLI or an API key.

**Note:** If you're using the `v1beta1` version of the API, we recommend using the `v1` version because new features like Account defense are available only on the `v1` version. For migrating from `v1beta1` to `v1`, see [Migrate from v1beta API to v1 API ](https://docs.cloud.google.com/recaptcha/docs/migration-v1).

###  gcloud CLI 

Before using any of the request data, make the following replacements: 

     * ASSESSMENT_ID: Value of the `name` field returned from the `projects.assessments.create` call.
     * ANNOTATION_LABEL: The label to indicate whether the assessment is legitimate or fraudulent. Possible values are `LEGITIMATE` or `FRAUDULENT`.
     * ANNOTATION_REASON: Describes the context for the annotation that was chosen for this assessment. To learn about possible values, see [reasons for annotating an assessment](https://cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate#reason).

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/ASSESSMENT_ID:annotate

Request JSON body: 
    
    {
    "annotation": "ANNOTATION_LABEL"
    "reasons": "ANNOTATION_REASON"
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

###  API key 

Before using any of the request data, make the following replacements: 

     * ASSESSMENT_ID: Value of the `name` field returned from the `projects.assessments.create` call
     * ANNOTATION_LABEL: The label to indicate whether the assessment is legitimate or fraudulent. Possible values are `LEGITIMATE` or `FRAUDULENT`.
     * ANNOTATION_REASON: Describes the context for the annotation that was chosen for this assessment. To learn about possible values, see [reasons for annotating an assessment](https://cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments/annotate#reason).

HTTP method and URL: 
    
    POST https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments/ASSESSMENT_ID:annotate?key=API_KEY

Request JSON body: 
    
    {
    "annotation": "ANNOTATION_LABEL"
    "reasons": "ANNOTATION_REASON"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** Create an [API key](https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key) to authenticate with the API.

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments/ASSESSMENT_ID:annotate?key=API_KEY"

#### PowerShell

**Note:** Create an [API key](https://cloud.google.com/docs/authentication/api-keys#creating_an_api_key) to authenticate with the API.

Save the request body in a file named `request.json`, and execute the following command: 
    
    $headers = @{  }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments/ASSESSMENT_ID:annotate?key=API_KEY" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




## What's next

  * Learn about the [user accounts protection features of Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/protect-accounts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
