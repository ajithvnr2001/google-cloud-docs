---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/import-existing-consumer-keys-and-secrets/
title: Import existing consumer keys and secrets \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:58.385317+00:00
---

# Import existing consumer keys and secrets  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/import-existing-consumer-keys-and-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Import existing consumer keys and secrets Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee automatically generates consumer keys and consumer secrets when you create developer apps and associate them with API products. (Those procedures are covered in [ Controlling access to your APIs by registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api).) However, you may have existing consumer keys and secrets that you want to import into Apigee from another system. Technically, this process isn't an import. It's recreating the existing keys in Apigee one at a time.

**Caution:** Be aware of the following size limits on API keys. By staying within these limits, you help avoid service disruptions.**Consumer key** (API key) size | 2 KB  
---|---  
**Consumer secret** size | 2 KB  
**Note:** Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed.

  1. **Create the consumer keys and secrets** using the Apigee API.  
See the [ `create` a consumer key and secret API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/create). Here's the curl:  

         
         curl https://apigee.googleapis.com/v1/organizations/{org}/developers/{developer_email}/apps/{app_name}/keys \
           -X POST \
           -H "Authorization: Bearer $TOKEN" \
           -H 'Content-type:application/json' \
           -d \
             '{
               "consumerKey": "key",
               "consumerSecret": "secret",
               "expiresInSeconds": "180"
             }'

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

For a description of the fields that you can provide in the request body, see [Resource: DeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys.create). 

  2. **Associate the consumer key/secret with one or more Apigee API products**. Doing this allows the imported consumer key (also called the API key) to be used in calls to API proxies where authorization is controlled by products.  
See the [ `ReplaceDeveloperAppKey` API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/replaceDeveloperAppKey). Here's the curl: 
         
         curl https://apigee.googleapis.com/v1/organizations/{org}/developers/{developer_email}/apps/{app_name}/keys/{key} \
           -X POST \
           -H "Authorization: Bearer $TOKEN" \
           -H 'Content-type:application/json' \
           -d \
             '{
               "apiProducts": ["product_1", "product_2"]
             }'

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

  3. Optionally delete the initial consumer key/secret that Apigee auto-generated. However, you can keep the auto-generated key. Both the imported key and the auto-generated key work in API calls, and both are displayed on the Developer App Details page in the Apigee UI.  
See the [ `delete` API key for developer app API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/delete).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
