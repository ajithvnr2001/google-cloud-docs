---
url: https://docs.cloud.google.com/build/docs/locations/
title: Cloud Build locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:57:08.334542+00:00
---

# Cloud Build locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Resources ](https://docs.cloud.google.com/build/docs/resources)



Send feedback 

#  Cloud Build locations Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build supports regional builds in [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) and [default pools](https://docs.cloud.google.com/build/docs/build-push-docker-image).

When selecting a region for your builds, your primary considerations should be latency and availability. You can generally select the region closest to your Cloud Build's users, but you should also consider the location of the [other Google Cloud products and services](https://cloud.google.com/about/locations/#locations) that your build might integrate with. Using services across multiple locations can affect your app's latency, as well as [pricing](https://cloud.google.com/build/pricing).

Cloud Build is available in the following regions:

  * `africa-south1`
  * `asia-east1`
  * `asia-east2`
  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-northeast3`
  * `asia-south1`
  * `asia-south2`
  * `asia-southeast1`
  * `asia-southeast2`
  * `asia-southeast3`
  * `australia-southeast1`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-north1`
  * `europe-north2`
  * `europe-southwest1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `europe-west10`
  * `europe-west12`
  * `me-central1`
  * `me-central2`
  * `me-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `northamerica-south1`
  * `southamerica-east1`
  * `southamerica-west1`
  * `us-central1`
  * `us-east1`
  * `us-east4`
  * `us-east5`
  * `us-south1`
  * `us-west1`
  * `us-west2`
  * `us-west3`
  * `us-west4`

**Important:** Not all machine types are available in all regions for private pools. See [Machine type availability by region](https://docs.cloud.google.com/build/docs/private-pools/private-pool-config-file-schema#expandable-2) for a list of supported regions for each machine type. The machine types available in each region are subject to change.

## Select a region

To run regional builds, specify the region when [starting a build via the command line](https://docs.cloud.google.com/build/docs/running-builds/start-build-command-line-api) or when [creating a build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).

To select a region for your private pool, specify the region when [creating the private pool](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools#creating_a_new_private_pool). Once you create a private pool within a region, you can't move it to another region. When you create a private pool in a specific region, it is managed by Google to be redundantly available across [all the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).

If the [build config](https://docs.cloud.google.com/build/docs/configuring-builds/create-basic-configuration) file associated with your trigger specifies a private pool, then the region you select for your trigger must match the region of the private pool.

If you select `global` as the region for the build trigger, then Cloud Build uses the region specified in the build config file associated with the trigger to run the build. This can either be the region of the private pool, if you specify a private pool in your build config file, or the global default pool if you don't specify a private pool.

## Access Cloud Build resources using regional endpoints

You can use regional endpoints to access resources in Cloud Build. Using regional endpoints lets you run your workloads in a manner that complies with [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) and data sovereignty requirements, where your request traffic is routed directly to the region specified in the endpoint.

Regional endpoints are request endpoints that only allow requests to proceed if the affected resource exists in the location specified by the endpoint. For example, when you use the endpoint `https://cloudBuild.me-central2.rep.googleapis.com` in a create builds request, the request only proceeds if the build config file is located in `me-central2`.

Unlike global endpoints, where requests can be processed in a different location from where the resource resides, regional endpoints guarantee that your requests are processed only within the location specified by the endpoint where the resource resides. Regional endpoints terminate TLS sessions in the location specified by the endpoint for requests received from the Internet, from other Google Cloud resources (such as Compute Engine virtual machines),from on-premise services using VPN or Interconnect, and from Virtual Private Clouds (VPCs).

Regional endpoints guarantee data residency by ensuring that your object's data at rest and in transit doesn't get moved out of the location specified by the endpoint. This guarantee excludes resource metadata, such as object names and bucket IAM policies. For more information, see [Note on Customer Data and Service data](https://docs.cloud.google.com/assured-workloads/docs/data-residency#customer-service-data).

**Note:** Regional endpoints support only HTTPS. HTTP isn't supported.

For information about the steps needed to run a build, see [Running builds](https://docs.cloud.google.com/build/docs/running-builds/submit-build-via-cli-api#running_builds).

**Configure the Google Cloud CLI for use with regional endpoints**

To configure the gcloud CLI for use with regional endpoints, do the following:

  1. Make sure you're using the Google Cloud CLI 402.0.0 or newer.

  2. Set the `api_endpoint_overrides/cloudbuild` property to the regional endpoint that you want to use:
         
         gcloud config set api_endpoint_overrides/cloudbuild https://cloudbuild.LOCATION.rep.googleapis.com/

Alternatively, you can set the `CLOUDSDK_API_ENDPOINT_OVERRIDES_CLOUDBUILD` environment variable to the endpoint:
         
         CLOUDSDK_API_ENDPOINT_OVERRIDES_CLOUDBUILD=https://cloudbuild.LOCATION.rep.googleapis.com/ 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
