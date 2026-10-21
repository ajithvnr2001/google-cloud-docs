---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/recover-node/
title: Reset a failed node in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:57.286267+00:00
---

# Reset a failed node in Google Distributed Cloud  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/recover-node/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Reset a failed node in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/recover-node)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/recover-node)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



If nodes in Google Distributed Cloud fail, such as due to storage, network, or OS misconfiguration, you want to efficiently restore cluster health. After you restore the cluster health, you can troubleshoot the node failure.

This document shows you how to recover from node failure scenarios by resetting a node, and forcefully removing the node if needed.

If you want to add or remove nodes from a cluster under normal circumstances when a node hasn't failed, see [Update clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-clusters).

## Overview

When there's a node failure, sometimes you can't run reset commands on the nodes as the node might be unreachable. You might need to forcefully remove the node from the cluster. 

When you [cleanly reset a node and update the cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-clusters), the following actions happen:

  1. The node resets, similar to `kubeadm reset`, and the machine reverts to the pre-installed state.
  2. The related references to the node are removed from the nodepool and cluster custom resources.

**Note:** In some of the following `bmctl` commands to reset nodes, the `--force` parameter indicates whether the reset commands (step 1) should be skipped. If the `--force` parameter is used, `bmctl` only performs the removal step (step 2), and doesn't run the reset commands.

### Worker node

To remove a node from a cluster, first try to cleanly remove it:

  1. Try to cleanly reset the node. After the node is reset, the node is removed from the cluster:
         
         bmctl reset nodes \
           --addresses COMMA_SEPARATED_IPS \
           --cluster CLUSTER_NAME \
           --kubeconfig ADMIN_KUBECONFIG
         

Replace the following values:

     * `COMMA_SEPARATED_IP`: the IP addresses of the nodes to reset, such as `10.200.0.8,10.200.0.9`.
     * `CLUSTER_NAME`: the name of the target cluster that contains the failed nodes.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.

You can now diagnose the node and fix any misconfigurations that caused the initial failure. Skip the remaining steps in this section.

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
         




### Single control plane node failure

The process is the same as for worker nodes. For control plane nodes, `bmctl` also cleans the `etcd` membership.

**Note:** The cluster becomes non-HA after you remove the failed node. To return to a highly available state, [add a healthy node to the cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-clusters).

To remove a node from a cluster, first try to cleanly remove it:

  1. Try to cleanly reset the node. After the node is reset, the node is removed from the cluster:
         
         bmctl reset nodes \
           --addresses COMMA_SEPARATED_IPS \
           --cluster CLUSTER_NAME \
           --kubeconfig ADMIN_KUBECONFIG
         

Replace the following values:

     * `COMMA_SEPARATED_IP`: the IP addresses of the nodes to reset, such as `10.200.0.8,10.200.0.9`.
     * `CLUSTER_NAME`: the name of the target cluster that contains the failed nodes.
     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.

You can now diagnose the node and fix any misconfigurations that caused the initial failure. Skip the remaining steps in this section.

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
         




### Quorum lost in HA control plane

If too many control planes nodes in an HA cluster enter a failed state, the cluster loses quorum and becomes unavailable.

**Note:** When you need to restore management clusters, don't provide the kubeconfig file in the reset commands. If you provide the kubeconfig file for a management cluster, it forces a new cluster to perform the reset operation. When you restore a user cluster, provide the path to the kubeconfig file.

  1. To recover a cluster that has lost quorum, run the following command on a remaining healthy node:
         
         bmctl restore --control-plane-node CONTROL_PLANE_NODE \
           --cluster CLUSTER_NAME \
           [--kubeconfig KUBECONFIG_FILE]
         

Replace the following values:

     * `CONTROL_PLANE_NODE`: the IP addresses of a healthy node that remains as part of the cluster.
     * `CLUSTER_NAME`: the name of the target cluster that contains the failed nodes.
     * `KUBECONFIG_FILE`: if recovering a user cluster, the path to the user cluster kubeconfig file.
  2. After you recover the failed nodes, run the `bmctl reset` command to reset the nodes:
         
         bmctl reset nodes \
           --addresses COMMA_SEPARATED_IPS \
           --cluster CLUSTER_NAME \
           [--kubeconfig KUBECONFIG_FILE]
         

Replace the following values:

     * `COMMA_SEPARATED_IP`: the IP addresses of the nodes to reset, such as `10.200.0.8,10.200.0.9`.
     * `CLUSTER_NAME`: the name of the target cluster that contains the failed nodes.
     * `KUBECONFIG_FILE`: the path to the admin cluster kubeconfig file.

If the failed nodes were part of the load balancer nodepools, after the nodes recover they might contend for the control plane virtual IP address and make the new cluster unstable. Run the reset commands against the failed nodes as soon as possible after you recover the nodes.


**Note:** This process only handles the disaster recovery for a 3-node control plane HA deployment. This process doesn't support the recovery for HA setups with 5 nodes or more.

## What's next

For more information on how to add or remove nodes from a cluster when there isn't a failure and check the node status, see [Update clusters](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-clusters).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
