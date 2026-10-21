---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/create-live-configs/
title: Create a configuration for a livestream event \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:22.656181+00:00
---

# Create a configuration for a livestream event  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/create-live-configs/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Create a configuration for a livestream event Stay organized with collections  Save and categorize content based on your preferences. 

For Ad Manager integration, you need to create a live configuration for a given livestream event. The Video Stitcher API registers this config with Ad Manager.

## Create a slate

Before you create the live configuration, you need to create a slate. The Video Stitcher API inserts a default slate video when ads can't be inserted. You must register slate video with the Video Stitcher API to indicate the slate to use in the absence of ads. The slate video can be any MP4 file with at least one audio track.

You have two options for creating this slate. You can create a default network slate in your Ad Manager account or you can create slates using the Video Stitcher API.

### Create a slate in Ad Manager

To create a default network slate in your Ad Manager account, follow the steps at [Create a slate to fill content gaps](https://support.google.com/admanager/answer/7292054) and then skip to section Create the live config.

### Create a slate using the Video Stitcher API

To create a slate using the Video Stitcher API, use the [`projects.locations.slates.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.slates/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your slate; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `SLATE_ID`: a user-defined identifier for the slate. This ID can only contain lower-case letters, numbers, and hyphens. The first character must be a letter, the last character must be a letter or a number, and the entire ID has a 63 character maximum.
  * `SLATE_URL`: the public URI for an MP4 video with at least one audio track ([sample video](https://docs.cloud.google.com/static/video-stitcher/images/ChromeCast.mp4))
  * `NETWORK_CODE`: the numeric identifier for your Ad Manager network; you can find this in the **[Global settings](https://support.google.com/admanager/answer/7674889)** for the publisher account **Important:** You must include the [`gamSlate`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.slates#Slate.FIELDS.gam_slate) object to use the slate with Google Ad Manager (GAM). 



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "uri": "SLATE_URL",
      "gamSlate": {
        "networkCode": "NETWORK_CODE"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/slates?slateId=SLATE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "uri": "SLATE_URL",
      "gamSlate": {
        "networkCode": "NETWORK_CODE"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/slates?slateId=SLATE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
        "verb": "create"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. Copy the returned `OPERATION_ID`, which is the last part of the `name` field, to use in the next section.

#### Check for the result

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/get) method to check if the slate has been created. If the response contains `"done: false"`, repeat the command until the response contains `"done: true"`.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the data; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `OPERATION_ID`: the identifier for the operation



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "endTime": END_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
        "verb": "create"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.video.stitcher.v1.Slate",
        "name": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
        "uri": "SLATE_URL",
        "gamSlate": {
          "networkCode": "NETWORK_CODE"
          "gamSlateId": "GAM_SLATE_ID"
        }
      }
    }
    

## Create the live config

To create the config, use the [`projects.locations.liveConfigs.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs/create) method. See the [live config reference documentation](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs) for optional fields (like [custom headers](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs#LiveConfig.FIELDS.source_fetch_options)).

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your live config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `LIVE_CONFIG_ID`: a user-defined identifier for the live config. This ID can only contain lower-case letters, numbers, and hyphens. The first character must be a letter, the last character must be a letter or a number, and the entire ID has a 63 character maximum.
  * `SOURCE_LIVESTREAM_URI`: the source URL to the livestream video manifest. This must be accessible to the Video Stitcher API. The URL must **either be publicly accessible or, if URL signing is enabled for the CDN,** a registered CDN key has been provided to the Video Stitcher API. If you [created a test livestream using the Live Stream API](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/before-you-begin#create-live-stream), then this is the URI to the `main.m3u8` or `main.mpd` file in the Cloud Storage bucket.
  * AD_TAG_URI

the URL for ad metadata retrieved from ad servers; for Ad Manager integration, **this must be a valid Ad Manager live video ad tag**. To get a valid ad tag, follow the steps on [Generate video and audio ad tags](https://support.google.com/admanager/answer/1181016) with these modifications: 
    * For **Live traffic** , enable live traffic.
    * For the **Player SDK type** , select **Google IMA SDK**.
    * Add the parameter `ad_rule=0` to the tag (for example, add `&ad_rule=0` to the end).
  * `SLATE_ID`: the ID of the slate to use in the absence of stitched ads **Note:** If you [created a default network slate using Ad Manager](https://support.google.com/admanager/answer/7292054), remove the `defaultSlate` field from the request to use the default network slate.
  * `NETWORK_CODE`: the numeric identifier for your Ad Manager network; you can find this in the **[Global settings](https://support.google.com/admanager/answer/7674889)** for the publisher account.
  * `AD_TRACKING`: the ad tracking behavior for your stream. For IMA SDK integrations, use `CLIENT`. For server-side ad tracking, use `SERVER`. You may also override this value on a per-session basis later.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** Ensure you have set the [ `GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#local-key) environment variable to the path for your service account private key file. 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "sourceUri": "SOURCE_LIVESTREAM_URI",
      "adTagUri": "AD_TAG_URI",
      "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
      "gamLiveConfig": {
        "networkCode": "NETWORK_CODE",
      },
      "adTracking": "AD_TRACKING"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs?liveConfigId=LIVE_CONFIG_ID"

#### PowerShell (Windows)

**Note:** Ensure you have set the [ `GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#local-key) environment variable to the path for your service account private key file. 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "sourceUri": "SOURCE_LIVESTREAM_URI",
      "adTagUri": "AD_TAG_URI",
      "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
      "gamLiveConfig": {
        "networkCode": "NETWORK_CODE",
      },
      "adTracking": "AD_TRACKING"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth application-default print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs?liveConfigId=LIVE_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
        "verb": "create"
      },
      "done": false
    }
    

The Video Stitcher API asynchronously registers the config on your Ad Manager account. This may take a couple of minutes.

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. For more information, see Check for the result.

## Get the config

To get the config, use the [`projects.locations.liveConfigs.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs/get) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the live config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `LIVE_CONFIG_ID`: the user-defined identifier for the live config



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
      "sourceUri": "SOURCE_LIVESTREAM_URI",
      "adTagUri": "AD_TAG_URI",
      "gamLiveConfig": {
        "networkCode": "NETWORK_CODE",
        "assetKey": "ASSET_KEY",
        "customAssetKey": "PROJECT_NUMBER-LOCATION-LIVE_CONFIG_ID"
      },
      "state": "READY",
      "adTracking": "CLIENT",
      "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
      "stitchingPolicy": "CUT_CURRENT"
    }
    

Find the `customAssetKey` field and copy the returned CUSTOM_ASSET_KEY. You send these values to the Interactive Media Ads (IMA) SDK in a subsequent step.

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/overview)

[ Next Prepare for your client application to work with Google Ad Manager  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/prepare-client-app-gam)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
