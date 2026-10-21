---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ca-rotation/
title: Rotating user cluster certificate authorities \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:04.418690+00:00
---

# Rotating user cluster certificate authorities  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ca-rotation/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Rotating user cluster certificate authorities Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/ca-rotation)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/ca-rotation)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud uses certificates and private keys to authenticate and encrypt connections between system components in user clusters. The admin cluster creates a new set of certificate authorities (CAs) for each user cluster, and uses these CA certificates to issue additional leaf certificates for system components. The admin cluster manages distribution of the public CA certificates and leaf certificate keypairs to system components, to establish their secure communication.

The user cluster CA rotation feature allows you to trigger a rotation of the core system certificates in a user cluster. During a rotation, the admin cluster replaces the core system CAs for the user cluster with newly generated CAs, and distributes the new public CA certificates and leaf certificate key pairs to user cluster system components. The rotation happens incrementally, so that system components can continue to communicate during the rotation. Note, however, that workloads and nodes will be restarted during the rotation.

There are three system CAs managed by the admin cluster for each user cluster:

  * The etcd CA secures communication from the API server to the etcd replicas and also traffic between etcd replicas. This CA is self-signed.
  * The cluster CA secures communication between the API server and all internal Kubernetes API clients (kubelets, controllers, schedulers). This CA is self-signed.
  * The front-proxy CA secures communication with [aggregated APIs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/). This CA is self-signed.



You may additionally be using an [org CA](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/security) to sign the certificate configured by the `authentication.sni` option. This CA and the SNI certificate are used to serve the Kubernetes API to clients outside the cluster. You manage this CA and manually generate the SNI certificate. Neither this CA nor the SNI certificate is affected by the user cluster CA rotation feature.

## Limitations

**Warning:** A CA rotation revokes the old CAs at the end of the operation. This invalidates kubeconfig files and authentication configuration files that were issued and distributed based on the old CA. These credentials will stop working after a CA rotation. The following instructions include details on how to download a new user cluster kubeconfig via the admin cluster and regenerate authentication configuration files after the CA rotation completes.

  * The user cluster CA rotation feature is supported on Anthos clusters on VMware clusters version 1.8 and above.
  * The user cluster CA rotation feature is specifically limited to the etcd, cluster, and front-proxy CAs mentioned in the overview. It does not rotate your org CA. user cluster CA rotation feature is additionally limited to certificates issued automatically by Anthos clusters on VMware. It does not update certificates issued manually by an administrator, even if those certificates are signed by the system CAs.
  * A CA rotation must restart the API server, other control-plane processes, and each node in the cluster multiple times. Each stage of a CA rotation progresses similarly to a cluster upgrade. While the user cluster does remain operational during a CA rotation, you should expect that workloads will be restarted and rescheduled. You should also expect brief periods of control-plane downtime when not using an HA configuration.
  * User cluster kubeconfig files and authentication configuration files for connecting to user clusters must be manually updated and redistributed following a CA rotation. This is because a CA rotation necessarily revokes the old CA, so these credentials will no longer authenticate.
  * Once initiated, a CA rotation cannot be paused or rolled-back.
  * A CA rotation may take considerable time to complete, depending on the size of the user cluster.



## How to perform a CA rotation

You can initiate a CA rotation and view the current status of the rotation by running the below gkectl commands.

### Rotate CA Certificates

To trigger a CA rotation, execute the following command.
    
    
    gkectl update credentials certificate-authorities rotate \
    --config USER_CONFIG_FILE \
    --kubeconfig ADMIN_KUBECONFIG_FILE
    

Where:

  * USER_CONFIG_FILE is the path to the user cluster configuration file of the user cluster to rotate CAs for.
  * ADMIN_KUBECONFIG_FILE is the path to the kubeconfig file for connecting to the admin cluster that manages the user cluster.



If the CA rotation is started successfully, you will see a message similar to the following:
    
    
    successfully started the CA rotation with CAVersion 2, use gkectl update credentials certificate-authorities status command to view the current state of CA rotation
    

If a CA rotation is already in progress, you will see an error message similar to the following:
    
    
    Exit with error:
    admission webhook "vonpremusercluster.onprem.cluster.gke.io" denied the request: requests must not modify CAVersion when cluster is not ready: ready condition is not true: ClusterCreateOrUpdate: Creating or updating user cluster control plane workloads
    

### View CA rotation status

To view the status of a CA rotation, execute the following command. This command reports the `CAVersion`, an integer the system automatically increments to differentiate the CAs used before and after each CA rotation, a status (`True` or `False`) that indicates whether the CA rotation is complete, and message describing which `CAVersion` is currently in use by each component of the system.
    
    
    gkectl update credentials certificate-authorities status \
    --config USER_CONFIG_FILE \
    --kubeconfig ADMIN_KUBECONFIG_FILE
    

If the CA rotation has already completed, you will see a message similar to the following:
    
    
    State of CARotation with CAVersion 2 is -
    status: True,
    reason: CARotationCompleted,
    message: Control plane has CA bundle [2], certs from CA 2, CA 2 is CSR signer. Data plane has CA bundle [2], CA 2 was CSR signer at last restart.
    

If the CA rotation is still in progress, you will see a message similar to the following:
    
    
    State of CARotation with CAVersion 2 is -
    status: False,
    reason: CARotationProgressed,
    message: Control plane has CA bundle [1 2], certs from CA 2, CA 1 is CSR signer. Data plane has CA bundle [1 2], CA 1 was CSR signer at last restart.
    

### Update User Cluster Credentials

Once a CA rotation completes, a new user cluster kubeconfig file must be downloaded from the admin cluster to replace the old kubeconfig that was previously used for connecting to user clusters. This is because the CA rotation revokes the old CA that the old kubeconfig file was based on. Run the following command after the CA rotation completes to download the new kubeconfig file:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG_FILE get secret admin \
     -n USER_CLUSTER_NAME -o jsonpath='{.data.admin\.conf}' \
     | base64 --decode > USER_CLUSTER_NAME-kubeconfig
    

If additional kubeconfig files were manually issued to other users of the cluster, they must also be updated.

### Update Authentication Configuration Files

Once the CA rotation completes, authentication configuration files must be updated and redistributed. Follow the linked instructions to update and redistribute these files after the CA rotation:

  * [Authenticating with OIDC](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/oidc)
  * [Authenticating with OIDC and AD FS](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/oidc-adfs)
  * [Authenticating with OIDC and Google](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/oidc-google)



## Control Plane Certificates Rotation

Without rotation, both the user cluster CAs and control-plane certificates will expire in 5 years from the date the cluster was created. The user cluster's control plane certificates are automatically rotated within ten hours of each user cluster upgrade, but the CAs are not automatically rotated. This means a CA rotation must be performed at least once every 5 years, in addition to regular version upgrades.

To prevent a user cluster from becoming unavailable, control-plane certificates are rotated within ten hours following a user cluster upgrade. When this happens, a message appears in the user cluster's CA rotation status.

To view the last version a user cluster has been upgraded to when control plane certificates were rotated:
    
    
    gkectl update credentials certificate-authorities status \
    --config USER_CONFIG_FILE \
    --kubeconfig ADMIN_KUBECONFIG_FILE
    

If a user cluster has recently been upgraded to version 1.10 or higher, a message will appear in the end of `message` field within ten hours. For example:
    
    
    Last Leaf Certificates Rotation Version: 1.10.0-gke.0.
    

## Troubleshooting a CA rotation

The `gkectl diagnose` command supports checking the expected status of a completed CA rotation against a user-cluster. For instructions on how to run gkectl diagnose on a user cluster, see [Diagnosing cluster issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#diagnose_user_cluster). If you experience issues with a CA rotation, please contact Google support and provide the `gkectl diagnose` output.

**Note:** Since this command checks for the expected end state of a CA rotation, it is expected for it to report that some certificates have not yet been rotated when run during a CA rotation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
