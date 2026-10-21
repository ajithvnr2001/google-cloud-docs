---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/storage-api-overview/
title: Storage API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:33.520536+00:00
---

# Storage API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/storage-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Storage API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Object Storage API uses Kubernetes custom resources and relies on the Kubernetes Resource Model. The APIs are used for the provisioning and administration of object storage resources. They are used to manage the lifecycle of object storage resources in a given organization, including creating, reading, updating, and deleting buckets. The APIs are also used for listing buckets, setting bucket retention policies, and setting the storage class of buckets. Block storage is managed with standard Kubernetes APIs.

## Service endpoint and discovery document

The Storage KRM APIs are provided in three packages depending on zonal deployment or global deployment.

The API endpoints for the zonal and global Storage APIs are the following, respectively:

  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/object.gdc.goog/v1`
  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/object.global.gdc.goog/v1`
  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/storage.global.gdc.goog/v1`



The `MANAGEMENT_API_SERVER_ENDPOINT` variable is the endpoint of the Management API server.

Using the `kubectl proxy` command, you can access that URL in your browser or with a tool such as `curl` to get the discovery document for the Object Storage API. The `kubectl proxy` command opens a proxy to the Kubernetes API server on your local machine. After that command is running, you can access the document at the following URLs:

  * `http://127.0.0.1:8001/apis/object.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/object.global.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/storage.global.gdc.goog/v1`



## S3 REST API overview

The Google Distributed Cloud (GDC) air-gapped Object Storage XML API is a RESTful interface that lets you manage object storage data in a programmatic way. As a RESTful API, it relies on method and scoping information to define the operations to perform:

  * **Method information**. You specify the method information with standard HTTP methods, such as `DELETE`, `GET`, `HEAD`, and `PUT`.
  * **Scoping information**. You specify the scoping information with an accessible endpoint (URI) and various scoping parameters. For the XML API, the primary scoping parameters are the bucket and object names. Further scope your operations by using HTTP headers and query string parameters.



## Volume Storage API overview

To create persistent volumes, follow the steps outlined by the Kubernetes documentation at <https://kubernetes.io/docs/concepts/storage/persistent-volumes/>. Interaction with Volume Storage within GDC occurs entirely through Kubernetes storage primitives. The Volume Storage driver implements the Container Storage Interface (CSI) protocol and provisions and orchestrates the volumes in the storage system, opaque to the end user of the persistent volume.

GDC supports a single storage class of type _standard-rwo_. See <https://kubernetes.io/docs/concepts/storage/storage-classes/> for more information on storage classes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
