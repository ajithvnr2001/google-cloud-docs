---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig.Types.KeyProjectResolutionMode
title: Google Cloud Key Management Service v1 API - Enum AutokeyConfig.Types.KeyProjectResolutionMode (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:11.398512+00:00
---

# Google Cloud Key Management Service v1 API - Enum AutokeyConfig.Types.KeyProjectResolutionMode (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AutokeyConfig.Types.KeyProjectResolutionMode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Enum AutokeyConfig.Types.KeyProjectResolutionMode (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public enum AutokeyConfig.Types.KeyProjectResolutionMode

Reference documentation and code samples for the Google Cloud Key Management Service v1 API enum AutokeyConfig.Types.KeyProjectResolutionMode.

Defines the resolution mode enum for the key project. The [KeyProjectResolutionMode][google.cloud.kms.v1.AutokeyConfig.KeyProjectResolutionMode] determines the mechanism by which [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] identifies a [key_project][google.cloud.kms.v1.AutokeyConfig.key_project] at its specific configuration node. This parameter also determines if Autokey can be used within this project or folder.

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`DedicatedKeyProject` | Keys are created in a dedicated project specified by `key_project`.  
`Disabled` | Disables the AutokeyConfig. When this mode is set, any AutokeyConfig from higher levels in the resource hierarchy are ignored for this resource and its descendants. This setting can be overridden by a more specific configuration at a lower level. For example, if Autokey is disabled on a folder, it can be re-enabled on a sub-folder or project within that folder by setting a different mode (e.g., DEDICATED_KEY_PROJECT or RESOURCE_PROJECT).  
`ResourceProject` | Keys are created in the same project as the resource requesting the key. The `key_project` must not be set when this mode is used.  
`Unspecified` | Default value. KeyProjectResolutionMode when not specified will act as `DEDICATED_KEY_PROJECT`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
