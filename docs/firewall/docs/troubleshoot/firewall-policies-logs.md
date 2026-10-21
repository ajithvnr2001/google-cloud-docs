---
url: https://docs.cloud.google.com/firewall/docs/troubleshoot/firewall-policies-logs/
title: Troubleshoot firewall policy rules log issues \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:32.288504+00:00
---

# Troubleshoot firewall policy rules log issues  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/troubleshoot/firewall-policies-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Troubleshoot firewall policy rules log issues Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot common issues that you might encounter when using firewall policy rules logging.

Firewall policy rules logging helps you audit, verify, and analyze the effects of your firewall rules. When you enable logging for firewall policy rules, you can view logs to verify that your rules work as intended and to understand how they affect connections. For more information, see [Firewall policy rules logging overview](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview).

## Can't view logs

If you can't view firewall rule logs in the **Logs Explorer** section of the Google Cloud console, it might be due to one of the following reasons.

  * Insufficient permissions
  * Legacy networks not supported
  * Incorrect project context



### Insufficient permissions

To view firewall rule logs, ask the project owner to grant your Identity and Access Management principal the [Logs Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project. For more information, see [Permissions](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging#permissions).

### Legacy networks not supported

You cannot use firewall policy rules logging in a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy). Only [Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/vpc) are supported.

### Incorrect project context

Google Cloud stores firewall rule logs in the project that contains the network. Make sure that you are looking for logs in the correct project.

In Shared VPC, you create virtual machine (VM) instances in service projects, but the VMs use a Shared VPC network in the host project. For Shared VPC, Google Cloud stores the firewall rule logs in the host project. If you use Shared VPC, make sure you have the appropriate [permissions](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging#permissions) to view the firewall logs in the host project.

## Log entries missing

If you can't find log entries for your firewall rules in Logs Explorer, check for the following common issues:

### Connections don't match the expected firewall rule

Verify that the firewall rule you expect is in the list of applicable firewall rules for an instance.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **VM instances** section, click the name of the VM instance.

  3. In the **Network interfaces** section, click **View details** under the **Network details** column.

  4. In the **Network configuration analysis** section, check the applicable firewall rules. For more information, see [View logs](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging#viewing_logs).

  5. If you are unsure about the IP addresses, ports, and protocols being used for the connection, you can use [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) to identify the traffic.

**Important:** Google Cloud bills for VPC Flow Logs based on the volume of logs generated. For pricing information, see [VPC pricing](https://cloud.google.com/vpc/pricing).



To make sure that you create your firewall rules correctly, see [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls).

### A higher priority rule without logging applies

Firewall rules are [evaluated according to their priorities](https://docs.cloud.google.com/firewall/docs/firewalls#priority_order_for_firewall_rules). Only one firewall rule applies to matching traffic. If a higher priority rule matches the traffic but does not have logging enabled, logs are not generated even if a lower-priority rule with logging enabled also matches the traffic.

To troubleshoot this issue, run a connectivity test from source to destination. For more information, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests). This will provide you information about the firewall rule used for the connection.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **VM instances** section, click the name of the VM instance.

  3. In the **Network interfaces** section, click **View details** under the **Network details** column.

  4. In the **Network configuration analysis** section, check the applicable firewall rules and identify your custom rules in that list.

  5. Temporarily enable logging for all of those custom firewall rules. With logging enabled, you can identify which rule is matching traffic.

  6. After you identify the rule, disable logging for rules that don't require it. To disable firewall rules logging, see [Disable firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging#disable-logging).




## Missing metadata for some log entries

If you notice missing metadata for some log entries in Logs Explorer, this might be caused by a delay in configuration propagation.

If you update a firewall rule that has firewall logging enabled, it might take a few minutes before Google Cloud finishes propagating the changes necessary to log traffic that matches the rule's updated components.

## What's next

  * [Logging overview](https://docs.cloud.google.com/logging/docs/overview)
  * [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
