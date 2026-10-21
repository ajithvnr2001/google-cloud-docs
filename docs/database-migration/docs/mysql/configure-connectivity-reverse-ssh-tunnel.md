---
url: https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-reverse-ssh-tunnel/
title: Configure connectivity using reverse SSH tunnel \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:15.334945+00:00
---

# Configure connectivity using reverse SSH tunnel  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/configure-connectivity-reverse-ssh-tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Configure connectivity using reverse SSH tunnel Stay organized with collections  Save and categorize content based on your preferences. 

You can establish connectivity from the destination database to the source database through a secure reverse SSH tunnel. This method requires a bastion host VM in the Google Cloud project as well as a machine (for example, a laptop on the network) that has connectivity to the source database.

**Important:** If your source is within a VPN (in AWS, for example, or your own on-premises VPN), your source connection profile should use the VPN IP address and port instead of the source IP address and port.

The Database Migration Service collects the required information at migration creation time, and auto-generates the script for setting it all up.

![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH server.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/mysql/mysql_hmm_reverse_ssh.svg) **Figure 1.** Migration networking example: source connectivity over an SSH tunnel. (click to enlarge) ![A networking diagram that shows a high-level connectivity
      setup over a dedicated SSH server.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/mysql/mysql_hmm_reverse_ssh.svg)

## Set up a reverse SSH tunnel

The following steps are performed in the Database Migration Service flow for [ creating a migration job](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job), to set up a reverse SSH tunnel between the source database and Cloud SQL instance. After you provide some parameters, you execute a set of `gcloud` commands on a machine which has connectivity to both the source database and to Google Cloud.

  1. Select the VM instance used to establish connectivity between the source database and the Cloud SQL instance. Typically this is a VM running in the VPC where the application accessing the new Cloud SQL database runs. The VM instance serves as the SSH tunnel bastion server.

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

     * Alter the `gcloud compute instances create` command by adding the [ `--no-address` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--address). 
     * Alter the `gcloud compute ssh` command by adding the [ `--internal-ip` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh#--internal-ip). 

Also, if you want to create a bastion host VM on a subnet which is on a shared VPC, then alter the `export SUBNET_NAME` command from the generated script to point to `/projects/project_name/regions/region_name/subnetworks/subnetwork_name`.

For example:

`export SUBNET_NAME=projects/myproject/regions/myregion/subnetworks/mysubnetwork`

project_name is the name of the project where the shared VPC is placed. A project has regions and subnetworks. region_name and subnetwork_name are the names of the region and subnetwork that are associated with the VPC project.

  5. **Run the script on a machine that has access to both the source database and the Compute Engine VM**. The script performs the following operations:

     * Configures the Compute Engine VM as an SSH tunnel bastion server.

     * Establishes a secure SSH connection between the source database and the VPC.

     * If you're creating a new Compute Engine VM, then after successfully running the script, copy the VM server IP from the script output and enter it in the provided text field. The Cloud SQL instance will be updated as needed when you later test or start the migration job.

  6. Click **CONFIGURE & CONTINUE**.

  7. [ Verify your migration job](https://docs.cloud.google.com/database-migration/docs/mysql/verify-migration) to confirm that it correctly migrated data from your source database instance to the destination Cloud SQL database instance.

  8. Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see the following pages [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) or [ Create HA VPN connections between Google Cloud and Azure](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-azure) in the Cloud VPN documentation.

  9. After your migration job is configured, connectivity is verified, and VPNs are configured successfully if necessary, then you can run the job.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
