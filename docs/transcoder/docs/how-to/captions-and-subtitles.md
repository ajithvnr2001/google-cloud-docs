---
url: https://docs.cloud.google.com/transcoder/docs/how-to/captions-and-subtitles/
title: Adding closed captions and subtitles \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:15.871742+00:00
---

# Adding closed captions and subtitles  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/how-to/captions-and-subtitles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Adding closed captions and subtitles Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to add closed captions and subtitles to an output video.

_Closed captions_ (or just _captions_) are the visual display of the audio in a video. Closed captions are typically in the same language as the audio and include background sounds and speaker changes.

_Subtitles_ are typically used to translate the dialogue of a video into a different language. Subtitles usually do not include background sounds and speaker changes.

This page uses the term _input caption file_ to refer to a text file that contains closed captions or subtitles. You provide this file as an input to a job.

## Add captions and subtitles to a job configuration

Refer to the [supported inputs and outputs](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats) for the supported input caption file formats. A sample video file and sample input caption files are provided for you to test your configuration.

Use the information in the following sections to add captions and subtitles to a job configuration. This page assumes you are familiar with a basic [JobConfig](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig). For more information on creating transcoding jobs, see [Creating and managing jobs](https://docs.cloud.google.com/transcoder/docs/how-to/jobs).

### Add captions

To create a job that embeds captions in the output video file container, do the following:

  1. Add an [`inputs`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.inputs) array to the beginning of the job configuration.

  2. Add an [`Input`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#input) object to the `inputs` array that defines the key and URI for the associated input video.

  3. Add another [`Input`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#input) object that includes the path to the input caption file.

**Note:** Don't put blank lines between the text lines in the input caption file.
  4. Add an [`editList`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.edit_list) array to the job configuration. This array is used to add inputs to the output video timeline.

  5. Add an [`EditAtom`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#editatom) object to the `editList` array. This [`EditAtom`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#editatom) object must reference the keys for the input video and captions you added in the `inputs` array. You can designate a `startTimeOffset` and `endTimeOffset` to trim the input video.

  6. Add the captions to the output containers by adding a [`textStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#textstream) object to the [`elementaryStreams`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.elementary_streams) array. Only one embedded text stream is supported and it is added to all output videos (as there is only one output timeline).

  7. Use the [`mapping`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#TextStream.FIELDS.mapping) array in the [`textStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#textstream) configuration object to reference the [`EditAtom`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#editatom) object key.




The following example configuration embeds CEA-608 closed captions in a video.

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
  * `STORAGE_INPUT_VIDEO`: The name of a video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
  * `STORAGE_CAPTIONS_FILE`: The name of a captions file in your Cloud Storage bucket, such as `captions.srt`. This field should take into account any folders that you created in the bucket (for example, `input/captions.srt`). 
  * `STORAGE_OUTPUT_FOLDER`: The name of the output folder in your Cloud Storage bucket where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



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
          },
          {
            "key": "caption_input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_CAPTIONS_FILE"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0",
              "caption_input0"
            ]
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
          },
          {
            "key": "cea-stream0",
            "textStream": {
              "codec": "cea608",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "caption_input0",
                  "inputTrack": 0
                }
              ],
              "languageCode": "en-US",
              "displayName": "English"
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd-hls",
            "container": "ts",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "sd-dash",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "audio-dash",
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
              "sd-hls"
            ]
          },
          {
            "fileName": "manifest.mpd",
            "type": "DASH",
            "muxStreams": [
              "sd-dash",
              "audio-dash"
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
          },
          {
            "key": "caption_input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_CAPTIONS_FILE"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0",
              "caption_input0"
            ]
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
          },
          {
            "key": "cea-stream0",
            "textStream": {
              "codec": "cea608",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "caption_input0",
                  "inputTrack": 0
                }
              ],
              "languageCode": "en-US",
              "displayName": "English"
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd-hls",
            "container": "ts",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "sd-dash",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "audio-dash",
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
              "sd-hls"
            ]
          },
          {
            "fileName": "manifest.mpd",
            "type": "DASH",
            "muxStreams": [
              "sd-dash",
              "audio-dash"
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
  * `STORAGE_INPUT_VIDEO`: The name of a video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
  * `STORAGE_CAPTIONS_FILE`: The name of a captions file in your Cloud Storage bucket, such as `captions.srt`. This field should take into account any folders that you created in the bucket (for example, `input/captions.srt`). 
  * `STORAGE_OUTPUT_FOLDER`: The name of the output folder in your Cloud Storage bucket where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



Save the following content in a file called `request.json`: 
    
    
    {
      "config": {
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          },
          {
            "key": "caption_input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_CAPTIONS_FILE"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0",
              "caption_input0"
            ]
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
          },
          {
            "key": "cea-stream0",
            "textStream": {
              "codec": "cea608",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "caption_input0",
                  "inputTrack": 0
                }
              ],
              "languageCode": "en-US",
              "displayName": "English"
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd-hls",
            "container": "ts",
            "elementaryStreams": [
              "video-stream0",
              "audio-stream0"
            ]
          },
          {
            "key": "sd-dash",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "audio-dash",
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
              "sd-hls"
            ]
          },
          {
            "fileName": "manifest.mpd",
            "type": "DASH",
            "muxStreams": [
              "sd-dash",
              "audio-dash"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        }
      }
    }

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create --location=LOCATION --file=request.json

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create --location=LOCATION --file=request.json

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create --location=LOCATION --file=request.json

You should receive a response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID",
      "config": {
       ...
      },
      "state": "PENDING",
      "createTime": CREATE_TIME,
      "ttlAfterCompletionDays": 30
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
    
    // createJobWithEmbeddedCaptions creates a job that embeds closed captions in the
    // output video. See https://cloud.google.com/transcoder/docs/how-to/captions-and-subtitles
    // for more information.
    func createJobWithEmbeddedCaptions(w io.Writer, projectID string, location string, inputVideoURI string, inputCaptionsURI string, outputURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputVideoURI := "gs://my-bucket/my-video-file"
    	// inputCaptionsURI := "gs://my-bucket/my-captions-file"
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
    			Key: "cea_stream0",
    			ElementaryStream: &transcoderpb.ElementaryStream_TextStream{
    				TextStream: &transcoderpb.TextStream{
    					Codec: "cea608",
    					Mapping: []*transcoderpb.TextStream_TextMapping{
    						{
    							AtomKey:    "atom0",
    							InputKey:   "caption_input0",
    							InputTrack: 0,
    						},
    					},
    					LanguageCode: "en-US",
    					DisplayName:  "English",
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
    							Key: "caption_input0",
    							Uri: inputCaptionsURI,
    						},
    					},
    					EditList: []*transcoderpb.EditAtom{
    						{
    							Key:    "atom0",
    							Inputs: []string{"input0", "caption_input0"},
    						},
    					},
    					ElementaryStreams: elementaryStreams,
    					MuxStreams: []*transcoderpb.MuxStream{
    						{
    							Key:               "sd-hls",
    							Container:         "ts",
    							ElementaryStreams: []string{"video_stream0", "audio_stream0"},
    						},
    						{
    							Key:               "sd-dash",
    							Container:         "fmp4",
    							ElementaryStreams: []string{"video_stream0"},
    						},
    						{
    							Key:               "audio-dash",
    							Container:         "fmp4",
    							ElementaryStreams: []string{"audio_stream0"},
    						},
    					},
    					Manifests: []*transcoderpb.Manifest{
    						{
    							FileName:   "manifest.m3u8",
    							Type:       transcoderpb.[Manifest_HLS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1/transcoderpb.html#cloud_google_com_go_video_transcoder_apiv1_transcoderpb_Manifest_MANIFEST_TYPE_UNSPECIFIED_Manifest_HLS_Manifest_DASH),
    							MuxStreams: []string{"sd-hls"},
    						},
    						{
    							FileName:   "manifest.mpd",
    							Type:       transcoderpb.[Manifest_DASH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/transcoder/apiv1/transcoderpb.html#cloud_google_com_go_video_transcoder_apiv1_transcoderpb_Manifest_MANIFEST_TYPE_UNSPECIFIED_Manifest_HLS_Manifest_DASH),
    							MuxStreams: []string{"sd-dash", "audio-dash"},
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
    import com.google.cloud.video.transcoder.v1.[TextStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.html);
    import com.google.cloud.video.transcoder.v1.[TextStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.html).[TextMapping](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TextStream.TextMapping.html);
    import com.google.cloud.video.transcoder.v1.[TranscoderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.TranscoderServiceClient.html);
    import com.google.cloud.video.transcoder.v1.[VideoStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.VideoStream.html);
    import java.io.IOException;
    
    public class CreateJobWithEmbeddedCaptions {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputVideoUri = "gs://my-bucket/my-video-file";
        String inputCaptionsUri = "gs://my-bucket/my-captions-file";
        String outputUri = "gs://my-bucket/my-output-folder/";
    
        createJobWithEmbeddedCaptions(projectId, location, inputVideoUri, inputCaptionsUri, outputUri);
      }
    
      // Creates a job from an ad-hoc configuration that embeds captions in the output video.
      public static void createJobWithEmbeddedCaptions(
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
                  .setCodec("cea608")
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
                      [ElementaryStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.html).newBuilder().setKey("cea_stream0").[setTextStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.ElementaryStream.Builder.html#com_google_cloud_video_transcoder_v1_ElementaryStream_Builder_setTextStream_com_google_cloud_video_transcoder_v1_TextStream_)(textStream0))
                  .addMuxStreams(
                      0,
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("sd")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("mp4")
                          .addElementaryStreams("video_stream0")
                          .addElementaryStreams("audio_stream0")
                          .build())
                  .addMuxStreams(
                      1,
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("sd_hls")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("ts")
                          .addElementaryStreams("video_stream0")
                          .addElementaryStreams("audio_stream0")
                          .build())
                  .addMuxStreams(
                      2,
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("sd_dash")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("fmp4")
                          .addElementaryStreams("video_stream0")
                          .build())
                  .addMuxStreams(
                      3,
                      [MuxStream](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.html).newBuilder()
                          .setKey("audio_dash")
                          .[setContainer](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.MuxStream.Builder.html#com_google_cloud_video_transcoder_v1_MuxStream_Builder_setContainer_java_lang_String_)("fmp4")
                          .addElementaryStreams("audio_stream0")
                          .build())
                  .[addManifests](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_addManifests_com_google_cloud_video_transcoder_v1_Manifest_)(
                      0,
                      [Manifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.html).newBuilder()
                          .setFileName("manifest.m3u8")
                          .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.Builder.html#com_google_cloud_video_transcoder_v1_Manifest_Builder_setType_com_google_cloud_video_transcoder_v1_Manifest_ManifestType_)([ManifestType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.ManifestType.html).HLS)
                          .addMuxStreams("sd_hls")
                          .build())
                  .[addManifests](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.JobConfig.Builder.html#com_google_cloud_video_transcoder_v1_JobConfig_Builder_addManifests_com_google_cloud_video_transcoder_v1_Manifest_)(
                      1,
                      [Manifest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.html).newBuilder()
                          .setFileName("manifest.mpd")
                          .[setType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.Builder.html#com_google_cloud_video_transcoder_v1_Manifest_Builder_setType_com_google_cloud_video_transcoder_v1_Manifest_ManifestType_)([ManifestType](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-transcoder/latest/com.google.cloud.video.transcoder.v1.Manifest.ManifestType.html).DASH)
                          .addMuxStreams("sd_dash")
                          .addMuxStreams("audio_dash")
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
    // inputCaptionsUri = 'gs://my-bucket/my-captions-file';
    // outputUri = 'gs://my-bucket/my-output-folder/';
    
    // Imports the Transcoder library
    const {TranscoderServiceClient} =
      require('[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)').v1;
    
    // Instantiates a client
    const transcoderServiceClient = new [TranscoderServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)();
    
    async function createJobWithEmbeddedCaptions() {
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
                key: 'caption_input0',
                uri: inputCaptionsUri,
              },
            ],
            editList: [
              {
                key: 'atom0',
                inputs: ['input0', 'caption_input0'],
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
                key: 'cea-stream0',
                textStream: {
                  codec: 'cea608',
                  mapping: [
                    {
                      atomKey: 'atom0',
                      inputKey: 'caption_input0',
                      inputTrack: 0,
                    },
                  ],
                  languageCode: 'en-US',
                  displayName: 'English',
                },
              },
            ],
            muxStreams: [
              {
                key: 'sd-hls',
                container: 'ts',
                elementaryStreams: ['video-stream0', 'audio-stream0'],
              },
              {
                key: 'sd-dash',
                container: 'fmp4',
                elementaryStreams: ['video-stream0'],
              },
              {
                key: 'audio-dash',
                container: 'fmp4',
                elementaryStreams: ['audio-stream0'],
              },
            ],
            manifests: [
              {
                fileName: 'manifest.m3u8',
                type: '[HLS](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.manifest.manifesttype.html)',
                muxStreams: ['sd-hls'],
              },
              {
                fileName: 'manifest.mpd',
                type: '[DASH](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.manifest.manifesttype.html)',
                muxStreams: ['sd-dash', 'audio-dash'],
              },
            ],
          },
        },
      };
    
      // Run request
      const [response] = await transcoderServiceClient.createJob(request);
      console.log(`Job: ${response.name}`);
    }
    
    createJobWithEmbeddedCaptions();

### Python

Before trying this sample, follow the Python setup instructions in the [Transcoder API quickstart using client libraries](https://docs.cloud.google.com/transcoder/docs/quickstart-client-libraries). For more information, see the [Transcoder API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/transcoder/latest). 

To authenticate to Transcoder API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import transcoder_v1
    from google.cloud.video.transcoder_v1.services.transcoder_service import (
        TranscoderServiceClient,
    )
    
    
    def create_job_with_embedded_captions(
        project_id: str,
        location: str,
        input_video_uri: str,
        input_captions_uri: str,
        output_uri: str,
    ) -> transcoder_v1.types.resources.Job:
        """Creates a job based on an ad-hoc job configuration that embeds closed captions in the output video.
    
        Args:
            project_id (str): The GCP project ID.
            location (str): The location to start the job in.
            input_video_uri (str): Uri of the input video in the Cloud Storage
              bucket.
            input_captions_uri (str): Uri of the input captions file in the Cloud
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
                    key="caption-input0",
                    uri=input_captions_uri,
                ),
            ],
            edit_list=[
                transcoder_v1.types.EditAtom(
                    key="atom0",
                    inputs=["input0", "caption-input0"],
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
                    key="cea-stream0",
                    text_stream=transcoder_v1.types.TextStream(
                        codec="cea608",
                        mapping_=[
                            transcoder_v1.types.TextStream.TextMapping(
                                atom_key="atom0",
                                input_key="caption-input0",
                                input_track=0,
                            ),
                        ],
                        language_code="en-US",
                        display_name="English",
                    ),
                ),
            ],
            mux_streams=[
                transcoder_v1.types.MuxStream(
                    key="sd-hls",
                    container="ts",
                    elementary_streams=["video-stream0", "audio-stream0"],
                ),
                transcoder_v1.types.MuxStream(
                    key="sd-dash",
                    container="fmp4",
                    elementary_streams=["video-stream0"],
                ),
                transcoder_v1.types.MuxStream(
                    key="audio-dash",
                    container="fmp4",
                    elementary_streams=["audio-stream0"],
                ),
            ],
            manifests=[
                transcoder_v1.types.Manifest(
                    file_name="manifest.m3u8",
                    type_="HLS",
                    mux_streams=["sd-hls"],
                ),
                transcoder_v1.types.Manifest(
                    file_name="manifest.mpd",
                    type_="DASH",
                    mux_streams=["sd-dash", "audio-dash"],
                ),
            ],
        )
        response = client.create_job(parent=parent, job=job)
        print(f"Job: {response.name}")
        return response
    
    

### Add subtitles

To create a job that produces multi-language subtitle files played from a manifest, do the following:

  1. Add an [`inputs`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.inputs) array to the job configuration.

  2. Add an [`Input`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#input) object to the `inputs` array that defines the key and URI for the associated input video.

  3. Add another [`Input`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#input) object that defines the URI for the input caption file.

  4. Add an [`editList`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.edit_list) array to the configuration. This array is used to add the inputs to the output video timeline.

  5. Add an [`EditAtom`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#editatom) object to the `editList` array that references the objects in the `inputs` array by key. You can designate a `startTimeOffset` and `endTimeOffset` to trim the input video.

  6. Add the captions to the output containers by adding a [`textStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#textstream) object to the [`elementaryStreams`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.elementary_streams) array.

  7. For the standalone caption file, specify the container in the [`muxStream`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#muxstream) array; see the objects with keys `text-vtt-en` and `text-vtt-es` in the following configuration. For embedded captions, you only need the elementary stream.




The following configuration generates multiple WebVTT files, one for English subtitles and one for Spanish subtitles. DASH subtitles in WebVTT files are created in the fMP4 container format.

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
  * `STORAGE_INPUT_VIDEO`: The name of a video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
  * `STORAGE_SUBTITLES_FILE1`: The name of the subtitles file in your Cloud Storage bucket, such as `subtitles-en.srt` for English language subtitles. This field should take into account any folders that you created in the bucket (for example, `input/subtitles-en.srt`). 
  * `STORAGE_SUBTITLES_FILE2`: The name of another subtitles file in your Cloud Storage bucket, such as `subtitles-es.srt` for Spanish language subtitles. This field should take into account any folders that you created in the bucket (for example, `input/subtitles-es.srt`). 
  * `STORAGE_OUTPUT_FOLDER`: The name of the output folder in your Cloud Storage bucket where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



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
          },
          {
            "key": "subtitle_input_en",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_SUBTITLES_FILE1"
          },
          {
            "key": "subtitle_input_es",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_SUBTITLES_FILE2"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0",
              "subtitle_input_en",
              "subtitle_input_es"
            ]
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
          },
          {
            "key": "vtt-stream-en",
            "textStream": {
              "codec": "webvtt",
              "languageCode": "en-US",
              "displayName": "English",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "subtitle_input_en"
                }
              ]
            }
          },
          {
            "key": "vtt-stream-es",
            "textStream": {
              "codec": "webvtt",
              "languageCode": "es-ES",
              "displayName": "Spanish",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "subtitle_input_es"
                }
              ]
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd-hls-fmp4",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "audio-hls-fmp4",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ]
          },
          {
            "key": "text-vtt-en",
            "container": "vtt",
            "elementaryStreams": [
              "vtt-stream-en"
            ],
            "segmentSettings": {
              "segmentDuration": "6s",
              "individualSegments": true
            }
          },
          {
            "key": "text-vtt-es",
            "container": "vtt",
            "elementaryStreams": [
              "vtt-stream-es"
            ],
            "segmentSettings": {
              "segmentDuration": "6s",
              "individualSegments": true
            }
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "type": "HLS",
            "muxStreams": [
              "sd-hls-fmp4",
              "audio-hls-fmp4",
              "text-vtt-en",
              "text-vtt-es"
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
          },
          {
            "key": "subtitle_input_en",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_SUBTITLES_FILE1"
          },
          {
            "key": "subtitle_input_es",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_SUBTITLES_FILE2"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0",
              "subtitle_input_en",
              "subtitle_input_es"
            ]
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
          },
          {
            "key": "vtt-stream-en",
            "textStream": {
              "codec": "webvtt",
              "languageCode": "en-US",
              "displayName": "English",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "subtitle_input_en"
                }
              ]
            }
          },
          {
            "key": "vtt-stream-es",
            "textStream": {
              "codec": "webvtt",
              "languageCode": "es-ES",
              "displayName": "Spanish",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "subtitle_input_es"
                }
              ]
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd-hls-fmp4",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "audio-hls-fmp4",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ]
          },
          {
            "key": "text-vtt-en",
            "container": "vtt",
            "elementaryStreams": [
              "vtt-stream-en"
            ],
            "segmentSettings": {
              "segmentDuration": "6s",
              "individualSegments": true
            }
          },
          {
            "key": "text-vtt-es",
            "container": "vtt",
            "elementaryStreams": [
              "vtt-stream-es"
            ],
            "segmentSettings": {
              "segmentDuration": "6s",
              "individualSegments": true
            }
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "type": "HLS",
            "muxStreams": [
              "sd-hls-fmp4",
              "audio-hls-fmp4",
              "text-vtt-en",
              "text-vtt-es"
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
  * `STORAGE_INPUT_VIDEO`: The name of a video in your Cloud Storage bucket that you are transcoding, such as `my-vid.mp4`. This field should take into account any folders that you created in the bucket (for example, `input/my-vid.mp4`). 
  * `STORAGE_SUBTITLES_FILE1`: The name of the subtitles file in your Cloud Storage bucket, such as `subtitles-en.srt` for English language subtitles. This field should take into account any folders that you created in the bucket (for example, `input/subtitles-en.srt`). 
  * `STORAGE_SUBTITLES_FILE2`: The name of another subtitles file in your Cloud Storage bucket, such as `subtitles-es.srt` for Spanish language subtitles. This field should take into account any folders that you created in the bucket (for example, `input/subtitles-es.srt`). 
  * `STORAGE_OUTPUT_FOLDER`: The name of the output folder in your Cloud Storage bucket where you want to save the encoded video outputs. **Note:** You don't need to create the output folder object before creating the job. When processing the job, the Transcoder API automatically prepends the folder name you specify as part of the names of the objects saved to Cloud Storage.



Save the following content in a file called `request.json`: 
    
    
    {
      "config": {
        "inputs": [
          {
            "key": "input0",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_INPUT_VIDEO"
          },
          {
            "key": "subtitle_input_en",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_SUBTITLES_FILE1"
          },
          {
            "key": "subtitle_input_es",
            "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_SUBTITLES_FILE2"
          }
        ],
        "editList": [
          {
            "key": "atom0",
            "inputs": [
              "input0",
              "subtitle_input_en",
              "subtitle_input_es"
            ]
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
          },
          {
            "key": "vtt-stream-en",
            "textStream": {
              "codec": "webvtt",
              "languageCode": "en-US",
              "displayName": "English",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "subtitle_input_en"
                }
              ]
            }
          },
          {
            "key": "vtt-stream-es",
            "textStream": {
              "codec": "webvtt",
              "languageCode": "es-ES",
              "displayName": "Spanish",
              "mapping": [
                {
                  "atomKey": "atom0",
                  "inputKey": "subtitle_input_es"
                }
              ]
            }
          }
        ],
        "muxStreams": [
          {
            "key": "sd-hls-fmp4",
            "container": "fmp4",
            "elementaryStreams": [
              "video-stream0"
            ]
          },
          {
            "key": "audio-hls-fmp4",
            "container": "fmp4",
            "elementaryStreams": [
              "audio-stream0"
            ]
          },
          {
            "key": "text-vtt-en",
            "container": "vtt",
            "elementaryStreams": [
              "vtt-stream-en"
            ],
            "segmentSettings": {
              "segmentDuration": "6s",
              "individualSegments": true
            }
          },
          {
            "key": "text-vtt-es",
            "container": "vtt",
            "elementaryStreams": [
              "vtt-stream-es"
            ],
            "segmentSettings": {
              "segmentDuration": "6s",
              "individualSegments": true
            }
          }
        ],
        "manifests": [
          {
            "fileName": "manifest.m3u8",
            "type": "HLS",
            "muxStreams": [
              "sd-hls-fmp4",
              "audio-hls-fmp4",
              "text-vtt-en",
              "text-vtt-es"
            ]
          }
        ],
        "output": {
          "uri": "gs://STORAGE_BUCKET_NAME/STORAGE_OUTPUT_FOLDER/"
        }
      }
    }

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create --location=LOCATION --file=request.json

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create --location=LOCATION --file=request.json

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud transcoder jobs create --location=LOCATION --file=request.json

You should receive a response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/jobs/JOB_ID",
      "config": {
       ...
      },
      "state": "PENDING",
      "createTime": CREATE_TIME,
      "ttlAfterCompletionDays": 30
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
    
    

## Play your video

To view the captions or subtitles on Windows, play the video in the Movies & TV app. Make sure to select the subtitles track.

To view the captions or subtitles on MacOS or Linux, you can play the video in [Shaka Player](https://shaka-player-demo.appspot.com/demo/). Make sure to enable captions or subtitles from the **Captions** menu.

**Note:** If you want to create a CDN for the media outputs, see the [Media CDN quickstart](https://docs.cloud.google.com/media-cdn/docs/quickstart).

To play the generated media file in [Shaka Player](https://shaka-player-demo.appspot.com/demo/), complete the following steps:

  1. [Make the Cloud Storage bucket you created publicly readable](https://docs.cloud.google.com/storage/docs/access-control/making-data-public#buckets).
  2. To [enable cross-origin resource sharing (CORS) on a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/using-cors#configure-cors-bucket), do the following: 
     1. Create a JSON file that contains the following: 
            
            [
              {
                "origin": ["https://shaka-player-demo.appspot.com/"],
                "responseHeader": ["Content-Type", "Range"],
                "method": ["GET", "HEAD"],
                "maxAgeSeconds": 3600
              }
            ]

     2. Run the following command after replacing JSON_FILE_NAME with the name of the JSON file you created in the previous step: 
            
            gcloud storage buckets update gs://STORAGE_BUCKET_NAME --cors-file=JSON_FILE_NAME.json

  3. Pick one of the MP4 or manifest files generated by the transcoding job in the Cloud Storage bucket. Click **Copy URL** in the file's **Public access** column.
  4. Navigate to [Shaka Player](https://shaka-player-demo.appspot.com/demo/), an online live stream player.
  5. Click **Custom Content** in the top navigation bar.
  6. Click the **+** button.
  7. Paste the public URL of the file into the **Manifest URL** box.

![Enter the URL of the file in Shaka Player.](https://docs.cloud.google.com/static/transcoder/images/shaka-player.png)

  8. Type a name in the **Name** box.

  9. Click **Save**.

  10. Click **Play**.

  11. Select the ellipsis button on the bottom right of the player and enable captions.


**Note:** Not all media players support captions or subtitles. Check the player documentation.

### Example

You can use the following files for a test job:

  * [Sample input video](https://docs.cloud.google.com/static/transcoder/images/ChromeCast.mp4)
  * [Sample input caption file for closed captions](https://docs.cloud.google.com/transcoder/images/captions.srt)
  * [Sample input caption file for English subtitles](https://docs.cloud.google.com/transcoder/images/subtitles-en.srt)
  * [Sample input caption file for Spanish subtitles](https://docs.cloud.google.com/transcoder/images/subtitles-es.srt)



The input caption file must not contain blank lines in between text lines.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
