---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a3-mega-high/
title: Run NCCL on GKE clusters that use A3 Mega or A3 High \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:06.438448+00:00
---

# Run NCCL on GKE clusters that use A3 Mega or A3 High  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a3-mega-high/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run NCCL on GKE clusters that use A3 Mega or A3 High Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This page describes how to run [NVIDIA Collective Communications Library (NCCL)](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview) tests on _custom GKE clusters_ that use A3 Mega and A3 High with GPUDirect-TCPXO and GPUDirect-TCPX networking protocols. A custom GKE cluster is a cluster that you create by using `gcloud` commands.

You can use the tests that are described on this page for the following scenarios:

  * If your GKE cluster uses Flex-start nodes, then use a basic test on two nodes.
  * If your GKE cluster uses different types of nodes such as on-demand or reservation-bound nodes, then use an NCCL test with Topology Aware Scheduling.



## Before you begin

The tests on this page use [JobSet](https://jobset.sigs.k8s.io/docs/overview/) and [Kueue with Topology Aware Scheduling (TAS)](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/). Before running any tests, you must set up your cluster and do the following:

  1. [Install JobSet](https://jobset.sigs.k8s.io/docs/installation/).

  2. Install Kueue.
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.16.5/manifests.yaml
         




## Set up your cluster with Jobset and Kueue

After you install JobSet and Kueue, take the following steps:

  1. Save the following manifest as a `kueue-config.yaml` file:

### A3 High
         
         apiVersion: kueue.x-k8s.io/v1beta2
           kind: Topology
           metadata:
             name: "gke-default"
           spec:
             levels:
             - nodeLabel: "cloud.google.com/gce-topology-block"
             - nodeLabel: "cloud.google.com/gce-topology-subblock"
             - nodeLabel: "cloud.google.com/gce-topology-host"
             - nodeLabel: "kubernetes.io/hostname"
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: ResourceFlavor
           metadata:
             name: a3-high-flavor
           spec:
             nodeLabels:
               cloud.google.com/gke-accelerator: nvidia-h100-80gb
             topologyName: "gke-default"
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: ResourceFlavor
           metadata:
             name: a3-high-dws-flavor
           spec:
             nodeLabels:
               cloud.google.com/gke-accelerator: nvidia-h100-80gb
             topologyName: "gke-default"
             tolerations:
             - key: "cloud.google.com/gke-queued"
               operator: "Exists"
               effect: NoSchedule
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: AdmissionCheck
           metadata:
             name: dws-prov
           spec:
             controllerName: kueue.x-k8s.io/provisioning-request
             parameters:
               apiGroup: kueue.x-k8s.io
               kind: ProvisioningRequestConfig
               name: dws-config
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: ProvisioningRequestConfig
           metadata:
             name: dws-config
           spec:
             provisioningClassName: queued-provisioning.gke.io
             podSetUpdates:
             - key: autoscaling.gke.io/provisioning-request
             valueFromProvisioningClassDetail: ResizeRequestName
             managedResources:
             - nvidia.com/gpu
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: ClusterQueue
           metadata:
             name: cq-tas
           spec:
             namespaceSelector: {}
             clusterQueueingStrategy: BestEffortFIFO
             resourceGroups:
             - flavors:
               - name: a3-high-flavor
                 resources:
                 - name: "cpu"
                   nominalQuota: 1000
                 - name: "memory"
                   nominalQuota: 1000Ti
                 - name: "nvidia.com/gpu"
                   nominalQuota: 1000
               - name: a3-high-dws-flavor
                 resources:
                 - name: "cpu"
                   nominalQuota: 1000
                 - name: "memory"
                   nominalQuota: 1000Ti
                 - name: "nvidia.com/gpu"
                   nominalQuota: 1000
             admissionChecksStrategy:
               admissionChecks:
               - name: "dws-prov"
                 onFlavors: [a3-high-dws-flavor]
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: LocalQueue
           metadata:
             namespace: default
             name: lq-tas
           spec:
             clusterQueue: cq-tas
         

### A3 Mega
         
         apiVersion: kueue.x-k8s.io/v1beta2
           kind: Topology
           metadata:
             name: "gke-default"
           spec:
             levels:
             - nodeLabel: "cloud.google.com/gce-topology-block"
             - nodeLabel: "cloud.google.com/gce-topology-subblock"
             - nodeLabel: "cloud.google.com/gce-topology-host"
             - nodeLabel: "kubernetes.io/hostname"
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: ResourceFlavor
           metadata:
             name: a3-mega-flavor
           spec:
             nodeLabels:
               cloud.google.com/gke-accelerator: nvidia-h100-mega-80gb
             topologyName: "gke-default"
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: ResourceFlavor
           metadata:
             name: a3-mega-dws-flavor
           spec:
             nodeLabels:
               cloud.google.com/gke-accelerator: nvidia-h100-mega-80gb
             topologyName: "gke-default"
             tolerations:
             - key: "cloud.google.com/gke-queued"
               operator: "Exists"
               effect: NoSchedule
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: AdmissionCheck
           metadata:
             name: dws-prov
           spec:
             controllerName: kueue.x-k8s.io/provisioning-request
             parameters:
               apiGroup: kueue.x-k8s.io
               kind: ProvisioningRequestConfig
               name: dws-config
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: ProvisioningRequestConfig
           metadata:
             name: dws-config
           spec:
             provisioningClassName: queued-provisioning.gke.io
             podSetUpdates:
             - key: autoscaling.gke.io/provisioning-request
             valueFromProvisioningClassDetail: ResizeRequestName
             managedResources:
             - nvidia.com/gpu
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: ClusterQueue
           metadata:
             name: cq-tas
           spec:
             namespaceSelector: {}
             clusterQueueingStrategy: BestEffortFIFO
             resourceGroups:
             - flavors:
               - name: a3-mega-flavor
                 resources:
                 - name: "cpu"
                   nominalQuota: 1000
                 - name: "memory"
                   nominalQuota: 1000Ti
                 - name: "nvidia.com/gpu"
                   nominalQuota: 1000
               - name: a3-mega-dws-flavor
                 resources:
                 - name: "cpu"
                   nominalQuota: 1000
                 - name: "memory"
                   nominalQuota: 1000Ti
                 - name: "nvidia.com/gpu"
                   nominalQuota: 1000
             admissionChecksStrategy:
               admissionChecks:
               - name: "dws-prov"
                 onFlavors: [a3-mega-dws-flavor]
           ---
           apiVersion: kueue.x-k8s.io/v1beta2
           kind: LocalQueue
           metadata:
             namespace: default
             name: lq-tas
           spec:
             clusterQueue: cq-tas
         

  2. Apply the manifest:
         
         kubectl apply -f kueue-config.yaml
         




When running workloads with Topology Aware Scheduling (TAS) enabled, you can specify how strictly topology constraints are enforced by using one of the following annotations in your workload manifest:

  * `kueue.x-k8s.io/podset-required-topology`: If you use this annotation, Kueue blocks scheduling until the workload can be scheduled within the requested topology constraint. Use this annotation to ensure that pods are placed together for optimal performance.

  * `kueue.x-k8s.io/podset-preferred-topology`: If you use this annotation, Kueue attempts to schedule pods within the requested topology constraint, but if that's not possible, it admits the workload without meeting topology constraints.


**Note:** Avoid using the required mode with **DWS Flex-start**. Because Flex-start provisions nodes dynamically, the resulting nodes might not satisfy strict topological requirements, which can result in unschedulable workloads. For these configurations, use `podset-preferred-topology` instead.

For either annotation, specify one of the following values as the topology constraint:

  * `cloud.google.com/gce-topology-block`: Schedules pods within the same network block.
  * `cloud.google.com/gce-topology-subblock`: Schedules pods within the same rack.
  * `cloud.google.com/gce-topology-host`: Schedules pods on the same physical host.



## Test on two Flex-start nodes

To run NCCL tests on a GKE cluster that uses A3 Mega or A3 High Flex-start VMs, use the following procedure. This procedure uses a [JobSet](https://jobset.sigs.k8s.io/) manifest to run an NCCL test on two nodes.

  1. Save the following manifest as a `nccl-tas-jobset.yaml` file:

### A3 High
         
         apiVersion: v1
           kind: ConfigMap
           metadata:
             name: nccl-config
                 data:
                   allgather.sh: |
                     #!/bin/bash
                     for script in /configs/*; do
                       name=$(basename $script)
                       cp $script "/scripts/$name"
                       chmod +x "/scripts/$name"
                     done
                     /scripts/init_ssh.sh ${@};
                     pushd /scripts;
                     /scripts/gen_hostfiles.sh ${@};
                     popd;
                     /scripts/run-allgather.sh 8 eth1,eth2,eth3,eth4 1M 512M ${#};
           ---
           apiVersion: jobset.x-k8s.io/v1alpha2
           kind: JobSet
           metadata:
             name: nccl-tas-test
             labels:
               kueue.x-k8s.io/queue-name: lq-tas
           spec:
             suspend: true
             network:
               enableDNSHostnames: true
             replicatedJobs:
             - name: worker
               replicas: 2
               template:
                 spec:
                   parallelism: 1
                   completions: 1
                   template:
                     metadata:
                       annotations:
                         kueue.x-k8s.io/podset-preferred-topology: "cloud.google.com/gce-topology-block"
                         networking.gke.io/default-interface: 'eth0'
                         networking.gke.io/interfaces: |
                                 [
                                   {"interfaceName":"eth0","network":"default"},
                                   {"interfaceName":"eth1","network":"vpc0"},
                                   {"interfaceName":"eth2","network":"vpc1"},
                                   {"interfaceName":"eth3","network":"vpc2"},
                                   {"interfaceName":"eth4","network":"vpc3"}
                                 ]
                     spec:
                       terminationGracePeriodSeconds: 0
                       nodeSelector:
                         cloud.google.com/gke-accelerator: nvidia-h100-80gb
                       tolerations:
                       - key: cloud.google.com/gke-queued
                         effect: NoSchedule
                         value: "true"
                       - key: "nvidia.com/gpu"
                         operator: "Exists"
                         effect: "NoSchedule"
                       setHostnameAsFQDN: true
                       containers:
                       - name: tcpx-daemon
                         image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpx/tcpgpudmarxd-dev:v2.0.11
                         command:
                           - /tcpgpudmarxd/build/app/tcpgpudmarxd
                           - --gpu_nic_preset
                           - a3vm
                           - --gpu_shmem_type
                           - fd
                           - --uds_path
                           - /run/tcpx
                           - --setup_param
                           - "--verbose 128 2 0 "
                         securityContext:
                           privileged: true
                           capabilities:
                             add:
                               - NET_ADMIN
                         volumeMounts:
                           - name: libraries
                             mountPath: /usr/local/nvidia/lib64
                           - name: tcpx-socket
                             mountPath: /run/tcpx
                           - name: sys
                             mountPath: /hostsysfs
                           - name: proc-sys
                             mountPath: /hostprocsysfs
                         env:
                           - name: LD_LIBRARY_PATH
                             value: /usr/local/nvidia/lib64
                       - name: nccl-test
                         image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpx/nccl-plugin-gpudirecttcpx-dev:v3.1.8
                         command:
                           - bash
                           - -c
                           - |
                             /scripts/container_entry.sh daemon;
                             sleep infinity;
                         securityContext:
                           privileged: true
                         volumeMounts:
                           - name: tcpx-socket
                             mountPath: /tmp
                           - name: libraries
                             mountPath: /usr/local/nvidia/lib64
                           - name: nccl-config
                             mountPath: /configs
                           - name: shared-memory
                             mountPath: /dev/shm
                         resources:
                           limits:
                             cpu: "200"
                             memory: "1800Gi"
                             nvidia.com/gpu: 8
                           requests:
                             cpu: "200"
                             memory: "1800Gi"
                             nvidia.com/gpu: 8
                       volumes:
                       - name: libraries
                         hostPath:
                           path: /home/kubernetes/bin/nvidia/lib64
                       - name: tcpx-socket
                         emptyDir: {}
                       - name: sys
                         hostPath:
                           path: /sys
                       - name: proc-sys
                         hostPath:
                           path: /proc/sys
                       - name: shared-memory
                         emptyDir:
                           medium: Memory
                           sizeLimit: 250Gi
                       - name: nccl-config
                         configMap:
                           name: nccl-config
                           defaultMode: 0777
         

### A3 Mega
         
         apiVersion: v1
           kind: ConfigMap
           metadata:
             name: nccl-configmap
                 data:
                   allgather.sh: |
                     #!/bin/bash
                     service ssh restart;
                     /scripts/init_ssh.sh ${@};
                     pushd /scripts;
                     /scripts/gen_hostfiles.sh ${@};
                     popd;
                     # Set up environment variables for GPUDirect-TCPXO
                     export LD_LIBRARY_PATH=/usr/local/nvidia/lib64
                     export NCCL_FASTRAK_CTRL_DEV=eth0
                     export NCCL_FASTRAK_IFNAME=eth1,eth2,eth3,eth4,eth5,eth6,eth7,eth8
                     export NCCL_SOCKET_IFNAME=eth0
                     export NCCL_CROSS_NIC=0
                     export NCCL_ALGO=Ring,Tree
                     export NCCL_PROTO=Simple
                     export NCCL_NET_GDR_LEVEL=PIX
                     # Run the benchmark
                     /scripts/demo-run-nccl-test-tcpxo-via-mpi.sh
           ---
           apiVersion: jobset.x-k8s.io/v1alpha2
           kind: JobSet
           metadata:
             name: nccl-tas-test
             labels:
               kueue.x-k8s.io/queue-name: lq-tas
           spec:
             ttlSecondsAfterFinished: 1200
             suspend: true
             network:
               enableDNSHostnames: true
             replicatedJobs:
               - name: worker
                 replicas: 2
                 template:
                   spec:
                     parallelism: 1
                     completions: 1
                     template:
                       metadata:
                         annotations:
                           kueue.x-k8s.io/podset-preferred-topology: "cloud.google.com/gce-topology-block"
                           networking.gke.io/default-interface: 'eth0'
                           networking.gke.io/interfaces: |
                             [
                               {"interfaceName":"eth0","network":"default"},
                               {"interfaceName":"eth1","network":"vpc0"},
                               {"interfaceName":"eth2","network":"vpc1"},
                               {"interfaceName":"eth3","network":"vpc2"},
                               {"interfaceName":"eth4","network":"vpc3"},
                               {"interfaceName":"eth5","network":"vpc4"},
                               {"interfaceName":"eth6","network":"vpc5"},
                               {"interfaceName":"eth7","network":"vpc6"},
                               {"interfaceName":"eth8","network":"vpc7"}
                             ]
                       spec:
                         activeDeadlineSeconds: 3600
                         restartPolicy: Never
                         nodeSelector:
                           cloud.google.com/gke-accelerator: nvidia-h100-mega-80gb
                         tolerations:
                         - key: cloud.google.com/gke-queued
                           effect: NoSchedule
                           value: "true"
                         - key: "nvidia.com/gpu"
                           operator: "Exists"
                           effect: "NoSchedule"
                         setHostnameAsFQDN: true
                         volumes:
                         - name: nvidia
                           hostPath:
                             path: /home/kubernetes/bin/nvidia
                         - name: lib64
                           hostPath:
                             path: /lib64
                         - name: proc
                           hostPath:
                             path: /proc
                         - name: shared-memory
                           emptyDir:
                             medium: "Memory"
                             sizeLimit: 250Gi
                         - name: nccl-config
                           configMap:
                             name: nccl-configmap
                             defaultMode: 0755
                         containers:
                         - name: nccl-test
                           image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/nccl-plugin-gpudirecttcpx-dev:v1.0.15
                           stdin: true
                           tty: true
                           securityContext:
                             privileged: true
                           env:
                           - name: LD_LIBRARY_PATH
                             value: /usr/local/nvidia/lib64
                           volumeMounts:
                           - name: nvidia
                             mountPath: /usr/local/nvidia
                           - name: shared-memory
                             mountPath: /dev/shm
                           - name: nccl-config
                             mountPath: /configs
                           resources:
                             limits:
                               cpu: "200"
                               memory: "3700Gi"
                               nvidia.com/gpu: 8
                             requests:
                               cpu: "200"
                               memory: "3700Gi"
                               nvidia.com/gpu: 8
                         - name: tcpxo-daemon
                           image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/tcpgpudmarxd-dev:v1.0.21
                           imagePullPolicy: Always
                           command: ["/bin/sh", "-c"]
                           args:
                             - |
                               set -ex
                               chmod 755 /fts/entrypoint_rxdm_container.sh
                               /fts/entrypoint_rxdm_container.sh --num_hops=2 --num_nics=8 --uid= --alsologtostderr
                           securityContext:
                             privileged: true
                             capabilities:
                               add:
                                 - NET_ADMIN
                                 - NET_BIND_SERVICE
                           volumeMounts:
                           - name: nvidia
                             mountPath: /usr/local/nvidia/lib64
                           - name: proc
                             mountPath: /proc
                           env:
                           - name: LD_LIBRARY_PATH
                             value: /usr/local/nvidia/lib64
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f nccl-tas-jobset.yaml
         

  3. Check that the JobSet is admitted and running:
         
         kubectl get jobset nccl-tas-test
         

Wait for the JobSet to be unsuspended and Pods to reach the `Running` status.

  4. Trigger the NCCL test by executing the `allgather.sh` script from the first worker Pod:
         
         kubectl exec --stdin --tty --container=nccl-test nccl-tas-test-worker-0-0 -- /configs/allgather.sh nccl-tas-test-worker-0-0 nccl-tas-test-worker-1-0
         

The output for a two-node test is similar to the following:

### A3 High
         
         #                                                              out-of-place                       in-place
           #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
           #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
               1048576         16384     float    none      -1    696.8    1.50    1.41      0    729.0    1.44    1.35      0
               ...
               536870912       8388608     float    none      -1   7101.7   75.60   70.87      0   7060.9   76.03   71.28      0
           # Out of bounds values : 0 OK
           # Avg bus bandwidth    : 29.8293
         

### A3 Mega
         
         #                                                              out-of-place                       in-place
           #        size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
           #         (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
               0                 0         float    none      -1     0.24    0.00    0.00      0     0.18    0.00    0.00      0
               ...
               8589934592     134217728    float    none      -1    42603  201.63  189.03      0    42670  201.31  188.73      0
           # Out of bounds values : 0 OK
           # Avg bus bandwidth    : 45.7587
         




## Deploy an NCCL test workload with TAS

If you have more than two nodes, we recommend using the following test, which uses (TAS). To run NCCL tests with TAS on a GKE cluster that uses A3 Mega or A3 High Flex-start VMs, use the following procedure.

  1. Save the following manifest as a `nccl-jobset-test.yaml` file. Replace `NUM_NODES` with the number of nodes in the node pool:

### A3 High
         
         apiVersion: jobset.x-k8s.io/v1alpha2
             kind: JobSet
             metadata:
               name: nccl-ag
               labels:
                 kueue.x-k8s.io/queue-name: lq-tas
             spec:
               ttlSecondsAfterFinished: 1200
               suspend: true
               network:
                 enableDNSHostnames: true
               replicatedJobs:
                 - name: worker
                   template:
                     spec:
                       parallelism: NUM_NODES
                       completions: NUM_NODES
                       template:
                         metadata:
                           annotations:
                             kueue.x-k8s.io/podset-preferred-topology: "cloud.google.com/gce-topology-subblock"
                             networking.gke.io/default-interface: 'eth0'
                             networking.gke.io/interfaces: |
                                 [
                                   {"interfaceName":"eth0","network":"default"},
                                   {"interfaceName":"eth1","network":"vpc0"},
                                   {"interfaceName":"eth2","network":"vpc1"},
                                   {"interfaceName":"eth3","network":"vpc2"},
                                   {"interfaceName":"eth4","network":"vpc3"}
                                 ]
                         spec:
                           activeDeadlineSeconds: 3600
                           restartPolicy: Never
                           nodeSelector:
                             cloud.google.com/gke-accelerator: nvidia-h100-80gb
                           tolerations:
                           - key: cloud.google.com/gke-queued
                             operator: "Exists"
                             effect: NoSchedule
                           - key: "nvidia.com/gpu"
                             operator: "Exists"
                             effect: "NoSchedule"
                           setHostnameAsFQDN: true
                           volumes:
                           - name: proc
                             hostPath:
                               path: /proc
                           - name: nvidia
                             hostPath:
                               path: /home/kubernetes/bin/nvidia
                           - name: libraries
                             hostPath:
                               path: /home/kubernetes/bin/nvidia/lib64
                           - name: tcpx-socket
                             emptyDir: {}
                           - name: shared-memory
                             emptyDir:
                               medium: "Memory"
                               sizeLimit: 250Gi
                           containers:
                           - name: tcpx-daemon
                             image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpx/tcpgpudmarxd-dev:v2.0.11
                             command:
                               - /tcpgpudmarxd/build/app/tcpgpudmarxd
                               - --gpu_nic_preset
                               - a3vm
                               - --gpu_shmem_type
                               - fd
                               - --uds_path
                               - /run/tcpx
                               - --setup_param
                               - "--verbose 128 2 0 "
                             securityContext:
                               privileged: true
                             volumeMounts:
                               - name: tcpx-socket
                                 mountPath: /run/tcpx
                               - name: libraries
                                 mountPath: /usr/local/nvidia/lib64
                           - name: nccl-test
                             stdin: true
                             tty: true
                             image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpx/nccl-plugin-gpudirecttcpx-dev:v3.1.8
                             securityContext:
                               privileged: true
                             env:
                             - name: MY_NODE_NAME
                               valueFrom:
                                 fieldRef:
                                   fieldPath: spec.nodeName
                             - name: OMPI_ALLOW_RUN_AS_ROOT
                               value: "1"
                             - name: OMPI_ALLOW_RUN_AS_ROOT_CONFIRM
                               value: "1"
                             - name: N_NODES
                               value: "NUM_NODES"
                             - name: LD_LIBRARY_PATH
                               value: /usr/local/nvidia/lib64
                             command:
                             - bash
                             - -c
                             - |
                               /scripts/container_entry.sh daemon &
                               export POSTFIX=$(hostname | cut -d . -f 2-)
                               export WORKERS_BASENAME=$(hostname | cut -d . -f 1 | rev | cut -d - -f 2- | rev )
                               export NODE_RANK=$JOB_COMPLETION_INDEX
                               for i in `seq 0 $(($N_NODES-1))`; do
                                 OTHER=${WORKERS_BASENAME}-${i}.${POSTFIX}
                                 until ssh -p 222 -o StrictHostKeyChecking=no $OTHER hostname; do
                                   sleep 10
                                 done
                                 echo ${OTHER} port=222 slots=8 | tee -a /tmp/hostfile;
                               done
                               if [[ "${NODE_RANK}" -eq "0" ]]; then
                                   /scripts/run-allgather.sh 8 eth1,eth2,eth3,eth4 1M 512M ${N_NODES}
                               else
                                   while ping -c 1 ${WORKERS_BASENAME}-0.${POSTFIX}; do
                                   sleep 5
                               done
                               fi
                               exit 0
                             volumeMounts:
                             - name: nvidia
                               mountPath: /usr/local/nvidia
                             - name: tcpx-socket
                               mountPath: /tmp
                             - name: libraries
                               mountPath: /usr/local/nvidia/lib64
                             - name: shared-memory
                               mountPath: /dev/shm
                             resources:
                               limits:
                                 cpu: "200"
                                 memory: "1800Gi"
                                 nvidia.com/gpu: 8
                               requests:
                                 cpu: "200"
                                 memory: "1800Gi"
                                 nvidia.com/gpu: 8
         

### A3 Mega
         
         apiVersion: jobset.x-k8s.io/v1alpha2
             kind: JobSet
             metadata:
               name: nccl-ag
               labels:
                 kueue.x-k8s.io/queue-name: lq-tas
             spec:
               ttlSecondsAfterFinished: 1200
               suspend: true
               network:
                 enableDNSHostnames: true
               replicatedJobs:
                 - name: worker
                   template:
                     spec:
                       parallelism: NUM_NODES
                       completions: NUM_NODES
                       template:
                         metadata:
                           annotations:
                             kueue.x-k8s.io/podset-preferred-topology: "cloud.google.com/gce-topology-subblock"
                             networking.gke.io/default-interface: 'eth0'
                             networking.gke.io/interfaces: |
                               [
                                 {"interfaceName":"eth0","network":"default"},
                                 {"interfaceName":"eth1","network":"vpc0"},
                                 {"interfaceName":"eth2","network":"vpc1"},
                                 {"interfaceName":"eth3","network":"vpc2"},
                                 {"interfaceName":"eth4","network":"vpc3"},
                                 {"interfaceName":"eth5","network":"vpc4"},
                                 {"interfaceName":"eth6","network":"vpc5"},
                                 {"interfaceName":"eth7","network":"vpc6"},
                                 {"interfaceName":"eth8","network":"vpc7"}
                               ]
                         spec:
                           activeDeadlineSeconds: 3600
                           restartPolicy: Never
                           nodeSelector:
                             cloud.google.com/gke-accelerator: nvidia-h100-mega-80gb
                           tolerations:
                           - key: cloud.google.com/gke-queued
                             operator: "Exists"
                             effect: NoSchedule
                           - key: "nvidia.com/gpu"
                             operator: "Exists"
                             effect: "NoSchedule"
                           setHostnameAsFQDN: true
                           volumes:
                           - name: proc
                             hostPath:
                               path: /proc
                           - name: nvidia
                             hostPath:
                               path: /home/kubernetes/bin/nvidia
                           - name: lib64
                             hostPath:
                               path: /lib64
                           - name: shared-memory
                             emptyDir:
                               medium: "Memory"
                               sizeLimit: 250Gi
                           containers:
                           - name: nccl-test
                             stdin: true
                             tty: true
                             image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/nccl-plugin-tcpxo-diagnostic:v1.0.6
                             securityContext:
                               privileged: true
                             env:
                             - name: MY_NODE_NAME
                               valueFrom:
                                 fieldRef:
                                   fieldPath: spec.nodeName
                             - name: OMPI_ALLOW_RUN_AS_ROOT
                               value: "1"
                             - name: OMPI_ALLOW_RUN_AS_ROOT_CONFIRM
                               value: "1"
                             - name: N_NODES
                               value: "NUM_NODES"
                             - name: NCCL_SOCKET_IFNAME
                               value: eth0
                             - name: NCCL_FASTRAK_CTRL_DEV
                               value: eth0
                             - name: NCCL_FASTRAK_IFNAME
                               value: eth1,eth2,eth3,eth4,eth5,eth6,eth7,eth8
                             - name: NCCL_CROSS_NIC
                               value: "0"
                             - name: NCCL_ALGO
                               value: Ring,Tree
                             - name: NCCL_PROTO
                               value: Simple
                             - name: NCCL_NET_GDR_LEVEL
                               value: PIX
                             - name: LD_LIBRARY_PATH
                               value: /usr/local/nvidia/lib64
                             command:
                             - bash
                             - -c
                             - |
                               set -x
                               /scripts/container_entry.sh daemon &
                               export POSTFIX=$(hostname | cut -d . -f 2-)
                               export WORKERS_BASENAME=$(hostname | cut -d . -f 1 | rev | cut -d - -f 2- | rev )
                               export NODE_RANK=$JOB_COMPLETION_INDEX
                               for i in `seq 0 $(($N_NODES-1))`; do
                                 OTHER=${WORKERS_BASENAME}-${i}.${POSTFIX}
                                 until ssh -p 222 -o StrictHostKeyChecking=no $OTHER hostname; do
                                   sleep 10
                                 done
                                 echo ${OTHER} port=222 slots=8 | tee -a /tmp/hostfile;
                               done
                               if [[ "${NODE_RANK}" -eq "0" ]]; then
                                   export NCCL_TESTS_SPLIT_MASK="0x0";
                                   ENV_VARS=$(echo ${!NCCL*} ${!OMPI*} LD_LIBRARY_PATH PATH | sed 's/ / -x /g')
                                   mpirun --hostfile /tmp/hostfile \
                                     -x $ENV_VARS  \
                                     -mca plm_rsh_no_tree_spawn 1 \
                                     --mca orte_keep_fqdn_hostnames 1 \
                                     --mca btl self,tcp \
                                     --mca btl_tcp_if_include eth0 \
                                     --bind-to none \
                                     --mca plm_rsh_agent "ssh -q -o LogLevel=ERROR -o StrictHostKeyChecking=no -p 222" \
                                     /third_party/nccl-tests/build/all_gather_perf -b 1K -e 8G -f 2 -g 1 -w 5 --iters 100 -c 1
                               else
                                   while ping -c 1 ${WORKERS_BASENAME}-0.${POSTFIX}; do
                                   sleep 5
                               done
                               fi
                               exit 0
                             volumeMounts:
                             - name: nvidia
                               mountPath: /usr/local/nvidia
                             - name: lib64
                               mountPath: /lib64
                             - name: shared-memory
                               mountPath: /dev/shm
                             resources:
                               limits:
                                 cpu: "200"
                                 memory: "3700Gi"
                                 nvidia.com/gpu: 8
                               requests:
                                 cpu: "200"
                                 memory: "3700Gi"
                                 nvidia.com/gpu: 8
                           - name: tcpxo-daemon
                             image: us-docker.pkg.dev/gce-ai-infra/gpudirect-tcpxo/tcpxo-daemon:v1.0.1
                             imagePullPolicy: Always
                             command:
                             - bash
                             - -c
                             - |
                               /usr/bin/tcpxo_daemon
                             securityContext:
                               privileged: true
                             volumeMounts:
                             - name: nvidia
                               mountPath: /usr/local/nvidia
                             - name: proc
                               mountPath: /proc
                             env:
                             - name: LD_LIBRARY_PATH
                               value: /usr/local/nvidia/lib64
         

  2. Apply the manifest:
         
         kubectl apply -f nccl-jobset-test.yaml
         

  3. Check that the workload is admitted and reaches the `Completed` state.

  4. Fetch logs for the Pod matching `nccl-ag-worker-0-0-.*` to see the results:
         
         kubectl logs $(kubectl get pods -o go-template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' | grep nccl-ag-worker-0-0)
         




## What's next

  * [Collect and Understand NCCL Logs for Troubleshooting](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand) to understand the test outputs and troubleshoot issues.
  * Learn about [troubleshooting slow performance](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
