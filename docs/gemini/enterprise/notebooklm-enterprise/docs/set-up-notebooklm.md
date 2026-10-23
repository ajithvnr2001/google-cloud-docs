---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm/
title: Set up Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:16.626213+00:00
---

# Set up Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)



Send feedback 

#  Set up Gemini Notebook Enterprise Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the start-up tasks that you must complete to set up Gemini Notebook Enterprise.

After you have performed the tasks on this page, your users can start creating and using notebooks in Gemini Notebook Enterprise.

## About identity setup

To complete the setup, you must have your organization's identity provider (IdP) configured in Google Cloud. Correct setup for identity is important for two reasons:

  * It lets your users use their current corporate credentials to access the Gemini Notebook Enterprise user interface.

  * It ensures that users see only the notebooks which they own or which have been shared with them.




### Supported frameworks

The following authentication frameworks are supported:

  * Cloud Identity:

    * Case 1: If you use Cloud Identity or Google Workspace, then all user identities and user groups are present and managed through Google Cloud. For more information about Cloud Identity, see the [Cloud Identity](https://docs.cloud.google.com/identity/docs) documentation.

    * Case 2: You use a third-party IdP, and you have synced identities with Cloud Identity. Your end users use Cloud Identity to authenticate before accessing Google resources or Google Workspace.

    * Case 3: You use a third-party IdP, and you have synced identities with Cloud Identity. However, you are still using your existing third-party IdP to perform the authentication. You have configured SSO with Cloud Identity such that your users begin their sign in using Cloud Identity and then get directed to your third-party IdP. (You might have already done this sync when setting up other Google Cloud resources or Google Workspace.)

  * Workforce Identity Federation: If you use an external identity provider (Microsoft Entra ID, Okta, Ping, PingFederate, or another OIDC or SAML 2.0 IdP), but don't want to sync your identities into Cloud Identity, then you must set up [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) in Google Cloud before you can turn on data source access control for Gemini Notebook Enterprise.

The `google.subject` attribute must map to the email address field in the external IdP. The following are example `google.subject` and `google.groups` attribute mappings for commonly used IdPs:

    * Microsoft Entra ID

      * [Microsoft Entra ID with OIDC protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id#create-oidc-provider)
            
            google.subject=assertion.email
            google.groups=assertion.groups
            

      * [Microsoft Entra ID with SAML protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id#create-saml-provider)
            
            google.subject=assertion.attributes['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name'][0]
            google.groups=assertion.attributes['http://schemas.microsoft.com/ws/2008/06/identity/claims/groups']
            

      * [Microsoft Entra ID with a large number of groups](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups)

If you use Microsoft Entra ID and have more than approximately 150 groups, then you should follow the setup procedures for a large number of groups.
            
            google.subject=user.emails[0].value.lowerAscii()
            google.groups=group.externalId
            

**Note:** If you use [System for Cross-domain Identity Management (SCIM)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim) (or extended attributes), the `google.groups` attribute mapping is ignored.
    * Okta

      * [Okta with OIDC protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#create-oidc-provider)
            
            google.subject=assertion.email
            google.groups=assertion.groups
            

      * [Okta with SAML protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#create-saml-provider)
            
            google.subject=assertion.subject
            google.groups=assertion.attributes['groups']
            




You can select only one IdP per Google Cloud project.

### Before you begin

Before starting the procedures on this page, make sure that one of the following is true:

  * You use Cloud Identity as your IdP, or

  * You use a third-party IdP and have configured SSO with Cloud Identity, or

  * You use a third-party IdP that is not Okta and have:

    * Set up [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) by following the instructions in [Configure Workforce Identity Federation with Microsoft Entra ID and sign in users](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id) or, if you have more than approximately 150 groups, in [Configure Workforce Identity Federation with Microsoft Entra ID with a large number of groups](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups).

If you follow the [Configure Workforce Identity Federation with Microsoft Entra ID and sign in users](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id) instructions, make sure to do the recommended security best practice steps to [add a group claim](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id#create_a_microsoft_entra_id_application) and select **All groups**. This is a required step for Gemini Notebook Enterprise.

    * Set up SCIM. See [Configure SCIM in Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/configure-scim-ms-entra). SCIM is necessary for [autocomplete of user emails and group names](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks#autocomplete) and for [Microsoft Entra ID with a large number of groups](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups).

  * You use Okta as your third-party IdP and have:

    * Followed the instructions in [Configure Workforce Identity Federation with Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta).

    * Set up SCIM. See [Configure SCIM in Okta](https://docs.cloud.google.com/iam/docs/configure-scim-okta). SCIM is necessary for [autocomplete of user emails and group names](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks#autocomplete).




## Create a project and enable the API

If you already have a Google Cloud project that you want to use, start at step 2.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Discovery Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Discovery Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com)




## Grant the Cloud NotebookLM Admin role

As the project owner, you need to assign the Cloud NotebookLM Admin role to any users who you want to be able to administer Gemini Notebook Enterprise in this project:

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter the user identifier. This is typically the email address for a Google Account or a user group. 

  5. In the **Select a role** list, select **Cloud NotebookLM Admin**. For more information, see [User roles](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#user_roles). 
  6. Click **Save**. 



## Set the IdP for Gemini Notebook Enterprise

The project owner or a user who has the Cloud NotebookLM Admin role can set up the IdP.

  1. In the Google Cloud console, go to the **Gemini Notebook Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/notebooklm)

  2. Set **Identity settings** to **Google identity provider** or **Third-party identity provider**.

For more information, see About identity setup above.

  3. If you are using a third-party IdP and Workforce Identity Federation, then specify the name of your workforce pool and your **Workforce pool provider**.

  4. Copy the **Link**.

You will send out this link to all the end-users of Gemini Notebook Enterprise. This is the link to the user interface that they'll use to create, edit, and share notebooks.




## Optional: Register customer-managed encryption keys

If you want to use customer-managed encryption keys (CMEK) instead of Google default encryption, then follow the instructions to register a key for Gemini Notebook Enterprise in [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/cmek).

Typically, you only need to use CMEK if your organization has strict regulatory requirements or internal policies that stipulate control over encryption keys. In most situations, Google default encryption is sufficient. For general information about CMEK, see the [Cloud Key Management Service documentation](https://docs.cloud.google.com/kms/docs/cmek).

**Important:** Register your key before your users start creating notebooks. Any notebooks created before the CMEK encryption is set up, won't be protected.

## Grant Gemini Notebook Enterprise roles to users

This section describes how to give your users the IAM roles that they need to access, manage, and share notebooks.

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=)
  2. Select the project. 
  3. Click person_add **Grant access**. 
  4. In the **New principals** field, enter the user identifier. This is typically the email address for a Google Account, a user group or the identifier for a user in a workforce identity pool. For details, see [ Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users), or contact your administrator. 

  5. In the **Select a role** list, select `Cloud NotebookLM User` role. 
  6. Click **Save**. 



In addition to the `Cloud NotebookLM User` role, users need a license for Gemini Notebook Enterprise. See [Get licenses for Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-licensing).

**Note:** The subscription page displays the previous name NotebookLM Enterprise.

## What's next

  * [Get licenses for Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-licensing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
