---
url: https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/creating-nested-vms/
title: Create nested VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:31.245636+00:00
---

# Create nested VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/creating-nested-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create nested VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

Nested virtualization is allowed by default, so unless somebody modifies the constraint for nested virtualization, you do not need to make any changes before you create nested VMs in an organization, folder, or project. If your project doesn't belong to an organization, nested virtualization is allowed by default and you can't change the constraint. For information about how to modify the constraint that determines whether you can create nested VMs, see [Manage the nested virtualization constraint](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint).

This document describes how to create various types of level 2 (L2) virtual machine (VM) instances. Before creating a nested VM, you must [create an L1 VM that has nested virtualization enabled](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/enabling). For a description of L1 and L2 VMs, see the [Nested virtualization overview](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview).

After creating an L1 VM that has nested virtualization enabled, you can do any of the following:

  * Create an L2 VM with external network access
  * Create an L2 VM with a private network bridge to the L1 VM
  * Create an L2 VM with network access from outside the L1 VM



## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Creating an L2 VM with external network access

Create an L2 VM with external network access by using the following procedure. This procedure uses [`qemu-system-x86_64`](https://manpages.debian.org/stretch/qemu-system-x86/qemu-system-x86_64.1.en.html) to start the L2 VM. If you are using another procedure to create an L2 VM and are experiencing trouble, reproduce the issue using this procedure before contacting [Support](https://docs.cloud.google.com/support).

  1. [Create an L1 VM that has nested virtualization enabled](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/enabling).

  2. Use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to the VM:
         
         gcloud compute ssh VM_NAME
         

Replace `VM_NAME` with the name of the VM to connect to.

  3. Install the latest `qemu-kvm` package:
         
         sudo apt update && sudo apt install qemu-kvm -y
         

  4. Download a QEMU-compatible OS image to use for the L2 VM.

  5. Use the following command to start the L2 VM. When prompted, log in with `user: root`, `password: root`.
         
         sudo qemu-system-x86_64 -enable-kvm -hda IMAGE_NAME -m 512 -curses
         

Replace `IMAGE_NAME` with the name of the QEMU-compatible OS image to use for the L2 VM.

  6. Test that your L2 VM has external access:
         
         user@nested-vm:~$ host google.com
         




## Creating an L2 VM with a private network bridge to the L1 VM

Create an L2 VM with a private network bridge to the previously created L1 VM by using the following procedure. For information about changing the default maximum transmission unit (MTU) for your VPC network, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).

  1. [Create an L1 VM that has nested virtualization enabled](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/enabling).

  2. Use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to the VM:
         
         gcloud compute ssh VM_NAME
         

Replace `VM_NAME` with the name of the VM to connect to.

  3. Install the packages necessary to create the private bridge:
         
         sudo apt update && sudo apt install uml-utilities qemu-kvm bridge-utils virtinst libvirt-daemon-system libvirt-clients -y
         

  4. Start the default network that comes with the `libvirt` package:
         
         sudo virsh net-start default
         

  5. Run the following command to check that you have the `virbr0` bridge:
         
         ip addr
         

  6. The output is similar to the following:
         
         1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
             link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
             inet 127.0.0.1/8 scope host lo
                valid_lft forever preferred_lft forever
             inet6 ::1/128 scope host
                valid_lft forever preferred_lft forever
         2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc pfifo_fast state UP group default qlen 1000
             link/ether 42:01:0a:80:00:15 brd ff:ff:ff:ff:ff:ff
             inet 10.128.0.21/32 brd 10.128.0.21 scope global eth0
                valid_lft forever preferred_lft forever
             inet6 fe80::4001:aff:fe80:15/64 scope link
                valid_lft forever preferred_lft forever
         3: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
             link/ether 52:54:00:8c:a6:a1 brd ff:ff:ff:ff:ff:ff
             inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
                valid_lft forever preferred_lft forever
         4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
             link/ether 52:54:00:8c:a6:a1 brd ff:ff:ff:ff:ff:ff
         

  7. Create a `tap` interface to go from the L1 VM to the L2 VM:
         
         sudo tunctl -t tap0
         sudo ifconfig tap0 up
         

  8. Bond the `tap` interface to the private bridge:
         
         sudo brctl addif virbr0 tap0
         

  9. Run the following command to verify the setup of the bridge network:
         
         sudo brctl show
         

  10. The output is similar to the following:
         
         bridge name     bridge id               STP enabled     interfaces
         virbr0          8000.5254008ca6a1       yes             tap0
                                                                 virbr0-nic
         

  11. Download a QEMU-compatible OS image to use for the L2 VM.

  12. Run `screen`, and press Enter at the welcome prompt:
         
         screen
         

  13. Use the following command to start the L2 VM. When prompted, login in with `user: root`, `password: root`.
         
         sudo qemu-system-x86_64 -enable-kvm -hda IMAGE_NAME -m 512 -net nic -net tap,ifname=tap0,script=no -curses
         

Replace `IMAGE_NAME` with the name of the QEMU-compatible OS image to use for the L2 VM.

  14. On the L2 VM, run `ip addr show` to confirm that the VM has an address in the `virbr0` space—for example, `192.168.122.89`:
         
         user@nested-vm:~$ ip addr
         

  15. Start a placeholder web server on port `8000`:
         
         user@nested-vm:~$ python -m http.server
         

  16. Detach from the `screen` session with `Ctrl+A`, `Ctrl+D`.

  17. Test that your L1 VM can ping the L2 VM, replacing the following IP address with the IP address of the L2 VM:
         
         curl 192.168.122.89:8000
         

  18. The output is similar to the following:
         
         <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><html>
         <title>Directory listing for /</title>
         <body>
         <h2>Directory listing for /</h2>
         <hr>
         <ol>
         <li><a href=".aptitude/">.aptitude/</a>
         <li><a href=".bashrc">.bashrc</a>
         <li><a href=".profile">.profile</a>
         </ol>
         <hr>
         </body>
         </html>
         




## Creating an L2 VM with network access from outside the L1 VM

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.create` permissions on the project, folder, or organization 



You can set up an L2 VM with an alias IP so that VMs outside the L1 VM can access the L2 VM. Use the following procedure to create an L2 VM with network access by way of an alias IP from outside the previously created L1 VM. For information about creating alias IP addresses, see [Configure alias IP ranges](https://docs.cloud.google.com/vpc/docs/configure-alias-ip-ranges).

The following procedure assumes a previously created subnet called `subnet1`. If you already have a subnet with a different name, replace `subnet1` with the name of your subnet, or create a new subnet named `subnet1`.

  1. Create an L1 VM with nested virtualization enabled and include an alias IP range and support for HTTP/HTTPS traffic. The minimum CPU platform for Intel VMs must be `"Intel Haswell"`:

###  gcloud 
         
         gcloud compute instances create VM_NAME --enable-nested-virtualization \
             --tags http-server,https-server --can-ip-forward \
             --network-interface subnet=subnet1,aliases=/30
         

Replace `VM_NAME` with the name for the L1 VM.

###  REST 
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
         
         {
           ...
           "name": VM_NAME,
           "tags": {
             "items": [
               http-server,https-server
             ],
           },
           "canIpForward": true,
           "networkInterfaces": [
             {
               "subnetwork": "subnet1",
               "aliasIpRanges": [
                 {
                   "ipCidrRange": "/30"
                 }
               ],
             }
           ],
           "advancedMachineFeatures": {
             "enableNestedVirtualization": true
           },
           ...
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID

     * `ZONE`: the zone to create the VM in

     * `VM_NAME`: the name of the VM

  2. Use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to the VM. If you have trouble connecting to the VM, try resetting the VM or modifying the firewall rules.
         
         gcloud compute ssh VM_NAME
         

Replace `VM_NAME` with the name of the VM to connect to.

  3. Update the VM and install the necessary packages:
         
         sudo apt update && sudo apt install uml-utilities qemu-kvm bridge-utils virtinst libvirt-daemon-system libvirt-clients -y
         

  4. Start the default network that comes with the `libvirt` package:
         
         sudo virsh net-start default
         

  5. Run the following command to check that you have the `virbr0` bridge:
         
         user@nested-vm:~$ ip addr
         

  6. Verify output similar to the following:
         
         1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
             link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
             inet 127.0.0.1/8 scope host lo
                valid_lft forever preferred_lft forever
             inet6 ::1/128 scope host
                valid_lft forever preferred_lft forever
         2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc pfifo_fast state UP group default qlen 1000
             link/ether 42:01:0a:80:00:15 brd ff:ff:ff:ff:ff:ff
             inet 10.128.0.21/32 brd 10.128.0.21 scope global eth0
                valid_lft forever preferred_lft forever
             inet6 fe80::4001:aff:fe80:15/64 scope link
                valid_lft forever preferred_lft forever
         3: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
             link/ether 52:54:00:8c:a6:a1 brd ff:ff:ff:ff:ff:ff
             inet 192.168.122.1/24 brd 192.168.122.255 scope global virbr0
                valid_lft forever preferred_lft forever
         4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
             link/ether 52:54:00:8c:a6:a1 brd ff:ff:ff:ff:ff:ff
         

  7. Create a `tap` interface to go from the L1 VM to the L2 VM:
         
         sudo tunctl -t tap0
         sudo ifconfig tap0 up
         

  8. Bond the `tap` interface to the private bridge:
         
         sudo brctl addif virbr0 tap0
         

  9. Run the following command to verify the setup of the bridge network:
         
         sudo brctl show
         

  10. Verify output similar to the following:
         
         bridge name     bridge id               STP enabled     interfaces
         virbr0          8000.5254008ca6a1       yes             tap0
                                                                 virbr0-nic
         

  11. Download a QEMU-compatible OS image to use for the L2 VM.

  12. Run `screen`, and press Enter at the welcome prompt:
         
         screen
         

  13. Use the following command to start the nested VM. When prompted, login in with `user: root`, `password: root`.
         
         sudo qemu-system-x86_64 -enable-kvm -hda IMAGE_NAME -m 512 -net nic -net tap,ifname=tap0,script=no -curses
         

Replace `IMAGE_NAME` with the name of the QEMU-compatible OS image to use for the L2 VM.

  14. On the L2 VM, run `ip addr` to confirm that the L2 VM has an address in the virbr0 space, such as `192.168.122.89`:
         
         user@nested-vm:~$ ip addr
         

  15. Start a placeholder web server on port `8000`:
         
         user@nested-vm:~$ python -m http.server
         

  16. Detach from the `screen` session with `Ctrl+A`, `Ctrl+D`.

  17. Test that your L1 VM can ping the L2 VM, replace the IP address below with the IP address of the L2 VM:
         
         curl 192.168.122.89:8000
         

  18. Verify that the response from the L2 VM is similar to the following:
         
         <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><html>
         <title>Directory listing for /</title>
         <body>
         <h2>Directory listing for /</h2>
         <hr>
         <ol>
         <li><a href=".aptitude/">.aptitude/</a>
         <li><a href=".bashrc">.bashrc</a>
         <li><a href=".profile">.profile</a>
         </ol>
         <hr>
         </body>
         </html>
         

  19. On the L1 VM, set up `iptables` to allow forwarding from the L1 VM to the L2 VM. For the L2 OS image used in these instructions, you must flush the IP tables:
         
         sudo iptables -F
         

  20. Determine the L1 VM's alias IP:
         
         ip route show table local
         

  21. Verify that the output is similar to the following. For this example, there are two IP addresses associated with the L2 VM's `eth0` ethernet device. The first, `10.128.0.2`, is the L2 VM's primary IP address, which is returned by `sudo ifconfig -a`. The second, `10.128.0.13`, is the L2 VM's alias IP address.
         
         local 10.128.0.2 dev eth0 proto kernel scope host src 10.128.0.2
         broadcast 10.128.0.2 dev eth0 proto kernel scope link src 10.128.0.2
         local 10.128.0.13/30 dev eth0 proto 66 scope host
         broadcast 127.0.0.0 dev lo proto kernel scope link src 127.0.0.1
         local 127.0.0.0/8 dev lo proto kernel scope host src 127.0.0.1
         local 127.0.0.1 dev lo proto kernel scope host src 127.0.0.1
         broadcast 127.255.255.255 dev lo proto kernel scope link src 127.0.0.1
         broadcast 192.168.122.0 dev virbr0 proto kernel scope link src
         192.168.122.1 linkdown
         local 192.168.122.1 dev virbr0 proto kernel scope host src 192.168.122.1
         broadcast 192.168.122.255 dev virbr0 proto kernel scope link src
         192.168.122.1 linkdown
         

  22. Run the following commands to forward traffic from the `10.128.0.13` example alias IP to the `192.168.122.89` example IP for the L2 VM:
         
         echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
         sudo iptables -t nat -A PREROUTING -d 10.128.0.13 -j DNAT --to-destination 192.168.122.89
         sudo iptables -t nat -A POSTROUTING -s 192.168.122.89 -j MASQUERADE
         sudo iptables -A INPUT -p udp -j ACCEPT
         sudo iptables -A FORWARD -p tcp -j ACCEPT
         sudo iptables -A OUTPUT -p tcp -j ACCEPT
         sudo iptables -A OUTPUT -p udp -j ACCEPT
         

For information about troubleshooting `iptables`, see [`iptables` not forwarding traffic](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-nested-vms#iptables_not_forwarding_traffic).

  23. Verify L2 VM access from outside the L1 VM by logging onto another VM that is on the same network as the L1 VM, and making a `curl` request to the alias IP, replacing the IP address below with the L2 VM's alias IP:
         
         user@another-vm:~$ curl 10.128.0.13:8000
         

  24. Verify that the `curl` response is similar to the following:
         
         <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"><html>
         <title>Directory listing for /</title>
         <body>
         <h2>Directory listing for /</h2>
         <hr>
         <ol>
         <li><a href=".aptitude/">.aptitude/</a>
         <li><a href=".bashrc">.bashrc</a>
         <li><a href=".profile">.profile</a>
         </ol>
         <hr>
         </body>
         </html>
         




## What's next

  * [Troubleshoot nested virtualization](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-nested-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
