---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-secrets/
title: Rotate service account keys \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:43.629163+00:00
---

# Rotate service account keys  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Rotate service account keys Stay organized with collections  Save and categorize content based on your preferences. 

To rotate the service account keys in Google Distributed Cloud, you update the existing cluster credentials with the `bmctl` command. This service account key rotation might be as part of your regular processes to update credentials, or in response to a potential exposure of the keys. When you update cluster credentials, the new information is passed to admin or hybrid clusters, or automatically routed to affected user clusters managed by an admin cluster.

## Cluster credentials that can be updated

Google Distributed Cloud clusters require multiple credentials when they are created. You set the credentials in the cluster config when you create an admin, standalone, or hybrid cluster. User clusters, as noted previously, are managed by an admin cluster (or a hybrid cluster acting as admin), and will reuse the same credentials from the admin cluster.

For more information about creating clusters and different cluster types, see [Installation overview: choosing a deployment model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep).

You can update the following credentials, and their corresponding secrets, in Google Distributed Cloud clusters with the `bmctl` command:

  * **SSH private key** : Used for node access.
  * **Artifact Registry key** (`anthos-baremetal-gcr`): Service account key used to authenticate with Artifact Registry for image pulling.
  * **Connect agent service account key** (`anthos-baremetal-connect`): Service account key used by Connect agent pods.
  * **Connect register service account key** (`anthos-baremetal-register`): Service account key used to authenticate with GKE Fleet when registering or unregistering a cluster.
  * **Cloud operations service account key** (`anthos-baremetal-cloud-ops`): Service account key to authenticate with Google Cloud Observability (logging & monitoring) APIs.



## Update credentials with `bmctl`

When you create clusters, Google Distributed Cloud creates Kubernetes Secrets based on your credential keys. If you generate new keys, you must update the corresponding Secrets as described in the following steps. If the name or path to your keys change, you must also update the corresponding cluster configuration file.

  1. Prepare the new values for the credentials you want to update:

     * You can [generate new Google service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating) through the Google Cloud CLI or through the Google Cloud console.

     * Generate new SSH private key on the admin workstation and make sure the cluster node machines have the corresponding public key.

  2. Update the credentials section of your cluster configuration file with paths to the new keys.

  3. Update the corresponding cluster Secrets with the `bmctl update credentials` command, adding the appropriate flags.

The following example updates the credentials for a new SSH private key:
         
         bmctl update credentials --kubeconfig ADMIN_KUBECONFIG \
             --cluster CLUSTER_NAME \
             --ssh-private-key-path SSH_KEY_PATH
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the kubeconfig file of the admin or self-managing cluster.

     * `CLUSTER_NAME`: the name of the cluster that you're updating the SSH key for.

     * `SSH_KEY_PATH`: the path of the SSH key file. By default, `bmctl` checks the SSH and service account key files specified in the cluster configuration file. If `bmctl` finds an expired key file, the command fails. If you have the new valid key file in a different location than what's specified in the configuration file, include the `--ignore-validation-errors` flag to avoid this failure.

For a complete list of the flags that you can use with the `bmctl update credentials` command, see [update credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#update_credentials) in the `bmctl` command reference.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
