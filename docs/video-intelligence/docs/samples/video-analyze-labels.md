---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-analyze-labels/
title: Annotate a local video file \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:39.714385+00:00
---

# Annotate a local video file  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-analyze-labels/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Annotate a local video file Stay organized with collections  Save and categorize content based on your preferences. 

Annotate a video file stored locally.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Analyze videos for labels](https://docs.cloud.google.com/video-intelligence/docs/analyze-labels)



## Code sample

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func label(w io.Writer, file string) error {
    	ctx := context.Background()
    	client, err := video.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("video.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	fileBytes, err := os.ReadFile(file)
    	if err != nil {
    		return err
    	}
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		Features: []videopb.Feature{
    			videopb.Feature_LABEL_DETECTION,
    		},
    		InputContent: fileBytes,
    	})
    	if err != nil {
    		return fmt.Errorf("AnnotateVideo: %w", err)
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	printLabels := func(labels []*videopb.LabelAnnotation) {
    		for _, label := range labels {
    			fmt.Fprintf(w, "\tDescription: %s\n", label.Entity.Description)
    			for _, category := range label.CategoryEntities {
    				fmt.Fprintf(w, "\t\tCategory: %s\n", category.Description)
    			}
    			for _, segment := range label.Segments {
    				start, _ := ptypes.Duration(segment.Segment.StartTimeOffset)
    				end, _ := ptypes.Duration(segment.Segment.EndTimeOffset)
    				fmt.Fprintf(w, "\t\tSegment: %s to %s\n", start, end)
    			}
    		}
    	}
    
    	// A single video was processed. Get the first result.
    	result := resp.AnnotationResults[0]
    
    	fmt.Fprintln(w, "SegmentLabelAnnotations:")
    	printLabels(result.SegmentLabelAnnotations)
    	fmt.Fprintln(w, "ShotLabelAnnotations:")
    	printLabels(result.ShotLabelAnnotations)
    	fmt.Fprintln(w, "FrameLabelAnnotations:")
    	printLabels(result.FrameLabelAnnotations)
    
    	return nil
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Instantiate a com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient
    try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
      // Read file and encode into Base64
      Path path = Paths.get(filePath);
      byte[] data = Files.readAllBytes(path);
    
      AnnotateVideoRequest request =
          AnnotateVideoRequest.newBuilder()
              .setInputContent(ByteString.copyFrom(data))
              .addFeatures(Feature.LABEL_DETECTION)
              .build();
      // Create an operation that will contain the response when the operation completes.
      OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> response =
          client.annotateVideoAsync(request);
    
      System.out.println("Waiting for operation to complete...");
      for (VideoAnnotationResults results : response.get().getAnnotationResultsList()) {
        // process video / segment level label annotations
        System.out.println("Locations: ");
        for (LabelAnnotation labelAnnotation : results.getSegmentLabelAnnotationsList()) {
          System.out.println("Video label: " + labelAnnotation.getEntity().getDescription());
          // categories
          for (Entity categoryEntity : labelAnnotation.getCategoryEntitiesList()) {
            System.out.println("Video label category: " + categoryEntity.getDescription());
          }
          // segments
          for (LabelSegment segment : labelAnnotation.getSegmentsList()) {
            double startTime =
                segment.getSegment().getStartTimeOffset().getSeconds()
                    + segment.getSegment().getStartTimeOffset().getNanos() / 1e9;
            double endTime =
                segment.getSegment().getEndTimeOffset().getSeconds()
                    + segment.getSegment().getEndTimeOffset().getNanos() / 1e9;
            System.out.printf("Segment location: %.3f:%.2f\n", startTime, endTime);
            System.out.println("Confidence: " + segment.getConfidence());
          }
        }
    
        // process shot label annotations
        for (LabelAnnotation labelAnnotation : results.getShotLabelAnnotationsList()) {
          System.out.println("Shot label: " + labelAnnotation.getEntity().getDescription());
          // categories
          for (Entity categoryEntity : labelAnnotation.getCategoryEntitiesList()) {
            System.out.println("Shot label category: " + categoryEntity.getDescription());
          }
          // segments
          for (LabelSegment segment : labelAnnotation.getSegmentsList()) {
            double startTime =
                segment.getSegment().getStartTimeOffset().getSeconds()
                    + segment.getSegment().getStartTimeOffset().getNanos() / 1e9;
            double endTime =
                segment.getSegment().getEndTimeOffset().getSeconds()
                    + segment.getSegment().getEndTimeOffset().getNanos() / 1e9;
            System.out.printf("Segment location: %.3f:%.2f\n", startTime, endTime);
            System.out.println("Confidence: " + segment.getConfidence());
          }
        }
    
        // process frame label annotations
        for (LabelAnnotation labelAnnotation : results.getFrameLabelAnnotationsList()) {
          System.out.println("Frame label: " + labelAnnotation.getEntity().getDescription());
          // categories
          for (Entity categoryEntity : labelAnnotation.getCategoryEntitiesList()) {
            System.out.println("Frame label category: " + categoryEntity.getDescription());
          }
          // segments
          for (LabelSegment segment : labelAnnotation.getSegmentsList()) {
            double startTime =
                segment.getSegment().getStartTimeOffset().getSeconds()
                    + segment.getSegment().getStartTimeOffset().getNanos() / 1e9;
            double endTime =
                segment.getSegment().getEndTimeOffset().getSeconds()
                    + segment.getSegment().getEndTimeOffset().getNanos() / 1e9;
            System.out.printf("Segment location: %.3f:%.2f\n", startTime, endTime);
            System.out.println("Confidence: " + segment.getConfidence());
          }
        }
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Video Intelligence library + Node's fs library
    const video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1;
    const fs = require('fs');
    const util = require('util');
    
    // Creates a client
    const client = new video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const path = 'Local file to analyze, e.g. ./my-file.mp4';
    
    // Reads a local video file and converts it to base64
    const readFile = util.promisify(fs.readFile);
    const file = await readFile(path);
    const inputContent = file.toString('base64');
    
    // Constructs request
    const request = {
      inputContent: inputContent,
      features: ['LABEL_DETECTION'],
    };
    
    // Detects labels in a video
    const [operation] = await client.annotateVideo(request);
    console.log('Waiting for operation to complete...');
    const [operationResult] = await operation.promise();
    // Gets annotations for video
    const annotations = operationResult.annotationResults[0];
    
    const labels = annotations.segmentLabelAnnotations;
    labels.forEach(label => {
      console.log(`Label ${label.entity.description} occurs at:`);
      label.segments.forEach(segment => {
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
          `\tStart: ${time.startTimeOffset.seconds}` +
            `.${(time.startTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(
          `\tEnd: ${time.endTimeOffset.seconds}.` +
            `${(time.endTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(`\tConfidence: ${segment.confidence}`);
      });
    });
    

### PHP

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoRequest;
    use Google\Cloud\VideoIntelligence\V1\Client\VideoIntelligenceServiceClient;
    use Google\Cloud\VideoIntelligence\V1\Feature;
    
    /**
     * @param string $path    File path to a video file to analyze
     * @param int $pollingIntervalSeconds
     */
    function analyze_labels_file(string $path, int $pollingIntervalSeconds = 0)
    {
        # Instantiate a client.
        $video = new VideoIntelligenceServiceClient();
    
        # Read the local video file
        $inputContent = file_get_contents($path);
    
        # Execute a request.
        $features = [Feature::LABEL_DETECTION];
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
                        $end->getSeconds() + $end->getNanos() / 1000000000.0);
                    printf('  Confidence: %f' . PHP_EOL, $segment->getConfidence());
                }
            }
            print(PHP_EOL);
    
            # Process shot level label annotations
            foreach ($results->getShotLabelAnnotations() as $label) {
                printf('Shot label description: %s' . PHP_EOL, $label->getEntity()->getDescription());
                foreach ($label->getCategoryEntities() as $categoryEntity) {
                    printf('  Category: %s' . PHP_EOL, $categoryEntity->getDescription());
                }
                foreach ($label->getSegments() as $shot) {
                    $start = $shot->getSegment()->getStartTimeOffset();
                    $end = $shot->getSegment()->getEndTimeOffset();
                    printf('  Shot: %ss to %ss' . PHP_EOL,
                        $start->getSeconds() + $start->getNanos() / 1000000000.0,
                        $end->getSeconds() + $end->getNanos() / 1000000000.0);
                    printf('  Confidence: %f' . PHP_EOL, $shot->getConfidence());
                }
            }
            print(PHP_EOL);
        } else {
            print_r($operation->getError());
        }
    }

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """Detect labels given a file path."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.LABEL_DETECTION]
    
    with io.open(path, "rb") as movie:
        input_content = movie.read()
    
    operation = video_client.annotate_video(
        request={"features": features, "input_content": input_content}
    )
    print("\nProcessing video for label annotations:")
    
    result = operation.result(timeout=90)
    print("\nFinished processing.")
    
    # Process video/segment level label annotations
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
    
    # Process shot level label annotations
    shot_labels = result.annotation_results[0].shot_label_annotations
    for i, shot_label in enumerate(shot_labels):
        print("Shot label description: {}".format(shot_label.entity.description))
        for category_entity in shot_label.category_entities:
            print(
                "\tLabel category description: {}".format(category_entity.description)
            )
    
        for i, shot in enumerate(shot_label.segments):
            start_time = (
                shot.segment.start_time_offset.seconds
                + shot.segment.start_time_offset.microseconds / 1e6
            )
            end_time = (
                shot.segment.end_time_offset.seconds
                + shot.segment.end_time_offset.microseconds / 1e6
            )
            positions = "{}s to {}s".format(start_time, end_time)
            confidence = shot.confidence
            print("\tSegment {}: {}".format(i, positions))
            print("\tConfidence: {}".format(confidence))
        print("\n")
    
    # Process frame level label annotations
    frame_labels = result.annotation_results[0].frame_label_annotations
    for i, frame_label in enumerate(frame_labels):
        print("Frame label description: {}".format(frame_label.entity.description))
        for category_entity in frame_label.category_entities:
            print(
                "\tLabel category description: {}".format(category_entity.description)
            )
    
        # Each frame_label_annotation has many frames,
        # here we print information only about the first frame.
        frame = frame_label.frames[0]
        time_offset = frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
        print("\tFirst frame time offset: {}s".format(time_offset))
        print("\tFirst frame confidence: {}".format(frame.confidence))
        print("\n")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
