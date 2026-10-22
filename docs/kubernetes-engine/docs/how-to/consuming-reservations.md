---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations/
title: Consuming reserved zonal resources \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:44.456105+00:00
---

# Consuming reserved zonal resources  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Consuming reserved zonal resources Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to consume reserved Compute Engine zonal resources in specific GKE workloads. These _capacity reservations_ give you a high level of assurance that specific hardware is available for your workloads.

Ensure that you're already familiar with the concepts of Compute Engine reservations, like consumption types, share types, and provisioning types. For details, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

This page is intended for the following people:

  * [Application operators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-app-sre) who deploy workloads that should run as soon as possible, usually with specialized hardware like GPUs.
  * [Platform administrators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-platform-admin) who want to obtain a high level of assurance that workloads run on optimized hardware that meets both application and organizational requirements.



## About reservation consumption in GKE

Compute Engine capacity reservations let you provision specific hardware configurations in Google Cloud zones, either immediately or at a specified future time. You can then consume this reserved capacity in GKE.

Depending on your GKE mode of operation, you can consume the following reservation types:

  * Autopilot mode: specific reservations, or any matching reservation using custom ComputeClasses.
  * Standard mode: specific reservations or any matching reservation.



For `any` matching reservation, you can choose between two behaviors:

  * **Any matching reservation with fallback:** attempts to consume any matching reservation. If none are available, it falls back to provisioning standard on-demand capacity.
  * **Any matching reservation without fallback:** attempts to consume any matching reservation. If none are available, the provisioning fails without falling back to on-demand capacity.



To enable consuming reservations to create your resources, you must specify a _reservation affinity_ , like `any`, `any-reservation-then-fail`, or `specific`.

### Reservation consumption options in GKE

GKE lets you consume reservations directly in individual workloads by using Kubernetes nodeSelectors in your workload manifest or by creating Standard mode node pools that consume the reservation. This page describes the approach of directly selecting reservations in individual resources.

You can also configure GKE to consume reservations during scaling operations that create new nodes by using _custom compute classes_. Custom compute classes let platform administrators define a hierarchy of node configurations for GKE to prioritize during node scaling so that workloads run on your selected hardware.

You can specify reservations in your custom compute class configuration so that any GKE workload that uses that custom ComputeClass indicates to GKE to consume the specified reservations for that ComputeClass.

To learn more, in the "About custom compute classes" page, see [Consume Compute Engine reservations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#reservations).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.

* [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster). 

## Consume capacity reservations in Autopilot clusters

Autopilot clusters support consuming resources from Compute Engine capacity reservations in the same project or in a shared project. You can set the consumption type property of the target reservation to _specific_ , and explicitly select that reservation in your manifest. Alternatively, you can consume _any_ matching reservation using custom ComputeClasses with the `AnyBestEffort` reservation affinity. If you don't explicitly specify a reservation or configure a custom ComputeClasses to consume one, Autopilot clusters won't consume reservations. To learn more about reservation consumption types, see [How reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-reservations-work).

These reservations qualify for Compute flexible [committed use discounts](https://docs.cloud.google.com/kubernetes-engine/cud). You must use the `Performance` ComputeClass or Pods that request accelerators to consume capacity reservations.

To consume any available reservation without falling back to on-demand capacity, your cluster must run GKE version 1.36.0-gke.3204000 or later.

### Create capacity reservations for Autopilot

Autopilot Pods can consume reservations that have the _specific_ consumption type property in the same project as the cluster or in a shared reservation from a different project. You can consume the reserved hardware by explicitly referencing that reservation in your manifest, or you can consume _any_ matching reservation using custom ComputeClasses. You can consume reservations in Autopilot for the following types of hardware:

  * Any of the following types of GPUs: 

    * `nvidia-gb200`: NVIDIA GB200 (Preview)
    * `nvidia-b200`: NVIDIA B200 (180GB)
    * `nvidia-h200-141gb`: NVIDIA H200 (141GB)
    * `nvidia-h100-mega-80gb`: NVIDIA H100 Mega (80GB)
    * `nvidia-h100-80gb`: NVIDIA H100 (80GB)
    * `nvidia-a100-80gb`: NVIDIA A100 (80GB)
    * `nvidia-tesla-a100`: NVIDIA A100 (40GB)
    * `nvidia-rtx-pro-6000`: NVIDIA RTX PRO 6000
    * `nvidia-l4`: NVIDIA L4
    * `nvidia-tesla-t4`: NVIDIA T4
  * Any of the following types of TPUs: 

    * `tpu7x`: Ironwood (TPU7x)
    * `tpu-v6e-slice`: TPU v6e slice
    * `tpu-v5p-slice`: TPU v5p slice
    * `tpu-v5-lite-podslice`: TPU v5 lite podslice
    * `tpu-v4-lite-device`: TPU v4 lite device
    * `tpu-v4-podslice`: TPU v4 podslice
    * `tpu-v3-device`: TPU v3 device
    * `tpu-v3-slice`: TPU v3 podslice



To create a capacity reservation, see the following resources. The reservation must meet the following requirements:

  * The machine types, accelerator types, and accelerator quantities match what your workloads will consume.
  * The reservation uses the _specific_ consumption type, unless you are using a custom ComputeClass to consume _any_ matching reservation. For example, in the gcloud CLI, you must specify the `--require-specific-reservation` flag when you create a specific reservation.

  * [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project)

  * [Create a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared)




GKE automatically attaches any Local SSDs from the selected specific reservation to your node. You don't need to select individual Local SSDs in your workload manifest. For example, if the reservation that you select includes two Local SSDs, the nodes that GKE creates from that reservation have two Local SSDs attached.

### Consume any matching reservation with fallback in Autopilot

This section shows you how to configure your Autopilot workloads to consume any matching reservation with a fallback to on-demand capacity. You do this by creating a custom ComputeClass that specifies the `AnyBestEffort` reservation affinity.

**Note:** Because Autopilot clusters are regional and span multiple zones, using `AnyBestEffort` reservation affinity does not provide a high level of assurance that GKE will consume your zonal reservation if on-demand capacity is available elsewhere in the region. For a high level of assurance that your reserved capacity is consumed, use a specific reservation instead.

  1. Save the following custom ComputeClass manifest as `any-reservation-cc.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: any-reservation
         spec:
           priorities:
           - reservations:
               affinity: AnyBestEffort
         

  2. Create the custom ComputeClass:
         
         kubectl apply -f any-reservation-cc.yaml
         

  3. Save the following Pod manifest as `any-reservation-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: any-reservation-pod
         spec:
           nodeSelector:
             cloud.google.com/compute-class: any-reservation
           containers:
           - name: my-container
             image: "k8s.gcr.io/pause"
             resources:
               requests:
                 cpu: 2
                 memory: "4Gi"
         

  4. Deploy the Pod:
         
         kubectl apply -f any-reservation-pod.yaml
         




### Consume any matching reservation without fallback in Autopilot

This section shows you how to configure your Autopilot workloads to consume any matching reservation without falling back to on-demand capacity if the reservation is exhausted. You do this by creating a custom ComputeClass that specifies the `AnyThenFail` reservation affinity and sets the value of the `whenUnsatisfiable` field to `DoNotScaleUp`. This reservation affinity requires GKE version 1.36.0-gke.3204000 or later.

  1. Save the following custom ComputeClass manifest as `any-then-fail-cc.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: any-then-fail
         spec:
           priorities:
           - reservations:
               affinity: AnyThenFail
             whenUnsatisfiable: DoNotScaleUp
         

  2. Create the custom ComputeClass:
         
         kubectl apply -f any-then-fail-cc.yaml
         

  3. Save the following Pod manifest as `any-then-fail-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: any-then-fail-pod
         spec:
           nodeSelector:
             cloud.google.com/compute-class: any-then-fail
           containers:
           - name: my-container
             image: "k8s.gcr.io/pause"
             resources:
               requests:
                 cpu: 2
                 memory: "4Gi"
         

  4. Deploy the Pod:
         
         kubectl apply -f any-then-fail-pod.yaml
         




### Consume a specific reservation in the same project in Autopilot

This section shows you how to consume a specific capacity reservation that's in the same project as your cluster. You can use kubectl or Terraform.

###  kubectl 

  1. Save the following manifest as `specific-autopilot.yaml`. This manifest has node selectors that consume a specific reservation. You can use VM instances or accelerators.

**VM instances**
         
         apiVersion: v1
           kind: Pod
           metadata:
             name: specific-same-project-pod
           spec:
             **nodeSelector :
               cloud.google.com/compute-class: Performance
               cloud.google.com/machine-family: MACHINE_SERIES
               cloud.google.com/reservation-name: RESERVATION_NAME
               cloud.google.com/reservation-affinity: "specific"**
             containers:
             - name: my-container
               image: "k8s.gcr.io/pause"
               resources:
                 requests:
                   cpu: 2
                   memory: "4Gi"
         

Replace the following:

     * `MACHINE_SERIES`: a machine series that contains the machine type of the VMs in your specific capacity reservation. For example, if your reservation is for `c3-standard-4` machine types, specify `c3` in the `MACHINE_SERIES` field.
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.

**GPU Accelerators**
    
    apiVersion: v1
      kind: Pod
      metadata:
        name: specific-same-project-pod
      spec:
        **nodeSelector :
          cloud.google.com/gke-accelerator: ACCELERATOR
          cloud.google.com/reservation-name: RESERVATION_NAME
          cloud.google.com/reservation-affinity: "specific"**
        containers:
        - name: my-container
          image: "k8s.gcr.io/pause"
          resources:
            requests:
              cpu: 12
              memory: "50Gi"
              ephemeral-storage: "200Gi"
            limits:
              nvidia.com/gpu: QUANTITY
    

Replace the following:

     * `ACCELERATOR`: the accelerator that you reserved in the Compute Engine capacity reservation. Must be one of the following values: 
       * `nvidia-gb200`: NVIDIA GB200 (Preview)
       * `nvidia-b200`: NVIDIA B200 (180GB)
       * `nvidia-h200-141gb`: NVIDIA H200 (141GB)
       * `nvidia-h100-mega-80gb`: NVIDIA H100 Mega (80GB)
       * `nvidia-h100-80gb`: NVIDIA H100 (80GB)
       * `nvidia-a100-80gb`: NVIDIA A100 (80GB)
       * `nvidia-tesla-a100`: NVIDIA A100 (40GB)
       * `nvidia-rtx-pro-6000`: NVIDIA RTX PRO 6000
       * `nvidia-l4`: NVIDIA L4
       * `nvidia-tesla-t4`: NVIDIA T4
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `QUANTITY`: the number of GPUs to attach to the container. Must be a supported quantity for the specified GPU, as described in [Supported GPU quantities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#supported-quantities).

**TPU Accelerators**
    
    apiVersion: v1
      kind: Pod
      metadata:
        name: specific-same-project-pod
      spec:
        **nodeSelector :
          cloud.google.com/gke-tpu-accelerator: ACCELERATOR
          cloud.google.com/gke-tpu-topology: TOPOLOGY
          cloud.google.com/reservation-name: RESERVATION_NAME
          cloud.google.com/reservation-affinity: "specific"**
        containers:
        - name: my-container
          image: "k8s.gcr.io/pause"
          resources:
            requests:
              cpu: 12
              memory: "50Gi"
              ephemeral-storage: "200Gi"
            limits:
              google.com/tpu: QUANTITY
    

Replace the following:

     * `ACCELERATOR`: the accelerator that you reserved in the Compute Engine capacity reservation. Must be one of the following values: 
       * `tpu7x`: Ironwood (TPU7x)
       * `tpu-v6e-slice`: TPU v6e slice
       * `tpu-v5p-slice`: TPU v5p slice
       * `tpu-v5-lite-podslice`: TPU v5 lite podslice
       * `tpu-v4-lite-device`: TPU v4 lite device
       * `tpu-v4-podslice`: TPU v4 podslice
       * `tpu-v3-device`: TPU v3 device
       * `tpu-v3-slice`: TPU v3 podslice
     * `TOPOLOGY`: the TPU topology.
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `QUANTITY`: the number of TPUs to attach to the container. Must be aligned with the [TPU topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).
  2. Deploy the Pod:
         
         kubectl apply -f specific-autopilot.yaml
         




Autopilot uses the reserved capacity in the specified reservation to provision a new node to place the Pod.

###  Terraform 

To consume a specific reservation in the same project with VM instances using Terraform, refer to the following example:
    
    
    resource "kubernetes_pod_v1" "default_pod" {
      metadata {
        name = "specific-same-project-pod"
      }
    
      spec {
        node_selector = {
          "cloud.google.com/compute-class"        = "Performance"
          "cloud.google.com/machine-family"       = "c3"
          "cloud.google.com/reservation-name"     = google_compute_reservation.specific_pod.name
          "cloud.google.com/reservation-affinity" = "specific"
        }
    
        container {
          name  = "my-container"
          image = "registry.k8s.io/pause"
    
          resources {
            requests = {
              cpu               = 2
              memory            = "8Gi"
              ephemeral-storage = "1Gi"
            }
          }
    
          security_context {
            allow_privilege_escalation = false
            run_as_non_root            = false
    
            capabilities {
              add  = []
              drop = ["NET_RAW"]
            }
          }
        }
    
        security_context {
          run_as_non_root     = false
          supplemental_groups = []
    
          seccomp_profile {
            type = "RuntimeDefault"
          }
        }
      }
    
      depends_on = [
        google_compute_reservation.specific_pod
      ]
    }

To consume a specific reservation in the same project using Terraform, refer to the following example:
    
    
    resource "kubernetes_pod_v1" "default_accelerator" {
      metadata {
        name = "specific-same-project-accelerator"
      }
    
      spec {
        node_selector = {
          "cloud.google.com/compute-class"        = "Accelerator"
          "cloud.google.com/gke-accelerator"      = "nvidia-l4"
          "cloud.google.com/reservation-name"     = google_compute_reservation.specific_accelerator.name
          "cloud.google.com/reservation-affinity" = "specific"
        }
    
        container {
          name  = "my-container"
          image = "registry.k8s.io/pause"
    
          resources {
            requests = {
              cpu               = 2
              memory            = "7Gi"
              ephemeral-storage = "1Gi"
              "nvidia.com/gpu"  = 1
    
            }
            limits = {
              "nvidia.com/gpu" = 1
            }
          }
    
          security_context {
            allow_privilege_escalation = false
            run_as_non_root            = false
    
            capabilities {
              add  = []
              drop = ["NET_RAW"]
            }
          }
        }
    
        security_context {
          run_as_non_root     = false
          supplemental_groups = []
    
          seccomp_profile {
            type = "RuntimeDefault"
          }
        }
      }
    
      depends_on = [
        google_compute_reservation.specific_accelerator
      ]
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Consume a specific shared reservation in Autopilot

This section uses the following terms:

  * Owner project: the project that owns the reservation and shares it with other projects.
  * Consumer project: the project that runs the workloads that consume the shared reservation.



To consume a specific shared reservation, configure Identity and Access Management (IAM) permissions to allow the GKE service agent from the consumer project to access the reservation in the owner project.

Complete the following steps in the project that owns the shared reservation:

  1. Create a custom IAM role that contains the `compute.reservations.list` permission in the owner project:
         
         gcloud iam roles create ROLE_NAME \
             --project=OWNER_PROJECT_ID \
             --permissions='compute.reservations.list'
         

Replace the following:

     * `ROLE_NAME`: a name for your new role.
     * `OWNER_PROJECT_ID`: the project ID of the project that owns the capacity reservation.
  2. Give the GKE service agent in the consumer project access to list shared reservations in the owner project:
         
         gcloud projects add-iam-policy-binding OWNER_PROJECT_ID \
             --project=OWNER_PROJECT_ID \
             --member=serviceAccount:service-CONSUMER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
             --role='projects/OWNER_PROJECT_ID/roles/ROLE_NAME'
         

Replace `CONSUMER_PROJECT_NUMBER` with the numerical project number of your consumer project. To find this number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in the Resource Manager documentation.

  3. Save the following manifest as `shared-autopilot.yaml`. This manifest has nodeSelectors that tell GKE to consume a specific shared reservation.

### VM instances
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: performance-pod
         spec:
           **nodeSelector :
             cloud.google.com/compute-class: Performance
             cloud.google.com/machine-family: MACHINE_SERIES
             cloud.google.com/reservation-name: RESERVATION_NAME
             cloud.google.com/reservation-project: OWNER_PROJECT_ID
             cloud.google.com/reservation-affinity: "specific"**
           containers:
           - name: my-container
             image: "k8s.gcr.io/pause"
             resources:
               requests:
                 cpu: 2
                 memory: "4Gi"
         

Replace the following:

     * `MACHINE_SERIES`: a machine series that contains the machine type of the VMs in your specific capacity reservation. For example, if your reservation is for `c3-standard-4` machine types, specify `c3` in the `MACHINE_SERIES` field.
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `OWNER_PROJECT_ID`: the project ID of the project that owns the capacity reservation.

### GPU Accelerators
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: specific-same-project-pod
    spec:
      **nodeSelector :
        cloud.google.com/gke-accelerator: ACCELERATOR
        cloud.google.com/reservation-name: RESERVATION_NAME
        cloud.google.com/reservation-project: OWNER_PROJECT_ID
        cloud.google.com/reservation-affinity: "specific"**
      containers:
      - name: my-container
        image: "k8s.gcr.io/pause"
        resources:
          requests:
            cpu: 12
            memory: "50Gi"
            ephemeral-storage: "200Gi"
          limits:
            nvidia.com/gpu: QUANTITY
    

Replace the following:

     * `ACCELERATOR`: the accelerator that you reserved in the Compute Engine capacity reservation. Must be one of the following values: 
       * `nvidia-gb200`: NVIDIA GB200 (Preview)
       * `nvidia-b200`: NVIDIA B200 (180GB)
       * `nvidia-h200-141gb`: NVIDIA H200 (141GB)
       * `nvidia-h100-mega-80gb`: NVIDIA H100 Mega (80GB)
       * `nvidia-h100-80gb`: NVIDIA H100 (80GB)
       * `nvidia-a100-80gb`: NVIDIA A100 (80GB)
       * `nvidia-tesla-a100`: NVIDIA A100 (40GB)
       * `nvidia-rtx-pro-6000`: NVIDIA RTX PRO 6000
       * `nvidia-l4`: NVIDIA L4
       * `nvidia-tesla-t4`: NVIDIA T4
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `OWNER_PROJECT_ID`: the project ID of the project that owns the capacity reservation.
     * `QUANTITY`: the number of GPUs to attach to the container. Must be a supported quantity for the specified GPU, as described in [Supported GPU quantities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#supported-quantities).

### TPU Accelerators
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: specific-shared-project-pod
    spec:
      **nodeSelector :
        cloud.google.com/gke-tpu-accelerator: ACCELERATOR
        cloud.google.com/gke-tpu-topology: TOPOLOGY
        cloud.google.com/reservation-name: RESERVATION_NAME
        cloud.google.com/reservation-project: OWNER_PROJECT_ID
        cloud.google.com/reservation-affinity: "specific"**
      containers:
      - name: my-container
        image: "k8s.gcr.io/pause"
        resources:
          requests:
            cpu: 12
            memory: "50Gi"
            ephemeral-storage: "200Gi"
          limits:
            google.com/tpu: QUANTITY
    

Replace the following:

     * `ACCELERATOR`: the accelerator that you reserved in the Compute Engine capacity reservation. Must be one of the following values: 
       * `tpu7x`: Ironwood (TPU7x)
       * `tpu-v6e-slice`: TPU v6e slice
       * `tpu-v5p-slice`: TPU v5p slice
       * `tpu-v5-lite-podslice`: TPU v5 lite podslice
       * `tpu-v4-lite-device`: TPU v4 lite device
       * `tpu-v4-podslice`: TPU v4 podslice
       * `tpu-v3-device`: TPU v3 device
       * `tpu-v3-slice`: TPU v3 podslice
     * `TOPOLOGY`: the TPU topology.
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `OWNER_PROJECT_ID`: the project ID of the project that owns the capacity reservation.
     * `QUANTITY`: the number of TPUs to attach to the container. Must be aligned with the [TPU topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).

  4. Deploy the Pod:
         
         kubectl apply -f shared-autopilot.yaml
         




Autopilot uses the reserved capacity in the specified reservation to provision a new node to place the Pod.

### Consume a specific reservation block in Autopilot

This section shows you how to consume a specific capacity reservation block that's in the same project as your cluster or in a shared project. This feature is available only for specific accelerators. You can use `kubectl` to configure your Pod to consume the reservation block.

  1. Save the following manifest as `reservation-block-autopilot.yaml`. This manifest has node selectors that consume a specific reservation.

**Local Project**
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: specific-same-project-pod
         spec:
           **nodeSelector :
             cloud.google.com/gke-accelerator: ACCELERATOR
             cloud.google.com/reservation-name: RESERVATION_NAME
             cloud.google.com/reservation-affinity: "specific"
             cloud.google.com/reservation-blocks: RESERVATION_BLOCKS_NAME
           **
           containers:
           - name: my-container
             image: "k8s.gcr.io/pause"
             resources:
               requests:
                 cpu: 12
                 memory: "50Gi"
                 ephemeral-storage: "200Gi"
               limits:
                 nvidia.com/gpu: QUANTITY
         

Replace the following:

     * `ACCELERATOR`: the accelerator that you reserved in the Compute Engine capacity reservation. Must be one of the following values: 
       * **`nvidia-b200`** : NVIDIA B200 (180GB)
       * **`nvidia-h200-141gb`** : NVIDIA H200 (141GB)
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `RESERVATION_BLOCKS_NAME`: the name of the Compute Engine capacity reservation block.
     * `QUANTITY`: the number of GPUs to attach to the container. Must be a supported quantity for the specified GPU, as described in [Supported GPU quantities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#supported-quantities).

For reservations that are owned by a different project, add the cloud.google.com/reservation-project: OWNER_PROJECT_ID to the `spec.nodeSelector` field. Replace `OWNER_PROJECT_ID` with the project ID of the project that owns the capacity reservation.

  2. Deploy the Pod:
         
         kubectl apply -f reservation-block-autopilot.yaml
         

Autopilot uses the reserved capacity in the specified reservation block to provision a new node to place the Pod.




### Consume a specific reservation sub-block in Autopilot

This section shows you how to consume a specific capacity reservation sub-block that's in the same project as your cluster or in a shared project.

  1. Save the following ComputeClass manifest as `reservation-sub-block-computeclass.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: specific-reservation-subblock
         spec:
           nodePoolAutoCreation:
             enabled: true
           priorities:
           - gpu:
               type: ACCELERATOR_TYPE
               count: ACCELERATOR_COUNT
             reservations:
               affinity: Specific
               specific:
               - name: RESERVATION_NAME
                 project: RESERVATION_PROJECT_ID
                 reservationBlock:
                   name: RESERVATION_BLOCK_NAME
                   reservationSubBlock:
                     name: RESERVATION_SUB_BLOCK_NAME
         

Replace the following:

     * `ACCELERATOR_TYPE`: the accelerator that you reserved in the Compute Engine capacity reservation. This value must be `nvidia-gb200`.
     * `ACCELERATOR_COUNT`: the number of accelerators to attach to each node. This value must be a supported quantity for the specified accelerator type. For more information, see [Supported GPU quantities](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus#supported-quantities).
     * `RESERVATION_NAME`: the name of the Compute Engine capacity reservation.
     * `RESERVATION_PROJECT_ID`: the project ID of the project that owns the capacity reservation.
     * `RESERVATION_BLOCK_NAME`: the name of the Compute Engine capacity reservation block.
     * `RESERVATION_SUB_BLOCK_NAME`: the name of the Compute Engine capacity reservation sub-block.
  2. Save the following Pod manifest as `reservation-sub-block-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: reservation-sub-block-pod
         spec:
           nodeSelector:
             cloud.google.com/compute-class: specific-reservation-subblock
           containers:
           - name: my-container
             image: "k8s.gcr.io/pause"
             resources:
               requests:
                 cpu: 12
                 memory: "50Gi"
                 ephemeral-storage: "200Gi"
               limits:
                 nvidia.com/gpu: CONTAINER_GPU_COUNT
         

Replace `CONTAINER_GPU_COUNT` with the number of GPUs to allocate to the container. This value must be less than or equal to the number of accelerators that the compute class attaches to each node.

  3. Deploy the Pod:
         
         kubectl apply -f reservation-sub-block-pod.yaml
         

Autopilot uses the reserved capacity in the specified reservation sub-block to provision a new node to run the Pod.




### Troubleshooting consuming reservations in Autopilot

  * Ensure that the machine types, accelerator types, local SSD configurations, and accelerator quantities match what your workloads will consume. For a complete list of properties which must match, see [Compute Engine capacity reservation properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements).
  * Ensure that the reservation is created with specific affinity, unless you are using a custom ComputeClasses to consume _any_ matching reservation.
  * If you used the `AnyBestEffort` reservation affinity and your reservation was not consumed, GKE might have provisioned on-demand capacity in a different zone within the region. To help ensure consumption of your reserved capacity, use a specific reservation.
  * When using shared reservations, ensure that GKE service agent in the consumer project has permission to list shared reservations in the owner project.



## Consuming reserved instances in GKE Standard

When you create a cluster or node pool, you can indicate the reservation consumption mode by specifying the `--reservation-affinity` flag.

### Consuming any matching reservations with fallback

You can create a reservation and instances to consume any reservation with a fallback to on-demand capacity by using the gcloud CLI or Terraform.

###  gcloud 

To consume from any matching reservations automatically, set the reservation affinity flag to `--reservation-affinity=any`. Since `any` is the default value defined in Compute Engine, you can omit the reservation affinity flag entirely.

In the `any` reservation consumption mode, nodes first take capacity from all single-project reservations before any shared reservations, because the shared reservations are more available to other projects. For more information about how instances are automatically consumed see [Consumption order](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-order).

  1. Create a reservation of three VM instances:
         
         gcloud compute reservations create RESERVATION_NAME \
             --machine-type=MACHINE_TYPE --vm-count=3
         

Replace the following:

     * `RESERVATION_NAME`: the name of the reservation to create.
     * `MACHINE_TYPE`: the [type of machine](https://docs.cloud.google.com/compute/docs/machine-types#machine_types) (name only) to use for the reservation. For example, `n1-standard-2`.
  2. Verify the reservation was created successfully:
         
         gcloud compute reservations describe RESERVATION_NAME
         

  3. Create a cluster having one node to consume _any_ matching reservation:
         
         gcloud container clusters create CLUSTER_NAME \
             --machine-type=MACHINE_TYPE --num-nodes=1 \
             --reservation-affinity=any
         

Replace `CLUSTER_NAME` with the name of the cluster to create.

  4. Create a node pool with three nodes to consume any matching reservation:
         
         gcloud container node-pools create NODEPOOL_NAME \
             --cluster CLUSTER_NAME --num-nodes=3 \
             --machine-type=MACHINE_TYPE --reservation-affinity=any
         

Replace `NODEPOOL_NAME` with the name of the node pool to create.




The total number of nodes is four, which exceeds the capacity of the reservation. Three of the nodes consume the reservation while the last node takes capacity from the general Compute Engine resource pool.

###  Terraform 

To create a reservation of three VM instances using Terraform, refer to the following example:
    
    
    resource "google_compute_reservation" "any_reservation" {
      name = "any-reservation"
      zone = "us-central1-a"
    
      specific_reservation {
        count = 3
    
        instance_properties {
          machine_type = "e2-medium"
        }
      }
    }

To create a cluster having one node to consume _any_ matching reservation using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name     = "gke-standard-zonal-cluster"
      location = "us-central1-a"
    
      initial_node_count = 1
    
      node_config {
        machine_type = "e2-medium"
    
        reservation_affinity {
          consume_reservation_type = "ANY_RESERVATION"
        }
      }
    
      depends_on = [
        google_compute_reservation.any_reservation
      ]
    }

To create a node pool with three nodes to consume any matching reservation using Terraform, refer to the following example:
    
    
    resource "google_container_node_pool" "any_node_pool" {
      name     = "gke-standard-zonal-any-node-pool"
      cluster  = google_container_cluster.default.name
      location = google_container_cluster.default.location
    
      initial_node_count = 3
      node_config {
        machine_type = "e2-medium"
    
        reservation_affinity {
          consume_reservation_type = "ANY_RESERVATION"
        }
      }
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Consuming any matching reservations without fallback

To consume any matching reservation without falling back to on-demand capacity when reservations are exhausted, set the reservation affinity flag to `--reservation-affinity=any-reservation-then-fail`. This reservation affinity requires GKE version 1.36.0-gke.3204000 or later.*

  1. Create a reservation of three VM instances:
         
         gcloud compute reservations create RESERVATION_NAME \
             --machine-type=MACHINE_TYPE --vm-count=3
         

Replace the following:

     * `RESERVATION_NAME`: the name of the reservation to create.
     * `MACHINE_TYPE`: the [type of machine](https://docs.cloud.google.com/compute/docs/machine-types#machine_types) (name only) to use for the reservation, for example, `n1-standard-2`.
  2. Verify that the reservation was created successfully:
         
         gcloud compute reservations describe RESERVATION_NAME
         

  3. Create a cluster that has one node, and configure the node to consume any matching reservation without fallback:
         
         gcloud container clusters create CLUSTER_NAME \
             --machine-type=MACHINE_TYPE --num-nodes=1 \
             --reservation-affinity=any-reservation-then-fail
         

Replace `CLUSTER_NAME` with the name of the cluster to create.

  4. Create a node pool that has three nodes, and configure those nodes to consume any matching reservation without fallback:
         
         gcloud container node-pools create NODEPOOL_NAME \
             --cluster CLUSTER_NAME --num-nodes=3 \
             --machine-type=MACHINE_TYPE \
             --reservation-affinity=any-reservation-then-fail
         

Replace `NODEPOOL_NAME` with the name of the node pool to create.




The total number of nodes is four, which exceeds the capacity of the reservation. Three of the nodes consume the reservation while the last node fails to provision. GKE will reconcile the node pool to provision the last node until new reserved capacity appears or existing capacity is freed.

### Consuming a specific single-project reservation

**Note:** If you're creating a node pool with GPUs, and you're consuming any reservation where the capacity is in a single zone, ensure that you follow the additional recommendations for the scenario of capacity in a single zone. For more information, see Consuming GPU reservations.

To consume a _specific_ reservation, set the reservation affinity flag to `--reservation-affinity=specific` and provide the specific reservation name. In this mode, instances must take capacity from the specified reservation in the zone. The request fails if the reservation does not have sufficient capacity.

To create a reservation and instances to consume a specific reservation, perform the following steps. You can use the gcloud CLI or Terraform.

###  gcloud 

  1. Create a specific reservation for three VM instances:
         
         gcloud compute reservations create RESERVATION_NAME \
             --machine-type=MACHINE_TYPE --vm-count=3 \
             --require-specific-reservation
         

Replace the following:

     * `RESERVATION_NAME`: the name of the reservation to create.
     * `MACHINE_TYPE`: the [type of machine](https://docs.cloud.google.com/compute/docs/machine-types#machine_types) (name only) to use for the reservation. For example, `n1-standard-2`.
  2. Create a node pool with a single node to consume a specific single-project reservation:
         
         gcloud container node-pools create NODEPOOL_NAME \
             --cluster CLUSTER_NAME \
             --machine-type=MACHINE_TYPE --num-nodes=1 \
             --reservation-affinity=specific --reservation=RESERVATION_NAME
         

Replace the following:

     * `NODEPOOL_NAME`: the name of the node pool to create.
     * `CLUSTER_NAME`: the name of the cluster that you created.



###  Terraform 

To create a specific reservation using Terraform, refer to the following example:
    
    
    resource "google_compute_reservation" "specific_reservation" {
      name = "specific-reservation"
      zone = "us-central1-a"
    
      specific_reservation {
        count = 1
    
        instance_properties {
          machine_type = "e2-medium"
        }
      }
    
      specific_reservation_required = true
    }

To create a node pool with a single node to consume a specific single-project reservation using Terraform, refer to the following example:
    
    
    resource "google_container_node_pool" "specific_node_pool" {
      name     = "gke-standard-zonal-specific-node-pool"
      cluster  = google_container_cluster.default.name
      location = google_container_cluster.default.location
    
      initial_node_count = 1
      node_config {
        machine_type = "e2-medium"
    
        reservation_affinity {
          consume_reservation_type = "SPECIFIC_RESERVATION"
          key                      = "compute.googleapis.com/reservation-name"
          values                   = [google_compute_reservation.specific_reservation.name]
        }
      }
    
      depends_on = [
        google_compute_reservation.specific_reservation
      ]
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Consuming a specific shared reservation

To consume a specific shared reservation, configure Identity and Access Management (IAM) permissions to allow the GKE service agent from the consumer project to access the reservation in the owner project.

Complete the following steps in the project that owns the shared reservation:

  1. Create a custom IAM role that contains the `compute.reservations.list` permission in the owner project:
         
         gcloud iam roles create ROLE_NAME \
             --project=OWNER_PROJECT_ID \
             --permissions='compute.reservations.list'
         

Replace the following:

     * `ROLE_NAME`: a name for your new role.
     * `OWNER_PROJECT_ID`: the project ID of the project that owns the capacity reservation.
  2. Give the GKE service agent in the consumer project access to list shared reservations in the owner project:
         
         gcloud projects add-iam-policy-binding OWNER_PROJECT_ID \
             --project=OWNER_PROJECT_ID \
             --member=serviceAccount:service-CONSUMER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
             --role='projects/OWNER_PROJECT_ID/roles/ROLE_NAME'
         

Replace `CONSUMER_PROJECT_NUMBER` with the numerical project number of your consumer project. To find this number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




To create a specific shared reservation and consume the shared reservation, perform the following steps. You can use the gcloud CLI or Terraform.

  1. Follow the steps in [Manage shared reservation creation](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).



###  gcloud 

  1. Create a specific shared reservation:
         
         gcloud compute reservations create RESERVATION_NAME \
             --machine-type=MACHINE_TYPE --vm-count=3 \
             --zone=ZONE \
             --require-specific-reservation \
             --project=OWNER_PROJECT_ID \
             --share-setting=projects \
             --share-with=CONSUMER_PROJECT_IDS
         

Replace the following:

     * `RESERVATION_NAME`: the name of reservation to create.
     * `MACHINE_TYPE`: the name of the [type of machine](https://docs.cloud.google.com/compute/docs/machine-types#machine_types) to use for the reservation. For example, `n1-standard-2`.
     * `OWNER_PROJECT_ID`: the project ID of the project that you want to create this shared reservation. If you omit the `--project` flag, GKE uses the current project as the owner project by default.
     * `CONSUMER_PROJECT_IDS`: a comma-separated list of the [project IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of projects that you want to share this reservation with. For example, `project-1,project-2`. You can include 1 to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the `OWNER_PROJECT_ID`, because it can consume this reservation by default.
  2. Consume the shared reservation:
         
         gcloud container node-pools create NODEPOOL_NAME \
               --cluster CLUSTER_NAME \
               --machine-type=MACHINE_TYPE --num-nodes=1 \
               --reservation-affinity=specific \
               --reservation=projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME
         

Replace the following:

     * `NODEPOOL_NAME`: the name of the node pool to create.
     * `CLUSTER_NAME`: the name of the cluster that you created.



###  Terraform 

To create a specific shared reservation using Terraform, refer to the following example:
    
    
    resource "google_compute_reservation" "specific_reservation" {
      name = "specific-reservation"
      zone = "us-central1-a"
    
      specific_reservation {
        count = 1
    
        instance_properties {
          machine_type = "e2-medium"
        }
      }
    
      specific_reservation_required = true
    }

To consume the specific shared reservation using Terraform, refer to the following example:
    
    
    resource "google_container_node_pool" "specific_node_pool" {
      name     = "gke-standard-zonal-specific-node-pool"
      cluster  = google_container_cluster.default.name
      location = google_container_cluster.default.location
    
      initial_node_count = 1
      node_config {
        machine_type = "e2-medium"
    
        reservation_affinity {
          consume_reservation_type = "SPECIFIC_RESERVATION"
          key                      = "compute.googleapis.com/reservation-name"
          values                   = [google_compute_reservation.specific_reservation.name]
        }
      }
    
      depends_on = [
        google_compute_reservation.specific_reservation
      ]
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

#### Additional considerations for consuming from a specific reservation

When a node pool is created with specific reservation affinity, including default node pools during cluster creation, its size is limited to the capacity of the specific reservation over the node pool's entire lifetime. This affects the following GKE features:

  * **Cluster with multiple zones** : In regional or multi-zonal clusters, nodes of a node pool can span across multiple zones. Since reservations are single-zonal, multiple reservations are needed. To create a node pool consuming specific reservation in these clusters, you must create a specific reservation with exactly the same name and machine properties in each zone of the node pool.
  * **Cluster autoscaling and node pool upgrades** : If you don't have extra capacity in the specific reservation, node pool upgrades or autoscaling of the node pool might fail because both operations require creating extra instances. To resolve this, you can [change the size of the reservation](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources#resizing_a_reservation), or free up some of its bounded resources.



### Consuming GPU reservations

To create a Standard node pool that consumes a GPU reservation, or that consumes any reservation where the capacity is in a single zone, you must specify the `--node-locations` flag when you add a node pool. When you create a [regional Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) or [multi-zonal Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#multi-zonal_clusters), specifying the node locations helps ensure that GKE creates nodes only in a zone where you have reserved GPU capacity.

For detailed instructions about creating a node pool which uses GPUs, refer to [Create a GPU node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create-gpu-pool-auto-drivers).

### Consuming TPU reservations

To create a Standard node pool that consumes a TPU reservation you must specify the `--node-locations` flag when you add a node pool. When you create a [regional Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) or [multi-zonal Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#multi-zonal_clusters), specifying the node locations helps ensure that GKE creates nodes only in a zone where you have reserved TPU capacity.

TPU reservations differ from other machine types. The following are TPU-specific aspects you should consider when creating TPU reservations:

  * When using [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus), `SPECIFIC` is the only supported value for the `--reservation-affinity` flag.



For detailed instructions about creating a node pool which uses TPUs, refer to [Create a TPU node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#create-node-pool).

### Creating nodes without consuming reservations

To explicitly avoid consuming resources from any reservations, set the affinity to `--reservation-affinity=none`.

  1. Create a cluster that won't consume any reservation:
         
         gcloud container clusters create CLUSTER_NAME --reservation-affinity=none
         

Replace `CLUSTER_NAME` with the name of the cluster to create.

  2. Create a node pool that won't consume any reservation:
         
         gcloud container node-pools create NODEPOOL_NAME \
             --cluster CLUSTER_NAME \
             --reservation-affinity=none
         

Replace `NODEPOOL_NAME` with the name of the node pool to create.




### Following available reservations between zones

When using node pools running in multiple zones with reservations that are not equal between zones, you can use the flag `--location_policy=ANY`. This approach helps ensure that when new nodes are added to the cluster they are created in the zone that still has unused reservations.

## Cleaning up

To avoid incurring charges to your Cloud Billing account for the resources used in this page:

  1. Delete the clusters you created by running the following command for each of the clusters:
         
         gcloud container clusters delete CLUSTER_NAME
         

  2. Delete the reservations you created by running the following command for each of the reservations:
         
         gcloud compute reservations delete RESERVATION_NAME
         




## What's next

  * [Learn more about reserving Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources).
  * [Learn more about node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
  * [Learn more about cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * [Learn more about node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
