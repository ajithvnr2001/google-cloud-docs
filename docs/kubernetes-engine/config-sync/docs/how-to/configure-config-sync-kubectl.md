---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl/
title: Configure Config Sync with kubectl commands \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:42.106177+00:00
---

# Configure Config Sync with kubectl commands  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Configure Config Sync with kubectl commands Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure Config Sync using `kubectl` commands after you've [installed Config Sync using the Google Cloud console or Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync).

While you can make many configuration changes using the console or CLI, you need to use `kubectl` commands to [override some Config Sync defaults](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#override-resources), to control SSL certificate verification, and to use a certificate authority.

## Create and edit the RootSync configuration file

To configure Config Sync using `kubectl` commands, you edit a [RootSync object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields) by creating a YAML file.

When you install Config Sync using the Google Cloud console or Google Cloud CLI, Config Sync automatically creates a RootSync object named `root-sync`. This object contains the most recent configuration information for Config Sync. Whenever you make a change in the Google Cloud console or Google Cloud CLI, `root-sync` is updated.

### Learn about the fields you can edit using `kubectl`

You can make advanced changes to `root-sync` using `kubectl` commands for the fields not supported in the Google Cloud console or Google Cloud CLI. If you want to create and then update RootSync or RepoSync objects directly using `kubectl` commands, see [RootSync and RepoSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

Before you make any changes to the YAML file that you create in the following section, familiarize yourself with the following table. This table lists the fields that you can edit and add. If you edit fields not listed in this table, Config Sync automatically reverts changes back to the values you set when you last configured Config Sync in the Google Cloud console or Google Cloud CLI.

Key | Description  
---|---  
`spec.helm` |  All fields for Helm repository configuration.   
`spec.override` |  All fields for overriding default configurations.   
`spec.git.noSSLVerify` |  Specifies whether to enable or disable SSL certificate verification for Git. The default is `false`.   
`spec.git.caCertSecretRef.name` |  The name of the Secret containing the certificate authority (CA) certificate for a Git repository.   
`spec.oci.caCertSecretRef.name` |  The name of the Secret containing the certificate authority (CA) certificate for an OCI repository.   
**Note:** Changes to fields that aren't in the preceding table are only reverted for the RootSync object that Config Sync creates when you install using the Google Cloud console or Google Cloud CLI. If you manually created a RootSync object named `root-sync` using an alternate installation method, you can edit all of the fields listed in [RootSync and RepoSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).

### Create the file

To create and edit a configuration file for `root-sync`, complete the following steps:

  1. To make sure that you're retrieving the configuration information for the correct cluster, configure `kubectl` command-line access:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --zone ZONE \
             --project PROJECT_ID
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster that has the Config Sync configuration that you want to change
     * `ZONE`: the zone that you created your cluster in
     * `PROJECT_ID`: your project ID
  2. Copy the configuration information from the RootSync object that Config Sync created into a YAML file:
         
         kubectl get rootsync root-sync -n config-management-system -o yaml >
         FILE_NAME.yaml
         

Replace `FILE_NAME` with a name for your configuration file.

  3. Open the YAML file that you created and make the required configuration changes. For example, to override the memory limit of the `git-sync` container, add the following fields in bold:
         
         apiVersion: v1
         items:
         - apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
         annotations:
           configmanagement.gke.io/managed-by-hub: "true"
           configmanagement.gke.io/update-time: "1644945169"
         creationTimestamp: "2022-02-15T17:12:52Z"
         generation: 1
         name: root-sync
         namespace: config-management-system
         resourceVersion: "211980457"
         uid: aa30a94b-2825-4590-ad30-5af848403502
         spec:
         git:
           auth: none
           branch: main
           dir: /quickstart/config-sync
           period: 15s
           repo: https://github.com/GoogleCloudPlatform/anthos-config-management-samples
           revision: HEAD
           secretRef: {}
         override:
           **resources :**
           **- containerName: "git-sync"**
             **memoryLimit : "400Mi"**
         sourceFormat: unstructured
         # Remainder of RootSync omitted
         

  4. Apply the changes to the YAML file:
         
         kubectl apply -f FILE_NAME.yaml
         

  5. To verify that Config Sync has applied your changes, view the RootSync object:
         
         kubectl describe rootsync root-sync -n config-management-system
         

  6. To verify that your changes haven't introduced any errors, use the [`nomos status`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install) command:
         
         nomos status
         




### Configure Certificate Authority

For servers configured with certificates from a Certificate Authority (CA) that is not already trusted, Config Sync can be configured to use a CA certificate to verify HTTPS connections to the server. This is supported for Git, Helm, or OCI servers. The CA certificate must include full SSL certificates (Root/Intermediate/Leaf). If your server is already using a trusted CA or you are not connecting over HTTPS, you can skip this step and leave `caCertSecretRef` unset.

### `RootSync`

  1. Fetch the CA certificate which was used to issue the certificate for your Git server and save it to a file.

  2. For `RootSync` objects, the Secret must be created in the `config-management-system` namespace. For example: 
         
         kubectl create secret generic ROOT_CA_CERT_SECRET_NAME   
         
          --namespace=config-management-system   
         
          --from-file=cert=/path/to/CA_CERT_FILE
         

  3. When you configure the `RootSync` object, set the value of the `caCertSecretRef.name` field in the `RootSync` object to ROOT_CA_CERT_SECRET_NAME.




### `RepoSync`

  1. Fetch the CA certificate which was used to issue the certificate for your Git server and save it to a file.

  2. For `RepoSync` objects, the Secret must be created in the same namespace as the RepoSync. For example: 
         
         kubectl create secret generic NAMESPACE_CA_CERT_SECRET_NAME   
         
          --namespace=REPO_SYNC_NAMESPACE   
         
          --from-file=cert=/path/to/CA_CERT_FILE
         

  3. When you [configure the `RepoSync`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#manage-namespace-repos-in-namespace), set the value of the `caCertSecretRef.name` field in the `RepoSync` object to NAMESPACE_CA_CERT_SECRET_NAME.




## Remove the RootSync object

To delete `root-sync`, run the following command:
    
    
    kubectl delete -f FILE_NAME
    

Replace `FILE_NAME` with the name of your RootSync configuration file. For example, `root-sync.yaml`.

Deleting a RootSync or RepoSync object does not clean up Config Sync annotations and labels. To clean up any managed resources, sync from an empty Git directory.

## What's next

  * Learn more about the [RootSync and RepoSync fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields).
  * Discover how to [Monitor RootSync and RepoSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-rootsync-reposync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
