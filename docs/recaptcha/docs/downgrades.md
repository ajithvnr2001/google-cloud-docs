---
url: https://docs.cloud.google.com/recaptcha/docs/downgrades/
title: Understand tier downgrades \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:52.703739+00:00
---

# Understand tier downgrades  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/downgrades/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Resources ](https://docs.cloud.google.com/recaptcha/docs/resources)



Send feedback 

#  Understand tier downgrades Stay organized with collections  Save and categorize content based on your preferences. 

A downgrade transitions your Google Cloud Fraud Defense project to a lower product tier. A downgrade occurs when a project no longer meets the eligibility criteria for its current tier.

## Why projects are downgraded

A tier transition typically happens for one of the following reasons:

  * **Enterprise to Premium:** Your Enterprise subscription has expired, lapsed, or is no longer active, or the project was unlinked from an account with an active subscription.
  * **Premium to Essentials:** The billing account associated with your Google Cloud project has been unlinked, disabled, or has billing issues, such as outstanding payments.



## Downgrade notifications

When a project is scheduled for a tier transition or enters a grace period, downgrade email notifications are sent to users assigned the following Identity and Access Management roles in the Google Cloud project:

  * Project Owner (`roles/owner`)
  * reCAPTCHA Enterprise Admin (`roles/recaptchaenterprise.admin`)



The email notifications provide warnings about the impending downgrade, instructions on how to resolve subscription or billing issues, and the date when the grace period expires.

## Grace period

Fraud Defense provides a 30-day grace period for Enterprise to Premium downgrades. During this time, you retain access to Enterprise features so you can resolve billing issues or update your integration. After the 30-day grace period expires, access to Enterprise-exclusive features is removed.

## Impact on features

A downgrade reduces the features that are available in your project to match the target tier:

  * **Downgrades to Premium:** You lose access to Enterprise-exclusive features. For a side-by-side comparison of features, see the [features comparison table](https://docs.cloud.google.com/recaptcha/docs/compare-tiers).
  * **Downgrades to Essentials:** You lose access to Premium features, and your monthly free assessment limit is capped at 10,000. Assessments beyond this limit return the `HTTP 429 (Resource Exhausted)` error.



## Impact on existing integrations

Depending on the features you use, a downgrade can cause API errors or user interface changes:

  * **Advanced reason codes:** The `CreateAssessment` response no longer contains advanced reasons in the `extended_verdict_reasons` field. If your backend relies on these codes, update it to use standard classification reasons.
  * **Related accounts API:** Calls to related account endpoints return a `PERMISSION_DENIED` error. You must stop calling these APIs.
  * **Transaction defense:** If you request transaction assessments without sending a frontend token, the API returns a `PERMISSION_DENIED` error. To continue using Transaction defense, you must implement a [frontend integration](https://docs.cloud.google.com/recaptcha/docs/fraud-prevention#installation-frontend).
  * **ATO analytics:** The `accountTakeoverVerdict` field is empty or missing from the `accountDefenderAssessment` response. Backend logic expecting this field must be updated to avoid errors.
  * **UI-only features:** Features such as Site-specific fraud reports and Attack investigations no longer appear in the Google Cloud console.
  * **[Policy Engine](https://docs.cloud.google.com/recaptcha/docs/policy-engine):** Depending on the target tier, a downgrade affects your policies as follows:

    * **Downgrades to Premium:** Any existing policies with more than three rules (the maximum allowed in the Premium tier) remain active and continue to enforce all rules without changes. However, any attempt to create a new policy or update an existing policy with more than three rules returns a `PERMISSION_DENIED` error. To update a policy that exceeds this limit, you must first delete excess rules until the policy contains three or fewer rules.
    * **Downgrades to Essentials:** Any existing policies remain active and continue to enforce all rules. However, you cannot create new policies or update existing ones. To modify these policies, you can only delete them.

**Example**

You have a policy with five rules and downgrade to the Premium tier. The policy continues applying all five rules. However, if you later try to update an existing rule or create a new policy with five rules, the API returns a `PERMISSION_DENIED` error.




## Verify your feature usage

To determine whether your integrations will be affected by a downgrade, verify the following:

  * Check the backend code for references to `extended_verdict_reasons` or `accountTakeoverVerdict`. For details, see [Interpret assessments for websites](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website). Also see [Detect and prevent account takeovers](https://docs.cloud.google.com/recaptcha/docs/account-takeovers).
  * Check whether your backend calls any [Related accounts API](https://docs.cloud.google.com/recaptcha/docs/account-query-apis) endpoints.
  * Check whether you are making transaction assessments without frontend tokens. For details, see [Install transaction defense](https://docs.cloud.google.com/recaptcha/docs/fraud-prevention#installation-frontend).
  * Check whether any Policy Engine policies have more than three rules. For details, see [Set up Policy Engine with a Universal key](https://docs.cloud.google.com/recaptcha/docs/policy-engine). If your project transitions to the Premium tier, you must reduce the rule count in a policy to three or fewer before updating it. If your project transitions to the Essentials tier, you cannot update policies.



### Prevent or restore from a downgrade

To prevent service disruption or restore access to features, resolve the billing or subscription issues:

  * **Restore Enterprise status:** Associate your project with an active billing account that has a valid Fraud Defense subscription. If you need a new subscription, contact your Google Cloud sales representative or [Google Cloud sales](https://cloud.google.com/contact).
  * **Restore Premium status:** Ensure your project is linked to an active, valid Google Cloud billing account.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
