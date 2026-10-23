---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/revisions-overview/
title: Cloud Service Mesh control plane revisions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:22.284733+00:00
---

# Cloud Service Mesh control plane revisions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/revisions-overview/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh control plane revisions

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.29/docs/supported-platforms#off-gcp). **Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.29/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. **Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview).

This page applies to the in-cluster and managed `ISTIOD` [control plane implementations](https://docs.cloud.google.com/service-mesh/v1.29/docs/check-control-plane-implementation). This page does not apply to the `TRAFFIC_DIRECTOR` control plane implementation, which is a multi-tenant, global control plane, without individual revisions.

This page describes how control plane _revisions_ work and the value of using them for safe service mesh upgrades (and rollbacks).

## Service mesh installation fundamentals

At a high level, Cloud Service Mesh installation consists of two major phases:

  1. First you use the `asmcli` tool to install an [in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.29/docs/unified-install/install-anthos-service-mesh) or configure the [managed control plane](https://docs.cloud.google.com/service-mesh/v1.29/docs/managed/provision-managed-anthos-service-mesh). The control plane consists of a set of system services that are responsible for managing mesh configuration.

  2. Next, you deploy a special _sidecar proxy_ throughout your environment that intercepts network communication to and from each workload. The proxies communicate with the control plane to get their configuration, which allows you to direct and control traffic (data plane traffic) around your mesh without making any changes to your workloads.

To deploy the proxies, you use a process called [_automatic sidecar injection_ (auto-injection)](https://docs.cloud.google.com/service-mesh/v1.29/docs/anthos-service-mesh-proxy-injection) to run a proxy as an additional sidecar container in each of your workload Pods. You don't need to modify the Kubernetes manifests that you use to deploy your workloads, but you do need to add a label to your namespaces and restart the Pods.




## Use revisions to upgrade your mesh safely

The ability to control traffic is one of the principal benefits of using a service mesh. For example, you can gradually shift traffic to a new version of an application when you first deploy it to production. If you detect problems during the upgrade, you can shift traffic back to the original version, providing a simple and low risk means of rolling back. This procedure is known as a _canary release_ , and it greatly reduces the risk associated with new deployments.

**Note:** An alternative type of upgrade is an _in-place upgrade_ in which you upgrade by installing a new version of the control plane. The new control plane version immediately replaces the old version. In-place upgrades are risky because if there are failures, rolling back can be difficult. To re-inject the proxies and have them communicate with the new control plane version, you must to restart all workloads in all of your namespaces. Depending on the number of workloads and namespaces in your mesh, the entire upgrade process could take an hour or more. In-place upgrades can lead to downtime and should be scheduled in maintenance windows.

Using control plane revisions in a canary upgrade, you install a new and separate control plane and configuration alongside the existing control plane. The installer assigns a string called a revision to identify the new control plane. At first, the sidecar proxies continue to receive configuration from the previous version of the control plane. You gradually associate workloads with the new control plane by labelling their namespaces or Pods with the new control plane revision. Once you have labelled a namespace or Pods with the new revision, you restart the workload Pods so that new sidecars are auto-injected, and they receive their configuration from the new control plane. If there are problems, you can easily roll back by associating the workloads with the original control plane.

## How does auto-injection work?

Auto-injection uses a Kubernetes feature called [admission control](https://kubernetes.io/blog/2019/03/21/a-guide-to-kubernetes-admission-controllers/). A mutating admission webhook is registered to watch for newly created Pods. The webhook is configured with a namespace selector so that it only matches Pods that are being deployed to namespaces that have a particular label. When a Pod matches, the webhook consults an injection service provided by the control plane to obtain a new, mutated configuration for the Pod, which contains the containers and volumes needed to run the sidecar.

![sidecar injector](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/Diagram_sidecar_injector.svg)

  1. A webhook configuration is created during installation. The webhook is registered with the Kubernetes API server.
  2. The Kubernetes API server watches for Pod deployments in namespaces that match the webhook `namespaceSelector`.
  3. A namespace is labeled so that it will be matched by the `namespaceSelector`.
  4. Pods deployed to the namespace trigger the webhook.
  5. The `inject` service provided by the control plane mutates the Pod specifications to auto-inject the sidecar.



## What is a revision?

The label used for auto-injection is like any other user-defined Kubernetes label. A label is essentially a key-value pair which can be used to support the concept of labelling. Labels are widely used for tagging and for revisions. For example, Git tags, Docker tags, and [Knative revisions](https://knative.dev/docs/getting-started/first-traffic-split/#creating-a-new-revision).

The current Cloud Service Mesh installation process lets you label the installed control plane with a revision string. The installer labels every control plane object with the revision. The key in the key-value pair is `istio.io/rev`, but the value of the revision label differs for the managed control plane and the in-cluster control planes.

  * For in-cluster control planes, the `istiod` Service and Deployment typically have a revision label similar to `istio.io/rev=asm-1298-11`, where `asm-1298-11` identifies the Cloud Service Mesh version. The revision becomes part of the service name, for example: `istiod-asm-1298-11.istio-system`

  * For the managed control plane, the revision label corresponds to a [release channel](https://docs.cloud.google.com/service-mesh/v1.29/docs/managed/select-a-release-channel):

Revision label | Channel  
---|---  
`istio.io/rev=asm-managed` | Regular  
`istio.io/rev=asm-managed-rapid` | Rapid  
`istio.io/rev=asm-managed-stable` | Stable  



Additionally, you have the option of using [default injection labels](https://docs.cloud.google.com/service-mesh/v1.29/docs/managed/select-a-release-channel#how_to_select_a_release_channel) (for example, `istio-injection=enabled`).

To enable auto-injection, you add a revision label to your namespaces that matches the revision label on the control plane. For example, a control plane with revision `istio.io/rev=asm-1298-11` selects Pods in namespaces with the label `istio.io/rev=asm-1298-11` and injects sidecars.

## The canary upgrade process

Revision labels make it possible to perform canary upgrades and easy rollbacks of the in-cluster control plane. The managed control uses a similar process, but your cluster is automatically upgraded to the latest version within that channel.

![canary upgrade](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/Diagram_Canary_upgrades.svg)

The following steps describe how the process works:

  1. Start with an existing Cloud Service Mesh or open source Istio installation. It doesn't matter whether the namespaces are using a revision label or the `istio-injection=enabled` label.
  2. Use a revision string when you install the new version of the control plane. Because of the revision string, the new control plane is installed alongside the existing version. The new installation includes a new webhook configuration with a `namespaceSelector` configured to watch for namespaces with that specific revision label.
  3. You migrate sidecar proxies to the new control plane by removing the old label from the namespace, adding the new revision label, and then restarting the Pods. If you use revisions with Cloud Service Mesh, you must stop using the `istio-injection=enabled` label. A control plane with a revision does not select Pods in namespaces with an `istio-injection` label, even if there is a revision label. The webhook for the new control plane injects sidecars into the Pods.
  4. Carefully test the workloads associated with the upgraded control plane and either continue to roll out the upgrade or roll back to the original control plane.



After associating Pods with the new control plane, the existing control plane and webhook are still installed. The old webhook has no effect for Pods in namespaces that have been migrated to the new control plane. You can roll back the Pods in a namespace to the original control plane by removing the new revision label, adding back the original label and restarting the Pods. When you are certain that the upgrade is complete, you can remove the old control plane.

For detailed steps on upgrading using revisions, see the [Upgrade guide](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade).

## A closer look at a mutating webhook configuration

To better understand the mutating webhook for automatic sidecar injection, inspect the configuration yourself. Use the following command:
    
    
    kubectl -n istio-system get mutatingwebhookconfiguration -l app=sidecar-injector -o yaml
    

You should see a separate configuration for each control plane that you have installed. A namespace selector for a revision-based control plane looks like this:
    
    
     namespaceSelector:
        matchExpressions:
        - key: istio-injection
          operator: DoesNotExist
        - key: istio.io/rev
          operator: In
          values:
          - asm-1298-11
    

The selector may vary depending on the version of Cloud Service Mesh or Istio that you are running. This selector matches namespaces with a specific revision label as long as they do not also have an `istio-injection` label.

When a Pod is deployed to a namespace matching the selector, its Pod specification is submitted to the injector service for mutation. The injector service to be called is specified as follows:
    
    
         service:
            name: istiod-asm-1298-11
            namespace: istio-system
            path: /inject
            port: 443
    

**Note:** For managed Cloud Service Mesh, the Google-managed service is specified by `url:` instead of `service:`.

The service is exposed by the control plane on port 443 at the `inject` URL path.

The `rules` section specifies that the webhook should apply to Pod creation:
    
    
       rules:
        - apiGroups:
          - ""
          apiVersions:
          - v1
          operations:
          - CREATE
          resources:
          - pods
          scope: '*'
    

## What's next

  * [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade)
  * [Injecting sidecar proxies](https://docs.cloud.google.com/service-mesh/v1.29/docs/onboarding/kubernetes-workloads#inject_sidecar_proxies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
