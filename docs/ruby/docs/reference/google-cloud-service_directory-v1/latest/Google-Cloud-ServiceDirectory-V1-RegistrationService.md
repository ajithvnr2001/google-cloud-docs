---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory-V1-RegistrationService/
title: Service Directory V1 API - Module Google::Cloud::ServiceDirectory::V1::RegistrationService (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:17.487843+00:00
---

# Service Directory V1 API - Module Google::Cloud::ServiceDirectory::V1::RegistrationService (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory-V1-RegistrationService/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Directory V1 API - Module Google::Cloud::ServiceDirectory::V1::RegistrationService (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the Service Directory V1 API module Google::Cloud::ServiceDirectory::V1::RegistrationService.

Service Directory API for registering services. It defines the following resource model:

  * The API has a collection of [Namespace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory-V1-Namespace "Google::Cloud::ServiceDirectory::V1::Namespace \(class\)") resources, named `projects/_/locations/_ /namespaces/__`.

  * Each Namespace has a collection of [Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory-V1-Service "Google::Cloud::ServiceDirectory::V1::Service \(class\)") resources, named `projects//locations/_/namespaces/_ /services/__`.

  * Each Service has a collection of [Endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory-V1-Endpoint "Google::Cloud::ServiceDirectory::V1::Endpoint \(class\)") resources, named `projects//locations/_/namespaces/_ /services/_/endpoints/_`.




To load this service and instantiate a REST client:
    
    
    require "google/cloud/service_directory/v1/registration_service/rest"
    client = ::Google::Cloud::ServiceDirectory::V1::RegistrationService::Rest::Client.new
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
