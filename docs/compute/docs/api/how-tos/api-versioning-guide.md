---
url: https://docs.cloud.google.com/compute/docs/api/how-tos/api-versioning-guide/
title: Compute Engine versioning guide: APIs, client libraries, and tools \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:10.924409+00:00
---

# Compute Engine versioning guide: APIs, client libraries, and tools  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/api/how-tos/api-versioning-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Compute Engine versioning guide: APIs, client libraries, and tools Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how Compute Engine manages versions across REST APIs, client libraries, and the `gcloud` command-line tool. It describes the difference between channel-based versioning (CBV) and interface-based versioning (IBV), while focusing primarily on the latter. 

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Channel-based versioning and interface-based versioning

The Compute Engine API supports two versioning schemes: channel-based versioning (CBV) and interface-based versioning (IBV).

  * In channel-based versioning, releases are long-lived and receive in-place updates. Compute Engine supports v1, beta, and alpha channels.

  * In interface-based versioning, individual interfaces, methods, and resources are versioned, and can evolve incrementally and independently.




IBV supersedes CBV. However, existing implementations of CBV are unaffected by the introduction of IBV and by new versions. You can continue to use CBV if you prefer to stay on the existing API release.

IBV helps you trust that the behavior of the API, and its request and response payload, conform to an intended API version. You use IBV by specifying an API version in your request, using either a query parameter or a header. For more information, see [Create an API request](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#constructing_an_api_request).

Using IBV provides the following benefits:

  * **Increased stability:** IBV protects running applications from change by allowing you to indicate the API version with which the service must respond.
  * **Control over change adoption:** with IBV, you choose which version serves your request. This lets you upgrade to new service features on your own schedule.



For more information about versioning strategies, see [API improvement proposal 185](https://google.aip.dev/185).

## Interface-based versioning policy

Every release of the Compute Engine IBV API is a collection of interface changes that share the same service version, even though interfaces might change version independently.

Compute Engine IBV API supports stable and preview versions.

### Stable versions

Most API releases are **stable versions**. Stable versions maintain strict compatibility, as defined in [AIP-180](https://google.aip.dev/180), meaning newer stable releases of the same version don't break existing functionality or require code rewrites.

Compute Engine identifies stable API versions using standard dates in the `YYYY-MM-DD` format (such as `2026-09-01`). Later dates indicate newer releases.

Compute Engine supports stable versions over long timeframes so your production systems remain reliable and uninterrupted. For most applications, you only need to use a single stable version to perform your daily tasks.

### Preview versions

Compute Engine can release **preview versions** to gather early user feedback on new features. Preview releases append a `-preview` tag to the date (such as `2026-10-01-preview`).

Preview versions include all capabilities from the latest stable release, plus newly added experimental features. Keep the following in mind when using preview versions:

  * Preview features don't guarantee compatibility with earlier or future releases.
  * We don't recommend using preview versions for mission-critical production environments.
  * We may change, refine, or remove preview features while promoting them to a stable release.



Use preview versions when you want to experiment with new capabilities, and plan to update your code when a stable version launches.

### Specify an API version in the request

To make API calls using IBV, your requests specify a target version by using either a query parameter or a header. For examples on how to make API requests, see [Create an API request](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#constructing_an_api_request).

## Cloud Client Libraries

Cloud Client Libraries remove the burden of building and parsing raw REST calls. Each library release connects directly to a specific date-based API version.

To access new features, update your Cloud Client Libraries package to the latest release. We publish updated Cloud Client Libraries alongside new stable and preview API releases.

We recommend running production applications on stable Cloud Client Libraries, while isolating preview libraries to testing environments.

## Google Cloud CLI (`gcloud`)

The `gcloud` CLI lets you manage Compute Engine resources without having to track individual REST endpoints manually.

The `gcloud` CLI divides commands into two categories:

  * **Stable commands:** standard commands (such as `gcloud compute instances create`) target stable API versions. These commands are fully supported, predictable, and recommended for production scripts.
  * **Preview commands:** early-access features use the `gcloud preview` group (such as `gcloud preview compute ...`). These commands show a brief warning because contracts can change before final release.



## Terraform

The Google Cloud Terraform Provider abstracts API versioning and manages underlying API interactions. Terraform configurations don't expose or require manual version header settings.

To access new features, update your Google Cloud Terraform Provider to the latest release. For preview features, use the `google-beta` provider.

## Frequently asked questions

This section answers frequently asked questions about Compute Engine API versioning.

  * **Do I have to migrate from v1 (CBV) to IBV?**

No, existing CBV v1 API requests continue to work as before. However, you won't be able to access new features available in IBV API.

  * **How long will an IBV API version be supported?**

Stable versions are maintained in perpetuity under the standard Google Cloud deprecation policy.

  * **How frequently are new IBV API versions released?**

New IBV API versions are planned with quarterly releases. Preview versions can be released at any time.

  * **Do I need to enable anything in Google Cloud console?**

No, IBV API is enabled by default with Compute Engine API.

  * **What happens if I don't specify a version in my request?**

Your request defaults to the CBV v1 endpoint.

  * **Where can I can find the API version in Cloud Audit Logs entries?**

The API version is logged in the `protoPayload.requestMetadata.callerSuppliedUserAgent` and in the request headers or query parameters.




## What's next

To learn more about the Compute Engine API, read the following documents:

  * Google API Improvement Proposals (AIPs): 
    * [AIP 9](https://google.aip.dev/9)
    * [AIP 180](https://google.aip.dev/180)
    * [AIP 181](https://google.aip.dev/181)
    * [AIP 184](https://google.aip.dev/184)
    * [AIP 185](https://google.aip.dev/185)
  * [Compute Engine API reference](https://docs.cloud.google.com/compute/docs/reference/rest/v1)
  * [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries)
  * [Google Cloud CLI (`gcloud`) overview](https://docs.cloud.google.com/sdk/gcloud)
  * [Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform)
  * [Compute Engine release notes](https://docs.cloud.google.com/compute/docs/release-notes) for the latest updates to the API



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
