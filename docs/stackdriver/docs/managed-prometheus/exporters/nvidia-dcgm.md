---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nvidia-dcgm/
title: NVIDIA Data Center GPU Manager (DCGM) \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:37.533276+00:00
---

# NVIDIA Data Center GPU Manager (DCGM)  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/nvidia-dcgm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  NVIDIA Data Center GPU Manager (DCGM) Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your Google Kubernetes Engine deployment so that you can use Google Cloud Managed Service for Prometheus to collect metrics from NVIDIA Data Center GPU Manager. This document shows you how to do the following: 

  * Set up the exporter for DCGM to report metrics.



These instructions apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [source repository](https://github.com/NVIDIA/dcgm-exporter) for DCGM Exporter for installation information.

These instructions are provided as an example and are expected to work in most Kubernetes environments. For information about a managed DCGM offering, see [ Collect and view DCGM metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics).

If you are having trouble installing an application or exporter due to restrictive security or organizational policies, then we recommend you consult open-source documentation for support.

For information about NVIDIA Data Center GPU Manager, see [NVIDIA DCGM](https://developer.nvidia.com/dcgm). 

## Prerequisites

To collect metrics from DCGM by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements: 

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).


  * Verify that you have [ sufficient quota for NVIDIA GPUs](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).

  * To enumerate GPU nodes in your GKE cluster and their GPU types in the relevant cluster, run the following command:
        
        kubectl get nodes -l cloud.google.com/gke-accelerator -o jsonpath='{range .items[*]}{@.metadata.name}{" "}{@.metadata.labels.cloud\.google\.com/gke-accelerator}{"\n"}{end}'
        

  * Note that you might have to [ install a compatible NVIDIA GPU driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#installing_drivers) on the nodes if automatic installation was disabled or not supported for your GKE version. To verify that the NVIDIA GPU device plugin is running, run the following command:
        
        kubectl get pods -n kube-system | grep nvidia-gpu-device-plugin
        


**Note:** these instructions only apply for GKE Standard clusters. Refer to [Run GPUs in GKE Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#create) to create a Standard node pool with NVIDIA GPUs.

## Install the DCGM exporter

We recommend that you install the DCGM exporter, [`DCGM-Exporter`](https://github.com/NVIDIA/dcgm-exporter), by using the following config:
    
    
    # Copyright 2023 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: nvidia-dcgm
      namespace: gmp-public
      labels:
        app: nvidia-dcgm
    spec:
      selector:
        matchLabels:
          app: nvidia-dcgm
      updateStrategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            name: nvidia-dcgm
            app: nvidia-dcgm
        spec:
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: cloud.google.com/gke-accelerator
                    operator: Exists
          tolerations:
          - operator: "Exists"
          volumes:
          - name: nvidia-install-dir-host
            hostPath:
              path: /home/kubernetes/bin/nvidia
              type: Directory
          containers:
          - image: "nvcr.io/nvidia/cloud-native/dcgm:3.3.0-1-ubuntu22.04"
            command: ["nv-hostengine", "-n", "-b", "ALL"]
            ports:
            - containerPort: 5555
              hostPort: 5555
            name: nvidia-dcgm
            securityContext:
              privileged: true
            volumeMounts:
            - name: nvidia-install-dir-host
              mountPath: /usr/local/nvidia
    ---
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: nvidia-dcgm-exporter
      namespace: gmp-public
      labels:
        app.kubernetes.io/name: nvidia-dcgm-exporter
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: nvidia-dcgm-exporter
      updateStrategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            app.kubernetes.io/name: nvidia-dcgm-exporter
        spec:
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: cloud.google.com/gke-accelerator
                    operator: Exists
          tolerations:
          - operator: "Exists"
          volumes:
          - name: nvidia-dcgm-exporter-metrics
            configMap:
              name: nvidia-dcgm-exporter-metrics
          - name: nvidia-install-dir-host
            hostPath:
              path: /home/kubernetes/bin/nvidia
              type: Directory
          - name: pod-resources
            hostPath:
              path: /var/lib/kubelet/pod-resources
          containers:
          - name: nvidia-dcgm-exporter
            image: nvcr.io/nvidia/k8s/dcgm-exporter:3.3.0-3.2.0-ubuntu22.04
            command: ["/bin/bash", "-c"]
            args:
            - hostname $NODE_NAME; dcgm-exporter --remote-hostengine-info $(NODE_IP) --collectors /etc/dcgm-exporter/counters.csv
            ports:
            - name: metrics
              containerPort: 9400
            securityContext:
              privileged: true
            env:
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: "DCGM_EXPORTER_KUBERNETES_GPU_ID_TYPE"
              value: "device-name"
            - name: LD_LIBRARY_PATH
              value: /usr/local/nvidia/lib64
            - name: NODE_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.hostIP
            - name: DCGM_EXPORTER_KUBERNETES
              value: 'true'
            - name: DCGM_EXPORTER_LISTEN
              value: ':9400'
            volumeMounts:
            - name: nvidia-dcgm-exporter-metrics
              mountPath: "/etc/dcgm-exporter"
              readOnly: true
            - name: nvidia-install-dir-host
              mountPath: /usr/local/nvidia
            - name: pod-resources
              mountPath: /var/lib/kubelet/pod-resources
    ---
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: nvidia-dcgm-exporter-metrics
      namespace: gmp-public
    data:
      counters.csv: |
        # Utilization (the sample period varies depending on the product),,
        DCGM_FI_DEV_GPU_UTIL, gauge, GPU utilization (in %).
        DCGM_FI_DEV_MEM_COPY_UTIL, gauge, Memory utilization (in %).
    
        # Temperature and power usage,,
        DCGM_FI_DEV_GPU_TEMP, gauge, Current temperature readings for the device in degrees C.
        DCGM_FI_DEV_MEMORY_TEMP, gauge, Memory temperature for the device.
        DCGM_FI_DEV_POWER_USAGE, gauge, Power usage for the device in Watts.
    
        # Utilization of IP blocks,,
        DCGM_FI_PROF_SM_ACTIVE, gauge, The ratio of cycles an SM has at least 1 warp assigned
        DCGM_FI_PROF_SM_OCCUPANCY, gauge, The fraction of resident warps on a multiprocessor
        DCGM_FI_PROF_PIPE_TENSOR_ACTIVE, gauge, The ratio of cycles the tensor (HMMA) pipe is active (off the peak sustained elapsed cycles)
        DCGM_FI_PROF_PIPE_FP64_ACTIVE, gauge, The fraction of cycles the FP64 (double precision) pipe was active.
        DCGM_FI_PROF_PIPE_FP32_ACTIVE, gauge, The fraction of cycles the FP32 (single precision) pipe was active.
        DCGM_FI_PROF_PIPE_FP16_ACTIVE, gauge, The fraction of cycles the FP16 (half precision) pipe was active.
    
        # Memory usage,,
        DCGM_FI_DEV_FB_FREE, gauge, Framebuffer memory free (in MiB).
        DCGM_FI_DEV_FB_USED, gauge, Framebuffer memory used (in MiB).
        DCGM_FI_DEV_FB_TOTAL, gauge, Total Frame Buffer of the GPU in MB.
    
        # PCIE,,
        DCGM_FI_PROF_PCIE_TX_BYTES, gauge, Total number of bytes transmitted through PCIe TX
        DCGM_FI_PROF_PCIE_RX_BYTES, gauge, Total number of bytes received through PCIe RX
    
        # NVLink,,
        DCGM_FI_PROF_NVLINK_TX_BYTES, gauge, The number of bytes of active NvLink tx (transmit) data including both header and payload.
        DCGM_FI_PROF_NVLINK_RX_BYTES, gauge, The number of bytes of active NvLink rx (read) data including both header and payload.
    

To verify that DCGM Exporter is emitting metrics on the expected endpoints, do the following: 

  1. Set up port-forwarding with the following command:
         
         kubectl -n gmp-public port-forward POD_NAME 9400
         

  2. Access the endpoint `localhost:9400/metrics` by using the browser or the `curl` utility in another terminal session.




You can customize the ConfigMap section to select [which GPU metrics](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/feature-overview.html#profiling-metrics) to emit.

Alternatively, consider using [the official Helm chart](https://github.com/NVIDIA/dcgm-exporter#quickstart-on-kubernetes) to install DCGM Exporter. 

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Define a PodMonitoring resource

For target discovery, the Managed Service for Prometheus Operator requires a PodMonitoring resource that corresponds to DCGM Exporter in the same namespace.

You can use the following PodMonitoring configuration:
    
    
    # Copyright 2023 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: monitoring.googleapis.com/v1
    kind: ClusterPodMonitoring
    metadata:
      name: nvidia-dcgm-exporter
      labels:
        app.kubernetes.io/name: nvidia-dcgm-exporter
        app.kubernetes.io/part-of: google-cloud-managed-prometheus
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: nvidia-dcgm-exporter
      endpoints:
      - port: metrics
        interval: 30s
      targetLabels:
        metadata: []
    

To apply configuration changes from a local file, run the following command: 
    
    
    kubectl apply -n NAMESPACE_NAME -f FILE_NAME
    

You can also [use Terraform](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#terraform-scrape) to manage your configurations.

## Verify the configuration

You can use Metrics Explorer to verify that you correctly configured DCGM Exporter. It might take one or two minutes for Cloud Monitoring to ingest your metrics.

To verify the metrics are ingested, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter and run the following query:  

         
         DCGM_FI_DEV_GPU_UTIL{cluster="CLUSTER_NAME", namespace="gmp-public"}
         




## Troubleshooting

For information about troubleshooting metric ingestion problems, see [ Problems with collection from exporters](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#exporter-problems) in [ Troubleshooting ingestion-side problems](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/troubleshooting#ingest-problems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
