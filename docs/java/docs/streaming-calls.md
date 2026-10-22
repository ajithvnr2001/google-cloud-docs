---
url: https://docs.cloud.google.com/java/docs/streaming-calls/
title: Stream calls on Cloud Client Libraries for Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:46.789640+00:00
---

# Stream calls on Cloud Client Libraries for Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/streaming-calls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Stream calls on Cloud Client Libraries for Java Stay organized with collections  Save and categorize content based on your preferences. 

Streaming calls enable more complex interaction patterns than simple request/response, allowing for multiple messages to be sent or received over a single connection.

Cloud Client Libraries for Java support three types of streaming calls:

  * **Server streaming:** The server sends a stream of responses back to you.
  * **Client streaming:** You send a stream of requests to the server.
  * **Bidirectional streaming:** You can send a stream of requests to the server, and the server can send back a stream of responses to you.



The streaming implementations are modeled after gRPC-Java implementations for server, client, and bidirectional streaming. 

**Note:** These concepts are borrowed, and the Cloud Client Libraries for Java's implementations are not a direct copy.

## Streaming support across transports

Streaming is fully supported when using gRPC, but only partially supported for `HttpJson`. See the following table for streaming support.

Streaming Type | gRPC | HttpJson  
---|---|---  
Server Streaming | Supported | Supported  
Client Streaming | Supported | Not Supported  
Bidirectional Streaming | Supported | Not Supported  
  
Unary calls (non-streaming) are supported for both gRPC and HttpJson.

## Determining the type of streaming

To determine the streaming type of the call, check the returned `Callable` type:

  * **`ServerStreamingCallable`:** Server streaming.
  * **`ClientStreamingCallable`:** Client streaming.
  * **`BidiStreamingCallable`:** Bidirectional streaming.



For example, using Java-Aiplatform and Java-Speech:
    
    
    // Server Streaming
    ServerStreamingCallable<ReadTensorboardBlobDataRequest, ReadTensorboardBlobDataResponse> callable = aiplatformClient.readTensorboardBlobDataCallable();
    
    // Bidirectional Streaming
    BidiStreamingCallable<StreamingRecognizeRequest, StreamingRecognizeResponse> callable = speechClient.streamingRecognizeCallable();
    

## Making streaming calls

Making a streaming call will differ depending on whether you are using server streaming or bidirectional streaming.

## Server streaming

Server streaming doesn't require additional implementation. The `ServerStream` class lets you iterate the stream of responses. Using Java-Maps-Routing as an example, the following shows how to call the Server Streaming API:
    
    
    try (RoutesClient routesClient = RoutesClient.create()) {
      ServerStreamingCallable<ComputeRouteMatrixRequest, RouteMatrixElement> computeRouteMatrix =
        routesClient.computeRouteMatrixCallable();  
      ServerStream<RouteMatrixElement> stream = computeRouteMatrix.call(
        ComputeRouteMatrixRequest.newBuilder().build());
      for (RouteMatrixElement element : stream) {
        // Do something with response
      }
    }
    

In this example, the client sends a single `ComputeRouteMatrixRequest` and receives a stream of responses. 

## Bidirectional streaming

Bidirectional streaming requires additional implementation to make the call. Using Java-Speech as an example, the following steps provide an example implementation to make a bidirectional streaming call. 

First, implement the `ResponseObserver` interface using the following code as a guideline:
    
    
    class BidiResponseObserver<T> implements ResponseObserver<T> {
      private final List<T> responses = new ArrayList<>();
      private final SettableApiFuture<List<T>> future = SettableApiFuture.create();
    
      @Override
      public void onStart(StreamController controller) {
        // no-op
      }
    
      @Override
      public void onResponse(T response) {
        responses.add(response);
      }
    
      @Override
      public void onError(Throwable t) {
        future.setException(t);
      }
    
      @Override
      public void onComplete() {
        future.set(responses);
      }
    
      public SettableApiFuture<List<T>> getFuture() {
        return future;
      }
    }
    
    

Then, follow these steps:

  1. Create an instance of the observer:
         
         BidiResponseObserver<StreamingRecognizeResponse> responseObserver = new BidiResponseObserver<>();
         

  2. Pass the observer into the callable:
         
         ClientStream<EchoRequest> clientStream = speechClient.streamingRecognizeCallable().splitCall(responseObserver);
         

  3. Send the requests to the server and close the stream when complete:
         
         clientStream.send(StreamingRecognizeRequest.newBuilder().build());
         clientStream.send(StreamingRecognizeRequest.newBuilder().build());
         // ... other requests ...
         clientStream.send(StreamingRecognizeRequest.newBuilder().build());
         clientStream.closeSend();
         

  4. Iterate through the responses:
         
         List<StreamingRecognizeResponse> responses = responseObserver.getFuture().get();
         
         for (StreamingRecognizeResponse response : responses) {
           // Do something with response
         }
         




## Non-supported streaming errors

For client libraries that support both gRPC and HTTP/JSON transports, it's possible to accidentally configure the client library to invoke a non-supported streaming call. For example, the following configuration shows the Java-Speech's `HttpJson` client making a bidirectional streaming call:
    
    
    // SpeechClient is configured to use HttpJson
    try (SpeechClient speechClient = SpeechClient.create(SpeechSettings.newHttpJsonBuilder().build())) {
      // Bidi Callable is not supported in HttpJson
      BidiStreamingCallable<StreamingRecognizeRequest, StreamingRecognizeResponse> callable = speechClient.streamingRecognizeCallable();
      ...
    }
    

This doesn't result in a compilation error, but shows up as a runtime error: 
    
    
    Not implemented: streamingRecognizeCallable(). REST transport is not implemented for this method yet.
    Important: The client library MUST be configured with gRPC to use client or bidirectional streaming.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
