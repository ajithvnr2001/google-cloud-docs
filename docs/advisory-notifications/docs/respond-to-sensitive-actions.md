---
url: https://docs.cloud.google.com/advisory-notifications/docs/respond-to-sensitive-actions/
title: Respond to Sensitive Actions notifications \u00a0|\u00a0 Advisory Notifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:24.326246+00:00
---

# Respond to Sensitive Actions notifications  |  Advisory Notifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/advisory-notifications/docs/respond-to-sensitive-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Advisory Notifications ](https://docs.cloud.google.com/advisory-notifications/docs)
  * [ Guides ](https://docs.cloud.google.com/advisory-notifications/docs/overview)



Send feedback 

#  Respond to Sensitive Actions notifications Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Sensitive actions can have a negative effect on your business if they are taken maliciously or in error.

## Investigate the activity

Consider reaching out to the owner of the user account that performed the action to make sure that the owner took the action themselves and that the action was intentional.

You can use Cloud Logging to view other actions taken by the same user account. For example, the following query searches for Admin Activity Audit Logs that mention `user@domain.com`:
    
    
    logName:cloudaudit.googleapis.com%2Factivity AND "user@domain.com"
    

By default, you can view Admin Activity Audit Logs in only a single project, folder, or organization at a time. To aggregate logs across your organization, see [Aggregate and store your organization's logs](https://docs.cloud.google.com/logging/docs/central-log-storage).

## Respond to an unrecognized activity

If you determine that the action was not legitimate, it is possible that the acting user account is compromised.

  * If you use Google Workspace as your identity provider, your Google Workspace administrator can take steps to [secure the account](https://support.google.com/a/answer/2984349).
  * If you use a third-party identity provider, check their documentation for what steps you can take.
  * Consider taking steps to undo the action. For example, if a sensitive role was unintentionally granted at the organization level, you should remove this role.



## What's next

  * Learn about [Sensitive Actions logs](https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-logs).
  * Learn how to [opt in to or out of notifications](https://docs.cloud.google.com/advisory-notifications/docs/opt-in-out-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
