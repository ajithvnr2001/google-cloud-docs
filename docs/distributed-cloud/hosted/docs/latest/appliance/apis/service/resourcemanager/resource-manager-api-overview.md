---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/resourcemanager/resource-manager-api-overview/
title: Resource Manager API overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:03.971069+00:00
---

# Resource Manager API overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/resourcemanager/resource-manager-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Resource Manager API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Resource Manager API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM) for provisioning and administration of organization and project resources. It is used to manage the lifecycle of Google Distributed Cloud (GDC) air-gapped appliance projects, such as installing, upgrading, and uninstalling.

To use the Resource Manager API, we recommend that you use the GDC console and gdcloud CLI. If your application needs to use your own libraries to call this API, use the following example and the [full API definition](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/resourcemanager/v1/resourcemanager-v1) to build your requests.

## Service endpoint and discovery document

The API endpoint for the Resource Manager API is `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/resourcemanager.gdc.goog/v1` where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.

The Resource Manager View API follows a similar convention for its API endpoint: `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/resourcemanagerview.gdc.goog/v1`.

Using the `kubectl proxy` command, you can access the API endpoint URLs in your browser or with a tool such as `curl` to get the discovery document for the Resource Manager API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. Once that command is running, you can access the document at the following URL: `http://127.0.0.1:8001/apis/resourcemanager.gdc.goog/v1`.

## Example Project resource

The following is an example of a `Project` object configured as a GDC project resource. As a user of the Resource Manager API, creating a project through the GDC console generates the `Project` object by default. You must only modify it to reflect the project state you want.
    
    
    apiVersion: resourcemanager.gdc.goog/v1
    kind: Project
      name: test-project
      namespace: test-namespace
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
