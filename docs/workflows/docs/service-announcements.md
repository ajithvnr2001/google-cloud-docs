---
url: https://docs.cloud.google.com/workflows/docs/service-announcements/
title: Service announcements \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:36.879921+00:00
---

# Service announcements  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/service-announcements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Resources ](https://docs.cloud.google.com/workflows/docs/resources)



Send feedback 

#  Service announcements Stay organized with collections  Save and categorize content based on your preferences. 

Learn about Workflows changes such as backward incompatible API changes, product or feature deprecations, mandatory migrations, or potentially disruptive maintenance.

Date published | Description | Instructions  
---|---|---  
January 28, 2025  | Announcement of requirement to access Google Kubernetes Engine clusters through DNS-based endpoints. See [release note](https://docs.cloud.google.com/workflows/docs/release-notes#January_28_2025).  | If you don't use Workflows to access GKE clusters, no action is required from you. For more information, in this document, see the January 28, 2025 section.   
  
## January 28, 2025

Effective **May 2, 2025** , Workflows will not support [HTTP requests](https://docs.cloud.google.com/workflows/docs/http-requests) to the [IP-based endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#ipendpointsconfig) of Google Kubernetes Engine (GKE) cluster control planes. To ensure that your workflow functions as expected, you must access the [DNS-based endpoints](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#dnsendpointconfig). As a best practice, we recommend that instead of making a direct HTTP call, you use the [Kubernetes API connector](https://docs.cloud.google.com/workflows/docs/access-kubernetes-api) in a workflow.

### Scope and impact

If you don't use Workflows to access GKE clusters, no action is required from you.

As of **May 2, 2025** , new workflows are impacted; however, existing workflows will continue to function.

By **August 1, 2025** , any workflows that continue to make HTTP requests to the IP-based endpoints of GKE clusters might not function as expected.

### Required action

Ensure that any workflows that access the IP-based endpoints of GKE clusters are modified to use the DNS-based endpoints instead by **July 21, 2025**. For more information, see [HTTP requests to GKE](https://docs.cloud.google.com/workflows/docs/issues#gke-calls).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
