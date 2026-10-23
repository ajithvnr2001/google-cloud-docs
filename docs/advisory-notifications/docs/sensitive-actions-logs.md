---
url: https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-logs/
title: Work with Sensitive Actions logs \u00a0|\u00a0 Advisory Notifications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:46.860405+00:00
---

# Work with Sensitive Actions logs  |  Advisory Notifications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/advisory-notifications/docs/sensitive-actions-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Advisory Notifications ](https://docs.cloud.google.com/advisory-notifications/docs)
  * [ Guides ](https://docs.cloud.google.com/advisory-notifications/docs/overview)



Send feedback 

#  Work with Sensitive Actions logs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Sensitive actions are always written to [Sensitive Actions Service platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#sensitive_actions_service). Additionally, Google Cloud provides a summary of sensitive actions through Advisory Notifications.

Links to view the first three individual actions of each type in the platform logs are provided in the notification. You need an appropriate [Identity and Access Management role](https://docs.cloud.google.com/logging/docs/access-control#considerations), such as `roles/logs.viewer`, to be able to view Cloud Logging logs.

If there are more than three sensitive actions of a particular type, the notification might also provide a link to view all actions in Logging. However, this link is not provided in all cases. Some sensitive actions, such as adding a project-level SSH key, can occur in several different projects in your organization. In this case, Google can't provide you with a single Logging link to view all the sensitive actions, because Logging is always scoped to a particular resource (project, folder, or organization).

## View all Sensitive Actions logs in the organization

If you want to see all Sensitive Actions logs in your organization, you can [set up a Logging bucket](https://docs.cloud.google.com/logging/docs/central-log-storage) to aggregate these logs.

Use the following query to include all Sensitive Actions logs in the bucket:
    
    
    logName:sensitiveaction.googleapis.com%2Faction
    

You can add additional terms if you only want certain types of Sensitive Actions logs, such as `AND "add_ssh_key"`.

## Set up alerts for Sensitive Actions logs

If you want to get more frequent alerts about sensitive actions, you can configure a [log-based alert](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts). For example, use the following query to match all Sensitive Actions logs:
    
    
    logName:sensitiveaction.googleapis.com%2Faction
    

## What's next

  * Learn about [audit logging](https://docs.cloud.google.com/advisory-notifications/docs/audit-logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
