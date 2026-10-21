---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/faq/
title: Common questions \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:18:46.397333+00:00
---

# Common questions  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Common questions Stay organized with collections  Save and categorize content based on your preferences. 

This page provides answers to some common questions about Google Cloud's Managed Service for Microsoft Active Directory.

## Which user account can I use to administer the Managed Microsoft AD?

When you create a new domain, Managed Microsoft AD automatically creates a [delegated administrator account](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-delegated-admin). You can use this user account to manage the Active Directory objects in your domain. The delegated administrator account doesn't have the Domain Administrator and Enterprise Administrator permissions, because Managed Microsoft AD is a managed service and Google reserves the right to use these permissions.

## What are the capabilities of a delegated administrator account?

The delegated administrator account has the permissions to perform a specific list of administrative activities to manage the Active Directory objects. The delegated administrator account doesn't have the permissions to perform any other administrative activities. For example, a delegated administrator can't create and manage the domain-level policies, and it can't perform administrative tasks such as backing up and restoring domains and extending the schema using the standard AD tools. For more information, see [Delegated administrator](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#delegated_administrator).

However, you can use these features through Managed Microsoft AD. Any user who has the necessary permissions to [back up and restore a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore#before_you_begin) and [extend the schema](https://docs.cloud.google.com/managed-microsoft-ad/docs/extend-schema#before_you_begin) can initiate these tasks.

## How can I manage organizational units (OU)?

When you create a new domain, Managed Microsoft AD automatically creates the `Cloud` and `Cloud Service Objects` OUs along with other [default Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects). For more information about managing these objects, see [Manage Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects).

## How can I manage group policy objects (GPO)?

By default, Managed Microsoft AD creates the `Cloud Service Default Computer Policy` [GPO](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#group_policy_objects) along with other [default Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects) and links it to the `Cloud` OU. If you need additional GPOs, you can create custom GPOs and add them to either the `Cloud` OU or to any other custom OUs that you have created under the `Cloud` OU. Only the creator of a custom GPO can edit it. For more information about managing these objects, see [Manage Active Directory objects](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects).

## How are domain controllers deployed?

Managed Microsoft AD creates domain controllers as VMs in dedicated [ Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) networks. Managed Microsoft AD then connects the domain controller VPC networks to your other existing VPC networks using [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).

For more information, see [Deploy an Active Directory resource forest](https://docs.cloud.google.com/managed-microsoft-ad/docs/part-1-deploy-active-directory).

## What are the supported Windows and Linux versions that I can join to a domain?

For information about the supported Windows and Linux versions that you can join to a domain, see [Compatible OS versions](https://docs.cloud.google.com/managed-microsoft-ad/docs/os-versions).

## When I create a new Managed Microsoft AD domain, how can I select the suitable IP address range?

Managed Microsoft AD requires a minimum of a /24 private [RFC 1918](https://tools.ietf.org/html/rfc1918) CIDR range, such as `10.1.0.0/24`, that isn't already a subnet on your authorized VPC network.

For more information, see [Select IP address ranges](https://docs.cloud.google.com/managed-microsoft-ad/docs/selecting-ip-address-ranges).

## Where can I view the event logs for domain controllers?

You can view the event logs for domain controllers by [setting up audit logging for the domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/using-ad-audit-logs).

## What should I expect during the maintenance of a domain controller? Is there any downtime during the maintenance?

Managed Microsoft AD ensures that there are at least two domain controllers running on each region for a domain in different availability zones. So, the domain remains available during patching. For more information, see [Patching](https://docs.cloud.google.com/managed-microsoft-ad/docs/hardening#patching).

## What is the timeline for applying security patches on domain controllers?

Managed Microsoft AD targets different timelines to apply different types of patches on domain controllers. For more information, see [Patching schedule](https://docs.cloud.google.com/managed-microsoft-ad/docs/hardening#patching-schedule).

## Can I restore my Active Directory data after a failure?

Managed Microsoft AD supports on-demand and automatic backups for your domain. You can use any of these backup types to [perform an authoritative restore](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore#restore-backup), which returns the domain to a previous point in time. For more information, see [Back up and restore your domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/backup-restore).

## Can I extend the Active Directory schema?

Yes, you can [extend the Active Directory schema](https://docs.cloud.google.com/managed-microsoft-ad/docs/extend-schema) of your Managed Microsoft AD domain. For more information, see [About schema extension](https://docs.cloud.google.com/managed-microsoft-ad/docs/schema-extension).

## Which time server do the domain controllers in Managed Microsoft AD use?

The domain controllers in Managed Microsoft AD sync their time with the `metadata.google.internal` time server. For more information, see [Configure NTP on a VM](https://docs.cloud.google.com/compute/docs/instances/configure-ntp).

## Do I need to create a separate project for each Managed Microsoft AD domain?

No, you don't need separate Google Cloud projects. By default, you can create two independent domains in the same project. [Contact support](https://docs.cloud.google.com/managed-microsoft-ad/docs/get-support) to increase the number of independent domains that you can create in the same project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
