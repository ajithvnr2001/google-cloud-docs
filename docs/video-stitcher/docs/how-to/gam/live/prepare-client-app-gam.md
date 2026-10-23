---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/prepare-client-app-gam/
title: Prepare for your client application to work with Google Ad Manager \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:01:23.800597+00:00
---

# Prepare for your client application to work with Google Ad Manager  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/prepare-client-app-gam/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Prepare for your client application to work with Google Ad Manager Stay organized with collections  Save and categorize content based on your preferences. 

## Collect the required information for your client applications

You should have the following information that is required for Google Ad Manager to create a live stream session:

Field| Description  
---|---  
`projectNumber`| The Google Cloud project number (`PROJECT_NUMBER`) used to create Ad Manager-enabled sessions; alternatively, you can use the project ID.  
`region` | The [location](https://docs.cloud.google.com/video-stitcher/docs/locations) (`LOCATION`) where the live configuration is registered.   
`liveConfigId`| The live configuration ID used to register the livestream event with the Video Stitcher API. The following shows the format for the full config resource name:  

    
    
    projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID

The config ID is the last part of the full name (`LIVE_CONFIG_ID`). Keep in mind that the location of the config must be in the same location in which you create the session.   
`customAssetKey`| The custom asset key (`CUSTOM_ASSET_KEY`) created during the live configuration registration; the IMA SDK needs this value to create the stream.  
`networkCode`| The numeric identifier (`NETWORK_CODE`) for your Ad Manager network.  
`oAuthToken`| A short-lived OAuth token for the service account with the **Video Stitcher User** role. See Generate short-lived OAuth tokens.  
  
**Table 1.** Required information for Ad Manager-enabled live stream sessions

## Generate short-lived OAuth tokens for testing

To generate a [short-lived OAuth token](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) associated with the [service account](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/before-you-begin#create-service-account-to-create-sessions) with the **Video Stitcher User** role, follow these steps:

  1. Replace `PATH_TO_YOUR_SERVICE_KEY` with the path to the JSON file you downloaded to your local machine. 
         
         gcloud auth activate-service-account --key-file PATH_TO_YOUR_SERVICE_KEY

  2. Retrieve the OAuth 2.0 bearer token from the service account: 
         
         gcloud auth print-access-token




Because this is a short-lived token, you need to generate it again periodically with the `gcloud auth print-access-token` command and send the new tokens to your client applications. See the following section for more information on building a production service to provide short-lived tokens.

**Important:** Regenerating an OAuth token is a time-consuming operation. Try to reuse an OAuth token as much as possible when creating sessions. You can extend the lifetime of a token using the [`--lifetime` flag](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).

## Create a service to provide information to your client applications

Create a service that can provide the required information to be passed to the client. When the application requests information from your service on how to play a live stream, the service should return the information described in Table 1.

In particular, the service must be able to provide OAuth tokens to client applications in a secure manner. Configure this service using two service accounts, one [impersonating the other](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation). One service account has the **Service Token Creator** role and creates an OAuth token for the service account that has the **Video Stitcher User** role. For example:

  * Service account 1: This is the caller service account. This account has the **Service Token Creator** permission on service account 2 and impersonates service account 2 to client applications.
  * Service account 2: This is the privilege-bearing service account that has the **Video Stitcher User** role to create sessions.



For information on providing an OAuth token from your service, including client library code samples, see [Create a short-lived access token](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#sa-credentials-oauth).

[ Previous arrow_back  Create a configuration for a livestream event  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/create-live-configs)

[ Next Android  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/android)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
