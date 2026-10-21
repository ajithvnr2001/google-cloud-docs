---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-cluster-creation-upgrade/
title: Troubleshooting cluster creation and upgrade \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:11.713013+00:00
---

# Troubleshooting cluster creation and upgrade  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-cluster-creation-upgrade/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Troubleshooting cluster creation and upgrade Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/troubleshoot-cluster-creation-upgrade)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/troubleshoot-cluster-creation-upgrade)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page shows you how to investigate issues with cluster creation, upgrade, and resizing in Google Distributed Cloud.

## Default logging behavior for `gkectl` and `gkeadm`

For `gkectl` and `gkeadm` it is sufficient to use the default logging settings:

  * For `gkectl`, the default log file is `/home/ubuntu/.config/gke-on-prem/logs/gkectl-$(date).log`, and the file is symlinked with the `logs/gkectl-$(date).log` file in the local directory where you run `gkectl`.

  * For `gkeadm`, the default log file is `logs/gkeadm-$(date).log` in the local directory where you run `gkeadm`.

  * The default `-v5` verbosity level covers all the log entries needed by the support team.

  * The log file includes the command executed and the failure message.




We recommend that you send the log file to the support team when you need help.

## Specifying a non-default locations for log files

To specify a non-default location for the `gkectl` log file, use the `--log_file` flag. The log file that you specify will not be symlinked with the local directory.

To specify a non-default location for the `gkeadm` log file, use the `--log_file` flag.

## Locating Cluster API logs in the admin cluster

If a VM fails to start after the admin control plane has started, you can investigate the issue by inspecting the logs from the Cluster API controllers Pod in the admin cluster.

  1. Find the name of the Cluster API controllers Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace kube-system \
             get pods | grep clusterapi-controllers
         

  2. View logs from the `vsphere-controller-manager`. Start by specifying the Pod, but no container::
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace kube-system \
             logs POD_NAME
         

The output tells you that you must specify a container, and it gives you the names of the containers in the Pod. For example:
         
         ... a container name must be specified ...,
         choose one of: [clusterapi-controller-manager vsphere-controller-manager rbac-proxy]
         

Choose a container, and view its logs:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace kube-system \
             logs POD_NAME --container CONTAINER_NAME
         




## Using `govc` to resolve issues with vSphere

You can use [`govc`](https://github.com/vmware/govmomi/tree/main/govc#govc) to investigate issues with vSphere. For example, you can confirm permissions and access for your vCenter user accounts, and you can collect vSphere logs.

## Debugging using the bootstrap cluster's logs

During installation, Google Distributed Cloud creates a temporary bootstrap cluster. After a successful installation, Google Distributed Cloud deletes the bootstrap cluster, leaving you with your admin cluster and user cluster. Generally, you should have no reason to interact with the bootstrap cluster.

If you pass `--cleanup-external-cluster=false` to `gkectl create cluster`, then the bootstrap cluster does not get deleted, and you can use the bootstrap cluster's logs to debug installation issues.

  1. Find the names of Pods running in the `kube-system` namespace:
         
         kubectl --kubeconfig /home/ubuntu/.kube/kind-config-gkectl get pods -n kube-system
         

  2. View the logs for a Pod:
         
         kubectl --kubeconfig /home/ubuntu/.kube/kind-config-gkectl -n kube-system get logs POD_NAME
         

  3. To get the logs from the bootstrap cluster directly, you can run the following command during cluster creation, update and upgrade:
         
         docker exec -it gkectl-control-plane bash
         

The command opens a terminal inside the gkectl-control-plane container that runs in the bootstrap cluster.

To inspect the kubelet and containerd logs, use the following commands and look for errors or warnings in the output:
         
         systemctl status -l kubelet
         journalctl --utc -u kubelet
         systemctl status -l containerd
         journalctl --utc -u containerd
         




## Rolling back a node pool after an upgrade

If you upgrade a user cluster and then discover an issue with the cluster nodes, you can roll back selected node pools to the previous version.

Rolling back selected node pools is supported for Ubuntu and COS node pools, but not for Windows node pools.

The version of a node pool can be the same or one minor version older than the version of the user cluster control plane. For example, if the control plane is at version 1.14, then the node pools can be at version 1.14 or 1.13.

### View available node pool versions

Suppose you recently [upgraded your user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading) worker nodes and control plane from version 1.13.1-gke.35 to version 1.14.0, and you discover an issue with the upgraded worker nodes. So you decide to roll back one or more node pools to the version you were previously running: 1.13.1-gke.35.

Verify that the previous version is available for rollback:
    
    
    gkectl version --cluster-name USER_CLUSTER_NAME --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

The output shows the current version and the previous version for each node pool. For example: 
    
    
    user cluster version: 1.14.0-gke.x
    
    node pools:
    - pool-1:
      - version: 1.14.0-gke.x
      - previous version: 1.13.1-gke.35
    - pool-2:
      - version: 1.14.0-gke.x
      - previous version: 1.13.1-gke.35
    
    available node pool versions:
    - 1.13.1-gke.35
    - 1.14.0-gke.x
    

### Roll back node pools

You can roll back one node pool at a time, or you can roll back several node pools in a single step.

In your user cluster configuration file, in one or more node pools, set the value of `gkeOnPremVersion` to the previous version: 1.13.1-gke.35 in this example:
    
    
    nodePools:
    - name: pool-1
      cpus: 4
      memoryMB: 8192
      replicas: 3
      gkeOnPremVersion: 1.13.1-gke.35
      ...
    

Update the cluster to roll back the node pool(s):
    
    
    gkectl update cluster --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Verify that the rollback:
    
    
    gkectl version --cluster-name USER_CLUSTER_NAME --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

For example, the following output shows that `pool-1` was rolled back to version 1.13.1-gke.35. 
    
    
    user cluster version: 1.14.0-gke.x
    
    node pools:
    - pool-1:
      - version: 1.13.1-gke.35
      - previous version: 1.14.0-gke.x
    - pool-2:
      - version: 1.14.0-gke.x
      - previous version: 1.13.1-gke.35
    
    available node pool versions:
    - 1.13.1-gke.35
    - 1.14.0-gke.x
    

### Upgrade to a new patch version

Suppose that the issue is fixed in a new patch version, say 1.14.1. Now you can upgrade all node pools and the control plane to the new patch version.

In your user cluster configuration file:

  * Set the value of `gkeOnPremVersion` to the new patch version: 1.14.1-gke.x in this example.

  * For each node pool, remove the `gkeOnPremVersion` field, or set it to the empty string. When no version is specified for a node pool, the version for the node pool defaults to the version specified for the cluster.




Example:
    
    
    gkeOnPremVersion: 1.14.1-gke.x
    
    nodePools:
    - name: pool-1
      cpus: 4
      memoryMB: 8192
      replicas: 3
      gkeOnPremVersion: ""
    - name: pool-2
      cpus: 8
      memoryMB: 8192
      replicas: 2
      gkeOnPremVersion: ""
    

Run `gkectl prepare` and `gkectl upgrade cluster` as described in [Upgrading Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading).

Verify the new cluster version, and see the versions that are now available for rollback:
    
    
    gkectl version --cluster-name USER_CLUSTER_NAME --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Example output: 
    
    
    user cluster version: 1.14.1-gke.y
    
    node pools:
    - pool-1:
      - version: 1.14.1-gke.y
      - previous version: 1.13.1-gke.35
    - pool-2:
      - version: 1.14.1-gke.y
      - previous version: 1.13.1-gke.35
    
    available node pool versions:
    - 1.13.1-gke.35
    - 1.14.0-gke.x
    - 1.14.1-gke.y
    

## Debugging F5 BIG-IP issues using the internal kubeconfig file

After an installation, Google Distributed Cloud generates a kubeconfig file named `internal-cluster-kubeconfig-debug` in the home directory of your admin workstation. This kubeconfig file is identical to your admin cluster's kubeconfig file, except that it points directly to the admin cluster's control plane node, where the Kubernetes API server runs. You can use the `internal-cluster-kubeconfig-debug` file to debug F5 BIG-IP issues.

## Resizing a user cluster fails

If a resizing of a user cluster fails:

  1. Find the names of the MachineDeployments and the Machines:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get machinedeployments --all-namespaces
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get machines --all-namespaces
         

  2. Describe a MachineDeployment to view its logs:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe machinedeployment MACHINE_DEPLOYMENT_NAME

  3. Check for errors on newly-created Machines:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe machine MACHINE_NAME




## No addresses can be allocated for cluster resize

This issue occurs if there are not enough IP addresses available to resize a user cluster.

`kubectl describe machine` displays the following error:
    
    
    Events:
    Type     Reason  Age                From                    Message
    ----     ------  ----               ----                    -------
    Warning  Failed  9s (x13 over 56s)  machineipam-controller  ipam: no addresses can be allocated
    

To resolve this issue, [Allocate more IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/resizing-a-user-cluster) for the cluster. Then, delete the affected Machine:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG delete machine MACHINE_NAME

Google Distributed Cloud creates a new Machine and assigns it one of the newly available IP addresses.

## Sufficient number of IP addresses allocated, but Machine fails to register with cluster

This issue can occur if there is an IP address conflict. For example, an IP address you specified for a machine is being used for a load balancer.

To resolve this issue, update your [cluster IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ip-block-file) so that the machine addresses do not conflict with addresses specified in your [cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file) or your [Seesaw IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance#ipblock_files).

## Snapshot is created automatically when admin cluster creation or upgrade fails

If you attempt to create or upgrade an admin cluster, and that operation fails, Google Distributed Cloud takes an external snapshot of the bootstrap cluster, which is a transient cluster that is used to create or upgrade the admin cluster. Although this snapshot of the bootstrap cluster is similar to the snapshot taken by running the [`gkectl diagnose snapshot` command](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#overview_diagnose_snapshot) on the admin cluster, it is instead automatically triggered. This snapshot of the bootstrap cluster contains important debugging information for the admin cluster creation and upgrade process. You can [provide this snapshot](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/getting-support) to Google Cloud Support if needed.

The external snapshot includes Pod logs from the `onprem-admin-cluster-controller` that you can view to debug cluster creation or upgrade issues. The logs are stored in a separate file, for example:
    
    
    kubectl_logs_onprem-admin-cluster-controller-6767f6597-nws8g_--container_onprem-admin-cluster-controller_--kubeconfig_.home.ubuntu..kube.kind-config-gkectl_--namespace_kube-system

## Health checks are run automatically when cluster upgrade fails

If you attempt to upgrade an admin or user cluster, and that operation fails, Google Distributed Cloud automatically runs the [`gkectl diagnose cluster` command](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#overview_diagnose_cluster) on the cluster.

To skip the automatic diagnosis, pass the `--skip-diagnose-cluster` flag to `gkectl upgrade`.

## Upgrade process becomes stuck

Google Distributed Cloud, behind the scenes, uses the [Kubernetes `drain` command](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) during an upgrade. This `drain` procedure can be blocked by a Deployment with only one replica that has a PodDisruptionBudget (PDB) created for it with `minAvailable: 1`.

From Google Distributed Cloud version 1.13, you can check failures through Kubernetes Pod events.

  1. Find the names of the Machines:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get machines --all-namespaces
         

  2. Check for errors using the `kubectl describe machine` command:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe machine MACHINE_NAME




Here is an example output:
    
    
    Events:
      Type     Reason              Age    From                Message
      ----     ------              ----   ----                -------
      Warning  PodEvictionTooLong  3m49s  machine-controller  Waiting too long(12m10.284294321s) for pod(default/test-deployment-669b85c4cc-z8pz7) eviction.
    

For a more detailed analysis on the machine objects status, run `gkectl diagnose cluster`:
    
    
    ...
    Checking machineset...SUCCESS
    Checking machine objects...FAILURE
        Reason: 1 machine objects error(s).
        Unhealthy Resources:
        Pod test-deployment-669b85c4cc-7zjpq: Pod cannot be evicted successfully. There is 1 related PDB.
    ...
    Checking all poddisruptionbudgets...FAILURE
        Reason: 1 pod disruption budget error(s).
        Unhealthy Resources:
        PodDisruptionBudget test-pdb: default/test-pdb might be configured incorrectly, the total replicas(3) should be larger than spec.MinAvailable(3).
    ...
    Some validation results were FAILURE or UNKNOWN. Check report above.
    

To resolve this issue, save the PDB, and remove it from the cluster before attempting the upgrade. You can then add the PDB back after the upgrade is complete.

## Diagnose virtual machine status

If an issue arises with virtual machine creation, run `gkectl diagnose cluster` to obtain a diagnosis of the virtual machine status.

Here is example output:
    
    
    
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
    Public page https://cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#overview_diagnose_snapshot
    

See [Diagnose cluster issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose) for more information.

## Re-create missing user cluster kubeconfig file

You might want to re-create a user cluster kubeconfig file in a couple of situations:

  * If you attempt to create a user cluster, and the creation operation fails, and you want to have its user cluster kubeconfig file.
  * If the user cluster kubeconfig file is missing, such as after being deleted.



Run the following command to re-create the user cluster kubeconfig file:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get secrets -n admin \
      -o jsonpath='{.data.admin\.conf}' | base64 -d  > USER_CLUSTER_KUBECONFIG
    

Replace the following:

  * USER_CLUSTER_KUBECONFIG: the name of the new kubeconfig file for your user cluster.
  * ADMIN_CLUSTER_KUBECONFIG: the path of the kubeconfig file for your admin cluster.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
