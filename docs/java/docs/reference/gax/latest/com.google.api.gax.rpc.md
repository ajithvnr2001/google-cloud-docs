---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc
title: Package com.google.api.gax.rpc (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:46.305285+00:00
---

# Package com.google.api.gax.rpc (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.api.gax.rpc (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/gax-java/gax/src/main/java/com/google/api/gax/rpc)  
---  
  
## Client Classes

Client classes are the main entry point to using a package. They contain several variations of Java methods for each of the API's methods. 

Client |  Description  
---|---  
[com.google.api.gax.rpc.LongRunningClient](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LongRunningClient) |  Implementation-agnostic interface for managing long-running operations.  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.api.gax.rpc.BatchingCallSettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchingCallSettings) |  A settings class to configure a UnaryCallable for calls to an API method that supports batching. The settings are provided using an instance of BatchingSettings.  
[com.google.api.gax.rpc.ClientSettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings) |  A base settings class to configure a client class. This base class includes settings that are applicable to all services, which includes things like settings for creating an executor, credentials, transport-specific settings, and identifiers  
[com.google.api.gax.rpc.OperationCallSettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings) |  A settings class to configure an OperationCallable for calls to initiate, resume, and cancel a long-running operation.  
[com.google.api.gax.rpc.PagedCallSettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings) |  A settings class to configure a UnaryCallable for calls to an API method that supports page streaming.  
[com.google.api.gax.rpc.ServerStreamingCallSettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallSettings) |  A settings class to configure a ServerStreamingCallable. This class includes settings that are applicable to all server streaming calls, which currently just includes retries and watchdog timers.  
[com.google.api.gax.rpc.StreamingCallSettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamingCallSettings) |  A settings class to configure a streaming callable object for calls to a streaming API method.  
[com.google.api.gax.rpc.StubSettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings) |  A base settings class to configure a client stub class. This base class includes settings that are applicable to all services, which includes things like settings for creating an executor, credentials, transport-specific settings, and identifiers  
[com.google.api.gax.rpc.UnaryCallSettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings) |  A base settings class to configure a UnaryCallable. An instance of UnaryCallSettings is not sufficient on its own to construct a UnaryCallable; a concrete derived type is necessary. This base class includes settings that are applicable to all calls, which currently is just  
  
## Classes

Class |  Description  
---|---  
[com.google.api.gax.rpc.ApiCallContext.Key](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiCallContext.Key) |  Key for api call context options key-value pair.  
[com.google.api.gax.rpc.ApiClientHeaderProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider) |  Implementation of HeaderProvider that provides headers describing the API client library making API calls.  
[com.google.api.gax.rpc.ApiClientHeaderProvider.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder) |   
[com.google.api.gax.rpc.ApiExceptionFactory](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiExceptionFactory) |  A factory class that returns the corresponding type of exception class from the given status code.  
[com.google.api.gax.rpc.ApiExceptions](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiExceptions) |  A utility class for working with ApiException.  
[com.google.api.gax.rpc.Batch](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Batch) |  A Batch contains a collection of requests that are to be batched into a single API call. A Batch contains a single UnaryCallable object, which will be used to make the API call, and a list of BatchedRequestIssuer objects, which represent the individual requests  
[com.google.api.gax.rpc.BatchedFuture](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchedFuture) |  An ApiFuture to be used with batching. This is public only for technical reasons, for advanced usage.  
[com.google.api.gax.rpc.BatchedRequestIssuer](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchedRequestIssuer) |  BatchedRequestIssuer receives a response or an exception and waits to set the given batchedFuture until sendResult() is called. This class is designed to be used by generated code.  
[com.google.api.gax.rpc.BatcherFactory](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatcherFactory) |  A Factory class which, for each unique partitionKey, creates a trio including a ThresholdBatcher, BatchExecutor, and ThresholdBatchingForwarder. The ThresholdBatchingForwarder pulls items from the ThresholdBatcher and forwards them to the BatchExecutor for processing.   
[com.google.api.gax.rpc.BatchingCallSettings.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchingCallSettings.Builder) |   
[com.google.api.gax.rpc.BatchingCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchingCallable) |  A UnaryCallable which will batch requests based on the given BatchingDescriptor and BatcherFactory. The BatcherFactory provides a distinct Batcher for each partition as specified by the BatchingDescriptor. An example of a batching partition would be a pubsub topic.   
[com.google.api.gax.rpc.BidiStream](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStream) |  A wrapper around a bidirectional stream. This class asynchronously pulls responses from upstream via StreamController#request(int) and exposes them via its Iterator. The implementation is back pressure aware and uses a constant buffer of 1 item.  
[com.google.api.gax.rpc.BidiStreamingCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamingCallable) |  A BidiStreamingCallable is an immutable object which is capable of making RPC calls to bidirectional streaming API methods. Not all transports support streaming. It is considered advanced usage for a user to create a BidiStreamingCallable themselves. This  
[com.google.api.gax.rpc.Callables](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Callables) |  Class with utility methods to create callable objects using provided settings. The callable objects wrap a given direct callable with features like retry and exception translation.  
[com.google.api.gax.rpc.ClientContext](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext) |  Encapsulates client state, including executor, credentials, and transport channel. Unlike ClientSettings which allows users to configure the client, ` ClientContext` is intended to be used in generated code. Most users will not need to use it.  
[com.google.api.gax.rpc.ClientContext.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder) |   
[com.google.api.gax.rpc.ClientSettings.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.Builder) |   
[com.google.api.gax.rpc.ClientStreamingCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientStreamingCallable) |  A ClientStreamingCallable is an immutable object which is capable of making RPC calls to client streaming API methods. Not all transports support streaming. It is considered advanced usage for a user to create a ClientStreamingCallable themselves.  
[com.google.api.gax.rpc.EndpointContext](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.EndpointContext) |  EndpointContext is an internal class used by the client library to resolve the endpoint. It is created once the library is initialized should not be updated manually. Contains the fields required to resolve the endpoint and Universe Domain  
[com.google.api.gax.rpc.EndpointContext.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.EndpointContext.Builder) |   
[com.google.api.gax.rpc.ErrorDetails](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails) |  This class contains a list of standard error messages that returns from server.  
[com.google.api.gax.rpc.ErrorDetails.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails.Builder) |   
[com.google.api.gax.rpc.FixedHeaderProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FixedHeaderProvider) |  An instance of HeaderProvider that always provides the same headers.  
[com.google.api.gax.rpc.FixedTransportChannelProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FixedTransportChannelProvider) |  An instance of TransportChannelProvider that always provides the same TransportChannel.  
[com.google.api.gax.rpc.FixedWatchdogProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FixedWatchdogProvider) |  A watchdog provider which always returns the same watchdog instance provided to the provider during construction. This is the internal class and is public only for technical reasons. It may change any time  
[com.google.api.gax.rpc.InstantiatingWatchdogProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InstantiatingWatchdogProvider) |  A watchdog provider which instantiates a new provider on every request. This is the internal class and is public only for technical reasons. It may change any time without notice, please do not depend on it explicitly.  
[com.google.api.gax.rpc.LibraryMetadata](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata) |  A context object that contains information about the GAPIC library. For internal use only.  
[com.google.api.gax.rpc.LibraryMetadata.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.Builder) |   
[com.google.api.gax.rpc.NoHeaderProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NoHeaderProvider) |  Implementation of HeaderProvider that provides empty headers.  
[com.google.api.gax.rpc.OperationCallSettings.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.Builder) |   
[com.google.api.gax.rpc.OperationCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable) |  An OperationCallable is an immutable object which is capable of initiating RPC calls to long-running API methods and returning an OperationFuture to manage the polling of the Operation and getting the response.   
[com.google.api.gax.rpc.PageContext](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PageContext) |  The context for a page call.  
[com.google.api.gax.rpc.PagedCallSettings.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.Builder) |   
[com.google.api.gax.rpc.PagedCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallable) |  A UnaryCallable which provides page streaming functionality for unary calls. Public for technical reasons - for advanced usage.  
[com.google.api.gax.rpc.RequestParamsBuilder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestParamsBuilder) |  This builder class builds a request params map that will be used by autogenerated implementation of RequestParamsExtractor.  
[com.google.api.gax.rpc.RequestUrlParamsEncoder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestUrlParamsEncoder) |  The request params encoder, which encodes URL-encoded parameters in one URL parameters string.  
[com.google.api.gax.rpc.ResumableUploadCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadCallable) |  A ResumableUploadCallable is an API-transport-independent wrapper for the Resumable Upload protocol. Operates directly on the request object and input stream payload.  
[com.google.api.gax.rpc.ResumableUploadCallableImpl](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadCallableImpl) |  Concrete implementation of ResumableUploadCallable that delegates the end-to-end management of a resumable upload session to ResumableUploadFutureImpl.  
[com.google.api.gax.rpc.ResumableUploadOptions](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadOptions) |  Options to configure a resumable upload invocation on a ResumableUploadCallable. Encapsulates protocol options such as payload chunk size and global upload timeout.  
[com.google.api.gax.rpc.ResumableUploadOptions.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadOptions.Builder) |  Builder for ResumableUploadOptions.  
[com.google.api.gax.rpc.ResumableUploadProgress](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadProgress) |  Progress snapshot of an ongoing or completed resumable upload session.  
[com.google.api.gax.rpc.ServerStream](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStream) |  A blocking Iterable-style wrapper around server stream responses. This class asynchronously pulls responses from upstream via StreamController#request(int) and exposes them via its Iterator. The implementation is back pressure aware and uses a constant buffer of 1 item.  
[com.google.api.gax.rpc.ServerStreamingCallSettings.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallSettings.Builder) |   
[com.google.api.gax.rpc.ServerStreamingCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallable) |  A ServerStreamingCallable is an immutable object which is capable of making RPC calls to server streaming API methods. Not all transports support streaming. It is considered advanced usage for a user to create a ServerStreamingCallable themselves.  
[com.google.api.gax.rpc.StateCheckingResponseObserver](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StateCheckingResponseObserver) |  Base implementation of ResponseObserver that performs state sanity checks.  
[com.google.api.gax.rpc.StreamingCallSettings.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamingCallSettings.Builder) |   
[com.google.api.gax.rpc.StubSettings.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.Builder) |   
[com.google.api.gax.rpc.TranslatingUnaryCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TranslatingUnaryCallable) |  A UnaryCallable that translates request types and response types using the given transformers.  
[com.google.api.gax.rpc.UnaryCallSettings.Builder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.Builder) |  A base builder class for UnaryCallSettings. This class should not be used to create an instance of the base class UnaryCallSettings. See the class documentation of UnaryCallSettings for a description of the different values that can be set, and for a description of when this builder may be used. Builders for concrete derived classes can be used to create instances of those classes.  
[com.google.api.gax.rpc.UnaryCallable](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) |  A UnaryCallable is an immutable object which is capable of making RPC calls to non-streaming API methods. In typical usage, the request to send to the remote service will not be bound to the  
[com.google.api.gax.rpc.Watchdog](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.Watchdog) |  Prevents the streams from hanging indefinitely. This middleware garbage collects idle streams in case the user forgot to close a ServerStream or if a connection is reset and GRPC does not get notified.   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.api.gax.rpc.ApiCallContext](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiCallContext) |  Context for an API call. An API call can be composed of many RPCs (in case of retries). This class contains settings for both: API calls and RPCs.  
[com.google.api.gax.rpc.ApiStreamObserver](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiStreamObserver) |  Receives notifications from an observable stream of messages. It is used for sending messages in bidi (bidirectional) or client-streaming calls, or for receiving messages in bidi or server-streaming calls.  
[com.google.api.gax.rpc.BatchingDescriptor](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BatchingDescriptor) |  Interface which represents an object that transforms request/response data for the purposes of batching. Implementations of BatchingDescriptor must guarantee that all methods are stateless and thread  
[com.google.api.gax.rpc.BidiStreamObserver](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.BidiStreamObserver) |   
[com.google.api.gax.rpc.ClientStream](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientStream) |  A wrapper used to send requests to the server. After sending requests, users must either call #closeSend() or #closeSendWithError(Throwable) on the stream. The error, if any, will be propagated to the server.  
[com.google.api.gax.rpc.ClientStreamReadyObserver](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientStreamReadyObserver) |  A callback used to report that the ClientStream is ready to send more messages.  
[com.google.api.gax.rpc.HeaderProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.HeaderProvider) |  Provider of headers to put on http requests.  
[com.google.api.gax.rpc.InputStreamSupplier](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InputStreamSupplier) |  A functional interface that supplies an InputStream and may throw IOException.  
[com.google.api.gax.rpc.PagedListDescriptor](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedListDescriptor) |  An interface which provides the functionality to extract data from requests and inject data into requests for the purposes of page streaming. This class is designed to be used by generated code.  
[com.google.api.gax.rpc.PagedListResponseFactory](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedListResponseFactory) |  Interface for constructing futures which return PagedListResponse objects. This class is designed to be used by generated code.  
[com.google.api.gax.rpc.RequestMutator](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestMutator) |  A request mutator takes a `request` message, applies some Function to it, and then returns the modified `request` message. This is currently only used for autopopulation of the request ID.   
[com.google.api.gax.rpc.RequestParamsEncoder](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestParamsEncoder) |  A request params encoder takes a `request` object and encodes some (or all) of its parameters in a string form following specific parameter extraction and string encoding rules, defined by concrete implementations of this interface.  
[com.google.api.gax.rpc.RequestParamsExtractor](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.RequestParamsExtractor) |  A request params extractor takes a `request` message, extracts specific field values from it, converts them in strings and returns them as key-value pairs, where a key is a request field name and a value is a string representation of a field value. Nested fields should also be extractable, in such case the "dot notation" can be used to represent a nested field name, for  
[com.google.api.gax.rpc.ResourceNameExtractor](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResourceNameExtractor) |  A resource name extractor takes a request message and extracts the resource name from it. This value is used primarily for tracing. It is added to spans as an attribute, labeled as gcp.resource.destination.id (See ObservabilityAttributes#DESTINATION_RESOURCE_ID_ATTRIBUTE).   
[com.google.api.gax.rpc.ResponseObserver](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResponseObserver) |  Receives notifications from server-streaming calls. The application is responsible for implementing the `ResponseObserver` and passing it to GAX, which then calls the observer with the messages for the application to receive them. The  
[com.google.api.gax.rpc.ResumableUploadFuture](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadFuture) |  A specialized ApiFuture for tracking and controlling an in-flight resumable upload. The payload [java.io.InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html) supplied when initiating the upload is managed by this future and will be closed automatically upon completion, failure, or cancellation.  
[com.google.api.gax.rpc.ResumableUploadProgressListener](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResumableUploadProgressListener) |  A callback listener for observing progress and state transitions of a resumable upload.  
[com.google.api.gax.rpc.StatusCode](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StatusCode) |  Transport-specific status code. The status codes are modeled after the status codes in grpc. For more information about grpc status codes, see  
[com.google.api.gax.rpc.StreamController](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamController) |  Allows the implementer of ResponseObserver to control the flow of responses. An instance of this class will be passed to ResponseObserver#onStart(StreamController), at which point the receiver can disable automatic flow control. The receiver can also save a reference to the instance and terminate the stream  
[com.google.api.gax.rpc.TransportChannel](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannel) |  Class whose instances can issue RPCs on a particular transport.  
[com.google.api.gax.rpc.TransportChannelProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider) |  Provides an interface to either build a TransportChannel or provide a fixed TransportChannel that will be used to make calls to a service. Implementations of TransportChannelProvider may choose to create a new TransportChannel for each call to #getTransportChannel, or may return a fixed TransportChannel instance.  
[com.google.api.gax.rpc.WatchdogProvider](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.WatchdogProvider) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.api.gax.rpc.StatusCode.Code](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StatusCode.Code) |   
  
## Exceptions

Exception |  Description  
---|---  
[com.google.api.gax.rpc.AbortedException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AbortedException) |  Exception thrown when the operation was aborted, typically due to a concurrency issue like sequencer check failures, transaction aborts, etc.  
[com.google.api.gax.rpc.AlreadyExistsException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException) |  Exception thrown when some entity that we attempted to create (e.g., file or directory) already exists.  
[com.google.api.gax.rpc.ApiException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException) |  Represents an exception thrown during an RPC call.  
[com.google.api.gax.rpc.AsyncTaskException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AsyncTaskException) |  This exception is used to preserve the caller's stacktrace when invoking an async task in a sync context. It will be added as a suppressed exception when propagating the async exception. This allows callers to catch ApiException thrown in an async operation, while still maintaining the call site.  
[com.google.api.gax.rpc.CancelledException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.CancelledException) |  The exception thrown when the operation was cancelled (typically by the caller).  
[com.google.api.gax.rpc.DataLossException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.DataLossException) |  Exception thrown due to unrecoverable data loss or corruption.  
[com.google.api.gax.rpc.DeadlineExceededException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.DeadlineExceededException) |  Exception thrown when deadline expired before operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.  
[com.google.api.gax.rpc.FailedPreconditionException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FailedPreconditionException) |  Exception thrown when the operation was rejected because the system is not in a state required for the operation's execution. For example, directory to be deleted may be non-empty, an rmdir operation is applied to a non-directory, etc.  
[com.google.api.gax.rpc.InternalException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InternalException) |  Exception thrown due to internal errors. Means some invariants expected by underlying system has been broken. If you see one of these errors, something is very broken.  
[com.google.api.gax.rpc.InvalidArgumentException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.InvalidArgumentException) |  Exception thrown when client specified an invalid argument. Note that this differs from FailedPreconditionException. This exception indicates arguments that are problematic regardless of the state of the system (e.g., a malformed file name).  
[com.google.api.gax.rpc.NotFoundException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException) |  Exception thrown when some requested entity (e.g., file or directory) was not found.  
[com.google.api.gax.rpc.OutOfRangeException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OutOfRangeException) |  Exception thrown when the operation was attempted past the valid range. E.g., seeking or reading past end of file.  
[com.google.api.gax.rpc.PermissionDeniedException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PermissionDeniedException) |  Exception thrown when the caller does not have permission to execute the specified operation.  
[com.google.api.gax.rpc.ProtocolBufferParsingException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ProtocolBufferParsingException) |  Exception thrown when parsing protocol buffer message failed  
[com.google.api.gax.rpc.ResourceExhaustedException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ResourceExhaustedException) |  Exception thrown when some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.  
[com.google.api.gax.rpc.UnauthenticatedException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnauthenticatedException) |  Exception thrown when the request does not have valid authentication credentials for the operation.  
[com.google.api.gax.rpc.UnavailableException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnavailableException) |  Exception thrown when the service is currently unavailable. This is a most likely a transient condition and may be corrected by retrying with a backoff.  
[com.google.api.gax.rpc.UnimplementedException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnimplementedException) |  Exception thrown when the operation is not implemented or not supported/enabled in this service.  
[com.google.api.gax.rpc.UnknownException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnknownException) |  Exception thrown due to an unknown error. An example of where this error may be returned is if a Status value received from another address space belongs to an error-space that is not known in this address space. Also errors raised by APIs that do not return enough error information may be converted to this error.  
[com.google.api.gax.rpc.WatchdogTimeoutException](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.WatchdogTimeoutException) |  The marker exception thrown when a timeout is exceeded. This error can be thrown under 2 circumstances:   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
