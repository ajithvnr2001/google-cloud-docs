---
url: https://docs.cloud.google.com/cpp/docs/reference/gkerecommender/latest/gkerecommender-override-retry/
title: Override Retry, Backoff, and Idempotency Policies \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:40.166381+00:00
---

# Override Retry, Backoff, and Idempotency Policies  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/gkerecommender/latest/gkerecommender-override-retry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Override Retry, Backoff, and Idempotency Policies Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1 

When it is safe to do so, the library automatically retries requests that fail due to a transient error. The library then uses [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) to backoff before trying again. Which operations are considered safe to retry, which errors are treated as transient failures, the details of the exponential backoff algorithm, and for how long the library retries are all configurable via policies.

This document provides examples showing how to override the default policies.

The policies can be set when the `*Connection` object is created. The library provides default policies for any policy that is not set. The application can also override some (or all) policies when the `*Client` object is created. This can be useful if multiple `*Client` objects share the same `*Connection` object, but you want different retry behavior in some of the clients. Finally, the application can override some retry policies when calling a specific member function.

The library uses three different options to control the retry loop. The options have per-client names.

## Configuring the transient errors and retry duration

The `*RetryPolicyOption` controls:

  * Which errors are to be treated as transient errors.
  * How long the library will keep retrying transient errors.



You can provide your own class for this option. The library also provides two built-in policies:

  * `*LimitedErrorCountRetryPolicy`: stops retrying after a specified number of transient errors.
  * `*LimitedTimeRetryPolicy`: stops retrying after a specified time.



Note that a library may have more than one version of these classes. Their name match the `*Client` and `*Connection` object they are intended to be used with. Some `*Client` objects treat different error codes as transient errors. In most cases, only [kUnavailable](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud_1a90e17f75452470f0f3ee1a06ffe58847.html) is treated as a transient error.

## Controlling the backoff algorithm

The `*BackoffPolicyOption` controls how long the client library will wait before retrying a request that failed with a transient error. You can provide your own class for this option.

The only built-in backoff policy is [`ExponentialBackoffPolicy`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html). This class implements a truncated exponential backoff algorithm, with jitter. In summary, it doubles the current backoff time after each failure. The actual backoff time for an RPC is chosen at random, but never exceeds the current backoff. The current backoff is doubled after each failure, but never exceeds (or is "truncated") if it reaches a prescribed maximum.

## Controlling which operations are retryable

The `*IdempotencyPolicyOption` controls which requests are retryable, as some requests are never safe to retry.

Only one built-in idempotency policy is provided by the library. The name matches the name of the client it is intended for. For example, `FooBarClient` will use `FooBarIdempotencyPolicy`. This policy is very conservative.

## Example

For example, this will override the retry policies for `gkerecommender_v1::GkeInferenceQuickstartClient`:
    
    
      auto options =
          google::cloud::Options{}
              .set<google::cloud::gkerecommender_v1::
                       GkeInferenceQuickstartConnectionIdempotencyPolicyOption>(
                  CustomIdempotencyPolicy().clone())
              .set<google::cloud::gkerecommender_v1::
                       GkeInferenceQuickstartRetryPolicyOption>(
                  google::cloud::gkerecommender_v1::
                      GkeInferenceQuickstartLimitedErrorCountRetryPolicy(3)
                          .clone())
              .set<google::cloud::gkerecommender_v1::
                       GkeInferenceQuickstartBackoffPolicyOption>(
                  google::cloud::ExponentialBackoffPolicy(
                      /*initial_delay=*/std::chrono::milliseconds(200),
                      /*maximum_delay=*/std::chrono::seconds(45),
                      /*scaling=*/2.0)
                      .clone());
      auto connection =
          google::cloud::gkerecommender_v1::MakeGkeInferenceQuickstartConnection(
              options);
    
      // c1 and c2 share the same retry policies
      auto c1 = google::cloud::gkerecommender_v1::GkeInferenceQuickstartClient(
          connection);
      auto c2 = google::cloud::gkerecommender_v1::GkeInferenceQuickstartClient(
          connection);
    
      // You can override any of the policies in a new client. This new client
      // will share the policies from c1 (or c2) *except* for the retry policy.
      auto c3 = google::cloud::gkerecommender_v1::GkeInferenceQuickstartClient(
          connection, google::cloud::Options{}
                          .set<google::cloud::gkerecommender_v1::
                                   GkeInferenceQuickstartRetryPolicyOption>(
                              google::cloud::gkerecommender_v1::
                                  GkeInferenceQuickstartLimitedTimeRetryPolicy(
                                      std::chrono::minutes(5))
                                      .clone()));
    
      // You can also override the policies in a single call:
      // c3.SomeRpc(..., google::cloud::Options{}
      //     .set<google::cloud::gkerecommender_v1::GkeInferenceQuickstartRetryPolicyOption>(
      //       google::cloud::gkerecommender_v1::GkeInferenceQuickstartLimitedErrorCountRetryPolicy(10).clone()));
    

This assumes you have created a custom idempotency policy. Such as:
    
    
    class CustomIdempotencyPolicy
        : public google::cloud::gkerecommender_v1::
              GkeInferenceQuickstartConnectionIdempotencyPolicy {
     public:
      ~CustomIdempotencyPolicy() override = default;
      std::unique_ptr<google::cloud::gkerecommender_v1::
                          GkeInferenceQuickstartConnectionIdempotencyPolicy>
      clone() const override {
        return std::make_unique<CustomIdempotencyPolicy>(*this);
      }
      // Override inherited functions to define as needed.
    };
    

## More Information

###### See Also

[`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html)

###### See Also

[`google::cloud::BackoffPolicy`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)

###### See Also

[`google::cloud::ExponentialBackoffPolicy`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
