---
url: https://docs.cloud.google.com/iap/docs/enabling-app-engine/
title: Enabling IAP for App Engine \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:56.317646+00:00
---

# Enabling IAP for App Engine  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/enabling-app-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Enabling IAP for App Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to secure an App Engine instance with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview).

## Before you begin

To enable IAP for App Engine, do the following:

  1. Use a Google Cloud console project with billing enabled.

  2. Make sure that the project belongs to a Google Cloud organization if you want to use the default Google-managed OAuth client. If you don't have an organization, you can [create one](https://docs.cloud.google.com/organizations/docs/create-organization). To learn about the benefits of using a custom OAuth client, see [Configure custom OAuth clients for App Engine](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#app-engine). The Google-managed OAuth client only allows access to internal users.

**Important:** If your project doesn't belong to an organization or you want to allow access to users who are outside of your organization, you must [use a custom OAuth configuration](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#app-engine). Enabling IAP on a project without an organization or custom credentials causes requests to fail with an [`HTTP 502: Empty Google Account OAuth client ID(s)/secret(s)`](https://docs.cloud.google.com/iap/docs/faq#error-502) error. 
  3. Set up your App Engine instance, if you haven't already. For a complete walkthrough, see [Deploying to App Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-appengine).




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




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
