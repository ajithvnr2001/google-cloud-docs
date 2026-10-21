---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/replacing-etcd-replica-ha/
title: Replacing a failed etcd replica \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:56.271397+00:00
---

# Replacing a failed etcd replica  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/replacing-etcd-replica-ha/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Replacing a failed etcd replica Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/replacing-etcd-replica-ha)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/replacing-etcd-replica-ha)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document describes how to replace a failed etcd replica in a high availability (HA) user cluster.

The instructions given here apply to an HA user cluster that uses [kubeception](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster); that is, a user cluster that does not have [Controlplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#enablecontrolplanev2-field) enabled. If you need to replace an etcd replica in a user cluster that has Controlplane V2 enabled, [contact Cloud Customer Care](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/getting-support).

## Before you begin

  * Make sure the admin cluster is working correctly.

  * Make sure the other two etcd members in the user cluster are working correctly. If more than one etcd member has failed, see [Recovery from etcd data corruption or loss](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/high-availability-disaster-recovery#recovery_from_etcd_data_corruption_or_loss).




## Replacing a failed etcd replica

  1. Back up a copy of the etcd PodDisruptionBudget (PDB) so you can restore it later.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME get pdb kube-etcd-pdb -o yaml > PATH_TO_PDB_FILE

Where:

     * `ADMIN_CLUSTER_KUBECONFIG` is the path to the kubeconfig file for the admin cluster.

     * `USER_CLUSTER_NAME` is the name of the user cluster that contains the failed etcd replica.

     * `PATH_TO_PDB_FILE` is the path where you want to save the etcd PDB file, for instance `/tmp/etcpdb.yaml`.

  2. Delete the etcd PodDisruptionBudget (PDB).
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME delete pdb kube-etcd-pdb

  3. Run the following command to open the kube-etcd [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) in your text editor:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME edit statefulset kube-etcd

Change the value of the `--initial-cluster-state` flag to `existing`.
         
         containers:
             - name: kube-etcd
               ...
               args:
                 - --initial-cluster-state=existing
               ...
          

  4. Drain the failed etcd replica node.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG drain NODE_NAME --ignore-daemonsets --delete-local-data

Where `NODE_NAME` is the name of the failed etcd replica node.

  5. Create a new shell in the container of one of the working kube-etcd pods.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG exec -it \
            KUBE_ETCD_POD --container kube-etcd --namespace USER_CLUSTER_NAME \
            -- bin/sh

Where `KUBE_ETCD_POD` is the name of the working kube-etcd pod. For example, `kube-etcd-0`.

From this new shell, run the following commands:

     1. Remove the failed etcd replica node from the etcd cluster.

First, list all the members of the etcd cluster:
            
            etcdctl member list -w table

The output shows all the member IDs. Determine the member ID of the failed replica.

Next, remove the failed replica:
            
            export ETCDCTL_CACERT=/etcd.local.config/certificates/etcdCA.crt
            export ETCDCTL_CERT=/etcd.local.config/certificates/etcd.crt
            export ETCDCTL_CERT=/etcd.local.config/certificates/etcd.crt
            export ETCDCTL_KEY=/etcd.local.config/certificates/etcd.key
            export ETCDCTL_ENDPOINTS=https://127.0.0.1:2379
            etcdctl member remove MEMBER_ID

Where `MEMBER_ID` is the hex member ID of the failed etcd replica pod.

  6. Follow steps 1-3 of [Deploying the utility Pods](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/backing-up#deploy_utility_pods) to create a utility Pod in the admin cluster. This Pod is used to access the PersistentVolume (PV) of the failed etcd member in the user cluster.

  7. Clean up the etcd data directory from within the utility Pod.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG exec -it -n USER_CLUSTER_NAME etcd-utility-MEMBER_NUMBER -- /bin/bash -c 'rm -rf /var/lib/etcd/*'

  8. Delete the utility Pod.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG delete pod -n USER_CLUSTER_NAME etcd-utility-MEMBER_NUMBER

  9. Uncordon the failed node.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG uncordon NODE_NAME

  10. Open the kube-etcd StatefulSet in your text editor.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME edit statefulset kube-etcd

Change the value of the `--initial-cluster-state` flag to `new`.
         
         containers:
             - name: kube-etcd
               ...
               args:
                 - --initial-cluster-state=new
               ...
          

  11. Restore the etcd PDB which was deleted in step 1.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG apply -f /path/to/etcdpdb.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
