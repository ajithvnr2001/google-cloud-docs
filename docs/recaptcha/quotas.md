---
url: https://docs.cloud.google.com/recaptcha/quotas/
title: Quotas and limits \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:08.812971+00:00
---

# Quotas and limits  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/quotas/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Resources ](https://docs.cloud.google.com/recaptcha/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists content limits and rate quotas for Google Cloud Fraud Defense.

## Rate quotas

The following table lists the API usage quotas for Fraud Defense:

Quota | Value  
---|---  
Requests per calendar month per organization (if billing is not enabled) | 10,000  
Requests per minute | 60,000  
MFA Requests using email per email address per day | 10  
MFA Requests using SMS per phone number per day | 10  
MFA Requests using SMS per phone number per 4 hours | 5  
MFA Requests (email/SMS) per day | 10,000  
**Note:** The free 10,000 assessments are per organization. The limit aggregates use across all accounts and all sites. All rate limits (such as requests per minute) apply separately for each Google Cloud project.

## Quota limit errors

When your API usage exceeds the specified quota limits, any new request returns an HTTP error with a `Resource Exhausted (429)` status code.

For V2, an end-user-visible error message is shown similar to the following message: `This site is exceeding reCAPTCHA quota`.

## What to do if you expect to go over the quotas

To use Fraud Defense above the monthly free quota of 10,000 assessments per organization, [enable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project) for your Google Cloud project. The monthly assessment quota is reset across your organization on the first day of each calendar month.

If you expect to exceed other quotas, reach out to your assigned Google Cloud sales representative. If you don't have an assigned Google Cloud sales representative, [contact Google Cloud sales](https://cloud.google.com/contact/).

For more information about quota errors and status codes, see [Troubleshoot quota errors](https://docs.cloud.google.com/docs/quotas/troubleshoot).

### Endpoint behavior when exceeding the monthly free quota

A Google Cloud project without an active billing account is subject to a free tier limit of 10,000 assessments per month across the organization. When this quota is exceeded across all accounts and all sites, the `CreateAssessment` and `SiteVerify` endpoints exhibit different behavior:

  * `CreateAssessment`: Requests that exceed the quota fail in a closed state. This means that the API returns an error, typically an `HTTP 429 (Too Many Requests)` status code or a `RESOURCE_EXHAUSTED` error. When this occurs, no assessment is created. To help prevent this, over-quota notifications and emails can alert you about a missing billing account.

  * `SiteVerify`: Requests that exceed the quota fail in an open state. The API returns an `HTTP 200 (OK)` status. The response body indicates `success:true` but contains a static score of 0.9 and an error message indicating that you exceeded the quota. This behavior is designed to prevent valid users from being blocked.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
