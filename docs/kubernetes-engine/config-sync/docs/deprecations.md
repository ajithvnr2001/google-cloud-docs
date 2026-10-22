---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/deprecations/
title: Config Sync feature deprecations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:53.318102+00:00
---

# Config Sync feature deprecations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/deprecations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/resources)



Send feedback 

#  Config Sync feature deprecations Stay organized with collections  Save and categorize content based on your preferences. 

The [Google Cloud Platform Terms of Service (section "Discontinuation of Services")](https://docs.cloud.google.com/terms) defines the deprecation policy that applies to Config Sync. The [deprecation policy](https://docs.cloud.google.com/terms/deprecation) only applies to the services, features, or products listed therein. 

After a service, feature, or product is officially deprecated, it continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the service is scheduled for shutdown. 

The following table lists deprecated Config Sync features and their related shutdown schedules:

Feature | Deprecated date | Shutdown date | Details  
---|---|---|---  
[`spec.git` fields of the `ConfigManagement` API](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields#configuration_for_git_repositories) | May 15, 2023 | May, 2024 | The use of `spec.git` fields in a `ConfigManagement` object to manage Git repository configurations is deprecated. The `RootSync` API offers the same functionality, along with additional features. For information about migration, see [Migrate your `ConfigManagement` object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-multi-repo).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
