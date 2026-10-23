---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users/
title: Managing users \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:37.925136+00:00
---

# Managing users  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing users Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Manage portal users, as described in the following sections. See also [ Creating a user account on the integrated portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#register).

After a developer creates an app on the integrated portal, as described in [ Register apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#register-apps), the user account information is synced to and available on Apigee on the [ Developers page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product#ui). The app developer record is associated with the user using the developer's email address. For more information about where user account and associated app information is stored, see [ Where user account information is stored](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#apidev-info-stored).

## Exploring the Users page

To access the Users page:

  1. Display the list of portals:

In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click the row of the portal for which you want to view users.

  3. Click **Accounts**.

  4. Click the **Users** tab.




A list of users is displayed.

The Users list lets you:

  * View details for all user accounts, including name, email, activation status, and date registered
  * If you have [ enrolled in the Preview release of the teams feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#enroll), view the teams of which each portal user is a member (see [Sharing responsibility for an app using teams (Preview)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#teams))
  * View user account details
  * Activate a user account that requires manual activation or has been deactivated
  * Deactivate a user account
  * Delete a user account



## Viewing user account details

To view user account details:

  1. Access the Users page.
  2. Click the row of the user for which you want to view account details.



The **User accounts details** page is displayed.

The User account details page lets you:

  * View user account name, email, and activation status
  * Activate or deactivate a user account
  * View custom registration fields (see [Adding custom registration fields to the account creation page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#add_custom_registration_fields_to_the_account_creation_page)
  * View apps created by the portal user (see [Registering developer apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#register-developer-apps))



If you have [ enrolled in the Preview release of the teams feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#enroll), the Account details page lets you perform the following additional tasks:

  * View teams that the portal user is a member of and related details (see [Sharing responsibility for an app using developer teams (Preview)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#teams))
  * Manage audiences associated with the portal user (see [Managing the audience for your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#manage-audience))



## Activating or enabling user accounts

You may need to manually activate or enable a user account in the following scenarios:

  * Your portal is configured to require manual activation for each user account, as described in [Configure manual activation of user accounts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#manual-approval).
  * A user account has been deactivated and you want to activate it.



In either scenario, the status for the user account is listed in the user accounts list.

**Note:** You may receive an email notification alerting you to the pending account activation, if configured. See [ Configure manual activation of user accounts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#manual-approval).

To activate a user account from the User details page:

  1. Access the Users page.
  2. Click the row of the user account that you want to activate.
  3. Activate or enable the user account. 
     1. Click edit **Edit**.
     2. Change the **Status** from do_not_disturb_on **Disabled** to check_circle **Enabled**.
     3. Click **Save**.



## Deactivating or disabling user accounts

There may be times when you need to prevent a user account from accessing the integrated portal, either temporarily or permanently. In this case, the status for the user account is listed in the Users list and the portal user cannot sign in.

To deactivate or disable a user account from the User details page:

  1. Access the Users page.
  2. Click the row of the user account that you want to deactivate.
  3. Deactivate or disable the user account. 
     1. Click edit **Edit**.
     2. Change the **Status** from check_circle **Enabled** to do_not_disturb_on **Disabled**.
     3. Click **Save**.



## Deleting user accounts

You can delete a user account that is no longer needed.

When you delete a user account: 

  * All apps and API keys owned by the portal user will be deleted.
  * If you have [ enrolled in the Preview release of the teams feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/developer-teams#enroll), then all teams and team apps for which the portal user is the only owner are deleted.
  * The user account information that is stored on Apigee on the [ Developers page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product#ui) **will not be deleted** when you delete a user account in the developer program.

**Best Practice:** To ensure a user and their associated developer record are fully removed from both the integrated portal and the Apigee platform, first delete the user account from the integrated portal. Wait a short period (e.g., a few minutes) to allow for synchronization. Then, delete the corresponding developer from the Apigee platform. Attempting to delete the developer from Apigee before deleting from the portal may result in the developer being automatically re-created.

To delete a user account:

  1. Access the Users page.
  2. Delete the user account.

For the user account that you want to delete, click delete **Delete**.

  3. Click **Delete** at the prompt to confirm the operation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
