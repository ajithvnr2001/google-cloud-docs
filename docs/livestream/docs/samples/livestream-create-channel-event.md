---
url: https://docs.cloud.google.com/livestream/docs/samples/livestream-create-channel-event/
title: Create a channel event \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:33.716757+00:00
---

# Create a channel event  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/samples/livestream-create-channel-event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Samples ](https://docs.cloud.google.com/livestream/docs/samples)



#  Create a channel event Stay organized with collections  Save and categorize content based on your preferences. 

Create a channel event to execute an operation on a channel resource without needing to stop the channel. For example, you can use a channel event to create ad break markers.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage channel events](https://docs.cloud.google.com/livestream/docs/how-to/create-channel-events)
  * [Quickstart for an HLS live stream](https://docs.cloud.google.com/livestream/docs/quickstarts/quickstart-hls)
  * [Quickstart for an MPEG-DASH live stream](https://docs.cloud.google.com/livestream/docs/quickstarts/quickstart-dash)



## Code sample

### C#

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.html);
    
    public class CreateChannelEventSample
    {
        public Event CreateChannelEvent(
             string projectId, string locationId, string channelId, string eventId)
        {
            // Create the client.
            [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html) client = [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_Create)();
    
            [CreateEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.CreateEventRequest.html) request = new [CreateEventRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.CreateEventRequest.html)
            {
                ParentAsChannelName = [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ChannelName.html).[FromProjectLocationChannel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ChannelName.html#Google_Cloud_Video_LiveStream_V1_ChannelName_FromProjectLocationChannel_System_String_System_String_System_String_)(projectId, locationId, channelId),
                EventId = eventId,
                Event = new [Event](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Event.html)
                {
                    AdBreak = new Event.Types.AdBreakTask
                    {
                        Duration = new Google.Protobuf.WellKnownTypes.Duration
                        {
                            Seconds = 30
                        }
                    },
                    ExecuteNow = true
                }
            };
    
            // Make the request.
            [Event](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Event.html) response = client.[CreateEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_CreateEvent_Google_Cloud_Video_LiveStream_V1_ChannelName_Google_Cloud_Video_LiveStream_V1_Event_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
            return response;
        }
    }

### Go

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/livestream). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"github.com/golang/protobuf/ptypes/duration"
    
    	livestream "cloud.google.com/go/video/livestream/apiv1"
    	"cloud.google.com/go/video/livestream/apiv1/livestreampb"
    )
    
    // createChannelEvent creates a channel event. An event is a sub-resource of a
    // channel, which can be scheduled by the user to execute operations on a
    // channel resource without having to stop the channel. This sample creates an
    // ad break event.
    func createChannelEvent(w io.Writer, projectID, location, channelID, eventID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// channelID := "my-channel"
    	// eventID := "my-channel-event"
    	ctx := context.Background()
    	client, err := livestream.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_Close)()
    
    	req := &livestreampb.CreateEventRequest{
    		Parent:  fmt.Sprintf("projects/%s/locations/%s/channels/%s", projectID, location, channelID),
    		EventId: eventID,
    		Event: &livestreampb.Event{
    			Task: &livestreampb.Event_AdBreak{
    				AdBreak: &livestreampb.Event_AdBreakTask{
    					Duration: &duration.Duration{
    						Seconds: 30,
    					},
    				},
    			},
    			ExecuteNow: true,
    		},
    	}
    	// Creates the channel event.
    	response, err := client.CreateEvent(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateEvent: %w", err)
    	}
    
    	fmt.Fprintf(w, "Channel event: %v", response.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/overview). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.livestream.v1.[ChannelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ChannelName.html);
    import com.google.cloud.video.livestream.v1.[CreateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateEventRequest.html);
    import com.google.cloud.video.livestream.v1.[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.html);
    import com.google.cloud.video.livestream.v1.[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.html).[AdBreakTask](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.AdBreakTask.html);
    import com.google.cloud.video.livestream.v1.[LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    
    public class CreateChannelEvent {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String channelId = "my-channel-id";
        String eventId = "my-channel-event-id";
    
        createChannelEvent(projectId, location, channelId, eventId);
      }
    
      public static void createChannelEvent(
          String projectId, String location, String channelId, String eventId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. In this example, try-with-resources is used
        // which automatically calls close() on the client to clean up resources.
        try ([LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html) livestreamServiceClient = [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html).create()) {
          var createEventRequest =
              [CreateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateEventRequest.html).newBuilder()
                  .setParent([ChannelName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ChannelName.html).of(projectId, location, channelId).toString())
                  .[setEventId](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateEventRequest.Builder.html#com_google_cloud_video_livestream_v1_CreateEventRequest_Builder_setEventId_java_lang_String_)(eventId)
                  .setEvent(
                      [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.html).newBuilder()
                          .[setAdBreak](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.Builder.html#com_google_cloud_video_livestream_v1_Event_Builder_setAdBreak_com_google_cloud_video_livestream_v1_Event_AdBreakTask_)(
                              [AdBreakTask](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.AdBreakTask.html).newBuilder()
                                  .setDuration([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(30).build())
                                  .build())
                          .[setExecuteNow](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.Builder.html#com_google_cloud_video_livestream_v1_Event_Builder_setExecuteNow_boolean_)(true)
                          .build())
                  .build();
    
          [Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.html) response = livestreamServiceClient.createEvent(createEventRequest);
          System.out.println("Channel event: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event.html#com_google_cloud_video_livestream_v1_Event_getName__)());
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
    // eventId = 'my-channel-event';
    
    // Imports the Livestream library
    const {LivestreamServiceClient} = require('[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)').v1;
    
    // Instantiates a client
    const livestreamServiceClient = new [LivestreamServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)();
    
    async function createChannelEvent() {
      // Construct request
      const request = {
        parent: livestreamServiceClient.[channelPath](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)(
          projectId,
          location,
          channelId
        ),
        eventId: eventId,
        event: {
          adBreak: {
            duration: {
              seconds: 30,
            },
          },
          executeNow: true,
        },
      };
    
      // Run request
      const [event] = await livestreamServiceClient.createEvent(request);
      console.log(`Channel event: ${event.name}`);
    }
    
    createChannelEvent();

### PHP

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videolivestream/readme). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\LiveStream\V1\Event;
    use Google\Cloud\Video\LiveStream\V1\Client\LivestreamServiceClient;
    use Google\Cloud\Video\LiveStream\V1\CreateEventRequest;
    use Google\Protobuf\Duration;
    
    /**
     * Creates a channel event. This particular sample inserts an ad break marker.
     * Other event types are supported.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the channel
     * @param string  $channelId          The ID of the channel
     * @param string  $eventId            The ID of the channel event
     */
    function create_channel_event(
        string $callingProjectId,
        string $location,
        string $channelId,
        string $eventId
    ): void {
        // Instantiate a client.
        $livestreamClient = new LivestreamServiceClient();
    
        $parent = $livestreamClient->channelName($callingProjectId, $location, $channelId);
    
        $eventAdBreak = (new Event\AdBreakTask())
            ->setDuration(new Duration(['seconds' => 30]));
        $event = (new Event())
            ->setAdBreak($eventAdBreak)
            ->setExecuteNow(true);
    
        // Run the channel event creation request.
        $request = (new CreateEventRequest())
            ->setParent($parent)
            ->setEvent($event)
            ->setEventId($eventId);
        $response = $livestreamClient->createEvent($request);
        // Print results.
        printf('Channel event: %s' . PHP_EOL, $response->getName());
    }

### Python

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/livestream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import live_stream_v1
    from google.cloud.video.live_stream_v1.services.livestream_service import (
        LivestreamServiceClient,
    )
    from google.protobuf import duration_pb2 as duration
    
    
    def create_channel_event(
        project_id: str, location: str, channel_id: str, event_id: str
    ) -> live_stream_v1.types.Event:
        """Creates a channel event.
        Args:
            project_id: The GCP project ID.
            location: The location of the channel.
            channel_id: The user-defined channel ID.
            event_id: The user-defined event ID."""
    
        client = LivestreamServiceClient()
        parent = f"projects/{project_id}/locations/{location}/channels/{channel_id}"
        name = f"projects/{project_id}/locations/{location}/channels/{channel_id}/events/{event_id}"
    
        event = live_stream_v1.types.Event(
            name=name,
            ad_break=live_stream_v1.types.Event.AdBreakTask(
                duration=duration.Duration(
                    seconds=30,
                ),
            ),
            execute_now=True,
        )
    
        response = client.create_event(parent=parent, event=event, event_id=event_id)
        print(f"Channel event: {response.name}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/live_stream"
    
    ##
    # Create a channel event
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location [String] The location (e.g. "us-central1")
    # @param channel_id [String] Your channel name (e.g. "my-channel")
    # @param event_id [String] Your event name (e.g. "my-event")
    #
    def create_channel_event project_id:, location:, channel_id:, event_id:
      # Create a Live Stream client.
      client = Google::Cloud::Video::LiveStream.livestream_service
    
      # Build the resource name of the parent.
      parent = client.channel_path project: project_id, location: location, channel: channel_id
    
      # Set the event fields.
      new_event = {
        ad_break: {
          duration: {
            seconds: 100
          }
        },
        execute_now: true
      }
    
      response = client.create_event parent: parent, event: new_event, event_id: event_id
    
      # Print the channel event name.
      puts "Channel event: #{response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=livestreamapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
