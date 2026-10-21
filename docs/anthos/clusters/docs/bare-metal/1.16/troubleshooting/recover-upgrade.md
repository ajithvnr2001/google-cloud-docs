---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/recover-upgrade/
title: Recover a failed upgrade in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:56.574223+00:00
---

# Recover a failed upgrade in Google Distributed Cloud  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/recover-upgrade/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Recover a failed upgrade in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/recover-upgrade)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/recover-upgrade)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



Occasionally, Google Distributed Cloud may run into conditions where you need to start an upgrade over again, or fix an error condition to complete the upgrade successfully. The following conditions may occur when upgrading clusters. Try to complete the cluster upgrade as noted with the condition.

## Recover admin, hybrid, and standalone cluster upgrades

Admin, hybrid, and standalone clusters are all upgraded with the [`bmctl upgrade` command](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade).

If your upgrade doesn't complete successfully, check the following conditions and try the upgrade again.

  * `bmctl` fails to parse the config file due to a mistake. Fix the config file and rerun the command.
  * `bmctl` fails to bootstrap the temporary cluster. Retry the command.
  * the log files indicate that the upgrade failed a [preflight check](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight). Correct the preflight condition, or force the upgrade.
  * the upgrade took too long (more than 30 minutes) or timed out. Retry the upgrade command.



## Recover user cluster upgrades

User clusters are [upgraded from an associated admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade) with the `kubectl apply` command.

If your upgrade doesn't complete successfully, check the following conditions and try the upgrade again.

  * Preflight check failed. Check the preflight check log and fix the corresponding error.
  * You may need to construct a new preflight custom resource [following these instructions](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/preflight#re-enabling_preflight_checks) and apply it to the cluster. Check that the triggered preflight passes, and that the cluster reconciler picks up the latest passing state.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
