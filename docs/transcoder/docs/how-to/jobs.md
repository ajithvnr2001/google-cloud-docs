---
url: https://docs.cloud.google.com/transcoder/docs/how-to/jobs/
title: Creating and managing jobs \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:35.774135+00:00
---

# Creating and managing jobs  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Creating and managing jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create and manage Transcoder API jobs.

A job represents the basic unit for managing work with the Transcoder API. When you submit a job to the Transcoder API, you specify the geographic location it should be processed in. You can list all jobs in a region.

To learn more about working with jobs and related Google Cloud resources across geographic regions, see [Regions](https://docs.cloud.google.com/transcoder/docs/locations).

## Set up your Google Cloud project and authentication

If you have not created a [Google Cloud project](https://docs.cloud.google.com/docs/overview#projects) and credentials, see [Before you begin](https://docs.cloud.google.com/transcoder/docs/how-to/before-you-begin). 

## Creating jobs

You can create jobs using either a preset job template or a custom job template you have created. To learn how to create a job template, see [Creating and managing job templates](https://docs.cloud.google.com/transcoder/docs/how-to/job-templates). Instead of using a template, you can also create a job and directly send the configuration of the job in the request.

The Transcoder API supports two [job modes](https://docs.cloud.google.com/transcoder/docs/concepts/overview#job_mode): interactive and batch. The following sections describe how to start a job in interactive mode. To start a job in batch mode, you must set an additional field (see more information on [batch jobs](https://docs.cloud.google.com/transcoder/docs/how-to/create-batch-jobs)).

**Note:** Jobs will be automatically deleted within 30 days of completion (by default). To change this time, set the [ `ttlAfterCompletionDays`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.ttl_after_completion_days) field in the `Job` resource.

### Creating jobs based on presets

To create a job, use the [`projects.locations.jobs.create`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/create) method. The job transcodes a media file that is stored as an object in Cloud Storage.

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
      "templateId": "preset/web-hd"
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
      "templateId": "preset/web-hd"
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
      --template-id="preset/web-hd"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create `
      --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" `
      --location=LOCATION `
      --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" `
      --template-id="preset/web-hd"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create ^
      --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" ^
      --location=LOCATION ^
      --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" ^
      --template-id="preset/web-hd"

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
    
    public class CreateJobFromPresetSample
    {
        public Job CreateJobFromPreset(
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
                TemplateId = preset
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
    
    // createJobFromPreset creates a job based on a given preset template. See
    // https://cloud.google.com/transcoder/docs/how-to/jobs#create_jobs_presets
    // for more information.
    func createJobFromPreset(w io.Writer, projectID string, location string, inputURI string, outputURI string) error {
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
    		},
    	}
    	// Creates the job, Jobs take a variable amount of time to run.
    	// You can query for the job state.
    	response, err := client.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("createJobFromPreset: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import java.io.IOException;
    
    public class CreateJobFromPreset {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputUri = "gs://my-bucket/my-video-file";
        String outputUri = "gs://my-bucket/my-output-folder/";
        // See https://cloud.google.com/transcoder/docs/concepts/overview#job_template
        // for information on this preset.
        String preset = "preset/web-hd";
    
        createJobFromPreset(projectId, location, inputUri, outputUri, preset);
      }
    
      // Creates a job from a preset.
      public static void createJobFromPreset(
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
    
    async function createJobFromPreset() {
      // Construct request
      const request = {
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
        job: {
          inputUri: inputUri,
          outputUri: outputUri,
          templateId: preset,
        },
      };
    
      // Run request
      const [response] = await transcoderServiceClient.createJob(request);
      console.log(`Job: ${response.name}`);
    }
    
    createJobFromPreset();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\CreateJobRequest;
    use Google\Cloud\Video\Transcoder\V1\Job;
    
    /**
     * Creates a job based on a job preset.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $inputUri Uri of the video in the Cloud Storage bucket.
     * @param string $outputUri Uri of the video output folder in the Cloud Storage bucket.
     * @param string $preset The preset template (for example, "preset/web-hd").
     */
    function create_job_from_preset($projectId, $location, $inputUri, $outputUri, $preset)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedParent = $transcoderServiceClient->locationName($projectId, $location);
        $job = new Job();
        $job->setInputUri($inputUri);
        $job->setOutputUri($outputUri);
        $job->setTemplateId($preset);
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
    
    
    def create_job_from_preset(
        project_id: str,
        location: str,
        input_uri: str,
        output_uri: str,
        preset: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job based on a job preset.
    
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
      template_id: preset
    }
    
    job = client.create_job parent: parent, job: new_job
    
    # Print the job name.
    puts "Job: #{job.name}"

### Creating jobs based on job templates

If you've created at least one job template in a location, you can specify a job template when sending a request to create a Transcoder API job in that location.

To create a job, use the [`projects.locations.jobs.create`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/create) method.

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
  * `STORAGE_OUTPUT_FOLDER`: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.
  * `TEMPLATE_ID`: The ID of the job template you created. If you don't specify a custom job template, the Transcoder API uses the `preset/web-hd` job template.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "inputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO",
      "outputUri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/",
      "templateId": "TEMPLATE_ID"
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
      "templateId": "TEMPLATE_ID"
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
                "frameRate": 60,
                "bitrateBps": 550000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 550000,
                "vbvFullnessBits": 495000,
                "entropyCoder": "cabac",
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
                "frameRate": 60,
                "bitrateBps": 2500000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 2500000,
                "vbvFullnessBits": 2250000,
                "entropyCoder": "cabac",
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

  1. Make the following replacements for the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create) command: 
     * STORAGE_BUCKET_NAME: The name of the Cloud Storage bucket you created. 
     * STORAGE_INPUT_VIDEO: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
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
     * STORAGE_OUTPUT_FOLDER: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.
     * TEMPLATE_ID: The ID of the job template you created. If you don't specify a custom job template, the Transcoder API uses the `preset/web-hd` job template. 
  2. Run the following command: 
         
         gcloud transcoder jobs create \
           --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" \
           --location=LOCATION \
           --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" \
           --template-id="TEMPLATE_ID"

You should see a response similar to the following: 
         
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
                     "frameRate": 60,
                     "bitrateBps": 550000,
                     "pixelFormat": "yuv420p",
                     "rateControlMode": "vbr",
                     "crfLevel": 21,
                     "gopDuration": "3s",
                     "vbvSizeBits": 550000,
                     "vbvFullnessBits": 495000,
                     "entropyCoder": "cabac",
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
                     "frameRate": 60,
                     "bitrateBps": 2500000,
                     "pixelFormat": "yuv420p",
                     "rateControlMode": "vbr",
                     "crfLevel": 21,
                     "gopDuration": "3s",
                     "vbvSizeBits": 2500000,
                     "vbvFullnessBits": 2250000,
                     "entropyCoder": "cabac",
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
    
    public class CreateJobFromTemplateSample
    {
        public Job CreateJobFromTemplate(
            string projectId, string location, string inputUri, string outputUri, string templateId)
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
                TemplateId = templateId
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
    
    // createJobFromTemplate creates a job from a template. See
    // https://cloud.google.com/transcoder/docs/how-to/jobs#create_jobs_templates
    // for more information.
    func createJobFromTemplate(w io.Writer, projectID string, location string, inputURI string, outputURI string, templateID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://my-bucket/my-video-file"
    	// outputURI := "gs://my-bucket/my-output-folder/"
    	// templateID := "my-job-template"
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
    				TemplateId: templateID,
    			},
    		},
    	}
    	// Creates the job, Jobs take a variable amount of time to run.
    	// You can query for the job state.
    	response, err := client.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("createJobFromTemplate: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.CreateJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import java.io.IOException;
    
    public class CreateJobFromTemplate {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputUri = "gs://my-bucket/my-video-file";
        String outputUri = "gs://my-bucket/my-output-folder/";
        String templateId = "my-job-template";
    
        createJobFromTemplate(projectId, location, inputUri, outputUri, templateId);
      }
    
      // Creates a job from a job template.
      public static void createJobFromTemplate(
          String projectId, String location, String inputUri, String outputUri, String templateId)
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
                          .[setTemplateId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.Builder.html#com_google_cloud_video_transcoder_v1_Job_Builder_setTemplateId_java_lang_String_)(templateId)
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
    // templateId = 'my-job-template';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function createJobFromTemplate() {
      // Construct request
      const request = {
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
        job: {
          inputUri: inputUri,
          outputUri: outputUri,
          templateId: templateId,
        },
      };
    
      // Run request
      const [response] = await transcoderServiceClient.createJob(request);
      console.log(`Job: ${response.name}`);
    }
    
    createJobFromTemplate();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\CreateJobRequest;
    use Google\Cloud\Video\Transcoder\V1\Job;
    
    /**
     * Creates a job based on a job template.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $inputUri Uri of the video in the Cloud Storage bucket.
     * @param string $outputUri Uri of the video output folder in the Cloud Storage bucket.
     * @param string $templateId The job template ID.
     */
    function create_job_from_template($projectId, $location, $inputUri, $outputUri, $templateId)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedParent = $transcoderServiceClient->locationName($projectId, $location);
        $job = new Job();
        $job->setInputUri($inputUri);
        $job->setOutputUri($outputUri);
        $job->setTemplateId($templateId);
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
    
    
    def create_job_from_template(
        project_id: str,
        location: str,
        input_uri: str,
        output_uri: str,
        template_id: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job based on a job template.
    
        Args:
            project_id: The GCP project ID.
            location: The location to start the job in.
            input_uri: Uri of the video in the Cloud Storage bucket.
            output_uri: Uri of the video output folder in the Cloud Storage bucket.
            template_id: The user-defined template ID.
    
        Returns:
            The job resource.
        """
    
        client = TranscoderServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        job = transcoder_v1.types.Job()
        job.input_uri = input_uri
        job.output_uri = output_uri
        job.template_id = template_id
    
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
    # template_id = "YOUR-JOB-TEMPLATE"  # (e.g. "my-job-template")
    
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
      template_id: template_id
    }
    
    job = client.create_job parent: parent, job: new_job
    
    # Print the job name.
    puts "Job: #{job.name}"

The response is similar to the response returned when creating a job using the default template.

### Creating jobs with ad-hoc configurations

You can send an ad-hoc configuration for a job with the request to create the job.

To create a job, use the [`projects.locations.jobs.create`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/create) method.

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
            "key": "video-stream1",
            "videoStream": {
              "h264": {
                "heightPixels": 720,
                "widthPixels": 1280,
                "bitrateBps": 2500000,
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
          },
          {
            "key": "hd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream1",
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
            "key": "video-stream1",
            "videoStream": {
              "h264": {
                "heightPixels": 720,
                "widthPixels": 1280,
                "bitrateBps": 2500000,
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
          },
          {
            "key": "hd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream1",
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
                "frameRate": 60,
                "bitrateBps": 550000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 550000,
                "vbvFullnessBits": 495000,
                "entropyCoder": "cabac",
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
                "frameRate": 60,
                "bitrateBps": 2500000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 2500000,
                "vbvFullnessBits": 2250000,
                "entropyCoder": "cabac",
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
  * `STORAGE_INPUT_VIDEO`: The name of the video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
  * `STORAGE_OUTPUT_FOLDER`: The Cloud Storage folder name where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



Save the following content in a file called `request.json`: 
    
    
    {
      "config": {
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
            "key": "video-stream1",
            "videoStream": {
              "h264": {
                "heightPixels": 720,
                "widthPixels": 1280,
                "bitrateBps": 2500000,
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
          },
          {
            "key": "hd",
            "container": "mp4",
            "elementaryStreams": [
              "video-stream1",
              "audio-stream0"
            ]
          }
        ]
      }
    }

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create \
      --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" \
      --location=LOCATION \
      --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" \
      --file="request.json"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create `
      --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" `
      --location=LOCATION `
      --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" `
      --file="request.json"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create ^
      --input-uri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO" ^
      --location=LOCATION ^
      --output-uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/" ^
      --file="request.json"

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
                "frameRate": 60,
                "bitrateBps": 550000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 550000,
                "vbvFullnessBits": 495000,
                "entropyCoder": "cabac",
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
                "frameRate": 60,
                "bitrateBps": 2500000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 2500000,
                "vbvFullnessBits": 2250000,
                "entropyCoder": "cabac",
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
    
    public class CreateJobFromAdHocSample
    {
        public Job CreateJobFromAdHoc(
            string projectId, string location, string inputUri, string outputUri)
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
    
            [VideoStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.VideoStream.html) videoStream1 = new [VideoStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.VideoStream.html)
            {
                H264 = new VideoStream.Types.H264CodecSettings
                {
                    BitrateBps = 2500000,
                    FrameRate = 60,
                    HeightPixels = 720,
                    WidthPixels = 1280
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
                Key = "video_stream1",
                VideoStream = videoStream1
            };
    
            [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html) elementaryStream2 = new [ElementaryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.ElementaryStream.html)
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
    
            [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.MuxStream.html) muxStream1 = new [MuxStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.MuxStream.html)
            {
                Key = "hd",
                Container = "mp4",
                ElementaryStreams = { "video_stream1", "audio_stream0" }
    
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
                ElementaryStreams = { elementaryStream0, elementaryStream1, elementaryStream2 },
                MuxStreams = { muxStream0, muxStream1 }
            };
    
            // Build the job.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) newJob = new [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html)
            {
                Config = jobConfig,
                InputUri = inputUri,
                OutputUri = outputUri
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
    
    // createJobFromAdHoc creates a job based on a given configuration. See
    // https://cloud.google.com/transcoder/docs/how-to/jobs#create_jobs_ad_hoc
    // for more information.
    func createJobFromAdHoc(w io.Writer, projectID string, location string, inputURI string, outputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputURI := "gs://my-bucket/my-video-file"
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
    							Key: "video_stream1",
    							ElementaryStream: &transcoderpb.ElementaryStream_VideoStream{
    								VideoStream: &transcoderpb.VideoStream{
    									CodecSettings: &transcoderpb.VideoStream_H264{
    										H264: &transcoderpb.VideoStream_H264CodecSettings{
    											BitrateBps:   2500000,
    											FrameRate:    60,
    											HeightPixels: 720,
    											WidthPixels:  1280,
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
    						{
    							Key:               "hd",
    							Container:         "mp4",
    							ElementaryStreams: []string{"video_stream1", "audio_stream0"},
    						},
    					},
    				},
    			},
    		},
    	}
    	// Creates the job, Jobs take a variable amount of time to run.
    	// You can query for the job state.
    	response, err := client.CreateJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("createJobFromAdHoc: %w", err)
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
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import com.google.cloud.video.transcoder.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html);
    import com.google.cloud.video.transcoder.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html).[H264CodecSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings.html);
    import java.io.IOException;
    
    public class CreateJobFromAdHoc {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputUri = "gs://my-bucket/my-video-file";
        String outputUri = "gs://my-bucket/my-output-folder/";
    
        createJobFromAdHoc(projectId, location, inputUri, outputUri);
      }
    
      // Creates a job from an ad-hoc configuration.
      public static void createJobFromAdHoc(
          String projectId, String location, String inputUri, String outputUri) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html) transcoderServiceClient = [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).create()) {
    
          [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html) videoStream0 =
              [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html).newBuilder()
                  .[setH264](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Builder.html#com_google_cloud_video_transcoder_v1_VideoStream_Builder_setH264_com_google_cloud_video_transcoder_v1_VideoStream_H264CodecSettings_)(
                      [H264CodecSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings.html).newBuilder()
                          .setBitrateBps(550000)
                          .setFrameRate(60)
                          .setHeightPixels(360)
                          .setWidthPixels(640))
                  .build();
    
          [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html) videoStream1 =
              [VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html).newBuilder()
                  .[setH264](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.Builder.html#com_google_cloud_video_transcoder_v1_VideoStream_Builder_setH264_com_google_cloud_video_transcoder_v1_VideoStream_H264CodecSettings_)(
                      [H264CodecSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.H264CodecSettings.html).newBuilder()
                          .setBitrateBps(2500000)
                          .setFrameRate(60)
                          .setHeightPixels(720)
                          .setWidthPixels(1280))
                  .build();
    
          [AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.AudioStream.html) audioStream0 =
              [AudioStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.AudioStream.html).newBuilder().setCodec("aac").setBitrateBps(64000).build();
    
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
                          .setKey("video_stream1")
                          .[setVideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setVideoStream_com_google_cloud_video_transcoder_v1_VideoStream_)(videoStream1))
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
                  .addMuxStreams(
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("hd")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("mp4")
                          .addElementaryStreams("video_stream1")
                          .addElementaryStreams("audio_stream0")
                          .build())
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
    // outputUri = 'gs://my-bucket/my-output-folder/';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function createJobFromAdHoc() {
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
                key: 'video-stream1',
                videoStream: {
                  h264: {
                    heightPixels: 720,
                    widthPixels: 1280,
                    bitrateBps: 2500000,
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
              {
                key: 'hd',
                container: 'mp4',
                elementaryStreams: ['video-stream1', 'audio-stream0'],
              },
            ],
          },
        },
      };
    
      // Run request
      const [response] = await transcoderServiceClient.createJob(request);
      console.log(`Job: ${response.name}`);
    }
    
    createJobFromAdHoc();

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
    use Google\Cloud\Video\Transcoder\V1\VideoStream;
    
    /**
     * Creates a job based on an ad-hoc job configuration.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $inputUri Uri of the video in the Cloud Storage bucket.
     * @param string $outputUri Uri of the video output folder in the Cloud Storage bucket.
     */
    function create_job_from_ad_hoc($projectId, $location, $inputUri, $outputUri)
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
                    ->setKey('video-stream1')
                    ->setVideoStream(
                        (new VideoStream())
                            ->setH264(
                                (new VideoStream\H264CodecSettings())
                                    ->setBitrateBps(2500000)
                                    ->setFrameRate(60)
                                    ->setHeightPixels(720)
                                    ->setWidthPixels(1280)
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
                        ->setElementaryStreams(['video-stream0', 'audio-stream0']),
                    (new MuxStream())
                        ->setKey('hd')
                        ->setContainer('mp4')
                        ->setElementaryStreams(['video-stream1', 'audio-stream0'])
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
    
    
    def create_job_from_ad_hoc(
        project_id: str,
        location: str,
        input_uri: str,
        output_uri: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job based on an ad-hoc job configuration.
    
        Args:
            project_id: The GCP project ID.
            location: The location to start the job in.
            input_uri: Uri of the video in the Cloud Storage bucket.
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
                    key="video-stream1",
                    video_stream=transcoder_v1.types.VideoStream(
                        h264=transcoder_v1.types.VideoStream.H264CodecSettings(
                            height_pixels=720,
                            width_pixels=1280,
                            bitrate_bps=2500000,
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
                transcoder_v1.types.MuxStream(
                    key="hd",
                    container="mp4",
                    elementary_streams=["video-stream1", "audio-stream0"],
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
            key: "video-stream1",
            video_stream: {
              h264: {
                height_pixels: 720,
                width_pixels: 1280,
                bitrate_bps: 2_500_000,
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
          },
          {
            key: "hd",
            container: "mp4",
            elementary_streams: [
              "video-stream1",
              "audio-stream0"
            ]
          }
        ]
      }
    }
    
    job = client.create_job parent: parent, job: new_job
    
    # Print the job name.
    puts "Job: #{job.name}"

## Getting job details

To check the details or status of a job, use the [`projects.locations.jobs.get`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/get) method.

### REST

Before using any of the request data, make the following replacements: 

* `JOB_ID`: The ID of the job you created.
* `PROJECT_ID`: Your Google Cloud project ID.
* `LOCATION`: The location of your job. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

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



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_ID" | Select-Object -Expand Content

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
                "frameRate": 60,
                "bitrateBps": 550000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 550000,
                "vbvFullnessBits": 495000,
                "entropyCoder": "cabac",
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
                "frameRate": 60,
                "bitrateBps": 2500000,
                "pixelFormat": "yuv420p",
                "rateControlMode": "vbr",
                "crfLevel": 21,
                "gopDuration": "3s",
                "vbvSizeBits": 2500000,
                "vbvFullnessBits": 2250000,
                "entropyCoder": "cabac",
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

  1. Make the following replacements for the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/transcoder/jobs/describe) command: 
     * JOB_ID: The ID of the job you created. 
     * LOCATION: The location of your job. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

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
  2. Run the following command: 
         
         gcloud transcoder jobs describe JOB_ID --location=LOCATION

You should see a response similar to the following: 
         
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
                     "frameRate": 60,
                     "bitrateBps": 550000,
                     "pixelFormat": "yuv420p",
                     "rateControlMode": "vbr",
                     "crfLevel": 21,
                     "gopDuration": "3s",
                     "vbvSizeBits": 550000,
                     "vbvFullnessBits": 495000,
                     "entropyCoder": "cabac",
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
                     "frameRate": 60,
                     "bitrateBps": 2500000,
                     "pixelFormat": "yuv420p",
                     "rateControlMode": "vbr",
                     "crfLevel": 21,
                     "gopDuration": "3s",
                     "vbvSizeBits": 2500000,
                     "vbvFullnessBits": 2250000,
                     "entropyCoder": "cabac",
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
    
    
    using [Google.Cloud.Video.Transcoder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.html);
    
    public class GetJobSample
    {
        public Job GetJob(string projectId, string location, string jobId)
        {
            // Create the client.
            [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html) client = [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_Create)();
    
            // Build the job name.
            [JobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html) jobName = [JobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html).[FromProjectLocationJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html#Google_Cloud_Video_Transcoder_V1_JobName_FromProjectLocationJob_System_String_System_String_System_String_)(projectId, location, jobId);
    
            // Call the API.
            [Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.Job.html) job = client.[GetJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_GetJob_Google_Cloud_Video_Transcoder_V1_GetJobRequest_Google_Api_Gax_Grpc_CallSettings_)(jobName);
    
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
    
    // getJob gets a previously-created job. See https://cloud.google.com/transcoder/docs/how-to/jobs#check_job_status
    // for more information.
    func getJob(w io.Writer, projectID string, location string, jobID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// jobID := "my-job-id"
    	ctx := context.Background()
    	client, err := transcoder.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_Close)()
    
    	req := &transcoderpb.GetJobRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/jobs/%s", projectID, location, jobID),
    	}
    
    	response, err := client.GetJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetJob: %w", err)
    	}
    
    	fmt.Fprintf(w, "Job: %v", response)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.GetJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import java.io.IOException;
    
    public class GetJob {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String jobId = "my-job-id";
    
        getJob(projectId, location, jobId);
      }
    
      // Gets a job.
      public static void getJob(String projectId, String location, String jobId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html) transcoderServiceClient = [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).create()) {
          [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html) jobName =
              [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html).newBuilder().setProject(projectId).setLocation(location).setJob(jobId).build();
          [GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.GetJobRequest.html) getJobRequest = [GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.GetJobRequest.html).newBuilder().setName(jobName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html#com_google_cloud_video_transcoder_v1_JobName_toString__)()).build();
    
          // Send the get job request and process the response.
          [Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html) job = transcoderServiceClient.getJob(getJobRequest);
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
    // jobId = 'my-job-id';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function getJob() {
      // Construct request
      const request = {
        name: transcoderServiceClient.[jobPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location, jobId),
      };
      const [response] = await transcoderServiceClient.getJob(request);
      console.log(`Job: ${response.name}`);
    }
    
    getJob();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\GetJobRequest;
    
    /**
     * Gets a Transcoder job.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $jobId The job ID.
     */
    function get_job($projectId, $location, $jobId)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedName = $transcoderServiceClient->jobName($projectId, $location, $jobId);
        $request = (new GetJobRequest())
            ->setName($formattedName);
        $job = $transcoderServiceClient->getJob($request);
    
        // Print job name.
        printf('Job: %s' . PHP_EOL, $job->getName());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import transcoder_v1
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        TranscoderServiceClient,
    )
    
    
    def get_job(
        project_id: str,
        location: str,
        job_id: str,
    ) -> transcoder_v1.types.resources.Job:
        """Gets a job.
    
        Args:
            project_id: The GCP project ID.
            location: The location this job is in.
            job_id: The job ID.
    
        Returns:
            The job resource.
        """
    
        client = TranscoderServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/jobs/{job_id}"
        response = client.get_job(name=name)
        print(f"Job: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location   = "YOUR-JOB-LOCATION"  # (e.g. "us-central1")
    # job_id     = "YOUR-JOB-ID"  # (e.g. "c82c295b-3f5a-47df-8562-938a89d40fd0")
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the job.
    name = client.job_path project: project_id, location: location, job: job_id
    
    # Get the job.
    job = client.get_job name: name
    
    # Print the job name.
    puts "Job: #{job.name}"

The response is similar to the response returned when creating a job.

## Listing jobs

If you want to review all the jobs you created in a location, use the [`projects.locations.jobs.list`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/list) method.

### REST

Before using any of the request data, make the following replacements: 

* `PROJECT_ID`: Your Google Cloud project ID.
* `LOCATION`: The location of your jobs. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

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



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "jobs": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/MY_JOB",
          "config": {
            ....
           },
          "state": "PENDING",
          "createTime": CREATE_TIME,
          "ttlAfterCompletionDays": 30
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/MY_OTHER_JOB",
          "config": {
            ....
           },
          "state": "SUCCEEDED",
          "createTime": CREATE_TIME,
          "startTime": START_TIME,
          "endTime": END_TIME,
          "ttlAfterCompletionDays": 30
        }
      ]
    }
    

### gcloud

  1. Make the following replacements for the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/transcoder/jobs/list) command: 
     * LOCATION: The location of your job(s). Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

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
  2. Run the following command: 
         
         gcloud transcoder jobs list --location=LOCATION

You should see a response similar to the following: 
         
         NAME                                                    STATE      FAILURE_REASON
         projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID  SUCCEEDED
         projects/PROJECT_NUMBER/locations/LOCATION/jobs/abc123  SUCCEEDED
         




### C#

Before trying this sample, follow the C# setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Transcoder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using System.Linq;
    using System.Collections.Generic;
    
    public class ListJobsSample
    {
        public IList<Job> ListJobs(string projectId, string location)
        {
            // Create the client.
            [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html) client = [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_Create)();
    
            // Build the parent location name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parentLocation = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, location);
    
            // Call the API.
            PagedEnumerable<ListJobsResponse, Job> response = client.[ListJobs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_ListJobs_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(parentLocation);
    
            // The returned sequence will lazily perform RPCs as it's being iterated over.
            return response.ToList();
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/transcoder). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"google.golang.org/api/iterator"
    
    	transcoder "cloud.google.com/go/video/transcoder/apiv1"
    	"cloud.google.com/go/video/transcoder/apiv1/transcoderpb"
    )
    
    // listJobs lists all jobs for a given location. See
    // https://cloud.google.com/transcoder/docs/how-to/jobs#list_jobs for more
    // information.
    func listJobs(w io.Writer, projectID string, location string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	ctx := context.Background()
    	client, err := transcoder.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_Close)()
    
    	req := &transcoderpb.ListJobsRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    	}
    
    	it := client.ListJobs(ctx, req)
    	fmt.Fprintln(w, "Jobs:")
    
    	for {
    		response, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListJobs: %w", err)
    		}
    		fmt.Fprintln(w, response.GetName())
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html);
    import com.google.cloud.video.transcoder.v1.[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ListJobsRequest.html);
    import com.google.cloud.video.transcoder.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import java.io.IOException;
    
    public class ListJobs {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
    
        listJobs(projectId, location);
      }
    
      // Lists the jobs for a given location.
      public static void listJobs(String projectId, String location) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html) transcoderServiceClient = [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).create()) {
    
          [ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ListJobsRequest.html) listJobsRequest =
              [ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ListJobsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.LocationName.html).of(projectId, location).toString())
                  .build();
    
          // Send the list jobs request and process the response.
          [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).[ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.ListJobsPagedResponse.html) response =
              transcoderServiceClient.listJobs(listJobsRequest);
          System.out.println("Jobs:");
    
          for ([Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Job.html) job : response.iterateAll()) {
            System.out.println(job.getName());
          }
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
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function listJobs() {
      const iterable = await transcoderServiceClient.[listJobsAsync](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)({
        parent: transcoderServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location),
      });
      console.info('Jobs:');
      for await (const response of iterable) {
        console.log(response.name);
      }
    }
    
    listJobs();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\ListJobsRequest;
    
    /**
     * Lists all Transcoder jobs in a location.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the jobs.
     */
    function list_jobs($projectId, $location)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedParent = $transcoderServiceClient->locationName($projectId, $location);
        $request = (new ListJobsRequest())
            ->setParent($formattedParent);
        $response = $transcoderServiceClient->listJobs($request);
    
        // Print job list.
        $jobs = $response->iterateAllElements();
        print('Jobs:' . PHP_EOL);
        foreach ($jobs as $job) {
            printf('%s' . PHP_EOL, $job->getName());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        pagers,
        TranscoderServiceClient,
    )
    
    
    def list_jobs(
        project_id: str,
        location: str,
    ) -> pagers.ListJobsPager:
        """Lists all jobs in a location.
    
        Args:
            project_id: The GCP project ID.
            location: The location of the jobs.
    
        Returns:
            An iterable object containing job resources.
        """
    
        client = TranscoderServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
        response = client.list_jobs(parent=parent)
        print("Jobs:")
        for job in response.jobs:
            print({job.name})
    
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location   = "YOUR-JOB-LOCATION"  # (e.g. "us-central1")
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the parent.
    parent = client.location_path project: project_id, location: location
    
    # Get the list of jobs.
    response = client.list_jobs parent: parent
    
    puts "Jobs:"
    # Print out all jobs.
    response.each do |job|
      puts job.name
    end

### Additional results

The list jobs response may include a `nextPageToken`, which you can use to retrieve additional results:
    
    
    {
      "jobs": [
        ...
      ],
      "nextPageToken": "NEXT_PAGE_TOKEN"
    }
    

In the following `curl` example, you can then send another request, and include the value of NEXT_PAGE_TOKEN to list additional jobs, similar to the following:
    
    
    curl -X GET \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs?pageToken=NEXT_PAGE_TOKEN
    

See the relevant [client library](https://docs.cloud.google.com/transcoder/docs/reference/libraries) for more information on using this token.

### Filtering results

You can filter the results of the list jobs method. For example, run the following `curl` command to list all active jobs:
    
    
    curl -X GET \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    **'** https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs**?filter=-state="FAILED"+AND+-state="SUCCEEDED"'**
    

This command uses the negation operator to list jobs that have not failed AND jobs that have not succeeded. The resulting list contains jobs that are running or pending (see [`ProcessingState`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#processingstate) for information on job states).

The following are some example filters:

  * `?filter=state="FAILED"+OR+state="SUCCEEDED"`: lists jobs that have completed
  * `?filter=createTime+>+"2021-06-09T19:25:21.007649960Z"`: lists jobs created after a certain timestamp
  * `?filter=inputUri="gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"`: lists jobs with a certain input URI
  * `?filter=config.output.uri="gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"`: lists jobs with a certain output URI



For more information, see [AIP-160 - Filtering](https://google.aip.dev/160).

## Deleting jobs

To delete a job, use the [`projects.locations.jobs.delete`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs/delete) method.

**Note:** Jobs will be automatically deleted within 30 days of completion (by default). To change this time, set the [ `ttlAfterCompletionDays`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.ttl_after_completion_days) field in the `Job` resource.

### REST

Before using any of the request data, make the following replacements: 

* `JOB_ID`: The ID of the job you created.
* `PROJECT_ID`: Your Google Cloud project ID.
* `LOCATION`: The location of your job. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

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



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://transcoder.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/jobs/JOB_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

### gcloud

  1. Make the following replacements for the [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/transcoder/jobs/delete) command: 
     * JOB_ID: The ID of the job you created. 
     * LOCATION: The location of your job. Use one of the [supported regions](https://docs.cloud.google.com/transcoder/docs/locations). 

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
  2. Run the following command: 
         
         gcloud transcoder jobs delete JOB_ID --location=LOCATION

You should see a response similar to the following: 
         
         Deleted job [projects/PROJECT_ID/locations/LOCATION/jobs/JOB_ID].
         




### C#

Before trying this sample, follow the C# setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Transcoder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.html);
    
    public class DeleteJobSample
    {
        public void DeleteJob(string projectId, string location, string jobId)
        {
            // Create the client.
            [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html) client = [TranscoderServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_Create)();
    
            // Build the job name.
            [JobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html) jobName = [JobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html).[FromProjectLocationJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.JobName.html#Google_Cloud_Video_Transcoder_V1_JobName_FromProjectLocationJob_System_String_System_String_System_String_)(projectId, location, jobId);
    
            // Call the API.
            client.[DeleteJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Transcoder.V1/latest/Google.Cloud.Video.Transcoder.V1.TranscoderServiceClient.html#Google_Cloud_Video_Transcoder_V1_TranscoderServiceClient_DeleteJob_Google_Cloud_Video_Transcoder_V1_DeleteJobRequest_Google_Api_Gax_Grpc_CallSettings_)(jobName);
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
    
    // deleteJob deletes a previously-created job. See
    // https://cloud.google.com/transcoder/docs/how-to/jobs#delete_jobs for more
    // information.
    func deleteJob(w io.Writer, projectID string, location string, jobID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// jobID := "my-job-id"
    	ctx := context.Background()
    	client, err := transcoder.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1.html#cloud_google_com_go_video_transcoder_apiv1_Client_Close)()
    
    	req := &transcoderpb.DeleteJobRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/jobs/%s", projectID, location, jobID),
    	}
    
    	err = client.DeleteJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("DeleteJob: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted job")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/overview). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.transcoder.v1.[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.DeleteJobRequest.html);
    import com.google.cloud.video.transcoder.v1.[JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import java.io.IOException;
    
    public class DeleteJob {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String jobId = "my-job-id";
    
        deleteJob(projectId, location, jobId);
      }
    
      // Deletes a job.
      public static void deleteJob(String projectId, String location, String jobId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html) transcoderServiceClient = [TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html).create()) {
          [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html) jobName =
              [JobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html).newBuilder().setProject(projectId).setLocation(location).setJob(jobId).build();
          [DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.DeleteJobRequest.html) deleteJobRequest = [DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.DeleteJobRequest.html).newBuilder().setName(jobName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobName.html#com_google_cloud_video_transcoder_v1_JobName_toString__)())
              .build();
    
          // Send the delete job request and process the response.
          transcoderServiceClient.deleteJob(deleteJobRequest);
          System.out.println("Deleted job");
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
    // jobId = 'my-job-id';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function deleteJob() {
      // Construct request
      const request = {
        name: transcoderServiceClient.[jobPath](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/v1.transcoderserviceclient.html)(projectId, location, jobId),
      };
      await transcoderServiceClient.deleteJob(request);
      console.log('Deleted job');
    }
    
    deleteJob();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/cloud-video-transcoder/latest/videotranscoder/readme). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Transcoder\V1\Client\TranscoderServiceClient;
    use Google\Cloud\Video\Transcoder\V1\DeleteJobRequest;
    
    /**
     * Deletes a Transcoder job.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     * @param string $location The location of the job.
     * @param string $jobId The job ID.
     */
    function delete_job($projectId, $location, $jobId)
    {
        // Instantiate a client.
        $transcoderServiceClient = new TranscoderServiceClient();
    
        $formattedName = $transcoderServiceClient->jobName($projectId, $location, $jobId);
        $request = (new DeleteJobRequest())
            ->setName($formattedName);
        $transcoderServiceClient->deleteJob($request);
    
        print('Deleted job' . PHP_EOL);
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        TranscoderServiceClient,
    )
    
    
    def delete_job(
        project_id: str,
        location: str,
        job_id: str,
    ) -> None:
        """Gets a job.
    
        Args:
            project_id: The GCP project ID.
            location: The location this job is in.
            job_id: The job ID."""
    
        client = TranscoderServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/jobs/{job_id}"
        response = client.delete_job(name=name)
        print("Deleted job")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location   = "YOUR-JOB-LOCATION"  # (e.g. "us-central1")
    # job_id     = "YOUR-JOB-ID"  # (e.g. "c82c295b-3f5a-47df-8562-938a89d40fd0")
    
    # Require the Transcoder client library.
    require "google/cloud/video/transcoder"
    
    # Create a Transcoder client.
    client = Google::Cloud::Video::Transcoder.transcoder_service
    
    # Build the resource name of the job.
    name = client.job_path project: project_id, location: location, job: job_id
    
    # Delete the job.
    client.delete_job name: name
    
    # Print a success message.
    puts "Deleted job"

## What's next

Learn about [Creating and managing job templates](https://docs.cloud.google.com/transcoder/docs/how-to/job-templates).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
