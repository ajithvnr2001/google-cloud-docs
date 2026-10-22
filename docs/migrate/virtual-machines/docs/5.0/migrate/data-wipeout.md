---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/data-wipeout/
title: User data deletion \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:05.709860+00:00
---

# User data deletion  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/data-wipeout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  User data deletion Stay organized with collections  Save and categorize content based on your preferences. 

This document gives you an overview of how Migrate to Virtual Machines handles the deletion of your data stored in Google Cloud while migrating your virtual machine (VM) instances using Migrate to Virtual Machines.

The deletion of your data begins when you perform one of the following actions:

  * **Disable the Migrate to Virtual Machines API or delete your Google Cloud project:** You can [shut down projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects) using the Google Cloud console or the [`projects.delete`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/delete) method in the API. A project must have a lifecycle state of `ACTIVE` to be shut down in this way.

This method immediately marks a project to be deleted. A notification email is sent to the user who initiated the delete operation and the Technical category contacts that are listed in [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) on a best effort basis; if the notification fails to send, the project is still marked to be deleted. If there's no contact in the Technical category, the fallback contact isn't notified.

**Note:** If a third-party user initiates project deletion, then the email notification isn't sent to the contacts that are listed in [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). 

A project that is marked for deletion isn't usable. If the project has a billing account associated with it, that association is broken and isn't reinstated if the project delete operation is canceled. After 30 days, the project is fully deleted. Until it is fully deleted, the project might still be visible, although it isn't usable.

To stop the project delete process during the 30-day period, see the [steps to restore a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project).

**Warning:** You can recover most resources if you restore a project within the 30-day period. Some services have delays in restoring and you might need to wait some time for services to be restored. Some resources, such as Cloud Storage or Pub/Sub resources, are deleted much sooner. These resources might not be fully recoverable even if you restore the project within the 30-day period. In some cases, projects may continue to incur charges for a period of time after shutdown. To avoid unexpected charges, [ disable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) before shutting down the project. The billing account must be manually linked again after the project is restored. 

At the end of the 30-day period, the project and all of its resources are deleted and cannot be recovered. Until it is deleted, the project counts towards your project quota.

  * **Delete your Google account:** When a Google Account is closed, Google Cloud may impose an internal recovery period up to 30 days, depending on past account activity. After that grace period expires, a signal containing the deleted billing account `user_id` is broadcasted to Google products and Google Cloud resources tied solely to that `user_id` are marked for deletion.




For an overview of the secure process that occurs when you delete your data, see [Data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
