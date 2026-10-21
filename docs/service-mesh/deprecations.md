---
url: https://docs.cloud.google.com/service-mesh/deprecations/
title: Deprecations \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:08.455587+00:00
---

# Deprecations  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/deprecations/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Resources ](https://docs.cloud.google.com/service-mesh/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deprecations

The [Google Cloud Platform Terms of Service (section "Discontinuation of Services")](https://docs.cloud.google.com/terms) defines the deprecation policy that applies to Cloud Service Mesh. The [deprecation policy](https://docs.cloud.google.com/terms/deprecation) only applies to the services, features, or products listed therein. 

After a service, feature, or product is officially deprecated, it continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the service is scheduled for shutdown. 

Feature | Deprecated date | End-of-support date | Details  
---|---|---|---  
Managed Cloud Service Mesh `ISTIOD` implementation | September 28, 2026 | March 1, 2028 |  Cloud Service Mesh support for the managed `ISTIOD` control plane implementation is deprecated. You must modernize any clusters using the `ISTIOD` implementation to the `TRAFFIC_DIRECTOR` control plane prior to the end of support date to continue using managed Cloud Service Mesh.  For more information, see [Modernize your Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/modernization).   
In-cluster control plane on GKE | September 28, 2026 | March 1, 2028 |  Cloud Service Mesh support for the in-cluster `ISTIOD` control plane for GKE on Google Cloud is deprecated. Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported.  For more information, see [Migrate in-cluster to managed control plane on a new cluster](https://docs.cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster).   
Attached clusters (Amazon EKS and Microsoft AKS) | May 27, 2025 | March 17, 2027 |  Cloud Service Mesh support for attached clusters on Amazon EKS and Microsoft AKS is deprecated. GKE attached clusters are not deprecated.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
