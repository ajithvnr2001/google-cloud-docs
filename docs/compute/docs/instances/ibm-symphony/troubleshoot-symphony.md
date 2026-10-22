---
url: https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/troubleshoot-symphony/
title: Troubleshoot IBM Spectrum Symphony connectors \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:22.212671+00:00
---

# Troubleshoot IBM Spectrum Symphony connectors  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/troubleshoot-symphony/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot IBM Spectrum Symphony connectors Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you resolve common issues with the IBM Spectrum Symphony integration for Google Cloud. Specifically, this document provides troubleshooting guidance for the [IBM Spectrum Symphony host factory service](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/overview#symphony-host-factory), the connectors for [Compute Engine and GKE providers](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/overview#gcp-host-factory-provider) and the [Symphony Operator for Kubernetes](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-kubernetes-provider#install-kub-operator).

## Symphony host factory service issues

These issues relate to the central [Symphony host factory service](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/overview#symphony-host-factory). You can find the main log file for this service at the following location on Linux:
    
    
    $EGO_TOP/hostfactory/log/hostfactory.hostname.log
    

You set the `$EGO_TOP` environment variable when you [load the host factory environment variables](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-compute-provider#load-hf-environment). In IBM Spectrum Symphony, `$EGO_TOP` points to the installation root of the Enterprise Grid Orchestrator (EGO), which is the core resource manager for the cluster. The default installation path for `$EGO_TOP` on Linux is typically `/opt/ibm/spectrumcomputing`.

### Cluster doesn't add new VMs for pending workloads

This issue occurs when the Symphony queue contains jobs, but the host factory fails to provision new virtual machines (VMs) to manage the load. The host factory log file contains no `SCALE-OUT` messages.

This issue usually occurs when the Symphony requestor isn't correctly configured or enabled. To resolve the issue, check the status of the configured requestor to verify that it is enabled and that there is a pending workload.

  1. Locate the requestor configuration file. The file is typically located at:
         
         $HF_TOP/conf/requestors/hostRequestors.json
         

The `$HF_TOP` environment variable is defined in your environment when you use the [source command](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-compute-provider#load-hf-environment). The value is the path to the top-level installation directory for the IBM Spectrum Symphony host factory service.

  2. Open the `hostRequestors.json` file and locate the `symAinst` entry. In that section, verify that the `enabled` parameter is set to a value of `1` and that the providers list includes the name of your configured Google Cloud provider instance.

     * For Compute Engine configurations, the provider list must show the name of the Compute Engine provider that you created in [Enable the provider instance](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-compute-provider#enable-provider) during the Compute Engine provider installation.
     * For GKE configurations, the provider list must show the name of the GKE provider that you created in [Enable the provider instance](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-kubernetes-provider#enable-provider-instance) during the GKE provider installation.
  3. After you confirm that the symAinst requestor is enabled, check if a consumer has a pending workload that requires a scale-out.

View a list of all consumers and their workload status:
         
         egosh consumer list
         

  4. In the output, look for the consumer associated with your workload and verify that the workload is pending. If the requestor is enabled and a workload is pending, but the host factory service does not initiate scale-out requests, then check the HostFactory service logs for errors.




### Host factory service not starting

If the host factory service doesn't run, follow these steps to resolve the issue:

  1. Check the status of the `HostFactory` service:
         
         egosh service list
         

In the output, locate the `HostFactory` service and check that the `STATE` field shows a status of `STARTED`.

  2. If the `HostFactory` service is not started, restart it:
         
         egosh service stop HostFactory
         egosh service start HostFactory
         




### Other errors and logging

If you encounter other errors with the host factory service, then increase the log verbosity to get more detailed logs. To do so, complete the following steps:

  1. Open the `hostfactoryconf.json` file for editing. The file is typically located at:
         
         $EGO_TOP/hostfactory/conf/
         

For more information about the value of the `$EGO_TOP` environment variable, see Symphony host factory service issues.

  2. Update the `HF_LOGLEVEL` value from `LOG_INFO` to `LOG_DEBUG`:
         
         {
           ...
           "HF_LOGLEVEL": "LOG_DEBUG",
           ...
         }
         

  3. Save the file after you make the change.

  4. To make the change take effect, restart the `HostFactory` service:
         
         egosh service stop HostFactory
         egosh service start HostFactory
         




After you restart, the `HostFactory` service generates more detailed logs, which you can use to troubleshoot complex issues. You can view these logs in the main host factory log file, located at `$EGO_TOP/hostfactory/log/hostfactory.hostname.log` on Linux.

## Host factory provider issues

The following issues occur within the [host factory provider scripts](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/overview#provider-scripts) for Compute Engine or Google Kubernetes Engine.

Check the provider logs (`hf-gce.log` or `hf-gke.log`) for detailed error messages. The location of the `hf-gce.log` and `hf-gke.log` files is determined by the `LOGFILE` variable set in the provider's configuration file in [Enable the provider instance](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-compute-provider#enable-provider).

### Virtual machine or pod is not provisioned

This issue might occur after the host factory provider logs show a call to the `requestMachines.sh` script, but the resource doesn't appear in your Google Cloud project.

To resolve this issue, follow these steps:

  1. Check the provider script logs (`hf-gce.log` or `hf-gke.log`) for error messages from the Google Cloud API. The location of the `hf-gce.log` and `hf-gke.log` files is determined by the `LOGFILE` variable set in the provider's configuration file in [Enable the provider instance](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-compute-provider#enable-provider).

  2. Verify that the service account has the correct IAM permissions:

     1. Follow the instructions in [View current access](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#view-access).
     2. Verify that the service account has the [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (roles/compute.instanceAdmin.v1) IAM role on the project. For more information about how to grant roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  3. To ensure that the Compute Engine parameters in your host template are valid, you must verify the following:

     1. The host template parameters must be in the `gcpgceinstprov_templates.json` file that you created when you [set up a provider instance](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/install-compute-provider) during the Compute Engine provider installation. The most common parameters to validate are `gcp_zone` and `gcp_instance_group`.

     2. Verify that the instance group set by the `gcp_instance_group` parameter exists. To confirm the instance group, follow the instructions in [View a MIG's properties](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_a_migs_properties), by using the `gcp_instance_group` name and `gcp_zone` zone values from the template file.




### Pod gets stuck in `Pending` or `Error` state on GKE

This issue might occur after the `hf-gke` log shows it created the `GCPSymphonyResource` resource, but the corresponding pod in the GKE cluster never reaches a `Running` state and might show a status like `Pending`, `ImagePullBackOff`, or `CrashLoopBackOff`.

This issue occurs if there is a problem within the Kubernetes cluster, such as an invalid container image name, insufficient CPU or memory resources, or a misconfigured volume or network setting.

To resolve this issue, use `kubectl describe` to inspect the events for both the custom resource and the pod to identify the root cause:
    
    
    kubectl describe gcpsymphonyresource RESOURCE_NAME
    kubectl describe pod POD_NAME
    

Replace the following:

  * `RESOURCE_NAME`: the name of the resource.
  * `POD_NAME`: the name of the pod.



## Troubleshoot Kubernetes operator issues

The [Kubernetes operator](https://docs.cloud.google.com/compute/docs/instances/ibm-symphony/overview#kubernetes-operator) manages the lifecycle of a Symphony pod. The following sections can help you troubleshoot common issues you might encounter with the operator and these resources.

### Diagnose issues with resource status fields

The Kubernetes operator manages Symphony workloads in GKE with two primary resource types:

  * The `GCPSymphonyResource` (GCPSR) resource manages the lifecycle of compute pods for Symphony workloads.
  * The `MachineReturnRequest` (MRR) resource handles the return and cleanup of compute resources.



Use these status fields to diagnose issues with the `GCPSymphonyResource` resource:

  * `phase`: The current lifecycle phase of the resource. The options are `Pending`, `Running`, `WaitingCleanup`, or `Completed`.
  * `availableMachines`: The number of compute pods that are ready.
  * `conditions`: Detailed status conditions with timestamps.
  * `returnedMachines`: A list of returned pods.



Use these status fields to diagnose issues with the `MachineReturnRequest` resource:

  * `phase`: The current phase of the return request. The options are `Pending`, `InProgress`, `Completed`, `Failed`, or `PartiallyCompleted`.
  * `totalMachines`: The total number of machines to return.
  * `returnedMachines`: The number of successfully returned machines.
  * `failedMachines`: The number of machines that failed to return.
  * `machineEvents`: Per-machine status details.



### `GCPSymphonyResource` resource stuck in the `Pending` state

This issue occurs when the `GCPSymphonyResource` resource remains in the `Pending` state and the value of `availableMachines` does not increase.

This issue might occur for one these reasons:

  * Insufficient node capacity in your cluster.
  * Problems with pulling the container image.
  * Resource quota limitations.



To resolve this issue:

  1. Check the status of the pods to identify any issues with image pulls or resource allocation:
         
         kubectl describe pods -n gcp-symphony -l symphony.requestId=REQUEST_ID
         

Replace `REQUEST_ID` with your request ID.

  2. Inspect nodes to ensure sufficient capacity:
         
         kubectl get nodes -o wide
         

  3. Pods might show a `Pending` status. This issue usually occurs when the Kubernetes cluster needs to scale up and takes longer than expected. Monitor the nodes to ensure the control plane can scale out.




### Pods are not returned

This issue occurs when you create a `MachineReturnRequest` (MRR), but the number of `returnedMachines` does not increase.

This issue can occur for these reasons:

  * Pods are stuck in a `Terminating` state.
  * There are node connectivity issues.



To resolve this issue:

  1. Check for pods stuck in the `Terminating` state:
         
         kubectl get pods -n gcp-symphony --field-selector=status.phase=Terminating
         

  2. Describe the `MachineReturnRequest` to get details about the return process:
         
         kubectl describe mrr MRR_NAME -n gcp-symphony
         

Replace `MRR_NAME` with the name of your `MachineReturnRequest`.

  3. Manually delete the custom resource object. This deletion activates the final cleanup logic:
         
         kubectl delete gcpsymphonyresource RESOURCE_NAME
         

Replace `RESOURCE_NAME` with the name of the `GCPSymphonyResource` resource.




### High number of failed machines in a `MachineReturnRequest`

This issue occurs when the `failedMachines` count in the `MachineReturnRequest` status is greater than `0`. This issue can occur for these reasons:

  * Pod deletion has timed out.
  * A node is unavailable.



To resolve this issue:

  1. Check the `machineEvents` in the `MachineReturnRequest` status for specific error messages:
         
         kubectl describe mrr MRR_NAME -n gcp-symphony
         

  2. Look for node failure events or control plane performance issues:

     1. Get the status of all nodes:
            
            kubectl get nodes -o wide
            

     2. Inspect a specific node:
            
            kubectl describe node NODE_NAME
            




### Pods are not deleted

This issue occurs when deleted pods are stuck in a `Terminating` or `Error` state.

This issue can occur for these reasons:

  * An overwhelmed control plane or operator, which can cause timeouts or API throttle events.
  * The manual deletion of the parent `GCPSymphonyResource` resource.



To resolve this issue:

  1. Check if the parent `GCPSymphonyResource` resource is still available and not in the `WaitingCleanup` state:
         
         kubectl describe gcpsymphonyresource RESOURCE_NAME
         

  2. If the parent `GCPSymphonyResource` resource is no longer on the system, manually remove the finalizer from the pod or pods. The finalizer tells Kubernetes to wait for the Symphony operator to complete its cleanup tasks before Kubernetes fully deletes the pod. First, inspect the YAML configuration to find the finalizer:
         
         kubectl get pods -n gcp-symphony -l symphony.requestId=REQUEST_ID -o yaml
         

Replace `REQUEST_ID` with the request ID associated with the pods.

  3. In the output, look for the finalizers field within the metadata section. You should see an output similar to this snippet:
         
         metadata:
         ...
         finalizers:
         -   symphony-operator/finalizer
         

  4. To manually remove the finalizer from the pod or pods, use the `kubectl patch` command:
         
         kubectl patch pod -n gcp-symphony -l symphony.requestId=REQUEST_ID --type json -p '[{"op": "remove", "path": "/metadata/finalizers", "value": "symphony-operator/finalizer"}]'
         

Replace `REQUEST_ID` with the request ID associated with the pods.




### Old Symphony resources are not automatically deleted from the GKE cluster

After a workload completes and GKE stops its pods, the associated `GCPSymphonyResource` and `MachineReturnRequest` objects remain in your GKE cluster for longer than the expected 24-hour cleanup period.

This issue occurs when a `GCPSymphonyResource` object lacks the required `Completed status` condition. The operator's automatic cleanup process depends on this status to remove the object. To resolve this issue, complete the following steps:

  1. Review the details of the `GCPSymphonyResource` resource in question:
         
         kubectl get gcpsr GCPSR_NAME -o yaml
         

Replace `GCPSR_NAME` with the name of the `GCPSymphonyResource` resource with this issue.

  2. Review the conditions for one of type `Completed` with a status of `True`:
         
         status:
           availableMachines: 0
           conditions:
           -   lastTransitionTime: "2025-04-14T14:22:40.855099+00:00"
             message: GCPSymphonyResource g555dc430-f1a3-46bb-8b69-5c4c481abc25-2pzvc has
               no pods.
             reason: NoPods
             status: "True"        # This condition will ensure this
             type: Completed       # custom resource is cleaned up by the operator
           phase: WaitingCleanup
           returnedMachines:
           -   name: g555dc430-f1a3-46bb-8b69-5c4c481abc25-2pzvc-pod-0
             returnRequestId: 7fd6805f-9a00-41f9-afe9-c38aa35002db
             returnTime: "2025-04-14T14:22:39.373216+00:00"
         

If this condition is not seen on the `GCPSymphonyResource` details, but the `phase: WaitingCleanup` is shown instead, the `Completed` event has been lost.

  3. Check for pods associated with the `GCPSymphonyResource`:
         
         kubectl get pods -l symphony.requestId=REQUEST_ID
         

Replace `REQUEST_ID` with the request ID.

  4. If no pods exist, safely delete the `GCPSymphonyResource` resource:
         
         kubectl delete gcpsr GCPSR_NAME
         

Replace `GCPSR_NAME` with the name of your `GCPSymphonyResource`.

  5. If the pods existed before you deleted the `GCPSymphonyResource`, then you must delete them. If the pods still exist, then follow the steps in the Pods are not deleted section.




### Pod does not join the Symphony cluster

This issue happens when a pod runs in GKE, but it doesn't appear as a valid host in the Symphony cluster.

This issue occurs if the Symphony software runs inside the pod is unable to connect and register with the Symphony primary host. This issue is often due to network connectivity issues or misconfiguration of the Symphony client within the container.

To resolve this issue, check the logs of the Symphony services running inside the pod.

  1. Use SSH or exec to access the pod and view the logs:
         
         kubectl exec -it POD_NAME -- /bin/bash
         

Replace `POD_NAME` with the name of the pod.

  2. When you have a sh inside the pod, the logs for the EGO and LIM daemons are located in the `$EGO_TOP`/kernel/log directory. The `$EGO_TOP` environment variable points to the root of the IBM Spectrum Symphony installation:
         
         cd $EGO_TOP/kernel/log
         

For more information on the value of the `$EGO_TOP` environment variable, see Symphony host factory service issues.

  3. Examine logs for configuration or network errors that block the connection from the GKE pod to the on-premises Symphony primary pod.




### Machine return request fails

This issue might occur during scale-in operations when you create a `MachineReturnRequest` custom resource, but the object gets stuck, and the operator does not terminate the corresponding Symphony pod.

A failure in the operator's finalizer logic prevents the clean deletion of the pod and its associated custom resource. This problem can lead to orphaned resources and unnecessary costs.

To resolve this issue, manually delete the custom resource, which should activate the operator's cleanup logic:
    
    
    kubectl delete gcpsymphonyresource RESOURCE_NAME
    

Replace `RESOURCE_NAME` with the name of the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
