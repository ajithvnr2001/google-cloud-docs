---
url: https://docs.cloud.google.com/compute/docs/networking/zonal-dns/
title: Overview of using Zonal DNS \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:25.156931+00:00
---

# Overview of using Zonal DNS  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/zonal-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Overview of using Zonal DNS Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes the benefits and recommended approach for migrating your workloads and organization from global DNS to zonal DNS.

Zonal DNS mitigates the risk of cross-regional outages and improves the overall reliability of your projects on Compute Engine.

## Benefits of using zonal DNS names

Google Cloud offers two types of internal DNS names: zonal and global.

Zonal DNS
    

Zonal DNS names include the name of your Compute Engine instance, the zone where your instance is located, and the project that owns the instance. These names are resolved within a specific zone. As a result, `my-vm.zone1.google.com` is unique to `zone1` and is represents a different instance than `my-vm.zone2.google.com`. This isolation provides a key benefit:

  * **Improved availability** : If one zone experiences an outage, then it doesn't affect DNS resolution in other zones, leading to higher availability for your applications.



Zonal DNS is the default internal DNS resolution method for organizations that were created after September 6, 2018.

Global DNS
    

Global DNS names don't include the zone where the instance is located. This means each instance must have a unique DNS name across _all_ zones within your project. This approach has a significant drawback:

  * **Single point of failure** : If the global DNS service experiences issues, then it can impact all your instances, regardless of the zone they are located in. This can cause the following problems: 
    * **Unable to create new instances** : You might be unable to create new instances in any region that is experiencing control plane failures.
    * **Service disruptions** : Critical Compute Engine services such as autoscaling or autohealing for managed instance groups (MIGs) might not function correctly.


**Note:** As of September 6, 2018, Zonal DNS is the default internal DNS system for new organizations on Google Cloud. Zonal DNS is offered at no charge, and it is not a part of Cloud DNS.

## Recommended approach to migrate from global DNS to zonal DNS

Generally, the global DNS to zonal DNS migration process has two steps:

  1. Configure new projects to use zonal DNS by default.
  2. Migrate existing projects from using global DNS to zonal DNS by changing the internal dns metadata setting.



Some projects may not be compatible with zonal DNS. These projects require analysis and troubleshooting before migrating them to zonal DNS.

**Caution:** Enabling zonal DNS names across your entire project applies zonal DNS settings to Compute Engine instances in the following services:

  * [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible), [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs), and [Containers running on Compute Engine ](https://docs.cloud.google.com/compute/docs/containers)
  * [Cloud SQL](https://docs.cloud.google.com/sql/docs), [Cloud Run functions](https://docs.cloud.google.com/functions/docs), and [Batch](https://docs.cloud.google.com/batch/docs/get-started)
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs) and [Dataflow](https://docs.cloud.google.com/dataflow/docs)



## Project Compatibility Guidance

Compute Engine checks your [preceding 30 days of internal DNS history](https://docs.cloud.google.com/compute/docs/networking/migrate-to-zonal-dns#query-analysis) to determine if you can migrate to Zonal DNS without performing any code changes. Even if your project is recommended for migration, Google recommends you to verify that your specific workload configuration is ready for the switch to Zonal DNS. To ensure that everything runs smoothly after the migration, review the following environmental factors:

### 1\. DNS Search Domains (Linux or Unix only)

When you switch to Zonal DNS, Compute Engine adds a new domain to the instance's search path.

  * **When to verify:** If you run older Linux or Unix distributions that use `glibc` version 2.25 or earlier, then the system has a maximum limit of six search domains.
  * **When to skip:** If the instance runs any of the following operating systems, then you don't need to verify anything:

    * Windows
    * Container-Optimized OS
    * Debian 10 or later
    * Fedora CoreOS 27 or later
    * RHEL 8 or later
    * Ubuntu 18.04 or later
    * Custom images using `glibc` version 2.26 or later



**How to verify your environment:**

  1. Connect to your Linux instance and check the `glibc` version by running the following command:
         
         ldd --version
         

  2. If you are on `glibc` version 2.25 or earlier, then view your current search domains by running the following command:
         
         cat /etc/resolv.conf
         

The `search` line in the output shows the current search domains. You should have no more than five domains to safely add a new search domain and avoid exceeding the OS limit of six.




**How to mitigate:**

If your instance exceeds the search domain limit on an affected OS version, then you can resolve the limitation using either of the following approaches:

  * **Create a new instance** : Create a replacement instance using a compliant OS image (such as Debian 10+ or RHEL 8+).
  * **Update the existing instance** : Update the guest OS on your compute instance so that it runs a compliant operating system.



### 2\. Instance Name Length (Legacy Operating Systems)

Zonal DNS appends a zonal qualifier to the internal Fully Qualified Domain Name (FQDN), making the overall name longer.

  * **When to verify:** Legacy systems like **Windows Server 2003** or earlier have a 15-character name limit due to older NetBIOS conventions.
  * **What to do:** If you use these legacy systems, then verify that the longer Zonal DNS names don't exceed this character limit.



Modern Windows OS images are unaffected.

**How to mitigate:**

If an instance name on a legacy OS exceeds 15 characters after appending the zonal qualifier, then you can address the issue by using either of the following methods:

  * **Rename the instance** : Stop the instance and rename it so that the combined FQDN stays within the 15-character NetBIOS limit.
  * **Upgrade the operating system** : Update the guest OS of the compute instance to a modern Windows operating system image for which NetBIOS naming restrictions no longer apply.



### 3\. Shared VPC Networks

If your infrastructure uses service projects connected using a Shared VPC, then name resolution behaves slightly differently after you switch to using Zonal DNS.

  * **What to do:** To ensure seamless communication across your Shared VPC, verify that your applications resolve instance names within those service projects using the **Zonal FQDN**. The Zonal FQDN includes the specific zone name.



## What's next

  * Review the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#resource-hierarchy-detail) for information about the relationship between organizations, folders, and projects.
  * Learn more about [internal DNS for Compute Engine](https://docs.cloud.google.com/compute/docs/internal-dns).
  * Implement an [organizational policy to ensure all new projects within your organization automatically use Zonal DNS.](https://docs.cloud.google.com/compute/docs/networking/use-zonal-dns)
  * [Migrate current projects to Zonal DNS](https://docs.cloud.google.com/compute/docs/networking/migrate-to-zonal-dns).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
