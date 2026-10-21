---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-managed-clouds/
title: Configure network connectivity to managed Oracle sources \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:04.498943+00:00
---

# Configure network connectivity to managed Oracle sources  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-managed-clouds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)



Send feedback 

#  Configure network connectivity to managed Oracle sources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure network connectivity to cloud-managed Oracle database offerings for heterogeneous Oracle to Cloud SQL for PostgreSQL migrations with Database Migration Service.

Oracle databases are available as a managed service from many different cloud providers. Database Migration Service doesn't offer targeted support for any specific cloud providers [ (except for Amazon RDS for Oracle sources)](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-aws-rds-oracle), but you can migrate from any managed Oracle database service as long as you can establish the necessary network connectivity.

There are three different methods you can use for managed Oracle database services:

  * Public IP allowlist
  * Forward-SSH tunnel
  * Requires Cloud VPN or Cloud Interconnect:  Private IP connectivity with Virtual Private Cloud peering



To learn more about source database network connectivity, see [ Source networking methods overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/networking-methods-source).

## Configure IP allowlist connectivity

To use the public IP allowlist connectivity method, follow these steps:

  1. Ensure that your source database has an IP address that can be reached from the public internet. You don't need to use the IP address to connect. If you have a DNS record associated with the IP, you can use that instead. 
  2. Create an inbound firewall rule on your source database server to accept connections from Database Migration Service. Use the following configuration: 
     1. For the rule type, use `port`.
     2. For the allowed IP address range, add all [ Database Migration Service public IP addresses](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/ip-allowlists-and-regions) for the region where you create the migration job. 
     3. Set the protocol to `TCP`.
     4. Set the port number associated with the rule to the port where your source database is listening for incoming connections. This is the same port number that you need to enter in the source connection profile. 

Oracle server by default use the `1521` port. 

The steps for configuring firewall rules differ depending on what server software you use. For more information, refer to the documentation of your firewall product. 

  3. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-source-connection-profile), in the **Define connectivity method** section, select **IP allowlist**. 



## Configure connectivity over a forward-SSH tunnel

To connect to your source database with a Secure Shell (SSH) tunnel, follow these steps:

  1. Create a Virtual Machine (VM) that can open the tunnel between Database Migration Service and your source database. The tunnel server can be any Unix/Linux host that: 
     * Can be accessed from the public internet over SSH.
     * Can access the private IP address of your source database.
  2. On the SSH server, create a user account that Database Migration Service can use to connect to to the SSH tunnel. 

For example, on an Ubuntu system, you can use the following commands:

     1. Create a user account: 
            
            adduser TUNNEL_ACCOUNT_USERNAME

     2. Restrict shell access for the user account to enhance security: 
            
            usermod -s /usr/sbin/nologin TUNNEL_ACCOUNT_USERNAME

  3. Decide what authentication method you want Database Migration Service to use when connecting to the tunnel.

You can use a password, or generate SSH keys in the `PEM` format that you can later upload to Database Migration Service when you create the source connection profile. 

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
     * SOURCE_DATABASE_PORT with the port number where your source database is listening for connections. The default port number for TCP connections on Oracle is `1433`. 
     * USERNAME with the name of the user account that will be running the tunnel. This is a separate account from TUNNEL_ACCOUNT_USERNAME. 
     * TUNNEL_SERVER_PUBLIC_IP with the public IP of your SSH tunnel server. 
    
    ssh -N -L \
    TUNNEL_SERVER_SSH_PORT:SOURCE_DATABASE_PRIVATE_IP:SOURCE_DATABASE_PORT \
    USERNAME@TUNNEL_SERVER_PUBLIC_IP

  6. Create an inbound firewall rule on your SSH tunnel to accept connections from [ Database Migration Service public IP addresses](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/ip-allowlists-and-regions) for the region where you create the migration job. 
  7. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-source-connection-profile), do the following: 
     1. In the **Define connection details** section, enter the private IP of your source Oracle instance. 
     2. In the **Define connectivity method** section, select **Forward-SSH tunnel**. 
     3. Provide the public IP address or hostname of your SSH server.
     4. Provide the port that you designated for the SSH connections on the tunnel server. 
     5. Enter the username for the user you created for Database Migration Service to connect as (that is, the value of TUNNEL_ACCOUNT_USERNAME). 
     6. From the **Authentication method** drop-down menu, select the authentication method you want to use with the TUNNEL_ACCOUNT_USERNAME user: 
        * If you want to use the user password, select **Password** and enter TUNNEL_ACCOUNT_USERNAME password in the form. 
        * If you configured your SSH server to use key-based authentication, select **Private/Public key pair** and upload the **private key** you generated in with the `ssh-keygen` command. 



## Configure private connectivity with VPC peering

To use private connectivity with cloud-managed Oracle sources, you need to have a Cloud VPN or Cloud Interconnect configured in the same VPC network where you intend to create the private connectivity configuration for Database Migration Service. If you can't create the private connectivity configuration in the VPC network where you have your Cloud VPN or Cloud Interconnect, then you also need a reverse proxy Virtual Machine (VM) on Compute Engine to establish the connection.

If you can't use Cloud VPN or Cloud Interconnect, we recommend that you use the  forward-SSH tunnel or the IP allowlist connectivity methods instead.

To use private connectivity with VPC peering and Cloud VPN, follow these steps:

  1. Set up direct connectivity with Cloud VPN to your Oracle source. 

Depending on your network architecture, you might need to set up additional VPN gateways in your system. For more information, see [ Create HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) in the Cloud VPN documentation. 

  2. Optional: If you can't create the private connectivity configuration in the same VPC network where you have the Cloud VPN, create [ a reverse proxy Virtual Machine (VM) on Compute Engine](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-src-connection-reverse-proxy) to forward the connections between VPCs. 
  3. In Database Migration Service, [ create a private connectivity configuration](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-private-connectivity-configuration) to peer with the VPC network where you have your Cloud VPN. 
  4. At a later stage, when you [ create the source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/create-source-connection-profile), do the following: 
     1. In the **Define connection details** section, enter the private IP of your Oracle source. 
     2. In the **Define connectivity method** section, select **Private connectivity (VPC peering)**. 
     3. From the drop-down menu, select the private connectivity configuration you created in the previous step. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
