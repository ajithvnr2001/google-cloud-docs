---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-nested-vms/
title: Troubleshooting nested virtualization \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:06.727227+00:00
---

# Troubleshooting nested virtualization  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-nested-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting nested virtualization Stay organized with collections  Save and categorize content based on your preferences. 

This document describes common errors that you may run into when using nested virtualization and methods for resolving those errors. For more information about nested virtualization, see [Creating nested VMs](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/creating-nested-vms).

## Can't start nested VM

If your project is part of an organization, your organization might have disabled the ability to create VMs with nested virtualization. Make sure that [nested virtualization is allowed](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint#check_whether_nested_virtualization_is_allowed) before you try to create a VM that has nested virtualization enabled.

## Processor not displaying nested virtualization

If the `grep -c vmx /proc/cpuinfo` command returns `0` and reports that the VM isn't enabled for nesting, make sure of the following:

  * You started your VM with a CPU platform of Intel Haswell or later. For more information, see [Nested virtualization overview](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview).
  * The machine series used to create the VM supports nested virtualization. For more information, see [Machine type comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
  * Your project or organization's policy constraints allow nested virtualization. If policy constraints disallow nested virtualization, the CPU won't expose nesting capabilities. For more information, see [Checking whether nested virtualization is allowed](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint#check_whether_nested_virtualization_is_allowed).



## Can't exit nested VM

If you did not run `screen` before each nested VM session, you can either shut down the nested VM or stop the process from another terminal. To shut down the nested VM, run the `poweroff` command from within your nested VM. Alternatively, log into the host VM in another terminal and end the process, then run `screen` on the host VM before you start a new nested VM.

## `iptables` not forwarding traffic

  * `iptables` resolve rules from top to bottom. Make sure your rules are higher priority than other rules.
  * Check that there are no conflicting rules intercepting your packets.
  * Consider flushing your `iptables`:

**Note:** Flushing `iptables` disables your firewall. You should only do this if you want to start over configuring your firewall.
    1. First, set the default policies:
           
           sudo iptables -P INPUT ACCEPT
           sudo iptables -P FORWARD ACCEPT
           sudo iptables -P OUTPUT ACCEPT
           

    2. Next, flush all tables and chains, and delete non-default chains:
           
           sudo iptables -t nat -F
           sudo iptables -t mangle -F
           sudo iptables -F
           sudo iptables -X
           




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
