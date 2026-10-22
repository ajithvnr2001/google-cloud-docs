---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand/
title: Collect and understand NCCL/gIB logs \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:41.851632+00:00
---

# Collect and understand NCCL/gIB logs  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Collect and understand NCCL/gIB logs Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes how you can collect and interpret NCCL/gIB logs to troubleshoot stability and performance issues on AI Hypercomputer, including guidance on how to achieve the following:

  * Collect NCCL logs.
  * Understand the structure of NCCL log entries.
  * Verify that NCCL/gIB plugins are loaded correctly.
  * Check that NCCL and gIB versions are correct.
  * Troubleshoot common NCCL warnings and errors.



## Collect NCCL logs

You can use [NVIDIA Collective Communications Library](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview) (NCCL) logs to debug NCCL failures. For any stability or performance debugging, collect NCCL logs _from all logging levels_ while you run the problematic workload. Avoid dumping log entries to the console, because the sheer volume of the logs may prevent the job from continuing.

To collect NCCL logs, set the following environment variables:
    
    
    NCCL_DEBUG=INFO
    NCCL_DEBUG_SUBSYS=INIT,ENV,GRAPH,NET,COLL,TUNING
    NCCL_DEBUG_FILE=DESIRED_PATH/nccl_logs.VM_NAME.RANK_PROCESS_ID
    

Replace the following:

DESIRED_PATH: the path where you want to store your log files

VM_NAME: the VM Name

RANK_PROCESS_ID: the process ID of the rank

## NCCL log format

NCCL logs are similar to the following:
    
    
    # A sample log entry from NCCL core.
    a3ultra-vm-0:606:642 [6] NCCL INFO Using network gIB
    
    # A sample log entry from the gIB network plugin.
    a3ultra-vm-0:606:642 [6] NCCL INFO NET/gIB : Initializing gIB v1.0.2
    

Regardless of their source, NCCL logs have a prefix that resembles the following:
    
    
    <VM name>:<pid>:<tid> [<GPU device ID>] <log level> <log content>
    

## Verify that the NCCL/gIB plugins are correctly loaded

NCCL/gIB is made up of multiple Google-developed plugins. Failure to load any of the plugins can result in poor performance, and in some cases, fatal errors.

We recommend that you use the NCCL bundled with the gIB installer to ensure the latest features, best performance, and most stability. If you choose to use a custom NCCL version for testing, such as a NCCL version that's bundled with your machine learning framework of choice, then you must also [install the `nccl-gib-plugins` package](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/install-nccl#plugins-only).

### Network plugin (libnccl-net.so)

If the gIB network plugin is correctly loaded, you should see NCCL log entries that are similar to the following:
    
    
    ... NCCL INFO Using network gIB
    

If you see log entries similar to any of the following, then use the steps in the A shared object cannot be loaded section to fix the issue.
    
    
    # Cannot find the gIB network plugin.
    ... NCCL INFO NET/Plugin: Could not find: libnccl-net.so. Using internal network plugin.
    
    # Using the built-in TCP plugin.
    ... NCCL INFO Using network Socket
    
    # Using the built-in IB plugin.
    ... NCCL INFO Using network IB
    

### Tuner plugin (libnccl-tuner.so)

If the gIB tuner plugin is correctly loaded, you should see NCCL log entries that are similar to the following:
    
    
    NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
    NCCL INFO TUNER/Plugin: Using tuner plugin A3xTunerPlugin_v2
    

If you see a log entry similar to the following, then use the steps in the A shared object cannot be loaded section to fix the issue.
    
    
    NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
    

### CollNet plugin

Although these log entries indicate a failure, they are expected and are _not_ a cause for concern:
    
    
    NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
    NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin symbol (>= v5). ncclCollNetPlugin symbols v4 and lower are not supported.
    

## Check NCCL and gIB version

We recommend that you use the NCCL bundled with the gIB installer to ensure the latest features, best performance, and most stability. However, you can choose to use a custom NCCL version for testing, such as a NCCL version that's bundled with your machine learning framework of choice. In that case, install the `nccl-gib-plugins` package.

To check the NCCL and gIB version used, look for the following NCCL log entries:
    
    
    # NCCL version.
    ... NCCL INFO NCCL version 2.23.4+cuda12.2
    
    # gIB version.
    ... NCCL INFO NET/gIB : Initializing gIB v1.0.2
    

To confirm that you're running the recommended versions, compare the logged NCCL and gIB versions against the versions bundled in the latest `nccl-gib` package. We recommend keeping `nccl-gib` updated across all nodes; see [Install NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/install-nccl).

## Verify NCCL/gIB environment variables

To achieve good NCCL performance, we provide a script that you can use to set the recommended NCCL environment variables. Before you run your workload, source the script in _the same environment_ as the workload. Within the NCCL/gIB installer, the script is at `/usr/local/gib/set_nccl_env.sh`. If you don't use this script, and as a result NCCL environment variables are set incorrectly, it's possible that the gIB NCCL Config Checker will terminate the workload, NCCL will crash, or NCCL performance will be poor.

To check that the NCCL/gIB environment variables are applied correctly, look for NCCL log entries similar to the following:
    
    
    # Explicitly set values.
    ... NCCL INFO NCCL_P2P_PCI_CHUNKSIZE set by environment to 131072.
    
    # Using default values because the set value is invalid.
    ... NCCL INFO Invalid value INVALID_VALUE for NCCL_P2P_PCI_CHUNKSIZE, using default 131072.
    

Compare the following values with the recommended NCCL environment variables.

## Check GKE workload manifest

On GKE, your Kubernetes workload manifest has several required setups to smoothly consume NCCL/gIB:

  * The manifest must mount the NCCL/gIB binaries from `/home/kubernetes/bin/gib` on the VM to `/usr/local/gib` in your workload container. Note that `/home/kubernetes/bin/nvidia` on the VM is automatically mounted to `/usr/local/nvidia` in your workload container.
  * Your workload container must set `LD_LIBRARY_PATH` to `/usr/local/gib/lib64:/usr/local/nvidia/lib64`.
  * Your cluster and node-pools must have GKE multi-networking set up, and your workload manifest must include the multi-networking annotations to avoid the need for setting `hostNetwork: true`.



An actual Kubernetes workload manifest on GKE is similar to the following:
    
    
    ...
    metadata:
      annotations:
        networking.gke.io/default-interface: 'eth0'
        networking.gke.io/interfaces: |
          [
            {"interfaceName":"eth0","network":"default"},
            {"interfaceName":"eth1","network":"gvnic-1"},
            {"interfaceName":"gpu0rdma0","network":"rdma-0"},
            {"interfaceName":"gpu1rdma0","network":"rdma-1"},
            {"interfaceName":"gpu2rdma0","network":"rdma-2"},
            {"interfaceName":"gpu3rdma0","network":"rdma-3"},
            {"interfaceName":"gpu4rdma0","network":"rdma-4"},
            {"interfaceName":"gpu5rdma0","network":"rdma-5"},
            {"interfaceName":"gpu6rdma0","network":"rdma-6"},
            {"interfaceName":"gpu7rdma0","network":"rdma-7"}
          ]
    spec:
      volumes:
        - name: gib
          hostPath:
            path: /home/kubernetes/bin/gib
    ...
    containers:
      - name: my-container
        volumeMounts:
          - name: gib
         mountPath: /usr/local/gib
        env:
          - name: LD_LIBRARY_PATH
            value: /usr/local/gib/lib64:/usr/local/nvidia/lib64
        resources:
          limits:
            nvidia.com/gpu: 8
    

## Check the GID table

In RoCE, the global identifier (GID) table is used to uniquely address RDMA traffic. If the GID table is broken, no RDMA traffic can pass.

We provide a script `show_gids.sh` to show the GID table. In the installer, it is located at `/usr/local/gib/scripts`. If you used our installer with no modifications, it is installed to `/var/lib/gib/scripts` on the VM.

As you run the script in the VM, you should see an output similar to the following:
    
    
    DEV     PORT  INDEX  GID                                      IPv4         VER  DEV
    ---     ----  -----  ---                                      ----         ---  ---
    mlx5_0  1     0      fe80:0000:0000:0000:689c:b8ff:fedf:3b01               v1   gp0rdma0
    mlx5_0  1     1      fe80:0000:0000:0000:689c:b8ff:fedf:3b01               v2   gp0rdma0
    mlx5_0  1     2      0000:0000:0000:0000:0000:ffff:c0a8:0202  192.168.2.2  v1   gp0rdma0
    mlx5_0  1     3      0000:0000:0000:0000:0000:ffff:c0a8:0202  192.168.2.2  v2   gp0rdma0
    ...
    

Review the output and confirm the following:

  * The GID table has the proper number of entries: 
    * For A3 Ultra or A4, 32 entries with 4 entries per CX-7.
    * For A3 Mega, 32 entries with 4 entries per CX-7.
    * For A3 High (8 GPUs), 16 entries with 4 entries per CX-7.
    * For A4X, 16 entries with 4 entries per CX-7.
  * The GID entries of each CX-7 have indexes 0, 1, 2, and 3.
  * For each CX-7, the indexes 2 and 3 have an IPv4 address, and that IP address matches the IPv4 of that device (for example from `ip a`).



If any of these items are false, then the GID table is broken. Consider rebooting your VM or restarting the network manager in your guest OS.

## NCCL warnings

NCCL logs have several levels, with NCCL warnings (`NCCL WARN`) being the most severe. NCCL warnings usually indicate failures, which may or may not be fatal. NCCL does not have a log level that automatically stops the workload.

### A shared object cannot be loaded

The following error occurs when a shared object cannot be loaded due to your setup.
    
    
    error while loading shared libraries: libnccl.so.2: cannot open shared object file: No such file or directory
    

To resolve the issue:

  1. Make sure the shared object is installed in your environment.
  2. Make sure the directory of the shared object is in the `$LD_LIBRARY_PATH` environment variable.



### Failed to map segment from shared object

The following error occurs when the directory of the shared object is not executable.
    
    
    error while loading shared libraries: libnccl.so.2: failed to map segment from shared object: Operation not permitted
    

To resolve the issue, run the following commands (these examples assume that the gIB binaries are installed in `/var/lib/gib` on the VMs):
    
    
    sudo mount --bind /var/lib/gib /var/lib/gib
    sudo mount -o remount,exec /var/lib/gib
    

### Guest Config Checker cannot find a config file

Log entries like these appear when the guest Config Checker cannot find a configuration file to use.
    
    
    ... NCCL WARN cannot find config file at default paths; you must specify NCCL_SHIMNET_GUEST_CONFIG_CHECKER_CONFIG_FILE
    
    ... NCCL WARN NCCL_SHIMNET_GUEST_CONFIG_CHECKER_CONFIG_FILE does not exist: /path/to/guest_config.txtpb
    

To resolve the issue, you can set the environment variable `NCCL_SHIMNET_GUEST_CONFIG_CHECKER_CONFIG_FILE` to point to the location of `guest_config.txtpb`. The NCCL/gIB installer's default location for the configuration file is `/usr/local/gib/configs/guest_config.txtpb`.

We don't recommend that you disable the guest Config Checker because it helps to ensure best practices and proper configuration. However, if necessary, you can disable the guest Config Checker by setting the environment variable `NCCL_SHIMNET_SHIM_LAYERS` to `UNUSED`.

### Guest Config Checker enforced or recommended a setting

The following errors occur when the NCCL/gIB environment variables are not set as recommended.
    
    
    # The guest Config Checker enforcing an environment variable.
    # This ends the workload.
    ... NCCL WARN NCCL/NET (shim) mismatch enforced: NCCL_P2P_NVL_CHUNKSIZE=524288 (expected 262144)
    
    # The guest Config Checker recommending an environment variable.
    # This does not end the workload.
    ... NCCL WARN NCCL/NET (shim) mismatch recommended: NCCL_MAX_P2P_NCHANNELS=8 (expected unset)
    

To resolve the issue:

  1. Follow the guidance of the guest Config Checker logs.
  2. Verify NCCL/gIB environment variables.



### Tuner cannot find a config file

The following error occurs when the tuner plugin cannot find a configuration file to use.
    
    
    ... NCCL WARN No NCCL_TUNER_CONFIG_PATH provided. Please populate NCCL_TUNER_CONFIG_PATH to use config-based tuner plugin.
    

To resolve the issue:

  1. Set the environment variable `NCCL_TUNER_CONFIG_PATH` to point to the location of `tuner_config.txtpb`. The NCCL/gIB installer's default location for the configuration file is `/usr/local/gib/configs/guest_config.txtpb`.
  2. Verify NCCL/gIB environment variables.



### Insufficient glibc version

The following error occurs when your distribution-local glibc version is too old, most likely because the Linux distribution in your local environment is too old. The NCCL/gIB binaries require glibc version 2.29.
    
    
    /usr/lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34' not found (required by /usr/local/gib/lib64/libnccl.so.2)
    

To resolve the issue, upgrade your image distribution (for example Ubuntu 20.04 or newer, RockyLinux 9 or newer).

### Message truncated

The following error occurs when you are using mixed NCCL versions across ranks.
    
    
    ... NCCL WARN Message truncated : received ### bytes instead of ###
    

To resolve the issue, check your NCCL and gIB Version. If you are using GKE, check or reinstall your NCCL/gIB installer daemonset (see [instructions for A3 Ultra and A4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra#install-rdma-configure-nccl) or [instructions for A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x#install-rdma-configure-nccl)).

### libibverbs cannot load the provider config

The following error occurs when you did not mount the directory containing gIB binaries to `/usr/local/gib`. This won't cause a workload failure. However, NCCL falls back to using TCP and can cause poor performance.
    
    
    libibverbs: Warning: couldn't open config directory '/usr/local/gib/rdma-core/build/etc/libibverbs.d'.
    

To resolve the issue, if you are using GKE, check your workload manifest.

### ibv_modify_qp errors

There are a number of errors you could run into as the gIB network plugin prepares QPs for actual network transactions.

#### Invalid argument (errno 22)

The following error occurs for one of the following reasons:

  1. The other end of the QP has a broken GID table.
  2. NCCL/gIB environment variables are misconfigured, especially `NCCL_IB_GID_INDEX`, `NCCL_IB_TC`, and `NCCL_IB_FIFO_TC`.


    
    
    ... NCCL WARN Call to ibv_modify_qp failed with error Invalid argument errno 22
    

To resolve the issue:

  1. Look for other `ibv_modify_qp` errors with the signature `No data available error 61`, and follow the mitigation instructions for error 61.
  2. Verify NCCL/gIB environment variables.



#### No data available (errno 61)

The following error occurs for one of the following reasons:

  1. This VM has a broken GID table.
  2. NCCL/gIB environment variables are misconfigured, especially `NCCL_IB_GID_INDEX`, `NCCL_IB_TC`, and `NCCL_IB_FIFO_TC`.


    
    
    ... NCCL WARN Call to ibv_modify_qp failed with error No data available errno 61
    

To resolve the issue, first check for the cause:

  1. Check the GID table.
  2. Verify NCCL/gIB environment variables.



If the GID table is broken, try the following mitigations:

  1. (Short term) Restart the network manager (for example `networkd`) on the VM until the IP address of the problematic interface gets refreshed. 
     1. You can restart `networkd` on the VM using `sudo systemctl restart systemd-networkd`.
     2. You can see the IP address of all interfaces using `ip a`.
     3. Check that the GID table has recovered.
  2. Contact Google Support for assistance with a long term solution.



#### Connection timed out (errno 110)

The following error occurs when there is a basic connectivity issue between the VMs.
    
    
    ... NCCL WARN Call to ibv_modify_qp failed with error Connection timed out errno 110
    

To resolve the issue, contact Google Support for assistance.

### QP Got Completion with Error

The following error occurs for one of the following reasons:

  1. Underlying RDMA connection issues (link flaps, etc).
  2. NCCL/gIB environment variables are misconfigured, especially `NCCL_IB_TIMEOUT` and `NCCL_IB_RETRY_CNT`.


    
    
    ... NCCL WARN NET/gIB : Got completion from peer 192.168.0.9<55224> with status=12 opcode=0 len=0 vendor err 129 (Recv) localGid ::ffff:192.168.3.6 remoteGids::ffff:192.168.3.9
    

To resolve the issue, contact Google Support for assistance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
