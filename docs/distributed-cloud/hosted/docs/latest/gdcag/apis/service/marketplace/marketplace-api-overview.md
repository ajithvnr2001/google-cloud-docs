---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/marketplace-api-overview/
title: Marketplace API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:28.377267+00:00
---

# Marketplace API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/marketplace/marketplace-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Marketplace API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Marketplace API uses Kubernetes custom resources and relies on the Kubernetes Resource Model. The APIs are used for the provisioning and administration of the Marketplace services in a given project through actions that include installing, upgrading, and uninstalling. The GDC Marketplace APIs are also used to see available versions, create, modify, or delete objects in your project to install, upgrade, or uninstall instances of a service.

## Service endpoint and discovery document

The following URL is the API endpoint for the Marketplace APIs: `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/marketplace.gdc.goog/v1` where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.

Using the `kubectl proxy` command, you can access that URL in your browser or with a tool such as `curl` to get the discovery document for the Marketplace API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. When the command is running, access the document at the following URL:

`http://127.0.0.1:8001/apis/marketplace.gdc.goog/v1`

## Service instance manifest format

The following is the format of a `ServiceInstance` resource:
    
    
    apiVersion: marketplace.gdc.goog/v1
    kind: ServiceInstance
    metadata:
      name: INSTANCE_NAME
    spec:
      clusterRef:
        name: CLUSTER_NAME
        namespace: CLUSTER_NAMESPACE
      serviceVersionRef:
        name: SERVICE_VERSION_NAME
        namespace: mkt-system
    

Replace the following:

  * `INSTANCE_NAME`: a name for your new application instance
  * `CLUSTER_NAME`: the name of the target user cluster where you want to install the application
  * `CLUSTER_NAMESPACE`: the namespace of the cluster (for example, `production-cluster`)
  * `SERVICE_VERSION_NAME`: the name of the `ServiceVersion` to install (for example, `dataproc-1.0.0`)



To install a service, create this object in a project's namespace with `kubectl apply`, as described in [Install a Distributed Cloud marketplace software package](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/marketplace-lifecycle#install-sw). To upgrade a service instance, modify it to indicate which version of that service. You can modify the object directly with an HTTP client or by using the `kubectl apply`, `kubectl patch`, or `kubectl edit` commands. To uninstall a service instance, delete the object with `kubectl delete`.

## Example KRM

The following is an example of a `ServiceInstance` object in the Marketplace API of Dataproc Container for Spark:
    
    
    apiVersion: marketplace.gdc.goog/v1
    kind: ServiceInstance
    metadata:
      name: dataproc-service
    spec:
      clusterRef:
        name: production
        namespace: production-cluster
      serviceVersionRef:
        name: SERVICE_VERSION_NAME
        namespace: mkt-system
    status:
      # Currently installed version of the service
      installedVersion: 1.0.0
      # Current conditions of the service (see https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.22/#condition-v1-meta)
      conditions:
        ...
    

Replace `SERVICE_VERSION_NAME` with the version of the service to install, for example `dataproc-1.0.19` or `elasticsearch:9.3.2`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
