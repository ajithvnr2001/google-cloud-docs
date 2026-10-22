---
url: https://docs.cloud.google.com/livestream/docs/samples/livestream-create-channel/
title: Create a channel \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:37.760919+00:00
---

# Create a channel  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/samples/livestream-create-channel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Samples ](https://docs.cloud.google.com/livestream/docs/samples)



#  Create a channel Stay organized with collections  Save and categorize content based on your preferences. 

Create a channel that ingests the input stream through an input endpoint, transcodes the input stream into multiple renditions, and publishes output live streams in certain formats in the specified location. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage channels](https://docs.cloud.google.com/livestream/docs/how-to/create-channels)
  * [Insert a slate into a live stream](https://docs.cloud.google.com/livestream/docs/how-to/insert-slate)
  * [Quickstart for an HLS live stream](https://docs.cloud.google.com/livestream/docs/quickstarts/quickstart-hls)



## Code sample

### C#

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public class CreateChannelSample
    {
        public async Task<Channel> CreateChannelAsync(
             string projectId, string locationId, string channelId, string inputId, string outputUri)
        {
            // Create the client.
            [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html) client = [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_Create)();
    
            [InputAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.InputAttachment.html) inputAttachment = new [InputAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.InputAttachment.html)
            {
                Key = "my-input",
                InputAsInputName = [InputName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.InputName.html).[FromProjectLocationInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.InputName.html#Google_Cloud_Video_LiveStream_V1_InputName_FromProjectLocationInput_System_String_System_String_System_String_)(projectId, locationId, inputId)
            };
    
            [VideoStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.VideoStream.html) videoStream = new [VideoStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.VideoStream.html)
            {
                H264 = new VideoStream.Types.H264CodecSettings
                {
                    Profile = "high",
                    BitrateBps = 3000000,
                    FrameRate = 30,
                    HeightPixels = 720,
                    WidthPixels = 1280
                }
            };
    
            [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ElementaryStream.html) elementaryStreamVideo = new [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ElementaryStream.html)
            {
                Key = "es_video",
                VideoStream = videoStream
            };
    
            [AudioStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.AudioStream.html) audioStream = new [AudioStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.AudioStream.html)
            {
                Codec = "aac",
                ChannelCount = 2,
                BitrateBps = 160000
            };
    
            [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ElementaryStream.html) elementaryStreamAudio = new [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.ElementaryStream.html)
            {
                Key = "es_audio",
                AudioStream = audioStream
            };
    
            [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.MuxStream.html) muxVideo = new [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.MuxStream.html)
            {
                Key = "mux_video",
                ElementaryStreams = { "es_video" },
                SegmentSettings = new [SegmentSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.SegmentSettings.html)
                {
                    SegmentDuration = new Google.Protobuf.WellKnownTypes.Duration
                    {
                        Seconds = 2
                    }
                }
            };
    
            [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.MuxStream.html) muxAudio = new [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.MuxStream.html)
            {
                Key = "mux_audio",
                ElementaryStreams = { "es_audio" },
                SegmentSettings = new [SegmentSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.SegmentSettings.html)
                {
                    SegmentDuration = new Google.Protobuf.WellKnownTypes.Duration
                    {
                        Seconds = 2
                    }
                }
            };
    
            [CreateChannelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.CreateChannelRequest.html) request = new [CreateChannelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.CreateChannelRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, locationId),
                ChannelId = channelId,
                Channel = new [Channel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Channel.html)
                {
                    InputAttachments = { inputAttachment },
                    Output = new Channel.Types.Output
                    {
                        Uri = outputUri
                    },
                    ElementaryStreams = { elementaryStreamVideo, elementaryStreamAudio },
                    MuxStreams = { muxVideo, muxAudio },
                    Manifests = {
                        new [Manifest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest.html) {
                            FileName = "manifest.m3u8",
                            Type = [Manifest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest.Types.html).[ManifestType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest.Types.ManifestType.html).[Hls](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Manifest.Types.ManifestType.html#Google_Cloud_Video_LiveStream_V1_Manifest_Types_ManifestType_Hls),
                            MuxStreams = { "mux_video", "mux_audio" },
                            MaxSegmentCount = 5
                        }
                    }
                }
            };
    
            // Make the request.
            Operation<Channel, OperationMetadata> response = await client.[CreateChannelAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_CreateChannelAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_LiveStream_V1_Channel_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<Channel, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
            // Retrieve the operation result.
            return completedResponse.Result;
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
    
    // createChannel creates a channel.
    func createChannel(w io.Writer, projectID, location, channelID, inputID, outputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// channelID := "my-channel"
    	// inputID := "my-input"
    	// outputURI := "gs://my-bucket/my-output-folder/"
    	ctx := context.Background()
    	client, err := livestream.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_Close)()
    
    	req := &livestreampb.CreateChannelRequest{
    		Parent:    fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		ChannelId: channelID,
    		Channel: &livestreampb.Channel{
    			InputAttachments: []*livestreampb.InputAttachment{
    				{
    					Key:   "my-input",
    					Input: fmt.Sprintf("projects/%s/locations/%s/inputs/%s", projectID, location, inputID),
    				},
    			},
    			Output: &livestreampb.Channel_Output{
    				Uri: outputURI,
    			},
    			ElementaryStreams: []*livestreampb.ElementaryStream{
    				{
    					Key: "es_video",
    					ElementaryStream: &livestreampb.ElementaryStream_VideoStream{
    						VideoStream: &livestreampb.VideoStream{
    							CodecSettings: &livestreampb.VideoStream_H264{
    								H264: &livestreampb.VideoStream_H264CodecSettings{
    									Profile:      "high",
    									BitrateBps:   3000000,
    									FrameRate:    30,
    									HeightPixels: 720,
    									WidthPixels:  1280,
    								},
    							},
    						},
    					},
    				},
    				{
    					Key: "es_audio",
    					ElementaryStream: &livestreampb.ElementaryStream_AudioStream{
    						AudioStream: &livestreampb.AudioStream{
    							Codec:        "aac",
    							ChannelCount: 2,
    							BitrateBps:   160000,
    						},
    					},
    				},
    			},
    			MuxStreams: []*livestreampb.MuxStream{
    				{
    					Key:               "mux_video",
    					ElementaryStreams: []string{"es_video"},
    					SegmentSettings: &livestreampb.SegmentSettings{
    						SegmentDuration: &duration.Duration{
    							Seconds: 2,
    						},
    					},
    				},
    				{
    					Key:               "mux_audio",
    					ElementaryStreams: []string{"es_audio"},
    					SegmentSettings: &livestreampb.SegmentSettings{
    						SegmentDuration: &duration.Duration{
    							Seconds: 2,
    						},
    					},
    				},
    			},
    			Manifests: []*livestreampb.Manifest{
    				{
    					FileName:        "manifest.m3u8",
    					Type:            livestreampb.[Manifest_HLS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1/livestreampb.html#cloud_google_com_go_video_livestream_apiv1_livestreampb_Manifest_MANIFEST_TYPE_UNSPECIFIED_Manifest_HLS_Manifest_DASH),
    					MuxStreams:      []string{"mux_video", "mux_audio"},
    					MaxSegmentCount: 5,
    				},
    			},
    		},
    	}
    	// Creates the channel.
    	op, err := client.CreateChannel(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateChannel: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Channel: %v", response.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/overview). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.livestream.v1.[AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.AudioStream.html);
    import com.google.cloud.video.livestream.v1.[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel.html);
    import com.google.cloud.video.livestream.v1.[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel.html).Output;
    import com.google.cloud.video.livestream.v1.[CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateChannelRequest.html);
    import com.google.cloud.video.livestream.v1.[ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ElementaryStream.html);
    import com.google.cloud.video.livestream.v1.[InputAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.InputAttachment.html);
    import com.google.cloud.video.livestream.v1.[InputName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.InputName.html);
    import com.google.cloud.video.livestream.v1.[LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html);
    import com.google.cloud.video.livestream.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LocationName.html);
    import com.google.cloud.video.livestream.v1.[Manifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Manifest.html);
    import com.google.cloud.video.livestream.v1.[Manifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Manifest.html).[ManifestType](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Manifest.ManifestType.html);
    import com.google.cloud.video.livestream.v1.[MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.MuxStream.html);
    import com.google.cloud.video.livestream.v1.[SegmentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.SegmentSettings.html);
    import com.google.cloud.video.livestream.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.VideoStream.html);
    import com.google.cloud.video.livestream.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.VideoStream.html).[H264CodecSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.VideoStream.H264CodecSettings.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateChannel {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String channelId = "my-channel-id";
        String inputId = "my-input-id";
        String outputUri = "gs://my-bucket/my-output-folder/";
    
        createChannel(projectId, location, channelId, inputId, outputUri);
      }
    
      public static void createChannel(
          String projectId, String location, String channelId, String inputId, String outputUri)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html) livestreamServiceClient = [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html).create();
        [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.VideoStream.html) videoStream =
            [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.VideoStream.html).newBuilder()
                .[setH264](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.VideoStream.Builder.html#com_google_cloud_video_livestream_v1_VideoStream_Builder_setH264_com_google_cloud_video_livestream_v1_VideoStream_H264CodecSettings_)(
                    [H264CodecSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.VideoStream.H264CodecSettings.html).newBuilder()
                        .[setProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.VideoStream.H264CodecSettings.Builder.html#com_google_cloud_video_livestream_v1_VideoStream_H264CodecSettings_Builder_setProfile_java_lang_String_)("high")
                        .setBitrateBps(3000000)
                        .setFrameRate(30)
                        .setHeightPixels(720)
                        .setWidthPixels(1280))
                .build();
    
        [AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.AudioStream.html) audioStream =
            [AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.AudioStream.html).newBuilder().setCodec("aac").setChannelCount(2).setBitrateBps(160000).build();
    
        var createChannelRequest =
            [CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateChannelRequest.html).newBuilder()
                .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LocationName.html).of(projectId, location).toString())
                .[setChannelId](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateChannelRequest.Builder.html#com_google_cloud_video_livestream_v1_CreateChannelRequest_Builder_setChannelId_java_lang_String_)(channelId)
                .setChannel(
                    [Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel.html).newBuilder()
                        .[addInputAttachments](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel.Builder.html#com_google_cloud_video_livestream_v1_Channel_Builder_addInputAttachments_com_google_cloud_video_livestream_v1_InputAttachment_)(
                            0,
                            [InputAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.InputAttachment.html).newBuilder()
                                .setKey("my-input")
                                .setInput([InputName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.InputName.html).of(projectId, location, inputId).toString())
                                .build())
                        .[setOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel.Builder.html#com_google_cloud_video_livestream_v1_Channel_Builder_setOutput_com_google_cloud_video_livestream_v1_Channel_Output_)(Output.newBuilder().setUri(outputUri).build())
                        .addElementaryStreams(
                            [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ElementaryStream.html).newBuilder()
                                .setKey("es_video")
                                .[setVideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ElementaryStream.Builder.html#com_google_cloud_video_livestream_v1_ElementaryStream_Builder_setVideoStream_com_google_cloud_video_livestream_v1_VideoStream_)(videoStream))
                        .addElementaryStreams(
                            [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ElementaryStream.html).newBuilder()
                                .setKey("es_audio")
                                .[setAudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ElementaryStream.Builder.html#com_google_cloud_video_livestream_v1_ElementaryStream_Builder_setAudioStream_com_google_cloud_video_livestream_v1_AudioStream_)(audioStream))
                        .addMuxStreams(
                            [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.MuxStream.html).newBuilder()
                                .setKey("mux_video")
                                .addElementaryStreams("es_video")
                                .[setSegmentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.MuxStream.Builder.html#com_google_cloud_video_livestream_v1_MuxStream_Builder_setSegmentSettings_com_google_cloud_video_livestream_v1_SegmentSettings_)(
                                    [SegmentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.SegmentSettings.html).newBuilder()
                                        .[setSegmentDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.SegmentSettings.Builder.html#com_google_cloud_video_livestream_v1_SegmentSettings_Builder_setSegmentDuration_com_google_protobuf_Duration_)(
                                            [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(2).build())
                                        .build())
                                .build())
                        .addMuxStreams(
                            [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.MuxStream.html).newBuilder()
                                .setKey("mux_audio")
                                .addElementaryStreams("es_audio")
                                .[setSegmentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.MuxStream.Builder.html#com_google_cloud_video_livestream_v1_MuxStream_Builder_setSegmentSettings_com_google_cloud_video_livestream_v1_SegmentSettings_)(
                                    [SegmentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.SegmentSettings.html).newBuilder()
                                        .[setSegmentDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.SegmentSettings.Builder.html#com_google_cloud_video_livestream_v1_SegmentSettings_Builder_setSegmentDuration_com_google_protobuf_Duration_)(
                                            [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(2).build())
                                        .build())
                                .build())
                        .[addManifests](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel.Builder.html#com_google_cloud_video_livestream_v1_Channel_Builder_addManifests_com_google_cloud_video_livestream_v1_Manifest_)(
                            [Manifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Manifest.html).newBuilder()
                                .setFileName("manifest.m3u8")
                                .setType([ManifestType](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Manifest.ManifestType.html).HLS)
                                .addMuxStreams("mux_video")
                                .addMuxStreams("mux_audio")
                                .[setMaxSegmentCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Manifest.Builder.html#com_google_cloud_video_livestream_v1_Manifest_Builder_setMaxSegmentCount_int_)(5)
                                .build()))
                .build();
        // First API call in a project can take up to 10 minutes.
        [Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel.html) result =
            livestreamServiceClient
                .[createChannelAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html#com_google_cloud_video_livestream_v1_LivestreamServiceClient_createChannelAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_livestream_v1_LocationName_com_google_cloud_video_livestream_v1_Channel_java_lang_String_)(createChannelRequest)
                .get(10, TimeUnit.MINUTES);
        System.out.println("Channel: " + result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel.html#com_google_cloud_video_livestream_v1_Channel_getName__)());
        livestreamServiceClient.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html#com_google_cloud_video_livestream_v1_LivestreamServiceClient_close__)();
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
    // inputId = 'my-input';
    // outputUri = 'gs://my-bucket/my-output-folder/';
    
    // Imports the Livestream library
    const {LivestreamServiceClient} = require('[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)').v1;
    
    // Instantiates a client
    const livestreamServiceClient = new [LivestreamServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)();
    
    async function createChannel() {
      // Construct request
      const request = {
        parent: livestreamServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)(projectId, location),
        channelId: channelId,
        channel: {
          inputAttachments: [
            {
              key: 'my-input',
              input: livestreamServiceClient.[inputPath](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)(
                projectId,
                location,
                inputId
              ),
            },
          ],
          output: {
            uri: outputUri,
          },
          elementaryStreams: [
            {
              key: 'es_video',
              videoStream: {
                h264: {
                  profile: 'high',
                  heightPixels: 720,
                  widthPixels: 1280,
                  bitrateBps: 3000000,
                  frameRate: 30,
                },
              },
            },
            {
              key: 'es_audio',
              audioStream: {
                codec: 'aac',
                channelCount: 2,
                bitrateBps: 160000,
              },
            },
          ],
          muxStreams: [
            {
              key: 'mux_video',
              elementaryStreams: ['es_video'],
              segmentSettings: {
                seconds: 2,
              },
            },
            {
              key: 'mux_audio',
              elementaryStreams: ['es_audio'],
              segmentSettings: {
                seconds: 2,
              },
            },
          ],
          manifests: [
            {
              fileName: 'manifest.m3u8',
              type: '[HLS](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/protos.google.cloud.video.livestream.v1.manifest.manifesttype.html)',
              muxStreams: ['mux_video', 'mux_audio'],
              maxSegmentCount: 5,
            },
          ],
        },
      };
    
      // Run request
      const [operation] = await livestreamServiceClient.createChannel(request);
      const response = await operation.promise();
      const [channel] = response;
      console.log(`Channel: ${channel.name}`);
    }
    
    createChannel();

### PHP

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videolivestream/readme). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\LiveStream\V1\AudioStream;
    use Google\Cloud\Video\LiveStream\V1\Channel;
    use Google\Cloud\Video\LiveStream\V1\ElementaryStream;
    use Google\Cloud\Video\LiveStream\V1\InputAttachment;
    use Google\Cloud\Video\LiveStream\V1\Client\LivestreamServiceClient;
    use Google\Cloud\Video\LiveStream\V1\CreateChannelRequest;
    use Google\Cloud\Video\LiveStream\V1\Manifest;
    use Google\Cloud\Video\LiveStream\V1\MuxStream;
    use Google\Cloud\Video\LiveStream\V1\SegmentSettings;
    use Google\Cloud\Video\LiveStream\V1\VideoStream;
    use Google\Protobuf\Duration;
    
    /**
     * Creates a channel.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the channel
     * @param string  $channelId          The ID of the channel to be created
     * @param string  $inputId            The ID of the input for the channel
     * @param string  $outputUri          Uri of the channel output folder in a
     *                                    Cloud Storage bucket. (e.g.
     *                                    "gs://my-bucket/my-output-folder/")
     */
    function create_channel(
        string $callingProjectId,
        string $location,
        string $channelId,
        string $inputId,
        string $outputUri
    ): void {
        // Instantiate a client.
        $livestreamClient = new LivestreamServiceClient();
    
        $parent = $livestreamClient->locationName($callingProjectId, $location);
        $channelName = $livestreamClient->channelName($callingProjectId, $location, $channelId);
        $inputName = $livestreamClient->inputName($callingProjectId, $location, $inputId);
    
        $channel = (new Channel())
            ->setName($channelName)
            ->setInputAttachments([
                new InputAttachment([
                    'key' => 'my-input',
                    'input' => $inputName
                ])
            ])
            ->setElementaryStreams([
                new ElementaryStream([
                    'key' => 'es_video',
                    'video_stream' => new VideoStream([
                        'h264' => new VideoStream\H264CodecSettings([
                            'profile' => 'high',
                            'width_pixels' => 1280,
                            'height_pixels' => 720,
                            'bitrate_bps' => 3000000,
                            'frame_rate' => 30
                        ])
                    ]),
                ]),
                new ElementaryStream([
                    'key' => 'es_audio',
                    'audio_stream' => new AudioStream([
                        'codec' => 'aac',
                        'channel_count' => 2,
                        'bitrate_bps' => 160000
                    ])
                ])
            ])
            ->setOutput(new Channel\Output(['uri' => $outputUri]))
            ->setMuxStreams([
                new MuxStream([
                    'key' => 'mux_video',
                    'elementary_streams' => ['es_video'],
                    'segment_settings' => new SegmentSettings([
                        'segment_duration' => new Duration(['seconds' => 2])
                    ])
                ]),
                new MuxStream([
                    'key' => 'mux_audio',
                    'elementary_streams' => ['es_audio'],
                    'segment_settings' => new SegmentSettings([
                        'segment_duration' => new Duration(['seconds' => 2])
                    ])
                ]),
            ])
            ->setManifests([
                new Manifest([
                    'file_name' => 'manifest.m3u8',
                    'type' => Manifest\ManifestType::HLS,
                    'mux_streams' => ['mux_video', 'mux_audio'],
                    'max_segment_count' => 5
                ])
            ]);
    
        // Run the channel creation request. The response is a long-running operation ID.
        $request = (new CreateChannelRequest())
            ->setParent($parent)
            ->setChannel($channel)
            ->setChannelId($channelId);
        $operationResponse = $livestreamClient->createChannel($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('Channel: %s' . PHP_EOL, $result->getName());
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
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
    
    
    def create_channel(
        project_id: str, location: str, channel_id: str, input_id: str, output_uri: str
    ) -> live_stream_v1.types.Channel:
        """Creates a channel.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the channel.
            channel_id: The user-defined channel ID.
            input_id: The user-defined input ID.
            output_uri: Uri of the channel output folder in a Cloud Storage bucket."""
    
        client = LivestreamServiceClient()
        parent = f"projects/{project_id}/locations/{location}"
        input = f"projects/{project_id}/locations/{location}/inputs/{input_id}"
        name = f"projects/{project_id}/locations/{location}/channels/{channel_id}"
    
        channel = live_stream_v1.types.Channel(
            name=name,
            input_attachments=[
                live_stream_v1.types.InputAttachment(
                    key="my-input",
                    input=input,
                ),
            ],
            output=live_stream_v1.types.Channel.Output(
                uri=output_uri,
            ),
            elementary_streams=[
                live_stream_v1.types.ElementaryStream(
                    key="es_video",
                    video_stream=live_stream_v1.types.VideoStream(
                        h264=live_stream_v1.types.VideoStream.H264CodecSettings(
                            profile="high",
                            width_pixels=1280,
                            height_pixels=720,
                            bitrate_bps=3000000,
                            frame_rate=30,
                        ),
                    ),
                ),
                live_stream_v1.types.ElementaryStream(
                    key="es_audio",
                    audio_stream=live_stream_v1.types.AudioStream(
                        codec="aac", channel_count=2, bitrate_bps=160000
                    ),
                ),
            ],
            mux_streams=[
                live_stream_v1.types.MuxStream(
                    key="mux_video",
                    elementary_streams=["es_video"],
                    segment_settings=live_stream_v1.types.SegmentSettings(
                        segment_duration=duration.Duration(
                            seconds=2,
                        ),
                    ),
                ),
                live_stream_v1.types.MuxStream(
                    key="mux_audio",
                    elementary_streams=["es_audio"],
                    segment_settings=live_stream_v1.types.SegmentSettings(
                        segment_duration=duration.Duration(
                            seconds=2,
                        ),
                    ),
                ),
            ],
            manifests=[
                live_stream_v1.types.Manifest(
                    file_name="manifest.m3u8",
                    type_="HLS",
                    mux_streams=["mux_video", "mux_audio"],
                    max_segment_count=5,
                ),
            ],
        )
        operation = client.create_channel(
            parent=parent, channel=channel, channel_id=channel_id
        )
        response = operation.result(600)
        print(f"Channel: {response.name}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/live_stream"
    
    ##
    # Create a channel
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location [String] The location (e.g. "us-central1")
    # @param channel_id [String] Your channel name (e.g. "my-channel")
    # @param input_id [String] Your input name (e.g. "my-input")
    # @param output_uri [String] Uri of the channel output folder in a Cloud Storage
    #     bucket. (e.g. "gs://my-bucket/my-output-folder/";)
    #
    def create_channel project_id:, location:, channel_id:, input_id:, output_uri:
      # Create a Live Stream client.
      client = Google::Cloud::Video::LiveStream.livestream_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
      # Build the resource name of the input.
      input_path = client.input_path project: project_id, location: location, input: input_id
    
      # Set the channel fields.
      new_channel = {
        input_attachments: [
          {
            key: "my-input",
            input: input_path
          }
        ],
        output: {
          uri: output_uri
        },
        elementary_streams: [
          {
            key: "es_video",
            video_stream: {
              h264: {
                profile: "high",
                bitrate_bps: 3_000_000,
                frame_rate: 30,
                height_pixels: 720,
                width_pixels: 1280
              }
            }
          },
          {
            key: "es_audio",
            audio_stream: {
              codec: "aac",
              channel_count: 2,
              bitrate_bps: 160_000
            }
          }
        ],
        mux_streams: [
          {
            key: "mux_video",
            elementary_streams: [
              "es_video"
            ],
            segment_settings: {
              segment_duration: {
                seconds: 2
              }
            }
          },
          {
            key: "mux_audio",
            elementary_streams: [
              "es_audio"
            ],
            segment_settings: {
              segment_duration: {
                seconds: 2
              }
            }
          }
        ],
        manifests: [
          {
            file_name: "main.m3u8",
            type: Google::Cloud::Video::LiveStream::V1::Manifest::ManifestType::HLS,
            mux_streams: [
              "mux_video", "mux_audio"
            ],
            max_segment_count: 5
          }
        ]
      }
    
      operation = client.create_channel parent: parent, channel: new_channel, channel_id: channel_id
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the channel name.
      puts "Channel: #{operation.response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=livestreamapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
