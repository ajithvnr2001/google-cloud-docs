---
url: https://docs.cloud.google.com/video-intelligence/docs/people-detection/
title: Detect people \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:41.372241+00:00
---

# Detect people  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/people-detection/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Detect people Stay organized with collections  Save and categorize content based on your preferences. 

The following code sample demonstrates how to detect people in a video file using Video Intelligence API.

Video Intelligence can detect the presence of humans in a video file and track individuals across a video or video segment.

**Note:** See the [Person detection](https://docs.cloud.google.com/video-intelligence/docs/feature-person-detection) concept page for more background on this feature.

## Person detection from a file in Cloud Storage

The following demonstrates how to send an annotation request to Video Intelligence with the person detection feature.

### REST

### Send video annotation request

The following shows how to send a POST request to the [`videos:annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. The example uses the Google Cloud CLI to create an access token. For instructions on installing the gcloud CLI, see the [Video Intelligence API Quickstart](https://docs.cloud.google.com/video-intelligence/docs/quickstarts). See also [`PersonDetectionConfig`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate#PersonDetectionConfig).

Before using any of the request data, make the following replacements: 

  * INPUT_URI: a Cloud Storage bucket that contains the file you want to annotate, including the file name. Must start with `gs://`.   
For example:  
`"inputUri": "gs://cloud-samples-data/video/googlework_short.mp4"`
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputUri": "INPUT_URI",
      "features": ["PERSON_DETECTION"],
      "videoContext": {
        "personDetectionConfig": {
          "includeBoundingBoxes": true,
          "includePoseLandmarks": true,
          "includeAttributes": true
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

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID"
    }
    

If the response is successful, the Video Intelligence API returns the `name` for your operation. The above shows an example of such a response, where:

  * PROJECT_NUMBER: the number of your project
  * LOCATION_ID: the Cloud region where annotation should take place. Supported cloud regions are: `us-east1`, `us-west1`, `europe-west1`, `asia-east1`. If no region is specified, a region will be determined based on video file location. 
  * OPERATION_ID: the ID of the long running operation created for the request and provided in the response when you started the operation, for example `12345...`



### Get annotation results

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
    
    
    {
      "name": "us-west1.10001026834554604237",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress",
        "annotationProgress": [
          {
            "inputUri": "/cloud-ml-sandbox/video/chicago.mp4",
            "progressPercent": 100,
             "startTime": "2020-02-08T21:26:56.577807Z",
            "updateTime": "2020-02-08T21:28:09.620665Z"
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
        "annotationResults": [
          {
            "inputUri": "/cloud-ml-sandbox/video/chicago.mp4",
            "personDetectionAnnotations": [
              {
                "tracks": [
                  {
                    "segment": {
                      "startTimeOffset": "0s",
                      "endTimeOffset": "1.507436s"
                    }
                  },
                  ...
                ]
              }
            ]
          }
        ]
      }
    }
    

Shot detection annotations are returned as a `shotAnnotations` list. Note: The **done** field is only returned when its value is **True**. It's not included in responses for which the operation has not completed. 

## Download annotation results

Copy the annotation from the source to the destination bucket: (see [Copy files and objects](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp)) 

`gcloud storage cp gcs_uri gs://my-bucket`

Note: If the output gcs uri is provided by the user, then the annotation is stored in that gcs uri. 

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html);
    import com.google.cloud.videointelligence.v1.[DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html);
    import com.google.cloud.videointelligence.v1.[DetectedLandmark](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedLandmark.html);
    import com.google.cloud.videointelligence.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html);
    import com.google.cloud.videointelligence.v1.[PersonDetectionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionAnnotation.html);
    import com.google.cloud.videointelligence.v1.[PersonDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionConfig.html);
    import com.google.cloud.videointelligence.v1.[TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html);
    import com.google.cloud.videointelligence.v1.[Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html);
    import com.google.cloud.videointelligence.v1.[VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html);
    import com.google.cloud.videointelligence.v1.[VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html);
    import com.google.cloud.videointelligence.v1.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html);
    import com.google.cloud.videointelligence.v1.[VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html);
    
    public class DetectPersonGcs {
    
      public static void detectPersonGcs() throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String gcsUri = "gs://cloud-samples-data/video/googlework_short.mp4";
        detectPersonGcs(gcsUri);
      }
    
      // Detects people in a video stored in Google Cloud Storage using
      // the Cloud Video Intelligence API.
      public static void detectPersonGcs(String gcsUri) throws Exception {
        try ([VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html) videoIntelligenceServiceClient =
            [VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html).create()) {
          // Reads a local video file and converts it to base64.
    
          [PersonDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionConfig.html) personDetectionConfig =
              [PersonDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionConfig.html).newBuilder()
                  // Must set includeBoundingBoxes to true to get poses and attributes.
                  .setIncludeBoundingBoxes(true)
                  .[setIncludePoseLandmarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionConfig.Builder.html#com_google_cloud_videointelligence_v1_PersonDetectionConfig_Builder_setIncludePoseLandmarks_boolean_)(true)
                  .setIncludeAttributes(true)
                  .build();
          [VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html) videoContext =
              [VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html).newBuilder().[setPersonDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.Builder.html#com_google_cloud_videointelligence_v1_VideoContext_Builder_setPersonDetectionConfig_com_google_cloud_videointelligence_v1_PersonDetectionConfig_)(personDetectionConfig).build();
    
          [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html) request =
              [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html).newBuilder()
                  .setInputUri(gcsUri)
                  .[addFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_addFeatures_com_google_cloud_videointelligence_v1_Feature_)([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html).PERSON_DETECTION)
                  .[setVideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_setVideoContext_com_google_cloud_videointelligence_v1_VideoContext_)(videoContext)
                  .build();
    
          // Detects people in a video
          OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
              videoIntelligenceServiceClient.[annotateVideoAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html#com_google_cloud_videointelligence_v1_VideoIntelligenceServiceClient_annotateVideoAsync_com_google_cloud_videointelligence_v1_AnnotateVideoRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
          [AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          // Get the first response, since we sent only one video.
          [VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html) annotationResult = response.[getAnnotationResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html#com_google_cloud_videointelligence_v1_AnnotateVideoResponse_getAnnotationResultsList__)().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(0);
    
          // Annotations for list of people detected, tracked and recognized in video.
          for ([PersonDetectionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionAnnotation.html) personDetectionAnnotation :
              annotationResult.[getPersonDetectionAnnotationsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html#com_google_cloud_videointelligence_v1_VideoAnnotationResults_getPersonDetectionAnnotationsList__)()) {
            System.out.print("Person detected:\n");
            for ([Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html) track : personDetectionAnnotation.getTracksList()) {
              [VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html) segment = track.getSegment();
              System.out.printf(
                  "\tStart: %d.%.0fs\n",
                  segment.[getStartTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getStartTimeOffset__)().getSeconds(),
                  segment.[getStartTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getStartTimeOffset__)().getNanos() / 1e6);
              System.out.printf(
                  "\tEnd: %d.%.0fs\n",
                  segment.[getEndTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getEndTimeOffset__)().getSeconds(), segment.[getEndTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getEndTimeOffset__)().getNanos() / 1e6);
    
              // Each segment includes timestamped objects that include characteristic--e.g. clothes,
              // posture of the person detected.
              [TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html) firstTimestampedObject = track.getTimestampedObjects(0);
    
              // Attributes include unique pieces of clothing, poses (i.e., body landmarks)
              // of the person detected.
              for ([DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html) attribute : firstTimestampedObject.[getAttributesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html#com_google_cloud_videointelligence_v1_TimestampedObject_getAttributesList__)()) {
                System.out.printf(
                    "\tAttribute: %s; Value: %s\n", attribute.getName(), attribute.getValue());
              }
    
              // Landmarks in person detection include body parts.
              for ([DetectedLandmark](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedLandmark.html) attribute : firstTimestampedObject.[getLandmarksList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html#com_google_cloud_videointelligence_v1_TimestampedObject_getLandmarksList__)()) {
                System.out.printf(
                    "\tLandmark: %s; Vertex: %f, %f\n",
                    attribute.getName(), attribute.getPoint().getX(), attribute.getPoint().getY());
              }
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
    // const gcsUri = 'GCS URI of the video to analyze, e.g. gs://my-bucket/my-video.mp4';
    
    // Imports the Google Cloud Video Intelligence library + Node's fs library
    const Video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1;
    
    // Creates a client
    const video = new Video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    async function detectPersonGCS() {
      const request = {
        inputUri: gcsUri,
        features: ['PERSON_DETECTION'],
        videoContext: {
          personDetectionConfig: {
            // Must set includeBoundingBoxes to true to get poses and attributes.
            includeBoundingBoxes: true,
            includePoseLandmarks: true,
            includeAttributes: true,
          },
        },
      };
      // Detects faces in a video
      // We get the first result because we only process 1 video
      const [operation] = await video.annotateVideo(request);
      const results = await operation.promise();
      console.log('Waiting for operation to complete...');
    
      // Gets annotations for video
      const personAnnotations =
        results[0].annotationResults[0].personDetectionAnnotations;
    
      for (const {tracks} of personAnnotations) {
        console.log('Person detected:');
    
        for (const {segment, timestampedObjects} of tracks) {
          console.log(
            `\tStart: ${segment.startTimeOffset.seconds}` +
              `.${(segment.startTimeOffset.nanos / 1e6).toFixed(0)}s`
          );
          console.log(
            `\tEnd: ${segment.endTimeOffset.seconds}.` +
              `${(segment.endTimeOffset.nanos / 1e6).toFixed(0)}s`
          );
    
          // Each segment includes timestamped objects that
          // include characteristic--e.g. clothes, posture
          // of the person detected.
          const [firstTimestampedObject] = timestampedObjects;
    
          // Attributes include unique pieces of clothing, poses (i.e., body
          // landmarks) of the person detected.
          for (const {name, value} of firstTimestampedObject.attributes) {
            console.log(`\tAttribute: ${name}; Value: ${value}`);
          }
    
          // Landmarks in person detection include body parts.
          for (const {name, point} of firstTimestampedObject.landmarks) {
            console.log(`\tLandmark: ${name}; Vertex: ${point.x}, ${point.y}`);
          }
        }
      }
    }
    
    detectPersonGCS();

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import videointelligence_v1 as videointelligence
    
    
    def detect_person(gcs_uri="gs://YOUR_BUCKET_ID/path/to/your/video.mp4"):
        """Detects people in a video."""
    
        client = videointelligence.VideoIntelligenceServiceClient()
    
        # Configure the request
        config = videointelligence.types.PersonDetectionConfig(
            include_bounding_boxes=True,
            include_attributes=True,
            include_pose_landmarks=True,
        )
        context = videointelligence.types.VideoContext(person_detection_config=config)
    
        # Start the asynchronous request
        operation = client.annotate_video(
            request={
                "features": [videointelligence.Feature.PERSON_DETECTION],
                "input_uri": gcs_uri,
                "video_context": context,
            }
        )
    
        print("\nProcessing video for person detection annotations.")
        result = operation.result(timeout=300)
    
        print("\nFinished processing.\n")
    
        # Retrieve the first result, because a single video was processed.
        annotation_result = result.annotation_results[0]
    
        for annotation in annotation_result.person_detection_annotations:
            print("Person detected:")
            for track in annotation.tracks:
                print(
                    "Segment: {}s to {}s".format(
                        track.segment.start_time_offset.seconds
                        + track.segment.start_time_offset.microseconds / 1e6,
                        track.segment.end_time_offset.seconds
                        + track.segment.end_time_offset.microseconds / 1e6,
                    )
                )
    
                # Each segment includes timestamped objects that include
                # characteristics - -e.g.clothes, posture of the person detected.
                # Grab the first timestamped object
                timestamped_object = track.timestamped_objects[0]
                box = timestamped_object.normalized_bounding_box
                print("Bounding box:")
                print("\tleft  : {}".format(box.left))
                print("\ttop   : {}".format(box.top))
                print("\tright : {}".format(box.right))
                print("\tbottom: {}".format(box.bottom))
    
                # Attributes include unique pieces of clothing,
                # poses, or hair color.
                print("Attributes:")
                for attribute in timestamped_object.attributes:
                    print(
                        "\t{}:{} {}".format(
                            attribute.name, attribute.value, attribute.confidence
                        )
                    )
    
                # Landmarks in person detection include body parts such as
                # left_shoulder, right_ear, and right_ankle
                print("Landmarks:")
                for landmark in timestamped_object.landmarks:
                    print(
                        "\t{}: {} (x={}, y={})".format(
                            landmark.name,
                            landmark.confidence,
                            landmark.point.x,  # Normalized vertex
                            landmark.point.y,  # Normalized vertex
                        )
                    )
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

## Person detection from a local file

The following example uses person detection to find entities in a video from a video file uploaded from your local machine.

### REST

### Send the process request

To perform person detection on a local video file, base64-encode the contents of the video file. For information on how to base64-encode the contents of a video file, see [Base64 Encoding](https://docs.cloud.google.com/video-intelligence/docs/base64). Then, make a POST request to the [`videos:annotate`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/videos/annotate) method. Include the base64-encoded contents in the `inputContent` field of the request and specify the `PERSON_DETECTION` feature.

The following shows an example of a POST request using curl. The example uses the Google Cloud CLI to create an access token. For instructions on installing the gcloud CLI, see the [Video Intelligence API Quickstart](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)

Before using any of the request data, make the following replacements: 

  * inputContent: Local video file in binary format  
For example: 'AAAAGGZ0eXBtcDQyAAAAAGlzb21tcDQyAAGVYW1vb3YAAABsbXZoZAAAAADWvhlR1r4ZUQABX5ABCOxo AAEAAAEAAAAAAA4...'
  * PROJECT_NUMBER: The numeric identifier for your Google Cloud project



HTTP method and URL: 
    
    
    POST https://videointelligence.googleapis.com/v1/videos:annotate

Request JSON body: 
    
    
    {
      "inputUri": "Local video file in binary format",
      "features": ["PERSON_DETECTION"],
      "videoContext": {
        "personDetectionConfig": {
          "includeBoundingBoxes": true,
          "includePoseLandmarks": true,
          "includeAttributes": true
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

#### Response
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/var>/operations/OPERATION_ID"
    
    }
    

If the request is successful, Video Intelligence the `name` for your operation. The above shows an example of such a response, where `project-number` is the number of your project and `operation-id` is the ID of the long-running operation created for the request.

`{ "name": "us-west1.17122464255125931980" }`

### Get the results

To retrieve the result of the operation, make a GET request to the [`operations`](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/v1/operations/get) endpoint and specify the name of your operation.

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
      "name": "us-west1.10001026834554604237",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress",
        "annotationProgress": [
          {
            "progressPercent": 100,
            "startTime": "2020-02-08T21:26:56.577807Z",
            "updateTime": "2020-02-08T21:28:09.620665Z"
          }
        ]
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
        "annotationResults": [
          {
            "personDetectionAnnotations": [
              {
                "tracks": [
                  {
                    "segment": {
                      "startTimeOffset": "0s",
                      "endTimeOffset": "1.507436s"
                    }
                  },
                  ...
                ]
              }
            ]
          }
        ]
      }
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html);
    import com.google.cloud.videointelligence.v1.[DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html);
    import com.google.cloud.videointelligence.v1.[DetectedLandmark](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedLandmark.html);
    import com.google.cloud.videointelligence.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html);
    import com.google.cloud.videointelligence.v1.[PersonDetectionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionAnnotation.html);
    import com.google.cloud.videointelligence.v1.[PersonDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionConfig.html);
    import com.google.cloud.videointelligence.v1.[TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html);
    import com.google.cloud.videointelligence.v1.[Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html);
    import com.google.cloud.videointelligence.v1.[VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html);
    import com.google.cloud.videointelligence.v1.[VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html);
    import com.google.cloud.videointelligence.v1.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html);
    import com.google.cloud.videointelligence.v1.[VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    
    public class DetectPerson {
    
      public static void detectPerson() throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String localFilePath = "resources/googlework_short.mp4";
        detectPerson(localFilePath);
      }
    
      // Detects people in a video stored in a local file using the Cloud Video Intelligence API.
      public static void detectPerson(String localFilePath) throws Exception {
        try ([VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html) videoIntelligenceServiceClient =
            [VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html).create()) {
          // Reads a local video file and converts it to base64.
          Path path = Paths.get(localFilePath);
          byte[] data = Files.readAllBytes(path);
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) inputContent = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(data);
    
          [PersonDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionConfig.html) personDetectionConfig =
              [PersonDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionConfig.html).newBuilder()
                  // Must set includeBoundingBoxes to true to get poses and attributes.
                  .setIncludeBoundingBoxes(true)
                  .[setIncludePoseLandmarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionConfig.Builder.html#com_google_cloud_videointelligence_v1_PersonDetectionConfig_Builder_setIncludePoseLandmarks_boolean_)(true)
                  .setIncludeAttributes(true)
                  .build();
          [VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html) videoContext =
              [VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html).newBuilder().[setPersonDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.Builder.html#com_google_cloud_videointelligence_v1_VideoContext_Builder_setPersonDetectionConfig_com_google_cloud_videointelligence_v1_PersonDetectionConfig_)(personDetectionConfig).build();
    
          [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html) request =
              [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html).newBuilder()
                  .[setInputContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_setInputContent_com_google_protobuf_ByteString_)(inputContent)
                  .[addFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_addFeatures_com_google_cloud_videointelligence_v1_Feature_)([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html).PERSON_DETECTION)
                  .[setVideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_setVideoContext_com_google_cloud_videointelligence_v1_VideoContext_)(videoContext)
                  .build();
    
          // Detects people in a video
          // We get the first result because only one video is processed.
          OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
              videoIntelligenceServiceClient.[annotateVideoAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html#com_google_cloud_videointelligence_v1_VideoIntelligenceServiceClient_annotateVideoAsync_com_google_cloud_videointelligence_v1_AnnotateVideoRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
          [AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html) response = future.get();
    
          // Gets annotations for video
          [VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html) annotationResult = response.[getAnnotationResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html#com_google_cloud_videointelligence_v1_AnnotateVideoResponse_getAnnotationResultsList__)().get(0);
    
          // Annotations for list of people detected, tracked and recognized in video.
          for ([PersonDetectionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.PersonDetectionAnnotation.html) personDetectionAnnotation :
              annotationResult.[getPersonDetectionAnnotationsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html#com_google_cloud_videointelligence_v1_VideoAnnotationResults_getPersonDetectionAnnotationsList__)()) {
            System.out.print("Person detected:\n");
            for ([Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html) track : personDetectionAnnotation.getTracksList()) {
              [VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html) segment = track.getSegment();
              System.out.printf(
                  "\tStart: %d.%.0fs\n",
                  segment.[getStartTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getStartTimeOffset__)().getSeconds(),
                  segment.[getStartTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getStartTimeOffset__)().getNanos() / 1e6);
              System.out.printf(
                  "\tEnd: %d.%.0fs\n",
                  segment.[getEndTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getEndTimeOffset__)().getSeconds(), segment.[getEndTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getEndTimeOffset__)().getNanos() / 1e6);
    
              // Each segment includes timestamped objects that include characteristic--e.g. clothes,
              // posture of the person detected.
              [TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html) firstTimestampedObject = track.getTimestampedObjects(0);
    
              // Attributes include unique pieces of clothing, poses (i.e., body landmarks)
              // of the person detected.
              for ([DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html) attribute : firstTimestampedObject.[getAttributesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html#com_google_cloud_videointelligence_v1_TimestampedObject_getAttributesList__)()) {
                System.out.printf(
                    "\tAttribute: %s; Value: %s\n", attribute.getName(), attribute.getValue());
              }
    
              // Landmarks in person detection include body parts.
              for ([DetectedLandmark](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedLandmark.html) attribute : firstTimestampedObject.[getLandmarksList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html#com_google_cloud_videointelligence_v1_TimestampedObject_getLandmarksList__)()) {
                System.out.printf(
                    "\tLandmark: %s; Vertex: %f, %f\n",
                    attribute.getName(), attribute.getPoint().getX(), attribute.getPoint().getY());
              }
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
    // const gcsUri = 'GCS URI of the video to analyze, e.g. gs://my-bucket/my-video.mp4';
    
    // Imports the Google Cloud Video Intelligence library + Node's fs library
    const Video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1;
    const fs = require('fs');
    // Creates a client
    const video = new Video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const path = 'Local file to analyze, e.g. ./my-file.mp4';
    
    // Reads a local video file and converts it to base64
    const file = fs.readFileSync(path);
    const inputContent = file.toString('base64');
    
    async function detectPerson() {
      const request = {
        inputContent: inputContent,
        features: ['PERSON_DETECTION'],
        videoContext: {
          personDetectionConfig: {
            // Must set includeBoundingBoxes to true to get poses and attributes.
            includeBoundingBoxes: true,
            includePoseLandmarks: true,
            includeAttributes: true,
          },
        },
      };
      // Detects faces in a video
      // We get the first result because we only process 1 video
      const [operation] = await video.annotateVideo(request);
      const results = await operation.promise();
      console.log('Waiting for operation to complete...');
    
      // Gets annotations for video
      const personAnnotations =
        results[0].annotationResults[0].personDetectionAnnotations;
    
      for (const {tracks} of personAnnotations) {
        console.log('Person detected:');
    
        for (const {segment, timestampedObjects} of tracks) {
          console.log(
            `\tStart: ${segment.startTimeOffset.seconds}` +
              `.${(segment.startTimeOffset.nanos / 1e6).toFixed(0)}s`
          );
          console.log(
            `\tEnd: ${segment.endTimeOffset.seconds}.` +
              `${(segment.endTimeOffset.nanos / 1e6).toFixed(0)}s`
          );
    
          // Each segment includes timestamped objects that
          // include characteristic--e.g. clothes, posture
          // of the person detected.
          const [firstTimestampedObject] = timestampedObjects;
    
          // Attributes include unique pieces of clothing, poses (i.e., body
          // landmarks) of the person detected.
          for (const {name, value} of firstTimestampedObject.attributes) {
            console.log(`\tAttribute: ${name}; Value: ${value}`);
          }
    
          // Landmarks in person detection include body parts.
          for (const {name, point} of firstTimestampedObject.landmarks) {
            console.log(`\tLandmark: ${name}; Vertex: ${point.x}, ${point.y}`);
          }
        }
      }
    }
    
    detectPerson();

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import io
    
    from google.cloud import videointelligence_v1 as videointelligence
    
    
    def detect_person(local_file_path="path/to/your/video-file.mp4"):
        """Detects people in a video from a local file."""
    
        client = videointelligence.VideoIntelligenceServiceClient()
    
        with io.open(local_file_path, "rb") as f:
            input_content = f.read()
    
        # Configure the request
        config = videointelligence.types.PersonDetectionConfig(
            include_bounding_boxes=True,
            include_attributes=True,
            include_pose_landmarks=True,
        )
        context = videointelligence.types.VideoContext(person_detection_config=config)
    
        # Start the asynchronous request
        operation = client.annotate_video(
            request={
                "features": [videointelligence.Feature.PERSON_DETECTION],
                "input_content": input_content,
                "video_context": context,
            }
        )
    
        print("\nProcessing video for person detection annotations.")
        result = operation.result(timeout=300)
    
        print("\nFinished processing.\n")
    
        # Retrieve the first result, because a single video was processed.
        annotation_result = result.annotation_results[0]
    
        for annotation in annotation_result.person_detection_annotations:
            print("Person detected:")
            for track in annotation.tracks:
                print(
                    "Segment: {}s to {}s".format(
                        track.segment.start_time_offset.seconds
                        + track.segment.start_time_offset.microseconds / 1e6,
                        track.segment.end_time_offset.seconds
                        + track.segment.end_time_offset.microseconds / 1e6,
                    )
                )
    
                # Each segment includes timestamped objects that include
                # characteristic - -e.g.clothes, posture of the person detected.
                # Grab the first timestamped object
                timestamped_object = track.timestamped_objects[0]
                box = timestamped_object.normalized_bounding_box
                print("Bounding box:")
                print("\tleft  : {}".format(box.left))
                print("\ttop   : {}".format(box.top))
                print("\tright : {}".format(box.right))
                print("\tbottom: {}".format(box.bottom))
    
                # Attributes include unique pieces of clothing,
                # poses, or hair color.
                print("Attributes:")
                for attribute in timestamped_object.attributes:
                    print(
                        "\t{}:{} {}".format(
                            attribute.name, attribute.value, attribute.confidence
                        )
                    )
    
                # Landmarks in person detection include body parts such as
                # left_shoulder, right_ear, and right_ankle
                print("Landmarks:")
                for landmark in timestamped_object.landmarks:
                    print(
                        "\t{}: {} (x={}, y={})".format(
                            landmark.name,
                            landmark.confidence,
                            landmark.point.x,  # Normalized vertex
                            landmark.point.y,  # Normalized vertex
                        )
                    )
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.VideoIntelligence.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-videointelligence/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/video-intelligence/docs/libraries) on the client libraries page and then visit the [Video Intelligence reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-video_intelligence/latest/Google/Cloud/VideoIntelligence/V1.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
