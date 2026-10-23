---
url: https://docs.cloud.google.com/video-intelligence/docs/analyze-shots/
title: Detect shot changes \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:05.417451+00:00
---

# Detect shot changes  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/analyze-shots/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Detect shot changes Stay organized with collections  Save and categorize content based on your preferences. 

**Shot change analysis** detects shot changes in a video.

This section demonstrates a few ways to analyze a video for shot changes.

Here is an example of performing video analysis for shot changes on a file located in Cloud Storage.

_Looking for something more in-depth? Check out our detailed[Python tutorial](https://docs.cloud.google.com/video-intelligence/docs/shot_detection)._

### REST

## Send video annotation request

The following shows how to send a POST request to the [`videos:annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. The example uses the Google Cloud CLI to create an access token. For instructions on installing the gcloud CLI, see the [Video Intelligence API Quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts).

Before using any of the request data, make the following replacements: 

  * INPUT_URI: a Cloud Storage bucket that contains the file you want to annotate, including the file name. Must start with `gs://`.
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
        "inputUri": "INPUT_URI",
        "features": ["SHOT_CHANGE_DETECTION"]
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
    

If the response is successful, the Video Intelligence API returns the `name` for your operation. The above shows an example of such a response, where `project-name` is the name of your project and `operation-id` is the ID of the long running operation created for the request. 

  * PROJECT_NUMBER: the number of your project
  * LOCATION_ID: the Cloud region where annotation should take place. Supported cloud regions are: `us-east1`, `us-west1`, `europe-west1`, `asia-east1`. If no region is specified, a region will be determined based on video file location. 
  * OPERATION_ID: the ID of the long running operation created for the request and provided in the response when you started the operation, for example `12345....`



## Get annotation results

To retrieve the result of the operation, make a [GET](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/projects.locations.operations/get) request, using the operation name returned from the call to [`videos:annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate), as shown in the following example. 

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
    
    
    {
      "inputUri": "/demomaker/gbikes_dinosaur.mp4",
      "shotAnnotations": [
        {
          "startTimeOffset": "0s",
          "endTimeOffset": "5.167104s"
        },
        {
          "startTimeOffset": "5.236736s",
          "endTimeOffset": "10.072064s"
        },
        {
          "startTimeOffset": "10.106880s",
          "endTimeOffset": "28.139520s"
        },
        {
          "startTimeOffset": "28.174336s",
          "endTimeOffset": "42.768384s"
        }
      ]
    }
    

Shot detection annotations are returned as a `shotAnnotations` list. Note: The **done** field is only returned when its value is **True**. It's not included in responses for which the operation has not completed. 

## Download annotation results

Copy the annotation from the source to the destination bucket: (see [Copy files and objects](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp)) 

`gcloud storage cp gcs_uri gs://my-bucket`

Note: If the output gcs uri is provided by the user, then the annotation is stored in that gcs uri. 

### Go
    
    
    func shotChangeURI(w io.Writer, file string) error {
    	ctx := context.Background()
    	client, err := video.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		Features: []videopb.Feature{
    			videopb.Feature_SHOT_CHANGE_DETECTION,
    		},
    		InputUri: file,
    	})
    	if err != nil {
    		return err
    	}
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	// A single video was processed. Get the first result.
    	result := resp.AnnotationResults[0].ShotAnnotations
    
    	for _, shot := range result {
    		start, _ := ptypes.Duration(shot.StartTimeOffset)
    		end, _ := ptypes.Duration(shot.EndTimeOffset)
    
    		fmt.Fprintf(w, "Shot: %s to %s\n", start, end)
    	}
    
    	return nil
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Instantiate a com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient
    try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
      // Provide path to file hosted on GCS as "gs://bucket-name/..."
      AnnotateVideoRequest request =
          AnnotateVideoRequest.newBuilder()
              .setInputUri(gcsUri)
              .addFeatures(Feature.SHOT_CHANGE_DETECTION)
              .build();
    
      // Create an operation that will contain the response when the operation completes.
      OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> response =
          client.annotateVideoAsync(request);
    
      System.out.println("Waiting for operation to complete...");
      // Print detected shot changes and their location ranges in the analyzed video.
      for (VideoAnnotationResults result : response.get().getAnnotationResultsList()) {
        if (result.getShotAnnotationsCount() > 0) {
          System.out.println("Shots: ");
          for (VideoSegment segment : result.getShotAnnotationsList()) {
            double startTime =
                segment.getStartTimeOffset().getSeconds()
                    + segment.getStartTimeOffset().getNanos() / 1e9;
            double endTime =
                segment.getEndTimeOffset().getSeconds()
                    + segment.getEndTimeOffset().getNanos() / 1e9;
            System.out.printf("Location: %.3f:%.3f\n", startTime, endTime);
          }
        } else {
          System.out.println("No shot changes detected in " + gcsUri);
        }
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Video Intelligence library
    const video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1;
    
    // Creates a client
    const client = new video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const gcsUri = 'GCS URI of file to analyze, e.g. gs://my-bucket/my-video.mp4';
    
    const request = {
      inputUri: gcsUri,
      features: ['SHOT_CHANGE_DETECTION'],
    };
    
    // Detects camera shot changes
    const [operation] = await client.annotateVideo(request);
    console.log('Waiting for operation to complete...');
    const [operationResult] = await operation.promise();
    // Gets shot changes
    const shotChanges = operationResult.annotationResults[0].shotAnnotations;
    console.log('Shot changes:');
    
    if (shotChanges.length === 1) {
      console.log('The entire video is one shot.');
    } else {
      shotChanges.forEach((shot, shotIdx) => {
        console.log(`Scene ${shotIdx} occurs from:`);
        if (shot.startTimeOffset === undefined) {
          shot.startTimeOffset = {};
        }
        if (shot.endTimeOffset === undefined) {
          shot.endTimeOffset = {};
        }
        if (shot.startTimeOffset.seconds === undefined) {
          shot.startTimeOffset.seconds = 0;
        }
        if (shot.startTimeOffset.nanos === undefined) {
          shot.startTimeOffset.nanos = 0;
        }
        if (shot.endTimeOffset.seconds === undefined) {
          shot.endTimeOffset.seconds = 0;
        }
        if (shot.endTimeOffset.nanos === undefined) {
          shot.endTimeOffset.nanos = 0;
        }
        console.log(
          `\tStart: ${shot.startTimeOffset.seconds}` +
            `.${(shot.startTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(
          `\tEnd: ${shot.endTimeOffset.seconds}.` +
            `${(shot.endTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
      });
    }
    

### Python

For more information on installing and using the Video Intelligence API Client Library for Python, refer to [Video Intelligence API Client Libraries](https://docs.cloud.google.com/video-intelligence/docs/reference/libraries). 
    
    
    """Detects camera shot changes."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.SHOT_CHANGE_DETECTION]
    operation = video_client.annotate_video(
        request={"features": features, "input_uri": path}
    )
    print("\nProcessing video for shot change annotations:")
    
    result = operation.result(timeout=90)
    print("\nFinished processing.")
    
    # first result is retrieved because a single video was processed
    for i, shot in enumerate(result.annotation_results[0].shot_annotations):
        start_time = (
            shot.start_time_offset.seconds + shot.start_time_offset.microseconds / 1e6
        )
        end_time = (
            shot.end_time_offset.seconds + shot.end_time_offset.microseconds / 1e6
        )
        print("\tShot {}: {} to {}".format(i, start_time, end_time))

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
