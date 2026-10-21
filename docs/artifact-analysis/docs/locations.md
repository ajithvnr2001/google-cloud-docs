---
url: https://docs.cloud.google.com/artifact-analysis/docs/locations/
title: Metadata storage locations \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:21.923713+00:00
---

# Metadata storage locations  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Resources ](https://docs.cloud.google.com/artifact-analysis/docs/resources)



Send feedback 

#  Metadata storage locations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting September 30th, 2024, Artifact Analysis is gradually transitioning to regionalized metadata storage, and providing additional API endpoints in corresponding locations.

This page outlines the locations where Artifact Analysis vulnerability metadata is stored, as well as the metadata API endpoints. Platform administrators and security managers can use this information to understand regionalized service support within Artifact Analysis.

When you push container images to Artifact Registry and perform on-push vulnerability scans, Artifact Analysis automatically stores the scan results for you. A single global endpoint is used for metadata retrieval: `https://containeranalysis.googleapis.com`.

## Upcoming changes

Starting September 30, 2024, Artifact Analysis is gradually rolling out regionalized data storage and endpoints to help support compliance with data residency requirements. The Container Analysis API stores metadata in the same region or multi-region as the Artifact Registry repository where your image is being scanned.

## Regions and multi-regions

Metadata can be stored in the following types of locations:

  * A _region_ is a specific geographic place, such as Tokyo or Northern Virginia.

  * A _multi-region_ is a large geographic area, such as Asia or the United States, that contains two or more geographic places.




## Data storage regions with regional endpoints

Artifact Analysis can store data in the following regions, which have both global and regional endpoints.

The format for each endpoint is `https://containeranalysis.REGION.rep.googleapis.com`.

**Region** | **Region description**  
---|---  
`asia-east1` | Taiwan  
`asia-east2` | Hong Kong  
`asia-northeast1` | Tokyo  
`asia-northeast3` | Seoul  
`asia-south1` | Mumbai  
`asia-south2` | Delhi  
`asia-southeast1` | Singapore  
`asia-southeast2` | Jakarta  
`australia-southeast1` | Sydney  
`europe-central2` | Warsaw  
`europe-north1` | Finland  
`europe-southwest1` | Madrid  
`europe-west1` | Belgium  
`europe-west2` | London  
`europe-west3` | Frankfurt  
`europe-west4` | Netherlands  
`europe-west6` | Zürich  
`europe-west8` | Milan  
`europe-west9` | Paris  
`me-central1` | Doha  
`me-central2` | Dammam  
`me-west1` | Tel Aviv  
`northamerica-northeast1` | Montréal  
`northamerica-northeast2` | Toronto  
`southamerica-east1` | São Paulo  
`southamerica-west1` | Santiago  
`us-central1` | Iowa  
`us-east1` | South Carolina  
`us-east4` | Northern Virginia  
`us-east5` | Columbus  
`us-south1` | Dallas  
`us-west1` | Oregon  
`us-west2` | Los Angeles  
`us-west3` | Salt Lake City  
`us-west4` | Las Vegas  
  
## Data storage regions using the global endpoint

Artifact Analysis can store data in the following regions. You must retrieve metadata through the global endpoint, `https://containeranalysis.googleapis.com`.

**Region** | **Region description**  
---|---  
`africa-south1` | Johannesburg  
`asia-northeast2` | Osaka  
`australia-southeast2` | Melbourne  
`europe-west10` | Berlin  
`europe-west12` | Turin  
  
## Data storage in multi-regions

Artifact Analysis can store data in the following regions, which only have a global endpoint. You must retrieve metadata through the global endpoint, `https://containeranalysis.googleapis.com`.

**Multi-region name** | **Multi-region description**  
---|---  
`asia` | Data centers in Asia  
`eu` | Data centers in the European Union  
`us` | Data centers in the United States  
  
## Restrict global API endpoint usage

To help enforce the use of regional endpoints, use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
