---
url: https://docs.cloud.google.com/architecture/identity/integrating-google-services-and-apps-with-azure-ad-portal/
title: Microsoft My Apps portal integration \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:19.570668+00:00
---

# Microsoft My Apps portal integration  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/integrating-google-services-and-apps-with-azure-ad-portal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Microsoft My Apps portal integration Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-07-30 UTC

This document shows how to add Google services and Identity-Aware Proxy (IAP) web-secured web applications to the Microsoft My Apps portal and how to enable automatic sign-on for these applications.

The document assumes that you have federated your Cloud Identity or Google Workspace account with Microsoft Entra ID by [configuring Microsoft Entra ID for single sign-on](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configuring_azure_ad_for_single_sign-on).

## Before you begin

Make sure you've completed the steps to [federate your Cloud Identity or Google Workspace account with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configuring_azure_ad_for_single_sign-on).

## Initiate single sign-on from a portal

To support authenticating with an external identity provider (IdP) like Microsoft Entra ID, Cloud Identity and Google Workspace rely on service provider–initiated sign-on. With this type of sign-on, authentication starts at the service provider, which then redirects you to the IdP—for example:

  1. You access a Google service such as the [Google Cloud console](https://console.cloud.google.com/) or [Data Studio](https://lookerstudio.google.com) by opening a URL or bookmark. Google and its services take the role as the service provider in this scenario.
  2. The Google Sign-in screen appears, prompting you to enter the email address of your Google identity.
  3. You're redirected to Microsoft Entra ID, which serves as the IdP.
  4. You sign in to Microsoft Entra ID.
  5. Microsoft Entra ID redirects you back to the Google service that you originally attempted to access.



A benefit of service provider–initiated sign-on is that users can directly access Google services by opening a link or using a bookmark. If your organization uses Microsoft Entra ID, then you can use the Microsoft My Apps portal for this purpose. Not being forced to open applications through a portal is convenient for power users who bookmark specific sites or might memorize certain URLs. For other users, it can still be valuable to expose the links to relevant applications in a portal.

However, adding a link such as <https://lookerstudio.google.com> to the Microsoft My Apps portal reveals a shortcoming of the service provider–initiated sign-on process. Although a user that clicks the link in the portal has a valid Microsoft Entra ID session, they might still see the Google Sign-in screen and are prompted to enter their email address. This seemingly redundant sign-in prompt is a result of Google Sign-In not being made aware of the existing Microsoft Entra ID session.

You can avoid the additional Google Sign-in prompt by using special URLs when configuring the Microsoft My Apps portal. These URLs embed a hint about which Cloud Identity or Google Workspace account users are expected to use. The extra information enables authentication to be performed silently, resulting in an improved user experience.

### Add links to the Microsoft My Apps portal

The following table lists common Google services, the corresponding name in Microsoft Entra ID, and the link that you can use to implement SSO as outlined in the previous section.

Google service | URL | Logo  
---|---|---  
Gemini Enterprise | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://vertexaisearch.cloud.google.com/home/cid/ID` | ![Gemini](https://docs.cloud.google.com/static/architecture/identity/images/logo-gemini.png)  
Google Cloud console | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://console.cloud.google.com/` | ![Google Cloud logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-cloud.png)  
Google Docs | `https://docs.google.com/a/DOMAIN` | ![Google Docs logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-docs.png)  
Google Sheets | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://sheets.google.com/` | ![Google Sheets logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-sheets.png)  
Google Sites | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://slides.google.com/` | ![Google Sites logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-slides.png)  
Google Drive | `https://drive.google.com/a/DOMAIN` | ![Google Drive logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-drive.png)  
Gmail | `https://mail.google.com/a/DOMAIN` | ![Gmail logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-gmail.png)  
Google Groups | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://groups.google.com/` | ![Google Groups logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-groups.png)  
Google Keep | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://keep.google.com/` | ![Google Keep logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-keep.png)  
Data Studio | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://lookerstudio.google.com/` | ![Data Studio logo](https://docs.cloud.google.com/static/architecture/identity/images/logo-looker.png)  
YouTube | `https://www.google.com/a/DOMAIN/ServiceLogin?continue=https://www.youtube.com/` | ![YouTube logo](https://www.gstatic.com/images/branding/productlogos/youtube/v9/web-96dp/logo_youtube_color_1x_web_96dp.png)  
  
For each Google service that you want to add to the Microsoft My Apps portal, create a new enterprise application:

  1. In the [Azure portal](https://portal.azure.com/), go to **Microsoft Entra ID** > **Enterprise applications**.
  2. Click **New application**.
  3. Click **Create your own application** and enter the following:

     * **What's the name of your app** : Enter the name of the Google service as indicated in the preceding table.
     * **What are you looking to do with your application** : Select **Integrate any other application you don't find in the gallery (Non-gallery)**.
  4. Click **Create**.

  5. Select **Properties**.

  6. Change the logo to the file linked in the table.

  7. Click **Save**.

  8. In the menu on the left, select **Single sign-on**.

  9. Select **Linked**.

  10. Enter the URL listed in the table—for example, `http://docs.google.com/a/DOMAIN`.

Replace `DOMAIN` with the primary domain name of your Cloud Identity or Google Workspace account such as `example.com`.

  11. Click **Save**.




Notice that you don't have to configure SAML-based SSO in the application. All single sign-on operations continue to be handled by [the application that you previously created for single sign-on.](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configuring_azure_ad_for_single_sign-on)

To assign the application to users, do the following:

  1. In the menu on the left, select **Properties**.
  2. Set **User assignment required** to **Yes**.
  3. Click **Save**.
  4. In the menu on the left, click **Manage > Users and groups**.
  5. Click **Add user**.
  6. Select **Users**.
  7. Select the users or groups that you want to provision. If you select a group, all members of the group are provisioned.
  8. Click **Select**.
  9. Click **Assign**.



It might take several minutes for a link to show up in the My Apps portal.

### Control access

Assigning users and groups to individual applications in Microsoft Entra ID controls the visibility of the link, but it doesn't control access to a service. A service that isn't visible on a user's My Apps portal might still be accessible if the user opens the right URL. To control which users and groups are allowed to access a service, you must also [turn the service on or off](https://support.google.com/a/answer/182442) in the Google [Admin Console](http://admin.google.com/).

You can simplify the process of controlling visibility and access by using groups:

  1. For each Google service, create a security group in Microsoft Entra ID—for example, `Data Studio users` and `Google Drive users`.
  2. Assign the groups to the appropriate Microsoft Entra ID enterprise application as outlined in the previous section. For example, assign `Data Studio users` to the **Data Studio** application and `Google Drive users` to the **Google Drive** application.
  3. [Configure the groups to be provisioned](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configure_group_provisioning) to your Cloud Identity or Google Workspace account.
  4. In the [Admin Console](http://admin.google.com/), [turn on the respective service for each group](https://support.google.com/a/answer/9050643#top&step4&step5&step6). For example, turn on **Data Studio** for the `Data Studio users` group and **Google Drive** for the `Google Drive users` group. Turn the service off for everybody else.



By adding and removing members to these groups, you now control both access and visibility in a single step.

## IAP-protected web applications

If you're using [IAP](https://docs.cloud.google.com/iap) to protect your web applications, you can add links to these applications to the Microsoft My Apps portal and enable a single sign-on experience for them.

### Add links to the Microsoft My Apps portal

The process for adding a link to the Microsoft My Apps portal is the same as for Google services, but you must use the URL of your IAP-protected web application.

As you can with Google services, you can prevent users from seeing a Google sign-in screen after following a link to a IAP-protected web application in the portal, but the process is different. Instead of using a special URL, you configure IAP to [always use a specific Cloud Identity or Google Workspace account for authentication](https://docs.cloud.google.com/iap/docs/customizing#authenticating_using_a_domain):

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Initialize an environment variable:

`PRIMARY_DOMAIN=primary-domain`

Replace `primary-domain` with the [primary domain](https://support.google.com/a/answer/182080) of your Cloud Identity or Google Workspace account—for example, `example.com`.

  3. Create a temporary settings file that instructs IAP to always use the primary domain of your Cloud Identity or Google Workspace account for authentication:
         
         cat << EOF > iap-settings.yaml
         accessSettings:
           oauthSettings:
             loginHint: "$PRIMARY_DOMAIN"
         EOF
         

  4. Apply the setting to all IAP web resources in the project:
         
         gcloud iap settings set iap-settings.yaml --resource-type=iap_web

  5. Remove the temporary settings file:
         
         rm iap-settings.yaml


**Note:** Configuring IAP to always use the primary domain of your Cloud Identity or Google Workspace account for authentication might prevent users from other Cloud Identity or Google Workspace accounts from being able to access the application.

### Control access

Assigning users and groups to individual applications in Microsoft Entra ID controls the visibility of the link to your IAP-protected web application, but does not control access to the application. To control access, you also have to [customize the Identity and Access Management (IAM) policy](https://docs.cloud.google.com/iap/docs/managing-access#managing_access_console) of the IAP-protected web application.

As with Google services, you can simplify the process of controlling visibility and access by using groups:

  1. For each application, create a security group in Microsoft Entra ID—for example, `Payroll application users`.
  2. Assign the group to the respective Microsoft Entra ID enterprise application.
  3. [Configure the group to be provisioned](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-ad-configuring-provisioning-and-single-sign-on#configure_group_provisioning) to your Cloud Identity or Google Workspace account.
  4. [Update the IAM policy](https://docs.cloud.google.com/iap/docs/managing-access#managing_access_console) of the IAP-protected web application to grant the **IAP-Secured Web App User** role to the `Payroll application users` group while disallowing access for other users



By adding and removing members to the `Payroll application users` group, you control both access and visibility in a single step.

## What's next

  * Learn more about [federating Google Cloud with Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory).
  * Read about [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and [best practices for federating Google Cloud with an external IdP](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * Read more about [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs).



## Contributors

Author: [Johannes Passing](https://www.linkedin.com/in/johannespassing) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
