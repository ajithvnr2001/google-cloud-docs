---
url: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions/
title: Manage a VOD session \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:03.197007+00:00
---

# Manage a VOD session  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Manage a VOD session Stay organized with collections  Save and categorize content based on your preferences. 

Using the Video Stitcher API, you create a video-on-demand (VOD) session each time you dynamically insert ads prior to delivery to client devices. When you create a session, the response includes the playback URL and information about the ads that you inserted into the video.

This page describes how to create and manage a VOD session that is _not_ enabled by Google Ad Manager. For more information on these types of VOD sessions, see [Manage a VOD session enabled by Google Ad Manager](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions-gam).

## Before you begin

  * [Create a VOD config](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs)



## Create a session

To create a session for an ad-stitched video, use the [`projects.locations.vodSessions.create`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions/create) method.

When you create a VOD session, the following field is required:

  * [`adTracking`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#VodSession.FIELDS.ad_tracking): determines if the client player is expected to trigger playback and activity events or if the Video Stitcher API is expected to trigger playback events on behalf of the client player; for more information on client-side ad tracking, see Handle VOD client ad tracking.

The example in this section uses server-side ad tracking.




When you create a VOD session, the following fields are optional:

  * [`adTagMacroMap`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#VodSession.FIELDS.ad_tag_macro_map): a list of key-value pairs for ad tag macro replacement; see the ad tag macros section
  * [`manifestOptions`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#VodSession.FIELDS.manifest_options): specifies which video renditions are generated in the stitched video manifest and the ordering of the renditions; see the [manifest options](https://docs.cloud.google.com/video-stitcher/docs/concepts/manifest-options) documentation



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
    
    

The Video Stitcher API generates a unique session ID for each request. A session expires after 4 hours.

An ad must be encoded before it can be stitched into a VOD session. When you create a session for an ad-stitched video, the Video Stitcher API determines if the ad has already been encoded from a previous session. If it has, the JSON response will indicate ad break events. The API only looks for encoded ads created by sessions associated with your Google Cloud project. For more information on this process, see the [Overview](https://docs.cloud.google.com/video-stitcher/docs/concepts/overview#ad_re-encoding).

Look at the JSON response. This response indicates that an ad was **not** stitched into the session. If this is the case, wait 5 minutes (for ad encoding) and then re-run the create session command. The response should now be similar to the following:
    
    
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
    

The response is a [VOD session object](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#VodSession) that contains the following fields:

  * A `name` field that shows the VOD `SESSION_ID`. Use this ID to get information about the session.
  * An [`interstitials`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#interstitials) object that contains metadata about the ads that were inserted (see the [ad metadata concepts](https://docs.cloud.google.com/video-stitcher/docs/concepts/ad-metadata)).
  * A `playUri` field that shows the URL that the client device uses to play the conditioned video asset.



If you're generating a session on behalf of your customers' devices, set the following parameters using HTTP headers:

Parameter | HTTP Header  
---|---  
`CLIENT_IP` | `x-user-ip`  
`REFERRER_URL` | `referer`  
`USER_AGENT` | `user-agent`  
  
You can add the following headers to the preceding `curl` request:
    
    
    -H "x-user-ip: CLIENT_IP" \
    -H "referer: REFERRER_URL" \
    -H "user-agent: USER_AGENT" \

### Ad tag macros

An ad tag can contain macros, which can result in a different ad tag for each session. Macros are denoted by square brackets in the ad tag, as illustrated by the following example:
    
    
    AD_TAG_URI&macro=[my-key]

The `adTagUri` is defined in the [VOD config](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-configs).

To substitute the value in the ad tag macro, provide a mapping in the [`adTagMacroMap`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#VodSession.FIELDS.ad_tag_macro_map) field. For example, if you want to replace the `[my-key]` macro with the string `my-value`, you need to provide the following:
    
    
    {
      ...
      "adTagMacroMap": {
        "my-key": "my-value"
      },
      ...
    }

When the Video Stitcher API requests the ad metadata, it uses the following ad tag:
    
    
    AD_TAG_URI&macro=my-value

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

The following shows a sample source VOD playlist before ad stitching:
    
    
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
    https://ads.us-west1.cdn.videostitcher.goog/preroll_ad/seg_01.ts
    #EXTINF:4.000,
    https://ads.us-west1.cdn.videostitcher.goog/preroll_ad/seg_02.ts
    #EXTINF:1.990,
    https://ads.us-west1.cdn.videostitcher.goog/preroll_ad/seg_03.ts
    #EXT-X-DISCONTINUITY
    #EXTINF:6.000,
    segment_01.ts
    #EXTINF:6.000,
    segment_02.ts
    #EXT-X-DISCONTINUITY
    #EXTINF:4.000,
    https://ads.us-west1.cdn.videostitcher.goog/midroll_ad/seg_01.ts
    #EXTINF:0.990,
    https://ads.us-west1.cdn.videostitcher.goog/midroll_ad/seg_02.ts
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
    https://ads.us-west1.cdn.videostitcher.goog/postroll_ad/seg_01.ts
    #EXTINF:4.000,
    https://ads.us-west1.cdn.videostitcher.goog/postroll_ad/seg_02.ts
    #EXTINF:1.990,
    https://ads.us-west1.cdn.videostitcher.goog/postroll_ad/seg_03.ts
    #EXT-X-ENDLIST
    

## Handle client-side ad tracking

When client ad tracking is enabled, the player is responsible for triggering ad tracking events. You can find client-side tracking information in the interstitials object returned when the VOD session is created.

The interstitials object includes ad tracking information and metadata for companion ads parsed from ad tag requests. To inspect which ads are stitched, see Inspect VOD sessions.

### Interstitials

Ad tracking information is grouped by ad breaks in the [`interstitials`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#interstitials) object.

Ad breaks may have progress events which specify the event URI and the time offset relative to the break start time for each event that has been fired. For more details about progress events, see the [`ProgressEvent`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/ProgressEvent) reference documentation.

Ad breaks may also have activity events and companion ads. For more details about companion ads, see the [`CompanionAds`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/CompanionAds) reference documentation.

The following is an interstitials example:
    
    
    {
      "adBreaks": [
        {
          "progressEvents": [
            {
              "timeOffset": "0s",
              "events": [
                {
                  "type": "IMPRESSION",
                  "uri": "https://example.com/impression"
                },
                {
                  "type": "START",
                  "uri": "https://example.com/start"
                }
              ]
            },
            {
              "timeOffset": "1.250s",
              "events": [
                {
                  "type": "FIRST_QUARTILE",
                  "uri": "https://example.com/firstquartile"
                }
              ]
            }
          ],
          "ads": [
            {
              "duration": "5s",
              "activityEvents": [
                {
                  "type": "PAUSE",
                  "uri": "https://example.com/pause"
                }
              ],
              "companionAds": {
                "required": "all",
                "companions": [
                  {
                    "width": 200,
                    "height": 100,
                    "staticResource": {
                      "uri": "https://example.com/static.png",
                      "creativeType": "image/png"
                    }
                  }
                ]
              }
            },
            {
              "duration": "10s"
            }
          ],
          "startTimeOffset": "0s",
          "endTimeOffset": "15.000s"
        }
      ],
      "sessionContent": {
          "duration": "120.000s"
      }
    }
    

In the preceding example, there is one pre-roll ad break with two ads stitched into a VOD asset. The duration of the first ad is 5 seconds and the duration of the second ad is 10 seconds. The total stitched video length is 120 seconds, as identified by the `duration` field in `sessionContent` .

When the client receives this object, it should do the following:

  * Make a request to `https://example.com/start` at the start of the ad break.
  * Make a request to `https://example.com/impression` at the start of the ad break.
  * Make a request to `https://example.com/pause` whenever the viewer pauses the video during the first ad.
  * Make a request to `https://example.com/firstQuartile` 1.25 seconds into the first ad.
  * Load the companion ad `https://example.com/static.png` during the first ad.



## Inspect VOD sessions

This section describes how to inspect the ad tag details and stitch details for a given VOD session. For more details, see the REST documentation for [`VodAdTagDetail`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodAdTagDetails) and [`VodStitchDetail`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodStitchDetails). 

**Note:** This section does not apply to VOD sessions created for [Google Ad Manager (GAM)](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions#gamsettings) ad insertion. You can't use the ad tag and stitch details endpoints for these sessions. Use the [Stream activity monitor](https://support.google.com/admanager/answer/7009058) in Ad Manager to see details about ad requests.

The `adTagUri` field, defined in the VOD config for the VOD session, specifies the URL from where ad metadata is retrieved. The Video Stitcher API also includes user metadata when it makes the request.

The `/vodAdTagDetails` endpoint contains the following information:

  * resolved ad tag
  * user metadata
  * request body and headers
  * response body and headers



The `/vodStitchDetails` endpoint contains the following information:

  * ad break ID
  * ad ID
  * ad time offset (in seconds)
  * reason if the ad was not inserted
  * ad media metadata

**Note:** The ad tag and stitch details information is stored for 30 days.

### List ad tag details

To list the ad tag details for a VOD session, use the [`projects.locations.vodSessions.vodAdTagDetails.list`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodAdTagDetails/list) method.

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
  * `SESSION_ID`: the session ID for the VOD session



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodAdTagDetails"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodAdTagDetails" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "vodAdTagDetails" : [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodAdTagDetails/VOD_AD_TAG_DETAILS_ID",
          "adRequests": [
            {
              "uri": "REQUEST_URL",
              "requestMetadata": "AD_TAG_REQUEST_METADATA",
              "responseMetadata": "AD_TAG_RESPONSE_METADATA"
            }
          ]
        }
      ]
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using System;
    
    public class ListVodAdTagDetailsSample
    {
        public PagedEnumerable<ListVodAdTagDetailsResponse, VodAdTagDetail> ListVodAdTagDetails(
            string projectId, string regionId, string sessionId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [ListVodAdTagDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ListVodAdTagDetailsRequest.html) request = new [ListVodAdTagDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ListVodAdTagDetailsRequest.html)
            {
                ParentAsVodSessionName = [VodSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionName.html).[FromProjectLocationVodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionName.html#Google_Cloud_Video_Stitcher_V1_VodSessionName_FromProjectLocationVodSession_System_String_System_String_System_String_)(projectId, regionId, sessionId)
            };
    
            // Make the request.
            PagedEnumerable<ListVodAdTagDetailsResponse, VodAdTagDetail> response = client.[ListVodAdTagDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_ListVodAdTagDetails_Google_Cloud_Video_Stitcher_V1_ListVodAdTagDetailsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            foreach ([VodAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail.html) vodAdTagDetail in response)
            {
                Console.WriteLine($"{vodAdTagDetail.Name}");
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
    
    // listVodAdTagDetails lists the ad tag details for a video on demand (VOD) session.
    func listVodAdTagDetails(w io.Writer, projectID, sessionID string) error {
    	// projectID := "my-project-id"
    	// sessionID := "123-456-789"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.ListVodAdTagDetailsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s/vodSessions/%s", projectID, location, sessionID),
    	}
    
    	it := client.ListVodAdTagDetails(ctx, req)
    	fmt.Fprintln(w, "VOD ad tag details:")
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
    
    
    import com.google.cloud.video.stitcher.v1.[ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).[ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse.html);
    import com.google.cloud.video.stitcher.v1.[VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail.html);
    import com.google.cloud.video.stitcher.v1.[VodSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSessionName.html);
    import java.io.IOException;
    
    public class ListVodAdTagDetails {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String sessionId = "my-session-id";
    
        listVodAdTagDetails(projectId, location, sessionId);
      }
    
      // Lists the ad tag details for a video on demand (VOD) session.
      public static [ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse.html) listVodAdTagDetails(
          String projectId, String location, String sessionId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest.html) listVodAdTagDetailsRequest =
              [ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest.html).newBuilder()
                  .setParent([VodSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSessionName.html).of(projectId, location, sessionId).toString())
                  .build();
    
          [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).[ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse.html) response =
              videoStitcherServiceClient.listVodAdTagDetails(listVodAdTagDetailsRequest);
    
          System.out.println("VOD ad tag details:");
          for ([VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail.html) adTagDetail : response.iterateAll()) {
            System.out.println(adTagDetail.toString());
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
    // sessionId = 'my-session-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function listVodAdTagDetails() {
      // Construct request
      const request = {
        parent: stitcherClient.[vodSessionPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, sessionId),
      };
      const iterable = await stitcherClient.[listVodAdTagDetailsAsync](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(request);
      console.log('VOD ad tag details:');
      for await (const response of iterable) {
        console.log(response.name);
      }
    }
    
    listVodAdTagDetails().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\ListVodAdTagDetailsRequest;
    
    /**
     * Lists the ad tag details for the specified VOD session.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $sessionId            The ID of the session
     */
    function list_vod_ad_tag_details(
        string $callingProjectId,
        string $location,
        string $sessionId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodSessionName($callingProjectId, $location, $sessionId);
        $request = (new ListVodAdTagDetailsRequest())
            ->setParent($formattedName);
        $response = $stitcherClient->listVodAdTagDetails($request);
    
        // Print the ad tag details list.
        $adTagDetails = $response->iterateAllElements();
        print('VOD ad tag details:' . PHP_EOL);
        foreach ($adTagDetails as $adTagDetail) {
            printf('%s' . PHP_EOL, $adTagDetail->getName());
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
    
    
    def list_vod_ad_tag_details(
        project_id: str, location: str, session_id: str
    ) -> pagers.ListVodAdTagDetailsPager:
        """Lists the ad tag details for the specified VOD session.
        Args:
            project_id: The GCP project ID.
            location: The location of the session.
            session_id: The ID of the VOD session.
    
        Returns:
            An iterable object containing VOD ad tag details resources.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = client.vod_session_path(project_id, location, session_id)
        page_result = client.list_vod_ad_tag_details(parent=parent)
        print("VOD ad tag details:")
        for response in page_result:
            print(response)
    
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # List the ad tag details for a VOD session
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param session_id [String] The VOD session ID (e.g. `my-vod-session-id`)
    #
    def list_vod_ad_tag_details project_id:, location:, session_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.vod_session_path project: project_id, location: location,
                                       vod_session: session_id
    
      # List all ad tag details for the VOD session.
      response = client.list_vod_ad_tag_details parent: parent
    
      puts "VOD ad tag details:"
      # Print out all VOD ad tag details.
      response.each do |vod_ad_tag_detail|
        puts vod_ad_tag_detail.name
      end
    end

The response returns a list of [`VodAdTagDetail`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodAdTagDetails) objects. Each [`VodAdTagDetail`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodAdTagDetails) represents the ad retrieval metadata for an ad tag, and each [`AdRequest`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/AdRequest) represents the ad request metadata for a single ad request.

#### Additional results

The `curl` response may include a `nextPageToken`, which you can use to retrieve additional results:
    
    
    {
      "vodAdTagDetails": [
        ...
      ],
      "nextPageToken": "NEXT_PAGE_TOKEN"
    }

You can send another `curl` request, including the value of `NEXT_PAGE_TOKEN`, to list the additional objects. Append the following to the URL in the preceding API call:
    
    
    ?pageToken=NEXT_PAGE_TOKEN
    

### Get ad tag details

To get the details for a single `VodAdTagDetail` object in a VOD session, use the [`projects.locations.vodSessions.vodAdTagDetails.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodAdTagDetails/get) method.

The following example demonstrates viewing a single ad tag detail for a VOD session using the name of an ad tag detail returned from a previous request:

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
  * `SESSION_ID`: the session ID for the VOD session
  * `VOD_AD_TAG_DETAILS_ID`: the ID for the VOD ad tag details



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodAdTagDetails/VOD_AD_TAG_DETAILS_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodAdTagDetails/VOD_AD_TAG_DETAILS_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodAdTagDetails/VOD_AD_TAG_DETAILS_ID",
      "adRequests": [
        {
          "uri": "REQUEST_URL",
          "requestMetadata": "AD_TAG_REQUEST_METADATA",
          "responseMetadata": "AD_TAG_RESPONSE_METADATA"
        }
      ]
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class GetVodAdTagDetailSample
    {
        public VodAdTagDetail GetVodAdTagDetail(
            string projectId, string location, string sessionId, string adTagDetailId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [GetVodAdTagDetailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodAdTagDetailRequest.html) request = new [GetVodAdTagDetailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodAdTagDetailRequest.html)
            {
                VodAdTagDetailName = [VodAdTagDetailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetailName.html).[FromProjectLocationVodSessionVodAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetailName.html#Google_Cloud_Video_Stitcher_V1_VodAdTagDetailName_FromProjectLocationVodSessionVodAdTagDetail_System_String_System_String_System_String_System_String_)(projectId, location, sessionId, adTagDetailId)
            };
    
            // Call the API.
            [VodAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail.html) vodAdTagDetail = client.[GetVodAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_GetVodAdTagDetail_Google_Cloud_Video_Stitcher_V1_GetVodAdTagDetailRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return vodAdTagDetail;
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
    
    // getVodAdTagDetail gets the specified ad tag detail for a video on demand (VOD) session.
    func getVodAdTagDetail(w io.Writer, projectID, sessionID, adTagDetailID string) error {
    	// projectID := "my-project-id"
    	// sessionID := "123-456-789"
    	// adTagDetailID := "01234-56789"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.GetVodAdTagDetailRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/vodSessions/%s/vodAdTagDetails/%s", projectID, location, sessionID, adTagDetailID),
    	}
    	// Gets the ad tag detail.
    	response, err := client.GetVodAdTagDetail(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetVodAdTagDetail: %w", err)
    	}
    	b, err := json.MarshalIndent(response, "", " ")
    	if err != nil {
    		return fmt.Errorf("json.MarshalIndent: %w", err)
    	}
    
    	fmt.Fprintf(w, "VOD ad tag detail:\n%s", string(b))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[GetVodAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodAdTagDetailRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail.html);
    import com.google.cloud.video.stitcher.v1.[VodAdTagDetailName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetailName.html);
    import java.io.IOException;
    
    public class GetVodAdTagDetail {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String sessionId = "my-session-id";
        String adTagDetailId = "my-ad-tag-id";
    
        getVodAdTagDetail(projectId, location, sessionId, adTagDetailId);
      }
    
      // Gets an ad tag detail for a video on demand (VOD) session.
      public static [VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail.html) getVodAdTagDetail(
          String projectId, String location, String sessionId, String adTagDetailId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [GetVodAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodAdTagDetailRequest.html) getVodAdTagDetailRequest =
              [GetVodAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodAdTagDetailRequest.html).newBuilder()
                  .setName(
                      [VodAdTagDetailName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetailName.html).of(projectId, location, sessionId, adTagDetailId).toString())
                  .build();
    
          [VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail.html) response =
              videoStitcherServiceClient.getVodAdTagDetail(getVodAdTagDetailRequest);
          System.out.println("VOD ad tag detail: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail.html#com_google_cloud_video_stitcher_v1_VodAdTagDetail_getName__)());
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
    // adTagDetailId = 'my-ad-tag-detail-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function getVodAdTagDetail() {
      // Construct request
      const request = {
        name: stitcherClient.[vodAdTagDetailPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(
          projectId,
          location,
          sessionId,
          adTagDetailId
        ),
      };
      const [adTagDetail] = await stitcherClient.getVodAdTagDetail(request);
      console.log(`VOD ad tag detail: ${adTagDetail.name}`);
    }
    
    getVodAdTagDetail().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\GetVodAdTagDetailRequest;
    
    /**
     * Gets the specified ad tag detail for the VOD session.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $sessionId            The ID of the session
     * @param string $adTagDetailId        The ID of the ad tag detail
     */
    function get_vod_ad_tag_detail(
        string $callingProjectId,
        string $location,
        string $sessionId,
        string $adTagDetailId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodAdTagDetailName($callingProjectId, $location, $sessionId, $adTagDetailId);
        $request = (new GetVodAdTagDetailRequest())
            ->setName($formattedName);
        $adTagDetail = $stitcherClient->getVodAdTagDetail($request);
    
        // Print results
        printf('VOD ad tag detail: %s' . PHP_EOL, $adTagDetail->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def get_vod_ad_tag_detail(
        project_id: str, location: str, session_id: str, ad_tag_detail_id: str
    ) -> stitcher_v1.types.VodAdTagDetail:
        """Gets the specified ad tag detail for a VOD session.
        Args:
            project_id: The GCP project ID.
            location: The location of the session.
            session_id: The ID of the VOD session.
            ad_tag_detail_id: The ID of the ad tag details.
    
        Returns:
            The VOD ad tag detail resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = client.vod_ad_tag_detail_path(
            project_id, location, session_id, ad_tag_detail_id
        )
        response = client.get_vod_ad_tag_detail(name=name)
        print(f"VOD ad tag detail: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Get the specified ad tag detail for a VOD session
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param session_id [String] The VOD session ID (e.g. `my-vod-session-id`)
    # @param ad_tag_detail_id [String] The ad tag detail ID (e.g. `my-ad-tag-id`)
    #
    def get_vod_ad_tag_detail project_id:, location:, session_id:, ad_tag_detail_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the VOD ad tag detail.
      name = client.vod_ad_tag_detail_path project: project_id, location: location,
                                           vod_session: session_id,
                                           vod_ad_tag_detail: ad_tag_detail_id
    
      # Get the VOD ad tag detail.
      ad_tag_detail = client.get_vod_ad_tag_detail name: name
    
      # Print the VOD ad tag detail name.
      puts "VOD ad tag detail: #{ad_tag_detail.name}"
    end

### List stitch details

You can view detailed information about the ads that were stitched for any VOD session.

To list the stitch details for a VOD session, use the [`projects.locations.vodSessions.vodStitchDetails.list`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodStitchDetails/list) method.

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
  * `SESSION_ID`: the session ID for the VOD session



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodStitchDetails"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodStitchDetails" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "vodStitchDetails" : [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodStitchDetails/VOD_STITCH_DETAILS_ID",
          "adStitchDetails": [
            {
              "adBreakId": "AD_BREAK_ID",
              "adId": "AD_ID",
              "adTimeOffset": "AD_TIME_OFFSET",
              "skipReason": "SKIP_REASON",
              "media": "MEDIA_OBJECT"
            },
            {
              "adBreakId": "my-other-ad-break-id",
              "adId": "my-other-ad-id",
              "adTimeOffset": "my-other-ad-time-offset",
              "skipReason": "my-other-skip-reason",
              "media": "my-other-media-object"
            }
          ]
        }
      ]
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using System;
    
    public class ListVodStitchDetailsSample
    {
        public PagedEnumerable<ListVodStitchDetailsResponse, VodStitchDetail> ListVodStitchDetails(
            string projectId, string regionId, string sessionId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [ListVodStitchDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ListVodStitchDetailsRequest.html) request = new [ListVodStitchDetailsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ListVodStitchDetailsRequest.html)
            {
                ParentAsVodSessionName = [VodSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionName.html).[FromProjectLocationVodSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionName.html#Google_Cloud_Video_Stitcher_V1_VodSessionName_FromProjectLocationVodSession_System_String_System_String_System_String_)(projectId, regionId, sessionId)
            };
    
            // Make the request.
            PagedEnumerable<ListVodStitchDetailsResponse, VodStitchDetail> response = client.[ListVodStitchDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_ListVodStitchDetails_Google_Cloud_Video_Stitcher_V1_ListVodStitchDetailsRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            foreach ([VodStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail.html) vodStitchDetail in response)
            {
                Console.WriteLine($"{vodStitchDetail.Name}");
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
    
    // listVodStitchDetails lists the stitch details for a video on demand (VOD) session.
    func listVodStitchDetails(w io.Writer, projectID, sessionID string) error {
    	// projectID := "my-project-id"
    	// sessionID := "123-456-789"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.ListVodStitchDetailsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s/vodSessions/%s", projectID, location, sessionID),
    	}
    
    	it := client.ListVodStitchDetails(ctx, req)
    	fmt.Fprintln(w, "VOD stitch details:")
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
    
    
    import com.google.cloud.video.stitcher.v1.[ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).[ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse.html);
    import com.google.cloud.video.stitcher.v1.[VodSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSessionName.html);
    import com.google.cloud.video.stitcher.v1.[VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail.html);
    import java.io.IOException;
    
    public class ListVodStitchDetails {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String sessionId = "my-session-id";
    
        listVodStitchDetails(projectId, location, sessionId);
      }
    
      // Lists the VOD stitch details for a video on demand (VOD) session.
      public static [ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse.html) listVodStitchDetails(
          String projectId, String location, String sessionId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest.html) listVodStitchDetailsRequest =
              [ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest.html).newBuilder()
                  .setParent([VodSessionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSessionName.html).of(projectId, location, sessionId).toString())
                  .build();
    
          [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).[ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse.html) response =
              videoStitcherServiceClient.listVodStitchDetails(listVodStitchDetailsRequest);
    
          System.out.println("VOD stitch details:");
          for ([VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail.html) stitchDetail : response.iterateAll()) {
            System.out.println(stitchDetail.toString());
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
    // sessionId = 'my-session-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function listVodStitchDetails() {
      // Construct request
      const request = {
        parent: stitcherClient.[vodSessionPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, sessionId),
      };
      const iterable = await stitcherClient.[listVodStitchDetailsAsync](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(request);
      console.log('VOD stitch details:');
      for await (const response of iterable) {
        console.log(response.name);
      }
    }
    
    listVodStitchDetails().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\ListVodStitchDetailsRequest;
    
    /**
     * Lists the stitch details for the specified VOD session.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $sessionId            The ID of the session
     */
    function list_vod_stitch_details(
        string $callingProjectId,
        string $location,
        string $sessionId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodSessionName($callingProjectId, $location, $sessionId);
        $request = (new ListVodStitchDetailsRequest())
            ->setParent($formattedName);
        $response = $stitcherClient->listVodStitchDetails($request);
    
        // Print the stitch details list.
        $stitchDetails = $response->iterateAllElements();
        print('VOD stitch details:' . PHP_EOL);
        foreach ($stitchDetails as $stitchDetail) {
            printf('%s' . PHP_EOL, $stitchDetail->getName());
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
    
    
    def list_vod_stitch_details(
        project_id: str, location: str, session_id: str
    ) -> pagers.ListVodStitchDetailsPager:
        """Lists the stitch details for the specified VOD session.
        Args:
            project_id: The GCP project ID.
            location: The location of the session.
            session_id: The ID of the VOD session.
    
        Returns:
            An iterable object containing VOD stitch details resources.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = client.vod_session_path(project_id, location, session_id)
        page_result = client.list_vod_stitch_details(parent=parent)
        print("VOD stitch details:")
        for response in page_result:
            print(response)
    
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # List the stitch details for a VOD session
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param session_id [String] The VOD session ID (e.g. `my-vod-session-id`)
    #
    def list_vod_stitch_details project_id:, location:, session_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.vod_session_path project: project_id, location: location,
                                       vod_session: session_id
    
      # List all stitch details for the VOD session.
      response = client.list_vod_stitch_details parent: parent
    
      puts "VOD stitch details:"
      # Print out all VOD stitch details.
      response.each do |vod_stitch_detail|
        puts vod_stitch_detail.name
      end
    end

The response returns a list of [`VodStitchDetail`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodStitchDetails) objects. Each `VodStitchDetail` represents the stitch detail for an ad tag, and each [`adStitchDetails`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodStitchDetails#adstitchdetail) object represents the stitch detail for a single ad.

The `curl` response may include a `nextPageToken`, which you can use to retrieve additional results.

### Get ad tag stitch detail

To get the stitch detail for a single ad tag for a VOD session, use the [`projects.locations.vodSessions.vodStitchDetails.get`](https://docs.cloud.google.com/video-stitcher/docs/reference/rest/v1/projects.locations.vodSessions.vodStitchDetails/get) method.

The following example demonstrates viewing a single ad tag stitch detail for a VOD session using the name of an stitch ad tag detail returned from a previous request:

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
  * `SESSION_ID`: the session ID for the VOD session
  * `VOD_STITCH_DETAILS_ID`: the ID for the VOD stitch details



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodStitchDetails/VOD_STITCH_DETAILS_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videostitcher.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodStitchDetails/VOD_STITCH_DETAILS_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/vodSessions/SESSION_ID/vodStitchDetails/VOD_STITCH_DETAILS_ID",
      "adStitchDetails": [
        {
          "adBreakId": "AD_BREAK_ID",
          "adId": "AD_ID",
          "adTimeOffset": "AD_TIME_OFFSET",
          "skipReason": "SKIP_REASON",
          "media": "MEDIA_OBJECT"
        }
      ]
    }
    

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class GetVodStitchDetailSample
    {
        public VodStitchDetail GetVodStitchDetail(
            string projectId, string location, string sessionId, string stitchDetailId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [GetVodStitchDetailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodStitchDetailRequest.html) request = new [GetVodStitchDetailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetVodStitchDetailRequest.html)
            {
                VodStitchDetailName = [VodStitchDetailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetailName.html).[FromProjectLocationVodSessionVodStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetailName.html#Google_Cloud_Video_Stitcher_V1_VodStitchDetailName_FromProjectLocationVodSessionVodStitchDetail_System_String_System_String_System_String_System_String_)(projectId, location, sessionId, stitchDetailId)
            };
    
            // Call the API.
            [VodStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail.html) vodStitchDetail = client.[GetVodStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_GetVodStitchDetail_Google_Cloud_Video_Stitcher_V1_GetVodStitchDetailRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return vodStitchDetail;
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
    
    // getVodStitchDetail gets the specified stitch detail for a video on demand (VOD) session.
    func getVodStitchDetail(w io.Writer, projectID, sessionID, stitchDetailID string) error {
    	// projectID := "my-project-id"
    	// sessionID := "123-456-789"
    	// stitchDetailID := "01234-56789"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.GetVodStitchDetailRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/vodSessions/%s/vodStitchDetails/%s", projectID, location, sessionID, stitchDetailID),
    	}
    	// Gets the stitch detail.
    	response, err := client.GetVodStitchDetail(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetStitchDetail: %w", err)
    	}
    	b, err := json.MarshalIndent(response, "", " ")
    	if err != nil {
    		return fmt.Errorf("json.MarshalIndent: %w", err)
    	}
    
    	fmt.Fprintf(w, "VOD stitch detail:\n%s", string(b))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[GetVodStitchDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodStitchDetailRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.cloud.video.stitcher.v1.[VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail.html);
    import com.google.cloud.video.stitcher.v1.[VodStitchDetailName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetailName.html);
    import java.io.IOException;
    
    public class GetVodStitchDetail {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String sessionId = "my-session-id";
        String stitchDetailId = "my-stitch-id";
    
        getVodStitchDetail(projectId, location, sessionId, stitchDetailId);
      }
    
      // Gets a stitch detail for a video on demand (VOD) session.
      public static [VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail.html) getVodStitchDetail(
          String projectId, String location, String sessionId, String stitchDetailId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [GetVodStitchDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodStitchDetailRequest.html) getVodStitchDetailRequest =
              [GetVodStitchDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodStitchDetailRequest.html).newBuilder()
                  .setName(
                      [VodStitchDetailName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetailName.html).of(projectId, location, sessionId, stitchDetailId).toString())
                  .build();
    
          [VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail.html) response =
              videoStitcherServiceClient.getVodStitchDetail(getVodStitchDetailRequest);
          System.out.println("VOD stitch detail: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail.html#com_google_cloud_video_stitcher_v1_VodStitchDetail_getName__)());
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
    // stitchDetailId = 'my-stitch-detail-id';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function getVodStitchDetail() {
      // Construct request
      const request = {
        name: stitcherClient.[vodStitchDetailPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(
          projectId,
          location,
          sessionId,
          stitchDetailId
        ),
      };
      const [stitchDetail] = await stitcherClient.getVodStitchDetail(request);
      console.log(`VOD stitch detail: ${stitchDetail.name}`);
    }
    
    getVodStitchDetail().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\GetVodStitchDetailRequest;
    
    /**
     * Gets the specified stitch detail for the VOD session.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $sessionId            The ID of the session
     * @param string $stitchDetailId       The ID of the stitch detail
     */
    function get_vod_stitch_detail(
        string $callingProjectId,
        string $location,
        string $sessionId,
        string $stitchDetailId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->vodStitchDetailName($callingProjectId, $location, $sessionId, $stitchDetailId);
        $request = (new GetVodStitchDetailRequest())
            ->setName($formattedName);
        $stitchDetail = $stitcherClient->getVodStitchDetail($request);
    
        // Print results
        printf('VOD stitch detail: %s' . PHP_EOL, $stitchDetail->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def get_vod_stitch_detail(
        project_id: str, location: str, session_id: str, stitch_detail_id: str
    ) -> stitcher_v1.types.VodStitchDetail:
        """Gets the specified stitch detail for a VOD session.
        Args:
            project_id: The GCP project ID.
            location: The location of the session.
            session_id: The ID of the VOD session.
            stitch_detail_id: The ID of the stitch details.
    
        Returns:
            The VOD stitch detail resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = client.vod_stitch_detail_path(
            project_id, location, session_id, stitch_detail_id
        )
        response = client.get_vod_stitch_detail(name=name)
        print(f"VOD stitch detail: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Get the specified stitch detail for a VOD session
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param session_id [String] The VOD session ID (e.g. `my-vod-session-id`)
    # @param stitch_detail_id [String] The stitch detail ID (e.g. `my-stitch-id`)
    #
    def get_vod_stitch_detail project_id:, location:, session_id:, stitch_detail_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the VOD stitch detail.
      name = client.vod_stitch_detail_path project: project_id, location: location,
                                           vod_session: session_id,
                                           vod_stitch_detail: stitch_detail_id
    
      # Get the VOD stitch detail.
      stitch_detail = client.get_vod_stitch_detail name: name
    
      # Print the VOD stitch detail name.
      puts "VOD stitch detail: #{stitch_detail.name}"
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
