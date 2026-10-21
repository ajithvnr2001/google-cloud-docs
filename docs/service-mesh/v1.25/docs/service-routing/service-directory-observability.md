---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-directory-observability/
title: Observability and debugging with Service Directory \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:20.412631+00:00
---

# Observability and debugging with Service Directory  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-directory-observability/

You are viewing archived v1.25 Service Mesh documentation.

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
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Observability and debugging with Service Directory

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Deprecated:** Cloud Service Mesh's integration with Service Directory is going to be deprecated. Creating new service binding resources will be disabled.

Cloud Service Mesh's integration with Service Directory introduces new complexities in debugging. Within your business, service consumers and service producers might belong to different teams or organizations. To help you debug such issues, Cloud Service Mesh integrates with Cloud Logging and Cloud Monitoring.

For example:

  * You have a `checkout` service that uses Cloud Service Mesh for application networking.
  * There's a `payment` service in Service Directory that a different team (the _service producer_) owns and maintains.
  * You want to call on the `payment` service from the `checkout` service so you create a new backend service in Cloud Service Mesh. This backend service attaches to the `payment` service using Service Directory for service discovery.



In this model, the service producer might want to delete or modify the `payment`service that is hosted in Service Directory. Because they own the `payment` service, they are permitted to make such changes. But if the `payment` service is deleted, service discovery is broken.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview).

## Logging

When Cloud Service Mesh resolves a backend service that is attached to a Service Directory service, it gets a list of endpoints from Service Directory. If the service has been deleted from Service Directory, Cloud Service Mesh doesn't get any endpoints. In such a case, a log entry is added to Logging. The log entry includes the following information:

  * The backend service name
  * The Service Directory name
  * A message: `Service Directory returned 0 endpoints for this service.`



This information helps you debug issues. You can also set up alerts to be proactively notified.

## Monitoring

Similar to the logging case, Cloud Service Mesh integrates with Monitoring to generate metrics. Cloud Service Mesh adds the following metrics to Monitoring for each backend service:

  * The backend service name
  * The number of endpoints associated with this backend service that are shared with Cloud Service Mesh's clients



Cloud Service Mesh clients are not able to send traffic to backend services that don't have endpoints.

## Google Cloud console

If a Service Directory service is deleted and an attachment to that service exists in the Cloud Service Mesh backend service, the Google Cloud console displays a warning: `The attached Service Directory service could not be found.`

## What's next

  * Learn about [integrating Cloud Service Mesh with Service Directory](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-directory-integration).
  * Learn how to [set up the integration](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/service-directory-integration-setup).
  * Learn about [Service Directory observability](https://docs.cloud.google.com/service-directory/docs/monitoring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
