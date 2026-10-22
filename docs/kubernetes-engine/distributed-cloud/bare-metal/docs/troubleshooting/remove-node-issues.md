---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/remove-node-issues/
title: Remove nodes blocked by PodDisruptionBudgets \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:07.761980+00:00
---

# Remove nodes blocked by PodDisruptionBudgets  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/remove-node-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Remove nodes blocked by PodDisruptionBudgets Stay organized with collections  Save and categorize content based on your preferences. 

Under certain conditions, [PodDisruptionBudgets (PDB)](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets) policies can prevent nodes from being removed successfully from nodepools. Under these conditions, the node status reports `Ready,SchedulingDisabled` despite being removed. This document shows how to remove nodes from your Google Distributed Cloud clusters that are currently blocked by PDB issues.

This page is for Admins and architects and Operators who manage the lifecycle of the underlying tech infrastructure, and respond to alerts and pages when service level objectives (SLOs) aren't met or applications fail. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## PDB conflicts with the number of Pods available

PDB policies help ensure app performance by preventing Pods going down at the same time when you make changes to the system. Consequently, PDB policies limit the number of simultaneously unavailable Pods in a replicated application.

However, the PDB policy can sometimes prevent node deletions that you want to make if you would violate the policy by removing a node.

For example, a PDB policy can define that there should always be two Pods available in the system (`.spec.minAvailable` is 2). But if you only have two Pods, and you try to remove the node containing one of them, then the PDB policy takes effect and prevents the removal of the node.

Similarly, when the PDB policy defines that no Pods should be unavailable (`.spec.maxUnavailable` is 0), the policy also prevents any associated nodes from being deleted. Even if you try to remove a single Pod at a time, the PDB policy prevents you from deleting the affected node.

## Disable and re-enable the PDB policy

To resolve a PDB conflict, back-up and then remove the PDB policy. After the PDB is deleted successfully, the node drains and the associated Pods are removed. You can then make the changes you want, and re-enable the PDB policy.

The following example shows how to delete a node in this condition, which can affect all types of Google Distributed Cloud clusters: admin, hybrid, standalone, and user clusters.

The same general procedure works for all cluster types. However, the specific commands for deleting a node from an admin cluster nodepool (for admin, hybrid, or standalone clusters) vary slightly from the commands for deleting a node from a user cluster nodepool.

  1. For ease of reading, the `${KUBECONFIG}` variable is used in the following commands.

Depending on the cluster type, export the admin cluster kubeconfig (`ADMIN_KUBECONFIG`) or user cluster kubeconfig (`USER_CLUSTER_CONFIG`) path to `$(KUBECONFIG)` and complete the following steps:

     * To delete a node from a user cluster, set `export KUBECONFIG=USER_CLUSTER_CONFIG`
     * To delete node from an admin cluster, set `export KUBECONFIG=ADMIN_KUBECONFIG`.
  2. Optional: If you are deleting a node from a user cluster nodepool, run the following command to extract the user cluster kubeconfig file:
         
         kubectl --kubeconfig ADMIN_KUBECONFIG -n cluster-USER_CLUSTER_NAME \
           get secret USER_CLUSTER_NAME-kubeconfig  \
           -o 'jsonpath={.data.value}' | base64 -d > USER_CLUSTER_CONFIG
         

Replace the following entries with information specific to your cluster environment:

     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.
     * `CLUSTER_NAME`: the name of the cluster you want to take a snapshot of.
     * `USER_CLUSTER_CONFIG`: the path to the user cluster config file.
  3. After you remove the node from the node pool, check the node status. The affected node reports `Ready, SchedulingDisabled`:
         
         kubectl get nodes --kubeconfig ${KUBECONFIG}
         

Node status looks similar to the following example output:
         
         NAME   STATUS                    ROLES      AGE      VERSION
         CP2    Ready                     Master     11m      v.1.18.6-gke.6600
         CP3    Ready,SchedulingDisabled  <none>     9m22s    v.1.18.6-gke.6600
         CP4    Ready                     <none>     9m18s    v.1.18.6-gke.6600
         

  4. Check the PDBs in your cluster:
         
         kubectl get pdb --kubeconfig ${KUBECONFIG} -A
         

The system reports PDBs similar to the ones shown in the following example output:
         
         NAMESPACE     NAME             MIN AVAILABLE    MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
         gke-system    istio-ingress    1                N/A               1                     19m
         gke-system    istiod           1                N/A               1                     19m
         kube-system   coredns          1                N/A               0                     19m
         kube-system   log-aggregator   N/A              0                 0                     19m
         kube-system   prometheus       N/A              0                 0                     19m
         

  5. Inspect the PDB. Find a match between the Pod label within the PDB and the matching Pods in the node. This match ensures you disable the correct PDB to remove the node successfully:
         
         kubectl --kubeconfig ${KUBECONFIG} get pdb log-aggregator -n kube-system -o 'jsonpath={.spec}'
         

The system returns matching label results in the PDB policy:
         
         {"maxUnavailable":0,"selector":{"matchLabels":{"app":"stackdriver-log-aggregator"}}}
         

  6. Find Pods that match the PDB policy label:
         
         kubectl --kubeconfig ${KUBECONFIG} get pods -A --selector=app=stackdriver-log-aggregator  \
           -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.nodeName}{"\n"}{end}'
         

The command returns a list of Pods that match the PDB label, and verifies the PDB policy you need to remove:
         
         stackdriver-log-aggregator-0    CP3
         stackdriver-log-aggregator-1    CP3
         

  7. After you confirm the affected Pod, make a backup copy of the PDB policy. The following example backs up the `log-aggregator` policy:
         
         kubectl get pdb log-aggregator --kubeconfig ${KUBECONFIG} -n kube-system  \
           -o yaml >> log-aggregator.yaml
         

  8. Delete the specific PDB policy. Again, the following examples deletes the `log-aggregator` policy:
         
         kubectl delete pdb log-aggregator --kubeconfig ${KUBECONFIG} -n kube-system
         

After you delete the PDB policy, the node proceeds to drain. However, it can take up to 30 minutes for the node to be fully deleted. Continue to check the node status to confirm that the process has successfully completed.

If you want to remove the node permanently, and also remove storage resources associated with the node, you can do this before you restore the PDB policy. For more information, see Remove storage resources.

  9. Restore the PDB policy from your copy:
         
         kubectl apply -f log-aggregator.yaml --kubeconfig ${KUBECONFIG}
         

  10. Verify that the deleted Pods are recreated successfully. In this example, if there were two `stackdriver-log-aggregator-x` Pods, then they are recreated:
         
         kubectl get pods -o wide --kubeconfig ${KUBECONFIG} -A
         

  11. If you want to restore the node, edit the appropriate nodepool config, and restore the node IP address.




## Remove storage resources from permanently deleted nodes

If you permanently delete a node, and don't want to restore it to your system, you can also delete the storage resources associated with that node.

  1. Check and get the name of the persistent volume (PV) associated with the node:
         
         kubectl get pv --kubeconfig ${KUBECONFIG}  \
           -A -o=jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{.spec.claimRef.name}{":\t"}  \
           {.spec.nodeAffinity.required.nodeSelectorTerms[0].matchExpressions[0].values}{"\n"}{end}'
         

  2. Delete the PV associated with the node:
         
         kubectl delete pv PV_NAME --kubeconfig ${KUBECONFIG}
         

Replace `PV_NAME` with the name of the persistent volume to delete.




## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
