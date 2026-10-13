---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/error-codes/gphw/
title: GPHW error reference \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:55.320786+00:00
---

# GPHW error reference  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/error-codes/gphw/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  GPHW error reference Stay organized with collections  Save and categorize content based on your preferences. 

GDC hardware error messages consist of an error ID in the format `GPHW1234` where `1234` is a unique number, followed by a description of the problem and a suggestion for how to fix it. This topic documents each of those error messages.

## GPHW3001: HighManagementPlaneCPUUsage

The Management CPU usage on the PANW Firewall is greater than 75%

## GPHW3002: HighDataplanePlaneCPUUsage

The Data plane CPU usage on the PANW Firewall is greater than 75%

## GPHW3003: EthernetInterfaceStatus

One of the ethernet interfaces on the PANW Firewall is down

## GPHW3004: HighSessionTableUtilization

Session Table utilization on the PANW Firewall is greater than 80%

## GPHW3101: TimeNotSynchronized

The server's timesync client is not synchronized with upstream server(s). Please check the health of the upstream NTP servers by checking the health of NTP pods: `kubectl -n gpc-system get pods -l app.kubernetes.io/name=ntp`.

## GPHW3401: LowCapacity

A NetApp ONTAP aggregate has less than 25% of its capacity remaining.

## GPHW3402: VeryLowCapacity

A NetApp ONTAP aggregate has less than 15% of its capacity remaining.

## GPHW3403: ExtremelyLowCapacity

A NetApp ONTAP aggregate has less than 5% of its capacity remaining.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
