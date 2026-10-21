---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions-gam/
title: Manage a live session enabled by Google Ad Manager \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:03.377913+00:00
---

# Manage a live session enabled by Google Ad Manager  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions-gam/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Manage a live session enabled by Google Ad Manager Stay organized with collections  Save and categorize content based on your preferences. 

Using the Video Stitcher API, you create a live session each time you start playback of a livestream in which ads served by Google Ad Manager are dynamically stitched during ad breaks. The response contains the playback URL and the configuration of the live session.

This page describes how to create and manage a live session that is enabled by Google Ad Manager. For information on live sessions that _don't_ use Google Ad Manager, see [Manage a live session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions).

## Before you begin

  * [Create a live config](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/create-live-configs). For the integration with Google Ad Manager, ensure that the [`gamLiveConfig`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveConfigs#LiveConfig.FIELDS.gam_live_config) object is set.
  * If you are specifying a slate, ensure that the [`gamSlate`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.slates#Slate.FIELDS.gam_slate) object is set on the slate you register.



## Create a live session

You can create a live session by using the IMA SDK (which calls the Video Stitcher API) or by using the Video Stitcher API directly.

### Use the IMA SDK

If you are [integrating with the IMA SDK](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/overview), the IMA SDK creates the live session.
    
    
    function requestVideoStitcherStream() {
      const streamRequest = new google.ima.dai.api.VideoStitcherLiveStreamRequest();
      streamRequest.liveStreamEventId = 'LIVE_CONFIG_ID';
      streamRequest.region = 'LOCATION';
      streamRequest.projectNumber = 'PROJECT_NUMBER';
      streamRequest.oAuthToken = 'OAUTH_TOKEN';
      streamRequest.networkCode = 'NETWORK_CODE';
      streamRequest.customAssetKey = 'CUSTOM_ASSET_KEY';
    
      streamManager.requestStream(streamRequest);
    }

You can set or override the following optional parameters per session:

  * [`manifestOptions`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions#LiveSession.FIELDS.manifest_options): specifies which video renditions are generated in the stitched video manifest and the ordering of the renditions; see the [manifest options](https://docs.cloud.google.com/video-stitcher/docs/concepts/manifest-options) documentation
  * [`adTracking`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions#LiveSession.FIELDS.ad_tracking): select either client-side ad tracking or server-side ad tracking
  * [`targetingParameters`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions#GamSettings.FIELDS.targeting_parameters): a Google Ad Manager ad tag can contain [targeting parameters that can be updated](https://support.google.com/admanager/answer/7320899) per session; see [how to set targeting parameters with the IMA SDK](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/html5/reference/js/VideoStitcherLiveStreamRequest#adTagParameters)



See the next section to learn how to set these parameters using the IMA SDK.

#### Optional parameters and overrides

You can set optional parameters per session, like the `manifestOptions` field. This field is not available in the live config. You can also override certain parameters that are set in the live config for a given session.

For example, if the default `adTracking` on the live config is set to `SERVER`, you can override that value to `CLIENT` and also set the `manifestOptions` field in the IMA SDK by setting the `videoStitcherSessionOptions` JSON object field.
    
    
    function requestVideoStitcherStream() {
      const streamRequest = new google.ima.dai.api.VideoStitcherLiveStreamRequest();
      streamRequest.liveStreamEventId = 'LIVE_CONFIG_ID';
      streamRequest.region = 'LOCATION';
      streamRequest.projectNumber = 'PROJECT_NUMBER';
      streamRequest.oAuthToken = 'OAUTH_TOKEN';
      streamRequest.networkCode = 'NETWORK_CODE';
      streamRequest.customAssetKey = 'CUSTOM_ASSET_KEY';
      streamRequest.videoStitcherSessionOptions = {
        adTracking: 'CLIENT',
        'manifestOptions': {
          'includeRenditions': [
            {
              'bitrateBps': 150000,
              'codecs': 'hvc1.1.4.L126.B0'
            },
            {
              'bitrateBps': 440000,
              'codecs': 'hvc1.1.4.L126.B0'
            },
          ],
          'bitrateOrder': 'descending'
        }
      };
      streamRequest.adTagParameters = {
        "key1": "value1",
        "key2": "value2",
      };
    
      streamManager.requestStream(streamRequest);
    }

For more information, see [Add streaming session options](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/live/ima-sdk/html5#optional_add_streaming_session_options).

### Use the API directly

To create a live session using the API directly, use the [`projects.locations.liveSessions.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions/create) method.

The `liveConfig` field is the only required field in the JSON body. You can set or override the following optional parameters per live session (as shown in the following REST example):

  * [`manifestOptions`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions#LiveSession.FIELDS.manifest_options): specifies which video renditions are generated in the stitched video manifest and the ordering of the renditions; see the [manifest options](https://docs.cloud.google.com/video-stitcher/docs/concepts/manifest-options) documentation
  * [`adTracking`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions#LiveSession.FIELDS.ad_tracking): select either client-side ad tracking or server-side ad tracking; this overrides the value in the live config for the session
  * [`targetingParameters`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions#GamSettings.FIELDS.targeting_parameters): a Google Ad Manager ad tag can contain [targeting parameters that can be updated](https://support.google.com/admanager/answer/7320899) per session; provide a mapping in this field (for example, to replace the `[my_key]` macro with the string `my_value`, see the REST example)



### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your session; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

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

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "liveConfig": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
      "manifestOptions": {
        "includeRenditions": [
          {
            "bitrateBps": 150000,
            "codecs": "hvc1.1.4.L126.B0"
          },
          {
            "bitrateBps": 440000,
            "codecs": "hvc1.1.4.L126.B0"
          }
        ],
        "bitrateOrder": "DESCENDING"
      },
      "adTracking": "SERVER",
      "gamSettings": {
        "targetingParameters": {
          "my_key": "my_value",
        },
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveSessions"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "liveConfig": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
      "manifestOptions": {
        "includeRenditions": [
          {
            "bitrateBps": 150000,
            "codecs": "hvc1.1.4.L126.B0"
          },
          {
            "bitrateBps": 440000,
            "codecs": "hvc1.1.4.L126.B0"
          }
        ],
        "bitrateOrder": "DESCENDING"
      },
      "adTracking": "SERVER",
      "gamSettings": {
        "targetingParameters": {
          "my_key": "my_value",
        },
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
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveSessions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveSessions/SESSION_ID",
      "playUri": "PLAY_URI",
      "manifestOptions": {
        "includeRenditions": [
          {
            "bitrateBps": 150000,
            "codecs": "hvc1.1.4.L126.B0"
          },
          {
            "bitrateBps": 440000,
            "codecs": "hvc1.1.4.L126.B0"
          }
        ],
        "bitrateOrder": "DESCENDING"
      },
      "gamSettings": {
        "streamId": "STREAM_ID"
      },
      "liveConfig": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
      "adTracking": "SERVER"
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class CreateLiveSessionSample
    {
        public LiveSession CreateLiveSession(
            string projectId, string location, string liveConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CreateLiveSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest.html) request = new [CreateLiveSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest.html)
            {
                Parent = $"projects/{projectId}/locations/{location}",
                LiveSession = new [LiveSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveSession.html)
                {
                    LiveConfig = [LiveConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfigName.html).[FormatProjectLocationLiveConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveConfigName.html#Google_Cloud_Video_Stitcher_V1_LiveConfigName_FormatProjectLocationLiveConfig_System_String_System_String_System_String_)(projectId, location, liveConfigId)
                }
            };
    
            // Call the API.
            [LiveSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveSession.html) session = client.[CreateLiveSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateLiveSession_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_LiveSession_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return session;
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
    	"cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // createLiveSession creates a livestream session in which to insert ads.
    // Live sessions are ephemeral resources that expire after a few minutes.
    func createLiveSession(w io.Writer, projectID, liveConfigID string) error {
    	// projectID := "my-project-id"
    	// liveConfigID := "my-live-config"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherpb.CreateLiveSessionRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		LiveSession: &stitcherpb.LiveSession{
    			LiveConfig: fmt.Sprintf("projects/%s/locations/%s/liveConfigs/%s", projectID, location, liveConfigID),
    		},
    	}
    	// Creates the live session.
    	response, err := client.CreateLiveSession(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateLiveSession: %w", err)
    	}
    
    	fmt.Fprintf(w, "Live session: %v\n", response.GetName())
    	fmt.Fprintf(w, "Play URI: %v", response.GetPlayUri())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[CreateLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveSessionRequest.html);
    import com.google.cloud.video.stitcher.v1.[LiveConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfigName.html);
    import com.google.cloud.video.stitcher.v1.[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    
    public class CreateLiveSession {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String liveConfigId = "my-live-config-id";
    
        createLiveSession(projectId, location, liveConfigId);
      }
    
      // Creates a live session given the parameters in the supplied live config.
      // For more information, see
      // https://cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions.
      public static [LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html) createLiveSession(
          String projectId, String location, String liveConfigId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CreateLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveSessionRequest.html) createLiveSessionRequest =
              [CreateLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveSessionRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .setLiveSession(
                      [LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html).newBuilder()
                          .setLiveConfig([LiveConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfigName.html).format(projectId, location, liveConfigId)))
                  .build();
    
          [LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html) response = videoStitcherServiceClient.createLiveSession(createLiveSessionRequest);
          System.out.println("Created live session: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html#com_google_cloud_video_stitcher_v1_LiveSession_getName__)());
          System.out.println("Play URI: " + response.[getPlayUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html#com_google_cloud_video_stitcher_v1_LiveSession_getPlayUri__)());
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
    
    async function createLiveSession() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        liveSession: {
          liveConfig: stitcherClient.[liveConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(
            projectId,
            location,
            liveConfigId
          ),
        },
      };
    
      const [session] = await stitcherClient.createLiveSession(request);
      console.log(`Live session: ${session.name}`);
      console.log(`Play URI: ${session.playUri}`);
    }
    
    createLiveSession().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateLiveSessionRequest;
    use Google\Cloud\Video\Stitcher\V1\LiveSession;
    
    /**
     * Creates a live session. Live sessions are ephemeral resources that expire
     * after a few minutes.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $liveConfigId         The live config ID to use to create the
     *                                     live session
     */
    function create_live_session(
        string $callingProjectId,
        string $location,
        string $liveConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $liveConfig = $stitcherClient->liveConfigName($callingProjectId, $location, $liveConfigId);
        $liveSession = new LiveSession();
        $liveSession->setLiveConfig($liveConfig);
    
        // Run live session creation request
        $request = (new CreateLiveSessionRequest())
            ->setParent($parent)
            ->setLiveSession($liveSession);
        $response = $stitcherClient->createLiveSession($request);
    
        // Print results
        printf('Live session: %s' . PHP_EOL, $response->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def create_live_session(
        project_id: str, location: str, live_config_id: str
    ) -> stitcher_v1.types.LiveSession:
        """Creates a live session. Live sessions are ephemeral resources that expire
        after a few minutes.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the session.
            live_config_id: The user-defined live config ID.
    
        Returns:
            The live session resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        live_config = (
            f"projects/{project_id}/locations/{location}/liveConfigs/{live_config_id}"
        )
    
        live_session = stitcher_v1.types.LiveSession(live_config=live_config)
    
        response = client.create_live_session(parent=parent, live_session=live_session)
        print(f"Live session: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create a live stream session. Live sessions are ephemeral resources
    # that expire after a few minutes.
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param live_config_id [String] Your live config name (e.g. `my-live-config`)
    #
    def create_live_session project_id:, location:, live_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      # Build the resource name of the live config.
      live_config_name = client.live_config_path project: project_id,
                                                 location: location,
                                                 live_config: live_config_id
    
      # Set the session fields.
      new_live_session = {
        live_config: live_config_name
      }
    
      response = client.create_live_session parent: parent,
                                            live_session: new_live_session
    
      # Print the live session name.
      puts "Live session: #{response.name}"
    end

The response is a [live session object](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions). The `playUri` is the URL the client device uses to play the ad stitched stream for this live session.

The Video Stitcher API generates a unique session ID for each request. A session expires if the `playUri` is not requested within the past 5 minutes.

If you're generating a session on behalf of your customers' devices, you can set the following parameters using HTTP headers:

Parameter | HTTP Header  
---|---  
CLIENT_IP | `x-forwarded-for`  
REFERRER_URL | `referer`  
USER_AGENT | `user-agent`  
  
You can add the following headers to the preceding `curl` request:
    
    
    -H "x-forwarded-for: CLIENT_IP" \
    -H "referer: REFERRER_URL" \
    -H "user-agent: USER_AGENT" \

If the `x-forwarded-for` header is not provided, the Video Stitcher API uses the client's IP address in ad metadata requests. Be aware that the client's IP address may not match the IP of your customers' devices if sessions are generated on behalf of your customers' devices.

## Get a session

To get the live session, use the [`projects.locations.liveSessions.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions/get) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location in which to create your session; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `SESSION_ID`: the identifier for the live session



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveSessions/SESSION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/liveSessions/SESSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/liveSessions/SESSION_ID",
      "playUri": "ad-stitched-live-stream-uri",
      "manifestOptions": {
        "includeRenditions": [
          {
            "bitrateBps": 150000,
            "codecs": "hvc1.1.4.L126.B0"
          },
          {
            "bitrateBps": 440000,
            "codecs": "hvc1.1.4.L126.B0"
          }
        ],
        "bitrateOrder": "DESCENDING"
      },
      "gamSettings": {
        "streamId": "STREAM_ID",
        "targetingParameters": {
          "my_key": "my_value"
        }
      },
      "liveConfig": "projects/PROJECT_NUMBER/locations/LOCATION/liveConfigs/LIVE_CONFIG_ID",
      "adTracking": "SERVER"
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class GetLiveSessionSample
    {
        public LiveSession GetLiveSession(
            string projectId, string location, string sessionId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [GetLiveSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetLiveSessionRequest.html) request = new [GetLiveSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetLiveSessionRequest.html)
            {
                LiveSessionName = [LiveSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveSessionName.html).[FromProjectLocationLiveSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveSessionName.html#Google_Cloud_Video_Stitcher_V1_LiveSessionName_FromProjectLocationLiveSession_System_String_System_String_System_String_)(projectId, location, sessionId)
            };
    
            // Call the API.
            [LiveSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveSession.html) session = client.[GetLiveSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_GetLiveSession_Google_Cloud_Video_Stitcher_V1_GetLiveSessionRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return session;
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
    	"cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // getLiveSession gets a livestream session by ID.
    func getLiveSession(w io.Writer, projectID, sessionID string) error {
    	// projectID := "my-project-id"
    	// sessionID := "123-456-789"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherpb.GetLiveSessionRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/liveSessions/%s", projectID, location, sessionID),
    	}
    	// Gets the session.
    	response, err := client.GetLiveSession(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetLiveSession: %w", err)
    	}
    
    	fmt.Fprintf(w, "Live session: %+v", response)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[GetLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveSessionRequest.html);
    import com.google.cloud.video.stitcher.v1.[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html);
    import com.google.cloud.video.stitcher.v1.[LiveSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSessionName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    
    public class GetLiveSession {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String sessionId = "my-session-id";
    
        getLiveSession(projectId, location, sessionId);
      }
    
      // Gets a live session.
      public static [LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html) getLiveSession(String projectId, String location, String sessionId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [GetLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveSessionRequest.html) getLiveSessionRequest =
              [GetLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveSessionRequest.html).newBuilder()
                  .setName([LiveSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSessionName.html).of(projectId, location, sessionId).toString())
                  .build();
    
          [LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html) response = videoStitcherServiceClient.getLiveSession(getLiveSessionRequest);
          System.out.println("Live session: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.html#com_google_cloud_video_stitcher_v1_LiveSession_getName__)());
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
    // sessionId = 'my-session-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function getLiveSession() {
      // Construct request
      const request = {
        name: stitcherClient.[liveSessionPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, sessionId),
      };
      const [session] = await stitcherClient.getLiveSession(request);
      console.log(`Live session: ${session.name}`);
    }
    
    getLiveSession().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\GetLiveSessionRequest;
    
    /**
     * Gets a live session.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $sessionId            The ID of the session
     */
    function get_live_session(
        string $callingProjectId,
        string $location,
        string $sessionId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->liveSessionName($callingProjectId, $location, $sessionId);
        $request = (new GetLiveSessionRequest())
            ->setName($formattedName);
        $session = $stitcherClient->getLiveSession($request);
    
        // Print results
        printf('Live session: %s' . PHP_EOL, $session->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def get_live_session(
        project_id: str, location: str, session_id: str
    ) -> stitcher_v1.types.LiveSession:
        """Gets a live session. Live sessions are ephemeral resources that expire
        after a few minutes.
        Args:
            project_id: The GCP project ID.
            location: The location of the session.
            session_id: The ID of the live session.
    
        Returns:
            The live session resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = client.live_session_path(project_id, location, session_id)
        response = client.get_live_session(name=name)
        print(f"Live session: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Get a live session. Live sessions are ephemeral resources
    # that expire after a few minutes.
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param session_id [String] The live session ID (e.g. `my-live-session-id`)
    #
    def get_live_session project_id:, location:, session_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the live session.
      name = client.live_session_path project: project_id, location: location,
                                      live_session: session_id
    
      # Get the live session.
      session = client.get_live_session name: name
    
      # Print the live session name.
      puts "Live session: #{session.name}"
    end

## Sample ad-stitched playlist

The following shows a sample source live playlist before ad-stitching:
    
    
    #EXTM3U
    #EXT-X-TARGETDURATION:10
    #EXT-X-VERSION:4
    #EXT-X-MEDIA-SEQUENCE:5
    #EXTINF:10.010
    segment_00005.ts
    #EXTINF:10.010
    segment_00006.ts
    #EXT-X-DATERANGE:ID="2415919105",START-DATE="2021-06-22T08:32:00Z",DURATION=60,SCTE35-OUT=0xF...
    #EXTINF:10.010
    segment_00007.ts
    #EXTINF:10.010
    segment_00008.ts
    #EXT-X-DATERANGE:ID="2415919105",START-DATE="2021-06-22T08:39:20Z",SCTE35-IN=0xF...
    #EXTINF:10.010
    segment_00009.ts
    

The following shows a sample source live playlist after ad-stitching:
    
    
    #EXTM3U
    #EXT-X-TARGETDURATION:10
    #EXT-X-VERSION:4
    #EXT-X-MEDIA-SEQUENCE:5
    #EXTINF:10.010
    segment_00005.ts
    #EXTINF:10.010
    segment_00006.ts
    #EXT-X-DISCONTINUITY
    #EXTINF:6.000
    https://dai.google.com/.../ad-1/seg-1.ts
    #EXTINF:5.000
    https://dai.google.com/.../ad-1/seg-2.ts
    #EXT-X-DISCONTINUITY
    #EXTINF:6.000
    https://dai.google.com/.../ad-2/seg-1.ts
    #EXTINF:5.000
    https://dai.google.com/.../ad-2/seg-2.ts
    #EXT-X-DISCONTINUITY
    #EXTINF:10.010
    segment_00009.ts
    

## Inspect live sessions enabled by Google Ad Manager

To see ad tag details for sessions, use the [Stream activity monitor](https://support.google.com/admanager/answer/7009058) in Ad Manager to see details about ad requests.

**Note:** You can't use the [ad tag details](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.liveSessions.liveAdTagDetails) endpoint for live sessions enabled by Google Ad Manager.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
