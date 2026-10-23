---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-storage-credentials/
title: Create and use credentials to import images from Cloud Storage for VM Runtime on GDC \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:17.087757+00:00
---

# Create and use credentials to import images from Cloud Storage for VM Runtime on GDC  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-storage-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Create and use credentials to import images from Cloud Storage for VM Runtime on GDC Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create and use credentials to access Cloud Storage using VM Runtime on GDC. A Cloud Storage plugin lets you use [Containerized Data Importer (CDI)](https://kubevirt.io/user-guide/operations/containerized_data_importer/) to import VM images from Cloud Storage buckets. You can then create virtual disks from these images in Cloud Storage and attach them to VMs that run in your cluster. CDI is automatically enabled in a cluster that runs VM Runtime on GDC.

## Before you begin

To complete this document, you need access to the following resources:

  * Access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Google Distributed Cloud on Compute Engine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).
  * A service account and service account key you want to use for Cloud Storage access. If needed, [configure a service account that can access a Cloud Storage bucket](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#bucket-sa).



## Credentials overview

To access Cloud Storage, you use a service account that provides credentials to the storage bucket. The service account requires different privileges to successfully access a storage bucket:

  * **Public storage bucket** : You use a service account for self-identification, but no specific permissions are required.
  * **Private storage bucket** : The storage account requires the _viewer_ or _admin_ privilege to the storage bucket.



There are two ways to provide the service account credentials to CDI:

  * Configure the Google Application Default Credentials (ADC) on the nodes in your cluster. For more information, see [Set up ADC for on-premises or another cloud provider](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises).
  * Provide a Secret that contains the key of the service account to access Cloud Storage. The rest of this document shows you how to create a service account key and Secret.



## Create a Secret

You pass the service account key to Kubernetes using a Secret created in the namespace of the Data Volume. The `data` section of the Secret contains an entry for `creds-gcp.json`. The value is the base64 encoded data of the service account key file. The CLI creates this base64 encoded data for you. If you use a YAML manifest to create the Secret, first create a base64 hash of the contents of your service account key file.

###  CLI 

  * Create the Secret using `kubectl`:
        
        kubectl create secret generic SECRET_NAME \
          --from-file=creds-gcp.json=SERVICE_ACCOUNT_KEY_PATH \
          --namespace NAMESPACE_NAME
        

Replace the following values:

    * `SECRET_NAME`: the name for your Secret.
    * `SERVICE_ACCOUNT_KEY_PATH`: the path to your service account key file.
    * `NAMESPACE_NAME`: the namespace for your Secret. 
      * Create your Secret in the cluster where CDI runs and in the same namespace as the Data Volume. CDI is automatically enabled in a cluster that runs VM Runtime on GDC.



###  Manifest 

  1. Create a `Secret` manifest, such as _my-secret.yaml_ , in the editor of your choice:
         
         nano my-secret.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: v1
         data:
           creds-gcp.json: BASE64_SERVICE_ACCOUNT_FILE
         kind: Secret
         metadata:
           name: SECRET_NAME
           namespace: NAMESPACE_NAME
         type: Opaque
         

Replace the following values:

     * `BASE64_SERVICE_ACCOUNT_FILE`: the base64 hash of the contents of your service account key file.
     * `SECRET_NAME`: the name for your Secret.
     * `NAMESPACE_NAME`: the namespace for your Secret. 
       * Create your Secret in the cluster where CDI runs and in the same namespace as the Data Volume. CDI is automatically enabled in a cluster that runs VM Runtime on GDC.
  3. Save and close the Secret manifest in your editor.

  4. Apply the Secret manifest using `kubectl`:
         
         kubectl apply -f my-secret.yaml
         




## Forward an existing Secret

Instead of creating a Secret, you can create a `SecretForwarder` to forward an existing Secret for use. The `SecretForwarder` supports forwarding Secrets within the same cluster, or across clusters, such as from the admin cluster to a user cluster.

To use the target Secret to access Cloud Storage, the source Secret must have a `creds-gcp.json` key in its `data` section.

###  Same cluster 

The following example `SecretForwarder` manifest forwards a secret in the same cluster:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: SecretForwarder
    metadata:
      name: cdi-gcs
      namespace: default
    spec:
      inClusterTargetSecrets:
        name: gcs-sa
        namespaces:
        - default
      sourceSecret:
        name: gke-connect
        namespace: anthos-creds
    

This example does the following:

  * Creates a `SecretForwarder` named `cdi-gcs` in the `default` namespace.
  * Forwards the secret named `gke-connect` in the `anthos-creds` namespace to a new secret named `gcs-sa` in the `default` namespace.
  * Creates the new secret in the same cluster.



To forward a Secret in the same cluster, complete the following steps:

  1. Create a `SecretForwarder` manifest, such as _my-forwarded-secret.yaml_ , in the editor of your choice:
         
         nano my-forwarded-secret.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: SecretForwarder
         metadata:
           name: SECRET_FORWARDER_NAME
           namespace: NAMESPACE_NAME
         spec:
           inClusterTargetSecrets:
             name: TARGET_SECRET_NAME
             namespaces:
             - TARGET_NAMESPACE_NAME
           sourceSecret:
             name: SOURCE_SECRET_NAME
             namespace: SOURCE_NAMESPACE_NAME
         

Replace the following values:

     * `SECRET_FORWARDER_NAME`: the name for your SecretForwarder.
     * `NAMESPACE_NAME`: the namespace for your SecretForwarder.
     * `TARGET_SECRET_NAME`: the name for your new Secret.
     * `TARGET_NAMESPACE_NAME`: the namespace(s) for your new Secret. 
       * Create your Secret in the cluster where CDI runs and in the same namespace as the Data Volume. CDI is automatically enabled in a cluster that runs VM Runtime on GDC.
     * `SOURCE_SECRET_NAME`: the name of your source Secret to forward.
     * `SOURCE_NAMESPACE_NAME`: the namespace of your source Secret to forward.
  3. Save and close the `SecretForwarder` manifest in your editor.

  4. Apply the `SecretForwarder` manifest using `kubectl`:
         
         kubectl apply -f my-forwarded-secret.yaml
         




###  Across clusters 

The following example `SecretForwarder` manifest forwards a secret across clusters:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: SecretForwarder
    metadata:
      name: cdi-gcs
      namespace: cluster-user1
    spec:
      RemoteClusterTargetSecrets:
        name: gcs-sa
        namespaces:
        - default
      sourceSecret:
        name: gke-connect
        namespace: anthos-creds
    

This example does the following:

  * Creates a `SecretForwarder` named `cdi-gcs` in the `cluster-user1` namespace.
  * Forwards the secret named `gke-connect` in the `anthos-creds` namespace to a new secret named `gcs-sa` in the `default` namespace.
  * Creates the new secret in the cluster named `user1`.



To forward a Secret in the same cluster, complete the following steps:

  1. Create a `SecretForwarder` manifest, such as _my-forwarded-secret.yaml_ , in the editor of your choice:
         
         nano my-forwarded-secret.yaml
         

  2. Copy and paste the following YAML manifest:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: SecretForwarder
         metadata:
           name: SECRET_FORWARDER_NAME
           namespace: NAMESPACE_NAME
         spec:
           RemoteClusterTargetSecrets:
             name: TARGET_SECRET_NAME
             namespaces:
             - TARGET_NAMESPACE_NAME
           sourceSecret:
             name: SOURCE_SECRET_NAME
             namespace: SOURCE_NAMESPACE_NAME
         

Replace the following values:

     * `SECRET_FORWARDER_NAME`: the name for your SecretForwarder in the remote cluster.
     * `NAMESPACE_NAME`: the namespace for your SecretForwarder in the remote cluster.
     * `TARGET_SECRET_NAME`: the name for your new Secret in the remote cluster.
     * `TARGET_NAMESPACE_NAME`: the namespace(s) for your new Secret in the remote cluster. 
       * Create your Secret in the cluster where CDI runs and in the same namespace as the Data Volume. CDI is automatically enabled in a cluster that runs VM Runtime on GDC.
     * `SOURCE_SECRET_NAME`: the name of your source Secret to forward.
     * `SOURCE_NAMESPACE_NAME`: the namespace of your source Secret to forward.
  3. Save and close the `SecretForwarder` manifest in your editor.

  4. Apply the `SecretForwarder` manifest in the admin cluster using `kubectl` with the `KUBECONFIG` of the admin cluster:
         
         kubectl apply -f my-forwarded-secret.yaml
         




## Use a Secret to import an image

To use the Secret to import an image from Cloud Storage when you create a virtual disk and VM, complete the following steps:

  1. Create a manifest that defines a `VirtualMachineDisk` and `VirtualMachine`, such as _my-vm.yaml,_ in the editor of your choice:
         
         nano my-vm.yaml
         

  2. Copy and paste the following YAML definition:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachineDisk
         metadata:
           name: VM_NAME-boot-dv
         spec:
           size: 20Gi
           source:
             gcs:
               url: IMAGE_URL
               secretRef: SECRET_NAME
         ---
         apiVersion: vm.cluster.gke.io/v1
         kind: VirtualMachine
         metadata:
           name: VM_NAME
         spec:
           interfaces:
             - name: eth0
               networkName: pod-network
               default: true
           disks:
             - boot: true
               virtualMachineDiskName: VM_NAME-boot-dv
         

Replace the following values:

     * `VM_NAME` \- the name of your VM.
     * `IMAGE_URL` \- the URL to your disk image Cloud Storage, such as `gs://my-images-bucket/disk.qcow2`.
     * `SECRET_NAME` \- the name of your secret.
  3. Save and close the manifest in your editor.

  4. Create the VM and disk using `kubectl`:
         
         kubectl apply -f my-vm.yaml
         




## What's next

  * [Create and manage virtual disks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/create-manage-disks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
