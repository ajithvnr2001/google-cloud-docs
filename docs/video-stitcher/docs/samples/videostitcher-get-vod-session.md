---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-get-vod-session/
title: Get a VOD session \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:13.532307+00:00
---

# Get a VOD session  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-get-vod-session/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  Get a VOD session Stay organized with collections  Save and categorize content based on your preferences. 

Get details for a Video Stitcher VOD session resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage a VOD session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions)
  * [Manage a VOD session enabled by Google Ad Manager](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions-gam)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videostitcherapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
