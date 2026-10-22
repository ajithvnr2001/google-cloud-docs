---
url: https://docs.cloud.google.com/iam/docs/request-missing-permissions/
title: Request missing permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:14.526223+00:00
---

# Request missing permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/request-missing-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Request missing permissions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can request missing permissions when you encounter a permission error message.

If you don't have permission to modify access-related policies in your organization, you must send an administrator an access request using the context from the error message. You can't resolve the permission errors on your own.

You can request access in the following ways:

  * **Request the required permissions.** This resolution is effective for all types of permission errors.

  * **Request a grant against a Privileged Access Manager entitlement.** This resolution is only effective if the permission error is caused by your allow policies and if you have a Privileged Access Manager entitlement with the required permissions.

  * **Request a role with the required permissions.** This resolution is only effective if the permission error is caused by your allow policies.




If you're using the Google Cloud console and you have the [permissions required to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions), then you can grant yourself the role directly from the error message instead of requesting it. For more information, see Self-grant a role in the Google Cloud console.

### Request the required permissions

To request the required permissions, do the following:

### Console

  1. In the list of missing permissions, click **Request permissions**.

  2. In the **Request Access** panel, choose how you want to notify your administrator:

     * If your organization supports [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) and allows auto-generated access request emails, then you can send an auto-generated email to your organization's [technical Essential Contact](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories). To send this email, do the following:

       1. Select **Send auto-generated email**.
       2. Add any context about the request that you want to include.
       3. Click **Send request**.
     * To copy the access request and paste it into your preferred request management system, do the following:

       1. If your organization supports Essential Contacts and allows auto-generated emails but you want to send the notification manually, select **Notify manually**.
       2. Add any context about the request that you want to include.
       3. Click **Copy message**.
       4. Paste the request into your preferred request management system.

Your administrator receives your access request, along with any additional context that you provided.




### gcloud

Copy the `error_info_id`, if available, and the list of missing permissions from the error message, then use your preferred request management system to ask an administrator to give you these permissions.

### REST

Copy the `error_info_id`, if available, and the list of missing permissions from the error message, then use your preferred request management system to ask an administrator to give you these permissions.

### Request a grant against a Privileged Access Manager entitlement

[Privileged Access Manager entitlements](https://docs.cloud.google.com/iam/docs/pam-overview) define a set of IAM roles that you can request at any time. If your request is successful, then you're granted the requested roles temporarily.

This resolution option is only available if the permission error is caused by your allow policies and if you have a Privileged Access Manager entitlement with the required permissions.

To request a grant against an existing entitlement, do the following:

### Console

  1. When you encounter an error message, find the **Request temporary access** section. This section lists all of the Privileged Access Manager entitlements that contain a role with the required permissions.

![](https://docs.cloud.google.com/static/iam/img/iam-error-request-pam.png)

![](https://docs.cloud.google.com/static/iam/img/iam-error-request-pam.png)

If no **Request temporary access** section is returned, then no entitlements contain the required permissions. In this case, you can ask an administrator to [create a new entitlement](https://docs.cloud.google.com/iam/docs/pam-create-entitlements).

  2. Review the list of available entitlements and select the entitlement that you want to request a grant against.

  3. Click the entitlement, then click **Request access**.

  4. In the **Request grant** panel, enter the details for the request grant:

     * The duration required for the grant, up to the maximum duration set on the entitlement.

     * If required, a justification for the grant.

     * Optional: The email addresses to notify of the grant request. Google identities that are associated with approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

  5. Click **Request grant**.

  6. To see your grant history including approval statuses, go to the [**Privileged Access Manager** page](https://console.cloud.google.com/iam-admin/pam/entitlements/) in the Google Cloud console, then click **Grants > My grants**.




### gcloud

  1. [Search for available entitlements](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#search_available_entitlements) to find an entitlement with a role that has the required permissions.

If no entitlement is returned, then you can ask an administrator to [create a new entitlement](https://docs.cloud.google.com/iam/docs/pam-create-entitlements).

  2. [Request a grant against the entitlement](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#request_a_grant_against_an_entitlement).

  3. Optional: [Check your grant request status](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#request_a_grant_against_an_entitlement). 




### REST

  1. [Search for available entitlements](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#search_available_entitlements) to find an entitlement with a role that has the required permissions.

If no entitlement is returned, then you can ask an administrator to [create a new entitlement](https://docs.cloud.google.com/iam/docs/pam-create-entitlements).

  2. [Request a grant against the entitlement](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#request_a_grant_against_an_entitlement).

  3. Optional: [Check your grant request status](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#request_a_grant_against_an_entitlement). 




### Request a role

If the permission error is caused by an allow policy, then you can request that an administrator grant you a role with the required permissions to resolve the error.

If the error is caused by a different policy type or if you aren't sure which policy type is causing the error, then request the required permissions instead.

### Console

  1. In the **Request a specific role** section, review the list of recommended roles and choose the one that you want to request. You can click the roles to view more details about them. This section is only visible if the permission error is caused by an allow policy.

**Note:** The list of roles in the error message isn't comprehensive—in most cases, there are other roles that include the required permissions. However, on the error message page, you can only request roles that are listed in the **Request a specific role** section.
  2. Click the role that you've chosen, then click **Request role**.

![](https://docs.cloud.google.com/static/iam/img/iam-error-request-role-2x.png)

**Note:** If you have the [permissions required to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions), then the Google Cloud console displays a **Grant role** button instead of a **Request access** button. In this case, you can click **Grant role** to grant yourself the role and resolve the permission error.
  3. In the **Request Access** panel, choose one of the options for notifying your administrator:

     * If your organization supports [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) and allows auto-generated access request emails, then you can send an auto-generated email to your organization's [technical Essential Contact](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). To send this email, do the following:

       1. Select **Send auto-generated email**.
       2. Add any context about the request that you want to include.
       3. Click **Send request**.
     * To copy the access request and paste it into your preferred request management system, do the following:

       1. If your organization supports Essential Contacts and allows auto-generated emails but you want to send the notification manually, select **Notify manually**.
       2. Add any context about the request that you want to include.
       3. Click **Copy message**.
       4. Paste the request into your preferred request management system.

Your administrator receives your access request, along with any additional context that you provided.




### gcloud

  1. Identify an IAM role that contains the missing permissions.

To see all of the roles that a given permission is included in, search for the permission in the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions), then click the permission name.

If no predefined roles match your use case, then you can [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) instead.

  2. Use your preferred request management system to request that an administrator grant you the role.




### REST

  1. Identify an IAM role that contains the missing permissions.

To see all of the roles that a given permission is included in, search for the permission in the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions), then click the permission name.

If no predefined roles match your use case, then you can [create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) instead.

  2. Use your preferred request management system to request that an administrator grant you the role.




## Self-grant a role in the Google Cloud console

If you encounter a permission error in the Google Cloud console and you have the [permissions required to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#required-permissions), then you can grant yourself a role directly from the permission error message:

  1. In the **Select a role to grant** section, review the list of recommended roles and choose the one that you want to request. You can click the roles to view more details about them.

**Note:** The list of roles in the error message isn't comprehensive—in most cases, there are other roles that include the required permissions. However, on the error message page, you can only grant roles that are listed in the **Select a role to grant** section. If you want to grant a different role, then follow the instructions in [Grant or revoke a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-grant-single-role-gcloud) to grant the role.
  2. To grant the role that you've chosen, click the role, then click **Grant access**.

![](https://docs.cloud.google.com/static/iam/img/iam-error-grant-role-2x.png)




## What's next

  * If you have administrative permissions and need to resolve a user access request, see [Resolve permission errors](https://docs.cloud.google.com/iam/docs/resolve-permission-errors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
