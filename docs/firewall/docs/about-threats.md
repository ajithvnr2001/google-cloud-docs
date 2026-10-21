---
url: https://docs.cloud.google.com/firewall/docs/about-threats/
title: Threat signatures overview \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:31.068632+00:00
---

# Threat signatures overview  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/about-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Threat signatures overview Stay organized with collections  Save and categorize content based on your preferences. 

To protect your network from malicious attacks, Cloud Next Generation Firewall (Cloud NGFW) uses Palo Alto Networks signature-based threat detection technologies. Signature-based threat detection identifies malicious behavior by matching network traffic patterns against known threat signatures.

In this document, you learn about threat detection features and how they protect resources in your Virtual Private Cloud (VPC) network. You also learn how to use security profiles to override default actions and customize threat exceptions and antivirus behavior.

You can configure and manage the following threat detection features:

  * Default threat signatures
  * Supported threat severity levels
  * Threat exceptions
  * Antivirus



## Default signature set

Cloud NGFW provides a default set of [threat signatures](https://docs.paloaltonetworks.com/pan-os/10-0/pan-os-admin/threat-prevention/threat-signatures.html) that help you to safeguard your network workloads from threats. The signatures are used to detect vulnerabilities and spyware. To view all the threat signatures configured in Cloud NGFW, go to the [threat vault](https://threatvault.paloaltonetworks.com/). If you don't already have an account, sign-up for a new account.

  * **Vulnerability detection signatures** detect attempts to exploit system flaws or gain unauthorized access to systems. While anti-spyware signatures help identify infected hosts when traffic leaves the network, vulnerability detection signatures safeguard against threats that penetrate the network.

For example, vulnerability detection signatures help protect against buffer overflows, illegal code execution, and other attempts to exploit system vulnerabilities. The default vulnerability detection signatures provide detection for clients and servers from all known critical-, high-, and medium-severity threats along with any low- and informational-severity threats.

  * **Anti-spyware signatures** detect spyware on compromised hosts. Such spyware might try to contact external command-and-control (C2) servers.

  * **Antivirus signatures** detect viruses and malware found in executables and file types.




Each threat signature also has a [default action](https://docs.paloaltonetworks.com/pan-os/10-2/pan-os-web-interface-help/objects/objects-security-profiles/actions-in-security-profiles) associated with it. You can use [security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles) to override the actions for these signatures, and reference these profiles as part of a [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups) in a firewall policy rule. If any configured threat signature is detected in the intercepted traffic, the [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) performs the corresponding action specified in the security profile on the matched packets.

## Threat severity levels

A threat signature's severity indicates the risk of the detected event, and Cloud NGFW generates alerts for matching traffic. The following table summarizes the threat severity levels.

Severity | Description  
---|---  
Critical |  Serious threats cause root compromise of servers. For example, threats that affect default installations of widely deployed software and where exploit code is widely available to the attackers. The attacker usually does not need any special authentication credentials or knowledge about the individual victims, and the target does not need to be manipulated into performing any special functions.   
High | Threats that have the ability to become critical but there are mitigating factors. For example, they might be difficult to exploit, don't result in elevated privileges, or don't have a large victim pool.  
Medium | Minor threats in which impact is minimized and that don't compromise the target, or exploits that require an attacker to reside on the same local network as the victim. Such attacks affect only non-standard configurations or obscure applications, or they provide very limited access.  
Low | Warning-level threats that have very little impact on an organization's infrastructure. Such threats usually require local or physical system access and can often result in victim privacy issues and information leaks.  
Informational | Suspicious events that don't pose an immediate threat, but that are reported to indicate deeper problems that could possibly exist.  
  
## Threat exceptions

If you want to suppress or increase alerts on specific threat signature IDs, you can use [security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles) to override the default actions associated with threats. You can find the threat signature IDs of existing threats detected by Cloud NGFW in your threat logs.

Cloud NGFW provides visibility on threats that are detected in your environment. To view threats detected in your network, see [View threats](https://docs.cloud.google.com/firewall/docs/view-threats).

## Antivirus

By default, Cloud NGFW generates an alert when it finds a virus threat in the network traffic of any of its supported protocols. You can use [security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles) to override this default action, and allow or deny the network traffic based on the network protocol.

### Supported protocols

Cloud NGFW supports the following protocols for antivirus detection:

  * `SMTP`
  * `SMB`
  * `POP3`
  * `IMAP`
  * `HTTP2`
  * `HTTP`
  * `FTP`



### Supported actions

Cloud NGFW supports the following antivirus actions for its supported protocols:

  * `DEFAULT`: the default behavior of Palo Alto Networks antivirus action.

If a threat is found in the SMTP, IMAP, or POP3 protocol traffic, Cloud NGFW generates an alert in the threat logs. If a threat is found in the FTP, HTTP, or SMB protocol traffic, Cloud NGFW blocks the traffic. For more information, see the [Palo Alto Networks actions documentation](https://docs.paloaltonetworks.com/network-security/security-policy/administration/security-profiles/security-profile-antivirus).

  * `ALLOW`: allow the traffic.

  * `DENY`: deny the traffic.

  * `ALERT`: generate an alert in the threat logs. This is the default behavior of Cloud NGFW.




### Best practices for using the antivirus actions

We recommend that you configure the antivirus actions to deny all virus threats. Use the following guidance to determine whether to deny the traffic or generate an alert:

  * For business-critical applications, start with the security profile's action set to `alert`. This setting lets you monitor and assess threats without disrupting the traffic. After you confirm that the security profile meets your business and security requirements, you can change the security profile's action to `deny`.
  * For non-critical applications, set the security profile's action to `deny`. It's safe to block malicious traffic for non-critical applications immediately.



To set up an alert or to deny network traffic for all supported network protocols, use the following commands:

  * To set up an alert action on antivirus threats for all supported protocols:
        
        gcloud network-security security-profiles threat-prevention add-override NAME \
            --antivirus SMB,IMAP,HTTP,HTTP2,FTP,SMTP,POP3 \
            --action ALERT \
            --organization ORGANIZATION_ID \
            --location LOCATION \
            --project PROJECT_ID
        

Replace the following:

    * `NAME`: the name of the security profile; you can specify the name as a string or as a unique URL identifier.

    * `ORGANIZATION_ID`: the organization where the security profile is created.

If you use a unique URL identifier for the `name` flag, you can omit the `organization` flag.

    * `LOCATION`: the location of the security profile.

Location is always set to `global`. If you use a unique URL identifier for the `name` flag, you can omit the `location` flag.

    * `PROJECT_ID`: the project ID to use for quotas and access restrictions on the security profile.

  * To set up a deny action on antivirus threats for all supported protocols:
        
        gcloud network-security security-profiles threat-prevention add-override NAME \
            --antivirus SMB,IMAP,HTTP,HTTP2,FTP,SMTP,POP3 \
            --action DENY \
            --organization ORGANIZATION_ID \
            --location LOCATION \
            --project PROJECT_ID
        

Replace the following:

    * `NAME`: the name of the security profile; you can specify the name as a string or as a unique URL identifier.

    * `ORGANIZATION_ID`: the organization where the security profile is created.

If you use a unique URL identifier for the `name` flag, you can omit the `organization` flag.

    * `LOCATION`: the location of the security profile.

Location is always set to `global`. If you use a unique URL identifier for the `name` flag, you can omit the `location` flag.

    * `PROJECT_ID`: the project ID to use for quotas and access restrictions on the security profile.




For more information about how to set up the override, see [Add override actions in a threat prevention security profile](https://docs.cloud.google.com/firewall/docs/configure-security-profiles#add-overrides).

## Content update frequency

Cloud NGFW automatically updates all signatures without any user intervention, enabling you to focus on analyzing and resolving threats without managing or updating signatures.

Updates from Palo Alto Networks are picked up by Cloud NGFW and pushed to all the existing firewall endpoints. Update latency is estimated to be up to 48 hours.

## View logs

Several features of Cloud NGFW generate alerts, which are sent to the threat log. For more information about logging, see [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).

## What's next

  * [View threats](https://docs.cloud.google.com/firewall/docs/view-threats)
  * [Intrusion detection and prevention service overview](https://docs.cloud.google.com/firewall/docs/about-intrusion-prevention)
  * [Configure intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
