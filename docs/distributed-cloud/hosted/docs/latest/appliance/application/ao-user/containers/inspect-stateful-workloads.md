---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/inspect-stateful-workloads/
title: Inspect stateful workloads \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:30.462829+00:00
---

# Inspect stateful workloads  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/inspect-stateful-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Inspect stateful workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to inspect existing stateful workloads running in a Google Distributed Cloud (GDC) air-gapped appliance Kubernetes cluster. Stateful workloads let you run your application with persistent container storage. You can view your stateful workloads with the GDC console or the kubectl CLI to monitor resource usage and workload health.

This page is for developers within the application operator group, who are responsible for managing application workloads for their organization.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

Ask your Organization IAM Admin to grant you the following roles in your project namespace based on the task to perform:

  * **Workload Viewer** (`workload-viewer`): view all workloads deployed to a cluster.
  * **Namespace Admin** (`namespace-admin`): create, delete, edit, or view workloads in a cluster project namespace.



### Prepare your environment

To run commands against the pre-configured bare metal Kubernetes cluster, make sure you have the following resources:

  1. Locate the Kubernetes cluster name, or ask your Platform Administrator what the cluster name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster if you don't have one.

  3. Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## View a project's container workloads

Run the following command to list all pods in your project:
    
    
    kubectl get pods -n PROJECT_NAMESPACE
    

The output is similar to the following:
    
    
    NAME                        READY   STATUS    RESTARTS   AGE
    nginx-workload-ah-aa-1228   1/1     Running   0          12h
    nginx-workload-ah-ab-6784   1/1     Running   0          11h
    nginx-workload-ah-ac-0045   1/1     Running   0          12h
    

## Inspect a `StatefulSet` resource

To request more detailed information about the components of a `StatefulSet` resource, run commands that directly target the entity you're looking to inspect.

### Get `StatefulSet` object information

To get detailed information about the `StatefulSet` object, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        describe statefulset STATEFULSET_NAME
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the `StatefulSet` object.

  * `NAMESPACE`: the project namespace.

  * `STATEFULSET_NAME`: the name of the `StatefulSet` object.




### Display live configuration in YAML format

To display the live configuration of the `StatefulSet` resource in YAML format, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        get statefulset STATEFULSET_NAME -o yaml
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the `StatefulSet` object.

  * `NAMESPACE`: the project namespace.

  * `STATEFULSET_NAME`: the name of the `StatefulSet` object.




### List pods

To list the `Pod` objects created by the `StatefulSet`, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        get pods -l app=APP_NAME
    

In this command, the `-l` flag lists all `Pod` objects labeled with `APP_NAME`.

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the `StatefulSet` object.

  * `NAMESPACE`: the project namespace.

  * `APP_NAME`: the name of the stateful application managed by the `StatefulSet` object.




### Get specific pod information

To get information about a specific `Pod` in the cluster, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        describe pod POD_NAME
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the pod.

  * `NAMESPACE`: the project namespace.

  * `POD_NAME`: the name of the pod managed by the `StatefulSet` object.




### List PVCs

To list the `PersistentVolumeClaim` (PVC) objects in the cluster, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        get pvc
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file of the Kubernetes cluster running the PVCs.

  * `NAMESPACE`: the project namespace.




### Get specific PVC information

To get information about a specific `PersistentVolumeClaim` (PVC) in the cluster, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        describe pvc PVC_NAME
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the PVC.

  * `NAMESPACE`: the project namespace.

  * `PVC_NAME`: the name of the PVC configured for the `StatefulSet` object.




### Get PV information

To get information about a specific `PersistentVolume` (PV) in the cluster, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        describe pv PV_NAME
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster running the PV.

  * `NAMESPACE`: the project namespace.

  * `PV_NAME`: the name of the PV configured for the `StatefulSet` object.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
