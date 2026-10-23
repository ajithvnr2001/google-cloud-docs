---
url: https://docs.cloud.google.com/java/docs/long-running-operations/
title: Manage long-running operations \u00a0|\u00a0 Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:54.695011+00:00
---

# Manage long-running operations  |  Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Manage long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud APIs use long-running operations (LROs) for calls expected to take significant time to complete (for example, provisioning a Compute Engine instance or initializing a Dataflow pipeline). These APIs don't keep an active long-lived connection or block while the task runs. For LRO APIs, the Cloud Client Libraries for Java returns a `future` for you to check later.

## Determining if an API is an LRO

There are two main ways to determine if an API is an LRO:

  * LRO APIs either have the suffix `Async` (for example, `createClusterAsync`) or `OperationCallable` (for example, `createClusterOperationCallable`).
  * LRO APIs return either an `OperationFuture` or `OperationCallable`.



The following snippet shows the two variations, using `Java-Dataproc` as an example:
    
    
    // Async suffix (#1) returns OperationFuture (#2)
    public final OperationFuture<Cluster, ClusterOperationMetadata> createClusterAsync(CreateClusterRequest request)
    
    // OperationCallable suffix (#1) returns OperationCallable (#2)
    public final OperationCallable<CreateClusterRequest, Cluster, ClusterOperationMetadata> createClusterOperationCallable()
    

These are two variations for the same API and not two different APIs (both calls create a Managed Service for Apache Spark cluster). The `Async` variant is recommended.

## High-level flow of an LRO

LRO APIs are essentially an initial request call followed by a series of small polling calls. The initial call sends the request and creates an "operation" on the server. All subsequent polling calls to the server track the status of the operation. If the operation is finished, the response is returned. Otherwise, an incomplete status is returned and the client library determines whether to poll again.

By default, the client handles the polling logic, and you don't need to configure the polling mechanism unless you have specific requirements.

From your perspective, the call runs in the background until a response is received. The polling calls and timeout configurations have default values that are pre-configured by the service team based on the expected time for their APIs. These configurations control many factors, such as how often to poll and how long to wait before giving up.

The Cloud Client Libraries for Java provide an interface for interacting with the LRO using `OperationFuture`.

The following snippet shows how to call an operation and to wait for a response, using `Java-Dataproc` as an example:
    
    
    try (ClusterControllerClient clusterControllerClient = ClusterControllerClient.create()) {
      CreateClusterRequest request =
          CreateClusterRequest.newBuilder().build();
      OperationFuture<Cluster, ClusterOperationMetadata> future =
          clusterControllerClient.createClusterAsync(request);
      // Blocks until there is a response
      Cluster response = future.get();
    } catch (CancellationException e) {
      // Exceeded the timeout without the Operation completing.
      // Library is no longer polling for the Operation's status.
    }
    

## Default LRO values

You can find the default values within each client's `StubSettings` class. The `initDefaults()` method initializes the LRO settings inside the nested `Builder` class.

For example, in `Java-Aiplatform v3.24.0`, the `deployModel` LRO call has the following default parameters:
    
    
    OperationTimedPollAlgorithm.create(
      RetrySettings.newBuilder()
        .setInitialRetryDelayDuration(Duration.ofMillis(5000L))
        .setRetryDelayMultiplier(1.5)
        .setMaxRetryDelayDuration(Duration.ofMillis(45000L))
        .setTotalTimeoutDuration(Duration.ofMillis(300000L))
        .setInitialRpcTimeoutDuration(Duration.ZERO) // not used
        .setRpcTimeoutMultiplier(1.0) // not used
        .setMaxRpcTimeoutDuration(Duration.ZERO) // not used
        .build()));
    

**Note:** LROs don't use RPC Timeout values and have default values (Duration.ZERO for timeouts or 1.0 for the multiplier).

Both retries and LROs share the same `RetrySettings` class. The following table shows the mapping between the fields inside `RetrySettings` and the LRO functionality:

RetrySettings | Description  
---|---  
InitialRetryDelay | Initial delay before the first poll.  
MaxRetryDelay | Maximum delay between each poll.  
RetryDelayMultiplier | Multiplier for the poll retry delay between polls.  
TotalTimeoutDuration | Maximum time allowed for the long-running operation.  
  
## When to configure LRO values

The main use case to manually configure the LRO values is to modify polling frequencies due to LRO timeouts. While the default values are configured as an estimate by the service team, certain factors might result in occasional timeouts.

To reduce the number of timeouts, increase the total timeout value. Increasing the other values can also help, and you should test them to ensure the expected behavior.

## How to configure LRO values

To configure the LRO values, create an `OperationTimedPollAlgorithm` object and update the polling algorithm for a specific LRO. The following snippet uses `Java-Dataproc` as an example:
    
    
    ClusterControllerSettings.Builder settingsBuilder = ClusterControllerSettings.newBuilder();
    // Create a new OperationTimedPollAlgorithm object
    TimedRetryAlgorithm timedRetryAlgorithm = OperationTimedPollAlgorithm.create(
      RetrySettings.newBuilder()
        .setInitialRetryDelayDuration(Duration.ofMillis(500L))
        .setRetryDelayMultiplier(1.5)
        .setMaxRetryDelayDuration(Duration.ofMillis(5000L))
        .setTotalTimeoutDuration(Duration.ofHours(24L))
        .build());
    // Set the new polling settings for the specific LRO API 
    settingsBuilder.createClusterOperationSettings().setPollingAlgorithm(timedRetryAlgorithm);
    ClusterControllerClient clusterControllerClient = ClusterControllerClient.create(settingsBuilder.build());
    

This configuration only modifies the LRO values for the `createClusterOperation` RPC. The other RPCs in the Client still use the pre-configured LRO values for each RPC unless also modified.

## LRO timeouts

The library continues to poll as long as the total timeout has not been exceeded. If the total timeout has exceeded, the library throws a `java.util.concurrent.CancellationException` with the message "Task was cancelled."

A `CancellationException` doesn't mean that the backend Google Cloud task was cancelled. This exception is thrown from the client library when a call has exceeded the total timeout and has not received a response. Even if the task is completed immediately after the timeout, the response won't be seen by the client library.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
