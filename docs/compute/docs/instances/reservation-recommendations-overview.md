---
url: https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview/
title: Reservation recommendations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:45:42.613098+00:00
---

# Reservation recommendations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Reservation recommendations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how Compute Engine generates reservation recommendations and the parameters to configure them.

Compute Engine provides reservation recommendations to help you identify idle or underutilized on-demand reservations for the previous seven days so that you can [modify](https://docs.cloud.google.com/compute/docs/instances/reservations-modify) or [delete the reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete).

Compute Engine generates recommendations automatically based on system metrics gathered by the Cloud Monitoring service. You can configure reservations recommendations to receive more or fewer recommendations.

  * To identify these recommendations and take action, see [View and apply idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/view-and-apply-idle-reservation-recommendations) or [View and apply underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/view-and-apply-underutilized-reservation-recommendations).
  * To configure these recommendations, see [Configure idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-idle-reservation-recommendations) or [Configure underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-underutilized-reservation-recommendations).
  * For an overview of Compute Engine reservations, see [About reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).



## Pricing

There are no costs associated with using idle reservation recommendations. Using recommendations to reduce your resource usage can result in cost savings. The displayed cost savings estimate is your potential monthly savings if you adjust your VM reservation to match your actual usage. For example, if you reserved 8 VMs but consistently use only 1, you see the cost savings of downsizing your reservation to 1 VM.

## Limitations

Idle and underutilized reservation recommendations aren't available for on-demand reservations that are attached to committed use discounts (CUDs).

## How detection of idle and underutilized reservations works

Reservation recommendations for Compute Engine are based on historical usage metrics. By default, the historical observation period is the previous 7 days. By changing the default observation period, you can customize the recommendations that you receive.

To generate recommendations, the algorithm considers reservations that accrue costs, but aren't associated with an active Compute Engine resource for the previous 7 days.

### Frequency of recommendations

After a reservation is created and you haven't consumed any resources for at least 7 days, Compute Engine begins generating recommendations for it. New recommendations are generated once per day. 

## Customize recommendations

Compute Engine lets you customize the recommendations you receive for your project by changing the configuration used by the recommendation algorithm. In particular, by changing the default observation period, you can receive recommendations that better fit your workloads, applications, and infrastructure needs.

To learn how to modify the configuration for your project, see the following:

  * [Configure idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-idle-reservation-recommendations)
  * [Configure underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-underutilized-reservation-recommendations).



## Choose the right configuration

This section describes the values that you can set for the configuration. Changing these values affects the recommendations that you receive.

### The observation period

Set the observation period duration to calculate recommendations by modifying the value for `idle_reservation_lookback_period` or `under_utilized_reservation_lookback_period` and upload the new configuration for your project. You can set the observation period to a value between 7 days and 30 days, for example:

  * For an observation period of the previous 7 days, use `"P7D"`.
  * For an observation period of the previous 30 days, use `"P30D"`.



By default, the observation period is 7 days.

  * For recommendations based on short-term changes in your workload, use a shorter observation period.
  * For recommendations that are not affected by short-term fluctuations in your workload, use a longer observation period.



Similarly, set the usage threshold that triggers an underutilized reservation recommendation by modifying the value for `under_utilized_reservation_utilization_threshold` and upload the new configuration for your project, for example:

  * For a threshold of 80%, `"0.8"`.



## What's next

  * Learn how to [view and apply idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/view-and-apply-idle-reservation-recommendations) or [view and apply underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/view-and-apply-underutilized-reservation-recommendations).
  * Learn how to [configure idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-idle-reservation-recommendations) or [configure underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-underutilized-reservation-recommendations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
