---
url: https://docs.cloud.google.com/healthcare-api/docs/requirements/
title: Requirements \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:14:12.565452+00:00
---

# Requirements  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Resources ](https://docs.cloud.google.com/healthcare-api/docs/resources)



Send feedback 

#  Requirements Stay organized with collections  Save and categorize content based on your preferences. 

This page lists Cloud Healthcare API requirements and related information.

## Regions and versions

### Cloud regions

Only these Google Cloud regions are available:

### Regional locations

| Region name | Region description  
---|---|---  
**Americas** |  |   
| [`northamerica-northeast1`](https://cloud.google.com/about/locations#americas) | Montréal  
| [`northamerica-northeast2`](https://cloud.google.com/about/locations#americas) | Toronto  
| [`us-central1`](https://cloud.google.com/about/locations#americas) | Iowa  
| [`us-east1`](https://cloud.google.com/about/locations#americas) | South Carolina  
| [`us-east4`](https://cloud.google.com/about/locations#americas) | North Virginia  
| [`us-west1`](https://cloud.google.com/about/locations#americas) | Oregon  
| [`us-west2`](https://cloud.google.com/about/locations#americas) | Los Angeles  
| [`us-west3`](https://cloud.google.com/about/locations#americas) | Salt Lake City  
| [`southamerica-east1`](https://cloud.google.com/about/locations#americas) | São Paulo  
**Asia Pacific** |  |   
| [`asia-east1`](https://cloud.google.com/about/locations#asia-pacific) | Taiwan  
| [`asia-east2`](https://cloud.google.com/about/locations#asia-pacific) | Hong Kong  
| [`asia-northeast1`](https://cloud.google.com/about/locations#asia-pacific) | Tokyo  
| [`asia-northeast2`](https://cloud.google.com/about/locations#asia-pacific) | Osaka  
| [`asia-northeast3`](https://cloud.google.com/about/locations#asia-pacific) | Seoul  
| [`asia-south1`](https://cloud.google.com/about/locations#asia-pacific) | Mumbai  
| [`asia-southeast1`](https://cloud.google.com/about/locations#asia-pacific) | Singapore  
| [`asia-southeast2`](https://cloud.google.com/about/locations#asia-pacific) | Jakarta  
| [`australia-southeast1`](https://cloud.google.com/about/locations#asia-pacific) | Sydney  
| [`australia-southeast2`](https://cloud.google.com/about/locations#asia-pacific) | Melbourne  
**Europe** |  |   
| [`europe-north1`](https://cloud.google.com/about/locations#europe) | Finland  
| [`europe-west2`](https://cloud.google.com/about/locations#europe) | London  
| [`europe-west3`](https://cloud.google.com/about/locations#europe) | Frankfurt  
| [`europe-west4`](https://cloud.google.com/about/locations#europe) | Netherlands  
| [`europe-west6`](https://cloud.google.com/about/locations#europe) | Zurich  
**Middle East** |  |   
| [`me-west1`](https://cloud.google.com/about/locations#middle-east) | Tel Aviv  
| [`me-central1`](https://cloud.google.com/about/locations#middle-east) | Doha  
| [`me-central2`](https://cloud.google.com/about/locations#middle-east) | Dammam  
  
### Multi-regional locations

Multi-region name | Multi-region description  
---|---  
[`us`](https://cloud.google.com/about/locations/?region=multi-region#multi-region) | Data centers in the United States  
[`eu`](https://cloud.google.com/about/locations/?region=multi-region#multi-region) | Data centers in Europe  
  
### Google Cloud CLI

Cloud Healthcare API requires version 236.0.0 or higher of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).

## Permitted characters and size requirements

Resources in the Cloud Healthcare API are limited to certain characters and might be limited to certain lengths.

The following table lists the permitted characters and sizes for each resource:

Resource | Limitations  
---|---  
Datasets and FHIR, DICOM, and HL7v2 store names | 

  * Permitted characters: Any string consisting of unicode numbers, unicode letters, ASCII underscores, dashes, and periods
  * Minimum length: 1 character
  * Maximum length: 256 characters
  * Requirements as a regular expression: `[\p{L}\p{N}_-.]{1,256}`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
