---
url: https://docs.cloud.google.com/datastream/docs/configure-mongodb-atlas-vpc-peering/
title: Configure MongoDB Atlas using VPC peering \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:15.747388+00:00
---

# Configure MongoDB Atlas using VPC peering  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-mongodb-atlas-vpc-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure MongoDB Atlas using VPC peering Stay organized with collections  Save and categorize content based on your preferences. 

Virtual Private Cloud (VPC) peering lets you stream change data capture (CDC) updates from a MongoDB Atlas database to Datastream over a private network. Because VPC peering is non-transitive, you route traffic through a Compute Engine network address translation (NAT) virtual machine (VM) with firewall rules. You also create a MongoDB user, add the NAT VM IP address to your MongoDB Atlas allowlist, and create a connection profile. This configuration doesn't provide high availability. If a MongoDB node fails the connection profile test, you must manually run the startup script on the NAT VM.

## Configure a MongoDB database user

To use Datastream with a MongoDB Atlas instance, you first need to create a database user and grant them access privileges:

  1. In the [MongoDB Atlas dashboard](https://www.mongodb.com/products/platform/cloud), under **Security** , click **Database access**.
  2. Click **New database user** and select the password authentication method for your user.
  3. Enter the username and password for your Datastream user.
  4. Under **Database user privileges** , select **Grant specific user privileges**.
  5. Under **Specific privileges** , add the following role: 
     * `readAnyDatabase`
  6. Click **Add user**.



## Set up your Virtual Private Cloud network

Identify the Virtual Private Cloud network in your Google Cloud project to peer with both Datastream and MongoDB Atlas. This page assumes that you use the default VPC and its subnet, for example the default subnet in the `us-central1` region.

  1. Ensure that the network that you identified doesn't have overlapping IP address ranges with your Datastream or MongoDB Atlas networks.
  2. [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration) to peer Datastream with your Virtual Private Cloud network: 
     1. Make sure that you select **VPC peering** from the **Private connectivity method** drop-down.
     2. Select your `default` VPC network.
     3. Provide an unused IP address range, for example `10.0.0.0/29`, for Datastream to use.
     4. Take note of the allocated IP range for your ingress firewall rule.
  3. Set up a network peering connection in MongoDB Atlas to peer your Virtual Private Cloud network with your MongoDB Atlas network. For more information, see [Set up a network peering connection](https://www.mongodb.com/docs/atlas/security-vpc-peering/) in the MongoDB documentation: 
     1. Provide your Google Cloud project ID and your default VPC name in MongoDB Atlas.
     2. Note the project ID and VPC name that MongoDB Atlas provides you with to complete the peering on the Google Cloud side.
  4. After you create the connection, in your MongoDB Atlas project, go to the **Network Access** > **VPC Peering** tab and take note of the classless inter-domain routing (CIDR) block for your egress firewall rule.



## Create a NAT VM

  1. In the Google Cloud Console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. In the **Name** field, enter a name for the VM, for example `mongo-nat-gateway`.

  4. In the **Region** field, select a region inside your default VPC, for example `us-central1`.

  5. In the navigation menu, click **Networking**.

  6. In the **Network tags** field, add a tag, such as `mongo-nat-vm`. This tag is used by the firewall rules.

  7. Under **IP forwarding** , select the **Enable** checkbox.

  8. Under **Network interfaces** , select your default VPC and its subnet, for example `default` in `us-central1`.

  9. In the navigation menu, click **Advanced**.

  10. In the **Automation** section, paste the following script in the **Startup script** field. Replace PRIVATE_SRV_RECORD with your MongoDB Atlas cluster's private SRV record, for example `my-cluster-pri.abcde.mongodb.net`.
         
         #!/bin/bash
         
         # --- Startup script for MongoDB Atlas NAT gateway ---
         # This script has two main functions:
         # 1. Resolves the IP address of a MongoDB Atlas node from its SRV record.
         # 2. Configures iptables to forward traffic to the resolved MongoDB IP.
         # --------------------------------------------------------------------------
         
         # --- Part 1: Resolve MongoDB node IP address ---
         
         #
         # EDIT THIS LINE to match your Mongo Atlas private SRV record
         #
         export SRV_RECORD=PRIVATE_SRV_RECORD
         
         echo "Resolving SRV record for: $SRV_RECORD"
         
         # Function to install DNS utilities if needed
         install_dns_tools() {
             echo "'dig' not found. Attempting to install DNS utilities..."
             if command -v apt-get &> /dev/null; then
                 # Wait for any existing apt processes to finish before trying to install packages.
                 # This is common on VM startup where the system might be running automatic updates.
                 echo "Checking for and waiting on existing apt-get processes..."
                 while fuser /var/lib/apt/lists/lock /var/lib/dpkg/lock /var/lib/dpkg/lock-frontend >/dev/null 2>&1; do
                     echo "Another apt process is running. Waiting 10 seconds..."
                     sleep 10
                 done
                 echo "Apt lock is free. Proceeding with installation."
         
                 apt-get update && apt-get install -y dnsutils
             else
                 echo "Error: Could not find apt-get to install DNS utilities."
                 exit 1
             fi
         
             # Verify that dig is now available
             if ! command -v dig &> /dev/null; then
                 echo "Error: Failed to install DNS utilities."
                 exit 1
             fi
         }
         
         # Check if 'dig' is installed. If not, install it.
         if ! command -v dig &> /dev/null; then
             install_dns_tools
         fi
         
         echo "Using 'dig' for DNS resolution."
         # The `+short` option provides a concise output.
         # We use `awk` to grab the 4th column (the hostname) and `head` to get the first one.
         NODE_HOSTNAME=$(dig +short SRV "_mongodb._tcp.${SRV_RECORD}" | awk '{print $4}' | head -n 1)
         if [ -n "$NODE_HOSTNAME" ]; then
             NODE_IP=$(dig +short A "$NODE_HOSTNAME")
         fi
         
         # Check if the SRV lookup was successful and we got a hostname.
         if [ -z "$NODE_HOSTNAME" ]; then
             echo "Error: Could not resolve SRV record. Check the hostname and your
             network connection."
             exit 1
         fi
         
         echo "Found node hostname: $NODE_HOSTNAME"
         
         # Check if the A record lookup was successful.
         if [ -z "$NODE_IP" ]; then
             echo "Error: Could not resolve the IP address for node: $NODE_HOSTNAME"
             exit 1
         fi
         
         # 3. Print the final result of the lookup.
         echo "Successfully resolved IP address of a node: $NODE_IP"
         
         # --- Part 2: Configure iptables for NAT ---
         
         # Substitute the resolved IP address into the DB_ADDR variable.
         export DB_ADDR=$NODE_IP
         export DB_PORT=27017
         
         # Enable the VM to receive packets whose destinations do
         # not match any running process local to the VM
         echo 1 > /proc/sys/net/ipv4/ip_forward
         
         # Ask the Metadata server for the IP address of the VM nic0
         # network interface:
         md_url_prefix="http://169.254.169.254/computeMetadata/v1/instance"
         vm_nic_ip="$(curl -H "Metadata-Flavor: Google" ${md_url_prefix}/network-interfaces/0/ip)"
         
         # Clear any existing iptables NAT table entries (all chains):
         iptables -t nat -F
         
         # Create a NAT table entry in the prerouting chain, matching
         # any packets with destination database port, changing the destination
         # IP address of the packet to the MongoDB instance IP address:
         iptables -t nat -A PREROUTING \
              -p tcp --dport $DB_PORT \
              -j DNAT \
              --to-destination $DB_ADDR
         
         # Create a NAT table entry in the postrouting chain, matching
         # any packets with destination database port, changing the source IP
         # address of the packet to the NAT VM's primary internal IPv4 address:
         iptables -t nat -A POSTROUTING \
              -p tcp --dport $DB_PORT \
              -j SNAT \
              --to-source $vm_nic_ip
         
         # Save iptables configuration:
         iptables-save
         
         echo "Startup script completed successfully. iptables rules are configured and saved."

  11. Click **Create** to launch the VM.

  12. After the VM is running, note its internal IP address, for example `10.128.0.2`.




## Create ingress and egress firewall rules

You must create two firewall rules in your VPC network.

  1. Create an ingress [firewall rule](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules) with these characteristics:

     * **Name:** INGRESS_RULE_NAME
     * **Direction:** ingress
     * **Action:** allow
     * **Target parameter:** the `mongo-nat-vm` target tag
     * **Source parameter:** the IP address range used by the Datastream private connectivity configuration, for example `10.0.0.0/29`
     * **Protocol:** TCP
     * **Port:** `27017`
  2. Create an egress [firewall rule](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules) with these characteristics:

     * **Name:** EGRESS_RULE_NAME
     * **Direction:** egress
     * **Action:** allow
     * **Target parameter:** the `mongo-nat-vm` target tag
     * **Destination parameter:** the MongoDB Atlas CIDR block, for example `192.168.240.0/21`
     * **Protocol:** TCP
     * **Port:** `27017`



## Configure IP allowlists in MongoDB Atlas

Allow the internal IP address of the NAT VM in your MongoDB Atlas security settings:

  1. Sign in to your [MongoDB Atlas account](https://cloud.mongodb.com/).
  2. In the navigation menu, click **Security** , and then click **Network access**.
  3. Click **Add IP address**.
  4. In the **Access list entry** field, enter the internal IP address of the NAT VM instance that you created in your VPC network.
  5. Click **Confirm** and wait for the status to change to **Active**.



## Create the connection profile

Create a Datastream connection profile for your database.

  1. Go to the **Connection profiles** page in the Google Cloud Console.

[Go to the Connection profiles page](https://console.cloud.google.com/datastream/connection-profiles)

  2. Click **Create profile** and select **MongoDB**.

  3. In the **Hostname** field, enter the internal IP address of the NAT VM instance that you created in your VPC network.

  4. In the **Port** field, enter `27017`.

  5. Enter the username and password for your database user.

  6. Add the `tls` and `tls_allow_invalid_hostnames` labels and set their values to `true`. For more information about setting labels, see [Create a connection profile for a MongoDB database](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4mongodb).

  7. Select **Private connectivity** as your connectivity method.

  8. Select the private connectivity configuration you created.

  9. Click **Create** to save the connection profile.

  10. Run a test to verify connection to your database.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
