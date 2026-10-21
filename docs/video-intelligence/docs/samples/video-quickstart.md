---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-quickstart/
title: Detect labels in video on Cloud Storage \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:57.685471+00:00
---

# Detect labels in video on Cloud Storage  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-quickstart/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Detect labels in video on Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Detect labels in a video stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Annotate a video by using client libraries](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-client-libraries)



## Code sample

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample video_quickstart uses the Google Cloud Video Intelligence API to label a video.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	"github.com/golang/protobuf/ptypes"
    
    	video "cloud.google.com/go/videointelligence/apiv1"
    	videopb "cloud.google.com/go/videointelligence/apiv1/videointelligencepb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := video.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_Client_Close)()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		InputUri: "gs://cloud-samples-data/video/cat.mp4",
    		Features: []videopb.Feature{
    			videopb.Feature_LABEL_DETECTION,
    		},
    	})
    	if err != nil {
    		log.Fatalf("Failed to start annotation job: %v", err)
    	}
    
    	resp, err := op.[Wait](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/videointelligence/latest/apiv1.html#cloud_google_com_go_videointelligence_apiv1_AnnotateVideoOperation_Wait)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to annotate: %v", err)
    	}
    
    	// Only one video was processed, so get the first result.
    	result := resp.GetAnnotationResults()[0]
    
    	for _, annotation := range result.SegmentLabelAnnotations {
    		fmt.Printf("Description: %s\n", annotation.Entity.Description)
    
    		for _, category := range annotation.CategoryEntities {
    			fmt.Printf("\tCategory: %s\n", category.Description)
    		}
    
    		for _, segment := range annotation.Segments {
    			start, _ := ptypes.Duration(segment.Segment.StartTimeOffset)
    			end, _ := ptypes.Duration(segment.Segment.EndTimeOffset)
    			fmt.Printf("\tSegment: %s to %s\n", start, end)
    			fmt.Printf("\tConfidence: %v\n", segment.Confidence)
    		}
    	}
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html);
    import com.google.cloud.videointelligence.v1.[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html);
    import com.google.cloud.videointelligence.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html);
    import com.google.cloud.videointelligence.v1.[LabelAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LabelAnnotation.html);
    import com.google.cloud.videointelligence.v1.[LabelSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LabelSegment.html);
    import com.google.cloud.videointelligence.v1.[VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html);
    import com.google.cloud.videointelligence.v1.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html);
    import java.util.List;
    
    public class QuickstartSample {
    
      /** Demonstrates using the video intelligence client to detect labels in a video file. */
      public static void main(String[] args) throws Exception {
        // Instantiate a video intelligence client
        try ([VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html) client = [VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html).create()) {
          // The Google Cloud Storage path to the video to annotate.
          String gcsUri = "gs://cloud-samples-data/video/cat.mp4";
    
          // Create an operation that will contain the response when the operation completes.
          [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html) request =
              [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html).newBuilder()
                  .setInputUri(gcsUri)
                  .[addFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_addFeatures_com_google_cloud_videointelligence_v1_Feature_)([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html).LABEL_DETECTION)
                  .build();
    
          OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> response =
              client.[annotateVideoAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html#com_google_cloud_videointelligence_v1_VideoIntelligenceServiceClient_annotateVideoAsync_com_google_cloud_videointelligence_v1_AnnotateVideoRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
    
          List<VideoAnnotationResults> results = response.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)().getAnnotationResultsList();
          if (results.isEmpty()) {
            System.out.println("No labels detected in " + gcsUri);
            return;
          }
          for ([VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html) result : results) {
            System.out.println("Labels:");
            // get video segment label annotations
            for ([LabelAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LabelAnnotation.html) annotation : result.getSegmentLabelAnnotationsList()) {
              System.out.println(
                  "Video label description : " + annotation.getEntity().getDescription());
              // categories
              for ([Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Entity.html) categoryEntity : annotation.getCategoryEntitiesList()) {
                System.out.println("Label Category description : " + categoryEntity.getDescription());
              }
              // segments
              for ([LabelSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.LabelSegment.html) segment : annotation.getSegmentsList()) {
                double startTime =
                    segment.getSegment().getStartTimeOffset().getSeconds()
                        + segment.getSegment().getStartTimeOffset().getNanos() / 1e9;
                double endTime =
                    segment.getSegment().getEndTimeOffset().getSeconds()
                        + segment.getSegment().getEndTimeOffset().getNanos() / 1e9;
                System.out.printf("Segment location : %.3f:%.3f\n", startTime, endTime);
                System.out.println("Confidence : " + segment.getConfidence());
              }
            }
          }
        }
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Video Intelligence library
    const videoIntelligence = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)');
    
    // Creates a client
    const client = new videoIntelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    // The GCS uri of the video to analyze
    const gcsUri = 'gs://cloud-samples-data/video/cat.mp4';
    
    // Construct request
    const request = {
      inputUri: gcsUri,
      features: ['LABEL_DETECTION'],
    };
    
    // Execute request
    const [operation] = await client.annotateVideo(request);
    
    console.log(
      'Waiting for operation to complete... (this may take a few minutes)'
    );
    
    const [operationResult] = await operation.promise();
    
    // Gets annotations for video
    const annotations = operationResult.annotationResults[0];
    
    // Gets labels for video from its annotations
    const labels = annotations.segmentLabelAnnotations;
    labels.forEach(label => {
      console.log(`Label ${label.entity.description} occurs at:`);
      label.segments.forEach(segment => {
        segment = segment.segment;
        console.log(
          `\tStart: ${segment.startTimeOffset.seconds}` +
            `.${(segment.startTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(
          `\tEnd: ${segment.endTimeOffset.seconds}.` +
            `${(segment.endTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
      });
    });

### PHP

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\VideoIntelligence\V1\Client\VideoIntelligenceServiceClient;
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoRequest;
    use Google\Cloud\VideoIntelligence\V1\Feature;
    
    # Instantiate a client.
    $video = new VideoIntelligenceServiceClient();
    
    # Execute a request.
    $features = [Feature::LABEL_DETECTION];
    $options = [
        'inputUri' => 'gs://cloud-samples-data/video/cat.mp4',
        'features' => $features
    ];
    $request = (new AnnotateVideoRequest())
        ->setInputUri($options['inputUri'])
        ->setFeatures($options['features']);
    $operation = $video->annotateVideo($request);
    
    # Wait for the request to complete.
    $operation->pollUntilComplete();
    
    # Print the result.
    if ($operation->operationSucceeded()) {
        $results = $operation->getResult()->getAnnotationResults()[0];
        # Process video/segment level label annotations
        foreach ($results->getSegmentLabelAnnotations() as $label) {
            printf('Video label description: %s' . PHP_EOL, $label->getEntity()->getDescription());
            foreach ($label->getCategoryEntities() as $categoryEntity) {
                printf('  Category: %s' . PHP_EOL, $categoryEntity->getDescription());
            }
            foreach ($label->getSegments() as $segment) {
                $start = $segment->getSegment()->getStartTimeOffset();
                $end = $segment->getSegment()->getEndTimeOffset();
                printf('  Segment: %ss to %ss' . PHP_EOL,
                    $start->getSeconds() + $start->getNanos() / 1000000000.0,
                    $end->getSeconds() + $end->getNanos() / 1000000000.0
                );
                printf('  Confidence: %f' . PHP_EOL, $segment->getConfidence());
            }
        }
    } else {
        print_r($operation->getError());
    }

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import videointelligence
    
    video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
    features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).LABEL_DETECTION]
    operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
        request={
            "features": features,
            "input_uri": "gs://cloud-samples-data/video/cat.mp4",
        }
    )
    print("\nProcessing video for label annotations:")
    
    result = operation.result(timeout=180)
    print("\nFinished processing.")
    
    # first result is retrieved because a single video was processed
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print("Video label description: {}".format(segment_label.entity.description))
        for category_entity in segment_label.category_entities:
            print(
                "\tLabel category description: {}".format(category_entity.description)
            )
    
        for i, segment in enumerate(segment_label.segments):
            start_time = (
                segment.segment.start_time_offset.seconds
                + segment.segment.start_time_offset.microseconds / 1e6
            )
            end_time = (
                segment.segment.end_time_offset.seconds
                + segment.segment.end_time_offset.microseconds / 1e6
            )
            positions = "{}s to {}s".format(start_time, end_time)
            confidence = segment.confidence
            print("\tSegment {}: {}".format(i, positions))
            print("\tConfidence: {}".format(confidence))
        print("\n")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
