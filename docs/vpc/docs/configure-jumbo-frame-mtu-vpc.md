---
url: https://docs.cloud.google.com/vpc/docs/configure-jumbo-frame-mtu-vpc/
title: Create and verify a jumbo frame MTU network \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:43.938349+00:00
---

# Create and verify a jumbo frame MTU network  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-jumbo-frame-mtu-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and verify a jumbo frame MTU network

This page walks you through creating a Virtual Private Cloud (VPC) network and two Compute Engine instances for testing. It assumes you are generally familiar with network [MTU](https://docs.cloud.google.com/vpc/docs/mtu).

## Create an auto mode VPC network

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select a project in the project pull-down menu.

  3. Click **Create VPC network**.

  4. Enter a **Name** for the network.

  5. Choose **Automatic** for the **Subnet creation mode**.

  6. Clear the **Set MTU automatically** checkbox.

  7. Set the **Maximum transmission unit (MTU)**.

For a compute instance to send and receive jumbo frames, the instance's virtual NIC needs to be connected to a VPC network that has an MTU value that is as large or larger than the machine MTU. Set the MTU to the largest possible value for the instance, for example

     1. If you're using GPU machines, see [Jumbo frames and GPU machines](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-frames-mtu).
  8. Click **Create**.




## Create firewall rules

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule**.

  3. Enter a **Name** for the firewall rule.   
This name must be unique for the project.

  4. In the **Network** pull-down menu, specify the name of the network you created.

  5. In the **Targets** pull-down menu, select **All instances in the network**.

  6. From the **Source filter** pull-down menu, select **IPv4 ranges**.

  7. In the field enter **10.128.0.0/16**.

  8. In **Protocols and ports** , select **Specified protocols and ports**.

  9. Check the **tcp** checkbox and enter **22** in the field.

  10. Check the **Other protocols** checkbox and enter **icmp** in the field.

  11. Click **Create**.




## Create compute instances

This section shows you how to create two compute instances for testing.

###  Console 

Do these steps twice to create two compute instances in the same zone.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Specify a **Name** for your instance.

  4. Click **Networking, Disks, Security, Management, Sole-tenancy**.

  5. Click **Networking**.

  6. In **Network interfaces** , click **default default (10.128.0.0/20)**.

  7. In the **Network** pull-down menu, select the network you created.




## Connect to compute instances by using SSH

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Connect** column of your first instance, click **SSH**.

  3. In the **Connect** column of your second instance, click **SSH**.




## Verify MTU

  1. In the terminal for your _first_ compute instance, run the following command:
         
         /sbin/ifconfig | grep mtu
         

The output is similar to the following. The MTU is reported as `8896`.
         
         ens4: flags=4163  mtu 8896
         lo: flags=73  mtu 65536
         

  2. In the terminal for your _second_ compute instance, install `tcpdump`:
         
         sudo apt-get install tcpdump --yes
         

  3. In the terminal of your _second_ compute instance, start `tcpdump`. Replace FIRST_INSTANCE with the name of your first instance.
         
         sudo tcpdump host FIRST_INSTANCE -v
         

  4. In the terminal of your _first_ compute instance, ping your second instance. In the `ping` command, specify a packet size that is 28 bytes smaller than the network MTU. Replace SECOND_INSTANCE with the name of your second instance.
         
         ping SECOND_INSTANCE -c 10 -M do -s 8868
         

  5. In the terminal of your _second_ compute instance, view the output of the `tcpdump` command. The output is similar to the following:
         
         tcpdump: listening on ens4, link-type EN10MB (Ethernet), snapshot length 262144 bytes
         19:43:57.116005 IP (tos 0x0, ttl 64, id 0, offset 0, flags [DF], proto ICMP (1), length 8896)
             FIRST_INSTANCE.c.PROJECT_ID.internal > SECOND_INSTANCE.c.PROJECT_ID.internal: ICMP echo request, id 5253, seq 1, length 8876
         19:43:57.116053 IP (tos 0x0, ttl 64, id 23961, offset 0, flags [none], proto ICMP (1), length 8896)
             SECOND_INSTANCE.c.PROJECT_ID.internal > FIRST_INSTANCE.c.PROJECT_ID.internal: ICMP echo reply, id 5253, seq 1, length 8876
         

The variables mean the following:

     * `FIRST_INSTANCE`: the name of your first instance.
     * `SECOND_INSTANCE`: the name of your second instance.
     * `PROJECT_ID`: the ID of the project containing the instances.
  6. On your second instance, press `Ctrl-c` to stop `tcpdump`.

  7. When you're done testing, delete your resources in the following order:

     1. Firewall rule and compute instances
     2. VPC network



## What's next

  * Learn more about [MTU](https://docs.cloud.google.com/vpc/docs/mtu).
  * Create a [VPC network with a specified MTU](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
