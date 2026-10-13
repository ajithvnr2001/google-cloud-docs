---
url: https://docs.cloud.google.com/dataflow/docs/support/beam-runtime-support/
title: Apache Beam runtime support \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:13.317657+00:00
---

# Apache Beam runtime support  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/support/beam-runtime-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Reference ](https://docs.cloud.google.com/dataflow/docs/apis)



Send feedback 

#  Apache Beam runtime support Stay organized with collections  Save and categorize content based on your preferences. 

This page shows the runtime environments supported by Apache Beam.

## Supported Java versions

The following table shows the Java runtimes supported by each version of the Apache Beam SDK.

Apache Beam releases | Supported Java versions  
---|---  
2.74.0-2.76.0 | 11, 17, 21, 25  
2.69.0-2.73.0 | 8, 11, 17, 21, 25  
2.52.0-2.68.0 | 8, 11, 17, 21  
2.37.0-2.51.0 | 8, 11, 17  
2.29.0-2.36.0 | 8, 11  
2.28.0 or earlier | 8  
  
## Supported Python versions

The following table shows the Python runtimes supported by each version of the Apache Beam SDK.

Apache Beam releases | Supported Python versions  
---|---  
2.73.0-2.76.0 | 3.10, 3.11, 3.12, 3.13, 3.14  
2.70.0-2.72.0 | 3.10, 3.11, 3.12, 3.13  
2.69.0 | 3.9, 3.10, 3.11, 3.12, 3.13  
2.61.0-2.68.0 | 3.9, 3.10, 3.11, 3.12  
2.57.0-2.60.0 | 3.8, 3.9, 3.10, 3.11, 3.12  
2.49.0-2.56.0 | 3.8, 3.9, 3.10, 3.11  
2.47.0-2.48.0 | 3.7, 3.8, 3.9, 3.10, 3.11  
2.43.0-2.46.0 | 3.7, 3.8, 3.9, 3.10  
2.39.0-2.42.0 | 3.7, 3.8, 3.9  
2.37.0-2.38.0 | 3.6, 3.7, 3.8, 3.9  
2.25.0-2.36.0 | 3.6, 3.7, 3.8  
2.23.0-2.24.0 | 2.7, 3.5, 3.6, 3.7, 3.8  
2.16.0-2.22.0 | 2.7, 3.5, 3.6, 3.7  
2.14.0-2.15.0 | 2.7, 3.5 (beta), 3.6 (beta), 3.7 (beta)  
2.12.0-2.13.0 | 2.7, 3.5 (alpha), 3.6 (alpha), 3.7 (alpha)  
2.11.0 | 2.7, 3.5 (alpha)  
2.10.0 or earlier | 2.7  
  
## Supported Go versions

We recommend that you use the latest version of Go when working with the Apache Beam SDK for Go.

Go is compiled ahead of time to machine code, and doesn't rely on a virtual machine or interpreter. For more information, see [Does Go have a runtime?](https://go.dev/doc/faq#runtime)

The following table shows the earliest supported Go version for each version of the Apache Beam SDK.

Apache Beam releases | Supported Go versions  
---|---  
2.73.0-2.76.0 | 1.26 or later  
2.69.0-2.72.0 | 1.25 or later  
2.64.0-2.68.0 | 1.23 or later  
2.63.0 | 1.22.10 or later  
2.59.0-2.62.0 | 1.21 or later  
2.50.0-2.58.0 | 1.20 or later  
2.46.0-2.49.0 | 1.19 or later  
2.40.0-2.45.0 | 1.18 or later  
2.39.0 or earlier | 1.16 or later  
  
You can also determine the earliest supported Go version for an Apache Beam SDK release by reviewing the SDK's `go.mod` file:
    
    
    https://raw.githubusercontent.com/apache/beam/vBEAM_SDK_VERSION/sdks/go.mod
    

Replace `BEAM_SDK_VERSION` with the Apache Beam SDK version number, such as `2.76.0`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
