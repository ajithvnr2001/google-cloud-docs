---
url: https://docs.cloud.google.com/cpp/docs/reference/licensemanager/latest/licensemanager_v1_1_1LicenseManagerClient-retry-snippet/
title: Override licensemanager_v1::LicenseManagerClient Retry Policies \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:10.779678+00:00
---

# Override licensemanager_v1::LicenseManagerClient Retry Policies  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/licensemanager/latest/licensemanager_v1_1_1LicenseManagerClient-retry-snippet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Override licensemanager_v1::LicenseManagerClient Retry Policies Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0 

This shows how to override the retry policies for licensemanager_v1::LicenseManagerClient:
    
    
      auto options = google::cloud::Options{}
                         .set<google::cloud::licensemanager_v1::
                                  LicenseManagerConnectionIdempotencyPolicyOption>(
                             CustomIdempotencyPolicy().clone())
                         .set<google::cloud::licensemanager_v1::
                                  LicenseManagerRetryPolicyOption>(
                             google::cloud::licensemanager_v1::
                                 LicenseManagerLimitedErrorCountRetryPolicy(3)
                                     .clone())
                         .set<google::cloud::licensemanager_v1::
                                  LicenseManagerBackoffPolicyOption>(
                             google::cloud::ExponentialBackoffPolicy(
                                 /*initial_delay=*/std::chrono::milliseconds(200),
                                 /*maximum_delay=*/std::chrono::seconds(45),
                                 /*scaling=*/2.0)
                                 .clone());
      auto connection =
          google::cloud::licensemanager_v1::MakeLicenseManagerConnection(options);
    
      // c1 and c2 share the same retry policies
      auto c1 = google::cloud::licensemanager_v1::LicenseManagerClient(connection);
      auto c2 = google::cloud::licensemanager_v1::LicenseManagerClient(connection);
    
      // You can override any of the policies in a new client. This new client
      // will share the policies from c1 (or c2) *except* for the retry policy.
      auto c3 = google::cloud::licensemanager_v1::LicenseManagerClient(
          connection,
          google::cloud::Options{}
              .set<google::cloud::licensemanager_v1::
                       LicenseManagerRetryPolicyOption>(
                  google::cloud::licensemanager_v1::
                      LicenseManagerLimitedTimeRetryPolicy(std::chrono::minutes(5))
                          .clone()));
    
      // You can also override the policies in a single call:
      // c3.SomeRpc(..., google::cloud::Options{}
      //     .set<google::cloud::licensemanager_v1::LicenseManagerRetryPolicyOption>(
      //       google::cloud::licensemanager_v1::LicenseManagerLimitedErrorCountRetryPolicy(10).clone()));
    

Assuming you have created a custom idempotency policy. Such as:
    
    
    class CustomIdempotencyPolicy : public google::cloud::licensemanager_v1::
                                        LicenseManagerConnectionIdempotencyPolicy {
     public:
      ~CustomIdempotencyPolicy() override = default;
      std::unique_ptr<google::cloud::licensemanager_v1::
                          LicenseManagerConnectionIdempotencyPolicy>
      clone() const override {
        return std::make_unique<CustomIdempotencyPolicy>(*this);
      }
      // Override inherited functions to define as needed.
    };
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
