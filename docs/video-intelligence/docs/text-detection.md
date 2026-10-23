---
url: https://docs.cloud.google.com/video-intelligence/docs/text-detection/
title: Recognize text \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:38.579587+00:00
---

# Recognize text  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/text-detection/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Recognize text Stay organized with collections  Save and categorize content based on your preferences. 

_Text Detection_ performs Optical Character Recognition (OCR), which detects and extracts text within an input video.

Text detection is available for all the [languages](https://docs.cloud.google.com/vision/docs/languages) supported by the Cloud Vision API.

## Request text detection for a video on Cloud Storage

The following samples demonstrate text detection on a file located in Cloud Storage.

### REST

## Send video annotation request

The following shows how to send a POST request to the [`videos:annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. The example uses the Google Cloud CLI to create an access token. For instructions on installing the gcloud CLI, see the [Video Intelligence API Quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts).

Before using any of the request data, make the following replacements: 

  * INPUT_URI: a Cloud Storage bucket that contains the file you want to annotate, including the file name. Must start with `gs://`.  
For example: `"inputUri": "gs://cloud-videointelligence-demo/assistant.mp4",`
  * LANGUAGE_CODE: [Optional] For example, "en-US"
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputUri": "INPUT_URI",
      "features": ["TEXT_DETECTION"],
      "videoContext": {
        "textDetectionConfig": {
          "languageHints": ["LANGUAGE_CODE"]
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videointelligence.googleapis.com/v1/videos:annotate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videointelligence.googleapis.com/v1/videos:annotate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID"
    }
    

If the response is successful, the Video Intelligence API returns the `name` for your operation. The above shows an example of such a response, where: `project-number` is the number of your project and `operation-id` is the ID of the long running operation created for the request. 

  * PROJECT_NUMBER: the number of your project
  * LOCATION_ID: the Cloud region where annotation should take place. Supported cloud regions are: `us-east1`, `us-west1`, `europe-west1`, `asia-east1`. If no region is specified, a region will be determined based on video file location. 
  * OPERATION_ID: the ID of the long running operation created for the request and provided in the response when you started the operation, for example `12345...`



## Get annotation results

To retrieve the result of the operation, make a [GET](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/get) request, using the operation name returned from the call to [videos:annotate](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate), as shown in the following example.

Before using any of the request data, make the following replacements: 

  * OPERATION_NAME: the name of the operation as returned by Video Intelligence API. The operation name has the format `projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID`
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    GET https://videointelligence.googleapis.com/v1/OPERATION_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER" \  
         "https://videointelligence.googleapis.com/v1/OPERATION_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videointelligence.googleapis.com/v1/OPERATION_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    "textAnnotations": [
      {
        "text": "Hair Salon",
        "segments": [
          {
            "segment": {
              "startTimeOffset": "0.833333s",
              "endTimeOffset": "2.291666s"
            },
            "confidence": 0.99438506,
            "frames": [
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.7015625,
                      "y": 0.59583336
                    },
                    {
                      "x": 0.7984375,
                      "y": 0.59583336
                    },
                    {
                      "x": 0.7984375,
                      "y": 0.64166665
                    },
                    {
                      "x": 0.7015625,
                      "y": 0.64166665
                    }
                  ]
                },
                "timeOffset": "0.833333s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "1.041666s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "1.250s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6319444
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6319444
                    }
                  ]
                },
                "timeOffset": "1.458333s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "1.666666s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "1.875s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "2.083333s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "2.291666s"
              }
            ]
          }
        ]
      },
      {
        "text": "\"Sure, give me one second.\"",
        "segments": [
          {
            "segment": {
              "startTimeOffset": "10.625s",
              "endTimeOffset": "13.333333s"
            },
            "confidence": 0.98716676,
            "frames": [
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.60859376,
                      "y": 0.59583336
                    },
                    {
                      "x": 0.8952959,
                      "y": 0.5903528
                    },
                    {
                      "x": 0.89560676,
                      "y": 0.6417387
                    },
                    {
                      "x": 0.60890454,
                      "y": 0.64721924
                    }
                  ]
                },
                "timeOffset": "10.625s"
              },
      ...
    
        ]
      }
    

Text detection annotations are returned as a `textAnnotations` list. Note: The **done** field is only returned when its value is **True**. It's not included in responses for which the operation has not completed. 

## Download annotation results

Copy the annotation from the source to the destination bucket: (see [Copy files and objects](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp)) 

`gcloud storage cp gcs_uri gs://my-bucket`

Note: If the output gcs uri is provided by the user, then the annotation is stored in that gcs uri. 

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	video "cloud.google.com/go/videointelligence/apiv1"
    	videopb "cloud.google.com/go/videointelligence/apiv1/videointelligencepb"
    	"github.com/golang/protobuf/ptypes"
    )
    
    // textDetectionGCS analyzes a video and extracts the text from the video's audio.
    func textDetectionGCS(w io.Writer, gcsURI string) error {
    	// gcsURI := "gs://python-docs-samples-tests/video/googlework_short.mp4"
    
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := video.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("video.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_Close)()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		InputUri: gcsURI,
    		Features: []videopb.Feature{
    			videopb.Feature_TEXT_DETECTION,
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("AnnotateVideo: %w", err)
    	}
    
    	resp, err := op.[Wait](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_AnnotateVideoOperation_Wait)(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	// Only one video was processed, so get the first result.
    	result := resp.GetAnnotationResults()[0]
    
    	for _, annotation := range result.TextAnnotations {
    		fmt.Fprintf(w, "Text: %q\n", annotation.GetText())
    
    		// Get the first text segment.
    		segment := annotation.GetSegments()[0]
    		start, _ := ptypes.Duration(segment.GetSegment().GetStartTimeOffset())
    		end, _ := ptypes.Duration(segment.GetSegment().GetEndTimeOffset())
    		fmt.Fprintf(w, "\tSegment: %v to %v\n", start, end)
    
    		fmt.Fprintf(w, "\tConfidence: %f\n", segment.GetConfidence())
    
    		// Show the result for the first frame in this segment.
    		frame := segment.GetFrames()[0]
    		seconds := float32(frame.GetTimeOffset().GetSeconds())
    		nanos := float32(frame.GetTimeOffset().GetNanos())
    		fmt.Fprintf(w, "\tTime offset of the first frame: %fs\n", seconds+nanos/1e9)
    
    		fmt.Fprintf(w, "\tRotated bounding box vertices:\n")
    		for _, vertex := range frame.GetRotatedBoundingBox().GetVertices() {
    			fmt.Fprintf(w, "\t\tVertex x=%f, y=%f\n", vertex.GetX(), vertex.GetY())
    		}
    	}
    
    	return nil
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Detect Text in a video.
     *
     * @param gcsUri the path to the video file to analyze.
     */
    public static VideoAnnotationResults detectTextGcs(String gcsUri) throws Exception {
      try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
        // Create the request
        AnnotateVideoRequest request =
            AnnotateVideoRequest.newBuilder()
                .setInputUri(gcsUri)
                .addFeatures(Feature.TEXT_DETECTION)
                .build();
    
        // asynchronously perform object tracking on videos
        OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
            client.annotateVideoAsync(request);
    
        System.out.println("Waiting for operation to complete...");
        // The first result is retrieved because a single video was processed.
        AnnotateVideoResponse response = future.get(300, TimeUnit.SECONDS);
        VideoAnnotationResults results = response.getAnnotationResults(0);
    
        // Get only the first annotation for demo purposes.
        TextAnnotation annotation = results.getTextAnnotations(0);
        System.out.println("Text: " + annotation.getText());
    
        // Get the first text segment.
        TextSegment textSegment = annotation.getSegments(0);
        System.out.println("Confidence: " + textSegment.getConfidence());
        // For the text segment display it's time offset
        VideoSegment videoSegment = textSegment.getSegment();
        Duration startTimeOffset = videoSegment.getStartTimeOffset();
        Duration endTimeOffset = videoSegment.getEndTimeOffset();
        // Display the offset times in seconds, 1e9 is part of the formula to convert nanos to seconds
        System.out.println(
            String.format(
                "Start time: %.2f", startTimeOffset.getSeconds() + startTimeOffset.getNanos() / 1e9));
        System.out.println(
            String.format(
                "End time: %.2f", endTimeOffset.getSeconds() + endTimeOffset.getNanos() / 1e9));
    
        // Show the first result for the first frame in the segment.
        TextFrame textFrame = textSegment.getFrames(0);
        Duration timeOffset = textFrame.getTimeOffset();
        System.out.println(
            String.format(
                "Time offset for the first frame: %.2f",
                timeOffset.getSeconds() + timeOffset.getNanos() / 1e9));
    
        // Display the rotated bounding box for where the text is on the frame.
        System.out.println("Rotated Bounding Box Vertices:");
        List<NormalizedVertex> vertices = textFrame.getRotatedBoundingBox().getVerticesList();
        for (NormalizedVertex normalizedVertex : vertices) {
          System.out.println(
              String.format(
                  "\tVertex.x: %.2f, Vertex.y: %.2f",
                  normalizedVertex.getX(), normalizedVertex.getY()));
        }
        return results;
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Video Intelligence library
    const Video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)');
    // Creates a client
    const video = new Video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const gcsUri = 'GCS URI of the video to analyze, e.g. gs://my-bucket/my-video.mp4';
    
    const request = {
      inputUri: gcsUri,
      features: ['TEXT_DETECTION'],
    };
    // Detects text in a video
    const [operation] = await video.annotateVideo(request);
    const results = await operation.promise();
    console.log('Waiting for operation to complete...');
    // Gets annotations for video
    const textAnnotations = results[0].annotationResults[0].textAnnotations;
    textAnnotations.forEach(textAnnotation => {
      console.log(`Text ${textAnnotation.text} occurs at:`);
      textAnnotation.segments.forEach(segment => {
        const time = segment.segment;
        console.log(
          ` Start: ${time.startTimeOffset.seconds || 0}.${(
            time.startTimeOffset.nanos / 1e6
          ).toFixed(0)}s`
        );
        console.log(
          ` End: ${time.endTimeOffset.seconds || 0}.${(
            time.endTimeOffset.nanos / 1e6
          ).toFixed(0)}s`
        );
        console.log(` Confidence: ${segment.confidence}`);
        segment.frames.forEach(frame => {
          const timeOffset = frame.timeOffset;
          console.log(
            `Time offset for the frame: ${timeOffset.seconds || 0}` +
              `.${(timeOffset.nanos / 1e6).toFixed(0)}s`
          );
          console.log('Rotated Bounding Box Vertices:');
          frame.rotatedBoundingBox.vertices.forEach(vertex => {
            console.log(`Vertex.x:${vertex.x}, Vertex.y:${vertex.y}`);
          });
        });
      });
    });

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """Detect text in a video stored on GCS."""
    from google.cloud import videointelligence
    
    video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
    features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).TEXT_DETECTION]
    
    operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
        request={"features": features, "input_uri": input_uri}
    )
    
    print("\nProcessing video for text detection.")
    result = operation.result(timeout=600)
    
    # The first result is retrieved because a single video was processed.
    annotation_result = result.annotation_results[0]
    
    for text_annotation in annotation_result.text_annotations:
        print("\nText: {}".format(text_annotation.text))
    
        # Get the first text segment
        text_segment = text_annotation.segments[0]
        start_time = text_segment.segment.start_time_offset
        end_time = text_segment.segment.end_time_offset
        print(
            "start_time: {}, end_time: {}".format(
                start_time.seconds + start_time.microseconds * 1e-6,
                end_time.seconds + end_time.microseconds * 1e-6,
            )
        )
    
        print("Confidence: {}".format(text_segment.confidence))
    
        # Show the result for the first frame in this segment.
        frame = text_segment.frames[0]
        time_offset = frame.time_offset
        print(
            "Time offset for the first frame: {}".format(
                time_offset.seconds + time_offset.microseconds * 1e-6
            )
        )
        print("Rotated Bounding Box Vertices:")
        for vertex in frame.rotated_bounding_box.vertices:
            print("\tVertex.x: {}, Vertex.y: {}".format(vertex.x, vertex.y))

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

## Request text detection for video from a local file

The following samples demonstrate text detection on a file stored locally.

### REST

## Send video annotation request

To perform annotation on a local video file, be sure to base64-encode the contents of the video file. Include the base64-encoded contents in the `inputContent` field of the request. For information on how to base64-encode the contents of a video file, see [Base64 Encoding](https://docs.cloud.google.com/video-intelligence/docs/base64).

The following shows how to send a POST request to the `videos:annotate` method. The example uses the Google Cloud CLI to create an access token. For instructions on installing the Google Cloud CLI, see the [Video Intelligence API Quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts)

Before using any of the request data, make the following replacements: 

  * "inputContent": BASE64_ENCODED_CONTENT   
For example:  
`"UklGRg41AwBBVkkgTElTVAwBAABoZHJsYXZpaDgAAAA1ggAAxPMBAAAAAAAQCAA..."`  

  * LANGUAGE_CODE: [Optional] For example, "en-US"
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project 



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputContent": "BASE64_ENCODED_CONTENT",
      "features": ["TEXT_DETECTION"],
      "videoContext": {
        "textDetectionConfig": {
          "languageHints": ["LANGUAGE_CODE"]
        }
      }
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://videointelligence.googleapis.com/v1/videos:annotate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://videointelligence.googleapis.com/v1/videos:annotate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID"
    }
    

If the response is successful, the Video Intelligence API returns the `name` of your operation. The above shows an example of such a response, where `project-number` is the name of your project and `operation-id` is the ID of the long running operation created for the request. 

  * OPERATION_ID: provided in the response when you started the operation, for example `12345...`



## Get annotation results

To retrieve the result of the operation, make a [GET](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/get) request, using the operation name returned from the call to [videos:annotate](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate), as shown in the following example.

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    GET https://videointelligence.googleapis.com/v1/OPERATION_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER" \  
         "https://videointelligence.googleapis.com/v1/OPERATION_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://videointelligence.googleapis.com/v1/OPERATION_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    "textAnnotations": [
      {
        "text": "Hair Salon",
        "segments": [
          {
            "segment": {
              "startTimeOffset": "0.833333s",
              "endTimeOffset": "2.291666s"
            },
            "confidence": 0.99438506,
            "frames": [
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.7015625,
                      "y": 0.59583336
                    },
                    {
                      "x": 0.7984375,
                      "y": 0.59583336
                    },
                    {
                      "x": 0.7984375,
                      "y": 0.64166665
                    },
                    {
                      "x": 0.7015625,
                      "y": 0.64166665
                    }
                  ]
                },
                "timeOffset": "0.833333s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "1.041666s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "1.250s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6319444
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6319444
                    }
                  ]
                },
                "timeOffset": "1.458333s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "1.666666s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "1.875s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "2.083333s"
              },
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.70234376,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6
                    },
                    {
                      "x": 0.7992188,
                      "y": 0.6333333
                    },
                    {
                      "x": 0.70234376,
                      "y": 0.6333333
                    }
                  ]
                },
                "timeOffset": "2.291666s"
              }
            ]
          }
        ]
      },
      {
        "text": "\"Sure, give me one second.\"",
        "segments": [
          {
            "segment": {
              "startTimeOffset": "10.625s",
              "endTimeOffset": "13.333333s"
            },
            "confidence": 0.98716676,
            "frames": [
              {
                "rotatedBoundingBox": {
                  "vertices": [
                    {
                      "x": 0.60859376,
                      "y": 0.59583336
                    },
                    {
                      "x": 0.8952959,
                      "y": 0.5903528
                    },
                    {
                      "x": 0.89560676,
                      "y": 0.6417387
                    },
                    {
                      "x": 0.60890454,
                      "y": 0.64721924
                    }
                  ]
                },
                "timeOffset": "10.625s"
              },
      ...
    
        ]
    }
    

Text detection annotations are returned as a `textAnnotations` list. Note: The **done** field is only returned when its value is **True**. It's not included in responses for which the operation has not completed. 

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	video "cloud.google.com/go/videointelligence/apiv1"
    	videopb "cloud.google.com/go/videointelligence/apiv1/videointelligencepb"
    	"github.com/golang/protobuf/ptypes"
    )
    
    // textDetection analyzes a video and extracts the text from the video's audio.
    func textDetection(w io.Writer, filename string) error {
    	// filename := "../testdata/googlework_short.mp4"
    
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := video.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("video.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_Close)()
    
    	fileBytes, err := os.ReadFile(filename)
    	if err != nil {
    		return fmt.Errorf("os.ReadFile: %w", err)
    	}
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		InputContent: fileBytes,
    		Features: []videopb.Feature{
    			videopb.Feature_TEXT_DETECTION,
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("AnnotateVideo: %w", err)
    	}
    
    	resp, err := op.[Wait](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_AnnotateVideoOperation_Wait)(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	// Only one video was processed, so get the first result.
    	result := resp.GetAnnotationResults()[0]
    
    	for _, annotation := range result.TextAnnotations {
    		fmt.Fprintf(w, "Text: %q\n", annotation.GetText())
    
    		// Get the first text segment.
    		segment := annotation.GetSegments()[0]
    		start, _ := ptypes.Duration(segment.GetSegment().GetStartTimeOffset())
    		end, _ := ptypes.Duration(segment.GetSegment().GetEndTimeOffset())
    		fmt.Fprintf(w, "\tSegment: %v to %v\n", start, end)
    
    		fmt.Fprintf(w, "\tConfidence: %f\n", segment.GetConfidence())
    
    		// Show the result for the first frame in this segment.
    		frame := segment.GetFrames()[0]
    		seconds := float32(frame.GetTimeOffset().GetSeconds())
    		nanos := float32(frame.GetTimeOffset().GetNanos())
    		fmt.Fprintf(w, "\tTime offset of the first frame: %fs\n", seconds+nanos/1e9)
    
    		fmt.Fprintf(w, "\tRotated bounding box vertices:\n")
    		for _, vertex := range frame.GetRotatedBoundingBox().GetVertices() {
    			fmt.Fprintf(w, "\t\tVertex x=%f, y=%f\n", vertex.GetX(), vertex.GetY())
    		}
    	}
    
    	return nil
    }
    

### Java
    
    
    /**
     * Detect text in a video.
     *
     * @param filePath the path to the video file to analyze.
     */
    public static VideoAnnotationResults detectText(String filePath) throws Exception {
      try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
        // Read file
        Path path = Paths.get(filePath);
        byte[] data = Files.readAllBytes(path);
    
        // Create the request
        AnnotateVideoRequest request =
            AnnotateVideoRequest.newBuilder()
                .setInputContent(ByteString.copyFrom(data))
                .addFeatures(Feature.TEXT_DETECTION)
                .build();
    
        // asynchronously perform object tracking on videos
        OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
            client.annotateVideoAsync(request);
    
        System.out.println("Waiting for operation to complete...");
        // The first result is retrieved because a single video was processed.
        AnnotateVideoResponse response = future.get(300, TimeUnit.SECONDS);
        VideoAnnotationResults results = response.getAnnotationResults(0);
    
        // Get only the first annotation for demo purposes.
        TextAnnotation annotation = results.getTextAnnotations(0);
        System.out.println("Text: " + annotation.getText());
    
        // Get the first text segment.
        TextSegment textSegment = annotation.getSegments(0);
        System.out.println("Confidence: " + textSegment.getConfidence());
        // For the text segment display it's time offset
        VideoSegment videoSegment = textSegment.getSegment();
        Duration startTimeOffset = videoSegment.getStartTimeOffset();
        Duration endTimeOffset = videoSegment.getEndTimeOffset();
        // Display the offset times in seconds, 1e9 is part of the formula to convert nanos to seconds
        System.out.println(
            String.format(
                "Start time: %.2f", startTimeOffset.getSeconds() + startTimeOffset.getNanos() / 1e9));
        System.out.println(
            String.format(
                "End time: %.2f", endTimeOffset.getSeconds() + endTimeOffset.getNanos() / 1e9));
    
        // Show the first result for the first frame in the segment.
        TextFrame textFrame = textSegment.getFrames(0);
        Duration timeOffset = textFrame.getTimeOffset();
        System.out.println(
            String.format(
                "Time offset for the first frame: %.2f",
                timeOffset.getSeconds() + timeOffset.getNanos() / 1e9));
    
        // Display the rotated bounding box for where the text is on the frame.
        System.out.println("Rotated Bounding Box Vertices:");
        List<NormalizedVertex> vertices = textFrame.getRotatedBoundingBox().getVerticesList();
        for (NormalizedVertex normalizedVertex : vertices) {
          System.out.println(
              String.format(
                  "\tVertex.x: %.2f, Vertex.y: %.2f",
                  normalizedVertex.getX(), normalizedVertex.getY()));
        }
        return results;
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Video Intelligence library + Node's fs library
    const Video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)');
    const fs = require('fs');
    const util = require('util');
    // Creates a client
    const video = new Video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const path = 'Local file to analyze, e.g. ./my-file.mp4';
    
    // Reads a local video file and converts it to base64
    const file = await util.promisify(fs.readFile)(path);
    const inputContent = file.toString('base64');
    
    const request = {
      inputContent: inputContent,
      features: ['TEXT_DETECTION'],
    };
    // Detects text in a video
    const [operation] = await video.annotateVideo(request);
    const results = await operation.promise();
    console.log('Waiting for operation to complete...');
    
    // Gets annotations for video
    const textAnnotations = results[0].annotationResults[0].textAnnotations;
    textAnnotations.forEach(textAnnotation => {
      console.log(`Text ${textAnnotation.text} occurs at:`);
      textAnnotation.segments.forEach(segment => {
        const time = segment.segment;
        if (time.startTimeOffset.seconds === undefined) {
          time.startTimeOffset.seconds = 0;
        }
        if (time.startTimeOffset.nanos === undefined) {
          time.startTimeOffset.nanos = 0;
        }
        if (time.endTimeOffset.seconds === undefined) {
          time.endTimeOffset.seconds = 0;
        }
        if (time.endTimeOffset.nanos === undefined) {
          time.endTimeOffset.nanos = 0;
        }
        console.log(
          `\tStart: ${time.startTimeOffset.seconds || 0}` +
            `.${(time.startTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(
          `\tEnd: ${time.endTimeOffset.seconds || 0}.` +
            `${(time.endTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(`\tConfidence: ${segment.confidence}`);
        segment.frames.forEach(frame => {
          const timeOffset = frame.timeOffset;
          console.log(
            `Time offset for the frame: ${timeOffset.seconds || 0}` +
              `.${(timeOffset.nanos / 1e6).toFixed(0)}s`
          );
          console.log('Rotated Bounding Box Vertices:');
          frame.rotatedBoundingBox.vertices.forEach(vertex => {
            console.log(`Vertex.x:${vertex.x}, Vertex.y:${vertex.y}`);
          });
        });
      });
    });

### Python
    
    
    import io
    
    from google.cloud import videointelligence
    
    def video_detect_text(path):
        """Detect text in a local video."""
        video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
        features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).TEXT_DETECTION]
        video_context = videointelligence.[VideoContext](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.VideoContext.html)()
    
        with io.open(path, "rb") as file:
            input_content = file.read()
    
        operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
            request={
                "features": features,
                "input_content": input_content,
                "video_context": video_context,
            }
        )
    
        print("\nProcessing video for text detection.")
        result = operation.result(timeout=300)
    
        # The first result is retrieved because a single video was processed.
        annotation_result = result.annotation_results[0]
    
        for text_annotation in annotation_result.text_annotations:
            print("\nText: {}".format(text_annotation.text))
    
            # Get the first text segment
            text_segment = text_annotation.segments[0]
            start_time = text_segment.segment.start_time_offset
            end_time = text_segment.segment.end_time_offset
            print(
                "start_time: {}, end_time: {}".format(
                    start_time.seconds + start_time.microseconds * 1e-6,
                    end_time.seconds + end_time.microseconds * 1e-6,
                )
            )
    
            print("Confidence: {}".format(text_segment.confidence))
    
            # Show the result for the first frame in this segment.
            frame = text_segment.frames[0]
            time_offset = frame.time_offset
            print(
                "Time offset for the first frame: {}".format(
                    time_offset.seconds + time_offset.microseconds * 1e-6
                )
            )
            print("Rotated Bounding Box Vertices:")
            for vertex in frame.rotated_bounding_box.vertices:
                print("\tVertex.x: {}, Vertex.y: {}".format(vertex.x, vertex.y))
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
