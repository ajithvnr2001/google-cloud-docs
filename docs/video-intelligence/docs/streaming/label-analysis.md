---
url: https://docs.cloud.google.com/video-intelligence/docs/streaming/label-analysis/
title: Label analysis \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:58.855191+00:00
---

# Label analysis  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/streaming/label-analysis/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Label analysis Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Label analysis identifies objects, locations, activities, animal species, products, and more.

## Use the standard model

The following code shows how to use Video Intelligence API streaming label detection to annotate a video.

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[BidiStream](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream.html);
    import com.google.cloud.videointelligence.v1p3beta1.LabelAnnotation;
    import com.google.cloud.videointelligence.v1p3beta1.LabelFrame;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingAnnotateVideoRequest;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingAnnotateVideoResponse;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingFeature;
    import com.google.cloud.videointelligence.v1p3beta1.StreamingLabelDetectionConfig;
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
    import java.util.concurrent.TimeoutException;
    
    class StreamingLabelDetection {
    
      // Perform streaming video label detection
      static void streamingLabelDetection(String filePath)
          throws IOException, TimeoutException, StatusRuntimeException {
        // String filePath = "path_to_your_video_file";
    
        try (StreamingVideoIntelligenceServiceClient client =
            StreamingVideoIntelligenceServiceClient.create()) {
    
          Path path = Paths.get(filePath);
          byte[] data = Files.readAllBytes(path);
          // Set the chunk size to 5MB (recommended less than 10MB).
          int chunkSize = 5 * 1024 * 1024;
          int numChunks = (int) Math.ceil((double) data.length / chunkSize);
    
          StreamingLabelDetectionConfig labelConfig =
              StreamingLabelDetectionConfig.newBuilder().setStationaryCamera(false).build();
    
          StreamingVideoConfig streamingVideoConfig =
              StreamingVideoConfig.newBuilder()
                  .setFeature(StreamingFeature.STREAMING_LABEL_DETECTION)
                  .setLabelDetectionConfig(labelConfig)
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
    
            for (LabelAnnotation annotation : annotationResults.getLabelAnnotationsList()) {
              String entity = annotation.getEntity().[getDescription](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.DescriptorValidationException.html#com_google_protobuf_Descriptors_DescriptorValidationException_getDescription__)();
    
              // There is only one frame per annotation
              LabelFrame labelFrame = annotation.getFrames(0);
              double offset =
                  labelFrame.getTimeOffset().getSeconds() + labelFrame.getTimeOffset().getNanos() / 1e9;
              float confidence = labelFrame.getConfidence();
    
              System.out.format("%fs: %s (%f)\n", offset, entity, confidence);
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
    // const path = 'Local file to analyze, e.g. ./my-file.mp4';
    const {StreamingVideoIntelligenceServiceClient} =
      require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1p3beta1;
    const fs = require('fs');
    
    // Instantiates a client
    const client = new [StreamingVideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/v1p3beta1.streamingvideointelligenceserviceclient.html)();
    // Streaming configuration
    const configRequest = {
      videoConfig: {
        feature: '[STREAMING_LABEL_DETECTION](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/video-intelligence/protos.google.cloud.videointelligence.v1p3beta1.streamingfeature.html)',
      },
    };
    const readStream = fs.createReadStream(path, {
      highWaterMark: 5 * 1024 * 1024, //chunk size set to 5MB (recommended less than 10MB)
      encoding: 'base64',
    });
    //Load file content
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
      const labels = annotations.labelAnnotations;
      labels.forEach(label => {
        console.log(
          `Label ${label.entity.description} occurs at: ${
            label.frames[0].timeOffset.seconds || 0
          }` + `.${(label.frames[0].timeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(` Confidence: ${label.frames[0].confidence}`);
      });
    });

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import videointelligence_v1p3beta1 as videointelligence
    
    # path = 'path_to_file'
    
    client = videointelligence.StreamingVideoIntelligenceServiceClient()
    
    # Set streaming config.
    config = videointelligence.StreamingVideoConfig(
        feature=(videointelligence.StreamingFeature.STREAMING_LABEL_DETECTION)
    )
    
    # config_request should be the first in the stream of requests.
    config_request = videointelligence.StreamingAnnotateVideoRequest(
        video_config=config
    )
    
    # Set the chunk size to 5MB (recommended less than 10MB).
    chunk_size = 5 * 1024 * 1024
    
    # Load file content.
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
    responses = client.streaming_annotate_video(requests, timeout=600)
    
    # Each response corresponds to about 1 second of video.
    for response in responses:
        # Check for errors.
        if response.error.message:
            print(response.error.message)
            break
    
        label_annotations = response.annotation_results.label_annotations
    
        # label_annotations could be empty
        if not label_annotations:
            continue
    
        for annotation in label_annotations:
            # Each annotation has one frame, which has a timeoffset.
            frame = annotation.frames[0]
            time_offset = (
                frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
            )
    
            description = annotation.entity.description
            confidence = annotation.frames[0].confidence
            # description is in Unicode
            print(
                "{}s: {} (confidence: {})".format(time_offset, description, confidence)
            )

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
