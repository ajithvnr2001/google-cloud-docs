---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance/
title: Receive your Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:17.345886+00:00
---

# Receive your Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/receive-appliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)
  * [ Guides ](https://docs.cloud.google.com/transfer-appliance/docs/4.0/procedure-guide)



Send feedback 

#  Receive your Transfer Appliance Stay organized with collections  Save and categorize content based on your preferences. 

## Confirm Receipt

If you have received the Transfer Appliance for data ingestion in cloud, follow these steps in the Google Cloud console:

  1. Ensure you have the following permissions:

     * transferappliance.appliances.update
     * transferappliance.orders.get
     * transferappliance.orders.update

You will be able to get these required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). You can search for [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) for a given permission.

  2. Go to [appliances page](https://console.cloud.google.com/appliances) and select the appliance.

  3. Open the Setup Checklist.

  4. Navigate to the "Track Shipment and Confirm Receipt" task.

  5. Click on the "Confirm Receipt" button. This will open a popup box to confirm the receipt.

  6. Ensure that you click the "Confirm Receipt" button in the popup box only if you have indeed received the appliance, as this action will mark the appliance as "ON_SITE."




## Verify the package contents

Before connecting Transfer Appliance, we strongly recommend that you verify that the package arrived intact, with all required cables and equipment. We ensure you have everything necessary for a successful data transfer.

After receiving Transfer Appliance, verify that package contents are intact by doing the following:

###  Rackable TA40 and TA300 

  1. Confirm that the shipping case and tamper-evident seals are intact.

![D-rings secured by tamper-evident tag](https://docs.cloud.google.com/transfer-appliance/docs/images/shipping-container-d-rings-secured.png)

**Caution:** If the seal on the shipping case is missing or broken, inspect the contents of the case to ensure no items are missing.
  2. Break or cut the tamper-evident wire tag using side cutters or other wire cutting tool capable of cutting a wire with a diameter of 2.5 millimeters (0.1 in). Open the shipping case.

  3. Contact the Transfer Appliance Team if any of the following items are missing:

Item | Description  
---|---  
![A photo depicting a NEMA 5-15P power cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/nema-5-15p-to-c13-power-cable.png) | NEMA 5-15p to C13 power cable (1.8 m / 5.91 ft)  
![A photo depicting a c14 to c13 power cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/c14-to-c13-power-cable.png) | C14 to C13 power cable, for connections to the power distribution unit (PDU) (1.5 m / 4.92 ft)  
![A photo depicting a Category 6 network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/cat6-ethernet-cable.png) | Cat 6 network cable (2.1 m / 6.89 ft)  
![A photo depicting a QSFP28 twinaxial copper network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/qsfp-plus-dac-twinax-cable.png) | **TA300 V2 and TA40 V2:** QSFP28 Twinax copper network cable  
![A photo depicting a QSFP28 to SFP28 adapter](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/qsfp28-to-sfp28-adapter.png) | **TA300 V2 and TA40 V2:** QSFP28 to SFP28 adapter  
![A photo depicting a SFP28 to SFP28 network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/sfp28-to-sfp28-cable.png) | **TA300 V2 and TA40 V2:** SFP28 to SFP28 network cable  
![A photo depicting a USB-to-serial adapter cable](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/usb-to-serial-adapter-cable.png) | USB-to-serial adapter cable – use only if instructed by Transfer Appliance Team  
![A photo depicting a pin-to-socket serial adapter](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/pin-to-socket-serial-adapter.png) | Pin-to-socket serial adapter  
![A photo depicting a SFP28 to RJ45 transceiver](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/sfp28-to-rj45-transceiver.jpg) | **TA40 V2:** SFP28 to RJ45 Transceiver  
![A photo depicting a tamper-evident tag](https://docs.cloud.google.com/transfer-appliance/docs/images/wire-tamper-evident-tag.png) | Wire tamper-evident tag  
![An example tie-on tag](https://docs.cloud.google.com/transfer-appliance/docs/images/tie-on-tag.png) | Tie-on tag  
![An example zip tie](https://docs.cloud.google.com/transfer-appliance/docs/images/zip-tie.png) | Zip tie  
![An example shipping label pouch](https://docs.cloud.google.com/transfer-appliance/docs/images/shipping-pouch.png) | Shipping-label pouch  
![A photo of a Transfer Appliance inside an opened shipping
              case](https://docs.cloud.google.com/transfer-appliance/docs/images/case-opened.png) | Transfer Appliance  



###  Freestanding TA40 and TA300 

  1. Confirm that the shipping case and tamper-evident seals are intact.

![Case secured by tamper-evident tags](https://docs.cloud.google.com/transfer-appliance/docs/images/ta-redesign-secured.png)

**Caution:** If the seal on the shipping case is missing or broken, inspect the contents of the case to ensure no items are missing.
  2. Break or cut the tamper-evident wire tag using side cutters or other wire cutting tool capable of cutting a wire with a diameter of 2.5 millimeters (0.1 in). Open the shipping case.

  3. Contact the Transfer Appliance Team if any of the following items are missing:

Item | Description  
---|---  
![A photo depicting a NEMA 5-15p to c13 power cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/nema-5-15p-to-c13-power-cable.png) | NEMA 5-15p to C13 power cable  
![A photo depicting a c14 to c13 power cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/c14-to-c13-power-cable.png) | C14 to C13 power cable, for connections to the power distribution unit (PDU)  
![A photo depicting a Category 6 network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/cat6-ethernet-cable.png) | Category 6 (Cat6) network cable  
![A photo depicting a QSFP+ Twinax copper network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/qsfp-plus-dac-twinax-cable.png) | QSFP+ Twinax copper network cable  
![A photo depicting a QSFP+ to 4xSFP+ network cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/qsfp-plus-to-4xsfp-plus.png) | QSFP+ to 4xSFP+ network cable  
![A photo depicting a USB-to-serial adapter cable](https://docs.cloud.google.com/static/transfer-appliance/docs/images/usb-to-serial-adapter-cable.png) | USB-to-serial adapter cable – use only if instructed by Transfer Appliance Team  
![A photo depicting a pin-to-socket serial adapter](https://docs.cloud.google.com/static/transfer-appliance/docs/images/pin-to-socket-serial-adapter.png) | Pin-to-socket serial adapter  
![A photo depicting a tamper-evident tag](https://docs.cloud.google.com/transfer-appliance/docs/images/wire-tamper-evident-tag.png) | Wire tamper-evident tag  



## Validate the appliance

Before connecting the appliance to your network, you must run a small application on your laptop to validate that the appliance hasn't been tampered with during shipping.

The Transfer Appliance Attestation Application supports the following 64-bit operating systems:

  * Linux kernel 2.6.23 or later
  * Microsoft Windows Server 2012 or later
  * Microsoft Windows 10
  * Apple macOS 10.11 or later



To validate the appliance, do the following:

  1. Connect the appliance:

###  Rackable TA40 and TA300 

     1. Connect a Cat6 cable between the left network port and your laptop.

     2. Connect the supplied power cable to the power socket on the appliance and to an open power socket on a power distribution unit (PDU).

        * **TA40 V2:** Connect both power sockets on the appliance.

**TA300 V2** ![Cable connections for TA300 V2](https://docs.cloud.google.com/transfer-appliance/docs/images/ta300v2-back-validate.png)**TA40 V2** ![Cable connections for TA40v2](https://docs.cloud.google.com/transfer-appliance/docs/images/ta40v2/ta40v2-validate-ports.png)

###  Freestanding TA40 and TA300 

     1. Connect a Cat6 cable between the left network port and your laptop.

![Left network port](https://docs.cloud.google.com/transfer-appliance/docs/images/ta-redesign-left-network-port.png)

     2. Connect the supplied power cable to the power socket on the appliance and to an open power socket on a power distribution unit (PDU).

![Cable connections for Transfer Appliance](https://docs.cloud.google.com/transfer-appliance/docs/images/ta-redesign-power-port.png)

  2. Power on Transfer Appliance.

  3. Use `ping` to verify that you can contact the appliance through its configuration port:
         
         ping 169.254.20.1

The following sample response resembles the output that is returned:
         
         PING 169.254.20.1 (169.254.20.1) 56(84) bytes of data.
         64 bytes from 169.254.20.1: icmp_seq=1 ttl=64 time=0.060 ms
         64 bytes from 169.254.20.1: icmp_seq=2 ttl=64 time=0.039 ms
         64 bytes from 169.254.20.1: icmp_seq=3 ttl=64 time=0.039 ms
         ^C
         --- 169.254.20.1 ping statistics ---
         3 packets transmitted, 3 received, 0% packet loss, time 2045ms
         rtt min/avg/max/mdev = 0.039/0.046/0.060/0.009 ms
         

**Note:** The `169.254.20.1` IPv4 address applies only to the appliance's configuration port.

  4. To download the Transfer Appliance Attestation Application to your laptop, do the following:

### Microsoft Windows

     1. [Download](https://storage.googleapis.com/transferappliance/attestator/taattestator_x86_64-windows.exe) the Transfer Appliance Attestation Application to your laptop.

     2. Open a **Command Prompt** , and navigate to the location where you downloaded the Transfer Appliance Attestation Application.

     3. To validate the appliance, run the following command on your laptop:
            
            taattestator_x86_64-windows.exe
            

### Linux

     1. On your laptop, open a terminal app.

     2. To download the Transfer Appliance Attestation Application, run the following command on your laptop:
            
            wget https://storage.googleapis.com/transferappliance/attestator/taattestator_x86_64-linux
            

     3. Run the following commands on your laptop to validate the appliance:
            
            chmod 0777 taattestator_x86_64-linux
            ./taattestator_x86_64-linux
            

### Apple macOS

     1. Open the **Terminal** app.

     2. Run the following command on your laptop to download the Transfer Appliance Attestation Application:
            
            curl -O https://storage.googleapis.com/transferappliance/attestator/taattestator_x86_64-darwin
            

     3. Run the following commands on your laptop to validate the appliance:
            
            chmod 0777 taattestator_x86_64-darwin
            ./taattestator_x86_64-darwin
            

  5. If the appliance was not tampered with during shipment, the app will return a Transfer Appliance Attestation Passcode.

  6. For data export appliance, once you have received the Transfer Appliance Attestation Passcode in the previous step, look for the email titled "Google Transfer Appliance Delivered and Validation Steps" with instructions for submitting the Transfer Appliance Attestation Passcode and receiving the credentials. Skip next step for data export order.

  7. For offline and online appliance, once you have received the Transfer Appliance Attestation Passcode in the previous step, proceed with the following instructions:

Ensure you have the following permissions: * transferappliance.appliances.update * transferappliance.credentials.get

You will be able to get these required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). You can search for [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) for a given permission.

     1. Go to [appliances page](https://console.cloud.google.com/appliances) and select the appliance.
     2. Open the Setup Checklist.
     3. Locate and select the "Check Integrity" task.
     4. Submit the Transfer Appliance Attestation Passcode returned by the appliance. In case of an incorrect entry, attempt to re-enter the correct code.
     5. Click the "Get Credentials" button to retrieve the seal password.

Once the attestation code is accepted, the seal password will be displayed in the Google Cloud console. If the Google Cloud console displays an error message, contact the Transfer Appliance Team at [data-support@google.com](mailto:data-support@google.com) for assistance.




The sealing layer offers enhanced data security and greater flexibility for relocating the appliance. 

## Connect to Transfer Appliance

You need the login details for the appliance to connect to it. The Transfer Appliance Team provides the appliance login details in exchange for a Transfer Appliance Attestation Passcode that indicates the appliance wasn't tampered with during shipping.

**Note:** A login password is not required. Once the seal password is assigned after successful attestation, you don't need to enter a password upon subsequent login attempts with your username. You are logged in directly (password-less login).

  1. After you have the login details, connect the appliance to your network:

###  Rackable TA40 and TA300 

     1. Keep the cable connected between the left network port and your laptop.

     2. Connect a cable to the right network port and to an open port that's connected to your network.

        * **TA300 V2 and TA40 V2** : Connect the appliance through either the QSFP port (using a QSFP28 cable) or the RJ45 port (using a Cat6 cable).

**TA300 V2** ![Network port highlighted on TA300 V2 appliance.](https://docs.cloud.google.com/transfer-appliance/docs/images/ta300v2-connect-network.png)**TA40 V2** ![Network port highlighted on the appliance.](https://docs.cloud.google.com/transfer-appliance/docs/images/ta40v2/ta40v2-connect-ports.png)

###  Freestanding TA40 and TA300 

     1. Keep the Cat6 cable connected between the left network port and your laptop.

     2. Connect a Cat6 cable to the right network port and to an open RJ45 port that's connected to your network.

![Right network port](https://docs.cloud.google.com/transfer-appliance/docs/images/ta-redesign-right-network-port.png)

  2. Connect to the appliance: 

### Windows

     1. Open Putty. 
     2. For **Connection type** , select **SSH**. 
     3. In the **Host Name** field, enter: 
            
            169.254.20.1
                        

     4. For **Connection type** , verify that **SSH** is selected. 
     5. Click **Open**. 
     6. Enter the username provided by Transfer Appliance Team when prompted. You are logged in directly without needing to enter a password. 

### Linux

     1. Run the following command: 
            
            ssh USERNAME@169.254.20.1
                        

Replacing `USERNAME` with the username provided by Transfer Appliance Team. 

You are logged in directly without needing to enter a password. 

### Mac

     1. Run the following command: 
            
            ssh USERNAME@169.254.20.1
                        

Replacing `USERNAME` with the username provided by Transfer Appliance Team. 

You are logged in directly without needing to enter a password. 




A freestanding appliance displays `Ready for setup` on the status screen after you connect to the appliance.

## Configure appliance software

Before you transfer data to the Transfer Appliance you must verify the status of the appliance and configure the software on the appliance to work on your network.

To configure the appliance's software, follow the instructions below:

  1. Verify the status of the appliance by running the following command from your laptop or workstation connected to the appliance:
         
         ta status 

The following sample response resembles the output that is returned:

###  TA300 V2 and TA40 V2 
         
         **You are ready to configure the appliance.**
         
         Next steps:
         » Configure the appliance using one of the following commands:
         **> ta config --data_port=RJ45 --ip=dhcp**
         **> ta config --data_port=QSFP --ip=dhcp**
         » To set a static IP address and gateway, use the '--ip' and '--gw' flags. For example:
         **> ta config --data_port=RJ45 --ip=192.168.0.100/24 --gw=192.168.0.1**
         **> ta config --data_port=QSFP --ip=192.168.0.100/24 --gw=192.168.0.1**
         

  2. Configure the appliance. You can configure the appliance to use DHCP to obtain an IP address automatically, or you can configure the appliance to use a static IP address.

To configure the appliance, run the following command:

### DHCP
         
         ta config --data_port=PORT --ip=dhcp [--proxy_addr=123.45.67.89]
         

     * Replace `PORT` with the data port you are using on the appliance, either `RJ45` or `QSFP`.

     * Optionally use the `--proxy_addr` flag to specify a proxy server IP address for online transfers.

### Static IP
    
    ta config --data_port=PORT --ip=IP_ADDRESS/NETMASK --gw=GATEWAY_ADDRESS [--proxy_addr=123.45.67.89]

Replace the following:

     * `PORT`: The data port you are using on the appliance, either `RJ45` or `QSFP`.

     * `IP_ADDRESS`: the IP address for the appliance, or `dhcp` for automatic IP address configuration.

     * `NETMASK`: The netmask in CIDR notation. Not required if you are using DHCP.

     * `GATEWAY_ADDRESS`: The gateway IP address. Not required if you are using DHCP.

If you do not want to use a gateway and only allow clients on the same subnet to connect to the Transfer Appliance, enter `--gw=0.0.0.0` as the `GATEWAY_ADDRESS`.

     * Optionally use the `--proxy_addr` flag to add proxy support when you perform online transfers and enter the IP address for the appliance.

The following sample response resembles the output that is returned:
    
    Configuring, encrypting, and mounting data partition...
    Verified partition settings for "/mnt/ta_metadata".
    Partition key generated and encrypted.
    Verifying partition settings and mounting data partition.
    This may take several minutes to finish...
    Mounted partition "/mnt/ta_data".
    Verified partition settings for "/mnt/ta_data".
    Data partition is mounted.
    Mounting now permissible under "/mnt/ta_data_base/ta_mounts".
    Customer fstab file "/opt/customer.fstab" created.
    Network is configured.
    Configured NFS share "/mnt/ta_data".
    NFS share "/mnt/ta_data" is configured.
    
    Appliance has been successfully configured. You can begin copying data.
    
    Use these commands to mount the NFS share from your client:
    **> sudo mkdir /mnt/data**
    **> sudo mount 192.168.0.100:/mnt/ta_data /mnt/data**
    




## Change appliance configurations

To change Transfer Appliance configurations, you can use the `ta config` command as often as you need with alternate arguments to reconfigure the settings on your appliance.

## Resuming copy after a reboot

To resume copy after a reboot, run the following command and enter the Transfer Appliance seal password (provided on the Google Cloud console credentials page) when prompted:
    
    
      ta unseal
      

After successful verification of the seal password, the data partition will become accessible again.

## What's next

  * **Optional** : Set the Transfer Appliance to [online mode](https://docs.cloud.google.com/transfer-appliance/docs/4.0/online-transfer#set_to_online_mode).

  * [Copy data](https://docs.cloud.google.com/transfer-appliance/docs/4.0/transfer-data) to the Transfer Appliance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
