---
url: https://docs.cloud.google.com/livestream/docs/samples/livestream-list-channel-events/
title: List channel events \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:32.610482+00:00
---

# List channel events  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/samples/livestream-list-channel-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Samples ](https://docs.cloud.google.com/livestream/docs/samples)



#  List channel events Stay organized with collections  Save and categorize content based on your preferences. 

List all channel events for a live stream channel resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage channel events](https://docs.cloud.google.com/livestream/docs/how-to/create-channel-events)



## Code sample

### C#

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.html);
    using System.Collections.Generic;
    using System.Linq;
    
    public class ListChannelEventsSample
    {
        public IList<Event> ListChannelEvents(
            string projectId, string regionId, string channelId)
        {
            // Create the client.
            [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html) client = [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_Create)();
    
            [ListEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ListEventsRequest.html) request = new [ListEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ListEventsRequest.html)
            {
                ParentAsChannelName = [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ChannelName.html).[FromProjectLocationChannel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ChannelName.html#Google_Cloud_Video_LiveStream_V1_ChannelName_FromProjectLocationChannel_System_String_System_String_System_String_)(projectId, regionId, channelId)
            };
    
            // Make the request.
            PagedEnumerable<ListEventsResponse, Event> response = client.[ListEvents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_ListEvents_Google_Cloud_Video_LiveStream_V1_ChannelName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // The returned sequence will lazily perform RPCs as it's being iterated over.
            return response.ToList();
        }
    }

### Go

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/livestream). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"google.golang.org/api/iterator"
    
    	livestream "cloud.google.com/go/video/livestream/apiv1"
    	"cloud.google.com/go/video/livestream/apiv1/livestreampb"
    )
    
    // listChannelEvents lists all channel events for a given channel.
    func listChannelEvents(w io.Writer, projectID, location, channelID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// channelID := "my-channel-id"
    	ctx := context.Background()
    	client, err := livestream.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_Close)()
    
    	req := &livestreampb.ListEventsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s/channels/%s", projectID, location, channelID),
    	}
    
    	it := client.ListEvents(ctx, req)
    	fmt.Fprintln(w, "Channel events:")
    
    	for {
    		response, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListEvents: %w", err)
    		}
    		fmt.Fprintln(w, response.GetName())
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/overview). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.livestream.v1.[ChannelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ChannelName.html);
    import com.google.cloud.video.livestream.v1.[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.html);
    import com.google.cloud.video.livestream.v1.[ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListEventsRequest.html);
    import com.google.cloud.video.livestream.v1.[LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html);
    import java.io.IOException;
    
    public class ListChannelEvents {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String channelId = "my-channel-id";
    
        listChannelEvents(projectId, location, channelId);
      }
    
      public static void listChannelEvents(String projectId, String location, String channelId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. In this example, try-with-resources is used
        // which automatically calls close() on the client to clean up resources.
        try ([LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html) livestreamServiceClient = [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html).create()) {
          var listEventsRequest =
              [ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListEventsRequest.html).newBuilder()
                  .setParent([ChannelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ChannelName.html).of(projectId, location, channelId).toString())
                  .build();
    
          [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html).[ListEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.ListEventsPagedResponse.html) response =
              livestreamServiceClient.listEvents(listEventsRequest);
          System.out.println("Channel events:");
    
          for ([Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.html) event : response.iterateAll()) {
            System.out.println(event.getName());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/livestream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // channelId = 'my-channel';
    
    // Imports the Livestream library
    const {LivestreamServiceClient} = require('[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)').v1;
    
    // Instantiates a client
    const livestreamServiceClient = new [LivestreamServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)();
    
    async function listChannelEvents() {
      const iterable = await livestreamServiceClient.[listEventsAsync](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)({
        parent: livestreamServiceClient.[channelPath](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)(
          projectId,
          location,
          channelId
        ),
      });
      console.info('Channel events:');
      for await (const response of iterable) {
        console.log(response.name);
      }
    }
    
    listChannelEvents();

### PHP

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videolivestream/readme). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\LiveStream\V1\Client\LivestreamServiceClient;
    use Google\Cloud\Video\LiveStream\V1\ListEventsRequest;
    
    /**
     * Lists the channel events for a given channel.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the channel
     * @param string  $channelId          The ID of the channel
     */
    function list_channel_events(
        string $callingProjectId,
        string $location,
        string $channelId
    ): void {
        // Instantiate a client.
        $livestreamClient = new LivestreamServiceClient();
        $parent = $livestreamClient->channelName($callingProjectId, $location, $channelId);
        $request = (new ListEventsRequest())
            ->setParent($parent);
    
        $response = $livestreamClient->listEvents($request);
        // Print the channel list.
        $events = $response->iterateAllElements();
        print('Channel events:' . PHP_EOL);
        foreach ($events as $event) {
            printf('%s' . PHP_EOL, $event->getName());
        }
    }

### Python

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/livestream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.live_stream_v1.services.livestream_service import (
        LivestreamServiceClient,
        pagers,
    )
    
    
    def list_channel_events(
        project_id: str, location: str, channel_id: str
    ) -> pagers.ListEventsPager:
        """Lists all events for a channel.
        Args:
            project_id: The GCP project ID.
            location: The location of the channel.
            channel_id: The user-defined channel ID."""
    
        client = LivestreamServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}/channels/{channel_id}"
        page_result = client.list_events(parent=parent)
        print("Events:")
    
        responses = []
        for response in page_result:
            print(response.name)
            responses.append(response)
    
        return responses
    
    

### Ruby

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/live_stream"
    
    ##
    # List the channel events
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location [String] The location (e.g. "us-central1")
    # @param channel_id [String] Your channel name (e.g. "my-channel")
    #
    def list_channel_events project_id:, location:, channel_id:
      # Create a Live Stream client.
      client = Google::Cloud::Video::LiveStream.livestream_service
    
      # Build the resource name of the parent.
      parent = client.channel_path project: project_id, location: location, channel: channel_id
    
      # Get the list of channel events.
      response = client.list_events parent: parent
    
      puts "Channel events:"
      # Print out all channel events.
      response.each do |event|
        puts event.name
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=livestreamapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
