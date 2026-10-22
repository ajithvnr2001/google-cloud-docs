---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke/
title: Run NCCL on GKE clusters that use Cluster Toolkit \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:40.200007+00:00
---

# Run NCCL on GKE clusters that use Cluster Toolkit  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run NCCL on GKE clusters that use Cluster Toolkit Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes how to run [NCCL](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview) tests on GKE clusters created by using Cluster Toolkit. If you created your cluster by using `gcloud` commands, the instructions in this document might not apply. Instead, see one of the following documents:

  * [Run NCCL on GKE clusters that use A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x)
  * [Run NCCL on GKE clusters that use A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom)



Choose the steps for your machine type:

### A4X

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=COMPUTE_REGION
         

Replace the following variables:

     * `CLUSTER_NAME`: the name of your cluster, which, for the clusters created with Cluster Toolkit, is based on the `DEPLOYMENT_NAME`.
     * `COMPUTE_REGION`: the name of the compute region.
  2. Deploy an all-gather NCCL performance test with TAS enabled by using the [gke-a4x/nccl-jobset-example.yaml](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4x/nccl-jobset-example.yaml) file:

     1. The test uses a certain number of nodes by default. If you want to change the number of nodes, modify the YAML file to change the following values to your required number of nodes:

        * `numNodes`
        * `parallelism`
        * `completions`
        * `N_NODES`
     2. Create the resources to run the test:
            
            kubectl create -f ~/cluster-toolkit/examples/gke-a4x/nccl-jobset-example.yaml
            

  3. Confirm that all `nccl-test` Pods have reached the `Completed` state:
         
         kubectl get pods
         

The output should be similar to the following:
         
         nccl-all-worker-0-0-ft8jm   0/1     Completed   0          13m
         nccl-all-worker-0-1-prpvw   0/1     Completed   0          13m
         

  4. Find a Pod name matching the pattern `nccl-all-worker-0-0-*`. The logs of this Pod contain the results of the NCCL test.

To fetch the logs for this Pod, run the following command:
         
         
         kubectl logs $(kubectl get pods -o go-template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}' | grep nccl-all-worker-0-0) 

The output should be similar to the following:
         
         #                                                              out-of-place                       in-place
         #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
                 1024            32     float    none      -1    19.60    0.05    0.05      0    19.00    0.05    0.05      0
                 2048            64     float    none      -1    19.63    0.10    0.09      0    19.47    0.11    0.09      0
                 4096           128     float    none      -1    19.88    0.21    0.18      0    19.61    0.21    0.18      0
                 8192           256     float    none      -1    20.31    0.40    0.35      0    19.82    0.41    0.36      0
                16384           512     float    none      -1    20.30    0.81    0.71      0    20.17    0.81    0.71      0
                32768          1024     float    none      -1    20.70    1.58    1.39      0    20.36    1.61    1.41      0
                65536          2048     float    none      -1    20.94    3.13    2.74      0    20.88    3.14    2.75      0
               131072          4096     float    none      -1    21.12    6.20    5.43      0    20.96    6.25    5.47      0
               262144          8192     float    none      -1    21.24   12.34   10.80      0    21.01   12.48   10.92      0
               524288         16384     float    none      -1    21.28   24.63   21.55      0    21.07   24.88   21.77      0
              1048576         32768     float    none      -1    21.95   47.77   41.80      0    21.72   48.28   42.24      0
              2097152         65536     float    none      -1    24.15   86.85   76.00      0    23.75   88.30   77.26      0
              4194304        131072     float    none      -1    31.50  133.13  116.49      0    30.75  136.39  119.34      0
              8388608        262144     float    none      -1    47.42  176.88  154.77      0    46.47  180.51  157.95      0
             16777216        524288     float    none      -1    48.72  344.39  301.34      0    47.85  350.63  306.80      0
             33554432       1048576     float    none      -1    75.08  446.91  391.05      0    73.89  454.10  397.34      0
             67108864       2097152     float    none      -1    178.7  375.47  328.53      0    179.1  374.67  327.84      0
            134217728       4194304     float    none      -1    211.1  635.86  556.37      0    211.3  635.21  555.81      0
            268435456       8388608     float    none      -1    413.2  649.68  568.47      0    414.9  646.95  566.08      0
            536870912      16777216     float    none      -1    820.1  654.64  572.81      0    814.9  658.81  576.46      0
           1073741824      33554432     float    none      -1   1566.5  685.43  599.76      0   1567.9  684.82  599.22      0
           2147483648      67108864     float    none      -1   3025.3  709.83  621.10      0   3017.2  711.74  622.77      0
           4294967296     134217728     float    none      -1   5898.8  728.11  637.10      0   5784.0  742.57  649.74      0
           8589934592     268435456     float    none      -1    11541  744.31  651.28      0    11293  760.67  665.58      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 236.839
         




### A4

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=COMPUTE_REGION
         

Replace the following variables:

     * `CLUSTER_NAME`: the name of your cluster, which, for the clusters created with Cluster Toolkit, is based on the `DEPLOYMENT_NAME`.
     * `COMPUTE_REGION`: the name of the compute region.
  2. Deploy an all-gather NCCL performance test with TAS enabled by using the [gke-a4/nccl-jobset-example.yaml](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/nccl-jobset-example.yaml) file:

     1. Modify the YAML file in the following ways if you meet the conditions:

        * The tests use a certain number of nodes by default. If you want to change the number of nodes, change the following values to your required number of nodes:

          * `parallelism`
          * `completions`
          * `N_NODES`
        * If you want to test nodes provisioned by flex-start, in the `metadata` field, do the following:

          * Replace the `kueue.x-k8s.io/queue-name` value with `dws-local-queue`.
          * Add the following annotation:
                
                annotations:
                    provreq.kueue.x-k8s.io/maxRunDurationSeconds: "600"
                

     2. Create the resources to run the test:
            
            kubectl create -f ~/cluster-toolkit/examples/gke-a4/nccl-jobset-example.yaml
            

This command returns a JobSet name.

The output should be similar to the following:
            
            jobset.jobset.x-k8s.io/all-gather8t7dt created
            

  3. To view the results of the NCCL test, run the following command to view all of the running Pods:
         
         kubectl get pods
         

The output should be similar to the following:
         
         NAME                          READY   STATUS      RESTARTS   AGE
         all-gather8t7dt-w-0-0-n9s6j   0/1     Completed   0          9m34s
         all-gather8t7dt-w-0-1-rsf7r   0/1     Completed   0          9m34s
         

  4. Find a Pod name matching the pattern `jobset-name-w-0-0-*`. The logs of this Pod contain the results of the NCCL test.

To fetch the logs for this Pod, run the following command:
         
         kubectl logs all-gather8t7dt-w-0-0-n9s6j
         

The output should be similar to the following:
         
         #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
                 1024            16     float    none      -1    54.07    0.02    0.02      0    55.80    0.02    0.02      0
                 2048            32     float    none      -1    55.46    0.04    0.03      0    55.31    0.04    0.03      0
                 4096            64     float    none      -1    55.59    0.07    0.07      0    55.38    0.07    0.07      0
                 8192           128     float    none      -1    56.05    0.15    0.14      0    55.92    0.15    0.14      0
                16384           256     float    none      -1    57.08    0.29    0.27      0    57.75    0.28    0.27      0
                32768           512     float    none      -1    57.49    0.57    0.53      0    57.22    0.57    0.54      0
                65536          1024     float    none      -1    59.20    1.11    1.04      0    59.20    1.11    1.04      0
               131072          2048     float    none      -1    59.58    2.20    2.06      0    63.57    2.06    1.93      0
               262144          4096     float    none      -1    63.87    4.10    3.85      0    63.61    4.12    3.86      0
               524288          8192     float    none      -1    64.83    8.09    7.58      0    64.40    8.14    7.63      0
              1048576         16384     float    none      -1    79.74   13.15   12.33      0    76.66   13.68   12.82      0
              2097152         32768     float    none      -1    78.41   26.74   25.07      0    79.05   26.53   24.87      0
              4194304         65536     float    none      -1    83.21   50.41   47.26      0    81.25   51.62   48.39      0
              8388608        131072     float    none      -1    94.35   88.91   83.35      0    99.07   84.68   79.38      0
             16777216        262144     float    none      -1    122.9  136.55  128.02      0    121.7  137.83  129.21      0
             33554432        524288     float    none      -1    184.2  182.19  170.80      0    178.1  188.38  176.60      0
             67108864       1048576     float    none      -1    294.7  227.75  213.51      0    277.7  241.62  226.52      0
            134217728       2097152     float    none      -1    495.4  270.94  254.00      0    488.8  274.60  257.43      0
            268435456       4194304     float    none      -1    877.5  305.92  286.80      0    861.3  311.65  292.17      0
            536870912       8388608     float    none      -1   1589.8  337.71  316.60      0   1576.2  340.61  319.33      0
           1073741824      16777216     float    none      -1   3105.7  345.74  324.13      0   3069.2  349.85  327.98      0
           2147483648      33554432     float    none      -1   6161.7  348.52  326.74      0   6070.7  353.75  331.64      0
           4294967296      67108864     float    none      -1    12305  349.03  327.22      0    12053  356.35  334.08      0
           8589934592     134217728     float    none      -1    24489  350.77  328.85      0    23991  358.05  335.67      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 120.248
         




### A3 Ultra

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=COMPUTE_REGION
         

Replace the following variables:

     * `CLUSTER_NAME`: the name of your cluster, which, for the clusters created with Cluster Toolkit, is based on the `DEPLOYMENT_NAME`.
     * `COMPUTE_REGION`: the name of the compute region.
  2. Deploy an all-gather NCCL performance test with TAS enabled by using the [gke-a3-ultragpu/nccl-jobset-example.yaml](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a3-ultragpu/nccl-jobset-example.yaml) file:

     1. Modify the YAML file in the following ways if you meet the conditions:

        * The tests use a certain number of nodes by default. If you want to change the number of nodes, change the following values to your required number of nodes:

          * `parallelism`
          * `completions`
          * `N_NODES`
        * If you want to test nodes provisioned by flex-start, in the `metadata` field, do the following:

          * Replace the `kueue.x-k8s.io/queue-name` value with `dws-local-queue`.
          * Add the following annotation:
                
                annotations:
                    provreq.kueue.x-k8s.io/maxRunDurationSeconds: "600"
                

     2. Create the resources to run the test:
            
            kubectl create -f ~/cluster-toolkit/examples/gke-a3-ultragpu/nccl-jobset-example.yaml
            

This command returns a JobSet name.

The output should be similar to the following:
            
            jobset.jobset.x-k8s.io/all-gather8t7dt created
            

  3. To view the results of the NCCL test, run the following command to view all of the running Pods:
         
         kubectl get pods
         

The output should be similar to the following:
         
         NAME                          READY   STATUS      RESTARTS   AGE
         all-gather8t7dt-w-0-0-n9s6j   0/1     Completed   0          9m34s
         all-gather8t7dt-w-0-1-rsf7r   0/1     Completed   0          9m34s
         

  4. Find a Pod name matching the pattern `jobset-name-w-0-0-*`. The logs of this Pod contain the results of the NCCL test.

To fetch the logs for this Pod, run the following command:
         
         kubectl logs all-gather8t7dt-w-0-0-n9s6j
         

The output should be similar to the following:
         
         #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
                 1024            16     float    none      -1    54.07    0.02    0.02      0    55.80    0.02    0.02      0
                 2048            32     float    none      -1    55.46    0.04    0.03      0    55.31    0.04    0.03      0
                 4096            64     float    none      -1    55.59    0.07    0.07      0    55.38    0.07    0.07      0
                 8192           128     float    none      -1    56.05    0.15    0.14      0    55.92    0.15    0.14      0
                16384           256     float    none      -1    57.08    0.29    0.27      0    57.75    0.28    0.27      0
                32768           512     float    none      -1    57.49    0.57    0.53      0    57.22    0.57    0.54      0
                65536          1024     float    none      -1    59.20    1.11    1.04      0    59.20    1.11    1.04      0
               131072          2048     float    none      -1    59.58    2.20    2.06      0    63.57    2.06    1.93      0
               262144          4096     float    none      -1    63.87    4.10    3.85      0    63.61    4.12    3.86      0
               524288          8192     float    none      -1    64.83    8.09    7.58      0    64.40    8.14    7.63      0
              1048576         16384     float    none      -1    79.74   13.15   12.33      0    76.66   13.68   12.82      0
              2097152         32768     float    none      -1    78.41   26.74   25.07      0    79.05   26.53   24.87      0
              4194304         65536     float    none      -1    83.21   50.41   47.26      0    81.25   51.62   48.39      0
              8388608        131072     float    none      -1    94.35   88.91   83.35      0    99.07   84.68   79.38      0
             16777216        262144     float    none      -1    122.9  136.55  128.02      0    121.7  137.83  129.21      0
             33554432        524288     float    none      -1    184.2  182.19  170.80      0    178.1  188.38  176.60      0
             67108864       1048576     float    none      -1    294.7  227.75  213.51      0    277.7  241.62  226.52      0
            134217728       2097152     float    none      -1    495.4  270.94  254.00      0    488.8  274.60  257.43      0
            268435456       4194304     float    none      -1    877.5  305.92  286.80      0    861.3  311.65  292.17      0
            536870912       8388608     float    none      -1   1589.8  337.71  316.60      0   1576.2  340.61  319.33      0
           1073741824      16777216     float    none      -1   3105.7  345.74  324.13      0   3069.2  349.85  327.98      0
           2147483648      33554432     float    none      -1   6161.7  348.52  326.74      0   6070.7  353.75  331.64      0
           4294967296      67108864     float    none      -1    12305  349.03  327.22      0    12053  356.35  334.08      0
           8589934592     134217728     float    none      -1    24489  350.77  328.85      0    23991  358.05  335.67      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 120.248
         




### A3 High

This workload includes a sidecar container named the _tcpx-daemon_ , which runs a service that lets the Pod use the GPUDirect-TCPX protocol. If you have any Pods in your own environment that need to use the GPUDirect-TCPX protocol, you must add this sidecar container to those Pods. For a snippet of the required fields to add to your manifests, see [Add GPUDirect to your manifest](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega#gpudirect-tcpx_6).

  1. Review the [`nccl-config.yaml` ConfigMap manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-config.yaml). This manifest deploys scripts that initialize an NCCL all-gather test and sets NCCL-specific configuration settings.

  2. Review the [`nccl-test-latest.yaml` Deployment manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-test-latest.yaml).

  3. Deploy the ConfigMap and the test workload:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-config.yaml
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpx/nccl-test-latest.yaml
         

  4. Run the following commands to trigger an NCCL all-gather test for the nodes:
         
         kubectl exec \
            --stdin --tty --container=nccl-test nccl-test-host-1 \
            -- /configs/allgather.sh nccl-host-1 nccl-host-2
         

The output is similar to the following:
         
         #                                                              out-of-place                       in-place
         #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
            1048576         16384     float    none      -1    696.8    1.50    1.41      0    729.0    1.44    1.35      0
            2097152         32768     float    none      -1    776.4    2.70    2.53      0    726.7    2.89    2.71      0
            4194304         65536     float    none      -1    774.3    5.42    5.08      0    805.1    5.21    4.88      0
            8388608        131072     float    none      -1    812.1   10.33    9.68      0    817.6   10.26    9.62      0
            16777216        262144     float    none      -1   1035.2   16.21   15.19      0   1067.8   15.71   14.73      0
            33554432        524288     float    none      -1   1183.3   28.36   26.59      0   1211.8   27.69   25.96      0
            67108864       1048576     float    none      -1   1593.4   42.12   39.49      0   1510.5   44.43   41.65      0
            134217728       2097152     float    none      -1   2127.8   63.08   59.13      0   2312.7   58.03   54.41      0
            268435456       4194304     float    none      -1   3603.0   74.50   69.85      0   3586.2   74.85   70.17      0
            536870912       8388608     float    none      -1   7101.7   75.60   70.87      0   7060.9   76.03   71.28      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 29.8293
         




After installation of the GPUDirect-TCPX on your nodes is complete, you can use it to optimize the throughput of GPU-heavy workloads that run on those nodes. The required fields to use GPUDirect-TCPX in your own Pods are described in [Add GPUDirect to your manifests](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega#gpudirect-tcpx_6).

### A3 Mega

This workload includes a sidecar container named the _tcpxo-daemon_ , which runs a service that lets the Pod use the GPUDirect-TCPXO protocol. If you have any Pods in your own environment that need to use the GPUDirect-TCPXO protocol, you must add this sidecar container to those Pods. For a snippet of the required fields to add to your manifests, see [Add GPUDirect to your manifest](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega#gpudirect-tcpxo_6).

  1. Review the [`nccl-test-latest.yaml` manifest in GitHub](https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/nccl-test-latest.yaml).

  2. Deploy two Pods with the test workload:
         
         kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/container-engine-accelerators/master/gpudirect-tcpxo/nccl-test-latest.yaml
         

  3. After the Pods deploy, trigger an all-gather test:
         
         kubectl exec --stdin --tty --container=nccl-test nccl-test-host-1 -- /scripts/allgather.sh nccl-host-1 nccl-host-2
         

The output is similar to the following:
         
         #                                                              out-of-place                       in-place
         #        size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #         (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
                     0             0     float    none      -1     0.24    0.00    0.00      0     0.18    0.00    0.00      0
                     0             0     float    none      -1     0.19    0.00    0.00      0     0.17    0.00    0.00      0
                     0             0     float    none      -1     0.17    0.00    0.00      0     0.17    0.00    0.00      0
                     0             0     float    none      -1     0.17    0.00    0.00      0     0.17    0.00    0.00      0
                     0             0     float    none      -1     0.17    0.00    0.00      0     0.17    0.00    0.00      0
                  256             4     float    none      -1    235.2    0.00    0.00      0    235.1    0.00    0.00      0
                  512             8     float    none      -1    241.0    0.00    0.00      0    236.1    0.00    0.00      0
                  1024            16     float    none      -1    236.3    0.00    0.00      0    233.3    0.00    0.00      0
                  2048            32     float    none      -1    234.1    0.01    0.01      0    233.4    0.01    0.01      0
                  4096            64     float    none      -1    237.1    0.02    0.02      0    235.3    0.02    0.02      0
                  8192           128     float    none      -1    236.2    0.03    0.03      0    235.2    0.03    0.03      0
                  16384           256     float    none      -1    236.6    0.07    0.06      0    238.5    0.07    0.06      0
                  32768           512     float    none      -1    237.9    0.14    0.13      0    238.8    0.14    0.13      0
                  65536          1024     float    none      -1    242.3    0.27    0.25      0    239.4    0.27    0.26      0
                  131072          2048     float    none      -1    263.0    0.50    0.47      0    275.1    0.48    0.45      0
                  262144          4096     float    none      -1    279.2    0.94    0.88      0    269.9    0.97    0.91      0
                  524288          8192     float    none      -1    273.5    1.92    1.80      0    273.5    1.92    1.80      0
            1048576         16384     float    none      -1    315.1    3.33    3.12      0    314.1    3.34    3.13      0
            2097152         32768     float    none      -1    319.2    6.57    6.16      0    311.5    6.73    6.31      0
            4194304         65536     float    none      -1    331.8   12.64   11.85      0    331.3   12.66   11.87      0
            8388608        131072     float    none      -1    356.3   23.54   22.07      0    353.8   23.71   22.23      0
            16777216        262144     float    none      -1    409.1   41.01   38.45      0    405.2   41.40   38.81      0
            33554432        524288     float    none      -1    451.4   74.34   69.69      0    447.7   74.94   70.26      0
            67108864       1048576     float    none      -1    713.4   94.07   88.19      0    713.8   94.01   88.13      0
            134217728       2097152     float    none      -1   1122.1  119.62  112.14      0   1116.3  120.23  112.72      0
            268435456       4194304     float    none      -1   1785.8  150.32  140.92      0   1769.2  151.72  142.24      0
            536870912       8388608     float    none      -1   2859.7  187.74  176.00      0   2852.6  188.20  176.44      0
            1073741824      16777216     float    none      -1   5494.1  195.44  183.22      0   5568.2  192.83  180.78      0
            2147483648      33554432     float    none      -1    10841  198.09  185.71      0    10798  198.88  186.45      0
            4294967296      67108864     float    none      -1    21453  200.21  187.70      0    21490  199.86  187.37      0
            8589934592     134217728     float    none      -1    42603  201.63  189.03      0    42670  201.31  188.73      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : 45.7587
         #
         

After installation of the GPUDirect-TCPXO on your nodes is complete, you can use it to optimize the throughput of GPU-heavy workloads that run on those nodes. The required fields to use GPUDirect-TCPXO in your own Pods are described in [Add GPUDirect to your manifests](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-standard-a3-high-mega#gpudirect-tcpxo_6).




## What's next

  * [Collect and Understand NCCL Logs for Troubleshooting](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand) to understand the test outputs and troubleshoot issues.
  * Learn about [troubleshooting slow performance](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
