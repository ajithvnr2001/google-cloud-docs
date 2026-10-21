---
url: https://docs.cloud.google.com/video-intelligence/docs/object-tracking/
title: Track objects \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:25.369946+00:00
---

# Track objects  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/object-tracking/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Track objects Stay organized with collections  Save and categorize content based on your preferences. 

Object tracking tracks objects detected in an input video. To make an object tracking request, call the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method and specify `OBJECT_TRACKING` in the `features` field.

For entities and spatial locations that are detected in a video or video segments, an object tracking request annotates the video with the appropriate labels for these entities and spatial locations. For example, a video of vehicles crossing a traffic signal might produce labels such as "car", "truck", "bike," "tires", "lights", "window" and so on. Each label can include a series of bounding boxes, with each bounding box having an associated time segment containing a time offset that indicates the duration offset from the beginning of the video. The annotation also contains additional entity information including an entity ID that you can use to find more information about the entity in the [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).

**Note:** There is a limit on the size of the detected objects. Very small objects in the video may not be detected.

## Object tracking vs. label detection

Object tracking differs from [label detection](https://docs.cloud.google.com/video-intelligence/docs/analyze-labels). Label detection provides labels without bounding boxes, whereas object tracking provides the labels of the individual objects present in a given video along with the bounding box of each object instance at every time step.

Multiple instances of the same object type are assigned to different instances of `ObjectTrackingAnnotation` message where all the occurrences of a given object track are kept in its own instance of `ObjectTrackingAnnotation`. For example, if there is a red car and a blue car appearing for 5 seconds in a video, the tracking request should return two instances of `ObjectTrackingAnnotation`. The first instance will contain the locations of one of the two cars, for example, the red car, while the second will contain the locations of the other car.

## Request object tracking for a video on Cloud Storage

The following samples demonstrate object tracking on a file located in Cloud Storage.

### REST

### Send the process request

The following shows how to send a `POST` request to the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. The example uses the access token for a service account set up for the project using the Google Cloud CLI. For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Video Intelligence quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts).

Before using any of the request data, make the following replacements: 

  * INPUT_URI: STORAGE_URI   
For example:  
`"inputUri": "gs://cloud-videointelligence-demo/assistant.mp4",`  

  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputUri": "STORAGE_URI",
      "features": ["OBJECT_TRACKING"]
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
    
    

If the request is successful, the Video Intelligence API returns the `name` of your operation. The above shows an example of such a response, where `PROJECT_NUMBER` is the number of your project and `OPERATION_ID` is the ID of the long-running operation created for the request.

### Get the results

To get the results of your request, send a `GET`, using the operation name returned from the call to `videos:annotate`, as shown in the following example.

Before using any of the request data, make the following replacements: 

  * OPERATION_NAME: the name of the operation as returned by the Video Intelligence API. The operation name has the format `projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID`
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
    
    
    // Object tracking annotations are returned as a objectAnnotations list.
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress",
        "annotationProgress": [
          {
            "inputUri": "/cloud-ml-sandbox/video/chicago.mp4",
            "progressPercent": 100,
            "startTime": "2019-12-21T16:56:46.755199Z",
            "updateTime": "2019-12-21T16:59:17.911197Z"
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
        "annotationResults": [
          {
            "inputUri": "/cloud-ml-sandbox/video/chicago.mp4",
            "objectAnnotations": [
              {
                "entity": {
                  "entityId": "/m/0k4j",
                  "description": "car",
                  "languageCode": "en-US"
                },
                "frames": [
                  {
                    "normalizedBoundingBox": {
                      "left": 0.2672763,
                      "top": 0.5677657,
                      "right": 0.4388713,
                      "bottom": 0.7623171
                    },
                    "timeOffset": "0s"
                  },
                  {
                    "normalizedBoundingBox": {
                      "left": 0.26920167,
                      "top": 0.5659805,
                      "right": 0.44331276,
                      "bottom": 0.76780635
                    },
                    "timeOffset": "0.100495s"
                  },
               ...
                  {
                    "normalizedBoundingBox": {
                      "left": 0.83573246,
                      "top": 0.6645812,
                      "right": 1,
                      "bottom": 0.99865407
                    },
                    "timeOffset": "2.311402s"
                  }
                ],
                "segment": {
                  "startTimeOffset": "0s",
                  "endTimeOffset": "2.311402s"
                },
                "confidence": 0.99488896
              },
            ...
              {
                "entity": {
                  "entityId": "/m/0cgh4",
                  "description": "building",
                  "languageCode": "en-US"
                },
                "frames": [
                  {
                    "normalizedBoundingBox": {
                      "left": 0.12340179,
                      "top": 0.010383379,
                      "right": 0.21914443,
                      "bottom": 0.5591795
                    },
                    "timeOffset": "0s"
                  },
                  {
                    "normalizedBoundingBox": {
                      "left": 0.12340179,
                      "top": 0.009684974,
                      "right": 0.22915152,
                      "bottom": 0.56070584
                    },
                    "timeOffset": "0.100495s"
                  },
               ...
                  {
                    "normalizedBoundingBox": {
                      "left": 0.12340179,
                      "top": 0.008624528,
                      "right": 0.22723165,
                      "bottom": 0.56158626
                    },
                    "timeOffset": "0.401983s"
                  }
                ],
                "segment": {
                  "startTimeOffset": "0s",
                  "endTimeOffset": "0.401983s"
                },
                "confidence": 0.33914912
              },
           ...
              {
                "entity": {
                  "entityId": "/m/0cgh4",
                  "description": "building",
                  "languageCode": "en-US"
                },
                "frames": [
                  {
                    "normalizedBoundingBox": {
                      "left": 0.79324204,
                      "top": 0.0006896425,
                      "right": 0.99659824,
                      "bottom": 0.5324423
                    },
                    "timeOffset": "37.585421s"
                  },
                  {
                    "normalizedBoundingBox": {
                      "left": 0.78935236,
                      "top": 0.0011992548,
                      "right": 0.99659824,
                      "bottom": 0.5374946
                    },
                    "timeOffset": "37.685917s"
                  },
               ...
                  {
                    "normalizedBoundingBox": {
                      "left": 0.79404694,
                      "right": 0.99659824,
                      "bottom": 0.5280966
                    },
                    "timeOffset": "38.590379s"
                  }
                ],
                "segment": {
                  "startTimeOffset": "37.585421s",
                  "endTimeOffset": "38.590379s"
                },
                "confidence": 0.3415429
              }
            ]
          }
        ]
      }
    }
    

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
    
    // objectTrackingGCS analyzes a video and extracts entities with their bounding boxes.
    func objectTrackingGCS(w io.Writer, gcsURI string) error {
    	// gcsURI := "gs://cloud-samples-data/video/cat.mp4"
    
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
    			videopb.Feature_OBJECT_TRACKING,
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
    
    	for _, annotation := range result.ObjectAnnotations {
    		fmt.Fprintf(w, "Description: %q\n", annotation.Entity.GetDescription())
    		if len(annotation.Entity.EntityId) > 0 {
    			fmt.Fprintf(w, "\tEntity ID: %q\n", annotation.Entity.GetEntityId())
    		}
    
    		segment := annotation.GetSegment()
    		start, _ := ptypes.Duration(segment.GetStartTimeOffset())
    		end, _ := ptypes.Duration(segment.GetEndTimeOffset())
    		fmt.Fprintf(w, "\tSegment: %v to %v\n", start, end)
    
    		fmt.Fprintf(w, "\tConfidence: %f\n", annotation.GetConfidence())
    
    		// Here we print only the bounding box of the first frame in this segment.
    		frame := annotation.GetFrames()[0]
    		seconds := float32(frame.GetTimeOffset().GetSeconds())
    		nanos := float32(frame.GetTimeOffset().GetNanos())
    		fmt.Fprintf(w, "\tTime offset of the first frame: %fs\n", seconds+nanos/1e9)
    
    		box := frame.GetNormalizedBoundingBox()
    		fmt.Fprintf(w, "\tBounding box position:\n")
    		fmt.Fprintf(w, "\t\tleft  : %f\n", box.GetLeft())
    		fmt.Fprintf(w, "\t\ttop   : %f\n", box.GetTop())
    		fmt.Fprintf(w, "\t\tright : %f\n", box.GetRight())
    		fmt.Fprintf(w, "\t\tbottom: %f\n", box.GetBottom())
    	}
    
    	return nil
    }
    

### Java
    
    
    /**
     * Track objects in a video.
     *
     * @param gcsUri the path to the video file to analyze.
     */
    public static VideoAnnotationResults trackObjectsGcs(String gcsUri) throws Exception {
      try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
        // Create the request
        AnnotateVideoRequest request =
            AnnotateVideoRequest.newBuilder()
                .setInputUri(gcsUri)
                .addFeatures(Feature.OBJECT_TRACKING)
                .setLocationId("us-east1")
                .build();
    
        // asynchronously perform object tracking on videos
        OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
            client.annotateVideoAsync(request);
    
        System.out.println("Waiting for operation to complete...");
        // The first result is retrieved because a single video was processed.
        AnnotateVideoResponse response = future.get(450, TimeUnit.SECONDS);
        VideoAnnotationResults results = response.getAnnotationResults(0);
    
        // Get only the first annotation for demo purposes.
        ObjectTrackingAnnotation annotation = results.getObjectAnnotations(0);
        System.out.println("Confidence: " + annotation.getConfidence());
    
        if (annotation.hasEntity()) {
          Entity entity = annotation.getEntity();
          System.out.println("Entity description: " + entity.getDescription());
          System.out.println("Entity id:: " + entity.getEntityId());
        }
    
        if (annotation.hasSegment()) {
          VideoSegment videoSegment = annotation.getSegment();
          Duration startTimeOffset = videoSegment.getStartTimeOffset();
          Duration endTimeOffset = videoSegment.getEndTimeOffset();
          // Display the segment time in seconds, 1e9 converts nanos to seconds
          System.out.println(
              String.format(
                  "Segment: %.2fs to %.2fs",
                  startTimeOffset.getSeconds() + startTimeOffset.getNanos() / 1e9,
                  endTimeOffset.getSeconds() + endTimeOffset.getNanos() / 1e9));
        }
    
        // Here we print only the bounding box of the first frame in this segment.
        ObjectTrackingFrame frame = annotation.getFrames(0);
        // Display the offset time in seconds, 1e9 converts nanos to seconds
        Duration timeOffset = frame.getTimeOffset();
        System.out.println(
            String.format(
                "Time offset of the first frame: %.2fs",
                timeOffset.getSeconds() + timeOffset.getNanos() / 1e9));
    
        // Display the bounding box of the detected object
        NormalizedBoundingBox normalizedBoundingBox = frame.getNormalizedBoundingBox();
        System.out.println("Bounding box position:");
        System.out.println("\tleft: " + normalizedBoundingBox.getLeft());
        System.out.println("\ttop: " + normalizedBoundingBox.getTop());
        System.out.println("\tright: " + normalizedBoundingBox.getRight());
        System.out.println("\tbottom: " + normalizedBoundingBox.getBottom());
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
      features: ['OBJECT_TRACKING'],
      //recommended to use us-east1 for the best latency due to different types of processors used in this region and others
      locationId: 'us-east1',
    };
    // Detects objects in a video
    const [operation] = await video.annotateVideo(request);
    const results = await operation.promise();
    console.log('Waiting for operation to complete...');
    //Gets annotations for video
    const annotations = results[0].annotationResults[0];
    const objects = annotations.objectAnnotations;
    objects.forEach(object => {
      console.log(`Entity description:  ${object.entity.description}`);
      console.log(`Entity id: ${object.entity.entityId}`);
      const time = object.segment;
      console.log(
        `Segment: ${time.startTimeOffset.seconds || 0}` +
          `.${(time.startTimeOffset.nanos / 1e6).toFixed(0)}s to ${
            time.endTimeOffset.seconds || 0
          }.` +
          `${(time.endTimeOffset.nanos / 1e6).toFixed(0)}s`
      );
      console.log(`Confidence: ${object.confidence}`);
      const frame = object.frames[0];
      const box = frame.normalizedBoundingBox;
      const timeOffset = frame.timeOffset;
      console.log(
        `Time offset for the first frame: ${timeOffset.seconds || 0}` +
          `.${(timeOffset.nanos / 1e6).toFixed(0)}s`
      );
      console.log('Bounding box position:');
      console.log(` left   :${box.left}`);
      console.log(` top    :${box.top}`);
      console.log(` right  :${box.right}`);
      console.log(` bottom :${box.bottom}`);
    });

### Python
    
    
    """Object tracking in a video stored on GCS."""
    from google.cloud import videointelligence
    
    video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
    features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).OBJECT_TRACKING]
    operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
        request={"features": features, "input_uri": gcs_uri}
    )
    print("\nProcessing video for object annotations.")
    
    result = operation.result(timeout=500)
    print("\nFinished processing.\n")
    
    # The first result is retrieved because a single video was processed.
    object_annotations = result.annotation_results[0].object_annotations
    
    for object_annotation in object_annotations:
        print("Entity description: {}".format(object_annotation.entity.description))
        if object_annotation.entity.entity_id:
            print("Entity id: {}".format(object_annotation.entity.entity_id))
    
        print(
            "Segment: {}s to {}s".format(
                object_annotation.segment.start_time_offset.seconds
                + object_annotation.segment.start_time_offset.microseconds / 1e6,
                object_annotation.segment.end_time_offset.seconds
                + object_annotation.segment.end_time_offset.microseconds / 1e6,
            )
        )
    
        print("Confidence: {}".format(object_annotation.confidence))
    
        # Here we print only the bounding box of the first frame in the segment
        frame = object_annotation.frames[0]
        box = frame.normalized_bounding_box
        print(
            "Time offset of the first frame: {}s".format(
                frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
            )
        )
        print("Bounding box position:")
        print("\tleft  : {}".format(box.left))
        print("\ttop   : {}".format(box.top))
        print("\tright : {}".format(box.right))
        print("\tbottom: {}".format(box.bottom))
        print("\n")

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

## Request object tracking for video from a local file

The following samples demonstrate object tracking on a file stored locally.

### REST

### Send the process request

To perform annotation on a local video file, base64-encode the contents of the video file. Include the base64-encoded contents in the `inputContent` field of the request. For information on how to base64-encode the contents of a video file, see [Base64 Encoding](https://docs.cloud.google.com/video-intelligence/docs/base64).

The following shows how to send a `POST` request to the [`videos:annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. The example uses the access token for a service account set up for the project using the Google Cloud CLI. For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Video Intelligence quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts).

Before using any of the request data, make the following replacements: 

  * inputContent: BASE64_ENCODED_CONTENT  
For example: `"UklGRg41AwBBVkkgTElTVAwBAABoZHJsYXZpaDgAAAA1ggAAxPMBAAAAAAAQCAA..."`  

  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputContent": "BASE64_ENCODED_CONTENT",
      "features": ["OBJECT_TRACKING"]
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

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID"
    }
    

If the request is successful, Video Intelligence the `name` for your operation. The following shows an example of such a response, where `PROJECT_NUMBER` is the number of your project and `OPERATION_ID` is the ID of the long-running operation created for the request.

### Get the results

To get the results of your request, you must send a `GET`, using the operation name returned from the call to `videos:annotate`, as shown in the following example.

**Note:** The `"done"` field is only returned when its value is `True`. It is not included in responses for which the operation has not completed.

Before using any of the request data, make the following replacements: 

  * OPERATION_NAME: the name of the operation as returned by the Video Intelligence API. The operation name has the format `projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID `
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
    
    
    // Object tracking annotations are returned as a objectAnnotations list.
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress",
        "annotationProgress": [
          {
            "inputContent": "UklGRg41AwBBVkkgTElTVAwBAABoZHJsYXZpaDgAAAA1ggAAxPMBAAAAAAAQCAA...",
            "progressPercent": 100,
            "startTime": "2018-06-21T16:56:46.755199Z",
            "updateTime": "2018-06-21T16:59:17.911197Z"
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
        "annotationResults": [
          {
            "inputContent": "/cloud-ml-sandbox/video/chicago.mp4",
            "objectAnnotations": [
              {
                "entity": {
                  "entityId": "/m/0k4j",
                  "description": "car",
                  "languageCode": "en-US"
                },
                "frames": [
                  {
                    "normalizedBoundingBox": {
                      "left": 0.2672763,
                      "top": 0.5677657,
                      "right": 0.4388713,
                      "bottom": 0.7623171
                    },
                    "timeOffset": "0s"
                  },
                  {
                    "normalizedBoundingBox": {
                      "left": 0.26920167,
                      "top": 0.5659805,
                      "right": 0.44331276,
                      "bottom": 0.76780635
                    },
                    "timeOffset": "0.100495s"
                  },
               ...
                  {
                    "normalizedBoundingBox": {
                      "left": 0.83573246,
                      "top": 0.6645812,
                      "right": 1,
                      "bottom": 0.99865407
                    },
                    "timeOffset": "2.311402s"
                  }
                ],
                "segment": {
                  "startTimeOffset": "0s",
                  "endTimeOffset": "2.311402s"
                },
                "confidence": 0.99488896
              },
            ...
              {
                "entity": {
                  "entityId": "/m/0cgh4",
                  "description": "building",
                  "languageCode": "en-US"
                },
                "frames": [
                  {
                    "normalizedBoundingBox": {
                      "left": 0.12340179,
                      "top": 0.010383379,
                      "right": 0.21914443,
                      "bottom": 0.5591795
                    },
                    "timeOffset": "0s"
                  },
                  {
                    "normalizedBoundingBox": {
                      "left": 0.12340179,
                      "top": 0.009684974,
                      "right": 0.22915152,
                      "bottom": 0.56070584
                    },
                    "timeOffset": "0.100495s"
                  },
               ...
                  {
                    "normalizedBoundingBox": {
                      "left": 0.12340179,
                      "top": 0.008624528,
                      "right": 0.22723165,
                      "bottom": 0.56158626
                    },
                    "timeOffset": "0.401983s"
                  }
                ],
                "segment": {
                  "startTimeOffset": "0s",
                  "endTimeOffset": "0.401983s"
                },
                "confidence": 0.33914912
              },
           ...
              {
                "entity": {
                  "entityId": "/m/0cgh4",
                  "description": "building",
                  "languageCode": "en-US"
                },
                "frames": [
                  {
                    "normalizedBoundingBox": {
                      "left": 0.79324204,
                      "top": 0.0006896425,
                      "right": 0.99659824,
                      "bottom": 0.5324423
                    },
                    "timeOffset": "37.585421s"
                  },
                  {
                    "normalizedBoundingBox": {
                      "left": 0.78935236,
                      "top": 0.0011992548,
                      "right": 0.99659824,
                      "bottom": 0.5374946
                    },
                    "timeOffset": "37.685917s"
                  },
               ...
                  {
                    "normalizedBoundingBox": {
                      "left": 0.79404694,
                      "right": 0.99659824,
                      "bottom": 0.5280966
                    },
                    "timeOffset": "38.590379s"
                  }
                ],
                "segment": {
                  "startTimeOffset": "37.585421s",
                  "endTimeOffset": "38.590379s"
                },
                "confidence": 0.3415429
              }
            ]
          }
        ]
      }
    }
    

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
    
    // objectTracking analyzes a video and extracts entities with their bounding boxes.
    func objectTracking(w io.Writer, filename string) error {
    	// filename := "../testdata/cat.mp4"
    
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := video.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("video.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_Close)()
    
    	fileBytes, err := os.ReadFile(filename)
    	if err != nil {
    		return err
    	}
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		InputContent: fileBytes,
    		Features: []videopb.Feature{
    			videopb.Feature_OBJECT_TRACKING,
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
    
    	for _, annotation := range result.ObjectAnnotations {
    		fmt.Fprintf(w, "Description: %q\n", annotation.Entity.GetDescription())
    		if len(annotation.Entity.EntityId) > 0 {
    			fmt.Fprintf(w, "\tEntity ID: %q\n", annotation.Entity.GetEntityId())
    		}
    
    		segment := annotation.GetSegment()
    		start, _ := ptypes.Duration(segment.GetStartTimeOffset())
    		end, _ := ptypes.Duration(segment.GetEndTimeOffset())
    		fmt.Fprintf(w, "\tSegment: %v to %v\n", start, end)
    
    		fmt.Fprintf(w, "\tConfidence: %f\n", annotation.GetConfidence())
    
    		// Here we print only the bounding box of the first frame in this segment.
    		frame := annotation.GetFrames()[0]
    		seconds := float32(frame.GetTimeOffset().GetSeconds())
    		nanos := float32(frame.GetTimeOffset().GetNanos())
    		fmt.Fprintf(w, "\tTime offset of the first frame: %fs\n", seconds+nanos/1e9)
    
    		box := frame.GetNormalizedBoundingBox()
    		fmt.Fprintf(w, "\tBounding box position:\n")
    		fmt.Fprintf(w, "\t\tleft  : %f\n", box.GetLeft())
    		fmt.Fprintf(w, "\t\ttop   : %f\n", box.GetTop())
    		fmt.Fprintf(w, "\t\tright : %f\n", box.GetRight())
    		fmt.Fprintf(w, "\t\tbottom: %f\n", box.GetBottom())
    	}
    
    	return nil
    }
    

### Java
    
    
    /**
     * Track objects in a video.
     *
     * @param filePath the path to the video file to analyze.
     */
    public static VideoAnnotationResults trackObjects(String filePath) throws Exception {
      try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
        // Read file
        Path path = Paths.get(filePath);
        byte[] data = Files.readAllBytes(path);
    
        // Create the request
        AnnotateVideoRequest request =
            AnnotateVideoRequest.newBuilder()
                .setInputContent(ByteString.copyFrom(data))
                .addFeatures(Feature.OBJECT_TRACKING)
                .setLocationId("us-east1")
                .build();
    
        // asynchronously perform object tracking on videos
        OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
            client.annotateVideoAsync(request);
    
        System.out.println("Waiting for operation to complete...");
        // The first result is retrieved because a single video was processed.
        AnnotateVideoResponse response = future.get(450, TimeUnit.SECONDS);
        VideoAnnotationResults results = response.getAnnotationResults(0);
    
        // Get only the first annotation for demo purposes.
        ObjectTrackingAnnotation annotation = results.getObjectAnnotations(0);
        System.out.println("Confidence: " + annotation.getConfidence());
    
        if (annotation.hasEntity()) {
          Entity entity = annotation.getEntity();
          System.out.println("Entity description: " + entity.getDescription());
          System.out.println("Entity id:: " + entity.getEntityId());
        }
    
        if (annotation.hasSegment()) {
          VideoSegment videoSegment = annotation.getSegment();
          Duration startTimeOffset = videoSegment.getStartTimeOffset();
          Duration endTimeOffset = videoSegment.getEndTimeOffset();
          // Display the segment time in seconds, 1e9 converts nanos to seconds
          System.out.println(
              String.format(
                  "Segment: %.2fs to %.2fs",
                  startTimeOffset.getSeconds() + startTimeOffset.getNanos() / 1e9,
                  endTimeOffset.getSeconds() + endTimeOffset.getNanos() / 1e9));
        }
    
        // Here we print only the bounding box of the first frame in this segment.
        ObjectTrackingFrame frame = annotation.getFrames(0);
        // Display the offset time in seconds, 1e9 converts nanos to seconds
        Duration timeOffset = frame.getTimeOffset();
        System.out.println(
            String.format(
                "Time offset of the first frame: %.2fs",
                timeOffset.getSeconds() + timeOffset.getNanos() / 1e9));
    
        // Display the bounding box of the detected object
        NormalizedBoundingBox normalizedBoundingBox = frame.getNormalizedBoundingBox();
        System.out.println("Bounding box position:");
        System.out.println("\tleft: " + normalizedBoundingBox.getLeft());
        System.out.println("\ttop: " + normalizedBoundingBox.getTop());
        System.out.println("\tright: " + normalizedBoundingBox.getRight());
        System.out.println("\tbottom: " + normalizedBoundingBox.getBottom());
        return results;
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Video Intelligence library
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
      features: ['OBJECT_TRACKING'],
      //recommended to use us-east1 for the best latency due to different types of processors used in this region and others
      locationId: 'us-east1',
    };
    // Detects objects in a video
    const [operation] = await video.annotateVideo(request);
    const results = await operation.promise();
    console.log('Waiting for operation to complete...');
    //Gets annotations for video
    const annotations = results[0].annotationResults[0];
    const objects = annotations.objectAnnotations;
    objects.forEach(object => {
      console.log(`Entity description:  ${object.entity.description}`);
      console.log(`Entity id: ${object.entity.entityId}`);
      const time = object.segment;
      console.log(
        `Segment: ${time.startTimeOffset.seconds || 0}` +
          `.${(time.startTimeOffset.nanos / 1e6).toFixed(0)}s to ${
            time.endTimeOffset.seconds || 0
          }.` +
          `${(time.endTimeOffset.nanos / 1e6).toFixed(0)}s`
      );
      console.log(`Confidence: ${object.confidence}`);
      const frame = object.frames[0];
      const box = frame.normalizedBoundingBox;
      const timeOffset = frame.timeOffset;
      console.log(
        `Time offset for the first frame: ${timeOffset.seconds || 0}` +
          `.${(timeOffset.nanos / 1e6).toFixed(0)}s`
      );
      console.log('Bounding box position:');
      console.log(` left   :${box.left}`);
      console.log(` top    :${box.top}`);
      console.log(` right  :${box.right}`);
      console.log(` bottom :${box.bottom}`);
    });

### Python
    
    
    """Object tracking in a local video."""
    from google.cloud import videointelligence
    
    video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
    features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).OBJECT_TRACKING]
    
    with io.open(path, "rb") as file:
        input_content = file.read()
    
    operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
        request={"features": features, "input_content": input_content}
    )
    print("\nProcessing video for object annotations.")
    
    result = operation.result(timeout=500)
    print("\nFinished processing.\n")
    
    # The first result is retrieved because a single video was processed.
    object_annotations = result.annotation_results[0].object_annotations
    
    # Get only the first annotation for demo purposes.
    object_annotation = object_annotations[0]
    print("Entity description: {}".format(object_annotation.entity.description))
    if object_annotation.entity.entity_id:
        print("Entity id: {}".format(object_annotation.entity.entity_id))
    
    print(
        "Segment: {}s to {}s".format(
            object_annotation.segment.start_time_offset.seconds
            + object_annotation.segment.start_time_offset.microseconds / 1e6,
            object_annotation.segment.end_time_offset.seconds
            + object_annotation.segment.end_time_offset.microseconds / 1e6,
        )
    )
    
    print("Confidence: {}".format(object_annotation.confidence))
    
    # Here we print only the bounding box of the first frame in this segment
    frame = object_annotation.frames[0]
    box = frame.normalized_bounding_box
    print(
        "Time offset of the first frame: {}s".format(
            frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
        )
    )
    print("Bounding box position:")
    print("\tleft  : {}".format(box.left))
    print("\ttop   : {}".format(box.top))
    print("\tright : {}".format(box.right))
    print("\tbottom: {}".format(box.bottom))
    print("\n")

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
