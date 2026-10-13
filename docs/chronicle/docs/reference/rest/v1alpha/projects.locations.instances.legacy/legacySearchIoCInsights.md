---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchIoCInsights/
title: Method: legacy.legacySearchIoCInsights \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:49.078204+00:00
---

# Method: legacy.legacySearchIoCInsights  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchIoCInsights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacy.legacySearchIoCInsights Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * InsightGroup
    * JSON representation
  * Insight
    * JSON representation



**Full name** : projects.locations.instances.legacy.legacySearchIoCInsights

Rpc to list IoC insights on given artifacts.

### HTTP request

`GET https://{endpoint}/v1alpha/{instance}/legacy:legacySearchIoCInsights`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. Chronicle instance this request is sent to. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`domainNames[]` |  `string` Optional. The domains we are interested in.  
`destinationIpAddresses[]` |  `string` Optional. The ip addresses we are interested in.  
  
### Request body

The request body must be empty.

### Response body

Any insights about the requested artifacts. Each insight is independent of the other, meaning an artifact can be repeated.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "insightGroups": [
        {
          object ([InsightGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchIoCInsights#InsightGroup))
        }
      ]
    }  
  
Fields  
---  
`insightGroups[]` |  `object (`[InsightGroup](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchIoCInsights#InsightGroup)`)` Can be empty if there is nothing interesting about the given artifacts.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacies.legacySearchIoCInsights`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## InsightGroup

Used for populating IoC insights in asset view. Represents a feed with its metadata and all of its artifact matches.

JSON representation  
---  
      
    
    {
      "title": string,
      "description": string,
      "insights": [
        {
          object ([Insight](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchIoCInsights#Insight))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` (e.g. Emerging Threats IoC)  
`description` |  `string` Description of the feed.  
`insights[]` |  `object (`[Insight](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacy/legacySearchIoCInsights#Insight)`)` Represents all artifacts that matched under this feed. This will have a minimum of 1 entry.  
  
## Insight

An ioc artifact and how it is categorized.

JSON representation  
---  
      
    
    {
      "subtitle": string,
      "artifact": {
        object ([ArtifactIndicator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ArtifactIndicator))
      },
      "confidenceScore": string,
      "rawSeverity": string,
      "feed": string
    }  
  
Fields  
---  
`subtitle` |  `string` A comma-separated string of categories (e.g. bitcoin related)  
`artifact` |  `object (`[ArtifactIndicator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/ArtifactIndicator)`)` (e.g., example.com or 198.51.100.23).  
`confidenceScore` |  `string` Raw confidence level from the IoC source, higher score means more confidence. If there is no confidence score in the raw data, this will not be set.  
`rawSeverity` |  `string` The indicator's raw severity.  
`feed` |  `string` ONLY RELEVANT TO FEED AGGREGATORS. The underlying feed from the feed aggregator that provided the IoC. This field will be empty for feeds that are not aggregators.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
