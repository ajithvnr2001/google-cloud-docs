---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/gpus/
title: Troubleshoot GPUs in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:06.356973+00:00
---

# Troubleshoot GPUs in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Troubleshoot GPUs in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

If your Google Kubernetes Engine (GKE) Pods are stuck in a `Pending` state while requesting `nvidia.com/gpu` resources, or if your nodes fail to register their available GPUs, you might have an issue with the NVIDIA driver installation or your node pool configuration. These problems prevent your workloads from accessing the GPU hardware that they need.

This document shows you how to diagnose and resolve common problems that prevent GKE from scheduling or running GPU-accelerated workloads. Learn how to verify the GPU driver installation, inspect Pod and node logs for errors, and confirm that your configurations are correct.

This information is for Platform admins and operators who manage GPU-enabled node pools and need to resolve NVIDIA driver issues, and for Application developers who need to debug GPU workloads that are stuck or failing to start. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## GPU driver installation

This section provides troubleshooting information for automatic NVIDIA device driver installation in GKE.

### Driver installation fails in Ubuntu nodes

If you use Ubuntu nodes that have attached L4, RTX PRO 6000, H100, or H200 GPUs, the default GPU driver that GKE installs might not be at or later than the required version for those GPUs. As a result, the GPU device plugin Pod remains stuck in the Pending state and your GPU workloads on those nodes might experience issues.

To resolve this issue, see the instructions for the respective GPU:

### L4 and H100

To resolve this issue for L4 and H100 GPUs, we recommend upgrading to the following GKE versions which install GPU driver version 535 as the default driver:

  * 1.26.15-gke.1483000 and later
  * 1.27.15-gke.1039000 and later
  * 1.28.11-gke.1044000 and later
  * 1.29.6-gke.1073000 and later
  * 1.30.2-gke.1124000 and later



Alternatively, you can manually install driver version 535 or later by running the following command:
    
    
    kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/ubuntu/daemonset-preloaded-R535.yaml
    

### RTX PRO 6000

To resolve this issue for RTX PRO 6000 GPUs, upgrade to one of the following GKE versions. These versions install GPU driver version 580 as the default driver:

  * 1.32.8-gke.1170000 and later
  * 1.33.4-gke.1245000 and later
  * 1.34.0-gke.1662000 and later



This solution works only for [G4 machine types](https://docs.cloud.google.com/compute/docs/gpus#rtx-6000-gpus) with one or more GPUs. G4 machine types that have less than one GPU don't support Ubuntu node images.

### H200

To resolve this issue for H200 GPUs, you must manually install driver version 550 or later by running the following command:
    
    
    kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/nvidia-driver-installer/ubuntu/daemonset-preloaded-R550.yaml
    

### GPU device plugins fail with CrashLoopBackOff errors

The following issue occurs if you used the [manual driver installation method](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers) in your node pool prior to **January 25, 2023** and later upgraded your node pool to a GKE version that supports automatic driver installation. Both installation workloads exist at the same time and try to install conflicting driver versions on your nodes.

The GPU device plugin init container fails with the `Init:CrashLoopBackOff` status. The logs for the container are similar to the following:
    
    
    failed to verify installation: failed to verify GPU driver installation: exit status 18
    

To resolve this issue, try the following methods:

  * Remove the manual driver installation DaemonSet from your cluster. This deletes the conflicting installation workload and lets GKE automatically install a driver to your nodes.

**Note:** Ensure that all of your node pools use automatic installation before you delete the DaemonSet.
        
        kubectl delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml
        

  * Re-apply the manual driver installation DaemonSet manifest to your cluster. On January 25, 2023, we updated the manifest to ignore nodes that use automatic driver installation.
        
        kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nvidia-driver-installer/cos/daemonset-preloaded.yaml
        

  * Disable automatic driver installation for your node pool. The existing driver installation DaemonSet should work as expected after the update operation completes.
        
        gcloud container node-pools update POOL_NAME \
            --accelerator=type=GPU_TYPE,count=GPU_COUNT,gpu-driver-version=disabled \
            --cluster=CLUSTER_NAME \
            --location=LOCATION
        

Replace the following:

    * `POOL_NAME`: the name of the node pool.
    * `GPU_TYPE`: the GPU type that the node pool already uses.
    * `GPU_COUNT`: the number of GPUs that are already attached to the node pool.
    * `CLUSTER_NAME`: the name of the GKE cluster that contains the node pool.
    * `LOCATION`: the Compute Engine location of the cluster.



For more information about mapping the GPU driver version to GKE version, see Map the GKE version and Container-Optimized OS node image version to the GPU driver version.

### Error: "Container image cos-nvidia-installer:fixed is not present with pull policy of Never." or "Container image ubuntu-nvidia-installer:fixed is not present with pull policy of Never."

This issue occurs when the `nvidia-driver-installer` Pods are in the `PodInitializing` state and the GPU plugin device or the GPU driver installer Pods report the following error. The specific error message depends on the operating system running on your node:

### COS
    
    
    Container image "cos-nvidia-installer:fixed" is not present with pull policy of Never.
    

### Ubuntu
    
    
    Container image "gke-nvidia-installer:fixed" is not present with pull policy of Never.
    

This issue can occur when the garbage collector removes the preloaded NVIDIA driver image to free space on a node. When the driver Pod is recreated or its container is restarted, GKE won't be able to locate the preloaded image.

To mitigate the garbage collection issue when you are running COS, upgrade your GKE nodes to one of these versions that contain the fix:

  * 1.25.15-gke.1040000 and later
  * 1.26.10-gke.1030000 and later
  * 1.27.6-gke.1513000 and later
  * 1.28.3-gke.1061000 and later



For more information about mapping the GPU driver version to GKE version, see Map the GKE version and Container-Optimized OS node image version to the GPU driver version.

If your nodes are running Ubuntu, no fix is available yet for this garbage collection issue. To mitigate this issue on Ubuntu, you can run a privileged container that interacts with the host to ensure the correct setup of NVIDIA GPU drivers. To do so, run `sudo /usr/local/bin/nvidia-container-first-boot` from your node or apply the following manifest:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: gke-nvidia-installer-fixup
    spec:
      nodeSelector:
        cloud.google.com/gke-os-distribution: ubuntu
      hostPID: true
      containers:
      - name: installer
        image: ubuntu
        securityContext:
          privileged: true
        command:
          - nsenter
          - -at
          - '1'
          - --
          - sh
          - -c
          - "/usr/local/bin/nvidia-container-first-boot"
      restartPolicy: Never
    

Another potential cause of the issue is when the NVIDIA driver images are lost after node reboot or host maintenance. This may occur on confidential nodes, or nodes with GPUs, that use ephemeral local SSD storage. In this situation, GKE preloads the `nvidia-installer-driver` container images on nodes and moves them from the boot disk to the local SSD on first boot.

To confirm there was a host maintenance event, use the following log filter:
    
    
    resource.type="gce_instance"
    protoPayload.serviceName="compute.googleapis.com"
    log_id("cloudaudit.googleapis.com/system_event")
    

To mitigate the host maintenance issue, upgrade your GKE version to one of these versions:

  * 1.27.13-gke.1166000 and later
  * 1.29.3-gke.1227000 and later
  * 1.28.8-gke.1171000 and later



### Error: failed to configure GPU driver installation dirs: failed to create lib64 overlay: failed to create dir /usr/local/nvidia/lib64: mkdir /usr/local/nvidia/lib64: not a directory.

You encounter this error from the GPU driver installer container inside the GPU device plugin when NCCL fastsocket is enabled:
    
    
    failed to configure GPU driver installation dirs: failed to create lib64 overlay: failed to create dir /usr/local/nvidia/lib64: mkdir /usr/local/nvidia/lib64: not a directory.
    

This issue only happens on clusters and nodes running GKE 1.28 and 1.29.

The issue is caused by a NCCL fastsocket race condition with the GPU driver installer.

To mitigate this issue, upgrade your GKE version to one of these versions:

  * 1.28.8-gke.1206000 and later
  * 1.29.3-gke.1344000 and later



For more information, read the [GPUDirect-TCPXO Release Notes](https://github.com/GoogleCloudPlatform/container-engine-accelerators/blob/master/gpudirect-tcpxo/README.md).

### Error: Failed to get device for nvidia0: device nvidia0 not found.

The following error indicates that XID 62 and RmInitAdapter failed for GPU with minor 0:
    
    
    Failed to get device for nvidia0: device nvidia0 not found.
    

NVIDIA driver version 525.105.17 has a bug that can cause communication errors (XID) and prevent the GPU from initializing properly, leading to a failure to initialize the GPU.

To fix this issue, upgrade the NVIDIA driver to driver version 525.110.11 or later.

## GPUDirect RDMA issues

This section provides troubleshooting information for GPUDirect RDMA issues.

### Error: Network gIB plugin is not found

The `pytorch/pytorch:latest` image from the PyTorch repository doesn't include the Netlink Library Protocol Suite (`libnl`), which is needed by the gIB plugin. The following error indicates that gIB plugin didn't load because the `libnl` libraries are missing from the image:
    
    
    ncclInvalidUsage: Error: network gIB not found.
    

To resolve this issue, you must use a different Pytorch base image or manually add the libraries to your containers. The issue is not specific to any machine type. For more information about using NCCL/gIB, see [Optimize cluster networking by using NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview).

#### Resolve the issue by using the Nvidia PyTorch image

You can fix this issue by using the [NVIDIA PyTorch image](https://nvcr.io/nvidia/pytorch:26.04-py3). To find the latest version, see the [PyTorch Release Notes](https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/index.html).

#### Resolve the issue through manual installation

If you can't migrate to another image base, you can also manually install the `libnl` libraries in the container image.
    
    
    apt update -y && apt upgrade -y && apt install -y libnl-3-200 libnl-route-3-200
    

To help ensure the consistency of IBVerbs library within the workload container, use the updated NCCL RDMA Installer DaemonSet to install the gIB plugin libraries on the container path.

To download the DaemonSet configuration, clone the container engine accelerators repository:
    
    
    cd
    git clone https://github.com/GoogleCloudPlatform/container-engine-accelerators.git
    

Find the configuration under tree/master/gpudirect-rdma directory:
    
    
    cd container-engine-accelerators/gpudirect-rdma
    ls -l nccl-rdma-installer*
    -rw-r----- 1 adelab primarygroup 2899 May  6 15:57 nccl-rdma-installer-a4x.yaml
    -rw-r----- 1 adelab primarygroup 2743 Apr 30 00:34 nccl-rdma-installer-autopilot.yaml
    -rw-r----- 1 adelab primarygroup 2677 May  6 15:57 nccl-rdma-installer.yaml
    

Choose one of the following installer configurations:

Description | `nccl-rdma-installer.yaml` | `nccl-rdma-installer-a4x.yaml` | `nccl-rdma-installer-autopilot.yaml`  
---|---|---|---  
GKE mode of operation | GKE Standard | GKE Standard | GKE Autopilot  
Machine types | [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-machine-type) and [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) machine types | [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-machine-type) machine type | [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-machine-type) and [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) machine types  
Namespace | Deploys to `kube-system`. | Deploys to `kube-system`. | Deploys to a dedicated `rdma-system` namespace (because Autopilot restricts modifications to the `kube-system` namespace).  
Priority class | Uses `system-node-critical` to help ensure the installer runs with high priority. | Uses `system-node-critical`. | None. (Autopilot restricts the use of system-level priority classes).  
Function | Runs as a DaemonSet and installs the GPUDirect-TCPX (GIB) NCCL plugin (specifically `nccl-plugin-gib:v1.1.1`) to the `/home/kubernetes/bin/nvidia/lib64` and `/home/kubernetes/bin/gib` host directories. This approach enables high-performance RDMA communication for NCCL on GKE nodes. | Similar to the base installer, but installs the ARM64-compiled version of the GPUDirect-TCPX (GIB) NCCL plugin (`nccl-plugin-gib-arm64:v1.1.0`). Also includes a specific node affinity for `nvidia-gb200` and `arm64` to help ensure it runs only on these specific GKE nodes. | Installs the GPUDirect-TCPX (GIB) NCCL plugin (`nccl-plugin-gib:v1.1.1`), but with modifications that support the security and operational model of Autopilot mode: 

  * It deploys in the `rdma-system` namespace.
  * The installation script is invoked with the `--install-nccl` flag, which performs additional setup to help ensure NCCL itself is properly configured or installed in the Autopilot environment. In GKE Autopilot, the host environment might be more restricted or pre-configured differently compared to GKE Standard.

  
  
Apply the daemonset:
    
    
    kubectl apply -f nccl-rdma-installer.yaml
    

### Map the GKE version and Container-Optimized OS node image version to the GPU driver version

To find the GPU driver versions that are mapped with [GKE versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) and Container-Optimized OS node image versions, do the following steps: 

  1. [Map Container-Optimized OS node image versions to GKE patch versions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#map-gke-cos) for the specific GKE version where you want to find the GPU driver version. For example, 1.33.0-gke.1552000 uses cos-121-18867-90-4. 
  2. Choose the milestone of the Container-Optimized OS node image version in the [Container-Optimized OS release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes). For example, choose Milestone 121 for cos-121-18867-90-4. 
  3. In the release notes page for the specific milestone, find the release note corresponding with the specific Container-Optimized OS node image version. For example, in [Container-Optimized OS Release Notes: Milestone 121](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121), see [cos-121-18867-90-4](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m121#cos-121-18867-90-4_). In the table in the **GPU Drivers** column, click **See List** to see the GPU driver version information. 



In GKE version 1.36.0-gke.3302004 and later, GKE automatically publishes the installed NVIDIA driver version as annotations on running GPU nodes. To view the driver version annotations on a GPU node, run the following command:
    
    
    kubectl get node GPU_NODE_NAME -o jsonpath='{.metadata.annotations}'

Replace `GPU_NODE_NAME` with the name of your GPU node.

The output includes annotations similar to the following:
    
    
    {
      "cloud.google.com/cuda.driver-version.full": "580.126.20",
      "cloud.google.com/cuda.driver-version.major": "580",
      "cloud.google.com/cuda.driver-version.minor": "126",
      "cloud.google.com/cuda.driver-version.revision": "20"
    }
    

### The `nvidia-smi` command fails

When you use GPU VMs to run workloads in GKE, commands like `nvidia-smi` might fail within the container with any of the following errors:

  * `bash: nvidia-smi: command not found`
  * Errors indicating that `libnvidia-ml.so` or other NVIDIA libraries cannot be found.



GKE mounts the necessary NVIDIA drivers and tools from the host node in your containers, typically under the `/usr/local/nvidia/` path. However, the container's default environment variables (`PATH` and `LD_LIBRARY_PATH`) might not include the paths to these NVIDIA binaries and libraries.

To solve these errors, update your Pod or Deployment manifest to include the necessary NVIDIA paths in the `PATH` and `LD_LIBRARY_PATH` environment variables for the container.

For example, add the following `env` block to your `spec.template.spec.containers` spec:
    
    
    spec:
      containers:
      - name: gpu-container
        image: gpu-image
        env:
        - name: LD_LIBRARY_PATH
          # Prepend NVIDIA lib64 directory to existing LD_LIBRARY_PATH
          value: /usr/local/nvidia/lib64
        - name: PATH
          # Prepend NVIDIA bin directory to existing PATH
          value: /usr/local/nvidia/bin:$PATH
        # ... other container settings
    

## Guest OS reboot for standard clusters

This section demonstrates how to use GKE to manage the reboot of the guest OS running on the node for standard clusters.

A GKE node might require a reboot when it has Xid or other GPU issues. For examples of Xid issues, see [Compute Engine Xid handling](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#xid_messages).

When you reboot the guest OS with this method the following occurs:

  * The guest OS is reset.
  * The GPU is reset.
  * The underlying instance is not changed and the boot disk is preserved, but after the reboot, the boot ID is different.



The reboot operation takes about five minutes. This time is in addition to the termination grace period configured on the pods. For more details about the Pod lifecycle and termination period, see [Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination).

### Requirements

This method for guest OS reboot requires the cluster to be running GKE version 1.37.0-gke.3503000 or later. Don't trigger a guest OS reboot on earlier versions, because GKE might not be able to schedule workloads on your nodes after the reboot completes.

### Reboot the guest OS on a GKE node

To reboot the guest OS on a GKE node, follow these steps:

  1. Identify the node to reboot.

  2. Apply the `cloud.google.com/perform-reboot=true` label by using the following command:
         
         kubectl label nodes NODE_NAME cloud.google.com/perform-reboot=true
         

Replace `NODE_NAME` with the name of the node.

When this label is applied, GKE reboots the guest OS by performing the following steps:

     1. Cordon the node.
     2. Evicts Pods, respecting any [distribution budgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and termination grace period. For details about how to configure these termination behaviors, see [Configure GKE to terminate your workloads gracefully](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#configure-gkev)
     3. Reboots the node by using `systemd`. The node shuts down and restarts, and the boot ID changes.
  3. Go to the node events to see that the node has successfully rebooted.

     1. In the Google Cloud console, go to **Kubernetes Engine** > **Clusters**.

[ Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

     2. Select the cluster that contains the node you're rebooting.

     3. Click **Nodes** and then select the node you're rebooting.

     4. Click **Events** to view the node events page.

Node events are recorded on this page. Events from a successful reboot process include the following:

        * When the node starts up after the reboot.
        * When the maintenance handler removes the `perform-reboot` node label.
        * When the boot ID change is detected.



If you followed these steps for a node that runs a version earlier than 1.37.0-gke.3503000, then the node might retain both the `cloud.google.com/impending-node-termination` taint and the `cloud.google.com/perform-reboot=true` label after the reboot completes. The node has the `Ready` state but can't run workloads. To resolve this issue, upgrade to GKE version 1.37.0-gke.3503000 or later. To mitigate this issue without upgrading, manually remove the taint and label from the affected node by running the following commands:
    
    
    # Remove the perform-reboot label
    kubectl label node NODE_NAME cloud.google.com/perform-reboot-
    
    # Remove the boot ID annotation (might report "not found", which is expected)
    kubectl annotate node NODE_NAME node.gke.io/reboot-boot-id-
    
    # Remove the taint (might already be removed automatically, which is expected)
    kubectl taint nodes NODE_NAME cloud.google.com/impending-node-termination:NoSchedule-
    

Replace `NODE_NAME` with the name of the stuck node.

After you remove the stuck state, wait at least 60 seconds for the maintenance handler to detect the changes. Don't attempt a guest OS reboot again unless your cluster runs version 1.37.0-gke.3503000 or later.

#### Reboot label ignored when re-applied quickly

On all GKE versions, if you re-apply the `cloud.google.com/perform-reboot=true` label within 60 seconds of a completed reboot, the maintenance handler might not act on the new label due to a race condition in its internal state. The node remains stuck with the `perform-reboot` label and the `cloud.google.com/impending-node-termination` taint, but no reboot occurs.

To mitigate this issue, wait at least 60 seconds after a reboot completes before re-applying the `cloud.google.com/perform-reboot=true` label. You can verify that the reboot completed by checking that the `perform-reboot` label and the `reboot-boot-id` annotation were removed from the node:
    
    
    kubectl get node NODE_NAME -o jsonpath='{.metadata.labels.cloud\.google\.com/perform-reboot}'
    kubectl get node NODE_NAME -o jsonpath='{.metadata.annotations.node\.gke\.io/reboot-boot-id}'
    

Replace `NODE_NAME` with the name of the node.

Both commands should return empty output before you re-apply the label.

If the node is already stuck, manually remove the Kubernetes node metadata that's causing the stuck state:

  1. Remove the `cloud.google.com/perform-reboot` node label:
         
         kubectl label node NODE_NAME \
             cloud.google.com/perform-reboot-
         

Replace `NODE_NAME` with the name of the stuck node.

  2. Remove the `node.gke.io/reboot-boot-id` annotation:
         
         kubectl annotate node NODE_NAME \
             node.gke.io/reboot-boot-id-
         

If the output is `not found`, then the annotation is already removed.

  3. Remove the `cloud.google.com/impending-node-termination:NoSchedule` taint:
         
         kubectl taint nodes NODE_NAME \
             cloud.google.com/impending-node-termination:NoSchedule-
         

If the output is `not found`, then the taint is already removed.

  4. Wait for at least 60 seconds.

  5. Re-apply the `cloud.google.com/perform-reboot` label:
         
         kubectl label node NODE_NAME \
             cloud.google.com/perform-reboot=true
         




## Reset GPUs on A3 and A4 VMs

Some issues might require you to reset the GPU on an A3 or A4 VM.

**Note:** You can also use the [gpu-reset-tool](https://github.com/ai-on-gke/tutorials-and-examples/tree/main/gpu-reset-tool) to reset all the GPUs. This tool automates the reset process and requires only the target node name.

To manually reset the GPU, follow these steps:

  1. Remove Pods that request GPU resources from the node where you need to reset the GPU.

  2. Disable the GPU device plugin on the node:
         
         kubectl get nodes \
             --selector=kubernetes.io/hostname=NODE_NAME \
             --no-headers | awk '{print $1}' \
             | xargs -I{} kubectl label node {} gke-no-default-nvidia-gpu-device-plugin=true
         

Replace `NODE_NAME` with the name of the node.

  3. If you have [DCGM metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics) enabled, then temporarily disable the DCGM exporter on the node by changing the driver version label:

a. Note the current value of the `cloud.google.com/gke-gpu-driver-version` label on the node.

b. Change the label value to `reset` to evict the DCGM exporter Pod:
         
         kubectl label node NODE_NAME \
               cloud.google.com/gke-gpu-driver-version=reset --overwrite
         

The Pod is automatically evicted because it requires the label to be `default` or `latest`.

  4. [Connect to the VM](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) backing the node.

  5. In the SSH session, reset the GPU:

Reset all the GPUs on the VM
         
         /home/kubernetes/bin/nvidia/bin/nvidia-smi --gpu-reset
         

To reset a specific GPU
         
         # Identify the faulty GPU
         /home/kubernetes/bin/nvidia/bin/nvidia-smi
         
         # Reset the specifc GPU using either the GPU index or PCI bus ID from above command output 
         /home/kubernetes/bin/nvidia/bin/nvidia-smi --gpu-reset -i <gpu_id>
         

  6. Restore the node labels to re-enable the GPU device plugin and DCGM exporter:

a. Re-enable the GPU device plugin:
         
         kubectl get nodes --selector=kubernetes.io/hostname=NODE_NAME \
               --no-headers \| awk '{print $1}' \
               | xargs -I{} kubectl label node {} gke-no-default-nvidia-gpu-device-plugin=false \
               --overwrite
         

b. Restore the original value of the `cloud.google.com/gke-gpu-driver-version` label (for example, `latest` or `default`) to re-enable the DCGM exporter:
         
         kubectl label node NODE_NAME \
               cloud.google.com/gke-gpu-driver-version=ORIGINAL_VALUE --overwrite
         




## GPUs on Confidential GKE Nodes

The following sections show you how to identify and fix issues with GPUs that run on Confidential GKE Nodes.

### GPU workloads not scheduling on Confidential GKE Nodes

Confidential GKE Nodes requires that you manually install a GPU driver that corresponds to your selected GPU type and your GKE version. If your GPU Pods aren't scheduling on Confidential GKE Nodes and remain in the `Pending` state, describe the driver installation DaemonSet:
    
    
    kubectl --namespace=kube-system get daemonset nvidia-driver-installer -o yaml
    

If the output returns a `NotFound` error, [install the driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers).

If the DaemonSet is running, the output is similar to the following:
    
    
    apiVersion: apps/v1
    kind: DaemonSet
    # lines omitted for clarity
    spec:
      revisionHistoryLimit: 10
      selector:
        matchLabels:
          k8s-app: nvidia-driver-installer
      template:
        metadata:
          creationTimestamp: null
          labels:
            k8s-app: nvidia-driver-installer
            name: nvidia-driver-installer
        **spec:
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: cloud.google.com/gke-accelerator
                    operator: Exists
                  - key: cloud.google.com/gke-gpu-driver-version
                    operator: DoesNotExist
                  - key: cloud.google.com/gke-confidential-nodes-instance-type
                    operator: In
                    values:
                    - TDX**
    

In this output, verify that the `nodeAffinity` field contains the `cloud.google.com/gke-confidential-nodes-instance-type` key. If the output doesn't contain this key, the driver installation DaemonSet doesn't support Confidential GKE Nodes.

Deploy the DaemonSet that supports GPUs on Confidential GKE Nodes:
    
    
    kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/nvidia-driver-installer/cos/daemonset-confidential.yaml
    

After you install the drivers, check whether your GPU workloads start successfully.

### Error: Failed to allocate device vector

The following error message in your GPU container logs indicates that the GPU was detached from the node VM instance:
    
    
    Failed to allocate device vector A (error code unknown error)!
    

This detachment might happen because of a hardware error or because of an issue with the encryption keys.

To resolve this issue, reboot the node instance. This operation is disruptive, and affects all of the workloads on that node. To reboot the instance, do the following steps:

  1. Get the name of the node that runs the GPU Pod:
         
         kubectl get pod POD_NAME -o yaml | grep "nodeName"
         

Replace `POD_NAME` with the name of the failing Pod.

The output is similar to the following:
         
         nodeName: gke-cluster-1-default-pool-b7asdfbt-fd3e
         

  2. Reset the Compute Engine instance:
         
         gcloud compute instances reset NODE_NAME
         

Replace `NODE_NAME` with the node name from the output of the previous step.

The gcloud CLI looks for VMs with that name in your active project. If you see a prompt to select a zone, specify `Y`.

  3. Check whether your GPU workloads run without errors.




### Error: Decryption failed with error -74

The following error message in your node logs indicates that the encryption keys for the GPU were lost:
    
    
    Decryption failed with error -74
    

This error happens when the NVIDIA persistence daemon, which runs on the node VM instance, fails. If you see this error message, reset the instance:
    
    
    gcloud compute instances reset NODE_NAME
    

Replace `NODE_NAME` with the name of the failing node.

The gcloud CLI looks for VMs with that name in your active project. If you see a prompt to select a zone, specify `Y`.

If resetting the instance doesn't fix this issue, contact Cloud Customer Care or submit a product bug. For more information, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support).

## Finding XID errors

The `gpu-device-plugin` daemonset runs within the `kube-system` namespace and is responsible for the following:

  * **GPU workload scheduling:** allocating GPU resources to Pods.
  * **GPU health checking:** monitoring the health of your GPUs.
  * **GPU metrics gathering:** collecting GPU-related metrics, such as duty cycle and memory usage.



The `gpu-device-plugin` uses NVIDIA Management Library (NVML) to detect XID errors. When an XID error occurs, the `gpu-device-plugin` Pod running on the affected node logs the error. You will find two types of XID error logs:

  * **Non-critical XID errors:**
    * Log format: `Skip error Xid=%d as it is not Xid Critical`
    * Meaning: These errors are considered non-critical. They can be caused by various software or hardware issues.
    * Action: GKE takes no automated action for non-critical XID errors.
  * **Critical XID errors:**
    * Log format: `XidCriticalError: Xid=%d, All devices will go unhealthy`
    * Meaning: These errors indicate a GPU hardware issue.
    * Action: 
      * GKE marks the node's GPU resources as unhealthy.
      * GKE prevents GPU workloads from being scheduled on the node.
      * If node auto-repair is enabled, GKE will recreate the node.



## GPUDirect-TCPX(O) issues

This section provides troubleshooting information for GPUDirect-TCPX(O) issues. If you are using affected versions of GKE version 1.34 or 1.35, also see the [GKE Known issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/known-issues#tcpx-cos125) page.

### Release note and upgrade instructions

For new users, [Maximize GPU network bandwidth in Standard mode clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx) provides guidance on using GPUDirect-TCPX(O). For existing users, read the [GPUDirect-TCPXO Release Notes](https://github.com/GoogleCloudPlatform/container-engine-accelerators/blob/master/gpudirect-tcpxo/README.md) for release information and upgrade instructions, because new versions are continuously released.

### `tcpx-daemon` and `tcpxo-daemon` failure after GKE version upgrade

You might encounter the following error if your `tcpx-daemon` or `tcpxo-daemon` Pods fail:
    
    
    cuda error detected! name: CUDA_ERROR_NO_DEVICE; string: no CUDA-capable device is detected
    

Also, check if the `device-injector` Pods in the `kube-system` namespace are in the `CrashLoopBackOff` or `Error` state.

This issue occurs if you upgraded your GKE node pools to one of the following versions or later:

  * For GKE 1.31: 1.31.14-gke.1033000
  * For GKE 1.32: 1.32.9-gke.1575000
  * For GKE 1.33: 1.33.5-gke.1862000
  * For GKE 1.34: 1.34.1-gke.3225000
  * For GKE 1.35 and later



The issue is caused by using an older version of the [NRI device injector](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx#nri-device-injector) manifest that includes an `initContainer` named `enable-nri`. In these affected GKE versions, NRI is enabled by default in the node configuration. The obsolete `enable-nri` container attempts to modify the configuration and restart the container runtime, which conflicts with the system defaults and causes the `nri-device-injector` Pods to crash. This failure prevents GPU devices from being exposed to the `tcpx-daemon` or `tcpxo-daemon` container.

To resolve this issue, update the `nri-device-injector` DaemonSet to the latest version, which removes the conflicting `initContainer`.

  1. Delete the existing DaemonSet:
         
         kubectl delete daemonset device-injector -n kube-system
         

  2. Apply the latest manifest:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/nri_device_injector/nri-device-injector.yaml
         

  3. Restart your workload Pods.




### Debug with NCCL logs

If you can't resolve an issue with NCCL, collect NCCL logs with debugging information. These logs contain valuable information about NCCL operations and can help you find the source of your problem. If you can't resolve the issue, collect these logs _before_ you open a case with Cloud Customer Care. These logs can help Cloud Customer Care resolve your issue more quickly.

To generate and collect the logs, complete the following steps:

  1. Set the following environment variables inside your Pod or application manifest:
         
         NCCL_DEBUG=INFO
         NCCL_DEBUG_SUBSYS=INIT,NET,ENV,COLL,GRAPH
         NCCL_DEBUG_FILE=/DIRECTORY/FILE_NAME.%h.%p
         

For more information about these environment variables, read [collect NCCL debugging logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx#collect-nccl-debugging-logs).

  2. To generate data for your logs, run an [NCCL test](https://github.com/NVIDIA/nccl-tests). The way to run this test depends on the type of cluster that you use. For GKE clusters, you can [deploy and run NCCL test with Topology Aware Scheduling (TAS)](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute#deploy-run-nccl-tas-test). After you run the NCCL test, NCCL automatically generates the logs on all participating nodes.

  3. Collect the logs from all nodes. Verify that you've collected NCCL logs from all nodes by verifying that the logs contain the following information:

     * The hostnames of all VMs that are involved in a workload.
     * The PIDs of all relevant processes on the VM.
     * The ranks of all GPUs that are used by the workload on each VM.

If you're not sure where the log files are located, the following example shows you where NCCL creates the log files when the `NCCL_DEBUG_FILE` variable is set to `/tmp/nccl_log.%h.%p`. You have two VMs named `a3plus-vm-1` and `a3plus-vm-2`, and each VM runs eight processes within the workload container. In this scenario, NCCL creates the following log files under the `/tmp` directory within the workload container on each VM:

     * On `a3plus-vm-1`: eight log files named `nccl_log.a3plus-vm-1.PID`, where `PID` is the process ID.
     * On `a3plus-vm-2`: eight log files named `nccl_log.a3plus-vm-2.PID`.
  4. Review the logs. NCCL log entries have the following format:
         
         HOSTNAME:PID:TID [RANK] NCCL_MESSAGE
         

These log entries contain the following values:

     * `HOSTNAME`: the hostname of the VM. This value identifies which VM was being used when NCCL generated the log entry.
     * `PID`: the PID. This value identifies which process generated the log entry.
     * `TID`: the thread ID. This value identifies which thread within the process was being used when NCCL generated the log entry.
     * `RANK`: the local rank ID. This value identifies which GPU was being used when NCCL generated the log entry. Ranks are numbered from 0-N, where N is the total number of GPUs that are involved in the process. For example, if your workload runs with eight GPUs per VM, then each VM should have eight different rank values (0-7).
     * `NCCL_MESSAGE`: a descriptive message that provides more information about the event and includes the timestamp of when NCCL created the log.

For example:
    
    gke-a3plus-mega-np-2-aa33fe53-7wvq:1581:1634 [1] NCCL INFO 00:09:24.631392: NET/FasTrak plugin initialized.
    

This example has the following values:

     * `gke-a3plus-mega-np-2-aa33fe53-7wvq`: the hostname.
     * `1581`: the process ID.
     * `1634`: the thread ID.
     * `1`: the local rank ID.
     * `NCCL INFO 00:09:24.631392: NET/FasTrak plugin initialized.`: the message explaining what happened.
  5. If you're opening a support case, package the logs that you collected, along with the output of the NCCL test, into a zip file. Include the zip file when you [submit a support case to Cloud Customer Care](https://cloud.google.com/support-hub).

  6. To stop collecting NCCL debugging logs, remove the variables that you added in step 1.




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
