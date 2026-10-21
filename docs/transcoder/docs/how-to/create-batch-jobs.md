---
url: https://docs.cloud.google.com/transcoder/docs/how-to/create-batch-jobs/
title: Creating jobs in batch mode \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:25.881145+00:00
---

# Creating jobs in batch mode  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/create-batch-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Creating jobs in batch mode Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create Transcoder API jobs in batch mode. Use batch mode to submit many jobs for which the processing latency isn't as critical as jobs submitted in the default interactive mode. For more information on job modes, see the [overview](https://docs.cloud.google.com/transcoder/docs/concepts/overview#job_mode).

You can specify the [job processing priority](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.batch_mode_priority) for a job in this mode. Jobs submitted in batch mode with the same priority value are put in a first-in, first out queue and have a job state of `PENDING` while they wait to be run.

## Set up your Google Cloud project and authentication

If you have not created a [Google Cloud project](https://docs.cloud.google.com/docs/overview#projects) and credentials, see [Before you begin](https://docs.cloud.google.com/transcoder/docs/how-to/before-you-begin). 

## Set the job mode

To start a job in batch mode, set the job [`mode`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.mode) to [`PROCESSING_MODE_BATCH`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#ProcessingMode).

The following samples use the [default job preset](https://docs.cloud.google.com/transcoder/docs/concepts/overview#job_template).

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
  * `STORAGE_INPUT_VIDEO`: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). **Note:** The input video must have at least one video track and one audio track in order to use the [`preset/web-hd` preset](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.template_id).
  * `STORAGE_OUTPUT_FOLDER`: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "inputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO",
      "outputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/",
      "templateId": "preset/web-hd",
      "mode": "PROCESSING_MODE_BATCH",
      "batchModePriority": 10
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
      "inputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO",
      "outputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/",
      "templateId": "preset/web-hd",
      "mode": "PROCESSING_MODE_BATCH",
      "batchModePriority": 10
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
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0"
            ],
            "startTimeOffset": "0s"
          }
        ],
        "elementaryStreams": [
          {
            "videoStream": {
              "h264": {
                "widthPixels": 640,
                "heightPixels": 360,
                "frameRate": 30,
                "bitrateBps": 550000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 550000,
                "vbvFullnessBits": 495000,
                "entropyCoder": "cabac",
                "bFrameCount": 3,
                "aqStrength": 1,
                "profile": "high",
                "preset": "veryfast"
              }
            },
            "key": "video-stream0"
          },
          {
            "videoStream": {
              "h264": {
                "widthPixels": 1280,
                "heightPixels": 720,
                "frameRate": 30,
                "bitrateBps": 2500000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 2500000,
                "vbvFullnessBits": 2250000,
                "entropyCoder": "cabac",
                "bFrameCount": 3,
                "aqStrength": 1,
                "profile": "high",
                "preset": "veryfast"
              }
            },
            "key": "video-stream1"
          },
          {
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "sampleRateHertz": 48000
            },
            "key": "audio-stream0"
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "fileName": "sd.mp4",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "hd",
            "fileName": "hd.mp4",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream1",
              "audio-stream0"
            ]
          },
          {
            "key": "media-sd",
            "fileName": "media-sd.ts",
            "container": "ts",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "media-hd",
            "fileName": "media-hd.ts",
            "container": "ts",
            "elementaryStreams": [
              "video-stream1",
              "audio-stream0"
            ]
          },
          {
            "key": "video-only-sd",
            "fileName": "video-only-sd.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "video-only-hd",
            "fileName": "video-only-hd.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream1"
            ]
          },
          {
            "key": "audio-only",
            "fileName": "audio-only.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ]
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "type": "HLS",
            "muxStreams": [
              "media-sd",
              "media-hd"
            ]
          },
          {
            "fileName": "manifest.mpd",
            "type": "DASH",
            "muxStreams": [
              "video-only-sd",
              "video-only-hd",
              "audio-only"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        }
      },
      "state": "PENDING",
      "createTime": CREATE_TIME,
      "ttlAfterCompletionDays": 30
    }
    

### gcloud

Before using any of the command data below, make the following replacements: 

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
  * `STORAGE_INPUT_VIDEO`: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). **Note:** The input video must have at least one video track and one audio track in order to use the [`preset/web-hd` preset](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.template_id).
  * `STORAGE_OUTPUT_FOLDER`: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create \
      --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" \
      --location=LOCATION \
      --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" \
      --template-id="preset/web-hd" \
      --batch-mode-priority=10

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create `
      --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" `
      --location=LOCATION `
      --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" `
      --template-id="preset/web-hd" `
      --batch-mode-priority=10

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create ^
      --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" ^
      --location=LOCATION ^
      --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" ^
      --template-id="preset/web-hd" ^
      --batch-mode-priority=10

You should receive a response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID",
      "config": {
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0"
            ],
            "startTimeOffset": "0s"
          }
        ],
        "elementaryStreams": [
          {
            "videoStream": {
              "h264": {
                "widthPixels": 640,
                "heightPixels": 360,
                "frameRate": 30,
                "bitrateBps": 550000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 550000,
                "vbvFullnessBits": 495000,
                "entropyCoder": "cabac",
                "bFrameCount": 3,
                "aqStrength": 1,
                "profile": "high",
                "preset": "veryfast"
              }
            },
            "key": "video-stream0"
          },
          {
            "videoStream": {
              "h264": {
                "widthPixels": 1280,
                "heightPixels": 720,
                "frameRate": 30,
                "bitrateBps": 2500000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 2500000,
                "vbvFullnessBits": 2250000,
                "entropyCoder": "cabac",
                "bFrameCount": 3,
                "aqStrength": 1,
                "profile": "high",
                "preset": "veryfast"
              }
            },
            "key": "video-stream1"
          },
          {
            "audioStream": {
              "codec": "aac",
              "bitrateBps": 64000,
              "channelCount": 2,
              "channelLayout": [
                "fl",
                "fr"
              ],
              "sampleRateHertz": 48000
            },
            "key": "audio-stream0"
          }
        ],
        "muxStreams": [
          {
            "key": "sd",
            "fileName": "sd.mp4",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "hd",
            "fileName": "hd.mp4",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream1",
              "audio-stream0"
            ]
          },
          {
            "key": "media-sd",
            "fileName": "media-sd.ts",
            "container": "ts",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "media-hd",
            "fileName": "media-hd.ts",
            "container": "ts",
            "elementaryStreams": [
              "video-stream1",
              "audio-stream0"
            ]
          },
          {
            "key": "video-only-sd",
            "fileName": "video-only-sd.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "video-only-hd",
            "fileName": "video-only-hd.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream1"
            ]
          },
          {
            "key": "audio-only",
            "fileName": "audio-only.m4s",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ]
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "type": "HLS",
            "muxStreams": [
              "media-sd",
              "media-hd"
            ]
          },
          {
            "fileName": "manifest.mpd",
            "type": "DASH",
            "muxStreams": [
              "video-only-sd",
              "video-only-hd",
              "audio-only"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        }
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
    
    public class CreateJobFromPresetBatchModeSample
    {
        public Job CreateJobFromPresetBatchMode(
            string projectId, string location, string inputUri, string outputUri, string preset)
        {
            // Create the client.
            [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html) client = [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_Create)();
    
            // Build the parent location name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, location);
    
            // Build the job.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) newJob = new [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html)
            {
                InputUri = inputUri,
                OutputUri = outputUri,
                TemplateId = preset,
                Mode = [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.Types.html).[ProcessingMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.Types.ProcessingMode.html).[Batch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.Types.ProcessingMode.html#Google_Cloud_Video_Transcoder_V1_Job_Types_ProcessingMode_Batch),
                BatchModePriority = 10
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
    
    	transcoder "cloud.google.com/go/video/transcoder/apiv1"
    	"cloud.google.com/go/video/transcoder/apiv1/transcoderpb"
    )
    
    // createJobFromPresetBatchMode creates a batch mode job based on a given preset
    // template. See
    // https://cloud.google.com/transcoder/docs/how-to/create-batch-jobs
    // for more information.
    func createJobFromPresetBatchMode(w io.Writer, projectID string, location string, inputURI string, outputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://my-bucket/my-video-file"
    	// outputURI := "gs://my-bucket/my-output-folder/"
    	preset := "preset/web-hd"
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
    			JobConfig: &transcoderpb.Job_TemplateId{
    				TemplateId: preset,
    			},
    			Mode:              transcoderpb.[Job_PROCESSING_MODE_BATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1/transcoderpb.html#cloud_google_com_go_video_transcoder_apiv1_transcoderpb_Job_PROCESSING_MODE_UNSPECIFIED_Job_PROCESSING_MODE_INTERACTIVE_Job_PROCESSING_MODE_BATCH),
    			BatchModePriority: 10,
    		},
    	}
    	// Creates the job, Jobs take a variable amount of time to run.
    	// You can query for the job state.
    	response, err := client.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("createJobFromPresetBatchMode: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html).[ProcessingMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.ProcessingMode.html);
    import com.google.cloud.video.transcoder.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import java.io.IOException;
    
    public class CreateJobFromPresetBatchMode {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputUri = "gs://my-bucket/my-video-file";
        String outputUri = "gs://my-bucket/my-output-folder/";
        // See https://cloud.google.com/transcoder/docs/concepts/overview#job_template
        // for information on this preset.
        String preset = "preset/web-hd";
    
        createJobFromPresetBatchMode(projectId, location, inputUri, outputUri, preset);
      }
    
      // Creates a job from a preset in batch mode.
      public static void createJobFromPresetBatchMode(
          String projectId, String location, String inputUri, String outputUri, String preset)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html) transcoderServiceClient = [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).create()) {
    
          [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html) createJobRequest =
              [CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html).newBuilder()
                  .setJob(
                      [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html).newBuilder()
                          .[setInputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setInputUri_java_lang_String_)(inputUri)
                          .[setOutputUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setOutputUri_java_lang_String_)(outputUri)
                          .[setTemplateId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setTemplateId_java_lang_String_)(preset)
                          .setMode([ProcessingMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.ProcessingMode.html).PROCESSING_MODE_BATCH)
                          .[setBatchModePriority](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setBatchModePriority_int_)(10)
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
    // outputUri = 'gs://my-bucket/my-output-folder/';
    // preset = 'preset/web-hd';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function createJobFromPresetBatchMode() {
      // Construct request
      const request = {
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
        job: {
          inputUri: inputUri,
          outputUri: outputUri,
          templateId: preset,
          mode: '[PROCESSING_MODE_BATCH](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.job.processingmode.html)',
          batchModePriority: 10,
        },
      };
    
      // Run request
      const [response] = await transcoderServiceClient.createJob(request);
      console.log(`Job: ${response.name}`);
    }
    
    createJobFromPresetBatchMode();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\CreateJobRequest;
    use Google\Cloud\Video\Transcoder\V1\Job;
    
    /**
     * Creates a job in batch mode based on a job preset.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $inputUri Uri of the video in the Cloud Storage bucket.
     * @param string $outputUri Uri of the video output folder in the Cloud Storage bucket.
     * @param string $preset The preset template (for example, "preset/web-hd").
     */
    function create_job_from_preset_batch_mode($projectId, $location, $inputUri, $outputUri, $preset)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedParent = $transcoderServiceClient->locationName($projectId, $location);
        $job = new Job();
        $job->setInputUri($inputUri);
        $job->setOutputUri($outputUri);
        $job->setTemplateId($preset);
        $job->setMode(Job\ProcessingMode::PROCESSING_MODE_BATCH);
        $job->setBatchModePriority(10);
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
    
    
    def create_job_from_preset_batch_mode(
        project_id: str,
        location: str,
        input_uri: str,
        output_uri: str,
        preset: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job in batch mode based on a job preset.
    
        Args:
            project_id: The GCP project ID.
            location: The location to start the job in.
            input_uri: Uri of the video in the Cloud Storage bucket.
            output_uri: Uri of the video output folder in the Cloud Storage bucket.
            preset: The preset template (for example, 'preset/web-hd').
    
        Returns:
            The job resource.
        """
    
        client = TranscoderServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        job = transcoder_v1.types.Job()
        job.input_uri = input_uri
        job.output_uri = output_uri
        job.template_id = preset
        job.mode = transcoder_v1.types.Job.ProcessingMode.PROCESSING_MODE_BATCH
        job.batch_mode_priority = 10
    
        response = client.create_job(parent=parent, job=job)
        print(f"Job: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location    = "YOUR-JOB-LOCATION"  # (e.g. "us-central1")
    # input_uri   = "YOUR-GCS-INPUT-VIDEO"  # (e.g. "gs://my-bucket/my-video-file")
    # output_uri  = "YOUR-GCS-OUTPUT-FOLDER/"  # (e.g. "gs://my-bucket/my-output-folder/")
    # preset      = "YOUR-JOB-PRESET"  # (e.g. "preset/web-hd")
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the parent.
    parent = client.location_path project: project_id, location: location
    
    # Set the job fields.
    new_job = {
      input_uri: input_uri,
      output_uri: output_uri,
      template_id: preset,
      mode: Google::Cloud::Video::Transcoder::V1::Job::ProcessingMode::PROCESSING_MODE_BATCH,
      batch_mode_priority: 10
    }
    
    job = client.create_job parent: parent, job: new_job
    
    # Print the job name.
    puts "Job: #{job.name}"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
