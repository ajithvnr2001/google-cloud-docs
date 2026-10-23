---
url: https://docs.cloud.google.com/secret-manager/quotas/
title: Quotas and limits \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:47.541747+00:00
---

# Quotas and limits  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/secret-manager/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

## Secret Manager quotas and limits

These quotas apply to each Google Cloud project and are shared across all applications and IP addresses using that project.

### Content limits

The Secret Manager API enforces the following usage limits for a given secret version.

Content limit | Value  
---|---  
Payload size | 64 KiB  
Alias | 50  
  
### Soft-enforced rate limits for modifying secrets and secret versions

The following table details the soft-enforced rate limits for `AddSecretVersion` and `UpdateSecret` operations:

Type of secret | Rate limit  
---|---  
Global secret | 2 requests per second (2 qps) per secret, and 120 requests per minute (120 qpm) per secret.  
Regional secret | 80 requests per second (80 qps) per secret per region, and 4800 requests per minute (4800 qpm) per secret per region.  
  
The following table details the rate limits for `EnableSecretVersion`, `DisableSecretVersion`, and `DestroySecretVersion` operations:

Type of secret | Rate limit  
---|---  
Global secret | 1 request per second (1 qps) per secret version, and 60 requests per minute (60 qpm) per secret version.  
Regional secret | 50 requests per second (50 qps) per secret version per region, and 3000 requests per minute (3000 qpm) per secret version per region.  
**Note:** Soft-enforcement allows us to continue serving requests beyond their quota as long as our backend systems can handle the load.

### Quotas on the rate of requests

The API usage quotas for the Secret Manager API are as follows:

Request quota | Value  
---|---  
Access request | 90,000 per minute per project  
Read request | 600 per minute per project  
Write request | 600 per minute per project  
  
  * An **access request** is any call to the [`access` API method](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/access).

  * A **read request** is any non-mutating operation (an operation that does not modify a secret version) _except for access requests_. Examples include listing secrets and fetching secret metadata.

  * A **write request** is any mutating operation (an operation that modifies or deletes a secret or secret version). Examples include creating, updating, or deleting a secret, or adding, enabling, disabling, or destroying a secret version.




### Checking your quotas

To check the quotas for resources in your project, go to the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console.

### Requesting increases

To request an increase of your Secret Manager quotas, please contact your sales representative or contact [Google Cloud Support](https://docs.cloud.google.com/support).

## Parameter Manager quotas and limits

These quotas apply to each Google Cloud project and are shared across all applications and IP addresses using that project.

### Content limits

The Parameter Manager API enforces the following usage limits for a given parameter version.

Content limit | Value  
---|---  
Payload size | 1 MiB  
  
### Quotas on the rate of requests

The API usage quotas for the Parameter Manager API are as follows:

Request quota | Value  
---|---  
Render request | 1,800 per minute per project  
Read request | 1,200 per minute per project  
Write request | 1,200 per minute per project  
  
  * A **render request** is any call to the [`render` API method](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions/render).

  * A **read request** is any non-mutating operation (an operation that does not modify a parameter version) _except for render requests_. Examples include listing parameters and fetching parameter metadata.

  * A **write request** is any mutating operation (an operation that modifies or deletes a parameter or parameter version). Examples include creating, updating, or deleting a parameter, or adding, enabling, disabling, or destroying a parameter version.




### Checking your quotas

To check the quotas for resources in your project, go to the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console.

### Requesting increases

To request an increase of your Parameter Manager quotas, please contact your sales representative or contact [Google Cloud Support](https://docs.cloud.google.com/support). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
