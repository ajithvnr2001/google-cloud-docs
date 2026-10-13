---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit.Types.UnitState
title: SaaS Runtime v1beta1 API - Enum Unit.Types.UnitState (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:43.882455+00:00
---

# SaaS Runtime v1beta1 API - Enum Unit.Types.UnitState (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.Unit.Types.UnitState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  SaaS Runtime v1beta1 API - Enum Unit.Types.UnitState (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public enum Unit.Types.UnitState

Reference documentation and code samples for the SaaS Runtime v1beta1 API enum Unit.Types.UnitState.

UnitState annotates what is the current state of the unit itself.

## Namespace

[Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1/latest/Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1)

## Assembly

Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1.dll

## Fields   
  
---  
**Name** | **Description**  
`Deprovisioning` | Unit is being deleted.  
`Error` | Unit has error, when it is not ready and some error operation  
`NotProvisioned` | Unit is not provisioned.  
`Provisioning` | Unit is being provisioned.  
`Ready` | Unit has been provisioned and is ready for use  
`Unspecified` | Unspecified state.  
`Updating` | Unit is being updated. This is typically when a unit is being upgraded to a new release or some of the input variables on the Unit is being changed. Certain kinds of updates may cause the Unit to become unusable while the update is in progress.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
