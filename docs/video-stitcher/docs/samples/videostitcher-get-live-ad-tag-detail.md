---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-get-live-ad-tag-detail/
title: Get live ad tag details \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:16.958784+00:00
---

# Get live ad tag details  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-get-live-ad-tag-detail/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  Get live ad tag details Stay organized with collections  Save and categorize content based on your preferences. 

Get details for a Video Stitcher live session ad tag. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage a live session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-live-sessions)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    
    public class GetLiveAdTagDetailSample
    {
        public LiveAdTagDetail GetLiveAdTagDetail(
            string projectId, string location, string sessionId, string adTagDetailId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [GetLiveAdTagDetailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetLiveAdTagDetailRequest.html) request = new [GetLiveAdTagDetailRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GetLiveAdTagDetailRequest.html)
            {
                LiveAdTagDetailName = [LiveAdTagDetailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveAdTagDetailName.html).[FromProjectLocationLiveSessionLiveAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveAdTagDetailName.html#Google_Cloud_Video_Stitcher_V1_LiveAdTagDetailName_FromProjectLocationLiveSessionLiveAdTagDetail_System_String_System_String_System_String_System_String_)(projectId, location, sessionId, adTagDetailId)
            };
    
            // Call the API.
            [LiveAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveAdTagDetail.html) liveAdTagDetail = client.[GetLiveAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_GetLiveAdTagDetail_Google_Cloud_Video_Stitcher_V1_GetLiveAdTagDetailRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Return the result.
            return liveAdTagDetail;
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
    
    // getLiveAdTagDetail gets the specified ad tag detail for a live session.
    func getLiveAdTagDetail(w io.Writer, projectID, sessionID, adTagDetailID string) error {
    	// projectID := "my-project-id"
    	// sessionID := "my-session-id"
    	// adTagDetailID := "my-ad-tag-detail-id"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.GetLiveAdTagDetailRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/liveSessions/%s/liveAdTagDetails/%s", projectID, location, sessionID, adTagDetailID),
    	}
    	// Gets the ad tag detail.
    	response, err := client.GetLiveAdTagDetail(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.GetLiveAdTagDetail: %w", err)
    	}
    	b, err := json.MarshalIndent(response, "", " ")
    	if err != nil {
    		return fmt.Errorf("json.MarshalIndent: %w", err)
    	}
    	fmt.Fprintf(w, "Live ad tag detail:\n%v", string(b))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[GetLiveAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveAdTagDetailRequest.html);
    import com.google.cloud.video.stitcher.v1.[LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail.html);
    import com.google.cloud.video.stitcher.v1.[LiveAdTagDetailName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetailName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    
    public class GetLiveAdTagDetail {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String sessionId = "my-session-id";
        String adTagDetailId = "my-ad-tag-detail-id";
    
        getLiveAdTagDetail(projectId, location, sessionId, adTagDetailId);
      }
    
      // Gets a live ad tag detail in a live session.
      public static [LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail.html) getLiveAdTagDetail(
          String projectId, String location, String sessionId, String adTagDetailId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [GetLiveAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveAdTagDetailRequest.html) getLiveAdTagDetailRequest =
              [GetLiveAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveAdTagDetailRequest.html).newBuilder()
                  .setName(
                      [LiveAdTagDetailName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetailName.html).of(projectId, location, sessionId, adTagDetailId).toString())
                  .build();
    
          [LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail.html) response =
              videoStitcherServiceClient.getLiveAdTagDetail(getLiveAdTagDetailRequest);
          System.out.println("Live ad tag detail: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail.html#com_google_cloud_video_stitcher_v1_LiveAdTagDetail_getName__)());
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
    
    async function getLiveAdTagDetail() {
      // Construct request
      const request = {
        name: stitcherClient.[liveAdTagDetailPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(
          projectId,
          location,
          sessionId,
          adTagDetailId
        ),
      };
      const [adTagDetail] = await stitcherClient.getLiveAdTagDetail(request);
      console.log(`Live ad tag detail: ${adTagDetail.name}`);
    }
    
    getLiveAdTagDetail().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\GetLiveAdTagDetailRequest;
    
    /**
     * Gets the specified ad tag detail for the live session.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the session
     * @param string $sessionId            The ID of the session
     * @param string $adTagDetailId        The ID of the ad tag detail
     */
    function get_live_ad_tag_detail(
        string $callingProjectId,
        string $location,
        string $sessionId,
        string $adTagDetailId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->liveAdTagDetailName($callingProjectId, $location, $sessionId, $adTagDetailId);
        $request = (new GetLiveAdTagDetailRequest())
            ->setName($formattedName);
        $adTagDetail = $stitcherClient->getLiveAdTagDetail($request);
    
        // Print results
        printf('Live ad tag detail: %s' . PHP_EOL, $adTagDetail->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def get_live_ad_tag_detail(
        project_id: str, location: str, session_id: str, ad_tag_detail_id: str
    ) -> stitcher_v1.types.LiveAdTagDetail:
        """Gets the specified ad tag detail for a live session.
        Args:
            project_id: The GCP project ID.
            location: The location of the session.
            session_id: The ID of the live session.
            ad_tag_detail_id: The ID of the ad tag details.
    
        Returns:
            The live ad tag detail resource.
        """
    
        client = VideoStitcherServiceClient()
    
        name = client.live_ad_tag_detail_path(
            project_id, location, session_id, ad_tag_detail_id
        )
        response = client.get_live_ad_tag_detail(name=name)
        print(f"Live ad tag detail: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Get the specified ad tag detail for a live session
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param session_id [String] The live session ID (e.g. `my-live-session-id`)
    # @param ad_tag_detail_id [String] The ad tag detail ID (e.g. `my-ad-tag-id`)
    #
    def get_live_ad_tag_detail project_id:, location:, session_id:,
                               ad_tag_detail_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the live ad tag detail.
      name = client.live_ad_tag_detail_path project: project_id, location: location,
                                            live_session: session_id,
                                            live_ad_tag_detail: ad_tag_detail_id
    
      # Get the live ad tag detail.
      ad_tag_detail = client.get_live_ad_tag_detail name: name
    
      # Print the live ad tag detail name.
      puts "Live ad tag detail: #{ad_tag_detail.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videostitcherapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
