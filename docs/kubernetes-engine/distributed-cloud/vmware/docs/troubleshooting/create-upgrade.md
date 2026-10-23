---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade/
title: Troubleshoot cluster creation or upgrade \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:42.106412+00:00
---

# Troubleshoot cluster creation or upgrade  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/create-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Troubleshoot cluster creation or upgrade Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to investigate issues with cluster creation and upgrade in Google Distributed Cloud (software only) for VMware.

## Installation issues

The following sections might help you to troubleshoot issues with installing Google Distributed Cloud.

### Use the bootstrap cluster to debug issues

During installation, Google Distributed Cloud creates a temporary bootstrap cluster. After a successful installation, Google Distributed Cloud deletes the bootstrap cluster, leaving you with your admin cluster and user cluster. Generally, you should have no reason to interact with the bootstrap cluster. However, if you encounter issues during installation, you can use the bootstrap cluster logs to help you debug the problem.

If you pass `--cleanup-external-cluster=false` to `gkectl create cluster`, then the bootstrap cluster doesn't get deleted, and you can use the bootstrap cluster to debug installation issues.

#### Examine the bootstrap cluster's logs

  1. Find the names of Pods running in the `kube-system` namespace:
         
         kubectl --kubeconfig /home/ubuntu/.kube/kind-config-gkectl get pods -n kube-system
         

  2. View the logs for a Pod:
         
         kubectl --kubeconfig /home/ubuntu/.kube/kind-config-gkectl -n kube-system get logs POD_NAME
         

Replace `POD_NAME` with the name of the Pod that you want to view.

  3. To get the logs from the bootstrap cluster directly, run the following command during cluster creation, update and upgrade:
         
         docker exec -it gkectl-control-plane bash
         

This command opens a terminal inside the `gkectl-control-plane` container that runs in the bootstrap cluster.

  4. To inspect the `kubelet` and `containerd` logs, use the following commands and look for errors or warnings in the output:
         
         systemctl status -l kubelet
         journalctl --utc -u kubelet
         systemctl status -l containerd
         journalctl --utc -u containerd
         




#### Examine the snapshot of the bootstrap cluster

If you attempt to create or upgrade an admin cluster, and that operation fails, Google Distributed Cloud takes an external snapshot of the bootstrap cluster. This snapshot of the bootstrap cluster is similar to the snapshot taken by running the [`gkectl diagnose snapshot` command](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster) on the admin cluster, but the process triggers automatically. The bootstrap cluster snapshot contains important debugging information for the admin cluster creation and upgrade process.

This external snapshot is uploaded automatically to Cloud Storage buckets for your Google Cloud project under the folders `/home/ubuntu`. The snapshot is taken only when the cluster creation or upgrade operation fails. You can [provide this snapshot](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) to Cloud Customer Care if needed. If the cluster operation succeeds, no snapshot is uploaded.

The external snapshot includes Pod logs from the `onprem-admin-cluster-controller` that you can view to debug cluster creation or upgrade issues. The logs are stored in a separate file, for example:
    
    
    kubectl_logs_onprem-admin-cluster-controller-6767f6597-nws8g_ \
        --container_onprem-admin-cluster-controller_ \
        --kubeconfig_.home.ubuntu..kube.kind-config-gkectl_\
        --namespace_kube-system
    

The external snapshot also includes descriptions of numerous custom resources. For example, the snapshot includes a description of Validation custom resources, which contain detailed status and event information for the failed operation:
    
    
    kubectl describe validations.onprem.cluster.gke.io \
        --kubeconfig /home/ubuntu/.kube/kind-config-gkectl \
        --request-timeout 30s \
        --namespace kube-node-lease
    

### VM doesn't start after admin control plane starts

If a VM fails to start after the admin control plane has started, you can investigate the issue by inspecting the logs from the Cluster API controllers Pod in the admin cluster:

  1. Find the name of the Cluster API controllers Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace kube-system \
             get pods | grep clusterapi-controllers
         

  2. View logs from the `vsphere-controller-manager`. Start by specifying the Pod, but no container:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace kube-system \
             logs POD_NAME
         

The output tells you that you must specify a container, and it gives you the names of the containers in the Pod. For example:
         
         ... a container name must be specified ...,
         choose one of: [clusterapi-controller-manager vsphere-controller-manager rbac-proxy]
         

  3. Choose a container, and view its logs:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG --namespace kube-system \
             logs POD_NAME --container CONTAINER_NAME
         




### Sufficient number of IP addresses allocated, but Machine fails to register with cluster

This issue can occur if there is an IP address conflict. For example, an IP address you specified for a machine is being used for a load balancer.

To resolve this issue, update your [cluster IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) so that the machine addresses don't conflict with addresses specified in your [cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest) or your [Seesaw IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/bundled-load-balance#ipblock_files)

## Kind cluster does not get deleted

When you create an admin cluster, a `kind` cluster (also called the bootstrap cluster) gets created as part of the process. When the admin cluster operation is complete, the `kind` cluster gets deleted automatically.

If you see the error message `Failed to delete the kind cluster`, you can perform the following steps, on your admin workstation, to manually delete the `kind` cluster:

  1. Get the `kind` container ID:
         
         docker inspect --format="{{.Id}}" gkectl-control-plane
         

  2. Get the `containerd-shim` process ID:
         
         sudo ps awx | grep containerd-shim | grep CONTAINER_ID | awk '{print $1}'
         

  3. Kill the process:
         
         sudo kill -9 PROCESS_ID
         




## Cluster upgrade issues

The following sections provide tips on how to resolve problems that you might encounter during a [cluster upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

### Roll back a node pool after an upgrade

If you upgrade a user cluster and then discover an issue with the cluster nodes, you can roll back selected node pools to the previous version.

Rolling back selected node pools is supported for Ubuntu and COS node pools, but not for Windows node pools.

The version of a node pool can be the same or one minor version older than the version of the user cluster control plane. For example, if the control plane is at version 1.14, then the node pools can be at version 1.14 or 1.13.

#### View available node pool versions

Suppose you recently [upgraded your user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading) worker nodes and control plane from version 1.13.1-gke.35 to version 1.14.0, and you discover an issue with the upgraded worker nodes. So you decide to roll back one or more node pools to the version you were previously running: 1.13.1-gke.35. Before you can begin the rollback, you need to verify that the previous version is available for rollback.

To view available versions, run the following command:
    
    
    gkectl version --cluster-name USER_CLUSTER_NAME \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

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
    

#### Roll back node pool version

You can roll back a node pool's version one node pool at a time, or you can roll back several node pools in a single step.

To roll back a node pool version, complete the following steps:

  1. In your user cluster configuration file, in one or more node pools, set the value of `gkeOnPremVersion` to the previous version. The following example shows you how to roll back to version 1.13.1-gke.35:
         
         nodePools:
         - name: pool-1
           cpus: 4
           memoryMB: 8192
           replicas: 3
           gkeOnPremVersion: 1.13.1-gke.35
           ...
         

  2. Update the cluster to roll back the node pool(s):
         
         gkectl update cluster --config USER_CLUSTER_CONFIG \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

  3. Verify that the rollback was successful:
         
         gkectl version --cluster-name USER_CLUSTER_NAME \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

The following output shows that `pool-1` was rolled back to version 1.13.1-gke.35.
         
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
         




#### Upgrade to a new patch version

You can upgrade all node pools and the control plane to a new patch version. This might be helpful if you rolled back to a previous version and want to upgrade to a version that includes a fix.

To upgrade to a new version, complete the following steps:

  1. Make the following changes in your user cluster configuration file:

     1. Set the value of `gkeOnPremVersion` to a new patch version. This example uses 1.14.1-gke.x.

     2. For each node pool, remove the `gkeOnPremVersion` field, or set it to the empty string. When no version is specified for a node pool, the version for the node pool defaults to the version specified for the cluster.

These changes look similar to the following example:
            
            gkeOnPremVersion: 1.14.1-gke.x
            
            nodePools:
            -   name: pool-1
              cpus: 4
              memoryMB: 8192
              replicas: 3
              gkeOnPremVersion: ""
            -   name: pool-2
              cpus: 8
              memoryMB: 8192
              replicas: 2
              gkeOnPremVersion: ""
            

  2. Run `gkectl prepare` and `gkectl upgrade cluster` as described in [Upgrading Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading).

  3. Verify the new cluster version, and see the versions that are available for rollback:
         
         gkectl version --cluster-name USER_CLUSTER_NAME \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

The output is similar to the following:
         
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
          ```
         




### Health checks are run automatically when cluster upgrade fails

If you attempt to upgrade an admin or user cluster, and that operation fails, Google Distributed Cloud automatically runs the [`gkectl diagnose cluster` command](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) on the cluster.

To skip the automatic diagnosis, pass the `--skip-diagnose-cluster` flag to `gkectl upgrade`.

### Upgrade process becomes stuck

Behind the scenes, Google Distributed Cloud uses the [Kubernetes `drain` command](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) during an upgrade. This `drain` procedure can be blocked by a Deployment with only one replica that has a PodDisruptionBudget (PDB) created for it with `minAvailable: 1`.

From Google Distributed Cloud version 1.13, you can check failures through Kubernetes Pod events.

  1. Find the names of the Machines:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get machines --all-namespaces
         

  2. Check for errors using the `kubectl describe machine` command:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe machine MACHINE_NAME
         

The output is similar to the following:
         
         Events:
           Type     Reason              Age    From                Message
           ----     ------              ----   ----                -------
           Warning  PodEvictionTooLong  3m49s  machine-controller  Waiting too long(12m10.284294321s) for pod(default/test-deployment-669b85c4cc-z8pz7) eviction.
         

  3. Optional: For a more detailed analysis on the machine objects status, run `gkectl diagnose cluster`.

The output is similar to the following:
         
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

### Remove unsupported changes to unblock upgrade

When upgrading clusters to 1.16 or earlier versions, changes to most fields are silently ignored during the upgrade, meaning that these changes don't take effect during and after the upgrade.

When upgrading user clusters to 1.28 or later versions, we validate all changes made in the configuration file and return an error for unsupported changes, instead of just ignoring them. This feature is for user clusters only. When upgrading admin clusters, changes to most fields are silently ignored and won't take effect after upgrade.

For example, if you attempt to disable node auto-repair when upgrading a user cluster to 1.28, the upgrade fails with the following error message:
    
    
    failed to generate desired create config: failed to generate desired OnPremUserCluster from seed config: failed to apply validating webhook to OnPremUserCluster: the following changes on immutable fields are forbidden during upgrade: (diff: -before, +after):
       v1alpha1.OnPremUserClusterSpec{
        ... // 20 identical fields
        CloudAuditLogging:     &{ProjectID: "syllogi-partner-testing", ClusterLocation: "us-central1", ServiceAccountKey: &{KubernetesSecret: &{Name: "user-cluster-creds", KeyName: "cloud-audit-logging-service-account-key"}}},
    -   AutoRepair:            &v1alpha1.AutoRepairConfig{Enabled: true},
    +   AutoRepair:            &v1alpha1.AutoRepairConfig{},
        CARotation:            &{Generated: &{CAVersion: 1}},
        KSASigningKeyRotation: &{Generated: &{KSASigningKeyVersion: 1}},
        ... // 8 identical fields
      }
    

If you need to bypass this error, there are the following workarounds:

  * Revert the attempted change, and then rerun the upgrade. For example, in the previous scenario, you would revert the changes made to the `AutoRepair` config and then rerun `gkectl upgrade`.
  * Alternatively, you can generate configuration files that match the current state of the cluster by running [`gkectl get-config`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/get-configuration-file-from-cluster), update the `gkeOnPremVersion` fields for the cluster and the node pools in the configuration file, and then rerun `gkectl upgrade`.



### Issue: OS Image not found after `gkectl prepare`

After running the `gkectl prepare` command and then attempting to upgrade a user cluster with `gkectl upgrade cluster`, you might encounter an error similar to the following:

`[FAILURE] User OS images exist: OS images [gke-on-prem-ubuntu-VERSION] don't exist, please run `gkectl prepare` to upload OS images.`

This error can happen when the admin cluster and the user cluster are configured to use different vSphere folders. By default, the `gkectl prepare` command uploads the OS image to the admin cluster's folder. To upload the image to the user cluster's folder, use the flag `--user-cluster-config` as shown in the following command:
    
    
      gkectl prepare --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-VERSION-full.tgz \
        --user-cluster-config USER_CLUSTER_CONFIG
    

## Debug F5 BIG-IP issues with the internal kubeconfig file

After an installation, Google Distributed Cloud generates a kubeconfig file named `internal-cluster-kubeconfig-debug` in the home directory of your admin workstation. This kubeconfig file is identical to your admin cluster's kubeconfig file, except that it points directly to the admin cluster's control plane node, where the Kubernetes API server runs. You can use the `internal-cluster-kubeconfig-debug` file to debug F5 BIG-IP issues.

## Debug issues with vSphere

You can use [`govc`](https://github.com/vmware/govmomi/tree/main/govc#govc) to investigate issues with vSphere. For example, you can confirm permissions and access for your vCenter user accounts, and you can collect vSphere logs.

## Re-create missing user cluster kubeconfig file

You might want to re-create a user cluster `kubeconfig` file in the following situations:

  * If you attempt to create a user cluster, and the creation operation fails, and you want to have its user cluster `kubeconfig` file.
  * If the user cluster `kubeconfig` file is missing, such as after being deleted.



To generate a new kubeconfig file for your user cluster, execute the following steps:

  1. Define Environment Variables:

Begin by setting the following environment variables with the appropriate values:
         
         USER_CONTROLPLANEVIP=USER_CONTROLPLANEVIP
         USER_CLUSTER_NAME=USER_CLUSTER_NAME
         ADMIN_CLUSTER_KUBECONFIG=PATH_TO_ADMIN_KUBECONFIG
         KUBECONFIG_SECRET_NAME=$(kubectl --kubeconfig $ADMIN_CLUSTER_KUBECONFIG get secrets -n $USER_CLUSTER_NAME | grep ^admin | cut -d' ' -f1 | head -n 1)
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the `kubeconfig` file for your admin cluster.
     * `USER_CONTROLPLANEVIP`: the `controlPlaneVIP` of the user cluster. This can be retrieved from the user cluster manifest file.
  2. Generate the Kubeconfig File:

Run the following command to create the new kubeconfig file:
         
         kubectl --kubeconfig $ADMIN_CLUSTER_KUBECONFIG get secrets $KUBECONFIG_SECRET_NAME \
          -n $USER_CLUSTER_NAME -o jsonpath='{.data.admin\.conf}'  | base64 -d | \
          sed -r "s/ kube-apiserver.*local\./${USER_CONTROLPLANEVIP}/" \
          > USER_CLUSTER_KUBECONFIG
         

Replace :

     * `USER_CLUSTER_KUBECONFIG`: the name of the new `kubeconfig` file for your user cluster.



## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
