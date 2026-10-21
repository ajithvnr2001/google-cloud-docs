---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/onboarding/kubernetes-off-gcp/install/migrate-in-cluster-to-managed-on-new-cluster/
title: Migrate in-cluster to managed control plane on a new cluster \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:33.655259+00:00
---

# Migrate in-cluster to managed control plane on a new cluster  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/onboarding/kubernetes-off-gcp/install/migrate-in-cluster-to-managed-on-new-cluster/

You are viewing archived v1.21 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate in-cluster to managed control plane on a new cluster

GKE clusters must be in one of the following regions or any zone within the following regions.

Region | Location  
---|---  
`asia-east1` | Taiwan  
`asia-east2` | Hong Kong  
`asia-northeast1` | Tokyo, Japan  
`asia-northeast2` | Osaka, Japan  
`asia-northeast3` | South Korea  
`asia-south1` | Mumbai, India  
`asia-south2` | Delhi, India  
`asia-southeast1` | Singapore  
`asia-southeast2 ` | Jakarta  
`australia-southeast1` | Sydney, Australia  
`australia-southeast2` | Melbourne, Australia  
`europe-central2` | Poland  
`europe-north1` | Finland  
`europe-southwest1` | Spain  
`europe-west1` | Belgium  
`europe-west2` | England  
`europe-west3` | Germany  
`europe-west4` | Netherlands  
`europe-west6` | Switzerland  
`europe-west8` | Italy  
`europe-west9` | France  
`me-central1` | Doha  
`me-central2` | Dammam, Saudi Arabia  
`me-west1` | Tel Aviv  
`northamerica-northeast1` | Montreal, Canada  
`northamerica-northeast2` | Toronto, Canada  
`southamerica-east1` | Brazil  
`southamerica-west1` | Chile  
`us-central1` | Iowa  
`us-east1` | South Carolina  
`us-east4` | Northern Virginia  
`us-east5` | Ohio  
`us-south1` | Dallas  
`us-west1` | Oregon  
`us-west2` | Los Angeles  
`us-west3` | Salt Lake City  
`us-west4` | Las Vegas  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
