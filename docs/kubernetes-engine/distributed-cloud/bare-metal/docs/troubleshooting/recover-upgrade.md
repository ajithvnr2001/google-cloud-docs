---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-upgrade/
title: Recover a failed upgrade in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:05.018653+00:00
---

# Recover a failed upgrade in Google Distributed Cloud  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/recover-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Recover a failed upgrade in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Occasionally, Google Distributed Cloud runs into conditions where you need to start an upgrade over again, or fix an error condition to complete the upgrade successfully. The following conditions may occur when upgrading clusters. Try to complete the cluster upgrade as noted with the condition.

## Recover admin, hybrid, and standalone cluster upgrades

Admin, hybrid, and standalone clusters are all upgraded with the [`bmctl upgrade` command](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade).

If your upgrade doesn't complete successfully, check the following conditions and try the upgrade again.

  * `bmctl` fails to parse the config file due to a mistake. Fix the config file and rerun the command.
  * `bmctl` fails to bootstrap the temporary cluster. Retry the command.
  * the log files indicate that the upgrade failed a [preflight check](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight). Correct the preflight condition, or force the upgrade.
  * the upgrade took too long (more than 30 minutes) or timed out. Retry the upgrade command.
  * the upgrade stops during the initialization phase: 
    * For version 1.35 and later, if you use RHEL 8 or Rocky Linux, check the node logs for Ansible execution errors indicating an unsupported Python version. Ansible requires Python 3.9 or newer on the target cluster. [Verify the installation of Python 3.9 or higher](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/rhel#update-python) on the failing node and retry the operation.
    * For version 1.35 and later, check that `cgroupsv2` is enabled. For more information on cgroupsv2, see [migrating to cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/#migrating-cgroupv2).



## Recover user cluster upgrades

User clusters are [upgraded from an associated admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) with the `kubectl apply` command.

If your upgrade doesn't complete successfully, check the following conditions and try the upgrade again.

  * Preflight check failed. Check the preflight check log and fix the corresponding error.
  * You may need to construct a new preflight custom resource [following these instructions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/preflight#re-enabling_preflight_checks) and apply it to the cluster. Check that the triggered preflight passes, and that the cluster reconciler picks up the latest passing state.



## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
