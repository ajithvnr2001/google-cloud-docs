---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-jetstream/
title: Configure disaster recovery using JetStream \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:41.530473+00:00
---

# Configure disaster recovery using JetStream  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-jetstream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure disaster recovery using JetStream

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to deploy and configure a JetStream disaster recovery (DR) solution on Google Cloud VMware Engine. This DR solution provides the following benefits:

  * You can ensure business continuity in the event of a disaster by setting up a Google Cloud VMware Engine private cloud as a recovery site for your on-premises applications.
  * You can protect workloads that are already running on VMware Engine private clouds. You can do this by setting up a private cloud as a primary site that is protected by a recovery site at a different Google Cloud location, or in your on-premises VMware environment.
  * You can eliminate the need for a secondary physical data center, which reduces your total cost of ownership (TCO).
  * You can provide global geographic resilience by leveraging Google Cloud's worldwide locations where VMware Engine is deployed.



To use this guide, you need the following:

  * JetStream version 5.0.8 or newer.
  * VMware Engine private clouds that run vSphere 8.0.



You must install, configure, and manage the JetStream solution in your private cloud, and provide your own licenses for the JetStream solution. You must also create and configure your VMware Engine private clouds, and provide your own VCF licenses for the VMware Engine nodes.

This DR solution continuously replicates critical infrastructure and application virtual machines (VMs) from your on-premises VMware environments. Replicated VMs are stored in your private cloud and in Cloud Storage, which provides multiple disaster recovery options.

**Note:** For information about sizing your disaster recovery environment, see the [Overview Sizing and Best Practice](https://jetstreamsoft.com/portal/jetstream-knowledge-base/jetstream-dr-automation-toolkit/) article.

## Before you begin

Before you can use JetStream Virtual Replication from your on-premises environment to your private cloud, complete the following prerequisites:

  1. [Connect your on-premises network to your VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises).
  2. [Configure DNS for management access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises) to forward requests from your on-premises network to your private Cloud DNS servers. To enable forwarding of DNS lookup, create a forwarding zone entry in your on-premises DNS server for `gve.goog` to private Cloud DNS servers.
  3. Set up DNS lookup for on-premises vCenter components to be forwarded to your on-premises DNS servers. The DNS servers must be reachable from your private cloud.
  4. Configure DNS for the JetStream network.
  5. Create a DNS A record for the JetStream Management Server Appliance (MSA).
  6. Create a Service Subnet (or NSX Segment) for the JetStream deployment. See [Create subnets](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-vlan-subnet).
  7. Ensure that the VMware Engine infrastructure, the JetStream MSA, and your workstation can resolve the FQDNs for VMware Engine (`gve.goog`) and the JetStream MSA appliance (your domain).
  8. [Configure internet access](https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access) for VMs on VMware Engine.
  9. [Configure DHCP](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-dhcp-dns) for the JetStream network (static IP is also supported).
  10. Configure Cloud Storage service accounts by using keyed-hash message authentication codes ([HMAC](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys)). See [Interoperability with other storage providers](https://docs.cloud.google.com/storage/docs/interoperability) and [Migrate from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/storage/docs/aws-simple-migration).
  11. Decide on the Cloud Storage bucket region you plan to use for your solution. Note that only regional buckets are supported during preview.
  12. Identify a VMware Engine [solution user account](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege) to use with the MSA, and set a strong password for the solution user account.



### Optional configuration on your private cloud

  1. Create one or more resource pools on your private cloud vCenter to use as target resource pools for VMs from your on-premises environment.
  2. Create one or more folders on your private cloud vCenter to use as target folders for VMs from your on-premises environment.
  3. [Create subnets](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-vlan-subnet) on your private cloud for your failover network and set up required firewall rules.



## Deploy JetStream disaster recovery

To deploy the JetStream solution in your on-premises environment and on your private cloud, follow the [JetStream documentation](https://jetstreamsoft.com/portal/online-docs/jsdr-admin/ObtaintheSoftware.html). The private cloud can be a protected site or a recovery site of your JetStream solution.

To deploy and configure JetStream on Google Cloud, complete the following tasks:

  * Deploy JetStream DR on VMware Engine
  * Configure the JetStream service account
  * Set the Cloud Storage region
  * Configure a storage site
  * Configure VM protection



### Deploy JetStream DR on VMware Engine

  1. [Download the JetStream MSA OVA ZIP archive](https://jsmms.blob.core.windows.net/jsdrmms/JSDR-GA-OVA-5.0.0.zip).
  2. Deploy the JetStream Management Server Appliance. Note: Set the password for the `admin` user during OVA deployment. See [Deploy MSA](https://jetstreamsoft.com/portal/jetstream-knowledge-base/installing-jetstream-dr-software/#deploy-msa).
  3. Install the vCenter plugin. Note: Use the elevated privilege solution user as the service account for installing the vCenter Plugin. See [solution user accounts](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege) and [Install plugin](https://jetstreamsoft.com/portal/jetstream-knowledge-base/installing-jetstream-dr-software/#install-plugin).



### Configure the JetStream service account

To configure the JetStream service account, complete the following steps:

  1. Sign in to the MSA appliance as `admin` by using the VM console or SSH.

**Note:** Use the elevated privilege solution user (as a service account) for the vCenter user and password. Use the `admin` account that was created during the MSA deployment. For more information, see [solution user accounts](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege).

Run the `manage_iofrest_user.ps1` script from the MSA:
         
         cd /opt/fio/vme2/python/
         pwsh ./manage_iofrest_user.ps1
         

Example execution:
         
         [admin@jetdr-msa-508-101 ~]$ cd /opt/fio/vme2/python/
         [admin@jetdr-msa-508-101 python]$ pwsh ./manage_iofrest_user.ps1
         SUCCESS: Check for powershell version passed
         SUCCESS: Check for module VMware.vSphere.SsoAdmin passed
         SUCCESS: Check for module VMware.VimAutomation.Core passed
         Enter vCenter IP or FQDN: <gcve-vcenter/IP-address>
         Enter vCenter user name: <solution-user-0x@gve.local>
         Enter vCenter password: *****************
         Enter MSA IP or FQDN: <msa/IP-address>
         Enter MSA user name: admin
         Enter MSA password: *********
         Disconnecting any connected viservers and ssoadmin servers from the powershell
         session
         
         vCenter version is 8.0.3, proceeding with user configuration.
         ### update_rest_user_on_msa ###
         Updating credentials of jetstream iofrest user on MSA
         https://<msa/IP-address>/jss/ms/login
         ### get_request ###
         Successfully obtained MSA session id
         ### get_rest_user ###
         Fetching credentials of jetstream iofrest user
         https://<msa/IP-address>/jss/ms/login
         ### get_request ###
         Successfully obtained MSA session id
         ### get_request ###
         Couldn't get iofrest user details from MSA <msa/IP-address>
         User details not present on MSA.
         ### create_rest_user ###
         Creating jetstream iofrest user
         Role Partner REST Read+Write already exists on the vCenter. Checking if it has
         required privileges.
         Role Partner REST Read+Write has required privileges. Continuing.
         User jetstream already exists in the vCenter.
         Password for jetstream@gve.local successfully refreshed.
         ### get_current_msa_version ###
         Current MSA plugin version is 5.0.8.665
         ### get_rest_user ###
         Fetching credentials of jetstream iofrest user
         https://<msa/IP-address>/jss/ms/login
         ### get_request ###
         Successfully obtained MSA session id
         ### get_request ###
         iofrest user successfully updated on MSA
         [admin@jetdr-msa-508-101 python]$
         

  2. Perform the IO Filter Package Installation.

**Note:** Sign in to vCenter with a solution user account for elevated privileges. See [IO Filter Package Installation](https://jetstreamsoft.com/portal/jetstream-knowledge-base/io-filter-package-installation/).



### Set the Cloud Storage region

To set the Cloud Storage region, complete the following steps:

  1. Sign in to the MSA appliance as `admin` by using the VM console or SSH.

Edit the server configuration by replacing `<cloud-storage-region>` with your specific Cloud Storage region (for example, `us-central1`):
         
         sudo echo "jss.dr.rs.cloudian.region=<cloud-storage-region>" | \
         sudo tee -a /var/lib/vme2/conf/server.properties
         

  2. Restart the MSA service:
         
         sudo systemctl restart msa-tomcat
         

You see a configured `server.properties` file that resembles the following:
         
         cat /var/lib/vme2/conf/server.properties
         # Properties file for the VME2 server configuration
         jss.dr.rs.cloudian.region=<cloud-storage-region>
         




### Configure a storage site

To configure a storage site, complete the following steps:

  1. Sign in to vCenter with the vSphere web client and navigate to the data center level.
  2. Click the **Configure** tab, and then select **JetStream DR**.
  3. In the JetStream UI, click the **Storage Sites** tab.
  4. Click **\+ Add Storage Site**.
  5. In the **Add Storage Site** window, enter the following settings for the S3 storage: 
     * **Storage site type** : Region-based S3.
     * **Storage site name** : A name for identification in the JetStream client.
     * **S3 storage endpoint** : `storage.googleapis.com`
     * **Access key** : The Cloud Storage HMAC access key.
     * **Secret key** : The Cloud Storage HMAC secret key.



### Configure VM protection

To configure VM protection, complete the following steps:

  1. [Deploy the Disaster Recovery Virtual Appliance (DRVA)](https://jetstreamsoft.com/portal/online-docs/jsdr-admin_5.0.4/deploydrva.html).
  2. [Create a Replication Log Volume](https://jetstreamsoft.com/portal/online-docs/jsdr-admin_5.0.4/replicationlogvolume.html).
  3. [Create a Protected Domain](https://jetstreamsoft.com/portal/online-docs/jsdr-admin_5.0.4/createprotecteddomain.html).
  4. [Select VMs for Protection](https://jetstreamsoft.com/portal/online-docs/jsdr-admin_5.0.4/selectprotectionvms.html).



## What's next

  * Read the [JetStream documentation](https://jetstreamsoft.com/portal/online-docs/jsdr-admin/WhatisJetStreamDR.html) for details on Day 2 management of JetStream.
  * Learn about [high availability for VMware virtual machines](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
