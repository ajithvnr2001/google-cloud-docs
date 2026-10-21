---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x-max/
title: Run NCCL on GKE clusters that use A4X Max \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:05.972127+00:00
---

# Run NCCL on GKE clusters that use A4X Max  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x-max/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run NCCL on GKE clusters that use A4X Max Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes how to run [NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview) tests on provisioned clusters that use GPUDirect RDMA. Depending on your use case, use one of the following options:

  * If you have two nodes to test, run a basic test.
  * If you have more than two nodes to test, run the test with JobSet.



### Test on two nodes

The following test runs a NCCL workload across two nodes. Understand the following about this test:

  * By default, GKE schedules the two Pods to separate node pools, if available. If node pools are created with distinct NVLink domains, then this test represents cross-domain RDMA throughput. To schedule Pods on the same domain, modify the Pod affinity to schedule on the same node pool.



Run the two-node test:

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=COMPUTE_REGION
         

Replace the following variables:

     * `CLUSTER_NAME`: the name of your cluster, which, for the clusters created with Cluster Toolkit, is based on the `DEPLOYMENT_NAME`.
     * `COMPUTE_REGION`: the name of the compute region.
  2. Deploy a NCCL test workload of two test Pods that are running on two A4X Max nodes:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-rdma/nccl-test-a4x-max.yaml
         

  3. Check that the Pods are both running on some nodes:
         
         kubectl get pods nccl-test-host-1 nccl-test-host-2
         

If the two Pods show a `Running` status, you can proceed to the next step.

  4. Trigger an all-gather test for the A4X Max nodes:
         
         HOSTS="nccl-host-1 nccl-host-2"
         kubectl exec nccl-test-host-1 -it -- bash -c "/usr/local/gib/scripts/run_nccl_tests.sh -t all_gather -b 1M -e 16G ${HOSTS}"
         

The output is similar to the following:
         
         # nccl-tests version 2.17.6 nccl-headers=22809 nccl-library=22809
         # Collective test starting: all_gather_perf
         # nThread 1 nGpus 1 minBytes 4096 maxBytes 17179869184 step: 2(factor) warmup iters: 1 iters: 20 agg iters: 1 validation: 1 graph: 0
         #
         # Using devices
         #  Rank  0 Group  0 Pid    299 on gke-psch-ug-cluster-a4xmax-2-1391c2ef-m9bm device  0 [0008:06:00] NVIDIA GB300
         #  Rank  1 Group  0 Pid    300 on gke-psch-ug-cluster-a4xmax-2-1391c2ef-m9bm device  1 [0009:06:00] NVIDIA GB300
         #  Rank  2 Group  0 Pid    301 on gke-psch-ug-cluster-a4xmax-2-1391c2ef-m9bm device  2 [0018:06:00] NVIDIA GB300
         #  Rank  3 Group  0 Pid    302 on gke-psch-ug-cluster-a4xmax-2-1391c2ef-m9bm device  3 [0019:06:00] NVIDIA GB300
         #  Rank  4 Group  0 Pid    237 on gke-psch-ug-cluster-a4xmax-03878a77-d3lp device  0 [0008:06:00] NVIDIA GB300
         #  Rank  5 Group  0 Pid    238 on gke-psch-ug-cluster-a4xmax-03878a77-d3lp device  1 [0009:06:00] NVIDIA GB300
         #  Rank  6 Group  0 Pid    239 on gke-psch-ug-cluster-a4xmax-03878a77-d3lp device  2 [0018:06:00] NVIDIA GB300
         #  Rank  7 Group  0 Pid    240 on gke-psch-ug-cluster-a4xmax-03878a77-d3lp device  3 [0019:06:00] NVIDIA GB300
         #
         #                                                              out-of-place                       in-place
         #       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong
         #        (B)    (elements)                               (us)  (GB/s)  (GB/s)             (us)  (GB/s)  (GB/s)
                 4096           128     float    none      -1    28.51    0.14    0.13       0    27.71    0.15    0.13       0
                 8192           256     float    none      -1    28.10    0.29    0.26       0    28.40    0.29    0.25       0
                16384           512     float    none      -1    28.55    0.57    0.50       0    28.19    0.58    0.51       0
                32768          1024     float    none      -1    30.56    1.07    0.94       0    29.65    1.11    0.97       0
                65536          2048     float    none      -1    33.30    1.97    1.72       0    33.14    1.98    1.73       0
               131072          4096     float    none      -1    36.18    3.62    3.17       0    36.14    3.63    3.17       0
               262144          8192     float    none      -1    38.50    6.81    5.96       0    94.91    2.76    2.42       0
               524288         16384     float    none      -1   152.25    3.44    3.01       0    54.79    9.57    8.37       0
              1048576         32768     float    none      -1    63.82   16.43   14.38       0    64.06   16.37   14.32       0
              2097152         65536     float    none      -1    65.10   32.21   28.19       0    66.13   31.71   27.75       0
              4194304        131072     float    none      -1    67.73   61.92   54.18       0    67.16   62.45   54.65       0
              8388608        262144     float    none      -1    79.65  105.31   92.15       0    80.02  104.83   91.73       0
             16777216        524288     float    none      -1   189.74   88.42   77.37       0   187.57   89.44   78.26       0
             33554432       1048576     float    none      -1   252.85  132.70  116.11       0   202.31  165.86  145.13       0
             67108864       2097152     float    none      -1   250.55  267.85  234.37       0   276.11  243.06  212.67       0
            134217728       4194304     float    none      -1   394.38  340.33  297.79       0   487.60  275.26  240.85       0
            268435456       8388608     float    none      -1   717.97  373.88  327.15       0   799.98  335.55  293.61       0
            536870912      16777216     float    none      -1  1421.29  377.73  330.52       0  1392.81  385.46  337.28       0
           1073741824      33554432     float    none      -1  2783.37  385.77  337.55       0  2596.97  413.46  361.78       0
           2147483648      67108864     float    none      -1  5396.10  397.97  348.22       0  5059.01  424.49  371.43       0
           4294967296     134217728     float    none      -1  10579.7  405.96  355.22       0  9918.44  433.03  378.90       0
           8589934592     268435456     float    none      -1  21012.9  408.79  357.69       0  20043.4  428.57  375.00       0
          17179869184     536870912     float    none      -1  42091.7  408.15  357.13       0  40243.2  426.90  373.54       0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 146.047
         #
         # Collective test concluded: all_gather_perf
         

If Pods are scheduled on nodes in distinct NVLink domains, this test represents cross-domain RDMA throughput, as shown in the provided output. To spread across to node pools created in distinct NVLink domains, modify the Pod spec affinity in `nccl-test-a4x-max.yaml` with the following:
         
         spec:
         ...
         affinity:
         podAntiAffinity:
           preferredDuringSchedulingIgnoredDuringExecution:
           - weight: 100
             podAffinityTerm:
               labelSelector:
                 matchLabels:
                   app: nccl-test
               topologyKey: cloud.google.com/gke-nodepool
         




## Test using JobSet

  1. Install JobSet:
         
         VERSION=v0.10.1
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/$VERSION/manifests.yaml
         

  2. Make sure that your non-GPU node pools have enough resources to schedule the JobSet controllers. Follow the step to [define your own resource adjustments](https://jobset.sigs.k8s.io/docs/installation/#step-4-define-your-resource-adjustments).

For more information about JobSet installation, see [Installation](https://jobset.sigs.k8s.io/docs/installation/).

  3. Run the following commands, replacing `NUM_NODES` with the number of nodes that you want to run the NCCL test with:
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/refs/heads/master/gpudirect-rdma/nccl-test-a4x-max-jobset.yaml
         
         NUM_NODES=2
         sed "s|__NUM_NODES__|NUM_NODES|" nccl-test-a4x-max-jobset.yaml | kubectl apply -f -
         

  4. Check that all Pods are in the `Completed` state:
         
         kubectl get pods | grep allgather-worker
         

The output is similar to the following:
         
         allgather-worker-0-0-g45d2   0/1     Completed   0          13m
         allgather-worker-0-1-prpvw   0/1     Completed   0          13m
         allgather-worker-0-2-qbwt5   0/1     Completed   0          13m
         

  5. See the test result from the head Pod (`nccl-test-nccl-test-0`) from where the test is launched:
         
         kubectl logs $(kubectl get pods -o go-template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' | grep allgather-worker-0-0)

The output is similar to the following:
         
         # nccl-tests version 2.17.6 nccl-headers=22809 nccl-library=22809
         # Collective test starting: all_gather_perf
         # nThread 1 nGpus 1 minBytes 1024 maxBytes 8589934592 step: 2(factor) warmup iters: 5 iters: 100 agg iters: 1 validation: 1 graph: 0
         #
         ...
         #                                                            out-of-place                       in-place
         #       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong
         #        (B)    (elements)                               (us)  (GB/s)  (GB/s)             (us)  (GB/s)  (GB/s)
                 1024            32     float    none      -1    45.49    0.02    0.02       0    45.29    0.02    0.02       0
                 2048            64     float    none      -1    45.52    0.04    0.04       0    45.37    0.05    0.04       0
                 4096           128     float    none      -1    46.02    0.09    0.08       0    45.83    0.09    0.08       0
                 8192           256     float    none      -1    63.93    0.13    0.11       0    46.98    0.17    0.15       0
                16384           512     float    none      -1    46.51    0.35    0.31       0    47.11    0.35    0.30       0
                32768          1024     float    none      -1    66.32    0.49    0.43       0    50.73    0.65    0.57       0
                65536          2048     float    none      -1    49.89    1.31    1.15       0    50.04    1.31    1.15       0
               131072          4096     float    none      -1    54.68    2.40    2.10       0    52.38    2.50    2.19       0
               262144          8192     float    none      -1    54.66    4.80    4.20       0    54.06    4.85    4.24       0
               524288         16384     float    none      -1    66.28    7.91    6.92       0    65.75    7.97    6.98       0
              1048576         32768     float    none      -1    85.63   12.25   10.72       0    86.44   12.13   10.61       0
              2097152         65536     float    none      -1    68.33   30.69   26.86       0    72.32   29.00   25.37       0
              4194304        131072     float    none      -1    71.85   58.37   51.08       0    71.58   58.60   51.28       0
              8388608        262144     float    none      -1    83.80  100.10   87.59       0    85.73   97.85   85.62       0
             16777216        524288     float    none      -1   195.94   85.62   74.92       0   195.86   85.66   74.95       0
             33554432       1048576     float    none      -1   240.84  139.32  121.91       0   210.82  159.16  139.27       0
             67108864       2097152     float    none      -1   254.95  263.22  230.32       0   250.93  267.44  234.01       0
            134217728       4194304     float    none      -1   411.09  326.49  285.68       0   386.11  347.61  304.16       0
            268435456       8388608     float    none      -1   741.69  361.92  316.68       0   722.42  371.58  325.13       0
            536870912      16777216     float    none      -1  1358.44  395.21  345.81       0  1343.63  399.57  349.62       0
           1073741824      33554432     float    none      -1  2679.62  400.71  350.62       0  2585.68  415.26  363.36       0
           2147483648      67108864     float    none      -1  5281.54  406.60  355.78       0  5074.73  423.17  370.28       0
           4294967296     134217728     float    none      -1  10476.2  409.97  358.73       0  10027.5  428.32  374.78       0
           8589934592     268435456     float    none      -1  20853.9  411.91  360.42       0  20194.7  425.36  372.19       0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 126.85
         #
         # Collective test concluded: all_gather_perf
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
