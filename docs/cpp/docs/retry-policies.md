---
url: https://docs.cloud.google.com/cpp/docs/retry-policies/
title: Retry Policies in the C++ Client Libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:46.360347+00:00
---

# Retry Policies in the C++ Client Libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/retry-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Guides ](https://docs.cloud.google.com/cpp/docs/setup)



Send feedback 

#  Retry Policies in the C++ Client Libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the retry model used by the C++ client libraries.

The client libraries issue RPCs (Remote Procedure Calls) on your behalf. These RPCs can fail due to transient errors. Servers restart, load balancers closing overloaded or idle connections, and rate limits can take effect, and these are only some examples of transient failures.

The libraries could return these errors to the application. However, many of these errors are easy to handle in the library, which makes the application code simpler.

## Retryable Errors and Retryable Operations

Only transient errors are retryable. For example, `kUnavailable` indicates that the client could not connect, or lost its connection to a service while a request was in progress. This is almost always a transient condition, though it may take a long time to recover. These errors are always retryable (assuming the operation itself is safe to retry). In contract, `kPermissionDenied` errors require additional intervention (usually by a human) to be resolved. Such errors are not considered "transient", or at least not transient in the timescales considered by the retry loops in the client library.

Likewise, some operations are not safe to retry, regardless of the nature of the error. This includes any operations that make incremental changes. For example, it is not safe to retry an operation to remove "the latest version of X" where there may be multiple versions of a resource named "X". This is because the caller probably intended to remove a single version, and retrying such a request can result in removing all the versions.

## Configure retry loops

The client libraries accept three different configuration parameters to control the retry loops:

  * The `*IdempotencyPolicy` determines if a particular request is idempotent. Only such requests are retried.
  * The `*RetryPolicy` determines (a) if an error should be consider a transient failure, and (b) how long (or how many times) the client library retries a request.
  * The `*BackoffPolicy` determines how long the client library waits before reissuing the request.



### Default Idempotency Policy

In general, an operation is [idempotent](https://en.wikipedia.org/wiki/Idempotence#Computer_science_meaning) if successfully calling the function multiple times leaves the system in the same state as successfully calling the function once. Only idempotent operations are safe to retry. Examples of idempotent operations include, but are not limited to, all read-only operations, and operations that can only succeed once.

By default, the client library only treat RPCs that are implemented via `GET` or `PUT` verbs as idempotent. This may be too conservative, in some services even some `POST` requests are idempotent. You can always override the default idempotency policy to better fit your needs.

Some operations are only idempotent if they include pre-conditions. For example, "remove the latest version if the latest version is Y" is idempotent, as it can only succeed once.

From time to time, the client libraries receive improvements to treat more operations as idempotent. We consider these improvements bug fixes, and therefore non-breaking even if they change the client library behavior.

Note that while it may be safe to retry an operation, this does not mean the operation produces the same result on the second attempt vs. the first successful attempt. For example, creating a uniquely identified resource may be safe to retry, as the second and successive attempts fail and leave the system in the same state. However, the client may receive an "already exists" error on the retry attempts.

### Default Retry Policy

Following the guidelines outlined in [aip/194](https://google.aip.dev/194), most C++ client libraries only retry `UNAVAILABLE` gRPC-errors. These are mapped to [`StatusCode::kUnavailable`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud_1a90e17f75452470f0f3ee1a06ffe58847). The default policy is to retry requests for 30 minutes.

Note that `kUnavailable` errors do **not** indicate that the server failed to receive the request. This error code is used when the request cannot be sent, but it is also used if the request is successfully sent, received by the service, and the connection is lost before the response is received by the client. Moreover, if you could determine if the request was successfully received, you could solve the [Two General's problem](https://en.wikipedia.org/wiki/Two_Generals%27_Problem), a well-known impossibility result in distributed systems.

Therefore, it is not safe to retry all operations that fail with `kUnavailable`. The idempotency of the operation matters too.

### Default Backoff Policy

By default, most libraries use a truncated exponential backoff strategy, with jitter. The initial backoff is 1 second, the maximum backoff is 5 minutes, and the backoff doubles after each retry.

## Change default retry and backoff policies

Each library defines an `*Option` struct to configure these policies. You can provide these options when you create the `*Client` class, or even on each request.

For example, this shows how to change the retry and backoff policies for a Cloud Pub/Sub client:
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::Options;
    using ::google::cloud::StatusOr;
    [](std::string project_id, std::string topic_id) {
      auto topic = pubsub::Topic(std::move(project_id), std::move(topic_id));
      // By default a publisher will retry for 60 seconds, with an initial backoff
      // of 100ms, a maximum backoff of 60 seconds, and the backoff will grow by
      // 30% after each attempt. This changes those defaults.
      auto publisher = pubsub::Publisher(pubsub::MakePublisherConnection(
          std::move(topic),
          Options{}
              .set<pubsub::RetryPolicyOption>(
                  pubsub::LimitedTimeRetryPolicy(
                      /*maximum_duration=*/std::chrono::minutes(10))
                      .clone())
              .set<pubsub::BackoffPolicyOption>(
                  pubsub::ExponentialBackoffPolicy(
                      /*initial_delay=*/std::chrono::milliseconds(200),
                      /*maximum_delay=*/std::chrono::seconds(45),
                      /*scaling=*/2.0)
                      .clone())));
    
      std::vector<future<bool>> done;
      for (char const* data : {"1", "2", "3", "go!"}) {
        done.push_back(
            publisher.Publish(pubsub::MessageBuilder().SetData(data).Build())
                .then([](future<StatusOr<std::string>> f) {
                  return f.get().ok();
                }));
      }
      publisher.Flush();
      int count = 0;
      for (auto& f : done) {
        if (f.get()) ++count;
      }
      std::cout << count << " messages sent successfully\n";
    }

Consult the documentation of each library to find the specific names and examples for that library.

## Next Steps

  * See [Client Library Configuration](https://docs.cloud.google.com/cpp/docs/reference/common/latest/group__options) to learn more about common library configuration options.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
