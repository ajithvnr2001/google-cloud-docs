---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/cluster/cluster-api-overview/
title: Cluster API overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:37.780460+00:00
---

# Cluster API overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/cluster/cluster-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Cluster API overview Stay organized with collections  Save and categorize content based on your preferences. 

The Cluster API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM). It manages the lifecycle of clusters in a given organization, such as installing, upgrading, and uninstalling.

To use the Cluster API, we recommend that you use the GDC console. If your application needs to use your own libraries to call this API, use the following example and the [full API definition](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/cluster/v1/cluster-v1) to build your requests.

## Service endpoint and discovery document

The API endpoint for the Cluster API is `https://MANAGEMENT_API_SERVER_ENDPOINT/apis/cluster.gdc.goog/v1`, where `MANAGEMENT_API_SERVER_ENDPOINT` is the endpoint of the Management API server.

Using the `kubectl proxy` command, you can access that URL in your browser or with a tool such as `curl` to get the discovery document for the Cluster API. The `kubectl proxy` command opens up a proxy to the Kubernetes API server on your local machine. Once that command is running, you can access the document at the following URL: `http://127.0.0.1:8001/apis/cluster.gdc.goog/v1`.

## Example Cluster resource

The following is an example of a `Cluster` object configured as a user cluster:
    
    
    apiVersion: cluster.gdc.goog/v1
    kind: Cluster
    metadata:
      name: user-vm-1
      namespace: platform
    spec:
      clusterNetwork:
        podCIDRSize: 21
        serviceCIDRSize: 23
      initialVersion:
        kubernetesVersion: 1.27.1-gke.700
      loadBalancer:
        ingressServiceIPSize: 21
      nodePools:
      - machineTypeName: n2-standard-8-gdc
        name: worker-node-pool
        nodeCount: 3
      releaseChannel:
        channel: UNSPECIFIED
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
