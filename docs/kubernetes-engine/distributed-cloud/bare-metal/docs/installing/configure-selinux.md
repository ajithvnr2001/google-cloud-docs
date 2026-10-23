---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-selinux/
title: Secure your containers using SELinux \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:06.136212+00:00
---

# Secure your containers using SELinux  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-selinux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Secure your containers using SELinux Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to secure your containers by enabling SELinux. SELinux is supported for Red Hat Enterprise Linux (RHEL). If your host machines are running RHEL and you want to enable SELinux for your cluster, you must enable SELinux in all of your host machines. Starting with Google Distributed Cloud release 1.9.0, you can enable or disable SELinux before or after cluster creation or cluster upgrades. When SELinux is enabled on the host, it is enabled for the container runtime.

## Check if SELinux is enabled

SELinux is enabled on RHEL by default.

  * To verify, run:
        
        getenforce
        




The command returns either `Enforcing`, `Permissive`, or `Disabled`. If the command returns `Enforcing`, then you can proceed with upgrading or creating your clusters.

## Enable SELinux

If the `getenforce` command returns `Permissive`, you can switch to `Enforcing` mode using the `setenforce` command. Toggling between `Permissive` and `Enforcing` mode using `setenforce` doesn't require a system reboot. However, if you want the changes to be persistent across reboots, you must update the `/etc/selinux/config` file.

  * To switch to `Enforcing` mode, run:
        
        sudo setenforce 1 # temporary
        sudo sed -i 's/SELINUX=permissive/SELINUX=enforcing/g' /etc/selinux/config # persistent - after reboot
        




If SELinux is `Disabled`, to enable it, we recommend to first enable it in `Permissive` mode first and reboot the system to verify that the system boots successfully. If there are no SELinux errors, then you can safely switch SELinux to `Enforcing` mode.

  1. **Optional** : Enable SELinux in `Permissive` mode:
         
         sudo sed -i 's/SELINUX=disabled/SELINUX=permissive/g' /etc/selinux/config
           sudo reboot
         

  2. If the system reboots successfully with no SELinux errors, then you can enable `Enforcing` mode:
         
         sudo sed -i 's/SELINUX=disabled/SELINUX=enforcing/g' /etc/selinux/config
           sudo reboot
         




Once SELinux is enabled in `Enforcing` mode, SELinux is enabled for all processes on the host, including the container runtime.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
