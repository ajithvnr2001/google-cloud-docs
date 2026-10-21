---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-kubectl/
title: Investigate a cluster's state with kubectl \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:00:11.845601+00:00
---

# Investigate a cluster's state with kubectl  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-kubectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Investigate a cluster's state with kubectl Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Diagnosing the root cause of Google Kubernetes Engine (GKE) issues often requires inspecting the live state, configuration, and events of your Kubernetes resources in detail. To move beyond surface-level symptoms, you need tools to directly query and interact with the cluster's control plane.

Use this page to learn essential `kubectl` commands for investigating the live state of your cluster. Learning these commands lets you gather detailed information directly from the Kubernetes control plane, helping you understand _why_ a problem is occurring.

This information is important for Platform admins and operators who need to perform in-depth cluster health checks, manage resources, and troubleshoot infrastructure issues at a granular level. It's also essential for Application developers for debugging application behavior, inspecting Pod logs and events, and verifying the exact state of their deployments within the Kubernetes environment. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

Before you start, perform the following tasks:

  * [Install kubectl](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_kubectl).
  * Configure the `kubectl` command-line tool to communicate with your cluster:
        
        gcloud container clusters get-credentials CLUSTER_NAME \
            --location=LOCATION
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * Review your permissions. To see if you have the required permissions to run `kubectl` commands, use the `kubectl auth can-i` command. For example, to see if you have permission to run `kubectl get nodes`, run the `kubectl auth can-i get nodes` command.

If you have the required permissions, the command returns `yes`; otherwise, the command returns `no`.

If you lack permission to run a `kubectl` command, you might see an error message similar to the following:
        
        Error from server (Forbidden): pods "POD_NAME" is forbidden: User
        "USERNAME@DOMAIN.com" cannot list resource "pods" in API group "" in the
        namespace "default"
        

If you don't have the required permissions, ask your cluster administrator to assign the necessary roles to you.




## Get an overview of what's running

The `kubectl get` command helps you to see an overall view of what's happening in your cluster. Use the following commands to see the status of two of the most important cluster components, nodes and Pods:

  1. To check if your nodes are healthy, view details about all nodes and their statuses:
         
         kubectl get nodes
         

The output is similar to the following:
         
         NAME                                        STATUS   ROLES    AGE     VERSION
         
         gke-cs-cluster-default-pool-8b8a777f-224a   Ready    <none>   4d23h   v1.32.3-gke.1785003
         gke-cs-cluster-default-pool-8b8a777f-egb2   Ready    <none>   4d22h   v1.32.3-gke.1785003
         gke-cs-cluster-default-pool-8b8a777f-p5bn   Ready    <none>   4d22h   v1.32.3-gke.1785003
         

Any status other than `Ready` requires additional investigation.

  2. To check if your Pods are healthy, view details about all Pods and their statuses:
         
         kubectl get pods --all-namespaces
         

The output is similar to the following:
         
         NAMESPACE   NAME       READY   STATUS      RESTARTS   AGE
         kube-system netd-6nbsq 3/3     Running     0          4d23h
         kube-system netd-g7tpl 3/3     Running     0          4d23h
         

Any status other than `Running` requires additional investigation. Here are some common statuses that you might see:

     * `Running`: a healthy, running state.
     * `Pending`: the Pod is waiting to be scheduled on a node.
     * `CrashLoopBackOff`: the containers in the Pod are repeatedly crashing in a loop because the app starts, exits with an error, and is then restarted by Kubernetes.
     * `ImagePullBackOff`: the Pod can't pull the container image.



The preceding commands are only two examples of how you can use the `kubectl get` command. You can also use the command to learn more about many types of Kubernetes resources. For a full list of the resources that you can explore, see [kubectl get](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/) in the Kubernetes documentation.

**Tip:** Add `-o wide` to your `kubectl get` commands to see additional information about your resources. For example, the `kubectl get nodes -o wide` command adds the following columns to the output: `Internal-IP`, `External-IP`, `OS-Image`, `Kernel-Version`, and `Container-Runtime`.

## Learn more about specific resources

After you identify a problem, you need to get more details. An example of a problem could be a Pod that doesn't have a status of `Running`. To get more details, use the `kubectl describe` command.

For example, to describe a specific Pod, run the following command:
    
    
    kubectl describe pod POD_NAME -n NAMESPACE_NAME
    

Replace the following:

  * `POD_NAME`: the name of the Pod experiencing issues.
  * `NAMESPACE_NAME`: the namespace that the Pod is in. If you're not sure what the namespace is, review the `Namespace` column from the output of the `kubectl get pods` command.



The output of the `kubectl describe` command includes detailed information about your resource. Here are some of the most helpful sections to review when you troubleshoot a Pod:

  * `Status`: the current status of the Pod.
  * `Conditions`: the overall health and readiness of the Pod.
  * `Restart Count`: how many times the containers in the Pod have restarted. High numbers can be a cause of concern.
  * `Events`: a log of important things that have happened to this Pod, like being scheduled to a node, pulling its container image, and whether any errors occurred. The `Events` section is often where you can find the direct clues to why a Pod is failing.



Like the `kubectl get` command, you can use the `kubectl describe` command to learn more about multiple types of resources. For a full list of the resources that you can explore, see [kubectl describe](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe/) in the Kubernetes documentation.

## What's next

  * Read [Conduct historical analysis with Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-logging) (the next page in this series).

  * See these concepts applied in the [example troubleshooting scenario](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/introduction-example).

  * For advice about resolving specific problems, review [GKE's troubleshooting guides](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
