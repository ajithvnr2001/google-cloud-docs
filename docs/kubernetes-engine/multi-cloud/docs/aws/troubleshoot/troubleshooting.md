---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshoot/troubleshooting/
title: Troubleshoot common issues \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:12.630274+00:00
---

# Troubleshoot common issues  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshoot/troubleshooting/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Troubleshoot common issues Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve common issues with GKE on AWS.

If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/getting-support). 

## Common error messages

The following sections explain the causes and resolutions for some common error messages.

### Server doesn't have a resource

Errors such as `error: the server doesn't have a resource type "services"` can happen when a cluster has no running node pools, or Connect gateway cannot connect to a node pool. To check the status of your node pools, run the following command:
    
    
    gcloud container aws node-pools list \
        --cluster-name CLUSTER_NAME \
        --location LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `LOCATION`: the Google Cloud location that manages your cluster



The output includes the status of your cluster's node pools. If you don't have a node pool listed, [Create a node pool](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-node-pool).

### Forbidden user

The following error occurs when your username does not have administrator access to your cluster:
    
    
    Error from server (Forbidden): users "administrator@example.com" is forbidden:
    User "system:serviceaccount:gke-connect:connect-agent-sa" cannot impersonate
    resource "users" in API group "" at the cluster scope
    

You can configure additional users by passing the [`--admin-users`](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create#--admin-users) flag when you create a cluster.

If you use Connect gateway and can't connect to your cluster, try the following steps:

  1. Get the authorized users for your cluster.
         
         gcloud container aws clusters describe CLUSTER_NAME \
             --format 'value(authorization.admin_users)'
         

Replace `CLUSTER_NAME` with your cluster's name.

The output includes the usernames with administrator access to the cluster. For example:
         
         {'username': 'administrator@example.com'}
         

  2. Get the username currently authenticated with the Google Cloud CLI.
         
         gcloud config get-value account
         

The output includes the account authenticated with the Google Cloud CLI. If the output of the `gcloud containers aws clusters describe` and `gcloud config get-value account` don't match, run `gcloud auth login` and authenticate as the username with administrative access to the cluster.




## Issues with kubectl commands

The following sections provide guidance on how to resolve issues with unresponsive or failing `kubectl` commands.

### kubectl commands stop responding

If your cluster runs a Kubernetes version earlier than 1.25 and `kubectl` commands are unresponsive or time out, the most common reason is that you have not yet created a node pool. By default, GKE on AWS generates `kubeconfig` files that use Connect gateway as an internet-reachable endpoint. For this to work, the `gke-connect-agent` Deployment needs to be running in a node pool on the cluster.

For more diagnostic information, run the following command:
    
    
    kubectl cluster-info -v=9
    

If there are no running node pools, you see requests to `connectgateway.googleapis.com` fail with a 404 `cannot find active connections for cluster` error.

For clusters with a Kubernetes version of 1.25 or later, the `gke-connect-agent` runs on the control plane, and a node pool is not required. If the `kubectl` command is unresponsive, check the control plane component logs with [Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/cloud-logging#control_plane_logs).

### kubectl exec, attach, and port-forward commands fail

The `kubectl exec`, `kubectl attach`, and `kubectl port-forward` commands might fail with the message `error: unable to upgrade connection` when using Connect gateway. This is a limitation when using Connect gateway as your Kubernetes API Server endpoint.

To work around this, use a `kubeconfig` that specifies the cluster's private endpoint. For instructions on accessing the cluster through its private endpoint, see [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cluster-access-for-kubectl).

### kubectl logs fails with remote error: tls: internal error

This issue might happen when the [Control Plane API Role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_the_control_plane_role) is missing a permission. For example, this can happen if your AWS role is missing the`ec2:DescribeDhcpOptions` permission. In this case, certificate signing requests from nodes can't be approved, and the worker node lacks a valid certificate.

To determine if this is the problem, you can check if there are pending Certificate Signing Requests that have not been approved with this command:
    
    
    kubectl get csr
    

To resolve this, [verify that your AWS role matches the requirements](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshooting/create-update#authorization-error).

### Generic kubectl troubleshooting

If you use Connect gateway:

  * Ensure you have enabled Connect gateway in your Google Cloud project:
        
        gcloud services enable connectgateway.googleapis.com
        

  * For clusters with a Kubernetes version earlier than 1.25, ensure that you have at least one Linux node pool running and that the `gke-connect-agent` is running. For details, see [Troubleshoot cluster connections](https://docs.cloud.google.com/anthos/fleet-management/docs/troubleshooting).

  * For clusters with a Kubernetes version of 1.25 or later, check the `gke-connect-agent` logs with [Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/cloud-logging#control_plane_logs).




## Kubernetes Service (LoadBalancer) or Kubernetes Ingress don't work

If your AWS Elastic Load Balancers (ELB/NLB/ALB) were created but aren't operating as you expected, this might be due to problems with subnet tagging. For more information, see [Load balancer subnets](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancer-subnets#troubleshooting).

## Pods on Arm nodes crashing

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following issue occurs when you deploy a Pod on an Arm node, but the container image isn't built for Arm architecture.

To identify the issue, complete the following tasks:

  1. Get the status of your Pods:
         
         kubectl get pods
         

  2. Get the logs for the crashing Pod:
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of the crashing Pod.

The error message in your Pod logs is similar to the following:
         
         exec ./hello-app: exec format error
         




To resolve this issue, ensure that your container image supports Arm architecture. As a best practice, build multiple architecture images.

## Cannot delete cluster

If you receive an error similar to the following when you try to delete a cluster, your GKE Multi-Cloud API role might not exist:
    
    
    ERROR: (gcloud.container.aws.clusters.delete) FAILED_PRECONDITION: Could not
    assume role
    "arn:aws:iam::ACCOUNT_NUMBER:role/gke123456-anthos-api-role"
    through service account
    "service-123456789@gcp-sa-gkemulticloud.iam.gserviceaccount.com".
    Please make sure the role has a trust policy allowing the GCP service agent to
    assume it: WebIdentityErr failed to retrieve credentials
    

To fix the problem, follow the steps at [Create GKE Multi-Cloud API role](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles#create_role). When you re-create the role with the same name and permissions, you can re-try the command.

## What's next

  * If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/getting-support). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
