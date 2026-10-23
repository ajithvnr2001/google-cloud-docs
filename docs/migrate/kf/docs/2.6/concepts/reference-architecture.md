---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/concepts/reference-architecture/
title: Kf reference architecture diagrams \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:52.023368+00:00
---

# Kf reference architecture diagrams  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/concepts/reference-architecture/

Version 2.6

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.6 ](https://docs.cloud.google.com/migrate/kf/docs/2.6)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.6/getting-started)



Send feedback 

#  Kf reference architecture diagrams Stay organized with collections  Save and categorize content based on your preferences. 

Kf can benefit from the rich ecosystem of GKE Enterprise and Google Kubernetes Engine (GKE), including automation, managed backing services, and development tools.

## GKE reference architecture

Kf clusters are managed just like any other GKE cluster, and access resources in the same way.

[ ![GKE and Kf cluster architecture](https://docs.cloud.google.com/migrate/kf/docs/2.6/images/gke-reference-diagram.svg)](https://docs.cloud.google.com/static/migrate/kf/docs/images/gke-reference-diagram.svg)

## Config Sync

Kf can work with [Config Management](https://docs.cloud.google.com/anthos-config-management/docs/overview) or standalone [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview) to automate Space creation across any number of clusters. Create new namespaces on non-Kf clusters, and Spaces on Kf clusters. You can also manage Spaces by removing the Kf CLI from Space management, if desired. Use `kubectl explain` to [get Kf CRD specs](https://docs.cloud.google.com/migrate/kf/docs/2.6/concepts/kf-dependencies#get_crd_details) to fully manage your product configuration via GitOps.

[ ![Config Management and Kf cluster architecture](https://docs.cloud.google.com/migrate/kf/docs/2.6/images/config-sync-reference-diagram.svg)](https://docs.cloud.google.com/static/migrate/kf/docs/images/config-sync-reference-diagram.svg)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
