---
url: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxConcurrencyOption/
title: Struct MaxConcurrencyOption (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:31.554191+00:00
---

# Struct MaxConcurrencyOption (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/pubsub/latest/structgoogle_1_1cloud_1_1pubsub_1_1MaxConcurrencyOption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Struct MaxConcurrencyOption (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The maximum callback concurrency. 

The Cloud Pub/Sub C++ client library will schedule parallel callbacks as long as the number of outstanding callbacks is less than this maximum.

Note that this controls the number of callbacks _scheduled_ , not the number of callbacks actually executing at a time. The application needs to create (or configure) the background threads pool with enough parallelism to execute more than one callback at a time.

Some applications may want to share a thread pool across many subscriptions. The additional level of control (scheduled vs. running callbacks) allows applications, for example, to ensure that at most `K` threads in the pool are used by any given subscription.

###### Example
    
    
      namespace pubsub = ::google::cloud::pubsub;
      using ::google::cloud::future;
      using ::google::cloud::GrpcBackgroundThreadPoolSizeOption;
      using ::google::cloud::Options;
      using ::google::cloud::StatusOr;
      auto sample = [](std::string project_id, std::string subscription_id) {
        // Create a subscriber with 16 threads handling I/O work, by default the
        // library creates `std::thread::hardware_concurrency()` threads.
        auto subscriber = pubsub::Subscriber(pubsub::MakeSubscriberConnection(
            pubsub::Subscription(std::move(project_id), std::move(subscription_id)),
            Options{}
                .set<pubsub::MaxConcurrencyOption>(8)
                .set<GrpcBackgroundThreadPoolSizeOption>(16)));
    
        // Create a subscription where up to 8 messages are handled concurrently. By
        // default the library uses `std::thread::hardware_concurrency()` as the
        // maximum number of concurrent callbacks.
        auto session = subscriber.Subscribe(
            [](pubsub::Message const& m, pubsub::AckHandler h) {
              // This handler executes in the I/O threads, applications could use,
              // std::async(), a thread-pool, or any other mechanism to transfer the
              // execution to other threads.
              std::cout << "Received message " << m << "\n";
              std::move(h).ack();
              PleaseIgnoreThisSimplifiesTestingTheSamples();
            });
        return std::make_pair(subscriber, std::move(session));
      };
    

## Type Aliases 

### Type

**Alias Of** : `std::size_t`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
