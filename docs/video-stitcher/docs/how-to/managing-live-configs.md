---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-configs/
title: Create and manage a live config \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:02.018146+00:00
---

# Create and manage a live config  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-configs/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Create and manage a live config Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to manage live configs. Live configs are used to configure [live sessions](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions#create-session). For more details, see the [REST documentation](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs).

## Before you begin

To create a live session, you must first configure a livestream encoder which generates a source HLS or DASH manifest for the Video Stitcher API. These manifests contain certain ad markers at ad break boundaries which are identified by the Video Stitcher API for ad stitching purposes. You can create a livestream with a compatible manifest by following one of the [Live Stream API quickstarts](https://docs.cloud.google.com/livestream/docs/quickstarts).

For more details on the supported HLS and DASH ad markers, see the [ad markers documentation](https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-markers).

## Define a live config

When you define a live config, the following fields are required:

  * `sourceUri`
  * `adTagUri`
  * `defaultSlate`
  * `adTracking`



`sourceUri` specifies the URL to the source livestream's HLS or DASH manifest to insert ads into. The Video Stitcher API returns an HLS playback URL if the provided URL references an HLS manifest and a DASH playback URL if the provided URL references a DASH manifest.

`adTagUri` specifies the URL of the ad server that returns the ad metadata.

`defaultSlate` specifies the default slate to use when no slates are specified in an ad break's ad marker SCTE-35 message. For details about managing slates, see the [slates documentation](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-slates).

`adTracking` determines if the client player is expected to trigger playback and activity events or if the Video Stitcher API is expected to trigger playback events on behalf of the client player. For more information on client-side ad tracking, see [Handle client-side ad tracking](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions#handle-client-side-ad-tracking).

The live config contains optional fields for [prefetching ads](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs#LiveConfig.FIELDS.prefetch_config) and [defining custom headers](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs#LiveConfig.FIELDS.source_fetch_options).

## Register a live config

To register a live config, use the [`projects.locations.liveConfigs.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs/create) method.

### REST

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
  * `SOURCE_LIVESTREAM_URI`: the URI of the livestream manifest; use a public URI or an unsigned URI for which you [registered a CDN key](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys)
  * AD_TAG_URI

the public URI for the default ad tag. If you don't have one, you can use a [Single Inline Linear](https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags) sample.
  * `SLATE_ID`: the ID of the slate to use in the absence of stitched ads 



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "sourceUri": "SOURCE_LIVESTREAM_URI",
      "adTagUri": "AD_TAG_URI",
      "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
      "adTracking": "SERVER",
      "stitchingPolicy": "CUT_CURRENT"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs?liveConfigId=LIVE_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "sourceUri": "SOURCE_LIVESTREAM_URI",
      "adTagUri": "AD_TAG_URI",
      "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
      "adTracking": "SERVER",
      "stitchingPolicy": "CUT_CURRENT"
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
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs?liveConfigId=LIVE_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. Copy the returned `OPERATION_ID`, which is the last part of the `name` field, to use in the next section. 

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public class CreateLiveConfigSample
    {
        public async Task<LiveConfig> CreateLiveConfigAsync(
            string projectId, string location, string liveConfigId, string sourceUri, string adTagUri, string slateId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CreateLiveConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveConfigRequest.html) request = new [CreateLiveConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveConfigRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, location),
                LiveConfigId = liveConfigId,
                LiveConfig = new [LiveConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfig.html)
                {
                    SourceUri = sourceUri,
                    AdTagUri = adTagUri,
                    DefaultSlate = [SlateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.SlateName.html).[FormatProjectLocationSlate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.SlateName.html#Google_Cloud_Video_Stitcher_V1_SlateName_FormatProjectLocationSlate_System_String_System_String_System_String_)(projectId, location, slateId),
                    AdTracking = [AdTracking](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AdTracking.html).[Server](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AdTracking.html#Google_Cloud_Video_Stitcher_V1_AdTracking_Server),
                    StitchingPolicy = [LiveConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfig.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfig.Types.html).[StitchingPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfig.Types.StitchingPolicy.html).[CutCurrent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfig.Types.StitchingPolicy.html#Google_Cloud_Video_Stitcher_V1_LiveConfig_Types_StitchingPolicy_CutCurrent)
                }
            };
    
            // Make the request.
            Operation<LiveConfig, OperationMetadata> response = await client.[CreateLiveConfigAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateLiveConfigAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_LiveConfig_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<LiveConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
            // Retrieve the operation result.
            return completedResponse.Result;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // createLiveConfig creates a live config. Live configs are used to configure live sessions.
    func createLiveConfig(w io.Writer, projectID, liveConfigID, sourceURI, slateID string) error {
    	// projectID := "my-project-id"
    	// liveConfigID := "my-live-config-id"
    
    	// Uri of the media to stitch; this URI must reference either an MPEG-DASH
    	// manifest (.mpd) file or an M3U playlist manifest (.m3u8) file.
    	// sourceURI := "https://storage.googleapis.com/my-bucket/main.mpd"
    
    	// See https://cloud.google.com/video-stitcher/docs/concepts for information
    	// on ad tags and ad metadata. This sample uses an ad tag URL that displays
    	// a Single Inline Linear ad
    	// (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags).
    	adTagURI := "https://pubads.g.doubleclick.net/gampad/ads?iu=/21775744923/external/single_ad_samples&sz=640x480&cust_params=sample_ct%3Dlinear&ciu_szs=300x250%2C728x90&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&impl=s&correlator="
    	// slateID := "my-slate-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.CreateLiveConfigRequest{
    		Parent:       fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		LiveConfigId: liveConfigID,
    		LiveConfig: &stitcherstreampb.LiveConfig{
    			SourceUri:       sourceURI,
    			AdTagUri:        adTagURI,
    			AdTracking:      stitcherstreampb.AdTracking_SERVER,
    			StitchingPolicy: stitcherstreampb.LiveConfig_CUT_CURRENT,
    			DefaultSlate:    fmt.Sprintf("projects/%s/locations/%s/slates/%s", projectID, location, slateID),
    		},
    	}
    	// Creates the live config.
    	op, err := client.CreateLiveConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.createLiveConfig: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Live config: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[AdTracking](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AdTracking.html);
    import com.google.cloud.video.stitcher.v1.[CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html);
    import com.google.cloud.video.stitcher.v1.[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html).[StitchingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.StitchingPolicy.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[SlateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.SlateName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateLiveConfig {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String liveConfigId = "my-live-config-id";
        // Uri of the live stream to stitch; this URI must reference either an MPEG-DASH
        // manifest (.mpd) file or an M3U playlist manifest (.m3u8) file.
        String sourceUri = "https://storage.googleapis.com/my-bucket/main.mpd";
        // See Single Inline Linear
        // (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags)
        String adTagUri = "https://pubads.g.doubleclick.net/gampad/ads...";
        String slateId = "my-slate-id";
    
        createLiveConfig(projectId, location, liveConfigId, sourceUri, adTagUri, slateId);
      }
    
      // Creates a live config. Live configs are used to configure live sessions.
      // For more information, see
      // https://cloud.google.com/video-stitcher/docs/how-to/managing-live-configs.
      public static [LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html) createLiveConfig(
          String projectId,
          String location,
          String liveConfigId,
          String sourceUri,
          String adTagUri,
          String slateId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest.html) createLiveConfigRequest =
              [CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .[setLiveConfigId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest.Builder.html#com_google_cloud_video_stitcher_v1_CreateLiveConfigRequest_Builder_setLiveConfigId_java_lang_String_)(liveConfigId)
                  .setLiveConfig(
                      [LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html).newBuilder()
                          .setSourceUri(sourceUri)
                          .setAdTagUri(adTagUri)
                          .[setDefaultSlate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.Builder.html#com_google_cloud_video_stitcher_v1_LiveConfig_Builder_setDefaultSlate_java_lang_String_)([SlateName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.SlateName.html).format(projectId, location, slateId))
                          .setAdTracking([AdTracking](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AdTracking.html).SERVER)
                          .[setStitchingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.Builder.html#com_google_cloud_video_stitcher_v1_LiveConfig_Builder_setStitchingPolicy_com_google_cloud_video_stitcher_v1_LiveConfig_StitchingPolicy_)([StitchingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.StitchingPolicy.html).CUT_CURRENT)
                          .build())
                  .build();
    
          [LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html) response =
              videoStitcherServiceClient
                  .[createLiveConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_createLiveConfigAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_LocationName_com_google_cloud_video_stitcher_v1_LiveConfig_java_lang_String_)(createLiveConfigRequest)
                  .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Created new live config: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html#com_google_cloud_video_stitcher_v1_LiveConfig_getName__)());
          return response;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // liveConfigId = 'my-live-config-id';
    // sourceUri = 'https://storage.googleapis.com/my-bucket/main.mpd';
    // See Single Inline Linear
    // (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags)
    // adTagUri = 'https://pubads.g.doubleclick.net/gampad/ads...';
    // slateId = 'my-slate';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function createLiveConfig() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        liveConfig: {
          sourceUri: sourceUri,
          adTagUri: adTagUri,
          adTracking: '[SERVER](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.adtracking.html)',
          stitchingPolicy: '[CUT_CURRENT](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.liveconfig.stitchingpolicy.html)',
          defaultSlate: stitcherClient.[slatePath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, slateId),
        },
        liveConfigId: liveConfigId,
      };
      const [operation] = await stitcherClient.createLiveConfig(request);
      const [response] = await operation.promise();
      console.log(`response.name: ${response.name}`);
    }
    
    createLiveConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\AdTracking;
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateLiveConfigRequest;
    use Google\Cloud\Video\Stitcher\V1\LiveConfig;
    
    /**
     * Creates a live config. Live configs are used to configure live sessions.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the live config
     * @param string $liveConfigId         The name of the live config to be created
     * @param string $sourceUri            Uri of the media to stitch; this URI must
     *                                     reference either an MPEG-DASH manifest
     *                                     (.mpd) file or an M3U playlist manifest
     *                                     (.m3u8) file.
     * @param string $adTagUri             The Uri of the ad tag
     * @param string $slateId              The user-defined slate ID of the default
     *                                     slate to use when no slates are specified
     *                                     in an ad break's message
     */
    function create_live_config(
        string $callingProjectId,
        string $location,
        string $liveConfigId,
        string $sourceUri,
        string $adTagUri,
        string $slateId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $defaultSlate = $stitcherClient->slateName($callingProjectId, $location, $slateId);
    
        $liveConfig = (new LiveConfig())
            ->setSourceUri($sourceUri)
            ->setAdTagUri($adTagUri)
            ->setAdTracking(AdTracking::SERVER)
            ->setStitchingPolicy(LiveConfig\StitchingPolicy::CUT_CURRENT)
            ->setDefaultSlate($defaultSlate);
    
        // Run live config creation request
        $request = (new CreateLiveConfigRequest())
            ->setParent($parent)
            ->setLiveConfigId($liveConfigId)
            ->setLiveConfig($liveConfig);
        $operationResponse = $stitcherClient->createLiveConfig($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('Live config: %s' . PHP_EOL, $result->getName());
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest)
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        [VideoStitcherServiceClient](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.services.video_stitcher_service.VideoStitcherServiceClient.html),
    )
    
    
    def create_live_config(
        project_id: str,
        location: str,
        live_config_id: str,
        live_stream_uri: str,
        ad_tag_uri: str,
        slate_id: str,
    ) -> stitcher_v1.types.LiveConfig:
        """Creates a live config.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the live config.
            live_config_id: The user-defined live config ID.
            live_stream_uri: Uri of the livestream to stitch; this URI must reference either an MPEG-DASH
                        manifest (.mpd) file or an M3U playlist manifest (.m3u8) file.
            ad_tag_uri: Uri of the ad tag.
            slate_id: The user-defined slate ID of the default slate to use when no slates are specified in an ad break's message.
    
        Returns:
            The live config resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        default_slate = f"projects/{project_id}/locations/{location}/slates/{slate_id}"
    
        live_config = [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest).[types](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.html).[LiveConfig](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.LiveConfig.html)(
            source_uri=live_stream_uri,
            ad_tag_uri=ad_tag_uri,
            ad_tracking="SERVER",
            stitching_policy="CUT_CURRENT",
            default_slate=default_slate,
        )
    
        operation = client.[create_live_config](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.services.video_stitcher_service.VideoStitcherServiceClient.html#google_cloud_video_stitcher_v1_services_video_stitcher_service_VideoStitcherServiceClient_create_live_config)(
            parent=parent, live_config_id=live_config_id, live_config=live_config
        )
        response = operation.result()
        print(f"Live config: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create a live config
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param live_config_id [String] Your live config name (e.g. `my-live-config`)
    # @param source_uri [String] Uri of the live stream to stitch
    #   (e.g. `https://storage.googleapis.com/my-bucket/main.mpd`)
    # @param ad_tag_uri [String] Uri of the ad tag
    #   (e.g. `https://pubads.g.doubleclick.net/gampad/ads...`)
    # @param slate_id [String] The default slate ID to use when no slates are
    #   specified in an ad break's message (e.g. `my-slate-id`)
    #
    def create_live_config project_id:, location:, live_config_id:, source_uri:,
                           ad_tag_uri:, slate_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      # Build the resource name of the default slate.
      slate_name = client.slate_path project: project_id, location: location,
                                     slate: slate_id
    
      # Set the live config fields.
      new_live_config = {
        source_uri: source_uri,
        ad_tag_uri: ad_tag_uri,
        ad_tracking: Google::Cloud::Video::Stitcher::V1::AdTracking::SERVER,
        stitching_policy: Google::Cloud::Video::Stitcher::V1::LiveConfig::StitchingPolicy::CUT_CURRENT,
        default_slate: slate_name
      }
    
      operation = client.create_live_config parent: parent,
                                            live_config_id: live_config_id,
                                            live_config: new_live_config
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the live config name.
      puts "Live config: #{operation.response.name}"
    end

### Check for the result

To check if the live config has been created, use the [`projects.locations.operations.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/get) method. If the response contains `"done: false"`, repeat the command until the response contains `"done: true"`.

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
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
        "verb": "create",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.video.stitcher.v1.LiveConfig",
        "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
        "sourceUri": "SOURCE_LIVESTREAM_URI",
        "adTagUri": "AD_TAG_URI",
        "state": "READY",
        "adTracking": "CLIENT",
        "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
        "stitchingPolicy": "CUT_CURRENT",
        "defaultAdBreakDuration": "30s"
      }
    }
    

## Get a live config

To get the details for a specific live config, use the [`projects.locations.liveConfigs.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs/get) method.

### REST

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
      "state": "READY",
      "adTracking": "SERVER",
      "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
      "stitchingPolicy": "CUT_CURRENT"
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class GetLiveConfigSample
    {
        public LiveConfig GetLiveConfig(
            string projectId, string location, string liveConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [GetLiveConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetLiveConfigRequest.html) request = new [GetLiveConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetLiveConfigRequest.html)
            {
                LiveConfigName = [LiveConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfigName.html).[FromProjectLocationLiveConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfigName.html#Google_Cloud_Video_Stitcher_V1_LiveConfigName_FromProjectLocationLiveConfig_System_String_System_String_System_String_)(projectId, location, liveConfigId)
            };
    
            // Call the API.
            [LiveConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfig.html) response = client.[GetLiveConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_GetLiveConfig_Google_Cloud_Video_Stitcher_V1_GetLiveConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return response;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // getLiveConfig gets a previously-created live config.
    func getLiveConfig(w io.Writer, projectID, liveConfigID string) error {
    	// projectID := "my-project-id"
    	// liveConfigID := "my-live-config-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.GetLiveConfigRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/liveConfigs/%s", projectID, location, liveConfigID),
    	}
    
    	response, err := client.GetLiveConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetLiveConfig: %w", err)
    	}
    	b, err := json.MarshalIndent(response, "", " ")
    	if err != nil {
    		return fmt.Errorf("json.MarshalIndent: %w", err)
    	}
    
    	fmt.Fprintf(w, "Live config:\n%s", string(b))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[GetLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html);
    import com.google.cloud.video.stitcher.v1.[LiveConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfigName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    
    public class GetLiveConfig {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String liveConfigId = "my-live-config-id";
    
        getLiveConfig(projectId, location, liveConfigId);
      }
    
      // Gets a live config.
      public static [LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html) getLiveConfig(String projectId, String location, String liveConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [GetLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveConfigRequest.html) getLiveConfigRequest =
              [GetLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveConfigRequest.html).newBuilder()
                  .setName([LiveConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfigName.html).of(projectId, location, liveConfigId).toString())
                  .build();
    
          [LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html) response = videoStitcherServiceClient.getLiveConfig(getLiveConfigRequest);
          System.out.println("Live config: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html#com_google_cloud_video_stitcher_v1_LiveConfig_getName__)());
          return response;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // liveConfigId = 'my-live-config-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function getLiveConfig() {
      // Construct request
      const request = {
        name: stitcherClient.[liveConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, liveConfigId),
      };
      const [liveConfig] = await stitcherClient.getLiveConfig(request);
      console.log(`Live config: ${liveConfig.name}`);
    }
    
    getLiveConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\GetLiveConfigRequest;
    
    /**
     * Gets a live config.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the live config
     * @param string $liveConfigId         The ID of the live config
     */
    function get_live_config(
        string $callingProjectId,
        string $location,
        string $liveConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->liveConfigName($callingProjectId, $location, $liveConfigId);
        $request = (new GetLiveConfigRequest())
            ->setName($formattedName);
        $liveConfig = $stitcherClient->getLiveConfig($request);
    
        // Print results
        printf('Live config: %s' . PHP_EOL, $liveConfig->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def get_live_config(
        project_id: str, location: str, live_config_id: str
    ) -> stitcher_v1.types.LiveConfig:
        """Gets a live config.
        Args:
            project_id: The GCP project ID.
            location: The location of the live config.
            live_config_id: The user-defined live config ID.
    
        Returns:
            The live config resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/liveConfigs/{live_config_id}"
        response = client.get_live_config(name=name)
        print(f"Live config: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Get a live config
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param live_config_id [String] Your live config name (e.g. `my-live-config`)
    #
    def get_live_config project_id:, location:, live_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the live config.
      name = client.live_config_path project: project_id, location: location,
                                     live_config: live_config_id
    
      # Get the live config.
      live_config = client.get_live_config name: name
    
      # Print the live config name.
      puts "Live config: #{live_config.name}"
    end

## Update a live config

To update a specific live config, use the [`projects.locations.liveConfigs.patch`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs/patch) method. You can only update the [custom headers](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/FetchOptions#FIELDS.headers).

### REST

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
  * `LIVE_CONFIG_ID`: the user-defined identifier for the live config
  * `KEY`: the key in a key-value pair used to define a custom header
  * `VALUE`: the value in a key-value pair used to define a custom header



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "sourceFetchOptions": {
        "headers": {
          "KEY": "VALUE"
        }
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID?updateMask=sourceFetchOptions.headers"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "sourceFetchOptions": {
        "headers": {
          "KEY": "VALUE"
        }
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID?updateMask=sourceFetchOptions.headers" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
        "verb": "update",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. For more information, see Check for the result. 

## List all registered live configs

To list all of the live configs registered for a given location in a project, use the [`projects.locations.liveConfigs.list`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs/list) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the live configs; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "liveConfigs": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
          "sourceUri": "SOURCE_LIVESTREAM_URI",
          "adTagUri": "AD_TAG_URI",
          "state": "READY",
          "adTracking": "SERVER",
          "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/SLATE_ID",
          "stitchingPolicy": "CUT_CURRENT"
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/my-other-live-config",
          "sourceUri": "my-other-live-stream-uri",
          "adTagUri": "my-other-ad-tag-uri",
          "state": "READY",
          "adTracking": "SERVER",
          "defaultSlate": "projects/PROJECT_NUMBER/locations/LOCATION/slates/my-other-slate",
          "stitchingPolicy": "CUT_CURRENT"
        }
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using System;
    
    public class ListLiveConfigsSample
    {
        public PagedEnumerable<ListLiveConfigsResponse, LiveConfig> ListLiveConfigs(
            string projectId, string regionId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [ListLiveConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ListLiveConfigsRequest.html) request = new [ListLiveConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ListLiveConfigsRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, regionId)
            };
    
            // Make the request.
            PagedEnumerable<ListLiveConfigsResponse, LiveConfig> response = client.[ListLiveConfigs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_ListLiveConfigs_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
            foreach ([LiveConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfig.html) liveConfig in response)
            {
                Console.WriteLine($"{liveConfig.Name}");
            }
    
            // Return the result.
            return response;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    	"google.golang.org/api/iterator"
    )
    
    // listLiveConfigs lists all live configs for a given location.
    func listLiveConfigs(w io.Writer, projectID string) error {
    	// projectID := "my-project-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.ListLiveConfigsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    
    	it := client.ListLiveConfigs(ctx, req)
    	fmt.Fprintln(w, "Live configs:")
    
    	for {
    		response, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next(): %w", err)
    		}
    		fmt.Fprintln(w, response.GetName())
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest.html);
    import com.google.cloud.video.stitcher.v1.[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).[ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse.html);
    import java.io.IOException;
    
    public class ListLiveConfigs {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
    
        listLiveConfigs(projectId, location);
      }
    
      // Lists the live configs for a given project and location.
      public static [ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse.html) listLiveConfigs(String projectId, String location)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest.html) listLiveConfigsRequest =
              [ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .build();
    
          [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).[ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse.html) response =
              videoStitcherServiceClient.listLiveConfigs(listLiveConfigsRequest);
    
          System.out.println("Live configs:");
          for ([LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig.html) liveConfig : response.iterateAll()) {
            System.out.println(liveConfig.getName());
          }
          return response;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function listLiveConfigs() {
      const iterable = await stitcherClient.[listLiveConfigsAsync](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)({
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
      });
      console.info('Live configs:');
      for await (const response of iterable) {
        console.log(response.name);
      }
    }
    
    listLiveConfigs().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\ListLiveConfigsRequest;
    
    /**
     * Lists all live configs for a location.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the live configs
     */
    function list_live_configs(
        string $callingProjectId,
        string $location
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $request = (new ListLiveConfigsRequest())
            ->setParent($parent);
        $response = $stitcherClient->listLiveConfigs($request);
    
        // Print the live config list.
        $liveConfigs = $response->iterateAllElements();
        print('Live configs:' . PHP_EOL);
        foreach ($liveConfigs as $liveConfig) {
            printf('%s' . PHP_EOL, $liveConfig->getName());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        pagers,
        VideoStitcherServiceClient,
    )
    
    
    def list_live_configs(project_id: str, location: str) -> pagers.ListLiveConfigsPager:
        """Lists all live configs in a location.
        Args:
            project_id: The GCP project ID.
            location: The location of the live configs.
    
        Returns:
            An iterable object containing live config resources.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        response = client.list_live_configs(parent=parent)
        print("Live configs:")
        for live_config in response.live_configs:
            print({live_config.name})
    
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # List live configs for a given location
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    #
    def list_live_configs project_id:, location:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      response = client.list_live_configs parent: parent
    
      puts "Live configs:"
      # Print out all live configs.
      response.each do |live_config|
        puts live_config.name
      end
    end

### Additional results

The `curl` response may include a `nextPageToken`, which you can use to retrieve additional results:
    
    
    {
      "liveConfigs": [
        ...
      ],
      "nextPageToken": "NEXT_PAGE_TOKEN"
    }
    

You can send another `curl` request, including the value of NEXT_PAGE_TOKEN, to list the additional configs. Append the following to the URL in the preceding API call:
    
    
    ?pageToken=NEXT_PAGE_TOKEN
    

See the relevant [client library](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries) for more information on using this token.

## Delete a live config

If a registered live config is no longer needed, delete it using the [`projects.locations.liveConfigs.delete`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs/delete) method.

### REST

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
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
        "verb": "delete",
        "cancelRequested": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

This command creates a [long-running operation (LRO)](https://docs.cloud.google.com/video-stitcher/docs/how-to/manage-long-running-operations) that you can query to track progress. For more information, see Check for the result. 

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public class DeleteLiveConfigSample
    {
        public async Task DeleteLiveConfigAsync(
            string projectId, string location, string liveConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [DeleteLiveConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteLiveConfigRequest.html) request = new [DeleteLiveConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteLiveConfigRequest.html)
            {
                LiveConfigName = [LiveConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfigName.html).[FromProjectLocationLiveConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfigName.html#Google_Cloud_Video_Stitcher_V1_LiveConfigName_FromProjectLocationLiveConfig_System_String_System_String_System_String_)(projectId, location, liveConfigId)
            };
    
            // Make the request.
            Operation<Empty, OperationMetadata> response = await client.[DeleteLiveConfigAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_DeleteLiveConfigAsync_Google_Cloud_Video_Stitcher_V1_DeleteLiveConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            await response.PollUntilCompletedAsync();
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // deleteLiveConfig deletes a previously-created live config.
    func deleteLiveConfig(w io.Writer, projectID, liveConfigID string) error {
    	// projectID := "my-project-id"
    	// liveConfigID := "my-live-config-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.DeleteLiveConfigRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/liveConfigs/%s", projectID, location, liveConfigID),
    	}
    	// Deletes the live config.
    	op, err := client.DeleteLiveConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.DeleteLiveConfig: %w", err)
    	}
    	err = op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Deleted live config")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[LiveConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfigName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteLiveConfig {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String liveConfigId = "my-live-config-id";
    
        deleteLiveConfig(projectId, location, liveConfigId);
      }
    
      // Deletes a live config.
      public static void deleteLiveConfig(String projectId, String location, String liveConfigId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest.html) deleteLiveConfigRequest =
              [DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest.html).newBuilder()
                  .setName([LiveConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfigName.html).of(projectId, location, liveConfigId).toString())
                  .build();
    
          videoStitcherServiceClient
              .[deleteLiveConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_deleteLiveConfigAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_LiveConfigName_)(deleteLiveConfigRequest)
              .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Deleted live config");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // liveConfigId = 'my-live-config-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function deleteLiveConfig() {
      // Construct request
      const request = {
        name: stitcherClient.[liveConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, liveConfigId),
      };
      const [operation] = await stitcherClient.deleteLiveConfig(request);
      await operation.promise();
      console.log('Deleted live config');
    }
    
    deleteLiveConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\DeleteLiveConfigRequest;
    
    /**
     * Deletes a live config.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the live config
     * @param string $liveConfigId         The ID of the live config
     */
    function delete_live_config(
        string $callingProjectId,
        string $location,
        string $liveConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->liveConfigName($callingProjectId, $location, $liveConfigId);
        $request = (new DeleteLiveConfigRequest())
            ->setName($formattedName);
        $operationResponse = $stitcherClient->deleteLiveConfig($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            // Print status
            printf('Deleted live config %s' . PHP_EOL, $liveConfigId);
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    from google.protobuf import empty_pb2 as empty
    
    
    def delete_live_config(
        project_id: str, location: str, live_config_id: str
    ) -> empty.Empty:
        """Deletes a live config.
        Args:
            project_id: The GCP project ID.
            location: The location of the live config.
            live_config_id: The user-defined live config ID."""
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/liveConfigs/{live_config_id}"
        operation = client.delete_live_config(name=name)
        response = operation.result()
        print("Deleted live config")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Delete a live config
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param live_config_id [String] Your live config name (e.g. `my-live-config`)
    #
    def delete_live_config project_id:, location:, live_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the live config.
      name = client.live_config_path project: project_id, location: location,
                                     live_config: live_config_id
    
      # Delete the live config.
      operation = client.delete_live_config name: name
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print a success message.
      puts "Deleted live config"
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
