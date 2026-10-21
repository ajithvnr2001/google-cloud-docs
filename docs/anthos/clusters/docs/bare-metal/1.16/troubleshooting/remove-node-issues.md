---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/remove-node-issues/
title: Removing nodes blocked by the Pod Disruption Budget \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:57.083009+00:00
---

# Removing nodes blocked by the Pod Disruption Budget  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/remove-node-issues/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Removing nodes blocked by the Pod Disruption Budget Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/remove-node-issues)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/remove-node-issues)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Under certain conditions, [Pod Disruption Budget (PDB)](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets) policies can prevent nodes from being removed successfully from nodepools. Under these conditions, the node status reports `Ready,SchedulingDisabled` despite being removed.

## Pod Disruption Budget conflicts with the number of Pods available

PDB policies help ensure app performance by preventing Pods going down at the same time when you make changes to the system. Consequently, PDB policies limit the number of simultaneously unavailable Pods in a replicated application.

However, the PDB policy can sometimes prevent node deletions you want to make, if by removing a node, you would violate the policy.

For example, a PDB policy can define that there should always be two Pods available in the system (`.spec.minAvailable` is 2). But if you only have two Pods, and you try to remove the node containing one of them, then the PDB policy takes effect and prevents the removal of the node.

Similarly, when the PDB policy defines that no Pods should be unavailable (`.spec.maxUnavailable` is 0), then the policy also prevents any associated nodes from being deleted. Even if you try to remove a single Pod at a time, the PDB policy prevents you from deleting the affected node.

## Workaround: disabling and re-enabling the PDB policy

To solve this conflict, you back-up and then remove the PDB policy. Once the PDB is deleted successfully, the node drains and the associated Pods are removed. After you make the changes you want, you can re-enable the PDB policy.

The following example shows how to delete a node in this condition, which can affect all types of Google Distributed Cloud clusters: Admin, Hybrid, Standalone, and User clusters.

The same general procedure works for all cluster types. However, the specific commands for deleting a node from an admin cluster nodepool (for admin, hybrid, or standalone clusters) vary slightly from the commands for deleting a node from a user cluster nodepool.

### Command variations for different cluster types

For ease of reading, note the placeholder `${KUBECONFIG}` in the following commands. Depending on the cluster type, export the admin cluster kubeconfig (ADMIN_KUBECONFIG) or user cluster kubeconfig (USER_CLUSTER_CONFIG) path to `$(KUBECONFIG)` and follow the steps below.

  * To delete a node from a user cluster, `export KUBECONFIG=USER_CLUSTER_CONFIG`
  * To delete node from an admin cluster, `export KUBECONFIG=ADMIN_KUBECONFIG`.


  1. (optional): If you are deleting a node from a user cluster nodepool, then execute the following command to extract the user cluster kubeconfig file. Note the variable `ADMIN_KUBECONFIG` specifies the path to the admin cluster kubeconfig, and the variable `USER_CLUSTER_NAME` specifies the name of the cluster:
         
         kubectl --kubeconfig ADMIN_KUBECONFIG -n cluster-USER_CLUSTER_NAME  \
         get secret USER_CLUSTER_NAME-kubeconfig  \
         -o 'jsonpath={.data.value}' | base64 -d > USER_CLUSTER_CONFIG
         

  2. After removing the node from the node pool, check the node status. The affected node reports `Ready, SchedulingDisabled`:
         
         kubectl get nodes --kubeconfig ${KUBECONFIG}
         

Node status looks similar to the following:
         
         NAME        STATUS                    ROLES      AGE      VERSION
         abmnewCP2   Ready                     Master     11m      v.1.18.6-gke.6600
         abmnewCP3   Ready,SchedulingDisabled  <none>     9m22s    v.1.18.6-gke.6600
         abmnewCP4   Ready                     <none>     9m18s    v.1.18.6-gke.6600
         

  3. Check the PDBs in your cluster:
         
         kubectl get pdb --kubeconfig ${KUBECONFIG} -A
         

The system reports PDBs similar to the ones shown below:
         
         NAMESPACE     NAME             MIN AVAILABLE    MAX UNAVAILABLE   ALLOWED DISRUPTIONS   AGE
         gke-system    istio-ingress    1                N/A               1                     19m
         gke-system    istiod           1                N/A               1                     19m
         kube-system   coredns          1                N/A               0                     19m
         kube-system   log-aggregator   N/A              0                 0                     19m
         kube-system   prometheus       N/A              0                 0                     19m  
          ```
         

  4. Inspect the PDB. You need to find a match between the Pod label within the PDB and the matching Pods in the node. This match ensures you disable the correct PDB to remove the node successfully:
         
         kubectl --kubeconfig ${KUBECONFIG} get pdb log-aggregator -n kube-system -o 'jsonpath={.spec}'
         

The system returns matching label results in the PDB policy:
         
         {"maxUnavailable":0,"selector":{"matchLabels":{"app":"stackdriver-log-aggregator"}}}
         

  5. Find Pods that match the PDB policy label:
         
         kubectl --kubeconfig ${KUBECONFIG} get pods -A --selector=app=stackdriver-log-aggregator  \
         -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.nodeName}{"\n"}{end}'
         

The command returns a list of Pods that match the PDB label, and verifies the PDB policy you need to remove:
         
         stackdriver-log-aggregator-0    abmnewCP3
         stackdriver-log-aggregator-1    abmnewCP3
         

  6. After confirming the affected Pod, make a backup copy of the PDB policy, in this example case, the `log-aggregator` policy:
         
         kubectl get pdb log-aggregator --kubeconfig ${KUBECONFIG} -n kube-system  \
         -o yaml >> log-aggregator.yaml
         

  7. Delete the specific PDB policy, in this case, the `log-aggregator` policy:
         
         kubectl delete pdb log-aggregator --kubeconfig ${KUBECONFIG} -n kube-system
         

After you've deleted the PDB policy, the node proceeds to drain. However, it can take some time (up to 30 minutes) for the node to be fully deleted, so continue to check the node status.

Note that if you want to remove the node permanently, and also remove storage resources associated with the node, you can do this before you restore the PDB policy. See Removing storage resources.

  8. Restore the PDB policy from your copy:
         
         kubectl apply -f log-aggregator.yaml --kubeconfig ${KUBECONFIG}
         

  9. Verify the deleted Pods are recreated successfully. In this example, if there were two `stackdriver-log-aggregator-x` Pods, then they are recreated:
         
         kubectl get pods -o wide --kubeconfig ${KUBECONFIG} -A
         




If you want to restore the node, edit the appropriate nodepool config, and restore the node IP address.

### Removing storage resources from permanently deleted nodes

If you permanently delete a node, and don't wish to restore it to your system, you can also delete the storage resources associated with that node. 

In the following commands, note the following variables:

  * `ADMIN-KUBECONFIG` specifies the path to the admin cluster
  * `USER_CLUSTER_CONFIG` specifies the path to the cluster config YAML file.


  1. Check and get the name of the persistent volume (PV) associated with the node:
         
         kubectl get pv --kubeconfig ${KUBECONFIG}  \
         -A -o=jsonpath='{range .items[*]}{"\n"}{.metadata.name}{":\t"}{.spec.claimRef.name}{":\t}  \
         {.spec.nodeAffinity.required.nodeSelectorTerms[0].matchExpressions[0].values}{"\n"}{end}'
         

  2. Delete the PV associated with the node:
         
         kubectl delete pv PV_NAME --kubeconfig ${KUBECONFIG}
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
