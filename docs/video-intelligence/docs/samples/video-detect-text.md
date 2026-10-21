---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-detect-text/
title: Detect text in a local video file \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:08.539535+00:00
---

# Detect text in a local video file  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-detect-text/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Detect text in a local video file Stay organized with collections  Save and categorize content based on your preferences. 

Detect text in a video stored locally.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Recognize text](https://docs.cloud.google.com/video-intelligence/docs/text-detection)



## Code sample

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoRequest;
    use Google\Cloud\VideoIntelligence\V1\Client\VideoIntelligenceServiceClient;
    use Google\Cloud\VideoIntelligence\V1\Feature;
    
    /**
     * @param string $path   File path to a video file to analyze
     * @param int $pollingIntervalSeconds
     */
    function analyze_text_detection_file(string $path, int $pollingIntervalSeconds = 0)
    {
        # Instantiate a client.
        $video = new VideoIntelligenceServiceClient();
    
        # Read the local video file
        $inputContent = file_get_contents($path);
    
        # Execute a request.
        $features = [Feature::TEXT_DETECTION];
        $request = (new AnnotateVideoRequest())
            ->setInputContent($inputContent)
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
            foreach ($results->getTextAnnotations() as $text) {
                printf('Video text description: %s' . PHP_EOL, $text->getText());
                foreach ($text->getSegments() as $segment) {
                    $start = $segment->getSegment()->getStartTimeOffset();
                    $end = $segment->getSegment()->getEndTimeOffset();
                    printf('  Segment: %ss to %ss' . PHP_EOL,
                        $start->getSeconds() + $start->getNanos() / 1000000000.0,
                        $end->getSeconds() + $end->getNanos() / 1000000000.0);
                    printf('  Confidence: %f' . PHP_EOL, $segment->getConfidence());
                }
            }
            print(PHP_EOL);
        } else {
            print_r($operation->getError());
        }
    }

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
