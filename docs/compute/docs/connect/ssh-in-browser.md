---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-in-browser/
title: SSH-in-browser \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:34.347333+00:00
---

# SSH-in-browser  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-in-browser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  SSH-in-browser Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

You can connect to Compute Engine instances from within the Google Cloud console by using the SSH-in-browser tool. SSH-in-browser doesn't require any additional extensions or software. SSH-in-browser supports connections to instances that store [SSH keys in metadata](https://docs.cloud.google.com/compute/docs/instances/ssh#metadata), instances that use [OS Login](https://docs.cloud.google.com/compute/docs/instances/ssh#os-login), and instances that use [IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#tunneling_ssh_connections).

Each time you connect to an instance by using SSH-in-browser, Compute Engine creates an ephemeral SSH key pair and sets a username for your connection. Your username and the location where Compute Engine stores your SSH keys depend on whether you use SSH keys stored in metadata, or OS Login. For more information see [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh).

## Requirements

To use SSH-in-browser, your environment must meet the following requirements:

  * Google Cloud console must be running in a [supported web browser](https://docs.cloud.google.com/compute/docs/console#supported_browsers).
  * The instance you're connecting to must have the [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) [installed and running](https://docs.cloud.google.com/compute/docs/images/install-guest-environment). The guest environment is pre-installed on instances that you create from [Google-provided public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).
  * Your network must meet the following requirements:

    * HTTPS proxies and security devices must not decrypt and re-encrypt traffic using their own TLS certificate, for example, to perform TLS inspection.
    * The network must allow traffic to and from hostnames ending in `google.com`, `gstatic.com`, or `googleapis.com`.
    * The network must allow packets to be sent to the IP addresses for the default domains.
    * To connect to instances through their external IP address, the Virtual Private Cloud (VPC) must [allow TCP ingress traffic for IP range `0.0.0.0/0`](https://docs.cloud.google.com/vpc/docs/using-firewalls#common-use-cases-allow-ssh).
    * To connect to instances that only have internal IP addresses, you must [configure firewall rules](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#create-firewall-rule) to allow IAP for TCP forwarding.



## Limitations

  * **Not supported within VPC Service Controls perimeters.** SSH-in-browser isn't supported within VPC Service Controls perimeters. Use the gcloud CLI instead. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) or [Connecting to a serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#gcloud_2), depending on your use case.
  * **Slow SSH key transfer times.** SSH-in-browser key transfer times range from 2 to 25 seconds.
  * **Intermittent disconnects.** At this time, we don't offer a specific Service Level Agreement (SLA) for connection lifetimes. If you plan to keep the terminal window open for an extended period of time, use terminal multiplexers like [tmux](https://tmux.github.io/) or [screen](http://www.gnu.org/software/screen/).
  * **File transfer might be slow for large files.** If you experience slow file transfer times, use the [`gcloud compute scp` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp) instead of SSH-in-browser.



## Use SSH-in-browser

The following sections describe how to use SSH-in-browser to connect to, disconnect from, and manage files on your instances.

### Connect to instances

To connect to an instance using SSH-in-browser, do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. In the list of instances, click the **SSH** button in the row of the instance that you want to connect to.




After you click **SSH** , SSH-in-browser opens in a new window.

If your instance has one of the following configurations, then review its section for more information about how to connect:

  * Instances that don't have public IP addresses
  * Instances that use OS Login and user-uploaded SSH keys
  * Cloud TPU instances



#### Connect to instances that don't have public IP addresses

When you use SSH-in-browser to connect to an instance that has only an internal IP address, SSH-in-browser uses [IAP TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#tunneling_ssh_connections).

#### Connect to instances with user-uploaded SSH keys

SSH-in-browser supports connections with user-uploaded ECDSA SSH keys for instances that use [OS Login](https://docs.cloud.google.com/compute/docs/oslogin).

To connect to an instance with a [user-uploaded SSH key](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login), do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. In the list of instances, click the arrow_drop_down drop-down next to the **SSH** button of the instance that you want to connect to.

  3. Click **Open in browser window using provided private SSH key**.

The SSH-in-browser window opens.

  4. Click **Connect with SSH key file** and choose the private key that is associated with the public key in your OS Login profile. 




#### Connect to Cloud TPU instances

To connect to a Cloud TPU, review [Connect to a Cloud TPU instance](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm#tpu-connect).

### Disconnect from instances

To disconnect from an instance and terminate an SSH-in-browser session, run the `exit` command.

The SSH-in-browser window also closes if you use your workstation's keyboard shortcut for closing windows:

###  Windows and Linux 

`Ctrl+W`

###  macOS 

`Cmd+W`

###  Chrome OS 

`Ctrl+Shift+W`

### Scroll through the terminal

You can scroll the terminal using your mouse wheel or trackpad. Alternatively, you can use the keyboard shortcuts for your workstation's operating system.

###  Windows and Linux 

To scroll up, use `Ctrl+Shift+PageUp`. To scroll down, use `Ctrl+Shift+PageDn`.

###  macOS 

To scroll up, use `Fn+Shift+Up`. To scroll down, use `Fn+Shift+Down`.

###  Chrome OS 

To scroll up, use `Alt+Shift+Up`. To scroll down, use `Alt+Shift+Down`.

### Copy and paste text

The default copy option for SSH-in-browser is **Copy on select**. Any text that you highlight in SSH-in-browser is copied. You can alternatively copy and paste the text using the keyboard shortcuts for your workstation's operating system.

###  Windows and Linux 

To copy text, use `Ctrl+C`. To paste text, use `Ctrl+V`.

###  macOS 

To copy text, use `Cmd+C`. To paste text, use `Cmd+V`.

###  Chrome OS 

There is no keyboard shortcut to copy files. To paste text, use `Ctrl+Shift+V`.

If you encounter problems while copying and pasting large blocks of text, then use file transfer instead.

### Transfer files

To learn how to transfer files to and from instances using SSH-in-browser, review [Transfer files using SSH-in-browser](https://docs.cloud.google.com/compute/docs/instances/transfer-files#transferbrowser).

## Troubleshoot

To debug methods and resolve common SSH errors—specifically if the SSH web console fails to connect or gets stuck on a loading screen—see the dedicated [Troubleshooting SSH-in-browser](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors#ssh-in-browser-errors) guidances.

For comprehensive diagnostics, see [Troubleshooting SSH](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
