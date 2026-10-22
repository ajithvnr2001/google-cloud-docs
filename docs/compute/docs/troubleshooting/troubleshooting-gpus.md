---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus/
title: Troubleshoot GPU VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:17.293333+00:00
---

# Troubleshoot GPU VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot GPU VMs Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to diagnose and resolve common issues with Compute Engine VMs that have attached GPUs, including hardware errors and performance bottlenecks.

## Troubleshoot GPU VMs by using NVIDIA DCGM

NVIDIA Data Center GPU Manager (DCGM) is a suite of tools for managing and monitoring NVIDIA data center GPUs in cluster environments.

To use DCGM to troubleshoot issues in your GPU environment, complete the following:

  * Ensure that you're using the latest recommended NVIDIA driver for the GPU model that's attached to your VM. To review driver versions, see [Recommended NVIDIA driver versions](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#minimum-driver).
  * Ensure that you installed the latest version of DCGM. To install the latest version, see [DCGM installation](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html).



### Diagnose issues

When you run a `dcgmi` diagnostic command, the issues reported by the diagnostic tool include next steps for taking action on the issue. The following example shows the actionable output from the `dcgmi diag -r memory -j` command.
    
    
    {
      ........
       "category":"Hardware",
       "tests":[
          {
             "name":"GPU Memory",
             "results":[
                {
                   "gpu_id":"0",
                   "info":"GPU 0 Allocated 23376170169
    bytes (98.3%)",
                   "status":"Fail",
                   ""warnings":[
                      {
                         **"warning":"Pending page
    retirements together with a DBE were detected on GPU 0. Drain the GPU and reset it or reboot the node to resolve this issue.",**
                         "error_id":83,
                         "error_category":10,
                         **"error_severity":6**
                      }
                   ]
                }
      .........
    

From the preceding output snippet, you can see that `GPU 0` has pending page retirements that are caused by a non-recoverable error. The output provided the unique `error_id` and advice on debugging the issue. For this example output, we recommend that you drain the GPU and reboot the VM. In most cases, following the instructions in this section of the output can help to resolve the issue.

**Pro Tip:** Take note of the error severity. In the example output a value of `"error_severity":6` corresponds to a `DCGM_ERROR_RESET` which means that a reset resolves issues with this severity value.

For a full list of `error_severity` values, review the `dcgmErrorSeverity_enum` section on the [ `dcgm_errors` GitHub file](https://github.com/NVIDIA/DCGM/blob/master/dcgmlib/dcgm_errors.h).

## Troubleshoot GPU performance issues for A3 VMs

The A3 machine series is available with NVIDIA H200 or H100 GPUs attached. This series includes [A3 Ultra (H200)](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms), [A3 Mega (H100)](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms), [A3 High (H100)](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-standard-vms), and [A3 Edge (H100)](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms) machine types.

### Identify a faulty node

Large-scale training or benchmark jobs on a multi-node GPU cluster can stop responding or perform poorly. This often occurs because one or more nodes underperform and slow down the entire operation. This section describes how to identify a faulty node or host machine by either running an NCCL benchmark test or analyzing NCCL logs.

### Run NCCL benchmark test

To identify the group of nodes causing the failure, systematically test subsets of your cluster by using NCCL benchmarks like `all_reduce_perf`.

  1. To identify your nodesets, group your nodes into logical sets, for example, [partitions in Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/modules/slurm-partition).
  2. To create hostfiles, create a separate hostfile for each nodeset, listing hostnames and the number of GPUs per node. The number of slots you specify depends on the GPU count of your A3 VM type. For example, `a3-highgpu-8g` VMs have 8 GPUs, so you must specify `slots=8`.
  3. To run benchmarks, execute the `all_reduce_perf` benchmark against each nodeset individually. 
         
         mpirun -x LD_LIBRARY_PATH --hostfile HOSTFILE_NAME -n TOTAL_PROCESSES \
             ./build/all_reduce_perf -b 1G -e 8G -f 2 -g NUM_GPUS_PER_NODE
                   

Replace the following:

     * `HOSTFILE_NAME`: the name of the hostfile that contains the list of nodes and the number of GPUs per node for the nodeset.
     * `TOTAL_PROCESSES`: the total number of MPI processes to launch across all hosts in the nodeset.
     * `NUM_GPUS_PER_NODE`: the number of GPUs per node. For all A3 machine types, this value is `8`.
  4. To analyze results, if a job hangs or shows significantly lower bus bandwidth (`busbw`) on a particular nodeset, then that set is likely faulty.
  5. To sub-divide, if a nodeset is faulty, then divide its hostfile in half and re-test to narrow down the binary search until you pinpoint the individual misbehaving node.



### Analyze NCCL logs

If the benchmark method doesn't pinpoint a node, then analyze detailed NCCL logs.

  1. To enable debug logging, set the following environment variables in the shell session where you plan to run your workload: 
         
         export NCCL_DEBUG=INFO
                 export NCCL_DEBUG_SUBSYS=INIT,NET,COLL
                 export NCCL_DEBUG_FILE="LOG_DIRECTORY/nccl_log.%h.%p"
                 

Replace `LOG_DIRECTORY` with the directory where you want to store your logs.

Setting `NCCL_DEBUG_FILE` with `%h` and `%p` creates unique, non-interleaved log files for each process. 

If you run a multi-node workload using `mpirun`, then propagate these variables to all nodes by using the `-x` flag. For example:
         
         mpirun -x NCCL_DEBUG -x NCCL_DEBUG_SUBSYS -x NCCL_DEBUG_FILE ...
                   

  2. To find the first error, use the following command to find the earliest timeout or failure events across all log files: 
         
         grep "NCCL WARN.*NET/FasTrak" LOG_DIRECTORY/* | sed 's/.*NET\/FasTrak\(.*\)/\1/g' \
           | sort | head -n 20
                   

Replace `LOG_DIRECTORY` with the directory where your logs are stored.

  3. To count collective operations, a straggler node completes fewer collective operations. Count `"opCount"` entries for suspect ranks: 
         
         grep "opCount" LOG_DIRECTORY/nccl_log.HOSTNAME.PID | wc -l
                   

Replace the following:

     * `LOG_DIRECTORY`: the directory where your logs are stored
     * `HOSTNAME`: the hostname of the node
     * `PID`: the process ID of the NCCL process
  4. To gather more logging data before a job aborts, temporarily increase the data transfer timeout: 
         
         export NCCL_FASTRAK_DATA_TRANSFER_TIMEOUT_MS=3600000
                 




### Monitor GPU thermal throttling

A3 series VMs can experience performance degradation if they consistently reach temperatures greater than 87 °C under load. To check for GPU thermal throttling across nodes in a cluster, use either `nvidia-smi` or `dcgmi`.

### Using nvidia-smi

To check the current temperature and throttling status of all GPUs on a node, run the following command:
    
    
    nvidia-smi --query-gpu=timestamp,name,pci.bus_id,temperature.gpu,clocks_throttle_reasons.hw_slowdown --format=csv
        

In the output, a value of `Active` in the `clocks_throttle_reasons.hw_slowdown` column indicates the GPU is being throttled due to high temperatures.

### Using dcgmi

The NVIDIA Data Center GPU Manager (DCGM) diagnostic suite includes checks for thermal violations. To run a level 1 diagnostic, run the following command:
    
    
    dcgmi diag -r 1

A result of `Warn` or `Fail` in the `Thermal` section indicates a thermal violation occurred during the test. If a thermal violation is accompanied by clock throttling, then the GPU is likely overheating and requires further investigation.

## Xid errors

After you create a VM that has attached GPUs, you must install NVIDIA device drivers [on your GPU VMs](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) so that your applications can access the GPUs. However, sometimes these drivers return error messages.

An Xid message is an error report from the NVIDIA driver that is printed to the operating system's kernel log or event log for your Linux VM. These messages are placed in the `/var/log/messages` file. For more information about Xid messages including potential causes, see [NVIDIA documentation](https://docs.nvidia.com/deploy/xid-errors/index.html).

### How Google handles Xid errors

Google uses passive health checks to evaluate GPU systems. If hardware replacement is indicated, then Google initiates [emergency maintenance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications) automatically. Google detects Xid errors and proactively sends machines to repair where error codes indicate a high probability of hardware failure, such as Xid 74, 79, and 140. For some Xid codes, because they can be caused by either software or hardware problems, Google uses pattern matching to trigger repairs, so not every occurrence results in an automatic repair.

**Important:** Aggregate error counts, `Aggregate SRAM Uncorrectable Parity`, that are reported by `nvidia-smi` represent lifetime counts for the GPU, and don't reset when the GPU is reset nor when the instance is rebooted. It is normal for GPUs to experience a small number of errors over their lifespan. Google automatically initiates repair actions when the GPU requires physical repair or replacement based on _lifetime error counts_.

### Types of Xid errors

The following list describes the three main categories of Xid errors and their recommended recovery actions:

  * **Application errors:** these indicate issues inside your application code. Application errors include Xids such as Xid 13, 31, 94, 95, and 137, which indicate various types of memory access violation, similar to a segmentation fault. These don't indicate an ECC error. To troubleshoot these errors, NVIDIA recommends using either of the following debugging approaches:

    * **Direct debugging:** run the application directly in [cuda-gdb](https://docs.nvidia.com/cuda/cuda-gdb/index.html) or run the [Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html) memcheck tool.
    * **Post-exception debugging:** run the application with `CUDA_DEVICE_WAITS_ON_EXCEPTION=1`. When an exception occurs, the GPU driver freezes the application state without exiting so you can attach a debugger later (`cuda-gdb -p <PID>`) to inspect the live stack trace.
  * **Driver errors:** these indicate issues caused by the NVIDIA GPU driver. To resolve these errors, ensure that you're using the latest NVIDIA driver version. Google monitors these errors and collaborates with NVIDIA on driver fixes.

  * **Firmware or hardware recoverable errors:** these indicate firmware or hardware errors that allow for recovery without hardware replacement. To resolve these errors, apply manual recovery measures such as resetting the GPU or rebooting the instance. Firmware or hardware recoverable errors include Error Correcting Code (ECC) errors (applicable to Xids such as Xid 48, 63, and 64) that indicate various stages of detecting and mitigating ECC errors. For more information about page retirement and ECC error mitigation, see NVIDIA's [Dynamic Page Retirement FAQ](https://docs.nvidia.com/deploy/dynamic-page-retirement/index.html#faq).

**Note:** When you encounter an uncorrectable ECC error, your workload terminates and the volatile error count increments. Our recommendation in this case is to reset the GPU or reboot the instance and not to report the host as faulty.



## Review Xid messages

To quickly diagnose why a GPU workload failed, stopped responding, or experienced performance degradation, check your instance's kernel logs (`dmesg` or `/var/log/kern.log`) for numeric NVIDIA Xid error codes.

Reviewing the Xid error tables in the following subsections helps you immediately:

  * **Pinpoint the root cause:** identify whether the failure is caused by an application bug (such as illegal memory access), a driver conflict, or a physical hardware fault (such as double-bit ECC memory errors).
  * **Determine operational ownership:** check what immediate manual recovery measures you must apply, such as resetting GPUs, rebooting VMs, or running debuggers, versus what automated repair and hardware replacement actions Google is actively managing on the host.
  * **Take the correct recovery steps:** avoid unnecessary troubleshooting procedures and know precisely when manual recovery is sufficient versus when you need to report the host as faulty. Sometimes, manual recovery isn't sufficient, for example, if the error source is in the GPU cache (SRAM), which can't be remapped, indicated by `Xid 48` with `SRAM Threshold Exceeded=Yes`, or if the GPU has exhausted its remap bank, indicated by `Xid 64: All reserved rows for bank are remapped`. In these cases, Google detects that the GPU is eligible for hardware replacement and proactively sends the machine to repair. If your workloads encounter recurring errors or if you observe repeated memory faults, then you can [report the faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host) to initiate automated repair or replacement. For GKE, see [How to report faulty hosts in GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters#report-faulty-hosts-how-to).



### Xid handling

The following sections group common Xid error messages by technical category alongside their authoritative resolutions and responsibilities:

  * GPU memory errors (Xids `48`, `63`, `64`, `92`, `94`, `95`)
  * GPU System Processor (GSP) errors (Xids `119`, `120`)
  * Illegal memory access errors (Xids `13`, `31`, `137`)
  * Other common Xid error messages (Xids `74`, `79`, `109`, `149`)



### GPU memory errors

GPU memory is the memory that is available on a GPU that can be used for temporary storage of data. GPU memory is protected with Error Correction Code (ECC), which detects and corrects single-bit errors (SBE) and detects and reports double-bit uncorrectable errors (DBE).

These memory errors are expected to occur over the lifespan of a GPU. Prior to the release of the NVIDIA A100 GPUs, [dynamic page retirement](https://docs.nvidia.com/deploy/a100-gpu-mem-error-mgmt/index.html#dynamic-blacklisting) was supported. For NVIDIA A100 and later GPU releases (such as NVIDIA H100), [row remap error recovery](https://docs.nvidia.com/deploy/a100-gpu-mem-error-mgmt/index.html#row-remapping) is introduced for HBM (DRAM) errors. ECC is enabled by default, and Google highly recommends keeping ECC enabled.

The following table lists common GPU memory errors and their suggested resolutions:

**Xid error message** | **Customer action** | **Google action**  
---|---|---  
`Xid 48: _Double Bit ECC_` A double-bit (uncorrectable) memory error was detected by ECC. This error always interrupts the running workload and generates Xid 48. | 

  1. Stop your workloads.
  2. Depending on your environment, reset the GPUs or reboot the VM to recover and resume workloads: 
     * **For Compute Engine VMs:** Reset the GPUs or [reboot the VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance). For more information about VM actions and lifecycle states, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).
     * **For GKE nodes:** Apply `kubectl label nodes NODE_NAME cloud.google.com/perform-reboot=true` to the impacted node to [trigger a guest OS reboot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#guest-os-reboot).

|  Google monitors when the GPU is eligible for hardware replacement, such as if the HBM remap bank is exhausted or the GPU exceeds its lifetime SRAM error threshold, and proactively sends the machine to repair to replace the GPU.  
`Xid 63: _ECC page retirement or row remapping recording event_` Indicates a dynamic page retirement or row remapping event was recorded due to a memory error. | 

  1. Stop your workloads.
  2. Depending on your environment, reset the GPUs or reboot the VM to recover and resume workloads: 
     * **For Compute Engine VMs:** Reset the GPUs or [reboot the VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance). For more information about VM actions and lifecycle states, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).
     * **For GKE nodes:** Apply `kubectl label nodes NODE_NAME cloud.google.com/perform-reboot=true` to the impacted node to [trigger a guest OS reboot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#guest-os-reboot).

|  Google monitors error thresholds and sends the machine to repair when the GPU requires physical repair or replacement.  
`Xid 64: _ECC page retirement or row remapper recording failure_` And the message contains the following information: ` Xid 64: All reserved rows for bank are remapped` | 

  1. Stop your workloads.
  2. Depending on your environment, reset the GPUs or reboot the VM to recover and resume workloads: 
     * **For Compute Engine VMs:** Reset the GPUs or [reboot the VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance). For more information about VM actions and lifecycle states, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).
     * **For GKE nodes:** Apply `kubectl label nodes NODE_NAME cloud.google.com/perform-reboot=true` to the impacted node to [trigger a guest OS reboot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#guest-os-reboot).

|  When the remap bank is exhausted (`All reserved rows for bank are remapped`), Google detects that the GPU is eligible for hardware replacement and proactively sends the machine to repair.  
If you get at least two of the following Xid messages together:

  * `Xid 48`
  * `Xid 63`
  * `Xid 64`

And the message contains the following information: `Xid XX: row remap pending` | 

  1. Stop your workloads.
  2. Depending on your environment, reset the GPUs or reboot the VM to recover and resume workloads: 
     * **For Compute Engine VMs:** Reset the GPUs or [reboot the VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance). For more information about VM actions and lifecycle states, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).
     * **For GKE nodes:** Apply `kubectl label nodes NODE_NAME cloud.google.com/perform-reboot=true` to the impacted node to [trigger a guest OS reboot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#guest-os-reboot).

|  Google sends the machine to repair if the remap bank is exhausted or when the GPU requires physical repair or replacement.  
`Xid 92: _High single-bit ECC error rate_` | This Xid message is returned after the GPU driver corrects a correctable error, and it shouldn't affect your workloads. This Xid message is informational only. _No action is needed_.  |  None  
`Xid 94: _Contained error_` Indicates that a GPU error occurred and whether the error was contained within a single application. Alone, Xid 94 doesn't indicate the root cause of the error; it must be interpreted alongside other co-occurring Xid errors in order to determine the fundamental cause. | 

  1. Since the error was contained within a single application, restart the application to recover.
  2. If necessary, reset the GPUs or stop your workloads.
  3. Investigate other co-occurring Xid errors for further recovery steps and root-cause determination.

|  None  
`Xid 95: _Uncontained error_` Indicates that a GPU error occurred and was not contained to a single application. Alone, Xid 95 doesn't indicate the root cause of the error; it must be interpreted alongside other co-occurring Xid errors in order to determine the fundamental cause. | 

  1. Since the error was not contained, stop your workloads and reset the GPUs or [reboot the VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance) to recover.
  2. Investigate other co-occurring Xid errors to determine the underlying root cause and further recovery steps.

|  None  
  
### GSP errors

A [GPU System Processor](https://download.nvidia.com/XFree86/Linux-x86_64/510.39.01/README/gsp.html) (GSP) is a microcontroller that runs on GPUs and handles some of the low level hardware management functions.

**Xid error message** | **Customer action** | **Google action**  
---|---|---  
`Xid 119: _GSP RPC timeout_` | 

  1. Stop your workloads.
  2. Check [Recommended NVIDIA driver branches](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#recommended-driver-branches) to ensure you are using a supported branch and a recent or latest driver version, as driver bugs in earlier versions are a major cause of GSP errors.
  3. If the error persists after checking or updating your driver, then [delete](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) and [recreate the VM](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus). If the error continues, then collect the NVIDIA bug report and file a case with [Cloud Customer Care](https://docs.cloud.google.com/support/docs).

|  None. If the error persists and you file a support case, Google investigates hardware or driver state through the support workflow.  
`Xid 120: _GSP error_`  
  
### Illegal memory access errors

The following Xids are returned when applications have illegal memory access faults:

**Xid error message** | **Customer action** | **Google action**  
---|---|---  
`Xid 13: _Graphics Engine Exception_` `Xid 31: _GPU memory page fault_` `Xid 137: _Memory access fault_` A memory access violation was detected, analogous to a segmentation fault. These errors typically indicate an application bug where GPU memory is accessed out of bounds, or on freed buffers such as dereferencing an invalid pointer or an out-of-bounds array. These don't represent ECC errors unless Xid 48 is also present. |  To resolve this issue, debug the memory access faults in your application. You can use [cuda-gdb](https://docs.nvidia.com/cuda/cuda-gdb/index.html), [Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html), or [cuda-memcheck](https://developer.nvidia.com/cuda-memcheck). For more details, see the [NVIDIA Xid documentation](https://docs.nvidia.com/deploy/xid-errors/index.html). |  None. In rare cases where hardware degradation might cause falsely reported illegal memory access errors, you can use [NVIDIA Data Center GPU Manager (DCGM)](https://developer.nvidia.com/dcgm) to run `dcgmi diag -r 3` or `dcgmi diag -r 4` for different levels of test coverage and duration. If you identify a hardware issue, then file a case with [Customer Care](https://docs.cloud.google.com/support/docs).  
  
### Other common Xid error messages

**Xid error message** | **Customer action** | **Google action**  
---|---|---  
`Xid 74: _NVLINK error_` | 

  1. Stop your workloads.
  2. Reset the GPUs.

|  None  
`Xid 79: _GPU has fallen off the bus_` This means the driver isn't able to communicate with the GPU because a hardware issue caused the GPU to disappear from the PCI bus. |  To recover your workloads, use either of the following approaches, depending on whether [emergency maintenance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations#emergency-notifications) is enabled for your project:

  * **Request an emergency maintenance:** If emergency maintenance is rolled out to your project, then trigger the maintenance event at your convenience.
  * **Wait for automated maintenance:** Otherwise, wait for an unplanned maintenance event right on the instance.

|  Google detects that the GPU has fallen off the PCI bus and sends the machine to repair.  
`Xid 109: _Context switch timeout_` Xid 109 is a generic error reported by the NVIDIA GPU driver, generated when a GPU instance fails to preempt or switch tasks within the expected timeout period. Google has a long history of investigating Xid 109 with NVIDIA, and known causes from driver bugs are fixed in the latest drivers. Xid 109 is not caused by a hardware issue. | 

  1. Stop your workloads.
  2. Depending on your environment, reset the GPUs or reboot the VM to recover and resume workloads: 
     * **For Compute Engine VMs:** Reset the GPUs or [reboot the VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance). For more information about VM actions and lifecycle states, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).
     * **For GKE nodes:** Apply `kubectl label nodes NODE_NAME cloud.google.com/perform-reboot=true` to the impacted node to [trigger a guest OS reboot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#guest-os-reboot).
  3. Consider upgrading to a newer NVIDIA driver version for your environment such as [installing the latest driver on your Compute Engine VM](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) or upgrading your GKE node pool/driver DaemonSet.

|  None  
`Xid 149` that mentions `0x02a`, such as the following example: 
    
    
    Xid (PCI:0000:c0:00): **149** ,NETIR_LINK_EVT Fatal XC0 i0 Link 04 (**0x02a** 485c6 0x00000000 0x00000000 0x00000000 0x00000000 0x00000000)

This indicates a [known issue affecting firmware for NVIDIA B200 GPUs](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#a4-firmware). | 

  1. Stop your workloads.
  2. Reset the GPUs.

|  None  
  
## Troubleshoot `nvidia-smi` failure after OS patching or kernel upgrade

If `nvidia-smi` fails with `NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver` after a maintenance window, OS patching run, or VM reboot, check your kernel package holds. Package locks from a previous driver installation in `binary` mode can prevent the installation of matching kernel headers.

To diagnose and resolve this issue, select your operating system:

###  Ubuntu 

  1. Check the running kernel version:
         
         uname -r
         

  2. Check whether a previous driver installation in `binary` mode locked the kernel packages, such as when you use `--force-version`, `--installation-branch=lts`, or NVIDIA RTX Virtual Workstation (vWS) compute instances:
         
         apt-mark showhold
         

Check whether `linux-image-gcp` or `linux-headers-gcp` is listed.

  3. Verify whether kernel headers are installed for the running kernel:
         
         dpkg -l | grep "linux-headers-$(uname -r)"
         

  4. If the kernel meta-packages are held, then remove the package locks:
         
         sudo apt-mark unhold linux-image-gcp linux-headers-gcp
         

  5. Install the kernel headers for the running kernel:
         
         sudo apt-get update && sudo apt-get install -y linux-headers-$(uname -r)
         

  6. Rebuild and load the NVIDIA kernel module:

     * If DKMS module sources are registered (check `sudo dkms status`):
           
           sudo dkms autoinstall
           sudo modprobe nvidia
           nvidia-smi
           

     * If `sudo dkms status` shows no registered NVIDIA module (for example, if the driver was previously installed using a `.run` binary without `--dkms`), rerun the Google Cloud GPU driver installer:
           
           sudo python3 cuda_installer.pyz install_driver
           




###  Debian 

  1. Check the running kernel version:
         
         uname -r
         

  2. Check whether a previous driver installation in `binary` mode locked the kernel packages, such as when you use `--force-version`, `--installation-branch=lts`, or NVIDIA RTX Virtual Workstation (vWS) compute instances:
         
         apt-mark showhold
         

Check whether `linux-image-cloud-amd64` or `linux-headers-cloud-amd64` is listed.

  3. Verify whether kernel headers are installed for the running kernel:
         
         dpkg -l | grep "linux-headers-$(uname -r)"
         

  4. If the kernel meta-packages are held, then remove the package locks:
         
         sudo apt-mark unhold linux-image-cloud-amd64 linux-headers-cloud-amd64
         

  5. Install the kernel headers for the running kernel:
         
         sudo apt-get update && sudo apt-get install -y linux-headers-$(uname -r)
         

  6. Rebuild and load the NVIDIA kernel module:

     * If DKMS module sources are registered (check `sudo dkms status`):
           
           sudo dkms autoinstall
           sudo modprobe nvidia
           nvidia-smi
           

     * If `sudo dkms status` shows no registered NVIDIA module (for example, if the driver was previously installed using a `.run` binary without `--dkms`), rerun the Google Cloud GPU driver installer:
           
           sudo python3 cuda_installer.pyz install_driver
           




###  RHEL and Rocky Linux 

  1. Check the running kernel version:
         
         uname -r
         

  2. Check whether a previous driver installation in `binary` mode locked the kernel packages, such as when you use `--force-version`, `--installation-branch=lts`, or NVIDIA RTX Virtual Workstation (vWS) compute instances:
         
         grep "^exclude=.*kernel" /etc/dnf/dnf.conf
         

  3. Verify whether kernel headers are installed for the running kernel:
         
         rpm -qa | grep "kernel-devel-$(uname -r)"
         

  4. If kernel packages are excluded, then remove `kernel*` from the `exclude=` line in `/etc/dnf/dnf.conf`.

  5. Install the kernel headers for the running kernel:
         
         sudo dnf install -y kernel-devel-$(uname -r) kernel-headers-$(uname -r)
         

  6. Rebuild and load the NVIDIA kernel module:

     * If DKMS module sources are registered (check `sudo dkms status`):
           
           sudo dkms autoinstall
           sudo modprobe nvidia
           nvidia-smi
           

     * If `sudo dkms status` shows no registered NVIDIA module (for example, if the driver was previously installed using a `.run` binary without `--dkms`), rerun the Google Cloud GPU driver installer:
           
           sudo python3 cuda_installer.pyz install_driver
           




## Troubleshooting Secure Boot

If you install the NVIDIA driver on a compute instance with [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) enabled and `nvidia-smi` fails to communicate with the NVIDIA driver, then Secure Boot might block the unsigned kernel module from loading.

To diagnose and resolve this issue, complete the following steps:

  1. Check whether Secure Boot rejected the kernel module due to a missing or invalid signature:
         
         sudo dmesg | grep -iE 'secure boot|nvidia'
         

  2. If Secure Boot blocked the module, then manually sign the driver modules and enroll your Machine Owner Key (MOK), or use an OS image with pre-signed kernel modules. For instructions, see [Install GPU drivers (Secure Boot VMs)](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#secure-boot).




## Reset GPUs

Some issues might require you to reset your GPUs. To reset GPUs, complete the following steps:

  * For N1, G2, A2, and G4 VMs with one or more GPUs attached, [reboot the VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance).
  * For G4 VMs with [fractional GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) (less than one GPU attached), complete the following steps: 
    1. [Delete the VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).
    2. [Recreate the VM](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).
  * For A3, A4, A4X, and A4X Max instances, run `sudo nvidia-smi --gpu-reset`. 
    * For most Linux VMs, the `nvidia-smi` executable is located in the `/var/lib/nvidia/bin` directory.
    * For GKE nodes, the `nvidia-smi` executable is located in the `/home/kubernetes/bin/nvidia` directory.
  * For A3, A4, A4X, and A4X Max instances on GKE nodes, you can also use the [gpu-reset-tool](https://github.com/ai-on-gke/tutorials-and-examples/tree/main/gpu-reset-tool) to automate the reset of all GPUs on a node. This tool requires only that you specify the target node name.



Alternatively, GPUs are also reset whenever you [reset a VM](https://docs.cloud.google.com/compute/docs/instances/reset-instance) or [stop and restart a VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance). For more information about VM lifecycle states and the differences between VM recovery actions, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle) and [Suspend, stop, or reset Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview).

## Open a support case

If you're unable to resolve the issues by using the guidance on this page, then gather the following information and [open a support case](https://docs.cloud.google.com/support/docs):

  * **Project ID** of the project where the affected instances are located.
  * **List of all instance names or IDs** in the cluster.
  * **List of suspect nodes** identified through troubleshooting.
  * **Complete, non-interleaved NCCL logs** with debug settings enabled.
  * **Output from hardware health checks** (`dcgmi`, `nvidia-smi`).
  * **Exact benchmark or workload command** that is failing.
  * **Relevant log files** such as host engine and diagnostic logs. To gather these, run `gather-dcgm-logs.sh`, located in `/usr/local/dcgm/scripts` in default installations.
  * **NVIDIA bug report**. Run `nvidia-bug-report.sh`. For Blackwell GPUs, follow [Generate NVIDIA Bug Report for Blackwell GPUs](https://docs.cloud.google.com/compute/docs/troubleshooting/generate-nvidia-bug-report-for-blackwell-gpus).
  * Details about any recent changes that were made to your environment preceding the failure.



## What's next

Review [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
