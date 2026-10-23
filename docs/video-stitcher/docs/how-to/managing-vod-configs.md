---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs/
title: Create and manage a VOD config \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:06.384128+00:00
---

# Create and manage a VOD config  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Create and manage a VOD config Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage VOD configs. VOD configs are used to configure [VOD sessions](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions). For more details, see the [REST documentation](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs).

## Before you begin

To create a VOD session, you must first configure an encoder which generates a source HLS or DASH manifest for the VOD asset. These manifests contain certain ad markers at ad break boundaries which are identified by the Video Stitcher API for ad stitching purposes. You can use the Transcoder API to [create a transcoding job](https://docs.cloud.google.com/transcoder/docs/transcode-video) to generate the manifest files from [media file types](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats) such as MP4 or MOV.

For more details on the supported HLS and DASH ad markers, see the [ad markers documentation](https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-markers).

## Define a VOD config

When you define a VOD config, the following fields are required:

  * `sourceUri`
  * `adTagUri`



`sourceUri` specifies the URL to the source VOD asset's HLS or DASH manifest to insert ads into. The Video Stitcher API returns an HLS playback URL if the provided URL references an HLS manifest and a DASH playback URL if the provided URL references a DASH manifest. You can use an existing manifest file or you can [create your own VOD source files](https://docs.cloud.google.com/video-stitcher/docs/create-vod-source-files).

`adTagUri` specifies the URL of the ad server that returns the ad metadata.

The VOD config contains an optional field for [defining custom headers](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs#VodConfig.FIELDS.source_fetch_options).

## Register a VOD config

To register a VOD config, use the [`projects.locations.vodConfigs.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/create) method.

### REST

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

the public URI of the ad tag; if you don't have one, you can use a [VMAP Pre-roll](https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags#vmap-pre-roll) sample



Request JSON body: 
    
    
    {
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI"
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
      "adTagUri": "AD_TAG_URI"
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

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public class CreateVodConfigSample
    {
        public async Task<VodConfig> CreateVodConfigAsync(
            string projectId, string location, string vodConfigId, string sourceUri, string adTagUri)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CreateVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateVodConfigRequest.html) request = new [CreateVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateVodConfigRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, location),
                VodConfigId = vodConfigId,
                VodConfig = new [VodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfig.html)
                {
                    SourceUri = sourceUri,
                    AdTagUri = adTagUri
                }
            };
    
            // Make the request.
            Operation<VodConfig, OperationMetadata> response = await client.[CreateVodConfigAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateVodConfigAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_VodConfig_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<VodConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
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
    
    // createVodConfig creates a VOD config. VOD configs are used to configure VOD sessions.
    func createVodConfig(w io.Writer, projectID, vodConfigID, sourceURI string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    
    	// Uri of the media to stitch; this URI must reference either an MPEG-DASH
    	// manifest (.mpd) file or an M3U playlist manifest (.m3u8) file.
    	// sourceURI := "https://storage.googleapis.com/my-bucket/main.mpd"
    
    	// See https://cloud.google.com/video-stitcher/docs/concepts for information
    	// on ad tags and ad metadata. This sample uses an ad tag URL that displays
    	// a VMAP Pre-roll ad
    	// (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags).
    	adTagURI := "https://pubads.g.doubleclick.net/gampad/ads?iu=/21775744923/external/vmap_ad_samples&sz=640x480&cust_params=sample_ar%3Dpreonly&ciu_szs=300x250%2C728x90&gdfp_req=1&ad_rule=1&output=vmap&unviewed_position_start=1&env=vp&impl=s&correlator="
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.CreateVodConfigRequest{
    		Parent:      fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		VodConfigId: vodConfigID,
    		VodConfig: &stitcherstreampb.VodConfig{
    			SourceUri: sourceURI,
    			AdTagUri:  adTagURI,
    		},
    	}
    	// Creates the VOD config.
    	op, err := client.CreateVodConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateVodConfig: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "VOD config: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateVodConfig {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
        // URI of the VOD stream to stitch; this URI must reference either an MPEG-DASH
        // manifest (.mpd) file or an M3U playlist manifest (.m3u8) file.
        String sourceUri = "https://storage.googleapis.com/my-bucket/main.mpd";
        // See VMAP Pre-roll
        // (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags)
        String adTagUri = "https://pubads.g.doubleclick.net/gampad/ads...";
    
        createVodConfig(projectId, location, vodConfigId, sourceUri, adTagUri);
      }
    
      // Creates a video on demand (VOD) config. VOD configs are used to configure VOD
      // sessions. For more information, see
      // https://cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs.
      public static [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) createVodConfig(
          String projectId, String location, String vodConfigId, String sourceUri, String adTagUri)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest.html) createVodConfigRequest =
              [CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .[setVodConfigId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest.Builder.html#com_google_cloud_video_stitcher_v1_CreateVodConfigRequest_Builder_setVodConfigId_java_lang_String_)(vodConfigId)
                  .setVodConfig(
                      [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html).newBuilder().setSourceUri(sourceUri).setAdTagUri(adTagUri).build())
                  .build();
    
          [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) response =
              videoStitcherServiceClient
                  .[createVodConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_createVodConfigAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_LocationName_com_google_cloud_video_stitcher_v1_VodConfig_java_lang_String_)(createVodConfigRequest)
                  .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Created new VOD config: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html#com_google_cloud_video_stitcher_v1_VodConfig_getName__)());
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
    // vodConfigId = 'my-vod-config-id';
    // sourceUri = 'https://storage.googleapis.com/my-bucket/main.mpd';
    // See VMAP Pre-roll
    // (https://developers.google.com/interactive-media-ads/docs/sdks/html5/client-side/tags)
    // adTagUri = 'https://pubads.g.doubleclick.net/gampad/ads...';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function createVodConfig() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        vodConfig: {
          sourceUri: sourceUri,
          adTagUri: adTagUri,
        },
        vodConfigId: vodConfigId,
      };
      const [operation] = await stitcherClient.createVodConfig(request);
      const [response] = await operation.promise();
      console.log(`response.name: ${response.name}`);
    }
    
    createVodConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateVodConfigRequest;
    use Google\Cloud\Video\Stitcher\V1\VodConfig;
    
    /**
     * Creates a VOD config. VOD configs are used to configure VOD sessions.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the VOD config
     * @param string $vodConfigId          The name of the VOD config to be created
     * @param string $sourceUri            Uri of the media to stitch; this URI must
     *                                     reference either an MPEG-DASH manifest
     *                                     (.mpd) file or an M3U playlist manifest
     *                                     (.m3u8) file.
     * @param string $adTagUri             The Uri of the ad tag
     */
    function create_vod_config(
        string $callingProjectId,
        string $location,
        string $vodConfigId,
        string $sourceUri,
        string $adTagUri
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
    
        $vodConfig = (new VodConfig())
            ->setSourceUri($sourceUri)
            ->setAdTagUri($adTagUri);
    
        // Run VOD config creation request
        $request = (new CreateVodConfigRequest())
            ->setParent($parent)
            ->setVodConfigId($vodConfigId)
            ->setVodConfig($vodConfig);
        $operationResponse = $stitcherClient->createVodConfig($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('VOD config: %s' . PHP_EOL, $result->getName());
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def create_vod_config(
        project_id: str,
        location: str,
        vod_config_id: str,
        vod_uri: str,
        ad_tag_uri: str,
    ) -> stitcher_v1.types.VodConfig:
        """Creates a VOD config.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the VOD config.
            vod_config_id: The user-defined VOD config ID.
            vod_uri: URI of the VOD to stitch; this URI must reference either an
                        MPEG-DASH manifest (.mpd) file or an M3U playlist manifest
                        (.m3u8) file.
            ad_tag_uri: Uri of the ad tag.
    
        Returns:
            The VOD config resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        vod_config = stitcher_v1.types.VodConfig(
            source_uri=vod_uri,
            ad_tag_uri=ad_tag_uri,
        )
    
        operation = client.create_vod_config(
            parent=parent, vod_config_id=vod_config_id, vod_config=vod_config
        )
        response = operation.result()
        print(f"VOD config: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create a VOD config. VOD configs are used to create VOD sessions.
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] Your VOD config name (e.g. `my-vod-config`)
    # @param source_uri [String] Uri of the VOD stream to stitch
    #   (e.g. `https://storage.googleapis.com/my-bucket/main.mpd`)
    # @param ad_tag_uri [String] Uri of the ad tag
    #   (e.g. `https://pubads.g.doubleclick.net/gampad/ads...`)
    #
    def create_vod_config project_id:, location:, vod_config_id:, source_uri:,
                          ad_tag_uri:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      # Set the VOD config fields.
      new_vod_config = {
        source_uri: source_uri,
        ad_tag_uri: ad_tag_uri
      }
    
      operation = client.create_vod_config parent: parent,
                                           vod_config_id: vod_config_id,
                                           vod_config: new_vod_config
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the VOD config name.
      puts "VOD config: #{operation.response.name}"
    end

### Check for the result

To check if the VOD config has been created, use the [`projects.locations.operations.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.operations/get) method. If the response contains `"done: false"`, repeat the command until the response contains `"done: true"`.

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
        "state": "READY"
      }
    }
    

## Get a VOD config

To get the details for a specific VOD config, use the [`projects.locations.vodConfigs.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/get) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the VOD config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `VOD_CONFIG_ID`: the user-defined identifier for the VOD config



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "state": "READY"
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class GetVodConfigSample
    {
        public VodConfig GetVodConfig(
            string projectId, string location, string vodConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [GetVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodConfigRequest.html) request = new [GetVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodConfigRequest.html)
            {
                VodConfigName = [VodConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html).[FromProjectLocationVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html#Google_Cloud_Video_Stitcher_V1_VodConfigName_FromProjectLocationVodConfig_System_String_System_String_System_String_)(projectId, location, vodConfigId)
            };
    
            // Call the API.
            [VodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfig.html) response = client.[GetVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_GetVodConfig_Google_Cloud_Video_Stitcher_V1_GetVodConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
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
    
    // getVodConfig gets a previously-created VOD config.
    func getVodConfig(w io.Writer, projectID, vodConfigID string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.GetVodConfigRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/vodConfigs/%s", projectID, location, vodConfigID),
    	}
    
    	response, err := client.GetVodConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetVodConfig: %w", err)
    	}
    	b, err := json.MarshalIndent(response, "", " ")
    	if err != nil {
    		return fmt.Errorf("json.MarshalIndent: %w", err)
    	}
    
    	fmt.Fprintf(w, "VOD config:\n%s", string(b))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html);
    import com.google.cloud.video.stitcher.v1.[VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html);
    import java.io.IOException;
    
    public class GetVodConfig {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
    
        getVodConfig(projectId, location, vodConfigId);
      }
    
      // Gets a video on demand (VOD) config.
      public static [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) getVodConfig(String projectId, String location, String vodConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest.html) getVodConfigRequest =
              [GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest.html).newBuilder()
                  .setName([VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html).of(projectId, location, vodConfigId).toString())
                  .build();
    
          [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) response = videoStitcherServiceClient.getVodConfig(getVodConfigRequest);
          System.out.println("VOD config: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html#com_google_cloud_video_stitcher_v1_VodConfig_getName__)());
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
    // vodConfigId = 'my-vod-config-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function getVodConfig() {
      // Construct request
      const request = {
        name: stitcherClient.[vodConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, vodConfigId),
      };
      const [vodConfig] = await stitcherClient.getVodConfig(request);
      console.log(`VOD config: ${vodConfig.name}`);
    }
    
    getVodConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\GetVodConfigRequest;
    
    /**
     * Gets a VOD config.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the VOD config
     * @param string $vodConfigId         The ID of the VOD config
     */
    function get_vod_config(
        string $callingProjectId,
        string $location,
        string $vodConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodConfigName($callingProjectId, $location, $vodConfigId);
        $request = (new GetVodConfigRequest())
            ->setName($formattedName);
        $vodConfig = $stitcherClient->getVodConfig($request);
    
        // Print results
        printf('VOD config: %s' . PHP_EOL, $vodConfig->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def get_vod_config(
        project_id: str, location: str, vod_config_id: str
    ) -> stitcher_v1.types.VodConfig:
        """Gets a VOD config.
        Args:
            project_id: The GCP project ID.
            location: The location of the VOD config.
            vod_config_id: The user-defined VOD config ID.
    
        Returns:
            The VOD config resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/vodConfigs/{vod_config_id}"
        response = client.get_vod_config(name=name)
        print(f"VOD config: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Get a VOD config
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] Your VOD config name (e.g. `my-vod-config`)
    #
    def get_vod_config project_id:, location:, vod_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the VOD config.
      name = client.vod_config_path project: project_id, location: location,
                                    vod_config: vod_config_id
    
      # Get the VOD config.
      vod_config = client.get_vod_config name: name
    
      # Print the vod config name.
      puts "VOD config: #{vod_config.name}"
    end

## Update a VOD config

To update a VOD config, use the [`projects.locations.vodConfigs.patch`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/patch) method. The following example updates the `sourceUri` field.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the VOD config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `VOD_CONFIG_ID`: the user-defined identifier for the VOD config
  * `VOD_URI`: the updated URI of the media to stitch 



Request JSON body: 
    
    
    {
      "sourceUri": "VOD_URI"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "sourceUri": "VOD_URI"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID?updateMask=sourceUri"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "sourceUri": "VOD_URI"
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
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID?updateMask=sourceUri" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
        "verb": "update"
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
    
    public class UpdateVodConfigSample
    {
        public async Task<VodConfig> UpdateVodConfigAsync(
            string projectId, string location, string vodConfigId, string sourceUri)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [UpdateVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.UpdateVodConfigRequest.html) request = new [UpdateVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.UpdateVodConfigRequest.html)
            {
                VodConfig = new [VodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfig.html)
                {
                    VodConfigName = [VodConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html).[FromProjectLocationVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html#Google_Cloud_Video_Stitcher_V1_VodConfigName_FromProjectLocationVodConfig_System_String_System_String_System_String_)(projectId, location, vodConfigId),
                    SourceUri = sourceUri,
                },
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) { Paths = { "sourceUri" } }
            };
    
            // Make the request.
            Operation<VodConfig, OperationMetadata> response = await client.[UpdateVodConfigAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_UpdateVodConfigAsync_Google_Cloud_Video_Stitcher_V1_UpdateVodConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<VodConfig, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
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
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    // updateVodConfig updates an existing VOD config. This sample updates the sourceURI for an
    // existing VOD config.
    func updateVodConfig(w io.Writer, projectID, vodConfigID, sourceURI string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    	// sourceURI := "https://storage.googleapis.com/my-bucket/main.mpd"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.UpdateVodConfigRequest{
    		VodConfig: &stitcherstreampb.VodConfig{
    			Name:      fmt.Sprintf("projects/%s/locations/%s/vodConfigs/%s", projectID, location, vodConfigID),
    			SourceUri: sourceURI,
    		},
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{
    				"sourceUri",
    			},
    		},
    	}
    	// Updates the VOD config.
    	op, err := client.UpdateVodConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.UpdateVodConfig: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Updated VOD config: %+v", response)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html);
    import com.google.cloud.video.stitcher.v1.[VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateVodConfig {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
        // Updated URI of the VOD stream to stitch; this URI must reference either an MPEG-DASH
        // manifest (.mpd) file or an M3U playlist manifest (.m3u8) file.
        String sourceUri = "https://storage.googleapis.com/my-bucket/main.mpd";
    
        updateVodConfig(projectId, location, vodConfigId, sourceUri);
      }
    
      // Updates the source URI in a video on demand (VOD) config.
      public static [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) updateVodConfig(
          String projectId, String location, String vodConfigId, String sourceUri)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest.html) updateVodConfigRequest =
              [UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest.html).newBuilder()
                  .setVodConfig(
                      [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html).newBuilder()
                          .setName([VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html).of(projectId, location, vodConfigId).toString())
                          .setSourceUri(sourceUri)
                          .build())
                  // Set the update mask to the sourceUri field in the existing VOD config. You must set
                  // the mask to the field you want to update.
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("sourceUri").build())
                  .build();
    
          [VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) response =
              videoStitcherServiceClient
                  .[updateVodConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_updateVodConfigAsync_com_google_cloud_video_stitcher_v1_UpdateVodConfigRequest_)(updateVodConfigRequest)
                  .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Updated VOD config: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html#com_google_cloud_video_stitcher_v1_VodConfig_getName__)());
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
    // vodConfigId = 'my-vod-config-id';
    // sourceUri = 'https://storage.googleapis.com/my-bucket/main.mpd';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function updateVodConfig() {
      // Construct request
      const request = {
        vodConfig: {
          name: stitcherClient.[vodConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, vodConfigId),
          sourceUri: sourceUri,
        },
        updateMask: {
          paths: ['sourceUri'],
        },
      };
    
      const [operation] = await stitcherClient.updateVodConfig(request);
      const [response] = await operation.promise();
      console.log(`Updated VOD config: ${response.name}`);
      console.log(`Updated sourceUri: ${response.sourceUri}`);
    }
    
    updateVodConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\UpdateVodConfigRequest;
    use Google\Cloud\Video\Stitcher\V1\VodConfig;
    use Google\Protobuf\FieldMask;
    
    /**
     * Updates the VOD config's sourceUri field.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the VOD config
     * @param string $vodConfigId          The name of the VOD config to update
     * @param string $sourceUri            Updated uri of the media to stitch; this URI must
     *                                     reference either an MPEG-DASH manifest
     *                                     (.mpd) file or an M3U playlist manifest
     *                                     (.m3u8) file.
     */
    function update_vod_config(
        string $callingProjectId,
        string $location,
        string $vodConfigId,
        string $sourceUri
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodConfigName($callingProjectId, $location, $vodConfigId);
        $vodConfig = new VodConfig();
        $vodConfig->setName($formattedName);
        $vodConfig->setSourceUri($sourceUri);
        $updateMask = new FieldMask([
            'paths' => ['sourceUri']
        ]);
    
        // Run VOD config update request
        $request = (new UpdateVodConfigRequest())
            ->setVodConfig($vodConfig)
            ->setUpdateMask($updateMask);
        $operationResponse = $stitcherClient->updateVodConfig($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('Updated VOD config: %s' . PHP_EOL, $result->getName());
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    from google.protobuf import field_mask_pb2 as field_mask
    
    
    def update_vod_config(
        project_id: str, location: str, vod_config_id: str, vod_uri: str
    ) -> stitcher_v1.types.VodConfig:
        """Updates a VOD config.
        Args:
            project_id: The GCP project ID.
            location: The location of the VOD config.
            vod_config_id: The existing VOD config's ID.
            vod_uri: Updated URI of the VOD to stitch; this URI must reference
                        either an MPEG-DASH manifest (.mpd) file or an M3U playlist
                        manifest (.m3u8) file.
    
        Returns:
            The VOD config resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/vodConfigs/{vod_config_id}"
        vod_config = stitcher_v1.types.VodConfig(
            name=name,
            source_uri=vod_uri,
        )
        update_mask = field_mask.FieldMask(paths=["sourceUri"])
    
        operation = client.update_vod_config(vod_config=vod_config, update_mask=update_mask)
        response = operation.result()
        print(f"Updated VOD config: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Update a VOD config
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] Your VOD config name (e.g. `my-vod-config`)
    # @param source_uri [String] Updated URI of the VOD stream to stitch
    #   (e.g. `https://storage.googleapis.com/my-bucket/main.mpd`)
    #
    def update_vod_config project_id:, location:, vod_config_id:, source_uri:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the VOD config.
      name = client.vod_config_path project: project_id, location: location,
                                    vod_config: vod_config_id
    
      # Set the update mask.
      update_mask = { paths: ["sourceUri"] }
    
      # Set the VOD config fields.
      update_vod_config = {
        name: name,
        source_uri: source_uri
      }
    
      operation = client.update_vod_config vod_config: update_vod_config, update_mask: update_mask
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the VOD config name and updated source URI.
      puts "Updated VOD config: #{operation.response.name}"
      puts "Updated source URI: #{operation.response.source_uri}"
    end

## List all registered VOD configs

To list all of the VOD configs registered for a given location in a project, use the [`projects.locations.vodConfigs.list`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/list) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the VOD configs; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

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
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "vodConfigs": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
          "sourceUri": "VOD_URI",
          "adTagUri": "AD_TAG_URI",
          "state": "READY"
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/my-other-vod-config",
          "sourceUri": "my-other-vod-stream-uri",
          "adTagUri": "my-other-ad-tag-uri",
          "state": "READY"
        }
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using System;
    
    public class ListVodConfigsSample
    {
        public PagedEnumerable<ListVodConfigsResponse, VodConfig> ListVodConfigs(
            string projectId, string regionId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [ListVodConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ListVodConfigsRequest.html) request = new [ListVodConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ListVodConfigsRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, regionId)
            };
    
            // Make the request.
            PagedEnumerable<ListVodConfigsResponse, VodConfig> response = client.[ListVodConfigs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_ListVodConfigs_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
            foreach ([VodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfig.html) vodConfig in response)
            {
                Console.WriteLine($"{vodConfig.Name}");
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
    
    // listVodConfigs lists all VOD configs for a given location.
    func listVodConfigs(w io.Writer, projectID string) error {
    	// projectID := "my-project-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.ListVodConfigsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    
    	it := client.ListVodConfigs(ctx, req)
    	fmt.Fprintln(w, "VOD configs:")
    
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
    
    
    import com.google.cloud.video.stitcher.v1.[ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).[ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse.html);
    import com.google.cloud.video.stitcher.v1.[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html);
    import java.io.IOException;
    
    public class ListVodConfigs {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
    
        listVodConfigs(projectId, location);
      }
    
      // Lists all the video on demand (VOD) configs for a given project and locatin.
      public static [ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse.html) listVodConfigs(String projectId, String location)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest.html) listVodConfigsRequest =
              [ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .build();
    
          [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).[ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse.html) response =
              videoStitcherServiceClient.listVodConfigs(listVodConfigsRequest);
    
          System.out.println("VOD configs:");
          for ([VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig.html) vodConfig : response.iterateAll()) {
            System.out.println(vodConfig.getName());
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
    
    async function listVodConfigs() {
      const iterable = await stitcherClient.[listVodConfigsAsync](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)({
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
      });
      console.info('VOD configs:');
      for await (const response of iterable) {
        console.log(response.name);
      }
    }
    
    listVodConfigs().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\ListVodConfigsRequest;
    
    /**
     * Lists all VOD configs for a location.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the VOD configs
     */
    function list_vod_configs(
        string $callingProjectId,
        string $location
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $request = (new ListVodConfigsRequest())
            ->setParent($parent);
        $response = $stitcherClient->listVodConfigs($request);
    
        // Print the VOD config list.
        $vodConfigs = $response->iterateAllElements();
        print('VOD configs:' . PHP_EOL);
        foreach ($vodConfigs as $vodConfig) {
            printf('%s' . PHP_EOL, $vodConfig->getName());
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
    
    
    def list_vod_configs(project_id: str, location: str) -> pagers.ListVodConfigsPager:
        """Lists all VOD configs in a location.
        Args:
            project_id: The GCP project ID.
            location: The location of the VOD configs.
    
        Returns:
            An iterable object containing VOD config resources.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        response = client.list_vod_configs(parent=parent)
        print("VOD configs:")
        for vod_config in response.vod_configs:
            print({vod_config.name})
    
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # List VOD configs for a given location
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    #
    def list_vod_configs project_id:, location:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      response = client.list_vod_configs parent: parent
    
      puts "VOD configs:"
      # Print out all VOD configs.
      response.each do |vod_config|
        puts vod_config.name
      end
    end

### Additional results

The `curl` response may include a `nextPageToken`, which you can use to retrieve additional results:
    
    
    {
      "vodConfigs": [
        ...
      ],
      "nextPageToken": "NEXT_PAGE_TOKEN"
    }
    

You can send another `curl` request, including the value of NEXT_PAGE_TOKEN, to list the additional configs. Append the following to the URL in the preceding API call:
    
    
    ?pageToken=NEXT_PAGE_TOKEN
    

See the relevant [client library](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries) for more information on using this token.

## Delete a VOD config

If a registered VOD config is no longer needed, delete it using the [`projects.locations.vodConfigs.delete`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs/delete) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number; this is located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of the VOD config; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `VOD_CONFIG_ID`: the user-defined identifier for the VOD config



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.common.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
        "verb": "delete"
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
    
    public class DeleteVodConfigSample
    {
        public async Task DeleteVodConfigAsync(
            string projectId, string location, string vodConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [DeleteVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteVodConfigRequest.html) request = new [DeleteVodConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteVodConfigRequest.html)
            {
                VodConfigName = [VodConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html).[FromProjectLocationVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html#Google_Cloud_Video_Stitcher_V1_VodConfigName_FromProjectLocationVodConfig_System_String_System_String_System_String_)(projectId, location, vodConfigId)
            };
    
            // Make the request.
            Operation<Empty, OperationMetadata> response = await client.[DeleteVodConfigAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_DeleteVodConfigAsync_Google_Cloud_Video_Stitcher_V1_DeleteVodConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
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
    
    // deleteVodConfig deletes a previously-created VOD config.
    func deleteVodConfig(w io.Writer, projectID, vodConfigID string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.DeleteVodConfigRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/vodConfigs/%s", projectID, location, vodConfigID),
    	}
    	// Deletes the VOD config.
    	op, err := client.DeleteVodConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.DeleteVodConfig: %w", err)
    	}
    	err = op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Deleted VOD config")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteVodConfig {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
    
        deleteVodConfig(projectId, location, vodConfigId);
      }
    
      // Deletes a video on demand (VOD) config.
      public static void deleteVodConfig(String projectId, String location, String vodConfigId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest.html) deleteVodConfigRequest =
              [DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest.html).newBuilder()
                  .setName([VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html).of(projectId, location, vodConfigId).toString())
                  .build();
    
          videoStitcherServiceClient
              .[deleteVodConfigAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_deleteVodConfigAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_VodConfigName_)(deleteVodConfigRequest)
              .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Deleted VOD config");
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
    // vodConfigId = 'my-vod-config-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function deleteVodConfig() {
      // Construct request
      const request = {
        name: stitcherClient.[vodConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, vodConfigId),
      };
      const [operation] = await stitcherClient.deleteVodConfig(request);
      await operation.promise();
      console.log('Deleted VOD config');
    }
    
    deleteVodConfig().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\DeleteVodConfigRequest;
    
    /**
     * Deletes a VOD config.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the VOD config
     * @param string $vodConfigId         The ID of the VOD config
     */
    function delete_vod_config(
        string $callingProjectId,
        string $location,
        string $vodConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodConfigName($callingProjectId, $location, $vodConfigId);
        $request = (new DeleteVodConfigRequest())
            ->setName($formattedName);
        $operationResponse = $stitcherClient->deleteVodConfig($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            // Print status
            printf('Deleted VOD config %s' . PHP_EOL, $vodConfigId);
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
    
    
    def delete_vod_config(
        project_id: str, location: str, vod_config_id: str
    ) -> empty.Empty:
        """Deletes a VOD config.
        Args:
            project_id: The GCP project ID.
            location: The location of the VOD config.
            vod_config_id: The user-defined VOD config ID."""
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/vodConfigs/{vod_config_id}"
        operation = client.delete_vod_config(name=name)
        response = operation.result()
        print("Deleted VOD config")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Delete a VOD config
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] Your VOD config name (e.g. `my-vod-config`)
    #
    def delete_vod_config project_id:, location:, vod_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the VOD config.
      name = client.vod_config_path project: project_id, location: location,
                                    vod_config: vod_config_id
    
      # Delete the VOD config.
      operation = client.delete_vod_config name: name
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print a success message.
      puts "Deleted VOD config"
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
