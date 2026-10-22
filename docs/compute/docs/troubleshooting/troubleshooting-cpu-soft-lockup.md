---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-cpu-soft-lockup/
title: Troubleshooting vCPU soft lockups \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:17.485452+00:00
---

# Troubleshooting vCPU soft lockups  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-cpu-soft-lockup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting vCPU soft lockups Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to troubleshoot vCPU soft lockups. A _soft lockup_ occurs when a virtual machine (VM) instance's vCPU is unable to run a new task for more than 20 seconds. Most soft lockups are caused by bugs in application software.

Soft lockups can cause VMs to become unresponsive for short periods of time, disrupt SSH access to VMs, and trigger application timeouts or failover. VMs that are experiencing a soft lockup might also have unusually high or unusually low CPU utilization, depending on the exact cause of the soft lockup.

## Identify soft lockups

To identify whether your VM is experiencing a soft lockup, do one of the following:

  * If you previously enabled [serial port output logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver) for your VM, [review serial port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#viewing_serial_port_output) for a soft lockup stack trace.
  * Review your VM's operating system logs (`/var/log/messages`) for a soft lockup stack trace.



**Example soft lockup stack trace**
    
    
    watchdog: BUG: soft lockup - CPU#3 stuck for 22s!
    

To detect future soft lockups, you can do the following:

  1. [Enable serial port output logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver).

  2. [Create a log-based alerting policy](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition) for the following log:
         
         resource.type="gce_instance" log_id("serialconsole.googleapis.com/serial_port_1_output") textPayload=~"watchdog.*lockup"
         

**Note:** When you test the query, it is likely that no logs appear. This is expected behavior.



## Troubleshoot soft lockups

After you've identified that a soft lockup is occurring, try the following troubleshooting steps to resolve the issue:

  1. Check your OS vendor's site for known errors with your OS version. Sometimes you might find reference to specific kernel modules in the stack trace that suggests a particular function or operation that is involved.
  2. Identify whether the soft lockup repeats with any frequency, such as coinciding with high load or certain activities. If the soft lockups correlate with high load, you might need to reconfigure your workload, for example by using a larger VM or splitting the load across more VMs.
  3. Check if the soft lockups correlate with any changes to your runtime environment such as new software deployments or OS image updates.
  4. Evaluate whether any [maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) have taken place around the time of the soft lockup, by reviewing [audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging#viewing_logs) for system event audit logs.



If the proceeding troubleshooting steps didn't resolve the issue, [file a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case) and include all of the information you gathered from troubleshooting.

## Best practices to avoid soft lockups

To help prevent your VMs from experiencing soft lockups, we recommend implementing the following best practices:

  * Ensure that you have appropriate redundant components configured for your system, such as high availability clusters, to provide a failover capability if a particular VM experiences a prolonged soft lockup. For more information, see [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems).
  * For compute-intensive workloads, consider using [compute-optimized machine families](https://docs.cloud.google.com/compute/docs/compute-optimized-machines).
  * Test your workload with simulated [maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) to learn how your workload performs during live migration (if enabled), particularly under load testing.
  * If you're running a custom Linux Kernel or custom modules in your VM, test new changes under load before deploying them to your production environment. Confirm that your custom changes don't disqualify you from receiving support from your OS vendor.
  * Keep your operating system up to date. For more information, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
