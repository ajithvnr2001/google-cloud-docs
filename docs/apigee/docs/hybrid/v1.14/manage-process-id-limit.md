---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/manage-process-id-limit/
title: Manage process ID limits \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:10:56.674205+00:00
---

# Manage process ID limits  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/manage-process-id-limit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage process ID limits Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/manage-process-id-limit.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/manage-process-id-limit.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/manage-process-id-limit.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/manage-process-id-limit.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/manage-process-id-limit.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/manage-process-id-limit.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/manage-process-id-limit.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/manage-process-id-limit.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/manage-process-id-limit.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/manage-process-id-limit.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/manage-process-id-limit.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/manage-process-id-limit.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/manage-process-id-limit.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/manage-process-id-limit.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/manage-process-id-limit.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/manage-process-id-limit.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/manage-process-id-limit.html)



## Overview

A **Process ID** (**PID**) limit is a Kubernetes resource constraint on nodes and pods to prevent excessive process creation, which can impact node stability. Apigee Hybrid supports the Kubernetes feature to set process ID limits. This document provides instructions on how to set these limits, with recommendations for values for Apigee services on specific platforms. 

When Apigee hybrid users manage their own clusters, setting PID limits in Kubernetes can improve system stability, security, and resource management. This is also consistent with Kubernetes best practices. 

**Note:** Setting the PID limit can potentially impact system performance if the limit is too low and restraints the pod from starting. With the recommended limits, the Apigee performance shall not be impacted.

### Definitions of process ID limits

Process ID limits include Node PID limits and Pod PID limits. 

Node PID limits include Kube-reserved PIDs and system-reserved PIDs. The total number of allocatable PIDs is the Kernel max minus the kube-reserved PIDs minus the system-reserved PIDs minus the eviction threshold PIDs: 

Kernel max ID limits  
---  
  
**-** Kube reserved
  
  
**-** System reserved
  
  
**-** Eviction threshold
  
= Allocatable  
  
  * **Kernel max ID limits** : Determined by the operating system and its kernel settings. Since Apigee Hybrid runs exclusively on a Linux kernel, this guide discusses Linus-based limits on Kubernetes nodes. The max number of process ID limits for a Linux kernel is 4194304.
  * **Kube-reserved** and **system-reserved** : For resource reservation for Kubernetes or OS system daemons.
  * **Eviction threshold** : The limit that signals pressure on the node. The node will be evicted when the threshold is met. See [PID based eviction](https://kubernetes.io/docs/concepts/policy/pid-limiting/#pid-based-eviction) for more details.
  * **Allocatable** : The number of PIDs available. See [Kubernetes: Node Allocatable](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#node-allocatable) for more information. Kube-reserved and system-reserved can be configured with Node PID limit settings.



The pod PID limit can be configured for the node and shared across all pods within the node.

## Prepare to manage the process ID limits

These procedures uses the following environment variables:
    
    
    export PROJECT_ID=MY_PROJECT_ID
    export CLUSTER_NAME=MY_CLUSTER_NAME
    export LOCATION=MY_CLUSTER_LOCATION
    export APIGEE_NAMESPACE=MY_APIGEE_NAMESPACE # Default: apigee
    

### Verify access

Before configuring the process ID limit, ensure that you have access to edit Kubernetes clusters.

The following steps are for installations on GKE. For other platforms, see the documentation for your platform.

  1. Check if you have roles/container.clusterAdmin in the IAM policy: 
         
         gcloud projects get-iam-policy ${PROJECT_ID}  \
          --flatten="bindings[].members" \
          --format='table(bindings.role)' \
          --filter="bindings.members:your_account_email"
         

  2. If you do not have the access, add the role to your account: 
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
          --member user:your_account_email \
          --role roles/container.clusterAdmin




### Verify Existing PID Limits

Verify whether the node has existing PID limits before configuring new limits.

  1. Get a node from the cluster to check values. You will need to check nodes from both the `apigee-data` and `apigee-runtime` node pools: 
         
         kubectl get nodes -n ${APIGEE_NAMESPACE}
         

Your output should look similar to the following:
         
         NAME                                      STATUS   ROLES    AGE    VERSION
         gke-my-hybrid-apigee-data-0a1b2c3d-efgh      Ready       2d8h   v1.31.5-gke.1169000
         gke-my-hybrid-apigee-runtime-1b2c3d4e-fghi   Ready       2d8h   v1.31.5-gke.1169000
         

  2. Export the node name from the output of the previous step. Run this the next step first for an `apigee-data` node and again for an `apigee-runtime` node: 

### Code
         
         export NODE_NAME=MY_NODE_NAME
         

### Example
         
         export NODE_NAME="gke-my-hybrid-apigee-data-0a1b2c3d-efgh"
         

  3. Check the **node** PID limits. Use the following commands to check the reserved values. If the value is null, the value is not configured: 
         
         kubectl get --raw "/api/v1/nodes/${NODE_NAME}/proxy/configz" | jq '.kubeletconfig.kubeReserved'
         kubectl get --raw "/api/v1/nodes/${NODE_NAME}/proxy/configz" | jq '.kubeletconfig.systemReserved'
         kubectl get --raw "/api/v1/nodes/${NODE_NAME}/proxy/configz" | jq '.kubeletconfig.evictionHard'
         

  4. Check the **pod** PID limit. Use the following command to check the existing pod PID limit. If the returned value is `-1` or empty, the limit is not set: 
         
         kubectl get --raw "/api/v1/nodes/${NODE_NAME}/proxy/configz" | jq '.kubeletconfig.podPidsLimit'
         




## Manage the process ID limits

### Manage the Node PID limits

For installations on GKE, the infrastructure resources of Kubernetes nodes are managed internally and you do not need to configure them. The current capacity and allocatable resources can be viewed following [Node allocatable resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#check_allocatable_resources_on_a_node) in the Google Kubernetes Engine documentation. 

For non-GKE platforms, refer to corresponding Kubernetes documentation for the platform. If the cluster/node is user-managed (as opposed to Fully-managed), the kube-reserved PID limit and system-reserved PID limit can be configured with Kubelet. See [Node PID limits](https://kubernetes.io/docs/concepts/policy/pid-limiting/#node-pid-limits) in the Kubernetes documentation. 

#### Tooling

This procedure uses Kubelet to manage the process ID limit. Kubelet is the agent that runs on pods and containers that ensures they are running according to their PodSpec. If you need to install Kubelet, follow the instructions in the Kubernetes documentation: [Installing kubeadm, kubelet and kubectl](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/#installing-kubeadm-kubelet-and-kubectl).

#### Procedure

  1. Create a Kubelet configuration file called `kubelet-config.yaml`. 
         
         apiVersion: kubelet.config.k8s.io/v1beta1
         kind: KubeletConfiguration
         kubeReserved:
          pid: PID_VALUE # Example: 1000
         

See more info on the configurations: [Kube Reserved](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/#kube-reserved) in the Kubernetes documentation.

  2. Apply the Kubelet configuration: 
         
         kubelet --config PATH_TO_KUBELET_CONFIG_YAML
         




### Manage the Pod PID limits

#### Choosing the Limit

If the PID limit is set too low, it can prevent a pod from starting up. If it is set too high, it can fail to detect resource misbehaviors. When selecting the appropriate limit, it is important to consider the previous behavior of the node and any service-specific requirements. 

GKE has a required range for the value: [1024, 4194304]. On GKE Platforms you can see the status of your Kubernetes service accounts in the Google Cloud console **Metrics Explorer**. Select **Kubernetes Node - PID usage** metrics and apply filters. This metrics shows the recent usage of process IDs and can be referenced when choosing a PID limit. 

[Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

On non-GKE platforms, different monitoring options may be available. Please refer to the corresponding platform's Kubernetes documentation to check the metrics. 

#### Process ID requirements for Apigee pods

Apigee Hybrid uses 2 node pools, apigee-data and apigee-runtime. Since some of the Apigee components are deployed in both node pools, the Pod PID limit shall be the same for the two node pools. The Pod PID limit should also be higher than the maximum number of PIDs required across all Apigee pods. The required Apigee Pod PID limit is 1000, which is below the minimum required number for GKE platforms. 

#### Recommended Pod PIDs Limit

Some platforms enforce a minimum value requirement for the number of the Pod PIDs limit, in which case the min value requirement is selected. 

Platform | Min Pod PID Limit  
---|---  
GKE on Google Cloud | 1024  
Google Distributed Cloud (software only) on VMware | 1024  
Google Distributed Cloud (software only) on bare metal | 1024  
EKS | 1000  
AKS | 1000  
OpenShift | 1000  
Rancher Kubernetes Engine (RKE) | 1000  
  
#### Procedure

The procedures for managing the Pod PID limits are different for GKE and non-GKE platforms. 

### GKE platform

GKE platform that supports PID limit update includes: 

  * GKE on Google Cloud: see [gcloud container node-pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools).
  * Google Distributed Cloud (software only) on VMware: see [gcloud container vmware node-pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools)
  * Google Distributed Cloud (software only) on bare metal: see [gcloud container bare-metal node-pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/node-pools)



The Pod PID limit is controlled by [Node system configurations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#using_a_node_system_configuration). GKE has a required range for the value: [1024, 4194304]. For more information, see [NodeKubeletConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeKubeletConfig). 

  1. Create a node system configuration called `node-config.yaml` with designated pod PID limit with the following contents: 
         
         kubeletConfig:
          podPidsLimit: POD_PID_VALUE # Example: 1024
         

  2. Apply the configuration to both the apigee `apigee-data` and `apigee-runtime` node pools. When you apply the configuration, the node will start rollout with one of the zero-downtime [Node upgrade strategies](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies). 
         
         gcloud container OPTIONAL_HOST_PLATFORM node-pools update NODE_POOL_NAME \
            --cluster CLUSTER_NAME \
            --region CLUSTER_LOCATION \
            --system-config-from-file=node-config.yaml \
            --project PROJECT_ID
         

**Note:** You can apply this configuration at different stages of cluster creation. See [Adding the configuration to a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#add).



### Non-GKE platforms

For non-GKE platforms, the Pod PID limit is controlled by Kubelet. The limit is set by the `podPidsLimit` field in the Kubelet configuration file. 

  1. Create a Kubelet configuration file called `kubelet-config.yaml` with the following contents: 
         
         apiVersion: kubelet.config.k8s.io/v1beta1
         kind: KubeletConfiguration
         podPidsLimit: POD_PID_VALUE # Example: 1024
         

  2. Apply the configuration. Setting the podPidsLimit requires rebooting the affected node, which could incur downtime: 
         
         kubelet --config PATH_TO_KUBELET_CONFIG_YAML
         

  3. Verify the configuration. See Verify Existing PID Limits for instructions. 



Pod PID limits configuration commands and tooling recommendations are different across various platforms. Refer to documentation of respective platforms for detailed commands. Below are some documentation links of non-GKE platforms for reference. Note that they are subject to changes: 

Platform | Documentation  
---|---  
EKS | [Customize managed nodes with launch templates](https://docs.aws.amazon.com/eks/latest/userguide/launch-templates.html)  
AKS | [Customize node configuration for Azure Kubernetes Service (AKS) node pools](https://learn.microsoft.com/en-us/azure/aks/custom-node-configuration?tabs=linux-node-pools)  
OpenShift | [Risks of setting higher process ID limits for Red Hat OpenShift Service on AWS pods](https://docs.openshift.com/rosa/rosa_cluster_admin/rosa-configuring-pid-limits.html#risks-setting-higher-process-id-limits_rosa-configuring-pid-limits)  
Rancher Kubernetes Engine (RKE) | [Access a Cluster with Kubectl and kubeconfig](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/manage-clusters/access-clusters/use-kubectl-and-kubeconfig)  
  
## Troubleshooting process ID limits

### Pod stuck in `Pending` status with a `FailedScheduling` error

When the Node or Pod PIDs limit evicts or restricts a pod from starting up, the pod will be stuck in `Pending` status and fail with `FailedScheduling` error.

  1. Get the Node column: 
         
         kubectl get pods -n ${APIGEE_NAMESPACE} ${POD_NAME} -o wide
         

  2. Check if there's a `PIDPressure` condition: 
         
         kubectl describe node -n apigee ${NODE_NAME} | grep PIDPressure
         

  3. Alternatively, check `ApigeeDeployment` of the corresponding pod. Get the `ApigeeDeployment` from the result that has the same prefix as the erroring pod. 
         
         kubectl get ApigeeDeployment -n ${APIGEE_NAMESPACE}
         

  4. Check if the recent `Events` has PID-related error messages: 
         
         kubectl describe ApigeeDeployment -n ${APIGEE_NAMESPACE} ${APIGEE_DEPLOYMENT_NAME}
         

  5. If the cause is confirmed to be PID limit, follow the steps in Manage the Node PID limits to update the PID limit to a higher value. 



### Invalid `podPidsLimit`

When setting the limit for GKE, if the `podPidsLimit` is beyond limit, error will prompt: 
    
    
    ERROR: (gcloud.container.node-pools.update) ResponseError: code=400, message=Invalid podPidsLimit : value must be 1024 <= podPidsLimit <= 4194304.
    

Update the podPidsLimit value to within the required range.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
