---
url: https://docs.cloud.google.com/bigtable/docs/regional-endpoints/
title: Regional and global endpoints \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:13.449223+00:00
---

# Regional and global endpoints  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Regional and global endpoints

This page describes Bigtable endpoints, explains what you should consider before using them, and shows how to set an endpoint using the [`cbt` CLI](https://docs.cloud.google.com/bigtable/docs/cbt-overview).

To send requests to Bigtable, you can use either a global or regional service endpoint. Regional endpoints for Bigtable ensure that an instance's data is stored and processed in the Bigtable region where the data resides. You might need to use regional endpoints for Bigtable in a specific geographic region in support of your project's security and compliance needs.

Before you read this document, familiarize yourself with [Instances, clusters, and nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes) and [App profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles).

Key concepts include the following:

  * **[Service endpoint](https://docs.cloud.google.com/apis/design/glossary#api_service_endpoint)** : a base URL that specifies the network address of an API service. Bigtable has both global and regional endpoints.

  * **Global endpoint** : lets Bigtable store and route the data in a Bigtable instance to any region that contains one of the instance's clusters. The global endpoint for the Cloud Bigtable API (Data API) is `bigtable.googleapis.com`. The default Data API endpoint accesses the global endpoint.

  * **Regional endpoint** : enforces regional restrictions, ensuring that Bigtable stores and processes data in a specified region. You can use regional endpoints only with the Cloud Bigtable API (Data API). Bigtable doesn't support regional endpoints for the Cloud Bigtable Admin API.




## When to use regional endpoints

The benefit of using a Bigtable regional endpoint over a global endpoint is that the regional endpoint provides regional isolation and protection to meet security, compliance, and regulatory requirements.

Regional endpoints, however, don't support [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) or the Cloud Bigtable Admin API. In addition, you can't configure Bigtable to achieve a monthly uptime percentage of >=99.999% when you use regional endpoints. For more information, see the Considerations to use a regional endpoint section of this document.

## When to use global endpoints

Use a global endpoint in the following cases:

  * You don't have regional restriction requirements that require you to use a regional endpoint.
  * You need to use Data Boost.
  * You need to use the Cloud Bigtable Admin API.
  * You require a monthly uptime percentage of at least 99.999%.



## Considerations to use a regional endpoint

If you use a regional endpoint, then consider the following factors:

  * Cluster locations
  * App profiles
  * Replication
  * Availability



### Cluster locations

Before you can use a regional endpoint, you must create an instance with at least one cluster in the region where you want to isolate your data. Bigtable regional endpoints are available in select Bigtable regions. For a list of available regions, see [Regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

You can only use a regional endpoint that belongs to the region where you want to isolate your data. For example, if a cluster is in the `us-central1` region, then you can't use `bigtable.us-west1.rep.googleapis.com` to serve requests.

If you attempt to use a regional endpoint to access a cluster that's in a different region, Bigtable rejects the request with a `FAILED_PRECONDITION` error message stating that no clusters are accessible using the specified cluster and endpoint. For more information about this error message, see [Bigtable status codes](https://docs.cloud.google.com/bigtable/docs/status-codes).

### App profiles

After you set a regional endpoint, you must use an app profile that's configured to route requests to a cluster in the endpoint's region.

If you attempt to use an app profile configured to send writes only to a cluster (using single-cluster routing) or clusters in a different region from the endpoint (using multi-cluster routing), then you receive the `FAILED_PRECONDITION` error message. For more information about cluster routing, see [Routing policy](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing).

If you use an app profile that's configured to route to any cluster in an instance for high availability (HA), and you also use a regional endpoint, then the regional endpoint ensures that all requests are routed only to clusters in its region, even if the instance has clusters in other regions. [Automatic failover](https://docs.cloud.google.com/bigtable/docs/failovers#automatic) is constrained, so requests are only served from clusters in the region of the endpoint.

Consider an example where you are sending requests using an app profile configured for multi-cluster routing to instance that has clusters in `us-west1-a` (Oregon), `us-west1-b` (Oregon), and `us-central1-a` (Iowa). If you send these requests to the `bigtable.us-central1.rep.googleapis.com` regional endpoint, then all requests are served by `us-central1-a` even if you don't reconfigure the app profile. Requests that can't be served by `us-central1-a` fail.

### Replication

Regional endpoints don't affect or prevent replication. If you configure a regional endpoint in Region A, and then you add a cluster to your instance in Region B, your data is replicated to Region B just as if you used the global endpoint.

To avoid replicating data to another region, create clusters only in the intended region.

To prevent users in your organization from adding clusters outside of the endpoint region, you can [set an organization policy that uses location constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).

### Availability

When you use regional endpoints, you can't configure Bigtable to achieve a monthly uptime percentage of >=99.999%. A monthly uptime of >=99.999% requires [automatic failover](https://docs.cloud.google.com/bigtable/docs/managing-failovers#automatic) of requests over regional boundaries. A regional endpoint prevents automatic failover because it confines all requests to a single region. For more information about monthly uptime percentages, see the [Bigtable service level agreement (SLA)](https://cloud.google.com/bigtable/sla).

## Regional endpoint semantics

A regional endpoint follows the format `bigtable.REGION.rep.googleapis.com`, where REGION is a Google Cloud region name, such as `northamerica-northeast2`.

For example, if you want to isolate your data in the Iowa region, because the region name for Iowa is `us-central1`, the regional endpoint URL for the Iowa region is `bigtable.us-central1.rep.googleapis.com`.

## Specify a regional endpoint

You can specify a Bigtable regional endpoint using the `cbt` CLI, or the [Cloud Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries).

###  cbt 

To specify a regional endpoint and override the global endpoint using the `cbt` CLI, you can use the `--data-endpoint` option in your request, or you can add the following to your ~/.cbtrc file. For additional information on creating a ~/.cbtrc file, see the [cbt CLI reference](https://docs.cloud.google.com/bigtable/docs/cbt-reference).
    
    
    data-endpoint = https://bigtable.REGION.rep.googleapis.com/
    

Replace `REGION` with the region where you want to set a regional endpoint, such as `us-central1` or `europe-west1`.

For example, to configure the regional endpoint as `us-central1` add this to the ~/.cbtrc file:
    
    
    data-endpoint = https://bigtable.us-central1.rep.googleapis.com/
    

## Specify the global endpoint

###  cbt 

To specify the global sendpoint, send your request without using the `--data-endpoint` option. If you previously added a `data-endpoint` line to your ~/.cbtrc file, delete it.

## Restrict global API endpoint usage

To help enforce the use of regional endpoints, use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

## What's next

  * [Review access control with IAM.](https://docs.cloud.google.com/bigtable/docs/access-control)
  * [Learn how to create and manage tags.](https://docs.cloud.google.com/bigtable/docs/tags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
