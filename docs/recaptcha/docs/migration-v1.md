---
url: https://docs.cloud.google.com/recaptcha/docs/migration-v1/
title: Migrate to the v1 API \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:17.650908+00:00
---

# Migrate to the v1 API  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/migration-v1/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Migrate to the v1 API Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to migrate from the `v1beta1` version to the `v1` version of the reCAPTCHA Enterprise API.

> **Caution:** The `v1beta1` endpoint was deprecated on August 31, 2025. To avoid service > disruption, migrate to the `v1` version of the reCAPTCHA Enterprise API as soon as possible.
> 
> Starting June 2026, the `v1beta1` endpoint will be progressively shut down. > During this phased shutdown, requests made to the `v1beta1` endpoint from unmigrated services will begin to return errors.

To migrate your assessment calls from `v1beta1` to `v1`, do the following:

  1. Replace calls to create assessments.

Replace `https://recaptchaenterprise.googleapis.com/v1beta1/projects/PROJECT_ID/assessments?key=API_KEY` with `https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments?key=API_KEY`

**Note:** You can use the same API key.
  2. Understand the changes in the assessment's JSON response:

When you use `v1`, the `reasons` and `score` fields are encapsulated in `riskAnalysis` in the response, and when you use `v1beta1`, the`reasons` and `score` fields are not encapsulated in the response.

### v1
         
         {
         "event":{
           "expectedAction":"EXPECTED_ACTION",
           "hashedAccountId":"ACCOUNT_ID",
           "siteKey":"KEY_ID",
           "token":"TOKEN",
           "userAgent":"(USER-PROVIDED STRING)",
           "userIpAddress":"USER_PROVIDED_IP_ADDRESS"
         },
         "name":"ASSESSMENT_ID",
         ** "riskAnalysis":{
           "reasons":[],
           "score":"SCORE
         },**
         "tokenProperties":{
           "action":"USER_INTERACTION",
           "createTime":"TIMESTAMP",
           "hostname":"HOSTNAME",
           "invalidReason":"(ENUM)",
           "valid":(BOOLEAN)
         }
         }

### v1beta1
         
         {
         "event":{
           "expectedAction":"EXPECTED_ACTION",
           "hashedAccountId":"ACCOUNT_ID",
           "siteKey":"KEY_ID",
           "token":"TOKEN",
           "userAgent":"(USER-PROVIDED STRING)",
           "userIpAddress":"USER_PROVIDED_IP_ADDRESS"
         },
         "name":"ASSESSMENT_ID",
         **"reasons" :[],
         "score":"SCORE",
         **
         "tokenProperties":{
           "action":"USER_INTERACTION",
           "createTime":"TIMESTAMP",
           "hostname":"HOSTNAME",
           "invalidReason":"(ENUM)",
           "valid":(BOOLEAN)
         }
         }

  3. Update your environment to use the `reasons` and `score` fields from the JSON response for `v1`.

The following sample code shows the fields that are used from the response of `v1` and `v1beta1`:

### v1
         
         .....
         .....
         # Get the risk score and the reason(s)
         for reason in response.risk_analysis.reasons:
             print(reason)
         print(
             "The reCAPTCHA score for this token is: "
             + str(response.risk_analysis.score)
         )
         ....
         ....

### v1beta1
         
         .....
         .....
         # Get the risk score and the reason(s)
         for reason in response.reasons:
             print(reason)
         print(
             "The reCAPTCHA score for this token is: "
             + str(response.score)
         )
         ....
         ....

  4. Replace calls to annotate assessments.

Replace `https://recaptchaenterprise.googleapis.com/v1beta1/projects/PROJECT_ID/assessments}:annotate` with `https://recaptchaenterprise.googleapis.com/v1/projects/PROJECT_ID/assessments}:annotate`

  5. If you are currently logging your `create` and `annotate` API calls using [audit logging](https://docs.cloud.google.com/recaptcha/docs/audit-logging) it is recommended to use [platform logging](https://docs.cloud.google.com/recaptcha/docs/platform-logging) (available for `v1` only).




## What's next

  * [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment)
  * [Annotate an assessment](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
