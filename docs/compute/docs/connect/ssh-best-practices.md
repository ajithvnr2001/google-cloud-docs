---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/
title: Best practices for securing SSH access to VM instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:04.253062+00:00
---

# Best practices for securing SSH access to VM instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for securing SSH access to VM instances Stay organized with collections  Save and categorize content based on your preferences. 

When you grant users access to connect to virtual machine (VM) instances using SSH, you impact the security of your VM and any resources that your VM has access to, such as storage buckets or databases.

You can limit the risks related to SSH access by following several best practices, including:

  * [Control network access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access): Implement zero trust access controls to restrict the networks, locations, and devices from which users can establish SSH connections to your VMs, and avoid VMs from being more exposed than necessary.

  * [Control SSH login access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/login-access): Restrict which users are allowed to establish SSH sessions and ensure that login access is revoked in a timely manner.

  * [Protect SSH credentials](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/credentials): Require users to authenticate with multiple factors and protect credentials from being leaked.

  * [Audit SSH access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/auditing): Maintain a reliable audit trail that tracks all SSH access.

  * [Use post-quantum SSH](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/post-quantum-ssh): Configure post-quantum key exchange algorithms on your clients and VMs to protect connections against capture-now, decrypt-later attacks.




## What's next

  * Learn more about the [best practices for controlling SSH network access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access)
  * Learn more about the [best practices for using post-quantum SSH](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/post-quantum-ssh)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
