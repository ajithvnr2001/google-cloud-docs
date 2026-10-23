---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:21.333630+00:00
---

# Security bulletins  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs)
  * [ Resources ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes all security bulletins related to Migrate to Virtual Machines 5.0 by Google.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `https://cloud.google.com/migrate-to-virtual-machines-security-bulletins.xml`



## GCP-2024-040

**Published:** 2024-07-10  
Description | Severity | Notes  
---|---|---  
The [Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector), the virtual appliance used to connect VMware sources to Migrate to Virtual Machines, is exposed to a security vulnerability on OpenSSH Daemon(SSHD) ([CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)).

#### What should I do?

Migrate Connector version 2.6.2497 has been released to mitigate this issue, and is being gradually rolled out. To apply it, go to the [Migrate to Virtual Machines page on the Google Cloud console](http://console.cloud.google.com/compute/mfce/sources). Once an update for your source appliance is available, you will see a banner with the words _An update is available for your source_. Approve the update to initiate the version update on the Migrate Connector. For more information, see [Modify a Migrate Connector configuration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector#update_a_migrate_connector). To mitigate the risk immediately, use any of the following options:

  1. Sign in to the Migrate Connector and run the following command: 
         
         sudo sed -i 's/#LoginGraceTime 2m/LoginGraceTime 0/g' /etc/ssh/sshd_config

**or**   
  
Edit `/etc/ssh/sshd_config` manually, uncomment the entry for `LoginGraceTime` and set its value to 0.
  2. Restart SSHD by running the following command: 
         
         sudo systemctl restart ssh




#### What vulnerabilities are being addressed?

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that can be used to obtain access to a remote shell, enabling attackers to gain root access. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts. | Critical | [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
