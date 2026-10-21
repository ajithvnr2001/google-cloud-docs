---
url: https://docs.cloud.google.com/java/docs/client-lifecycle/
title: Manage client lifecycles on Java Cloud Client Libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:14.619977+00:00
---

# Manage client lifecycles on Java Cloud Client Libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/client-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Manage client lifecycles on Java Cloud Client Libraries Stay organized with collections  Save and categorize content based on your preferences. 

Client library instances are reusable and designed to be long-lived. Typically, applications maintain a single instance of a client library, rather than creating a library for each request.

**Note:** See Cases for multiple clients for examples of when you might consider creating multiple instances of a client library.

Using Java-KMS as an example, the following snippet shows multiple requests being invoked with the same client instance:
    
    
    // Create one instance of KMS's KeyManagementServiceClient
    KeyManagementServiceClient keyManagementServiceClient =
     KeyManagementServiceClient.create();
    keyManagementServiceClient.listKeyRings();
    keyManagementServiceClient.asymmetricSign();
    keyManagementServiceClient.createCryptoKey();
    // ... other code ...
    
    // Create one instance of KMS's AutokeyClient
    AutokeyClient autokeyClient = AutokeyClient.create();
    autokeyClient.listKeyHandles();
    autokeyClient.getKeyHandle();
    

## Close a client

How you manage a client's lifecycle can depend on the use case and the specific client library. For example, if you're using a framework, follow the framework's guidelines for client management. While some scenarios might use `try-with-resources` for shorter-lived clients, reusing a long-lived client instance is generally recommended for efficiency

Calling `close()` on a client attempts an orderly shutdown and ensures that existing tasks continue until completion. The client won't accept new tasks. If you don't close the client, its resources continue to persist, and your application incurs memory leaks.

The following example uses Java-KMS and shows the client being closed:
    
    
    KeyManagementServiceClient keyManagementServiceClient =
      KeyManagementServiceClient.create(keyManagementServiceSettings);
    // ... other code ...
    keyManagementServiceClient.close();
    
    // For gRPC clients, it's recommended to call awaitTermination to ensure a
    // graceful shutdown and avoid the following error message in the logs:
    // ERROR i.g.i.ManagedChannelOrphanWrapper - *~*~*~ Channel ManagedChannelImpl
    // was not shutdown properly!!! ~*~*~*
    // java.lang.RuntimeException: ManagedChannel allocation site
    // at io.grpc.internal.ManagedChannelOrphanWrapper$ManagedChannelReference.<init>
    keyManagementServiceClient.awaitTermination(DURATION, TimeUnit.SECONDS);
    
    // Optionally include a shutdownNow() call after awaitTermination() to force
    // close any lingering resources
    keyManagementServiceClient.shutdownNow();
    

In addition to `close()`, some Java client libraries expose a few related methods for managing the client lifecycle:

  * `shutdown()`: Equivalent to `close()`.
  * `shutdownNow()`: Invokes the shutdown process immediately. Stops all executing tasks and doesn't wait for the task to complete.
  * `isShutdown()`: Returns `true` if the background tasks have been shut down.
  * `isTerminated()`: Returns `true` if all tasks have completed following shutdown.
  * `awaitTermination()`: Blocks for a duration until all work has completed following shutdown.



## Cases for multiple clients

There can be specific customer use cases that warrant multiple co-existing instances of a client library. The main use case for having multiple clients is when there are requests that must be sent to multiple different endpoints. A client instance connects to a single endpoint. To connect to multiple endpoints, create a client for each.

**Note:** General performance issues can suggest an underlying issue with how the client is configured. Using multiple clients for performance gain can result in unnecessary complexity.

## Potential multi-client risks

There are a few common risks with applications using multiple client library instances:

  * **Increased potential for memory leaks.** Resources linger if not all client instances are properly closed.
  * **Performance implications.** Initializing multiple gRPC channels incurs a performance cost, which can add up in performance-sensitive applications.
  * **Issues with in-flight requests.** Closing a client while requests are still in-flight can lead to a `RejectedExecutionException`. Ensure requests complete before closing the client.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
