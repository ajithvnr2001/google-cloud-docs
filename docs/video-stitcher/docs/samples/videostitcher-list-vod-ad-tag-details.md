---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-list-vod-ad-tag-details/
title: List VOD ad tag details \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:20.851386+00:00
---

# List VOD ad tag details  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-list-vod-ad-tag-details/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  List VOD ad tag details Stay organized with collections  Save and categorize content based on your preferences. 

List all Video Stitcher ad tag details for a VOD session.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage a VOD session](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-vod-sessions)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videostitcherapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
