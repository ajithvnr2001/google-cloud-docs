---
url: https://docs.cloud.google.com/vpc-service-controls/docs/vpc-networks-rules/
title: Rules for including VPC networks in service perimeters \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:52.706259+00:00
---

# Rules for including VPC networks in service perimeters  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/vpc-networks-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Rules for including VPC networks in service perimeters Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the rules to add VPC networks to VPC Service Controls.

When you add VPC networks to service perimeters, the following rules apply:

  * If the host project is not protected by a perimeter, you can add VPC networks in the host project to separate perimeters under the same access policy.

  * VPC networks in the same host project must exist under the same access policy.

  * You can add VPC networks and their host project to the same perimeter.

  * VPC networks and their host project must not exist in different perimeters.

  * You cannot add a VPC network to multiple perimeters.

  * You cannot use VPC networks in a perimeter bridge.

  * If a VPC network's parent project is in a perimeter bridge, you cannot add the VPC network to a perimeter.




## What's next

  * Learn about how to [create service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
