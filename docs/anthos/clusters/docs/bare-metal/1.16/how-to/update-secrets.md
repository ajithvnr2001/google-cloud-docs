---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-secrets/
title: Rotate service account keys \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:34.818194+00:00
---

# Rotate service account keys  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-secrets/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Rotate service account keys Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/update-secrets)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/update-secrets)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



To rotate the service account keys in Google Distributed Cloud, you update the existing cluster credentials with the `bmctl` command. This service account key rotation might be as part of your regular processes to update credentials, or in response to a potential exposure of the keys. When you update cluster credentials, the new information is passed to admin or hybrid clusters, or automatically routed to affected user clusters managed by an admin cluster.

## Cluster credentials that can be updated

Google Distributed Cloud clusters require multiple credentials when they are created. You set the credentials in the cluster config when you create an admin, standalone, or hybrid cluster. User clusters, as noted above, are managed by an admin cluster (or a hybrid cluster acting as admin), and will reuse the same credentials from the admin cluster.

For more information about creating clusters and different cluster types, see [Installation overview: choosing a deployment model](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/install-prep).

You can update the following credentials, and their corresponding secrets, in Google Distributed Cloud clusters with the `bmctl` command:

  * **SSH private key** : Used for node access.
  * **Container Registry key** (`anthos-baremetal-gcr`): Service account key used to authenticate with Container Registry for image pulling.
  * **Connect agent service account key** (`anthos-baremetal-connect`): Service account key used by Connect agent pods.
  * **Connect registry service account key** (`anthos-baremetal-register`): Service account key used to authenticate with GKE Fleet when registering or unregistering a cluster.
  * **Cloud operations service account key** (`anthos-baremetal-cloud-ops`): Service account key to authenticate with Google Cloud Observability (logging & monitoring) APIs.



## Update credentials with `bmctl`

When you create clusters, Google Distributed Cloud creates Kubernetes Secrets based on your credential keys. If you generate new keys, you must update the corresponding Secrets as described in the following steps. If the name or path to your keys change, you must also update the corresponding cluster configuration file.

  1. Prepare the new values for the credentials you want to update:

     * You can [generate new Google service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) through the `gcloud` command or through the Google Cloud console.

     * Generate new SSH private key on the admin workstation and make sure the cluster node machines have the corresponding public key.

  2. Update the credentials section of your cluster configuration file with paths to the new keys.

  3. Update the corresponding cluster Secrets with the `bmctl update credentials` command, adding the appropriate flags described below.

For example, here `bmctl` updates the credentials for a new SSH private key, where ADMIN_KUBECONFIG specifies the path to the kubeconfig of the admin, hybrid, or standalone cluster, SSH_KEY_PATH specifies the path to the new SSH private key, and CLUSTER_NAME specifies the name of the cluster:
         
         bmctl update credentials --kubeconfig ADMIN_KUBECONFIG --ssh-private-key-path
         SSH_KEY_PATH --cluster CLUSTER_NAME
         




You can specify the following flags with `bmctl` to update credentials:

Flag | description  
---|---  
`--kubeconfig` | **required** , path to the kubeconfig of the admin, hybrid, or standalone cluster  
`--cluster` | **required** , name of the admin, hybrid, or standalone cluster  
`--ssh-private-key-path` | path to the new SSH private key  
`--gcr-key-path` | path to the new Container Registry service account key  
`--gke-connect-agent-service-account-key-path` | path to the new Connect agent service account key  
`--gke-connect-register-service-account-key-path` | path to the new Connect register service account key  
`--cloud-operations-service-account-key-path` | path to the new Google Cloud Observability service account key  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
