---
url: https://docs.cloud.google.com/gemini/docs/codeassist/manage-licenses/
title: Manage Gemini Code Assist Standard and Enterprise licenses \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:12.310018+00:00
---

# Manage Gemini Code Assist Standard and Enterprise licenses  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/manage-licenses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Manage Gemini Code Assist Standard and Enterprise licenses Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** This page discusses access to Gemini Code Assist using a Gemini Code Assist Standard and Enterprise license. Consumer account access to Gemini Code Assist features, such as through Gemini Code Assist for individuals, [has been deprecated](https://developers.google.com/gemini-code-assist/docs/deprecations/code-assist-individuals).

Before using Gemini Code Assist Standard and Enterprise, each user in your organization needs a license.

By default, automatic license assignment is enabled for all subscriptions. Users in your organization with the required permissions are automatically assigned a license when they start using Gemini Code Assist in a supported IDE. Those permissions are detailed later in this document. After you set up Gemini Code Assist, you can choose to assign licenses manually or continue with automatic assignment.

You can assign licenses to any users that have access to a project linked to the relevant [billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account).

## Before you begin

  * Ensure that you have the Billing Account Administrator ([`roles/billing.admin`](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)) or Consumer Procurement Order Administrator ([`roles/consumerprocurement.orderAdmin`](https://docs.cloud.google.com/marketplace/docs/access-control#consumerprocurement.orderAdmin)) IAM roles so that you can grant additional permissions required on the billing account for specific license management tasks detailed in the following sections.

  * Verify you have [set up Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini).

  * If you want to manage licenses using an API rather than the Google Cloud console, then verify the following:

    * Set up a [quota project](https://docs.cloud.google.com/docs/quotas/quota-project) for your billing account.
    * Enable the [Cloud Commerce Consumer Procurement API](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest) in your quota project.
    * Verify the following header key-value pairs are present on all API calls: 
      * `Authorization`: your [Google Cloud access token](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token) from the Google Cloud CLI
      * `x-goog-user-project`: the project ID of your quota project



## Change the number of Gemini Code Assist Standard and Enterprise licenses in a subscription

You can add or remove the number of Gemini Code Assist licenses [directly through the Google Cloud console](https://docs.cloud.google.com/gemini/docs/admin#edit-subscription), or through your Google account representative or an authorized reseller.

## View Gemini Code Assist Standard and Enterprise license assignments

Select one of the following options:

###  Console 

  1. Verify that you have the following IAM permissions on the billing account that owns the subscription:

     * `billing.accounts.get`
     * `consumerprocurement.orders.get`
     * `consumerprocurement.licensePools.get`
     * `consumerprocurement.licensePools.enumerateLicensedUsers`
     * `resourcemanager.projects.get`
  2. Go to the **Admin for Gemini** page and select the project attached to your billing account with the Gemini Code Assist Standard or Enterprise subscription.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin)

  3. Choose the subscription that you want to change, and then select **Modify Subscription**.

The following information is available for each user that has been assigned a license:

     * Name.
     * Email.
     * Date the license was assigned.
     * Date and time the license was last used.
  4. To find a specific set of users, you can filter and sort the list as follows:

     * To filter the list, in the **Filter** field, enter the properties and values.
     * To sort the list, select the heading of the column that you want to sort by. For example, to sort alphabetically by the user names, select the **Name** column heading.



### API

To view Gemini Code Assist Standard or Enterprise license assignments, use the [`billingAccounts.orders.licensePool.enumerateLicensedUsers` method](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1/billingAccounts.orders.licensePool/enumerateLicensedUsers).

  1. Verify that you have the `consumerprocurement.licensePools.enumerateLicensedUsers` IAM permission on the billing account that contains the license pool whose license assignments you want to view.

  2. Use [`cURL`](http://curl.haxx.se/) to call the method:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://cloudcommerceconsumerprocurement.googleapis.com/v1/billingAccounts/BILLING_ACCOUNT_ID/orders/ORDER_ID/licensePool:enumerateLicensedUsers/"
         

Replace the following:

     * PROJECT_ID: the ID for a project. Quota usage and charges associated with the API request are applied against this project.
     * `BILLING_ACCOUNT_ID`: the ID for the billing account associated with the license pool.
     * `ORDER_ID`: the order ID. If you don't know the order ID, you can retrieve it by [listing the orders associated with your billing account](https://cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1/billingAccounts.orders/list).



If the command succeeds, it returns `licensedUsers` output in the following format:
    
    
    {
      "licensedUsers": [
          {
              "username": "dana@example.com",
              "assignTime": "2024-09-26T16:24:40.559222Z"
          },
          {
              "username": "lee@example.com",
              "assignTime": "2024-09-26T16:24:40.559222Z"
          },
          {
              "username": "taylor@example.com",
              "assignTime": "2024-09-26T16:24:40.559222Z"
          },
          {
              "username": "bola@example.com",
              "assignTime": "2024-09-26T16:24:14.610828Z"
          }
      ]
    }
    

If there are no Gemini Code Assist Standard or Enterprise license assignments or the `ORDER_ID` is invalid, it returns `licensedUsers` output in the following format:
    
    
    {}
    

## Automatically assign Gemini Code Assist Standard and Enterprise licenses

You can enable automatic license assignment for a subscription.

Automatic license assignment is only supported in VS Code, IntelliJ, and other [supported JetBrains IDEs](https://docs.cloud.google.com/gemini/docs/codeassist/supported-languages#supported_ides).

If you choose to automatically assign licenses for Gemini Code Assist Standard or Enterprise, you can't remove or add individual user licenses under that account. Users with license assignments who haven't used any Gemini Code Assist Standard or Enterprise features are automatically de-provisioned at the end of the inactivity period set by the administrator.

  1. In the Google Cloud console, go to the **Admin for Gemini** page.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin)

  2. Select **Manage Gemini Code Assist** , and then select **Manage Subscription**.

  3. Select **License Management** , and then select **Enable Automatic License Assignment**. The **Enable automatic licenses** dialog appears.

Switching this subscription to automatically assign licenses turns off manual license assignment after the change, but pre-existing license assignments are unaffected.

  4. Set the length of time for a license to unassign if the assignee is inactive, then select **Confirm Change**. The **Automatic license assignment has been enabled** dialog appears.

If you configured `T` days of inactivity for unassignment, then license(s) are automatically unassigned and available in the license pool on day `T+1`. For example, if you configure `7` days of inactivity for unassignment, then the license(s) are unassigned and available in the license pool on day `8`.

  5. Select **Close**.

  6. Make sure you [grant the Gemini for Google Cloud User and Service Usage Consumer IAM roles to users](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini#grant-iam) to the licensed users.

Users with the `cloudaicompanion.licenses.selfAssign` permission automatically receive a license when they first access Gemini Code Assist Standard or Enterprise in a project paid by a billing account that has a valid subscription that is configured for automatic license assignment and has available licenses covered by your subscriptions in the billing account.




To disable automatic license assignment, follow these steps:

  1. In the Google Cloud console, go to the **Admin for Gemini** page.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin)

  2. Select **Manage Gemini Code Assist** , and then select **Manage Subscription**.

  3. Select **License Management** , and then select **Manage Automatic License Assignment**. The **Manage automatic license assignment** dialog appears.

  4. Select **Disable automatic license management**.

  5. Select **Confirm change**.




## Manually assign Gemini Code Assist Standard and Enterprise licenses to individual users

With manual license assignment, you can add and remove licenses for individual users. This method gives you direct control over who can access Gemini Code Assist, which is ideal for granting access to a specific set of users.

Select one of the following options:

###  Console 

  1. Verify that you have the following IAM permissions on the billing account that owns the subscription:

     * `billing.accounts.get`
     * `consumerprocurement.orders.get`
     * `consumerprocurement.licensePools.get`
     * `consumerprocurement.licensePools.enumerateLicensedUsers`
     * `consumerprocurement.licensePools.assign`
     * `resourcemanager.projects.get`
  2. Go to the **Admin for Gemini** page.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin)

  3. Select **Manage Gemini Code Assist** , and then select **Modify Subscription**.

  4. For this Gemini Code Assist Standard or Enterprise subscription, verify that you set **License Assignment** to **Manually Assign Licenses**. If the Gemini Code Assist Standard or Enterprise subscription is set to **Automatically Assign Licenses** , then you cannot manage individual licenses. Switching this billing account to **Manually Assign Licenses** turns off automatic license assignment after the change, but pre-existing license assignments are unaffected.

  5. Select **Add licensed user**. A user selection dialog appears. Only individual Google Account email addresses are supported, such as `@gmail.com`, `@googlegroups.com`, and Google Workspace domains. Workforce Identity Federation (BYOID) is not supported.

  6. Select **Add licensed user**.

  7. Verify that you [grant the Gemini for Google Cloud User and Service Usage Consumer IAM roles to users](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini#grant-iam) to the licensed users.




### API

To assign Gemini Code Assist Standard and Enterprise licenses, use the [`billingAccounts.orders.licensePool.assign` method](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1/billingAccounts.orders.licensePool/assign).

  1. Verify that you have the following IAM permissions on the billing account that contains the license pool whose license you intend to assign:


  * `billing.accounts.get`
  * `consumerprocurement.licensePools.assign`
  * `consumerprocurement.licensePools.get`
  * `consumerprocurement.licensePools.unassign`
  * `consumerprocurement.orders.get`


  1. Create a JSON file that contains the following information:
         
         {
           "usernames": [
             USER_EMAILS
           ]
         }
         

Replace `USER_EMAILS` with a comma-separated list of user accounts that are being assigned the license—for example, `"dana@example.com", "lee@example.com"`. Only individual Google Account email addresses are supported, such as `@gmail.com`, `@googlegroups.com`, and Google Workspace domains. Workforce Identity Federation (BYOID) is not supported.

  2. Use [`cURL`](http://curl.haxx.se/) to call the method:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         -H "Content-Type: application/json" \
         "https://cloudcommerceconsumerprocurement.googleapis.com/v1/billingAccounts/BILLING_ACCOUNT_ID/orders/ORDER_ID/licensePool:assign/"

Replace the following:

     * `JSON_FILE_NAME`: the path for the JSON file that you created in Step 2.
     * PROJECT_ID: the ID for a project. Quota usage and charges associated with the API request are applied against this project.
     * `BILLING_ACCOUNT_ID`: the ID for the billing account associated with the license pool.
     * `ORDER_ID`: the order ID. If you don't know the order ID, you can retrieve it by [listing the orders associated with your billing account](https://cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1/billingAccounts.orders/list).



If successful, the response is similar to the following:
    
    
    {}
    

To verify the assignment, view the list of assignments.

Then, verify that you [grant the Gemini for Google Cloud User and Service Usage Consumer IAM roles to users](https://docs.cloud.google.com/gemini/docs/codeassist/set-up-gemini#grant-iam) to the licensed users.

## Manually unassign Gemini Code Assist Standard and Enterprise licenses

Select one of the following options:

###  Console 

  1. Verify that you have the following IAM permissions on the billing account that owns the subscription:

     * `billing.accounts.get`
     * `consumerprocurement.orders.get`
     * `consumerprocurement.licensePools.get`
     * `consumerprocurement.licensePools.enumerateLicensedUsers`
     * `consumerprocurement.licensePools.unassign`
     * `resourcemanager.projects.get`
  2. Go to the **Admin for Gemini** page.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin)

  3. Select **Manage Gemini Code Assist** , and then select **Manage Subscription**.

  4. Select **License Management** , and then select **Manage Automatic License Assignment**. The **Manage automatic license assignment** dialog appears.

  5. Select the users for which you want to unassign licenses, then select **Unassign License**.

  6. Select **Confirm**.




### API

To unassign Gemini Code Assist Standard and Enterprise licenses, use the [`billingAccounts.orders.licensePool.unassign` method](https://docs.cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1/billingAccounts.orders.licensePool/unassign).

  1. To perform this task, you must have the `consumerprocurement.licensePools.unassign` Identity and Access Management (IAM) permission on the billing account that contains the license pool whose license you intend to unassign.

  2. Create a JSON file that contains the following information:
         
         {
           "usernames": [
             USER_EMAILS
           ]
         }
         

Replace `USER_EMAILS` with a comma-separated list of user accounts that are assigned the license—for example, `"dana@example.com", "lee@example.com"`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the method:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         -H "Content-Type: application/json" \
         "https://cloudcommerceconsumerprocurement.googleapis.com/v1/billingAccounts/BILLING_ACCOUNT_ID/orders/ORDER_ID/licensePool:unassign/"

Replace the following:

     * `JSON_FILE_NAME`: the path for the JSON file that you created in Step 2.
     * PROJECT_ID: the ID for a project. Quota usage and charges associated with the API request are applied against this project.
     * `BILLING_ACCOUNT_ID`: the ID for the billing account associated with the license pool.
     * `ORDER_ID`: the order ID. If you don't know the order ID, you can retrieve it by [listing the orders associated with your billing account](https://cloud.google.com/marketplace/docs/reference/consumerprocurement/rest/v1/billingAccounts.orders/list).



If successful, the response is similar to the following:
    
    
    {}
    

To verify the unassignment, view the list of assignments.

## Transfer Gemini Code Assist Standard and Enterprise licenses

Gemini Code Assist Standard and Enterprise licenses cannot be transferred directly between users. Instead, unassign the license from a user and then assign a license to the new user.

## Prevent cross-organization license usage

Gemini Code Assist Standard and Enterprise licenses are assigned to individual users, not organizations or projects, allowing individual users to use Gemini Code Assist Standard and Enterprise across multiple organizations.

Any [logs generated from Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/log-gemini) usage are stored within the project in which the usage occurred and not with the licensee. Additionally, any customization or configuration of Gemini Code Assist (such as [code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization)) is done on the project, not at the license or subscription level.

Some large organizations might want to prevent developers in their organization from using Gemini Code Assist Standard or Enterprise in certain projects in their organization, such as when certain projects have different billing accounts or when different projects are associated with different customers with different tenancies and tools.

In these cases, to help prevent cross-organization usage of Gemini Code Assist Standard and Enterprise in a project, you can do one of the following:

  * [Disable the Gemini for Google Cloud API on a project](https://docs.cloud.google.com/gemini/docs/turn-off-gemini#companion-api).
  * Use Identity and Access Management (IAM) [denial policies](https://docs.cloud.google.com/iam/docs/deny-overview) to deny specific users access to the project.



## Limitations

  * Gemini Code Assist license management does not support [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
