---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/troubleshooting/
title: Troubleshoot common issues \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:07.586125+00:00
---

# Troubleshoot common issues  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/troubleshooting/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot common issues

This page shows you how to resolve common issues with GKE on Azure.

If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support). 

## Common error messages

The following sections explain the causes and resolutions for some common error messages.

### Server doesn't have a resource

Errors such as `error: the server doesn't have a resource type "services"` can happen when a cluster has no running node pools, or Connect gateway cannot connect to a node pool. To check the status of your node pools, run the following command:
    
    
    gcloud container azure node-pools list \
        --cluster-name CLUSTER_NAME \
        --location LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `LOCATION`: the Google Cloud location that manages your cluster



The output includes the status of your cluster's node pools. If you don't have a node pool listed, [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-node-pool).

### Forbidden user

The following error occurs when your username does not have administrator access to your cluster:
    
    
    Error from server (Forbidden): users "administrator@example.com" is forbidden:
    User "system:serviceaccount:gke-connect:connect-agent-sa" cannot impersonate
    resource "users" in API group "" at the cluster scope
    

You can configure additional users by passing the [`--admin-users`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/clusters/create#--admin-users) flag when you create a cluster.

If you use Connect gateway and can't connect to your cluster, try the following steps:

  1. Get the authorized users for your cluster.
         
         gcloud container azure clusters describe CLUSTER_NAME \
             --format 'value(authorization.admin_users)'
         

Replace `CLUSTER_NAME` with your cluster's name.

The output includes the usernames with administrator access to the cluster. For example:
         
         {'username': 'administrator@example.com'}
         

  2. Get the username currently authenticated with the Google Cloud CLI.
         
         gcloud config get-value account
         

The output includes the account authenticated with the Google Cloud CLI. If the output of the `gcloud containers azure clusters describe` and `gcloud config get-value account` don't match, run `gcloud auth login` and authenticate as the username with administrative access to the cluster.




## Issues with kubectl commands

The following sections provide guidance on how to resolve issues with unresponsive or failing `kubectl` commands.

### kubectl commands stop responding

If your cluster runs a Kubernetes version earlier than 1.25 and `kubectl` commands are unresponsive or time out, the most common reason is that you have not yet created a node pool. By default, GKE on Azure generates `kubeconfig` files that use Connect gateway as an internet-reachable endpoint. For this to work, the `gke-connect-agent` Deployment needs to be running in a node pool on the cluster.

For more diagnostic information, run the following command:
    
    
    kubectl cluster-info -v=9
    

If there are no running node pools, you see requests to `connectgateway.googleapis.com` fail with a 404 `cannot find active connections for cluster` error.

For clusters with a Kubernetes version of 1.25 or later, the `gke-connect-agent` runs on the control plane, and a node pool is not required. If the `kubectl` command is unresponsive, check the control plane component logs with [Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/cloud-logging#control_plane_logs).

### kubectl exec, attach, and port-forward commands fail

The `kubectl exec`, `kubectl attach`, and `kubectl port-forward` commands might fail with the message `error: unable to upgrade connection` when using Connect gateway. This is a limitation when using Connect gateway as your Kubernetes API Server endpoint.

To work around this, use a `kubeconfig` that specifies the cluster's private endpoint. For instructions on accessing the cluster through its private endpoint, see [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/configure-cluster-access-for-kubectl).

### Generic kubectl troubleshooting

If you use Connect gateway:

  * Ensure you have enabled Connect gateway in your Google Cloud project:
        
        gcloud services enable connectgateway.googleapis.com
        

  * For clusters with a Kubernetes version earlier than 1.25, ensure that you have at least one Linux node pool running and that the `gke-connect-agent` is running. For details, see [Troubleshoot cluster connections](https://docs.cloud.google.com/anthos/fleet-management/docs/troubleshooting).

  * For clusters with a Kubernetes version of 1.25 or later, check the `gke-connect-agent` logs with [Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/cloud-logging#control_plane_logs).




## What's next

  * If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
