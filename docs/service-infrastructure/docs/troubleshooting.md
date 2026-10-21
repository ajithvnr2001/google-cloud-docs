---
url: https://docs.cloud.google.com/service-infrastructure/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:31.003106+00:00
---

# Troubleshooting  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Resources ](https://docs.cloud.google.com/service-infrastructure/docs/resources)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page contains troubleshooting information for each version of the following Service Infrastructure APIs:

  * The Service Management API
  * The Service Control API
  * The Service Consumer Management API

**Note:** For Service Infrastructure troubleshooting information for the Service Usage API, see [Troubleshooting](https://docs.cloud.google.com/service-usage/docs/troubleshooting).

### How do I handle Service Control API errors in general?

The Service Control API provides control plane functionality, such as logging, monitoring, to managed services. Therefore, the callers of the Service Control API typically are server applications. Here are general recommendations on how to handle errors at the REST/RPC API level:

  * Your server should log all errors returned by the Service Control API and you can use the data to toubleshoot your [managed service](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed).
  * If your server receives `429` errors from the Service Control API, it should return `429` errors to its clients.
  * If your server cannot access the Service Control API, it can choose to either fail-open (ignore the error) or fail-close (return `503` to its client).
  * If your server receives `500` errors from the Service Control API, it should return `500` error to its clients. Such errors typically mean bugs within the Service Control API.
  * If your server receives other errors from the Service Control API, it should return `500` error to its clients. Such errors typically mean bugs within your managed service.



### What does the "service not enabled" error mean?

To use any Google API service, you need to have a Google Cloud project, enable the service for that project, and pass an API key or an OAuth access token associated with the project for each API request. See [Auth Guide](https://docs.cloud.google.com/docs/authentication) for details. To fix this error, you need to enable the service for your project using the Google Cloud console, Google Cloud CLI, or Service Usage API. To learn how to enable a service, see [Enabling and Disabling Services](https://docs.cloud.google.com/service-usage/docs/enable-disable).

### How do I fix permission denied errors?

Such errors typically mean the caller doesn't have the right [Identity and Access Management](https://docs.cloud.google.com/iam) permission on certain resources. For information on the required permissions for each of the following Service Infrastructure APIs, see the respective Access Control page:

  * [Service Control API Access Control](https://docs.cloud.google.com/service-infrastructure/docs/service-control/access-control)
  * [Service Management API Access Control](https://docs.cloud.google.com/service-infrastructure/docs/service-management/access-control)



### How do I perform a retry on API errors?

It is recommended to perform a retry with exponential intervals plus randomness. The minimum retry interval should be 30s for `429` quota errors; 1s for `500` and `503` server errors. For other errors, retry should only be performed based on additional error information. See [`google.rpc.Code`](https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto) for more details.

### How do I request higher API quota?

To learn how to apply for higher quota for each of the following Service Infrastructure APIs, visit the respective section of the [Quotas and Limits](https://docs.cloud.google.com/service-infrastructure/docs/quotas) page:

  * [Service Control API Quota](https://docs.cloud.google.com/service-infrastructure/docs/quotas#control)
  * [Service Consumer Management API Quota](https://docs.cloud.google.com/service-infrastructure/docs/quotas#consumer)
  * [Service Management API Quota](https://docs.cloud.google.com/service-infrastructure/docs/quotas#management)



### How do I fix "Ownership for domain name cannot be verified" errors?

This error indicates the caller does not have the ownership of the domain name used for the [managed service](https://docs.cloud.google.com/service-infrastructure/docs/glossary#managed) name specified in a [service configuration](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service). Follow the [guide](https://docs.cloud.google.com/endpoints/docs/custom-domain) to use a valid domain.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
