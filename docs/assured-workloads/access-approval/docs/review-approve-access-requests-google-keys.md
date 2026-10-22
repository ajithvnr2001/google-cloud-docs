---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys/
title: Review and approve access requests using the Google-managed signing key \u00a0|\u00a0 Access Approval \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:41.181444+00:00
---

# Review and approve access requests using the Google-managed signing key  |  Access Approval  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management)
  * [ Access Transparency ](https://docs.cloud.google.com/assured-workloads/access-transparency)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to set up Access Approval using the Google Cloud console to receive email notifications of access requests for a project.

Access Approval ensures that a cryptographically-signed approval is present for Google personnel to access your content stored on Google Cloud.

## Before you begin

  * Enable [ Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) for your organization. For more information, see [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable). 



### Required roles

To get the permissions that you need to set up Access Approval and approve access requests, ask your administrator to grant you the following IAM roles on your project: 

  * View and update Access Approval configuration and approve access requests: [Access Approval Config Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.configEditor) (`roles/accessapproval.configEditor`) 
  * View Access Approval configuration and approve access requests: [Access Approval Approver ](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.approver) (`roles/accessapproval.approver`) 
  * View Access Approval configuration and access requests and download log reports: [Access Approval Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.viewer) (`roles/accessapproval.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enroll in Access Approval

To enroll in Access Approval, do the following:

  1. In the Google Cloud console, select the project for which you want to enable Access Approval.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Go to the **Access Approval** page.

[Go to Access Approval](https://console.cloud.google.com/security/access-approval)

  3. To enroll in Access Approval, click **Enroll**.

  4. In the dialog, select the enrollment mode for your policy and click **Enroll**.




### Access Approval enrollment mode

You can configure Access Approval in one of three modes and can change the mode at any time in the Access Approval settings. The following modes can be selected:

  1. **Transparency (Default)** : Use this mode to monitor Google administrative access into your workload without additional approval. For more information, see the [Access Transparency docs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs).
  2. **Streamlined support** : Use this mode to automatically approve Customer Care access to work on your support cases. Other access reasons require Access Approval.
  3. **Access Approval** : Use this mode to enable full Access Approval functionality for all accesses.



Access Transparency logs are generated automatically for all Access Approval modes.

## Configure settings

On the **Access Approval** page in the Google Cloud console, click settings**Manage settings**.

### Select services

Access Approval settings, including the list of enabled products, are inherited from the parent resource. You can expand the scope of enrollment by enabling Access Approval for all or selected additional services [supported services](https://docs.cloud.google.com/assured-workloads/access-approval/docs/supported-services).

### Set up email and Pub/Sub notifications

This section explains how you can receive access request notifications for this project.

#### Add yourself as an approver for Access Approval requests and configure notifications

To add yourself as an approver so you can review and approve access requests, do the following:

  1. Go to the **Access Approval** page in the Google Cloud console.

[Go to Access Approval](https://console.cloud.google.com/security/access-approval)

  2. Click settings**Manage settings**.

  3. To enable email notifications, add your email address in the **User or group email** field under **Set up approval notifications**.

  4. To enable Pub/Sub notifications:

     1. Add your Pub/Sub topic in the **Pub/Sub topic** field under **Set up approval notifications**.
     2. In Identity and Access Management (IAM), grant the Pub/Sub Publisher role (`roles/pubsub.publisher`) to the **customer-approval-jobs@system.gserviceaccount.com** principal to allow Access Approval to create notifications. Notifications won't be created without this step.



#### Review Default Settings

Default settings govern the behavior of Access Approval requests.

  * **Prefer resource specific approval requests** : Sets the default scope of Access Approval requests. By default, this setting is disabled. If you enable this setting, the number of Access Approval requests that you receive to access the same data might increase, possibly delaying assistance from Google support. Example Defaults: 
    * Disabled: product.googleapis.com/project/12345/
    * Enabled: product.googleapis.com/project/12345/instances/abcde
  * **Approval Request Default Expiration Days** : Set the default expiration for Access Approval requests. This can be changed at the time of approval for each request.
  * **Preferred maximum scope of access** : Sets the largest recommended resource access scope for a Google administrator to request. For example, when set to Project, Google administrators will request Project or Resource level access.



### Choose your signing key

Access Approval uses a signing key to verify the integrity of the Access Approval request.

By default, a Google-owned and managed key is used, and doesn't require any additional configuration.

To optionally configure a customer managed encryption key, see [setting up a custom key](https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-custom-keys).

## Review Approval requests

After you enroll in Access Approval and add yourself as an approver for access requests, you can expect to receive email notifications for access requests.

The following image shows a sample email notification that Access Approval sends when Google personnel request access to Customer Data.

![](https://docs.cloud.google.com/static/assured-workloads/access-approval/docs/images/access-request-email.png)![The email notification that gets sent when Google personnel request access to Customer Data.](https://docs.cloud.google.com/static/assured-workloads/access-approval/docs/images/access-request-email.png)

To review and approve an incoming access request, do the following:

  1. Go to the **Access Approval** page in the Google Cloud console.

[Go to Access Approval](https://console.cloud.google.com/security/access-approval)

To be taken to this page, you can also click the link in the email sent to you with the approval request.

  2. Click **Approve**.




After you approve the request, Google personnel with [characteristics](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approval-request-details) matching the approval, such as the same justification, location, or desk location, can access the specified resource and its child resources within the approved timeframe.

## Clean up

Access Approval is a standard Google Cloud control that is enabled in an audit only policy by default with the Transparency policy.

To restore the default Transparency policy and remove any required Access Approvals:

  1. On the **Access Approval** page in the Google Cloud console, click **Manage settings**.
  2. Click **Remove Settings**.
  3. In the dialog that opens, click **Remove Settings**.

**Note:** If the resource inherits settings from a parent resource, clicking **Remove Settings** removes the local configuration and reverts the resource to its inherited settings. This might not be the system default Transparency policy. 

## What's next

  * Learn about the [anatomy of an access request](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approval-request-details).
  * Learn how to [approve Access Approval requests](https://docs.cloud.google.com/assured-workloads/access-approval/docs/approve-requests).
  * Learn how to [view historical Access Approval requests](https://docs.cloud.google.com/assured-workloads/access-approval/docs/view-historical-requests).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
