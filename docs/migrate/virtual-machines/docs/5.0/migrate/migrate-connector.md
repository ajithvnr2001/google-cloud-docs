---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector/
title: Install the Migrate Connector \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:07.362885+00:00
---

# Install the Migrate Connector  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Install the Migrate Connector Stay organized with collections  Save and categorize content based on your preferences. 

To migrate VMs from an on-premises data center, you must first configure a _migration source_ that specifies the data center from which you want to migrate your VMs. To configure a migration source, install and configure the **Migrate Connector** on your vSphere data center. **Note:** The **Migrate Connector** does not support vCenter linked mode. That means you must install the Migrate Connector separately on each vCenter.

Once installed, the Migrate Connector:

  * Establishes a secure datapath between the on-premises environment and the Google Cloud using Google Cloud APIs over port 443. Migration traffic can be routed over public internet, VPN, [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options), or [Dedicated interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview).

  * Performs storage operations against VM disks using the vSphere APIs.

  * Queries on-premises VM inventory so that you can use the [Google Cloud console](https://console.cloud.google.com/) to browse the VMs on the data center available for migration.

  * Stops and monitors source VMs using vSphere APIs when performing cut-over.




See [Migrate to Virtual Machines Architecture](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture) for more on the Migrate Connector.

## Before you begin

Before you install and register the Migrate Connector, do the following:

  * Enable Migrate to Virtual Machines on Google Cloud. See [Enabling Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services).
  * Verify the vSphere version is [supported](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-vmware-source#VMware-versions).
  * Create the SSH public/private key pair.
  * Ensure the following Migrate Connector hardware requirements are met: 
    * 4 CPUs with Instruction Set Architecture (ISA) compatibility to Sandy Bridge CPU or higher
    * 16 GB of RAM
    * 30 GB of datastore space
  * Review [Create a VMware source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-vmware-source) documentation.



### Create the SSH public/private key pair

Create an SSH public/private key pair used to connect your workstation to the Migrate Connector VM running on vSphere or on VMware Engine. You then copy the public key to the Migrate Connector VM as part of the registration procedure. The Migrate Connector uses the public key when authenticating any remote SSH connections.

The following examples show how to use `ssh-keygen` and PuTTY to generate SSH keys, but there are many ways to generate a public/private SSH key pair, depending on the workstation and OS. We recommend that you always use the latest version of the tool that you use to generate SSH keys.

To generate SSH keys using `ssh-keygen` on Linux, follow these steps:

  1. Sign in to your workstation, meaning the remote machine that you use to connect to the vSphere or VMware Engine data center.

  2. Change directory to `~/.ssh`.

If this directory does not exist, create it.

**Note:** Some key generation utilities will create this directory for you.
  3. Use the following example generates a public key (`~/.ssh/id_rsa.pub`) and a private key (`~/.ssh/id_rsa`) with a single command:
         
         ssh-keygen -t rsa

This command creates a public key named `id_rsa.pub` that you pass to the Migrate Connector during registration. The actual name of your public key depends on the utility that you use to create the key.




To generate SSH keys using PuTTY on Windows, follow these steps:

  1. [Download and install PuTTY](https://www.chiark.greenend.org.uk/%7Esgtatham/putty/latest.html).

  2. Start `puttykeygen.exe`.

  3. Under **Parameters** , select **RSA**.

  4. Select **Generate** to create the keys.

You see the public key displayed in PuTTy, in the form `ssh-rsa AAAAB3NzaC1yc2EAAAADAQA...`. Copy the public key for use later in this procedure.

  5. Select **Save public key** and **Save private key** to save the keys.




You can now install the Migrate Connector.

## Install the Migrate Connector

You can install the Migrate Connector Open Virtualization Format (OVA) by using the vSphere user interface (UI) or the VMware OVF Tool (ovftool) command-line interface (CLI).

**Note:** Your on-premises hosts might also use Private Google Access. With Private Google Access, your on-premises hosts connect to Google Cloud APIs through a Cloud VPN tunnel or Cloud Interconnect. To configure the domain name server (DNS) on your on-premises hosts for private access, set [Google API Address](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector#vsphere-ui) as **Private** or **Restricted**. For more information on configuring Private Google Access for your on-premises hosts, see [Private Google Access-specific domains and VIPs](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid).

###  vSphere UI 

To install the Migrate Connector OVA using the vSphere UI, follow these steps:

  1. Download the [Migrate Connector OVA file](https://storage.googleapis.com/vmmigration-public-artifacts/migrate-connector-2-8-2977.ova) to VCenter ([checksum](https://storage.googleapis.com/vmmigration-public-artifacts/migrate-connector-2-8-2977.sha256)).

  2. Sign in to vSphere using an account with the permissions required to deploy an OVF file.

  3. Right-click on your data center and select **Deploy OVF Template**.

  4. Select the Migrate Connector OVA file, and then select **Next**.

  5. Choose the virtual machine name and folder for the connector, or use the default name, and then select **Next**.

  6. Select the compute resource, and then select **Next**.

  7. Review the installation details, and then select **Next**.

  8. Select the datastore used by the connector, and then select **Next**.

  9. Select the network that you want to host the connector on, and then select **Next**.

  10. Customize the template:

     1. Provide the SSH public key that you created on your workstation machine.

This is the key you created in Create the SSH public or private key pair. In that example, the SSH public key was written to a file named `~/.ssh/id_rsa.pub`. Provide the contents of the file here. For example `ssh-rsa AAAAB3NzaC1yc2EAAAADAQA...`.

     2. Set the **hostname** of the machine or accept the default.

     3. Optionally, set any properties under **Networking Properties**. If you don't set these properties, then the VM uses DHCP. You might need to set the following properties:

        1. **Google API Address:** Specifies if the API address is **Public** , **Private** , or **Restricted**. The default value is **Public**. Choose **Private** or **Restricted** if you are using Private Google Access. Ensure that you specify the DNS service of the Google Cloud VMware Engine management plane.

        2. **HTTP Proxy:** Specifies a proxy server used for all outbound traffic to Google Cloud. The Migrate Connector does not support authentication so don't specify any authentication credentials.

        3. **Static network route:** If required by your network environment specify static routes.

  11. Select **Finish** when you have completed the configuration to deploy the VM.

  12. After deployment completes, start the VM.

  13. After the VM starts, record its IP address.




You need the IP address in the next section to register the connector.

###  VMware OVF Tool (ovftool) 

To install the Migrate Connector using the ovftool command line, follow these steps:

  1. Download and install the [VMware OVF Tool](https://developer.broadcom.com/tools/open-virtualization-format-ovf-tool/latest). For more information, see [OVF Tool User's Guide](https://docs.vmware.com/en/VMware-vSphere/8.0/ovf-tool-user-guide/GUID-84A7C807-98FC-421B-9897-562850E75FA0.html).

  2. To install the Migrate Connector, pass the following parameters using the `--prop` prefix.
         
         ovftool.exe -ds=  -n=  --net:"VM Network=" --prop:ip0="" --prop:gateway="" --prop:DNS="" --prop:route0="" --prop:netmask0="" --prop:hostname="host name" --prop:public-keys="" --prop:connectiontype="Public" --acceptAllEulas  vi:/

The following command is an example of deploying the `migrate-connector-2-3-2077.ova` file to a vCenter `172.23.0.10/Manual/host/esx-qa-03.gvelos.lab`, creating a VM named `m2vm`, and setting its parameters.
         
         ovftool.exe -ds=ds.23.0.33 -n=m2vm  --net:"VM Network=Lab" --prop:ip0="172.23.0.243" --prop:gateway="172.23.255.253" --prop:DNS="172.23.0.1" --prop:route0="10.0.0.0/16 172.23.0.1" --prop:netmask0="255.255.0.0" --prop:hostname="host name" --prop:public-keys="public keys1212121211" --prop:connectiontype="Public" --acceptAllEulas migrate-connector-2-3-2077.ova vi://user%40gvelos.lab@172.23.0.10/Manual/host/esx-qa-03.gvelos.lab

The following table describes the parameters you can pass with the `--prop` prefix to install the Migrate Connector:

Parameter | Description  
---|---  
public-keys  | The public key that grants SSH login access for the administrator. Minimum length is 20 characters.   
hostname  | The hostname to set for this Migrate Connector appliance. The hostname must be between 0-255 characters long.   
connectiontype  | Google API addresses to use this Migrate Connector appliance. The valid values are Public, Private, and Restricted. Public is the default value.   
Ip0  | The IP address to set for this Migrate Connector appliance. Use `0.0.0.0` for DHCP. By default, `0.0.0.0` is used when no value is supplied for this parameter.   
netmask0  | The netmask or prefix for the network interface. Ignore if DHCP is used.   
gateway  | The default gateway address for this Migrate Connector appliance. Ignore if DHCP is used.   
DNS  | The DNS for this Migrate Connector appliance (comma separated). Ensure that you specify the DNS service of the Google Cloud VMware Engine management plane. Ignore if DHCP is used.   
route0  | A static network route. Format:`<Network>/<Bits> <Gateway>`  
proxy  | HTTP proxy address. Format: `<IP address>:<Port>`  



### Private Google Access for on-premises hosts

Migration traffic can also be routed over VPN or [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options) instead:

[ ![Migrate Connector access over a VPN.](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/m4ce-arch-private.svg)](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/m4ce-arch-private.svg)

With Private Google Access, your on-premises hosts connect to Google Cloud APIs through a Cloud VPN tunnel or Cloud Interconnect by using one of the [Private Google Access-specific domains and VIPs](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid#private-vips). If your environment uses Private Google Access, ensure that you have configured access correctly so that the Migrate Connector can access Google Cloud APIs.

For more information, see [Dedicated interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview).

### Use a proxy to connect to Google Cloud APIs

In some environments, the Migrate Connector might not be able to make external internet requests. In this case, the Migrate Connector might have to access a proxy that is then allowed to make the connection:

[ ![Migrate Connector access over a proxy.](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/m4ce-arch-proxy.svg)](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/m4ce-arch-proxy.svg)

## Register the Migrate Connector as a Google Cloud source

After you install the Migrate Connector on vSphere, you need to register it as a Google Cloud source. Registration allows the connector to then pass data to Google Cloud.

**Note:** The Migrate Connector VM contains the `m2vm` CLI that you use to perform registration.

To register the connector:

  1. From your workstation, open an SSH connection to the Migrate Connector using the IP address of the Migrate Connector VM and the private key you created earlier in Create the SSH public or private key pair.

For example, for Linux you can use the `ssh` command:
         
         ssh -i path-to-private-key admin@connector-ip-or-hostname 

For Windows, you can use PuTTy to open the connection:

     1. Start Putty.

     2. Under **Connection - > SSH-> AUTH -> private key file for authentication** select the private key file.

     3. In **Session - > Host Name** specify:

`admin@connector-ip-or-hostname`

     4. Click **Open**.

  2. View help information for the `m2vm` CLI:
         
         m2vm --help

  3. View the connector status:
         
         m2vm status

The results should show that the connector can reach Cloud APIs and that it is not registered.

  4. To register the connector enter the command:
         
         m2vm register

You are prompted for the following information:

     1. The **vCenter host IP** address, meaning the IP address of the vCenter in the vSphere cluster you are migrating VM from. This is typically the same IP address that you see when you sign in to vSphere.

     2. Verify the vSphere thumbprint.

     3. Enter the username and password for the vCenter account used to administer the Migrate Connector. This is the account you created as described in [1\. Create the vCenter user for the Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-vmware-source#step-1).

     4. Enter your Google Cloud access token:
            
            Please provide your Google Cloud User Account access token to register Migrate Connector (Note: The token is valid for 60 minutes) Enter access token:

To obtain an access token using the Google Cloud console, follow these steps:

        1. Navigate to [the Google Cloud console](https://console.cloud.google.com/).

        2. Click the **Activate Cloud Shell Terminal** terminal button in the top-right of Google Cloud console. The Cloud Shell Terminal should appear at the bottom of your screen.

        3. In the Cloud Shell Terminal, run the following command:
               
               gcloud auth print-access-token

        4. Copy the access token from Cloud Shell and paste it into the Migrate to Virtual Machines CLI.

     5. Select the Google Cloud **host** project you want to connect with the Migrate Connector. You must have already enabled the Migrate to Virtual Machines API in this project as described in [Enable Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/enable-services).

     6. Select the Google Cloud region you want to connect with this Migrate Connector. See [Select the Google Cloud region](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-vmware-source#step-4) for more on selecting the region.

     7. Enter the **source name.** This is the name of the source as shown in the Google Cloud console for Migrate to Virtual Machines.

     8. Select **new** and enter name for a new source, or select an existing source to overwrite it.

     9. Specify the **service** account in your host project to be used by the Migrate Connector to connect to Google Cloud. You can select an existing **service** account, or let the Migrate Connector create a new one for you as described in [Define Google Cloud accounts](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-vmware-source#step-3).

The Migrate Connector connects to disks on your on-premises data center to replicate data to Google Cloud. Registration applies the necessary roles to this service account automatically to enable this data transfer.

**Note:** It might take several minutes for the registration process to complete before the status indicates that the connector is registered.
     10. Enter the [customer managed encryption key (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) you want to use to protect your data in Google Cloud. By default, Google Cloud automatically [encrypts data when it is at rest](https://cloud.google.com/docs/security/encryption/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use CMEK to encrypt and decrypt your data at rest. These encryption keys are created, managed, and owned by you.

  5. Check the status:
         
         m2vm status

Ensure that the connector is now registered.

  6. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  7. Select the **Sources** tab. You should see the new source appear in the source drop-down list.

**Note:** It might take several minutes for the new source to appear in the drop-down list.



## Set up throttling for the Migrate Connector

Migrate to Virtual Machines lets you set up throttling on the Migrate Connector to control the rate at which data is transferred from the Migrate Connector. Throttling ensures that the migration process distributes bandwidth evenly between the migration and any other tasks using the network. In this way, the migration can complete successfully without disrupting any other tasks.

You can set the upper limit of throttling to any value up to the supported bandwidth of the outbound links of the Migrate Connector. The lower limit is 5 MBps. Throttling is disabled by default. You can manage throttling using the `m2vm` CLI.

Starting with version 2.7, Migrate Connector supports throttling with a second NIC. If you use multiple NICs and set a throttling rate, Migrate Connector applies that same rate to all the NICs. For example, if you have 2 NICs and you limit the throttling rate to 10 MBps, Migrate Connector limits both NIC 1 and NIC 2 to 10 MBps.

**Note:** The throttling rate is configured in Megabytes per second (MBps), rather than Megabits per second (Mbps) which is commonly used to describe network throughput.

  * To set up throttling, use the following command:
        
        m2vm upload-max-rate set MBPS
        

Replace MBPS with the maximum rate at which you want to throttle data transferred from the Migrate Connector.

  * To check if throttling is set up, use the following command:
        
        m2vm upload-max-rate show
        

  * To remove throttling, use the following command:
        
        m2vm upload-max-rate unset
        




You can use the vSphere UI to monitor the network bandwidth of an appliance. Select an appliance VM and navigate to the **Monitor** page. If throttling is set, the graph in the **Network** chart is displayed below the configured rate limit.

## Modify a Migrate Connector configuration

You can modify the properties of a Migrate Connector configuration. The way you modify the connector is based on the properties that you want to update:

  * To modify properties of the Migrate Connector VM, such as the **Static network route** , sign in to vSphere and edit the OVA parameters for the Migrate Connector.

  * To modify the properties used to register the connector as a Google Cloud source, such as the Google Cloud host project or region, use the `m2vm` CLI.




**To modify the VM parameters:**

  1. Sign in to vSphere using an account with the permissions required to edit a VM.

  2. Stop the Migrate Connector VM.

  3. Edit the OVA parameters for the Migrate Connector.

  4. Start the VM.




**To modify the Google Cloud registration properties:**

**Note:** All existing registration properties are deleted when you start the modification process. You must complete the entire registration process to perform the modification. If you cancel the process before completing the entire process, the connector won't work.

  1. From your workstation, open an SSH connection to the Migrate Connector using the IP address of the Migrate Connector VM and the private key you created earlier:
         
         ssh -i path-to-private-key admin@connector-vm-ip 

  2. Run the `register` command:
         
         m2vm register

See Registering the Migrate Connector as a Google Cloud source.




## Update a Migrate Connector

Migrate to Virtual Machines supports Migrate Connector updates. When an update is available for a Migrate Connector, you can see a relevant message in the **Sources** card on the dashboard, and also on the **Sources** tab while the relevant source is selected. A notification is also displayed on the **Sources** tab if other sources have updates.

To update your Migrate Connector, follow these steps:

  1. Click the **Sources** tab. If an update is available, you can see the message **An update is available for your source**.

  2. Click the **View details** button. On the **Source details** page, you can see the message **An in-place update is available for your source**.

**Note:** If the **Update** button is unavailable and you see the message **A new version of the Migrate Connector is available for your source** , you need to redeploy your Migrate Connector.
  3. Click the **Update** button. Once your Migrate Connector has been updated, you can see the message **Source has been successfully updated**.

  4. Optional: Verify the update by checking the **Last update** field on the **Source details** page.




## Redeploy a Migrate Connector

In rare cases (such as a significant change in the core Migrate Connector code base), automatic updates may not be available for your Migrate Connector. In this case, you need to redeploy your Migrate Connector.

To redeploy a Migrate Connector, follow these steps:

  1. Download and install the Migrate Connector OVA file.

  2. Register the new Migrate Connector using the same **region** and **source** (your earlier Migrate Connector is now idle).

  3. Stop and delete your previous Migrate Connector's VM to clean up resources.




## Add a second NIC to your Migrate Connector

Migrate to Virtual Machines enables your Migrate Connector to use two different network interface cards (NICs).

If you want to use two NICs, first [install your migrate connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector#install-migrate-connector), then verify your existing **NIC ID** before adding a second NIC to your Migrate Connector using vSphere and Migrate to Virtual Machines.

**Note:** Using a second NIC is optional.**Note:** Starting with version 2.7, Migrate Connector supports throttling with a second NIC.

To add a second NIC to your Migrate Connector, follow these steps:

  1. Identify the first **NIC ID** on your Migrate Connector's VM:
         
         sudo ls /sys/class/net/ | grep ens

  2. Navigate to vSphere. Within vSphere, open the **Network Adapter** dialog:

Click **Select VM > Edit Settings > Add New Device > Network Adapter**.

  3. Identify the newly added **NIC ID** on your Migrate Connector's VM by running the following command:
         
         sudo ls /sys/class/net/ | grep ens

Take note of the new **NIC ID** as you will use it in your [netplan configuration file](https://netplan.readthedocs.io/en/stable/netplan-yaml/).

  4. Create a new netplan configuration file by running the command: `posix-terminal sudo vi /etc/netplan/config2.yaml`

**Warning:** **Do not change the existing network configuration file** (`/etc/netplan/config.yaml`). It is automatically created on every boot.
  5. Edit your netplan configuration file to contain your new NIC configuration:

     1. To configure a second NIC named ens224 to use DHCP, follow this example:
            
            network:
              version: 2
              renderer: networkd
              ethernets:
                ens224:
                 dhcp4: yes
                 link-local: []
            

     2. To configure a second NIC named ens224 to use Static IP, follow this example:
            
            network:
              version: 2
              renderer: networkd
              ethernets:
                ens224:
                 dhcp4: no
                 addresses: IP/CIDR
                 gateway4: GW address
                 link-local: []
                 nameservers:
                   addresses: DNS servers
            

Lastly, to apply your configuration, run the following command:
    
    sudo netplan apply




For more information, see the [Netplan configuration examples](https://netplan.readthedocs.io/en/stable/examples/) documentation.

## Delete a Migrate Connector

To delete a Migrate Connector, you must delete the corresponding source in the Google Cloud console, and delete the vSphere VM for the Migrate Connector. Follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Sources** tab.

  3. From the drop-down list, select the source corresponding to the Migrate Connector.

  4. Select the **Migrations** tab.

  5. Select all source VMs.

  6. Select **Delete** and then confirm the deletion.

The VMs are removed from the Migration table.

  7. Select the **Sources** tab.

  8. Select **Source Details**.

  9. Under the **Data center connectors** section of the **Source Details** page, select the trash icon next to the name of the source to delete the connector.

  10. Confirm the delete.

  11. Select **Delete Source** to delete the source.

  12. Sign in to vSphere using an account with the permissions required to delete a VM.

  13. Stop the Migrate Connector VM.

  14. Delete the VM.




## What's next

  * [Migrate individual VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
