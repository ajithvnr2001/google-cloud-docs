---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-user-cluster/
title: Back up and restore a user cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:10.195923+00:00
---

# Back up and restore a user cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-user-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Back up and restore a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to back up and restore the etcd store for a user cluster created with Google Distributed Cloud (software only) for VMware. This page also provides a script that you can use to automatically back up a cluster's etcd store.

You can create a backup file for recovery from unexpected disasters that might damage your cluster's etcd data. Store the backup file in a location that is outside of the cluster and isn't dependent on the cluster's operation.

**Note:** Using a third-party backup tool, such as Veeam, to back up a user cluster isn't supported. Backing up the cluster with a third-party tool might lead to unforeseen errors in cluster operations.

## Limitations

  * This procedure does not back up application-specific data.

  * This procedure does not back up your PersistentVolumes.

  * Workloads scheduled after you create a backup aren't restored with that backup.

  * You can't restore a cluster after a failed upgrade.

  * This procedure isn't intended to restore a deleted cluster.

  * Don't use this procedure for clusters with [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters) enabled. Instead, refer to [Back up and restore advanced clusters with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-advanced-cluster-with-gkectl).


**Warning:** Using a backup file to restore your etcd data is a last resort. We don't recommend restoring from a backup file unless the cluster is completely broken. Contact Google support for help in deciding the best course of action.

For more information about limitations, see [Infrastructure incompatibility](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/infrastructure-incompatibility).

## Backing up a user cluster

A user cluster backup is a snapshot of the user cluster's etcd store. The etcd store contains all of the Kubernetes objects and custom objects required to manage cluster state. The snapshot contains the data required to recreate the cluster's components and workloads.

The backup steps that you follow depend on whether Controlplane V2 is enabled on the user cluster. When Controlplane V2 is enabled, the control plane for the user cluster runs on the user cluster itself. When Controlplane V2 isn't enabled, the control plane for the user cluster runs on one or more nodes in the admin cluster, which is referred to as kubeception.

Run the following command to determine whether the cluster has Controlplane V2 enabled:
    
    
    kubectl get onpremuserclusters --kubeconfig USER_CLUSTER_KUBECONFIG \
      -n kube-system -o jsonpath='{.items[0].spec.enableControlplaneV2}' && echo
    

If the output is `true`, follow the **Controlplane V2** steps to back up the cluster. Otherwise, follow the **Kubeception** steps.

### Kubeception

  1. Get a shell into the `kube-etcd` container:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG exec -it \
          kube-etcd-0 -c kube-etcd -n USER_CLUSTER_NAME \
          -- /bin/sh
         

where:

     * ADMIN_CLUSTER_KUBECONFIG is the admin cluster's kubeconfig file.
     * USER_CLUSTER_NAME is the name of the user cluster.
  2. In your shell, in the `/tmp` directory, create backup named `snapshot.db`:
         
         ETCDCTL_API=3 etcdctl \
           --endpoints=https://127.0.0.1:2379 \
           --cacert=/etcd.local.config/certificates/etcdCA.crt \
           --cert=/etcd.local.config/certificates/etcd.crt \
           --key=/etcd.local.config/certificates/etcd.key \
           snapshot save /tmp/snapshot.db
         

  3. In your shell, enter `exit` to exit the shell.

  4. Copy `/tmp/snapshot.db` from the `kube-etcd` container to the current directory:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG cp \
           USER_CLUSTER_NAME/kube-etcd-0:/tmp/snapshot.db \
           --container kube-etcd snapshot.db
         




### Controlplane V2

  1. Get the etcd Pod's name:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get pods \
          -n kube-system -l component=etcd,tier=control-plane -ojsonpath='{$.items[*].metadata.name}{"\n"}'
         

where:

     * USER_CLUSTER_KUBECONFIG is the user cluster's kubeconfig file.

Example:
    
    NAME          READY   STATUS    RESTARTS   AGE
    etcd-uc1-cp1  1/1     Running   0          38m
    etcd-uc1-cp2  1/1     Running   0          37m
    etcd-uc1-cp3  1/1     Running   0          38m
    

Note that there can be multiple `etcd` pods, example, 3 for HA clusters. For backup, any `etcd` pod should work.

  2. Get a shell into the `etcd` container:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG exec -it \
          POD_NAME -c etcd -n kube-system -- /bin/sh
         
         

where:

     * POD_NAME is the name of the etcd pod taken from the previous step.
  3. In your shell, create a backup file named `snapshot.db`:
         
         ETCDCTL_API=3 etcdctl \
           --endpoints=https://127.0.0.1:2379 \
           --cacert=/etc/kubernetes/pki/etcd/ca.crt \
           --cert=/etc/kubernetes/pki/etcd/server.crt \
           --key=/etc/kubernetes/pki/etcd/server.key \
           snapshot save /tmp/snapshot.db
         

  4. In your shell, enter `exit` to exit the shell.

  5. Copy `snapshot.db` from the `etcd` container to the workstation home directory:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
          cp POD_NAME:/tmp/snapshot.db ~/snapshot.db \
          -c etcd -n kube-system
         

  6. Copy the secrets from the PKI directory:
         
         ssh -i NODE_NAME.key ubuntu@NODE_EXTERNAL_IP
         sudo chmod -R 0644 /etc/kubernetes/pki/*
         sudo chmod 0755 /etc/kubernetes/pki/etcd
         exit
         scp -ri NODE_NAME.key ubuntu@NODE_EXTERNAL_IP:/etc/kubernetes/pki ~/pki_NODE_NAME
         

where:

     * NODE_NAME is the file containing [ssh key](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node#user) for the control plane node
     * NODE_EXTERNAL_IP is the IP address of the user control plane node from where you want the secrets to be copied from.
**Note:** For HA clusters, copy the secrets from all the user control plane nodes using the instructions



## Restoring a user cluster from a backup (non-HA)

Before you use a backup file to restore your user cluster's etcd store, [diagnose your cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster) and resolve existing issues. Using a backup to restore a problematic cluster might re-create or exacerbate issues. Contact the Google Cloud support team for further assistance with restoring your clusters.

The following instructions explain how to use a backup file to restore a user cluster in cases where the cluster's etcd data has become damaged and the user cluster's etcd Pod is crashlooping.

### Kubeception

You can restore the etcd data by deploying a utility Pod that overwrites the damaged data with the backup. The admin cluster's API server must be running and the admin cluster's scheduler must be able to schedule new Pods.

  1. Find the name of the Secret used by etcd in the user cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG -n USER_CLUSTER_NAME \
            get secrets | grep kube-etcd-certs
         

  2. Copy the following Pod manifest to a file named `etcd-utility.yaml`. Replace the following:

     * `NODE_NAME`: the node where the `kube-etcd-0` Pod is running.

     * `ADMIN_CLUSTER_KUBECONFIG`: the admin cluster's kubeconfig file.

     * `USER_CLUSTER_NAME`: the name of the user cluster.

     * `GKE_ON_PREM_VERSION`: the version of the cluster where you want to perform the etcd restore (for example, 1.5.0-gke.0).

     * `KUBE_ETCD_SECRET_NAME`: the name of the Secret used by etcd in the user cluster, starting with `kube-etcd-certs`.
    
    apiVersion: v1
    kind: Pod
    metadata:
     name: etcd-utility-0
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
         claimName: data-kube-etcd-0
     - name: etcd-certs
       secret:
         defaultMode: 420
         secretName: KUBE_ETCD_SECRET_NAME
    

  3. Deploy the utility Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           create -f etcd-utility.yaml --namespace USER_CLUSTER_NAME
         

  4. Copy `snapshot.db` from the current directory to the root directory of the utility Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG cp snapshot.db \
           USER_CLUSTER_NAME/etcd-utility-0:snapshot.db --container etcd-utility
         

  5. Get a shell into the `etcd-utility` container:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG exec it \
           etcd-utility-0 --container etcd-utility --namespace USER_CLUSTER_NAME \
           -- bin/sh
         

  6. In your shell, in the root directory, run the following command to create a new folder that contains the backup:
         
         ETCDCTL_API=3 etcdctl \
           --endpoints=https://127.0.0.1:2379 \
           --cacert=/etcd.local.config/certificates/etcdCA.crt \
           --cert=/etcd.local.config/certificates/etcd.crt \
           --key=/etcd.local.config/certificates/etcd.key \
           snapshot restore snapshot.db
         

  7. In your shell, delete the old etcd data:
         
         rm -r var/lib/etcd/*
         

  8. In your shell, copy the restored etcd data to its permanent location:
         
         cp -r default.etcd/* var/lib/etcd/
         

  9. In your shell, enter `exit` to exit the shell.

  10. Delete the crashing etcd Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           delete pod kube-etcd-0 --namespace USER_CLUSTER_NAME
         

  11. Verify that the etcd Pod is no longer crashing.

  12. Delete the utility Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           delete pod etcd-utility-0 --namespace USER_CLUSTER_NAME

  13. Remove `etcd-utility.yaml` from the current directory:
         
         rm etcd-utility.yaml
         




### Controlplane V2

You can restore the `etcd` data one at a time by deploying a temporary etcd container that overwrites the damaged data with the backup.

  1. Get a shell into the user control plane node:
         
         ssh -i NODE_NAME.key ubuntu@NODE_EXTERNAL_IP
         

  2. In the shell, stop the Kubernetes API server and the etcd server:
         
         sudo mv /etc/kubernetes/manifests/kube-apiserver.yaml /etc/kubernetes/manifests/etcd.yaml ~
         

  3. In the shell, enter `exit` to exit the shell.

  4. Run `scp` to copy the backup file `snapshot.db` & secrets to the user control plane node:
         
         scp -i NODE_NAME.key ~/snapshot.db ubuntu@NODE_EXTERNAL_IP:/tmp/
         
         
         chmod a+rw pki/
         scp -ri NODE_NAME.key ~/pki_NODE_NAME ubuntu@NODE_EXTERNAL_IP:/etc/kubernetes/pki
         

  5. In the shell, use `snapshot.db` to restore the etcd data:
         
         ETCDCTL_API=3 sudo etcdctl \
          --cacert=/etc/kubernetes/pki/etcd/ca.crt \
          --cert=/etc/kubernetes/pki/etcd/server.crt \
          --key=/etc/kubernetes/pki/etcd/server.key \
          --data-dir=/opt/data/var/lib/etcd \
          --name=NODE_NAME \
          --initial-advertise-peer-urls=https://NODE_IP_ADDRESS:2380 \
          --initial-cluster=NODE_NAME=https://NODE_IP_ADDRESS:2380 \
          snapshot restore /tmp/snapshot.db
         

Replace the following:

     * `NODE_NAME`: the name of the node where the restore is being performed
     * `NODE_IP_ADDRESS`: the IP address of the said node.
  6. Add the flag `- --initial-cluster-state=new` in the etcd manifest file under container command.

Example:
         
         containers:
               - command:
                 - etcd
                 ...
                 - --initial-cluster-state=new
                 ...

  7. In the shell, start the kube-apiserver and etcd servers:
         
         sudo mv ~/etcd.yaml ~/kube-apiserver.yaml /etc/kubernetes/manifests/
         

  8. In the shell, enter `exit` to exit the shell.


**Note:** If `events-etcd` pods are in `CrashLoopBackOff` state then add the flag `- --initial-cluster-state=new` and restart the pods. The events will be out-of-sync and you would lose events stored previously.

## Restoring a user cluster from a backup (HA)

### Kubeception

This section shows how to restore the etcd data for a high-availability (HA) user cluster.

For an HA user cluster, there are three nodes in the admin cluster that serve as control planes for the user cluster. Each of those nodes runs an etcd Pod that maintains etcd data on a storage volume.

If two of the etcd Pods are healthy, and the data on the associated storage volumes is intact, then there is no need to use a backup file. That is because you still have an etcd quorum.

In the rare case that two of the etcd storage volumes have corrupt data, you need to use a backup file to restore the etcd data.

To perform the steps in this section, you must have already created a `snapshot.db` file as described in Backing up a user cluster.

### Listing your etcd Pods and nodes

  1. List the etcd Pods that manage the etcd store for your user cluster. These Pods run in the admin cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods --namespace USER_CLUSTER_NAME \
         --output wide | grep kube-etcd
         

The output shows the etcd Pods and the nodes where the Pods run. The nodes shown in the output are nodes in the admin cluster that serve as control planes for your user cluster:
         
         NAME              ...   NODE
         kube-etcd-0       ...   xxx
         kube-etcd-1       ...   yyy
         kube-etcd-2       ...   zzz
         

  2. Make a note of the Pod names and the control plane node names for later.

Notice that each etcd Pod is named `kube-etcd` appended with a number. This number is called the _member number_ for the Pod. It identifies the Pod as being a particular member of the etcd cluster that holds the object data for your user cluster. This guide uses the placeholder MEMBER_NUMBER to refer to the etcd Pod member number.

Also notice that each Pod in your etcd cluster runs on its own node.




### Preparing to deploy the utility Pods

  1. Save a manifest for the PodDisruptionBudget (PDB) for the user cluster's Kubernetes API server. Then delete the PDB.
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG get pdb --namespace USER_CLUSTER_NAME \
         kube-apiserver-pdb --output yaml > kube-apiserver-pdb.yaml
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG delete pdb --namespace USER_CLUSTER_NAME \
         kube-apiserver-pdb
         

  2. Stop the Kubernetes API server and the etcd maintenance Deployment. This ensures that no components will use etcd during restoration:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG --namespace USER_CLUSTER_NAME \
         scale --replicas 0 statefulset kube-apiserver
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG --namespace USER_CLUSTER_NAME \
         scale --replicas 0 deployment gke-master-etcd-maintenance
         

  3. Recall the name of the container image for your etcd Pods.




### Deploying the utility Pods

**Important:** Perform the steps in this section for each of your etcd Pods.

  1. Recall the name of the etcd Pod and the name of the node where the Pod runs.

  2. Save the following Pod manifest in the current directory in a file named `etcd-utility-MEMBER_NUMBER.yaml`:



    
    
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
    

The preceding manifest describes a utility Pod that you run temporarily to restore etcd data.

  1. Create the utility Pod in your admin cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG apply -f etcd-utility-MEMBER_NUMBER.yaml
         

  2. Copy your backup file, `snapshot.db`, to the root directory of your utility Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG cp snapshot.db \
         USER_CLUSTER_NAME/etcd-utility-MEMBER_NUMBER:snapshot.db
         

  3. Get a shell into the `etcd-utility` container in the utility Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG exec -it --namespace USER_CLUSTER_NAME \
         etcd-utility-MEMBER_NUMBER --container etcd-utility -- bin/sh
         

  4. In your shell, in the root directory, use `snapshot.db` to restore the etcd data:
         
         ETCDCTL_API=3 etcdctl \
         --endpoints=https://127.0.0.1:2379 \
         --cacert=/etcd.local.config/certificates/etcdCA.crt \
         --cert=/etcd.local.config/certificates/etcd.crt \
         --key=/etcd.local.config/certificates/etcd.key \
         --name=kube-etcd-MEMBER_NUMBER \
         --initial-cluster=kube-etcd-0=https://kube-etcd-0.kube-etcd:2380,kube-etcd-1=https://kube-etcd-1.kube-etcd:2380,kube-etcd-2=https://kube-etcd-2.kube-etcd:2380 \
         --initial-cluster-token=etcd-cluster-1 \
         --initial-advertise-peer-urls=https://kube-etcd-MEMBER_NUMBER.kube-etcd:2380 \
         snapshot restore snapshot.db
         

The preceding command stored etcd data in the `/kube-etcd-MEMBER_NUMBER.etcd` directory.

  5. In your shell, delete the old etcd data:
         
         rm -r var/lib/etcd/*
         

  6. In your shell, copy the restored etcd data to its permanent location:
         
         cp -r kube-etcd-MEMBER_NUMBER.etcd/* var/lib/etcd/
         

  7. In your shell, remove the temporary etcd directory and the backup file:
         
         rm -R kube-etcd-MEMBER_NUMBER.etcd/
         rm snapshot.db
         

  8. In your shell, enter `exit` to exit the shell.

  9. Delete the utility Pod:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG delete pod \
         --namespace USER_CLUSTER_NAME etcd-utility-MEMBER_NUMBER
         




### Restarting components

Now that you have deployed and deleted your utility Pods, you need to restart some cluster components.

  1. Restart the Pods in the `kube-etcd` StatefulSet:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG rollout restart statefulset \
         --namespace USER_CLUSTER_NAME kube-etcd
         

  2. Start the Kubernetes API servers for your user cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG scale statefulset --replicas 3 \
         --namespace USER_CLUSTER_NAME kube-apiserver
         

  3. Start the etcd maintenance Deployment for your user cluster:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG scale deployment --replicas 1 \
         --namespace=USER_CLUSTER_NAME  gke-master-etcd-maintenance
         

  4. Restore the PDB for the Kubernetes API server:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONIFG apply -f kube-apiserver-pdb.yaml
         




### Controlplane V2

This section shows how to restore the etcd data for a high-availability (HA) user cluster.

For a HA user cluster, there are three nodes in the user cluster that serves as control plane for the user cluster. Each of those nodes runs an etcd Pod that maintains etcd data on a storage volume.

If two of the etcd Pods are healthy, and the data on the associated storage volumes is intact, then there is no need to use a backup file. That is because you'd still have an etcd quorum.

In the rare case that two of the etcd storage volumes have corrupt data, you need to use a backup file to restore the etcd data.

To do the steps in this section, you must have already created a `snapshot.db` file as described in Backing up a user cluster.

### Listing your etcd Pods and nodes

**Important:** Do the steps in the following sections for each of your user cluster CP nodes.

  1. List the etcd Pods and their respective node:
         
         kubectl get pod --kubeconfig USER_CLUSTER_KUBECONFIG \
          -n kube-system -l component=etcd,tier=control-plane -o wide
         

The output shows the etcd Pods and the nodes where the Pods run. The nodes shown in the output are nodes in the admin cluster that serve as control planes for your user cluster:
         
         NAME           ...   NODE
         etcd-xxx       ...   xxx
         etcd-yyy       ...   yyy
         etcd-zzz       ...   zzz
         

  2. Make a note of the Pod names and the control plane node names for later.

Notice that each etcd Pod is named `etcd-xxx` appended with a node name. This is because in Controlplane V2 the etcd pods runs as a static pod.




### Preparing to restore

  1. Run `scp` to copy the backup file `snapshot.db` to all the user control plane nodes:
         
         scp -i NODE_NAME.key ~/snapshot.db ubuntu@NODE_EXTERNAL_IP:/tmp/
         

  2. Copy the secrets to the respective user control plane node:
         
         chmod a+rw ~/pki_*
         scp -ri NODE_NAME.key ~/pki_NODE_NAME/* ubuntu@NODE_EXTERNAL_IP:/opt/data/etc/kubernetes/pki/
         

  3. Get a shell into the user control plane node:
         
         ssh -i NODE_NAME.key ubuntu@NODE_EXTERNAL_IP
         




### Performing the restore

  1. Recall the name of the etcd Pod and the name of the node where the Pod runs.

  2. In the shell, stop the Kubernetes API server and the etcd server on all the user control plane nodes:
         
         sudo mv /etc/kubernetes/manifests/kube-apiserver.yaml /etc/kubernetes/manifests/etcd.yaml ~
         

  3. In the shell, use `snapshot.db` to restore the etcd data on all the user control plane nodes:
         
         ETCDCTL_API=3 sudo etcdctl \
          --cacert=/etc/kubernetes/pki/etcd/ca.crt \
          --cert=/etc/kubernetes/pki/etcd/server.crt \
          --key=/etc/kubernetes/pki/etcd/server.key \
          --data-dir=/opt/data/var/lib/etcd \
          --name=NODE_NAME \
          --initial-advertise-peer-urls=https://NODE_IP_ADDRESS:2380 \
          --initial-cluster=NODE1=https://NODE1_IP:2380,NODE2=https://NODE2_IP:2380,NODE3=https://NODE3_IP:2380 \
          snapshot restore /tmp/snapshot.db
         

Replace the following:

     * `NODE_NAME`: the name of the node where the restore is being performed.
     * `NODE_IP_ADDRESS`: the IP address of the said node.
     * Fill the `NODE1`, `NODE2`, `NODE3` and the `NODE1_IP`, `NODE2_IP`, `NODE3_IP` of their respective node for `--initial-cluster` flag. You can also get this from the etcd manifest.
  4. Add the flag `- --initial-cluster-state=existing` in the etcd manifest file under container command.

Example:
         
         containers:
               - command:
                 - etcd
                 ...
                 - --initial-cluster-state=existing
                 ...




### Restarting components

  1. In the shell, start the `kube-apiserver` and `etcd` servers in all the user control plane nodes:
         
         sudo mv ~/etcd.yaml ~/kube-apiserver.yaml /etc/kubernetes/manifests/
         

  2. In the shell, enter `exit` to exit the shell.

  3. Verify the `kube-apiserver` and `etcd` is running on all user control plane nodes:
         
         kubectl get pod --kubeconfig USER_CLUSTER_KUBECONFIG \
         -n kube-system -l tier=control-plane
         


**Note:** If `events-etcd` pods are in `CrashLoopBackOff` state then add the flag `- --initial-cluster-state=new` and restart the pods. The events will be out-of-sync and you would lose events stored previously.

## Automatic cluster backup

You can use the script given here as an example on how to automatically back up your clusters. Note that the following script is not supported, and should only be used as reference to write a better, more robust and complete script. Before you run the script, fill in values for the five variables at the beginning of the script:

### Kubeception

  * Set `BACKUP_DIR` to the path where you want to store the admin and user cluster backups. This path shouldn't exist.
  * Set `ADMIN_CLUSTER_KUBECONFIG` to the path of the admin cluster's kubeconfig file
  * Set `USER_CLUSTER_NAMESPACE` to the name of your user cluster. The name of your user cluster is a namespace in the admin cluster.
  * Set `EXTERNAL_IP` to the VIP that you reserved for the admin control plane service.
  * Set `SSH_PRIVATE_KEY` to the path of your SSH key.
  * If you are using a private network, set `JUMP_IP` to your network's jump server's IP address.


    
    
    #!/usr/bin/env bash
    
    # Automates manual steps for taking backups of user and admin clusters.
    # Fill in the variables below before running the script.
    
    BACKUP_DIR=""                       # path to store user and admin cluster backups
    ADMIN_CLUSTER_KUBECONFIG=""         # path to admin cluster kubeconfig
    USER_CLUSTER_NAMESPACE=""           # user cluster namespace
    EXTERNAL_IP=""                      # admin control plane node external ip - follow steps in documentation
    SSH_PRIVATE_KEY=""                  # path to vsphere_tmp ssh private key - follow steps in documentation
    JUMP_IP=""                          # network jump server IP - leave empty string if not using private network.
    
    mkdir -p $BACKUP_DIR
    mkdir $BACKUP_DIR/pki
    
    # USER CLUSTER BACKUP
    
    # Snapshot user cluster etcd
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} exec -it -n ${USER_CLUSTER_NAMESPACE} kube-etcd-0 -c kube-etcd -- /bin/sh -ec "export ETCDCTL_API=3; etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etcd.local.config/certificates/etcdCA.crt --cert=/etcd.local.config/certificates/etcd.crt --key=/etcd.local.config/certificates/etcd.key snapshot save ${USER_CLUSTER_NAMESPACE}_snapshot.db"
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} cp ${USER_CLUSTER_NAMESPACE}/kube-etcd-0:${USER_CLUSTER_NAMESPACE}_snapshot.db $BACKUP_DIR/user-cluster_${USER_CLUSTER_NAMESPACE}_snapshot.db 
    
    # ADMIN CLUSTER BACKUP
    
    # Set up ssh options
    SSH_OPTS=(-oStrictHostKeyChecking=no -i ${SSH_PRIVATE_KEY})
    if [ "${JUMP_IP}" != "" ]; then
      SSH_OPTS+=(-oProxyCommand="ssh -oStrictHostKeyChecking=no -i ${SSH_PRIVATE_KEY} -W %h:%p ubuntu@${JUMP_IP}")
    fi
    
    # Copy admin certs
    ssh "${SSH_OPTS[@]}" ubuntu@${EXTERNAL_IP} 'sudo chmod -R +rw /etc/kubernetes/pki/*'
    scp -r "${SSH_OPTS[@]}" ubuntu@${EXTERNAL_IP}:/etc/kubernetes/pki/* ${BACKUP_DIR}/pki/
    
    # Snapshot admin cluster etcd
    admin_etcd=$(kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} get pods -n kube-system -l component=etcd,tier=control-plane -ojsonpath='{$.items[*].metadata.name}{"\n"}')
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} exec -it -n kube-system ${admin_etcd} -- /bin/sh -ec "export ETCDCTL_API=3; etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt --key=/etc/kubernetes/pki/etcd/healthcheck-client.key snapshot save admin_snapshot.db"
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} cp -n kube-system ${admin_etcd}:admin_snapshot.db $BACKUP_DIR/admin-cluster_snapshot.db
    

### Controlplane V2

  * Set `BACKUP_DIR` to the path where you want to store the admin and user cluster backups. This path shouldn't exist.
  * Set `ADMIN_CLUSTER_KUBECONFIG` to the path of the admin cluster's kubeconfig file
  * Set `USER_CLUSTER_KUBECONFIG` to the path of your user cluster kubeconfig.
  * Set `EXTERNAL_IP` to the VIP that you reserved for the admin control plane service.
  * Set `SSH_PRIVATE_KEY` to the path of your SSH key.
  * If you are using a private network, set `JUMP_IP` to your network's jump server's IP address.


    
    
    #!/usr/bin/env bash
    
    # Automates manual steps for taking backups of user and admin clusters.
    # Fill in the variables below before running the script.
    
    BACKUP_DIR=""                       # path to store user and admin cluster backups
    ADMIN_CLUSTER_KUBECONFIG=""         # path to admin cluster kubeconfig
    USER_CLUSTER_KUBECONFIG=""          # path to user cluster kubeconfig
    EXTERNAL_IP=""                      # admin control plane node external ip - follow steps in documentation
    SSH_PRIVATE_KEY=""                  # path to ssh private key - follow steps in documentation
    JUMP_IP=""                          # network jump server IP - leave empty string if not using private network
    
    mkdir -p $BACKUP_DIR
    mkdir $BACKUP_DIR/pki
    
    # USER CLUSTER BACKUP
    user_etcd=$(kubectl --kubeconfig=${USER_CLUSTER_KUBECONFIG} get pods -n kube-system -l component=etcd,tier=control-plane -ojsonpath='{$.items[0].metadata.name}{"\n"}')
    kubectl --kubeconfig=${USER_CLUSTER_KUBECONFIG} exec -it -n kube-system ${user_etcd} -c etcd -- /bin/sh -ec "export ETCDCTL_API=3; etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /tmp/${user_etcd}_snapshot.db"
    kubectl --kubeconfig=${USER_CLUSTER_KUBECONFIG} cp kube-system/${user_etcd}:/tmp/${user_etcd}_snapshot.db $BACKUP_DIR/${user_etcd}_snapshot.db
    
    # ADMIN CLUSTER BACKUP
    
    # Set up ssh options
    SSH_OPTS=(-oStrictHostKeyChecking=no -i ${SSH_PRIVATE_KEY})
    if [ "${JUMP_IP}" != "" ]; then
      SSH_OPTS+=(-oProxyCommand="ssh -oStrictHostKeyChecking=no -i ${SSH_PRIVATE_KEY} -W %h:%p ubuntu@${JUMP_IP}")
    fi
    
    # Copy admin certs
    ssh "${SSH_OPTS[@]}" ubuntu@${EXTERNAL_IP} 'sudo chmod -R +rw /etc/kubernetes/pki/*'
    scp -r "${SSH_OPTS[@]}" ubuntu@${EXTERNAL_IP}:/etc/kubernetes/pki/* ${BACKUP_DIR}/pki/
    
    # Snapshot admin cluster etcd
    admin_etcd=$(kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} get pods -n kube-system -l component=etcd,tier=control-plane -ojsonpath='{$.items[*].metadata.name}{"\n"}')
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} exec -it -n kube-system ${admin_etcd} -- /bin/sh -ec "export ETCDCTL_API=3; etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt --key=/etc/kubernetes/pki/etcd/healthcheck-client.key snapshot save /tmp/${admin_etcd}_snapshot.db"
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} cp -n kube-system ${admin_etcd}:/tmp/${admin_etcd}_snapshot.db $BACKUP_DIR/${admin_etcd}_snapshot.db
    

## Verify the restoration

To verify that your cluster was successfully restored, run [gkectl diagnose cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster).

## What's next

  * [Back up and restore an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-admin-cluster)
  * [Diagnose cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose)
  * [Learn about auger](https://github.com/etcd-io/auger), an open-source tool for restoring individual objects from etcd backups.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
