---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/configure-for-high-availability/
title: Configure Policy Controller for high availability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:34.095649+00:00
---

# Configure Policy Controller for high availability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/configure-for-high-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Configure Policy Controller for high availability Stay organized with collections  Save and categorize content based on your preferences. 

You can set deployment-level configurations for Policy Controller that override resource requirements and configure parameters for high availability.

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce, and who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

To get a list of all configuration options, run `gcloud container fleet policycontroller deployment set --help`.

The commands on this page use the `--all-memberships` flag to apply a configuration to all clusters registered to a fleet. To apply a command to a single, registered cluster instead, use `--membership=MEMBERSHIP_NAME`, replacing `MEMBERSHIP_NAME` with the membership name of the registered cluster.

## Configure replica counts

You can configure your Policy Controller deployments for a [`ReplicaSet`](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) by setting a replica count.

**Note:** You can't set replica counts for audit deployments.

To set a replica count, run the following command:
    
    
    gcloud container fleet policycontroller deployment set DEPLOYMENT_TYPE replica-count QUANTITY \
      --all-memberships
    

Replace the following:

  * `DEPLOYMENT_TYPE`: the deployment type that you want to set a replica count for. The value is either `mutation` or `admission`.
  * `QUANTITY`: the number of replicas that you want to set, for example 3.



To remove a replica count, run the following command:
    
    
    gcloud container fleet policycontroller deployment remove DEPLOYMENT_TYPE replica-count \
      --all-memberships
    

Replace `DEPLOYMENT_TYPE` with the deployment type that you're removing the replicas from. This value is either `mutation` or `admission`.

## Set resource requirements

You can specify limits and requests for memory and CPU.

### Set memory limits and requests

To set a memory limit, run the following command:
    
    
    gcloud container fleet policycontroller deployment set DEPLOYMENT_TYPE memory-limit QUANTITY \
      --all-memberships
    

Replace the following:

  * `DEPLOYMENT_TYPE`: the deployment type that you want to set a memory limit on. One of the following values: `audit`, `mutation`, or `admission`.
  * `QUANTITY`: the quantity that you want to set with a [quantity suffix](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory), for example 4Gi.



To set a memory request, run the following command:
    
    
    gcloud container fleet policycontroller deployment set DEPLOYMENT_TYPE memory-request QUANTITY \
      --all-memberships
    

Replace the following:

  * `DEPLOYMENT_TYPE`: the deployment type that you want to set a memory request on. One of the following values: `audit`, `mutation`, or `admission`.
  * `QUANTITY`: the quantity that you want to set with a [quantity suffix](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory), for example 2Gi.



### Set CPU limits and requests

To set a CPU limit, run the following command:
    
    
    gcloud container fleet policycontroller deployment set DEPLOYMENT_TYPE cpu-limit QUANTITY \
      --all-memberships
    

Replace the following:

  * `DEPLOYMENT_TYPE`: the deployment type that you want to set a CPU limit on. One of the following values: `audit`, `mutation`, or `admission`.
  * `QUANTITY`: the [CPU quantity](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-cpu) that you want to set, for example 500m.



To set a CPU request, run the following command:
    
    
    gcloud container fleet policycontroller deployment set DEPLOYMENT_TYPE cpu-request QUANTITY \
      --all-memberships
    

Replace the following:

  * `DEPLOYMENT_TYPE`: the deployment type that you want to set a CPU request on. One of the following values: `audit`, `mutation`, or `admission`.
  * `QUANTITY`: the quantity that you want to set, for example 250m.



### Remove limits and requests

To remove a configuration, run the following command:
    
    
    gcloud container fleet policycontroller deployment remove DEPLOYMENT_TYPE RESOURCE_TYPE \
      --all-memberships
    

Replace the following:

  * `DEPLOYMENT_TYPE`: the deployment type that you're removing the request or limit on. One of the following values: `audit`, `mutation`, or `admission`.
  * `RESOURCE_TYPE`: the resource type that you want to remove. One of the following values: `memory-limit`, `memory-request`, `cpu-limit`, `cpu-request`.



## Configure tolerations

You can set [tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) on your Policy Controller deployments.

You can set a toleration with one of the following methods:

  * To set a toleration with a key, run the following command:
        
        gcloud container fleet policycontroller deployment set admission toleration KEY \
          --all-memberships
        

Replace `KEY` with your key value, for example `key1`.

  * To set a toleration with a key and value, run the following command:
        
        gcloud container fleet policycontroller deployment set admission toleration KEY=VALUE \
          --all-memberships
        

Replace the following:

    * `KEY`: your key value, for example `key1`.
    * `VALUE`: your key value, for example `value1`.
  * To set a toleration with a key and value, and the effect `NoSchedule`, run the following command:
        
        gcloud container fleet policycontroller deployment set admission toleration KEY=VALUE \
          --all-memberships \
          --effect=NoSchedule
        

Replace the following:

    * `KEY`: your key value, for example `key1`.
    * `VALUE`: your key value, for example `value1`.



If you need to edit a toleration, you must remove the existing toleration and then set a new toleration with one of the previous commands. To remove a toleration, run the previous command with `remove` instead of `set`, for example:
    
    
    gcloud container fleet policycontroller deployment remove admission toleration KEY=VALUE \
      --all-memberships
    

## Configure affinity

You can set [pod affinity](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/) on your Policy Controller deployments. The available settings are `anti` (corresponding to anti-affinity) and `none` (corresponding to no-affinity). For the `admissions` deployment, `anti` is the default. For all other deployments, `none` is the default.

To set pod anti-affinity, run the following command:
    
    
    gcloud container fleet policycontroller deployment set mutation pod-affinity anti \
      --all-memberships
    

To remove pod affinity, run the following command:
    
    
    gcloud container fleet policycontroller deployment set mutation pod-affinity none \
      --all-memberships
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
