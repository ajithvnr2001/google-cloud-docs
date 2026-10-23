---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rep/
title: Use Cloud SQL regional endpoints \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:49.152196+00:00
---

# Use Cloud SQL regional endpoints  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rep/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use Cloud SQL regional endpoints Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rep "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rep "View this page for the SQL Server database engine")

## Overview

Cloud SQL supports regional endpoints for Admin APIs. This feature enhances data residency for data in-transit and improves regional reliability.

There are two options for routing Cloud SQL Admin API requests:

  * Through the global endpoint, which routes the requests through a global load balancer before they reach the appropriate region.
  * Through regional endpoints, which let you direct your API calls to a region-specific endpoint where they're handled by that region's frontend infrastructure. This improves data locality and helps meet strict compliance expectations.

Endpoint Type | URL Format | Example | Use Case  
---|---|---|---  
Global | `sqladmin.googleapis.com` | `sqladmin.googleapis.com` | Managing resources globally across multiple regions.  
Regional | `sqladmin.{region}.rep.googleapis.com` | `sqladmin.us-central1.rep.googleapis.com` | Provides strict data residency at the frontend level.  
**Note:** Multi-regional endpoints such as `sqladmin.us.rep.googleapis.com` are not supported at this time.

## Supported regions

Region | API  
---|---  
africa-south1 | `sqladmin.africa-south1.rep.googleapis.com`  
asia-east1 | `sqladmin.asia-east1.rep.googleapis.com`  
asia-east2 | `sqladmin.asia-east2.rep.googleapis.com`  
asia-northeast1 | `sqladmin.asia-northeast1.rep.googleapis.com`  
asia-northeast2 | `sqladmin.asia-northeast2.rep.googleapis.com`  
asia-northeast3 | `sqladmin.asia-northeast3.rep.googleapis.com`  
asia-south1 | `sqladmin.asia-south1.rep.googleapis.com`  
asia-south2 | `sqladmin.asia-south2.rep.googleapis.com`  
asia-southeast1 | `sqladmin.asia-southeast1.rep.googleapis.com`  
asia-southeast2 | `sqladmin.asia-southeast2.rep.googleapis.com`  
asia-southeast3 | `sqladmin.asia-southeast3.rep.googleapis.com`  
australia-southeast1 | `sqladmin.australia-southeast1.rep.googleapis.com`  
australia-southeast2 | `sqladmin.australia-southeast2.rep.googleapis.com`  
europe-central2 | `sqladmin.europe-central2.rep.googleapis.com`  
europe-north1 | `sqladmin.europe-north1.rep.googleapis.com`  
europe-north2 | `sqladmin.europe-north2.rep.googleapis.com`  
europe-southwest1 | `sqladmin.europe-southwest1.rep.googleapis.com`  
europe-west1 | `sqladmin.europe-west1.rep.googleapis.com`  
europe-west10 | `sqladmin.europe-west10.rep.googleapis.com`  
europe-west12 | `sqladmin.europe-west12.rep.googleapis.com`  
europe-west2 | `sqladmin.europe-west2.rep.googleapis.com`  
europe-west3 | `sqladmin.europe-west3.rep.googleapis.com`  
europe-west4 | `sqladmin.europe-west4.rep.googleapis.com`  
europe-west6 | `sqladmin.europe-west6.rep.googleapis.com`  
europe-west8 | `sqladmin.europe-west8.rep.googleapis.com`  
europe-west9 | `sqladmin.europe-west9.rep.googleapis.com`  
me-central1 | `sqladmin.me-central1.rep.googleapis.com`  
me-central2 | `sqladmin.me-central2.rep.googleapis.com`  
me-west1 | `sqladmin.me-west1.rep.googleapis.com`  
northamerica-northeast1 | `sqladmin.northamerica-northeast1.rep.googleapis.com`  
northamerica-northeast2 | `sqladmin.northamerica-northeast2.rep.googleapis.com`  
northamerica-south1 | `sqladmin.northamerica-south1.rep.googleapis.com`  
southamerica-east1 | `sqladmin.southamerica-east1.rep.googleapis.com`  
southamerica-west1 | `sqladmin.southamerica-west1.rep.googleapis.com`  
us-central1 | `sqladmin.us-central1.rep.googleapis.com`  
us-central2 | `sqladmin.us-central2.rep.googleapis.com`  
us-east1 | `sqladmin.us-east1.rep.googleapis.com`  
us-east4 | `sqladmin.us-east4.rep.googleapis.com`  
us-east5 | `sqladmin.us-east5.rep.googleapis.com`  
us-south1 | `sqladmin.us-south1.rep.googleapis.com`  
us-west1 | `sqladmin.us-west1.rep.googleapis.com`  
us-west2 | `sqladmin.us-west2.rep.googleapis.com`  
us-west3 | `sqladmin.us-west3.rep.googleapis.com`  
us-west4 | `sqladmin.us-west4.rep.googleapis.com`  
us-west8 | `sqladmin.us-west8.rep.googleapis.com`  
  
## Regional endpoint differences from the global endpoint

When migrating to regional endpoints, be aware of the following behavior changes compared to the global endpoint:

### Strict region matching

Regional endpoints enforce strict region boundaries. If you send an API request such as `INSERT`, `UPDATE`, `PATCH`, `DELETE`, or `GET` to a regional endpoint, then the target resource defined in your request body must match the region of the endpoint.

**Behavior** : If the region in the endpoint and the region in the request don't match, then the request is rejected with a 4xx error.

### Instance.List behavior

When using the `Instance.List` API:

  * The **global endpoint** queries and returns instances across all regions where the user has resources.
  * A **regional endpoint** only lists instances that exist within that specific region.



**v1 example** (Regional):
    
    
    GET https://sqladmin.{region}.rep.googleapis.com/v1/projects/{project}/instances
    

**v1beta4 example** (Regional):
    
    
    GET https://sqladmin.{region}.rep.googleapis.com/sql/v1beta4/projects/{project}/instances
    

### Backups and disaster recovery

For backups, regional endpoints behave the same way as the global endpoint, with no change in behavior, which means that you can use them to access backups for disaster recovery (DR) scenarios involving cross-region restores,

However, because backups are treated as global resources to ensure that they can be restored across regions during a single-region outage, we strongly recommend that you use the global endpoint rather than regional endpoints for accessing backups.

**Global API example:**
    
    
    GET https://sqladmin.googleapis.com/v1/projects/{project}/backups
    

**Regional API example:**
    
    
    GET https://sqladmin.{region}.rep.googleapis.com/v1/projects/{project}/backups
    

**Note:** `BackupRuns`, however, are served from the regional endpoint of each instance's region, not from the global endpoint.

## Use regional endpoints in API requests

Authentication methods (such as Bearer tokens), API paths, request bodies, and API versions remain completely unchanged when using regional endpoints.

To make a request to a regional endpoint using `curl` or a custom HTTP client, replace the global base URL (`sqladmin.googleapis.com`) with a specific regional base URL (like `sqladmin.us-west1.rep.googleapis.com`).

### Examples using `curl`

**Global API example**
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" https://sqladmin.googleapis.com/v1/projects/{project}/instances
    

**Regional API example** (us-central1)
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" https://sqladmin.us-central1.rep.googleapis.com/v1/projects/{project}/instances
    

## Use manual overrides for [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and Terraform

You can use Cloud SQL regional endpoints with the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and Terraform by using a manual configuration override that explicitly directs the tool to your specific regional URL (`sqladmin.{region}.rep.googleapis.com`).

Example [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) override:
    
    
    gcloud config set api_endpoint_overrides/sql https://sqladmin.us-central1.rep.googleapis.com/
    

Example Terraform override:
    
    
    export GOOGLE_SQL_CUSTOM_ENDPOINT="https://sqladmin.us-central1.rep.googleapis.com/sql"
    

## Limitations

Cloud SQL regional endpoints has the following limitations.

  * **Limited network support** : access to a Cloud SQL Admin API regional endpoint is restricted to public network connections only. You can't connect to a regional endpoint from a Virtual Private Cloud network or a private network connection.

  * **No multi-regional support** : multi-regional endpoints, which are endpoints that are include multiple regions (for example, `us.rep.googleapis.com`), aren't supported.

  * **Backend dependencies** : although the frontend of the Cloud SQL Admin API is regionalized, certain backend dependencies of the API and metadata can still rely on global components.

  * **Manual tooling configuration** : built-in support isn't provided for the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and Terraform. You must use configuration overrides to use regional endpoints with the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and Terraform.

  * **Google Cloud console and Kubernetes Config Connector support** : there isn't support for regional endpoints within the Google Cloud console or [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview).

  * **Backup and recovery** : backups are treated as global resources to help ensure that they can be restored across regions. While you can create backups using regional endpoints for disaster recovery, we recommend that you continue to use the global endpoint for creating and restoring backups to avoid complications.

  * **Cloud SQL remote MCP server doesn't support regional endpoints** : you can't use regional endpoints to access the remote Cloud SQL MCP server. Connect using the global endpoint, `https://sqladmin.googleapis.com/mcp`. For more information about the remote Cloud SQL MCP server, see [Use the Cloud SQL remote MCP server](https://docs.cloud.google.com/sql/docs/mysql/use-cloudsql-mcp).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
