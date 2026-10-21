---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-ca-rotation/
title: Rotating admin cluster CA certificates \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:04.834292+00:00
---

# Rotating admin cluster CA certificates  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-ca-rotation/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Rotating admin cluster CA certificates Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/admin-ca-rotation)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/admin-ca-rotation)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud use certificates and private keys to authenticate communication between Kubernetes system components in an admin cluster. When you create an admin cluster, new certificate authority (CA) certificates are created, and these root certificates are used to issue additional leaf certificates for Kubernetes system components.

This guide applies only to rotation of admin cluster CA certificates. For user clusters, see [Rotating user cluster CA certificates](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/ca-rotation).

There are three CA certificates used by the Kubernetes system in an admin cluster:

  * The etcd CA certificate secures communication from the Kubernetes API server to the etcd replicas and also communication between etcd replicas. This certificate is self-signed.

  * The cluster CA certificate secures communication between the Kubernetes API server and all internal Kubernetes API clients, for example, the kubelet, the controller manager, and the scheduler. This certificate is self-signed.

  * The front-proxy CA certificate secures communication with [aggregated APIs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/). This certificate is self-signed.




You can use `gkectl` to trigger a certificate rotation. During a rotation, `gkectl` replaces the core system CA certificates for the admin cluster with newly generated certificates. Then it distributes the new CA certificates, leaf certificates, and private keys to admin cluster system components. The rotation happens incrementally, so that system components can continue to communicate during the rotation. Note, however, that workloads and nodes are restarted during the rotation.

Without rotation, CA certificates and control-plane certificates will expire five years from the date the cluster was created. The control plane certificates are automatically rotated during a cluster upgrade, but the CAs are not automatically rotated. This means a CA rotation must be performed at least once every five years, in addition to regular version upgrades.

**Warning:** A CA certificate rotation revokes the old CA certificates at the end of the operation. This invalidates kubeconfig files that were based on an old certificate. Consequently, the credentials in the kubeconfig file stop working after a CA certificate rotation. This guide includes instructions on how to update your kubeconifg file. The same issue applies to authentication configuration files.

## Limitations

  * CA certificate rotation limited to the etcd, cluster, and front-proxy certificates mentioned previously.

  * CA certificate rotation is limited to certificates issued automatically by Google Distributed Cloud. It does not update certificates issued manually by an administrator, even if those certificates are signed by the system CAs.

  * CA certificate rotation restarts the Kubernetes API server, other control-plane processes, and each node in the admin cluster multiple times. Each stage of a rotation progresses similarly to a cluster upgrade. While the admin cluster and the user clusters managed by the admin cluster do remain operational during a certificate rotation, you should expect that workloads in the admin cluster will be restarted and rescheduled. You should also expect brief periods of downtime for the admin cluster control plane and user cluster control plane.

  * You must update the admin cluster kubeconfig file in the middle of a certificate rotation and again after the rotation completes. This is because the old cluster certificate is revoked, and the credentials in the kubeconfig file will no longer work.

  * Once initiated, a CA certificate rotation cannot be rolled back.

  * A CA certificate rotation might take considerable time to complete, depending on the size of the cluster.

  * The certificate rotation process can be resumed by re-running the same command if it is interrupted. However, you must ensure that there is only one rotation command running at a time.




## Start the rotation

To start the certificate rotation, run the following command. It performs the first half of the rotation and stops at a pause point.

Start the rotation:
    
    
    gkectl update credentials certificate-authorities rotate \
        --admin-cluster \
        --config ADMIN_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

Replace the following:

  * ADMIN_CLUSTER_CONFIG: the path of the admin cluster configuration file

  * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file




If the command is interrupted, resume it by running the same command.

## Update the kubeconfig file

When the preceding command pauses, update the kubeconfig file for the admin cluster. This places a new client certificate and a new CA certificate in the kubeconfig file. The old client certificate is removed from the kubeconfig file, and the old CA certificate remains in the kubeconfig file.
    
    
    gkectl update credentials certificate-authorities update-kubeconfig \
        --admin-cluster \
        --config ADMIN_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

## Continue the rotation

Run the following command to perform the second half of the procedure. The command will not proceed until `gkectl` verifies that the updated kubeconfig file is in the current directory.
    
    
    gkectl update credentials certificate-authorities rotate \
        --admin-cluster \
        --complete \
        --config ADMIN_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

If the command is interrupted, resume it by running the same command.

When the rotation is complete, it reports the current CA version.

## Update the kubeconfig file again

After the second half of the rotation completes, update the kubeconfig file again. This removes the old CA certificate from the kubeconfig file.
    
    
    gkectl update credentials certificate-authorities update-kubeconfig \
        --admin-cluster \
        --config ADMIN_CLUSTER_CONFIG \
        --kubeconfig ADMIN_CLUSTER_KUBECONFIG
    

## Distribute the new kubeconfig file

Distribute the new admin cluster kubeconfig file to all cluster users.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
