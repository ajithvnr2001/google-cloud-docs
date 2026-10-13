---
url: https://docs.cloud.google.com/iap/docs/programmatic-oauth-clients/
title: Programmatically creating OAuth clients for IAP \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:56.122044+00:00
---

# Programmatically creating OAuth clients for IAP  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/programmatic-oauth-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)



Send feedback 

#  Programmatically creating OAuth clients for IAP Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** The IAP OAuth Admin API was shut down on March 19, 2026\. You can no longer create or manage OAuth brands or clients programmatically using this API. For migration instructions, see [Migrate from the IAP OAuth Admin API](https://docs.cloud.google.com/iap/docs/deprecations/migrate-oauth-client). To create and configure OAuth clients manually or with Terraform, see [Customize OAuth configuration](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration).

This page describes how to programmatically create OAuth clients for use with IAP, enabling you to set up IAP programmatically end-to-end for internal applications.

## Known limitations

There are a few limitations for OAuth clients created programmatically using this API:

  * OAuth clients created by the API can only be modified by using the API. You cannot modify an OAuth client via the Google Cloud console if it was created by using the API.
  * The OAuth clients created by the API are locked for IAP usage only, and therefore the API does not allow any updates to the redirect URI or other attributes.
  * The API does not operate on the OAuth clients that were created using the Google Cloud console.
  * Only 500 OAuth clients are allowed per project when using the API.
  * API-created OAuth consent screen brands have specific limitations. For more information, see Understanding brands and branding state.



## Understanding brands and branding state

The [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent), which contains branding information for users, is known as a **brand**. Brands can be limited to internal users or public users. An internal brand makes the OAuth flow accessible to someone who belongs to the same Google Workspace organization as the project. A public brand makes the OAuth flow available to anyone on the internet.

Brands can be created manually or programmatically through an API. API-created brands are automatically configured with different settings:

  * They're set to internal and must be manually set to public if selected

  * They're set to an "unreviewed" state and a brand review must be triggered




To manually set an internal brand to public:

  1. Open the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent).
  2. Select your selected project from the drop-down menu.
  3. On the **OAuth consent screen** page, note that the **User Type** is automatically set to **Internal**. To set it to **Public** , click **Edit App**. More configuration options become available.
  4. Under **Application type** , click **Public**.

**Note:** When an API-created internal brand is set to public, the [`identityAwareProxyClients.create()`](https://docs.cloud.google.com/iap/docs/reference/rest/v1/projects.brands.identityAwareProxyClients/create) API will stop working, as it requires the brand to be set to internal. Therefore, you cannot create new OAuth clients via the API after an internal brand is made public.

To trigger a brand review for an unreviewed API-created brand:

  1. Open the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent).
  2. Select your project from the drop-down menu.
  3. On the **OAuth consent screen** page, enter any required information, and then click **Submit for verification**.



The verification process may take up to several weeks, and you will receive email updates as it progresses. [Learn more](https://support.google.com/cloud/answer/9110914?hl=en) about verification. While the verification process is ongoing, you can still use the application within your Google Workspace organization. [Learn more](https://support.google.com/cloud/answer/7454865?hl=en_US) about how your application will behave before it's verified.

## Before you begin

Before you can create a client, first ensure that the caller has been granted the following permissions:

  * `clientauthconfig.brands.list`
  * `clientauthconfig.brands.create`
  * `clientauthconfig.brands.get`
  * `clientauthconfig.clients.create`
  * `clientauthconfig.clients.listWithSecrets` (Only required for listing OAuth clients with secret.)
  * `clientauthconfig.clients.getWithSecret`
  * `clientauthconfig.clients.delete`
  * `clientauthconfig.clients.update`



These permissions are included in the Editor (`roles/editor`) and Owner (`roles/owner`) [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic), however we recommend that you create a [custom role](https://docs.cloud.google.com/iam/docs/understanding-roles#custom_roles) that contains these permissions and grant it to the caller instead.

## Set up OAuth for IAP

The following steps describe how to configure the consent screen and create and oauth client for IAP.

### Configuring consent screen

  1. Check if you already have an existing brand by using the [list](https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/list) command. You may only have one brand per project.
         
         gcloud iap oauth-brands list

The following is an example gcloud response, if the brand exists:
         
         name: projects/[PROJECT_NUMBER]/brands/[BRAND_ID]
         applicationTitle: [APPLICATION_TITLE]
         supportEmail: [SUPPORT_EMAIL]
         orgInternalOnly: true
         

**Note:** If a brand already exists for a project and has been configured for external users (`orgInternalOnly: false`), but you want to restrict it to internal users, you must make that change manually from the [OAuth consent screen](https://console.cloud.google.com/auth/audience) in order to create OAuth clients with this API.
  2. If no brand exists, use the [create](https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-brands/create) command:
         
         gcloud iap oauth-brands create --application_title=APPLICATION_TITLE --support_email=SUPPORT_EMAIL

The above fields are required when calling this API:

     * `supportEmail`: The support email displayed on the OAuth consent screen. This email address can either be a user's address or a Google Groups alias. While service accounts also have an email address, they are not actual valid email addresses, and cannot be used when creating a brand. However, a service account can be the owner of a Google Group. Either create a new Google Group or configure an existing group and set the desired service account as an owner of the group.

**Note:** The user issuing the request must be an owner of the specified support email address.
     * `applicationTitle`: The application name displayed on OAuth consent screen.

The response contains the following fields:
    
    name: projects/[PROJECT_NUMBER]/brands/[BRAND_ID]
    applicationTitle: [APPLICATION_TITLE]
    supportEmail: [SUPPORT_EMAIL]
    orgInternalOnly: true
    




### Creating an IAP OAuth Client

  1. Use the create command to [create](https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-clients/create) a client. Use the brand `name` from previous step.
         
         gcloud iap oauth-clients create projects/PROJECT_NUMBER/brands/BRAND-ID --display_name=NAME

The response contains the following fields:
         
         name: projects/[PROJECT_NUMBER]/brands/[BRAND_NAME]/identityAwareProxyClients/[CLIENT_ID]
         secret: [CLIENT_SECRET]
         displayName: [NAME]
         




Use the client ID (`client_id` in the previous example) and `secret` to enable IAP. See the following topics for more information about enabling IAP using the credentials you've just created:

  * [IAP for GKE](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto)
  * [IAP for App Engine](https://docs.cloud.google.com/iap/docs/enabling-app-engine)
  * [IAP for Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto)
  * [IAP for Cloud Run](https://docs.cloud.google.com/iap/docs/enabling-cloud-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
