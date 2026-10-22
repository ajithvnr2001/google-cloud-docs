---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/post-quantum-ssh/
title: Best practices for using post-quantum SSH \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:35.628254+00:00
---

# Best practices for using post-quantum SSH  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/post-quantum-ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for using post-quantum SSH Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes best practices for configuring your workstation and Compute Engine virtual machine (VM) instances to use post-quantum key exchange algorithms for SSH connections.

To learn more about how SSH connections work in Compute Engine, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh). To learn about managing SSH access with IAM, see [About OS Login](https://docs.cloud.google.com/compute/docs/oslogin).

The following sections describe post-quantum cryptography in the context of SSH:

  * Understand the threat of capture-now, decrypt-later attacks
  * Understand the scope of post-quantum protection in SSH



The following sections contain best practices that can help you protect SSH connections against future quantum computing threats:

  * Configure your SSH client to prefer or require post-quantum algorithms
  * Configure your VM for post-quantum key exchange
  * Verify the negotiated key exchange algorithm



## Understand the threat of capture-now, decrypt-later attacks

Classical public-key cryptography (such as RSA and elliptic-curve cryptography) is theoretically vulnerable to attack by quantum computers. Although large-scale quantum computers don't exist yet, adversaries can capture and store encrypted network traffic today with the goal of decrypting it later when a sufficiently capable quantum computer becomes available. This is known as a _capture-now, decrypt-later_ attack.

To protect against this threat, OpenSSH and other modern SSH clients support _post-quantum cryptography_ (_PQC_) key exchange methods. These methods use hybrid key exchange algorithms that combine a post-quantum algorithm with a classical algorithm (such as X25519). As long as either algorithm remains secure, the session's encryption key cannot be derived by an eavesdropper.

The following hybrid post-quantum key exchange algorithms are supported in modern SSH implementations:

  * **`sntrup761x25519-sha512@openssh.com`** : A hybrid of Streamlined NTRU Prime 761 and X25519. Supported in OpenSSH 9.0 and later, and PuTTY 0.78 and later.
  * **`mlkem768x25519-sha256`** : A hybrid of the NIST-standardized ML-KEM-768 (formerly CRYSTALS-Kyber) and X25519. Supported in OpenSSH 10.0 and later, and PuTTY 0.83 and later. `mlkem768x25519-sha256` is the current preferred post-quantum key exchange algorithm for SSH.



## Understand the scope of post-quantum protection in SSH

An SSH connection involves three cryptographic phases:

  1. **Key exchange (`KexAlgorithms`)**: The client and server establish a shared symmetric secret. When you use a post-quantum key exchange algorithm, this shared secret is protected from decryption by quantum computers.
  2. **User and host authentication** : The client verifies the server host key, and the server verifies the user's SSH key or certificate. Standard OpenSSH doesn't yet use post-quantum signature algorithms for user authentication, but because authentication occurs _inside_ the encrypted channel established by the key exchange, your credentials and host keys are protected from retroactive decryption.
  3. **Session data encryption (`Ciphers`)**: Once keys are exchanged, the session is encrypted using a symmetric cipher (such as `aes256-gcm@openssh.com` or `chacha20-poly1305@openssh.com`). Symmetric ciphers aren't vulnerable to quantum computing attacks in the way that asymmetric (key exchange) ciphers are.



### How algorithm negotiation works

During the SSH connection handshake, the client sends an ordered list of key exchange algorithms that it supports. The server compares the client's list against its own supported algorithms and selects the first algorithm in the client's list that the server also supports.

Because the **client determines the preference order** , configuring your workstation client to prefer post-quantum algorithms ensures that post-quantum key exchange is used whenever the target VM supports it.

## Configure your SSH client

Configure the SSH client on your workstation to prioritize or enforce post-quantum key exchange algorithms. Complete the steps for your preferred client tool.

###  Console 

**SSH-in-browser** (built into the Google Cloud console) supports and prefers post-quantum key exchange algorithms automatically.

If you connect to your VM using SSH-in-browser, you don't need to configure any settings on your workstation. When the target VM supports post-quantum algorithms, SSH-in-browser automatically negotiates a post-quantum key exchange.

To connect using SSH-in-browser:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of VM instances, click **SSH** in the row of the VM that you want to connect to.




###  gcloud 

The gcloud CLI (`gcloud compute ssh`) uses the OpenSSH client installed on your local workstation.

  1. Verify that your workstation has OpenSSH 9.0 or later installed:
         
         ssh -V
         

If your OpenSSH version is earlier than 9.0, upgrade OpenSSH using your operating system's package manager.

  2. When your workstation runs OpenSSH 9.0 or later, OpenSSH includes post-quantum key exchange in its default algorithm list. When you connect to a compatible VM, the connection negotiates a post-quantum key exchange without additional flags:
         
         gcloud compute ssh <var>VM_NAME</var> --zone=<var>ZONE</var>
         

Replace the following:

     * `<var>VM_NAME</var>`: the name of the VM that you want to connect to.
     * `<var>ZONE</var>`: the zone where the VM is located.



###  OpenSSH client 

If you use the standard OpenSSH client (`ssh`) on Linux, macOS, or Windows:

  1. Verify that your local OpenSSH client version is 9.0 or later:
         
         ssh -V
         

  2. Open or create your user SSH configuration file (`~/.ssh/config` on Linux and macOS, or `%USERPROFILE%\.ssh\config` on Windows).

  3. Add or update the `KexAlgorithms` directive.

     * **To prioritize post-quantum algorithms while allowing classical fallback (recommended)** , add the following configuration:
           
           KexAlgorithms ^mlkem768x25519-sha256,sntrup761x25519-sha512@openssh.com,diffie-hellman-group-exchange-sha256
           

     * **To strictly enforce post-quantum algorithms and reject classical connections** , specify only post-quantum algorithms:
           
           KexAlgorithms mlkem768x25519-sha256,sntrup761x25519-sha512@openssh.com
           

**Caution:** If you strictly enforce post-quantum algorithms on your client, connections to servers that run OpenSSH earlier than 9.0 fail with a `no matching key exchange method found` error. 
  4. Connect to your VM using SSH:
         
         ssh -i <var>PATH_TO_PRIVATE_KEY</var> <var>USERNAME</var>@<var>EXTERNAL_IP</var>
         

Replace the following:

     * `<var>PATH_TO_PRIVATE_KEY</var>`: the path to your private SSH key.
     * `<var>USERNAME</var>`: your username (such as your OS Login username).
     * `<var>EXTERNAL_IP</var>`: the external IP address of the VM.



###  PuTTY app 

If you connect to VMs using PuTTY on Windows:

  1. Ensure that you run PuTTY version 0.78 or later (or version 0.83 or later for ML-KEM support). To check your version, open PuTTY and click **About**. If needed, download the latest version from the [PuTTY download page](https://www.chiark.greenend.org.uk/%7Esgtatham/putty/download.html).

  2. Open PuTTY.

  3. In the **Category** pane, navigate to **Connection** > **SSH** > **Kex**.

  4. In the **Algorithm selection policy** list, locate the post-quantum algorithm:

     * **NTRU Prime / Curve25519 hybrid kex** (available in PuTTY 0.78+)
     * **ML-KEM / Curve25519 hybrid kex** (available in PuTTY 0.83+)
  5. Select the post-quantum algorithm and click **Up** until it is at the top of the list, above classical Diffie-Hellman and ECDH algorithms.

  6. (Optional) To strictly enforce post-quantum algorithms, select each classical algorithm and click **Down** until it is below the **\-- Warn below here --** or **\-- Don't use below here --** divider.

  7. In the **Category** pane, click **Session**.

  8. Under **Saved Sessions** , select your session name and click **Save** to persist your algorithm preference.

  9. Click **Open** to connect to the VM.




## Configure your VM

To use post-quantum key exchange algorithms, your VM's operating system and SSH daemon must support them. Review the compatible operating systems and understand the default behavior before making configuration changes.

### Compatible operating systems

To support post-quantum key exchange, your VM must run an operating system that includes OpenSSH 9.0 or later. The following public Linux images available on Compute Engine include OpenSSH 9.0 or later:

  * **Debian** : Debian 12 (Bookworm) and later
  * **Ubuntu** : Ubuntu 24.04 LTS (Noble Numbat) and later
  * **Fedora** : Fedora 39 and later
  * **Container-Optimized OS** : Milestone 109 and later
  * **Rocky Linux / AlmaLinux** : Version 10 and later



Older operating system releases (such as Ubuntu 22.04 LTS, Debian 11, or RHEL 9) include OpenSSH versions earlier than 9.0 by default and don't support post-quantum key exchange.

### Default behavior

If your VM runs an operating system with OpenSSH 9.0 or later, the OpenSSH server (`sshd`) supports `sntrup761x25519-sha512@openssh.com` by default. VMs running OpenSSH 10.0 or later also support `mlkem768x25519-sha256` by default.

By default, no changes to the VM configuration are required. When a post-quantum capable client connects, the VM automatically negotiates a post-quantum key exchange. At the same time, the VM continues to accept connections from clients that only support classical algorithms.

### Strictly require post-quantum algorithms

If your organization requires post-quantum key exchange for all SSH sessions, you can configure the VM's SSH daemon to accept only post-quantum key exchange algorithms.

**Warning: You risk locking yourself out of your VM.** Configuring your VM to strictly require post-quantum algorithms prevents access from any SSH client that doesn't support them. If your client doesn't support post-quantum key exchange, or if you make an error in the configuration, **you will lose SSH access to the VM**. Before you configure your VM to strictly require post-quantum algorithms: 

  * Ensure that all users, workstations, and automated tools that connect to the VM are using OpenSSH 9.0 or later, or PuTTY 0.78 or later.
  * Review the recovery options in Recover from an SSH lockout before applying changes.



To strictly require post-quantum algorithms on your VM:

  1. Connect to your VM using SSH.

  2. Create a drop-in configuration file in `/etc/ssh/sshd_config.d/`:
         
         sudo bash -c 'cat << 'EOF' > /etc/ssh/sshd_config.d/99-post-quantum-kex.conf
         # Require post-quantum key exchange algorithms only
         KexAlgorithms mlkem768x25519-sha256,sntrup761x25519-sha512@openssh.com
         EOF'
         

  3. Test the SSH daemon configuration for syntax errors:
         
         sudo sshd -t
         

If the command produces errors, check the configuration file before proceeding.

  4. Reload the SSH daemon to apply the change without dropping active sessions:
         
         sudo systemctl reload sshd
         

If your Linux distribution uses `ssh` as the service name, run `sudo systemctl reload ssh` instead.

  5. Keep your current terminal window open, and open a _new_ terminal window to test connecting to the VM. If the new connection succeeds, your VM is successfully configured to require post-quantum algorithms.




### Recover from an SSH lockout

If you configure your VM to strictly require post-quantum algorithms and get locked out because your client doesn't support the required algorithms, use one of the following recovery options:

  1. **Use SSH-in-browser** : Open the Google Cloud console and connect using SSH-in-browser. SSH-in-browser supports post-quantum key exchange and can connect even when post-quantum algorithms are strictly required on the VM. Once connected, remove or modify `/etc/ssh/sshd_config.d/99-post-quantum-kex.conf` and reload `sshd`.
  2. **Use the virtual serial console** : Connect to the VM using the [special administrative console (SAC) or serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console). Log in with your credentials, remove the configuration file, and reload `sshd`.
  3. **Use a startup script** : If interactive access is unavailable: 
     1. In the Google Cloud console, stop the VM.
     2. Edit the VM metadata to add a startup script deleting the `/etc/ssh/sshd_config.d/99-post-quantum-kex.conf` configuration file you previously created, then restarting the SSH server daemon: `startup-script`: `rm -f /etc/ssh/sshd_config.d/99-post-quantum-kex.conf && (systemctl reload ssh || systemctl reload sshd)`
     3. Start the VM. The startup script runs as root and restores classical compatibility.
     4. Remove the startup script from metadata after you regain access.



## Verify the negotiated key exchange algorithm

To confirm that an active SSH connection is using a post-quantum key exchange algorithm, check the connection details from your client.

### Verify using OpenSSH or gcloud CLI

Connect to your VM with verbose output enabled by using the `-v` flag:

  * **Using OpenSSH** :
        
        ssh -v -i <var>PATH_TO_PRIVATE_KEY</var> <var>USERNAME</var>@<var>EXTERNAL_IP</var>
        

  * **Using gcloud CLI** :
        
        gcloud compute ssh <var>VM_NAME</var> --zone=<var>ZONE</var> -- -v
        




Inspect the terminal output during connection establishment. Look for the `kex: algorithm` line:
    
    
    debug1: kex: algorithm: sntrup761x25519-sha512@openssh.com
    

or:
    
    
    debug1: kex: algorithm: mlkem768x25519-sha256
    

If the output lists `sntrup761x25519-sha512` or `mlkem768x25519-sha256`, the connection is protected by post-quantum key exchange. If it lists an algorithm like `curve25519-sha256` or `ecdh-sha2-nistp256`, the connection is using classical key exchange and is still vulnerable to "capture now, decrypt later" attacks.

### Verify using PuTTY

  1. In PuTTY, connect to your VM.
  2. Right-click the PuTTY window title bar and select **Event Log**.
  3. In the **PuTTY Event Log** window, look for the line indicating the key exchange algorithm: 
     * `Using NTRU Prime / Curve25519 hybrid key exchange`
     * `Using ML-KEM / Curve25519 hybrid key exchange`



## What's next

  * Learn more about [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).
  * Review [Best practices for securing SSH access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices).
  * Learn how to [Protect SSH credentials with security keys](https://docs.cloud.google.com/compute/docs/oslogin/security-keys).
  * Learn about [SSH-in-browser features and configuration](https://docs.cloud.google.com/compute/docs/connect/ssh-in-browser).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
