---
url: https://docs.cloud.google.com/identity-platform/quotas/
title: Quotas and limits \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:11:58.158035+00:00
---

# Quotas and limits  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Resources ](https://docs.cloud.google.com/identity-platform/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

The following auth operations have limitations on the frequency you can perform them. If you encounter a limit or have special use cases requiring higher thresholds, contact Google Cloud support at least two weeks in advance to discuss your quota adjustment needs.

**Note:** Limitations apply per customer and can change without notice. Abuse protections may be enabled without warning on accounts that demonstrate suspicious traffic patterns.

## Daily instrumentless usage limits

The following limits are daily usage limits for users of Identity Platform without a billing instrument, which is based on the no-cost [Spark pricing plan](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans#spark-pricing-plan). These usage limits correspond directly to [Google Cloud Pricing Tiers](https://cloud.google.com/identity-platform/pricing).

Usage | Instrumentless Limit  
---|---  
Tier 1 Daily Active Users | 3000 per day  
Tier 2 Daily Active Users | 2 per day  
  
## Account creation and deletion limits

Operation | Limit  
---|---  
New account creation | 100 accounts/hour for each IP address  
Account deletion | 10 accounts/second  
Batch account deletion | 1 request/second  
Account configuration updates | 10 requests/second  
  
## Account limits

Account type | Limit  
---|---  
Anonymous user accounts | 100 million  
Registered user accounts | Unlimited  
  
## Tenants per project

Billing model | Limit  
---|---  
Instrumentless | 2 tenants/project  
Billing instrument | Unlimited  
  
## Providers per project or tenant

There is no limit on the number of identity providers allowed per project or tenant.

## Email sending limits

The quotas listed in this section scale with the number of users.

Operation | Instrumentless | With billing instrument  
---|---|---  
Address verification emails | 1000 emails/day | 100,000 emails/day  
Address change emails | 1000 emails/day | 10,000 emails/day  
Password reset emails | 150 emails/day | 10,000 emails/day  
Email link sign-in emails | 5 emails/day | 25,000 emails/day  
**Note:** The limits for email link sign-in emails were recently changed. Please add a billing instrument to go beyond 5 email link sign-in emails.

## Email link generation limits

The quotas listed in this section scale with the number of users.

Operation | Instrumentless | With billing instrument  
---|---|---  
Address verification links | 10,000 links/day | 1,000,000 links/day  
Password reset links | 1500 links/day | 100,000 links/day  
Sign-in links | 20,000 links/day | 250,000 links/day  
  
## Phone number sign-in limits

Operation | Limit  
---|---  
User sign-ins | 1600/minute, as well as the pricing and limits specified on the [Pricing](https://docs.cloud.google.com/identity-platform/pricing) page   
Verification code SMS messages |  Instrumentless: 10 sent SMS/day Billing instrument: No SMS/day limit  
Verification requests | 150 requests/IP address/hour  
  
## Verification SMS sending limits

Operation | Limit  
---|---  
Verification SMS sent. |  1,000 sent/minute   
Verification SMS sent per IP address | 50 sent/minute, 500 sent/hour  
  
Additionally, there is a limit on the number of verification SMS messages a project can send to a single phone number within a set amount of time. You can test with [fictional numbers](https://firebase.google.com/docs/auth/android/phone-auth#test-with-fictional-phone-numbers) or across multiple devices to ensure a project does not exceed these limits.

Additionally, you can track verification codes sent per phone number if you've enabled [Activity Logging](https://cloud.google.com/identity-platform/docs/activity-logging) on your project.

## SMS MFA limits

Operation | Limit  
---|---  
Start MFA enrollment per project and IP address | 50 requests/minute, 500 requests/hour  
Finalize MFA enrollment per project and IP address | 150 requests/hour  
Start MFA sign-in per project and IP address | 50 requests/minute, 500 requests/hour  
Finalize MFA sign-in per project and IP address | 150 requests/hour  
SMS verification codes sent per phone number | 10 sent/hour  
  
## Identity Toolkit API limits

Operation | Limit  
---|---  
Queries per user | 30,000 requests/minute  
Queries per project | 180,000 requests/minute  
Account uploads per project* | 3,600 requests/minute  
Account downloads per project* | 21,000 requests/minute  
UserInfo queries per project* | 900 requests/minute  
Configuration updates per project* | 300 requests/minute  
Configuration updates per project and user* | 300 requests/minute  
Bulk delete accounts per project* | 60 requests/minute  
Custom token sign-ins per project | 45,000 sign-ins/minute  
`createAuthURI` calls per IP address | 120 requests/hour  
Blocking function invocations per project | 4,000 requests/minute  
`GetAccountInfo` per project* | 500,000 requests/minute  
  
* Admin-only operations.

The `fetchProvidersForEmail()` and [`fetchSignInMethodsForEmail(email)`](https://firebase.google.com/docs/reference/js/auth.md#fetchsigninmethodsforemail) methods leverage the `createAuthURI` endpoint.

## Token service API limits

Operation | Limit  
---|---  
Token exchange per project | 18,000 exchanges/minute  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
