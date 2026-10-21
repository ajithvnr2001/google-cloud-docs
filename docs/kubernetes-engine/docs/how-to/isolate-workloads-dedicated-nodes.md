---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes/
title: Isolate your workloads in dedicated node pools \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:10.755049+00:00
---

# Isolate your workloads in dedicated node pools  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Isolate your workloads in dedicated node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to reduce the risk of privilege escalation attacks in your cluster by telling Google Kubernetes Engine (GKE) to schedule your workloads on a separate, dedicated node pool away from privileged GKE-managed workloads. You should use this approach only if you _can't_ use GKE Sandbox. [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) is the recommended approach for node isolation. GKE Sandbox also provides other hardening benefits for your workloads.

This page is for Security specialists who require a layer of isolation on workloads but can't use GKE Sandbox. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This page applies to Standard clusters without node auto-provisioning. To separate workloads in Autopilot clusters and in Standard clusters with node auto-provisioning enabled, refer to [Configure workload separation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation).

## Overview

GKE clusters use privileged GKE-managed workloads to enable specific cluster functionality and features, such as [metrics gathering](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#understand_how_metrics_server_works_and_how_to_monitor_it). These workloads are given special permissions to run correctly in the cluster.

Workloads that you deploy to your nodes might have the potential to be compromised by a malicious entity. Running these workloads alongside privileged GKE-managed workloads means that an attacker who breaks out of a compromised container can use the credentials of the privileged workload on the node to escalate privileges in your cluster.

### Prevent container breakouts

Your primary defense should be your applications. GKE has multiple features that you can use to harden your clusters and Pods. In most cases, we **strongly recommend** using [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) to isolate your workloads. GKE Sandbox is based on the [gVisor open source project](https://github.com/google/gvisor), and implements the Linux kernel API in the userspace. Each Pod runs on a dedicated kernel that sandboxes applications to prevent access to privileged system calls in the host kernel. Workloads running in GKE Sandbox are automatically scheduled on separate nodes, isolated from other workloads.

You should also follow the recommendations in [Harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).

### Avoid privilege escalation attacks

If you can't use GKE Sandbox, and you want an extra layer of isolation in addition to other hardening measures, you can use [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) and [node affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/) to schedule your workloads on a dedicated node pool. A node taint tells GKE to avoid scheduling workloads without a corresponding toleration (such as GKE-managed workloads) on those nodes. The node affinity on your own workloads tells GKE to schedule your Pods on the dedicated nodes.

**Caution:** Node isolation is an advanced defence-in-depth mechanism that you should **only** use alongside other isolation features such as minimally-privileged containers and service accounts. Node isolation might not cover all escalation paths, and should never be used as a primary security boundary. We don't recommend this approach unless you can't use GKE Sandbox.

### Limitations of node isolation

  * Attackers can still initiate Denial-of-Service (DoS) attacks from the compromised node.
  * Compromised nodes can still read many resources, including all Pods and namespaces in the cluster.
  * Compromised nodes can access Secrets and credentials used by every Pod running on that node.
  * Using a separate node pool to isolate your workloads can impact your cost efficiency, autoscaling, and resource utilization.
  * Compromised nodes can still bypass egress network policies.
  * Some GKE-managed workloads must run on every node in your cluster, and are configured to tolerate all taints.
  * If you deploy DaemonSets that have elevated permissions and can tolerate any taint, those Pods may be a pathway for privilege escalation from a compromised node.



## How node isolation works

To implement node isolation for your workloads, you must do the following:

  1. Taint and label a node pool for your workloads.
  2. Update your workloads with the corresponding toleration and node affinity rule.



This guide assumes that you start with one node pool in your cluster. Using node affinity in addition to node taints isn't mandatory, but we recommend it because you benefit from greater control over scheduling.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Choose a specific name for the node taint and the node label that you want to use for the dedicated node pools.



## Taint and label a node pool for your workloads

**Best practice** : to prevent the kubelet from modifying node labels that you use for workload isolation, prefix your label keys with `node-restriction.kubernetes.io/`. 

Create a new node pool for your workloads and apply a node taint and a node label. When you apply a taint or a label at the node pool level, any new nodes, such as those created by autoscaling, will automatically get the specified taints and labels.

You can also add node taints and node labels to existing node pools. If you use the `NoExecute` effect, GKE evicts any Pods running on those nodes that don't have a toleration for the new taint.

For workload isolation, always use the `node-restriction.kubernetes.io/` prefix for your node labels and for the corresponding selectors in your Pod manifests. This prefix prevents an attacker from using the node's credential to set or modify the labels that use this prefix. For more information, see [Node isolation/restriction](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-isolation-restriction) in the Kubernetes documentation.

To add a taint and a label to a new node pool, run the following command:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster=CLUSTER_NAME \
        --node-taints=TAINT_KEY=TAINT_VALUE:TAINT_EFFECT \
        --node-labels=node-restriction.kubernetes.io/LABEL_KEY=LABEL_VALUE
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool for your workloads.
  * `CLUSTER_NAME`: the name of your GKE cluster.
  * `TAINT_KEY=TAINT_VALUE`: a key-value pair associated with a scheduling `TAINT_EFFECT`. For example, `workloadType=untrusted`.
  * `TAINT_EFFECT`: one of the following [effect values](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/): `NoSchedule`, `PreferNoSchedule`, or `NoExecute`. `NoExecute` provides a better eviction guarantee than `NoSchedule`.
  * `node-restriction.kubernetes.io/LABEL_KEY`=`LABEL_VALUE`: key-value pairs for the node labels, which correspond to the selectors that you specify in your workload manifests. The `node-restriction.kubernetes.io/` prefix prevents the node credentials from being used to set these key-value pairs on nodes.



## Add a toleration and a node affinity rule to your workloads

After you taint the dedicated node pool, no workloads can schedule on it unless they have a toleration corresponding to the taint you added. Add the toleration to the specification for your workloads to let those Pods schedule on your tainted node pool.

If you labelled the dedicated node pool, you can also add a node affinity rule to tell GKE to only schedule your workloads on that node pool.

The following example adds a toleration for the `workloadType=untrusted:NoExecute` taint and a node affinity rule for the `workloadType=untrusted` node label.
    
    
    kind: Deployment
    apiVersion: apps/v1
    metadata:
      name: my-app
      namespace: default
      labels:
        app: my-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        **spec :
          tolerations:
          - key: TAINT_KEY
            operator: Equal
            value: TAINT_VALUE
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: node-restriction.kubernetes.io/LABEL_KEY
                    operator: In
                    values:
                    - "LABEL_VALUE"**
          containers:
          - name: sleep
            image: ubuntu
            command: ["/bin/sleep", "inf"]
    

Replace the following:

  * `TAINT_KEY`: the taint key that you applied to your dedicated node pool.
  * `TAINT_VALUE`: the taint value that you applied to your dedicated node pool.
  * `LABEL_KEY`: the node label key that you applied to your dedicated node pool.
  * `LABEL_VALUE`: the node label value that you applied to your dedicated node pool.



When you update your Deployment with `kubectl apply`, GKE recreates the affected Pods. The node affinity rule forces the Pods onto the dedicated node pool that you created. The toleration allows only those Pods to be placed on the nodes.

## Verify that the separation works

To verify that the scheduling works correctly, run the following command and check whether your workloads are on the dedicated node pool:
    
    
    kubectl get pods -o=wide
    

## Recommendations and best practices

After setting up node isolation, we recommend that you do the following:

  * Restrict specific node pools to GKE-managed workloads only by adding the `components.gke.io/gke-managed-components` taint. Adding this taint prevents your own Pods from scheduling on those nodes, improving the isolation.
  * When creating new node pools, prevent most GKE-managed workloads from running on those nodes by adding your own taint to those node pools.
  * Whenever you deploy new workloads to your cluster, such as when installing third-party tooling, audit the permissions that the Pods require. When possible, avoid deploying workloads that use elevated permissions to shared nodes.



## What's next

  * [Learn more about GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods).
  * [Learn about GKE Autopilot, which implements many GKE security features by default](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
