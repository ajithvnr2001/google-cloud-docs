---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-cpu-bus-locks/
title: Troubleshoot CPU bus locks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:00.013532+00:00
---

# Troubleshoot CPU bus locks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-cpu-bus-locks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot CPU bus locks Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document explains how to identify and troubleshoot _CPU bus locks_ in Linux guest operating systems. It covers the symptoms of CPU bus locks, how to diagnose these issues by using kernel log messages, how to locate the faulty code, and how to apply mitigations or fixes.

## Overview

A CPU bus lock occurs when a processor must assert a hardware `LOCK#` signal to acquire exclusive access to the system-wide memory bus. This issue typically happens in one of the following circumstances:

  * An atomic instruction operates on unaligned memory that crosses a cache line boundary (a split lock).
  * An atomic instruction operates on memory that is designated as `uncacheable` (UC), such as `Memory-Mapped I/O` (MMIO).



Because the CPU asserts a global bus lock, all other processors and devices in the guest operating system must wait while the memory operation completes. A high rate of bus locks might severely degrade CPU performance.

While older processors didn't track bus locks, modern x86 processors such as Intel Sapphire Rapids and later, or AMD Zen 5 or later, include a hardware feature that detects CPU bus locks. When an instruction triggers a CPU bus lock, the CPU issues a debug exception (`#DB`) immediately after the instruction completes.

Beginning with Linux kernel version 5.13 on Intel and 6.13 on AMD, the Linux kernel intercepts this `#DB` exception and applies a mitigation, typically by rate-limiting the faulty process. By intentionally forcing the thread to sleep, the kernel prevents a single application from saturating the memory bus, preserving system performance for the rest of the compute instance at the cost of the faulty application performance.

## Symptoms

If a process in your Linux guest is triggering CPU bus locks, you might experience the following symptoms:

  * Degraded application performance: CPU bus locks might introduce unanticipated latency for applications.
  * System-wide load spikes: overall system responsiveness might decline.
  * Unexpected application crashes: if you configure the kernel to handle split or bus locks strictly (`split_lock_detect=fatal`), then the faulty application may crash with a `SIGBUS` error.



## Identify CPU bus locks

To identify whether your compute instance is experiencing CPU bus locks, do one of the following:

  * If you've enabled [serial port output logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver) for your compute instance, [review serial port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#viewing_serial_port_output) for a CPU bus lock trace.
  * Review your compute instance's operating system logs (`/var/log/messages`) for a CPU bus lock trace.



**Example CPU bus lock trace**

`x86/split lock detection: #DB: <process_name>/<pid> took a bus_lock trap at address: 0x<address>`

To detect future CPU bus locks, do the following:

  1. [Enable serial port output logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver).
  2. [Create a log-based alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition) for the following log:

`resource.type="gce_instance" log_id("serialconsole.googleapis.com/serial_port_1_output") textPayload=~"took a bus_lock trap"`

This log entry gives you the process name (`<process_name>`) and Process ID (`<pid>`) that is responsible for the CPU bus lock, as well as the instruction pointer address where the fault occurred.




## Troubleshoot CPU bus locks

If you are developing or compiling the faulty application, you can use specific C or C++ compiler warnings to identify variables and structures that might cause split locks.

**Compiler warnings**

If you use `GCC` or `Clang`, compile your code with the following flags to help identify alignment issues:

  * `-Wcast-align` or `-Wcast-align=strict`: these flags warn you when a pointer cast increases the required alignment of the target. Casting a generic `char*` buffer to a `uint64_t*` and performing an atomic operation on it is a classic cause of split locks.
  * `-Waddress-of-packed-member`: this flag warns you when you take the address of a packed struct member (for example, using `#pragma pack(1)` or `__attribute__((packed))`). Because packed structures disregard natural memory alignment, any atomic operation on a member of a packed struct has a high probability of crossing a 64-byte cache line boundary.



**Catching uncacheable (UC) memory locks**

If atomic operations on uncacheable memory causes the CPU bus lock, compiler warnings won't catch it. This issue typically happens when interacting with device memory:

  * Audit memory mappings: review your code for uses of `mmap` with flags like `O_SYNC` or direct access to `/dev/mem` or `/dev/uio`.
  * Avoid atomics on MMIO: don't use atomic operations like `__sync_fetch_and_add` or `std::atomic` on memory regions mapped to device registers or uncacheable memory buffers



## Fixing CPU bus locks

You can fix CPU bus lock issues by correcting the memory alignment in the application's source code.

  * Avoid using `#pragma pack` or `__attribute__((packed))` on structures that contain atomic variables, mutexes, or spinlocks.
  * Use standard alignment directives (like `alignas(64)` in C++11 or `__attribute__((aligned(64)))` in C) to force variables that are heavily used in atomic operations to align to cache line boundaries.
  * Make sure that there are no alignment-related warnings during compilation.
  * Make sure that you only use standard locking mechanisms (mutexes, spinlocks) or atomic instructions on standard, cacheable RAM, never on MMIO or UC memory.



If the troubleshooting steps didn't resolve the issue, then [contact Cloud Customer Care](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case) and include all of the information you gathered during troubleshooting.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
