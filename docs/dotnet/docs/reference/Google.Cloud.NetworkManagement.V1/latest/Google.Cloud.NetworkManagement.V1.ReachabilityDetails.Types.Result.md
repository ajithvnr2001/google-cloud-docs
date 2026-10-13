---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.ReachabilityDetails.Types.Result
title: Network Management v1 API - Enum ReachabilityDetails.Types.Result (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:38.051505+00:00
---

# Network Management v1 API - Enum ReachabilityDetails.Types.Result (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1.ReachabilityDetails.Types.Result

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Management v1 API - Enum ReachabilityDetails.Types.Result (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.1.0  1.0.0 
    
    
    public enum ReachabilityDetails.Types.Result

Reference documentation and code samples for the Network Management v1 API enum ReachabilityDetails.Types.Result.

The overall result of the test's configuration analysis.

## Namespace

[Google.Cloud.NetworkManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkManagement.V1/latest/Google.Cloud.NetworkManagement.V1)

## Assembly

Google.Cloud.NetworkManagement.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`Ambiguous` | The source and destination endpoints do not uniquely identify the test location in the network, and the reachability result contains multiple traces. For some traces, a packet could be delivered, and for others, it would not be. This result is also assigned to configuration analysis of return path if on its own it should be REACHABLE, but configuration analysis of forward path is AMBIGUOUS.  
`Reachable` | Possible scenarios are:

  * The configuration analysis determined that a packet originating from the source is expected to reach the destination.
  * The analysis didn't complete because the user lacks permission for some of the resources in the trace. However, at the time the user's permission became insufficient, the trace had been successful so far.

  
`Undetermined` | The configuration analysis did not complete. Possible reasons are:

  * A permissions error occurred--for example, the user might not have read permission for all of the resources named in the test.
  * An internal error occurred.
  * The analyzer received an invalid or unsupported argument or was unable to identify a known endpoint.

  
`Unreachable` | A packet originating from the source is expected to be dropped before reaching the destination.  
`Unspecified` | No result was specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
