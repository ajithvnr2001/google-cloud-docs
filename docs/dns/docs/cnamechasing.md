---
url: https://docs.cloud.google.com/dns/docs/cnamechasing/
title: CNAME chasing \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:40.950653+00:00
---

# CNAME chasing  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/cnamechasing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  CNAME chasing Stay organized with collections  Save and categorize content based on your preferences. 

CNAME chasing refers to a subsequent lookup of a DNS name returned from a CNAME record answer to an initial query. Public DNS resolvers perform subsequent lookup of CNAME answers according to their configuration. Generally, public resolvers chase CNAME answers in any public zones.

When Google Cloud VMs use their metadata server (`169.254.169.254`) as their name server, and no alternative name server is defined in an outbound server policy of the VPC network, Cloud DNS performs CNAME chasing as described in the following table.

Source of CNAME answer | Cloud DNS resolver behavior  
---|---  
**Cloud DNS private zone**  
with local records (not a forwarding zone)  |  Cloud DNS systems perform queries for the CNAME answer in Cloud DNS private zones that are authorized for the VPC network.  Cloud DNS systems _don't_ perform queries for the CNAME answer in any public DNS zones, including Cloud DNS public zones.   
**Cloud DNS forwarding zone** | Cloud DNS systems _don't_ perform queries for any CNAME answers received from forwarding target name servers.   
**Cloud DNS response policy zone** | Cloud DNS systems _don't_ perform queries for any CNAME answers received from local data rules of response policy zones.   
**Cloud DNS public zone** |  Cloud DNS systems perform queries for the CNAME answer in the [internal DNS service](https://docs.cloud.google.com/compute/docs/internal-dns) and public zones, including Cloud DNS public zones.  Cloud DNS systems _don't_ perform queries for the CNAME answer in any Cloud DNS private zones (including any forwarding, peering, or response policy zones).   
  
## What's next

  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
