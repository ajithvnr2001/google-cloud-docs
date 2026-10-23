---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-configure-zerto-vaio-solution/
title: Configure a Zerto VAIO-based solution in VMware Engine private clouds \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:51.334498+00:00
---

# Configure a Zerto VAIO-based solution in VMware Engine private clouds  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-configure-zerto-vaio-solution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure a Zerto VAIO-based solution in VMware Engine private clouds

This document explains how to set up a Zerto VAIO-based solution in a VMware Engine private cloud that's running on vSphere 8.x. This solution is required if you need to use Zerto for disaster recovery and migration with vSphere 8.x. [SecureBoot](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#pre-update_required_actions) is enabled by default on ESXi nodes in vSphere 8.x, which prevents the Zerto Non-VAIO solution from functioning. Therefore, setting up the Zerto VAIO-based solution is necessary.

## Prerequisites and requirements

Before you can use VMware Engine to update your private cloud, you must update your Zerto vCenter Plugin to version 10.0_U7 or higher and [convert](https://help.zerto.com/bundle/Linux.ZVM.HTML.10.0_U7/page/Converting_to_VAIO.htm) to a [VAIO-based solution](https://help.zerto.com/bundle/VAIO_FAQs/page/vaio_with_zerto_frequently_asked_questions_faqs_.html). This conversion helps to ensure continuity and successful upgrades of your private cloud.

## Host credential workaround

Zerto requires host-based credentials for VAIO deployments on ESXi servers with [Secure Boot](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#pre-update_required_actions) enabled. Zerto requires a common root password for all hosts in a cluster.

Using a common root password is against Google security best practices. Therefore, in this solution, you use a PowerCLI script that creates a local administrative user with common administrator rights and a shared password on all hosts in the private cloud. You can get this script by contacting Cloud Customer Care.

Note the following:

  * The PowerCLI script is a separate attachment.
  * The administrator user created by the script is removed from hosts after 48 hours.
  * You might need to rerun the script for VRA redeployments or upgrades.
  * If your organization's policies prohibit using a common password across multiple hosts, [contact Zerto](https://support.hpe.com/connect/s/) for alternative solutions.



## Set up Zerto

This procedure assumes a new Zerto deployment on a new VMware Engine private cloud.

  1. Install Zerto ZVM on your VMware Engine private cloud. Use the [service VLAN for network connectivity](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets#configuring_service_subnets) to improve performance and reduce load on NSX.
  2. Sign in to the [Zerto management console](https://help.zerto.com/bundle/Linux.ZVM.HTML.10.0_U1/page/ZVM_Linux_Management_Console.htm) as an administrator.
  3. Add the first tweak: 
     * **Tweak Name:** `t_VraInstallHostUserName`
     * **Type:** ZVM Tweak
     * **Tweak Value:** Enter the custom Zerto username you plan to create using the PowerCLI script, for example `zertouser`.
  4. Add the second tweak: 
     * **Tweak Name:** `t_automaticIsolatedNetworkCreator`
     * **Type:** ZVM Tweak
     * **Tweak Value:** Set value to `True`.
  5. Add vCenter to Zerto, and ensure VAIO Support is enabled.
  6. Contact Cloud Customer Care to add the necessary SSH exception on all hosts for the ZVM.
  7. Download the PowerCLI script (provided separately by Google) to a system that has PowerCLI installed and network access to the VMware Engine vCenter.
  8. Edit the script to replace the placeholder values for: 
     * vCenter IP/FQDN ($vCenterServer)
     * vCenter username ($vCenterUser)
     * New ESXi local username ($NewESXiUser)—Ensure this matches the `Tweak Value` from step 3.
     * New ESXi local user password ($NewESXiPassword)
  9. Run the script. If you encounter issues, validate network connectivity, DNS resolution, firewall rules, and credentials. If issues persist, contact Cloud Customer Care.
  10. Sign in to ZVM as an administrator.
  11. Go to the setup page in VRA.
  12. Click **Edit Cluster Default Settings**.
  13. Select the **Use Credentials to connect to host** option.
  14. Enter the Zerto user's password (the one used in the PowerCLI script) as the **Host root Password**.
  15. Verify the network details, and then click **Save**.
  16. Select the cluster, and then click **Install VRAs**.
  17. Complete the Zerto setup to protect your VMs.



## What's next

  * Read the [Zerto documentation](https://help.zerto.com/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
