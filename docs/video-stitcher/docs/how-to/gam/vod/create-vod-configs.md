---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/create-vod-configs/
title: Create a configuration for a VOD session \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:00.519940+00:00
---

# Create a configuration for a VOD session  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/create-vod-configs/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Create a configuration for a VOD session Stay organized with collections  Save and categorize content based on your preferences. 

For Ad Manager integration, you need to create an ad tag for the VOD session. You also need to create a VOD configuration. The Video Stitcher API registers this config with Ad Manager.

## Create an ad tag in Ad Manager

Perform the following steps in your Ad Manager account:

  1. [Add a new ad unit](https://support.google.com/admanager/answer/10477477?ref_topic=10478086).
  2. [Activate ad rules](https://support.google.com/admanager/answer/9170964).
  3. [Create a new ad rule](https://support.google.com/admanager/answer/9204132). As part of this step, find the **Targeting > Inventory** section in Ad Manager. Select the new ad unit from the previous step.

  4. Create a valid ad tag by following the steps on [Generate video and audio ad tags](https://support.google.com/admanager/answer/1181016) with the following modifications:

     * For the Player SDK type, select **Google IMA SDK**.
     * Add the parameter `ad_rule=1` to the tag (for example, add `&ad_rule=1` to the end).
     * Add the parameter `vid_d=vod-asset-duration-in-secs` to the tag (for example, add `&vid_d=1800` to the end for a 30 minute VOD asset).
     * Modify the parameter `output=vast` to be `output=xml_vmap1`. The Video Multiple Ad Playlist (VMAP) specification is the only supported output type. 



## Create a VOD config

**Note:** Don't create a VOD config if your target platform is the IMA SDK on Chromecast. Skip the following step.

To create the config, use the [`projects.locations.vodConfigs.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/create) method. See the [VOD config reference documentation](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs) for optional fields (like [custom headers](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs#VodConfig.FIELDS.source_fetch_options)).

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your VOD config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `VOD_CONFIG_ID`: a user-defined identifier for the VOD config. This ID can only contain lower-case letters, numbers, and hyphens. The first character must be a letter, the last character must be a letter or a number, and the entire ID has a 63 character maximum.
  * `VOD_URI`: the URI of the media to stitch. This URI must reference either an MPEG-DASH manifest (MPD) file or an HLS manifest (M3U8) file. Use a public URI or an unsigned URI for which you [registered a CDN key](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys). **Note:** You can use the Transcoder API to create these manifest files. See [Create VOD source files](https://docs.cloud.google.com/video-stitcher/docs/create-vod-source-files) for more information. You must make the manifest files public so that the Video Stitcher API can access them.
  * AD_TAG_URI

the URL for ad metadata retrieved from ad servers; for Ad Manager integration, **this must be a valid Ad Manager video ad tag**. To get a valid ad tag, follow the steps in the previous section Create an ad tag in Ad Manager. 
  * `NETWORK_CODE`: the numeric identifier for your Ad Manager network; you can find this in the **[Global settings](https://support.google.com/admanager/answer/7674889)** for the publisher account 



Request JSON body: 
    
    
    {
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "gamVodConfig": {
        "networkCode": "NETWORK_CODE"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "gamVodConfig": {
        "networkCode": "NETWORK_CODE"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs?vodConfigId=VOD_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "gamVodConfig": {
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
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs?vodConfigId=VOD_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. Copy the returned `OPERATION_ID`, which is the last part of the `name` field, to use in the next section.

### Check for the result

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/get) method to check if the VOD config has been created. If the response contains `"done: false"`, repeat the command until the response contains `"done: true"`.

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
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
        "verb": "create"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.video.stitcher.v1.VodConfig",
        "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
        "sourceUri": "VOD_URI",
        "adTagUri": "AD_TAG_URI",
        "gamVodConfig": {
          "networkCode": "NETWORK_CODE"
        },
        "state": "READY"
      }
    }
    

Check that the state is set to `READY`. If not, wait for a few seconds and send the request again.

For more information on VOD configs, see [Create and manage a VOD config](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs).

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/overview)

[ Next Prepare for your client application to work with Google Ad Manager  arrow_forward  ](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/prepare-client-app-gam)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
