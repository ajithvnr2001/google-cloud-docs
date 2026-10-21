---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-src-connection-aws-rds-sqlserver/
title: Configure network connectivity to Amazon RDS for SQL Server sources \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:10.884001+00:00
---

# Configure network connectivity to Amazon RDS for SQL Server sources  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-src-connection-aws-rds-sqlserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Configure network connectivity to Amazon RDS for SQL Server sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure network connectivity to Amazon RDS for SQL Server sources for heterogeneous SQL Server to AlloyDB for PostgreSQL migrations with Database Migration Service.

There are several methods you can use to configure the necessary network connectivity for migrations from Amazon RDS for SQL Server sources:

  * Public IP allowlist
  * Forward-SSH tunnel
  * Private IP connectivity. These methods require Cloud VPN or Cloud Interconnect: 
    * Recommended:  Private IP connectivity with Private Service Connect interfaces
    * Private IP connectivity with Virtual Private Cloud peering



To learn more about source database network connectivity, see [ Source networking methods overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/networking-methods-source).

## Configure IP allowlist connectivity

To use the public IP allowlist connectivity method, follow these steps:

  1. In the AWS Management Console, perform the following steps: 
     1. Ensure that your source Amazon RDS database is configured for public IP connections. 
     2. Identify the endpoint name and port number. You need to enter these values when you create the connection profile. 

For more information about preparing your Amazon RDS for SQL Server instance, see [ Connecting to a DB instance running the Microsoft SQL Server database engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.html) in the Amazon RDS documentation. 

  2. Create a security group that allows traffic from Database Migration Service to your Amazon RDS VPC. See [ Provide access to your DB instance in your VPC by creating a security group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html#CHAP_SettingUp.SecurityGroup). 

Make sure you allow all [ Database Migration Service public IP addresses](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/ip-allowlists-and-regions) for the region where you create the migration job. 

  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. In the **Define connection details** section, use your instance's endpoint name for the source database IP. 
     2. In the **Define connectivity method** section, select **IP allowlist**. 



## Configure connectivity over a forward-SSH tunnel

To connect to your source database with a Secure Shell (SSH) tunnel, follow these steps:

  1. Launch an Amazon EC2 instance to serve as a dedicated forward-SSH tunnel. Make sure you configure it in the same Amazon VPC where you have your source Amazon RDS for SQL Server. 

For more information, see [ Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) in the Amazon documentation. 

  2. [ Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-connect-to-instance) and set up the SSH tunnel. Follow these steps: 
     1. Create a separate, dedicated user account for Database Migration Service to connect as: 
            
            adduser TUNNEL_ACCOUNT_USERNAME

     2. Restrict shell access for the Database Migration Service account to enhance security: 
            
            usermod -s /usr/sbin/nologin TUNNEL_ACCOUNT_USERNAME

     3. Decide what authentication method you want Database Migration Service to use when connecting to the tunnel.

You can use a simple password, or generate SSH keys in the `PEM` format that you can later upload to Database Migration Service when you create the source connection profile. 

        * If you want to use a password, you don't need to configure anything additional. Remember what password you created for the TUNNEL_ACCOUNT_USERNAME account. 
        * If you want to use key-based authentication, you need to generate a private-public key pair. For example, you can use the `ssh-keygen` utility: 
          1. Generate the key pair: 
                 
                 ssh-keygen -m PEM -f YOUR_KEY_NAME
                     

          2. Copy the public key (`YOUR_KEY_NAME.pub`) to the `~/.ssh/` directory on your tunnel server. 
          3. Save the private key. You need to upload it later to Database Migration Service when you create the source connection profile. 
     4. Edit the `/etc/ssh/sshd_config` file to configure the forward-SSH tunnel to match your organization's requirements. We recommend using the following settings: 
            
            # Only allow the Database Migration Service user to connect.
            AllowUsers TUNNEL_ACCOUNT_USERNAME
            
            # Send keep-alive packets every 60 seconds to ensure that
            # the tunnel doesn't close during the migration
            ServerAliveInterval=60
            
            # Optional: Force key-based authentication
            PasswordAuthentication no
            
            # Enables Database Migration Service to connect from a different host
            PermitTunnel yes
            GatewayPorts yes

     5. Run the `ssh` command to start the tunnel. 

Before using any of the command data below, make the following replacements:

        * TUNNEL_SERVER_SSH_PORT with the port number where your server is listening for SSH connections. 
        * SOURCE_DATABASE_PRIVATE_IP with the private IP address of your source database. The SSH server needs to be able to reach that IP. 
        * SOURCE_DATABASE_PORT with the port number where your source database is listening for connections. The default port number for TCP connections on SQL Server is `1433`. 
        * USERNAME with the name of the user account that will be running the tunnel. This is a separate account from TUNNEL_ACCOUNT_USERNAME. 
        * TUNNEL_SERVER_PUBLIC_IP with the public IP of your SSH tunnel server. 
    
    ssh -N -L \
    TUNNEL_SERVER_SSH_PORT:SOURCE_DATABASE_PRIVATE_IP:SOURCE_DATABASE_PORT \
    USERNAME@TUNNEL_SERVER_PUBLIC_IP

  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. In the **Define connection details** section, use your instance's endpoint name for the source database IP. 
     2. In the **Define connectivity method** section, select **Forward-SSH tunnel**. 
     3. Provide the public IP address or hostname of your SSH server.
     4. Provide the port that you designated for the SSH connections on the tunnel server. 
     5. Enter the username for the user you created for Database Migration Service to connect as (that is, the value of TUNNEL_ACCOUNT_USERNAME). 
     6. From the **Authentication method** drop-down menu, select the authentication method you want to use with TUNNEL_ACCOUNT_USERNAME: 
        * If you want to use the user password, select **Password** and enter TUNNEL_ACCOUNT_USERNAME password in the form. 
        * If you configured your SSH server to use key-based authentication, select **Private/Public key pair** and upload the **private key** you generated in with the `ssh-keygen` command. 



## Configure private connectivity with Private Service Connect interfaces

This connectivity method lets you connect to the private IP of your source database without consuming [ VPC peering quota](https://docs.cloud.google.com/vpc/docs/vpc-peering#peering-limits). Private Service Connect interfaces are the recommended method for private IP connectivity.

To use this method, you need to have a Cloud VPN or Cloud Interconnect configured in the same VPC network where you intend to create the network attachment. If you can't create the network attachment in the VPC network where you have your Cloud VPN or Cloud Interconnect, then you also need a reverse proxy Virtual Machine (VM) on Compute Engine to establish the connection.

If you can't use Cloud VPN or Cloud Interconnect, we recommend that you use the  forward-SSH tunnel or the IP allowlist connectivity methods instead.

To get the permissions that you need to configure Private Service Connect interfaces ask your administrator to grant the required IAM roles on your project for the following [ accounts involved in the migration process](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/access-control)

  * User account that performs the migration: 
    * To create and manage network attachments: [ Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 
    * To create and manage private connectivity configurations: [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * If you need to create a network attachment or its underlying subnetwork in a different project than Database Migration Service (for example, if you use a Shared VPC host project), then you need to grant the following role to the **Database Migration Service service account** (`service-PROJECT_NUMBER@gcp-sa-datamigration.iam.gserviceaccount.com`): [ Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) 




For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to perform homogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous SQL Server migrations with Database Migration Service: 

  * User account that performs the migration: 
    * `datamigration.*`
    * `compute.networkAttachments.create`
    * `compute.networkAttachments.get`
    * `compute.networkAttachments.list`
    * `compute.networkAttachments.update`
    * `compute.networkAttachments.delete`
  * Database Migration Service service account: 
    * `compute.networkAttachments.get`
    * `compute.networkAttachments.update`
    * `compute.subnetworks.get`
    * `compute.subnetworks.list`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

To use Private Service Connect interface connectivity, do the following:

  1. Set up direct connectivity with Cloud VPN to your Amazon RDS for PostgreSQL instance. 

For more information, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) in the Cloud VPN documentation. 

  2. Optional: If you can't create the network attachment in the same VPC network where you have the Cloud VPN, create [ a reverse proxy Virtual Machine (VM) on Compute Engine](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-src-connection-reverse-proxy) to forward the connections between VPCs. 
  3. Create a network attachment in the VPC where you have your Cloud VPN. Follow these steps: 
     1. In the Google Cloud console, go to the **Network attachments** page. 

[ Go to Network attachments](https://console.cloud.google.com/net-services/psc/list/networkAttachments)

     2. Click **Create network attachment**.
     3. Enter a name for the attachment.
     4. From the **Network** menu, select the VPC where your source resides.
     5. For the region, use the same region where you plan to create the destination database. 

Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 

     6. From the **Subnetwork** menu, select a subnet where you have at least 6 free usable IP addresses for Database Migration Service (that is, a `/29` range). 
     7. In **Connection preference** select **Accept connections for selected projects**. 

Database Migration Service automatically adds the producer project to the **Accepted projects** list when you later [ create the private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-private-connectivity-configuration#create-psci-config). 

**Caution:** The **Automatically accept connections for all projects** option is less secure because it allows any service to obtain IP addresses from your subnet. We don't recommend using this option. 
     8. Don't add **Accepted projects** or **Rejected projects**.
     9. Click **Create network attachment**.
  4. In Database Migration Service, [ create a private connectivity configuration for Private Service Connect interfaces](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-private-connectivity-configuration#create-psci-config). 
  5. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. In the **Define connection details** section, enter the private IP of your source Amazon RDS instance. 
     2. In the **Define connectivity method** section, select **Private connectivity**. 
     3. From the drop-down menu, select the private connectivity configuration you created in the previous step. 



## Configure private connectivity with VPC peering

To use private connectivity with Amazon RDS for SQL Server sources, you need to have a Cloud VPN or Cloud Interconnect configured in the same VPC network where you intend to create the private connectivity configuration for Database Migration Service. If you can't create the private connectivity configuration in the VPC network where you have your Cloud VPN or Cloud Interconnect, then you also need a reverse proxy Virtual Machine (VM) on Compute Engine to establish the connection.

If you can't use Cloud VPN or Cloud Interconnect, we recommend that you use the  forward-SSH tunnel or the IP allowlist connectivity methods instead.

To use private connectivity with VPC peering and Cloud VPN, follow these steps:

  1. Set up direct connectivity with Cloud VPN to your Amazon RDS for PostgreSQL instance. 

For more information, see [ Create HA VPN connections between Google Cloud and AWS](https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws) in the Cloud VPN documentation. 

  2. Optional: If you can't create the private connectivity configuration in the same VPC network where you have the Cloud VPN, create [ a reverse proxy Virtual Machine (VM) on Compute Engine](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-src-connection-reverse-proxy) to forward the connections between VPCs. 
  3. In Database Migration Service, [ create a private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-private-connectivity-configuration) to peer with the VPC network where you have your Cloud VPN. 
  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-source-connection-profile), do the following: 
     1. In the **Define connection details** section, enter the private IP of your source Amazon RDS instance. 
     2. In the **Define connectivity method** section, select **Private connectivity**. 
     3. From the drop-down menu, select the private connectivity configuration you created in the previous step. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
