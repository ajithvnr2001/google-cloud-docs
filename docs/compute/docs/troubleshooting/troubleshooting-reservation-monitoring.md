---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-monitoring/
title: Troubleshooting reservation monitoring \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:27.248054+00:00
---

# Troubleshooting reservation monitoring  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting reservation monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to resolve issues with monitoring the consumption of [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) of Compute Engine zonal resources by using Cloud Monitoring. 

## Fail to access Cloud Monitoring

**Issue:** This error occurs when you can't access Monitoring.

**Resolution:** Make sure that you [grant access to Cloud Monitoring](https://docs.cloud.google.com/monitoring/access-control#grant-monitoring-access) to the current project, or the organization where the current project is located grants access to it.

## Fail to view the time series of a reservation

**Issue:** This error occurs when you can't access and view the time series of a reservation.

**Resolution:** After creating a reservation, its time series becomes available within 30 minutes. If you can't access and view the time series of a reservation after this timeframe, try one of the following:

  * To make sure that a reservation exists, [view the details of the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#describe-reservations).

  * If you can't view the details of a reservation:

    * Make sure that you're in the same project where the reservation was created. You can only access and view the time series of a reservation created in the current project.

    * Deleting a reservation also deletes its time series. The time series can't be recovered.




## MQL query misses an operation

**Issue:** This error occurs when you attempt to run a MQL query without specifying a `| condition` or `| absent_for` operation.

**Resolution:** When creating an MQL-based alert condition, make sure to specify one of the following operations at the end of your query:

  * For threshold alerts, specify [`condition`](https://docs.cloud.google.com/monitoring/mql/reference#condition-tabop).

  * For absence alerts, specify [`absent_for`](https://docs.cloud.google.com/monitoring/mql/reference#absent_for-tabop).




For more information, see [Alerting policies with MQL](https://docs.cloud.google.com/monitoring/mql/alerts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
