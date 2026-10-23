---
url: https://docs.cloud.google.com/ull-solution/participants/use-onload/
title: Work with Onload \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:36.708972+00:00
---

# Work with Onload  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/use-onload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Work with Onload

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes how to use Onload with U4 Compute Engine instances.

## About Onload

[Onload](https://github.com/Xilinx-CNS/onload) is a high-performance network stack for latency-sensitive applications that require ultra-low latency, minimal jitter, and consistent performance. Onload provides a TCP/IP implementation that bypasses the operating system kernel and runs directly in the user space while enabling applications to use standard BSD socket APIs.

Using Onload with ULL Solution includes support for the following:

  * **Flow steering** : You can bypass default Receive Side Scaling (RSS) hashing by [steering specific traffic flows](https://www.kernel.org/doc/Documentation/networking/scaling.txt) directly to a designated [Receive Queue (RX)](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx). 3-tuple flow steering is supported (protocol, destination IP address, destination port).



## Before you begin

Before you work with Onload on U4 Compute Engine instances, you must meet the following requirements.

### Create a U4 instance

If you haven't already, create a U4 Compute Engine instance by using one of the following procedures that include the required configuration for Onload:

  * To create a U4P or U4C bare metal instance, see [Create ULL Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/create-ull-instances).
  * To create a U4S virtual machine (VM) instance, see [Create non-ULL Compute Engine instances for auxiliary workloads](https://docs.cloud.google.com/ull-solution/participants/create-non-ull-instances).



### Connect to your instance by using SSH

If you haven't already, [connect to your instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

### Switch to the root user

The commands and scripts in the following procedures modify system-level settings, kernel parameters, and network interfaces. To run them successfully, you must execute them as the root user. You can switch to a root shell by running `sudo su`, or add `sudo` before running commands as needed.

## Set up Onload

This section describes the steps required to set up Onload on a U4 instance.

### Install dependencies

  1. If you are using Rocky Linux, enable the CodeReady Builder (CRB) repository. If you are using Red Hat Enterprise Linux (RHEL), skip this step.
         
         dnf -y config-manager --enable crb
         

  2. Install the required dependencies for Onload:
         
         dnf -y install git clang numactl \
            python3-setuptools \
            linuxptp \
            libcap-devel libbpf-devel libxdp-devel
         




### Pull Onload source

To pull the [`onload`](https://github.com/Xilinx-CNS/onload) repository with the required changes, run the following commands:
    
    
    umask 0022
    mkdir -p /usr/src/
    
    git clone https://github.com/Xilinx-CNS/onload /usr/src/onload
    
    # Latest commit on v9_2 branch to which patches can be applied cleanly
    git -C /usr/src/onload checkout f4283aa7258cbaaf1f0c9946a67176b1b4997003
    
    # Verify tree hash for the base commit
    [[ "$(git -C /usr/src/onload rev-parse HEAD^{tree})" \
        == "e6e6f1e86ae667050433049f2c23d674f013f794" ]] || \
        { echo "ERROR: mismatch tree hash"; exit 1; }
    
    # Pull Google-specific Onload changes not yet merged as of v9_2
    curl -L https://github.com/Xilinx-CNS/onload/pull/279.patch | git -C /usr/src/onload am -3
    curl -L https://github.com/Xilinx-CNS/onload/pull/282.patch | git -C /usr/src/onload am -3
    curl -L https://github.com/Xilinx-CNS/onload/pull/325.patch | git -C /usr/src/onload am -3
    curl -L https://github.com/Xilinx-CNS/onload/pull/327.patch | git -C /usr/src/onload am -3
    curl -L https://github.com/Xilinx-CNS/onload/pull/342.patch | git -C /usr/src/onload am -3
    
    # Verify tree hash after applying patches
    [[ "$(git -C /usr/src/onload rev-parse HEAD^{tree})" \
        == "4215562a6f4806c36598a52767bac2a76268c5c8" ]] || \
        { echo "ERROR: mismatch tree hash"; exit 1; }

### Build Onload

To build Onload, run the following commands:
    
    
    cd /usr/src/onload
    USEONLOADEXT=1 ./scripts/onload_install --no-sfc
    
    pushd ./src/tools/bpf_link_helper
    clang xdp_onload_prepare.c  -lbpf -o xdp_onload_prepare
    clang -target bpf -O2 -g -c xdp_tstamp.c -o ./xdp_tstamp.o
    popd

### Disable Indirect Branch Tracking (IBT)

IBT must be disabled to use Onload as described in [Indirect Branch Tracking (IBT) Incompatibility ](https://docs.amd.com/r/en-US/ug1586-onload-user/Indirect-Branch-Tracking-IBT-Incompatibility).

To disable IBT, run the following commands:
    
    
    grubby --args="ibt=off" --update-kernel=ALL
    reboot

### Load Onload

This section describes how to load Onload on your instance.

#### Load Onload on a U4P or U4C instance

To load Onload on a U4P or U4C bare metal instance, use the following script.
    
    
    IFNAMES=($( find /sys/class/net -type l -not -lname '*virtual*' -printf '%l %f\n' | sort | awk '{print $2}'))
    
    for IFNAME in "${IFNAMES[@]}"; do
      ethtool -L "${IFNAME}" rx 16 tx 16
      ethtool -G "${IFNAME}" rx 1024 rx-buf-len 2048
      ethtool -K "${IFNAME}" ntuple on
      ethtool -K "${IFNAME}" rx-gro-hw off
      echo 0 > "/sys/class/net/${IFNAME}/threaded"
      /usr/src/onload/src/tools/bpf_link_helper/xdp_onload_prepare \
        "${IFNAME}" /usr/src/onload/src/tools/bpf_link_helper/xdp_tstamp.o
    done
    
    setenforce 0
    numactl --cpunodebind=0,2 onload_tool reload --onload-only
    for IFNAME in "${IFNAMES[@]}"; do
      echo "${IFNAME}" 16 > /sys/module/sfc_resource/afxdp/register
      until [[ $(cat "/sys/class/net/${IFNAME}/carrier") == 1 ]]; do
        sleep 1
      done
      hwstamp_ctl -i "${IFNAME}" -r 1
    done
    
    echo 1 > /sys/module/sfc_resource/parameters/enable_af_xdp_flow_filters
    echo 256 > /sys/module/onload/parameters/xdp_headroom
    echo -1 > /sys/module/onload/parameters/inject_kernel_gid

#### Load Onload on a U4S instance

To load Onload on a U4S VM instance, use the following script.
    
    
    IFNAME=NIC_NAME
    ALLOCATED_QUEUES=ALLOCATED_QUEUES
    
    ethtool -L "$IFNAME" rx "${ALLOCATED_QUEUES}" tx "${ALLOCATED_QUEUES}"
    ethtool -G "$IFNAME" rx 1024 rx-buf-len 2048
    ethtool -K "$IFNAME" ntuple on
    ethtool -K "$IFNAME" rx-gro-hw off
    echo 0 > "/sys/class/net/${IFNAME}/threaded"
    /usr/src/onload/src/tools/bpf_link_helper/xdp_onload_prepare "$IFNAME" \
      /usr/src/onload/src/tools/bpf_link_helper/xdp_tstamp.o
    
    setenforce 0
    numactl --cpunodebind=0 onload_tool reload --onload-only
    
    echo "${IFNAME} ${ALLOCATED_QUEUES}" | tee /sys/module/sfc_resource/afxdp/register
    until [[ $(cat "/sys/class/net/${IFNAME}/carrier") == 1 ]]; do
        sleep 1
    done
    hwstamp_ctl -i "$IFNAME" -r 1
    
    echo 1 > /sys/module/sfc_resource/parameters/enable_af_xdp_flow_filters
    echo 256 > /sys/module/onload/parameters/xdp_headroom
    echo -1 > /sys/module/onload/parameters/inject_kernel_gid

Replace the following:

  * `NIC_NAME`: the OS name of the network interface, such as `enp22s0f0`.
  * `ALLOCATED_QUEUES`: the number of receive (RX) and transmit (TX) queues to allocate for Onload on the network interface. Set this value to half the total number of RX or TX queues assigned to the vNIC.

For U4S instances, the total queue count (for RX or TX queues respectively) is equal to `num_vcpus / num_vnics`, up to a maximum of `16` queues per vNIC. For example, if the vNIC has `4` total TX queues, set this value to `2`. If the vNIC has `16` total TX queues, set this value to `8`.

For more information about default queue allocation, see [Receive and transmit queues](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx).




### Configure Onload flags

To optimize performance and help reduce latency, you can use the following set of environment variables and flags when running your applications with Onload. This section includes recommended settings that you can adjust as needed for your applications.

You must specify these parameters before your application commands. For example, to run an application with these settings, use the following format:
    
    
    env EF_NO_FAIL=0 \
      EF_POLL_USEC=100000 \
      EF_RX_TIMESTAMPING=3 \
      EF_MAX_ENDPOINTS=1048576 \
      EF_WODA_SINGLE_INTERFACE=1 \
      EF_UL_EPOLL=3 \
      EF_USE_HUGE_PAGES=0 \
      EF_EPOLL_CTL_HANDOFF=0 \
      EF_FDS_MT_SAFE=0 \
      EF_NONAGLE_INFLIGHT_MAX=-1 \
      EF_RXQ_SIZE=4096 \
      EF_TCP_RCVBUF_ESTABLISHED_DEFAULT=65536 \
      EF_MAX_PACKETS=65536 \
      EF_PREFAULT_PACKETS=65536 \
      EF_EVS_PER_POLL=256 \
      onload -v --profile=latency APPLICATION_COMMAND

### Unload Onload

To unload Onload, use the following script.
    
    
    IFNAMES=($( find /sys/class/net -type l -not -lname '*virtual*' -printf '%l %f\n' | sort | awk '{print $2}'))
    
    for IFNAME in "${IFNAMES[@]}"; do
      rm -f "/sys/fs/bpf/onload_xdp_xsk_${IFNAME}"
    done
    
    onload_tool unload --onload-only
    
    for IFNAME in "${IFNAMES[@]}"; do
      # (optional) Disable threaded busypolling in case it's up. See busypolling
      # section
      echo 0 > "/sys/class/net/${IFNAME}/threaded"
    
      ip link set dev "${IFNAME}" xdp off
    done

### Configure a `systemd` service that automatically starts Onload

To automatically start Onload when your instance boots, you can register it as a [`systemd` service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html). Create a service file using the following template:
    
    
    [Unit]
    Description=ULL Solution -- Loading & instance tuning for Onload
    After=network-online.target
    After=google-guest-agent-manager.service google-guest-agent.service
    Before=multi-user.target
    Before=sshd.service
    
    [Service]
    Type=oneshot
    RemainAfterExit=yes
    ExecStart=START_SCRIPT_PATH
    ExecStartPost=OPTIMIZATION_SCRIPT_PATH
    ExecStop=STOP_SCRIPT_PATH
    
    [Install]
    WantedBy=multi-user.target
    

Replace the following:

  * `START_SCRIPT_PATH`: the path to the script that starts Onload, such as one of the scripts in Load Onload.
  * `OPTIMIZATION_SCRIPT_PATH`: the path to the optional script that applies optimization configurations. If desired, you can create a script that includes your performance optimizations and include it here. Otherwise, you can remove the line that includes this variable.
  * `STOP_SCRIPT_PATH`: the path to the script that stops Onload, such as the script in Unload Onload.



## Configure busy polling

This section provides examples of how to configure busy polling on your instance.

Busy polling continuously checks for new network packets instead of waiting for device interrupts, which helps reduce latency and jitter. For more information about busy polling, see [Busy polling](https://docs.kernel.org/networking/napi.html#busy-polling) in the Linux Kernel documentation.

### Get the RX queue that an Onload stack is using

To get the RX queue that an Onload stack is using, do the following:

  1. Get the Onload stack ID by running [`onload_stackdump`](https://docs.amd.com/r/en-US/ug1586-onload-user/onload_stackdump):
         
         onload_stackdump
         

  2. Because the Onload stack ID and NAPI queue ID might not always match, use the following script to get the corresponding interface name, index, and queue ID from a stack ID.
         
         ONLOAD_STACK=ONLOAD_STACK_ID
         
         INTF_HWPORT_MAP=($(onload_stackdump "${ONLOAD_STACK}" netif_extra | grep -oP "intf_i_to_hwport=\K.*$" | tr ',' '\n'))
         HWPORT_IFINDEX_MAP=($(onload_stackdump "${ONLOAD_STACK}" hwport_to_base_ifindex | grep -oP "\d+$"))
         while read -r INTF_ID QUEUE_ID; do
          HW_PORT="${INTF_HWPORT_MAP[INTF_ID]}"
          IFINDEX="${HWPORT_IFINDEX_MAP[HW_PORT]}"
          IFNAME=$(ip -j link | jq -r ".[] | select(.ifindex == ${IFINDEX}) | .ifname")
          echo "ifname=${IFNAME} ifindex=${IFINDEX} queue_id=${QUEUE_ID}"
         done < <(onload_stackdump "${ONLOAD_STACK}" netif | grep -oP "((intf|vi)=)\K\d+" | xargs -n 2)

Replace `ONLOAD_STACK_ID` with the ID of the stack for which you want to enable or disable busy polling.

  3. Record the values to use when you enable or disable busy polling in the following sections.




### Enable busy polling on an RX queue

This section provides an example of how you can enable busy polling on a specific [RX queue](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) that an Onload stack is using.

  1. Run the following bash script in your terminal. The `enable_single_queue` function does the following:

     * Gets the `napi_id` that corresponds to an RX queue by using netlink (`ynl`)
     * Sets the `threaded: busy-poll` property on the `napi_id`
     * Gets the `kthread_pid` of the thread that is busy polling the `napi_id`
     * Uses `taskset` to bind the `kthread_pid` to a specific CPU
    
    readonly NETDEV_YAML=${NETDEV_YAML:-"/usr/share/ynl/specs/netdev.yaml"}
    
    call_ynl() {
      ynl --spec "${NETDEV_YAML}" "$@"
    }
    
    enable_single_queue() {
      local -r interface="$1"
      local -r ifindex=$(cat "/sys/class/net/${interface}/ifindex")
      local -r q_id="$2"
      local -r cpu="$3"
    
      local napi_id
      napi_id=$(call_ynl --output-json --do queue-get \
        --json "{\"ifindex\": ${ifindex}, \"id\": ${q_id}, \"type\": \"rx\"}" | \
        jq -r '."napi-id"')
    
      if [[ -z "${napi_id}" || "${napi_id}" == "null" ]]; then
        echo "Error: No napi_id found for queue ${q_id} on interface ${interface}" >&2
        exit 1
      fi
    
      echo "Enabling busypolling for queue ${q_id} (NAPI ${napi_id}) on CPU ${cpu}"
      call_ynl --do napi-set --json "{\"id\": \"${napi_id}\", \"threaded\": \"busy-poll\"}" >/dev/null
    
      local napi_kthread_pid
      napi_kthread_pid=$(call_ynl --do napi-get --output-json \
        --json "{\"id\": \"${napi_id}\"}" | jq -r '."pid" // empty')
    
      if [[ -z "${napi_kthread_pid}" ]]; then
        echo "Error: Could not get PID for NAPI ${napi_id}" >&2
        exit 1
      fi
    
      taskset -pc "${cpu}" "${napi_kthread_pid}" >/dev/null
    }

  2. Run the following command to invoke the `enable_single_queue` function:
         
         enable_single_queue NIC_NAME QUEUE_ID CPU_ID
         

Replace the following:

     * `NIC_NAME`: the OS name of the network interface, such as `ens8f0`.
     * `QUEUE_ID`: the queue ID that you got previously.
     * `CPU_ID`: the ID of the CPU on which to run the busy polling thread, such as `5`.
  3. Ensure that you plan for thread re-creation events that might affect your busy polling configuration.




#### Plan for thread re-creation events

When the kernel re-creates a thread, associated thread configurations don't persist, such as its CPU affinity mask and scheduling policy. Events such as the following cause the kernel to re-create a thread that is busy polling NAPI:

  * Link flaps/resets
  * XDP program attachments (for example, when running the scripts to load Onload or attaching custom XDP programs)
  * Ring parameter changes (`ethtool -G`)
  * Queue count changes (`ethtool -L`)



To help prevent issues, consider avoiding tasks that cause thread re-creation events during normal operations.

To maintain your busy polling configuration after a thread is re-created, you must obtain the new Process ID (PID) of the thread and re-bind it to the CPU. You can do this by running the `enable_single_queue` function again.

### Disable busy polling on an RX queue

This section provides an example of how you can disable busy polling on a specific [RX queue](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) that an Onload stack is using.

  1. Get the RX queue that an Onload stack is using by running [`onload_stackdump`](https://docs.amd.com/r/en-US/ug1586-onload-user/onload_stackdump):
         
         onload_stackdump
         

  2. Run the following bash script in your terminal. The `disable_single_queue` function does the following:

     * Gets the `napi_id` that corresponds to an RX queue by using netlink (`ynl`)
     * Sets the threaded property of the `napi_id` to `disabled`
    
    disable_single_queue() {
      local -r interface="$1"
      local -r ifindex=$(cat "/sys/class/net/${interface}/ifindex")
      local -r q_id="$2"
    
      local napi_id
      napi_id=$(call_ynl --output-json --do queue-get \
        --json "{\"ifindex\": ${ifindex}, \"id\": ${q_id}, \"type\": \"rx\"}" | \
        jq -r '."napi-id"')
    
      if [[ -z "${napi_id}" || "${napi_id}" == "null" ]]; then
        echo "Error: No napi_id found for queue ${q_id} on interface ${interface}" >&2
        exit 1
      fi
    
      echo "Disabling busypolling for queue ${q_id} (NAPI ${napi_id})"
      call_ynl --do napi-set --json "{\"id\": \"${napi_id}\", \"threaded\": \"disabled\"}" >/dev/null
    }

  3. Run the following command to invoke the `disable_single_queue` function:
         
         disable_single_queue NIC_NAME QUEUE_ID
         

Replace the following:

     * `NIC_NAME`: the OS name of the network interface, such as `ens8f0`.
     * `QUEUE_ID`: the queue ID that you got previously.



### Get busy polling status of a queue

To check the NAPI status of a queue to see if it is busy polling, you can use the following commands:
    
    
    IFNAME=NIC_NAME
    QUEUE_ID=QUEUE_ID
    QUEUE_TYPE=QUEUE_TYPE
    
    IFINDEX=$(cat "/sys/class/net/${IFNAME}/ifindex")
    NAPI_ID=$(ynl --spec /usr/share/ynl/specs/netdev.yaml \
      --output-json --do queue-get \
      --json '{"ifindex": '${IFINDEX}', "id": '${QUEUE_ID}', "type": "'${QUEUE_TYPE}'"}' | \
      jq '."napi-id"')
    ynl --spec /usr/share/ynl/specs/netdev.yaml \
      --output-json --do napi-get \
      --json '{"id": '${NAPI_ID}'}' | jq -r '"status: \(.threaded)"'

Replace the following:

  * `NIC_NAME`: the OS name of the network interface, such as `ens8f0`.
  * `QUEUE_ID`: the ID of the queue that you want to check.
  * `QUEUE_TYPE`: `rx` or `tx`.



## Optimize performance

This section provides general guidance for optimizing the performance of your U4 bare metal instances (U4P and U4C). Adjust the examples in this guidance as needed for your workloads.

### Review the NUMA topology for U4 bare metal instances

The following table describes which network interfaces use which NUMA nodes for U4 bare metal instances:

NIC (Google Cloud name) | NIC (OS name) | NUMA node | PCIE BDF  
---|---|---|---  
`nic0` | `enp22s0f0` | 0 | `0000:16:00.0`  
`nic1` | `ens8f0` | 0 | `0000:27:00.0`  
`nic2` | `ens48f0` | 2 | `0000:b8:00.0`  
  
The preceding table includes typical OS-assigned network interface names for RHEL. The actual names might be different.

### Determine a CPU isolation scheme

For best performance, we recommend that you isolate the following:

  * The CPUs that are used by your application
  * The CPUs that are used to busy poll the Onload RX queues
  * The CPUs that are used for kernel and driver interrupts



The following table provides an example of how you can isolate CPUs on U4 bare metal instances. Adjust the mapping as needed for your workloads, for example you might want more application CPUs.

Purpose | CPUs  
---|---  
General kernel interrupts | 0,1,30,31,60,61,90,91  
`nic0` driver interrupts for queues 0-11 | 2  
`nic1` driver interrupts for queues 0-11 | 3  
`nic0` and `nic1` driver interrupts for queues 12-15 | 4  
`nic1` busy polling | 5-16  
`nic1` application threads (Onload) | 17-29  
`nic0` busy polling | 32-43  
`nic0` application threads (Onload) | 44-59  
`nic2` driver interrupts for queues 0-11 | 62  
`nic2` driver interrupts for queues 12-15 | 63  
`nic2` busy polling | 64-75  
`nic2` application threads (Onload) | 76-89  
  
### Install dependencies for performance optimization

To install the required dependencies for performance optimization, run the following command:
    
    
    dnf -y install numactl tuna jq
    

### Configure kernel boot parameters

To isolate CPUs from kernel scheduling, run the following command. This also disables Intel QuickAssist Technology (QAT) so that it doesn't interfere with your isolated cores.

The following example command isolates CPUs `2-29`, `32-59`, and `62-89` and designates `0,1,30,31,60,61,90,91` for general kernel interrupts. These values correspond to the example CPU isolation scheme. Replace the values as needed depending on your CPU isolation scheme.
    
    
    grubby --args="isolcpus=domain,managed_irq,2-29,32-59,62-89 nohz=on nohz_full=2-29,32-59,62-89 rcu_nocbs=2-29,32-59,62-89 irqaffinity=0,1,30,31,60,61,90,91 rcu_nocb_poll modprobe.blacklist=intel_qat,qat_4xxx" --update-kernel=ALL
    reboot

### Configure post-boot CPU isolation

To isolate CPUs after boot, run the following command. The values correspond to the example CPU isolation scheme. Replace the values as needed depending on our CPU isolation scheme.
    
    
    tuna isolate -c 2-29,32-59,62-89
    

### Assign queue interrupts to specific CPUs

This section describes how to move `gve` queue interrupt requests (IRQs) to specific CPUs. The `gve` driver is used by the `GVNIC` network interface type in Google Cloud.

  1. Determine the IRQs for a given network interface and queue range. See the following bash example, which defines an `irq_list` function.
         
         irq_list() {
           local ifname=$1
           local queue_begin=$2
           local queue_end=$3
         
           pci_name=$(basename $(readlink /sys/class/net/${ifname}/device))
           rx_ntfy_blk_start=$(ethtool -l "${ifname}" | awk '
             /Pre-set maximums:/ { in_preset = 1 }
             /Current hardware settings:/ { in_preset = 0 }
             in_preset && $1 == "RX:" { rx = $2 }
             in_preset && $1 == "TX:" { tx = $2 }
             END { print int((rx + tx) / 2) }
           ')
           for i in $(seq "${queue_begin}" "${queue_end}"); do
             irq_tx="gve-ntfy-blk${i}@pci:${pci_name}"
             irq_rx="gve-ntfy-blk$(($i + rx_ntfy_blk_start))@pci:${pci_name}"
             # gve IRQ names are stored in a char[IFNAMSIZ + 16] so capped to 31 characters.
             echo "${irq_tx:0:31}"
             echo "${irq_rx:0:31}"
           done | paste -sd ','
         }

  2. Assign IRQs to the appropriate CPU based on your CPU isolation scheme. The following example script uses `tuna` and the `irq_list` function from the previous step:
         
         tuna move -c 2 -q "$(irq_list enp22s0f0 0 11)"
         tuna move -c 4 -q "$(irq_list enp22s0f0 12 15)"
         
         tuna move -c 3 -q "$(irq_list ens8f0 0 11)"
         tuna move -c 4 -q "$(irq_list ens8f0 12 15)"
         
         tuna move -c 62 -q "$(irq_list ens48f0 0 11)"
         tuna move -c 63 -q "$(irq_list ens48f0 12 15)"




### Configure OS and device settings

  1. Run the following script to configure settings that help minimize latency and prevent default OS behaviors from interfering with your Onload configurations.
         
         echo 0 > /proc/sys/net/core/busy_poll
         echo 0 > /proc/sys/net/core/busy_read
         echo 0 > /proc/sys/kernel/timer_migration
         echo 0 > /proc/sys/net/core/rps_sock_flow_entries
         echo -1 > /proc/sys/kernel/sched_rt_runtime_us
         
         for IFNAME in "${IFNAMES[@]}"; do
           ethtool -C "${IFNAME}" rx-usecs 0 tx-usecs 0
           echo 0 > "/sys/class/net/${IFNAME}/napi_defer_hard_irqs"
           echo 15000 > "/sys/class/net/${IFNAME}/gro_flush_timeout"
         done

  2. To steer traffic away from queues that are dedicated to Onload workloads, use RSS (`ethtool -X`). The following example script is based on the values in the example CPU isolation scheme. Because Onload uses queues `0-11`, the script directs all other traffic to queues `12-15`.
         
         for IFNAME in "${IFNAMES[@]}"; do
           ethtool -X "${IFNAME}" weight 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1
         done




## What's next

  * To synchronize your instance system clock to the physical NIC clock of its host server, see [Configure accurate time](https://docs.cloud.google.com/ull-solution/participants/configure-time-sync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
