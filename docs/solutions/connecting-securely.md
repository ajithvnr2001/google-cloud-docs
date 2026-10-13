---
url: https://docs.cloud.google.com/solutions/connecting-securely/
title: Securely connecting to VM instances \u00a0|\u00a0 Solutions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:43.290433+00:00
---

# Securely connecting to VM instances  |  Solutions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/solutions/connecting-securely/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Solutions ](https://docs.cloud.google.com/solutions)



Send feedback 

#  Securely connecting to VM instances Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices for securely connecting to Compute Engine virtual machine (VM) instances, including storing host keys by enabling guest attributes and preventing VMs from being reached from the public internet.

**Note:** When a user connects to a VM, that user can use all of the IAM permissions granted to the service account attached to the VM. 

## Storing host keys by enabling guest attributes

A host key is a key pair that identifies a particular host or machine. When you connect to a remote host, the host key is used to verify that you're connecting to the intended machine.

If you use [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to connect to your Linux VMs, you can add a layer of security by storing your host keys as guest attributes.

Storing SSH host keys as guest attributes improves the security of your connections by helping to protect against vulnerabilities such as man-in-the-middle (MITM) attacks. On the initial boot of a VM, if guest attributes are enabled, Compute Engine stores your generated host keys as guest attributes. After that, Compute Engine uses these stored host keys to verify all subsequent connections to the VM.

Host keys can be stored as guest attributes on the following public operating system images:

  * Debian
  * Ubuntu
  * Red Hat Enterprise Linux (RHEL)
  * CentOS
  * SUSE Linux Enterprise Server (SLES)



To write host keys to guest attributes, you must enable guest attributes before you boot the VM for the first time. You can enable guest attributes either on select VMs during VM creation or on your entire project.

After you enable guest attributes for a project or VM, the Guest OS agent automatically publishes the host key as a guest attribute. If you use `gcloud compute ssh` instead of a plain SSH client, then the gcloud CLI automatically reads the attributes and updates the `known_hosts` file the next time you connect.

To store host keys as guest attributes, complete the following steps:

  1. Before you boot your VM for the first time, [enable guest attributes](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#enable_attributes) either on select VMs during VM creation or on your entire project.

  2. Connect to your VM by using [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh).

     1. Ensure that you have the latest version of the Google Cloud CLI:
            
            gcloud components update
            

     2. Connect to the VM:
            
            gcloud compute ssh --project=PROJECT_ID \
             --zone=ZONE \
             VM_NAME
            

Replace the following:

        * `PROJECT_ID`: the ID of the project that contains the VM
        * `ZONE`: the name of the zone in which the VM is located
        * `VM_NAME`: the name of the VM

If you have [set default properties](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties) for the Google Cloud CLI, you can omit the `--project` and `--zone` flags from this command. For example:
    
    gcloud compute ssh VM_NAME
    

     3. Review the startup message. For example, a Debian operating system might display the following message:
            
            Writing 3 keys to YOUR_HOME_DIRECTORY/.ssh/google_compute_known_hosts
            Linux host-key-2 4.9.0-9-amd64 #1 SMP Debian 4.9.168-1+deb9u3 (2019-06-16) x86_64
            




To confirm that host keys are stored as guest attributes for this VM, either review the host key values to verify that SSH keys are written to guest attributes for the VM (Option 1), or review the serial port for the presence of host keys (Option 2):

**Option 1: Review the host key values**

You can use the Google Cloud CLI to verify that SSH keys are written to guest attributes:
    
    
    gcloud compute instances get-guest-attributes VM_NAME \
      --query-path="hostkeys/" \
      --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM
  * `ZONE`: the name of the zone in which the VM is located



The output is similar to the following:
    
    
    NAMESPACE  KEY                  VALUE
    hostkeys   ecdsa-sha2-nistp256  AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBJAGpTm
                                    V3mFxBTHK1NIu9a7kVQWaHsZVaFUsqF8cLxQRQ+N96/Djiiuz1tucHQ8vBTJI=
    hostkeys   ssh-ed25519          AAAAC3NzaC1lZDI1NTE5AAAAIM/WYBn3jIEW5t3BZumx0X/Htm61J6S9FcU8L
    hostkeys   ssh-rsa              AAAAB3NzaC1yc2EAAAADAQABAAABAQDU3jReR/MoSttlWYfauW6qEqS2dhe5
                                    Zdd3guYk2H7ZyxblNuP56nOl/IMuniVmsFa9v8W6MExViu6G5Cy4iIesot09
                                    1hsgkG0U7sbWrXM10PQ8pnpI3B5arplCiEMhRtXy64rlW3Nx156bLdcxv5l+
                                    7Unu4IviKlY43uqqwSyTv+V8q4ThpQ9dNbk1Gg838+KzazljzHahtbIaE1rm
                                    I0L1lUqKiKLSLKuBgrI2Y/WSuqvqGEz+bMH7Ri4ht+7sAwykph6FbOgKqoBI
                                    hVWBo38/Na/gEuvtmgULUwK+xy9zWg9k8k/Qtihc6El9GD9y

**Option 2: Review the serial port**

  1. View the [serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#viewing_serial_port_output).
  2. Select **serial port 1**.
  3. Search for the following message:
         
         INFO Wrote ssh-rsa host key to guest attributes

If your image uses a supported operating system but the guest attributes setting wasn't enabled before the first VM boot, you might see the following message:
         
         Unable to write ssh-rsa host key to guest attributes

This means that host keys aren't stored as guest attributes for this VM. If you want to store host keys for additional VMs that you plan to create, enable guest attributes before the first boot of the VM.




## Preventing VMs from being reached from the public internet

When developing projects on Compute Engine, there are a variety of scenarios in which you want to keep the VMs from being reached from the public internet:

  * Web services are still under development and not ready to be exposed to external users because they are feature incomplete or have not yet been configured with HTTPS.
  * The VM might be providing services designed to be consumed only by other VMs in the project.
  * VMs should only be reached through dedicated interconnect options from company offices or data centers.



Even when a service is intentionally internet-facing, it is important that communication with the service be restricted to the target user groups, and occur over secure channels, such as SSH or HTTPS, to protect sensitive information.

This article demonstrates several methods for securing communications with VMs with external IP addresses and VMs without external IP addresses. Whether or not you secure communications with these methods, Google Cloud always allows communication between a VM instance and its corresponding metadata server. For more information, see [always allowed traffic](https://docs.cloud.google.com/vpc/docs/firewalls#alwaysallowed).

### Protecting services on machines with external IP addresses

When VMs have a public IP address, it is important that only the services and traffic you intend to be exposed are reachable, and for those that are exposed, any sensitive information is secured in transit. There are several methods for protecting services on VMs with external IP addresses explained in this document, including firewalls, HTTPS and SSL, port forwarding over SSH, and SOCKS proxy over SSH.

#### Firewalls

Your first line of defense is to restrict who can reach the VM using [firewalls](https://docs.cloud.google.com/compute/docs/vpc/firewalls). By creating firewall rules, you can restrict all traffic to a network or target machines on a given set of ports to specific source IP addresses.

Firewalls are not a standalone solution. Restricting traffic to specific source IPs does not protect sensitive information, such as login credentials, commands that create or destroy resources or files, or logs. When running a web service on a publicly-accessible machine, such as a Compute Engine VM with an external IP, you must encrypt all communication between your host and the deployed VM to ensure proper security.

In addition, firewalls aren't always the appropriate solution. For example, firewalls are not ideal for development environments that do not have static IP addresses, such as roaming laptops.

#### HTTPS and SSL

For production web systems, you should configure HTTPS/SSL. HTTPS/SSL can be set up either by setting up a VM to terminate HTTPS or by configuring HTTPS load balancing. HTTPS/SSL does involve some initial complexity, requiring you to perform the following tasks:

  * Register a domain name.
  * Acquire an SSL certificate from a certificate authority.
  * [Register the certificate with your HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) and its connected VMs, or configure an SSL-terminated web server or proxy on one or more Compute Engine VMs.

**Note:** The steps required to set up SSL for a domain directly on a Compute Engine VM depend on the web server that you are using. For details, see the documentation for your web server. An alternative to setting up SSL is to use a different security method, such as port forwarding or SOCKS proxy.

#### Port forwarding over SSH

You can use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) to start a server on a given local port that forwards all traffic to a remote host over an SSH connection.

First, take note of the VM and port that are providing the service to which you would like to establish a secure connection. Next, run the following command:
    
    
    gcloud compute ssh VM_NAME \
        --project PROJECT_ID \
        --zone ZONE \
        -- -NL LOCAL_PORT:localhost:REMOTE_PORT
    

**Note:** If using Cloud Shell to run the command, add a `-4` to the SSH flags to use IPv4 to connect. Example: `-- -4 -NL LOCAL_PORT:localhost:REMOTE_PORT`

Replace the following:

  * `VM_NAME` is the name of the VM to which you'd like to connect.
  * `PROJECT_ID` is your [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: The zone in which your VM is running, for example, `us-central1-a`.
  * `LOCAL_PORT`: The local port you're listening on, for example, `2222`.
  * `REMOTE_PORT`: The remote port you're connecting to, for example `8888`.



For example, if you specify a local port of '2222' and a remote port of '8888', and you open <http://localhost:2222/> in your browser, the HTTP connection uses the SSH tunnel that you created to your remote host to connect to the specified VM using SSH. The HTTP connection will then use the SSH tunnel to connect to port `8888` on the same machine, but over an encrypted, secure SSH connection.

The `gcloud` command creates and maintains an SSH connection while the SSH session is active. As soon as you exit the SSH session, port forwarding using http://`VM_NAME`:`LOCAL_PORT` stops working.

To create more than one port forwarding rule, you can specify multiple rules on a single command line by repeating the flags:
    
    
    gcloud compute ssh VM_NAME \
        --project PROJECT_ID \
        --zone ZONE \
        -- -NL LOCAL_PORT:localhost:REMOTE_PORT \
        -- -NL LOCAL_PORT:localhost:REMOTE_PORT
    

**Note:** If using Cloud Shell to run the command, add a `-4` to the SSH flags to use IPv4 to connect. Example: `-- -4 -NL LOCAL_PORT:localhost:REMOTE_PORT`

Alternatively, you can run a new `gcloud` command each time to create a separate tunnel. Note that you cannot add or remove port forwarding from an existing connection without exiting and re-establishing the connection from scratch.

#### SOCKS proxy over SSH

If you want to connect to a number of different hosts in your cloud deployment, the easiest way to do so is to change your browser to do the lookups directly from your [network](https://docs.cloud.google.com/compute/docs/vpc). This approach lets you use the short name of the hosts instead of looking up each host's IP address, opening up ports for each service, or creating an SSH tunnel for each host/port pair.

The approach that you use here is as follows:

  1. Set up a single SSH tunnel to one of the hosts on the network, and create a SOCKS proxy on that host.
  2. Change the browser configuration to do all the lookups using that SOCKS proxy host.



Note that because you are tunneling _all_ traffic using that host, avoid using that browser or that specific profile to browse the web because you need to dedicate that bandwidth to your cloud service. In general, you might want to use a separate browser profile and switch to it when necessary.

##### Start the SOCKS proxy

To start your SOCKS proxy, run the following command:
    
    
    gcloud compute ssh VM_NAME \
        --project PROJECT_ID \
        --zone ZONE
        --ssh-flag="-D" \
        --ssh-flag="LOCAL_PORT" \
        --ssh-flag="-N"
    

Replace the following:

  * `VM_NAME`: The name of the VM to which you would like to connect.
  * `PROJECT_ID`: Your [Google Cloud project ID](https://docs.cloud.google.com/storage/docs/projects#projectid-using).
  * `ZONE`: The zone in which your VM is running, for example, `us-central1-a`.
  * `LOCAL_PORT`: The local port you're listening on, for example, `1080`.



Note that, in this case, you don't need to specify a remote port. Because a SOCKS proxy does not bind to any specific remote port, any connection you make using the SOCKS proxy will be resolved relative to the host you connect to.

By using a SOCKS proxy, you can connect to any VM that shares a Compute Engine network with your proxy VM by using the VM's short name. In addition, you can connect to any port on a given VM.

This approach is much more flexible than the simple port-forwarding method, but will also require you to change the settings in your web browser to utilize the proxy.

Next, configure either Chrome or Firefox to use the proxy.

###  Chrome 

Chrome uses system-wide proxy settings by default, so you need to specify a different proxy using command-line flags. Launching Chrome by default creates a VM of an already-running profile, so to enable you to run multiple copies of Chrome simultaneously, one that's using the proxy and others that are not, you need a new profile.

Launch Chrome using a new profile. It will be created automatically if it does not exist.

**Linux:**
    
    
    /usr/bin/google-chrome \
        --user-data-dir="$HOME/chrome-proxy-profile" \
        --proxy-server="socks5://localhost:1080"
    

**macOS:**
    
    
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
        --user-data-dir="$HOME/chrome-proxy-profile" \
        --proxy-server="socks5://localhost:1080"
    

**Windows:**
    
    
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" ^
        --user-data-dir="%USERPROFILE%\chrome-proxy-profile" ^
        --proxy-server="socks5://localhost:1080"
    

Set the localhost port to the same value that you used in the `gcloud` command earlier (`1080` in our example).

###  Firefox 

Before changing these settings, you might want to [create a new Firefox profile](https://support.mozilla.org/en-US/kb/profile-manager-create-and-remove-firefox-profiles). Otherwise, it will affect all VMs of Firefox to use that host as a proxy, which is likely not what you want.

After you have Firefox running with a separate profile, you can set up the SOCKS proxy:

  1. Open **Preferences**.
  2. Click **Advanced** > **Networks** > **Settings** to open the **Connection Settings** dialog.
  3. Choose the option **Manual proxy configuration**. 
     1. In the **SOCKS Host** section, fill in `localhost` as the host and the port you selected when you ran the `gcloud` command earlier.
     2. Choose **SOCKS v5**.
     3. Check the box **Remote DNS**.
     4. Leave all other entries blank.
  4. Click **OK** and close the **Preferences** dialog box.



### Connecting to VMs without external IP addresses

When VMs do not have external IP addresses (including VMs that are backends for HTTPS and SSL proxy load balancers) they can only be reached by the following:

  * Other VMs on the network
  * Identity-Aware Proxy's TCP forwarding feature
  * The [metadata server](https://docs.cloud.google.com/vpc/docs/firewalls#gcp-metadata-server)
  * Google Cloud SDK
  * Managed VPN gateway



You can provision VMs in your network to act as trusted relays for inbound connections, also known as bastion hosts. Additionally, you can configure a Cloud NAT for outbound network traffic, or set up the interactive serial console to maintain or troubleshoot VMs without external IP addresses.

#### Bastion hosts

[Bastion hosts](https://wikipedia.org/wiki/Bastion_host) provide an external facing point of entry into a network containing private network instances, as illustrated in the following diagram.

![Architecture of Bastion hosts acting as the external-facing point of entry for a network of private instances.](https://docs.cloud.google.com/static/solutions/images/bastion.png)

This host can provide a single point of fortification or audit and can be started and stopped to enable or disable inbound SSH. By using a bastion host, you can connect to a VM that does not have an external IP address. This approach allows you to connect to a development environment or manage the database instance for your external application, for example, without configuring additional firewall rules.

A complete hardening of a bastion host is outside the scope of this article, but some initial steps taken can include:

  * Limit the CIDR range of source IPs that can communicate with the bastion.
  * Configure firewall rules to allow SSH traffic to private VMs from only the bastion host.



By default, SSH on VMs is configured to use private keys for authentication. When using a bastion host, you log into the bastion host first, and then into your target private VM. Because of this two-step login, which is why bastion hosts are sometimes called "jump servers," you should use `ssh` forwarding instead of storing the target machine's private key on the bastion host as a way of reaching the target machine. You need to do this even if using the same key pair for both bastion and target VMs because the bastion has direct access to only the public half of the key pair.

To learn how to use a bastion host instance to connect to other VMs on your Google Cloud network, see [Connect to Linux VMs using a bastion host](https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host).

To learn how to use `ssh` forwarding and other methods to connect to VMs that do not have an external IP address, see see [Connecting to VMs that do not have external IP addresses](https://docs.cloud.google.com/compute/docs/instances/connecting-advanced#sshbetweeninstances).

#### IAP for TCP forwarding

Using SSH with IAP's TCP forwarding feature wraps an SSH connection inside HTTPS. IAP's TCP forwarding feature then sends it to the remote VM.

To learn how to connect to a remote VM with IAP, see [Connect to Linux VMs using Identity-Aware Proxy](https://docs.cloud.google.com/compute/docs/connect/ssh-using-iap).

#### VPN

Cloud VPN lets you connect your existing network to your Google Cloud network by using an IPsec connection to a VPN gateway device. This allows direct routing of traffic from your premises to the private IP interfaces of Compute Engine VMs. Traffic is encrypted as it transits over public links to Google.

For details on setting up, configuring, and using VPN with Compute Engine, see the [Cloud VPN documentation](https://docs.cloud.google.com/network-connectivity/docs/vpn).

To learn how to connect to VMs on your Google Cloud network through an existing VPN rather than through external IP addresses of VMs, read [Connect to Linux VMs using Cloud VPN or Cloud Interconnect](https://docs.cloud.google.com/compute/docs/connect/ssh-using-vpn).

#### Outbound traffic using Cloud NAT

When a VM does not have an external IP address assigned, it cannot make direct connections to external services, including other Google Cloud services. To allow these VMs to reach services on the public internet, you can set up and configure [Cloud NAT](https://docs.cloud.google.com/nat/docs), which can route traffic on behalf of any VM on the network. Do not consider a single VM to be highly available or able to support high traffic throughput for multiple VMs.

#### Interactive serial console access

When a VM doesn't have an external IP address, you might still need to interact with the VM for troubleshooting or maintenance purposes. Setting up a Bastion host, as discussed earlier, is one option but might require more setup than worthwhile for your needs. If you want to troubleshoot a VM without an external IP address, consider [enabling interactive access on the serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console), which allows you to interact with a VM's serial console using SSH and run commands against the serial console.

To learn more, read [Interacting with the Serial Console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console).

#### HTTPS and SSL proxy load balancers

VMs that are backends for HTTPS and SSL proxy load balancers do not have to have external IP addresses to be accessed through the load balancer. To access these resources directly requires the use of methods listed in the section Connecting to VMs without external IP addresses.

To learn more, read the [load balancing documentation](https://docs.cloud.google.com/load-balancing/docs) for those load balancers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
