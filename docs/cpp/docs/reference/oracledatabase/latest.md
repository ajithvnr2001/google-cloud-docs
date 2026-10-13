---
url: https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/
title: Oracle Database Google Cloud API C++ Client Library \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:36.179331+00:00
---

# Oracle Database Google Cloud API C++ Client Library  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Oracle Database Google Cloud API C++ Client Library Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0 

An idiomatic C++ client library for the [Oracle Database Google Cloud API](https://cloud.google.com/oracle/database/docs).

The Oracle Database Google Cloud API provides a set of APIs to manage Oracle database services, such as Exadata and Autonomous Databases.

While this library is **GA** , please note that the Google Cloud C++ client libraries do **not** follow [Semantic Versioning](https://semver.org/).

### Quickstart

The following shows the code that you'll run in the `google/cloud/oracledatabase/quickstart/` directory, which should give you a taste of the Oracle Database Google Cloud API C++ client library API.
    
    
    #include "google/cloud/oracledatabase/v1/oracle_database_client.h"
    #include "google/cloud/location.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " project-id location-id\n";
        return 1;
      }
    
      auto const location = google::cloud::Location(argv[1], argv[2]);
    
      namespace oracledatabase = ::google::cloud::oracledatabase_v1;
      auto client = oracledatabase::OracleDatabaseClient(
          oracledatabase::MakeOracleDatabaseConnection());
    
      for (auto r : client.ListCloudExadataInfrastructures(location.FullName())) {
        if (!r) throw std::move(r).status();
        std::cout << r->DebugString() << "\n";
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }
    

### Main classes

The main class in this library is [`oracledatabase_v1::OracleDatabaseClient`](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1_1_1OracleDatabaseClient). All RPCs are exposed as member functions of this class. Other classes provide helpers, configuration parameters, and infrastructure to mock [`oracledatabase_v1::OracleDatabaseClient`](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1_1_1OracleDatabaseClient) when testing your application.

### More Information

  * [Error Handling](https://docs.cloud.google.com/cpp/docs/reference/common/latest/common-error-handling.html) \- describes how the library reports errors.
  * [How to Override the Default Endpoint](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/oracledatabase-override-endpoint) \- describes how to override the default endpoint.
  * [How to Override the Authentication Credentials](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/oracledatabase-override-authentication) \- describes how to change the authentication credentials used by the library.
  * [Override Retry, Backoff, and Idempotency Policies](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/oracledatabase-override-retry) \- describes how to change the default retry policies.
  * [Environment Variables](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/oracledatabase-env) \- describes environment variables that can configure the behavior of the library. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
