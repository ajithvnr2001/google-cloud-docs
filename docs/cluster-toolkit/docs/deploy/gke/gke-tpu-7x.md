---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x/
title: Deploy a GKE TPU 7x cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:58.517557+00:00
---

# Deploy a GKE TPU 7x cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Deploy a GKE TPU 7x cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use a [Cluster Toolkit blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint) to automate the deployment of a Google Kubernetes Engine (GKE) cluster that has a dedicated Cloud TPU 7x node pool. You can choose between the _standard_ blueprint and the _advanced_ blueprint. These blueprints let you rapidly provision repeatable, scalable infrastructure optimized to train and serve large-scale AI models.

Both blueprints provision the same underlying GKE cluster infrastructure. You can deploy the standard blueprint immediately by using default settings, or you can configure and deploy the advanced blueprint, which adds automatic bucket creation, performance-tuned storage mounts, and support for optional high-performance storage systems. For a detailed description of these differences, see [Comparison of blueprint options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview#comparison-blueprint-options).

For more information about the architecture of this TPU, see the [TPU 7x](https://docs.cloud.google.com/tpu/docs/tpu7x).

For more information about TPUs in GKE, see [How TPUs in GKE work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#how_tpus_work).

## Before you begin

Before you begin, verify that you have completed the following tasks:

  * Verify that you have a TPU-compatible version of GKE. For more information, see [Validate TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability).
  * [Enable the Kubernetes Engine API](https://console.cloud.google.com/flows/enableapi?apiid=container.googleapis.com).
  * [Install and initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * [Verify that you have sufficient quota for Cloud TPU 7x](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota) in your target region.



### Required roles

To get the permissions that you need to deploy the GKE Cloud TPU 7x cluster, ask your administrator to grant you the following IAM roles: 

  * [Editor ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`) on your project
  * [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) on your project
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) on your project
  * For Google Cloud Managed Lustre configurations, you need the following roles: 
    * [Lustre Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/lustre#lustre.admin) (`roles/lustre.admin`) on your project
    * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on your project
  * For Hyperdisk Balanced configurations, you need the following roles: [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on your project 
  * For Filestore configurations, you need the following roles: [Cloud Filestore Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/file#file.editor) (`roles/file.editor`) on your project 
  * To consume a single-project reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project 
  * To consume a shared reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up the cluster infrastructure

To set up the cluster infrastructure that's required for both blueprint deployments, do the following:

  1. Create a Cloud Storage bucket to store the state of the Terraform deployment:
         
         gcloud storage buckets create gs://BUCKET_NAME \
           --default-storage-class=STANDARD \
           --location=COMPUTE_REGION \
           --uniform-bucket-level-access
         

Replace the following:

     * `BUCKET_NAME`: the name of the new Cloud Storage bucket.
     * `COMPUTE_REGION`: the compute region where you want to store the Terraform state.
  2. Enable versioning on the bucket:
         
         gcloud storage buckets update gs://BUCKET_NAME --versioning
         

  3. Open the [`examples/gke-tpu-7x/gke-tpu-7x-deployment.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-deployment.yaml) file.

  4. Choose a consumption option for your GKE deployment:

By default, the deployment file is configured to consume [standard or future reservations](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options?tab=cloud-tpu#tpu-reservations). To use an alternative consumption model, update your deployment YAML file. For more information, see [GKE consumption options](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-consumption-options).

  5. In the `terraform_backend_defaults` and `vars` sections, replace the placeholders to match your chosen deployment:
         
         terraform_backend_defaults:
          type: gcs
          configuration:
            bucket: BUCKET_NAME
         
         vars:
          project_id: PROJECT_ID
          deployment_name: DEPLOYMENT_NAME
          region: REGION
          zone: ZONE
          num_slices: NUM_SLICES
          machine_type: MACHINE_TYPE
          tpu_topology: TPU_TOPOLOGY
          authorized_cidr: AUTHORIZED_CIDR
         
         

Replace the following:

     * `BUCKET_NAME`: the Cloud Storage bucket used for storing Terraform state.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the Google Cloud region used for this deployment—for example, `us-east5`.
     * `ZONE`: the Google Cloud zone used for this deployment—for example, `us-east5-c`.
     * `DEPLOYMENT_NAME`: the name of your deployment.
     * `NUM_SLICES`: the number of independent Cloud TPU slices to create.
     * `MACHINE_TYPE`: the machine type for your Cloud TPU nodes.
     * `TPU_TOPOLOGY`: the physical arrangement of the Cloud TPU chips in a slice.
     * `AUTHORIZED_CIDR`: the CIDR block containing the IP address of the machine calling Terraform. To allow all IP addresses, use `0.0.0.0/0`. Identity and Access Management (IAM) restrictions are still enforced. To allow only your IP address, use your IP address followed by `/32`. 

Cluster Toolkit automatically calculates the exact number of nodes required based on your selected `tpu_topology` and `machine_type`.

  6. Generate Application Default Credentials (ADC) to provide access to Terraform:
         
         gcloud auth application-default login
         




## Deploy the standard blueprint

If you want to use the more advanced [`examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml) blueprint, skip this section and go to Deploy the advanced blueprint.

After you have set up the cluster infrastructure, deploy the standard blueprint to provision the GKE infrastructure:
    
    
    cd ~/cluster-toolkit
    ./gcluster deploy -d \
      examples/gke-tpu-7x/gke-tpu-7x-deployment.yaml \
      examples/gke-tpu-7x/gke-tpu-7x.yaml
    

## Deploy the advanced blueprint

The following GitHub repository also includes an advanced blueprint which is optimized for production workloads: [`examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml). To get a better understanding of the advanced blueprint functionality, see [Advanced blueprints](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview#advanced-blueprints).

To deploy the advanced blueprint, do the following:

  1. Set up the cluster infrastructure.
  2. Configure advanced scheduling with Kueue.
  3. Optional: Configure Managed Lustre.
  4. Optional: Configure Hyperdisk Balanced.
  5. Optional: Configure Filestore.
  6. Deploy the advanced GKE Cloud TPU 7x cluster.



### Configure advanced scheduling with Kueue

The advanced blueprint supports [Kueue](https://kueue.sigs.k8s.io/), a Kubernetes-native system for managing quotas and Job queuing. The advanced blueprint enables Kueue by default.

  1. Submit a Job to the queue by adding the `kueue.x-k8s.io/queue-name: user-queue` label to your Job or JobSet manifest.
  2. Create the resources by using the provided sample Job file:
         
         kubectl create -f ~/cluster-toolkit/examples/gke-tpu-7x/kueue-job-sample.yaml
         

  3. Check the status of your workload:
         
         kubectl get workloads
         




### Configure Managed Lustre

[Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) provides a fully managed parallel file system optimized for AI and HPC applications. To configure Managed Lustre for your GKE Cloud TPU 7x deployment, do the following:

  1. Open the [`examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml) file.
  2. In the `vars` section, uncomment the Managed Lustre variables.
  3. Find the section commented `# --- MANAGED LUSTRE ADDITIONS ---` and uncomment the `private_service_access`, `lustre_firewall_rule`, `managed-lustre`, and `lustre-pv` modules.
  4. Deploy the cluster by using the standard [`gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy).



### Configure Hyperdisk Balanced

[Hyperdisk Balanced](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) provides highly available and consistent performance across GKE nodes. To configure Hyperdisk Balanced for your GKE Cloud TPU 7x deployment, do the following:

  1. Open the [`examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml) file.
  2. In the `gke-tpu-7x-cluster` module, verify that the value `enable_persistent_disk_csi: true` is set.
  3. Find the section commented `# --- HYPERDISK BALANCED ADDITIONS ---` and uncomment the `hyperdisk-balanced-setup` and `fio-bench-job-hyperdisk` modules.
  4. Deploy the cluster by using the standard `gcluster deploy` command.



### Configure Filestore

[Filestore](https://docs.cloud.google.com/filestore/docs/overview) provides managed NFS capabilities that let multiple Cloud TPU hosts share logs, code, or datasets. To configure Filestore for your GKE Cloud TPU 7x deployment, do the following:

  1. Open the [`examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml) file.
  2. In the `gke-tpu-7x-cluster` module, ensure that `enable_filestore_csi: true` is set.
  3. Find the section commented `# --- FILESTORE ADDITIONS ---` and uncomment the `filestore`, `shared-filestore-pv`, and `shared-fs-job` modules.
  4. Deploy the cluster by using the standard `gcluster deploy` command.



### Deploy the advanced GKE Cloud TPU 7x cluster

After you have set up the cluster infrastructure and configured your chosen storage option, deploy the blueprint to provision the GKE infrastructure:
    
    
    cd ~/cluster-toolkit
    ./gcluster deploy -d \
      examples/gke-tpu-7x/gke-tpu-7x-deployment.yaml \
      examples/gke-tpu-7x/gke-tpu-7x-advanced.yaml
    

After deployment, the blueprint prints instructions for running a FIO benchmark Job. This Job acts as a validation test to verify that your Cloud Storage FUSE mounts are working correctly for both reading and writing. Follow the printed instructions in the terminal to run the validation test.

## Run the sample Job

The [`examples/gke-tpu-7x/gke-tpu-7x-job.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-job.yaml) file creates a Service and a Job resource in Kubernetes. The workload returns the number of Cloud TPU chips across all of the nodes in a multi-host Cloud TPU slice.

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials DEPLOYMENT_NAME \
           --region=REGION \
           --project=PROJECT_ID
         

Replace the following:

     * `DEPLOYMENT_NAME`: the name of your deployment.
     * `REGION`: the Google Cloud region used for this deployment.
     * `PROJECT_ID`: your Google Cloud project ID.
  2. Open the [`examples/gke-tpu-7x/gke-tpu-7x-job.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-tpu-7x/gke-tpu-7x-job.yaml) file and update the `nodeSelector` values in the template specification to match the accelerator and topology that you used in your blueprint.

For example, the `nodeSelector` section might look like the following example:
         
         nodeSelector:
             cloud.google.com/gke-tpu-accelerator: tpu7x
             cloud.google.com/gke-tpu-topology: 2x2x1
         

  3. In the `resources` section of the container specification, update the values for the `google.com/tpu` field in both the `requests` and `limits` sections. Supply values that match the number of chips per node for your selected machine type:
         
         resources:
           requests:
             google.com/tpu: CHIPS_PER_NODE
           limits:
             google.com/tpu: CHIPS_PER_NODE
         

Replace `CHIPS_PER_NODE` with the number of Cloud TPU chips per node in your machine type, such as `4`.

  4. Create the resources:
         
         kubectl create -f ~/cluster-toolkit/examples/gke-tpu-7x/gke-tpu-7x-job.yaml
         

  5. Get a list of Pods, and identify two Pods with the prefix `multislice-job-slice`:
         
         kubectl get pods
         

  6. Get the logs of either of the Pods:
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of one of the Pods that you identified in the previous step.

The logs display `Global device count: 32` at the end, which is the number of Cloud TPU chips across all of the nodes in a multi-host Cloud TPU slice.




## Verify storage integrations

If you configured any of the optional storage systems, verify that your storage integrations work correctly. To do so, perform the following steps:

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials DEPLOYMENT_NAME \
           --region=REGION \
           --project=PROJECT_ID
         

Replace the following:

     * `DEPLOYMENT_NAME`: the name of your deployment.
     * `REGION`: the Google Cloud region used for this deployment.
     * `PROJECT_ID`: your Google Cloud project ID.
  2. Follow the relevant section for your storage option:

     * Test the Managed Lustre mount
     * Test the Hyperdisk Balanced mount
     * Test the shared Filestore mount



### Test the Managed Lustre mount

To test the Managed Lustre mount, do the following:

  1. Create a file named `lustre-claim-pod.yaml` with the following settings:

     * The `storageClassName` field must be empty to bind to the manually created `PersistentVolumeClaim` resource.
     * The `storage` field size must match the `lustre_size_gib` value from your blueprint.
    
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-lustre-claim
    spec:
      accessModes:
      - ReadWriteMany
      storageClassName: ""
      resources:
        requests:
          storage: 36000Gi
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      name: lustre-test-pod
    spec:
      containers:
      - name: test-container
        image: ubuntu:22.04
        command: ["/bin/sleep", "infinity"]
        volumeMounts:
        - name: lustre-storage
          mountPath: /mnt/lustre
      volumes:
      - name: lustre-storage
        persistentVolumeClaim:
          claimName: my-lustre-claim
    

  2. Apply the manifest to your cluster:
         
         kubectl apply -f lustre-claim-pod.yaml
         

The Pod starts, and the Managed Lustre file system is available inside the container at `/mnt/lustre`.




### Test the Hyperdisk Balanced mount

To test the Hyperdisk Balanced mount, do the following:

  1. Apply the generated Flexible I/O tester (FIO) Job manifest:
         
         kubectl apply -f PATH_TO_FIO_BENCHMARK
         

Replace `PATH_TO_FIO_BENCHMARK` with the path to the generated `fio-benchmark.yaml` file. The path is displayed in the final instructions printed to the terminal after you deploy the blueprint.

The Job created in the cluster is named `fio-benchmark`.

  2. Wait for the Job to complete, and then obtain the list of Pods:
         
         kubectl get jobs
         kubectl get pods
         

  3. View the logs of the completed Pod to check the benchmark results:
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of the completed benchmark Pod. You can find the Pod name in the output of the `kubectl get pods` command in the previous step.

The logs of the Pod verify that the disk is mounted successfully and show the results of a mixed input and output test that is used to validate the disk's provisioned performance.




### Test the shared Filestore mount

The blueprint includes a sample Job named `shared-fs-job` that demonstrates how two different Pods can write to and read from the same file simultaneously.

To test the shared Filestore mount, do the following:

  1. Apply the Filestore test manifest:
         
         kubectl apply -f PATH_TO_SHARED_FS_JOB
         

Replace `PATH_TO_SHARED_FS_JOB` with the path to the generated `shared-fs-job.yaml` file. The path is displayed in the final instructions printed to the terminal after you deploy the blueprint.

  2. Check the logs of the first Pod to verify that the first Pod is reading data written by the second Pod:
         
         kubectl get pods
         kubectl logs FIRST_POD_NAME
         

Replace `FIRST_POD_NAME` with the name of the first Pod in the output of the `kubectl get pods` command.

The logs display content from the `shared_output.txt` file, showing timestamps and hostnames from both Pods, confirming that the file system is shared.




## Delete resources

To avoid recurring charges for the resources used on this page, use the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy) to delete the resources provisioned by Cluster Toolkit, including the Virtual Private Cloud (VPC) networks and GKE cluster:
    
    
    ./gcluster destroy DEPLOYMENT_NAME/
    

Replace `DEPLOYMENT_NAME` with the name of your deployment. You can find this name in the Set up the cluster infrastructure section, where you defined the `deployment_name` variable in the `examples/gke-tpu-7x/gke-tpu-7x-deployment.yaml` file.

## What's next

  * [Learn about Cloud TPU deployments in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview)
  * [Deploy a GKE Cloud TPU v6e cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
