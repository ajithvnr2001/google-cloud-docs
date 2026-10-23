---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions-gam/
title: Manage a VOD session enabled by Google Ad Manager \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:02.866566+00:00
---

# Manage a VOD session enabled by Google Ad Manager  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions-gam/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Manage a VOD session enabled by Google Ad Manager Stay organized with collections  Save and categorize content based on your preferences. 

Using the Video Stitcher API, you create a video-on-demand (VOD) session each time you dynamically insert ads served by Google Ad Manager prior to delivery to client devices. When you create a session, the response includes the playback URL and information about the ads that you inserted into the video.

This page describes how to create and manage a VOD session that is enabled by Google Ad Manager. For information on VOD sessions that _don't_ use Google Ad Manager, see [Manage a VOD session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions).

## Before you begin

  * [Create a VOD config](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs). For the integration with Google Ad Manager, ensure that the [`gamVodConfig` object](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodConfigs#gamvodconfig) is set.



## Create a session

You can create a VOD session by using the IMA SDK (which calls the Video Stitcher API) or by using the Video Stitcher API directly.

### Use the IMA SDK

If you are [integrating with the IMA SDK](https://docs.cloud.google.com/video-stitcher/docs/how-to/gam/vod/playback-ima-sdk), the IMA SDK creates the VOD session.
    
    
    function requestVodVideoStitcherStream() {
      const streamRequest = new google.ima.dai.api.VideoStitcherVodStreamRequest();
      streamRequest.vodConfigId = 'VOD_CONFIG_ID';
      streamRequest.region = 'LOCATION';
      streamRequest.projectNumber = 'PROJECT_NUMBER';
      streamRequest.oAuthToken = 'OAUTH_TOKEN';
      streamRequest.networkCode = 'NETWORK_CODE';
    
      streamManager.requestStream(streamRequest);
    }

VOD sessions enabled by Google Ad Manager must use client-side ad tracking.

You can set or override the following optional parameters per session:

  * [`manifestOptions`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#VodSession.FIELDS.manifest_options): specifies which video renditions are generated in the stitched video manifest and the ordering of the renditions; see the [manifest options](https://docs.cloud.google.com/video-stitcher/docs/concepts/manifest-options) documentation
  * [`targetingParameters`](https://support.google.com/admanager/answer/7320899): a Google Ad Manager ad tag can contain [targeting parameters that can be updated](https://support.google.com/admanager/answer/7320899) per session; see [how to set targeting parameters with the IMA SDK](https://developers.google.com/ad-manager/dynamic-ad-insertion/sdk/html5/reference/js/VideoStitcherVodStreamRequest#adTagParameters)



See the next section to learn how to set these parameters using the IMA SDK.

#### Optional parameters and overrides
    
    
    function requestVodVideoStitcherStream() {
      const streamRequest = new google.ima.dai.api.VideoStitcherVodStreamRequest();
      streamRequest.vodConfigId = 'VOD_CONFIG_ID';
      streamRequest.region = 'LOCATION';
      streamRequest.projectNumber = 'PROJECT_NUMBER';
      streamRequest.oAuthToken = 'OAUTH_TOKEN';
      streamRequest.networkCode = 'NETWORK_CODE';
      streamRequest.videoStitcherSessionOptions = {
        manifestOptions: {
          "includeRenditions": [
            {
              "bitrateBps": 150000,
              "codecs": "hvc1.1.4.L126.B0"
            },
            {
              "bitrateBps": 440000,
              "codecs": "hvc1.1.4.L126.B0"
            },
          ],
          "bitrateOrder": "descending",
        },
      };
      streamRequest.adTagParameters = {
        "key1": "value1",
        "key2": "value2",
      };
    
      streamManager.requestStream(streamRequest);
    }

### Use the API directly

To create a session for an ad-stitched video, use the [`projects.locations.vodSessions.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions/create) method.

**Note:** You need to configure the [`gamSettings` object](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#gamsettings) in the following code samples. Also, VOD sessions enabled by Google Ad Manager must use client-side ad tracking.

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
  * `VOD_CONFIG_ID`: the user-defined identifier for the VOD config 



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
      "adTracking": "SERVER"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID",
      "adTracking": "SERVER"
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
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID",
      "interstitials": {
        "sessionContent": {
          "duration": "60s"
        }
      },
      "playUri": "PLAY_URI", # This is the ad-stitched VOD URI
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "assetId": "ASSET_ID",
      "adTracking": "SERVER",
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class CreateVodSessionSample
    {
        public VodSession CreateVodSession(
            string projectId, string location, string vodConfigId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CreateVodSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateVodSessionRequest.html) request = new [CreateVodSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateVodSessionRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, location),
                VodSession = new [VodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSession.html)
                {
                    VodConfig = [VodConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html).[FormatProjectLocationVodConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodConfigName.html#Google_Cloud_Video_Stitcher_V1_VodConfigName_FormatProjectLocationVodConfig_System_String_System_String_System_String_)(projectId, location, vodConfigId),
                    AdTracking = [AdTracking](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AdTracking.html).[Server](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AdTracking.html#Google_Cloud_Video_Stitcher_V1_AdTracking_Server)
                }
            };
    
            // Call the API.
            [VodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSession.html) session = client.[CreateVodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateVodSession_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_VodSession_Google_Api_Gax_Grpc_CallSettings_)(request);
    
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
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // createVodSession creates a video on demand (VOD) session in which to insert ads.
    // VOD sessions are ephemeral resources that expire after a few hours.
    func createVodSession(w io.Writer, projectID, vodConfigID string) error {
    	// projectID := "my-project-id"
    	// vodConfigID := "my-vod-config-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.CreateVodSessionRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		VodSession: &stitcherstreampb.VodSession{
    			VodConfig:  fmt.Sprintf("projects/%s/locations/%s/vodConfigs/%s", projectID, location, vodConfigID),
    			AdTracking: stitcherstreampb.AdTracking_SERVER,
    		},
    	}
    	// Creates the VOD session.
    	response, err := client.CreateVodSession(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateVodSession: %w", err)
    	}
    
    	fmt.Fprintf(w, "VOD session: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[AdTracking](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AdTracking.html);
    import com.google.cloud.video.stitcher.v1.[CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html);
    import com.google.cloud.video.stitcher.v1.[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html);
    import java.io.IOException;
    
    public class CreateVodSession {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String vodConfigId = "my-vod-config-id";
    
        createVodSession(projectId, location, vodConfigId);
      }
    
      // Creates a video on demand (VOD) session using the parameters in the designated VOD config.
      // For more information, see
      // https://cloud.google.com/video-stitcher/docs/how-to/creating-vod-sessions.
      public static [VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html) createVodSession(String projectId, String location, String vodConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest.html) createVodSessionRequest =
              [CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .setVodSession(
                      [VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html).newBuilder()
                          .setVodConfig([VodConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfigName.html).format(projectId, location, vodConfigId))
                          .setAdTracking([AdTracking](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AdTracking.html).SERVER)
                          .build())
                  .build();
    
          [VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html) response = videoStitcherServiceClient.createVodSession(createVodSessionRequest);
          System.out.println("Created VOD session: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html#com_google_cloud_video_stitcher_v1_VodSession_getName__)());
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
    
    async function createVodSession() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        vodSession: {
          vodConfig: stitcherClient.[vodConfigPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(
            projectId,
            location,
            vodConfigId
          ),
          adTracking: '[SERVER](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.adtracking.html)',
        },
      };
      const [session] = await stitcherClient.createVodSession(request);
      console.log(`VOD session: ${session.name}`);
    }
    
    createVodSession().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\AdTracking;
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateVodSessionRequest;
    use Google\Cloud\Video\Stitcher\V1\VodSession;
    
    /**
     * Creates a VOD session. VOD sessions are ephemeral resources that expire
     * after a few hours.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $vodConfigId          The name of the VOD config to use for the session
     */
    function create_vod_session(
        string $callingProjectId,
        string $location,
        string $vodConfigId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $vodConfig = $stitcherClient->vodConfigName($callingProjectId, $location, $vodConfigId);
        $vodSession = new VodSession();
        $vodSession->setVodConfig($vodConfig);
        $vodSession->setAdTracking(AdTracking::SERVER);
    
        // Run VOD session creation request
        $request = (new CreateVodSessionRequest())
            ->setParent($parent)
            ->setVodSession($vodSession);
        $response = $stitcherClient->createVodSession($request);
    
        // Print results
        printf('VOD session: %s' . PHP_EOL, $response->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def create_vod_session(
        project_id: str, location: str, vod_config_id: str
    ) -> stitcher_v1.types.VodSession:
        """Creates a VOD session. VOD sessions are ephemeral resources that expire
        after a few hours.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the session.
            vod_config_id: The user-defined VOD config ID to use to create the
                            session.
    
        Returns:
            The VOD session resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        vod_config_name = (
            f"projects/{project_id}/locations/{location}/vodConfigs/{vod_config_id}"
        )
    
        vod_session = stitcher_v1.types.VodSession(
            vod_config=vod_config_name, ad_tracking="SERVER"
        )
    
        response = client.create_vod_session(parent=parent, vod_session=vod_session)
        print(f"VOD session: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create a video on demand (VOD) session. VOD sessions are ephemeral resources
    # that expire after a few hours.
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param vod_config_id [String] The VOD config ID (e.g. `my-vod-config`) to use
    #
    def create_vod_session project_id:, location:, vod_config_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      # Build the resource name of the VOD config.
      vod_config_name = client.vod_config_path project: project_id,
                                               location: location,
                                               vod_config: vod_config_id
    
      # Set the session fields.
      new_vod_session = {
        vod_config: vod_config_name,
        ad_tracking: Google::Cloud::Video::Stitcher::V1::AdTracking::SERVER
      }
    
      response = client.create_vod_session parent: parent,
                                           vod_session: new_vod_session
    
      # Print the VOD session name.
      puts "VOD session: #{response.name}"
    end

The Video Stitcher API generates a unique session ID for each request. A session expires after 4 hours.

The response should now be similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID",
      "interstitials": {
        "adBreaks": [
          {
            "progressEvents": [
              {
                "timeOffset": "0s",
                "events": [
                  {
                    "type": "IMPRESSION",
                    "uri": "https://securepubads.g.doubleclick.net/pcs/view..."
                  },
                  {
                    "type": "START",
                    "uri": "https://pubads.g.doubleclick.net/pagead/interaction/..."
                  },
                  ...
                ]
              },
              ...
            ],
            "ads": [
              {
                "duration": "10s",
                "activityEvents": [
                  {
                    "type": "ERROR",
                    "uri": "https://pubads.g.doubleclick.net/pagead/interaction/..."
                  },
                  {
                    "type": "CLICK_THROUGH",
                    "uri": "https://pubads.g.doubleclick.net/pcs/click...",
                    "id": "GDFP"
                  },
                  ...
                ]
              }
            ],
            "endTimeOffset": "10s",
            "startTimeOffset": "0s"
          }
        ],
        "sessionContent": {
          "duration": "70s"
        }
      },
      "playUri": "PLAY_URI",
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "assetId": "ASSET_ID",
      "adTracking": "SERVER",
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"
    }
    

The response is a [`VodSession` object](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions) that contains the following fields:

  * A `name` field that shows the VOD SESSION_ID. Use this ID to get the session.
  * An `interstitials` field that contains metadata about the ads that were inserted (see the [ad metadata concepts](https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-metadata)).
  * A `playUri` field that shows the URL that the client device uses to play the conditioned video asset.



If you're generating a session on behalf of your customers' devices, set the following parameters using HTTP headers:

Parameter | HTTP Header  
---|---  
CLIENT_IP | `x-user-ip`  
REFERRER_URL | `referer`  
USER_AGENT | `user-agent`  
  
You can add the following headers to the preceding `curl` request:
    
    
    -H "x-user-ip: CLIENT_IP" \
    -H "referer: REFERRER_URL" \
    -H "user-agent: USER_AGENT" \

## Get a session

To get the session for an ad-stitched video, use the [`projects.locations.vodSessions.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions/get) method.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number located in the **Project number** field on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page
  * `LOCATION`: the location of your session; use one of the [supported regions](https://docs.cloud.google.com/video-stitcher/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `us-west1`
    * `asia-east1`
    * `asia-south1`
    * `asia-southeast1`
    * `europe-west1`
    * `southamerica-east1`
  * `SESSION_ID`: the identifier for the VOD session



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID",
      "interstitials": {
        "adBreaks": [
          {
            "progressEvents": [
              {
                "timeOffset": "0s",
                "events": [
                  {
                    "type": "IMPRESSION",
                    "uri": "https://securepubads.g.doubleclick.net/pcs/view..."
                  },
                  {
                    "type": "START",
                    "uri": "https://pubads.g.doubleclick.net/pagead/interaction/..."
                  },
                  ...
                ]
              },
              ...
            ],
            "ads": [
              {
                "duration": "10s",
                "activityEvents": [
                  {
                    "type": "ERROR",
                    "uri": "https://pubads.g.doubleclick.net/pagead/interaction/..."
                  },
                  {
                    "type": "CLICK_THROUGH",
                    "uri": "https://pubads.g.doubleclick.net/pcs/click...",
                    "id": "GDFP"
                  },
                  ...
                ]
              }
            ],
            "endTimeOffset": "10s",
            "startTimeOffset": "0s"
          }
        ],
        "sessionContent": {
          "duration": "70s"
        }
      },
      "playUri": "PLAY_URI",
      "sourceUri": "VOD_URI",
      "adTagUri": "AD_TAG_URI",
      "assetId": "ASSET_ID",
      "adTracking": "SERVER",
      "vodConfig": "projects/PROJECT_NUMBER/locations/LOCATION/vodConfigs/VOD_CONFIG_ID"
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class GetVodSessionSample
    {
        public VodSession GetVodSession(
            string projectId, string location, string sessionId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [GetVodSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodSessionRequest.html) request = new [GetVodSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodSessionRequest.html)
            {
                VodSessionName = [VodSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionName.html).[FromProjectLocationVodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionName.html#Google_Cloud_Video_Stitcher_V1_VodSessionName_FromProjectLocationVodSession_System_String_System_String_System_String_)(projectId, location, sessionId)
            };
    
            // Call the API.
            [VodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSession.html) session = client.[GetVodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_GetVodSession_Google_Cloud_Video_Stitcher_V1_GetVodSessionRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return session;
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
    
    // getVodSession gets a VOD session by ID.
    func getVodSession(w io.Writer, projectID, sessionID string) error {
    	// projectID := "my-project-id"
    	// sessionID := "123-456-789"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.GetVodSessionRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/vodSessions/%s", projectID, location, sessionID),
    	}
    	// Gets the session.
    	response, err := client.GetVodSession(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetVodSession: %w", err)
    	}
    	b, err := json.MarshalIndent(response, "", " ")
    	if err != nil {
    		return fmt.Errorf("json.MarshalIndent: %w", err)
    	}
    
    	fmt.Fprintf(w, "VOD session:\n%s", string(b))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[GetVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodSessionRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html);
    import com.google.cloud.video.stitcher.v1.[VodSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSessionName.html);
    import java.io.IOException;
    
    public class GetVodSession {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String sessionId = "my-session-id";
    
        getVodSession(projectId, location, sessionId);
      }
    
      // Gets a video on demand (VOD) session.
      public static [VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html) getVodSession(String projectId, String location, String sessionId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [GetVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodSessionRequest.html) getVodSessionRequest =
              [GetVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodSessionRequest.html).newBuilder()
                  .setName([VodSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSessionName.html).of(projectId, location, sessionId).toString())
                  .build();
    
          [VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html) response = videoStitcherServiceClient.getVodSession(getVodSessionRequest);
          System.out.println("VOD session: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession.html#com_google_cloud_video_stitcher_v1_VodSession_getName__)());
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
    
    async function getVodSession() {
      // Construct request
      const request = {
        name: stitcherClient.[vodSessionPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, sessionId),
      };
      const [session] = await stitcherClient.getVodSession(request);
      console.log(`VOD session: ${session.name}`);
    }
    
    getVodSession().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\GetVodSessionRequest;
    
    /**
     * Gets a VOD session.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $sessionId            The ID of the session
     */
    function get_vod_session(
        string $callingProjectId,
        string $location,
        string $sessionId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodSessionName($callingProjectId, $location, $sessionId);
        $request = (new GetVodSessionRequest())
            ->setName($formattedName);
        $session = $stitcherClient->getVodSession($request);
    
        // Print results
        printf('VOD session: %s' . PHP_EOL, $session->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def get_vod_session(
        project_id: str, location: str, session_id: str
    ) -> stitcher_v1.types.VodSession:
        """Gets a VOD session. VOD sessions are ephemeral resources that expire
        after a few hours.
        Args:
            project_id: The GCP project ID.
            location: The location of the session.
            session_id: The ID of the VOD session.
    
        Returns:
            The VOD session resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = client.vod_session_path(project_id, location, session_id)
        response = client.get_vod_session(name=name)
        print(f"VOD session: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Get a VOD session. VOD sessions are ephemeral resources that expire
    # after a few hours.
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param session_id [String] The VOD session ID (e.g. `my-vod-session-id`)
    #
    def get_vod_session project_id:, location:, session_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the VOD session.
      name = client.vod_session_path project: project_id, location: location,
                                     vod_session: session_id
    
      # Get the VOD session.
      session = client.get_vod_session name: name
    
      # Print the VOD session name.
      puts "VOD session: #{session.name}"
    end

## Sample ad-stitched playlist

The following shows a sample source VOD playlist before ad-stitching:
    
    
    #EXTM3U
    #EXT-X-TARGETDURATION:6
    #EXT-X-VERSION:4
    #EXT-X-PLAYLIST-TYPE:VOD
    #EXT-X-MEDIA-SEQUENCE:0
    #EXTINF:6.000,
    segment_01.ts
    #EXTINF:6.000,
    segment_02.ts
    #EXTINF:6.000,
    segment_03.ts
    #EXTINF:6.000,
    segment_04.ts
    #EXTINF:6.000,
    segment_05.ts
    #EXTINF:6.000,
    segment_06.ts
    #EXT-X-ENDLIST
    

The following shows a sample source VOD playlist after ad stitching with pre-roll, mid-roll, and post-roll ads:
    
    
    #EXTM3U
    #EXT-X-VERSION:4
    #EXT-X-TARGETDURATION:6
    #EXT-X-PLAYLIST-TYPE:VOD
    #EXT-X-DISCONTINUITY
    #EXTINF:4.000,
    https://redirector.googlevideo.com/videoplayback/...
    #EXTINF:4.000,
    https://redirector.googlevideo.com/videoplayback/...
    #EXTINF:1.990,
    https://redirector.googlevideo.com/videoplayback/...
    #EXT-X-DISCONTINUITY
    #EXTINF:6.000,
    segment_01.ts
    #EXTINF:6.000,
    segment_02.ts
    #EXT-X-DISCONTINUITY
    #EXTINF:4.000,
    https://redirector.googlevideo.com/videoplayback/...
    #EXTINF:0.990,
    https://redirector.googlevideo.com/videoplayback/...
    #EXT-X-DISCONTINUITY
    #EXTINF:6.000,
    segment_03.ts
    #EXTINF:6.000,
    segment_04.ts
    #EXTINF:6.000,
    segment_05.ts
    #EXTINF:6.000,
    segment_06.ts
    #EXT-X-DISCONTINUITY
    #EXTINF:4.000,
    https://redirector.googlevideo.com/videoplayback/...
    #EXTINF:4.000,
    https://redirector.googlevideo.com/videoplayback/...
    #EXTINF:1.990,
    https://redirector.googlevideo.com/videoplayback/...
    #EXT-X-ENDLIST
    

## Handle client-side ad tracking

The IMA SDK will automatically handle the client-side ad tracking.

## Inspect VOD sessions enabled by Google Ad Manager

To inspect VOD sessions and the ad tag details for these sessions, use the [Stream activity monitor](https://support.google.com/admanager/answer/7009058) in Ad Manager.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
