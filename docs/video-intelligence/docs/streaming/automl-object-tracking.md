---
url: https://docs.cloud.google.com/video-intelligence/docs/streaming/automl-object-tracking/
title: Object tracking \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:06.968914+00:00
---

# Object tracking  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/streaming/automl-object-tracking/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Object tracking Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Object tracking tracks multiple objects detected in an input video. To use a pre-trained model see [Analyze labels](https://cloud.google.com/video-intelligence/docs/streaming/label-analysis). 

## Use AutoML video

### Before you begin

For background on creating an AutoML model, check out the Vertex AI [Beginner's guide](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide#video). For instructions on how to create your AutoML model, start with "Creating a dataset" using the [console](https://docs.cloud.google.com/vertex-ai/docs/datasets/create-dataset-console#video) or [api](https://docs.cloud.google.com/vertex-ai/docs/datasets/create-dataset-api#video).

### Use your AutoML model

The following code sample demonstrates how to use your [AutoML model](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide#video) for object tracking using the streaming client library.

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[BidiStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream.html);
    import com.google.cloud.videointelligence.v1p3beta1.ObjectTrackingAnnotation;
    import com.google.cloud.videointelligence.v1p3beta1.ObjectTrackingFrame;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingAnnotateVideoRequest;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingAnnotateVideoResponse;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingAutomlObjectTrackingConfig;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingFeature;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingVideoAnnotationResults;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingVideoConfig;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingVideoIntelligenceServiceClient;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import io.grpc.StatusRuntimeException;
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.util.Arrays;
    
    class StreamingAutoMlObjectTracking {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "YOUR_VIDEO_FILE";
        String projectId = "YOUR_PROJECT_ID";
        String modelId = "YOUR_AUTOML_OBJECT_TRACKING_MODEL_ID";
        streamingAutoMlObjectTracking(filePath, projectId, modelId);
      }
    
      // Perform streaming video object tracking with an AutoML Model
      static void streamingAutoMlObjectTracking(String filePath, String projectId, String modelId)
          throws StatusRuntimeException, IOException {
    
        try (StreamingVideoIntelligenceServiceClient client =
            StreamingVideoIntelligenceServiceClient.create()) {
    
          Path path = Paths.get(filePath);
          byte[] data = Files.readAllBytes(path);
          // Set the chunk size to 5MB (recommended less than 10MB).
          int chunkSize = 5 * 1024 * 1024;
          int numChunks = (int) Math.ceil((double) data.length / chunkSize);
    
          String modelPath =
              String.format("projects/%s/locations/us-central1/models/%s", projectId, modelId);
    
          StreamingAutomlObjectTrackingConfig streamingAutomlObjectTrackingConfig =
              StreamingAutomlObjectTrackingConfig.newBuilder().setModelName(modelPath).build();
    
          StreamingVideoConfig streamingVideoConfig =
              StreamingVideoConfig.newBuilder()
                  .setFeature(StreamingFeature.STREAMING_AUTOML_OBJECT_TRACKING)
                  .setAutomlObjectTrackingConfig(streamingAutomlObjectTrackingConfig)
                  .build();
    
          BidiStream<StreamingAnnotateVideoRequest, StreamingAnnotateVideoResponse> call =
              client.streamingAnnotateVideoCallable().call();
    
          // The first request must **only** contain the audio configuration:
          call.send(
              StreamingAnnotateVideoRequest.newBuilder().setVideoConfig(streamingVideoConfig).build());
    
          // Subsequent requests must **only** contain the audio data.
          // Send the requests in chunks
          for (int i = 0; i < numChunks; i++) {
            call.send(
                StreamingAnnotateVideoRequest.newBuilder()
                    .setInputContent(
                        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(
                            Arrays.copyOfRange(data, i * chunkSize, i * chunkSize + chunkSize)))
                    .build());
          }
    
          // Tell the service you are done sending data
          call.closeSend();
    
          for (StreamingAnnotateVideoResponse response : call) {
            StreamingVideoAnnotationResults annotationResults = response.getAnnotationResults();
    
            for (ObjectTrackingAnnotation objectAnnotations :
                annotationResults.getObjectAnnotationsList()) {
    
              String entity = objectAnnotations.getEntity().[getDescription](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html#com_google_protobuf_Descriptors_DescriptorValidationException_getDescription__)();
              float confidence = objectAnnotations.getConfidence();
              long trackId = objectAnnotations.getTrackId();
              System.out.format("%s: %f (ID: %d)\n", entity, confidence, trackId);
    
              // In streaming, there is always one frame.
              ObjectTrackingFrame frame = objectAnnotations.getFrames(0);
              double offset =
                  frame.getTimeOffset().getSeconds() + frame.getTimeOffset().getNanos() / 1e9;
              System.out.format("Offset: %f\n", offset);
    
              System.out.println("Bounding Box:");
              System.out.format("\tLeft: %f\n", frame.getNormalizedBoundingBox().getLeft());
              System.out.format("\tTop: %f\n", frame.getNormalizedBoundingBox().getTop());
              System.out.format("\tRight: %f\n", frame.getNormalizedBoundingBox().getRight());
              System.out.format("\tBottom: %f\n", frame.getNormalizedBoundingBox().getBottom());
            }
          }
          System.out.println("Video streamed successfully.");
        }
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const path = 'Local file to analyze, e.g. ./my-file.mp4';
    // const modelId = 'AutoML model'
    // const projectId = 'Your GCP Project'
    
    const {StreamingVideoIntelligenceServiceClient} =
      require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1p3beta1;
    const fs = require('fs');
    
    // Instantiates a client
    const client = new [StreamingVideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/v1p3beta1.streamingvideointelligenceserviceclient.html)();
    
    // Streaming configuration
    const modelName = `projects/${projectId}/locations/us-central1/models/${modelId}`;
    const configRequest = {
      videoConfig: {
        feature: '[STREAMING_AUTOML_OBJECT_TRACKING](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.streamingfeature.html)',
        automlObjectTrackingConfig: {
          modelName: modelName,
        },
      },
    };
    
    const readStream = fs.createReadStream(path, {
      highWaterMark: 5 * 1024 * 1024, //chunk size set to 5MB (recommended less than 10MB)
      encoding: 'base64',
    });
    //Load file content
    // Note: Input videos must have supported video codecs. See
    // https://cloud.google.com/video-intelligence/docs/streaming/streaming#supported_video_codecs
    // for more details.
    const chunks = [];
    readStream
      .on('data', chunk => {
        const request = {
          inputContent: chunk.toString(),
        };
        chunks.push(request);
      })
      .on('close', () => {
        // configRequest should be the first in the stream of requests
        stream.write(configRequest);
        for (let i = 0; i < chunks.length; i++) {
          stream.write(chunks[i]);
        }
        stream.end();
      });
    
    const stream = client.streamingAnnotateVideo().on('data', response => {
      //Gets annotations for video
      const annotations = response.annotationResults;
      const objects = annotations.objectAnnotations;
      objects.forEach(object => {
        console.log(`Entity description: ${object.entity.description}`);
        console.log(`Entity id: ${object.entity.entityId}`);
        console.log(`Track id: ${object.trackId}`);
        console.log(`Confidence: ${object.confidence}`);
        console.log(
          `Time offset for the frame: ${
            object.frames[0].timeOffset.seconds || 0
          }` + `.${(object.frames[0].timeOffset.nanos / 1e6).toFixed(0)}s`
        );
        //Every annotation has only one frame.
        const box = object.frames[0].normalizedBoundingBox;
        console.log('Bounding box position:');
        console.log(`\tleft: ${box.left}`);
        console.log(`\ttop: ${box.top}`);
        console.log(`\tright: ${box.right}`);
        console.log(`\tbottom: ${box.bottom}`);
      });
    });

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import io
    
    from google.cloud import videointelligence_v1p3beta1 as videointelligence
    
    # path = 'path_to_file'
    # project_id = 'project_id'
    # model_id = 'automl_object_tracking_model_id'
    
    client = videointelligence.StreamingVideoIntelligenceServiceClient()
    
    model_path = "projects/{}/locations/us-central1/models/{}".format(
        project_id, model_id
    )
    
    automl_config = videointelligence.StreamingAutomlObjectTrackingConfig(
        model_name=model_path
    )
    
    video_config = videointelligence.StreamingVideoConfig(
        feature=videointelligence.StreamingFeature.STREAMING_AUTOML_OBJECT_TRACKING,
        automl_object_tracking_config=automl_config,
    )
    
    # config_request should be the first in the stream of requests.
    config_request = videointelligence.StreamingAnnotateVideoRequest(
        video_config=video_config
    )
    
    # Set the chunk size to 5MB (recommended less than 10MB).
    chunk_size = 5 * 1024 * 1024
    
    # Load file content.
    # Note: Input videos must have supported video codecs. See
    # https://cloud.google.com/video-intelligence/docs/streaming/streaming#supported_video_codecs
    # for more details.
    stream = []
    with io.open(path, "rb") as video_file:
        while True:
            data = video_file.read(chunk_size)
            if not data:
                break
            stream.append(data)
    
    def stream_generator():
        yield config_request
        for chunk in stream:
            yield videointelligence.StreamingAnnotateVideoRequest(input_content=chunk)
    
    requests = stream_generator()
    
    # streaming_annotate_video returns a generator.
    # The default timeout is about 300 seconds.
    # To process longer videos it should be set to
    # larger than the length (in seconds) of the stream.
    responses = client.streaming_annotate_video(requests, timeout=900)
    
    # Each response corresponds to about 1 second of video.
    for response in responses:
        # Check for errors.
        if response.error.message:
            print(response.error.message)
            break
    
        object_annotations = response.annotation_results.object_annotations
    
        # object_annotations could be empty
        if not object_annotations:
            continue
    
        for annotation in object_annotations:
            # Each annotation has one frame, which has a timeoffset.
            frame = annotation.frames[0]
            time_offset = (
                frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
            )
    
            description = annotation.entity.description
            confidence = annotation.confidence
    
            # track_id tracks the same object in the video.
            track_id = annotation.track_id
    
            # description is in Unicode
            print("{}s".format(time_offset))
            print("\tEntity description: {}".format(description))
            print("\tTrack Id: {}".format(track_id))
            if annotation.entity.entity_id:
                print("\tEntity id: {}".format(annotation.entity.entity_id))
    
            print("\tConfidence: {}".format(confidence))
    
            # Every annotation has only one frame
            frame = annotation.frames[0]
            box = frame.normalized_bounding_box
            print("\tBounding box position:")
            print("\tleft  : {}".format(box.left))
            print("\ttop   : {}".format(box.top))
            print("\tright : {}".format(box.right))
            print("\tbottom: {}\n".format(box.bottom))

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
