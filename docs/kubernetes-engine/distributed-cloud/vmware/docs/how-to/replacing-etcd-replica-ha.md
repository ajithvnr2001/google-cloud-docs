---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/replacing-etcd-replica-ha/
title: Replacing a failed etcd replica \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:45.383309+00:00
---

# Replacing a failed etcd replica  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/replacing-etcd-replica-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Replacing a failed etcd replica Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to replace a failed etcd replica in a high availability (HA) user cluster for Google Distributed Cloud.

The instructions given here apply to an HA user cluster that uses [kubeception](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster); that is, a user cluster that does not have [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) enabled. If you need to replace an etcd replica in a user cluster that has Controlplane V2 enabled, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support).

## Before you begin

  * Make sure the admin cluster is working correctly.

  * Make sure the other two etcd members in the user cluster are working correctly. If more than one etcd member has failed, see [Recovery from etcd data corruption or loss](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery#recovery_from_etcd_data_corruption_or_loss).




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

     2. Add a new member with the same name and peer URL as the failed replica node.
            
            etcdctl member add MEMBER_NAME --peer-urls=https://MEMBER_NAME.kube-etcd:2380

Where `MEMBER_NAME` is the identifier of the failed kube-etcd replica node. For example, `kube-etcd-1` or `kube-etcd2`.

  6. List the etcd Pods that manage the etcd store for your user cluster. These Pods run in the admin cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods --namespace USER_CLUSTER_NAME \
             --output wide | grep kube-etcd
         

The output shows the etcd Pods and the nodes where the Pods run. The nodes shown in the output are nodes in the admin cluster that serve as control planes for your user cluster:
         
         NAME              ...   NODE
         kube-etcd-0       ...   node-abc
         kube-etcd-1       ...   node-yyy
         kube-etcd-2       ...   node-zzz
         

  7. Make a note of the Pod names and the control plane node names to use in the Pod manifest that you create in the next step.

Notice that each etcd Pod is named `kube-etcd` appended with a number. This number is called the _member number_ for the Pod. It identifies the Pod as being a particular member of the etcd cluster that holds the object data for your user cluster. This guide uses the placeholder MEMBER_NUMBER to refer to the etcd Pod member number.

Also notice that each Pod in your etcd cluster runs on its own node.

  8. Create a Pod manifest that describes a utility Pod that you run temporarily to restore etcd data. Save the following Pod manifest in the current directory in a file named `etcd-utility-MEMBER_NUMBER.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: etcd-utility-MEMBER_NUMBER
           namespace: USER_CLUSTER_NAME
         spec:
           containers:
           - command: ["/bin/sh"]
             args: ["-ec", "while :; do echo '.'; sleep 5 ; done"]
             image: gcr.io/gke-on-prem-release/etcd-util:GKE_ON_PREM_VERSION
             name: etcd-utility
             volumeMounts:
             - mountPath: /var/lib/etcd
               name: data
             - mountPath: /etcd.local.config/certificates
               name: etcd-certs
           nodeSelector:
             kubernetes.googleapis.com/cluster-name: USER_CLUSTER_NAME
             kubernetes.io/hostname: NODE_NAME
           tolerations:
           - effect: NoExecute
             key: node.kubernetes.io/not-ready
             operator: Exists
             tolerationSeconds: 300
           - effect: NoExecute
             key: node.kubernetes.io/unreachable
             operator: Exists
             tolerationSeconds: 300
           - effect: NoSchedule
             key: node.kubernetes.io/unschedulable
             operator: Exists
           volumes:
           - name: data
             persistentVolumeClaim:
               claimName: data-kube-etcd-MEMBER_NUMBER
           - name: etcd-certs
             secret:
               defaultMode: 420
               secretName: KUBE_ETCD_SECRET_NAME
         

Replace the following:

     * `NODE_NAME`: the node where the `kube-etcd-0` Pod is running.

     * `USER_CLUSTER_NAME`: the name of the user cluster.

     * `GKE_ON_PREM_VERSION`: the version of the cluster where you want to perform the etcd restore (for example, 1.31.100-gke.136).

     * `KUBE_ETCD_SECRET_NAME`: the name of the Secret used by etcd in the user cluster, starting with `kube-etcd-certs`.

  9. Create the utility Pod in your admin cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG apply -f etcd-utility-MEMBER_NUMBER.yaml
         

  10. Clean up the etcd data directory from within the utility Pod.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG exec -it -n USER_CLUSTER_NAME etcd-utility-MEMBER_NUMBER -- /bin/bash -c 'rm -rf /var/lib/etcd/*'

  11. Delete the utility Pod.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG delete pod -n USER_CLUSTER_NAME etcd-utility-MEMBER_NUMBER

  12. Uncordon the failed node.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG uncordon NODE_NAME

  13. Open the kube-etcd StatefulSet in your text editor.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME edit statefulset kube-etcd

Change the value of the `--initial-cluster-state` flag to `new`.
         
         containers:
             - name: kube-etcd
               ...
               args:
                 - --initial-cluster-state=new
               ...
          

  14. Restore the etcd PDB which was deleted in step 1.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG apply -f /path/to/etcdpdb.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
