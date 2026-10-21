---
url: https://docs.cloud.google.com/transcoder/docs/how-to/concatenate-videos/
title: Concatenating multiple input videos \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:26.775475+00:00
---

# Concatenating multiple input videos  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/concatenate-videos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Concatenating multiple input videos Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to combine multiple input videos into a single output video. You can also trim the timelines of the input videos.

For each input video, add an [`Input`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#input) object to the [`inputs`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.inputs) array. Each [`Input`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#input) object defines the key and URI for the associated input video. You can add an optional [`PreprocessingConfig`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#PreprocessingConfig) object to an [`Input`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#input) to [crop](https://docs.cloud.google.com/transcoder/docs/how-to/crop-videos), pad, or perform other preprocessing on the input video. The [`inputs`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) array is not ordered; you can add input videos in any order.

To add an input video to the output video timeline, add an [`EditAtom`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#editatom) object to the [`editList`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.edit_list) array. The [`editList`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.edit_list) array is ordered. The first input designated in this array will be used first in the output video, the second input will be used next, and so on. You identify an input video by its key.

You can also designate a `startTimeOffset` and `endTimeOffset` to trim the input video. These fields are optional. If you don't specify these fields, the entire input video is used.

The following configuration concatenates two input videos into a single output video.
    
    
    "inputs": [
      {
        "key": "input1",
        "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO1"
      },
      {
        "key": "input2",
        "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO2"
      }
    ],
    "editList": [
      {
        "key": "atom1",
        "inputs": [
          "input1"
        ],
        "startTimeOffset": "START_TIME_OFFSET1s",
        "endTimeOffset": "END_TIME_OFFSET1s"
      },
      {
        "key": "atom2",
        "inputs": [
          "input2"
        ],
        "startTimeOffset": "START_TIME_OFFSET2s",
        "endTimeOffset": "END_TIME_OFFSET2s"
      }
    ],
    

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
  * `STORAGE_INPUT_VIDEO1`: The name of a video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). This video will be used first in the output video timeline. 
  * `START_TIME_OFFSET1`: The start time, in fractional seconds (for example, `0.0`), relative to the first input video timeline. Use this field to trim content from the beginning of the video. 
  * `END_TIME_OFFSET1`: The end time, in fractional seconds (for example, `8.1`), relative to the first input video timeline. Use this field to trim content from the end of the video. 
  * `STORAGE_INPUT_VIDEO2`: The name of a video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). This video will be used second in the output video timeline. 
  * `START_TIME_OFFSET2`: The start time, in fractional seconds (for example, `3.5`), relative to the second input video timeline. Use this field to trim content from the beginning of the second video. 
  * `END_TIME_OFFSET2`: The end time, in fractional seconds (for example, `15`), relative to the second input video timeline. Use this field to trim content from the end of the second video. 
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
            "key": "input1",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO1"
          },
          {
            "key": "input2",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO2"
          }
        ],
        "editList": [
          {
            "key": "atom1",
            "inputs": [
              "input1"
            ],
            "startTimeOffset": "START_TIME_OFFSET1s",
            "endTimeOffset": "END_TIME_OFFSET1s"
          },
          {
            "key": "atom2",
            "inputs": [
              "input2"
            ],
            "startTimeOffset": "START_TIME_OFFSET2s",
            "endTimeOffset": "END_TIME_OFFSET2s"
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
        }
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
            "key": "input1",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO1"
          },
          {
            "key": "input2",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO2"
          }
        ],
        "editList": [
          {
            "key": "atom1",
            "inputs": [
              "input1"
            ],
            "startTimeOffset": "START_TIME_OFFSET1s",
            "endTimeOffset": "END_TIME_OFFSET1s"
          },
          {
            "key": "atom2",
            "inputs": [
              "input2"
            ],
            "startTimeOffset": "START_TIME_OFFSET2s",
            "endTimeOffset": "END_TIME_OFFSET2s"
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
        }
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
     * LOCATION: The location where your job will run. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

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
     * STORAGE_BUCKET_NAME: The name of the Cloud Storage bucket you created.
     * STORAGE_INPUT_VIDEO1: The name of a video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). This video will be used first in the output video timeline. 
     * START_TIME_OFFSET1: The start time, in fractional seconds (for example, `0.0`), relative to the first input video timeline. Use this field to trim content from the beginning of the video. 
     * END_TIME_OFFSET1: The end time, in fractional seconds (for example, `8.1`), relative to the first input video timeline. Use this field to trim content from the end of the video. 
     * STORAGE_INPUT_VIDEO2: The name of a video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). This video will be used second in the output video timeline. 
     * START_TIME_OFFSET2: The start time, in fractional seconds (for example, `3.5`), relative to the second input video timeline. Use this field to trim content from the beginning of the second video. 
     * END_TIME_OFFSET2: The end time, in fractional seconds (for example, `15`), relative to the second input video timeline. Use this field to trim content from the end of the second video. 
     * STORAGE_OUTPUT_FOLDER: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.
    
    {
      "config": {
        "inputs": [
          {
            "key": "input1",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO1"
          },
          {
            "key": "input2",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO2"
          }
        ],
        "editList": [
          {
            "key": "atom1",
            "inputs": [
              "input1"
            ],
            "startTimeOffset": "START_TIME_OFFSET1s",
            "endTimeOffset": "END_TIME_OFFSET1s"
          },
          {
            "key": "atom2",
            "inputs": [
              "input2"
            ],
            "startTimeOffset": "START_TIME_OFFSET2s",
            "endTimeOffset": "END_TIME_OFFSET2s"
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
        }
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
    
    public class CreateJobWithConcatenatedInputsSample
    {
        public Job CreateJobWithConcatenatedInputs(
            string projectId, string location, string inputUri1, TimeSpan startTimeInput1, TimeSpan endTimeInput1, string inputUri2, TimeSpan startTimeInput2, TimeSpan endTimeInput2, string outputUri)
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
    
            [Input](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html) input1 = new [Input](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html)
            {
                Key = "input1",
                Uri = inputUri1
            };
    
            [Input](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html) input2 = new [Input](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html)
            {
                Key = "input2",
                Uri = inputUri2
            };
    
            [EditAtom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.EditAtom.html) atom1 = new [EditAtom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.EditAtom.html)
            {
                Key = "atom1",
                StartTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(startTimeInput1),
                EndTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(endTimeInput1),
                Inputs = { input1.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html#Google_Cloud_Video_Transcoder_V1_Input_Key) }
            };
    
            [EditAtom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.EditAtom.html) atom2 = new [EditAtom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.EditAtom.html)
            {
                Key = "atom2",
                StartTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(startTimeInput2),
                EndTimeOffset = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(endTimeInput2),
                Inputs = { input2.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Input.html#Google_Cloud_Video_Transcoder_V1_Input_Key) }
            };
    
            [Output](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Output.html) output = new [Output](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Output.html)
            {
                Uri = outputUri
            };
    
            [JobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobConfig.html) jobConfig = new [JobConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobConfig.html)
            {
                Inputs = { input1, input2 },
                EditList = { atom1, atom2 },
                Output = output,
                ElementaryStreams = { elementaryStream0, elementaryStream1 },
                MuxStreams = { muxStream0 }
            };
    
            // Build the job.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) newJob = new [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html)
            {
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
    	"time"
    
    	transcoder "cloud.google.com/go/video/transcoder/apiv1"
    	"cloud.google.com/go/video/transcoder/apiv1/transcoderpb"
    	"google.golang.org/protobuf/types/known/durationpb"
    )
    
    // createJobWithConcatenatedInputs creates a job that concatenates two input
    // videos. See https://cloud.google.com/transcoder/docs/how-to/concatenate-videos
    // for more information.
    func createJobWithConcatenatedInputs(w io.Writer, projectID string, location string, input1URI string, startTimeInput1 time.Duration, endTimeInput1 time.Duration, input2URI string, startTimeInput2 time.Duration, endTimeInput2 time.Duration, outputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	//
    	// input1URI := "gs://my-bucket/my-video-file1"
    	// startTimeInput1 := 0*time.Second
    	// endTimeInput1 := 8*time.Second + 100*time.Millisecond
    	//
    	// input2URI := "gs://my-bucket/my-video-file2"
    	// startTimeInput2 := 3*time.Second + 500*time.Millisecond
    	// endTimeInput2 := 15*time.Second
    	//
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
    			OutputUri: outputURI,
    			JobConfig: &transcoderpb.Job_Config{
    				Config: &transcoderpb.JobConfig{
    					Inputs: []*transcoderpb.Input{
    						{
    							Key: "input1",
    							Uri: input1URI,
    						},
    						{
    							Key: "input2",
    							Uri: input2URI,
    						},
    					},
    					EditList: []*transcoderpb.EditAtom{
    						{
    							Key:             "atom1",
    							Inputs:          []string{"input1"},
    							StartTimeOffset: durationpb.New(startTimeInput1),
    							EndTimeOffset:   durationpb.New(endTimeInput1),
    						},
    						{
    							Key:             "atom2",
    							Inputs:          []string{"input2"},
    							StartTimeOffset: durationpb.New(startTimeInput2),
    							EndTimeOffset:   durationpb.New(endTimeInput2),
    						},
    					},
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
    import com.google.cloud.video.transcoder.v1.[MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html);
    import com.google.cloud.video.transcoder.v1.[Output](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Output.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import com.google.cloud.video.transcoder.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    
    public class CreateJobWithConcatenatedInputs {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputUri1 = "gs://my-bucket/my-video-file1";
        [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) startTimeInput1 = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(0).setNanos(0).build();
        [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) endTimeInput1 = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(8).setNanos(100000000).build();
        String inputUri2 = "gs://my-bucket/my-video-file2";
        [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) startTimeInput2 = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(3).setNanos(500000000).build();
        [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) endTimeInput2 = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(15).setNanos(0).build();
        String outputUri = "gs://my-bucket/my-output-folder/";
    
        createJobWithConcatenatedInputs(
            projectId,
            location,
            inputUri1,
            startTimeInput1,
            endTimeInput1,
            inputUri2,
            startTimeInput2,
            endTimeInput2,
            outputUri);
      }
    
      // Creates a job from an ad-hoc configuration that concatenates two input videos.
      public static void createJobWithConcatenatedInputs(
          String projectId,
          String location,
          String inputUri1,
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) startTimeInput1,
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) endTimeInput1,
          String inputUri2,
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) startTimeInput2,
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) endTimeInput2,
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
    
          [JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html) config =
              [JobConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.html).newBuilder()
                  .addInputs([Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html).newBuilder().setKey("input1").setUri(inputUri1))
                  .addInputs([Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Input.html).newBuilder().setKey("input2").setUri(inputUri2))
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
                  .[addEditList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_addEditList_com_google_cloud_video_transcoder_v1_EditAtom_)(
                      0, // Index in the edit list
                      [EditAtom](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.EditAtom.html).newBuilder()
                          .setKey("atom1")
                          .addInputs("input1")
                          .setStartTimeOffset(startTimeInput1)
                          .setEndTimeOffset(endTimeInput1)
                          .build())
                  .[addEditList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_addEditList_com_google_cloud_video_transcoder_v1_EditAtom_)(
                      1, // Index in the edit list
                      [EditAtom](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.EditAtom.html).newBuilder()
                          .setKey("atom2")
                          .addInputs("input2")
                          .setStartTimeOffset(startTimeInput2)
                          .setEndTimeOffset(endTimeInput2)
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
    // inputUri1 = 'gs://my-bucket/my-video-file1';
    // startTimeOffset1 = 0;
    // endTimeOffset1 = 8.1;
    // inputUri2 = 'gs://my-bucket/my-video-file2';
    // startTimeOffset2 = 3.5;
    // endTimeOffset2 = 15;
    // outputUri = 'gs://my-bucket/my-output-folder/';
    
    function calcOffsetNanoSec(offsetValueFractionalSecs) {
      if (offsetValueFractionalSecs.toString().indexOf('.') !== -1) {
        return (
          1000000000 *
          Number('.' + offsetValueFractionalSecs.toString().split('.')[1])
        );
      }
      return 0;
    }
    const startTimeOffset1Sec = Math.trunc(startTimeOffset1);
    const startTimeOffset1NanoSec = calcOffsetNanoSec(startTimeOffset1);
    const endTimeOffset1Sec = Math.trunc(endTimeOffset1);
    const endTimeOffset1NanoSec = calcOffsetNanoSec(endTimeOffset1);
    
    const startTimeOffset2Sec = Math.trunc(startTimeOffset2);
    const startTimeOffset2NanoSec = calcOffsetNanoSec(startTimeOffset2);
    const endTimeOffset2Sec = Math.trunc(endTimeOffset2);
    const endTimeOffset2NanoSec = calcOffsetNanoSec(endTimeOffset2);
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function createJobWithConcatenatedInputs() {
      // Construct request
      const request = {
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
        job: {
          outputUri: outputUri,
          config: {
            inputs: [
              {
                key: 'input1',
                uri: inputUri1,
              },
              {
                key: 'input2',
                uri: inputUri2,
              },
            ],
            editList: [
              {
                key: 'atom1',
                inputs: ['input1'],
                startTimeOffset: {
                  seconds: startTimeOffset1Sec,
                  nanos: startTimeOffset1NanoSec,
                },
                endTimeOffset: {
                  seconds: endTimeOffset1Sec,
                  nanos: endTimeOffset1NanoSec,
                },
              },
              {
                key: 'atom2',
                inputs: ['input2'],
                startTimeOffset: {
                  seconds: startTimeOffset2Sec,
                  nanos: startTimeOffset2NanoSec,
                },
                endTimeOffset: {
                  seconds: endTimeOffset2Sec,
                  nanos: endTimeOffset2NanoSec,
                },
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
            ],
            muxStreams: [
              {
                key: 'sd',
                container: 'mp4',
                elementaryStreams: ['video-stream0', 'audio-stream0'],
              },
            ],
          },
        },
      };
    
      // Run request
      const [response] = await transcoderServiceClient.createJob(request);
      console.log(`Job: ${response.name}`);
    }
    
    createJobWithConcatenatedInputs();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\AudioStream;
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\CreateJobRequest;
    use Google\Cloud\Video\Transcoder\V1\EditAtom;
    use Google\Cloud\Video\Transcoder\V1\ElementaryStream;
    use Google\Cloud\Video\Transcoder\V1\Input;
    use Google\Cloud\Video\Transcoder\V1\Job;
    use Google\Cloud\Video\Transcoder\V1\JobConfig;
    use Google\Cloud\Video\Transcoder\V1\MuxStream;
    use Google\Cloud\Video\Transcoder\V1\VideoStream;
    use Google\Protobuf\Duration;
    
    /**
     * Creates a job based on a supplied job config that concatenates two input videos.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $input1Uri Uri of the first video in the Cloud Storage bucket.
     * @param float  $startTimeInput1 Start time, in fractional seconds, relative to the first input video timeline.
     * @param float  $endTimeInput1 End time, in fractional seconds, relative to the first input video timeline.
     * @param string $input2Uri Uri of the second video in the Cloud Storage bucket.
     * @param float  $startTimeInput2 Start time, in fractional seconds, relative to the second input video timeline.
     * @param float  $endTimeInput2 End time, in fractional seconds, relative to the second input video timeline.
     * @param string $outputUri Uri of the video output folder in the Cloud Storage bucket.
     */
    function create_job_with_concatenated_inputs($projectId, $location, $input1Uri, $startTimeInput1, $endTimeInput1, $input2Uri, $startTimeInput2, $endTimeInput2, $outputUri)
    {
        $startTimeInput1Sec = (int) floor(abs($startTimeInput1));
        $startTimeInput1Nanos = (int) (1000000000 * bcsub((string) abs($startTimeInput1), (string) floor(abs($startTimeInput1)), 4));
        $endTimeInput1Sec = (int) floor(abs($endTimeInput1));
        $endTimeInput1Nanos = (int) (1000000000 * bcsub((string) abs($endTimeInput1), (string) floor(abs($endTimeInput1)), 4));
    
        $startTimeInput2Sec = (int) floor(abs($startTimeInput2));
        $startTimeInput2Nanos = (int) (1000000000 * bcsub((string) abs($startTimeInput2), (string) floor(abs($startTimeInput2)), 4));
        $endTimeInput2Sec = (int) floor(abs($endTimeInput2));
        $endTimeInput2Nanos = (int) (1000000000 * bcsub((string) abs($endTimeInput2), (string) floor(abs($endTimeInput2)), 4));
    
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedParent = $transcoderServiceClient->locationName($projectId, $location);
        $jobConfig =
            (new JobConfig())->setInputs([
                (new Input())
                    ->setKey('input1')
                    ->setUri($input1Uri),
                (new Input())
                    ->setKey('input2')
                    ->setUri($input2Uri)
            ])->setEditList([
                (new EditAtom())
                    ->setKey('atom1')
                    ->setInputs(['input1'])
                    ->setStartTimeOffset(new Duration(['seconds' => $startTimeInput1Sec, 'nanos' => $startTimeInput1Nanos]))
                    ->setEndTimeOffset(new Duration(['seconds' => $endTimeInput1Sec, 'nanos' => $endTimeInput1Nanos])),
                (new EditAtom())
                    ->setKey('atom2')
                    ->setInputs(['input2'])
                    ->setStartTimeOffset(new Duration(['seconds' => $startTimeInput2Sec, 'nanos' => $startTimeInput2Nanos]))
                    ->setEndTimeOffset(new Duration(['seconds' => $endTimeInput2Sec, 'nanos' => $endTimeInput2Nanos])),
            ])->setElementaryStreams([
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
            ]);
    
        $job = (new Job())
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
    
    from google.cloud.video import [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest)
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        [TranscoderServiceClient](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.services.transcoder_service.TranscoderServiceClient.html),
    )
    from google.protobuf import duration_pb2 as duration
    
    
    def create_job_with_concatenated_inputs(
        project_id: str,
        location: str,
        input1_uri: str,
        start_time_input1: str,
        end_time_input1: str,
        input2_uri: str,
        start_time_input2: str,
        end_time_input2: str,
        output_uri: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job based on an ad-hoc job configuration that concatenates two input videos.
    
        Args:
            project_id (str): The GCP project ID.
            location (str): The location to start the job in.
            input1_uri (str): Uri of the first video in the Cloud Storage bucket.
            start_time_input1 (str): Start time, in fractional seconds ending in 's'
              (e.g., '0s'), relative to the first input video timeline.
            end_time_input1 (str): End time, in fractional seconds ending in 's'
              (e.g., '8.1s'), relative to the first input video timeline.
            input2_uri (str): Uri of the second video in the Cloud Storage bucket.
            start_time_input2 (str): Start time, in fractional seconds ending in 's'
              (e.g., '3.5s'), relative to the second input video timeline.
            end_time_input2 (str): End time, in fractional seconds ending in 's'
              (e.g., '15s'), relative to the second input video timeline.
            output_uri (str): Uri of the video output folder in the Cloud Storage
              bucket.
    
        Returns:
            The job resource.
        """
    
        s1 = duration.Duration()
        s1.FromJsonString(start_time_input1)
        e1 = duration.Duration()
        e1.FromJsonString(end_time_input1)
    
        s2 = duration.Duration()
        s2.FromJsonString(start_time_input2)
        e2 = duration.Duration()
        e2.FromJsonString(end_time_input2)
    
        client = TranscoderServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        job = [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[Job](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.Job.html)()
        job.output_uri = output_uri
        job.config = [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[JobConfig](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.JobConfig.html)(
            inputs=[
                [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[Input](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.Input.html)(
                    key="input1",
                    uri=input1_uri,
                ),
                [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[Input](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.Input.html)(
                    key="input2",
                    uri=input2_uri,
                ),
            ],
            edit_list=[
                [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[EditAtom](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.EditAtom.html)(
                    key="atom1",
                    inputs=["input1"],
                    start_time_offset=s1,
                    end_time_offset=e1,
                ),
                [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[EditAtom](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.EditAtom.html)(
                    key="atom2",
                    inputs=["input2"],
                    start_time_offset=s2,
                    end_time_offset=e2,
                ),
            ],
            elementary_streams=[
                [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[ElementaryStream](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.ElementaryStream.html)(
                    key="video-stream0",
                    video_stream=[transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[VideoStream](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.VideoStream.html)(
                        h264=[transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[VideoStream](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.VideoStream.html).[H264CodecSettings](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.VideoStream.H264CodecSettings.html)(
                            height_pixels=360,
                            width_pixels=640,
                            bitrate_bps=550000,
                            frame_rate=60,
                        ),
                    ),
                ),
                [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[ElementaryStream](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.ElementaryStream.html)(
                    key="audio-stream0",
                    audio_stream=[transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[AudioStream](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.AudioStream.html)(
                        codec="aac", bitrate_bps=64000
                    ),
                ),
            ],
            mux_streams=[
                [transcoder_v1](https://docs.cloud.google.com/python/docs/reference/transcoder/latest).[types](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.html).[MuxStream](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.types.MuxStream.html)(
                    key="sd",
                    container="mp4",
                    elementary_streams=["video-stream0", "audio-stream0"],
                ),
            ],
        )
        response = client.[create_job](https://docs.cloud.google.com/python/docs/reference/transcoder/latest/google.cloud.video.transcoder_v1.services.transcoder_service.TranscoderServiceClient.html#google_cloud_video_transcoder_v1_services_transcoder_service_TranscoderServiceClient_create_job)(parent=parent, job=job)
        print(f"Job: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id        = # Your project ID, e.g. "my-project"
    # location          = # Data location, e.g. "us-central1"
    # input1_uri        = # First video, e.g. "gs://my-bucket/my-video-file1"
    # start_time_input1 = # Start time in fractional seconds relative to the
    #                     # first input video timeline, e.g. 0.0
    # end_time_input1   = # End time in fractional seconds relative to the
    #                     # first input video timeline, e.g. 8.125
    # input2_uri        = # Second video, e.g. "gs://my-bucket/my-video-file2"
    # start_time_input2 = # Start time in fractional seconds relative to the
    #                     # second input video timeline, e.g. 3.5
    # end_time_input2   = # End time in fractional seconds relative to the
    #                     # second input video timeline, e.g. 15
    # output_uri        = # Output folder, e.g. "gs://my-bucket/my-output-folder/"
    
    s1_sec = start_time_input1.to_i
    s1_nanos = (start_time_input1.to_f.remainder(1) * 1_000_000_000).round
    e1_sec = end_time_input1.to_i
    e1_nanos = (end_time_input1.to_f.remainder(1) * 1_000_000_000).round
    
    s2_sec = start_time_input2.to_i
    s2_nanos = (start_time_input2.to_f.remainder(1) * 1_000_000_000).round
    e2_sec = end_time_input2.to_i
    e2_nanos = (end_time_input2.to_f.remainder(1) * 1_000_000_000).round
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the parent.
    parent = client.location_path project: project_id, location: location
    
    # Build the job config.
    new_job = {
      output_uri: output_uri,
      config: {
        inputs: [
          {
            key: "input1",
            uri: input1_uri
          },
          {
            key: "input2",
            uri: input2_uri
          }
        ],
        edit_list: [
          {
            key: "atom1",
            inputs: ["input1"],
            start_time_offset: {
              seconds: s1_sec,
              nanos: s1_nanos
            },
            end_time_offset: {
              seconds: e1_sec,
              nanos: e1_nanos
            }
          },
          {
            key: "atom2",
            inputs: ["input2"],
            start_time_offset: {
              seconds: s2_sec,
              nanos: s2_nanos
            },
            end_time_offset: {
              seconds: e2_sec,
              nanos: e2_nanos
            }
          }
        ],
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
        ]
      }
    }
    
    job = client.create_job parent: parent, job: new_job
    
    # Print the job name.
    puts "Job: #{job.name}"

## Example

Consider the following sample videos:

  * [ForBiggerEscapes.mp4](https://docs.cloud.google.com/static/transcoder/images/ForBiggerEscapes.mp4)
  * [ForBiggerJoyrides.mp4](https://docs.cloud.google.com/static/transcoder/images/ForBiggerJoyrides.mp4)



Both videos are similar in that they contain three parts:

  1. Watching a movie or game on a mobile device
  2. Watching the same content on a big screen
  3. Show brief ad copy for the product



As an example, you can concatenate these two videos together such that the output video shows parts one and two from the first video, and then parts two and three from the second video. You can accomplish this concatenation using the following time offsets:

  * [ForBiggerEscapes.mp4](https://docs.cloud.google.com/static/transcoder/images/ForBiggerEscapes.mp4)
    * `startTimeOffset`: `0s`
    * `endTimeOffset`: `8.1s`
  * [ForBiggerJoyrides.mp4](https://docs.cloud.google.com/static/transcoder/images/ForBiggerJoyrides.mp4)
    * `startTimeOffset`: `3.5s`
    * `endTimeOffset`: `15s`



Use the preceding code along with these two videos and their time offsets to see an action-packed [result video](https://docs.cloud.google.com/static/transcoder/images/ForBiggerResult.mp4).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
