---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/ca-rotation/
title: Rotate certificate authorities \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:49.918408+00:00
---

# Rotate certificate authorities  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/ca-rotation/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Rotate certificate authorities Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/ca-rotation)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/ca-rotation)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Distributed Cloud uses certificates and private keys to authenticate and encrypt connections between system components in clusters. The cluster certificate authority (CA) manages these certificates and keys. When you run the `bmctl update credentials certificate-authorities rotate` command, Google Distributed Cloud performs the following actions:

  * Creates and uploads new cluster certificate authorities (CAs) for the cluster CA, the etcd CA, and the front-proxy CA to the user cluster namespace in the admin cluster.

  * The admin cluster controllers replace the user cluster certificate authorities with the newly generated ones.

  * The admin cluster controllers distribute the new public CA certificates and leaf certificate key pairs to user cluster system components.




To maintain secure cluster communication, rotate your user cluster CA periodically and whenever there is a possible security breach.

**Important:** If your cluster certificates have expired, you must renew them manually to regain cluster operation. For more information and instructions, see [Renew expired cluster certificates manually](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/expired-certs).

## Before you begin

Before you rotate your cluster's certificate authority, plan according to the following conditions and impacts:

  * Ensure admin and user clusters are at version 1.9.0 or higher before starting the CA rotation.

  * CA rotation is incremental, allowing system components to communicate during the rotation.

  * The CA rotation process restarts the API server, control plane processes, and pods in the user cluster.

  * Expect workloads to restart and be rescheduled during CA rotation.

  * For non-high-availability cluster configurations, expect brief periods of control plane downtime during CA rotation.

  * Cluster management operations aren't allowed during CA rotation.

  * CA rotation duration depends on the size of your cluster. For example, CA rotation may take close to two hours to complete for a cluster with one control plane and 50 worker nodes.




## Limitations

The certificate authority rotation capability has the following limitations:

  * CA rotation doesn't update certificates issued manually by an administrator, even if the cluster CA signs the certificates. Update and redistribute any manually issued certificates after user cluster CA rotation is complete.

  * Once started, CA rotation can't be paused or rolled back.




## Start a cluster CA rotation

Use the following command to start the CA rotation process:
    
    
    bmctl update credentials certificate-authorities rotate --cluster CLUSTER_NAME \
        --kubeconfig KUBECONFIG
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster for which you want to rotate CAs.
  * `KUBECONFIG`: the path to the admin cluster kubeconfig file. For self-managing clusters, this file is the cluster's kubeconfig file.



The `bmctl` command exits after the CA is rotated successfully and a new kubeconfig file is generated. The standard path for the kubeconfig file is `bmctl-workspace/CLUSTER_NAME/CLUSTER_NAME-kubeconfig`.

## Troubleshoot a cluster CA rotation

The `bmctl update credentials` command displays the progress of the CA rotation. The associated `update-credentials.log` file is saved to the following timestamped directory:

`bmctl-workspace/CLUSTER_NAME/log/update-credentials-TIMESTAMP`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
