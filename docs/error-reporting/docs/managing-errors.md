---
url: https://docs.cloud.google.com/error-reporting/docs/managing-errors/
title: Manage error groups \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:14.442007+00:00
---

# Manage error groups  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/managing-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Manage error groups Stay organized with collections  Save and categorize content based on your preferences. 

Error Reporting lets you track investigation progress, coordinate triage with external issue trackers, and manage notifications for recurring application errors. Because grouped error events share common characteristics, Error Reporting retains up to 1,000 sample events and extrapolates the remaining data. To inspect all individual occurrences within an error group, you can examine the associated log entries in the Logs Explorer. For information about how errors are aggregated, see [How error events are grouped](https://docs.cloud.google.com/error-reporting/docs/grouping-errors#how_errors_are_grouped).

## Before you begin

**Note** : If you see the message "Set up Error Reporting" on the **Error Reporting** page, then your Google Cloud project has no error groups to display.

  * Make sure that you have at least one error group. For more information, see [Collect error events by using Error Reporting](https://docs.cloud.google.com/error-reporting/docs/setup).


  * To get the permissions that you need to manage errors, ask your administrator to grant you the [Error Reporting User ](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.user) (`roles/errorreporting.user`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Change resolution status

To record the status of your investigation into an error group, do the following:

  1. In the Google Cloud console, go to the **Error Reporting** page: 

[Go to **Error Reporting**](https://console.cloud.google.com/errors)

You can also find this page by using the search bar.

  2. On the error group that you want to update, click **Open** , and then select a resolution status. You can select any of the following values:

     * **Open** : The default initial state of all error groups. The other states are set manually. You can revert an error group's status to **Open** at any time.
     * **Acknowledged** : A state for triaging error groups.
     * **Resolved** : A state for indicating that an error group is fixed and no longer expected to occur. If an error group marked as **Resolved** later reoccurs, then Error Reporting changes the resolution status to **Open**.
     * **Muted** : A state for hiding an error group from your list. If an error event occurs in a muted error group, then the error event isn't recorded and you aren't notified.



## Add links to error groups

You can link error groups to pages such as issue trackers or documentation with resolution steps.

  * To add a link to an error group, click _add_ **Set the link to an issue tracker for this error group** , and then complete the dialog.

  * To edit the link on an error group, click _edit_ **Set the link to an issue tracker for this error group** , and then complete the dialog.

  * To open the link for an error group, click _link_ **Link to the issue tracker for this error group**.




## Set notifications

Error Reporting can notify you when new error events occur. It can also notify you when an error event occurs in an error group that has been marked **Resolved**. To learn more, and for instructions on setting notifications, see [Configure and manage notifications](https://docs.cloud.google.com/error-reporting/docs/notifications).

## Delete errors

You can delete all error events that are stored for the given Google Cloud project, and reset error-event counts to zero, by using either the Google Cloud CLI or the Error Reporting API.

###  gcloud 

To delete all error events, run this command:
    
    
    gcloud beta error-reporting events delete
    

###  REST API 

To delete all error events, use the [projects.deleteEvents](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects/deleteEvents) method of the REST API.

If you subscribe to [notifications](https://docs.cloud.google.com/error-reporting/docs/notifications) for the Google Cloud project and delete error events for an error group that has a status of **Resolved** , then the error group resolution status changes back to **Open**. If a new error event occurs, then Error Reporting sends a notification.

If you delete error events when the status of the error group is **Open** or **Acknowledged** , then Error Reporting doesn't send a notification if new error events occur.

## What's next

  * [Configure and manage notifications](https://docs.cloud.google.com/error-reporting/docs/notifications)
  * [View and filter error groups](https://docs.cloud.google.com/error-reporting/docs/viewing-errors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
