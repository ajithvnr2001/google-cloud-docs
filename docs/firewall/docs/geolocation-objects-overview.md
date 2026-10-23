---
url: https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview/
title: Geolocation objects \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:50.894321+00:00
---

# Geolocation objects  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Geolocation objects Stay organized with collections  Save and categorize content based on your preferences. 

Geolocation objects in the firewall policy rules let you filter external IPv4 and external IPv6 traffic based on specific geographic locations or regions.

You can apply rules with geolocation objects to ingress and egress traffic. Based on the direction of the traffic, the IP addresses associated with the country codes are matched against the source or destination of the traffic.

## Specifications

The following firewall specifications apply to geolocation objects:

  * You can configure geolocation objects for hierarchical firewall policies, global network firewall policies, and regional network firewall policies.

  * To add geolocations to the firewall policy rules, use the two-letter country or region codes as defined in the [ISO 3166 alpha-2 country codes](https://wikipedia.org/wiki/ISO_3166-1_alpha-2).

For example, if you want to allow incoming traffic only from the US into the network, create an ingress firewall policy rule with the source country code set to `US` and the action set to `allow`. Similarly, if you want to allow outbound traffic only to the US, configure an egress firewall policy rule with the destination country code set to `US` and the action set to `allow`.

  * Cloud NGFW lets you configure firewall rules for the following territories subject to comprehensive US sanctions: 

Territories | Assigned code  
---|---  
Crimea | XC  
So-Called Donetsk People's Republic and Luhansk People's Republic | XD  
  * If there are any duplicate country codes included in a single firewall rule, only one entry for that country code is retained. The duplicate entry is removed. For example, in the country code list `ca,us,us`, only `ca,us` is retained.

  * Google maintains a database with IP addresses and country code mappings. Google Cloud firewalls use this database to map the IP addresses of source and destination traffic to the country code, and then apply the matching firewall policy rule with geolocation objects.

  * Sometimes, IP address assignments and country codes change due to the following conditions:

    * IP address movement across geographic locations
    * Updates to the [ISO 3166 alpha-2 country codes](https://wikipedia.org/wiki/ISO_3166-1_alpha-2) standard

Because it takes some time for these changes to be reflected in Google's database, you might see some traffic disruptions and changes in behavior for certain traffic being blocked or allowed.

**Note:** Google's database is maintained based on input from various trusted sources. Google doesn't support customizations to this database based on individual customer requests.



## Geolocation objects matching for internal IP addresses

Geolocation objects are designed to apply to external IP addresses. Geolocation objects don't apply to the private internal IP addresses shown in the following table:

Address type | Ranges and specifications  
---|---  
Internal IPv4 (Private) | All RFC-defined [private IPv4 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) (including RFC 1918 and RFC 6598) and link-local addresses (`169.254.0.0/16`).  
Internal IPv6 (Private) | Unique Local Addresses (ULA) (`fc00::/7`) and link-local addresses (`fe80::/10`).  
  
However, geolocation objects firewall policy rules _do_ apply to internal IP addresses if they are privately used public IP addresses. Even though these addresses are internal to the VPC network, they are public addresses and are matched against geolocation objects. To prevent communication issues when you use privately used public IP addresses, create higher priority firewall policy rules that allow traffic to or from the privately used public IP address ranges.

## Use geolocation objects with other firewall policy rule filters

You can use geolocation objects along with other source or destination filters. Depending on the rule direction, the firewall policy rule is applied to the incoming or outgoing traffic that matches the union of all the specified filters.

For information about how geolocation objects work with other source filters in the ingress rules, see [Sources for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src).

For information about how geolocation objects work with other destination filters in the egress rules, see [Destinations for egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest).

## What's next

  * [Configure global network firewall policy to deny egress connections to specific geolocations](https://docs.cloud.google.com/firewall/docs/tutorials/configure-fwpolicy-deny-egress-geolocation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
