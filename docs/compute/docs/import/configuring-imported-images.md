---
url: https://docs.cloud.google.com/compute/docs/import/configuring-imported-images/
title: Manually configure imported disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:52.109723+00:00
---

# Manually configure imported disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/import/configuring-imported-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manually configure imported disks Stay organized with collections  Save and categorize content based on your preferences. 

After you [manually import a virtual disk](https://docs.cloud.google.com/compute/docs/import/import-existing-image) to Compute Engine, you need to optimize those images so they can use features specific to the Compute Engine environment.

## Contents

## Install the Compute Engine guest environment

You must install the [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) before you can use key features of Compute Engine. To find out when you need to manually install the guest environment, see [when to manually install or update the guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment#when-to-install).

[Install the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment) on the running VM instance you created after [manually importing your existing image](https://docs.cloud.google.com/compute/docs/import/import-existing-image). To perform the installation, access the VM instance via SSH with a user account you created before importing it or by [interacting with the Serial Console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console).

**Important:** Install the guest environment **after** you have imported your existing image. The guest environment makes configuration changes to the instance that are specific to Compute Engine.**Important:** Failure to install the guest environment on a VM instance created from an imported image results in key features of Compute Engine being unavailable to the instance. For example, you won't be able to use all of the methods for [connecting to Linux instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance), and the instance might be unable to participate in [load balancing](https://docs.cloud.google.com/compute/docs/load-balancing) configurations.

## Configure your imported image for Compute Engine

You can run your boot disk image in Compute Engine without additional changes, but you can also further optimize the image so that it runs optimally within Compute Engine and has access to all Compute Engine features.

  * Edit the `ntp.conf` file to include only the `server metadata.google.internal iburst` Google NTP server entry.

  * Set the timezone to UTC:
        
        sudo ln -sf /usr/share/zoneinfo/UTC /etc/localtime

  * To ensure high performance network capability, use the following recommended network configurations:

    * Use the [ISC DHCP client](http://www.isc.org/downloads/dhcp/).
    * Set the DHCP MTU to the network MTU. The Compute Engine DHCP server serves this parameter as the `interface-mtu` option, which most clients respect. For more information about network MTUs, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).
    * If you don't plan to [configure IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address), disable IPv6.
    * Remove persistent network rules to prevent the instance from remembering MAC addresses. For example:
          
          rm -f /etc/udev/rules.d/70-persistent-net.rules

    * Disable the operating system firewall unless you have specific requirements not supported by Compute Engine Firewall Rules. Compute Engine provides a firewall for inbound and outbound traffic. For more information about firewalls, see [Firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls).

  * To ensure high performance network and disk capability, disable or remove the `irqbalance` daemon. This daemon does not correctly balance IRQ requests for the guest operating systems on virtual machine (VM) instances. Instead, use the scripts that are part of the guest environment to correctly balance IRQ settings for virtual CPUs.

  * Configure SSH access to the base image:

    * Disable root ssh login.
    * Disable password authentication.
    * Disable host-based authentication.
    * Enable strict, host-key checking.
    * Use `ServerAliveInterval` to keep connections open.
    * Remove SSH keys from your image so that others can't access the public or private keys in your image. Instead, use Compute Engine to [manage access to instances](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).

    * Edit the `/etc/ssh/ssh_config` file to use the following configuration:
          
          Host *
          Protocol 2
          ForwardAgent no
          ForwardX11 no
          HostbasedAuthentication no
          StrictHostKeyChecking no
          Ciphers aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,aes128-cbc,3des-cbc
          Tunnel no
          
          # Compute Engine times out connections after 10 minutes of inactivity.
          # Keep alive ssh connections by sending a packet every 7 minutes.
          ServerAliveInterval 420
          

    * Edit the `/etc/ssh/sshd_config` file to use the following configuration:
          
          # Disable PasswordAuthentication because ssh keys are more secure.
          PasswordAuthentication no
          
          # Disable root login. Using sudo provides better auditing.
          PermitRootLogin no
          
          PermitTunnel no
          AllowTcpForwarding yes
          X11Forwarding no
          
          # Compute Engine times out connections after 10 minutes of inactivity.
          # Keep alive ssh connections by sending a packet every 7 minutes.
          ClientAliveInterval 420
          




After you configure and optimize your boot disk on Compute Engine, create an image from that boot disk so that you can create instances from a fully-optimized version of the image rather than having to configure each instance every time you create it.

## Configure security best practices

You should always provide a secure operating system environment, but it can be difficult to strike a balance between a secure and an accessible environment. Virtual machines that are vulnerable to attack can consume expensive resources. Google strongly recommends that your images comply with the following security best practices:

  * Minimize the amount of software installed by default (for example, perform a minimal install of the OS).
  * Enable automatic updates.
  * By default, disable all network services except for SSH, DHCP, and NTPD. You can allow a mail server, such as Postfix, to run if it is only accepting connections from localhost.
  * Do not allow externally listening ports except for sshd.
  * Install the [denyhosts](http://denyhosts.sourceforge.net/faq.html#1_0) package to help prevent SSH brute-force login attempts.
  * Remove all unnecessary non-user accounts from the default install.
  * In `/etc/passwd`, set the shell of all non-user accounts to `/sbin/nologin` or `/usr/sbin/nologin` (depending on where your OS installed nologin).
  * Configure your OS to use salted SHA512 for passwords in `/etc/shadow`.
  * Set up and configure [pam_cracklib](http://linux.die.net/man/8/pam_cracklib) for strong passwords.
  * Set up and configure [pam_tally](http://linux.die.net/man/8/pam_tally) to lock out accounts for 5 minutes after 3 failures.
  * In `/etc/shadow`, configure the root account to be locked by default. Run the following command to lock the root account:
        
        usermod -L root

  * Deny root in `/etc/ssh/sshd_config` by adding the following line:
        
        PermitRootLogin no

  * Create [AppArmor](https://www.kernel.org/doc/html/latest/admin-guide/LSM/apparmor.html) or [SELinux](http://selinuxproject.org/page/Main_Page) profiles for all default running network-facing services.

  * Use file system capabilities where possible to remove the need for the S*ID bit and to provide more granular control.

  * Enable compiler and runtime exploit mitigations when compiling network-facing software. For example, here are some of the mitigations that the [GNU Compiler Collection (GCC)](http://gcc.gnu.org/) offers and how to enable them:

    * Stack smash protection: Enable this with `-fstack-protector`. By default, this option protects functions with a stack-allocated buffer longer than eight bytes. To increase protection by covering functions with buffers of at least four bytes, add `--param=ssp-buffer-size=4`.
    * Address space layout randomization (ASLR): Enable this by building a position-independent executable with `-fPIC -pie`.
    * Glibc protections: Enable these protections with `-D_FORTIFY_SOURCE=2`.
    * Global Offset Table (GOT) protection: Enable this runtime loader feature with `-Wl,-z,relro,-z,now`.
    * Compile-time errors for missing format strings: `-Wformat -Wformat-security -Werror=format-security`
  * Disable [`CAP_SYS_MODULE`](http://man7.org/linux/man-pages/man7/capabilities.7.html), which allows for loading and unloading of kernel modules. To disable this feature, edit the `/etc/sysctl.conf` file and include the following setting:
        
        kernel.modules_disabled = 1

  * Remove the [kernel symbol table](http://en.wikipedia.org/wiki/System.map):
        
        sudo rm /boot/System.map




## What's next

  * After your image is ready for production, [create a final version](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) of that custom image and [include the image in an image family](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#setting_families) so that you can easily manage updated versions of the custom image.
  * Learn how to [start an instance from an image](https://docs.cloud.google.com/compute/docs/instances/creating-and-starting-an-instance#startinginstancwithimage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
