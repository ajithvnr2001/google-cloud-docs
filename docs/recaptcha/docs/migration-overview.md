---
url: https://docs.cloud.google.com/recaptcha/docs/migration-overview/
title: reCAPTCHA Classic to reCAPTCHA Enterprise migration overview \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:57.874761+00:00
---

# reCAPTCHA Classic to reCAPTCHA Enterprise migration overview  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/migration-overview/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  reCAPTCHA Classic to reCAPTCHA Enterprise migration overview Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the migration of reCAPTCHA Classic to reCAPTCHA Enterprise on Google Cloud, including the reasons to migrate, the automated process, and the impact on your existing reCAPTCHA implementations.

## Why migrate to reCAPTCHA

reCAPTCHA on Google Cloud provides enterprise-grade features like Account defense, SMS defense, multi-factor authentication, and fraud prevention. The platform uses Google Cloud for dashboards and integrates with Cloud Monitoring and Looker for enhanced monitoring, reporting, and alerts.

Whether you [migrate your keys yourself](https://www.google.com/recaptcha/admin/migrate) or wait for the automated migration, your keys continue to function without any code changes.

## Impact on existing keys and data

Your existing v2 or v3 site keys continue to work after migration. You don't need to change any code on your website. The key continues to function even if you don't immediately accept the project ownership invitation.

### Google Cloud-based deployment benefits

Moving to the Google Cloud-based deployment provides the following benefits:

  * **Simplified technology** : All reCAPTCHA development is dedicated to this unique offering.
  * **Stronger compliance** : The platform improves adherence to data protection regulations by shifting from data controller to data processor.
  * **Advanced feature exposure** : You gain access to advanced features such as Account defense and Password defense, as well as an improved Google Cloud experience that includes generative AI insights and enhanced dashboard.
  * **Resolves terms of service issues** : The platform resolves issues where users' transitive enterprise use Terms of Service restrict their data usage.



## Automatic migration process overview

If you don't migrate your keys yourself, reCAPTCHA automatically migrates them. The automatic migration provisions a Google Cloud project and associates your reCAPTCHA keys with that project. Automigration includes the following steps:

  1. A Google Cloud project is created to hold your existing keys.

  2. Your project keys are associated with the Google Cloud project.

  3. An email invitation is sent to you to accept ownership of the project. If a key has multiple owners, all of them are invited to the same new project.

Project ownership invitations don't expire. Your keys continue to function after migration. However, to manage the keys, such as to create, delete, or modify them, you must accept the project.

**Google Workspace users** : Your workspace organization might have restricted access to Google Cloud. To resolve this, ask your administrator to turn on the Google Cloud service in the Google Admin console. For more information, see [Turn Google Cloud on or off for users](https://support.google.com/a/answer/182442).

If you have an existing Google Cloud organization, you can [migrate](https://docs.cloud.google.com/resource-manager/docs/project-migration) the project that was created by the automigration process to your existing Google Cloud organization. If you want to manage your reCAPTCHA integration from an existing project, create a new reCAPTCHA key in that project.


**Important:** If the administrator or owner of the Classic reCAPTCHA key protecting your site is no longer active, the automatic migration still proceeds. If this occurs, you cannot reclaim the migrated project. Instead, create a new reCAPTCHA key in a new or existing Google Cloud project that you can access and update your integration accordingly.

## Migration timeline

All reCAPTCHA Classic customers must self-migrate or will be automatically migrated to Google Cloud. The process involves the following phases.

  * **Q3 2024** : New Classic keys are no longer allowed.
  * **Q1 2025** : The first notification that informs customers to migrate using the self-migration tool is sent.
  * **Q3 2025** : A follow-up notification is sent to customers that haven't yet migrated from Classic, which links directly to the [migration tool](https://www.google.com/recaptcha/admin/migrate) in [the Google Cloud console](https://docs.cloud.google.com/recaptcha/docs/migrate-recaptcha#migrate-through-cloud-console).
  * **Q4 2025** : Begin automated migration of Classic keys.
  * **Q1 2026** : Complete automated migration. API access locked for keys without a Google Cloud project.



You can migrate your Classic accounts at your convenience. Consider your company's code freeze schedule when planning your migration. The Google team automatically migrates your Classic accounts in October if you don't migrate your account. No immediate code changes are required. SiteVerify requests continue to function as they did before the migration. Migrate and [create an assessment](https://docs.cloud.google.com/recaptcha/docs/using-features) after your account migrates to Google Cloud to use the advanced features.

## Access to the reCAPTCHA Admin console

The [reCAPTCHA Admin console](https://www.google.com/recaptcha/admin) remains available. After you migrate your account to Google Cloud, you can still access your historical data and any configuration related to your Classic accounts from the [reCAPTCHA Admin console](https://www.google.com/recaptcha/admin). However, any changes to key configuration must be made through the Google Cloud console.

**Important:** If you don't accept project ownership after your account is migrated, the reCAPTCHA Admin console will redirect you to accept project ownership.

## Billing and enforcement

reCAPTCHA Enterprise has a free tier of 10,000 monthly assessments. For usage over 10,000 assessments per month, you must enable [billing](https://docs.cloud.google.com/recaptcha/docs/billing-information#how-it-works) for your Google Cloud project.

If you exceed the free 10,000 monthly assessments after automigration and don't enable billing, reCAPTCHA returns an error for any new request.

  * **`SiteVerify` requests**: After migration, `SiteVerify` requests that exceed their quota will `fail open`. This means that they will return `success:true` with a score of `0.9`, and the API response will include an error message indicating that you exceeded the quota. This behavior is designed to prevent valid users from being blocked, similar to the previous Classic reCAPTCHA policy. It is a change in API behavior for Enterprise keys.

  * **`CreateAssessment` requests**: `CreateAssessment` requests that exceed their quota `fail closed`. This means that the request will return a `Resource Exhausted (429)` HTTP error and no `Assessment` is created. To help prevent this, over-quota notifications and emails will alert you about a missing billing account.




## Key management and monitoring

After migration, you onboard to the Google Cloud console for key management. Use the Google Cloud console to monitor your site's traffic and analyze risk for requests that occur after the migration.

## What's next

  * [Use reCAPTCHA features after migration](https://docs.cloud.google.com/recaptcha/docs/using-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
