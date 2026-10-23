---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-get-vod-stitch-detail/
title: Get VOD ad tag stitch details \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:37.809144+00:00
---

# Get VOD ad tag stitch details  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-get-vod-stitch-detail/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  Get VOD ad tag stitch details Stay organized with collections  Save and categorize content based on your preferences. 

Get stitch details for a Video Stitcher VOD session ad tag. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage a VOD session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videostitcherapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
