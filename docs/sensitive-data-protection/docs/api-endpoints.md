---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints/
title: Global and regional endpoints for Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:16.436239+00:00
---

# Global and regional endpoints for Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/api-endpoints/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Global and regional endpoints for Sensitive Data Protection Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the different types of API endpoints available with Sensitive Data Protection. This document also provides points to consider when deciding which endpoint type to use in your Sensitive Data Protection requests. For general information about the different types of API endpoints, see [Google Cloud API endpoint overview](https://docs.cloud.google.com/docs/security/compliance/endpoints).

An API endpoint (or _service endpoint_) is a base URL that specifies the network address of a Google Cloud API service like Sensitive Data Protection. Sensitive Data Protection has global and regional endpoints.

## Global API endpoint

The global endpoint of Sensitive Data Protection is `dlp.googleapis.com`.

Globally scoped endpoints provide highly available service endpoints that terminate the TLS session as close to the client as possible, which minimizes latency when serving API calls from a dispersed client population over the internet.

When you send a request to a global endpoint, you can specify the location where you want to process the request.

### Requests to a global endpoint with no location specified

If you don't specify a location in your request—or if you specify the `global` region—then the request is processed in the `global` region. For example, if you send a `POST` request to the following URL, the request is sent to the global endpoint and processed in the `global` region.
    
    
    https://dlp.googleapis.com/v2/projects/example-project/content:inspect
    

### Requests to a global endpoint with a location specified

If you specify a location in your request to a global endpoint, the request is sent to the global endpoint and processed in the region or multi-region that you specified. For example, if you send a `POST` request to the following URL, the request is sent to the global endpoint and processed in the `us-west1` region.
    
    
    https://dlp.googleapis.com/v2/projects/example-project/locations/us-west1/content:inspect
    

There is no guarantee that the data in transit remains in the processing region that you specified. If you aren't required to keep in-transit data within a specific region, then calling the global endpoint in this manner is sufficient.

## Regional API endpoints

Regional endpoints let you keep in-transit data within a specific region. A regional endpoint specifies the location as a subdomain—for example, `dlp.us-west1.rep.googleapis.com`.

A regional endpoint for Sensitive Data Protection follows this format:
    
    
    dlp.REGION.rep.googleapis.com
    

Replace `REGION` with a [regional endpoint available for Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/locations#regional-endpoints).

Regional endpoints terminate TLS sessions in the location specified by the endpoint for requests received from the public internet or from private connectivity.

Regional endpoints guarantee [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) by ensuring that your data at rest, in use, and in transit isn't moved out of the location specified by the endpoint. This guarantee excludes Service Data. For more information, see [Note on Customer Data and Service Data](https://docs.cloud.google.com/assured-workloads/docs/data-residency#customer-service-data).

## Choose between the global and regional endpoints

If your organization is required to keep data at rest, in use, and in transit within a specific region, then you must use regional endpoints. If you aren't required to keep in-transit data within a specific region, then you can use global endpoints.

Regional endpoints are supported by a limited number of locations. For a full list of regions and multi-regions where Sensitive Data Protection is available, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).

The following sections describe common use cases for each type of endpoint.

### When to use regional endpoints

The following are some common use cases:

  * **Enforce strict geographical data residency** : Ensure that customer data at rest, in use, and in transit never leaves a specific region to satisfy local data sovereignty laws and regulations.
  * **Comply with regulated industry frameworks** : Fulfill compliance requirements (such as FedRAMP, HIPAA, or financial regulations) when working with Assured Workloads and organizational endpoint restrictions.
  * **Co-locate API processing with cloud resources** : Route inspection traffic to local endpoint infrastructure within the same region where your Cloud Storage buckets or Compute Engine instances reside.



### When to use the global endpoint

The following are some common use cases:

  * **Minimize latency for geographically dispersed clients** : Allow Google's global edge infrastructure to terminate TLS connections as close to the client as possible for globally distributed workloads.
  * **Handle high-throughput API workloads** : Use higher default request quotas allocated to the global endpoint when traffic exceeds regional endpoint limits.
  * **Process multi-region or global datasets** : Inspect payloads that don't have single-region data residency constraints.



### Architectural considerations

Consider the following factors when configuring endpoints:

  * Regional endpoints are supported by a limited number of locations. For a full list of regions and multi-regions where Sensitive Data Protection is available, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).

  * Sensitive Data Protection has separate sets of [quotas](https://docs.cloud.google.com/sensitive-data-protection/limits#request-quotas) for the following:

    * Requests to the global endpoint with no location specified (processed in the `global` region)
    * Requests to the global endpoint where a processing location is specified (processed in the specified region)
    * Requests to regional endpoints

The quotas for regional endpoints are lower than the quotas for the other two.

  * If your client application is configured to use global endpoints and you want to start using regional endpoints, you need to configure your client application to specify the region or multi-region in the subdomain and the path of each hostname that you use in your requests. For more information, see [Specify a region in a request to a regional endpoint](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location#specify-region-rep).




## Restrict global API endpoint usage

To help enforce the use of regional endpoints, use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage) in the Assured Workloads documentation.

## What's next

  * Refer to a list of [locations where Sensitive Data Protection is available](https://docs.cloud.google.com/sensitive-data-protection/docs/locations).
  * Learn how to [specify a location in your request](https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
