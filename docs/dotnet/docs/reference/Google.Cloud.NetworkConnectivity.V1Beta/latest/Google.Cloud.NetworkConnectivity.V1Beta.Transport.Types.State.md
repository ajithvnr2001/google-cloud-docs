---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Transport.Types.State
title: Network Connectivity v1beta API - Enum Transport.Types.State (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:27.827876+00:00
---

# Network Connectivity v1beta API - Enum Transport.Types.State (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Transport.Types.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1beta API - Enum Transport.Types.State (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta02 (latest)  1.0.0-beta01 
    
    
    public enum Transport.Types.State

Reference documentation and code samples for the Network Connectivity v1beta API enum Transport.Types.State.

Represents the status of the underlying connectivity. One of the following states, depending on who has initiated the Transport request.

## Namespace

[Google.Cloud.NetworkConnectivity.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta)

## Assembly

Google.Cloud.NetworkConnectivity.V1Beta.dll

## Fields   
  
---  
**Name** | **Description**  
`Active` | The Transport is configured and the underlying connectivity is considered operational.  
`Creating` | The resource exists locally and is being created / associated with the resource on the remote provider’s end of the underlying connectivity.  
`Deleting` | The Transport is being deleted from GCP. The underlying connectivity is no longer operational.  
`Deprovisioned` | The Transport was deleted on the remote provider's end and is no longer operational. GCP has insufficient information to move the resource back to PENDING_KEY state.  
`PendingConfig` | The Transport exists on both sides of the connection, and is waiting for configuration to finalize and be verified as operational.  
`PendingKey` | The Transport was created in GCP. Depending on the profile’s key provisioning flow, this is either waiting for an activation key to be input (the key will be validated that it uses remote resources that match the Transport), or for the generated key to be input to the provider for finalizing. The configured bandwidth is not yet guaranteed.  
`Unspecified` | Unspecified state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
