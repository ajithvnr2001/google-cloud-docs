---
url: https://docs.cloud.google.com/resource-manager/docs/project-suspension-guidelines/
title: Project suspension guidelines \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:01:47.402041+00:00
---

# Project suspension guidelines  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/project-suspension-guidelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/resource-manager/docs/resources)



Send feedback 

#  Project suspension guidelines Stay organized with collections  Save and categorize content based on your preferences. 

## Google terms of service violations and Google Cloud resources

Google treats policy and Terms of Service (ToS) violations very seriously in order to protect users, resources, and data. At the same time at Google we understand the value of users' Google Cloud resources and we have provided safeguards and recovery mechanisms for legitimate users that temporarily lose access to their Google Cloud resources due to ToS violations.

This page describes how ToS violations may affect access to your Google Cloud resources and provides best practices to ensure a quick recovery.

## Suspended vs orphaned Project resources

A Project resource or user can be suspended by Google due to ToS violations. If the user is the sole owner of a Project resource, that Project will also be suspended. When this happens, existing workloads are shut down, and users lose access to the suspended Project resource. Project owners will receive an email notification informing them of the suspension, and how to appeal the suspension. If a Project resource is suspended for more than nine months, it is marked for deletion. See the [Policy Violations FAQ](https://support.google.com/cloud/answer/7002354?hl=en) for more information on appeal best practices in case of a Project resource suspension. 

A Project resource becomes orphaned if it does not have an owner, regardless of whether they are active or suspended. This might come about if the Google accounts belonging to all owners or users associated with the Project resource are deleted. A Project resource isn't considered orphaned if the owners are suspended.

Orphaned Project resources are inaccessible. If you want to recover an orphaned project, reach out to [Google support](https://console.cloud.google.com/support). A Project resource that is orphaned will immediately be marked for deletion unless one of the following criteria is met:

  1. It has some API activity that is reflected in the logs.
  2. It is associated with a [Google Workspace](https://gsuite.google.com) customer domain.
  3. It has a live [App Engine](https://cloud.google.com/appengine) app.
  4. It has any active or future Variable Term Quota.
  5. It is linked to a Cloud Billing account.
  6. It is owned by an [Organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) resource.



Projects that are marked for deletion are not usable, and will be fully deleted after approximately 30 days. Some resources, such as Cloud Storage resources, are deleted much sooner. For more information about the project deletion process, see [Creating and Managing Projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

## How to avoid orphaned projects

In order to prevent a project from becoming orphaned, we recommend that more than one owner be associated with the project at all times.

If a project belongs to an [Organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations), then it will always have at least the Organization as an owner and as such will not be orphaned. The Organization administrator has full control over each project in the Organization. To eliminate the risk of a Project resource becoming orphaned, we recommend [obtaining an Organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) and migrating all production projects under it.

## Effect of ToS violations

### Google-wide disabled account

In some cases a Google-wide account (which covers access to a variety of Google products like Google Photos, Google Play, Google Drive, and Google Cloud) will be disabled for violations of a Google ToS, egregious policy violations, or as required by law. Owners of disabled Google accounts will not be able to access their Google Cloud resources until the account is reinstated. If an account is disabled, a notification is sent to the secondary email address provided during the signup process, if available. If a phone number is available, the user is notified via text message. The notification includes a link for appeal and recovery, where applicable.

In order to regain access to their Google Cloud resources, owners of disabled Google accounts will need to contact Google support and have their account re-enabled. To contact Google support, [log in to your Google account](https://accounts.google.com/Login).

To minimize the effect of an account being disabled on Google Cloud resources, we recommend that you add more than one owner to all resources. As long as there is at least one active owner, Google Cloud resources will not be suspended due to the one of the owners being disabled.

### Google Cloud account suspension

In certain circumstances when a Google Cloud user is consistently violating ToS or [Google Cloud Acceptable Use Policy](https://cloud.google.com/terms/aup) (AUP) through their projects, their access to Google Cloud may be suspended. When that happens, the developer will not be able to access their Cloud projects. They will continue to have access to other Google services like Gmail.

When a Google Cloud account is suspended and the developer has at least one active project, they will get an email informing them about the project being suspended. The developer can go to the Console, fill out the form and reach out to Google to resolve the issue.

See the [Policy Violations FAQ](https://support.google.com/cloud/answer/7002354?hl=en) for more information on appeal best practices in case of a Project resource suspension. 

### Google Cloud project suspension

Google Cloud projects may be suspended due to violations of the Google Cloud ToS, including the Google Cloud Acceptable Use Policy (Google Cloud AUP). When activities that violate the Google Cloud AUP or ToS are detected in a project, the project owner has an obligation to fix the violation immediately. If the violation is not fixed, Google may take action to suspend the project. It is important that Google Cloud developers check the project owner email account regularly. If Google suspends a Google Cloud project then all the associated Google Cloud workloads will be suspended as well. The owner of a suspended project will receive a notification email from google-cloud-compliance@google.com with resources to appeal.

If a suspended Project resource has at least one owner, whether active or suspended, it is not considered orphaned and will not marked be for deletion. However, a Project resource that has been suspended for nine months will be marked for deletion even if it is not orphaned.

To recover a suspended project fix the issue and follow the link in the notification email or contact Google Support. To contact Google support, [log in to your Google account](https://accounts.google.com/Login). See the [Policy Violations FAQ](https://support.google.com/cloud/answer/7002354?hl=en) for more information on appeal best practices in case of a Project resource suspension.

## Cloud Billing account suspension

Google Cloud Cloud Billing accounts may be suspended due to violations of Google Cloud ToS, missed payments, or for suspected fraud. If a Cloud Billing account is suspended then all Google Cloud resources attached to that Cloud Billing account are suspended as well.

If your Cloud Billing account remains invalid for a protracted period, some resources might be removed from the projects associated with your account. **Removed resources are not recoverable.** See the [Resolve Cloud Billing issues](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues) page for more information.

To recover a suspended Cloud Billing account, owners can use one of these options:

  * **Submit documents or request a verification code** : Use [Google payments center](https://payments.google.com) to see if you need to submit documents or get a verification code.

[Learn about verifying an account in Google payments center](https://support.google.com/googlepay/answer/7644078#zippy=%2Crequest-a-verification-code%2Cupload-documents).

  * **Make a manual payment** : In the Google Cloud console, sign in to the **Payment overview** page for your Cloud Billing account, and click **Make a payment**.

[Go to Payment overview](https://console.cloud.google.com/billing/payment)

[Learn about making manual payments to your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manual-payment).




You might need to manually restart services that were shut down while the Cloud Billing account was suspended. See [Restarting Google Cloud services](https://docs.cloud.google.com/billing/docs/how-to/restart-services) for information on restarting your services.

Cloud resources linked to a suspended Cloud Billing account are not considered orphaned, as long as they have at least one active owner.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
