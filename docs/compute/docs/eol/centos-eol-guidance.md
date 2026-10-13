---
url: https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance/
title: CentOS end of support guidance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:33.058325+00:00
---

# CentOS end of support guidance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/eol/centos-eol-guidance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  CentOS end of support guidance Stay organized with collections  Save and categorize content based on your preferences. 

In December 2020, the CentOS community and Red Hat announced the [sunset of CentOS](https://blog.centos.org/2020/12/future-is-centos-stream/). Red Hat also announced CentOS Stream, a new, upstream development platform for the CentOS community. For more information, see [Transforming the development experience within CentOS](https://www.redhat.com/en/blog/transforming-development-experience-within-centos).

## What does this mean for CentOS users?

CentOS 6, 7, and 8 are the final releases of CentOS Linux. The end of support (EOS) dates for these versions are as follows:

  * CentOS 7 - June 30, 2024
  * CentOS 8 - December 31, 2021
  * CentOS 6 - November 30, 2020



If you have workloads that are running on CentOS versions that have reached their EOS date, your projects might be at risk because you are running VMs that are not receiving security updates. Google Cloud recommends that you migrate your workloads to a supported OS by using the migration options detailed in this document. For CentOS 7 users, Google Cloud recommends reviewing migration options and planning accordingly.

## Impact on existing VMs

Your current VMs that are running CentOS are not affected by the EOS date for that version. After the EOS date, you can still start or stop your existing VMs that use these images.

However, after this date, the following changes take effect for CentOS versions that have reached EOS:

  * CentOS images for that version are marked as deprecated, but are still available.
  * If you need to create VMs using CentOS images after the EOS date, [make copies of the images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) in your projects to ensure you can still use them.
  * For your existing CentOS based VMs, limited technical support is available through Google Cloud.



## CentOS 7

As of June 30, 2024, the CentOS 7 operating system no longer receives software updates. For Google Cloud customers running CentOS 7, we recommend that you migrate your workloads to another operating system.

### Long Term Support options

For maintaining your existing CentOS 7 systems on Google Cloud, there are long term support options from Google partners that provide secure packages, updates, and security patches to extend the lifetime of your CentOS environments. To receive CentOS technical support for your Google Cloud workloads, we recommend the following option:

  * [CIQ Bridge](http://ciq.com/products/ciq-bridge/google-cloud/?utm_source=gc&utm_medium=gcinbound&utm_campaign=centos-eol-guidance): Extends CentOS 7 support by up to 3 years. CIQ, the exclusive provider of enterprise Rocky Linux for Google Cloud, offers access to a global repository of CentOS 7 packages, security updates, and patches to maintain business continuity and regulated industries compliance. In partnership with Google, CIQ is committed to helping Google Cloud customers by providing promotional discounts for CentOS 7 long term support.



## CentOS 8

CentOS 8 reached its end of support (EOS) on December 31, 2021. This operating system no longer receives software updates or security patches.

If you have any remaining workloads on CentOS 8, we strongly recommend migrating them to a supported operating system to ensure you receive necessary security updates and support.

## CentOS 6

CentOS 6 reached its end of support (EOS) on November 30, 2020. This operating system no longer receives software updates or security patches.

If you have any remaining workloads on CentOS 6, we strongly recommend migrating them to a supported operating system to ensure you receive necessary security updates and support.

## Migration options

You can choose to either migrate your workloads that are running on CentOS to a compatible OS distribution, or you might choose an OS that uses a different system.

To migrate your workloads, complete the following steps:

  1. Decide on whether you want to move to a compatible OS or not.

     * For a list of compatible operating systems, see CentOS compatible operating systems.
     * For a list of other operating systems that you might consider, see Other operating systems.
  2. To move from CentOS to the new OSes, you have the following options:

     * Create a new VM with the new OS and redeploy your workloads. **Google recommends using this option**.
     * Migrate your workloads to a new OS using conversion tools. Choose one of the following:

       * Use the migration tool that is available from the OS distribution that you want to migrate to. While a few community tools might be available for converting your workloads from CentOS to another distribution, Google Cloud does not provide or support any of these conversion tools.
       * Use the [`migrate2rocky`](https://github.com/rocky-linux/rocky-tools/tree/main/migrate2rocky) tool provided by CIQ to convert CentOS to Rocky Linux. For instructions on how to use this tool and the supported operating systems, see the [Rocky Linux documentation](https://docs.rockylinux.org/guides/migrate2rocky/).
       * Use the `Convert2RHEL` tool provided by Red Hat to convert CentOS to Red Hat Enterprise Linux. For instructions on how to use this tool and the supported operating systems, see the [Convert2RHEL documentation](https://www.redhat.com/en/blog/converting-centos-linux-rhel-google-cloud).
  3. Append the relevant OS license strings. For a list of OS license strings on Compute Engine, see [Operating systems details](https://docs.cloud.google.com/compute/docs/images/os-details#license-strings). To append the license string, see [Append and validate a user license](https://docs.cloud.google.com/compute/docs/licenses/view-append#append_and_validate_a_user_license).




## CentOS compatible operating systems

The following table summarizes the list of CentOS compatible operating systems that you can migrate to on Google Cloud.

**Distribution** | **Image available on Google Cloud** | **Image license cost** | **Support models**  
---|---|---|---  
[Red Hat Enterprise Linux (RHEL)](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel)***** | Yes | [Premium image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) | [Commercial support (provided by Google Cloud)](https://cloud.google.com/support-hub)  
[Rocky Linux](https://docs.cloud.google.com/compute/docs/images/os-details#rocky_linux) | Yes | None | 

  * [Community support](https://forums.rockylinux.org/)
  * [Commercial support (provided by Google Cloud)](https://cloud.google.com/support-hub)
  * [Commercial support (provided by CIQ)](https://console.cloud.google.com/marketplace/product/ciqrocky-public/ciq-supported-rocky-linux-8)

  
[Alma Linux](https://docs.cloud.google.com/compute/docs/images#almalinux) | Yes | None | 

  * [Community support](https://forums.almalinux.org/)
  * [Commercial support (provided by AlmaLinux)](https://almalinux.org/)

  
[CentOS Stream](https://docs.cloud.google.com/compute/docs/images/os-details#centos) | Yes | None | [Community support](https://discussion.fedoraproject.org/c/neighbors/centos/)  
[SUSE Multi-Linux Support (SMLS)](https://console.cloud.google.com/marketplace/product/mp-images-public/suse-multi-linux-support) | No** | [Premium image pricing](https://console.cloud.google.com/marketplace/product/mp-images-public/suse-multi-linux-support) | [Commercial support (provided by SUSE)](https://www.suse.com/products/multi-linux-support/)  
  
***** RHEL on-demand images are available on Google Cloud. We also support RHEL Cloud Access (BYOS) subscription based gold images. For more information about RHEL's Cloud Access program, see [Red Hat Cloud Access](https://www.redhat.com/en/technologies/cloud-computing/cloud-access).

****** If you use SMLS for your existing instances, you don't need a new image because SUSE offers an in-place conversion. With an in-place conversion, you will receive enterprise support from SUSE regardless of the OS distribution of the original boot image.

### Promotional offers from Red Hat

Red Hat in partnership with Google is committed to helping you migrate from CentOS to RHEL. To help with this migration, we are providing promotional offers to qualified customers subject to approval from Red Hat. If you are interested in learning more about the RHEL promotional offers, contact your Google Cloud account representative.

### Promotional offers from CIQ for CentOS

In partnership with Google, CIQ is providing promotional discounts for long term support for all CentOS customers on Google Cloud. [CIQ Bridge](http://ciq.com/products/ciq-bridge/google-cloud/?utm_source=gc&utm_medium=gcinbound&utm_campaign=centos-eol-guidance) can help ensure your CentOS systems remain secure, compliant and fully operational for up to 3 years.

## Other operating systems

If you do not require a CentOS compatible operating system, the following options are available.

**Distribution** | **Image available on Google Cloud** | **Image license cost** | **Support models**  
---|---|---|---  
[Ubuntu LTS](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_lts) | Yes | None | The following options are available:  


  * [Community support](https://ubuntu.com/support/community-support)
  * [Commercial support (Ubuntu)](https://ubuntu.com/advantage)

  
[Debian](https://docs.cloud.google.com/compute/docs/images/os-details#debian) | Yes | None | [Community support](https://www.debian.org/support)  
[OpenSUSE](https://docs.cloud.google.com/compute/docs/images#opensuse) | Yes | None | [Community support](https://forums.opensuse.org/)  
[Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_pro) | Yes | [Premium image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) | [Commercial support (Google Cloud)](https://cloud.google.com/support-hub)  
[SLES](https://docs.cloud.google.com/compute/docs/images/os-details#suse_linux_enterprise_server_sles) | Yes | [Premium image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) | [Commercial support (Google Cloud)](https://cloud.google.com/support-hub)  
  
## Using the CentOS Vault

**Caution:** The CentOS vault is a snapshot of older trees that have been removed from the main CentOS servers. It doesn't receive updates. CentOS doesn't support using the vault and Google doesn't recommend its usage.

As part of the CentOS deprecation, all content was removed from the CentOS 7 repositories. If it is necessary to install new packages on an existing CentOS 7 system, you can switch repositories from the supported `mirror.centos.org` to the unsupported `vault.centos.org`.

To switch to the CentOS vault repositories, you can run the following command:
    
    
    sed -i -e s/mirror.centos.org/vault.centos.org/g -e s/^#baseurl=/baseurl=/g -e s/^mirrorlist=/#mirrorlist=/g /etc/yum.repos.d/CentOS-*.repo

You can also provide this command during VM creation by using a [startup script](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux).

For more information about the CentOS vault, see the [CentOS vault readme](https://vault.centos.org/readme.txt).

## What's next

  * Learn more about [images](https://docs.cloud.google.com/compute/docs/images) on Compute Engine.
  * Learn more about the [operating systems](https://docs.cloud.google.com/compute/docs/images/os-details) that are available on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
