---
url: https://docs.cloud.google.com/data-fusion/docs/reference/sap-ariba-batch-source-reference/
title: SAP Ariba Batch Source reference \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:14.785991+00:00
---

# SAP Ariba Batch Source reference  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/sap-ariba-batch-source-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  SAP Ariba Batch Source reference Stay organized with collections  Save and categorize content based on your preferences. 

The Ariba Batch Source plugin lets you integrate bulk data from SAP Ariba applications with Cloud Data Fusion. You can configure and execute bulk data transfers from Ariba without any coding.

For more information, see [Connect to SAP Ariba](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-ariba-batch-source).

## Configuration

**Property** | **Macro enabled** | **Description**  
---|---|---  
Label | No | Required. A name for the Ariba node in the Cloud Data Fusion data pipeline.  
Use connection (On/Off toggle) | No | Whether to use an existing connection (see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections)).   
Connections (browse connections) | Yes | Choose the existing connection to use.  
Token Endpoint | Yes | Required. Token path of the Ariba API.  
API Endpoint | Yes | Required. Specifies the base path of the Ariba API, similar to the following:  
`https://sandbox.api.sap.com`  
Ariba Client ID | Yes | Required. The Ariba client ID.  
Ariba Client Secret | Yes | Required. The Ariba client secret.  
Ariba API Key | Yes | Required. The Ariba application key.  
Realm | Yes | Required. The Realm name from which the data is extracted, similar to the following: `S4VALL`.  
System Type | No | Required. The type of system the Ariba instance runs on: Production or Sandbox.  
Reference Name | No | Required. Uniquely identifies the source for lineage, annotating metadata.  
View Template Name | Yes | Required. The Name of the view template from which data is extracted, similar to the following: `RequestFactSystemView`.  
From Date  | Yes | The start date of the extraction, similar to the following: `2021-12-01T00:00:00Z`.  
To Date | Yes | The end date of the extraction, similar to the following: `2022-03-29T00:00:00Z`.   
  
## Data Type Mapping

**Ariba Data Type** | **Cloud Data Fusion Schema Data Type**  
---|---  
`Number` | `Double`  
`Boolean` | `Boolean`  
`String` | `String`  
`Array` | `Array`  
`Date` | `Timestamp`  
`Object` | `Record`  
  
## Limits

For more information about the SAP Ariba Analytical Reporting API limits, see the [SAP documentation](https://blogs.sap.com/2021/04/13/sap-ariba-analytical-reporting-api-part-2-sap-ariba-reporting-api-structure/). The following rate limits affect your Cloud Data Fusion pipelines.

### Time span limits

The number of transactions posted within a certain time period must not exceed the limit.

The time span limit between `From Date` and `To Date` is one year. Exceeding the limit results in a validation error. For example, entering the following filter results in a validation error because the time span is greater than one year: `TimeCreated >= 2021-12-01T00:00:00Z and TimeCreated <= 2022-03-29T00:00:00Z`.

### API rate limits

**Job submission limits** : 1 per second, 2 per minute, 8 per hour, 40 per day.

When the limits are exceeded during a job, the pipeline fails.

The data extraction limit for one day is two million records. For example: 40 API calls per day * 50,000 records extracted per API call = 2,000,000 (2 million) records per day.

Rate limits are restored regularly at 00:00 AM in the timezone of the SAP Ariba data center.

### Volume limits

  * The limit is 50,000 records per call. For more information, see the [SAP documentation about limits](https://blogs.sap.com/2021/04/13/sap-ariba-analytical-reporting-api-part-2-sap-ariba-reporting-api-structure/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
