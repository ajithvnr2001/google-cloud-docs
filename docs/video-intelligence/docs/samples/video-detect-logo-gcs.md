---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-detect-logo-gcs/
title: Recognize logos in a Cloud Storage file \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:40.105259+00:00
---

# Recognize logos in a Cloud Storage file  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-detect-logo-gcs/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Recognize logos in a Cloud Storage file Stay organized with collections  Save and categorize content based on your preferences. 

Detect, track, and recognize the presence of logos in video content from file in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Recognize logos](https://docs.cloud.google.com/video-intelligence/docs/logo-recognition)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
