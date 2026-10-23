---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node/
title: Reset a failed node in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:57.650199+00:00
---

# Reset a failed node in Google Distributed Cloud  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-node/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Reset a failed node in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

When nodes in Google Distributed Cloud fail, which can happen because of issues with storage, network, or OS misconfiguration, you want to efficiently restore cluster health. After you restore the cluster health, you can troubleshoot the node failure. This document shows you how to recover from node failure scenarios by resetting a node, and forcefully removing the node if needed.

If you want to add or remove nodes from a cluster when a node hasn't failed, see [Update clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters).

## Reset nodes

When nodes in Google Distributed Cloud fail because of hardware faults, disk corruption, or operating system issues, you must restore cluster health before you troubleshoot the underlying machine.

### Node recovery architecture

Physical nodes in Google Distributed Cloud are designed as disposable infrastructure units. If a node's operating system is corrupted, you must cleanly remove the node from the cluster, reinstall a fresh base Linux operating system, and re-add the node to the cluster.

Don't try to restore a node from a host-level OS image backup or disk snapshot. Restoring a node from an earlier OS state corrupts the Raft consensus on control plane nodes and introduces Dataplane V2 IP address collisions on worker nodes. For more information about backup and disaster recovery constraints, see [Back up and restore clusters with bmctl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/bmctl-backup-restore).

When there's a node failure, sometimes you can't run reset commands on the nodes if the node is unreachable. You might need to forcefully remove the node from the cluster.

When you [cleanly reset a node and update the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters), the following actions happen:

  1. The node resets, similar to `kubeadm reset`, and the machine reverts to the pre-installed state.
  2. The related references to the node are removed from the nodepool and cluster custom resources.



In some of the following `bmctl` commands to reset nodes, the `--force` parameter indicates whether the reset commands (step 1) should be skipped. If the `--force` parameter is used, `bmctl` only performs the removal step (step 2), and doesn't run the reset commands.

### Remove worker node

To remove a worker node from a cluster, complete the following steps:

  1. Try to cleanly reset the node. After the node is reset, the node is removed from the cluster:
         
         bmctl reset nodes \
             --addresses COMMA_SEPARATED_IPS \
             --cluster CLUSTER_NAME \
             --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * `COMMA_SEPARATED_IP`: the IP addresses of the nodes to reset, such as `10.200.0.8,10.200.0.9`.
     * `CLUSTER_NAME`: the name of the target cluster that contains the failed nodes.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster `kubeconfig` file.

If this command succeeds, you can now diagnose the node and fix any misconfigurations that caused the initial failure. Skip the remaining steps in this section.

  2. If the previous step to reset the node fails, forcefully remove the node from the cluster. This forceful removal skips the previous step that runs that reset commands and only performs the step to remove the related references to the node from the nodepool and cluster custom resources:
         
         bmctl reset nodes \
             --addresses COMMA_SEPARATED_IPS \
             --cluster CLUSTER_NAME \
             --kubeconfig ADMIN_KUBECONFIG \
             --force
         

You can now diagnose the node and fix any misconfigurations that caused the initial failure.

  3. If you forcefully removed the node from the node cluster in the previous step, run the `bmctl reset` command again to reset the nodes:
         
         bmctl reset nodes \
             --addresses COMMA_SEPARATED_IPS \
             --cluster CLUSTER_NAME \
             --kubeconfig ADMIN_KUBECONFIG
         




If the underlying operating system on the machine is corrupted or unrecoverable:

  1. Wipe the machine's local storage drives.
  2. Install a fresh, supported Linux operating system and configure the node prerequisites described in [Operating system configuration requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs) and [Workstation and node prerequisites](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/workstation-prerequisites).
  3. Re-add the healthy node to the cluster by following [Update clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters).



### Remove single control plane node

The process is the same as for worker nodes. For control plane nodes, `bmctl` also cleans the etcd membership.

The cluster stops being in a highly available (HA) state after you remove the failed node. To return to a HA state, [add a healthy node to the cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters).

To remove a node from a cluster, complete the following steps:

  1. Try to cleanly reset the node. After the node is reset, the node is removed from the cluster:
         
         bmctl reset nodes \
             --addresses COMMA_SEPARATED_IPS \
             --cluster CLUSTER_NAME \
             --kubeconfig ADMIN_KUBECONFIG
         

Replace the following values:

     * `COMMA_SEPARATED_IP`: the IP addresses of the nodes to reset, such as `10.200.0.8,10.200.0.9`.
     * `CLUSTER_NAME`: the name of the target cluster that contains the failed nodes.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster `kubeconfig` file.

If this command succeeds, you can now diagnose the node and fix any misconfigurations that caused the initial failure. Skip the remaining steps in this section.

  2. If the previous step to reset the node fails, you can forcefully remove the node from the cluster. This forceful removal skips the previous step that runs that reset commands, and only performs the step to remove the related references to the node from the nodepool and cluster custom resources:
         
         bmctl reset nodes \
           --addresses COMMA_SEPARATED_IPS \
           --cluster CLUSTER_NAME \
           --kubeconfig ADMIN_KUBECONFIG \
           --force
         

You can now diagnose the node and fix any misconfigurations that caused the initial failure.

  3. If you forcefully removed the node from the node cluster in the previous step, run the `bmctl reset` command again to reset the nodes:
         
         bmctl reset nodes \
           --addresses COMMA_SEPARATED_IPS \
           --cluster CLUSTER_NAME \
           --kubeconfig ADMIN_KUBECONFIG
         




If the underlying operating system on the machine is corrupted or unrecoverable:

  1. Wipe the machine's local storage drives.
  2. Install a fresh, supported Linux operating system and configure the node prerequisites described in [Operating system configuration requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs) and [Workstation and node prerequisites](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/workstation-prerequisites).
  3. Re-add the healthy node to the cluster by following [Update clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters).



### Reset a node when control plane is inaccessible

You can run the following command to revert a machine to pre-installed states when the cluster control plane is inaccessible:
    
    
    bmctl reset nodes \
        --addresses NODE_IP_ADDRESSES \
        --ssh-private-key-path SSH_PRIVATE_KEY_PATH \
        --login-user LOGIN_USER \
        --gcr-service-account-key AR_SERVICE_ACCOUNT_KEY
    

Replace the following:

  * `NODE_IP_ADDRESSES`: a comma-separated list of node IP addresses, one for each node that you're resetting.

  * `SSH_PRIVATE_KEY_PATH`: the path of the SSH private key file.

  * `LOGIN_USER`: the username used for passwordless SUDO access to the node machines. Unless you explicitly specify a non-root username for node access in the cluster configuration ([`nodeAccess.loginUser`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#nodeaccess-loginuser)), `root` is used.

  * `AR_SERVICE_ACCOUNT_KEY`: the path of the Artifact Registry service account JSON key file.




This command doesn't remove references to the node from the nodepool and cluster custom resources. After restoring access to the cluster control plane, you should forcibly remove the node from the cluster if you want to retain the cluster.

### Quorum lost in HA control plane

If too many control planes nodes in an HA cluster enter a failed state, the cluster loses quorum and becomes unavailable.

When you need to restore management clusters, don't provide the `kubeconfig` file in the reset commands. If you provide the `kubeconfig` file for a management cluster, it forces a new cluster to perform the reset operation. When you restore a user cluster, provide the path to the `kubeconfig` file.

  1. To recover a cluster that has lost quorum, run the following command on a remaining healthy node:
         
         bmctl restore --control-plane-node CONTROL_PLANE_NODE \
             --cluster CLUSTER_NAME \
             [--kubeconfig KUBECONFIG_FILE]
         

Replace the following:

     * `CONTROL_PLANE_NODE`: the IP addresses of a healthy node that remains as part of the cluster.
     * `CLUSTER_NAME`: the name of the target cluster that contains the failed nodes.
     * `KUBECONFIG_FILE`: if recovering a user cluster, the path to the user cluster `kubeconfig` file.
  2. After you recover the failed nodes, run the `bmctl reset` command to reset the nodes:
         
         bmctl reset nodes \
            --addresses COMMA_SEPARATED_IPS \
            --cluster CLUSTER_NAME \
            [--kubeconfig KUBECONFIG_FILE]
         

Replace the following:

     * `COMMA_SEPARATED_IP`: the IP addresses of the nodes to reset, such as `10.200.0.8,10.200.0.9`.
     * `CLUSTER_NAME`: the name of the target cluster that contains the failed nodes.
     * `KUBECONFIG_FILE`: the path to the admin cluster `kubeconfig` file.

If the failed nodes were part of the load balancer node pools, after the nodes recover they might contend for the control plane virtual IP address and make the new cluster unstable. Run the reset commands against the failed nodes as soon as possible after you recover the nodes.




This process only handles the disaster recovery for a 3-node control plane HA deployment. This process doesn't support the recovery for HA setups with 5 nodes or more.

### Remediate an accidental OS image restore

If a physical node was restored from an OS-level image backup or snapshot and is causing cluster instability, etcd consensus errors, or Dataplane V2 IP collisions, complete the following steps to recover cluster health:

  1. Immediately disconnect or shut down the affected node to prevent further cluster state corruption.
  2. From the admin workstation, run the `bmctl reset nodes --force` command to remove the node's custom resources from the cluster.
  3. Wipe the physical drives on the machine.
  4. Install a clean base Linux operating system following the [Operating system configuration requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/os-reqs).
  5. Re-add the node to the cluster by following [Update clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters).



## What's next

For more information about how to add or remove nodes from a cluster when there isn't a failure and to check node status, see [Update clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters).

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
