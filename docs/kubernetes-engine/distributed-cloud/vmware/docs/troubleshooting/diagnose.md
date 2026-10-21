---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose/
title: Diagnose cluster issues \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:59.266218+00:00
---

# Diagnose cluster issues  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Diagnose cluster issues Stay organized with collections  Save and categorize content based on your preferences. 

The `gkectl` tool has two commands for troubleshooting issues with clusters: `gkectl diagnose cluster` and `gkectl diagnose snapshot`. The commands work with both admin and user clusters. This document shows how to use the `gkectl diagnose` command to diagnose issues in your clusters.

Note the following limitation with advanced clusters:

  * Version 1.31: the `gkectl diagnose` commands aren't supported on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field).
  * Version 1.32 and higher: the `gkectl diagnose` commands are supported on advanced clusters.



For more information how to use the `gkectl diagnose snapshot` command to create snapshots that can help Cloud Customer Care diagnose issues, see [Create snapshots to diagnose clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/snapshots).

**Tip:** After running a `gkectl diagnose` command, use [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) ([Preview](https://cloud.google.com/products#product-launch-stages)) to help you understand the output. For example, you can paste the generated report or specific error messages into Gemini Cloud Assist, and ask it to explain the potential causes of any issues and recommend next steps.

## `gkectl diagnose cluster`

This command performs health checks on your cluster and reports errors. The command runs health checks on the following components:

  * vCenter 
    * Credential
    * DRS
    * Anti-affinity groups
    * Network
    * Version
    * Datacenter
    * Datastore
    * ResourcePool
    * Folder
    * Network
  * Load balancer (F5, Seesaw, or Manual)
  * User cluster and node pools
  * Cluster objects
  * Konnectivity server readiness of the user cluster
  * Machine objects and the corresponding cluster nodes
  * Pods in the `kube-system` and `gke-system` namespaces
  * Control plane
  * vSphere persistent volumes in the cluster
  * User and admin cluster vCPU (virtual CPU) and memory contention signals
  * User and admin cluster ESXi [preconfigured Host CPU Usage and Memory Usage alarms](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.monitoring.doc/GUID-82933270-1D72-4CF3-A1AF-E5A1343F62DE.html).
  * Time of day (TOD)
  * Node network policy for a cluster with Dataplane V2 enabled
  * Overall healthiness of the Dataplane V2 node agent



## Diagnose an admin cluster

To diagnose an admin cluster, specify the path to your admin cluster:
    
    
    gkectl diagnose cluster --kubeconfig=ADMIN_CLUSTER_KUBECONFIG
    

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of your admin cluster kubeconfig file.

The following example output is returned from the `gkectl diagnose cluster` command:
    
    
    Preparing for the diagnose tool...
    Diagnosing the cluster......DONE
    
    - Validation Category: Admin Cluster Connectivity
    Checking VMs TOD (availability)...SUCCESS
    Checking Konnectivity Server (readiness)...SUCCESS
    
    - Validation Category: Admin Cluster F5 BIG-IP
    Checking f5 (credentials, partition)...SUCCESS
    
    - Validation Category: Admin Cluster VCenter
    Checking Credentials...SUCCESS
    Checking DRS enabled...SUCCESS
    Checking Hosts for AntiAffinityGroups...SUCCESS
    Checking Version...SUCCESS
    Checking Datacenter...SUCCESS
    Checking Datastore...SUCCESS
    Checking Resource pool...SUCCESS
    Checking Folder...SUCCESS
    Checking Network...SUCCESS
    
    - Validation Category: Admin Cluster
    Checking cluster object...SUCCESS
    Checking machine deployment...SUCCESS
    Checking machineset...SUCCESS
    Checking machine objects...SUCCESS
    Checking kube-system pods...SUCCESS
    Checking anthos-identity-service pods...SUCCESS
    Checking storage...SUCCESS
    Checking resource...SUCCESS
    Checking virtual machine resource contention...SUCCESS
    Checking host resource contention...SUCCESS
    All validation results were SUCCESS.
    Cluster is healthy!
    

If there's an issue with a virtual IP address (VIP) in the target cluster, use the `--config` flag to provide the admin cluster configuration file to provide more debugging information.
    
    
    gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config CLUSTER_CONFIG
    

Replace `CLUSTER_CONFIG` with the path of the admin or user cluster configuration file.

**Note:** Always set `--kubeconfig` to the path of the admin cluster kubeconfig file, regardless of whether you are diagnosing an admin or user cluster.

The following example output shows that the `gkectl diagnose cluster` command can now correctly connect to the cluster and check for issues:
    
    
    Failed to access the api server via LB VIP "...": ...
    Try to use the admin master IP instead of problematic VIP...
    Reading config with version "[CONFIG_VERSION]"
    Finding the admin master VM...
    Fetching the VMs in the resource pool "[RESOURCE_POOL_NAME]"...
    Found the "[ADMIN_MASTER_VM_NAME]" is the admin master VM.
    Diagnosing admin|user cluster "[TARGET_CLUSTER_NAME]"...
    ...
    

## Diagnose a user cluster

To diagnose a user cluster, you must specify the user cluster name. If you need to get the name of a user cluster, run the following command:
    
    
    kubectl get cluster --kubeconfig=USER_CLUSTER_KUBECONFIG
    

Replace `USER_CLUSTER_KUBECONFIG` with the path of the user cluster kubeconfig file.

Specify the name of the user cluster along with the config file as follows:
    
    
    gkectl diagnose cluster --kubeconfig=ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name=USER_CLUSTER_NAME
    

Replace `USER_CLUSTER_NAME` with the name of the user cluster.

The following example output is returned from the `gkectl diagnose cluster` command:
    
    
    Preparing for the diagnose tool...
    Diagnosing the cluster......DONE
    
    Diagnose result is saved successfully in <DIAGNOSE_REPORT_JSON_FILE>
    
    - Validation Category: User Cluster Connectivity
    Checking Node Network Policy...SUCCESS
    Checking VMs TOD (availability)...SUCCESS
    Checking Dataplane-V2...Success
    
    - Validation Category: User Cluster F5 BIG-IP
    Checking f5 (credentials, partition)...SUCCESS
    
    - Validation Category: User Cluster VCenter
    Checking Credentials...SUCCESS
    Checking DRS enabled...SUCCESS
    Checking Hosts for AntiAffinityGroups...SUCCESS
    Checking VSphere CSI Driver...SUCCESS
    Checking Version...SUCCESS
    Checking Datacenter...SUCCESS
    Checking Datastore...SUCCESS
    Checking Resource pool...SUCCESS
    Checking Folder...SUCCESS
    Checking Network...SUCCESS
    
    - Validation Category: User Cluster
    Checking user cluster and node pools...SUCCESS
    Checking cluster object...SUCCESS
    Checking machine deployment...SUCCESS
    Checking machineset...SUCCESS
    Checking machine objects...SUCCESS
    Checking control plane pods...SUCCESS
    Checking kube-system pods...SUCCESS
    Checking gke-system pods...SUCCESS
    Checking gke-connect pods...SUCCESS
    Checeking anthos-identity-service pods...SUCCESS
    Checking storage...SUCCESS
    Checking resource...SUCCESS
    Checking virtual machine resource contention...SUCCESS
    Checking host resource contention...SUCCESS
    All validation results were SUCCESS.
    Cluster is healthy!
    

## Diagnose virtual machine status

If an issue arises with virtual machine creation, run `gkectl diagnose cluster` to obtain a diagnosis of the virtual machine status.

The output is similar to the following:
    
    
    - Validation Category: Cluster Healthiness
    Checking cluster object...SUCCESS
    Checking machine deployment...SUCCESS
    Checking machineset...SUCCESS
    Checking machine objects...SUCCESS
    Checking machine VMs...FAILURE
        Reason: 1 machine VMs error(s).
        Unhealthy Resources:
        Machine [NODE_NAME]: The VM's UUID "420fbe5c-4c8b-705a-8a05-ec636406f60" does not match the machine object's providerID "420fbe5c-4c8b-705a-8a05-ec636406f60e".
        Debug Information:
        null
    ...
    Exit with error:
    Cluster is unhealthy!
    Run gkectl diagnose cluster automatically in gkectl diagnose snapshot
    Public page https://cloud.google.com/anthos/clusters/docs/on-prem/latest/diagnose#overview_diagnose_snapshot
    

## Troubleshoot

The following table outlines some possible resolutions for problems with running the `gkectl diagnose cluster` command:

Issue| Possible causes| Resolution  
---|---|---  
Kubernetes API server is not reachable, either for the admin cluster, or for user clusters. | Check the virtual machine health OOB (out-of-box) memory latency graphs, which ideally should have a memory latency around zero. Memory contention can also increase CPU contention, and the CPU readiness graphs might have a spike as there will be swapping involved. | Increase physical memory. For other options, see [VMware troubleshooting suggestions](https://kb.vmware.com/s/article/2001003).  
Nodepool creation times out. | VMDK high read/write latency. Check VM health OOB for virtual disk read and write latency. According to VMware, a total latency greater than 20ms indicates a problem. | See [VMware solutions for disk performance problems](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.monitoring.doc/GUID-E813116C-9D72-4464-BF3E-1B19F70F45BE.html).  
  
### `BundleUnexpectedDiff` error

The Kubernetes Cluster API resource managed by a Google Distributed Cloud bundle might be accidentally modified which can cause failure of system components, or cluster upgrade or update failure.

In Google Distributed Cloud version 1.13 and later, the `onprem-user-cluster-controller` periodically checks the status of objects, and reports any unexpected differences from the desired state through logs and events. These objects include the user cluster control plane and add-ons such as Services and DaemonSets.

The following example output shows an unexpected difference event:
    
    
     Type     Reason                 Age    From                              Message
     ----     ------                 ----   ----                              -------
     Warning  BundleUnexpectedDiff   13m    onpremusercluster/ci-bundle-diff  Detected unexpected difference of user control plane objects: [ConfigMap/istio], please check onprem-user-cluster-controller logs for more details.
    

The following example output shows logs generated by the `onprem-user-cluster-controller`:
    
    
    2022-08-06T02:54:42.701352295Z W0806 02:54:42.701252       1 update.go:206] Detected unexpected difference of user addon object(ConfigMap/istio), Diff:   map[string]string{
    2022-08-06T02:54:42.701376406Z -    "mesh": (
    2022-08-06T02:54:42.701381190Z -        """
    2022-08-06T02:54:42.701385438Z -        defaultConfig:
    2022-08-06T02:54:42.701389350Z -          discoveryAddress: istiod.gke-system.svc:15012
    ...
    2022-08-06T02:54:42.701449954Z -        """
    2022-08-06T02:54:42.701453099Z -    ),
    2022-08-06T02:54:42.701456286Z -    "meshNetworks": "networks: {}",
    2022-08-06T02:54:42.701459304Z +    "test-key":     "test-data",
    2022-08-06T02:54:42.701462434Z   }
    

The events and logs won't block cluster operation. Objects that have unexpected differences from their desired state are overwritten in the next cluster upgrade.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
