---
url: https://docs.cloud.google.com/security-command-center/docs/faq/
title: Frequently asked questions \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:25.195123+00:00
---

# Frequently asked questions  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Frequently asked questions Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Can I limit who views which projects? 
     Yes. Permissions for Security Command Center can be applied at the organization, folder, and project level. For more information on Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 
How can I export data? 
     To export data from Security Command Center, use the [API](https://docs.cloud.google.com/security-command-center/docs/reference/rest) or the Google Cloud console. For more information about using the Google Cloud console, see [Exporting Security Command Center data](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data). 
Does Security Command Center support more assets like BigQuery? 
     Security Command Center supports discovery and inventory of BigQuery datasets. A future release will add support for BigQuery tables. We prioritize the addition of new products and resources based on customer feedback and demand. 
Does Security Command Center support alerting and setting alert policies? 
    

The Security Command Center API includes a notifications feature that sends information to a Pub/Sub topic to provide findings updates and new findings within minutes. Notifications include all finding information displayed in the Google Cloud console. To get started, see [Setting up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications). 

Security Command Center also provides an App Engine application that enables you to define custom queries for the [Notifier app](https://docs.cloud.google.com/security-command-center/docs/how-to-cloud-scc-tools#notifier). The Notifier app and other Security Command Center tools become obsolete as their full functionalities are added to Security Command Center features. For now, you can use the app to publish your queries to a user-defined Pub/Sub topic and integrate the feed with email and SMS. Support is offered on a best-effort basis only for all Security Command Center tools. 

When are new features released, and when can we expect bug fixes? 
     Security Command Center is in GA, so we release regular bug fixes and functionality as available. 
How fresh is the Security Command Center data that's displayed in the Google Cloud console? 
     Data freshness depends on finding source and the time of the most recent asset scan. For more information, see the assets and findings sections on the [using Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center) page. 
Why is the OPEN_FIREWALL module not producing findings for some of my firewall rules containing the source IP range 0.0.0.0/0 ? 
    

Your firewall rule may contain a destination port which explicitly does not produce findings.

There may be several reasons why findings are not being created. The firewall rule may be configured as a DENY rule. Your firewall rule may permit network traffic that utilizes protocols or ports explicitly ignored by the module. Findings are created for rules allowing traffic from any IP addresses (0.0.0.0/0) of any protocol or to any port (applicable to TCP, UDP, and SCTP protocols) with the exceptions noted below.

Findings aren't created for the following protocols:

  * ICMP
  * TCP 443 (HTTPS)
  * TCP 22 (SSH)
  * SCTP 22 (SSH)
  * TCP 3389 (RDP)
  * UDP 3389 (RDP)


Which types of findings are set to `INACTIVE` automatically, and which types of findings need to be marked as `INACTIVE` manually? 
    

See [ Overview of the finding lifecycle](https://docs.cloud.google.com/security-command-center/docs/finding-lifecycle-overview). 

Who do I contact if I have questions about Security Command Center service tiers? 
     For questions regarding Security Command Center service tiers, please contact your account representative or contact [Google Cloud sales](https://cloud.google.com/contact/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
