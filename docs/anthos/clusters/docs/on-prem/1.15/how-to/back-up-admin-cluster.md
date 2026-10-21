---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-admin-cluster/
title: Back up and restore an admin cluster \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:56.361288+00:00
---

# Back up and restore an admin cluster  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-admin-cluster/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Back up and restore an admin cluster Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/back-up-admin-cluster)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/back-up-admin-cluster)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to backup and restore the etcd store for an admin cluster. This document also provides a script that you can use to automatically back up a cluster's etcd store.

You can create a backup file for recovery from foreseen disasters that might damage your cluster's etcd data. Store the backup file in a location that is outside of the cluster and is not dependent on the cluster's operation.

**Warning:** Using a backup file to restore your etcd data is a last resort. We do not recommend restoring from a backup file unless the cluster is completely broken. Contact Google support for help in deciding the best course of action.

## Limitations

  * This procedure does not back up application-specific data.

  * This procedure does not back up your PersistentVolumes.

  * Workloads scheduled after you create a backup aren't restored with that backup.

  * You cannot restore a cluster after a failed upgrade.

  * This procedure is not intended to restore a deleted cluster.




## Backing up an admin cluster

**Note:** A new preview feature provides an easier way to perform backups. See [Back up and restore an admin cluster with `gkectl`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-and-restore-an-admin-cluster-with-gkectl). Consider using that method instead of the one described in this section.

An admin cluster backup contains the following:

  * A snapshot of the admin cluster's etcd.
  * Admin control plane's Secrets, which are required for authenticating to the admin and user clusters.



Complete the following steps before you create an admin cluster backup:

  1. Find the admin cluster's external IP address, which is used to SSH in to the admin cluster control plane:
         
         kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] get nodes -n kube-system -o wide | grep master

where [ADMIN_CLUSTER_KUBECONFIG] is the admin cluster's kubeconfig file.

  2. Create an SSH key called `vsphere_tmp` from the admin cluster's private key.

You can find the private key from the admin clusters Secrets:
         
         kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] get secrets sshkeys -n kube-system -o yaml

In the command output, you can find the private key in the `vsphere_tmp` field.

Copy the private key to `vsphere_tmp`:
         
         echo "[PRIVATE_KEY]" | base64 -d > vsphere_tmp; chmod 600 vsphere_tmp

  3. Check that you can shell into the admin control plane using this private key:
         
         ssh -i vsphere_tmp ubuntu@[EXTERNAL_IP]
         

  4. Exit the container:
         
         exit




### Backing up an admin cluster's etcd store

To back up the admin cluster's etcd store:

  1. Get the etcd Pod's name:
         
         kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] get pods \
             -n kube-system -l component=etcd,tier=control-plane -ojsonpath='{$.items[*].metadata.name}{"\n"}'

  2. Shell into Pod's kube-etcd container:
         
         kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]  exec -it \
             -n kube-system [ADMIN_ETCD_POD] -- bin/sh

where [ADMIN_ETCD_POD] is the name of the etcd Pod.

  3. From the shell, use `etcdctl` to create a backup named `snapshot.db` in the local directory:
         
         ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt \
             --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt \
             --key=/etc/kubernetes/pki/etcd/healthcheck-client.key snapshot save /tmp/snapshot.db
         

  4. Exit the container:
         
         exit

  5. Copy the backup out of the kube-etcd container using `kubectl cp`:
         
         kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] cp \
         kube-system/[ADMIN_ETCD_POD]:tmp/snapshot.db [RELATIVE_DIRECTORY]
         

where [RELATIVE_DIRECTORY] is a path where you want to store your backup.




### Backing up an admin cluster's Secrets

To back up the admin control plane's Secrets:

  1. Use SSH to connect to the admin control plane node:
         
         ssh -i vsphere_tmp ubuntu@EXTERNAL_IP
         

Replace `EXTERNAL_IP` with the admin control plane's external IP address, which you noted previously.

  2. Optional but highly recommended: Create a local backup directory.

You need to change the backup Secrets' permissions to copy them out of the node.
         
         mkdir backup

  3. Locally copy the Secrets to the local backup directory:
         
         sudo cp -r /etc/kubernetes/pki/* backup/

  4. Change the permissions of the backup Secrets:
         
         sudo chmod -R a+rX backup/

  5. Exit the admin control plane node:
         
         exit

  6. Run `scp` to copy the backup folder out of the admin control plane node:
         
         sudo scp -r -i vsphere_tmp  ubuntu@EXTERNAL_IP:backup/ RELATIVE_DIRECTORY
         

Replace `RELATIVE_DIRECTORY` with a path where you want to store your backup.




## Restoring an admin cluster

**Note:** A new preview feature provides an easier way to restore an admin cluster. See [Back up and restore the admin cluster with `gkectl`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-and-restore-an-admin-cluster-with-gkectl).

The following procedure recreates a backed-up admin cluster and all of the user control planes it managed when its etcd snapshot was created.

**Note:** The user cluster can still run its workloads even if the user control plane is down. However, if a user control plane is down, it can't schedule new or updated workloads or handle other cluster failures.

  1. Run `scp` to copy `snapshot.db` to the admin control plane:
         
         sudo scp -i vsphere_tmp snapshot.db ubuntu@[EXTERNAL_IP]:

where [EXTERNAL_IP] is the admin control plane's external IP address, which you gathered previously.

  2. Shell into the admin control plane:
         
         sudo ssh -i vsphere_tmp ubuntu@[EXTERNAL_IP]
         

  3. Copy `snapshot.db/` to `/mnt`:
         
         sudo cp snapshot.db /mnt/

  4. Make temporary directory, like `backup`:

**Note:** You don't need to do this if there is already a backup folder containing the Secrets.
         
         mkdir backup

  5. Exit the admin control plane:
         
         exit

  6. Copy the certificates to `backup/`:
         
         sudo scp -r -i vsphere_tmp [BACKUP_CERT_FILE] ubuntu@[EXTERNAL_IP]:backup/

  7. Shell into the admin control plane node:
         
         ssh -i vsphere_tmp ubuntu@[EXTERNAL_IP]
         

where [EXTERNAL_IP] is the admin control plane's external IP address, which you gathered previously.

  8. Stop `kube-etcd` and `kube-apiserver`.
         
         sudo mv /etc/kubernetes/manifests/etcd.yaml /tmp/etcd.yaml
         
         sudo mv /etc/kubernetes/manifests/kube-apiserver.yaml /tmp/kube-apiserver.yaml

  9. Copy the backup Secrets to `/etc/kubernetes/pki/`:
         
         sudo cp -r backup/* /etc/kubernetes/pki/

  10. Run `etcdctl restore` with Docker:
         
         sudo docker run --rm \
         -v '/mnt:/backup' \
         -v '/var/lib/etcd:/var/lib/etcd' --env ETCDCTL_API=3 'gcr.io/gke-on-prem-release/etcd-util:GKE_ON_PREM_VERSION' /bin/sh -c "etcdctl snapshot restore '/backup/snapshot.db'; rm -r /var/lib/etcd/*; mv /default.etcd/member/ /var/lib/etcd/"

  11. Restart `kube-etcd` and `kube-apiserver`.
         
         sudo mv /tmp/etcd.yaml /etc/kubernetes/manifests/etcd.yaml
         
         sudo mv /tmp/kube-apiserver.yaml /etc/kubernetes/manifests/kube-apiserver.yaml

  12. Verify `kube-etcd` and `kube-apiserver` have started.
         
         sudo crictl ps -a

**Note:** If `kube-etcd` or `kube-apiserver` are in an exited status Follow, [troubleshoot admin restore](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-admin-cluster#troubleshoot_admin_restore).
  13. Copy `/etc/kubernetes/admin.conf` to a `.kube` folder so it can be accessed from admin workstation:
         
         mkdir -p [HOME]/.kube
         
         sudo cp -i /etc/kubernetes/admin.conf [HOME]/.kube/config
         
         sudo chown $(id -u):$(id -g) $HOME/.kube/config

  14. Exit the admin control plane:
         
         exit

  15. Copy the newly generated kubeconfig file out of the admin node:
         
         sudo scp -i vsphere_tmp ubuntu@[EXTERNAL_IP]:[HOME]/.kube/config kubeconfig
         
         sudo chown $(id -u):$(id -g) kubeconfig

where:

     * [EXTERNAL_IP] is the admin control plane's external IP address.
     * [HOME] is the home directory on the admin node.

Now you can use this new kubeconfig file to access the restored cluster.




### Troubleshooting an admin cluster restore

If you encounter an issue when restoring the admin cluster, you must contact Google Support to resolve the issue with the admin cluster.

In the meantime, you can check the following to further troubleshoot.

  1. Find the etcd container id 
         
         sudo crictl ps -a | grep [ADMIN_ETCD_POD]

where [ADMIN_ETCD_POD] is the name of the etcd Pod.

  2. Examine the logs from the etc container 
         
         sudo crictl logs [ETCD_CONTAINER_ID]

where [ETCD_CONTAINER_ID] is the id of the etcd container.

  3. Look for the following permission denied log messages like

`etcdserver: create snapshot directory error:mkdir /var/lib/etcd/member/snap: permission denied`

  4. If permission denied messages are found update the ownership of /opt/data/var/lib/etcd/ 
         
         sudo chown -R 2001:2001 /opt/data/var/lib/etcd/

  5. Verify `kube-etcd` and `kube-apiserver` have started. 
         
         sudo crictl ps




## Automatic cluster backup

You can use the script given here as an example on how to automatically back up your clusters. Note that the following script is not supported, and should only be used as reference to write a better, more robust and complete script. Before you run the script, fill in values for the five variables at the beginning of the script:

  * Set `BACKUP_DIR` to the path where you want to store the admin and user cluster backups. This path should not exist.
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
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} exec -it -n ${USER_CLUSTER_NAMESPACE} kube-etcd-0 -c kube-etcd -- /bin/sh -ec "export ETCDCTL_API=3; etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etcd.local.config/certificates/etcdCA.crt --cert=/etcd.local.config/certificates/etcd.crt --key=/etcd.local.config/certificates/etcd.key snapshot save /tmp/${USER_CLUSTER_NAMESPACE}_snapshot.db"
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} cp ${USER_CLUSTER_NAMESPACE}/kube-etcd-0:tmp/${USER_CLUSTER_NAMESPACE}_snapshot.db $BACKUP_DIR/user-cluster_${USER_CLUSTER_NAMESPACE}_snapshot.db 
     
    # ADMIN CLUSTER BACKUP
     
    # Set up ssh options
    SSH_OPTS=(-oStrictHostKeyChecking=no -i ${SSH_PRIVATE_KEY})
    if [ "${JUMP_IP}" != "" ]; then
        SSH_OPTS+=(-oProxyCommand="ssh -oStrictHostKeyChecking=no -i ${SSH_PRIVATE_KEY} -W %h:%p ubuntu@${JUMP_IP}")
    fi
     
    # Copy admin certs
    ssh "${SSH_OPTS[@]}" ubuntu@${EXTERNAL_IP} 'sudo chmod -R a+rX /etc/kubernetes/pki/*'
    scp -r "${SSH_OPTS[@]}" ubuntu@${EXTERNAL_IP}:/etc/kubernetes/pki/* ${BACKUP_DIR}/pki/
     
    # Snapshot admin cluster etcd
    admin_etcd=$(kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} get pods -n kube-system -l component=etcd,tier=control-plane -ojsonpath='{$.items[*].metadata.name}{"\n"}')
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} exec -it -n kube-system ${admin_etcd} -- /bin/sh -ec "export ETCDCTL_API=3; etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt --key=/etc/kubernetes/pki/etcd/healthcheck-client.key snapshot save /tmp/admin_snapshot.db"
    kubectl --kubeconfig=${ADMIN_CLUSTER_KUBECONFIG} cp -n kube-system ${admin_etcd}:tmp/admin_snapshot.db $BACKUP_DIR/admin-cluster_snapshot.db
    

## What's next

  * [Back up and restore a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-user-cluster)
  * [Learn how to diagnose cluster issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose)
  * [Learn about augur](https://github.com/jpbetz/auger), an open-source tool for restoring individual objects from etcd backups.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
