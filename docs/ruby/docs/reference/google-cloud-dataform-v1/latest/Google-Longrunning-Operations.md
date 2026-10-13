---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Longrunning-Operations/
title: Dataform V1 API - Module Google::Longrunning::Operations (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:45.337254+00:00
---

# Dataform V1 API - Module Google::Longrunning::Operations (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Longrunning-Operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataform V1 API - Module Google::Longrunning::Operations (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataform V1 API module Google::Longrunning::Operations.

Manages long-running operations with an API service.

When an API method normally takes long time to complete, it can be designed to return [Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataform-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") to the client, and the client can use this interface to receive the real response asynchronously by polling the operation resource, or pass the operation resource to another API (such as Pub/Sub API) to receive the response. Any API service that returns long-running operations should implement the `Operations` interface so developers can have a consistent client experience.

To load this service and instantiate a REST client:
    
    
    require "google/longrunning/operations/rest"
    client = ::Google::Longrunning::Operations::Rest::Client.new
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
