---
url: https://docs.cloud.google.com/livestream/docs/how-to/vpc/secure-pipeline/
title: Use VPC Service Controls to secure your pipeline \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:26.024039+00:00
---

# Use VPC Service Controls to secure your pipeline  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/vpc/secure-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Use VPC Service Controls to secure your pipeline Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) is a Google Cloud product that lets you set up a secure perimeter to guard against data exfiltration. This page shows how to use VPC Service Controls with a live stream private pool to secure your live streams.

## Limitations

Protecting input endpoints within a VPC Service Controls perimeter requires setting up a private connection to the live stream service and switching to a private pool in the Live Stream API.

## Enable VPC Service Controls enforcement for the Live Stream API

  1. Set up a private connection between your virtual private cloud network and the Live Stream API producer network using private services access. See [Configure private services access](https://docs.cloud.google.com/livestream/docs/how-to/vpc/configure-private-services-access).
  2. Configure the live stream default pool to use the private connection created in the previous step. See [Configure a private pool](https://docs.cloud.google.com/livestream/docs/how-to/vpc/configure-private-pool).



[ Next Configure private services access  arrow_forward  ](https://docs.cloud.google.com/livestream/docs/how-to/vpc/configure-private-services-access)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
