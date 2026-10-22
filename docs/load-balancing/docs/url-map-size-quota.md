---
url: https://docs.cloud.google.com/load-balancing/docs/url-map-size-quota/
title: URL map size and quota units \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:16.546587+00:00
---

# URL map size and quota units  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/url-map-size-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  URL map size and quota units Stay organized with collections  Save and categorize content based on your preferences. 

The load balancer configuration size quotas measure the size of all URL maps in a project, VPC network, or region of a VPC network, depending on the type of Application Load Balancer. Individual URL maps are limited to 1 MB of data each, with the exception of the classic Application Load Balancer, which retains its 64 KB limit. Quota units represent the complexity of the configuration of your URL map. A routing configuration with few rules or short matchers consumes fewer quota units, while a highly complex configuration with many rules, hostnames, or path matchers consumes more.

## How the quota works

Only the URL maps that are part of a complete Application Load Balancer configuration contribute to the usage of a load balancer configuration size quota. To be part of a complete configuration, a URL map must be referenced by a target HTTP proxy or target HTTPS proxy, and the target proxy must be referenced by a forwarding rule. Google Cloud calculates the total quota usage for URL maps that are part of a complete configuration using the following formula:

_Quota usage = sum of single URL map quota units_ ×  _number of forwarding rules referencing the same URL map through a target HTTP proxy or target HTTPS proxy_

If a relationship between a forwarding rule, through a target HTTP proxy or target HTTPS proxy, to the URL map doesn't exist, the URL map doesn't contribute to the usage of a load balancer configuration size quota.

## Manage quota usage

The usage of each configuration size quota changes as you modify Application Load Balancers:

  * **Updating a URL map** : Modifying an existing URL map (such as adding or removing host rules, path matchers, or route rules) changes the number of quota units that the URL map uses. The number of quota units is multiplied by the number of forwarding rules that reference the URL map through target HTTP proxies and target HTTPS proxies.
  * **Updating a Target Proxy** : If you update a target proxy to reference a different URL map, and no other target proxy references the previous URL map, the quota units used by the previous URL map no longer contribute to the usage of a configuration size quota.
  * **Creating or deleting a forwarding rule** : Creating a new forwarding rule associated with a target proxy that uses a URL map increases the number of quota units that the URL map contributes to a configuration size quota. Conversely, deleting a forwarding rule reduces the number of quota units that the URL map contributes to a configuration size quota.



## Check quota usage

To determine the number of quota units an existing URL map uses, use the following Google Cloud CLI command:
    
    
    gcloud beta compute url-maps describe URL_MAP_NAME [--region=REGION_NAME | --global] --format="value(status)"
    

Replace the following:

  * `URL_MAP_NAME`: the name of your URL map.
  * `REGION_NAME`: the region in which the load balancer is defined.



The output includes a read-only `status.quotaUsage` object showing the total number of units calculated for the URL map, as well as the number of forwarding rules using it.

For more information, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#config-size-limits).

## What's next

  * [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas#url_maps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
