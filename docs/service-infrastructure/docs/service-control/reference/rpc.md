---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/
title: Service Control API \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:34.094543+00:00
---

# Service Control API  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Service Control API Stay organized with collections  Save and categorize content based on your preferences. 

Provides admission control and telemetry reporting for services integrated with Service Infrastructure.

## Service: servicecontrol.googleapis.com

The Service name `servicecontrol.googleapis.com` is needed to create RPC client stubs.

## `[google.api.servicecontrol.v1.QuotaController](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaController)`

Methods  
---  
``[AllocateQuota](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaController.AllocateQuota)`` |  Attempts to allocate quota for the specified consumer.  
  
## `[google.api.servicecontrol.v1.ServiceController](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ServiceController)`

Methods  
---  
``[Check](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ServiceController.Check)`` |  Checks whether an operation on a service should be allowed to proceed based on the configuration of the service and related policies.  
``[Report](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ServiceController.Report)`` |  Reports operation results to Google Service Control, such as logs and metrics.  
  
## `[google.api.servicecontrol.v2.ServiceController](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ServiceController)`

Methods  
---  
``[Check](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ServiceController.Check)`` |  This method provides admission control for services that are integrated with [Service Infrastructure](https://cloud.google.com/service-infrastructure).  
``[Report](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ServiceController.Report)`` |  This method provides telemetry reporting for services that are integrated with [Service Infrastructure](https://cloud.google.com/service-infrastructure).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
