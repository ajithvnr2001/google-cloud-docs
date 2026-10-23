---
url: https://docs.cloud.google.com/video-intelligence/docs/logo-recognition/
title: Recognize logos \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:54.788876+00:00
---

# Recognize logos  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/logo-recognition/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Recognize logos Stay organized with collections  Save and categorize content based on your preferences. 

The Video Intelligence API can detect, track, and recognize the presence of over 100,000 brands and logos in video content.

This page describes how to recognize a logo in a video using the Video Intelligence API.

## Annotate a video in Cloud Storage

The following code sample demonstrates how to detect logos in a video in Cloud Storage.

### REST

### Send the process request

To perform annotation on a local video file, base64-encode the contents of the video file. Include the base64-encoded contents in the `inputContent` field of the request. For information on how to base64-encode the contents of a video file, see [Base64 Encoding](https://docs.cloud.google.com/video-intelligence/docs/base64).

The following shows how to send a `POST` request to the [`videos:annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. The example uses the access token for a service account set up for the project using the Google Cloud CLI. For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Video Intelligence quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts).

Before using any of the request data, make the following replacements: 

  * INPUT_URI: a Cloud Storage bucket that contains the file you want to annotate, including the file name. Must start with `gs://`.  
For example:  
`"inputUri": "gs://cloud-videointelligence-demo/assistant.mp4",`
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
        "inputUri":"INPUT_URI",
        "features": ["LOGO_RECOGNITION"]
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



### Get the results

To get the results of your request, you send a `GET` request, using the operation name returned from the call to `videos:annotate`, as shown in the following example.

Before using any of the request data, make the following replacements: 

  * OPERATION_NAME: the name of the operation as returned by Video Intelligence API. The operation name has the format `projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID`
Note: The **done** field is returned only when its value is **True**. It's not included in responses for which the operation has not completed.
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
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress",
        "annotationProgress": [
         {
          "inputUri": "/cloud-samples-data/video/googlework_short.mp4",
          "progressPercent": 100,
          "startTime": "2020-02-31T16:27:44.889439Z",
          "updateTime": "2020-02-31T16:27:56.526050Z"
         }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
        "annotationResults": [
          {
            "inputUri": "/cloud-samples-data/video/googlework_short.mp4",
            "segment": {
              "startTimeOffset": "0s",
              "endTimeOffset": "34.234200s"
            },
            "logoRecognitionAnnotations": [{
              "entity": {
                "entityId": "/m/045c7b",
                "description": "Google",
                "languageCode": "en-US"
              },
              "tracks": [{
                  "segment": {
                    "startTimeOffset": "10.543866s",
                    "endTimeOffset": "12.345666s"
                  },
                  "timestampedObjects": [{
                      "normalizedBoundingBox": {
                        "left": 0.3912032,
                        "top": 0.26212785,
                        "right": 0.6469412,
                        "bottom": 0.4434373
                      },
                      "timeOffset": "10.543866s"
                    },
                    ...
                  ],
                  "confidence": 0.8588119
                },
                {
                  "segment": {
                    "startTimeOffset": "15.348666s",
                    "endTimeOffset": "18.752066s"
                  },
                  "timestampedObjects": [
                    {
                      "normalizedBoundingBox": {
                        "left": 0.69989866,
                        "top": 0.79943377,
                        "right": 0.76465744,
                        "bottom": 0.9271479
                      },
                      "timeOffset": "15.348666s"
                     },
                     {
                      "normalizedBoundingBox": {
                        "left": 0.68997324,
                        "top": 0.78775305,
                        "right": 0.75723547,
                        "bottom": 0.91808647
                      },
                      "timeOffset": "15.448766s"
                    },
                    ...
                  }
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

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	video "cloud.google.com/go/videointelligence/apiv1"
    	videopb "cloud.google.com/go/videointelligence/apiv1/videointelligencepb"
    	"github.com/golang/protobuf/ptypes"
    )
    
    // logoDetectionGCS analyzes a video and extracts logos with their bounding boxes.
    func logoDetectionGCS(w io.Writer, gcsURI string) error {
    	// gcsURI := "gs://cloud-samples-data/video/googlework_tiny.mp4"
    
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := video.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("video.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_Close)()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*180)
    	defer cancel()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		InputUri: gcsURI,
    		Features: []videopb.Feature{
    			videopb.Feature_LOGO_RECOGNITION,
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
    
    	// Annotations for list of logos detected, tracked and recognized in video.
    	for _, annotation := range result.LogoRecognitionAnnotations {
    		fmt.Fprintf(w, "Description: %q\n", annotation.Entity.GetDescription())
    		// Opaque entity ID. Some IDs may be available in Google Knowledge
    		// Graph Search API (https://developers.google.com/knowledge-graph/).
    		if len(annotation.Entity.EntityId) > 0 {
    			fmt.Fprintf(w, "\tEntity ID: %q\n", annotation.Entity.GetEntityId())
    		}
    
    		// All logo tracks where the recognized logo appears. Each track
    		// corresponds to one logo instance appearing in consecutive frames.
    		for _, track := range annotation.Tracks {
    			// Video segment of a track.
    			segment := track.GetSegment()
    			start, _ := ptypes.Duration(segment.GetStartTimeOffset())
    			end, _ := ptypes.Duration(segment.GetEndTimeOffset())
    			fmt.Fprintf(w, "\tSegment: %v to %v\n", start, end)
    			fmt.Fprintf(w, "\tConfidence: %f\n", track.GetConfidence())
    
    			// The object with timestamp and attributes per frame in the track.
    			for _, timestampedObject := range track.TimestampedObjects {
    				// Normalized Bounding box in a frame, where the object is
    				// located.
    				box := timestampedObject.GetNormalizedBoundingBox()
    				fmt.Fprintf(w, "\tBounding box position:\n")
    				fmt.Fprintf(w, "\t\tleft  : %f\n", box.GetLeft())
    				fmt.Fprintf(w, "\t\ttop   : %f\n", box.GetTop())
    				fmt.Fprintf(w, "\t\tright : %f\n", box.GetRight())
    				fmt.Fprintf(w, "\t\tbottom: %f\n", box.GetBottom())
    
    				// Optional. The attributes of the object in the bounding box.
    				for _, attribute := range timestampedObject.Attributes {
    					fmt.Fprintf(w, "\t\t\tName: %q\n", attribute.GetName())
    					fmt.Fprintf(w, "\t\t\tConfidence: %f\n", attribute.GetConfidence())
    					fmt.Fprintf(w, "\t\t\tValue: %q\n", attribute.GetValue())
    				}
    			}
    
    			// Optional. Attributes in the track level.
    			for _, trackAttribute := range track.Attributes {
    				fmt.Fprintf(w, "\t\tName: %q\n", trackAttribute.GetName())
    				fmt.Fprintf(w, "\t\tConfidence: %f\n", trackAttribute.GetConfidence())
    				fmt.Fprintf(w, "\t\tValue: %q\n", trackAttribute.GetValue())
    			}
    		}
    
    		// All video segments where the recognized logo appears. There might be
    		// multiple instances of the same logo class appearing in one VideoSegment.
    		for _, segment := range annotation.Segments {
    			start, _ := ptypes.Duration(segment.GetStartTimeOffset())
    			end, _ := ptypes.Duration(segment.GetEndTimeOffset())
    			fmt.Fprintf(w, "\tSegment: %v to %v\n", start, end)
    		}
    	}
    
    	return nil
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html);
    import com.google.cloud.videointelligence.v1.[DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html);
    import com.google.cloud.videointelligence.v1.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html);
    import com.google.cloud.videointelligence.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html);
    import com.google.cloud.videointelligence.v1.[LogoRecognitionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LogoRecognitionAnnotation.html);
    import com.google.cloud.videointelligence.v1.[NormalizedBoundingBox](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html);
    import com.google.cloud.videointelligence.v1.[TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html);
    import com.google.cloud.videointelligence.v1.[Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html);
    import com.google.cloud.videointelligence.v1.[VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html);
    import com.google.cloud.videointelligence.v1.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html);
    import com.google.cloud.videointelligence.v1.[VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class LogoDetectionGcs {
    
      public static void detectLogoGcs() throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String gcsUri = "gs://YOUR_BUCKET_ID/path/to/your/video.mp4";
        detectLogoGcs(gcsUri);
      }
    
      public static void detectLogoGcs(String inputUri)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html) client = [VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html).create()) {
          // Create the request
          [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html) request =
              [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html).newBuilder()
                  .setInputUri(inputUri)
                  .[addFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_addFeatures_com_google_cloud_videointelligence_v1_Feature_)([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html).LOGO_RECOGNITION)
                  .build();
    
          // asynchronously perform object tracking on videos
          OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
              client.[annotateVideoAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html#com_google_cloud_videointelligence_v1_VideoIntelligenceServiceClient_annotateVideoAsync_com_google_cloud_videointelligence_v1_AnnotateVideoRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
          // The first result is retrieved because a single video was processed.
          [AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html) response = future.get(600, TimeUnit.SECONDS);
          [VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html) annotationResult = response.[getAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html#com_google_cloud_videointelligence_v1_AnnotateVideoResponse_getAnnotationResults_int_)(0);
    
          // Annotations for list of logos detected, tracked and recognized in video.
          for ([LogoRecognitionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LogoRecognitionAnnotation.html) logoRecognitionAnnotation :
              annotationResult.[getLogoRecognitionAnnotationsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html#com_google_cloud_videointelligence_v1_VideoAnnotationResults_getLogoRecognitionAnnotationsList__)()) {
            [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html) entity = logoRecognitionAnnotation.getEntity();
            // Opaque entity ID. Some IDs may be available in
            // [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).
            System.out.printf("Entity Id : %s\n", entity.[getEntityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html#com_google_cloud_videointelligence_v1_Entity_getEntityId__)());
            System.out.printf("Description : %s\n", entity.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html#com_google_cloud_videointelligence_v1_Entity_getDescription__)());
            // All logo tracks where the recognized logo appears. Each track corresponds to one logo
            // instance appearing in consecutive frames.
            for ([Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html) track : logoRecognitionAnnotation.getTracksList()) {
    
              // Video segment of a track.
              [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) startTimeOffset = track.getSegment().getStartTimeOffset();
              System.out.printf(
                  "\n\tStart Time Offset: %s.%s\n",
                  startTimeOffset.[getSeconds](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getSeconds__)(), startTimeOffset.[getNanos](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getNanos__)());
              [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) endTimeOffset = track.getSegment().getEndTimeOffset();
              System.out.printf(
                  "\tEnd Time Offset: %s.%s\n", endTimeOffset.[getSeconds](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getSeconds__)(), endTimeOffset.[getNanos](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getNanos__)());
              System.out.printf("\tConfidence: %s\n", track.getConfidence());
    
              // The object with timestamp and attributes per frame in the track.
              for ([TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html) timestampedObject : track.getTimestampedObjectsList()) {
    
                // Normalized Bounding box in a frame, where the object is located.
                [NormalizedBoundingBox](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html) normalizedBoundingBox =
                    timestampedObject.getNormalizedBoundingBox();
                System.out.printf("\n\t\tLeft: %s\n", normalizedBoundingBox.[getLeft](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html#com_google_cloud_videointelligence_v1_NormalizedBoundingBox_getLeft__)());
                System.out.printf("\t\tTop: %s\n", normalizedBoundingBox.[getTop](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html#com_google_cloud_videointelligence_v1_NormalizedBoundingBox_getTop__)());
                System.out.printf("\t\tRight: %s\n", normalizedBoundingBox.[getRight](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html#com_google_cloud_videointelligence_v1_NormalizedBoundingBox_getRight__)());
                System.out.printf("\t\tBottom: %s\n", normalizedBoundingBox.[getBottom](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html#com_google_cloud_videointelligence_v1_NormalizedBoundingBox_getBottom__)());
    
                // Optional. The attributes of the object in the bounding box.
                for ([DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html) attribute : timestampedObject.getAttributesList()) {
                  System.out.printf("\n\t\t\tName: %s\n", attribute.getName());
                  System.out.printf("\t\t\tConfidence: %s\n", attribute.getConfidence());
                  System.out.printf("\t\t\tValue: %s\n", attribute.getValue());
                }
              }
    
              // Optional. Attributes in the track level.
              for ([DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html) trackAttribute : track.getAttributesList()) {
                System.out.printf("\n\t\tName : %s\n", trackAttribute.getName());
                System.out.printf("\t\tConfidence : %s\n", trackAttribute.getConfidence());
                System.out.printf("\t\tValue : %s\n", trackAttribute.getValue());
              }
            }
    
            // All video segments where the recognized logo appears. There might be multiple instances
            // of the same logo class appearing in one VideoSegment.
            for ([VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html) segment : logoRecognitionAnnotation.getSegmentsList()) {
              System.out.printf(
                  "\n\tStart Time Offset : %s.%s\n",
                  segment.getStartTimeOffset().getSeconds(), segment.getStartTimeOffset().getNanos());
              System.out.printf(
                  "\tEnd Time Offset : %s.%s\n",
                  segment.getEndTimeOffset().getSeconds(), segment.getEndTimeOffset().getNanos());
            }
          }
        }
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const inputUri = 'gs://cloud-samples-data/video/googlework_short.mp4';
    
    // Imports the Google Cloud client libraries
    const Video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)');
    
    // Instantiates a client
    const client = new Video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    // Performs asynchronous video annotation for logo recognition on a file hosted in GCS.
    async function detectLogoGcs() {
      // Build the request with the input uri and logo recognition feature.
      const request = {
        inputUri: inputUri,
        features: ['LOGO_RECOGNITION'],
      };
    
      // Make the asynchronous request
      const [operation] = await client.annotateVideo(request);
    
      // Wait for the results
      const [response] = await operation.promise();
    
      // Get the first response, since we sent only one video.
      const annotationResult = response.annotationResults[0];
      for (const logoRecognitionAnnotation of annotationResult.logoRecognitionAnnotations) {
        const entity = logoRecognitionAnnotation.entity;
        // Opaque entity ID. Some IDs may be available in
        // [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).
        console.log(`Entity Id: ${entity.entityId}`);
        console.log(`Description: ${entity.description}`);
    
        // All logo tracks where the recognized logo appears.
        // Each track corresponds to one logo instance appearing in consecutive frames.
        for (const track of logoRecognitionAnnotation.tracks) {
          console.log(
            `\n\tStart Time Offset: ${track.segment.startTimeOffset.seconds}.${track.segment.startTimeOffset.nanos}`
          );
          console.log(
            `\tEnd Time Offset: ${track.segment.endTimeOffset.seconds}.${track.segment.endTimeOffset.nanos}`
          );
          console.log(`\tConfidence: ${track.confidence}`);
    
          // The object with timestamp and attributes per frame in the track.
          for (const timestampedObject of track.timestampedObjects) {
            // Normalized Bounding box in a frame, where the object is located.
            const normalizedBoundingBox = timestampedObject.normalizedBoundingBox;
            console.log(`\n\t\tLeft: ${normalizedBoundingBox.left}`);
            console.log(`\t\tTop: ${normalizedBoundingBox.top}`);
            console.log(`\t\tRight: ${normalizedBoundingBox.right}`);
            console.log(`\t\tBottom: ${normalizedBoundingBox.bottom}`);
            // Optional. The attributes of the object in the bounding box.
            for (const attribute of timestampedObject.attributes) {
              console.log(`\n\t\t\tName: ${attribute.name}`);
              console.log(`\t\t\tConfidence: ${attribute.confidence}`);
              console.log(`\t\t\tValue: ${attribute.value}`);
            }
          }
    
          // Optional. Attributes in the track level.
          for (const trackAttribute of track.attributes) {
            console.log(`\n\t\tName: ${trackAttribute.name}`);
            console.log(`\t\tConfidence: ${trackAttribute.confidence}`);
            console.log(`\t\tValue: ${trackAttribute.value}`);
          }
        }
    
        // All video segments where the recognized logo appears.
        // There might be multiple instances of the same logo class appearing in one VideoSegment.
        for (const segment of logoRecognitionAnnotation.segments) {
          console.log(
            `\n\tStart Time Offset: ${segment.startTimeOffset.seconds}.${segment.startTimeOffset.nanos}`
          );
          console.log(
            `\tEnd Time Offset: ${segment.endTimeOffset.seconds}.${segment.endTimeOffset.nanos}`
          );
        }
      }
    }
    
    detectLogoGcs();

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import videointelligence
    
    
    def detect_logo_gcs(input_uri="gs://YOUR_BUCKET_ID/path/to/your/file.mp4"):
        client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
    
        features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).LOGO_RECOGNITION]
    
        operation = client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
            request={"features": features, "input_uri": input_uri}
        )
    
        print("Waiting for operation to complete...")
        response = operation.result()
    
        # Get the first response, since we sent only one video.
        annotation_result = response.annotation_results[0]
    
        # Annotations for list of logos detected, tracked and recognized in video.
        for logo_recognition_annotation in annotation_result.logo_recognition_annotations:
            entity = logo_recognition_annotation.entity
    
            # Opaque entity ID. Some IDs may be available in [Google Knowledge Graph
            # Search API](https://developers.google.com/knowledge-graph/).
            print("Entity Id : {}".format(entity.entity_id))
    
            print("Description : {}".format(entity.description))
    
            # All logo tracks where the recognized logo appears. Each track corresponds
            # to one logo instance appearing in consecutive frames.
            for track in logo_recognition_annotation.tracks:
                # Video segment of a track.
                print(
                    "\n\tStart Time Offset : {}.{}".format(
                        track.segment.start_time_offset.seconds,
                        track.segment.start_time_offset.microseconds * 1000,
                    )
                )
                print(
                    "\tEnd Time Offset : {}.{}".format(
                        track.segment.end_time_offset.seconds,
                        track.segment.end_time_offset.microseconds * 1000,
                    )
                )
                print("\tConfidence : {}".format(track.confidence))
    
                # The object with timestamp and attributes per frame in the track.
                for timestamped_object in track.timestamped_objects:
                    # Normalized Bounding box in a frame, where the object is located.
                    normalized_bounding_box = timestamped_object.normalized_bounding_box
                    print("\n\t\tLeft : {}".format(normalized_bounding_box.left))
                    print("\t\tTop : {}".format(normalized_bounding_box.top))
                    print("\t\tRight : {}".format(normalized_bounding_box.right))
                    print("\t\tBottom : {}".format(normalized_bounding_box.bottom))
    
                    # Optional. The attributes of the object in the bounding box.
                    for attribute in timestamped_object.attributes:
                        print("\n\t\t\tName : {}".format(attribute.name))
                        print("\t\t\tConfidence : {}".format(attribute.confidence))
                        print("\t\t\tValue : {}".format(attribute.value))
    
                # Optional. Attributes in the track level.
                for track_attribute in track.attributes:
                    print("\n\t\tName : {}".format(track_attribute.name))
                    print("\t\tConfidence : {}".format(track_attribute.confidence))
                    print("\t\tValue : {}".format(track_attribute.value))
    
            # All video segments where the recognized logo appears. There might be
            # multiple instances of the same logo class appearing in one VideoSegment.
            for segment in logo_recognition_annotation.segments:
                print(
                    "\n\tStart Time Offset : {}.{}".format(
                        segment.start_time_offset.seconds,
                        segment.start_time_offset.microseconds * 1000,
                    )
                )
                print(
                    "\tEnd Time Offset : {}.{}".format(
                        segment.end_time_offset.seconds,
                        segment.end_time_offset.microseconds * 1000,
                    )
                )
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

## Annotate a local video

The following code sample demonstrates how to detect logos in a local video file.

### REST

### Send video annotation request

To perform annotation on a local video file, be sure to base64-encode the contents of the video file. Include the base64-encoded contents in the `inputContent` field of the request. For information on how to base64-encode the contents of a video file, see [Base64 Encoding](https://docs.cloud.google.com/video-intelligence/docs/base64).

The following shows how to send a POST request to the `videos:annotate` method. The example uses the access token for a service account set up for the project using the Google Cloud CLI. For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Video Intelligence API Quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts)

Before using any of the request data, make the following replacements: 

  * "inputContent": BASE64_ENCODED_CONTENT   
For example:  
`"UklGRg41AwBBVkkgTElTVAwBAABoZHJsYXZpaDgAAAA1ggAAxPMBAAAAAAAQCAA..."`  

  * LANGUAGE_CODE: [Optional] See [supported languages](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages)
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputContent": "BASE64_ENCODED_CONTENT",
      "features": ["LOGO_RECOGNITION"],
      "videoContext": {
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
    

If the response is successful, the Video Intelligence API returns the `name` for your operation. The above shows an example of such a response, where `project-number` is the name of your project and `operation-id` is the ID of the long running operation created for the request. 

  * OPERATION_ID: provided in the response when you started the operation, for example `12345...`



### Get annotation results

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
    
    
    "name": "projects/512816187662/locations/us-east1/operations/8399514592783793684",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1p3beta1.AnnotateVideoProgress",
        "annotationProgress": [
          {
            "inputUri": "/videointelligence-prober-videos/face.mkv",
            "progressPercent": 100,
            "startTime": "2020-03-18T19:45:17.725359Z",
            "updateTime": "2020-03-18T19:45:26.532315Z"
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1p3beta1.AnnotateVideoResponse",
        "annotationResults": [
          {
            "inputUri": "/videointelligence-prober-videos/face.mkv",
            "segment": {
              "startTimeOffset": "0s",
              "endTimeOffset": "10.010s"
            },
            "logoRecognitionAnnotations": [
              {
                "entity": {
                  "entityId": "/m/02z_b",
                  "description": "Fox News",
                  "languageCode": "en-US"
                },
                "tracks": [
                  {
                    "segment": {
                      "startTimeOffset": "0s",
                      "endTimeOffset": "1.901900s"
                    },
                    "timestampedObjects": [
                      {
                        "normalizedBoundingBox": {
                          "left": 0.032402553,
                          "top": 0.73683465,
                          "right": 0.16249886,
                          "bottom": 0.8664769
                        },
                        "timeOffset": "0s"
                      },
                      {
                        "normalizedBoundingBox": {
                          "left": 0.03267879,
                          "top": 0.73522913,
                          "right": 0.1627307,
                          "bottom": 0.86775583
                        },
                        "timeOffset": "0.100100s"
                      },
                      {
                        "normalizedBoundingBox": {
                          "left": 0.031819325,
                          "top": 0.73514116,
                          "right": 0.16305345,
                          "bottom": 0.8677738
                        },
                        "timeOffset": "0.200200s"
                      },
                      {
                        "normalizedBoundingBox": {
                          "left": 0.03155339,
                          "top": 0.7349258,
                          "right": 0.16275825,
                          "bottom": 0.86660737
                        },
                        "timeOffset": "0.300300s"
                      },
             ....
      ]
    }
    

Text detection annotations are returned as a `textAnnotations` list. Note: The **done** field is returned only when its value is **True**. It's not included in responses for which the operation has not completed. 

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    	"time"
    
    	video "cloud.google.com/go/videointelligence/apiv1"
    	videopb "cloud.google.com/go/videointelligence/apiv1/videointelligencepb"
    	"github.com/golang/protobuf/ptypes"
    )
    
    // logoDetection analyzes a video and extracts logos with their bounding boxes.
    func logoDetection(w io.Writer, filename string) error {
    	// filename := "../testdata/googlework_short.mp4"
    
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := video.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("video.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_Close)()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*180)
    	defer cancel()
    
    	fileBytes, err := os.ReadFile(filename)
    	if err != nil {
    		return fmt.Errorf("os.ReadFile: %w", err)
    	}
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		InputContent: fileBytes,
    		Features: []videopb.Feature{
    			videopb.Feature_LOGO_RECOGNITION,
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
    
    	// Annotations for list of logos detected, tracked and recognized in video.
    	for _, annotation := range result.LogoRecognitionAnnotations {
    		fmt.Fprintf(w, "Description: %q\n", annotation.Entity.GetDescription())
    		// Opaque entity ID. Some IDs may be available in Google Knowledge
    		// Graph Search API (https://developers.google.com/knowledge-graph/).
    		if len(annotation.Entity.EntityId) > 0 {
    			fmt.Fprintf(w, "\tEntity ID: %q\n", annotation.Entity.GetEntityId())
    		}
    
    		// All logo tracks where the recognized logo appears. Each track
    		// corresponds to one logo instance appearing in consecutive frames.
    		for _, track := range annotation.Tracks {
    			// Video segment of a track.
    			segment := track.GetSegment()
    			start, _ := ptypes.Duration(segment.GetStartTimeOffset())
    			end, _ := ptypes.Duration(segment.GetEndTimeOffset())
    			fmt.Fprintf(w, "\tSegment: %v to %v\n", start, end)
    			fmt.Fprintf(w, "\tConfidence: %f\n", track.GetConfidence())
    
    			// The object with timestamp and attributes per frame in the track.
    			for _, timestampedObject := range track.TimestampedObjects {
    				// Normalized Bounding box in a frame, where the object is
    				// located.
    				box := timestampedObject.GetNormalizedBoundingBox()
    				fmt.Fprintf(w, "\tBounding box position:\n")
    				fmt.Fprintf(w, "\t\tleft  : %f\n", box.GetLeft())
    				fmt.Fprintf(w, "\t\ttop   : %f\n", box.GetTop())
    				fmt.Fprintf(w, "\t\tright : %f\n", box.GetRight())
    				fmt.Fprintf(w, "\t\tbottom: %f\n", box.GetBottom())
    
    				// Optional. The attributes of the object in the bounding box.
    				for _, attribute := range timestampedObject.Attributes {
    					fmt.Fprintf(w, "\t\t\tName: %q\n", attribute.GetName())
    					fmt.Fprintf(w, "\t\t\tConfidence: %f\n", attribute.GetConfidence())
    					fmt.Fprintf(w, "\t\t\tValue: %q\n", attribute.GetValue())
    				}
    			}
    
    			// Optional. Attributes in the track level.
    			for _, trackAttribute := range track.Attributes {
    				fmt.Fprintf(w, "\t\tName: %q\n", trackAttribute.GetName())
    				fmt.Fprintf(w, "\t\tConfidence: %f\n", trackAttribute.GetConfidence())
    				fmt.Fprintf(w, "\t\tValue: %q\n", trackAttribute.GetValue())
    			}
    		}
    
    		// All video segments where the recognized logo appears. There might be
    		// multiple instances of the same logo class appearing in one VideoSegment.
    		for _, segment := range annotation.Segments {
    			start, _ := ptypes.Duration(segment.GetStartTimeOffset())
    			end, _ := ptypes.Duration(segment.GetEndTimeOffset())
    			fmt.Fprintf(w, "\tSegment: %v to %v\n", start, end)
    		}
    	}
    
    	return nil
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html);
    import com.google.cloud.videointelligence.v1.[DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html);
    import com.google.cloud.videointelligence.v1.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html);
    import com.google.cloud.videointelligence.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html);
    import com.google.cloud.videointelligence.v1.[LogoRecognitionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LogoRecognitionAnnotation.html);
    import com.google.cloud.videointelligence.v1.[NormalizedBoundingBox](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html);
    import com.google.cloud.videointelligence.v1.[TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html);
    import com.google.cloud.videointelligence.v1.[Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html);
    import com.google.cloud.videointelligence.v1.[VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html);
    import com.google.cloud.videointelligence.v1.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html);
    import com.google.cloud.videointelligence.v1.[VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class LogoDetection {
    
      public static void detectLogo() throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String localFilePath = "path/to/your/video.mp4";
        detectLogo(localFilePath);
      }
    
      public static void detectLogo(String filePath)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html) client = [VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html).create()) {
          // Read file
          Path path = Paths.get(filePath);
          byte[] data = Files.readAllBytes(path);
          // Create the request
          [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html) request =
              [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html).newBuilder()
                  .[setInputContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_setInputContent_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(data))
                  .[addFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_addFeatures_com_google_cloud_videointelligence_v1_Feature_)([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html).LOGO_RECOGNITION)
                  .build();
    
          // asynchronously perform object tracking on videos
          OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
              client.[annotateVideoAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html#com_google_cloud_videointelligence_v1_VideoIntelligenceServiceClient_annotateVideoAsync_com_google_cloud_videointelligence_v1_AnnotateVideoRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
          // The first result is retrieved because a single video was processed.
          [AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html) response = future.get(300, TimeUnit.SECONDS);
          [VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html) annotationResult = response.[getAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html#com_google_cloud_videointelligence_v1_AnnotateVideoResponse_getAnnotationResults_int_)(0);
    
          // Annotations for list of logos detected, tracked and recognized in video.
          for ([LogoRecognitionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LogoRecognitionAnnotation.html) logoRecognitionAnnotation :
              annotationResult.[getLogoRecognitionAnnotationsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html#com_google_cloud_videointelligence_v1_VideoAnnotationResults_getLogoRecognitionAnnotationsList__)()) {
            [Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html) entity = logoRecognitionAnnotation.getEntity();
            // Opaque entity ID. Some IDs may be available in
            // [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).
            System.out.printf("Entity Id : %s\n", entity.[getEntityId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html#com_google_cloud_videointelligence_v1_Entity_getEntityId__)());
            System.out.printf("Description : %s\n", entity.[getDescription](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html#com_google_cloud_videointelligence_v1_Entity_getDescription__)());
            // All logo tracks where the recognized logo appears. Each track corresponds to one logo
            // instance appearing in consecutive frames.
            for ([Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html) track : logoRecognitionAnnotation.getTracksList()) {
    
              // Video segment of a track.
              [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) startTimeOffset = track.getSegment().getStartTimeOffset();
              System.out.printf(
                  "\n\tStart Time Offset: %s.%s\n",
                  startTimeOffset.[getSeconds](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getSeconds__)(), startTimeOffset.[getNanos](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getNanos__)());
              [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) endTimeOffset = track.getSegment().getEndTimeOffset();
              System.out.printf(
                  "\tEnd Time Offset: %s.%s\n", endTimeOffset.[getSeconds](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getSeconds__)(), endTimeOffset.[getNanos](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html#com_google_protobuf_Duration_getNanos__)());
              System.out.printf("\tConfidence: %s\n", track.getConfidence());
    
              // The object with timestamp and attributes per frame in the track.
              for ([TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html) timestampedObject : track.getTimestampedObjectsList()) {
    
                // Normalized Bounding box in a frame, where the object is located.
                [NormalizedBoundingBox](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html) normalizedBoundingBox =
                    timestampedObject.getNormalizedBoundingBox();
                System.out.printf("\n\t\tLeft: %s\n", normalizedBoundingBox.[getLeft](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html#com_google_cloud_videointelligence_v1_NormalizedBoundingBox_getLeft__)());
                System.out.printf("\t\tTop: %s\n", normalizedBoundingBox.[getTop](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html#com_google_cloud_videointelligence_v1_NormalizedBoundingBox_getTop__)());
                System.out.printf("\t\tRight: %s\n", normalizedBoundingBox.[getRight](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html#com_google_cloud_videointelligence_v1_NormalizedBoundingBox_getRight__)());
                System.out.printf("\t\tBottom: %s\n", normalizedBoundingBox.[getBottom](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.NormalizedBoundingBox.html#com_google_cloud_videointelligence_v1_NormalizedBoundingBox_getBottom__)());
    
                // Optional. The attributes of the object in the bounding box.
                for ([DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html) attribute : timestampedObject.getAttributesList()) {
                  System.out.printf("\n\t\t\tName: %s\n", attribute.getName());
                  System.out.printf("\t\t\tConfidence: %s\n", attribute.getConfidence());
                  System.out.printf("\t\t\tValue: %s\n", attribute.getValue());
                }
              }
    
              // Optional. Attributes in the track level.
              for ([DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html) trackAttribute : track.getAttributesList()) {
                System.out.printf("\n\t\tName : %s\n", trackAttribute.getName());
                System.out.printf("\t\tConfidence : %s\n", trackAttribute.getConfidence());
                System.out.printf("\t\tValue : %s\n", trackAttribute.getValue());
              }
            }
    
            // All video segments where the recognized logo appears. There might be multiple instances
            // of the same logo class appearing in one VideoSegment.
            for ([VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html) segment : logoRecognitionAnnotation.getSegmentsList()) {
              System.out.printf(
                  "\n\tStart Time Offset : %s.%s\n",
                  segment.getStartTimeOffset().getSeconds(), segment.getStartTimeOffset().getNanos());
              System.out.printf(
                  "\tEnd Time Offset : %s.%s\n",
                  segment.getEndTimeOffset().getSeconds(), segment.getEndTimeOffset().getNanos());
            }
          }
        }
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const localFilePath = 'path/to/your/video.mp4'
    
    // Imports the Google Cloud client libraries
    const Video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)');
    const fs = require('fs');
    
    // Instantiates a client
    const client = new Video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    // Performs asynchronous video annotation for logo recognition on a file.
    async function detectLogo() {
      const inputContent = fs.readFileSync(localFilePath).toString('base64');
    
      // Build the request with the input content and logo recognition feature.
      const request = {
        inputContent: inputContent,
        features: ['LOGO_RECOGNITION'],
      };
    
      // Make the asynchronous request
      const [operation] = await client.annotateVideo(request);
    
      // Wait for the results
      const [response] = await operation.promise();
    
      // Get the first response, since we sent only one video.
      const annotationResult = response.annotationResults[0];
      for (const logoRecognitionAnnotation of annotationResult.logoRecognitionAnnotations) {
        const entity = logoRecognitionAnnotation.entity;
        // Opaque entity ID. Some IDs may be available in
        // [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/).
        console.log(`Entity Id: ${entity.entityId}`);
        console.log(`Description: ${entity.description}`);
    
        // All logo tracks where the recognized logo appears.
        // Each track corresponds to one logo instance appearing in consecutive frames.
        for (const track of logoRecognitionAnnotation.tracks) {
          console.log(
            `\n\tStart Time Offset: ${track.segment.startTimeOffset.seconds}.${track.segment.startTimeOffset.nanos}`
          );
          console.log(
            `\tEnd Time Offset: ${track.segment.endTimeOffset.seconds}.${track.segment.endTimeOffset.nanos}`
          );
          console.log(`\tConfidence: ${track.confidence}`);
    
          // The object with timestamp and attributes per frame in the track.
          for (const timestampedObject of track.timestampedObjects) {
            // Normalized Bounding box in a frame, where the object is located.
            const normalizedBoundingBox = timestampedObject.normalizedBoundingBox;
            console.log(`\n\t\tLeft: ${normalizedBoundingBox.left}`);
            console.log(`\t\tTop: ${normalizedBoundingBox.top}`);
            console.log(`\t\tRight: ${normalizedBoundingBox.right}`);
            console.log(`\t\tBottom: ${normalizedBoundingBox.bottom}`);
            // Optional. The attributes of the object in the bounding box.
            for (const attribute of timestampedObject.attributes) {
              console.log(`\n\t\t\tName: ${attribute.name}`);
              console.log(`\t\t\tConfidence: ${attribute.confidence}`);
              console.log(`\t\t\tValue: ${attribute.value}`);
            }
          }
    
          // Optional. Attributes in the track level.
          for (const trackAttribute of track.attributes) {
            console.log(`\n\t\tName: ${trackAttribute.name}`);
            console.log(`\t\tConfidence: ${trackAttribute.confidence}`);
            console.log(`\t\tValue: ${trackAttribute.value}`);
          }
        }
    
        // All video segments where the recognized logo appears.
        // There might be multiple instances of the same logo class appearing in one VideoSegment.
        for (const segment of logoRecognitionAnnotation.segments) {
          console.log(
            `\n\tStart Time Offset: ${segment.startTimeOffset.seconds}.${segment.startTimeOffset.nanos}`
          );
          console.log(
            `\tEnd Time Offset: ${segment.endTimeOffset.seconds}.${segment.endTimeOffset.nanos}`
          );
        }
      }
    }
    
    detectLogo();

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import io
    
    from google.cloud import videointelligence
    
    
    def detect_logo(local_file_path="path/to/your/video.mp4"):
        """Performs asynchronous video annotation for logo recognition on a local file."""
    
        client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
    
        with io.open(local_file_path, "rb") as f:
            input_content = f.read()
        features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).LOGO_RECOGNITION]
    
        operation = client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
            request={"features": features, "input_content": input_content}
        )
    
        print("Waiting for operation to complete...")
        response = operation.result()
    
        # Get the first response, since we sent only one video.
        annotation_result = response.annotation_results[0]
    
        # Annotations for list of logos detected, tracked and recognized in video.
        for logo_recognition_annotation in annotation_result.logo_recognition_annotations:
            entity = logo_recognition_annotation.entity
    
            # Opaque entity ID. Some IDs may be available in [Google Knowledge Graph
            # Search API](https://developers.google.com/knowledge-graph/).
            print("Entity Id : {}".format(entity.entity_id))
    
            print("Description : {}".format(entity.description))
    
            # All logo tracks where the recognized logo appears. Each track corresponds
            # to one logo instance appearing in consecutive frames.
            for track in logo_recognition_annotation.tracks:
                # Video segment of a track.
                print(
                    "\n\tStart Time Offset : {}.{}".format(
                        track.segment.start_time_offset.seconds,
                        track.segment.start_time_offset.microseconds * 1000,
                    )
                )
                print(
                    "\tEnd Time Offset : {}.{}".format(
                        track.segment.end_time_offset.seconds,
                        track.segment.end_time_offset.microseconds * 1000,
                    )
                )
                print("\tConfidence : {}".format(track.confidence))
    
                # The object with timestamp and attributes per frame in the track.
                for timestamped_object in track.timestamped_objects:
                    # Normalized Bounding box in a frame, where the object is located.
                    normalized_bounding_box = timestamped_object.normalized_bounding_box
                    print("\n\t\tLeft : {}".format(normalized_bounding_box.left))
                    print("\t\tTop : {}".format(normalized_bounding_box.top))
                    print("\t\tRight : {}".format(normalized_bounding_box.right))
                    print("\t\tBottom : {}".format(normalized_bounding_box.bottom))
    
                    # Optional. The attributes of the object in the bounding box.
                    for attribute in timestamped_object.attributes:
                        print("\n\t\t\tName : {}".format(attribute.name))
                        print("\t\t\tConfidence : {}".format(attribute.confidence))
                        print("\t\t\tValue : {}".format(attribute.value))
    
                # Optional. Attributes in the track level.
                for track_attribute in track.attributes:
                    print("\n\t\tName : {}".format(track_attribute.name))
                    print("\t\tConfidence : {}".format(track_attribute.confidence))
                    print("\t\tValue : {}".format(track_attribute.value))
    
            # All video segments where the recognized logo appears. There might be
            # multiple instances of the same logo class appearing in one VideoSegment.
            for segment in logo_recognition_annotation.segments:
                print(
                    "\n\tStart Time Offset : {}.{}".format(
                        segment.start_time_offset.seconds,
                        segment.start_time_offset.microseconds * 1000,
                    )
                )
                print(
                    "\tEnd Time Offset : {}.{}".format(
                        segment.end_time_offset.seconds,
                        segment.end_time_offset.microseconds * 1000,
                    )
                )
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
