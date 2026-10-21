---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel/
title: Configure connectivity using reverse SSH tunnel \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:00.980670+00:00
---

# Configure connectivity using reverse SSH tunnel  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-reverse-ssh-tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Configure connectivity using reverse SSH tunnel Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-reverse-ssh-tunnel "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/configure-connectivity-reverse-ssh-tunnel "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


## Overview

You can establish connectivity from the destination AlloyDB database to the source database through a secure reverse SSH tunnel. This method requires a bastion host VM in the Google Cloud project as well as a machine (for example, a laptop on the network) that has connectivity to the source database. **Important:** If your source is within a VPN (in AWS, for example, or your own on-premises VPN), your source connection profile should use the VPN IP address and port instead of the source IP address and port.

The Database Migration Service for PostgreSQL to AlloyDB collects the required information at migration creation time, and auto-generates the script for setting it all up.

See the following diagram: ![Reverse SSH tunnel diagram](https://docs.cloud.google.com/static/database-migration/docs/images/alloydb-reverse-ssh.svg)

## Set up a reverse SSH tunnel

The following steps are performed in the Database Migration Service flow for [creating a migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job), to set up a reverse SSH tunnel between the source database and AlloyDB instance. After you provide some parameters, you execute a set of `gcloud` commands on a machine which has connectivity to both the source database and to Google Cloud.

  1. Select the VM instance used to establish connectivity between the source database and the AlloyDB instance. Typically this is a VM running in the VPC where the application accessing the new AlloyDB database runs. The VM instance serves as the SSH tunnel bastion server.
  2. You can use an existing Compute Engine VM instance for this purpose.

     1. Choose the Compute Engine VM instance from the list.

     2. Provide a free port that the SSH tunnel can use.

Note: For the reverse SSH tunnel to work, set the `GatewayPorts` parameter to `yes` in the `/etc/ssh/sshd_config` file on the target server. After you update the file, restart the sshd service using the `sudo systemctl restart sshd.service` command.  
  
If you don't want to change the configuration of your existing VM, then create a new VM.
  3. Alternatively, you can create a new VM at this step. Select `CREATE A COMPUTE ENGINE VM INSTANCE` and the generated script includes instructions to create it.

     1. Provide a name for the VM instance.

     2. Select a machine type for the VM.

     3. Specify a subnet for the VM

Note: A Compute Engine VM instance created by the script isn't managed by Database Migration Service. If one is created, then your organization is charged for the instance based on standard pricing, and is responsible for its management, including deleting the instance when it's no longer needed.
  4. Click **VIEW SCRIPT** to view the generated script.

By default, the script will generate a public IP address for the Compute Engine VM server. If you want the IP address to be private, then do the following:

     * Alter the `gcloud compute instances create` command by adding the [\--no-address](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create#--address) flag.
     * Alter the `gcloud compute ssh` command by adding the [\--internal-ip](https://cloud.google.com/sdk/gcloud/reference/compute/ssh#--internal-ip) flag.

Also, if you want to create a bastion host VM on a subnet which is on a shared VPC, then alter the `export SUBNET_NAME` command from the generated script to point to `/projects/project_name/regions/region_name/subnetworks/subnetwork_name`.

For example:

`export SUBNET_NAME=projects/myproject/regions/myregion/subnetworks/mysubnetwork`

project_name is the name of the project where the shared VPC is placed. A project has regions and subnetworks. region_name and subnetwork_name are the names of the region and subnetwork that are associated with the VPC project.

**Make sure the replication connections section of the`pg_hba.conf` file or the AWS RDS security groups definitions on the source database are updated to accept connections from the AlloyDB VPC's IP address range.**

  5. **Run the script on a machine that has access to both the source database and the Compute Engine VM**. The script performs the following operations:

     * Configures the Compute Engine VM as an SSH tunnel bastion server.

     * Establishes a secure SSH connection between the source database and the VPC.

     * If you're creating a new Compute Engine VM, then after successfully running the script, copy the VM server IP from the script output and enter it in the provided text field. The AlloyDB instance will be updated as needed when you later test or start the migration job.

  6. Click **CONFIGURE & CONTINUE**.

  7. [Verify your migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/verify-migration) to confirm that it correctly migrated data from your source database instance to the destination AlloyDB database instance.

  8. If your source is within a VPN (in AWS, for example, or your own on-premises VPN), proceed to the section on [ connecting VPCs through VPNs](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/configure-connectivity-vpns#vpc-vpn) for more information on configuring the source VPN and Google Cloud VPN to work with each other.

  9. After your migration job is configured, connectivity is verified, and VPNs are configured successfully if necessary, then you can run the job.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


