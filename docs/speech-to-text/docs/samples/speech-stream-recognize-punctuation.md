---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-stream-recognize-punctuation/
title: Streaming speech recognition with punctuation \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:59.258924+00:00
---

# Streaming speech recognition with punctuation  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-stream-recognize-punctuation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Streaming speech recognition with punctuation Stay organized with collections  Save and categorize content based on your preferences. 

Performs streaming speech recognition on raw PCM audio data.

## Code sample

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs streaming speech recognition on raw PCM audio data.
     *
     * @param fileName the path to a PCM audio file to transcribe.
     */
    public static void streamingTranscribeWithAutomaticPunctuation(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      byte[] data = Files.readAllBytes(path);
    
      // Instantiates a client with GOOGLE_APPLICATION_CREDENTIALS
      try (SpeechClient speech = SpeechClient.create()) {
    
        // Configure request with local raw PCM audio
        RecognitionConfig recConfig =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                .setSampleRateHertz(16000)
                .setEnableAutomaticPunctuation(true)
                .build();
    
        // Build the streaming config with the audio config
        StreamingRecognitionConfig config =
            StreamingRecognitionConfig.newBuilder().setConfig(recConfig).build();
    
        class ResponseApiStreamingObserver<T> implements ApiStreamObserver<T> {
          private final SettableFuture<List<T>> future = SettableFuture.create();
          private final List<T> messages = new java.util.ArrayList<T>();
    
          @Override
          public void onNext(T message) {
            messages.add(message);
          }
    
          @Override
          public void onError(Throwable t) {
            future.setException(t);
          }
    
          @Override
          public void onCompleted() {
            future.set(messages);
          }
    
          // Returns the SettableFuture object to get received messages / exceptions.
          public SettableFuture<List<T>> future() {
            return future;
          }
        }
    
        ResponseApiStreamingObserver<StreamingRecognizeResponse> responseObserver =
            new ResponseApiStreamingObserver<>();
    
        BidiStreamingCallable<StreamingRecognizeRequest, StreamingRecognizeResponse> callable =
            speech.streamingRecognizeCallable();
    
        ApiStreamObserver<StreamingRecognizeRequest> requestObserver =
            callable.bidiStreamingCall(responseObserver);
    
        // The first request must **only** contain the audio configuration:
        requestObserver.onNext(
            StreamingRecognizeRequest.newBuilder().setStreamingConfig(config).build());
    
        // Subsequent requests must **only** contain the audio data.
        requestObserver.onNext(
            StreamingRecognizeRequest.newBuilder()
                .setAudioContent(ByteString.copyFrom(data))
                .build());
    
        // Mark transmission as completed after sending the data.
        requestObserver.onCompleted();
    
        List<StreamingRecognizeResponse> responses = responseObserver.future().get();
    
        for (StreamingRecognizeResponse response : responses) {
          // For streaming recognize, the results list has one is_final result (if available) followed
          // by a number of in-progress results (if iterim_results is true) for subsequent utterances.
          // Just print the first result here.
          StreamingRecognitionResult result = response.getResultsList().get(0);
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
          System.out.printf("Transcript : %s\n", alternative.getTranscript());
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
