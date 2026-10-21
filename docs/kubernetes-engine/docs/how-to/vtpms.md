---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vtpms/
title: Access vTPMs and attestation information in Confidential GKE Nodes \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:15.081560+00:00
---

# Access vTPMs and attestation information in Confidential GKE Nodes  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vtpms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Access vTPMs and attestation information in Confidential GKE Nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

The workloads that you run on Confidential Google Kubernetes Engine Nodes can access and use platform integrity and security features such as Virtual Trusted Platform Modules (vTPMs) and Confidential Computing attestation reports. This document shows Security engineers how to make vTPMs and hardware-based devices visible to GKE workloads to perform tasks like remote attestation, secret sealing, and random number generation.

You should already be familiar with the following resources:

  * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
  * [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes)



The specific Confidential Computing technology that you use depends on your organization's threat model and security requirements. For more information, see [Confidential Computing technologies](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies).

## Confidential Computing tasks

You can access vTPMs and hardware modules from Pods that run on Confidential GKE Nodes. You can use these modules to perform cryptographic operations like secret sealing or for remote attestation. The specific modules that are used for these tasks depend on the Confidential Computing technology that the nodes use, as follows:

  * **Secret sealing** : in all Confidential Computing technologies, workloads can use the Shielded VM vTPM as the root of trust for secret sealing.
  * **Remote attestation** : workloads can use one of the following modules for remote attestation:

    * **AMD SEV** : the Shielded VM vTPM.
    * **AMD SEV-SNP** : the hardware-based AMD Secure Processor.
    * **Intel TDX** : the hardware-based Intel TDX module.

For more information about how remote attestation works in each of these Confidential Computing technologies, see [Attester architecture and evidence](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview#attester_architecture_and_evidence).




## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable Confidential GKE Nodes on a cluster or node pool that meets all of the conditions in the Requirements section. For more information, see [Configure Confidential GKE Nodes at the cluster level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#conf-nodes-cluster-level) or [Configure Confidential GKE Nodes at the node pool level](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#enable_on_node_pools).



### Requirements

You can use Confidential GKE Nodes under the following conditions:

  * The cluster and node pools must run one of the following versions, depending on which Confidential Computing module you want to access:

    * **vTPMs** : any GKE version.
    * **AMD SEV-SNP hardware-based devices** : GKE version 1.33.5-gke.1350000 and later or version 1.34.1-gke.2037000 and later.
    * **Intel TDX hardware-based devices** : GKE version 1.33.5-gke.1697000 and later or version 1.34.1-gke.2909000 and later.
  * The node pools must be in a Compute Engine location that has the corresponding machine types. For more information about regional availability, see [Machine types, CPUs, and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).

  * The nodes must use the [Container-Optimized OS node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos).




## Install the device plugin

To make integrity and security information visible to GKE Pods, you install a [device plugin](https://github.com/google/cc-device-plugin). To use a DaemonSet to install the plugin, follow these steps:

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster control plane, such as `us-central1` or `us-central1-a`.
  2. Create the `cc-device-plugin` DaemonSet:
         
         kubectl create -f https://raw.githubusercontent.com/google/cc-device-plugin/main/manifests/cc-device-plugin.yaml
         




After you create the DaemonSet, any Confidential Computing devices on your Confidential GKE Nodes become visible to Pods that run on those nodes.

## Access Confidential Computing devices from Pods

After you create the DaemonSet to install the device plugin, you can access vTPMs and hardware-based devices from Pods similarly to how you request other [extended resources in Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/). The following sections show you how to access vTPMs from any Pod and how to access hardware-based modules in AMD SEV-SNP and Intel TDX nodes.

### Access vTPMs from Pods

To access the Shielded VM vTPM from any Pod that runs on Confidential GKE Nodes, add the `google.com/cc` device to the container resource limits. The following steps request access to a vTPM in an example Pod:

  1. Save the following Pod manifest as `example-vtpm-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
         name: my-vtpm-pod
         spec:
         containers:
         - name: test-vtpm
           image: ubuntu
           command: ["/bin/sh", "-c", "ls -l /dev/tpmrm0; sleep 3600"]
           ports:
           - containerPort: 8080
             name: http
           **resources :
             limits:
               google.com/cc: 1**
         

  2. Create the Pod:
         
         kubectl apply -f example-vtpm-pod.yaml
         

The Pod gets access to the `/dev/tpmrm0` device.

  3. To verify that the Pod can access the vTPM, check the Pod logs:
         
         kubectl logs my-vtpm-pod
         

If the output contains file information, then the Pod can access the device.




You can interact with the device from your application code. For example, you can use the [Go-TPM library](https://github.com/google/go-tpm) to communicate with the vTPM and perform tasks like sealing. If you use AMD SEV, you can also use the vTPM to perform remote attestation of the Confidential VM instance.

### Access hardware-based modules from Pods

If you use AMD SEV-SNP or Intel TDX, then you can also access the corresponding hardware-based modules in Pods by specifying the corresponding selector in the container resource limits. You must use these modules to perform remote attestation of nodes that use AMD SEV-SNP and Intel TDX, because the vTPM isn't the root of trust for measurements in these technologies.

The following steps show you how to request access to the AMD Secure Processor or the Intel TDX module:

  1. Save one of the following example Pods:

     * **Request AMD SEV-SNP devices** :
           
           apiVersion: v1
           kind: Pod
           metadata:
             name: snp-test-pod
           spec:
             containers:
             - name: test-container
               image: alpine
               command: ["/bin/sh", "-c"]
               args:
                 - |
                   echo "Checking for SEV-SNP device..."
                   ls -l /dev/sev-guest
                   echo "SNP container started successfully"
                   sleep 3600
           ** resources:**
           ** limits:**
           ** amd.com/sev-snp: "1"**
                 requests:
                   amd.com/sev-snp: "1"
             nodeSelector:
               cloud.google.com/gke-confidential-nodes-instance-type: SEV_SNP

     * **Request Intel TDX devices** :
           
           apiVersion: v1
           kind: Pod
           metadata:
             name: tdx-test-pod
           spec:
             containers:
             - name: test-container
               image: alpine
               command: ["/bin/sh", "-c"]
               args:
                 - |
                   echo "Checking for TDX device..."
                   ls -l /dev/tdx*
                   echo "TDX container started successfully"
                   sleep 3600
           ** resources:**
           ** limits:**
           ** intel.com/tdx: "1"**
                 requests:
                   intel.com/tdx: "1"
             nodeSelector:
               cloud.google.com/gke-confidential-nodes-instance-type: TDX

  2. Create the Pod:
         
         kubectl create -f PATH_TO_POD_MANIFEST
         

Replace `PATH_TO_POD_MANIFEST` with the path to the Pod manifest file that you saved.

The Pods get access to one of the following devices:

     * `/dev/sev-guest` for AMD SEV-SNP.
     * `/dev/tdx_guest` for Intel TDX.
  3. To verify that the Pod can access the device, check the Pod logs:
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of the example Pod that you deployed in the previous step.

If the output contains file information, then the Pod can access the device.




## What's next

  * Learn how to [remotely attest that workloads are running on Confidential VM](https://codelabs.developers.google.com/codelabs/vtpm-remote-attestation-and-sealing-on-confidential-gke-nodes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
