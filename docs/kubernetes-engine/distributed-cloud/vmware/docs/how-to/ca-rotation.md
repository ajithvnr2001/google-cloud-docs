---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ca-rotation/
title: Rotating user cluster certificate authorities \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:52.666459+00:00
---

# Rotating user cluster certificate authorities  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ca-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Rotating user cluster certificate authorities Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud uses certificates and private keys to authenticate and encrypt connections between system components in user clusters. The admin cluster creates a new set of certificate authorities (CAs) for each user cluster, and uses CA certificates to issue additional leaf certificates for system components. The admin cluster manages distribution of the public CA certificates and leaf certificate key pairs to system components to establish their secure communication.

The user cluster CA rotation feature lets you trigger a rotation of the core system certificates in a user cluster. During a rotation, the admin cluster replaces the core system CAs for the user cluster with newly generated CAs, and distributes the new public CA certificates and leaf certificate key pairs to user cluster system components. The rotation happens incrementally, so that system components can continue to communicate during the rotation. Note, however, that workloads and nodes are restarted during the rotation.

There are three system CAs managed by the admin cluster for each user cluster:

  * The etcd CA secures communication from the API server to the etcd replicas and also traffic between etcd replicas. This CA is self-signed.
  * The cluster CA secures communication between the API server and all internal Kubernetes API clients (kubelets, controllers, schedulers). This CA is self-signed.
  * The front-proxy CA secures communication with [aggregated APIs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/). This CA is self-signed.



Also, you might be using an [org CA](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/security) to sign the certificate configured by the `authentication.sni` option. This CA and the SNI certificate are used to serve the Kubernetes API to clients outside the cluster. You manage this CA and manually generate the SNI certificate. Neither this CA nor the SNI certificate is affected by the user cluster CA rotation feature.

## Limitations

**Warning:** A CA rotation revokes the old CAs at the end of the operation. This invalidates kubeconfig files and authentication configuration files that were issued and distributed based on the old CA. These credentials stop working after a CA rotation. The following instructions include details on how to download a new user cluster kubeconfig from the admin cluster and regenerate authentication configuration files after the CA rotation completes.

  * Note the following limitation with advanced clusters:

    * Version 1.31: CA rotation isn't supported on [advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field).
    * Version 1.32 and higher: CA rotation is supported on advanced clusters, but there are some minor differences noted where applicable in this document.
  * CA certificate rotation is limited to the etcd, cluster, and front-proxy CAs mentioned previously.

  * CA certificate rotation is limited to certificates issued automatically by Google Distributed Cloud. It doesn't update certificates issued manually by an administrator, even if those certificates are signed by the system CAs.

  * A CA rotation restarts the API server, other control-plane processes, and each node in the cluster multiple times. Each stage of a CA rotation progresses similarly to a cluster upgrade. While the user cluster does remain operational during a CA rotation, you should expect that workloads to be restarted and rescheduled. You should also expect brief periods of control-plane downtime if your user cluster does not have a [high-availability control plane](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-ips-section).

  * You must update the user cluster kubeconfig file and authentication configuration files after a CA rotation. This is because the old cluster certificate is revoked, and the credentials in the kubeconfig file no longer work.

  * After a CA rotation is started, it cannot be paused or rolled-back.

  * A CA rotation might take considerable time to complete, depending on the size of the user cluster.




## Perform a CA rotation

  1. Start the rotation:
         
         gkectl update credentials certificate-authorities rotate \
             --config USER_CLUSTER_CONFIG \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace the following:

     * USER_CLUSTER_CONFIG: the path of the user cluster configuration file

     * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file




The behavior of the command differs depending on whether advanced cluster is enabled:

### Not enabled

If advanced cluster isn't enabled on the cluster, the command is asynchronous and starts the CA rotation and then exits. You don't need to watch the output of the command for the entire duration of the CA rotation. Instead, you can periodically check on the progress by running the `gkectl update credentials certificate-authorities status` command.

If the CA rotation starts successfully, you see a message similar to following:
    
    
    successfully started the CA rotation with CAVersion 2, use gkectl update credentials certificate-authorities status command to view the current state of CA rotation
    

If a CA rotation is already in progress, you see an error message similar to the following:
    
    
    Exit with error:
    admission webhook "vonpremusercluster.onprem.cluster.gke.io" denied the request: requests must not modify CAVersion when cluster is not ready: ready condition is not true: ClusterCreateOrUpdate: Creating or updating user cluster control plane workloads
    

To view the status of the rotation:
    
    
    gkectl update credentials certificate-authorities status \
        --config USER_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

The preceding command reports the `CAVersion`, which is an integer the system automatically increments to differentiate the CAs used before and after a rotation. The command also reports a status (`True` or `False`) that indicates whether the CA rotation is complete, and a message describing which `CAVersion` is currently in use by each component of the system.

If the CA rotation has already completed, you see a message similar to this:
    
    
    State of CARotation with CAVersion 2 is -
    status: True,
    reason: CARotationCompleted,
    message: Control plane has CA bundle [2], certs from CA 2, CA 2 is CSR signer. Data plane has CA bundle [2], CA 2 was CSR signer at last restart.
    

If the CA rotation is still in progress, you see a message similar to this:
    
    
    State of CARotation with CAVersion 2 is -
    status: False,
    reason: CARotationProgressed,
    message: Control plane has CA bundle [1 2], certs from CA 2, CA 1 is CSR signer. Data plane has CA bundle [1 2], CA 1 was CSR signer at last restart.
    

### Update user cluster credentials

On clusters that don't have advanced cluster enabled, you must get a new user cluster kubeconfig file from the admin cluster. This is because the CA rotation revokes the CA that the old kubeconfig file was based on.

Get a new kubeconfig file:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get secret admin \
      -n USER_CLUSTER_NAME -o jsonpath='{.data.admin\.conf}' \
      | base64 --decode > USER_CLUSTER_NAME-kubeconfig
    

### Enabled

If advanced cluster is enabled, the `gkectl update credentials certificate-authorities rotate` command is synchronous. The command outputs status messages to the admin workstation as the CA rotation progresses.

After the CA is rotated successfully, the command exits and a new kubeconfig file is automatically generated. The command output provides the name of the new kubeconfig file, and is similar to the following:
    
    
    Beginning CA rotation with generated CA
    ...
    Successfully rotated CA for user cluster "USER_CLUSTER_NAME". The
    kubeconfig file "/home/ubuntu"/USER_CLUSTER_NAME-kubeconfig" has
    been updated.
    

The new kubeconfig is located in the same directory as the admin cluster kubeconfig that you specified in the command. The name of the new kubeconfig is `USER_CLUSTER_NAME-kubeconfig`.

## Distribute the new kubeconfig file

Distribute the new kubeconfig file to everyone who uses a kubeconfig file to interact with the cluster.

## Update authentication configuration files

After the CA rotation completes, authentication configuration files must be updated and redistributed. For more information see [Manage user identity](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/authentication).

## Control plane certificates rotation

Without rotation, both the user cluster CAs and control-plane certificates expire ten years from the date the cluster was created (for versions before 1.36.100, these certificates expire after five years). The user cluster's control-plane certificates are automatically rotated within ten hours of each user cluster upgrade, but the CAs are not automatically rotated. This means a CA rotation must be performed at least once every ten years (five years for versions before 1.36.100) in addition to regular version upgrades.

To prevent a user cluster from becoming unavailable, control-plane certificates are rotated within ten hours following a user cluster upgrade. When this happens, a message appears in the user cluster's CA rotation status.

To view the last version a user cluster has been upgraded to when control-plane certificates were rotated:
    
    
    gkectl update credentials certificate-authorities status \
    --config USER_CLUSTER_CONFIG \
    --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

The information appears at the end of the `message` field within ten hours of an upgrade. For example:
    
    
    Last Leaf Certificates Rotation Version: 1.16.0-gke.0.
    

## Troubleshooting a CA rotation

The `gkectl diagnose` command supports checking the expected status of a completed CA rotation against a user-cluster. For instructions on how to run `gkectl diagnose` on a user cluster, see [Diagnosing cluster issues](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster). If you experience issues with a CA rotation, contact Google support and provide the `gkectl diagnose` output.

**Note:** Because this command checks for the expected end state of a CA rotation, it is expected for it to report that some certificates have not yet been rotated when run during a CA rotation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
