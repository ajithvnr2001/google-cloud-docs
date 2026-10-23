---
url: https://docs.cloud.google.com/vmware-engine/docs/service-announcements/
title: Latest service announcements \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:44.808534+00:00
---

# Latest service announcements  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/service-announcements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Support ](https://docs.cloud.google.com/vmware-engine/docs/support)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Latest service announcements

Learn about Google Cloud VMware Engine changes such as upgrades, backward-incompatible API changes, product or feature deprecations, mandatory migrations, or potentially disruptive maintenance.

For previous service announcements, see [Archived service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive).

## August 24, 2026

The VMware Engine operations team is updating VMware components to newer versions in August 2026. You will receive an email specifying the maintenance windows for your private cloud.

### Update contents

This update addresses security vulnerabilities described in Broadcom Security Advisory [VMSA-2026-0006](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017).

For details about the changes, see the VMware release notes:

  * [vCenter Server](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3k-release-notes.html)
  * [ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3k-release-notes.html)



### VMware component versions post-update

VMware Component | Version | Build  
---|---|---  
vCenter Server | 8.0 Update 3k | 25600417  
ESXi | 8.0 Update 3k | 25595708  
  
### Update schedule

Updates begin in August 2026. VMware Engine sends maintenance schedule notifications by email to all project users and any [additional configured email addresses](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts). A reminder is sent one hour before the update starts.

### Update actions and impact

Updates are applied in a rolling sequence to minimize disruption:

  * **vCenter Server** : The vCenter UI and API are unavailable for up to 60 minutes (typically under 30 minutes).
  * **Network (NSX Edge)** : NSX Edge VMs are updated during off-peak hours (Monday–Friday, 8:00 PM to 8:00 AM local time). Traffic might experience a 1–2 second interruption during VM failover or BGP re-establishment.
  * **Workload VMs (ESXi)** : Hosts enter maintenance mode sequentially, automatically migrating VMs to other hosts in the cluster before updating.



#### Preparation steps

  * **Review or reschedule the maintenance window** : View or change the scheduled time in the [Update center](https://docs.cloud.google.com/vmware-engine/docs/update-center).
  * **Verify third-party solutions** : Ensure backup, monitoring, and disaster recovery tools connected to vCenter are compatible with the target versions.
  * **Check custom configurations** : Complete the steps in [Preparing private clouds for updates](https://docs.cloud.google.com/vmware-engine/docs/concepts-maintenance-updates#preparation). Configurations that prevent hosts from entering maintenance mode are disabled during the update.



### Update FAQs

**Is maintenance included in the service cost?**

Yes. Routine updates and patches are included with your VMware Engine service.

**How long does the update take?**

Duration depends on cluster size, storage utilization, and private cloud complexity, ranging from a few hours to several days.

**Is there workload downtime during the update?**

Workload VM downtime is not expected. Ensure that your private cloud has at least 30% free storage capacity before the update begins.

**What notifications are sent?**

VMware Engine sends the following notifications:

  * Initial schedule notification email
  * Console notification banners in the Update Center, vCenter, and NSX Manager
  * Advance reminder emails at 1 week, 24 hours, and 1 hour before maintenance
  * Completion confirmation email



**Is post-update action required?**

No action is required after the update completes.

**How do I track update progress?**

Track progress in the [Update center](https://docs.cloud.google.com/vmware-engine/docs/update-center).

**Where can I get support?**

For questions or assistance, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## June 24, 2026

The VMware Engine operations team is initiating updates of the HCX Manager Appliance to version 4.11.4. You will receive an email with the planned maintenance windows of the upgrade for your private cloud.

### Reasons for the upgrade

Broadcom has identified an issue in HCX 4.11.3 that affects private clouds with Mobility Optimized Networking (MON) enabled. This issue causes a "RestartZMQ" service panic, which leads to a crash and restart of the Network Extension (NE) appliance services.

Upgrading to HCX 4.11.4 provides a permanent resolution for this issue, stabilizing MAC learning and traffic steering for MON-enabled segments. For more details, see the Broadcom article [HCX Extended VLANs with MON Enabled Fail to Pass Traffic After CGW Service Restart](https://knowledge.broadcom.com/external/article/429789/hcx-extended-vlans-with-mon-enabled-fail.html).

### Upgrade contents

The upgrade contents are detailed in the VMware release notes:

  * [HCX](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/hcx-4-11-release-notes/vmware-hcx-4114-release-notes.html)



### Action required

This maintenance covers only the HCX Manager Appliance upgrade. You're responsible for performing the upgrade operations for the following components:

  * HCX On-Prem/Connectors
  * HCX Service Mesh Appliances



For more information, see the Broadcom article [Upgrade procedure to HCX 4.11.4](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/updating-vmware-hcx/about-hcx-service-updates.html).

### Upgrade procedure and impact

Review the upgrade procedure and expected impacts:

  * **Ongoing migrations:** Make sure that there are no ongoing migrations during the upgrade.
  * **Downtime:** The HCX Manager is unavailable for approximately 5 minutes during the upgrade process.
  * **Scheduled maintenance window:** To minimize disruption, the upgrade is performed during your scheduled maintenance window. You can view or change the schedule using the VMware Engine [Update center](https://docs.cloud.google.com/vmware-engine/docs/update-center). If you're not using HCX in your private cloud, this upgrade doesn't impact your environment.



## June 1, 2026

All 3-year (36-month) post-paid `ve2` [committed use discounts (CUDs)](https://docs.cloud.google.com/vmware-engine/docs/cud) for Google Cloud VMware Engine purchased after May 31, 2026, will terminate on October 15, 2028. 3-year CUD pricing will apply, regardless of the actual term of the CUD. Additionally, 3-year pre-paid CUDs are no longer available; only 1-year pre-paid CUDs are available.

## May 20, 2026

All 1-year [committed use discounts (CUDs)](https://docs.cloud.google.com/vmware-engine/docs/cud) for Google Cloud VMware Engine `ve1` SKUs are now End-of-Sale across the europe-west2 (London, UK) region. You can continue to use `ve1` nodes with on-demand pricing. This change doesn't affect existing CUDs. You can also use `ve2` nodes, including `ve2` CUDs.

This change affects the following 1-year commitments:

Node type | Commitment type | SKU ID  
---|---|---  
Google Cloud VMware Engine VE1 Standard 72 Node | Commitment - 1 year - dollar based Unlicensed - BYOL | `D13D-E972-9357`  
Google Cloud VMware Engine VE1 Standard 72 Node | Prepay Commitment - 1 year - dollar based Unlicensed - BYOL | `85C5-6A47-5974`  
Google Cloud VMware Engine VE1 Standard Storage Only Node | Commitment - 1 year - dollar based Unlicensed - BYOL | `0219-A3C9-5C9A`  
Google Cloud VMware Engine VE1 Standard Storage Only Node | Prepay Commitment - 1 year - dollar based Unlicensed - BYOL | `4CEE-C7F0-5FCB`  
  
For the regional availability of `ve1` SKUs, see [Google Cloud VMware Engine node types](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types). For `ve2` node pricing in the region, see [VMware Engine pricing](https://cloud.google.com/vmware-engine/pricing).

## March 24, 2026

Beginning April 15, 2026, Google Cloud VMware Engine uses Essential Contacts exclusively for email notifications. To avoid missing important notifications about service events, you must set up Essential Contacts in your Google Cloud VMware Engine projects. For more information, see [Overview of Google Cloud VMware Engine monitoring](https://docs.cloud.google.com/vmware-engine/docs/concepts-monitoring).

## February 16, 2026

The Google Cloud VMware Engine operations team is initiating essential maintenance of the network infrastructure. This maintenance involves upgrading the network switch fabric software to improve equipment robustness, redundancy, and to apply the latest security patches.

The planned network maintenance is limited to the Google Cloud VMware Engine network fabric. No updates or upgrades are performed on VMware components (vCenter, NSX, HCX, or ESXi hosts) of your private cloud as part of this maintenance.

This maintenance is carried out on the common network infrastructure that supports all private clouds in a given region. Consequently, the maintenance schedule isn't customized on a private cloud basis.

### Maintenance Schedule & Communication

The maintenance is carried out across all zones and regions with a specific schedule for each VMware Engine placement group.

The maintenance is scheduled in specific windows (typically 4 hours). You can view the specific start and end times for your private cloud in the notifications sent to your team.

### Notifications

VMware Engine sends the following notifications about this maintenance to all users of VMware Engine using Essential Contacts:

  * **Announcement Notification:** Sent at least 14 days in advance for each of your private clouds, identifying the schedule.
  * **24-Hour Notice:** Sent one day prior to the start of the maintenance event.
  * **1-Hour Notice:** Sent one hour prior to the start of the maintenance event.
  * **Completion Notification:** Sent immediately upon the successful completion of the maintenance.



### Maintenance Scope and Impact

You can expect this maintenance to have the following scope and impact:

  * **Scope:** Google Cloud VMware Engine network fabric directly attached to your private cloud's nodes.
  * **Impact:** This maintenance is performed using In-Service Software Upgrade (ISSU). 
    * **Non-Disruptive:** We don't expect any disruption to network traffic or workload VMs.
    * **No Packet Loss:** The upgrade is designed to be hitless.
    * **No Hardware Resets:** Switches don't require a reload or a physical maintenance mode entry or exit that affects links.
  * **Required actions:** No action is required from you. Google Cloud VMware Engine monitors and ensures the stability of the service throughout the window.
  * **Suggested actions:** Ensure your team is aware of the maintenance schedule. While no impact is expected, it is always best practice to be aware of active maintenance windows affecting your environment.



### Maintenance FAQs

Why are you doing the upgrade?
    Our technology partners have delivered newer software versions that provide higher robustness, security, and redundancy for critical infrastructure components.
How does this maintenance improve my Google Cloud VMware Engine experience?
    Keeping the network fabric up to date ensures that your production applications are always available and that Google engineers can continue to deliver new features securely.
Does this cause a service impact to my production applications?
    No. Unlike previous maintenance cycles, this maintenance uses ISSU (In-Service Software Upgrade) designed to upgrade the network fabric without impacting the data path.
Are any software changes made to VMware components?
    No, this network infrastructure maintenance doesn't have any impact on software versions of VMware components in your private cloud.
How do I know when the maintenance has been completed?
    The VMware Engine operations team sends notifications using Essential Contacts at the start of maintenance and again upon its completion.
How can I get help?
    If you have any questions about the upgrade or need any help after the maintenance, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## October 31, 2025

Due to Broadcom's recent licensing changes, Google Cloud VMware Engine nodes must use VCF Portable licenses starting November 1, 2025. Therefore, we are restricting on-demand usage of Google Cloud VMware Engine to your current usage. To enforce this, we adjusted the quota for each project across all Google Cloud regions to your current usage in each region. This change applies to both `ve1` and `ve2`, and covers all [node types](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types). If a region has no usage, we set the quota for that region for any specific hardware SKU to zero. If you have CUDs for new nodes purchased on or before October 15, 2025 and need to expand your Google Cloud VMware Engine using these CUDs, submit a [Quota Increase Request](https://docs.cloud.google.com/vmware-engine/quotas#requesting_quota). Google takes three days to review and approve this quota request.

## October 3, 2025

This is to notify you about upcoming changes in licensing model with Google Cloud VMware Engine following [Broadcom's recent announcement](https://blogs.vmware.com/cloud-foundation/2025/08/29/vmware-cloud-foundation-cloud-on-your-terms/) to move to a "bring your own" subscription model for VMware Cloud Foundation (VCF).

You can renew or add additional capacity of VMware Engine nodes with VCF-license included until **October 15, 2025**. After that, Google Cloud isn't able to sell new VMware Engine VCF license-included nodes. You can buy new VMware Engine BYOL nodes and use them with "bring your own" VCF subscriptions (purchased by you from Broadcom) for new capacity after **October 15, 2025**.

For any questions, please reach out to your Google Cloud sales team, who can help review your specific scenarios, discuss the implications of these changes for your organization, and help you manage this transition.

## July 15, 2025

The VMware Engine operations team updates VMware components to newer versions in July 2025. You receive an email with the planned maintenance windows for the update.

### Update contents

VMware Engine provides access to the most up-to-date features and functions of vSphere. The VMware stack updates from version 7.0 Update 3 to the [VMware Cloud Foundation (VCF) 5.2.1 stack](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-521-release-notes.html). The update lets you use new features of vSphere, vSAN, and NSX.

The following VMware release notes provide more information about the update contents:

  * [vCenter Server](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3e-release-notes.html)
  * [ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3f-release-notes.html)
  * [NSX](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/release-notes/vmware-nsx-4221-release-notes.html)
  * [HCX](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/hcx-4-10-release-notes/vmware-hcx-4103-release-notes.html)



### VMware component versions post-update

VMware Component | Version | Build  
---|---|---  
vCenter Server | 8.0 Update 3e | 24674346  
ESXi | 8.0 Update 3f | 24784735  
NSX | 4.2.2.1 | 24765084  
HCX | 4.10.3 | 24447633  
  
### Update schedule

This update is scheduled to start in July 2025. You receive an email notification with the planned maintenance windows of the update for your private cloud. The VMware Engine operations team sends another email notification an hour before the update starts. The system sends notifications to all VMware Engine users and any [additional configured email addresses](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts).

### Pre-update required actions

VMware Engine enables Secure Boot on your ESXi nodes, which introduces additional security constraints. This security setting prevents the Zerto Non-VAIO solution from functioning.

If you use Zerto for disaster recovery in your VMware Engine private clouds, you must update your existing Zerto vCenter Plugin to version 10.0_U7 and convert to a VAIO-based solution. This conversion must be completed before VMware Engine can perform updates on your private clouds. Specific changes required for Zerto to support VMware Engine can be found in the [Configure a Zerto VAIO-based solution in VMware Engine private clouds](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-configure-zerto-vaio-solution) guide.

For additional information, refer to the [VMware Engine Zerto configuration requirements](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-zerto) and [VAIO with Zerto: Frequently Asked Questions (FAQs)](https://help.zerto.com/bundle/VAIO_FAQs/page/vaio_with_zerto_frequently_asked_questions_faqs_.html). Contact Zerto directly with any concerns regarding the update and conversion process.

**Important:** Updating to vSphere 8.0 disables Zerto Non-VAIO replications.

### Update actions

VMware Engine performs the update in a rolling fashion to ensure that your private clouds and virtual machines are not affected. vCenter isn't accessible for up to 60 minutes (takes less than 30 minutes on average) during the update. NSX Edge VMs vMotion during the maintenance period, and there is a one to two seconds network disconnect when the NSX Edge VM fails over or BGP sessions are reestablished.

#### Private cloud upgrade impact

**Network impact** : NSX Edge VM update is performed during non-business hours Monday - Friday 8 PM to 8 AM local time of the private cloud. During this operation, there will be a brief period of VM failover and BGP sessions getting reestablished, which can take seconds.

**VM impact** : ESXi nodes are placed into maintenance mode, which migrates all VMs on the node to other nodes in the cluster. This process allows each ESXi node to be updated during the update window.

#### Prepare the upgrade

**Review (or change) proposed timeframe** : Gain control over your update schedule with the new VMware Engine [Update center](https://docs.cloud.google.com/vmware-engine/docs/update-center). You can manage and schedule your updates directly.

**Integrate with VMware third-party solutions** : Prior to the update, make sure any add-on solutions deployed on your private cloud vCenter are compatible with the new versions. Examples include backup, monitoring, disaster recovery orchestrator, and other tools. Check with the solution vendor and update third-party tools ahead of time to avoid any incompatibility after the update.

**Custom configurations** : Review and take the steps required for the [preparation of private clouds](https://docs.cloud.google.com/vmware-engine/docs/concepts-maintenance-updates#preparation) for update. VMware Engine disables any configuration that impacts the host entering maintenance mode.

### Upgrade FAQs

**Does the upgrade cost anything?**

No, your organization is not charged for the upgrade. All new capabilities of vSphere are covered by the service.

**How long will the upgrade take?**

Upgrades can take anywhere from a few hours to a few days, depending on the complexity of your deployment, the number of clusters, and the amount of data present on your private cloud.

**Does the upgrade cause any issues?**

We don't expect downtime during the upgrade process. However, we recommend that you check with solution vendors of any deployed solutions on your private cloud for compatibility with the VCF 5.2.1 stack and make sure you have enough free storage capacity—over 30%—for the upgrade to be performed.

**How will I be notified?**

VMware Engine sends the following notifications about this update to all users of the VMware Engine portal, and to any email addresses that are configured to receive email alerts:

  * Initial notification email about the upcoming maintenance.
  * Notification banners on the Update Center page.
  * Notification banners on vCenter and NSX-T manager about the upcoming maintenance.
  * 1 week advance notification before the start of the update.
  * 24-hour advance notification before the start of the update.
  * 1 hour notification before the start of the update.
  * A final notification email upon completion of the maintenance.



**Do I need to do anything after the upgrade?**

No action is required from you after the upgrade. You can check the versions of VMware components and use all the new features available with this upgrade.

**How will I know when the upgrade has completed?**

You receive notifications of the upgrade progress and completion directly within the VMware Engine Update center. Additionally, the VMware Engine operations team sends an email upon completion. Make sure you have email alerts enabled to receive these notifications. You can configure additional email alerts to notify other relevant users.

**How can I get help?**

If you have any questions about the upgrade or need any help after the upgrade, contact [Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## May 19, 2025

The VMware Engine operations team updates VMware components to newer versions in May 2025. You receive an email with the planned maintenance windows for the update.

### Update contents

VMware Engine provides access to the most up-to-date features and functions of vSphere. The VMware stack updates from version 7.0 Update 3 to the [VMware Cloud Foundation (VCF) 5.2.1 stack](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes/vmware-cloud-foundation-521-release-notes.html). The update lets you use new features of vSphere, vSAN, and NSX.

The following VMware release notes provide more information about the update contents:

  * [vCenter Server](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/vcenter-server-update-and-patch-release-notes/vsphere-vcenter-server-80u3e-release-notes.html)
  * [ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/release-notes/esxi-update-and-patch-release-notes/vsphere-esxi-80u3e-release-notes.html)
  * [NSX](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/release-notes/vmware-nsx-4212-release-notes.html)
  * [HCX](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-10/hcx-4-10-release-notes/vmware-hcx-4103-release-notes.html)



### VMware component versions post-update

VMware Component | Version | Build  
---|---|---  
vCenter Server | 8.0 Update 3e | 24674346  
ESXi | 8.0 Update 3e | 24674464  
NSX | 4.2.1.2 | 24476729  
HCX | 4.10.3 | 24447633  
  
### Update schedule

This update is scheduled to start in May 2025. You receive an email notification with the planned maintenance windows of the update for your private cloud. The VMware Engine operations team sends another email notification an hour before the update starts. The system sends notifications to all VMware Engine users and any [additional configured email addresses](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts).

### Pre-update required actions

VMware Engine enables Secure Boot on your ESXi nodes, which introduces additional security constraints. This security setting prevents the Zerto Non-VAIO solution from functioning.

If you use Zerto for disaster recovery in your VMware Engine private clouds, you must update your existing Zerto vCenter Plugin to version 10.0_U7 and convert to a VAIO-based solution. This conversion must be completed before VMware Engine can perform updates on your private clouds.

For additional information, refer to [VAIO with Zerto: Frequently Asked Questions(FAQs)](https://help.zerto.com/bundle/VAIO_FAQs/page/vaio_with_zerto_frequently_asked_questions_faqs_.html). Contact Zerto directly with any concerns regarding the update and conversion process.

**Important:** Updating to vSphere 8.0 disables Zerto Non-VAIO replications.

### Update actions

VMware Engine performs the update in a rolling fashion to ensure that your private clouds and virtual machines are not affected. vCenter isn't accessible for up to 60 minutes (takes less than 30 minutes on average) during the update. NSX Edge VMs vMotion during the maintenance period, and there is a one to two seconds network disconnect when the NSX Edge VM fails over or BGP sessions are reestablished.

#### Private cloud upgrade impact

**Network impact** : NSX Edge VM update is performed during non-business hours Monday - Friday 8 PM to 8 AM local time of the private cloud. During this operation, there will be a brief period of VM failover and BGP sessions getting reestablished, which can take seconds.

**VM impact** : ESXi nodes are placed into maintenance mode, which migrates all VMs on the node to other nodes in the cluster. This process allows each ESXi node to be updated during the update window.

#### Prepare the upgrade

**Review (or change) proposed timeframe** : Gain control over your update schedule with the new VMware Engine [Update center](https://docs.cloud.google.com/vmware-engine/docs/update-center). You can manage and schedule your updates directly.

**Integrate with VMware third-party solutions** : Prior to the update, make sure any add-on solutions deployed on your private cloud vCenter are compatible with the new versions. Examples include backup, monitoring, disaster recovery orchestrator, and other tools. Check with the solution vendor and update third-party tools ahead of time to avoid any incompatibility after the update.

**Custom configurations** : Review and take the steps required for the [preparation of private clouds](https://docs.cloud.google.com/vmware-engine/docs/concepts-maintenance-updates#preparation) for update. VMware Engine disables any configuration that impacts the host entering maintenance mode.

### Upgrade FAQs

**Does the upgrade cost anything?**

No, your organization is not charged for the upgrade. All new capabilities of vSphere are covered by the service.

**How long will the upgrade take?**

Upgrades can take anywhere from a few hours to a few days, depending on the complexity of your deployment, the number of clusters, and the amount of data present on your private cloud.

**Does the upgrade cause any issues?**

We don't expect downtime during the upgrade process. However, we recommend that you check with solution vendors of any deployed solutions on your private cloud for compatibility with the VCF 5.2.1 stack and make sure you have enough free storage capacity—over 30%—for the upgrade to be performed.

**How will I be notified?**

VMware Engine sends the following notifications about this update to all users of the VMware Engine portal, and to any email addresses that are configured to receive email alerts:

  * Initial notification email about the upcoming maintenance.
  * Notification banners on the Update Center page.
  * Notification banners on vCenter and NSX-T manager about the upcoming maintenance.
  * 1 week advance notification before the start of the update.
  * 24-hour advance notification before the start of the update.
  * 1 hour notification before the start of the update.
  * A final notification email upon completion of the maintenance.



**Do I need to do anything after the upgrade?**

No action is required from you after the upgrade. You can check the versions of VMware components and use all the new features available with this upgrade.

**How will I know when the upgrade has completed?**

You receive notifications of the upgrade progress and completion directly within the VMware Engine Update center. Additionally, the VMware Engine operations team sends an email upon completion. Make sure you have email alerts enabled to receive these notifications. You can configure additional email alerts to notify other relevant users.

**How can I get help?**

If you have any questions about the upgrade or need any help after the upgrade, contact [Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## March 12, 2024

On March 12, 2024, the VMware Engine operations team continues the essential network infrastructure maintenance. This maintenance improves equipment robustness and applies security patches.

The planned network maintenance is limited to the Google Cloud VMware Engine network fabric. No updates or upgrades are performed on VMware components of your private cloud as part of this maintenance.

This maintenance is carried out on the common network infrastructure that supports all private clouds in a given region. This maintenance schedule isn't customized on a private cloud basis.

### Maintenance schedule and communication

The maintenance is carried across all zones and regions but with a specific schedule for each VMware Engine [placement group](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware#placement_groups). The maintenance is rolled out during off-business hours, and lasts four (4) hours every day between 2 AM and 6 AM of the region local time zone.

#### Notifications

VMware Engine sends the following notifications about this maintenance to all users of the VMware Engine portal and to any email addresses that are [configured to receive email alerts](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts):

  * A general notification at least seven (7) days in advance for each of your private clouds identifying the week that it's scheduled for maintenance.
  * 24-hour and 1-hour advance notifications before the start of any impacting maintenance event.
  * A final notification upon completion of the maintenance.



### Maintenance scope and impact

You can expect this maintenance to have the following scope and impact:

  * **Scope:** VMware Engine network fabric directly attached to your private cloud's nodes.

  * **Impact:** Each node might go through a minor disruption up to two times during two maintenance windows (separate days). VMware Engine nodes have a redundant uplink configuration for NSX-T Edge and the distributed virtual switches (DVS). There are two types of impact expected:

    * Network traffic impact to DVS links on ESXi nodes. We expect a network traffic impact of up to two seconds for the failover of an active DVS link on an ESXi node.
    * Network traffic impact to NSX-T Edge. Failover events occur when the connected switch is upgraded. The failover to the standby entity takes up to seven seconds for NSX-T Edge. Such failover can take place up to two times while both the redundant top of rack switches undergo maintenance. However, it's possible that the failover might need to occur only once in your private cloud.
  * **Required actions:** No action is required from you. Google Cloud VMware Engine monitors and ensures restoration of service.

  * **Suggested actions:** Ensure your team is aware of the maintenance and is available to validate any critical application during the maintenance process and after the process is complete. Take additional care if your workloads are sensitive to the network outages mentioned.




### Maintenance FAQs

Why are you doing the upgrade?
    Our technology partners have delivered newer software versions that provide higher robustness, security, and redundancy for critical infrastructure components.
How does this maintenance improve my Google Cloud VMware Engine experience?
    Keeping the network fabric up to date ensures that your production applications are always available and that Google engineers can continue to deliver new features.
Does this cause a service impact to my production applications?
    Maintenance can cause an impact to the workload VMs if they cannot tolerate short gaps in connectivity.
Are any software changes made to VMware components?
    No, this network infrastructure maintenance doesn't have any impact on software versions of VMware components in your private cloud.
How do I know when the maintenance has been completed?
    The VMware Engine operations team sends email notifications at the start of maintenance and again upon its completion.
Do I need to do anything after the maintenance?
    No action is required from you after the maintenance. You can check that your applications are operating as expected during the maintenance and after maintenance is complete.
How can I get help?
    If you have any questions about the upgrade or need any help after the maintenance, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## March 7, 2024

The VMware Engine operations team upgrades VMware components to newer versions beginning mid-March 2024. You receive an email with the planned maintenance windows of the upgrade.

### Upgrade contents

We aim to provide you with access to the most up-to-date features and functions of vSphere. We upgrade the VMware stack from version 7.0 Update 2 to 7.0 Update 3 and the NSX-T stack from version 3.1.2 to 3.2.3.1. The upgrade lets you use new features of vSphere, vSAN, and NSX-T.

Learn more about the upgrade contents in the VMware release notes:

  * [vCenter](https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-vcenter-server-70u3o-release-notes/index.html)
  * [ESXi](https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-70u3o-release-notes/index.html)
  * [NSX-T](https://docs.vmware.com/en/VMware-NSX/3.2.3.1/rn/vmware-nsxt-data-center-3231-release-notes/index.html)
  * [HCX](https://docs.vmware.com/en/VMware-HCX/4.6.2/rn/vmware-hcx-462-release-notes/index.html)



### VMware components post-upgrade

VMware component | Version | Build  
---|---|---  
vCenter Server | 7.0 Update 3p | 23085514  
ESXi | 7.0 Update 3o | 23066467  
NSX-T | 3.2.3.1.hp | 3263187  
HCX | 4.6.2 | Cloud build: 21779414  
  
### Upgrade schedule

This upgrade is scheduled between March and June 2024.

The upgrade is carried out in a rolling fashion, hence we don't anticipate any disruptions to your workload VMs. There is a transient unavailability of vCenter for up to 15 minutes during the upgrade to the new version. NSX-T edge VMs move to another host during the upgrade and might cause a brief 1 to 7 second disruption to traffic during this change.

### How does this change impact your private cloud?

  * **Upgrade steps that are potentially impacting:** vCenter and NSX-T Edge are upgraded during non-business hours. The non-business hours are based on the time zone of the region where the private cloud is deployed.

  * **Upgrade steps that are non-impacting:** Your private cloud is augmented by an additional node and ESXi upgrades are performed on a rolling basis after gracefully putting each node into maintenance mode. These upgrades are carried out in business and off-business hours.




### What do you need to do?

  * **Review (or change) proposed maintenance schedule:** As communicated earlier, we are informing you about the impending upgrade of your private cloud with 15 days notice. Review the notification for the time window for the upgrade. Should you need further assistance in rescheduling the upgrade, contact Google Customer support. We request you to inform us 3 days in advance to be able to accommodate your request for rescheduling the upgrade.

  * **VMware third-party solutions:** Before the upgrade, ensure that any add-on solutions deployed on your private cloud vCenter are compatible with the versions mentioned previously. Examples are backup, monitoring, disaster recovery orchestrator and other similar tools. Check with the solution vendor and upgrade solutions ahead of time if necessary to avoid any incompatibility after the upgrade.

  * **On-premises HCX Preparation:** Ensure that your version of HCX on-premises is compatible with cloud-based HCX. In the next weeks, there is a second message regarding the Cloud HCX upgrade, which takes place at a later date. You may ignore this section if your HCX version is already 4.6.2.

  * **Upgrade preparation:** Ensure that you have taken care of items listed in [Preparation](https://docs.cloud.google.com/vmware-engine/docs/concepts-maintenance-updates#preparation) before the upgrade starts.




### How are you notified?

VMware Engine sends the following notifications about this upgrade to all users of the VMware Engine portal and to any email addresses that are configured to receive email alerts:

  * Notification banners on vCenter and NSX portals about the upcoming upgrade.
  * 30 days notice - A general notification at least 30 days in advance for each of your private clouds.
  * 15 days notice - A general notification at least 15 days in advance for each of your private clouds identifying the week it is scheduled for upgrade.
  * 24-hour and 1-hour advance notifications before the start of the upgrade.
  * A notification at the start of the upgrade.
  * A final notification upon completion of the upgrade.
  * Additional notifications are sent for reschedules, extension of schedules or complications.



### Upgrade FAQs

Does it cost my organization anything to upgrade?
    No, your organization is not charged for the upgrade. All new capabilities of vSphere are covered by your service.
How long does the upgrade take?
    Upgrades can take anywhere from a few hours to a few days, depending on the complexity of your deployment, the number of clusters, and the amount of data present on your private cloud.
Does the upgrade break anything?
    We don't expect downtime during the upgrade process. However, we recommend that you check with solution vendors of any deployed solutions on your private cloud for compatibility with vSphere 7.0 and ensure that you have over 30% free storage capacity for the upgrade to be performed.
Do I need to do anything after the upgrade?
    No action is required from you after the upgrade. You can check the versions of VMware components and use all new features available with this upgrade.
How do I know when the upgrade has completed?
    The VMware Engine operations team sends you an email at the start of the upgrade and again upon its completion.
How can I get help?
    If you have any questions about the upgrade or need any help after the upgrade, contact [Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
