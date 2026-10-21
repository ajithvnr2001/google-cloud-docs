---
url: https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive/
title: Archived service announcements \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:07.214072+00:00
---

# Archived service announcements  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Support ](https://docs.cloud.google.com/vmware-engine/docs/support)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Archived service announcements

This page contains service announcements for Google Cloud VMware Engine changes such as upgrades, backward incompatible API changes, product or feature deprecations, mandatory migrations, or potentially disruptive maintenance.

For the latest service announcement, see [Latest service announcement](https://docs.cloud.google.com/vmware-engine/docs/service-announcements).

Date published | Description | Instructions  
---|---|---  
[October 11, 2022](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#2022-10-11) |  Maintenance announcement for VMware Engine network switch upgrades | No action is required from you.  
[May 20, 2022](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#2022-05-20) |  Maintenance announcement for VMware Engine network switch upgrades | No action is required from you.  
[April 29, 2022](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#2022-04-29) |  Update announcement for important security updates to vCenter Server and NSX-T | No action is required from you.  
[February 15, 2022](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#2022-02-15) |  Maintenance announcement for VMware Engine network switch upgrades | No action is required from you.  
[November 22, 2021](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#2021-11-22) |  Update to September 22, 2021 service announcement | See the [Prepare for the upgrade](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#prepare-for-upgrade-2021-09-22) section in the September 22, 2021 service announcement.  
[September 22, 2021](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#2021-09-22) |  Upgrade announcement for the following software:

  * Upgrade VMware stack to version 7.0 Update 2
  * Upgrade NSX-T stack to version 3.1.2

| See the [Prepare for the upgrade](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#prepare-for-upgrade-2021-09-22) section.  
[November 20, 2020](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#2020-11-20) |  Upgrade announcement for the following software:

  * Upgrade VMware stack from version 6.7 to 7.0
  * Upgrade NSX-T stack from version 2.5 to 3.0

| See the [Preparing for the upgrade](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#prepare-for-upgrade-2020-11-20) section.  
  
## October 11, 2022

On October 15, 2022, the VMware Engine operations team will continue the essential network infrastructure maintenance announced in the May 30, 2022 service announcement. This maintenance improves equipment robustness and applies security patches.

The planned network maintenance is limited to the Google Cloud VMware Engine network fabric. No updates or upgrades will be performed on VMware components of your private cloud as part of this maintenance.

This maintenance is carried out on the common network infrastructure that supports all private clouds in a given region. The maintenance schedule cannot be customized on a private cloud basis.

### Maintenance schedule & communication

The maintenance will be carried across all zones and regions but with a specific schedule for each VMware Engine [placement group](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware#placement_groups). The maintenance will be rolled out during off-business hours, and lasts six (6) hours every day between 12 AM and 6 AM of the region local time zone.

#### Notifications

VMware Engine will send the following notifications about this maintenance to all users of the VMware Engine portal and to any email addresses that are [configured to receive email alerts](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts):

  * A general notification at least seven (7) days in advance for each of your private clouds identifying the week that it's scheduled for maintenance.
  * 24-hour and 1-hour advance notifications before the start of any impacting maintenance event.
  * A final notification upon completion of the maintenance.



### Maintenance scope and impact

You can expect this maintenance to have the following scope and impact:

  * **Scope:** VMware Engine network fabric directly attached to your private cloud's nodes.
  * **Impact:** Each node might go through a minor disruption up to two times during two maintenance windows (separate days). VMware Engine nodes have a redundant uplink configuration for NSX-T Edge and the distributed virtual switches (DVS). There are three types of impact expected:

    * Network traffic impact to DVS links on ESXi nodes. We expect a network traffic impact of up to 2 seconds for the failover of an active DVS link on an ESXi node.
    * Network traffic impact to NSX-T Edge. Failover events will occur when the connected switch is upgraded. The failover to the standby entity takes up to 7 seconds for NSX-T Edge. Such failover can take place up to two times while both the redundant top of rack switches undergo maintenance. However, it's possible that the failover might need to occur only once in your private cloud.
    * Network traffic impact with uplink profile enhancement. We expect a network traffic impact of up to 3 seconds for the reconfiguration of the node uplink profile.
  * **Required actions:** No action is required from you. Google Cloud VMware Engine will monitor and ensure restoration of service.

  * **Suggested actions:** Ensure your team is aware of the maintenance and is available to validate any critical application during the maintenance process and after the process is complete. Take additional care if your workloads are sensitive to the network outages mentioned above.




### Maintenance FAQs

Why are you doing the upgrade?
    Our technology partners have delivered newer software versions that provide higher robustness, security, and redundancy for critical infrastructure components.
How does this maintenance improve my Google Cloud VMware Engine experience?
    Keeping the network fabric up to date ensures that your production applications are always available and that Google engineers can continue to deliver new features.
Will this cause a service impact to my production applications?
    Maintenance can cause an impact to the workload VMs if they cannot tolerate short gaps in connectivity.
Will any software changes be made to VMware components?
    No, this network infrastructure maintenance will not have any impact on software versions of VMware components in your private cloud.
How will I know when the maintenance has been completed?
    The VMware Engine operations team will send email notifications at the start of maintenance and again upon its completion.
Do I need to do anything after the maintenance?
    No action is required from you after the maintenance. You can check that your applications are operating as expected during the maintenance and after maintenance is complete.
How can I get help?
    If you have any questions about the upgrade or need any help after the maintenance, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## May 20, 2022

On May 30, 2022, the VMware Engine operations team will continue the essential network infrastructure maintenance announced in the February 15, 2022 service announcement. This maintenance improves equipment robustness and applies security patches.

The planned network maintenance is limited to the Google Cloud VMware Engine network fabric. No updates or upgrades will be performed on VMware components of your private cloud as part of this maintenance.

This maintenance is carried out on the common network infrastructure that supports all private clouds in a given region. The maintenance schedule cannot be customized on a private cloud basis.

### Maintenance schedule & communication

The maintenance will be carried across all zones and regions but with a specific schedule for each VMware Engine [placement group](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware#placement_groups). The maintenance will be rolled out during off-business hours, and lasts six (6) hours every day between 12 AM and 6 AM of the region local time zone.

#### Notifications

VMware Engine will send the following notifications about this maintenance to all users of the VMware Engine portal and to any email addresses that are [configured to receive email alerts](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts):

  * A general notification at least seven (7) days in advance for each of your private clouds identifying the week it is scheduled for maintenance.
  * 24-hour and 1-hour advance notifications before the start of any impacting maintenance event.
  * A final notification upon completion of the maintenance.



### Maintenance scope and impact

You can expect this maintenance to have the following scope and impact:

  * **Scope:** VMware Engine network fabric directly attached to your private cloud's nodes.
  * **Impact:** Each node might go through a minor disruption up to two times. VMware Engine nodes have a redundant uplink configuration for NSX-T Edge and the distributed virtual switches (DVS). There are two types of impact expected:

    * Network traffic impact to DVS links on ESXi nodes. We expect a network traffic impact of up to 2 seconds for the failover of an active DVS link on an ESXi node.
    * Network traffic impact to NSX-T Edge. Failover events will occur when the connected switch is upgraded. The failover to the standby entity takes up to 7 seconds for NSX-T Edge. Such failover can take place up to two times while both the redundant top of rack switches undergo maintenance. However, it's possible that the failover might need to occur only once in your private cloud.
  * **Required actions:** No action is required from you. Google Cloud VMware Engine will monitor and ensure restoration of service.

  * **Suggested actions:** Ensure your team is aware of the maintenance and is available to validate any critical application during the maintenance process and after the process is complete. Take additional care if your workloads are sensitive to the network outages mentioned above.




### Maintenance FAQs

Why are you doing the upgrade?
    Our technology partners have delivered newer software versions that provide higher robustness, security, and redundancy for critical infrastructure components.
How does this maintenance improve my Google Cloud VMware Engine experience?
    Keeping the network fabric up to date ensures that your production applications are always available and that Google engineers can continue to deliver new features.
Will this cause a service impact to my production applications?
    Maintenance can cause an impact to the workload VMs if they cannot tolerate short gaps in connectivity.
Will any software changes be made to VMware components?
    No, this network infrastructure maintenance will not have any impact on software versions of VMware components in your private cloud.
How will I know when the maintenance has been completed?
    The VMware Engine operations team will send email notifications at the start of maintenance and again upon its completion.
Do I need to do anything after the maintenance?
    No action is required from you after the maintenance. You can check that your applications are operating as expected during the maintenance and after maintenance is complete.
How can I get help?
    If you have any questions about the upgrade or need any help after the maintenance, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## April 29, 2022

The VMware Engine operations team will apply important security updates to vCenter Server and NSX-T beginning early May 2022. The VMware Engine operations team will send an email with the planned maintenance window for each of your private clouds.

### VMware component versions post-upgrade

VMware component | Version | Build  
---|---|---  
vCenter Server | 7.0 Update 2d | 19272235  
NSX-T | 3.1.2 | 19262105  
  
### Maintenance schedule & communication

Maintenance will occur separately for each private cloud. VMware Engine plans to roll out the patch during the off-business hours of each private cloud's region local time zone.

#### Notifications

VMware Engine will send the following notifications about this maintenance to all users of the VMware Engine portal and to any email addresses that are [configured to receive email alerts](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts):

  * A general notification at least seven (7) days in advance for each of your private clouds identifying the week that it's scheduled for maintenance.
  * 6-hour advance notification before the start of any impacting maintenance event.
  * A final notification upon completion of the maintenance.



### Maintenance scope and impact

You can expect this maintenance to have the following scope and impact:

  * **Scope:** vCenter Server and NSX-T Manager appliances in each private cloud.
  * **Impact:** During the maintenance, the vCenter Server and NSX-T Manager appliances running on your private cloud will be unavailable for up to an hour. Typically, the management appliances are inaccessible only for a few minutes. Workload virtual machines on the private cloud are not affected, and we expect no impact to network connectivity.
  * **Required actions:** No action is required from you. Google Cloud VMware Engine will monitor and ensure restoration of service.
  * **Suggested actions:** Verify access to private cloud management appliances after you receive the notification that maintenance is complete.



## February 15, 2022

On February 21, 2022, the VMware Engine operations team will begin essential maintenance of the network infrastructure to improve equipment robustness and apply security patches.

The planned network maintenance is limited to the Google Cloud VMware Engine network fabric. No updates or upgrades will be performed on VMware components of your private cloud as part of this maintenance.

This maintenance is carried out on the common network infrastructure that supports all private clouds in a given region. The maintenance schedule cannot be customized on a private cloud basis.

### Maintenance schedule & communication

The maintenance will be carried across all zones and regions but with a specific schedule for each VMware Engine [placement group](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware#placement_groups). The maintenance will be rolled out during off-business hours, and lasts six (6) hours every day between 12 AM and 6 AM of the region local time zone.

#### Notifications

VMware Engine will send the following notifications about this maintenance to all users of the VMware Engine portal and to any email addresses that are [configured to receive email alerts](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts):

  * A general notification at least seven (7) days in advance for each of your private clouds identifying the week it is scheduled for maintenance.
  * 24-hour and 1-hour advance notifications before the start of any impacting maintenance event.
  * A final notification upon completion of the maintenance.



### Maintenance scope and impact

You can expect this maintenance to have the following scope and impact:

  * **Scope:** VMware Engine network fabric directly attached to your private cloud's nodes.
  * **Impact:** Each node might go through a minor disruption up to two times. VMware Engine nodes have a redundant uplink configuration for NSX-T Edge and the distributed virtual switches (DVS). There are two types of impact expected:

    * Network traffic impact to DVS links on ESXi nodes. We expect a network traffic impact of up to 2 seconds for the failover of an active DVS link on an ESXi node.
    * Network traffic impact to NSX-T Edge. Failover events will occur when the connected switch is upgraded. The failover to the standby entity takes up to 7 seconds for NSX-T Edge. Such failover can take place up to two times while both the redundant top of rack switches undergo maintenance. However, it's possible that the failover might need to occur only once in your private cloud.
  * **Required actions:** No action is required from you. Google Cloud VMware Engine will monitor and ensure restoration of service.

  * **Suggested actions:** Ensure your team is aware of the maintenance and is available to validate any critical application during the maintenance process and after the process is complete. Take additional care if your workloads are sensitive to the network outages mentioned above.




### Maintenance FAQs

Why are you doing the upgrade?
    Our technology partners have delivered newer software versions that provide higher robustness, security, and redundancy for critical infrastructure components.
How does this maintenance improve my Google Cloud VMware Engine experience?
    Keeping the network fabric up to date ensures that your production applications are always available and that Google engineers can continue to deliver new features.
Will this cause a service impact to my production applications?
    Maintenance can cause an impact to the workload VMs if they cannot tolerate short gaps in connectivity.
Will any software changes be made to VMware components?
    No, this network infrastructure maintenance will not have any impact on software versions of VMware components in your private cloud.
How will I know when the maintenance has been completed?
    The VMware Engine operations team will send email notifications at the start of maintenance and again upon its completion.
Do I need to do anything after the maintenance?
    No action is required from you after the maintenance. You can check that your applications are operating as expected during the maintenance and after maintenance is complete.
How can I get help?
    If you have any questions about the upgrade or need any help after the maintenance, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## November 22, 2021

On December 1, 2021, the VMware Engine operations team will continue the upgrades announced in the September 22, 2021 service announcement. You will receive an email with the planned maintenance windows of the upgrade. Private clouds upgraded during this time frame will have their HCX Cloud appliances upgraded to HCX version 4.2.2 Build 18868175 which includes a mandatory security update.

We also recommend that you upgrade your on-premises HCX appliance or previously upgraded HCX Cloud appliance (for upgrades conducted before November 1, 2021) as soon as possible. For more details, refer to the [VMware HCX release notes](https://docs.vmware.com/en/VMware-HCX/4.2/rn/VMware-HCX-422-Release-Note.html).

### Upgrade contents

We aim to provide you with access to the most up-to-date features and functions of vSphere. We will upgrade the VMware stack from version 7.0 Update 1 to 7.0 Update 2 and the NSX-T stack from version 3.0 to 3.1.2. The upgrade lets you use new features of vSphere, vSAN, and NSX-T.

Learn more about the upgrade contents in the VMware release notes:

  * [vCenter Server](https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-vcenter-server-70u2d-release-notes.html)
  * [ESXi](https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-70u2c-release-notes.html)
  * [NSX-T](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/rn/VMware-NSX-T-Data-Center-312-Release-Notes.html)
  * [HCX](https://docs.vmware.com/en/VMware-HCX/4.2/rn/VMware-HCX-422-Release-Note.html)



### VMware component versions post-upgrade

VMware component | Version | Build  
---|---|---  
vCenter Server | 7.0 Update 2d | 18455184  
ESXi | 7.0 Update 2c | 18426014  
NSX-T | 3.1.2 | 17883596  
HCX | 4.2.2 |  Cloud build: 18868175   
  
### Upgrade schedule

This upgrade is scheduled between December 1, 2021 and end of January 2022. You will receive an email notification with the planned maintenance windows of the upgrade for your private cloud. Six hours before the upgrade starts, the VMware Engine operations team will send another email notice. Notifications are sent to all users of VMware Engine and any [additional configured email IDs](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts). Another email will be sent once the upgrade is complete.

### Upgrade actions

During the upgrade, VMware Engine will add a new node to your vSphere cluster and place an existing node in maintenance mode. You will not be charged for the temporary node used during the upgrade. The new node maintains availability and capacity of your private cloud during the upgrade process. When VMware components are upgraded, you might see alarms in vCenter Server. The alarms are a part of the maintenance operations performed by the VMware Engine operations team.

Depending on the size and complexity of your deployment, this upgrade might take from a few hours to a few days. The following actions will happen during the upgrade:

  * VMs configured with vSAN storage policy for Failures to Tolerate (FTT) of 0 are changed to vSAN storage policy for FTT of 1 to maintain the [SLA](https://cloud.google.com/vmware-engine/sla).
  * CDs mounted on a VM using a datastore ISO file or client are disconnected.
  * Any in-progress VMware tool installations or upgrades are terminated.
  * VMs with SCSI bus sharing are powered off.
  * DRS rules are disabled during the upgrade and re-enabled after the upgrade.
  * Orphaned or inaccessible VMs are removed from vCenter inventory.



### Prepare for the upgrade

See the [Prepare for the upgrade section](https://docs.cloud.google.com/vmware-engine/docs/service-announcements-archive#prepare-for-upgrade-2021-09-22) in the September 22, 2021 service announcement.

### Upgrade FAQs

Will it cost my organization anything to upgrade?
    No, your organization is not charged for the upgrade. All new capabilities of vSphere are covered by your service.
How long will the upgrade take?
    Upgrades can take anywhere from a few hours to a few days, depending on the complexity of your deployment, the number of clusters, and the amount of data present on your private cloud.
Will the upgrade break anything?
    We don't expect downtime during the upgrade process. However, we recommend that you check with solution vendors of any deployed solutions on your private cloud for compatibility with vSphere 7.0 and ensure that you have enough free storage capacity—over 30%—for the upgrade to be performed.
Do I need to do anything after the upgrade?
    No action is required from you after the upgrade. You can check the versions of VMware components and use all new features available with this upgrade.
How will I know when the upgrade has completed?
    The VMware Engine operations team will send you an email at the start of the upgrade and again upon its completion. Ensure you have turned on [email alerts](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts) to receive notifications from the VMware Engine team. You can configure additional email alerts to notify any other users who need to be notified.
How can I get help?
    If you have any questions about the upgrade or need any help after the upgrade, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## September 22, 2021

The VMware Engine operations team will upgrade VMware components to newer versions beginning mid October 2021. You will receive an email with the planned maintenance windows of the upgrade.

### Upgrade contents

We aim to provide you with access to the most up-to-date features and functions of vSphere. We will upgrade the VMware stack from version 7.0 Update 1 to 7.0 Update 2 and the NSX-T stack from version 3.0 to 3.1.2. The upgrade lets you use new features of vSphere, vSAN, and NSX-T.

Learn more about the upgrade contents in the VMware release notes:

  * [vCenter Server](https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-vcenter-server-70u2d-release-notes.html)
  * [ESXi](https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-70u2c-release-notes.html)
  * [NSX-T](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/rn/VMware-NSX-T-Data-Center-312-Release-Notes.html)
  * [HCX](https://docs.vmware.com/en/VMware-HCX/4.2/rn/VMware-HCX-42-Release-Note.html)



### VMware component versions post-upgrade

VMware component | Version | Build  
---|---|---  
vCenter Server | 7.0 Update 2d | 18455184  
ESXi | 7.0 Update 2c | 18426014  
NSX-T | 3.1.2 | 17883596  
HCX | 4.2.x |  Cloud build: 18422312   
  
### Upgrade schedule

This upgrade is scheduled between October and November 2021. You will receive an email notification with the planned maintenance windows of the upgrade for your private cloud. An hour before the upgrade starts, the VMware Engine operations team will send another email notice. Notifications are sent to all users of VMware Engine and any [additional configured email IDs](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts).

### Upgrade actions

During the upgrade, VMware Engine will add a new node to your vSphere cluster and place an existing node in maintenance mode. The new node maintains availability and capacity of your private cloud during the upgrade process. When VMware components are upgraded, you might see alarms in vCenter Server. The alarms are a part of the maintenance operations performed by the VMware Engine operations team.

Depending on the size and complexity of your deployment, this upgrade might take from a few hours to a few days. The following actions will happen during the upgrade:

  * VMs configured with vSAN storage policy for Failures to Tolerate (FTT) of 0 are changed to vSAN storage policy for FTT of 1 to maintain the [SLA](https://cloud.google.com/vmware-engine/sla).
  * CDs mounted on a VM using a datastore ISO file or client are disconnected.
  * Any in-progress VMware tool installations or upgrades are terminated.
  * VMs with SCSI bus sharing are powered off.
  * DRS rules are disabled during the upgrade and re-enabled after the upgrade.
  * Orphaned or inaccessible VMs are removed from vCenter inventory.



### Prepare for the upgrade

#### VMware HCX

If you currently use HCX and any of the following conditions apply, we recommend you contact [Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/getting-support) about an HCX update:

  * Your on-premises HCX Connector connected to VMware Engine is version 3.5.3 or earlier.
  * Your HCX Manager in VMware Engine is version 3.5.3.
  * Your on-premises vSphere environment connected to VMware Engine is version 5.5.



Your Google representative will also contact you about upgrade preparation from an HCX standpoint. Please note that it is critical to perform steps to prepare for the upgrade, in order to ensure continued support.

#### Update VMware add-ons and third-party solutions

Verify that VMware add-ons and third party solutions deployed on your private cloud vCenter are compatible with the post-upgrade versions mentioned above. Examples of tools include those for backup, monitoring, disaster recovery orchestration, and other similar functions. Check with the solution vendor and update ahead of time if necessary to ensure compatibility after the upgrade.

**Note:** If you use Veeam Backup & Replication, ensure that you are running Veeam Backup & Replication version 11 P20210525 (build 11.0.0.837 P20210525) or later for compatibility with the new VMware stack. You can learn more about Veeam compatibility in [Veeam Backup & Replication support for VMware vSphere](https://www.veeam.com/kb2443).

#### Other upgrade preparation

  * **Check storage capacity:** Ensure your vSphere Cluster's storage space utilization is below 75% to maintain the [SLA](https://cloud.google.com/vmware-engine/sla). If the utilization is above 75%, upgrades might take longer than normal or fail completely. If your storage utilization is higher than 70%, [add a node](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#add-nodes) to expand the cluster and avoid any potential downtime during upgrades.
  * **Change vSAN storage policies with FTT of 0:** Change VMs configured with a vSAN storage policy for Failures to Tolerate (FTT) of 0 to a vSAN storage policy with FTT of 1 to maintain the [SLA](https://cloud.google.com/vmware-engine/sla).
  * **Remove VM CD mounts:** Remove any CDs mounted on your workload VMs.
  * **Complete VMware tool installations:** Complete any installations or upgrades of VMware tools before the scheduled upgrade begins.
  * **Remove SCSI bus sharing on VMs:** Remove SCSI bus sharing on VMs if you don't want the VMs to be powered off.
  * **Remove inaccessible VMs and datastores:** Remove orphaned and inaccessible VMs from vCenter inventory. Remove any inaccessible external datastores.
  * **Disable DRS rules:** DRS rules that pin a VM to a host prevent a node from entering maintenance mode. You can disable the DRS rules before the upgrade and enable them after the upgrade is complete.



### Upgrade FAQs

Will it cost my organization anything to upgrade?
    No, your organization is not charged for the upgrade. All new capabilities of vSphere are covered by your service.
How long will the upgrade take?
    Upgrades can take anywhere from a few hours to a few days, depending on the complexity of your deployment, the number of clusters, and the amount of data present on your private cloud.
Will the upgrade break anything?
    We don't expect downtime during the upgrade process. However, we recommend that you check with solution vendors of any deployed solutions on your private cloud for compatibility with vSphere 7.0 and ensure that you have enough free storage capacity—over 30%—for the upgrade to be performed.
Do I need to do anything after the upgrade?
    No action is required from you after the upgrade. You can check the versions of VMware components and use all new features available with this upgrade.
How will I know when the upgrade has completed?
    The VMware Engine operations team will send you an email at the start of the upgrade and again upon its completion. Ensure you have turned on [email alerts](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts) to receive notifications from the VMware Engine team. You can configure additional email alerts to notify any other users who need to be notified.
How can I get help?
    If you have any questions about the upgrade or need any help after the upgrade, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

## November 20, 2020

The VMware Engine operations team will upgrade VMware components to newer versions beginning mid December 2020. You will receive an email with the planned maintenance dates and times of the upgrade.

### Upgrade contents

We aim to provide you with access to the most up-to-date features and functions of vSphere. We will upgrade the VMware stack from version 6.7 to 7.0 and the NSX-T stack from version 2.5 to 3.0. The upgrade lets you use new features of vSphere, vSAN, and NSX-T and enjoy significant improvements in storage and networking performance.

Learn more about [vSphere 7.0 features](https://blogs.vmware.com/vsphere/2020/03/vsphere-7-features.html) and [NSX-T 3.0 features](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/rn/VMware-NSX-T-Data-Center-30-Release-Notes.html).

### VMware component versions post-upgrade

VMware component | Version | Build  
---|---|---  
vCenter Server | 7.0 U1a | 17004997  
ESXi | 7.0.1 U1a | 17119627  
vSAN | 7.0 U1 | N/A  
NSX-T | 3.0.2 | 16887200  
  
### Upgrade schedule

This upgrade is scheduled between December 2020 and January 2021. You will receive an email notification with the planned maintenance dates and times of the upgrade for your private cloud. An hour before the upgrade starts, the VMware Engine operations team will send another email notice. Notifications are sent to all users of VMware Engine and any [additional configured email IDs](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts).

### Upgrade actions

During the upgrade, VMware Engine will add a new node to your vSphere cluster and place an existing node in maintenance mode. The new node maintains availability and capacity of your private cloud during the upgrade process. When VMware components are upgraded, you might see alarms in vCenter Server. The alarms are a part of the maintenance operations performed by the VMware Engine operations team.

Depending on the size and complexity of your deployment, this upgrade might take from a few hours to a few days. The following actions will happen during the upgrade:

  * VMs configured with vSAN storage policy for Failures to Tolerate (FTT) of 0 are changed to vSAN storage policy for FTT of 1 to maintain the [SLA](https://cloud.google.com/vmware-engine/sla).
  * CDs mounted on a VM using a datastore ISO file or client are disconnected.
  * Any in-progress VMware tool installations or upgrades are terminated.
  * VMs with SCSI bus sharing are powered off.
  * DRS rules are disabled during the upgrade and re-enabled after the upgrade.
  * Orphaned or inaccessible VMs are removed from vCenter inventory.



### Preparing for the upgrade

  * **Check storage capacity:** Ensure your vSphere Cluster's storage space utilization is below 75% to maintain the [SLA](https://cloud.google.com/vmware-engine/sla). If the utilization is above 75%, upgrades might take longer than normal or fail completely. If your storage utilization is higher than 70%, [add a node](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#add-nodes) to expand the cluster and avoid any potential downtime during upgrades.
  * **Check solution compatibility:** Ensure that any add-on solutions deployed on your private cloud vCenter are compatible with vSphere 7.0. Some examples are backup, monitoring tools, and disaster recovery orchestrator and tools. Check with the solution vendor and upgrade these solutions if necessary to avoid any incompatibility after upgrade.
  * **Change vSAN storage policies with FTT of 0:** Change VMs configured with a vSAN storage policy for Failures to Tolerate (FTT) of 0 to a vSAN storage policy with FTT of 1 to maintain the [SLA](https://cloud.google.com/vmware-engine/sla).
  * **Remove VM CD mounts:** Remove any CDs mounted on your workload VMs.
  * **Complete VMware tool installations:** Complete any installations or upgrades of VMware tools before the scheduled upgrade begins.
  * **Remove SCSI bus sharing on VMs:** Remove SCSI bus sharing on VMs if you don't want the VMs to be powered off.
  * **Remove inaccessible VMs and datastores:** Remove orphaned and inaccessible VMs from vCenter inventory. Remove any inaccessible external datastores.
  * **Disable DRS rules:** DRS rules that pin a VM to a host prevent a node from entering maintenance mode. You can disable the DRS rules before the upgrade and enable them after the upgrade is complete.



### Upgrade FAQs

Will it cost my organization anything to upgrade?
    No, your organization is not charged for the upgrade. All new capabilities of vSphere are covered by your service.
How long will the upgrade take?
    Upgrades can take anywhere from a few hours to a few days, depending on the complexity of your deployment, the number of clusters, and the amount of data present on your private cloud.
Will the upgrade break anything?
    We don't expect downtime during the upgrade process. However, we recommend that you check with solution vendors of any deployed solutions on your private cloud for compatibility with vSphere 7.0 and ensure that you have enough free storage capacity—over 30%—for the upgrade to be performed.
Do I need to do anything after the upgrade?
    No action is required from you after the upgrade. You can check the versions of VMware components and use all new features available with this upgrade.
How will I know when the upgrade has completed?
    The VMware Engine operations team will send you an email at the start of the upgrade and again upon its completion. Ensure you have turned on [email alerts](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-account#set_up_email_alerts) to receive notifications from the VMware Engine team. You can configure additional email alerts to notify any other users who need to be notified.
How can I get help?
    If you have any questions about the upgrade or need any help after the upgrade, [contact Cloud Customer Care](http://www.google.com/support/enterprise/go/support_info#cloud).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
