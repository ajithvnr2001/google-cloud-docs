---
url: https://docs.cloud.google.com/compute/docs/architecture/regional-views-global-resources/
title: Use regional views for resilient control-plane reads \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:19:48.297404+00:00
---

# Use regional views for resilient control-plane reads  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/architecture/regional-views-global-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Use regional views for resilient control-plane reads Stay organized with collections  Save and categorize content based on your preferences. 

_Control plane dependencies_ are the APIs and metadata services that manage resource definitions in your applications. To build highly available, resilient applications and to automate deployment workflows on Compute Engine, it's critical that you isolate these dependencies. Although global API endpoints provide strong consistency across all regions, any transient latency spike or disruption in the global control plane or in a remote region can delay or block local services.

To build reliable applications that can survive global API disruptions and operate independently within each region, you can configure your services to query regional views of global resources. By using regionalized read-only API endpoints to read resource definitions, your application communicates strictly with the control plane for a specific region. This regional fault isolation ensures your services stay highly available and responsive even across global disruptions.

## Supported resource types

Regional view endpoints are available for the following global resources:

  * **Projects** : the `projectViews` endpoint provides regional read-only access to the global [project resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects).
  * **OS images** : the `imageViews` endpoint provides regional read-only access to global [OS image resources](https://docs.cloud.google.com/compute/docs/images).



## Limitations

Metadata for all global resources is stored in a central global database. When you create, read, update, or delete a resource using standard global API endpoints, Compute Engine requests read from and write directly to the central global database, providing strong consistency.

Regional view endpoints read resource metadata from regional read-only replicas of the central global database. Because changes are copied to these regional replicas asynchronously, you might experience the following behaviors when you query regional views:

  * **Slight delays** : when you create, update, or delete a resource globally, it can take up to 60 seconds for that change to copy over to all regional view endpoints. During this short window, reading from a regional view might return slightly older data.
  * **Automatic fallback** : if you request a resource from a regional view before it finishes copying to that region, Compute Engine automatically reads directly from the central global database so that your request still succeeds.

**Caution:** Don't use regional view endpoints if your application strictly requires updates to be visible immediately across all regions. For real-time resource reads or any write operations (creating, updating, or deleting resources), use the standard global API endpoints.

## Differences between regional view and global API

The following tabs summarize the differences between regional view endpoints and standard global API endpoints for each resource type:

###  Projects 

The following tables summarize the differences between regional view endpoints and standard global API endpoints for the project resource:

Feature | Global API | Regional view API  
---|---|---  
Endpoint | Global | Regional  
Resource URL | `/projects/PROJECT_ID` | `/projects/PROJECT_ID/regions/REGION/projectViews`  
Failure domain | Global | Isolated to the specified region  
Supported methods | Read and write | Read-only (`Get`)  
API quota | Consumes global API read and write quota buckets | Consumes regional API read quota buckets  
Read-after-write consistency | Strongly consistent (reads from central global database) | Eventually consistent (reads from regional replica)  
Quota field behavior | Returns the `quota` array, using cross-regional fanouts to provide real-time quota usage data across all regions and zones. | The `quota` array is excluded from the returned `Project` object. Because the `projectViews` endpoint reads strictly from a regional replica and does not perform cross-region fanouts to collect quota metrics, the `quota` array is not returned at all. For quota configuration limits and accurate real-time usage metrics, query the global [`projects.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/get) endpoint.  
  
###  OS images 

The following tables summarize the differences between regional view endpoints and standard global API endpoints for the OS image resource:

Feature | Global API | Regional view API  
---|---|---  
Endpoint | Global | Regional  
Resource URL | `/projects/PROJECT_ID/global/images` | `/projects/PROJECT_ID/regions/REGION/imageViews`  
Failure domain | Global | Isolated to the specified region  
Supported methods | Read and write | Read-only (`Get` and `List`)  
API quota | Consumes global API read and write quota buckets | Consumes regional API read quota buckets  
Read-after-write consistency | Strongly consistent (reads from central global database) | Eventually consistent (reads from regional replica)  
  
## Pricing

Accessing regional views through regional read-only API endpoints doesn't incur additional charges. Like standard global Compute Engine API requests, requests to regional view endpoints consume your project's [standard API quotas](https://docs.cloud.google.com/compute/api-quota), specifically regional API read quotas, but don't incur additional fees.

## Best practices for high availability

To maximize application resilience, prevent disproportionate control plane load, and avoid creating single-region hotspots, follow these reliability practices when you configure automated systems and client workloads:

  * **Query local regions to reduce the affected area** : send `projectViews` and `imageViews` API requests to the exact region where your client workload or deployment cluster runs. For zonal workloads, use the parent region. Localizing reads ensures that a network disruption or outage in another region doesn't impact your local service.
  * **Detect region strings dynamically** : don't hardcode specific default region strings in shared client libraries or deployment templates. Instead, dynamically detect the workload's current execution region from its local runtime environment so that multi-region failovers work transparently.
  * **Use regional quota isolation against competing workloads** : Compute Engine enforces API rate limits per region. Traffic spikes or runaway scripts in one region consume read quota from that specific region's bucket without impacting API availability or triggering rate limits (`429 Too Many Requests`) in your other critical regions.



## What's next

  * Learn how to [Access global resources regionally for high availability](https://docs.cloud.google.com/compute/docs/architecture/access-global-resources-regionally).
  * Learn how to [Troubleshoot regional views of global resources](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-regional-views-global-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
