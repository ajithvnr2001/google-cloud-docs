---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress/
title: Disable bundled ingress \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:02:58.672672+00:00
---

# Disable bundled ingress  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/disable-bundled-ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Disable bundled ingress Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to disable bundled ingress for a user cluster in Google Distributed Cloud.

By default, bundled ingress is enabled in user clusters. This means that the `istiod` and `istio-ingress` Deployments are running. For more information, see [Ingress components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-service-ingress#ingress_components).

If you want to use a full installation of [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) in a user cluster, you might want to disable bundled ingress. This is because bundled ingress is not needed when Cloud Service Mesh is fully installed, and there are potential conflicts between bundled ingress and Cloud Service Mesh.

## Disable bundled ingress for a new cluster

Create a user cluster as described in [Create a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

As you fill in your user cluster configuration file:

  * Set `disableBundledIngress` to `true`.
  * Do not specify a value for `loadBalancer.vips.ingressVIP`.


    
    
    apiVersion: v1
    kind: UserCluster
    ...
    disableBundledIngress: true
    ...
    loadBalancer:
      vips:
        controlPlaneVIP: 172.16.21.30
        ingressVIP:
    

## Disable bundled ingress for an existing cluster

In your existing user cluster configuration file:

  * Set `disableBundledIngress` to `true`.
  * Remove the `loadBalancer.vips.ingressVIP` value. 



Update the cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

  * USER_CLUSTER_CONFIG: the path of the user cluster configuration file




## Manual load balancing

If your cluster uses manual load balancing and you want to disable bundled ingress, do not specify values for the following fields:

  * `loadBalancer.manualLB.ingressHTTPSNodePort`
  * `loadBalancer.manualLB.ingressHTTPNodePort`


    
    
    loadBalancer:
      Kind: ManaulLB
      manualLB:
        ingressHTTPSNodePort:
        ingressHTTPNodePort:
        controlPlaneNodePort: 30562
    

## Enable bundled ingress for an existing cluster

If you want to enable bundled ingress for an existing user cluster that has bundled ingress disabled, edit the user cluster configuration file, and run `gkectl update cluster`.

## Related documents

  * [Overview of load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/setup-load-balance)
  * [Create a Service and an Ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-service-ingress)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
