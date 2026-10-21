---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies/
title: VM Extension Manager policies for the Ops Agent overview \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:03.370408+00:00
---

# VM Extension Manager policies for the Ops Agent overview  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  VM Extension Manager policies for the Ops Agent overview Stay organized with collections  Save and categorize content based on your preferences. 

You can use [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager) policies to automate the deployment, configuration, and version management of the Ops Agent across your Compute Engine fleet. You can apply policies globally across your project or target specific zones and labeled subsets of VMs, roll out custom configurations, and keep agents updated or pinned to a specific release.

## About extension policies for the Ops Agent

With VM Extension Manager, you create policies that declare which extensions you want to install on VMs. The Ops Agent is one of the available extensions. When you create an extension policy, you describe how you want a supported extension like the Ops Agent to be installed and maintained on any VMs that match the policy's criteria.

You can use extension policies for the Ops Agent to perform tasks like the following:

  * Fleetwide installation: Install the Ops Agent on the following:

    * All VMs in one or more zones in your Google Cloud project.
    * All VMs globally (in your Google Cloud project).
    * A labeled subset of VMs in a zone.
    * A labeled subset of VMs across zones in your Google Cloud project.
  * Version control:

    * Keep the Ops Agent updated to the latest version.
    * Pin the Ops Agent version to a specific release.
  * Configuration management: Apply and update a custom configuration to the Ops Agent on all VMs managed by a policy.




## Supported operating systems

Before attempting to use VM Extension Manager policies to manage the Ops Agent, verify that your target operating system is compatible with both the Ops Agent and VM Extension Manager.

VM Extension Manager supports all operating systems supported by the Ops Agent, except for SUSE Linux Enterprise Server (SLES) and Ubuntu. For more information about the operating systems supported by the Ops Agent, see [Operating systems](https://docs.cloud.google.com/monitoring/agent/ops-agent#supported_operating_systems).

If your operating system is supported by both the Ops Agent and VM Extension Manager, then you can use extension policies to manage the Ops Agent.

## Quota

For information about the number of extension policies you can create in a Google Cloud project, see [Quota](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#quota).

## Pricing

For information about costs associated with using VM Extension Manager, see [Pricing](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager#pricing).

If you install the Ops Agent, then you might be charged for the metrics, logs, or traces that the agent sends to your Google Cloud project. For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing). 

## What's next

  * [Create extension policies to install the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-agent-vmem-policies).
  * Modify the installation by [updating your extension policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/manage-agent-vmem-policies).
  * [Troubleshoot problems in extension policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/manage-agent-vmem-policies).
  * Learn more about [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).
  * View detailed information about [configuring the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
