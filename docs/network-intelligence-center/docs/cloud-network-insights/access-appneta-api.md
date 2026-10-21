---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/access-appneta-api/
title: Access the AppNeta API \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:42:17.266728+00:00
---

# Access the AppNeta API  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/access-appneta-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ APIs and reference ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/apis)



#  Access the AppNeta API Stay organized with collections  Save and categorize content based on your preferences. 

You can interact with the AppNeta API using a token-based authentication flow that originates from Google Cloud. 

## Before you begin

To generate the necessary Google Cloud access token, you need to operate within a Google Cloud project. We recommend that you use the project in which you have enabled Cloud Network Insights.

The user or service account requesting the token must have one of the following roles in the Google Cloud project:

  * If you want the account to have **read-only** access to Cloud Network Insights resources, grant it one of the following roles in your project: 
    * Cloud Network Insights Viewer (`roles/networkmanagement.CloudNetworkInsightsViewer`)
    * Network Management Viewer (`networkmanagement.viewer`)
    * The basic Viewer role
  * If you want the account to have **full access** to Cloud Network Insights resources, grant it one of the following roles in your project: 
    * Cloud Network Insights Editor (`roles/networkmanagement.CloudNetworkInsightsEditor`)
    * Network Management Admin (`networkmanagement.admin`)

**Important:** Your access level in AppNeta is determined by your Google Cloud IAM role.

## Create an AppNeta API token

You can create an AppNeta API token by generating a Google Cloud access token to exchange for a provider-specific token that is used with the AppNeta API.

### Generate a Google Cloud access token

Generate a Google Cloud access token for the user or service account that makes the API calls. There are several ways to obtain a Google Cloud access token, depending on your environment and how you are authenticated to Google Cloud.

  * Service Accounts: If you're running applications on Google Cloud infrastructure (for example, Compute Engine, Google Kubernetes Engine) or using service account keys, you can use the Cloud Client Libraries or the metadata server to fetch tokens.
  * Other Environments: Google Cloud provides various authentication mechanisms.



See [Authentication token types](https://docs.cloud.google.com/docs/authentication/token-types) for a comprehensive guide on choosing the best method for your situation.

If you have the Google Cloud CLI installed and configured, you can generate a token to copy using [gcloud CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/auth).
    
    
      gcloud auth print-access-token
    

If you want application default credentials, use the following gcloud CLI command.
    
    
    gcloud auth application-default print-access-token
    

### Exchange tokens

Use the copied Google Cloud access token to call the Network Management API to generate a provider-specific access token for AppNeta.

The AppNeta token expires when the Google Cloud token used to generate it expires. Google Cloud access tokens are typically valid for one hour. We recommend using a fresh Google Cloud access token each time you perform the `generateProviderAccessToken`call to ensure the AppNeta token has the maximum possible lifespan.

### gcloud
    
    
    gcloud network-management network-monitoring-providers generate-provider-access-token NETWORK_MONITORING_PROVIDER --location=global --gcp-access-token=GCP_ACCESS_TOKEN
    

Replace the following:

  * `NETWORK_MONITORING_PROVIDER`: the provider name. Use `external` unless you have actively set a different name.
  * `GCP_ACCESS_TOKEN`: the token you generated in Google Cloud.



### curl
    
    
    curl -H "Authorization: Bearer GCP_ACCESS_TOKEN"   
    
     "https://networkmanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/networkMonitoringProviders/external:generateProviderAccessToken?gcp_access_token=GCP_ACCESS_TOKEN"
    

Replace the following:

  * `GCP_ACCESS_TOKEN`: the token you generated in Google Cloud.
  * `PROJECT_ID`: the project where Cloud Network Insights is enabled.



The response from this call contains the `providerAccessToken`, which you use to authenticate requests directly against the AppNeta API endpoints.

## Use the AppNeta token

Use the `providerAccessToken` as a bearer token in the authorization header when making calls to the AppNeta API. Refer to the [AppNeta API documentation](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/api.html) for details on available endpoints and request formats.

If you receive a [`401` error](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/api/api-v4.html#title-appneta-api_error-codes), generate a new Google Cloud access token or application default credential token, and then exchange tokens again.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
