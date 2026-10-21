---
url: https://docs.cloud.google.com/video-intelligence/docs/analyze-labels/
title: Analyze videos for labels \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:04.089366+00:00
---

# Analyze videos for labels  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/analyze-labels/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Analyze videos for labels Stay organized with collections  Save and categorize content based on your preferences. 

The Video Intelligence API can identify entities shown in video footage using the [LABEL_DETECTION](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#feature) feature. This feature identifies objects, locations, activities, animal species, products, and more.

The analysis can be compartmentalized as follows: 

  * Frame level:   
Entities are identified and labeled within each frame (with one frame per second sampling). 
  * Shot level:   
Shots are automatically detected within every segment (or video). Entities are then identified and labeled within each shot. 
  * Segment level:  
User-selected segments of a video can be specified for analysis by stipulating beginning and ending time offsets for the purposes of annotation (see [VideoSegment](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#videosegment)). Entities are then identified and labeled within each segment. If no segments are specified, the whole video is treated as one segment. 

**Note:** For an example, see the [Label detection](https://docs.cloud.google.com/video-intelligence/docs/label-tutorial) tutorial

## Annotate a local file

Here is an example of performing video analysis for labels on a local file.

_Looking for something more in-depth? Check out our detailed[Python tutorial](https://docs.cloud.google.com/video-intelligence/docs/label-tutorial)._

### REST

### Send the process request

The following shows how to send a `POST` request to the [`videos:annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. You can configure the [`LabelDetectionMode`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#labeldetectionmode) to shot-level and/or frame-level annotations. We recommend using `SHOT_AND_FRAME_MODE`. The example uses the access token for a service account set up for the project using the Google Cloud CLI. For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Video Intelligence quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts).

Before using any of the request data, make the following replacements: 

  * BASE64_ENCODED_CONTENT: your video as base64 encoded data. See [the instructions on how to convert your data to base64](https://docs.cloud.google.com/video-intelligence/docs/base64).
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputContent": "BASE64_ENCODED_CONTENT",
      "features": ["LABEL_DETECTION"],
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
    

If the request is successful, Video Intelligence returns the name of your operation.

### Get the results

To get the results of your request, you must send a `GET` request to the [`projects.locations.operations`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/get) resource. The following shows how to send such a request.

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
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress",
        "annotationProgress": [
          {
            "progressPercent": 100,
            "startTime": "2019-03-12T19:36:09.110351Z",
            "updateTime": "2019-03-12T19:36:17.519069Z"
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
        "annotationResults": [
          {
            "segmentLabelAnnotations": [
              {
                "entity": {
                  "entityId": "/m/01prls",
                  "description": "land vehicle",
                  "languageCode": "en-US"
                },
                "categoryEntities": [
                  {
                    "entityId": "/m/07yv9",
                    "description": "vehicle",
                    "languageCode": "en-US"
                  }
                ],
                "segments": [
                  {
                    "segment": {
                      "startTimeOffset": "0s",
                      "endTimeOffset": "38.757872s"
                    },
                    "confidence": 0.6614419
                  }
                ]
              },
              {
                "entity": {
                  "entityId": "/m/039jbq",
                  "description": "urban area",
                  "languageCode": "en-US"
                },
                "categoryEntities": [
                  {
                    "entityId": "/m/01n32",
                    "description": "city",
                    "languageCode": "en-US"
                  }
                ],
                "segments": [
                  {
                    "segment": {
                      "startTimeOffset": "0s",
                      "endTimeOffset": "38.757872s"
                    },
                    "confidence": 0.92337775
                  }
                ]
              },
              ...
    

### Go
    
    
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
    

### Python

For more information on installing and using the Video Intelligence API Client Library for Python, refer to [Video Intelligence API Client Libraries](https://cloud.google.com/video-intelligence/docs/reference/libraries). 
    
    
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

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

## Annotate a file on Cloud Storage

Here is an example of performing video analysis for labels on a file located in Cloud Storage.

### REST

For more information on installing and using the Video Intelligence API Client Library for Python, refer to [Video Intelligence API Client Libraries](https://cloud.google.com/video-intelligence/docs/reference/libraries). 

### Send the process request

The following shows how to send a `POST` request to the [`annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. The example uses the access token for a service account set up for the project using the Google Cloud CLI. For instructions on installing the Google Cloud CLI, setting up a project with a service account, and obtaining an access token, see the [Video Intelligence quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts).

Before using any of the request data, make the following replacements: 

  * INPUT_URI: a Cloud Storage bucket that contains the file you want to annotate, including the file name. Must start with `gs://`.
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputUri": "INPUT_URI",
      "features": ["LABEL_DETECTION"],
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
    

If the request is successful, the Video Intelligence returns the name of your operation.

### Get the results

To get the results of your request, you must send a `GET` request to the [`projects.locations.operations`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/get) resource. The following shows how to send such a request.

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
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress",
        "annotationProgress": [
          {
            "inputUri": "INPUT_URI",
            "progressPercent": 100,
            "startTime": "2019-11-13T19:25:56.206335Z",
            "updateTime": "2019-11-13T19:26:16.215615Z"
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
        "annotationResults": [
          {
            "inputUri": "INPUT_URI",
            "segmentLabelAnnotations": [
              {
                "entity": {
                  "entityId": "/m/01vkl",
                  "description": "circle",
                  "languageCode": "en-US"
                },
                "categoryEntities": [
                  {
                    "entityId": "/m/016nqd",
                    "description": "shape",
                    "languageCode": "en-US"
                  }
                ],
                "segments": [
                  {
                    "segment": {
                      "startTimeOffset": "0s",
                      "endTimeOffset": "16.416666s"
                    },
                    "confidence": 0.36535457
                  }
                ]
              },
              ...
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
    
    
    func labelURI(w io.Writer, file string) error {
    	ctx := context.Background()
    	client, err := video.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("video.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		Features: []videopb.Feature{
    			videopb.Feature_LABEL_DETECTION,
    		},
    		InputUri: file,
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
    
    
    // Instantiate a com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient
    try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
      // Provide path to file hosted on GCS as "gs://bucket-name/..."
      AnnotateVideoRequest request =
          AnnotateVideoRequest.newBuilder()
              .setInputUri(gcsUri)
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
            System.out.printf("Segment location: %.3f:%.3f\n", startTime, endTime);
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
            System.out.printf("Segment location: %.3f:%.3f\n", startTime, endTime);
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
    
    
    // Imports the Google Cloud Video Intelligence library
    const video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1;
    
    // Creates a client
    const client = new video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const gcsUri = 'GCS URI of the video to analyze, e.g. gs://my-bucket/my-video.mp4';
    
    const request = {
      inputUri: gcsUri,
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

### Python
    
    
    """Detects labels given a GCS path."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.LABEL_DETECTION]
    
    mode = videointelligence.LabelDetectionMode.SHOT_AND_FRAME_MODE
    config = videointelligence.LabelDetectionConfig(label_detection_mode=mode)
    context = videointelligence.VideoContext(label_detection_config=config)
    
    operation = video_client.annotate_video(
        request={"features": features, "input_uri": path, "video_context": context}
    )
    print("\nProcessing video for label annotations:")
    
    result = operation.result(timeout=180)
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

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
