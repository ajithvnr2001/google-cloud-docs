---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1
title: Google Container Analysis v1 API - Namespace Google.Cloud.DevTools.ContainerAnalysis.V1 (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:32.759377+00:00
---

# Google Container Analysis v1 API - Namespace Google.Cloud.DevTools.ContainerAnalysis.V1 (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Container Analysis v1 API - Namespace Google.Cloud.DevTools.ContainerAnalysis.V1 (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 

## Classes 

### [ContainerAnalysis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysis)

Retrieves analysis results of Cloud components such as Docker container images. The Container Analysis API is an implementation of the [Grafeas](https://grafeas.io) API.

Analysis results are stored as a series of occurrences. An `Occurrence` contains information about a specific analysis instance on a resource. An occurrence refers to a `Note`. A note contains details describing the analysis and is generally stored in a separate project, called a `Provider`. Multiple occurrences can refer to the same note.

For example, an SSL vulnerability could affect multiple images. In this case, there would be one note for the vulnerability and an occurrence for each image with the vulnerability referring to that note.

### [ContainerAnalysis.ContainerAnalysisBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysis.ContainerAnalysisBase)

Base class for server-side implementations of ContainerAnalysis

### [ContainerAnalysis.ContainerAnalysisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysis.ContainerAnalysisClient)

Client for ContainerAnalysis

### [ContainerAnalysisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysisClient)

ContainerAnalysis client wrapper, for convenient use.

### [ContainerAnalysisClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysisClientBuilder)

Builder class for [ContainerAnalysisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysisClient) to provide simple configuration of credentials, endpoint etc.

### [ContainerAnalysisClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysisClientImpl)

ContainerAnalysis client wrapper implementation, for convenient use.

### [ContainerAnalysisSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysisSettings)

Settings for [ContainerAnalysisClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ContainerAnalysisClient) instances.

### [ExportSBOMRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ExportSBOMRequest)

The request to generate and export SBOM. Target must be specified for the request.

### [ExportSBOMRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ExportSBOMRequest.Types)

Container for nested types declared in the ExportSBOMRequest message type.

### [ExportSBOMRequest.Types.CloudStorageLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ExportSBOMRequest.Types.CloudStorageLocation)

Empty placeholder to denote that this is a Google Cloud Storage export request.

### [ExportSBOMResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ExportSBOMResponse)

The response from a call to ExportSBOM.

### [GetVulnerabilityOccurrencesSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.GetVulnerabilityOccurrencesSummaryRequest)

Request to get a vulnerability summary for some set of occurrences.

### [VulnerabilityOccurrencesSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.VulnerabilityOccurrencesSummary)

A summary of how many vulnerability occurrences there are per resource and severity type.

### [VulnerabilityOccurrencesSummary.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.VulnerabilityOccurrencesSummary.Types)

Container for nested types declared in the VulnerabilityOccurrencesSummary message type.

### [VulnerabilityOccurrencesSummary.Types.FixableTotalByDigest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.VulnerabilityOccurrencesSummary.Types.FixableTotalByDigest)

Per resource and severity counts of fixable and total vulnerabilities.

## Enums 

### [ExportSBOMRequest.TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DevTools.ContainerAnalysis.V1/latest/Google.Cloud.DevTools.ContainerAnalysis.V1.ExportSBOMRequest.TargetOneofCase)

Enum of possible cases for the "target" oneof.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
