---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations/
title: Artifact Registry locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:54.570698+00:00
---

# Artifact Registry locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Resources ](https://docs.cloud.google.com/artifact-registry/docs/resources)



Send feedback 

#  Artifact Registry locations Stay organized with collections  Save and categorize content based on your preferences. 

When you create a repository, you must specify its location. The chosen location determines where the repository storage is created. You can create repositories in the following types of locations:

  * _Region_ is a specific geographic place, such as Tokyo or Northern Virginia.

  * _Multi-region_ is a large geographic area, such as Asia or the United States, that contains two or more geographic places.




Artifact Registry stores artifacts in the selected location in accordance with the [Service Specific Terms](https://cloud.google.com/terms/service-terms).

A good location balances latency, availability, and bandwidth costs for data consumers:

  * Single-region repositories may help optimize latency and network bandwidth for uploads and downloads by systems located in the same region.


  * Multi-region repositories may continue to work if one of their regions are down. However, operations in multi-region repositories may be slower than single-region repositories. In addition, if a multi-region repository has an operational failure, all users of that repository will be affected regardless of region.



Generally, you should store your artifacts in a location that is convenient or contains the majority of the users of your data.

If you're also using Compute Engine, consider the following:

  * Storing data in the same region as your [Compute Engine VM instances](https://docs.cloud.google.com/compute/docs/instances) can provide better performance.

  * While you can't specify a Compute Engine zone repository location, all Compute Engine VM instances in zones within a given region have similar performance when accessing storage in that region.




To view a list of supported repository locations, run the command:
    
    
    gcloud artifacts locations list
    

## Location constraints

Your organization might have specific requirements for the location of stored data. If your organization policy includes [resource location constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), Artifact Registry enforces the constraints when you create a repository.

Organization policy compliance isn't enforced retroactively on existing repositories. To enforce new location constraints on existing stored artifacts, create new repositories after the organization policy is applied, and then migrate artifacts from old repositories to the new ones. You can use the [gcrane](https://github.com/google/go-containerregistry/tree/main/cmd/gcrane) tool to copy images between repositories.

## Available regions

Continent | Region Name | Region Description  
---|---|---  
**North America** |  |   
| `northamerica-northeast1` | Montréal  
| `northamerica-northeast2` | Toronto  
| `northamerica-south1` | Queretaro  
| `us-central1` | Iowa  
| `us-east1` | South Carolina  
| `us-east4` | Northern Virginia  
| `us-east5` | Columbus  
| `us-south1` | Dallas  
| `us-west1` | Oregon  
| `us-west2` | Los Angeles  
| `us-west3` | Salt Lake City  
| `us-west4` | Las Vegas  
**South America** |  |   
| `southamerica-east1` | São Paulo  
| `southamerica-west1` | Santiago  
**Europe** |  |   
| `europe-central2` | Warsaw  
| `europe-north1` | Finland  
| `europe-north2` | Stockholm  
| `europe-southwest1` | Madrid  
| `europe-west1` | Belgium  
| `europe-west2` | London  
| `europe-west3` | Frankfurt  
| `europe-west4` | Netherlands  
| `europe-west6` | Zürich  
| `europe-west8` | Milan  
| `europe-west9` | Paris  
| `europe-west10` | Berlin  
| `europe-west12` | Turin  
**Middle East** |  |   
| `me-central1` | Doha  
| `me-central2` | Dammam  
| `me-west1` | Tel Aviv  
**Asia** |  |   
| `asia-east1` | Taiwan  
| `asia-east2` | Hong Kong  
| `asia-northeast1` | Tokyo  
| `asia-northeast2` | Osaka  
| `asia-northeast3` | Seoul  
| `asia-south1` | Mumbai  
| `asia-south2` | Delhi  
| `asia-southeast1` | Singapore  
| `asia-southeast2` | Jakarta  
| `asia-southeast3` | Bangkok  
**Australia** |  |   
| `australia-southeast1` | Sydney  
| `australia-southeast2` | Melbourne  
**Africa** |  |   
| `africa-south1` | Johannesburg  
  
## Available multi-regions

A multi-regional location's data centers are spread across a general geographical area. For example, a resource created in the `europe` multi-region persists in multiple data centers within the European Union. It is not possible to configure which data centers are selected or where they are located within the multi-region.

If you use Google Kubernetes Engine [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming), your Artifact Registry repository must be in the same region as your GKE nodes, or in a multi-region that corresponds with the region where your nodes are running. For example:

  * If your nodes are in `us-east1`, Image streaming is available for repositories in the `us-east1` region or the `us` multi-region since both GKE and Artifact Registry are running in data center locations within the United States.
  * If your nodes are in the `northamerica-northeast1` region, the nodes are running in Canada. In this situation, Image streaming is only available for repositories in the same region.

Multi-Region Name | Multi-Region Description  
---|---  
`asia` | Data centers in Asia  
`europe` | Data centers in the European Union1  
`us` | Data centers in the United States  
  
1 Object data added to a repository in the `europe` multi-region is not stored in the `europe-west2` or `europe-west6` data center.

## What's next

  * [Create repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos)
  * [Learn more about location concepts](https://docs.cloud.google.com/docs/geography-and-regions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
