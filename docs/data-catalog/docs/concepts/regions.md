---
url: https://docs.cloud.google.com/data-catalog/docs/concepts/regions/
title: Data Catalog regions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:32:53.075032+00:00
---

# Data Catalog regions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/concepts/regions/

Data Catalog is deprecated and will be discontinued on June 1, 2026. For steps to transition your Data Catalog users, workloads, and content to Knowledge Catalog (formerly Dataplex Universal Catalog), see [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Catalog ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Resources ](https://docs.cloud.google.com/data-catalog/docs/resources)



Send feedback 

#  Data Catalog regions Stay organized with collections  Save and categorize content based on your preferences. 

Data Catalog hosts resources in multiple worldwide locations called regions. A region is a specific geographical location where you can access your resources. For more information, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

To decrease network latency, we recommend using the API endpoint for a region that is close to where you plan to use it. For example, if you plan to access Data Catalog from Asia, then you could use the endpoint for Taiwan.

**Note:** For more information about regions that data lineage is supported in, see [About data lineage in Data Catalog](https://docs.cloud.google.com/data-catalog/docs/lineage-data-catalog).

## Supported regions

| Region | Endpoint | Supported resources  
---|---|---|---  
**Africa** |  |  |   
| Johannesburg | `africa-south1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
**Americas** |  |  |   
| Columbus | `us-east5-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Dallas | `us-south1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Iowa | `us-central1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Las Vegas | `us-west4-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Los Angeles | `us-west2-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Mexico | `northamerica-south1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Montréal | `northamerica-northeast1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Northern Virginia | `us-east4-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Oregon | `us-west1-datacatalog.googleapis.com` | Tag templates, user created entries  
| Salt Lake City | `us-west3-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Santiago | `southamerica-west1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| São Paulo | `southamerica-east1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| South Carolina | `us-east1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Toronto | `northamerica-northeast2-datacatalog.googleapis.com` | Tag templates, user created entries  
**Asia Pacific** |  |  |   
| Delhi | `asia-south2-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Hong Kong | `asia-east2-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Jakarta | `asia-southeast2-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Melbourne | `australia-southeast2-datacatalog.googleapis.com` | Tag templates, user created entries  
| Mumbai | `asia-south1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Osaka | `asia-northeast2-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Seoul | `asia-northeast3-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Singapore | `asia-southeast1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Sydney | `australia-southeast1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Taiwan | `asia-east1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Tokyo | `asia-northeast1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
**Europe** |  |  |   
| Belgium | `europe-west1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Berlin | `europe-west10-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Finland | `europe-north1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Frankfurt | `europe-west3-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| London | `europe-west2-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Madrid | `europe-southwest1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Milan | `europe-west8-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Netherlands | `europe-west4-datacatalog.googleapis.com` | Tag templates, user created entries  
| Paris | `europe-west9-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Stockholm | `europe-north2-datacatalog.googleapis.com` | Tag templates, user created entries  
| Turin | `europe-west12-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Warsaw | `europe-central2-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Zurich | `europe-west6-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
**Middle East** |  |  |   
| [Dammam](https://docs.cloud.google.com/docs/dammam-region-access)* | `me-central2-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Doha | `me-central1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
| Tel Aviv | `me-west1-datacatalog.googleapis.com` | Tag templates, BigQuery, user created entries  
  
* Dammam has region-specific access controls described in this [document](https://docs.cloud.google.com/docs/dammam-region-access).

### Multi-regions (eu, us)

Multi-regions such as `eu` and `us` are special regions, where Data Catalog can replicate and serve resources anywhere within them.

Multi-region | Endpoint | Supported resources  
---|---|---  
Asia | `asia-datacatalog.googleapis.com` | Tag templates, user created entries  
European Union | `eu-datacatalog.googleapis.com` | BigQuery, tag templates, user created entries  
United States | `us-datacatalog.googleapis.com` | BigQuery, tag templates, user created entries  
**Important:** Data Catalog **does not** guarantee higher availability or reliability for multi-regions compared to other Google Cloud regions. Multi-regions should be treated just like other [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).

### BigQuery Omni regions

| BigQuery Omni regions | Endpoint | Supported resources  
---|---|---|---  
**AWS** |  |  |   
| AWS - Asia Pacific (Seoul) | `aws-ap-northeast-2-datacatalog.googleapis.com` | BigQuery (except connections)  
| AWS - Asia Pacific (Sydney) | `aws-ap-southeast-2-datacatalog.googleapis.com` | BigQuery (except connections)  
| AWS - Europe (Frankfurt) | `aws-eu-central-1-datacatalog.googleapis.com` | BigQuery (except connections)  
| AWS - Europe (Ireland) | `aws-eu-west-1-datacatalog.googleapis.com` | BigQuery (except connections)  
| AWS - US East (N. Virginia) | `aws-us-east-1-datacatalog.googleapis.com` | BigQuery (except connections)  
| AWS - US West (Oregon) | `aws-us-west-2-datacatalog.googleapis.com` | BigQuery (except connections)  
**Azure** |  |  |   
| Azure - East US 2 (Virginia) | `azure-eastus2-datacatalog.googleapis.com` | BigQuery (except connections)  
  
## Access resources with regional APIs

Resources can be accessed using locational endpoints (see Supported regions). Client libraries let you configure endpoints.

For backward compatibility, regional APIs are supported by the `datacatalog.googleapis.com` endpoint, with some limitations. For more information, see HTTP batch support and gRPC support. We recommend using locational endpoints for regional APIs.

### Non-regional APIs

Although data assets are located in particular regions, Data Catalog search is globally scoped. Non-regional APIs like `SearchCatalog` and `LookupEntry` return assets from all regions, and can be accessed with the `datacatalog.googleapis.com` endpoint.

**Important:** Non-regional APIs can't be used from locational endpoints.

## HTTP batch support

**Note:** Standard [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) use gRPC (and don't support HTTP batch). If you're using these libraries, you can ignore this section.

Data Catalog supports [HTTP batch](https://developers.google.com/classroom/guides/batch), which lets you batch multiple API calls into a single request.

The following are some constraints when using HTTP batch for regional APIs:

  * A HTTP batch request must only include API requests for resources belonging to the same region.
  * You must use locational endpoints when batching regional APIs. `datacatalog.googleapis.com` doesn't support batched regional APIs. Regional and non-regional requests can't be batched together.
  * Non-region dependent APIs (`SearchCatalog` and `LookupEntry`) can be batched together, using the `datacatalog.googleapis.com` endpoint.



If you aren't sure whether you're using HTTP batch, do the following:

  * Check whether you are directly making a HTTP request with a path set to `/batch`, such as `http://datacatalog.googleapis.com/batch`.
  * If you are using the [Google API Client Libraries](https://developers.google.com/api-client-library), check the following:

    * Java: using [BatchRequest](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.batch.BatchRequest) to call APIs.
    * Python: using [BatchHTTP](https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.http.BatchHttpRequest-class.html) request to call APIs.
    * Similar bindings exist for other libraries (see the library specific documentation).



## gRPC support

Locational endpoints are the recommended way to use gRPC for regional APIs.

If you are using manually created gRPC libraries to make calls to the `datacatalog.googleapis.com` endpoint, you must specify a `x-google-request-params` header with a `locations=<region>` tag in the request. The existing [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) that use gRPC internally already have this specified.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
