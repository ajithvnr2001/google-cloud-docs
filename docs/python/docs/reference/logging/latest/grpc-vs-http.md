---
url: https://docs.cloud.google.com/python/docs/reference/logging/latest/grpc-vs-http/
title: gRPC vs HTTP \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:40.068953+00:00
---

# gRPC vs HTTP  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/logging/latest/grpc-vs-http/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  gRPC vs HTTP Stay organized with collections  Save and categorize content based on your preferences. 

3.17.0 (latest)  3.16.3  3.15.0  3.13.0  3.12.1  3.11.3  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.1  3.2.5  3.1.2  3.0.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.2  1.15.3  1.14.0  1.13.0  1.12.1 

`google-cloud-logging` supports two different protocols for sending logs over the network: gRPC and HTTP. Both implementations conform to the same API, and should be invisible to the end user.

gRPC is enabled by default. You can switch to HTTP mode by either:

  * setting the DISABLE_GRPC environment variable to TRUE

  * or, passing _use_grpc=False when initializing a Client




We recommend using gRPC whenever possible, but you may want to try the HTTP implementation if you have network issues when using gRPC.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
