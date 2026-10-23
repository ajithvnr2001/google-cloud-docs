---
url: https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts/
title: Quickstart: Authenticate users with Google Accounts \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:43.598562+00:00
---

# Quickstart: Authenticate users with Google Accounts  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Authenticate users with Google Accounts

This quickstart shows you how to enable [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) to secure an App Engine standard or flexible environment application and grant access to users with Google Accounts.

If you plan to serve resources from a content delivery network (CDN), see the [caching best practices guide](https://docs.cloud.google.com/iap/docs/concepts-best-practices#caching) for important information.

When an App Engine application consists of multiple services, you can configure different IAP permissions across services, including making only some services [publicly accessible](https://docs.cloud.google.com/iap/docs/managing-access#public_access) while keeping others protected.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?tutorial=context_aware_access_secure_web_app)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. To enable IAP for App Engine, you need to set up the App Engine instance. If you don't have your App Engine instance set up already, see [Deploying to App Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine) for a complete walkthrough. 

By default, IAP uses a Google-managed OAuth client, which requires your project to belong to an organization and only allows access to internal users. 

**Important:** If your project does not belong to an organization or you want to allow access to users outside of your organization, you must [configure custom OAuth clients for App Engine](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#app-engine). Enabling IAP on a project without an organization or custom credentials causes requests to fail with an [`HTTP 502: Empty Google Account OAuth client ID(s)/secret(s)`](https://docs.cloud.google.com/iap/docs/faq#error-502) error. 



### Required roles

To get the permissions that you need to authenticate users with Google Accounts, ask your administrator to grant you the [IAP Policy Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.policyAdmin) (`roles/iap.policyAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable IAP

### Console

If your project does not belong to an organization, you must use custom OAuth credentials.

Dynamic include file

If you haven't configured your project's OAuth consent screen, you'll be prompted to do so. To configure your OAuth consent screen, see [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615).

### Setting up IAP access

  1. Go to the [Identity-Aware Proxy page](https://console.cloud.google.com/security/iap).   
[Go to the Identity-Aware Proxy page](https://console.cloud.google.com/security/iap)
  2. Select the project you want to secure with IAP.
  3. Select the checkbox next to the resource you want to grant access to. 
  4. On the right side panel, click **Add principal**. 
  5. In the **Add principals** dialog that appears, enter the email addresses of groups or individuals who should have the **IAP-secured Web App User** role for the project. 

The following kinds of principals can have this role:

     * **Google Account** : user@gmail.com 
     * **Google Group** : admins@googlegroups.com 
     * **Service account** : server@example.gserviceaccount.com 
     * **Google Workspace domain** : example.com 

Make sure to add a Google Account that you have access to.

  6. Select **Cloud IAP > IAP-secured Web App User** from the **Roles** drop-down list. 
  7. Click **Save**. 



### Turning on IAP

  1. On the **Identity-Aware Proxy** page, under **Applications** , find the application you want to restrict access to. To turn on IAP for a resource,  toggle the on/off switch in the **IAP** column.   

  2. In the **Turn on IAP** window that appears, click **Turn On** to confirm that you want IAP to secure your resource. After you turn on IAP, it requires login credentials for all connections to your load balancer. Only principals with the IAP-Secured Web App User (`roles/iap.httpsResourceAccessor`) role on the project will be given access. 



### gcloud

Before you set up your project and IAP, you need an up-to-date version of the gcloud CLI. For instructions on how to install the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads).

  1. To authenticate, use the Google Cloud CLI and run the following command. 
         
         gcloud auth login

  2. Click the URL that appears and sign in.
  3. After you sign in, copy the verification code that appears and paste it in the command line. 
  4. Run the following command to specify the project that contains the applications that you want to protect with IAP. 
         
         gcloud config set project PROJECT_ID

  5. To enable IAP, run the following command. 
         
         gcloud iap web enable --resource-type=app-engine --versions=version

  6. Add principals who should have the IAP-secured Web App user role to the project. 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
                --member=PRINCIPAL_IDENTIFIER \
                --role=roles/iap.httpsResourceAccessor

     * Replace PROJECT_ID with your project ID.
     * Replace PRINCIPAL_IDENTIFIER with the necessary principals. This can be a type of domain, group, serviceAccount, or user. For example, `user:myemail@example.com`.



After you enable IAP, you can use the gcloud CLI to modify the IAP access policy using the IAM role `roles/iap.httpsResourceAccessor`. Learn more about [managing roles and permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### API

  1. Run the following command to prepare a `settings.json` file. 
         
         cat << EOF > settings.json
         {
         "iap":
           {
             "enabled":true
           }
         }
         EOF
         

  2. Run the following command to enable IAP. 
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @settings.json \
         "https://appengine.googleapis.com/v1/apps/PROJECT_ID?updateMask=iap"
         




After you enable IAP, you can use the Google Cloud CLI to modify the IAP access policy using the IAM role `roles/iap.httpsResourceAccessor`. Learn more about [managing roles and permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You can enable IAP on a App Engine service within your project. To make some services publicly accessible and require authentication for others, you can use different access levels across services. To learn more, see [Manage access with IAP](https://docs.cloud.google.com/iap/docs/managing-access). To make services publicly accessible, grant the IAP-secured Web App User role to `allAuthenticatedUsers`.

**Role-based access:** Only principals with the IAP-secured Web App User (`roles/iap.httpsResourceAccessor`) role on this project are given access. Access to IAP-protected applications is not automatically granted, even to roles with extensive permissions, such as `Owner` or `Editor`. 

## Test user authentication

  1. After the role is granted, principals can access the app by authenticating with IAP. Access the app URL from a Google Account that was granted the IAP-secured Web App User (`roles/iap.httpsResourceAccessor`) role.

  2. To test access, open an Incognito window in Chrome, access the app URL, and sign in when prompted. Users who are granted the [IAP-secured Web App User (`roles/iap.httpsResourceAccessor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.httpsResourceAccessor) role and have successfully authenticated can access the app. Users who aren't granted the required role or fail to authenticate cannot access the app.




## What's next

  * Learn about how to [get the user's identity](https://docs.cloud.google.com/iap/docs/identity-howto) and develop your own [App Engine](https://docs.cloud.google.com/appengine) app.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
