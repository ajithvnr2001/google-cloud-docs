---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm/
title: Run NCCL on Slurm clusters \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:07.100795+00:00
---

# Run NCCL on Slurm clusters  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run NCCL on Slurm clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This page describes how to run [NCCL](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview) tests on a Slurm cluster. To use a managed Slurm environment that includes built-in NCCL tests for verifying cluster health, see instead [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#verify-health).

Choose the steps for your machine type:

###  A4X Max, A4X, and A4 

The following test uses [Ramble](https://github.com/GoogleCloudPlatform/ramble), which is an open-source, multi-platform experimentation framework written in Python that is used to coordinate the running of NCCL tests. Ramble and its dependencies are compatible with the ARM64 architecture used by A4X Max and A4X machines.

The run scripts used for this test are staged in the `/opt/apps/system_benchmarks` on the Slurm controller node and are available to all nodes in the cluster. Running this test installs Ramble to the `/opt/apps/ramble` directory.

  1. From the login node in the ${HOME} directory, run the following command. Because the test can take approximately 10 minutes, or longer if other jobs are in the queue, the following command uses `nohup` and redirects the `stdout/err` to a log file.
         
         nohup bash /opt/apps/system_benchmarks/run-nccl-tests-via-ramble.sh >& nccl.log &

This command creates a folder called `nccl-tests_$(date +%s)` that stores all of the test results. The date tag ensures that a unique folder is created based on each current timestamp.

For example, if your cluster has 16 nodes then NCCL tests are run for `all-gather`, `all-reduce`, and `reduce-scatter` on 2, 4, 8, and 16 nodes.

  2. Review the results. The `nccl.log` contains the logs from setting up and running the test. To view these logs, run the following:
         
         tail -f nccl.log

You can also use `Ctrl+C` to stop tailing the output at any time. At the end of the `nccl.log`, your output should resemble the following:
         
         ...
         ---- SUMMARY for >1GB Message Sizes ----
         workload        n_nodes msg_size        busbw
         all-gather      2       1073741824      ###.##
         all-gather      2       2147483648      ###.##
         all-gather      2       4294967296      ###.##
         all-gather      2       8589934592      ###.##
         ...
         all-reduce      2       1073741824      ###.##
         ...
         reduce-scatter  2       1073741824      ###.##
         ...
         -------- Benchmarking Complete -------
         

All of the Slurm job scripts and nccl-tests output logs are stored in the `nccl-tests_$(date +%s)/experiments` directory. A summary of the NCCL test performance is also stored in the `nccl-tests_${date +%s)/summary.tsv` file.

Removing `nccl-tests_$(date +%s)/` directory removes all of the files generated during these tests.




###  A3 Ultra 

  1. From the shared directory of the login node (this node is usually located at `${HOME}`), download the script needed to build the NCCL test by running the following command:
         
         wget -np -nd https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/heads/main/examples/machine-learning/a3-ultragpu-8g/nccl-tests/build-nccl-tests.sh

  2. After the script downloads, import a Pytorch image from the [NVIDIA container registry](https://catalog.ngc.nvidia.com/containers) and build the NCCL tests. To do this, run the following command:
         
         sbatch build-nccl-tests.sh

The preceding script runs on one of your nodes. It uses the `--container-mounts` switch to mount your current directory, `$PWD`, into the `/nccl` directory within the container.

  3. Verify that the NCCL test is built. To verify this, run the following command:
         
         sacct -a

If successfully completed, the output is similar to the following:
         
         JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
         ------------ ---------- ---------- ---------- ---------- ---------- --------
         1            build-ncc+    a3ultra                   112  COMPLETED      0:0
         

If the build is successful you should also have a file named `nvidia+pytorch+24.09-py3.sqsh` in the directory where you ran the command along with a directory named `nccl-tests`.

  4. Check that the `nccl-tests/build` folder contains several binaries, including `all_gather_perf`, `all_reduce_perf`, `reduce_scatter_perf`, and `alltoall_perf`.

  5. Download the NCCL test script.
         
         wget -np -nd https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/heads/main/examples/machine-learning/a3-ultragpu-8g/nccl-tests/run-nccl-tests.sh

To run any job on an A3 Ultra cluster, several environment variables must be set in order to enable high performance networking with RDMA. Because you use enroot containers in this procedure to launch workloads, these variables must be set in the container environment as opposed to the host environment. These variables can be inspected in the `run-nccl-tests.sh` script that you just downloaded.

  6. Run the NCCL test script. The test can take approximately 15 minutes, or longer.
         
         sbatch run-nccl-tests.sh

  7. Review the results. The script outputs a `slurm-XX.out` file that contains the result of the nccl `all_gather_perf` benchmark.

The output is similar to the following:
         
         #
         #                                                              out-of-place                       in-place
         #        size         count     type     redop   root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #         (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
             268435456       4194304     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
             536870912       8388608     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            1073741824      16777216     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            2147483648      33554432     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            4294967296      67108864     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            8589934592     134217728     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : ###.##
         #
         




###  A3 Mega 

  1. From the shared directory of the login node (this node is usually located at `${HOME}`), download the script needed to build the NCCL test by running the following command:
         
         wget -np -nd https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/heads/main/examples/machine-learning/a3-megagpu-8g/nccl-tests/build-nccl-tests.sh

  2. After the script downloads, import a Pytorch image from the [NVIDIA container registry](https://catalog.ngc.nvidia.com/containers) and build the NCCL tests.
         
         sbatch build-nccl-tests.sh

The preceding script runs on one of your nodes. It uses the `--container-mounts` switch to mount your current directory, `$PWD`, into the `/nccl` directory within the container.

  3. Verify that the NCCL test is built:
         
         sacct -a

The output is similar to the following:
         
         JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
         ------------ ---------- ---------- ---------- ---------- ---------- --------
         1            build-ncc+    a3mega                   112  COMPLETED      0:0
         

After the build completes, the `nccl-tests` directory is created. This directory contains the `nvidia+pytorch+24.09-py3.sqsh` file. A `.sqsh` file is a compressed, read-only file system image that serves as the standard container format for AI workloads.

  4. Check that the `nccl-tests/build` folder contains several binaries, including `all_gather_perf`, `all_reduce_perf`, `reduce_scatter_perf`, and `alltoall_perf`.

  5. Download the NCCL test script:
         
         wget -np -nd https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/heads/main/examples/machine-learning/a3-megagpu-8g/nccl-tests/run-nccl-tests.sh

To run any job on an A3 Mega cluster, several environment variables must be set to enable high performance networking with GPUDirect-TCPXO protocol. Because you use enroot containers in this procedure to launch workloads, these variables must be set in the container environment as opposed to the host environment. You can inspect these variables in the `run-nccl-tests.sh` script that you downloaded in the previous step.

  6. Run the NCCL test script. The test can take approximately 15 minutes, or longer.
         
         sbatch run-nccl-tests.sh

  7. Review the results. The script outputs a `slurm-XX.out` file that contains the result of the nccl `all_gather_perf` benchmark.

The output is similar to the following:
         
         #
         #                                                              out-of-place                       in-place
         #        size         count     type     redop   root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #         (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
             268435456       4194304     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
             536870912       8388608     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            1073741824      16777216     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            2147483648      33554432     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            4294967296      67108864     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            8589934592     134217728     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : ###.##
         #
         




###  A3 High 

  1. From the shared directory of the login node (this node is usually located at `${HOME}`), download the script needed to build the NCCL test by running the following command: 
         
         wget -np -nd https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/heads/main/examples/machine-learning/a3-highgpu-8g/nccl-tests/build-nccl-tests.sh

  2. After the script downloads, import a Pytorch image from the [NVIDIA container registry](https://catalog.ngc.nvidia.com/containers) and build the NCCL tests. To do so, run the following command:
         
         sbatch build-nccl-tests.sh

The preceding script runs on one of your nodes. It uses the `--container-mounts` switch to mount your current directory, `$PWD`, into the `/nccl` directory within the container.

  3. Verify that the NCCL test is built:
         
         sacct -a

The output is similar to the following:
         
         JobID           JobName  Partition    Account  AllocCPUS      State ExitCode
         ------------ ---------- ---------- ---------- ---------- ---------- --------
         1            build-ncc+    a3high                   112  COMPLETED      0:0
         

If the build is successful, then the `nccl-tests` directory is created. This directory contains the `nvidia+pytorch+24.09-py3.sqsh` file. A `.sqsh` file is a compressed, read-only file system image that serves as the standard container format for AI workloads.

  4. Check that the `nccl-tests/build` folder contains several binaries, including `all_gather_perf`, `all_reduce_perf`, `reduce_scatter_perf`, and `alltoall_perf`.

  5. Download the NCCL test script:
         
         wget -np -nd https://raw.githubusercontent.com/GoogleCloudPlatform/cluster-toolkit/refs/heads/main/examples/machine-learning/a3-highgpu-8g/nccl-tests/run-nccl-tests.sh

To run any job on an A3 High cluster, several environment variables must be set to enable high performance networking with GPUDirect-TCPX. Because you use enroot containers in this procedure to launch workloads, these variables must be set in the container environment as opposed to the host environment. You can inspect these variables in the `run-nccl-tests.sh` script that you just downloaded.

  6. Run the NCCL test script. The test can take approximately 15 minutes, or longer.
         
         sbatch run-nccl-tests.sh

  7. Review the results. The script outputs a `slurm-XX.out` file that contains the result of the nccl `all_gather_perf` benchmark.

The output is similar to the following:
         
         #
         #                                                              out-of-place                       in-place
         #        size         count     type     redop   root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
         #         (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
             268435456       4194304     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
             536870912       8388608     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            1073741824      16777216     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            2147483648      33554432     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            4294967296      67108864     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
            8589934592     134217728     float    none      -1    #####  ###.##  ###.##    N/A   ######  ###.##  ###.##      0
         # Out of bounds values : 0 OK
         # Avg bus bandwidth    : ###.##
         #
         




## What's next

  * [Collect and Understand NCCL Logs for Troubleshooting](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand) to understand the test outputs and troubleshoot issues.
  * [Monitor Compute Engine instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor).
  * Learn about [troubleshooting slow performance](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
