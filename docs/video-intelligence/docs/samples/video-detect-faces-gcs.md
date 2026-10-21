---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-detect-faces-gcs/
title: Detect faces in a Cloud Storage file \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:40.594077+00:00
---

# Detect faces in a Cloud Storage file  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-detect-faces-gcs/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Detect faces in a Cloud Storage file Stay organized with collections  Save and categorize content based on your preferences. 

Detect faces in a Cloud Storage file

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect faces](https://docs.cloud.google.com/video-intelligence/docs/face-detection)



## Code sample

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoProgress.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html);
    import com.google.cloud.videointelligence.v1.[AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html);
    import com.google.cloud.videointelligence.v1.[DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html);
    import com.google.cloud.videointelligence.v1.[FaceDetectionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.FaceDetectionAnnotation.html);
    import com.google.cloud.videointelligence.v1.[FaceDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.FaceDetectionConfig.html);
    import com.google.cloud.videointelligence.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html);
    import com.google.cloud.videointelligence.v1.[TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html);
    import com.google.cloud.videointelligence.v1.[Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html);
    import com.google.cloud.videointelligence.v1.[VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html);
    import com.google.cloud.videointelligence.v1.[VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html);
    import com.google.cloud.videointelligence.v1.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html);
    import com.google.cloud.videointelligence.v1.[VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html);
    
    public class DetectFacesGcs {
    
      public static void detectFacesGcs() throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String gcsUri = "gs://cloud-samples-data/video/googlework_short.mp4";
        detectFacesGcs(gcsUri);
      }
    
      // Detects faces in a video stored in Google Cloud Storage using the Cloud Video Intelligence API.
      public static void detectFacesGcs(String gcsUri) throws Exception {
        try ([VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html) videoIntelligenceServiceClient =
            [VideoIntelligenceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html).create()) {
    
          [FaceDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.FaceDetectionConfig.html) faceDetectionConfig =
              [FaceDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.FaceDetectionConfig.html).newBuilder()
                  // Must set includeBoundingBoxes to true to get facial attributes.
                  .setIncludeBoundingBoxes(true)
                  .setIncludeAttributes(true)
                  .build();
          [VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html) videoContext =
              [VideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.html).newBuilder().[setFaceDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoContext.Builder.html#com_google_cloud_videointelligence_v1_VideoContext_Builder_setFaceDetectionConfig_com_google_cloud_videointelligence_v1_FaceDetectionConfig_)(faceDetectionConfig).build();
    
          [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html) request =
              [AnnotateVideoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.html).newBuilder()
                  .setInputUri(gcsUri)
                  .[addFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_addFeatures_com_google_cloud_videointelligence_v1_Feature_)([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Feature.html).FACE_DETECTION)
                  .[setVideoContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoRequest.Builder.html#com_google_cloud_videointelligence_v1_AnnotateVideoRequest_Builder_setVideoContext_com_google_cloud_videointelligence_v1_VideoContext_)(videoContext)
                  .build();
    
          // Detects faces in a video
          OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> future =
              videoIntelligenceServiceClient.[annotateVideoAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient.html#com_google_cloud_videointelligence_v1_VideoIntelligenceServiceClient_annotateVideoAsync_com_google_cloud_videointelligence_v1_AnnotateVideoRequest_)(request);
    
          System.out.println("Waiting for operation to complete...");
          [AnnotateVideoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
    
          // Gets annotations for video
          [VideoAnnotationResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html) annotationResult = response.[getAnnotationResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.AnnotateVideoResponse.html#com_google_cloud_videointelligence_v1_AnnotateVideoResponse_getAnnotationResultsList__)().[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(0);
    
          // Annotations for list of people detected, tracked and recognized in video.
          for ([FaceDetectionAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.FaceDetectionAnnotation.html) faceDetectionAnnotation :
              annotationResult.[getFaceDetectionAnnotationsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoAnnotationResults.html#com_google_cloud_videointelligence_v1_VideoAnnotationResults_getFaceDetectionAnnotationsList__)()) {
            System.out.print("Face detected:\n");
            for ([Track](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.Track.html) track : faceDetectionAnnotation.getTracksList()) {
              [VideoSegment](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html) segment = track.getSegment();
              System.out.printf(
                  "\tStart: %d.%.0fs\n",
                  segment.[getStartTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getStartTimeOffset__)().getSeconds(),
                  segment.[getStartTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getStartTimeOffset__)().getNanos() / 1e6);
              System.out.printf(
                  "\tEnd: %d.%.0fs\n",
                  segment.[getEndTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getEndTimeOffset__)().getSeconds(), segment.[getEndTimeOffset](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.VideoSegment.html#com_google_cloud_videointelligence_v1_VideoSegment_getEndTimeOffset__)().getNanos() / 1e6);
    
              // Each segment includes timestamped objects that
              // include characteristics of the face detected.
              [TimestampedObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html) firstTimestampedObject = track.getTimestampedObjects(0);
    
              for ([DetectedAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.DetectedAttribute.html) attribute : firstTimestampedObject.[getAttributesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-intelligence/latest/com.google.cloud.videointelligence.v1.TimestampedObject.html#com_google_cloud_videointelligence_v1_TimestampedObject_getAttributesList__)()) {
                // Attributes include glasses, headwear, smiling, direction of gaze
                System.out.printf(
                    "\tAttribute %s: %s %s\n",
                    attribute.getName(), attribute.getValue(), attribute.getConfidence());
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
    
    async function detectFacesGCS() {
      const request = {
        inputUri: gcsUri,
        features: ['FACE_DETECTION'],
        videoContext: {
          faceDetectionConfig: {
            // Must set includeBoundingBoxes to true to get facial attributes.
            includeBoundingBoxes: true,
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
      const faceAnnotations =
        results[0].annotationResults[0].faceDetectionAnnotations;
    
      for (const {tracks} of faceAnnotations) {
        console.log('Face detected:');
    
        for (const {segment, timestampedObjects} of tracks) {
          console.log(
            `\tStart: ${segment.startTimeOffset.seconds}.` +
              `${(segment.startTimeOffset.nanos / 1e6).toFixed(0)}s`
          );
          console.log(
            `\tEnd: ${segment.endTimeOffset.seconds}.` +
              `${(segment.endTimeOffset.nanos / 1e6).toFixed(0)}s`
          );
    
          // Each segment includes timestamped objects that
          // include characteristics of the face detected.
          const [firstTimestapedObject] = timestampedObjects;
    
          for (const {name} of firstTimestapedObject.attributes) {
            // Attributes include 'glasses', 'headwear', 'smiling'.
            console.log(`\tAttribute: ${name}; `);
          }
        }
      }
    }
    
    detectFacesGCS();

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import videointelligence_v1 as videointelligence
    
    
    def detect_faces(gcs_uri="gs://YOUR_BUCKET_ID/path/to/your/video.mp4"):
        """Detects faces in a video."""
    
        client = videointelligence.VideoIntelligenceServiceClient()
    
        # Configure the request
        config = videointelligence.FaceDetectionConfig(
            include_bounding_boxes=True, include_attributes=True
        )
        context = videointelligence.VideoContext(face_detection_config=config)
    
        # Start the asynchronous request
        operation = client.annotate_video(
            request={
                "features": [videointelligence.Feature.FACE_DETECTION],
                "input_uri": gcs_uri,
                "video_context": context,
            }
        )
    
        print("\nProcessing video for face detection annotations.")
        result = operation.result(timeout=300)
    
        print("\nFinished processing.\n")
    
        # Retrieve the first result, because a single video was processed.
        annotation_result = result.annotation_results[0]
    
        for annotation in annotation_result.face_detection_annotations:
            print("Face detected:")
            for track in annotation.tracks:
                print(
                    "Segment: {}s to {}s".format(
                        track.segment.start_time_offset.seconds
                        + track.segment.start_time_offset.microseconds / 1e6,
                        track.segment.end_time_offset.seconds
                        + track.segment.end_time_offset.microseconds / 1e6,
                    )
                )
    
                # Each segment includes timestamped faces that include
                # characteristics of the face detected.
                # Grab the first timestamped face
                timestamped_object = track.timestamped_objects[0]
                box = timestamped_object.normalized_bounding_box
                print("Bounding box:")
                print("\tleft  : {}".format(box.left))
                print("\ttop   : {}".format(box.top))
                print("\tright : {}".format(box.right))
                print("\tbottom: {}".format(box.bottom))
    
                # Attributes include glasses, headwear, smiling, direction of gaze
                print("Attributes:")
                for attribute in timestamped_object.attributes:
                    print(
                        "\t{}:{} {}".format(
                            attribute.name, attribute.value, attribute.confidence
                        )
                    )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
