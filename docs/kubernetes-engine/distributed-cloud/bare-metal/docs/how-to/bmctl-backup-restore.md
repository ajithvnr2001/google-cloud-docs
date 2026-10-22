---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore/
title: Back up and restore clusters with bmctl \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:21.382446+00:00
---

# Back up and restore clusters with bmctl  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Back up and restore clusters with bmctl Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use `bmctl` to back up and restore clusters created with Distributed Cloud software only for bare metal. These instructions apply to all cluster types.

**Warning:** Using a backup file to restore your cluster is a last resort. The restore process resets the existing cluster and overwrites the cluster information. We don't recommend restoring from a backup file unless the cluster has failed catastrophically. Contact Cloud Customer Care for help in deciding the best course of action.

## What is and isn't backed up

The `bmctl` backup and restore process operates at the Kubernetes control plane layer and is different from other backup solutions. Non-Kubernetes backup solutions capture workload data, persistent storage, and the host operating systems of the physical machines. The `bmctl` backup and restore process restores your Kubernetes clusters without backing up any of these other components.

### Control plane state (backed up by the `bmctl` backup process)

`bmctl` backs up the following objects:

  * etcd store. All Kubernetes resources and custom objects that define the cluster's configuration and chosen state (for example, pod specifications, deployments, ConfigMaps, and secrets).
  * PKI certificates. Certificates used for secure communication within the cluster.
  * Node configuration files and manifests. Configurations related to the cluster nodes.



### Workload and VM Runtime storage (not backed up by the `bmctl` backup process)

`bmctl` doesn't back up the following data:

  * Live pod and container runtime state. `bmctl` doesn't save active processes and in-memory application data. After a restore, Kubernetes restarts pods from the etcd specifications. Any unsaved in-memory state is lost.
  * Persistent volume storage. `bmctl` doesn't back up data stored in persistent volumes, volumes created by the local volume provisioner (LVP), or external storage drivers.
  * Virtual machine disks. `bmctl` doesn't back up the contents of the VM's virtual hard drive, like databases, files, or operating system state inside the VM.



You must use Kubernetes-native or in-guest backup mechanisms to protect application data and the virtual machine state. If your underlying storage driver supports CSI volume snapshots, use standard Kubernetes [Volume Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) to create point-in-time copies of persistent volumes. For more information about configuring storage, see [Storage overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/storage).

Run backup agents inside the guest operating system of VM Runtime virtual machines or deploy application-native backup tools within Kubernetes workloads.

### Physical host operating systems (unsupported)

Treat physical Linux operating systems on Google Distributed Cloud nodes as disposable infrastructure. Kubernetes networking architecture doesn't support restoring host-level OS images. Therefore, Google doesn't support installing third-party host-level backup agents directly on the host OS or restoring physical nodes from OS-level image backups or disk snapshots.

If you install third-party physical backup agents directly on the host Linux OS, you can introduce serious risks.

Many backup agents install proprietary kernel modules or block-level filter drivers to track changes and lock local disk blocks during snapshot operations which can cause the following issues:

  * The etcd database can't append to its write-ahead logs, node heartbeats time out, Raft consensus fails, and clusters become unstable.
  * Unsupported third-party kernel drivers conflict with low-level kernel routines and the container runtime, causing cluster upgrades to fail.
  * Restoring a physical node from an image backup or disk snapshot violates the Raft consensus protocol. The etcd database becomes out of sync with logs on control plane nodes and severe cluster state corruption occurs.
  * Worker nodes become out of sync with the API server's source of truth, Dataplane V2 (Cilium) IP addresses collide, and traffic is dropped.



To recover a physical node that has experienced operating system or hardware failure, don't restore an OS image. Instead, cleanly remove the node from the cluster, reinstall a clean base operating system, and re-add the node to the node pool. For detailed recovery instructions, see [Reset a failed node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node).

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



## Back up a cluster

The `bmctl backup cluster` command packages the cluster's etcd data and PKI certificates into a tar file. The etcd database is the central datastore for all cluster data, containing all Kubernetes objects and custom resources required to manage cluster state. The PKI certificates authenticate over TLS. This data is backed up from the cluster's control plane or from one of the control planes for a [high-availability](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep#high_availability) (HA) deployment.

The backup tar file contains sensitive credentials, including your service account keys and the SSH key. Store backup files in a secure location. To prevent unintended file exposure, the Google Distributed Cloud backup process uses in-memory files only.

Back up your clusters regularly to ensure your snapshot data is relatively current. Adjust the rate of backups to reflect the frequency of significant changes to your clusters.

The `bmctl` version you use to backup a cluster must match the version of the managing cluster.

If you installed Node Agent on your clusters, the `/tmp` directory on the admin node and all target nodes must have 12 GB of free space. If you can't change the size of the `/tmp` directory for your target nodes, see [Change local storage capacity for target nodes](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/node-agent#target-node-capacity). If you can't change the size of the `/tmp` directory for the admin node, see [Change local storage capacity for an admin node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/node-agent#admin-capacity).

To back up a cluster:

  1. Ensure your cluster is operating properly, with working credentials and SSH connectivity to all nodes.

The intent of the backup process is to capture your cluster in a known good state, so that you can restore operation if a catastrophic failure occurs.

Use the following command to check your cluster:
         
         bmctl check cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you plan to back up.
     * `ADMIN_KUBECONFIG`: the path of the kubeconfig file for the admin cluster.
  2. Run the following command to ensure the target cluster is not in a reconciliation state:
         
         kubectl describe cluster CLUSTER_NAME -n CLUSTER_NAMESPACE --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster to back up.
     * `CLUSTER_NAMESPACE`: the namespace for the cluster. By default, the cluster namespaces for Google Distributed Cloud are the name of the cluster prefaced with `cluster-`. For example, if you name your cluster `test`, the namespace has a name like `cluster-test`.
     * `ADMIN_KUBECONFIG`: the path of the kubeconfig file for the admin cluster.
  3. Check the `Status` section in the command output for `Conditions` of type `Reconciling`.

As shown in the following example, a status of `False` for these `Conditions` means the cluster is stable and ready to be backed up.
         
         ...
         Status:
           ...
           Cluster State:  Running
           ...
           Control Plane Node Pool Status:
             ...
             Conditions:
               Last Transition Time:  2023-11-03T16:37:15Z
               Observed Generation:   1
               Reason:                ReconciliationCompleted**Status:                False
               Type:                  Reconciling**
           ...
         

  4. Run the following command to back up the cluster:
         
         bmctl backup cluster -c CLUSTER_NAME --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster to back up.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.

By default, the backup tar file saved to the workspace directory (`bmctl-workspace`, by default) on your admin workstation. The tar file is named `CLUSTER_NAME_backup_TIMESTAMP.tar.gz`, where `CLUSTER_NAME` is the name of the cluster being backed up and `TIMESTAMP` is the date and time the backup was made. For example, if the cluster name is `testuser`, the backup file has a name like `testuser_backup_2006-01-02T150405Z0700.tar.gz`.

To specify a different name and location for your backup file, use the `--backup-file` flag.




The backup file expires after a year and the cluster restore process doesn't work with expired backup files.

## Restore a cluster

Restoring a cluster from a backup is a last resort and should be used when a cluster has failed catastrophically and cannot be returned to service any other way. For example, the etcd data is corrupted or the etcd Pod is in a crash loop.

**Note:** To improve cluster performance, Google Distributed Cloud uses a separate etcd instance to store Event objects. These Event objects have a time to live (TTL) of one hour. The cluster restore operation creates a new, empty etcd-events instance, so you lose existing Event objects. However, the loss of Event objects has no impact on cluster operation. Events should be treated as informative, best-effort, supplemental data only.

The backup tar file contains sensitive credentials, including your service account keys and the SSH key. To prevent unintended file exposure, the Google Distributed Cloud restore process uses in-memory files only.

The `bmctl` version you use to restore a cluster must match the version of the managing cluster.

To restore a cluster:

  1. Ensure all node machines that were available for the cluster at the time of the backup are operating properly and reachable.

  2. Ensure that SSH connectivity between nodes works with the SSH keys that were used at the time of the backup.

These SSH keys are reinstated as part of the restore process.

  3. Ensure that the service account keys that were used at the time of the backup are still active.

These service account keys are reinstated for the restored cluster.

  4. To restore an admin, hybrid, or standalone cluster, run the following command:
         
         bmctl restore cluster -c CLUSTER_NAME --backup-file BACKUP_FILE
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you are restoring.
     * `BACKUP_FILE`: the path and name of the backup file you are using.
  5. To restore a user cluster, run the following command:
         
         bmctl restore cluster -c CLUSTER_NAME --backup-file BACKUP_FILE \
             --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you are restoring.
     * `BACKUP_FILE`: the path and name of the backup file you are using.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.



At the end of the restore process, a new kubeconfig file is generated for the restored cluster.

When the restore finishes, use the following steps to verify that it was successful:

  1. Run the following commands to verify the node readiness and system pods running with the generated kubeconfig file:

There are two types of etcd pods:

     * `etcd-HOST_NAME`, which corresponds to the main `etcd` Pod
     * `etcd-events-HOST_NAME`, which corresponds to the `etcd-events` Pod
    
    kubectl get pods -n kube-system --kubeconfig GENERATED_KUBECONFIG
    kubectl get nodes --kubeconfig GENERATED_KUBECONFIG
    

  2. For each etcd pod, run following to verify etcd healthiness:
         
         kubectl exec ETCD_POD_NAME -n kube-system \
             --kubeconfig GENERATED_KUBECONFIG \
             -- /bin/sh -c 'ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
             --cacert=/etc/kubernetes/pki/etcd/ca.crt --key=/etc/kubernetes/pki/etcd/peer.key \
             --cert=/etc/kubernetes/pki/etcd/peer.crt endpoint health'
         

For a healthy etcd member, the response should look like the following:
         
         https://127.0.0.1:2379 is healthy: successfully committed proposal: took = 11.514177ms
         

  3. For each `etcd-events` Pod, run following command to verify `etcd-events` healthiness:
         
         kubectl exec ETCD_EVENTS_POD_NAME -n kube-system \
             --kubeconfig GENERATED_KUBECONFIG \
             -- /bin/sh -c 'ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2382 \
             --cacert=/etc/kubernetes/pki/etcd/ca.crt --key=/etc/kubernetes/pki/etcd/peer.key \
             --cert=/etc/kubernetes/pki/etcd/peer.crt endpoint health'
         

For a healthy etcd-events member, the response should look like the following:
         
         https://127.0.0.1:2382 is healthy: successfully committed proposal: took = 14.308148ms
         




## Troubleshoot

If you have problems with the backup or restore process, the following sections might help you troubleshoot the issue.

If you need additional assistance, reach out to [Google Support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support).

### Running out of memory during a backup or restore

You might receive error messages during the backup or restore process that aren't very self-explanatory or clear on next steps. If the workstation where you run the `bmctl` command run doesn't have a lot of RAM, you might have insufficient memory to perform the backup or restore process.

Google Distributed Cloud version 1.13 and later can use the `--use-disk` parameter in the backup command. To preserve the file permissions, this parameter modifies permissions of the files, so it requires the user that runs the command to be a root user (or use `sudo`). 

### Missing permissions to files during restore

After a successful restore task, deleting bootstrap can fail with an error message similar to the following example:
    
    
      Error: failed to restore node config files: sftp: "Failure" (SSH_FX_FAILURE)
    

This error could mean that some directories required by the restore aren't writable.

Google Distributed Cloud version 1.14 and later have more clear error messages on which directories must be writable. Make sure that the reported directories are writable, and update permissions on directories as needed.

### Refresh of SSH key after a backup breaks the restore process

SSH-related operations during the restore process might fail if the SSH key is refreshed after backup was performed. In this case, the new SSH key becomes invalid for the restore process.

To resolve this issue, you can temporarily add the original SSH key back, then perform the restore. After the restore process is complete, you can rotate the SSH key.

### Can't create a backup for a Node Agent node

If you use Node Agent and receive an error that creating the backup fails to create an archive file, similar to this:
    
    
      I0508 15:29:36.831790  657351 backup_cluster.go:255] Retrying backup node: 128.187.102.133, due to error: failed receive chunk data: rpc error: code = Unknown desc = archiver.CreateArchiveWithList
      failed: failed to create archive file: failed to copy data from file: var/lib/etcd-events/member/snap/db, file size: 26136576, copy bytes: 12478464,
      error: write /tmp/uploadFileTemp1561164777: no space left on device
    

Check that 12 GBs of free space in the `/tmp` directory on the admin node and all target nodes. If you can't change the size of the `/tmp` directory for your target nodes, see [Increase local storage capacity for Node Agent backups](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/node-agent#increase-capacity).

After you confirm that 12 GBs of free space exists in the `/tmp` directory for the admin node and all target nodes, try the backup again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
