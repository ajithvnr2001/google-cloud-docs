---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/anthos-service-mesh-proxy-injection/
title: Inject sidecar proxies with Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:43.459752+00:00
---

# Inject sidecar proxies with Cloud Service Mesh  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/anthos-service-mesh-proxy-injection/

You are viewing archived v1.19 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Inject sidecar proxies with Cloud Service Mesh

This document covers how to configure sidecar proxy injection with Cloud Service Mesh to enhance network security, reliability, and observability. These functions are abstracted away from the application's primary container and implemented in a common out-of-process proxy (the sidecar), delivered as a separate container in the same Pod. This provides the [Cloud Service Mesh's features](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview) without redesigning your production applications to participate in a service mesh.

Automatic sidecar proxy injection (auto-injection) occurs when Cloud Service Mesh detects a namespace label you configure for the workload's Pod. The proxy intercepts all inbound and outbound traffic to the workloads and communicates with Cloud Service Mesh.

#### Permissions required for these tasks

To perform the tasks on this page, you must have the `roles/container.clusterAdmin` or a higher role. See [ Google Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/understanding-roles#container) for details on the permissions included in this role. 

## Enabling automatic sidecar injection

The recommended way to inject sidecar proxies is to use the webhooks-based automatic sidecar injector, although you can manually update your Pods' Kubernetes configuration.

To enable auto-injection, you label your namespaces with the _[default injection labels](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag)_ if the default tag is set up, or with the [revision label](https://docs.cloud.google.com/service-mesh/v1.19/docs/revisions-overview) to your namespace. The label that you add also depends on whether you deployed managed Cloud Service Mesh (with the [fleet API](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh) or with [`asmcli`](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh-asmcli)), or installed the in-cluster control plane. The label is used by the sidecar injector webhook to associate injected sidecars with a particular control plane revision.

To enable auto-injection:

### In-cluster

  1. Use the following command to locate the revision label on `istiod`:
         
         kubectl -n istio-system get pods -l app=istiod --show-labels
         

The output looks similar to the following:
         
         NAME                                READY   STATUS    RESTARTS   AGE   LABELS
         istiod-asm-11910-9-5788d57586-bljj4   1/1     Running   0          23h   app=istiod,istio.io/rev=asm-11910-9,istio=istiod,pod-template-hash=5788d57586
         istiod-asm-11910-9-5788d57586-vsklm   1/1     Running   1          23h   app=istiod,istio.io/rev=asm-11910-9,istio=istiod,pod-template-hash=5788d57586

In the output, under the `LABELS` column, note the value of the `istiod` revision label, which follows the prefix `istio.io/rev=`. In this example, the value is `asm-11910-9`.

**Note:** You can substitute `istio.io/rev` with the `istio-injection=enabled` label if the [default tag](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) is configured. Verify the default tag exists by running ` istioctl tag list` with the `istioctl` from `OUTPUT_DIR`. 

  2. Apply the revision label to namespaces and remove the istio-injection label (if it exists). In the following command, `NAMESPACE` is the name of the namespace where you want to enable auto-injection, and `REVISION` is the revision label you noted in the previous step.
         
         kubectl label namespace NAMESPACE  istio-injection- istio.io/rev=REVISION --overwrite
         

You can ignore the message `"istio-injection not found"` in the output. That means that the namespace didn't previously have the `istio-injection` label, which you should expect in new installations of Cloud Service Mesh or new deployments. Because auto-injection behavior is undefined when a namespace has both the `istio-injection` and the revision label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly ensure that only one is set. 

  3. Restart the affected pods, using the steps in the next section.




### Managed service mesh

  1. Use the following command to locate the available release channels:
         
         kubectl -n istio-system get controlplanerevision
         

The output is similar to the following:
         
         NAME                AGE
         asm-managed         6d7h
         

In the output, select the value under the `NAME` column is the `REVISION` label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version. Apply this label to your namespaces, and remove the `istio-injection` label (if it exists). In the following command, replace `REVISION` with the revision label you noted above, and replace `NAMESPACE ` with the name of the namespace where you want to enable auto-injection:
         
         kubectl label namespace NAMESPACE  istio-injection- istio.io/rev=REVISION --overwrite
         

You can ignore the message `"istio-injection not found"` in the output. That means that the namespace didn't previously have the `istio-injection` label, which you should expect in new installations of Cloud Service Mesh or new deployments. Because auto-injection behavior is undefined when a namespace has both the `istio-injection` and the revision label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly ensure that only one is set. 

  2. Restart the affected pods, using the steps in the next section.

  3. If you also deployed the optional [Google-managed data plane](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh#managed-data-plane), annotate the `demo` namespace as follows:
         
         kubectl annotate --overwrite namespace YOUR_NAMESPACE \
         mesh.cloud.google.com/proxy='{"managed":"true"}'
         




### Restart Pods to update sidecar proxies

**Warning:** Unless you have a load balancer or router setup for [blue-green deployments](https://martinfowler.com/bliki/BlueGreenDeployment.html), make sure you test restarting Pods in a staging environment to verify that your services can handle any potential traffic interruption.

With automatic sidecar injection, you can update the sidecars for existing Pods with a Pod restart:

How you restart Pods depends on if they were created as part of a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

  1. If you used a Deployment, restart the Deployment, which restarts all Pods with sidecars:
         
         kubectl rollout restart deployment -n YOUR_NAMESPACE

If you didn't use a Deployment, delete the Pods, and they are automatically recreated with sidecars:
         
         kubectl delete pod -n YOUR_NAMESPACE --all

  2. Check that all the Pods in the namespace have sidecars injected:
         
         kubectl get pod -n YOUR_NAMESPACE

In the following example output from the previous command, notice that the `READY` column indicates there are two containers for each of your workloads: the primary container and the container for the sidecar proxy.
         
         NAME                    READY   STATUS    RESTARTS   AGE
         YOUR_WORKLOAD           2/2     Running   0          20s
         ...
         




## What's next

Learn more about:

  * [Cloud Service Mesh control plane revisions](https://docs.cloud.google.com/service-mesh/v1.19/docs/revisions-overview)
  * [Deploying workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview)
  * [Customizing injection](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#customizing-injection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
