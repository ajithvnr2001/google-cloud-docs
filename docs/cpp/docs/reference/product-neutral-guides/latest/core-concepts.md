---
url: https://docs.cloud.google.com/cpp/docs/reference/product-neutral-guides/latest/core-concepts/
title: Google Cloud Platform C++ Client Libraries: Core Concepts \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:06.765062+00:00
---

# Google Cloud Platform C++ Client Libraries: Core Concepts  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/product-neutral-guides/latest/core-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Google Cloud Platform C++ Client Libraries: Core Concepts Stay organized with collections  Save and categorize content based on your preferences. 

3.3.0 (latest)  3.3.0-rc  3.2.0 

This documentation covers essential patterns and usage for the Google Cloud C++ Client Library, focusing on performance, data handling (`StatusOr`), and flow control (Pagination, Futures, Streaming).

## 1\. Installation & Setup

The C++ libraries are typically installed via **vcpkg** or **Conda** , or compiled from source using **CMake**.

**Example using vcpkg:**
    
    
    vcpkg install google-cloud-cpp
    

**CMakeLists.txt:**
    
    
    find_package(google_cloud_cpp_pubsub REQUIRED)
    add_executable(my_app main.cc)
    target_link_libraries(my_app google-cloud-cpp::pubsub)
    

## 2\. StatusOr<T> and Error Handling

C++ does not use exceptions for API errors by default. Instead, it uses `google::cloud::StatusOr<T>`.

  * **Success:** The object contains the requested value.
  * **Failure:** The object contains a `Status` (error code and message).


    
    
    void HandleResponse(google::cloud::StatusOr<std::string> response) {
      if (!response) {
        // Handle error
        std::cerr << "RPC failed: " << response.status().message() << "\n";
        return;
      }
      // Access value
      std::cout << "Success: " << *response << "\n";
    }
    

## 3\. Pagination (StreamRange)

List methods in C++ return a `google::cloud::StreamRange<T>`. This works like standard C++ input iterator. The library automatically fetches new pages in the background as you iterate.
    
    
    #include "google/cloud/secretmanager/secret_manager_client.h"
    
    void ListSecrets(google::cloud::secretmanager::SecretManagerServiceClient client) {
      // Call the API
      // Returns StreamRange<google::cloud::secretmanager::v1::Secret>
      auto range = client.ListSecrets("projects/my-project");
    
      for (auto const& secret : range) {
        if (!secret) {
          // StreamRange returns StatusOr<T> on dereference to handle failures mid-stream
          std::cerr << "Error listing secret: " << secret.status() << "\n";
          break;
        }
        std::cout << "Secret: " << secret->name() << "\n";
      }
    }
    

## 4\. Long Running Operations (LROs)

LROs in C++ return a `std::future<StatusOr<T>>`.

### Blocking Wait
    
    
    #include "google/cloud/compute/instances_client.h"
    
    void CreateInstance(google::cloud::compute::InstancesClient client) {
      google::cloud::compute::v1::InsertInstanceRequest request;
      // ... set request fields ...
    
      // Start the operation
      // Returns future<StatusOr<Operation>>
      auto future = client.InsertInstance(request);
    
      // Block until complete
      auto result = future.get();
    
      if (!result) {
        std::cerr << "Creation failed: " << result.status() << "\n";
      } else {
        std::cout << "Instance created successfully\n";
      }
    }
    

### Async / Non-Blocking

You can use standard C++ `future` capabilities, such as polling `wait_for` or attaching continuations (via `.then` if using the library's future extension, though standard `std::future` is strictly blocking/polling).

## 5\. Update Masks

The C++ libraries use `google::protobuf::FieldMask`.
    
    
    #include "google/cloud/secretmanager/secret_manager_client.h"
    #include <google/protobuf/field_mask.pb.h>
    
    void UpdateSecret(google::cloud::secretmanager::SecretManagerServiceClient client) {
      namespace secretmanager = ::google::cloud::secretmanager::v1;
    
      secretmanager::Secret secret;
      secret.set_name("projects/my-project/secrets/my-secret");
      (*secret.mutable_labels())["env"] = "production";
    
      google::protobuf::FieldMask update_mask;
      update_mask.add_paths("labels");
    
      secretmanager::UpdateSecretRequest request;
      *request.mutable_secret() = secret;
      *request.mutable_update_mask() = update_mask;
    
      auto result = client.UpdateSecret(request);
    }
    

## 6\. gRPC Streaming

### Server-Side Streaming

Similar to pagination, Server-Side streaming usually returns a `StreamRange` or a specialized reader object.
    
    
    #include "google/cloud/bigquery/storage/bigquery_read_client.h"
    
    void ReadRows(google::cloud::bigquery_storage::BigQueryReadClient client) {
      google::cloud::bigquery::storage::v1::ReadRowsRequest request;
      request.set_read_stream("projects/.../streams/...");
    
      // Returns a StreamRange of ReadRowsResponse
      auto stream = client.ReadRows(request);
    
      for (auto const& response : stream) {
        if (!response) {
          std::cerr << "Error reading row: " << response.status() << "\n";
          break;
        }
        // Process response->avro_rows()
      }
    }
    

### Bidirectional Streaming

Bidirectional streaming uses a `AsyncReaderWriter` pattern (or synchronous `ReaderWriter`).
    
    
    #include "google/cloud/speech/speech_client.h"
    
    void StreamingRecognize(google::cloud::speech::SpeechClient client) {
      // Start the stream
      auto stream = client.StreamingRecognize();
    
      // 1. Send Config
      google::cloud::speech::v1::StreamingRecognizeRequest config_request;
      // ... configure ...
      stream->Write(config_request);
    
      // 2. Send Audio
      google::cloud::speech::v1::StreamingRecognizeRequest audio_request;
      // ... load audio data ...
      stream->Write(audio_request);
    
      // 3. Close writing to signal we are done sending
      stream->WritesDone();
    
      // 4. Read responses
      google::cloud::speech::v1::StreamingRecognizeResponse response;
      while (stream->Read(&response)) {
        for (const auto& result : response.results()) {
           std::cout << "Transcript: " << result.alternatives(0).transcript() << "\n";
        }
      }
    
      // Check final status
      auto status = stream->Finish();
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
