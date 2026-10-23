---
url: https://docs.cloud.google.com/storage/docs/samples/storage-view-lifecycle-management-configuration/
title: Get a lifecycle policy for a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:29.017143+00:00
---

# Get a lifecycle policy for a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-view-lifecycle-management-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Get a lifecycle policy for a bucket Stay organized with collections  Save and categorize content based on your preferences. 

View the lifecycle configuration of a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage object lifecycles](https://docs.cloud.google.com/storage/docs/managing-lifecycles)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> updated_metadata =
          client.GetBucketMetadata(bucket_name);
      if (!updated_metadata) throw std::move(updated_metadata).status();
    
      if (!updated_metadata->has_lifecycle() ||
          updated_metadata->lifecycle().rule.empty()) {
        std::cout << "Bucket lifecycle management is not enabled for bucket "
                  << updated_metadata->name() << ".\n";
        return;
      }
      std::cout << "Bucket lifecycle management is enabled for bucket "
                << updated_metadata->name() << ".\n";
      std::cout << "The bucket lifecycle rules are";
      for (auto const& kv : updated_metadata->lifecycle().rule) {
        std::cout << "\n " << kv.condition() << ", " << kv.action();
      }
      std::cout << "\n";
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
