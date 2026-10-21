---
url: https://docs.cloud.google.com/transcoder/docs/how-to/create-overlays/
title: Creating overlays \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:24.967391+00:00
---

# Creating overlays  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/create-overlays/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Creating overlays Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to insert overlays into transcoded videos. An overlay consists of an image that is inserted on top of the output video, and can optionally be faded in or out over a specified time period. To insert an overlay, use the [`overlays`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#overlay) array in the `JobConfig` template.

See the [list of supported image file formats](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).

## Upload an image to Cloud Storage

To get started, do the following to upload an overlay image to your Cloud Storage bucket:

  1. In the Google Cloud console, go to the Cloud Storage Browser page.  
[Go to the Cloud Storage Browser page](https://console.cloud.google.com/storage/browser)  

  2. Click the name of your bucket to open it.
  3. Click **Upload files**.
  4. Select an image file to upload from your local machine.



## Create an overlay

You can create two types of overlays: static or animated. Both types of overlays use a static image. You can show or hide static overlays. Animated overlays support fade in and fade out animations of the image.

You can insert multiple overlays into a single output video.

### Create a static overlay

In the `image` object, use the [`uri`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#image) field to specify the overlay image in Cloud Storage. In the `resolution` object, set the x and y values from 0 to 1.0. A value of 0 maintains the source image resolution for that dimension; a value of 1.0 will stretch the image to match the dimension of the output video. For example, use the values `x: 1` and `y: 0.5` to stretch the overlay image the full width and half of the height of the output video.

In the `animations` array, create an `animationStatic` object with x and y coordinates from 0 to 1.0. These coordinates are based on the output video resolution. Use the values `x: 0` and `y: 0` to position the top-left corner of the overlay in the top-left corner of the output video. Specify when the overlay should appear in the output video timeline using the `startTimeOffset` field.

To remove the static animation, create an `animationEnd` object. Specify when the animation should end (that is, the overlay should disappear) in the output video timeline using the `startTimeOffset` field.

You can add this configuration to a [job template](https://docs.cloud.google.com/transcoder/docs/how-to/job-templates) or include it in an [ad-hoc job configuration](https://docs.cloud.google.com/transcoder/docs/how-to/jobs#create_jobs_ad_hoc):

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project).
  * `LOCATION`: The location where your job will run. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

Show locations

    * `us-central1`
    * `us-west1`
    * `us-west2`
    * `us-east1`
    * `us-east4`
    * `southamerica-east1`
    * `northamerica-northeast1`
    * `asia-east1`
    * `asia-northeast1`
    * `asia-northeast3`
    * `asia-south1`
    * `asia-southeast1`
    * `australia-southeast1`
    * `europe-west1`
    * `europe-west2`
    * `europe-west4`
    * `me-west1`
    * `me-central1`
    * `me-central2`
  * `STORAGE_BUCKET_NAME`: The name of the Cloud Storage bucket you created.
  * `STORAGE_INPUT_VIDEO`: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
  * `STORAGE_INPUT_OVERLAY`: The name of the image in your Cloud Storage bucket that you are using for the overlay, such as `my-overlay.png`. This field should take into account any folders that you created in the bucket (for example, `input/my-overlay.png`). 
  * `STORAGE_OUTPUT_FOLDER`: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "config": {
        "inputs": [
              {
                "key": "input0",
                "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
              }
        ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "heightPixels": 360,
                "widthPixels": 640,
                "bitrateBps": 550000,
                "frameRate": 60
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        },
        "overlays": [
          {
            "image": {
              "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_OVERLAY",
              "resolution": {
                "x": 1,
                "y": 0.5
              },
              "alpha": 1
            },
            "animations": [
              {
                "animationStatic": {
                  "xy": {
                    "x": 0,
                    "y": 0
                  },
                  "startTimeOffset": "0s"
                }
              },
              {
                "animationEnd": {
                  "startTimeOffset": "10s"
                }
              }
            ]
          }
        ]
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "config": {
        "inputs": [
              {
                "key": "input0",
                "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
              }
        ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "heightPixels": 360,
                "widthPixels": 640,
                "bitrateBps": 550000,
                "frameRate": 60
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        },
        "overlays": [
          {
            "image": {
              "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_OVERLAY",
              "resolution": {
                "x": 1,
                "y": 0.5
              },
              "alpha": 1
            },
            "animations": [
              {
                "animationStatic": {
                  "xy": {
                    "x": 0,
                    "y": 0
                  },
                  "startTimeOffset": "0s"
                }
              },
              {
                "animationEnd": {
                  "startTimeOffset": "10s"
                }
              }
            ]
          }
        ]
      }
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
        -Uri "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID",
      "config": {
       ...
      },
      "state": "PENDING",
      "createTime": CREATE_TIME,
      "ttlAfterCompletionDays": 30
    }
    

### gcloud

  1. Create a `request.json` file that defines the job fields. Make the following replacements for the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create) command: 
     * STORAGE_BUCKET_NAME: The name of the Cloud Storage bucket you created. 
     * STORAGE_INPUT_VIDEO: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
     * STORAGE_INPUT_OVERLAY: The name of the image file in your Cloud Storage bucket that you are using for the overlay, such as `my-overlay.png`. This field should take into account any folders that you created in the bucket (for example, `input/my-overlay.png`). 
     * LOCATION: The location where your job will run. Use a location from the following list. 

Show locations

       * `us-central1`
       * `us-west1`
       * `us-west2`
       * `us-east1`
       * `us-east4`
       * `southamerica-east1`
       * `northamerica-northeast1`
       * `asia-east1`
       * `asia-northeast1`
       * `asia-northeast3`
       * `asia-south1`
       * `asia-southeast1`
       * `australia-southeast1`
       * `europe-west1`
       * `europe-west2`
       * `europe-west4`
       * `me-west1`
       * `me-central1`
       * `me-central2`
     * STORAGE_OUTPUT_FOLDER: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.
    
    {
      "config": {
        "inputs": [
              {
                "key": "input0",
                "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
              }
        ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "heightPixels": 360,
                "widthPixels": 640,
                "bitrateBps": 550000,
                "frameRate": 60
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        },
        "overlays": [
          {
            "image": {
              "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_OVERLAY",
              "resolution": {
                "x": 1,
                "y": 0.5
              },
              "alpha": 1
            },
            "animations": [
              {
                "animationStatic": {
                  "xy": {
                    "x": 0,
                    "y": 0
                  },
                  "startTimeOffset": "0s"
                }
              },
              {
                "animationEnd": {
                  "startTimeOffset": "10s"
                }
              }
            ]
          }
        ]
      }
    }

  2. Run the following command: 
         
         gcloud transcoder jobs create --location=LOCATION --file="request.json"

You should see a response similar to the following: 
         
         {
           "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID",
           "config": {
            ...
           },
           "state": "PENDING",
           "createTime": CREATE_TIME,
           "ttlAfterCompletionDays": 30
         }
         




### C#

Before trying this sample, follow the C# setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Transcoder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CreateJobWithStaticOverlaySample
    {
        public Job CreateJobWithStaticOverlay(
            string projectId, string location, string inputUri, string overlayImageUri, string outputUri)
        {
            // Create the client.
            [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html) client = [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_Create)();
    
            // Build the parent location name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, location);
    
            // Build the job config.
            [VideoStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.VideoStream.html) videoStream0 = new [VideoStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.VideoStream.html)
            {
                H264 = new VideoStream.Types.H264CodecSettings
                {
                    BitrateBps = 550000,
                    FrameRate = 60,
                    HeightPixels = 360,
                    WidthPixels = 640
                }
            };
    
            [AudioStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.AudioStream.html) audioStream0 = new [AudioStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.AudioStream.html)
            {
                Codec = "aac",
                BitrateBps = 64000
            };
    
            // Create the overlay image. Image resolution is based on output video
            // resolution. To respect the original image aspect ratio, set either x
            // or y to 0.0. This example stretches the overlay image the full width
            // and half of the height of the output video.
            Overlay.Types.Image overlayImage = new Overlay.Types.Image
            {
                Uri = overlayImageUri,
                Alpha = 1,
                Resolution = new Overlay.Types.NormalizedCoordinate
                {
                    X = 1,
                    Y = 0.5
                }
            };
    
            // Create the starting animation (when the overlay appears). Use the values x: 0 and y: 0 to
            // position the top-left corner of the overlay in the top-left corner of the output video.
            Overlay.Types.Animation animationStart = new Overlay.Types.Animation
            {
                AnimationStatic = new Overlay.Types.AnimationStatic
                {
                    Xy = new Overlay.Types.NormalizedCoordinate
                    {
                        X = 0,
                        Y = 0
                    },
                    StartTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(TimeSpan.FromSeconds(0))
                }
            };
    
    
            // Create the ending animation (when the overlay disappears). In this example, the overlay
            // disappears at the 10-second mark in the output video.
            Overlay.Types.Animation animationEnd = new Overlay.Types.Animation
            {
                AnimationEnd = new Overlay.Types.AnimationEnd
                {
                    StartTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(TimeSpan.FromSeconds(10))
                }
            };
    
            // Create the overlay and add the image and animations to it.
            [Overlay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.html) overlay = new [Overlay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.html)
            {
                Image = overlayImage,
                Animations = { animationStart, animationEnd }
            };
    
            [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html) elementaryStream0 = new [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html)
            {
                Key = "video_stream0",
                VideoStream = videoStream0
            };
    
            [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html) elementaryStream1 = new [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html)
            {
                Key = "audio_stream0",
                AudioStream = audioStream0
            };
    
            [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.MuxStream.html) muxStream0 = new [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.MuxStream.html)
            {
                Key = "sd",
                Container = "mp4",
                ElementaryStreams = { "video_stream0", "audio_stream0" }
            };
    
            [Input](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html) input = new [Input](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html)
            {
                Key = "input0",
                Uri = inputUri
            };
    
            [Output](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Output.html) output = new [Output](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Output.html)
            {
                Uri = outputUri
            };
    
            [JobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobConfig.html) jobConfig = new [JobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobConfig.html)
            {
                Inputs = { input },
                Output = output,
                ElementaryStreams = { elementaryStream0, elementaryStream1 },
                MuxStreams = { muxStream0 },
                Overlays = { overlay }
            };
    
            // Build the job.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) newJob = new [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html)
            {
                InputUri = inputUri,
                OutputUri = outputUri,
                Config = jobConfig
            };
    
            // Call the API.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) job = client.[CreateJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_CreateJob_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Transcoder_V1_Job_Google_Api_Gax_Grpc_CallSettings_)(parent, newJob);
    
            // Return the result.
            return job;
        }
    }

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
    
    // createJobWithStaticOverlay creates a job based on a given configuration that
    // includes a static overlay. See
    // https://cloud.google.com/transcoder/docs/how-to/create-overlays#create-static-overlay
    // for more information.
    func createJobWithStaticOverlay(w io.Writer, projectID string, location string, inputURI string, overlayImageURI string, outputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://my-bucket/my-video-file"
    	// overlayImageURI := "gs://my-bucket/my-overlay-image-file"
    	// outputURI := "gs://my-bucket/my-output-folder/"
    	ctx := context.Background()
    	client, err := transcoder.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_Close)()
    
    	req := &transcoderpb.CreateJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Job: &transcoderpb.Job{
    			InputUri:  inputURI,
    			OutputUri: outputURI,
    			JobConfig: &transcoderpb.Job_Config{
    				Config: &transcoderpb.JobConfig{
    					ElementaryStreams: []*transcoderpb.ElementaryStream{
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
    					},
    					MuxStreams: []*transcoderpb.MuxStream{
    						{
    							Key:               "sd",
    							Container:         "mp4",
    							ElementaryStreams: []string{"video_stream0", "audio_stream0"},
    						},
    					},
    					Overlays: []*transcoderpb.Overlay{
    						{
    							Image: &transcoderpb.Overlay_Image{
    								Uri: overlayImageURI,
    								Resolution: &transcoderpb.Overlay_NormalizedCoordinate{
    									X: 1,
    									Y: 0.5,
    								},
    								Alpha: 1,
    							},
    							Animations: []*transcoderpb.Overlay_Animation{
    								{
    									AnimationType: &transcoderpb.Overlay_Animation_AnimationStatic{
    										AnimationStatic: &transcoderpb.Overlay_AnimationStatic{
    											Xy: &transcoderpb.Overlay_NormalizedCoordinate{
    												X: 0,
    												Y: 0,
    											},
    											StartTimeOffset: &duration.Duration{
    												Seconds: 0,
    											},
    										},
    									},
    								},
    
    								{
    									AnimationType: &transcoderpb.Overlay_Animation_AnimationEnd{
    										AnimationEnd: &transcoderpb.Overlay_AnimationEnd{
    											StartTimeOffset: &duration.Duration{
    												Seconds: 10,
    											},
    										},
    									},
    								},
    							},
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
    		return fmt.Errorf("createJobWithStaticOverlay: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.AudioStream.html);
    import com.google.cloud.video.transcoder.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html);
    import com.google.cloud.video.transcoder.v1.[Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html);
    import com.google.cloud.video.transcoder.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html);
    import com.google.cloud.video.transcoder.v1.[MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html);
    import com.google.cloud.video.transcoder.v1.[Output](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Output.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[AnimationEnd](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationEnd.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[AnimationStatic](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationStatic.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[NormalizedCoordinate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import com.google.cloud.video.transcoder.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    
    public class CreateJobWithStaticOverlay {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputUri = "gs://my-bucket/my-video-file";
        String overlayImageUri = "gs://my-bucket/my-overlay-image.jpg";
        String outputUri = "gs://my-bucket/my-output-folder/";
    
        createJobWithStaticOverlay(projectId, location, inputUri, overlayImageUri, outputUri);
      }
    
      // Creates a job from an ad-hoc configuration and adds a static overlay to it.
      public static void createJobWithStaticOverlay(
          String projectId, String location, String inputUri, String overlayImageUri, String outputUri)
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
    
          // Create the overlay image. Image resolution is based on output video resolution.
          // To respect the original image aspect ratio, set either x or y to 0.0. This example
          // stretches the overlay image the full width and half of the height of the
          // output video.
          [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Image.html) overlayImage =
              [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).Image.newBuilder()
                  .setUri(overlayImageUri)
                  .[setResolution](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Image.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Image_Builder_setResolution_com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_)([NormalizedCoordinate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.html).newBuilder().[setX](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setX_double_)(1).[setY](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setY_double_)(0.5).build())
                  .[setAlpha](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Image.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Image_Builder_setAlpha_double_)(1)
                  .build();
    
          // Create the starting animation (when the overlay appears). Use the values x: 0 and y: 0 to
          // position the top-left corner of the overlay in the top-left corner of the output video.
          [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[Animation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.html) animationStart =
              [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).Animation.newBuilder()
                  .[setAnimationStatic](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Animation_Builder_setAnimationStatic_com_google_cloud_video_transcoder_v1_Overlay_AnimationStatic_)(
                      [AnimationStatic](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationStatic.html).newBuilder()
                          .setXy([NormalizedCoordinate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.html).newBuilder().[setX](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setX_double_)(0).[setY](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setY_double_)(0).build())
                          .setStartTimeOffset([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(0).build())
                          .build())
                  .build();
    
          // Create the ending animation (when the overlay disappears). In this example, the overlay
          // disappears at the 10-second mark in the output video.
          [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[Animation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.html) animationEnd =
              [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).Animation.newBuilder()
                  .[setAnimationEnd](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Animation_Builder_setAnimationEnd_com_google_cloud_video_transcoder_v1_Overlay_AnimationEnd_)(
                      [AnimationEnd](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationEnd.html).newBuilder()
                          .setStartTimeOffset([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(10).build())
                          .build())
                  .build();
    
          // Create the overlay and add the image and animations to it.
          [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html) overlay =
              [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).newBuilder()
                  .[setImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Builder_setImage_com_google_cloud_video_transcoder_v1_Overlay_Image_)(overlayImage)
                  .[addAnimations](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Builder_addAnimations_com_google_cloud_video_transcoder_v1_Overlay_Animation_)(animationStart)
                  .[addAnimations](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Builder_addAnimations_com_google_cloud_video_transcoder_v1_Overlay_Animation_)(animationEnd)
                  .build();
    
          [JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html) config =
              [JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html).newBuilder()
                  .addInputs([Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html).newBuilder().setKey("input0").setUri(inputUri))
                  .[setOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_setOutput_com_google_cloud_video_transcoder_v1_Output_)([Output](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Output.html).newBuilder().setUri(outputUri))
                  .addElementaryStreams(
                      [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html).newBuilder()
                          .setKey("video_stream0")
                          .[setVideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setVideoStream_com_google_cloud_video_transcoder_v1_VideoStream_)(videoStream0))
                  .addElementaryStreams(
                      [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html).newBuilder()
                          .setKey("audio_stream0")
                          .[setAudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setAudioStream_com_google_cloud_video_transcoder_v1_AudioStream_)(audioStream0))
                  .addMuxStreams(
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("sd")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("mp4")
                          .addElementaryStreams("video_stream0")
                          .addElementaryStreams("audio_stream0")
                          .build())
                  .[addOverlays](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_addOverlays_com_google_cloud_video_transcoder_v1_Overlay_)(overlay) // Add the overlay to the job config
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html).newBuilder()
                  .setJob(
                      [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html).newBuilder()
                          .[setInputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setInputUri_java_lang_String_)(inputUri)
                          .[setOutputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setOutputUri_java_lang_String_)(outputUri)
                          .setConfig(config)
                          .build())
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
    // inputUri = 'gs://my-bucket/my-video-file';
    // overlayImageUri = 'gs://my-bucket/my-overlay-image-file';
    // outputUri = 'gs://my-bucket/my-output-folder/';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function createJobFromStaticOverlay() {
      // Construct request
      const request = {
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
        job: {
          inputUri: inputUri,
          outputUri: outputUri,
          config: {
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
            ],
            muxStreams: [
              {
                key: 'sd',
                container: 'mp4',
                elementaryStreams: ['video-stream0', 'audio-stream0'],
              },
            ],
            overlays: [
              {
                image: {
                  uri: overlayImageUri,
                  resolution: {
                    x: 1,
                    y: 0.5,
                  },
                  alpha: 1.0,
                },
                animations: [
                  {
                    animationStatic: {
                      xy: {
                        x: 0,
                        y: 0,
                      },
                      startTimeOffset: {
                        seconds: 0,
                      },
                    },
                  },
                  {
                    animationEnd: {
                      startTimeOffset: {
                        seconds: 10,
                      },
                    },
                  },
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
    
    createJobFromStaticOverlay();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\AudioStream;
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\CreateJobRequest;
    use Google\Cloud\Video\Transcoder\V1\ElementaryStream;
    use Google\Cloud\Video\Transcoder\V1\Job;
    use Google\Cloud\Video\Transcoder\V1\JobConfig;
    use Google\Cloud\Video\Transcoder\V1\MuxStream;
    use Google\Cloud\Video\Transcoder\V1\Overlay;
    use Google\Cloud\Video\Transcoder\V1\VideoStream;
    use Google\Protobuf\Duration;
    
    /**
     * Creates a job based on a supplied job config that includes a static image overlay.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $inputUri Uri of the video in the Cloud Storage bucket.
     * @param string $overlayImageUri Uri of the image for the overlay in the Cloud Storage bucket.
     * @param string $outputUri Uri of the video output folder in the Cloud Storage bucket.
     */
    function create_job_with_static_overlay($projectId, $location, $inputUri, $overlayImageUri, $outputUri)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedParent = $transcoderServiceClient->locationName($projectId, $location);
        $jobConfig =
            (new JobConfig())->setElementaryStreams([
                (new ElementaryStream())
                    ->setKey('video-stream0')
                    ->setVideoStream(
                        (new VideoStream())
                            ->setH264(
                                (new VideoStream\H264CodecSettings())
                                    ->setBitrateBps(550000)
                                    ->setFrameRate(60)
                                    ->setHeightPixels(360)
                                    ->setWidthPixels(640)
                            )
                    ),
                (new ElementaryStream())
                    ->setKey('audio-stream0')
                    ->setAudioStream(
                        (new AudioStream())
                            ->setCodec('aac')
                            ->setBitrateBps(64000)
                    )
            ])->setMuxStreams([
                (new MuxStream())
                    ->setKey('sd')
                    ->setContainer('mp4')
                    ->setElementaryStreams(['video-stream0', 'audio-stream0'])
            ])->setOverlays([
                (new Overlay())
                    ->setImage(
                        (new Overlay\Image())
                            ->setUri($overlayImageUri)
                            ->setResolution(
                                (new Overlay\NormalizedCoordinate())
                                    ->setX(1)
                                    ->setY(0.5)
                            )
                            ->setAlpha(1)
                    )
                    ->setAnimations([
                        (new Overlay\Animation())
                            ->setAnimationStatic(
                                (new Overlay\AnimationStatic())
                                    ->setXy(
                                        (new Overlay\NormalizedCoordinate())
                                            ->setY(0)
                                            ->setX(0)
                                    )
                                    ->setStartTimeOffset(
                                        (new Duration())
                                            ->setSeconds(0)
                                    )
                            ),
                        (new Overlay\Animation())
                            ->setAnimationEnd(
                                (new Overlay\AnimationEnd())
                                    ->setStartTimeOffset(
                                        (new Duration())
                                            ->setSeconds(10)
                                    )
                            )
                    ])
            ]);
    
        $job = (new Job())
            ->setInputUri($inputUri)
            ->setOutputUri($outputUri)
            ->setConfig($jobConfig);
        $request = (new CreateJobRequest())
            ->setParent($formattedParent)
            ->setJob($job);
    
        $response = $transcoderServiceClient->createJob($request);
    
        // Print job name.
        printf('Job: %s' . PHP_EOL, $response->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import transcoder_v1
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        TranscoderServiceClient,
    )
    from google.protobuf import duration_pb2 as duration
    
    
    def create_job_with_static_overlay(
        project_id: str,
        location: str,
        input_uri: str,
        overlay_image_uri: str,
        output_uri: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job based on an ad-hoc job configuration that includes a static image overlay.
    
        Args:
            project_id: The GCP project ID.
            location: The location to start the job in.
            input_uri: Uri of the video in the Cloud Storage bucket.
            overlay_image_uri: Uri of the image for the overlay in the Cloud Storage bucket.
            output_uri: Uri of the video output folder in the Cloud Storage bucket.
    
        Returns:
            The job resource.
        """
    
        client = TranscoderServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        job = transcoder_v1.types.Job()
        job.input_uri = input_uri
        job.output_uri = output_uri
        job.config = transcoder_v1.types.JobConfig(
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
                        codec="aac", bitrate_bps=64000
                    ),
                ),
            ],
            mux_streams=[
                transcoder_v1.types.MuxStream(
                    key="sd",
                    container="mp4",
                    elementary_streams=["video-stream0", "audio-stream0"],
                ),
            ],
            overlays=[
                transcoder_v1.types.Overlay(
                    image=transcoder_v1.types.Overlay.Image(
                        uri=overlay_image_uri,
                        resolution=transcoder_v1.types.Overlay.NormalizedCoordinate(
                            x=1,
                            y=0.5,
                        ),
                        alpha=1,
                    ),
                    animations=[
                        transcoder_v1.types.Overlay.Animation(
                            animation_static=transcoder_v1.types.Overlay.AnimationStatic(
                                xy=transcoder_v1.types.Overlay.NormalizedCoordinate(
                                    x=0,
                                    y=0,
                                ),
                                start_time_offset=duration.Duration(
                                    seconds=0,
                                ),
                            ),
                        ),
                        transcoder_v1.types.Overlay.Animation(
                            animation_end=transcoder_v1.types.Overlay.AnimationEnd(
                                start_time_offset=duration.Duration(
                                    seconds=10,
                                ),
                            ),
                        ),
                    ],
                ),
            ],
        )
        response = client.create_job(parent=parent, job=job)
        print(f"Job: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location    = "YOUR-JOB-LOCATION"  # (e.g. "us-central1")
    # input_uri   = "YOUR-GCS-INPUT-VIDEO"  # (e.g. "gs://my-bucket/my-video-file")
    # overlay_image_uri   = "YOUR-GCS-OVERLAY-IMAGE"  # (e.g. "gs://my-bucket/overlay.jpg")
    # output_uri  = "YOUR-GCS-OUTPUT-FOLDER/"  # (e.g. "gs://my-bucket/my-output-folder/")
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the parent.
    parent = client.location_path project: project_id, location: location
    
    # Build the job config.
    new_job = {
      input_uri: input_uri,
      output_uri: output_uri,
      config: {
        elementary_streams: [
          {
            key: "video-stream0",
            video_stream: {
              h264: {
                height_pixels: 360,
                width_pixels: 640,
                bitrate_bps: 550_000,
                frame_rate: 60
              }
            }
          },
          {
            key: "audio-stream0",
            audio_stream: {
              codec: "aac",
              bitrate_bps: 64_000
            }
          }
        ],
        mux_streams: [
          {
            key: "sd",
            container: "mp4",
            elementary_streams: [
              "video-stream0",
              "audio-stream0"
            ]
          }
        ],
        overlays: [
          {
            image: {
              uri: overlay_image_uri,
              resolution: {
                x: 1,
                y: 0.5
              },
              alpha: 1
            },
            animations: [
              {
                animation_static: {
                  xy: {
                    x: 0,
                    y: 0
                  },
                  start_time_offset: {
                    seconds: 0
                  }
                }
              },
              {
                animation_end: {
                  start_time_offset: {
                    seconds: 10
                  }
                }
              }
            ]
          }
        ]
      }
    }
    
    job = client.create_job parent: parent, job: new_job
    
    # Print the job name.
    puts "Job: #{job.name}"

In the output video, the static overlay has the following characteristics:

  * It appears at the beginning of the timeline and is visible for 10 seconds.
  * It stretches the full width and half of the height of the output video.
  * It is positioned in the top-left corner of the output video.



See the [sample output video](https://docs.cloud.google.com/static/transcoder/images/static-overlay-sample.mp4) for this configuration. This video uses a [sample overlay image](https://docs.cloud.google.com/static/transcoder/images/overlay.png).

### Create an animated overlay

In the `image` object, use the [`uri`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#image) field to specify the overlay image in Cloud Storage. In the `resolution` object, set the x and y values from 0 to 1.0. A value of 0 maintains the source image resolution for that dimension; a value of 1.0 will stretch the image to match the dimension of the output video. For example, use the values `x: 0` and `y: 0` to maintain the original resolution of the overlay image.

In the `animations` array, create an `animationFade` object with a `fadeType` of `FADE_IN`. Set the x and y coordinates from 0 to 1.0. These coordinates are based on the output video resolution. Use the values `x: 0.5` and `y: 0.5` to position the top-left corner of the overlay in the center of the output video. Specify when the overlay should start to appear in the output video timeline using the `startTimeOffset` field. The overlay should be fully visible by the time set in the `endTimeOffset` field.

To fade out the overlay, create another `animationFade` object. This time, set the `fadeType` to `FADE_OUT`. Input the position coordinates and start and end times as before.

You can add this configuration to a [job template](https://docs.cloud.google.com/transcoder/docs/how-to/job-templates) or include it in an [ad-hoc job configuration](https://docs.cloud.google.com/transcoder/docs/how-to/jobs#create_jobs_ad_hoc):

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project).
  * `LOCATION`: The location where your job will run. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

Show locations

    * `us-central1`
    * `us-west1`
    * `us-west2`
    * `us-east1`
    * `us-east4`
    * `southamerica-east1`
    * `northamerica-northeast1`
    * `asia-east1`
    * `asia-northeast1`
    * `asia-northeast3`
    * `asia-south1`
    * `asia-southeast1`
    * `australia-southeast1`
    * `europe-west1`
    * `europe-west2`
    * `europe-west4`
    * `me-west1`
    * `me-central1`
    * `me-central2`
  * `STORAGE_BUCKET_NAME`: The name of the Cloud Storage bucket you created.
  * `STORAGE_INPUT_VIDEO`: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
  * `STORAGE_INPUT_OVERLAY`: The name of the image in your Cloud Storage bucket that you are using for the overlay, such as `my-overlay.png`. This field should take into account any folders that you created in the bucket (for example, `input/my-overlay.png`). 
  * `STORAGE_OUTPUT_FOLDER`: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "config": {
        "inputs": [
              {
                "key": "input0",
                "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
              }
        ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "heightPixels": 360,
                "widthPixels": 640,
                "bitrateBps": 550000,
                "frameRate": 60
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        },
        "overlays": [
          {
            "image": {
              "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_OVERLAY",
              "resolution": {
                "x": 0,
                "y": 0
              },
              "alpha": 1
            },
            "animations": [
              {
                "animationFade": {
                  "fadeType": "FADE_IN",
                  "xy": {
                    "x": 0.5,
                    "y": 0.5
                  },
                  "startTimeOffset": "5s",
                  "endTimeOffset": "10s"
                }
              },
              {
                "animationFade": {
                  "fadeType": "FADE_OUT",
                  "xy": {
                    "x": 0.5,
                    "y": 0.5
                  },
                  "startTimeOffset": "12s",
                  "endTimeOffset": "15s"
                }
              }
            ]
          }
        ]
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "config": {
        "inputs": [
              {
                "key": "input0",
                "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
              }
        ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "heightPixels": 360,
                "widthPixels": 640,
                "bitrateBps": 550000,
                "frameRate": 60
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        },
        "overlays": [
          {
            "image": {
              "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_OVERLAY",
              "resolution": {
                "x": 0,
                "y": 0
              },
              "alpha": 1
            },
            "animations": [
              {
                "animationFade": {
                  "fadeType": "FADE_IN",
                  "xy": {
                    "x": 0.5,
                    "y": 0.5
                  },
                  "startTimeOffset": "5s",
                  "endTimeOffset": "10s"
                }
              },
              {
                "animationFade": {
                  "fadeType": "FADE_OUT",
                  "xy": {
                    "x": 0.5,
                    "y": 0.5
                  },
                  "startTimeOffset": "12s",
                  "endTimeOffset": "15s"
                }
              }
            ]
          }
        ]
      }
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
        -Uri "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID",
      "config": {
       ...
      },
      "state": "PENDING",
      "createTime": CREATE_TIME,
      "ttlAfterCompletionDays": 30
    }
    

### gcloud

  1. Create a `request.json` file that defines the job fields. Make the following replacements for the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create) command: 
     * STORAGE_BUCKET_NAME: The name of the Cloud Storage bucket you created. 
     * STORAGE_INPUT_VIDEO: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
     * STORAGE_INPUT_OVERLAY: The name of the image file in your Cloud Storage bucket that you are using for the overlay, such as `my-overlay.png`. This field should take into account any folders that you created in the bucket (for example, `input/my-overlay.png`). 
     * LOCATION: The location where your job will run. Use a location from the following list. 

Show locations

       * `us-central1`
       * `us-west1`
       * `us-west2`
       * `us-east1`
       * `us-east4`
       * `southamerica-east1`
       * `northamerica-northeast1`
       * `asia-east1`
       * `asia-northeast1`
       * `asia-northeast3`
       * `asia-south1`
       * `asia-southeast1`
       * `australia-southeast1`
       * `europe-west1`
       * `europe-west2`
       * `europe-west4`
       * `me-west1`
       * `me-central1`
       * `me-central2`
     * STORAGE_OUTPUT_FOLDER: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.
    
    {
      "config": {
        "inputs": [
              {
                "key": "input0",
                "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
              }
        ],
        "elementaryStreams": [
          {
            "key": "video-stream0",
            "videoStream": {
              "h264": {
                "heightPixels": 360,
                "widthPixels": 640,
                "bitrateBps": 550000,
                "frameRate": 60
              }
            }
          },
          {
            "key": "audio-stream0",
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        },
        "overlays": [
          {
            "image": {
              "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_OVERLAY",
              "resolution": {
                "x": 0,
                "y": 0
              },
              "alpha": 1
            },
            "animations": [
              {
                "animationFade": {
                  "fadeType": "FADE_IN",
                  "xy": {
                    "x": 0.5,
                    "y": 0.5
                  },
                  "startTimeOffset": "5s",
                  "endTimeOffset": "10s"
                }
              },
              {
                "animationFade": {
                  "fadeType": "FADE_OUT",
                  "xy": {
                    "x": 0.5,
                    "y": 0.5
                  },
                  "startTimeOffset": "12s",
                  "endTimeOffset": "15s"
                }
              }
            ]
          }
        ]
      }
    }

  2. Run the following command: 
         
         gcloud transcoder jobs create --location=LOCATION --file="request.json"

You should see a response similar to the following: 
         
         {
           "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID",
           "config": {
            ...
           },
           "state": "PENDING",
           "createTime": CREATE_TIME,
           "ttlAfterCompletionDays": 30
         }
         




### C#

Before trying this sample, follow the C# setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Transcoder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CreateJobWithAnimatedOverlaySample
    {
        public Job CreateJobWithAnimatedOverlay(
            string projectId, string location, string inputUri, string overlayImageUri, string outputUri)
        {
            // Create the client.
            [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html) client = [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_Create)();
    
            // Build the parent location name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, location);
    
            // Build the job config.
            [VideoStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.VideoStream.html) videoStream0 = new [VideoStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.VideoStream.html)
            {
                H264 = new VideoStream.Types.H264CodecSettings
                {
                    BitrateBps = 550000,
                    FrameRate = 60,
                    HeightPixels = 360,
                    WidthPixels = 640
                }
            };
    
            [AudioStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.AudioStream.html) audioStream0 = new [AudioStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.AudioStream.html)
            {
                Codec = "aac",
                BitrateBps = 64000
            };
    
            // Create the overlay image. Image resolution is based on output video resolution.
            // This example uses the values x: 0 and y: 0 to maintain the original resolution
            // of the overlay image.
            Overlay.Types.Image overlayImage = new Overlay.Types.Image
            {
                Uri = overlayImageUri,
                Alpha = 1,
                Resolution = new Overlay.Types.NormalizedCoordinate
                {
                    X = 0,
                    Y = 0
                }
            };
    
            // Create the starting animation (when the overlay starts to fade in). Use the values x: 0.5
            // and y: 0.5 to position the top-left corner of the overlay in the center of the output
            // video.
            Overlay.Types.Animation animationFadeIn = new Overlay.Types.Animation
            {
                AnimationFade = new Overlay.Types.AnimationFade
                {
                    FadeType = [Overlay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.Types.html).[FadeType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.Types.FadeType.html).[FadeIn](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.Types.FadeType.html#Google_Cloud_Video_Transcoder_V1_Overlay_Types_FadeType_FadeIn),
                    Xy = new Overlay.Types.NormalizedCoordinate
                    {
                        X = 0.5,
                        Y = 0.5
                    },
                    StartTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(TimeSpan.FromSeconds(5)),
                    EndTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(TimeSpan.FromSeconds(10))
                }
            };
    
            // Create the ending animation (when the overlay starts to fade out). The overlay will start
            // to fade out at the 12-second mark in the output video.
            Overlay.Types.Animation animationFadeOut = new Overlay.Types.Animation
            {
                AnimationFade = new Overlay.Types.AnimationFade
                {
                    FadeType = [Overlay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.Types.html).[FadeType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.Types.FadeType.html).[FadeOut](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.Types.FadeType.html#Google_Cloud_Video_Transcoder_V1_Overlay_Types_FadeType_FadeOut),
                    Xy = new Overlay.Types.NormalizedCoordinate
                    {
                        X = 0.5,
                        Y = 0.5
                    },
                    StartTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(TimeSpan.FromSeconds(12)),
                    EndTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(TimeSpan.FromSeconds(15))
                }
            };
    
            // Create the overlay and add the image and animations to it.
            [Overlay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.html) overlay = new [Overlay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Overlay.html)
            {
                Image = overlayImage,
                Animations = { animationFadeIn, animationFadeOut }
            };
    
            [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html) elementaryStream0 = new [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html)
            {
                Key = "video_stream0",
                VideoStream = videoStream0
            };
    
            [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html) elementaryStream1 = new [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html)
            {
                Key = "audio_stream0",
                AudioStream = audioStream0
            };
    
            [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.MuxStream.html) muxStream0 = new [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.MuxStream.html)
            {
                Key = "sd",
                Container = "mp4",
                ElementaryStreams = { "video_stream0", "audio_stream0" }
            };
    
            [Input](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html) input = new [Input](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html)
            {
                Key = "input0",
                Uri = inputUri
            };
    
            [Output](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Output.html) output = new [Output](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Output.html)
            {
                Uri = outputUri
            };
    
            [JobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobConfig.html) jobConfig = new [JobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobConfig.html)
            {
                Inputs = { input },
                Output = output,
                ElementaryStreams = { elementaryStream0, elementaryStream1 },
                MuxStreams = { muxStream0 },
                Overlays = { overlay }
            };
    
            // Build the job.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) newJob = new [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html)
            {
                InputUri = inputUri,
                OutputUri = outputUri,
                Config = jobConfig
            };
    
            // Call the API.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) job = client.[CreateJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_CreateJob_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Transcoder_V1_Job_Google_Api_Gax_Grpc_CallSettings_)(parent, newJob);
    
            // Return the result.
            return job;
        }
    }

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
    
    // createJobWithAnimatedOverlay creates a job based on a given configuration that
    // includes an animated overlay. See
    // https://cloud.google.com/transcoder/docs/how-to/create-overlays#create-animated-overlay
    // for more information.
    func createJobWithAnimatedOverlay(w io.Writer, projectID string, location string, inputURI string, overlayImageURI string, outputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://my-bucket/my-video-file"
    	// overlayImageURI := "gs://my-bucket/my-overlay-image-file"
    	// outputURI := "gs://my-bucket/my-output-folder/"
    	ctx := context.Background()
    	client, err := transcoder.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_Close)()
    
    	req := &transcoderpb.CreateJobRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Job: &transcoderpb.Job{
    			InputUri:  inputURI,
    			OutputUri: outputURI,
    			JobConfig: &transcoderpb.Job_Config{
    				Config: &transcoderpb.JobConfig{
    					ElementaryStreams: []*transcoderpb.ElementaryStream{
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
    					},
    					MuxStreams: []*transcoderpb.MuxStream{
    						{
    							Key:               "sd",
    							Container:         "mp4",
    							ElementaryStreams: []string{"video_stream0", "audio_stream0"},
    						},
    					},
    					Overlays: []*transcoderpb.Overlay{
    						{
    							Image: &transcoderpb.Overlay_Image{
    								Uri: overlayImageURI,
    								Resolution: &transcoderpb.Overlay_NormalizedCoordinate{
    									X: 0,
    									Y: 0,
    								},
    								Alpha: 1,
    							},
    							Animations: []*transcoderpb.Overlay_Animation{
    								{
    									AnimationType: &transcoderpb.Overlay_Animation_AnimationFade{
    										AnimationFade: &transcoderpb.Overlay_AnimationFade{
    											FadeType: transcoderpb.[Overlay_FADE_IN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1/transcoderpb.html#cloud_google_com_go_video_transcoder_apiv1_transcoderpb_Overlay_FADE_TYPE_UNSPECIFIED_Overlay_FADE_IN_Overlay_FADE_OUT),
    											Xy: &transcoderpb.Overlay_NormalizedCoordinate{
    												X: 0.5,
    												Y: 0.5,
    											},
    											StartTimeOffset: &duration.Duration{
    												Seconds: 5,
    											},
    											EndTimeOffset: &duration.Duration{
    												Seconds: 10,
    											},
    										},
    									},
    								},
    
    								{
    									AnimationType: &transcoderpb.Overlay_Animation_AnimationFade{
    										AnimationFade: &transcoderpb.Overlay_AnimationFade{
    											FadeType: transcoderpb.[Overlay_FADE_OUT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1/transcoderpb.html#cloud_google_com_go_video_transcoder_apiv1_transcoderpb_Overlay_FADE_TYPE_UNSPECIFIED_Overlay_FADE_IN_Overlay_FADE_OUT),
    											Xy: &transcoderpb.Overlay_NormalizedCoordinate{
    												X: 0.5,
    												Y: 0.5,
    											},
    											StartTimeOffset: &duration.Duration{
    												Seconds: 12,
    											},
    											EndTimeOffset: &duration.Duration{
    												Seconds: 15,
    											},
    										},
    									},
    								},
    							},
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
    		return fmt.Errorf("createJobWithAnimatedOverlay: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.AudioStream.html);
    import com.google.cloud.video.transcoder.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html);
    import com.google.cloud.video.transcoder.v1.[Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html);
    import com.google.cloud.video.transcoder.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html);
    import com.google.cloud.video.transcoder.v1.[MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html);
    import com.google.cloud.video.transcoder.v1.[Output](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Output.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[Animation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[AnimationFade](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationFade.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[FadeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.FadeType.html);
    import com.google.cloud.video.transcoder.v1.[Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[NormalizedCoordinate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import com.google.cloud.video.transcoder.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    
    public class CreateJobWithAnimatedOverlay {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputUri = "gs://my-bucket/my-video-file";
        String overlayImageUri = "gs://my-bucket/my-overlay-image.jpg";
        String outputUri = "gs://my-bucket/my-output-folder/";
    
        createJobWithAnimatedOverlay(projectId, location, inputUri, overlayImageUri, outputUri);
      }
    
      // Creates a job from an ad-hoc configuration and adds an animated overlay to it.
      public static void createJobWithAnimatedOverlay(
          String projectId, String location, String inputUri, String overlayImageUri, String outputUri)
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
    
          // Create the overlay image. Image resolution is based on output video resolution.
          // This example uses the values x: 0 and y: 0 to maintain the original resolution
          // of the overlay image.
          [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Image.html) overlayImage =
              [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).Image.newBuilder()
                  .setUri(overlayImageUri)
                  .[setResolution](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Image.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Image_Builder_setResolution_com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_)([NormalizedCoordinate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.html).newBuilder().[setX](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setX_double_)(0).[setY](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setY_double_)(0).build())
                  .[setAlpha](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Image.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Image_Builder_setAlpha_double_)(1)
                  .build();
    
          // Create the starting animation (when the overlay starts to fade in). Use the values x: 0.5
          // and y: 0.5 to position the top-left corner of the overlay in the top-left corner of the
          // output video.
          [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[Animation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.html) animationFadeIn =
              [Animation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.html).newBuilder()
                  .[setAnimationFade](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Animation_Builder_setAnimationFade_com_google_cloud_video_transcoder_v1_Overlay_AnimationFade_)(
                      [AnimationFade](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationFade.html).newBuilder()
                          .[setFadeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationFade.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_AnimationFade_Builder_setFadeType_com_google_cloud_video_transcoder_v1_Overlay_FadeType_)([FadeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.FadeType.html).FADE_IN)
                          .setXy([NormalizedCoordinate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.html).newBuilder().[setX](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setX_double_)(0.5).[setY](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setY_double_)(0.5).build())
                          .setStartTimeOffset([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(5).build())
                          .setEndTimeOffset([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(10).build())
                          .build())
                  .build();
    
          // Create the ending animation (when the overlay starts to fade out). The overlay will start
          // to fade out at the 12-second mark in the output video.
          [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).[Animation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.html) animationFadeOut =
              [Animation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.html).newBuilder()
                  .[setAnimationFade](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Animation.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Animation_Builder_setAnimationFade_com_google_cloud_video_transcoder_v1_Overlay_AnimationFade_)(
                      [AnimationFade](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationFade.html).newBuilder()
                          .[setFadeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.AnimationFade.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_AnimationFade_Builder_setFadeType_com_google_cloud_video_transcoder_v1_Overlay_FadeType_)([FadeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.FadeType.html).FADE_OUT)
                          .setXy([NormalizedCoordinate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.html).newBuilder().[setX](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setX_double_)(0.5).[setY](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.NormalizedCoordinate.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_NormalizedCoordinate_Builder_setY_double_)(0.5).build())
                          .setStartTimeOffset([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(12).build())
                          .setEndTimeOffset([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(15).build())
                          .build())
                  .build();
    
          // Create the overlay and add the image and animations to it.
          [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html) overlay =
              [Overlay](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.html).newBuilder()
                  .[setImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Builder_setImage_com_google_cloud_video_transcoder_v1_Overlay_Image_)(overlayImage)
                  .[addAnimations](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Builder_addAnimations_com_google_cloud_video_transcoder_v1_Overlay_Animation_)(animationFadeIn)
                  .[addAnimations](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Overlay.Builder.html#com_google_cloud_video_transcoder_v1_Overlay_Builder_addAnimations_com_google_cloud_video_transcoder_v1_Overlay_Animation_)(animationFadeOut)
                  .build();
    
          [JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html) config =
              [JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html).newBuilder()
                  .addInputs([Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html).newBuilder().setKey("input0").setUri(inputUri))
                  .[setOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_setOutput_com_google_cloud_video_transcoder_v1_Output_)([Output](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Output.html).newBuilder().setUri(outputUri))
                  .addElementaryStreams(
                      [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html).newBuilder()
                          .setKey("video_stream0")
                          .[setVideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setVideoStream_com_google_cloud_video_transcoder_v1_VideoStream_)(videoStream0))
                  .addElementaryStreams(
                      [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html).newBuilder()
                          .setKey("audio_stream0")
                          .[setAudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setAudioStream_com_google_cloud_video_transcoder_v1_AudioStream_)(audioStream0))
                  .addMuxStreams(
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("sd")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("mp4")
                          .addElementaryStreams("video_stream0")
                          .addElementaryStreams("audio_stream0")
                          .build())
                  .[addOverlays](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_addOverlays_com_google_cloud_video_transcoder_v1_Overlay_)(overlay) // Add the overlay to the job config
                  .build();
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html).newBuilder()
                  .setJob(
                      [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html).newBuilder()
                          .[setInputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setInputUri_java_lang_String_)(inputUri)
                          .[setOutputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setOutputUri_java_lang_String_)(outputUri)
                          .setConfig(config)
                          .build())
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
    // inputUri = 'gs://my-bucket/my-video-file';
    // overlayImageUri = 'gs://my-bucket/my-overlay-image-file';
    // outputUri = 'gs://my-bucket/my-output-folder/';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function createJobFromAnimatedOverlay() {
      // Construct request
      const request = {
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
        job: {
          inputUri: inputUri,
          outputUri: outputUri,
          config: {
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
            ],
            muxStreams: [
              {
                key: 'sd',
                container: 'mp4',
                elementaryStreams: ['video-stream0', 'audio-stream0'],
              },
            ],
            overlays: [
              {
                image: {
                  uri: overlayImageUri,
                  resolution: {
                    x: 0,
                    y: 0,
                  },
                  alpha: 1.0,
                },
                animations: [
                  {
                    animationFade: {
                      fadeType: '[FADE_IN](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.overlay.fadetype.html)',
                      xy: {
                        x: 0.5,
                        y: 0.5,
                      },
                      startTimeOffset: {
                        seconds: 5,
                      },
                      endTimeOffset: {
                        seconds: 10,
                      },
                    },
                  },
                  {
                    animationFade: {
                      fadeType: '[FADE_OUT](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.overlay.fadetype.html)',
                      xy: {
                        x: 0.5,
                        y: 0.5,
                      },
                      startTimeOffset: {
                        seconds: 12,
                      },
                      endTimeOffset: {
                        seconds: 15,
                      },
                    },
                  },
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
    
    createJobFromAnimatedOverlay();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\AudioStream;
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\CreateJobRequest;
    use Google\Cloud\Video\Transcoder\V1\ElementaryStream;
    use Google\Cloud\Video\Transcoder\V1\Job;
    use Google\Cloud\Video\Transcoder\V1\JobConfig;
    use Google\Cloud\Video\Transcoder\V1\MuxStream;
    use Google\Cloud\Video\Transcoder\V1\Overlay;
    use Google\Cloud\Video\Transcoder\V1\VideoStream;
    use Google\Protobuf\Duration;
    
    /**
     * Creates a job based on a supplied job config that includes an animated overlay.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $inputUri Uri of the video in the Cloud Storage bucket.
     * @param string $overlayImageUri Uri of the image for the overlay in the Cloud Storage bucket.
     * @param string $outputUri Uri of the video output folder in the Cloud Storage bucket.
     */
    function create_job_with_animated_overlay($projectId, $location, $inputUri, $overlayImageUri, $outputUri)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedParent = $transcoderServiceClient->locationName($projectId, $location);
        $jobConfig =
            (new JobConfig())->setElementaryStreams([
                (new ElementaryStream())
                    ->setKey('video-stream0')
                    ->setVideoStream(
                        (new VideoStream())->setH264(
                            (new VideoStream\H264CodecSettings())
                                ->setBitrateBps(550000)
                                ->setFrameRate(60)
                                ->setHeightPixels(360)
                                ->setWidthPixels(640)
                        )
                    ),
                (new ElementaryStream())
                    ->setKey('audio-stream0')
                    ->setAudioStream(
                        (new AudioStream())
                            ->setCodec('aac')
                            ->setBitrateBps(64000)
                    )
            ])->setMuxStreams([
                (new MuxStream())
                    ->setKey('sd')
                    ->setContainer('mp4')
                    ->setElementaryStreams(['video-stream0', 'audio-stream0'])
            ])->setOverlays([
                (new Overlay())->setImage(
                    (new Overlay\Image())
                        ->setUri($overlayImageUri)
                        ->setResolution(
                            (new Overlay\NormalizedCoordinate())
                                ->setX(0)
                                ->setY(0)
                        )
                        ->setAlpha(1)
                )->setAnimations([
                    (new Overlay\Animation())->setAnimationFade(
                        (new Overlay\AnimationFade())
                            ->setFadeType(Overlay\FadeType::FADE_IN)
                            ->setXy(
                                (new Overlay\NormalizedCoordinate())
                                    ->setY(0.5)
                                    ->setX(0.5)
                            )
                            ->setStartTimeOffset(new Duration(['seconds' => 5]))
                            ->setEndTimeOffset(new Duration(['seconds' => 10]))
                    ),
                    (new Overlay\Animation())->setAnimationFade(
                        (new Overlay\AnimationFade())
                            ->setFadeType(Overlay\FadeType::FADE_OUT)
                            ->setXy(
                                (new Overlay\NormalizedCoordinate())
                                    ->setY(0.5)
                                    ->setX(0.5)
                            )
                            ->setStartTimeOffset(new Duration(['seconds' => 12]))
                            ->setEndTimeOffset(new Duration(['seconds' => 15]))
                    )
                ])
            ]);
    
        $job = (new Job())
            ->setInputUri($inputUri)
            ->setOutputUri($outputUri)
            ->setConfig($jobConfig);
        $request = (new CreateJobRequest())
            ->setParent($formattedParent)
            ->setJob($job);
    
        $response = $transcoderServiceClient->createJob($request);
    
        // Print job name.
        printf('Job: %s' . PHP_EOL, $response->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import transcoder_v1
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        TranscoderServiceClient,
    )
    from google.protobuf import duration_pb2 as duration
    
    
    def create_job_with_animated_overlay(
        project_id: str,
        location: str,
        input_uri: str,
        overlay_image_uri: str,
        output_uri: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job based on an ad-hoc job configuration that includes an animated image overlay.
    
        Args:
            project_id: The GCP project ID.
            location: The location to start the job in.
            input_uri: Uri of the video in the Cloud Storage bucket.
            overlay_image_uri: Uri of the image for the overlay in the Cloud Storage bucket.
            output_uri: Uri of the video output folder in the Cloud Storage bucket.
    
        Returns:
            The job resource.
        """
    
        client = TranscoderServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        job = transcoder_v1.types.Job()
        job.input_uri = input_uri
        job.output_uri = output_uri
        job.config = transcoder_v1.types.JobConfig(
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
                        codec="aac", bitrate_bps=64000
                    ),
                ),
            ],
            mux_streams=[
                transcoder_v1.types.MuxStream(
                    key="sd",
                    container="mp4",
                    elementary_streams=["video-stream0", "audio-stream0"],
                ),
            ],
            overlays=[
                transcoder_v1.types.Overlay(
                    image=transcoder_v1.types.Overlay.Image(
                        uri=overlay_image_uri,
                        resolution=transcoder_v1.types.Overlay.NormalizedCoordinate(
                            x=0,
                            y=0,
                        ),
                        alpha=1,
                    ),
                    animations=[
                        transcoder_v1.types.Overlay.Animation(
                            animation_fade=transcoder_v1.types.Overlay.AnimationFade(
                                fade_type=transcoder_v1.types.Overlay.FadeType.FADE_IN,
                                xy=transcoder_v1.types.Overlay.NormalizedCoordinate(
                                    x=0.5,
                                    y=0.5,
                                ),
                                start_time_offset=duration.Duration(
                                    seconds=5,
                                ),
                                end_time_offset=duration.Duration(
                                    seconds=10,
                                ),
                            ),
                        ),
                        transcoder_v1.types.Overlay.Animation(
                            animation_fade=transcoder_v1.types.Overlay.AnimationFade(
                                fade_type=transcoder_v1.types.Overlay.FadeType.FADE_OUT,
                                xy=transcoder_v1.types.Overlay.NormalizedCoordinate(
                                    x=0.5,
                                    y=0.5,
                                ),
                                start_time_offset=duration.Duration(
                                    seconds=12,
                                ),
                                end_time_offset=duration.Duration(
                                    seconds=15,
                                ),
                            ),
                        ),
                    ],
                ),
            ],
        )
        response = client.create_job(parent=parent, job=job)
        print(f"Job: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location    = "YOUR-JOB-LOCATION"  # (e.g. "us-central1")
    # input_uri   = "YOUR-GCS-INPUT-VIDEO"  # (e.g. "gs://my-bucket/my-video-file")
    # overlay_image_uri   = "YOUR-GCS-OVERLAY-IMAGE"  # (e.g. "gs://my-bucket/overlay.jpg")
    # output_uri  = "YOUR-GCS-OUTPUT-FOLDER/"  # (e.g. "gs://my-bucket/my-output-folder/")
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the parent.
    parent = client.location_path project: project_id, location: location
    
    # Build the job config.
    new_job = {
      input_uri: input_uri,
      output_uri: output_uri,
      config: {
        elementary_streams: [
          {
            key: "video-stream0",
            video_stream: {
              h264: {
                height_pixels: 360,
                width_pixels: 640,
                bitrate_bps: 550_000,
                frame_rate: 60
              }
            }
          },
          {
            key: "audio-stream0",
            audio_stream: {
              codec: "aac",
              bitrate_bps: 64_000
            }
          }
        ],
        mux_streams: [
          {
            key: "sd",
            container: "mp4",
            elementary_streams: [
              "video-stream0",
              "audio-stream0"
            ]
          }
        ],
        overlays: [
          {
            image: {
              uri: overlay_image_uri,
              resolution: {
                x: 0,
                y: 0
              },
              alpha: 1
            },
            animations: [
              {
                animation_fade: {
                  fade_type: Google::Cloud::Video::Transcoder::V1::Overlay::FadeType::FADE_IN,
                  xy: {
                    x: 0.5,
                    y: 0.5
                  },
                  start_time_offset: {
                    seconds: 5
                  },
                  end_time_offset: {
                    seconds: 10
                  }
                }
              },
              {
                animation_fade: {
                  fade_type: Google::Cloud::Video::Transcoder::V1::Overlay::FadeType::FADE_OUT,
                  xy: {
                    x: 0.5,
                    y: 0.5
                  },
                  start_time_offset: {
                    seconds: 12
                  },
                  end_time_offset: {
                    seconds: 15
                  }
                }
              }
            ]
          }
        ]
      }
    }
    
    job = client.create_job parent: parent, job: new_job
    
    # Print the job name.
    puts "Job: #{job.name}"

In the resulting video, the animated overlay has the following characteristics:

  1. It starts to fade in at the 5-second mark in the output video. The alpha value for the overlay starts at 0 and ends at 1.0. The top-left corner of the overlay appears at the center of the output video. The overlay appears at the original resolution of the overlay image.
  2. After it fades in, the overlay shows for 2 seconds.
  3. It starts to fade out at the 12-second mark in the output video. The alpha value for the overlay starts at 1.0 and ends at 0.
  4. The animation disappears by the 15-second mark.



See the [sample output video](https://docs.cloud.google.com/static/transcoder/images/animated-overlay-sample.mp4) for this configuration. This video uses a [sample overlay image](https://docs.cloud.google.com/static/transcoder/images/overlay.png).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
