---
url: https://docs.cloud.google.com/security-command-center/docs/investigate-vmtd-kernel-tampering-findings/
title: Inspect a VM for signs of kernel memory tampering \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:45.983568+00:00
---

# Inspect a VM for signs of kernel memory tampering  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/investigate-vmtd-kernel-tampering-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Inspect a VM for signs of kernel memory tampering Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes tasks that you can perform to confirm the validity of a [kernel-mode rootkit finding](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#kernel-mode-rootkit-threat-findings) from Virtual Machine Threat Detection. Kernel-mode rootkit findings indicate that a VM's kernel memory has potentially been tampered with by malware.

When you receive a kernel-mode rootkit finding from VM Threat Detection, we recommend that you run these Linux commands on the affected Compute Engine instance to probe your system for data points that might indicate anomalies, like hijacked system calls or hidden kernel modules.

Alternatively, you can run the provided data collection script on the affected VM. The script executes the commands that are described on this page.

Unless otherwise stated, each inspection task on this page is relevant to all kernel-mode rootkit findings.

This document assumes the following:

  * You are performing the tasks in this document after receiving a kernel-mode rootkit finding from VM Threat Detection. For a list of the relevant finding categories, see [Kernel-mode rootkit threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#kernel-mode-rootkit-threat-findings).

  * You have an understanding of Linux command-line tools and the Linux kernel.




## About VM Threat Detection

Virtual Machine Threat Detection is a built-in service of Security Command Center. This service scans virtual machines to detect potentially malicious applications, such as cryptocurrency mining software, kernel-mode rootkits, and malware running in compromised cloud environments.

VM Threat Detection is part of the Security Command Center threat detection suite and is designed to complement the existing capabilities of [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).

For information about VM Threat Detection, see [Virtual Machine Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview). To learn how to view the details of a VM Threat Detection finding, see [Review findings in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection#findings-vmtd).

## Before you begin

To get the permissions that you need to view all resources and findings in Security Command Center and manage the affected Compute Engine instance, ask your administrator to grant you the following IAM roles: 

  * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`) on the organization
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the Compute Engine instance



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Identify the affected VM

  1. [View the details of the finding](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection#findings-vmtd).
  2. In the **Affected resource** section, in the **Resource full name** field, click the link. The details view of the affected Compute Engine instance opens on a new tab.
  3. Connect to the instance. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) in the Compute Engine documentation.



## Find unexpected kernel modules

The presence of unexpected modules in a VM can indicate that the kernel memory of the VM is potentially compromised.

To find unexpected kernel modules, follow these steps:

  1. List all loaded kernel modules in the VM:
         
         lsmod
         cat /proc/modules
         

  2. List the `sysfs` entries for the loaded and unloaded modules:
         
         ls -l /sys/module/
         

  3. Compare the results of these lists with lists from other VMs in the project. Look for modules that appear in the affected VM but not in the other VMs.




## Search `syslog` for out-of-tree modules

Signs that an out-of-tree module has been loaded in a VM can indicate that atypical kernel modules have been loaded. You can search the kernel log buffer and `syslog` messages to determine if an out-of-tree module has been loaded. In the log entries, an out-of-tree module is marked as tainted load.

In the kernel log buffer and the `syslog` messages, search for log entries that resemble the following:
    
    
    MODULE_NAME: loading out-of-tree module taints kernel.
    

  * Search the kernel log buffer for log entries indicating the presence of out-of-tree modules:
        
        sudo dmesg | grep out-of-tree
        

  * Search all `syslog` messages for log entries indicating the presence of out-of-tree modules:
        
        grep "out-of-tree" /var/log/syslog*
        




## Check for livepatching

Livepatching in a VM can interfere with VM Threat Detection detections and can trigger false-positive findings.

To check for livepatching, follow these steps:

  1. Check `syslog` for livepatching module installation and logging. Live patching typically modifies the kernel code by installing kernel `ftrace` points.
         
         sudo grep livepatch /var/log/syslog*
         

  2. Search for new kernel modules installed for livepatching (typically prefixed with `livepatch`):
         
         sudo lsmod | grep livepatch
         

  3. Search for patch files:
         
         sudo ls -l /sys/kernel/livepatch
         




For information about livepatching, see [Livepatch](https://docs.kernel.org/livepatch/livepatch.html) in the Linux Kernel documentation.

## Check for other potentially malicious activities detected in the VM

  1. In Security Command Center, [view the details of the VM Threat Detection finding](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection#findings-vmtd) that you are investigating.
  2. In the **Affected resource** section, in the **Resource full name** field, click the drop-down arrow and then click **Show all findings with this resource full name**. The findings query is updated to show only findings for this VM.
  3. Check for findings that point to potential cryptomining activities, malware, unusual IAM grants, and other security threats.



## Check whether antivirus software is causing a false-positive finding

Antivirus software can interfere with VM Threat Detection detections and can trigger false-positive findings.

## Check all running processes on the system

The presence of unexpected processes can indicate that the VM Threat Detection finding is valid and the VM has been compromised.

  1. List all processes that are running on the VM:
         
         ps -eAf
         

  2. Look for debugger processes—like `gdb`, `strace`, and `pstack`—that you don't typically run on this VM. Debugger processes can snoop on other processes.

  3. Look for other suspicious processes on the VM.




## Check the booted kernel

Check the booted kernel to identify your Linux kernel:
    
    
    cat /proc/version
    

If the value returned is not your expected kernel version, that can indicate a hijacking attack that is done by exploiting the `kexec` tool in the kernel. The `kexec` tool can softboot the system to use a different kernel.

## Additional task for `Unexpected system call handler`

Perform this task if you get a `Defense Evasion: Unexpected system call handler` finding.

Audit system calls and look for anomalies in their usage and invokers. The audit logs provide information about the invoking process and arguments for the system calls. You can also perform verification tasks to check for expected behaviors of common system calls. For more information, see Example inspection with the Diamorphine rootkit on this page.

## Additional task for `Unexpected interrupt handler`

Perform this task if you get a `Defense Evasion: Unexpected interrupt handler` finding.

List the live interrupt handlers on the system and compare the results with information from other similar VMs in the project. Unexpected interrupt handlers can indicate that the VM is compromised.

To list the live interrupt handlers, run the following command:
    
    
    cat /proc/interrupts
    

The output resembles the following:
    
    
               CPU0       CPU1
      0:         44          0   IO-APIC   0-edge      timer
      1:          9          0   IO-APIC   1-edge      i8042
      4:      17493          0   IO-APIC   4-edge      ttyS0
      8:          0          0   IO-APIC   8-edge      rtc0
      9:          0          0   IO-APIC   9-fasteoi   acpi
     12:          0        152   IO-APIC  12-edge      i8042
     24:         16          0   PCI-MSI 81920-edge      virtio2-config
     25:          0      40194   PCI-MSI 81921-edge      virtio2-inflate
     26:      58528          0   PCI-MSI 81922-edge      virtio2-deflate
     27:          0     966356   PCI-MSI 81923-edge      virtio2-stats
     28:          0          0   PCI-MSI 49152-edge      virtio0-config
     29:          0          0   PCI-MSI 49153-edge      virtio0-control
     30:          0          0   PCI-MSI 49154-edge      virtio0-event
     31:          0     555807   PCI-MSI 49155-edge      virtio0-request
     32:          0          0   PCI-MSI 98304-edge      virtio3-config
     33:        184          0   PCI-MSI 98305-edge      virtio3-input
     34:          0          0   PCI-MSI 65536-edge      virtio1-config
     35:     556203          0   PCI-MSI 65537-edge      virtio1-input.0
     36:     552746          1   PCI-MSI 65538-edge      virtio1-output.0
     37:          1     426036   PCI-MSI 65539-edge      virtio1-input.1
     38:          0     408475   PCI-MSI 65540-edge      virtio1-output.1
    

## Additional task for `Unexpected processes in runqueue`

Perform these steps if you get a `Defense Evasion: Unexpected processes in runqueue` finding. This section helps you gather additional data points to investigate your findings. These data points might not directly indicate a malware problem.

In this task, you review the per-CPU scheduler queue. Although some processes might be short-lived, you can still evaluate the scheduler queue behavior with the running processes per CPU to look for anomalous behavior.

  1. Display details about the amount of time each running process spends per CPU. This helps you see if a particular CPU is extremely busy. You can correlate the results to interrupts pinned to the CPU from `/proc/interrupts`.
         
         cat /proc/schedstat
         

For more information about this command, see [Scheduler Statistics](https://docs.kernel.org/scheduler/sched-stats.html) in the Linux Kernel documentation.

  2. List all current runnable tasks and details about context switches for each CPU.
         
         cat /proc/sched_debug
         

The output resembles the following:
         
         Sched Debug Version: v0.11, 5.4.0-1081-gke #87-Ubuntu
         ktime                                   : 976187427.733850
         sched_clk                               : 976101974.761097
         cpu_clk                                 : 976101973.335113
         jiffies                                 : 4538939132
         sched_clock_stable()                    : 1
         
         sysctl_sched
           .sysctl_sched_latency                    : 12.000000
           .sysctl_sched_min_granularity            : 1.500000
           .sysctl_sched_wakeup_granularity         : 2.000000
           .sysctl_sched_child_runs_first           : 0
           .sysctl_sched_features                   : 2059067
           .sysctl_sched_tunable_scaling            : 1 (logarithmic)
         
         cpu#0, 2199.998 MHz
           .nr_running                    : 0
           .nr_switches                   : 16250401
           .nr_load_updates               : 0
           .nr_uninterruptible            : 12692
           .next_balance                  : 4538.939133
           .curr->pid                     : 0
           .clock                         : 976101971.732857
           .clock_task                    : 976101971.732857
           .avg_idle                      : 880408
           .max_idle_balance_cost         : 500000
         
         runnable tasks:
          S           task   PID         tree-key  switches  prio     wait-time             sum-exec        sum-sleep
         -----------------------------------------------------------------------------------------------------------
          S        systemd     1     51740.602172    326778   120         0.000000    165741.786097         0.000000 0 0 /init.scope
          S       kthreadd     2   1482297.917240      1361   120         0.000000       112.028205         0.000000 0 0 /
          I      rcu_sched    11   1482642.606136   1090339   120         0.000000     17958.156471         0.000000 0 0 /
          S        cpuhp/1    15       537.058588         8   120         0.000000         2.275927         0.000000 0 0 /
          S  idle_inject/1    16        -2.994953         3    49         0.000000         0.012780         0.000000 0 0 /
          S    migration/1    17         0.000000    245774     0         0.000000      5566.508869         0.000000 0 0 /
          S    ksoftirqd/1    18   1482595.656315     47766   120         0.000000      1235.099147         0.000000 0 0 /
          I   kworker/1:0H    20       536.961474         5   100         0.000000         0.043908         0.000000 0 0 /
          S      kdevtmpfs    21     11301.343465       177   120         0.000000         3.195291         0.000000 0 0 /
          I          netns    22         6.983329         2   100         0.000000         0.021870         0.000000 0 0 /
          Srcu_tasks_kthre    23        10.993528         2   120         0.000000         0.010200         0.000000 0 0 /
          S        kauditd    24   1482525.828948       319   120         0.000000        14.489652         0.000000 0 0 /
         

  3. Look for the following:

     * Running process names.
     * Number of context-switches per CPU. See if a process is incurring too few or too many switches on the CPU.
     * CPU time spent (time not idle).



## Example inspection with the Diamorphine rootkit

This section demonstrates an inspection of a VM that has the [Diamorphine](https://github.com/m0nad/Diamorphine) rootkit installed. Diamorphine is a popular loadable kernel module (LKM). This rootkit triggers the following finding categories:

  * `Defense Evasion: Unexpected system call handler`
  * `Defense Evasion: Unexpected kernel modules`
  * `Defense Evasion: Unexpected kernel read-only data modification`



For more information about these finding categories, see [Kernel-mode rootkit threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview#kernel-mode-rootkit-threat-findings).

The inspection steps taken and the symptoms that were observed on the VM are as follows:

  1. Search `syslog` for all out-of-tree kernel modules that are loaded.

     1. Search the kernel log buffer:
            
            sudo dmesg | grep out-of-tree
            

Output:
            
            diamorphine: loading out-of-tree module taints kernel.
            

     2. Search the `syslog` messages:
            
            grep "out-of-tree" /var/log/syslog*
            

Output:
            
            /var/log/syslog: diamorphine: loading out-of-tree module taints kernel.
            

  2. Search `syslog` for any module verification failures (not available on all Linux distributions).

     1. Search the kernel log buffer:
            
            sudo dmesg | grep "module verification failed"
            

Output:
            
            diamorphine: module verification failed: signature and/or required key missing - tainting kernel
            

     2. Search the `syslog` messages:
            
            sudo grep "module verification failed" /var/log/syslog*
            

Output:
            
            /var/log/syslog: diamorphine: module verification failed: signature and/or required key missing - tainting kernel
            

  3. Confirm that the module is hidden from the `/proc/modules` and `lsmod` commands.
         
         sudo grep diamorphine /proc/modules
         sudo lsmod | grep diamorphine
         

No results were displayed.

  4. Confirm that the module has an entry in `sysfs`.
         
         sudo cat /sys/module/diamorphine/coresize
         

Output:
         
         16384
         

  5. Get the system call table for the architecture:
         
         sudo ausyscall --dump
         

Output:
         
         Using x86_64 syscall table:
         0       read
         1       write
         2       open
         3       close
         

Audit for anomalies in system calls—like `kill` and `getdents`—that are typically tampered with by rootkits.

  6. To check for system call handler tampering, audit the system calls and check for anomalous behaviors. These behaviors vary for each system call.

A system call that is typically hacked is the `kill` call. You can check if the `kill` system call has been bypassed. In the following example, the `kill` system call was audited.

     1. Install `auditd` and observe the VM's behavior without the Diamorphine rootkit:
            
            $ sudo apt-get update && sudo apt-get install auditd
            $ # Add audit rules for specific system calls
            $ sudo echo "-a exit,always -F arch=b64 -S kill -k audit_kill" >> /etc/audit/rules.d/audit.rules
            $  sudo /etc/init.d/auditd restart
            Restarting auditd (via systemctl): auditd.service.
            
            $ # Behavior observed without rootkit
            $ sleep 600 &
            [1] 1119
            $ sudo kill -9 1119
            $ sudo ausearch -k audit_kill | grep -A 3 "pid=1119"
            type=OBJ_PID msg=audit(1677517839.523:198): opid=1119 oauid=1001 ouid=0 oses=1 obj=unconfined ocomm="sleep"
            type=SYSCALL msg=audit(1677517839.523:198): arch=c000003e syscall=62 success=yes exit=0 a0=45f a1=9 a2=0 a3=7f61c64b2ac0 items=0 ppid=1034 pid=1035 auid=1001 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0
            tty=pts0 ses=1 comm="bash" exe="/usr/bin/bash" subj=unconfined key="audit_kill"
            $ sleep 600 &
            [1] 1087
            $ sudo kill -31 1087
            $ sudo ausearch -k audit_kill | grep -A 3 "pid=1087"
            type=OBJ_PID msg=audit(1677517760.844:168): opid=1087 oauid=1001 ouid=0 oses=1 obj=unconfined ocomm="sleep"
            type=SYSCALL msg=audit(1677517760.844:168): arch=c000003e syscall=62 success=yes exit=0 a0=43f a1=1f a2=0 a3=7f61c64b2ac0 items=0 ppid=1034 pid=1035 auid=1001 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=pts0        ses=1 comm="bash" exe="/usr/bin/bash" subj=unconfined key="audit_kill"
            

At this point in the inspection, the Diamorphine rootkit was installed. The next steps show the VM's behavior after the rootkit's installation.

**Warning:** For this example inspection, the Diamorphine rootkit was installed in a controlled environment. Don't install the Diamorphine rootkit in your own cloud environment.
     2. Confirm that an audit log entry for the signal is now absent after the Diamorphine rootkit was installed:
            
            $ sudo ausearch -k audit_kill | grep -A 3 "pid=1158"
            $ sleep 600 &
            [2] 1167
            

     3. Check the details in the audit log entry for the signal. In this example, although this particular signal was not completely hijacked by the rootkit, information about the invoker process is available.
            
            $ sudo kill -9 1167
            $ sudo ausearch -k audit_kill | grep -A 3 "pid=1167"
            type=OBJ_PID msg=audit(1677518008.586:237): opid=1167 oauid=1001 ouid=0 oses=1 obj=unconfined ocomm="sleep"
            type=SYSCALL msg=audit(1677518008.586:237): arch=c000003e syscall=62 success=yes exit=0 a0=48f a1=9 a2=0 a3=7f61c64b2ac0 items=0 ppid=1034 pid=1035 auid=1001 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0
            tty=pts0 ses=1 comm="bash" exe="/usr/bin/bash" subj=unconfined key="audit_kill"
            




## Debug data collection script

The following script performs many of the debugging tasks described on this page. You can run this script in `sudo` or `root` mode. The script only reads debug information from the system.
    
    
    $ cat kprot.sh
    #!/bin/bash
    
    echo "Boot command line"
    cat /proc/cmdline
    echo "=================================================="
    echo "Loaded modules"
    cat /proc/modules
    echo "=================================================="
    echo "Current tracer"
    cat /sys/kernel/debug/tracing/current_tracer
    echo "=================================================="
    echo "Tracing event enable"
    cat /sys/kernel/debug/tracing/events/enable
    echo "=================================================="
    echo "Tracing sub events enable"
    for en in `find /sys/kernel/debug/tracing/events/*/enable`; do printf "\b$en\n"; cat $en; done
    echo "=================================================="
    echo "IP table rules"
    iptables -L
    echo "=================================================="
    echo "Ftrace list"
    cat /sys/kernel/debug/tracing/enabled_functions
    echo "=================================================="
    echo "Kprobes enabled"
    cat /sys/kernel/debug/kprobes/enabled
    echo "=================================================="
    echo "Kprobes list"
    cat /sys/kernel/debug/kprobes/list
    echo "=================================================="
    echo "Kprobes blocklist"
    cat /sys/kernel/debug/kprobes/blacklist
    echo "=================================================="
    echo "BPF trace"
    sudo apt update && sudo apt-get update && sudo apt-get install bpftrace
    bpftrace -l
    echo "=================================================="
    echo "BPF prog list"
    sudo apt update && sudo apt install linux-tools-`uname -r`
    bpftool prog
    echo "=================================================="
    

## What's next

  * [Learn more about Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview)
  * [Learn how to use Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
