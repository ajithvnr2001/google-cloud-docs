---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanager/resource-manager-api-overview/
title: Resource Manager API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:13.258098+00:00
---

# Resource Manager API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanager/resource-manager-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Resource Manager API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Resource Manager API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM) for provisioning and administration of organization and project resources. It is used to manage the lifecycle of Google Distributed Cloud (GDC) air-gapped organizations and projects, such as installing, upgrading, and uninstalling.

To use the Resource Manager API, we recommend that you use the GDC console, gdcloud CLI, or call the API directly using the `kubectl` CLI. If your application needs to use your own libraries to call this API, use the following examples and the full API definitions to build your requests:

  * [resourcemanager.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanager/v1/resourcemanager-v1)
  * [resourcemanager.global.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanager/v1/global-resourcemanager-v1)
  * [resourcemanagerview.gdc.goog](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/resourcemanagerview/v1/resourcemanagerview-v1)



## Service endpoint and discovery document

The Resource Manager APIs are provided in two packages depending on zonal deployment or global deployment.

The API endpoints for the zonal and global Resource Manager APIs are the following, respectively:

  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/resourcemanager.gdc.goog/v1`
  * `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/resourcemanager.global.gdc.goog/v1`



The API endpoint for the Resource Manager View API is the following:
    
    
    https://MANAGEMENT_API_SERVER_ENDPOINT/apis/resourcemanagerview.gdc.goog/v1
    

The `MANAGEMENT_API_SERVER_ENDPOINT` variable is the endpoint of the Management API server.

Using the `kubectl proxy` command, you can access the API endpoint URLs in your browser or with a tool such as `curl` to get the discovery document for the Resource Manager API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. After that command is running, you can access the documents at the following URLs:

  * `http://127.0.0.1:8001/apis/resourcemanager.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/resourcemanager.global.gdc.goog/v1`
  * `http://127.0.0.1:8001/apis/resourcemanagerview.gdc.goog/v1`



## Example Project resource

The following is an example of a `Project` object configured as a GDC project resource. As a user of the Resource Manager API, creating a project through the GDC console generates the `Project` object by default. You must only modify it to reflect the project state you want.
    
    
    apiVersion: resourcemanager.global.gdc.goog/v1
    kind: Project
    metadata:
      namespace: platform
      name: test-project
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
