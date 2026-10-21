---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-create-live-config/
title: Create a live config \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:37.937133+00:00
---

# Create a live config  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-create-live-config/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  Create a live config Stay organized with collections  Save and categorize content based on your preferences. 

Create a live config to apply to live sessions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage a live config](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-configs)
  * [Insert ads into livestreams](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-live)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videostitcherapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
