---
url: https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions/
title: Use regions that consume low-carbon energy \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:20.137033+00:00
---

# Use regions that consume low-carbon energy  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Use regions that consume low-carbon energy Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-28 UTC

This principle in the sustainability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability) provides recommendations to help you select low-carbon regions for your workloads in Google Cloud.

## Principle overview

When you plan to deploy a workload in Google Cloud, an important architectural decision is the choice of Google Cloud region for the workload. This decision affects the carbon footprint of your workload. To minimize the carbon footprint, your region-selection strategy must include the following elements:

  * **Data-driven selection** : To identify and prioritize regions, consider the ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) indicator and the [carbon-free energy (CFE)](https://cloud.google.com/sustainability/region-carbon) metric.
  * **Policy-based governance** : Restrict resource creation to environmentally optimal locations by using the [resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) constraint in Organization Policy Service.
  * **Operational flexibility** : Use techniques like time-shifting and carbon-aware scheduling to run batch workloads during hours when the carbon intensity of the [electrical grid](https://en.wikipedia.org/wiki/Electrical_grid) is the lowest.



The electricity that's used to power your application and workloads in the cloud is an important factor that affects your choice of Google Cloud regions. In addition, consider the following factors:

  * **Data residency and sovereignty** : The location where you need to store your data is a foundational factor that dictates your choice of Google Cloud region. This choice affects compliance with local [data residency](https://docs.cloud.google.com/assured-workloads/docs/data-residency) requirements.
  * **Latency for end users** : The geographical distance between your end users and the regions where you deploy applications affects user experience and application performance.
  * **Cost** : The pricing for Google Cloud resources can be different across regions.



The [Google Cloud Region Picker](https://cloud.withgoogle.com/region-picker/) tool helps you select optimal Google Cloud regions based on your requirements for carbon footprint, cost, and latency. You can also use [Cloud Location Finder](https://docs.cloud.google.com/location-finder/docs/overview) to find cloud locations in Google Cloud and other providers based on your requirements for proximity, carbon-free energy (CFE) usage, and other parameters.

## Recommendations

To deploy your cloud workloads in low-carbon regions, consider the recommendations in the following sections. These recommendations are based on the guidance in [Carbon-free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).

### Understand the carbon intensity of cloud regions

Google Cloud data centers in a region use energy from the electrical grid where the region is located. Google measures the carbon impact of a region by using the CFE metric, which is calculated every hour. CFE indicates the percentage of carbon-free energy out of the total energy that's consumed during an hour. The CFE metric depends on two factors:

  * The type of power-generation plants that supply the grid during a given period.
  * [Google-attributed](https://sustainability.google/progress/projects/ppa/) clean energy that's supplied to the grid during that time.



For information about the aggregated average hourly CFE% for each Google Cloud region, see [Carbon-free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon). You can also get this data in a machine-readable format from the [Carbon free energy for Google Cloud regions](https://github.com/GoogleCloudPlatform/region-carbon-info) repository in GitHub and a [BigQuery public dataset](https://console.cloud.google.com/marketplace/product/bigquery-public-datasets/regional-cfe).

### Incorporate CFE in your location-selection strategy

Consider the following recommendations:

  * Select the cleanest region for your applications. If you plan to run an application for a long period, run it in the region that has the highest CFE%. For batch workloads, you have greater flexibility in choosing a region because you can predict when the workload must run.
  * Select low-carbon regions. Certain pages in the Google Cloud website and location selectors in the Google Cloud console show the ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) indicator for regions that have the lowest carbon impact.
  * Restrict the creation of resources to specific low-carbon Google Cloud regions by using the [resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) Organization Policy constraint. For example, to allow the creation of resources in only US-based low-carbon regions, create a constraint that specifies the `in:us-low-carbon-locations` value group.



When you select locations for your Google Cloud resources, also consider [best practices for region selection](https://cloud.google.com/solutions/best-practices-compute-engine-region-selection), including factors like data residency requirements, latency to end users, redundancy of the application, availability of services, and pricing.

### Use time-of-day scheduling

The carbon intensity of an electrical grid can vary significantly throughout the day. The variation depends on the mix of energy sources that supply the grid. You can schedule workloads, particularly those that are flexible or non-urgent, to run when the grid is supplied by a higher proportion of CFE.

For example, many grids have higher CFE percentages during off-peak hours or when renewable sources like solar and wind supply more power to the grid. By scheduling compute-intensive tasks such as model training and large-scale batch inference during higher-CFE hours, you can significantly reduce the associated carbon emissions without affecting performance or cost. This approach is known as _time-shifting_ , where you use the dynamic nature of a grid's carbon intensity to optimize your workloads for sustainability.

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/architecture/framework/sustainability)

[ Next Optimize AI and ML workloads  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-28 UTC."],[],[]] 
