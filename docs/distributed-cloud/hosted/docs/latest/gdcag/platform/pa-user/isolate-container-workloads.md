---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/isolate-container-workloads/
title: Isolate your workloads in dedicated node pools \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:50.987985+00:00
---

# Isolate your workloads in dedicated node pools  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/isolate-container-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Isolate your workloads in dedicated node pools Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

Dedicated node pools in Google Distributed Cloud (GDC) air-gapped let you isolate container workloads to strengthen Kubernetes cluster security and control pod placement. This separation helps reduce the risk of privilege escalation attacks. To set up dedicated pools, you apply taints and labels, match them with workload tolerations and node affinity rules, and verify scheduling.

This document is for IT administrators in the platform administrator group who manage Kubernetes clusters and developers in the application operator group who run containers. For more information, see [Node isolation overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/node-isolation-overview) and [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to isolate container workloads in your Kubernetes cluster. The roles you require depend on whether you are working within an organization-scoped shared cluster or project-scoped standard cluster. For more information, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

#### Shared cluster roles

Contact your IAM Org Admin to request the following roles to taint and label a node pool in a shared cluster:

  * **User Cluster Admin** (`user-cluster-admin`): create, delete, edit, or view the resources of a shared cluster hosted on the management API server. This role provides access to the node pools of the shared cluster.

  * **User Cluster Developer** (`user-cluster-developer`): create, delete, edit, or view a shared cluster. This role provides access to the data plane APIs hosted within the shared cluster.




These roles are not bound to a namespace.

#### Standard cluster roles

Contact your IAM Project Admin to request the following roles to taint and label a node pool in a standard cluster:

  * **Cluster Admin** (`cluster-admin`): create, delete, edit, or view all resources in a standard cluster. This role provides access to the data plane APIs hosted within the standard cluster that govern the cluster's resources.

  * **Cluster Developer** (`cluster-developer`): create, delete, edit, or view a standard cluster. This role provides access to the data plane APIs hosted within the standard cluster that govern the cluster.

  * **Standard Cluster Admin** (`standard-cluster-admin`): create, delete, edit, or view the resources of a standard cluster hosted on the management API server. This role provides access to the node pools of the standard cluster.




These roles are bound to your project namespace.

### Prepare your environment

To run commands against a [Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#cluster-architecture) using the API, make sure you have the following resources:

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster.

  * Use the kubeconfig path of the Kubernetes cluster to replace `KUBERNETES_CLUSTER_KUBECONFIG` in these instructions.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-resources-kubeconfig) the kubeconfig file for the management API server.

  * Use the kubeconfig path of the management API server to replace `MANAGEMENT_API_SERVER` in these instructions.

  * Choose a specific name for the node taint and the node label that you want to use for the dedicated node pools. For example, `workloadType=untrusted`.




## Taint and label a new node pool

When you apply a taint or a label to a new node pool, all nodes, including any nodes added later, will automatically get the specified taints and labels. You cannot remove a taint or label from a node pool after it's applied.

**Note:** To apply a taint or label to an existing node pool, you must manually apply the change to each existing node. Taints and labels don't auto-propagate to all nodes in an existing node pool. For more information, see Taint and label an existing node pool.

To add a taint and a label to a new node pool, complete the following steps:

  1. Edit the `nodePools` section of the `Cluster` custom resource directly when [creating the node pool](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools#add-a-node-pool):
         
         nodePools:
           # Several lines of code are omitted here.
           - machineTypeName: n2-standard-2-gdc
             name: nodepool-1
             nodeCount: 3
             taints:
             - key: "TAINT_KEY"
               value: "TAINT_VALUE"
               effect: "TAINT_EFFECT"
             labels:
               LABEL_KEY: LABEL_VALUE
         

Replace the following:

     * `TAINT_KEY`: the taint key portion of the key-value pair associated with a scheduling `TAINT_EFFECT`. For example, `workloadType`.
     * `TAINT_VALUE`: the taint value portion of the key-value pair associated with a scheduling `TAINT_EFFECT`. For example, `untrusted`.
     * `TAINT_EFFECT`: one of the following effect values: 
       * `NoSchedule`: pods that don't tolerate this taint are not scheduled on the node; existing pods are not evicted from the node.
       * `PreferNoSchedule`: Kubernetes avoids scheduling pods that don't tolerate this taint onto the node.
       * `NoExecute`: the pod is evicted from the node if it's already running on the node, and is not scheduled onto the node if it's not yet running on the node.
     * `LABEL_KEY: LABEL_VALUE`: the key-value pairs for the node labels, which correspond to the selectors that you specify in your workload manifests.
  2. Apply the `Cluster` resource to create the new node pool:
         
         kubectl apply -f cluster.yaml --kubeconfig MANAGEMENT_API_SERVER
         

Replace `MANAGEMENT_API_SERVER` with the zonal API server's kubeconfig path where the Kubernetes cluster is hosted.




## Taint and label an existing node pool

To apply a taint or label to an existing node pool, you must apply the changes to each existing node. You cannot dynamically update node pool configurations.

You cannot remove a taint or label from a node pool after it's applied.

To add a taint and label to an existing node pool, complete the following steps:

  1. List the nodes in the dedicated node pool:
         
         kubectl get node --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG \
             -l baremetal.cluster.gke.io/node-pool=NODE_POOL_NAME
         

Replace the following variables:

     * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig path for the Kubernetes cluster.
     * `NODE_POOL_NAME`: the name of your dedicated node pool.

Note each node ID of all the nodes in the node pool from the output.

  2. For each node in the node pool, apply the taints:
         
         kubectl taint nodes NODE_ID \
             TAINT_KEY=TAINT_VALUE:TAINT_EFFECT \
             --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG
         

Replace the following variables:

     * `NODE_ID`: the ID of the worker node in the dedicated node pool.
     * `TAINT_KEY=TAINT_VALUE`: a key-value pair associated with a scheduling `TAINT_EFFECT`. For example, `workloadType=untrusted`.
     * `TAINT_EFFECT`: one of the following effect values: 
       * `NoSchedule`: pods that don't tolerate this taint are not scheduled on the node; existing pods are not evicted from the node.
       * `PreferNoSchedule`: Kubernetes avoids scheduling pods that don't tolerate this taint onto the node.
       * `NoExecute`: the pod is evicted from the node if it's already running on the node, and is not scheduled onto the node if it's not yet running on the node.
     * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig path for the Kubernetes cluster.
  3. For each node in the node pool, apply the labels that correspond with the selectors you'll define in your container workloads:
         
         kubectl label NODE_ID \
             LABEL_KEY:LABEL_VALUE \
             --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG
         

Replace the following variables:

     * `NODE_ID`: the ID of the worker node in the dedicated node pool.
     * `LABEL_KEY:LABEL_VALUE`: the key-value pairs for the node labels, which correspond to the selectors that you specify in your workload manifests.
     * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig path for the Kubernetes cluster.



## Add a toleration and a node affinity rule

After you taint the dedicated node pool, no workloads can schedule on it unless they have a toleration corresponding to the taint you added. Add the toleration to the specification for your workloads to let those pods schedule on your tainted node pool.

If you labeled the dedicated node pool, you can also add a node affinity rule to tell GDC to only schedule your workloads on that node pool.

To configure your container workload to run in the dedicated node pool, complete the following steps:

  1. Add the following sections to the `.spec.template.spec` section of your container workload manifest file, such as a `Deployment` custom resource:
         
         tolerations:
         - key: TAINT_KEY
           operator: Equal
           value: TAINT_VALUE
           effect: TAINT_EFFECT
         affinity:
           nodeAffinity:
             requiredDuringSchedulingIgnoredDuringExecution:
               nodeSelectorTerms:
               - matchExpressions:
                 - key: LABEL_KEY
                   operator: In
                   values:
                   - "LABEL_VALUE"
         

Replace the following:

     * `TAINT_KEY`: the taint key that you applied to your dedicated node pool.
     * `TAINT_VALUE`: the taint value that you applied to your dedicated node pool.
     * `TAINT_EFFECT`: one of the following effect values: 
       * `NoSchedule`: pods that don't tolerate this taint are not scheduled on the node; existing pods are not evicted from the node.
       * `PreferNoSchedule`: Kubernetes avoids scheduling pods that don't tolerate this taint onto the node.
       * `NoExecute`: the pod is evicted from the node if it's already running on the node, and is not scheduled onto the node if it's not yet running on the node.
     * `LABEL_KEY`: the node label key that you applied to your dedicated node pool.
     * `LABEL_VALUE`: the node label value that you applied to your dedicated node pool.

For example, the following `Deployment` resource adds a toleration for the `workloadType=untrusted:NoExecute` taint and a node affinity rule for the `workloadType=untrusted` node label:
    
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
        spec:
          tolerations:
          - key: workloadType
            operator: Equal
            value: untrusted
            effect: NoExecute
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: workloadType
                    operator: In
                    values:
                    - "untrusted"
          containers:
          - name: my-app
            image: harbor-1.org-1.zone1.google.gdc.test/harborproject/my-app
            ports:
            - containerPort: 80
          imagePullSecrets:
          - name: SECRET
    

  2. Update your container workload:
         
         kubectl apply -f deployment.yaml -n NAMESPACE \
             --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG
         

Replace the following variables:

     * `NAMESPACE`: the namespace of your container workload. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.
     * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig path for the Kubernetes cluster.



GDC recreates the affected pods. The node affinity rule forces the pods onto the dedicated node pool that you created. The toleration allows only those pods to be placed on the nodes.

## Verify that the separation works

Verify that the pods you designated are running on the labelled node pool.

  * List the pods in the given namespace:
        
        kubectl get pods -o=wide -n NAMESPACE \
            --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG
        

Replace the following variables:

    * `NAMESPACE`: the namespace of your container workload. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.
    * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig path for the Kubernetes cluster.

The output looks similar to the following:
    
    pod/kube-abc-12tyuj
    pod/kube-abc-39oplef
    pod/kube-abc-95rzkap
    

Confirm that your workloads are running in the dedicated node pool.




## What's next

  * [Container workloads in GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)
  * [Deploy a highly available container application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-container-app)
  * [Kubernetes workloads for HA](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/enhance-kubernetes-ha)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
