---
url: https://docs.cloud.google.com/fault-injection-testing/set-up-experiment/
title: Choose setup instructions for a fault type \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:14.243976+00:00
---

# Choose setup instructions for a fault type  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/set-up-experiment/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Choose setup instructions for a fault type Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page links to instructions for creating an experiment for specific faults. An experiment is an instance of a fault injection experiment against your target resources, which should fail because of the fault.

To set up a new experiment, you'll create an experiment template, which defines the fault to be injected and the target resources. Choose from the following pages based on the fault to inject.

  * [Fail Compute](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/fail-compute) \- simulate the unavailability of GKE or Compute Engine [compute](https://docs.cloud.google.com/compute/docs/overview) resources.
  * [Degrade Application Traffic](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/application-traffic) \- simulate traffic degradation through a layer 7 [load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).
  * [Failover Cloud SQL](https://docs.cloud.google.com/fault-injection-testing/experiment-setup/cloud-sql) \- fail an HA-enabled [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/high-availability) database from primary to standby.



These faults are designed to restrict the scope of the experiment to a single project's resources in a single region or narrower. The experiment won't affect a wider scope than what is intended. However, these faults cause real failures to the targeted resources in its environment.

By targeting infrastructure components such as a Cloud SQL database or an Application Load Balancer, as well as other components that will be supported in the future, you can reasonably approximate a zone or region failure in the context of your own application.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
