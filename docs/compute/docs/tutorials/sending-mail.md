---
url: https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/
title: Sending email from an instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:11.420025+00:00
---

# Sending email from an instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Sending email from an instance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the options for sending mail from a virtual machine (VM) instance and provides general recommendations on how to set up your instances to send email.

## Using standard email ports

Google Cloud does not place any restrictions on traffic sent to external destination IP addresses using destination TCP ports 587 or 465. The [implied allow egress firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) allows this traffic unless you've created egress deny firewall rules that block it.

Due to the risk of abuse, connections to destination TCP Port 25 are blocked when the destination is external to your VPC network. This includes using SMTP relay with Google Workspace. However, some projects do not have this restriction and do allow external SMTP egress on port 25. For more information, see [Blocked and limited traffic](https://docs.cloud.google.com/vpc/docs/firewalls#blockedtraffic).

**Note:** Subject to Google Cloud firewall rules, connections to destination TCP Port 25 are allowed within your VPC network, a VPC connected using VPC Network Peering, or an on-premises network connected to your VPC network using Cloud VPN tunnels or Cloud Interconnect attachments (VLANs).

## Choosing a third-party email service to use

In addition to using standard email ports, having a trusted third-party email provider such as SendGrid, Mailgun, or Mailjet improves your [IP reputation score](https://sendgrid.com/blog/email-reputation-and-email-engagement-metrics/).

SendGrid, Mailgun, and Mailjet offer a free tier for Compute Engine customers to set up and send email through their servers. If you don't have a Google Workspace account, use these third-party partners to take advantage of features like click tracking, analytics, APIs, and other features to meet your email needs.

Alternatively, if you are familiar with [Google Workspace](https://gsuite.google.com) and are already paying for a Google Workspace account that supports email, you can [set up a relay service to send email through Google Workspace](https://support.google.com/a/answer/176600). Note that Gmail and Google Workspace enforce [limits for email activity](https://support.google.com/a/answer/166852).

If you don't have a Google Workspace account or don't want to use Google Workspace or a third-party mail provider, you can set up your own email server on an instance by using a non-standard port. You can choose any [ephemeral port](https://wikipedia.org/wiki/Ephemeral_port) that isn't blocked by Compute Engine.

  * **To use SendGrid, Mailgun, or Mailjet** : Follow the instructions for [Sending Email using SendGrid](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-sendgrid), [Sending Email using Mailgun](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailgun), or [Sending Email using Mailjet](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailjet).
  * **To use a Google Workspace domain** : Follow the instructions for [SMTP relay service](https://support.google.com/a/answer/2956491) settings in the Google Workspace documentation. SMTP relaying through Google Workspace is only allowed through ports 465 or 587. Port 25 is not supported through Google Workspace.



If you want to use your own email server on a custom port, use the documentation specific to your email service to configure a custom email port.

## Setting up a firewall rule to allow outbound traffic on a custom port

To allow outbound traffic through a custom port, you need to set up a firewall rule. For example, the following steps set up a rule that allows outbound traffic on port 2525. Replace port 2525 with the custom port of your choice.

  1. In the Google Cloud console, go to the **Create a firewall rule** page.

[Go to Create a firewall rule](https://console.cloud.google.com/networking/firewalls/add)

  2. Choose a name for the firewall rule.

  3. Under **Network** , select the network that is hosting the VM instance that you intend to send email messages from.

  4. Under **Direction of traffic** , select **Egress**.

  5. Under **Targets** , choose the appropriate target for this rule. For example, you might choose **Specified target tags** if you want the rule to apply to instances that have a [specific tag](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).

  6. Under **Destination filter** , set `0.0.0.0/0` if you want to allow egress traffic from the VM instance to any destination. If you want to limit the destination, enter another IP range here.

  7. Under **Protocols and ports** , select **Specified protocols and ports** , select **tcp** , and enter `2525`.

  8. Click **Create** to save your changes.




## Sending mail through corporate mail servers

In some cases, you might have a corporate mail server that is already running an email service for you. If you need to send mail through a corporate mail server but are blocked by the port restrictions described at the top of this page, you can use a VPN to bypass these restrictions. This method requires running a VPN client on your Compute Engine cluster, and a VPN server on your corporate network router. This setup lets your instance appear "inside" your corporate firewall, and allows unrestricted access to your corporate mail server.

There are security implications for this configuration, and you should ensure that your Compute Engine instance has access to **only** the services it requires, and nothing more.

## What's next

  * Send emails from your instance [using Sendgrid](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-sendgrid).
  * Send emails from your instance [using Mailgun](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailgun).
  * Send emails from your instance [using Mailjet](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail/using-mailjet).
  * Read the Google Workspace domain documentation to learn how to use the [SMTP relay service](https://support.google.com/a/answer/2956491).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
