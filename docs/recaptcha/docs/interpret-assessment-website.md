---
url: https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website/
title: Interpret assessments for websites \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:55.217011+00:00
---

# Interpret assessments for websites  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Interpret assessments for websites Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to interpret a score to understand the level of risk that user interactions pose, and take appropriate actions for your site.

reCAPTCHA returns a score for each request based on the interactions with your site, regardless of the key type. After you receive the score from reCAPTCHA, you must interpret the score and take appropriate actions for your site.

## Before you begin

[Create an assessment for your website](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).

## Interpret the assessment

After your backend submits a user's reCAPTCHA response token to reCAPTCHA, you receive an assessment as a JSON response as shown in the following example.

**Note:** We recommend using any JSON parsers in the non-strict parsing mode to prevent outages in case of any additional fields being introduced to the JSON response. [reCAPTCHA Client Libraries](https://docs.cloud.google.com/recaptcha/docs/libraries) handle additional fields for you.

To interpret an assessment, consider the following parameters:

  * `valid`: indicates whether the provided user response token is valid. When `valid = false`, the reason is specified in `invalidReason`. `valid = false` can also indicate that a user has failed to solve a challenge or there is a `siteKey` mismatch.
  * `invalidReason`: the reason associated with the response when `valid = false`.
  * `action`: a user interaction that triggered reCAPTCHA verification.
  * `expectedAction`: the expected action from a user that you specified when creating the assessment.
  * `score`: the level of risk that the user interaction poses. A higher score indicates lower risk.
  * `reasons`: additional information about how reCAPTCHA has interpreted the user interaction.
  * `challenge`: indicates the response to the challenge for policy-based challenge keys. Possible values: `PASS`, `FAIL`, or `NOCAPTCHA`.
  * `extended_verdict_reasons`: advanced reasons contributing to the risk analysis verdict.

Reason codes are available after triggering an automatic security review by adding a billing account to your project. To request access to reason codes, [add a billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account) to your project.

Assessments from projects with an Enterprise subscription also receive Advanced reason codes. Contact your account representative or [Google Cloud sales](https://cloud.google.com/contact) for the full list of Advanced reasons and how to interpret them.
        
        {
         "event":{
           **** "expectedAction":"EXPECTED_ACTION",
            "hashedAccountId":"ACCOUNT_ID",
            "siteKey":"KEY_ID",
            "token":"TOKEN",
            "userAgent":"(USER-PROVIDED STRING)",
            "userIpAddress":"USER_PROVIDED_IP_ADDRESS"
         },
         "name":"ASSESSMENT_ID",
         **"riskAnalysis" :{
           "reasons":[],
           "extended_verdict_reasons":[],
           "score":"SCORE",
           "challenge":"PASS"
         },
         **"tokenProperties":{
           **"action" :"USER_INTERACTION"**,
           "createTime":"TIMESTAMP",
           "hostname":"HOSTNAME",
           **"invalidReason" :"(ENUM)"**,
           **"valid" :(BOOLEAN)**
         }
        }




### Verify actions

The JSON response contains the `action` parameter that you specified for a user interaction when calling `execute()` and the `expectedAction` parameter that you specified when creating the assessment.

Verify that `action` matches the `expectedAction`. For example, a `login` action should be returned on your **login** page. If there is a mismatch, it indicates that an attacker is attempting to falsify actions. You can take actions against the user interaction, such as adding additional verifications or blocking the interaction to prevent any fraudulent activities.

### Interpret scores

The scoring system of reCAPTCHA is an expansion from prior versions of reCAPTCHA to allow greater granularity in responses. reCAPTCHA has 11 levels for scores with values ranging from 0.0 to 1.0. The score 1.0 indicates that the interaction poses low risk and is very likely legitimate, whereas 0.0 indicates that the interaction poses high risk and might be fraudulent.

Out of the 11 levels, only the following four score levels are available before triggering an automatic security review by adding a billing account to your project: 0.1, 0.3, 0.7, and 0.9.

To request access to 11 score levels, [add a billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account) to your project.

The SMS defense risk score works inversely in comparison to the reCAPTCHA global score. A SMS defense risk score of 0.0 shows low confidence of SMS toll fraud occurring; a risk score of 1.0 shows high confidence of SMS toll fraud occurring.

reCAPTCHA learns by monitoring real traffic on your site. Therefore, scores in a staging environment and within 7 days of implementation might differ from the long-term production scores.

If you installed score-based keys, you can first run reCAPTCHA without taking action and then decide on thresholds by looking at the traffic.

Based on the score, you can take an appropriate action in the context of your site. To protect your site better, we recommend that you take the action in the background instead of blocking traffic.

The following table lists some of the actions you might take:

Use case |  Action  
---|---  
homepage | See a cohesive view of your traffic on the admin console while filtering scrapers.  
login | With low scores, require MFA or email verification to prevent credential stuffing attacks.  
social | Limit unanswered friend requests from abusive users and send risky comments to moderation.  
e-commerce | Put your real sales ahead of bots and identify risky transactions.  
  
### Reason codes

Reason codes are available after triggering an automatic security review by adding a billing account to your project. To request access to reason codes, [add a billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account) to your project.

Some scores might be returned with reason codes that provide additional information about how reCAPTCHA interpreted the interactions.

The following table lists the reason codes and their descriptions:

Reason code | Description  
---|---  
AUTOMATION | The interaction matches the behavior of an automated agent.  
UNEXPECTED_ENVIRONMENT | The event originated from an illegitimate environment.  
TOO_MUCH_TRAFFIC | Traffic volume from the event source is higher than normal.  
UNEXPECTED_USAGE_PATTERNS | The interaction with your site was significantly different from expected patterns.  
LOW_CONFIDENCE_SCORE | Too little traffic was received from this site to generate quality risk analysis.  
  
### Response of the `siteverify` method

For request, response, and error code details for the `siteverify` method, see [Verify user response tokens with legacy SiteVerify](https://docs.cloud.google.com/recaptcha/docs/verify).

## What's next

  * To tune your site-specific model, you can send the assessment IDs back to Google to confirm true positives and true negatives, or correct errors. For details, see [Annotate assessments](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
