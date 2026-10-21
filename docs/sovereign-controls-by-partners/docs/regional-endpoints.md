---
url: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/regional-endpoints/
title: Accessing regional API endpoints \u00a0|\u00a0 Sovereign Controls by Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:36.539825+00:00
---

# Accessing regional API endpoints  |  Sovereign Controls by Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sovereign-controls-by-partners/docs/regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sovereign Controls by Partners ](https://docs.cloud.google.com/sovereign-controls-by-partners/docs)



Send feedback 

#  Accessing regional API endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use regional API endpoints (_regional endpoints_) in Google Cloud, which are available for the `me-central2` (KSA) region.

Regional endpoints provide in-transit data residency capabilities by routing and serving traffic in the same [Google Cloud region](https://cloud.google.com/about/locations) as the client. When a client calls a service using a regional endpoint, the client's TLS session terminates in the region indicated in the endpoint name. As a result, regional endpoints should only be used for workloads that have no dependencies outside of a single region or jurisdiction.

You can connect over the internet to public regional endpoints. For internet ingress traffic, these endpoints use best-effort routing to keep in-transit traffic local to the region (or jurisdiction) because they don't use the global [Google Front End (GFE)](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service). Instead, they resolve to IP addresses that are announced only on the peering points closest to the selected region.

For example, a data engineer working in KSA can configure their client to use BigQuery in the `me-central2` region (Dammam) by using the regional service endpoint `bigquery.me-central2.rep.googleapis.com`. Traffic is routed using [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier), and the TLS session from their client will be terminated in `me-central2`.

In this scenario, the public VIP corresponding to the regional service endpoint will originate from an IP prefix announced by Google on the region's peering points. Thus, if the user is connected to a local ISP in KSA, traffic can be routed within its jurisdiction.

**Note:** Regional endpoints are only available for supported Google Cloud services that provide region-specific service endpoints and their associated configuration options.

## Regional endpoint format

Regional endpoints use the following format:
    
    
    SERVICE_NAME.REGION.rep.googleapis.com

The placeholder values are defined as follows:

  * SERVICE_NAME: A supported service endpoint name, such as `bigquery`.
  * REGION: A supported Google Cloud region, such as `me-central2`.



The following example is a complete regional endpoint for BigQuery:
    
    
    bigquery.me-central2.rep.googleapis.com

## Supported regions and services

Regional endpoints are supported in the following regions:

Region name | Location  
---|---  
`me-central2` | Dammam, Kingdom of Saudi Arabia (KSA)  
  
Regional endpoints are supported by the following services:

Service name | Regional endpoint  
---|---  
[Artifact Registry](https://docs.cloud.google.com/artifact-registry) |  `artifactregistry.me-central2.rep.googleapis.com  
apt.me-central2.rep.pkg.dev  
docker.me-central2.rep.pkg.dev  
go.me-central2.rep.pkg.dev  
googet.me-central2.rep.pkg.dev  
kfp.me-central2.rep.pkg.dev  
maven.me-central2.rep.pkg.dev  
npm.me-central2.rep.pkg.dev  
python.me-central2.rep.pkg.dev  
yum.me-central2.rep.pkg.dev  
`  
[BigQuery](https://docs.cloud.google.com/bigquery) |  `bigquery.me-central2.rep.googleapis.com  
bigquerydatatransfer.me-central2.rep.googleapis.com bigquerymigration.me-central2.rep.googleapis.com bigqueryreservation.me-central2.rep.googleapis.com  
bigquerystorage.me-central2.rep.googleapis.com `  
[Bigtable](https://docs.cloud.google.com/bigtable) |  `bigtable.me-central2.rep.googleapis.com`  
[Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms) |  `cloudkms.me-central2.rep.googleapis.com`  
[Cloud Logging](https://docs.cloud.google.com/logging) |  `logging.me-central2.rep.googleapis.com`  
[Spanner](https://docs.cloud.google.com/spanner) |  `spanner.me-central2.rep.googleapis.com`  
[Cloud Storage](https://docs.cloud.google.com/storage) |  `storage.me-central2.rep.googleapis.com`  
[Dataflow](https://docs.cloud.google.com/dataflow) |  `dataflow.me-central2.rep.googleapis.com`  
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc) |  `dataproc.me-central2.rep.googleapis.com`  
[Pub/Sub](https://docs.cloud.google.com/pubsub) |  `pubsub.me-central2.rep.googleapis.com`  
  
## Configuring a client to access regional endpoints from the public internet

To use regional endpoints from the public internet, you must first configure your client (such as the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) or a [Google Cloud SDK client library](https://docs.cloud.google.com/apis/docs/cloud-client-libraries)) to connect to a specific regional endpoint.

### Configure the gcloud CLI

By default, the gcloud CLI uses global service endpoints, such as `bigquery.googleapis.com`. To use a regional service endpoint, you must configure the gcloud CLI to use them by completing the following steps.

  1. If a supported service has not yet been enabled, enable it using the following command:
         
         gcloud services enable SERVICE_NAME

Replace SERVICE_NAME with the name of a supported service you want to use. For example:
         
         gcloud services enable cloudkms

  2. To use a regional service endpoint, you must configure the gcloud CLI by using the [`gcloud config set api_endpoint_overrides`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/endpoint-override) command:
         
         gcloud config set api_endpoint_overrides/SERVICE_NAME REGIONAL_API_URL

Replace the following values with your own:

     * SERVICE_NAME: The name of the supported service you want to use. For example: `cloudkms`
     * REGIONAL_API_URL: The URL for the specific endpoint. For example:
           
           https://SERVICE_NAME.REGION_NAME.rep.googleapis.com/SERVICE_NAME/API_VERSION

Replace the following values with your own:

       * REGION_NAME: The name of the required Google Cloud region. For example: `me-central2`
       * API_VERSION: The API version of the service you want to use. For example: `v1`. **Note** : Some services may not require this parameter.

The following is an example REGIONAL_API_URL value:
    
    https://cloudkms.me-central2.rep.googleapis.com/cloudkms/v1

Put together, the following is an example `gcloud config set api_endpoint_overrides` command for Cloud KMS:
    
    gcloud config set api_endpoint_overrides/cloudkms https://cloudkms.me-central2.rep.googleapis.com/cloudkms/v1




Now that gcloud CLI has been configured to use a regional service endpoint, future commands will use it as the default instead of the global service endpoint.

### Configure Google Cloud SDK client libraries

By default, Google Cloud SDK client libraries use global service endpoints, such as `pubsub.googleapis.com`. To use a regional service endpoint, you must configure Google Cloud SDK client libraries to use them.

#### Python

Set the `api_endpoint` parameter in the [`ClientOptions` class](https://googleapis.dev/python/google-api-core/latest/client_options.html) of the `google-api-core` package:
    
    
    from google.api_core.client_options import ClientOptions
    
    options = ClientOptions(api_endpoint = "pubsub.me-central2.rep.googleapis.com")
    client = pubsub_v1.PublisherClient(client_options=options)
    
    // Alternatively
    client = pubsub_v1.PublisherClient(client_options={"api_endpoint": "pubsub.me-central2.rep.googleapis.com")

#### Java

Use the `newBuilder` method of the [`ImageAnnotatorSettings` class](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p2beta1.ImageAnnotatorSettings) in the `com.google.cloud.vision` package:
    
    
    ImageAnnotatorSettings settings = ImageAnnotatorSettings.newBuilder()
      .setEndpoint("pubsub.me-central2.rep.googleapis.com")
      .build();
    ImageAnnotatorClient client = ImageAnnotatorClient.create(settings);

#### Go

Use the `WithEndpoint` function in the [`ClientOptions` package](https://godoc.org/google.golang.org/api/option) of the `api` package:
    
    
    client, err := pubsub.NewClient(ctx, projID,
        option.WithEndpoint("pubsub.me-central2.rep.googleapis.com"), // Override endpoint

#### .NET

Set the `Endpoint` property in the client's [`ClientBuilder` class](https://docs.cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint) in the `Google.Cloud` package of the library you are using:
    
    
    string region = "me-central2";
    var client = new DatasetServiceClientBuilder
    {
        Endpoint = $"pubsub.{region}.rep.googleapis.com"
    }.Build();

## Restrict global API endpoint usage

To help enforce the use of regional endpoints, use the `constraints/gcp.restrictEndpointUsage` organization policy constraint to block requests to the global API endpoint. For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
