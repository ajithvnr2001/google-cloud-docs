---
url: https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/
title: Cloud Datastore API C++ Client Library \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:37.144161+00:00
---

# Cloud Datastore API C++ Client Library  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Cloud Datastore API C++ Client Library Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

An idiomatic C++ client library for the [Cloud Datastore API](https://cloud.google.com/datastore). This API accesses the schemaless NoSQL database to provide fully managed, robust, scalable storage for your application.

While this library is **GA** , please note that the Google Cloud C++ client libraries do **not** follow [Semantic Versioning](https://semver.org/).

### Quickstart

The following shows the code that you'll run in the `google/cloud/datastore/quickstart/` directory, which should give you a taste of the Cloud Datastore API C++ client library API.
    
    
    #include "google/cloud/datastore/v1/datastore_client.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " project-id\n";
        return 1;
      }
    
      namespace datastore = ::google::cloud::datastore_v1;
      auto client =
          datastore::DatastoreClient(datastore::MakeDatastoreConnection());
    
      auto const* project_id = argv[1];
    
      google::datastore::v1::Key key;
      key.mutable_partition_id()->set_project_id(project_id);
      auto& path = *key.add_path();
      path.set_kind("Task");
      path.set_name("sampletask1");
    
      google::datastore::v1::Mutation mutation;
      auto& upsert = *mutation.mutable_upsert();
      *upsert.mutable_key() = key;
      google::datastore::v1::Value value;
      value.set_string_value("Buy milk");
      upsert.mutable_properties()->insert({"description", std::move(value)});
    
      auto put = client.Commit(
          project_id, google::datastore::v1::CommitRequest::NON_TRANSACTIONAL,
          {mutation});
      if (!put) throw std::move(put).status();
    
      std::cout << "Saved " << key.DebugString() << " " << put->DebugString()
                << "\n";
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }
    

### Main classes

This library offers multiple `*Client` classes, which are listed below. Each one of these classes exposes all the RPCs for a service as member functions of the class. This library groups multiple services because they are part of the same product or are often used together. A typical example may be the administrative and data plane operations for a single product.

The library also has other classes that provide helpers, configuration parameters, and infrastructure to mock the `*Client` classes when testing your application.

  * [`datastore_admin_v1::DatastoreAdminClient`](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__admin__v1_1_1DatastoreAdminClient)
  * [`datastore_v1::DatastoreClient`](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/classgoogle_1_1cloud_1_1datastore__v1_1_1DatastoreClient)



### More Information

  * [Error Handling](https://docs.cloud.google.com/cpp/docs/reference/common/latest/common-error-handling.html) \- describes how the library reports errors.
  * [How to Override the Default Endpoint](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/datastore-override-endpoint) \- describes how to override the default endpoint.
  * [How to Override the Authentication Credentials](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/datastore-override-authentication) \- describes how to change the authentication credentials used by the library.
  * [Override Retry, Backoff, and Idempotency Policies](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/datastore-override-retry) \- describes how to change the default retry policies.
  * [Environment Variables](https://docs.cloud.google.com/cpp/docs/reference/datastore/latest/datastore-env) \- describes environment variables that can configure the behavior of the library. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
