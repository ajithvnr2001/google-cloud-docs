---
url: https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/hypercomputecluster-override-endpoint/
title: How to Override the Default Endpoint \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:02.436870+00:00
---

# How to Override the Default Endpoint  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/hypercomputecluster-override-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  How to Override the Default Endpoint Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0 

In some cases, you may need to override the default endpoint used by the client library. Use the [EndpointOption](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1EndpointOption.html) when initializing the client library to change this default.

For example, this will override the default endpoint for `hypercomputecluster_v1::HypercomputeClusterClient`:
    
    
      // This configuration is common with Private Google Access:
      //     https://cloud.google.com/vpc/docs/private-google-access
      auto options = google::cloud::Options{}.set<google::cloud::EndpointOption>(
          "private.googleapis.com");
      auto vpc_client =
          google::cloud::hypercomputecluster_v1::HypercomputeClusterClient(
              google::cloud::hypercomputecluster_v1::
                  MakeHypercomputeClusterConnection(options));
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
