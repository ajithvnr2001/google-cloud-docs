---
url: https://docs.cloud.google.com/gemini/enterprise/docs/licenses/
title: Get subscriptions and assign licenses for Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:08.846211+00:00
---

# Get subscriptions and assign licenses for Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/licenses/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Get subscriptions and assign licenses for Gemini Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get subscriptions for Gemini Enterprise and how to manage user licenses.

Setting up access typically involves the following stages:

  1. **Procure** : Purchase a subscription to a product edition for your billing account.
  2. **Distribute** : Allocate licenses from the subscription to specific projects and locations.
  3. **Assign** : Assign the distributed licenses to individual users.



## About licenses

To sign in to the Gemini Enterprise app, a user must have a _license_. Licenses can be assigned to users manually or automatically.

  * **Manually-assigned licenses:** You can add users by their email addresses.

  * **Automatically-assigned licenses:** You can configure a subscription so that Gemini Enterprise automatically assigns a license to a user the first time they access the Gemini Enterprise or the Gemini Notebook Enterprise interface.


**Note:** Licenses are specific to a Google Cloud project and a location. For example, if users require access to a Gemini Enterprise app located in a Google Cloud project that is in both the US and global multi-regions, you need to have two separate licenses for these two separate locations within the same Google Cloud project.

## About subscriptions

To get licenses, you must first have a _subscription_ to a Gemini Enterprise edition. Subscriptions are specific to a billing account. For information about available editions, see [Compare editions of Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/editions).

For Gemini Enterprise, you can buy a monthly subscription or a year-long subscription. These subscriptions can be set to renew automatically.

You can purchase subscriptions for the Gemini Enterprise Standard, Gemini Enterprise Plus, and Gemini Enterprise Pay-as-you-go editions using the Google Cloud console.

### Subscription seat quantity limits

When you purchase or modify a seat-based subscription directly through the Google Cloud console, automatic seat quantity caps apply based on your Cloud Billing account type:

  * **Self-serve (or Online) and resold billing accounts:** Limited to a maximum of 25 seats per account when managing subscriptions using Google Cloud console.
  * **Invoiced (or Offline) account billing accounts:** Limited to a maximum of 1,000 seats per account.



If your organization requires more seats or if you encounter the maximum seat limit error when trying to add licenses to an existing subscription, contact your Google Cloud sales representative or account manager to purchase additional licenses through an offline order or request an allowlist exemption.

## About subscription states

A subscription can be in one of the following states:

State | Description  
---|---  
Not started |  You purchased the subscription, but it is not yet active. You can distribute licenses from this subscription to projects, but users assigned these licenses won't have access to Gemini Enterprise until the subscription becomes active. For more information, see Distribute licenses.   
Active |  The subscription is active, and users who have a license in this subscription can access Gemini Enterprise.   
Deactivating |  The subscription is in a deactivating state, with licenses scheduled for early termination. Users with licenses in this subscription continue to have access to Gemini Enterprise for a grace period of one week. After this week, the licenses transition to the Expired state. For more information, see Handle early termination.   
Expired |  Users with licenses in this subscription lose access to Gemini Enterprise when the subscription term ends or when licenses transition from the deactivating state to the expired state after early termination.   
  
## Before you begin

Before starting the procedures on this page, make sure you meet the following prerequisites:

  * Complete all tasks outlined in [Set up Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin). This includes:

    * Setting up a billing account for your project.
    * Granting at least the Gemini Enterprise User role to any users you'll license to use Gemini Enterprise.
  * Verify that billing is enabled for your Google Cloud project. For more information, see [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).

**Note:** To subscribe to the Gemini Enterprise Pay-as-you-go edition, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

  * Confirm that you have the required IAM roles and permissions:

    * The [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

    * If you manage billing for your organization, you must have the following roles to manage Gemini Enterprise subscriptions and procurement orders.

      * [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)
      * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)

Alternatively, for granular IAM control, you can use a custom role with the following permissions instead of the **Billing Account Administrator** role:

Service | Permissions  
---|---  
Discovery Engine |  `discoveryengine.billingAccountLicenseConfigs.distribute`  
`discoveryengine.billingAccountLicenseConfigs.get`  
`discoveryengine.billingAccountLicenseConfigs.list`  
`discoveryengine.billingAccountLicenseConfigs.retract`  
`discoveryengine.licenseConfigs.create`  
`discoveryengine.licenseConfigs.get`  
`discoveryengine.licenseConfigs.list`  
`discoveryengine.licenseConfigs.update`  
`discoveryengine.projects.get`  
`discoveryengine.projects.provision`  
`discoveryengine.projects.reportConsentChange`  
`discoveryengine.userStores.batchUpdateUserLicenses`  
`discoveryengine.userStores.listUserLicenses`  
Consumer Procurement |  `consumerprocurement.orders.get`  
`consumerprocurement.licensePools.assign`  
`consumerprocurement.licensePools.unassign`  
`consumerprocurement.licensePools.enumerateLicensedUsers`  
Resource Manager |  `resourcemanager.projects.get`  
`resourcemanager.projects.list`  
Service Usage |  `serviceusage.services.get`  
`serviceusage.services.list`  



## Get a subscription

To get licenses, purchase a subscription to a Gemini Enterprise edition for your billing account. The subscription provides a pool of licenses that you can use with any project connected to that billing account, distribute to projects, and assign to users.

### Standard and Plus

To subscribe to the Gemini Enterprise Standard or Plus edition, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage subscriptions > Create subscription**.

  3. For the **Gemini Enterprise Standard** or **Gemini Enterprise Plus** edition, click **Subscribe**.

  4. Configure the **Billing details** :

     1. Select the **Billing account** from the drop-down.
     2. Enter a **Subscription name**.
     3. Enter the **Number of licenses** you need for the edition.
  5. Select the **Subscription period**.

  6. If you want the subscription to renew automatically, select **Auto renew subscription**.

  7. Configure the **Distribution details** :

     1. In the **Select a project** drop-down, select your project.
     2. Choose a **Location type** for your subscription. If you don't have compliance or regulatory reasons to locate your data in the US or EU multi-regions, Google recommends that you choose the global multi-region for maximum availability and low latency.
  8. Click **Create > Confirm**.




### Pay-as-you-go

With a Pay-as-you-go subscription, you pay monthly for what you consume. For more information, see [Quotas and pricing for the Pay-as-you-go edition](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#quotas-pay-as-you-go). You can use the subscription with any project connected to your billing account.

**Note:** To subscribe to the Gemini Enterprise Pay-as-you-go edition, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

To subscribe to the Gemini Enterprise Pay-as-you-go edition, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage subscriptions > Create subscription**.

  3. On the **Gemini Enterprise Pay-as-you-go** edition, click **Subscribe**.

  4. Configure the **Billing details** :

     1. Enter a **Subscription name**.
     2. Enter the **Number of licenses** you need for the edition.
  5. Configure the **Distribution details** :

     1. In the **Select a project** drop-down, select your project.
     2. Choose a **Location type** for your subscription. If you don't have compliance or regulatory reasons to locate your data in the US or EU multi-regions, Google recommends that you choose the global multi-region for maximum availability and low latency.
  6. Click **Create > Confirm**.




## Manage subscriptions

This section describes how to view, update, distribute, and reclaim Gemini Enterprise subscriptions.

### View subscription details

To view the details of your Gemini Enterprise subscriptions, do the following:

### Console

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage subscriptions**.

  3. Select the **Billing account** from the drop-down.

  4. In the **Gemini Subscriptions** table, click the name of your subscription.




### REST

To get subscription detail, run the following command:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_NUMBER" \
      "https://discoveryengine.googleapis.com/v1alpha/billingAccounts/BILLING_ACCOUNT_ID/billingAccountLicenseConfigs"
    

Replace the following:

  * `PROJECT_NUMBER`: The project number to which you have Service Usage Consumer role
  * `BILLING_ACCOUNT_ID`: ID of your Google Cloud billing account.



Sample output
    
    
    {
      "billingAccountLicenseConfigs": [{
        "name": "billingAccounts/BILLING_ACCOUNT_ID/billingAccountLicenseConfigs/BILLING_ACCOUNT_LICENSE_CONFIG_ID",
        "licenseCount": "2",
        "licenseConfigDistributions": {"projects/PROJECT_NUMBER/locations/global/licenseConfigs/LICENSE_CONFIG_ID": "1"
        },
        "subscriptionName": "subscriptions/SUBSCRIPTION_NAME",
        "subscriptionTier": "SUBSCRIPTION_TIER",
        "subscriptionTerm": "SUBSCRIPTION_TERM",
        "startDate": ...,
        "endDate": ...,
        "state": "ACTIVE",
        "procurementEntitlementId": "...",
        "subscriptionDisplayName": "...",
        "geminiBundle": true
      }]
    }
    

### Update subscription settings

After you create a subscription, you can update the settings, such as the license count or the auto-renewal setting.

The method for adding more licenses depends on how you originally purchased your subscription:

  * If you purchased your subscription through the Google Cloud console, add more licenses directly within the Google Cloud console using the steps in this section.
  * If you purchased using an offline order form, you must update the order form with the new license count. Contact your Google account manager to update the order form.



**Note:** When updating your subscription seat count in the Google Cloud console, maximum seat limits apply based on your billing account type (up to **25 seats** for self-serve (or online) and resold billing accounts, and up to **1,000 seats** for invoiced (or offline) billing accounts). For more information, see Subscription seat quantity limits.

If your existing subscription exceeds these thresholds (for example, if it was initially provisioned through a sales-led offline order), attempting to add more licenses directly through the Google Cloud console might result in a seat limit error. Contact your Google Cloud sales representative or account manager to adjust your license count or request an allowlist exception.

Follow these steps to update the license count if you purchased through the Google Cloud console:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage subscriptions**.

  3. Click the subscription you want to update from the **Gemini Subscriptions** table.

  4. Click **Edit** next to **Subscription details**.

  5. Update the license count or turn on or turn off auto renewal.

  6. Click **Submit**.




### Cancel a subscription

To cancel a Gemini Enterprise subscription, you must turn off automatic renewal. Your subscription remains active until the subscription term ends, and you might incur charges until that date. To learn more about your subscription, see View subscription details.

To cancel your subscription, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage subscriptions**.

  3. In the **Gemini Subscriptions** table, click the name of your subscription to open the subscription details page.

  4. Click **Edit**.

  5. In the **Edit subscription** panel, clear the **Auto renew subscription** checkbox.

  6. Click **Submit**.




### Distribute licenses

If you haven't distributed the subscribed licenses to a project, which might happen when you purchase the subscription offline or when the license distribution failed previously, do the following:

### Console

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage subscriptions**.

  3. Select the **Billing account** from the drop-down.

  4. In the **Gemini Subscriptions** table, click the name of your subscription.

  5. Click **Distribute License** at the top of the page. A list appears, displaying existing license distributions and statistics of remaining and total seats.

  6. To distribute licenses to a project:

     1. Click the project selector to select a project. The selector supports autocompletion.
     2. Note: If you haven't enabled the Discovery Engine API for the selected project, a dialog appears prompting you to enable it.
     3. Select a **Location**.
     4. Enter the number of licenses to allocate.
     5. Repeat these steps if you want to distribute licenses to multiple projects or locations.
  7. Click **Submit**.

  8. In the confirmation dialog, review the summary of changes and click **Confirm**.




### REST

To distribute licenses to a project or multiple projects, run the following command:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_NUMBER" \
      -d '{
        "projectNumber": "TARGET_PROJECT_NUMBER",
        "location": "LOCATION",
        "licenseCount": LICENSE_COUNT,
        "licenseConfigId": "LICENSE_CONFIG_ID"
      }' \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/billingAccounts/BILLING_ACCOUNT_ID/billingAccountLicenseConfigs/BILLING_ACCOUNT_LICENSE_CONFIG_ID:distributeLicenseConfig"
    

Replace the following:

  * `PROJECT_NUMBER`: the project number to which you have Service Usage Consumer role
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`.
  * `TARGET_PROJECT_NUMBER`: the project number you want to distribute licenses to.
  * `LICENSE_COUNT`: the number of licenses to distribute.
  * `BILLING_ACCOUNT_ID`: ID of your Google Cloud billing account.
  * `BILLING_ACCOUNT_LICENSE_CONFIG_ID`: locate the Billing Account License Config ID within the subscription detail.
  * _Optional_ `LICENSE_CONFIG_ID`: the ID of an existing project-level license configuration. You can find this ID in the `licenseConfigDistributions` field when you view subscription details.

**Note:** If you omit the `LICENSE_CONFIG_ID` from this API request, a new license configuration is created for the specified project number and location. To update an existing license configuration, you must include the `LICENSE_CONFIG_ID`.



### Reclaim unassigned licenses in a subscription

This section describes how to reclaim unassigned licenses from a project, making them available in the billing account for redistribution to other projects.

### Console

**Note:** You can only perform this action once per calendar day.

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage subscriptions**.

  3. Select the **Billing account** from the drop-down.

  4. In the **Gemini Subscriptions** table, click the name of your subscription.

  5. Click **Distribute License** at the top of the page (this button opens the management form for all allocations).

  6. In the list of allocations, locate the row for the project and location you want to reclaim licenses from.

  7. Choose one of the following actions:

     * To reduce the number of licenses: Decrease the count in the license input field.
     * To fully reclaim licenses: Move the pointer over the row to reveal the delete button, and then click **Delete**.
  8. Click **Submit**.

  9. In the confirmation dialog, review the summary of changes (which will list any reclaimed licenses) and click **Confirm**.




### REST

**Note:** You can only perform this action once per day.

To transfer subscription licenses back to the billing account for re-distribution, run the following command:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_NUMBER" \
      -d '{
        "licenseConfig": "projects/TARGET_PROJECT_NUMBER/locations/LOCATION/licenseConfigs/LICENSE_CONFIG_ID",
        "licenseCount": LICENSE_COUNT
      }' \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/billingAccounts/BILLING_ACCOUNT_ID/billingAccountLicenseConfigs/BILLING_ACCOUNT_LICENSE_CONFIG_ID:retractLicenseConfig"
    

Replace the following:

  * `PROJECT_NUMBER`: the project number to which you have Service Usage Consumer role
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`.
  * `TARGET_PROJECT_NUMBER`: the project number you want to reclaim licenses from.
  * `LICENSE_COUNT`: the number of licenses to reclaim.
  * `BILLING_ACCOUNT_ID`: ID of your Google Cloud billing account.
  * `BILLING_ACCOUNT_LICENSE_CONFIG_ID`: locate the Billing Account License Config ID within the subscription detail.
  * `LICENSE_CONFIG_ID`: the license config ID of an existing project-level license config. 



### Handle early termination

When you migrate between different subscription types or if there's an issue with your billing account, a subscription might end earlier than planned.

To ensure a smoother transition and prevent service interruptions, we provide a one-week (seven days) grace period where affected licenses are in a deactivating state before they fully expire. During this grace period, you can continue to use the service while you transition to a new subscription.

To ensure your users retain access, transfer their licenses to a new, active subscription either automatically or manually.

The following image shows an example of a deactivating license in the Google Cloud console:

![An example of a deactivating license in the Google Cloud console](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/license/deactivating-license.png)

## Manage user licenses

This section describes how to view licenses, export user data, and assign, transfer, and remove licenses for individual users.

### View licenses

To view the licenses and the users assigned to them, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage users**.

  3. Select the **Multi-region** of the existing license.




### Export user data

The users table in the Google Cloud console does not support sorting or filtering. If you need to sort, filter, or analyze your user data, you can export up to 1,000,000 user records to a comma-separated values (CSV) file.

The exported CSV file includes the following columns.

Column name | Description  
---|---  
`user_principal` | The email address of the user.  
`license_config` |  The full Google Cloud resource name for the user's assigned subscription (for example, `projects/PROJECT_NUMBER/locations/LOCATION/licenseConfigs/LICENSE_CONFIG_ID`). The license config ID corresponds to the Gemini Enterprise edition (for example, Standard or Plus) assigned to the user.   
`assignment_time` | The timestamp (in UTC) when an administrator assigned the license.  
`last_login_time` | The timestamp (in UTC) when the user last signed in.  
`license_assignment_state` |  The license assignment state. The following values are available: 

  * `ASSIGNED`: The user has an assigned license. 
  * `NO_LICENSE`: The user does not have a license because an administrator hasn't assigned one or has removed an existing license. 
  * `BLOCKED`: A policy or administrator blocks the user from receiving a license. 

  
  
To export user data to a CSV file, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** > **Manage users** page.

[Manage users](https://console.cloud.google.com/gemini-enterprise/user-license)

  2. Select the **Multi-region** of the existing license.

  3. In the **Users** section, click **Export all users**.

Depending on the size of the users table, the export process might take up to 2.5 minutes to complete. During this time, the console displays a loading state. When the export finishes, your browser downloads the CSV file to its default download location.




#### Troubleshoot export issues

The following table lists common issues when exporting user data and their resolutions.

Issue | Resolution  
---|---  
The **Export all users** button is hidden  |  Make sure that there are users assigned to licenses in the selected multi-region. If there are no assigned users, the **Export all users** button does not appear.   
The export request fails with a limit-exceeded error  |  If your user list exceeds the export limit of 1,000,000 users, the Google Cloud console rejects the export request and displays a limit-exceeded error message.   
The export request fails with a permission denied error  |  Make sure that your account has the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role, which includes the required `discoveryengine.userStores.listUserLicenses` permission.   
  
### Assign licenses to users

This section explains how to automatically or manually assign licenses to new users. You can assign a license to a new user at any time and, after a license is assigned, the user can access Gemini Enterprise immediately.

#### Add users and assign them licenses automatically

To assign licenses to users automatically when they sign in to the Gemini Enterprise app, do the following:

**Note:** Ensure your subscription has enough licenses for the maximum number of users who are expected to use Gemini Enterprise.

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage users**.

  3. Select the **Multi-region** of the existing license.

  4. Select **Assign licenses automatically** and then select the subscription.

Each time a user without a manually-assigned license signs in, Gemini Enterprise automatically assigns them a license from this subscription. If no licenses remain in the subscription, Gemini Enterprise shows users a message notifying them that they don't have access.

For more information about subscriptions, see the About subscriptions section.




#### Add users and manually assign them licenses

To give specific users access to Gemini Enterprise, you can manually assign them licenses from an active subscription.

### Console

To manually assign licenses to users, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/start)

  2. Click **Manage users**.

  3. Select the **Multi-region** of the existing license.

  4. Click **Add users**.

  5. On the **Add users** page:

     1. Enter the email addresses of the users. Make sure to use the same email address that they'll use to sign in to the Gemini Enterprise app.

     2. Select the subscription to assign to those users.

     3. Click **Submit**.




### REST

To manually assign licenses to users, run the following command:

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/userStores/default_user_store:batchUpdateUserLicenses" \
      -d '{
       "inlineSource":{
          "userLicenses":[
             {
                "userPrincipal":"USER_EMAIL_1",
                "licenseConfig":"projects/PROJECT_NUMBER/locations/LOCATION/licenseConfigs/SUBSCRIPTION_ID"
             },
             {
                "userPrincipal":"USER_EMAIL_2",
                "licenseConfig":"projects/PROJECT_NUMBER/locations/LOCATION/licenseConfigs/SUBSCRIPTION_ID"
             }
          ],
          "updateMask": "userPrincipal,licenseConfig"
       },
       "deleteUnassignedUserLicenses":false
      }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us` or `eu`
  * `USER_EMAIL`: the email address of the user you want to add to the license.
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `SUBSCRIPTION_ID`: the ID of your Gemini Enterprise subscription.



### Transfer licenses from expired subscriptions

Users can't sign in to Gemini Enterprise if the subscription has expired. There are a couple of approaches to returning sign-in access to them:

  * Automatically transfer existing users with expired licenses to the default subscription.

  * Manually transfer existing users to a new subscription.


**Note:** If you previously blocked a user from accessing a license, Gemini Enterprise grants them access within 30 minutes after you assign the new license.

#### Automatically transfer users to an active subscription

To automatically transfer users to an active subscription, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Manage users** page.

[Gemini Enterprise License](https://console.cloud.google.com/gemini-enterprise/user-license)

  2. Select the **Multi-region** of the existing license.

  3. Make sure that you have an active subscription. If you don't have one, get a subscription.

  4. Select **Assign licenses automatically** and choose the active subscription.

  5. Select **Automatically update expired license**.

When a user with an expired license next signs in, Gemini Enterprise automatically grants them a license in the chosen subscription.




#### Manually transfer users to an active subscription

To manually transfer users to an active subscription, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Manage users** page.

[Gemini Enterprise License](https://console.cloud.google.com/gemini-enterprise/user-license)

  2. Select the **Multi-region** of the existing license.

  3. Make sure that you have an active subscription. If you don't have one, get a subscription.

  4. Select the users and click **Assign different license**.

  5. In the **Edit Users** pane, select the subscription and click **Submit**.




### List the licenses

To list the licenses and the users assigned to them, run the following command:

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/userStores/default_user_store/userLicenses"
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us` or `eu`



### Remove users from a license

You can remove a license from a user at any time. When a license is removed, the user immediately loses access to Gemini Enterprise. To remove users from a license, do the following:

### Console

To remove users from a license using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Manage users** page.

[Gemini Enterprise License](https://console.cloud.google.com/gemini-enterprise/user-license)

  2. Select the **Multi-region** of the existing license.

  3. In the users table, select the users.

  4. To remove users from a license, choose one of the following:

     * To only remove the license from the selected users, click **Unassign license**.
     * To remove the license and also delete the selected users from the project, click **Unassign and delete license**.
  5. Click **Confirm**.




### REST

To remove users from a license, run the following command:

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/userStores/default_user_store:batchUpdateUserLicenses" \
      -d '{
       "inlineSource":{
          "userLicenses":[
             {
                "userPrincipal":"USER_EMAIL_1"
             },
             {
                "userPrincipal":"USER_EMAIL_2"
             }
          ],
          "updateMask": "userPrincipal,licenseConfig"
       },
       "deleteUnassignedUserLicenses":true
      }'
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us` or `eu`
  * `USER_EMAIL`: the email address of the user you want to remove from the license.



## What's next

  * Learn more about the [Frequently asked questions about Gemini Enterprise licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses-faqs).
  * Learn about [IAM roles and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
