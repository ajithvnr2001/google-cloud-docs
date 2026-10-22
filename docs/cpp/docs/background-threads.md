---
url: https://docs.cloud.google.com/cpp/docs/background-threads/
title: Background threads in the C++ Client Libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:27.157196+00:00
---

# Background threads in the C++ Client Libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/background-threads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Guides ](https://docs.cloud.google.com/cpp/docs/setup)



Send feedback 

#  Background threads in the C++ Client Libraries Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the threading model used by the C++ client libraries, and shows you how to override the default thread pool(s) in your application.

## Objectives

  * Describe the default threading model for the C++ client libraries.
  * Describe how to override these defaults for applications that need to.



## Why do the client libraries use background threads?

Most functions in the client libraries use the thread calling the function to complete all the work, including any RPCs to the service and/or refreshing access tokens for authentication.

Asynchronous functions, by their nature, cannot use the current thread to complete their work. Some separate thread must wait for the work to complete and handle the response.

It is also wasteful to block the calling thread on long-running operations, where it may take minutes or longer for the service to complete the work. For such operations the client library uses background threads to periodically poll the state of the long-running operation.

## What functions and libraries require background threads?

Functions that return a [`future<T>`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future) for some type `T` use background threads to wait until the work completes.

Not all client libraries have asynchronous functions or long-running operations. Libraries that do not need them, do not create any background threads.

You may notice additional threads in your application, but these may be created by dependencies of the C++ client library, such as gRPC. These threads are usually less interesting, because no application code ever runs in these threads and they only serve ancillary functions.

## How do these background threads affect my application?

As usual, these threads compete for CPU and memory resources with the rest of your application. If needed, you can create your own thread pool to gain fine control of any resources these threads use. See below for details.

## Does any of my code run in any of these threads?

Yes. When you attach a callback to a [`future<T>`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1future) the callback is almost always executed by one of the background threads. The only case where this would not happen is if the `future<T>` is already satisfied by the time you attach the callback. In that case the callback runs immediately, in the context of the thread attaching the callback.

For example, consider an application using the Pub/Sub client library. The `Publish()` call returns a future and the application can attach a callback after performing some work:
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace g = google::cloud;
    
    void Callback(g::future<g::StatusOr<std::string>>);
    
    void F(pubsub::Publisher publisher) {
      auto my_future = publisher.Publish(
          pubsub::MessageBuilder("Hello World!").Build());
      // do some work.
      my_future.then(Callback);
    }
    

If `my_future` is satisfied before the `.then()` function is called, then the callback is invoked immediately. If you want to guarantee the code runs in a separate thread, you need to use your own thread pool and provide a callable in `.then()` that forwards the execution to your thread pool.

## Default Thread Pools

For those libraries that require background threads the `Make*Connection()` creates a default thread pool. Unless you override the thread pool each `*Connection` object has a separate thread pool.

The default thread pool in most libraries contains a single thread. More threads are rarely needed as the background thread is used to poll the state of long-running operations. These calls are reasonably short lived and consume very little CPU, so a single background thread can handle hundreds of pending long-running operations, and very few applications have even that many.

Other asynchronous operations may require more resources. Use [`GrpcBackgroundThreadPoolSizeOption`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1GrpcBackgroundThreadPoolSizeOption) to change the default background thread pool size if needed.

The Pub/Sub library expects to have significantly more work, as it is common for Pub/Sub applications to receive or send thousands of messages per second. Consequently, this library defaults to one thread per core on 64-bit architectures. On 32-bit architectures (or when compiled in 32-bit mode, even if running on a 64-bit architecture) this default changes to only 4 threads.

## Providing your own Thread Pool

You can provide your own thread pool for background threads. Create a [`CompletionQueue`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1CompletionQueue) object, attach threads to it, and configure the [`GrpcCompletionQueueOption`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1GrpcCompletionQueueOption) when initializing your client. For example:
    
    
    namespace admin = ::google::cloud::spanner_admin;
    namespace g = ::google::cloud;
    
    void F() {
      // You will need to create threads
      auto cq = g::CompletionQueue();
      std::vector<std::jthread> threads;
      for (int i = 0; i != 10; ++i) {
        threads.emplace_back([](auto cq) { cq.Run(); }, cq);
      }
      auto client = admin::InstanceAdminClient(admin::MakeInstanceAdminConnection(
          g::Options{}.set<g::GrpcCompletionQueueOption>(cq)));
      // Use `client` as usual
    }
    

You can share the same [`CompletionQueue`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1CompletionQueue) object across multiple clients, even for different services:
    
    
    namespace admin = ::google::cloud::spanner_admin;
    namespace pubsub = ::google::cloud::pubsub;
    namespace g = ::google::cloud;
    
    void F(pubsub::Topic const& topic1, pubsub::Topic const& topic2) {
      // You will need to create threads
      auto cq = g::CompletionQueue();
      std::vector<std::jthread> threads;
      for (int i = 0; i != 10; ++i) {
        threads.emplace_back([](auto cq) { cq.Run(); }, cq);
      }
      auto client = admin::InstanceAdminClient(admin::MakeInstanceAdminConnection(
          g::Options{}.set<g::GrpcCompletionQueue>(cq)));
      auto p1 = pubsub::Publisher(pubsub::MakePublisherConnection(
          topic1, g::Options{}.set<g::GrpcCompletionQueueOption>(cq)));
      auto p2 = pubsub::Publisher(pubsub::MakePublisherConnection(
          topic2, g::Options{}.set<g::GrpcCompletionQueueOption>(cq)));
      // Use `client`, `p1`, and `p2` as usual
    }
    

## Next Steps

  * See [Client Library Configuration](https://docs.cloud.google.com/cpp/docs/reference/common/latest/group__options) to learn more about common library configuration options.
  * See [Cloud Pub/Sub C++ Client Library](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest) for the full Pub/Sub client library reference docs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
