---
url: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/
title: Well-Architected Framework: AI and ML perspective \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:25.181654+00:00
---

# Well-Architected Framework: AI and ML perspective  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Well-Architected Framework: AI and ML perspective Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-10-11 UTC

To view the content in the AI and ML perspective on a single page or to to get a PDF output of the content, see [View on one page](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable). 

This document in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) describes principles and recommendations to help you to design, build, and manage AI and ML workloads in Google Cloud that meet your operational, security, reliability, cost, and performance goals.

The target audience for this document includes decision makers, architects, administrators, developers, and operators who design, build, deploy, and maintain AI and ML workloads in Google Cloud.

The following pages describe principles and recommendations that are specific to AI and ML, for each pillar of the Well-Architected Framework:

  * [AI and ML perspective: Operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence)
  * [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security)
  * [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability)
  * [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization)
  * [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization)



## Contributors

Authors: 

  * [Benjamin Sadik](https://www.linkedin.com/in/benjaminhaimsadik) | AI and ML Specialist Customer Engineer
  * [Charlotte Gistelinck, PhD](https://www.linkedin.com/in/charlottegistelinck) | Partner Engineer
  * [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist
  * [Isaac Lo](https://www.linkedin.com/in/isaac-l-25525440) | AI Business Development Manager
  * [Kamilla Kurta](https://www.linkedin.com/in/kamillakurta) | GenAI/ML Specialist Customer Engineer
  * [Mohamed Fawzi](https://www.linkedin.com/in/fawzii) | Benelux Security and Compliance Lead
  * [Rick (Rugui) Chen](https://www.linkedin.com/in/rugui-chen) | AI Infrastructure Field Solutions Architect
  * [Sannya Dang](https://www.linkedin.com/in/thugiangdang) | AI Solution Architect



Other contributors: 

  * [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect
  * [Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect
  * [Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist
  * [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework
  * [Ryan Cox](https://www.linkedin.com/in/ryanlcox) | Principal Architect
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer
  * [Stef Ruinard](https://www.linkedin.com/in/stefruinard) | Generative AI Field Solutions Architect
  * [Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director
  * [Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist



[ Next Operational excellence  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-10-11 UTC."],[],[]] 
