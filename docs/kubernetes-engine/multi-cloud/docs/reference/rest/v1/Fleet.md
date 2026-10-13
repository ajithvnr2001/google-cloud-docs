---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/Fleet/
title: Fleet \u00a0|\u00a0 GKE Multi-Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:15.220657+00:00
---

# Fleet  |  GKE Multi-Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/Fleet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE Multi-Cloud Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/reference/rest/v1/projects.locations)



Send feedback 

#  Fleet Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Fleet related configuration.

Fleets are a Google Cloud concept for logically organizing clusters, letting you use and manage multi-cluster capabilities and apply consistent policies across your systems.

See [Anthos Fleets](https://cloud.google.com/anthos/multicluster-management/fleets) for more details on Anthos multi-cluster capabilities using Fleets.

JSON representation  
---  
      
    
    {
      "project": string,
      "membership": string
    }  
  
Fields  
---  
`project` |  `string` Required. The name of the Fleet host project where this cluster will be registered.Project names are formatted as `projects/<project-number>`.  
`membership` |  `string` Output only. The name of the managed Hub Membership resource associated to this cluster.Membership names are formatted as `projects/<project-number>/locations/global/membership/<cluster-id>`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
