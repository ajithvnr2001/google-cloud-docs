---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control/
title: Set up data source access control \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:32.766589+00:00
---

# Set up data source access control  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Set up data source access control Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

This page describes how to enforce data source access control for search apps in Agent Search.

Access control for your data sources in Agent Search limits the data that users can view in your search app's results. Google uses your identity provider to identify the end user performing a search and determine if they have access to the documents that are returned as results.

For example, say that employees at your company search across Confluence documents using your search app. However, you need to make sure they can't view content through the app that they aren't allowed to access. If you have set up a workforce pool in Google Cloud for your organization's identity provider, then you can also specify that workforce pool in Agent Search. Now, if an employee uses your app, they get search results only for documents that their account already has access to in Confluence.

## About data source access control

Turning on access control is a one-time procedure.

Access control is available for Cloud Storage, BigQuery, Google Drive, and all third-party data sources.

To turn on data source access control for Agent Search, you must have your organization's identity provider configured in Google Cloud. The following authentication frameworks are supported:

  * Google Identity:

    * Case 1: If you use Google Identity, then all user identities and user groups are present and managed through Google Cloud. For more information about Google Identity, see the [Google Identity](https://developers.google.com/identity) documentation.

    * Case 2: You use a third-party identity provider, and you have synced identities with Google Identity. Your end users use Google Identity to authenticate before accessing Google resources or Google Workspace.

    * Case 3: You use a third-party identity provider, and you have synced identities with Google Identity. However, you are still using your existing third-party identity provider to perform the authentication. You have configured SSO with Google Identity such that your users begin their sign in using Google Identity and then get directed to your third-party identity provider. (You might have already done this sync when setting up other Google Cloud resources or Google Workspace.)

  * Third-party identity provider federation: If you use an external identity provider—for example, Microsoft Entra ID, Okta, or Ping, but don't want to sync your identities into Google Cloud Identity, then you must set up [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) in Google Cloud before you can turn on data source access control for Agent Search.

If you use [third-party connectors](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#connect_a_third-party_data_source), the `google.subject` attribute must map to the email address field in the external identity provider. The following are example `google.subject` and `google.groups` attribute mappings for commonly used identity providers:

    * [Microsoft Entra ID with OIDC protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id#create-oidc-provider)
          
          google.subject=assertion.email
          google.groups=assertion.groups
          

    * [Microsoft Entra ID with SAML protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id#create-saml-provider)
          
          google.subject=assertion.attributes['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name'][0]
          google.groups=assertion.attributes['http://schemas.microsoft.com/ws/2008/06/identity/claims/groups']
          

    * [Okta with OIDC protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#create-oidc-provider)
          
          google.subject=assertion.email
          google.groups=assertion.groups
          

    * [Okta with SAML protocol](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta#create-saml-provider)
          
          google.subject=assertion.subject
          google.groups=assertion.attributes['groups']
          




## Limitations

Access control has the following limitations:

  * 3000 readers are allowed per document. Each principal counts as a reader, where a principal can be a group or an individual user.
  * You can select one identity provider per Agent Search-supported location.
  * To set a data source as access-controlled, you must select this setting during data store creation. You can't turn this setting on or off for an existing data store.
  * The **Data** > **Documents** tab in the console doesn't show data for access-controlled data sources because this data should only be visible to users that have view access.
  * To preview UI results for search apps that use third-party access control, you must sign in to the federated console. See Preview results for access controlled apps.



## Before you begin

This procedure assumes you have set up an identity provider in your Google Cloud project.

  * **Google Identity** : If you use Google Identity, you can proceed to the Connect to your identity provider procedure.
  * **Third-party identity provider** : Make sure you have set up a workforce identity pool for your third-party identity provider. Verify that you have specified subject and group attribute mappings when setting up workforce pool. For information about attribute mappings, see [Attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings) in the IAM documentation. For more information about workforce identity pools, see [Manage workforce identity pool providers](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers) in the IAM documentation.



## Connect to your identity provider

To specify an identity provider for Agent Search and turn on data source access control, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. Go to the **Settings** > **Authentication** page.

  3. Click the edit icon  edit  for the location that you want to update.

  4. Select your identity provider in the **Add identity provider** dialog. If you select a third party identity provider, also select the workforce pool that applies for your data sources.

  5. Click **Save changes**.




## Configure a data source with access control

To apply access control to a data source, use the following steps depending on the kind of data source you're setting up:

  * Third-party data sources: No additional configuration is required when you create your app. Skip to Preview results for apps with third-party access control
  * Google Drive: No additional configuration is required when you create your app.
  * Unstructured data from Cloud Storage
  * Structured data from Cloud Storage
  * Unstructured data from BigQuery
  * Structured data from BigQuery



### Unstructured data from Cloud Storage

When setting up a data store for unstructured data from Cloud Storage, you need to also upload ACL metadata and set the data store as access controlled:

  1. When preparing your data, include ACL information in your metadata using the `acl_info` field. For example:
         
         {
            "id": "<your-id>",
            "jsonData": "<JSON string>",
            "content": {
              "mimeType": "<application/pdf or text/html>",
              "uri": "gs://<your-gcs-bucket>/directory/filename.pdf"
            },
            "acl_info": {
              "readers": [
                {
                  "principals": [
                    { "group_id": "group_1" },
                    { "user_id": "user_1" }
                  ]
                }
              ]
            }
          }
         

For more information about unstructured data with metadata, see the Unstructured data section of [Prepare data for ingesting](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#unstructured).

  2. When following the steps for data store creation in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es), you can enable access control by doing the following in either the console or using the API:

     * **Console** : When creating a data store, select **This data store contains access control information** during data store creation.
     * **API** : When creating data store, include the flag `"aclEnabled": "true"` in your JSON payload.
  3. When following the steps for data import in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es), make sure to do the following:

     * Upload your metadata with ACL information from the same bucket as your unstructured data
     * If using the API, set [`GcsSource.dataSchema`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/GcsSource) to `document`



### Structured data from Cloud Storage

When setting up a data store for structured data from Cloud Storage, you need to also upload ACL metadata and set the data store as access controlled:

  1. When preparing your data, include ACL information in your metadata using the `acl_info` field. For example:
         
         {
            "id": "<your-id>",
            "jsonData": "<JSON string>",
            "acl_info": {
              "readers": [
                {
                  "principals": [
                    { "group_id": "group_1" },
                    { "user_id": "user_1" }
                  ]
                }
              ]
            }
          }
         

  2. When following the steps for data store creation in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es), you can enable access control by doing the following in either the console or using the API:

     * **Console** : When creating a data store, select **This data store contains access control information** during data store creation.
     * **API** : When creating data store, include the flag `"aclEnabled": "true"` in your JSON payload.
  3. When following the steps for data import in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es), make sure to do the following:

     * Upload your metadata with ACL information from the same bucket as your unstructured data
     * If using the API, set [`GcsSource.dataSchema`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/GcsSource) to `document`



### Unstructured data from BigQuery

When setting up a data store for unstructured data from BigQuery, you need to set the data store as access controlled and provide ACL metadata using a predefined schema for Agent Search:

  1. When preparing your data, specify the following schema. Don't use a custom schema.
         
         [
           {
             "name": "id",
             "mode": "REQUIRED",
             "type": "STRING",
             "fields": []
           },
           {
             "name": "jsonData",
             "mode": "NULLABLE",
             "type": "STRING",
             "fields": []
           },
           {
             "name": "content",
             "type": "RECORD",
             "mode": "NULLABLE",
             "fields": [
               {
                 "name": "mimeType",
                 "type": "STRING",
                 "mode": "NULLABLE"
               },
               {
                 "name": "uri",
                 "type": "STRING",
                 "mode": "NULLABLE"
               }
             ]
           }
           {
             "name": "acl_info",
             "type": "RECORD",
             "mode": "NULLABLE",
             "fields": [
               {
                 "name": "readers",
                 "type": "RECORD",
                 "mode": "REPEATED",
                 "fields": [
                   {
                     "name": "principals",
                     "type": "RECORD",
                     "mode": "REPEATED",
                     "fields": [
                       {
                         "name": "user_id",
                         "type": "STRING",
                         "mode": "NULLABLE"
                       },
                       {
                         "name": "group_id",
                         "type": "STRING",
                         "mode": "NULLABLE"
                       }
                     ]
                   }
                 ]
               }
             ]
           }
         ]
         

  2. Include your ACL metadata as a column in your BigQuery table.

  3. When following the steps in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es), enable access control in either the console or using the API:

     * **Console** : When creating a data store, select **This data store contains access control information** during data store creation.
     * **API** : When creating data store, include the flag `"aclEnabled": "true"` in your JSON payload.
  4. When following the steps for data import in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es), if using the API, set [`BigQuerySource.dataSchema`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BigQuerySource) to `document`.




### Structured data from BigQuery

When setting up a data store for structured data from BigQuery, you need to set the data store as access controlled and provide ACL metadata using a predefined schema for Agent Search:

  1. When preparing your data, specify the following schema. Don't use a custom schema.
         
         [
           {
             "name": "id",
             "mode": "REQUIRED",
             "type": "STRING",
             "fields": []
           },
           {
             "name": "jsonData",
             "mode": "NULLABLE",
             "type": "STRING",
             "fields": []
           },
           {
             "name": "acl_info",
             "type": "RECORD",
             "mode": "NULLABLE",
             "fields": [
               {
                 "name": "readers",
                 "type": "RECORD",
                 "mode": "REPEATED",
                 "fields": [
                   {
                     "name": "principals",
                     "type": "RECORD",
                     "mode": "REPEATED",
                     "fields": [
                       {
                         "name": "user_id",
                         "type": "STRING",
                         "mode": "NULLABLE"
                       },
                       {
                         "name": "group_id",
                         "type": "STRING",
                         "mode": "NULLABLE"
                       }
                     ]
                   }
                 ]
               }
             ]
           }
         ]
         

  2. Include your ACL metadata as a column in your BigQuery table.

  3. When following the steps in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es), enable access control in either the console or using the API:

     * **Console** : When creating a data store, select **This data store contains access control information** during data store creation.
     * **API** : When creating data store, include the flag `"aclEnabled": "true"` in your JSON payload.
  4. When following the steps for data import in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es), make sure to do the following:

     * If using the console, then when specifying the kind of data you're uploading, select **JSONL for structured data with metadata**
     * If using the API, set [`BigQuerySource.dataSchema`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BigQuerySource) to `document`



## Preview results in the Workforce Identity Federation console

To preview results for apps with third-party access control in the Google Cloud console, you must sign in with your organization's credentials.

To preview UI results, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. Click the name of the search app whose results you want to preview.

  3. Go to the **Preview** page.

  4. Click **Preview with federated identity** to go to the Workforce Identity Federation console.

  5. Enter your workforce pool provider and organization's credentials.

  6. Preview results for your app on the **Preview** page that appears.

For more information about previewing your search results, see [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results).




For more information about the Workforce Identity Federation console, see [About the console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-learn-more).

## Grant search permissions to your users

**Caution:** Previously, Google recommended granting the Discovery Engine Viewer role. This role can grant broader permissions to features that users might not need to access. The Discovery Engine Viewer role is suitable for initial testing, but Google recommends that you use [custom Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) for production usage.

To give your users the ability to search access-controlled data using your app, you need to grant access to users in your domain or workforce pool. Google recommends that you grant a custom IAM role to your user group.

  * **Google Identity** : If you use Google Identity, then Google recommends that you create a [Google group](https://groups.google.com) that includes all employees that need to search. If you're a Google Workspace administrator, you can include all users in an organization in a Google group by following the steps in [Add all your organization's users to a group](https://support.google.com/a/answer/9689259).
  * **Third-party identity provider** : If you use an external identity provider, for example Okta or Microsoft Entra ID, then add everyone in your workforce pool to a single group.



Google recommends that you create a custom IAM role to grant to your user group, using the following permissions:

  * `discoveryengine.answers.get`
  * `discoveryengine.servingConfigs.answer`
  * `discoveryengine.servingConfigs.search`
  * `discoveryengine.sessions.get`
  * `discoveryengine.widgetConfigs.get`



For more information about permissions for Agent Search resources using Identity and Access Management (IAM), see [Access control with IAM](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control).

For more information about custom roles, see the [Custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) in the IAM documentation.

## Authorize the search widget

If you want to deploy a search widget for an access-controlled app, follow these steps:

  1. Grant the Discovery Engine Viewer role to users in your domain or workforce pool who need to make search API calls.

  2. Generate authorization tokens to pass to your widget:

     * For Google Identity: Generate OAuth 2.0 access tokens.
     * For Workforce Identity Federation: Follow the steps in [Obtain short-lived tokens for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials) to get your token.
  3. Follow the steps in [Add a widget with an authorization token](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget#auth-token) to pass the token to your widget.




## What's next

[Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
