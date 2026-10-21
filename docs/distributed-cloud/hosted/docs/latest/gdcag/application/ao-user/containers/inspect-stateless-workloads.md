---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/inspect-stateless-workloads/
title: Inspect stateless workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:12:52.992501+00:00
---

# Inspect stateless workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/inspect-stateless-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Inspect stateless workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document explains how to inspect existing stateless workloads running in a Google Distributed Cloud (GDC) air-gapped Kubernetes cluster. Stateless workloads let you run your application deployment without having to store data or application state. You can view your stateless workloads with the GDC console or the kubectl CLI to monitor resource usage and workload health.

This document is for developers within the application operator group, who are responsible for managing application workloads for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to view and inspect stateless workloads. The roles you require depend on whether you are working within an organization-scoped shared cluster or project-scoped standard cluster. For more information, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

#### Shared cluster roles

Ask your Project IAM Admin to grant you the following roles in your project namespace based on the task to perform:

  * **Workload Viewer** (`workload-viewer`): view all workloads deployed to a shared cluster.
  * **Namespace Admin** (`namespace-admin`): create, delete, edit, or view workloads in a shared cluster project namespace.



These roles are bound to your project namespace.

#### Standard cluster roles

To create, delete, edit, or view workloads in a standard cluster, ask your Project IAM Admin to grant you the **Cluster Developer** (`cluster-developer`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against a [Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#cluster-architecture) using the API, make sure you have the following resources:

  * Locate the Kubernetes cluster name, or ask a member of the platform administrator group what the cluster name is.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster.

  * Use the kubeconfig path of the Kubernetes cluster to replace `KUBERNETES_CLUSTER_KUBECONFIG` in these instructions.




## View a project's container workloads

To view your project's container workloads, complete the following:

###  Console 

  * In the navigation menu, select **Kubernetes Engine > Workloads**.

You can view details for your container workloads, such as the following:

    * Name
    * Type
    * Number of pods
    * Kubernetes cluster
    * Last modified date

The container workloads are organized by which Kubernetes cluster they belong to. Select the **Cluster** drop-down to switch the cluster context.




###  kubectl 

  * Run the following command to list all pods in your project:
        
        kubectl get pods -n PROJECT_NAMESPACE
        

The output is similar to the following:
        
        NAME                        READY   STATUS    RESTARTS   AGE
        nginx-workload-ah-aa-1228   1/1     Running   0          12h
        nginx-workload-ah-ab-6784   1/1     Running   0          11h
        nginx-workload-ah-ac-0045   1/1     Running   0          12h
        




## Inspect the deployment

To request more detailed information about the components of a `Deployment` resource, run commands that directly target the entity you're looking to inspect.

### Get `Deployment` object information

To get detailed information about the `Deployment` object, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG -n NAMESPACE \
        describe deployment DEPLOYMENT_NAME
    

Replace the following:

  * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster running the deployment.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `DEPLOYMENT_NAME`: the name of the `Deployment` object.




### Display live configuration in YAML format

To view a `Deployment` object's manifest, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG -n NAMESPACE \
        get deployments DEPLOYMENT_NAME -o yaml
    

This command displays the `Deployment` object's live configuration in YAML format.

### List pods

To list the `Pod` objects created by the deployment, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG -n NAMESPACE \
        get pods -l KEY=VALUE
    

In this command, the `-l` flag lists all `Pod` objects with the specified key-value pair label in the specified cluster.

Replace the following:

  * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster running the deployment.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `KEY`: the key for the key-value pair label set in the deployment. For example, if the `.template.metadata.labels` field has the `app: myapp` label configured, the key is `app`.

  * `VALUE`: the value for the key-value pair label set in the deployment. For example, if the `.template.metadata.labels` field has the `app: myapp` label configured, the value is `my-app`.




For example, if you labeled the `Deployment` object `app: my-app`, you'd run the following command to see `Pod` objects with that label:
    
    
    kubectl --kubeconfig /tmp/kubeconfig.yaml -n my-namespace \
        get pods -l app=my-app
    

### Get specific pod information

To get information about a specific `Pod` object, run:
    
    
    kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG -n NAMESPACE \
        describe pod POD_NAME
    

Replace the following:

  * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster running the deployment.

  * `NAMESPACE`: the namespace. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

  * `POD_NAME`: the name of the pod managed by the deployment.




## What's next

  * [Update stateless workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/update-stateless-workloads)
  * [Scale stateless workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/scale-stateless-workloads)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
