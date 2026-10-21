---
url: https://docs.cloud.google.com/location-finder/docs/overview/
title: Cloud Location Finder overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:38.424025+00:00
---

# Cloud Location Finder overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/location-finder/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Cloud Location Finder ](https://docs.cloud.google.com/location-finder/docs)
  * [ Guides ](https://docs.cloud.google.com/location-finder/docs/overview)



Send feedback 

#  Cloud Location Finder overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Location Finder is a public API that offers a repository of all Google Cloud and Google Distributed Cloud locations, as well as cloud locations for other cloud providers.

## What Cloud Location Finder provides

Cloud Location Finder provides a cloud location repository for cloud locations across providers. It automatically updates its locations to prevent issues with outdated, hard-coded lists.

With Cloud Location Finder, you can do the following:

  * Identify locations to deploy workloads that are close to existing workloads
  * Filter for locations within a designated country for compliance reasons
  * Sort locations based on their carbon footprint



You can identify cloud locations based on the following filters. For more information about how to use these filters, see [Query and filter syntax for Cloud Location Finder](https://docs.cloud.google.com/location-finder/docs/syntax).

Cloud location filtering type | Description  
---|---  
Proximity | Deploy workloads in locations that minimize latency between endpoints across cloud providers. Proximity is based on network latency. Cloud Location Finder measures network latency as the round-trip time between a pair of locations. The nearest location to a given source location is based on network latency observed between a pair of locations.  
Territory code | Identify relevant territories for compliance requirements. Cloud Location Finder uses [two-letter ISO 3166-1 alpha-2](https://www.iso.org/iso-3166-country-codes.html) codes to identify locations. Filtering locations by territory code helps you determine whether a location meets security, tax, data regulatory, or other requirements. To see the list of country codes, visit the [ISO Online Browsing Platform](https://www.iso.org/obp/ui/#search/code/).  
Carbon free energy (CFE) usage | Minimize the carbon footprint of your applications to meet sustainability goals. Cloud Location Finder measures a location's carbon footprint using [Google Cloud's CFE](https://cloud.google.com/sustainability/region-carbon) consumption data. Carbon footprint data is available only for Google Cloud locations.  
Cloud provider | Find the nearest location across each cloud provider you use.  
Cloud region or zone | Drill down within a region to find location information about specific zones.  
  
## Supported locations

Cloud Location Finder includes public locations from each of these location sources:

  * Google Cloud public [regions and zones](https://cloud.google.com/about/locations)

  * [Google Distributed Cloud](https://cloud.google.com/distributed-cloud) infrastructure

  * Google Distributed Cloud connected zones within specified regions

  * Amazon Web Services public [regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html) and [zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-availability-zones.html)

  * Amazon Web Services public [local zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations)

  * Microsoft Azure [geographies](https://learn.microsoft.com/en-us/rest/api/resources/subscriptions/list-locations?view=rest-resources-2022-12-01&tabs=HTTP)

  * Oracle Cloud Infrastructure public [regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/To_view_the_list_of_infrastructure_regions.htm) and [availability domains](https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.56.1/oci_cli_docs/cmdref/iam/availability-domain/list.html)


**Important:** Data for supported third-party cloud locations outside of Google Cloud is based on publicly-available resources, and Google Cloud isn't responsible for the accuracy of results. Data is updated every 24 hours.

## Location sorting

In the Google Cloud CLI, the [`list`](https://docs.cloud.google.com/location-finder/docs/reference/rest) command sorts by both CFE and cloud location ID. The [`search`](https://docs.cloud.google.com/location-finder/docs/reference/rest) command sorts by proximity, CFE%, and cloud location ID.

Results for proximity use an ascending sort, meaning the smallest distance appears first. Results for CFE% use a descending sort, meaning the largest CFE% appears first.

## Model Context Protocol for agents

Cloud Location Finder supports the Model Context Protocol (MCP) in **Public Preview**. This integration enables LLM-powered agents to natively call Cloud Location Finder to find optimal cloud locations, check carbon footprints, and filter by compliance rules using natural language.

For more information on configuring your agents to search and list locations, see [Use the Model Context Protocol (MCP) with Cloud Location Finder](https://docs.cloud.google.com/location-finder/docs/mcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
