---
url: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher/
title: Class BlockingPublisher (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:41.289374+00:00
---

# Class BlockingPublisher (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class BlockingPublisher (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Publish messages to the Cloud Pub/Sub service. 

This class is used to publish messages to any given topic. It is intended for low-volume publishers. Applications sending less than one message per second may find this class easier to use than [`Publisher`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1Publisher), which can handle thousands of messages per second.

###### See Also

<https://cloud.google.com/pubsub> for an overview of the Cloud Pub/Sub service.

###### Example
    
    
      namespace pubsub = ::google::cloud::pubsub;
      [](std::string project_id, std::string topic_id) {
        auto topic = pubsub::Topic(std::move(project_id), std::move(topic_id));
        auto publisher =
            pubsub::BlockingPublisher(pubsub::MakeBlockingPublisherConnection());
        auto id = publisher.Publish(
            topic, pubsub::MessageBuilder().SetData("Hello World!").Build());
        if (!id) throw std::move(id).status();
        std::cout << "Hello World successfully published on topic "
                  << topic.FullName() << " with id " << *id << "\n";
      }
    

###### Performance

[`BlockingPublisher`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher) objects are relatively cheap to create, copy, and move. However, each [`BlockingPublisher`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisher) object must be created with a `std::shared_ptr<`[`BlockingPublisherConnection`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisherConnection)`>`, which itself is relatively expensive to create. Therefore, connection instances should be shared when possible. See the [`MakeBlockingPublisherConnection()`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/namespacegoogle_1_1cloud_1_1pubsub) method and the [`BlockingPublisherConnection`](https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/classgoogle_1_1cloud_1_1pubsub_1_1BlockingPublisherConnection) interface for more details.

###### Thread Safety

Instances of this class created via copy-construction or copy-assignment share the underlying pool of connections. Access to these copies via multiple threads is guaranteed to work. Two threads operating on the same instance of this class is not guaranteed to work.

###### Background Threads

This class uses the background threads configured via the [`Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) from `GrpcOptionList`. Applications can create their own pool of background threads by (a) creating their own [`google::cloud::CompletionQueue`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1CompletionQueue.html), (b) passing this completion queue as a [`GrpcCompletionQueueOption`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1GrpcCompletionQueueOption.html), and (c) attaching any number of threads to the completion queue.

###### Error Handling

This class uses [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` to report errors. When an operation fails to perform its work the returned [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` contains the error details. If the `ok()` member function in the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html)`<T>` returns `true` then it contains the expected result. Please consult the [`google::cloud::StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) documentation for more details. 

## Constructors 

### BlockingPublisher(std::shared_ptr< BlockingPublisherConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< BlockingPublisherConnection >`   
  
`opts` |  `Options`   
  
  
### BlockingPublisher(BlockingPublisher const &)

**Parameter**  
---  
**Name** | **Description**  
`` |  `BlockingPublisher const &`   
  
  
### BlockingPublisher(BlockingPublisher &&)

**Parameter**  
---  
**Name** | **Description**  
`` |  `BlockingPublisher &&`   
  
  
## Operators 

### operator=(BlockingPublisher const &)

**Parameter**  
---  
**Name** | **Description**  
`` |  `BlockingPublisher const &`   
  
**Returns**  
---  
**Type** | **Description**  
`BlockingPublisher &` |   
  
### operator=(BlockingPublisher &&)

**Parameter**  
---  
**Name** | **Description**  
`` |  `BlockingPublisher &&`   
  
**Returns**  
---  
**Type** | **Description**  
`BlockingPublisher &` |   
  
## Functions 

### Publish(Topic, Message, Options)

Publishes the `message` on the topic `topic`. 

###### Idempotency

This is a non-idempotent operation, but the client library will automatically retry RPCs that fail with transient errors. As Cloud Pub/Sub has "at least once" delivery semantics applications are expected to handle duplicate messages without problems. The application can disable retries by changing the retry policy, please see the example below.

###### Example
    
    
      namespace pubsub = ::google::cloud::pubsub;
      [](std::string project_id, std::string topic_id) {
        auto topic = pubsub::Topic(std::move(project_id), std::move(topic_id));
        auto publisher =
            pubsub::BlockingPublisher(pubsub::MakeBlockingPublisherConnection());
        auto id = publisher.Publish(
            topic, pubsub::MessageBuilder().SetData("Hello World!").Build());
        if (!id) throw std::move(id).status();
        std::cout << "Hello World successfully published on topic "
                  << topic.FullName() << " with id " << *id << "\n";
      }
    

###### Example
    
    
      namespace pubsub = ::google::cloud::pubsub;
      [](std::string project_id, std::string topic_id) {
        auto topic = pubsub::Topic(std::move(project_id), std::move(topic_id));
        auto publisher =
            pubsub::BlockingPublisher(pubsub::MakeBlockingPublisherConnection());
        auto id = publisher.Publish(
            topic, pubsub::MessageBuilder().SetData("Hello World!").Build(),
            google::cloud::Options{}.set<pubsub::RetryPolicyOption>(
                pubsub::LimitedErrorCountRetryPolicy(/*maximum_failures=*/0)
                    .clone()));
        if (!id) return;  // Without retries, errors are likely.
        std::cout << "Hello World successfully published on topic "
                  << topic.FullName() << " with id " << *id << "\n";
      }
    

**Parameters**  
---  
**Name** | **Description**  
`topic` |  `Topic`   
  
`message` |  `Message`   
  
`opts` |  `Options`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< std::string >` | On success, the server-assigned ID of the message. IDs are guaranteed to be unique within the topic.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
