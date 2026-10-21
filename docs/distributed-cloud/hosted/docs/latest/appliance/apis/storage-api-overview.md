---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/storage-api-overview/
title: Storage API overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:04.596714+00:00
---

# Storage API overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/storage-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Storage API overview Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

## Object storage

The Object Storage API includes Kubernetes Resource Model (KRM) and S3 REST API sections. Block storage is managed with standard Kubernetes storage API (<https://kubernetes.io/docs/concepts/storage/>).

The Object Storage API uses Kubernetes custom resources and relies on the Kubernetes Resource Model. The APIs are used for provisioning and administration of object storage resources. They are used to manage the lifecycle of object storage resources in the organization, including creating, reading, updating, and deleting buckets. The APIs are also used for listing, setting retention policies, and setting the storage class of buckets and bucket-level access control.

### Service endpoint and discovery document

The following URL is the API endpoint for the Object Storage APIs: `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/object.gdc.goog/v1` where `MANAGEMENT_API_SERVER_ENDPOINT` is the API endpoint of your Management API server.

Using the `kubectl proxy` command, you can access that URL in your browser or with a tool such as `curl` to get the discovery document for the Object Storage API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. After that command is running, access the document at the following URL: `http://127.0.0.1:8001/apis/object.gdc.goog/v1`.

### S3 REST API overview

Software-defined storage provides the Object Storage API compatible with the Amazon S3 API. The Google Distributed Cloud (GDC) air-gapped appliance Object Storage XML API is a RESTful interface that lets you to manage object storage data in a programmatic way. As a RESTful API, it relies on method information and scoping information to define the operations to perform: 

  * **Method information**. You specify the method information with standard HTTP methods, such as DELETE, GET, HEAD, and PUT.
  * **Scoping information**. You specify the scoping information with an accessible endpoint (URI) and various scoping parameters. For the XML API, the primary scoping parameters are the bucket and object names. Further scope your operations by using HTTP headers and query string parameters.



## Block storage

### Volume storage API overview

Interaction with storage within GDC occurs entirely using the Kubernetes storage primitives. To create persistent volumes, follow the documentation (<https://kubernetes.io/docs/concepts/storage/persistent-volumes/>) by Kubernetes.

Here is an example of a persistent volume claim:
    
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
    name: my_volume
    spec:
    accessModes:
    - ReadWriteOnce
    volumeMode: Filesystem
    resources:
    requests:
    storage: 1Gi
    storageClassName: standard-rwo
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
