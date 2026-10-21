---
url: https://docs.cloud.google.com/transcoder/docs/samples/transcoder-create-job-with-standalone-captions/
title: Create a job that can use captions from a standalone file \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:06.304153+00:00
---

# Create a job that can use captions from a standalone file  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/samples/transcoder-create-job-with-standalone-captions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Samples ](https://docs.cloud.google.com/transcoder/docs/samples)



#  Create a job that can use captions from a standalone file Stay organized with collections  Save and categorize content based on your preferences. 

Create a transcoding job that can use captions from a standalone file. Captions can include both closed captions and subtitles.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Adding closed captions and subtitles](https://docs.cloud.google.com/transcoder/docs/how-to/captions-and-subtitles)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/transcoder). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"github.com/golang/protobuf/ptypes/duration"
    
    	transcoder "cloud.google.com/go/video/transcoder/apiv1"
    	"cloud.google.com/go/video/transcoder/apiv1/transcoderpb"
    )
    
    // createJobWithStandaloneCaptions creates a job that can use subtitles from a
    // standalone file. See https://cloud.google.com/transcoder/docs/how-to/captions-and-subtitles
    // for more information.
    func createJobWithStandaloneCaptions(w io.Writer, projectID string, location string, inputVideoURI string, inputSubtitles1URI string, inputSubtitles2URI string, outputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputVideoURI := "gs://my-bucket/my-video-file"
    	// inputSubtitles1URI := "gs://my-bucket/my-subtitles-file1"
    	// inputSubtitles2URI := "gs://my-bucket/my-subtitles-file2"
    	// outputURI := "gs://my-bucket/my-output-folder/"
    
    	ctx := context.Background()
    	client, err := transcoder.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_Close)()
    
    	// Set up elementary streams. The InputKey field refers to inputs in
    	// the Inputs array defined the job config.
    	elementaryStreams := []*transcoderpb.ElementaryStream{
    		{
    			Key: "video_stream0",
    			ElementaryStream: &transcoderpb.ElementaryStream_VideoStream{
    				VideoStream: &transcoderpb.VideoStream{
    					CodecSettings: &transcoderpb.VideoStream_H264{
    						H264: &transcoderpb.VideoStream_H264CodecSettings{
    							BitrateBps:   550000,
    							FrameRate:    60,
    							HeightPixels: 360,
    							WidthPixels:  640,
    						},
    					},
    				},
    			},
    		},
    		{
    			Key: "audio_stream0",
    			ElementaryStream: &transcoderpb.ElementaryStream_AudioStream{
    				AudioStream: &transcoderpb.AudioStream{
    					Codec:      "aac",
    					BitrateBps: 64000,
    				},
    			},
    		},
    		{
    			Key: "vtt_stream_en",
    			ElementaryStream: &transcoderpb.ElementaryStream_TextStream{
    				TextStream: &transcoderpb.TextStream{
    					Codec:        "webvtt",
    					LanguageCode: "en-US",
    					DisplayName:  "English",
    					Mapping: []*transcoderpb.TextStream_TextMapping{
    						{
    							AtomKey:  "atom0",
    							InputKey: "subtitle_input_en",
    						},
    					},
    				},
    			},
    		},
    		{
    			Key: "vtt_stream_es",
    			ElementaryStream: &transcoderpb.ElementaryStream_TextStream{
    				TextStream: &transcoderpb.TextStream{
    					Codec:        "webvtt",
    					LanguageCode: "es-ES",
    					DisplayName:  "Spanish",
    					Mapping: []*transcoderpb.TextStream_TextMapping{
    						{
    							AtomKey:  "atom0",
    							InputKey: "subtitle_input_es",
    						},
    					},
    				},
    			},
    		},
    	}
    
    	req := &transcoderpb.CreateJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Job: &transcoderpb.Job{
    			OutputUri: outputURI,
    			JobConfig: &transcoderpb.Job_Config{
    				Config: &transcoderpb.JobConfig{
    					Inputs: []*transcoderpb.Input{
    						{
    							Key: "input0",
    							Uri: inputVideoURI,
    						},
    						{
    							Key: "subtitle_input_en",
    							Uri: inputSubtitles1URI,
    						},
    						{
    							Key: "subtitle_input_es",
    							Uri: inputSubtitles2URI,
    						},
    					},
    					EditList: []*transcoderpb.EditAtom{
    						{
    							Key:    "atom0",
    							Inputs: []string{"input0", "subtitle_input_en", "subtitle_input_es"},
    						},
    					},
    					ElementaryStreams: elementaryStreams,
    					MuxStreams: []*transcoderpb.MuxStream{
    						{
    							Key:               "sd-hls-fmp4",
    							Container:         "fmp4",
    							ElementaryStreams: []string{"video_stream0"},
    						},
    						{
    							Key:               "audio-hls-fmp4",
    							Container:         "fmp4",
    							ElementaryStreams: []string{"audio_stream0"},
    						},
    						{
    							Key:               "text-vtt-en",
    							Container:         "vtt",
    							ElementaryStreams: []string{"vtt_stream_en"},
    							SegmentSettings: &transcoderpb.SegmentSettings{
    								SegmentDuration: &duration.Duration{
    									Seconds: 6,
    								},
    								IndividualSegments: true,
    							},
    						},
    						{
    							Key:               "text-vtt-es",
    							Container:         "vtt",
    							ElementaryStreams: []string{"vtt_stream_es"},
    							SegmentSettings: &transcoderpb.SegmentSettings{
    								SegmentDuration: &duration.Duration{
    									Seconds: 6,
    								},
    								IndividualSegments: true,
    							},
    						},
    					},
    					Manifests: []*transcoderpb.Manifest{
    						{
    							FileName:   "manifest.m3u8",
    							Type:       transcoderpb.[Manifest_HLS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1/transcoderpb.html#cloud_google_com_go_video_transcoder_apiv1_transcoderpb_Manifest_MANIFEST_TYPE_UNSPECIFIED_Manifest_HLS_Manifest_DASH),
    							MuxStreams: []string{"sd-hls-fmp4", "audio-hls-fmp4", "text-vtt-en", "text-vtt-es"},
    						},
    					},
    				},
    			},
    		},
    	}
    	// Creates the job. Jobs take a variable amount of time to run.
    	// You can query for the job state; see getJob() in get_job.go.
    	response, err := client.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateJob: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.AudioStream.html);
    import com.google.cloud.video.transcoder.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[EditAtom](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.EditAtom.html);
    import com.google.cloud.video.transcoder.v1.[ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html);
    import com.google.cloud.video.transcoder.v1.[Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html);
    import com.google.cloud.video.transcoder.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html);
    import com.google.cloud.video.transcoder.v1.[Manifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.html);
    import com.google.cloud.video.transcoder.v1.[Manifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.html).[ManifestType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.ManifestType.html);
    import com.google.cloud.video.transcoder.v1.[MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html);
    import com.google.cloud.video.transcoder.v1.[Output](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Output.html);
    import com.google.cloud.video.transcoder.v1.[SegmentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.SegmentSettings.html);
    import com.google.cloud.video.transcoder.v1.[TextStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.html);
    import com.google.cloud.video.transcoder.v1.[TextStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.html).[TextMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.TextMapping.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import com.google.cloud.video.transcoder.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    
    public class CreateJobWithStandaloneCaptions {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputVideoUri = "gs://my-bucket/my-video-file";
        String inputCaptionsUri = "gs://my-bucket/my-captions-file";
        String outputUri = "gs://my-bucket/my-output-folder/";
    
        createJobWithStandaloneCaptions(
            projectId, location, inputVideoUri, inputCaptionsUri, outputUri);
      }
    
      // Creates a job from an ad-hoc configuration that can use captions from a standalone file.
      public static void createJobWithStandaloneCaptions(
          String projectId,
          String location,
          String inputVideoUri,
          String inputCaptionsUri,
          String outputUri)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html) transcoderServiceClient = [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).create()) {
    
          [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html) videoStream0 =
              [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html).newBuilder()
                  .[setH264](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Builder.html#com_google_cloud_video_transcoder_v1_VideoStream_Builder_setH264_com_google_cloud_video_transcoder_v1_VideoStream_H264CodecSettings_)(
                      [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html).H264CodecSettings.newBuilder()
                          .setBitrateBps(550000)
                          .setFrameRate(60)
                          .setHeightPixels(360)
                          .setWidthPixels(640))
                  .build();
    
          [AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.AudioStream.html) audioStream0 =
              [AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.AudioStream.html).newBuilder().setCodec("aac").setBitrateBps(64000).build();
    
          [TextStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.html) textStream0 =
              [TextStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.html).newBuilder()
                  .setCodec("webvtt")
                  .addMapping(
                      0,
                      [TextMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.TextMapping.html).newBuilder()
                          .setAtomKey("atom0")
                          .setInputKey("caption_input0")
                          .setInputTrack(0)
                          .build())
                  .build();
    
          [JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html) config =
              [JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html).newBuilder()
                  .addInputs([Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html).newBuilder().setKey("input0").setUri(inputVideoUri))
                  .addInputs([Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html).newBuilder().setKey("caption_input0").setUri(inputCaptionsUri))
                  .[addEditList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_addEditList_com_google_cloud_video_transcoder_v1_EditAtom_)(
                      0, // Index in the edit list
                      [EditAtom](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.EditAtom.html).newBuilder()
                          .setKey("atom0")
                          .addInputs("input0")
                          .addInputs("caption_input0")
                          .build())
                  .[setOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_setOutput_com_google_cloud_video_transcoder_v1_Output_)([Output](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Output.html).newBuilder().setUri(outputUri))
                  .addElementaryStreams(
                      [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html).newBuilder()
                          .setKey("video_stream0")
                          .[setVideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setVideoStream_com_google_cloud_video_transcoder_v1_VideoStream_)(videoStream0))
                  .addElementaryStreams(
                      [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html).newBuilder()
                          .setKey("audio_stream0")
                          .[setAudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setAudioStream_com_google_cloud_video_transcoder_v1_AudioStream_)(audioStream0))
                  .addElementaryStreams(
                      [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html).newBuilder().setKey("vtt_stream0").[setTextStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setTextStream_com_google_cloud_video_transcoder_v1_TextStream_)(textStream0))
                  .addMuxStreams(
                      0,
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("sd_hls_fmp4")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("fmp4")
                          .addElementaryStreams("video_stream0")
                          .build())
                  .addMuxStreams(
                      1,
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("audio_hls_fmp4")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("fmp4")
                          .addElementaryStreams("audio_stream0")
                          .build())
                  .addMuxStreams(
                      2,
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("text_vtt")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("vtt")
                          .addElementaryStreams("vtt_stream0")
                          .[setSegmentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setSegmentSettings_com_google_cloud_video_transcoder_v1_SegmentSettings_)(
                              [SegmentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.SegmentSettings.html).newBuilder()
                                  .[setSegmentDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.SegmentSettings.Builder.html#com_google_cloud_video_transcoder_v1_SegmentSettings_Builder_setSegmentDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(6).build())
                                  .[setIndividualSegments](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.SegmentSettings.Builder.html#com_google_cloud_video_transcoder_v1_SegmentSettings_Builder_setIndividualSegments_boolean_)(true)
                                  .build())
                          .build())
                  .[addManifests](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_addManifests_com_google_cloud_video_transcoder_v1_Manifest_)(
                      0,
                      [Manifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.html).newBuilder()
                          .setFileName("manifest.m3u8")
                          .setType([ManifestType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.ManifestType.html).HLS)
                          .addMuxStreams("sd_hls_fmp4")
                          .addMuxStreams("audio_hls_fmp4")
                          .addMuxStreams("text_vtt")
                          .build())
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html).newBuilder()
                  .setJob([Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html).newBuilder().[setOutputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setOutputUri_java_lang_String_)(outputUri).setConfig(config).build())
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html).of(projectId, location).toString())
                  .build();
    
          // Send the job creation request and process the response.
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html) job = transcoderServiceClient.createJob(createJobRequest);
          System.out.println("Job: " + job.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html#com_google_cloud_video_transcoder_v1_Job_getName__)());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // inputVideoUri = 'gs://my-bucket/my-video-file';
    // inputSubtitles1Uri = 'gs://my-bucket/my-captions-file1';
    // inputSubtitles2Uri = 'gs://my-bucket/my-captions-file2';
    // outputUri = 'gs://my-bucket/my-output-folder/';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function createJobWithStandaloneCaptions() {
      // Construct request
      const request = {
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
        job: {
          outputUri: outputUri,
          config: {
            inputs: [
              {
                key: 'input0',
                uri: inputVideoUri,
              },
              {
                key: 'subtitle_input_en',
                uri: inputSubtitles1Uri,
              },
              {
                key: 'subtitle_input_es',
                uri: inputSubtitles2Uri,
              },
            ],
            editList: [
              {
                key: 'atom0',
                inputs: ['input0', 'subtitle_input_en', 'subtitle_input_es'],
              },
            ],
            elementaryStreams: [
              {
                key: 'video-stream0',
                videoStream: {
                  h264: {
                    heightPixels: 360,
                    widthPixels: 640,
                    bitrateBps: 550000,
                    frameRate: 60,
                  },
                },
              },
              {
                key: 'audio-stream0',
                audioStream: {
                  codec: 'aac',
                  bitrateBps: 64000,
                },
              },
              {
                key: 'vtt-stream-en',
                textStream: {
                  codec: 'webvtt',
                  languageCode: 'en-US',
                  displayName: 'English',
                  mapping: [
                    {
                      atomKey: 'atom0',
                      inputKey: 'subtitle_input_en',
                    },
                  ],
                },
              },
              {
                key: 'vtt-stream-es',
                textStream: {
                  codec: 'webvtt',
                  languageCode: 'es-ES',
                  displayName: 'Spanish',
                  mapping: [
                    {
                      atomKey: 'atom0',
                      inputKey: 'subtitle_input_es',
                    },
                  ],
                },
              },
            ],
            muxStreams: [
              {
                key: 'sd-hls-fmp4',
                container: 'fmp4',
                elementaryStreams: ['video-stream0'],
              },
              {
                key: 'audio-hls-fmp4',
                container: 'fmp4',
                elementaryStreams: ['audio-stream0'],
              },
              {
                key: 'text-vtt-en',
                container: 'vtt',
                elementaryStreams: ['vtt-stream-en'],
                segmentSettings: {
                  segmentDuration: {
                    seconds: 6,
                  },
                  individualSegments: true,
                },
              },
              {
                key: 'text-vtt-es',
                container: 'vtt',
                elementaryStreams: ['vtt-stream-es'],
                segmentSettings: {
                  segmentDuration: {
                    seconds: 6,
                  },
                  individualSegments: true,
                },
              },
            ],
            manifests: [
              {
                fileName: 'manifest.m3u8',
                type: '[HLS](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.manifest.manifesttype.html)',
                muxStreams: [
                  'sd-hls-fmp4',
                  'audio-hls-fmp4',
                  'text-vtt-en',
                  'text-vtt-es',
                ],
              },
            ],
          },
        },
      };
    
      // Run request
      const [response] = await transcoderServiceClient.createJob(request);
      console.log(`Job: ${response.name}`);
    }
    
    createJobWithStandaloneCaptions();

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import transcoder_v1
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        TranscoderServiceClient,
    )
    from google.protobuf import duration_pb2 as duration
    
    
    def create_job_with_standalone_captions(
        project_id: str,
        location: str,
        input_video_uri: str,
        input_subtitles1_uri: str,
        input_subtitles2_uri: str,
        output_uri: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job based on an ad-hoc job configuration that can use subtitles from a standalone file.
    
        Args:
            project_id (str): The GCP project ID.
            location (str): The location to start the job in.
            input_video_uri (str): Uri of the input video in the Cloud Storage
              bucket.
            input_subtitles1_uri (str): Uri of an input subtitles file in the Cloud
              Storage bucket.
            input_subtitles2_uri (str): Uri of an input subtitles file in the Cloud
              Storage bucket.
            output_uri (str): Uri of the video output folder in the Cloud Storage
              bucket.
    
        Returns:
            The job resource.
        """
    
        client = TranscoderServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        job = transcoder_v1.types.Job()
        job.output_uri = output_uri
        job.config = transcoder_v1.types.JobConfig(
            inputs=[
                transcoder_v1.types.Input(
                    key="input0",
                    uri=input_video_uri,
                ),
                transcoder_v1.types.Input(
                    key="subtitle-input-en",
                    uri=input_subtitles1_uri,
                ),
                transcoder_v1.types.Input(
                    key="subtitle-input-es",
                    uri=input_subtitles2_uri,
                ),
            ],
            edit_list=[
                transcoder_v1.types.EditAtom(
                    key="atom0",
                    inputs=["input0", "subtitle-input-en", "subtitle-input-es"],
                ),
            ],
            elementary_streams=[
                transcoder_v1.types.ElementaryStream(
                    key="video-stream0",
                    video_stream=transcoder_v1.types.VideoStream(
                        h264=transcoder_v1.types.VideoStream.H264CodecSettings(
                            height_pixels=360,
                            width_pixels=640,
                            bitrate_bps=550000,
                            frame_rate=60,
                        ),
                    ),
                ),
                transcoder_v1.types.ElementaryStream(
                    key="audio-stream0",
                    audio_stream=transcoder_v1.types.AudioStream(
                        codec="aac",
                        bitrate_bps=64000,
                    ),
                ),
                transcoder_v1.types.ElementaryStream(
                    key="vtt-stream-en",
                    text_stream=transcoder_v1.types.TextStream(
                        codec="webvtt",
                        language_code="en-US",
                        display_name="English",
                        mapping_=[
                            transcoder_v1.types.TextStream.TextMapping(
                                atom_key="atom0",
                                input_key="subtitle-input-en",
                            ),
                        ],
                    ),
                ),
                transcoder_v1.types.ElementaryStream(
                    key="vtt-stream-es",
                    text_stream=transcoder_v1.types.TextStream(
                        codec="webvtt",
                        language_code="es-ES",
                        display_name="Spanish",
                        mapping_=[
                            transcoder_v1.types.TextStream.TextMapping(
                                atom_key="atom0",
                                input_key="subtitle-input-es",
                            ),
                        ],
                    ),
                ),
            ],
            mux_streams=[
                transcoder_v1.types.MuxStream(
                    key="sd-hls-fmp4",
                    container="fmp4",
                    elementary_streams=["video-stream0"],
                ),
                transcoder_v1.types.MuxStream(
                    key="audio-hls-fmp4",
                    container="fmp4",
                    elementary_streams=["audio-stream0"],
                ),
                transcoder_v1.types.MuxStream(
                    key="text-vtt-en",
                    container="vtt",
                    elementary_streams=["vtt-stream-en"],
                    segment_settings=transcoder_v1.types.SegmentSettings(
                        segment_duration=duration.Duration(
                            seconds=6,
                        ),
                        individual_segments=True,
                    ),
                ),
                transcoder_v1.types.MuxStream(
                    key="text-vtt-es",
                    container="vtt",
                    elementary_streams=["vtt-stream-es"],
                    segment_settings=transcoder_v1.types.SegmentSettings(
                        segment_duration=duration.Duration(
                            seconds=6,
                        ),
                        individual_segments=True,
                    ),
                ),
            ],
            manifests=[
                transcoder_v1.types.Manifest(
                    file_name="manifest.m3u8",
                    type_="HLS",
                    mux_streams=[
                        "sd-hls-fmp4",
                        "audio-hls-fmp4",
                        "text-vtt-en",
                        "text-vtt-es",
                    ],
                ),
            ],
        )
        response = client.create_job(parent=parent, job=job)
        print(f"Job: {response.name}")
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=transcoderapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
