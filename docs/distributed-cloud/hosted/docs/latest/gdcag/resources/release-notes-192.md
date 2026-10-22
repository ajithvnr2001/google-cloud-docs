---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-192/
title: Google Distributed Cloud air-gapped 1.9.2 release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:01.332872+00:00
---

# Google Distributed Cloud air-gapped 1.9.2 release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/release-notes-192/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Google Distributed Cloud air-gapped 1.9.2 release notes Stay organized with collections  Save and categorize content based on your preferences. 

## March 31, 2023 [GDC 1.9.2]

* * *

Announcement

Google Distributed Cloud air-gapped 1.9.2 is now released.

See the [product overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/overview) to learn about the features of Google Distributed Cloud air-gapped.

* * *

Change

Updated Google Distributed Cloud version to 1.14.3-gke.8 to apply the latest security patches and important updates. 

See [Google Distributed Cloud 1.14.3 release notes](https://cloud.google.com/anthos/clusters/docs/bare-metal/latest/release-notes?_gl=1*5sa311*_ga*ODUwNDI2MDExLjE2Nzk1MDM0NDM.*_ga_4LYFWVHBEB*MTY4MDA5NzQ2OS4xLjEuMTY4MDA5NzQ2OS4wLjAuMA..#March_24_2023) for details.

* * *

Change

Between 1070 and 1072 the NVIDIA driver was not signed to match the kernel and therefore the NVIDIA driver couldn't load during a secured boot. Updated Canonical Ubuntu OS image version to 20230309 with matching signed NVIDIA driver to address the problem. 

* * *

Change

In the Firewall operable component, add a default authentication profile for all non-emergency access administrators. This profile enforces a limit of three (3) consecutive failed login attempts before the account is locked. Only an emergency access admin account can restore access.   
This change is a requirement from the Security Technical Implementation Guide (STIG) V-228639. 

* * *

Change

In the Firewall operable component, GDC 1.9.2 implements a default deny rule for traffic flows, and only system-required flows are explicitly allowed. You can use the Firewall API to create a firewall policy to allow additional flows.

For information about using the Firewall API to create a firewall policy, see:

  * [How to create `OrganizationFirewallPolicy` (for Platform Administrator)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/firewall-policy)



* * *

Security

The following container image security vulnerabilities are fixed:

  * [CVE-2023-0215](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0215)
  * [CVE-2023-0361](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0361)
  * [CVE-2023-0286](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-0286)
  * [CVE-2022-4450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4450)
  * [CVE-2022-4304](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-4304)
  * [CVE-2022-2097](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2097)
  * [CVE-2022-32221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32221)
  * [CVE-2022-43552](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-43552)
  * [CVE-2021-46848](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46848)
  * [CVE-2022-42898](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42898)
  * [CVE-2023-23916](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-23916)
  * [CVE-2022-21628](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21628)
  * [CVE-2020-6829](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-6829)
  * [CVE-2020-12403](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-12403)
  * [CVE-2023-21835](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-21835)
  * [CVE-2022-21626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21626)



* * *

Fixed

In Google Distributed Cloud air-gapped 1.9.2, the Node and Operating System component uses an auto restart on configuration feature of the VM to resolve the issue of potential failure to use a new VM disk for a VM after stopping and restarting KVM during cluster upgrade.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where role-based access control (RBAC) and schema settings in the VM manager is stopping users from starting VM backup and restore processes. 

* * *

Issue

Google Distributed Cloud air-gapped 1.9.0 has a known issue where remote server management software is occasionally unable to retrieve the key from HSM.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where using the `standard-block` storage class might prevent virtual machines (VMs) from starting or restarting.

* * *

Issue

During an upgrade from Google Distributed Cloud air-gapped 1.9.1 to 1.9.2, operations to Artifact Registry may fail with Unauthorized errors.

* * *

Issue

Unable to retrieve logs for pod due to a missing image.

* * *

Issue

A server is stuck in the `available` state and its encryption configuration job keeps failing due to an SSH key error.

* * *

Issue

Provisioning a user cluster through GUI gets stuck.

* * *

Issue

At bootstrap, Google Distributed Cloud air-gapped 1.9.2 fails to return metrics from Cortex.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue during the Node OS upgrade where a the server is stuck in deprovisioning because `boot.ipxe` URL is invalid.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue during the Node OS upgrade where a node fails the `machine-init` job.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where the upgrade from 1.9.0 to 1.9.1 is blocked because the `ods-fleet` add-on failed to install.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where the `vm-runtime` addon is stuck during the upgrade of the `gpu-org-system-cluster` from 1.9.1 to 1.9.2 because the `kubevm-gpu-driver-daemonset` pods are in the `CrashLoopBackOff` state.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where a user cluster does not become ready in time.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where an `OrganizationUpgrade` status does not get updated.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue in the UI that lets you select an incompatible coupling of GPU to VM type.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where VMs with memory greater than 32 GB require a memory override due to an incorrect QEMU overhead calculation.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where the `kube-state-metrics` deployment crash loops.

* * *

Issue

Google Distributed Cloud air-gapped 1.9.2 has a known issue where alerts in organization system clusters don't reach the ticketing system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
