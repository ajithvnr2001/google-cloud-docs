---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.Build.Types.FailureInfo.Types.FailureType
title: Cloud Build v1 API - Enum Build.Types.FailureInfo.Types.FailureType (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:12.789704+00:00
---

# Cloud Build v1 API - Enum Build.Types.FailureInfo.Types.FailureType (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.Build.Types.FailureInfo.Types.FailureType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Build v1 API - Enum Build.Types.FailureInfo.Types.FailureType (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public enum Build.Types.FailureInfo.Types.FailureType

Reference documentation and code samples for the Cloud Build v1 API enum Build.Types.FailureInfo.Types.FailureType.

The name of a fatal problem encountered during the execution of the build.

## Namespace

[Google.Cloud.CloudBuild.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1)

## Assembly

Google.Cloud.CloudBuild.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`FetchSourceFailed` | The source fetching has failed.  
`LoggingFailure` | Backend logging failures. Should retry.  
`PushFailed` | Unable to push the image to the repository.  
`PushImageNotFound` | Final image not found.  
`PushNotAuthorized` | Unauthorized push of the final image.  
`Unspecified` | Type unspecified  
`UserBuildStep` | A build step has failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
