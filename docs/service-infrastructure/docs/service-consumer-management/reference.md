---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/
title: Overview \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:48:46.430507+00:00
---

# Overview  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

## Service Consumer Management API

The Service Consumer Management API allows the owner or administrator of a _service_ to manage the _consumers_ of the service.

### Which API to use

The Service Consumer Management API is part of a larger family of APIs related to service infrastructure.

To control the behavior of a service for a specific consumer or set of consumers, use this API.

To control the default behavior of a service for all of its consumers, use the Service Management API.

To manage the relationships of a single consumer to all of the services that it consumes, use the Service Usage API. The Service Consumer Management API manages these relationships from the perspective of the service, whereas the Service Usage API manages the same relationships from the perspective of the consumer.

### Concepts

A **service** is a network service that typically provides some REST or RPC APIs. Services are managed by the Service Management API.

A **consumer** is a resource defined by the Cloud Resource Manager API: a [project](https://support.google.com/cloud/answer/6158853), folder, or organization. Some capabilities in the Service Consumer Management API apply only to projects.

A **service owner** is a user authorized to take management actions on the service, typically by having permissions on the _producer project_ associated with the service. The Service Consumer Management API is intended to be used by service owners.

A service can be **enabled** on a consumer through the Service Usage API or through the [Google Cloud Console](https://console.cloud.google.com). Enabling an API establishes a relationship between the consumer and the service. Once the service is enabled for the consumer, clients can send traffic to the service that is associated with that consumer (using an API key, or an OAuth token). The consumer also becomes searchable by the service owner through the Service Consumer Management API.

A service defines some quota configuration structure for its consumers, including **metrics** , which define the quantities that are measured for quota enforcement, and **limits** , which limit how much of those metric-defined quotas may be consumed by a consumer within a given time interval (rate limits) or in total (allocation limits).

The Service Consumer Management API allows a service owner to **override** the default values of quota limits for a particular consumer, to raise (or lower) the available quota for that consumer.

### Resource Names

The SCM API operates on state associated with the relationship between a service and a consumer. Each such relationship is a resource, with a name of the form:
    
    
    services/{service_name}/{consumer_collection}/{consumer_id}
    

The `service_name` is the DNS name of the service [as defined by the Service Management API](https://cloud.google.com/service-infrastructure/docs/service-management/getting-started), such as `serviceusage.googleapis.com`.

The `consumer_collection` can be `projects`, `folders`, or `organizations`:
    
    
    services/{service_name}/projects/{project_id}
    services/{service_name}/folders/{folder_id}
    services/{service_name}/organizations/{organization_id}
    

All other resources in the Service Consumer Management API are subresources under this relationship resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
