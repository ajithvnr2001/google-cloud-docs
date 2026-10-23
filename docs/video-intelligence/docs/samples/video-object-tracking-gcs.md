---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-object-tracking-gcs/
title: Track objects in a video on Cloud Storage \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:30.120277+00:00
---

# Track objects in a video on Cloud Storage  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-object-tracking-gcs/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Track objects in a video on Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Track multiple objects detected in a video stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Track objects](https://docs.cloud.google.com/video-intelligence/docs/object-tracking)



## Code sample

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoRequest;
    use Google\Cloud\VideoIntelligence\V1\Client\VideoIntelligenceServiceClient;
    use Google\Cloud\VideoIntelligence\V1\Feature;
    
    /**
     * @param string $uri The cloud storage object to analyze (gs://your-bucket-name/your-object-name)
     * @param int $pollingIntervalSeconds
     */
    function analyze_object_tracking(string $uri, int $pollingIntervalSeconds = 0)
    {
        # Instantiate a client.
        $video = new VideoIntelligenceServiceClient();
    
        # Execute a request.
        $features = [Feature::OBJECT_TRACKING];
        $request = (new AnnotateVideoRequest())
            ->setInputUri($uri)
            ->setFeatures($features);
        $operation = $video->annotateVideo($request);
    
        # Wait for the request to complete.
        $operation->pollUntilComplete([
            'pollingIntervalSeconds' => $pollingIntervalSeconds
        ]);
    
        # Print the results.
        if ($operation->operationSucceeded()) {
            $results = $operation->getResult()->getAnnotationResults()[0];
            # Process video/segment level label annotations
            $objectEntity = $results->getObjectAnnotations()[0];
    
            printf('Video object entity: %s' . PHP_EOL, $objectEntity->getEntity()->getEntityId());
            printf('Video object description: %s' . PHP_EOL, $objectEntity->getEntity()->getDescription());
    
            $start = $objectEntity->getSegment()->getStartTimeOffset();
            $end = $objectEntity->getSegment()->getEndTimeOffset();
            printf('  Segment: %ss to %ss' . PHP_EOL,
                $start->getSeconds() + $start->getNanos() / 1000000000.0,
                $end->getSeconds() + $end->getNanos() / 1000000000.0);
            printf('  Confidence: %f' . PHP_EOL, $objectEntity->getConfidence());
    
            foreach ($objectEntity->getFrames() as $objectEntityFrame) {
                $offset = $objectEntityFrame->getTimeOffset();
                $boundingBox = $objectEntityFrame->getNormalizedBoundingBox();
                printf('  Time offset: %ss' . PHP_EOL,
                    $offset->getSeconds() + $offset->getNanos() / 1000000000.0);
                printf('  Bounding box position:' . PHP_EOL);
                printf('   Left: %s', $boundingBox->getLeft());
                printf('   Top: %s', $boundingBox->getTop());
                printf('   Right: %s', $boundingBox->getRight());
                printf('   Bottom: %s', $boundingBox->getBottom());
            }
            print(PHP_EOL);
        } else {
            print_r($operation->getError());
        }
    }

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
