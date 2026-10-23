---
url: https://docs.cloud.google.com/architecture/framework/performance-optimization/
title: Well-Architected Framework: Performance optimization pillar \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:53.467263+00:00
---

# Well-Architected Framework: Performance optimization pillar  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/performance-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Well-Architected Framework: Performance optimization pillar Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-22 UTC

To view the content in the performance optimization pillar on a single page or to get a PDF output of the content, see [View on one page](https://docs.cloud.google.com/architecture/framework/performance-optimization/printable). 

This pillar in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to optimize the performance of workloads in Google Cloud.

This document is intended for architects, developers, and administrators who plan, design, deploy, and manage workloads in Google Cloud.

The recommendations in this pillar can help your organization to operate efficiently, improve customer satisfaction, increase revenue, and reduce cost. For example, when the backend processing time of an application decreases, users experience faster response times, which can lead to higher user retention and more revenue.

The performance optimization process can involve a trade-off between performance and cost. However, optimizing performance can sometimes help you reduce costs. For example, when the load increases, autoscaling can help to provide predictable performance by ensuring that the system resources aren't overloaded. Autoscaling also helps you to reduce costs by removing unused resources during periods of low load.

Performance optimization is a continuous process, not a one-time activity. The following diagram shows the stages in the performance optimization process:

![Performance optimization process](https://docs.cloud.google.com/static/architecture/framework/images/perf-optimization-process.svg)

The performance optimization process is an ongoing cycle that includes the following stages:

  1. **Define requirements** : Define granular performance requirements for each layer of the application stack before you design and develop your applications. To plan resource allocation, consider the key workload characteristics and performance expectations.
  2. **Design and deploy** : Use elastic and scalable design patterns that can help you meet your performance requirements.
  3. **Monitor and analyze** : Monitor performance continually by using logs, tracing, metrics, and alerts.
  4. **Optimize** : Consider potential redesigns as your applications evolve. Rightsize cloud resources and use new features to meet changing performance requirements.

As shown in the preceding diagram, continue the cycle of monitoring, re-assessing requirements, and adjusting the cloud resources.




For performance optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization) in the Well-Architected Framework. 

## Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the [`google-cloud-waf-performance-optimization`](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-performance-optimization) skill, which is available in the Google Agent Skills repository in GitHub.

To install the skill, run the following command in your agent's client or terminal:
    
    
    npx skills add google/skills --skill google-cloud-waf-performance-optimization
    

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global).

If you've already installed the skill, you can update it to the latest version by running the following command:
    
    
    npx skills update
    

**Note:** If `npx` is not available in your environment, install [Node.js](https://nodejs.org/en/download), which includes `npm` and `npx`.

## Core principles

The recommendations in the performance optimization pillar of the Well-Architected Framework are mapped to the following core principles:

  * [Plan resource allocation](https://docs.cloud.google.com/architecture/framework/performance-optimization/plan-resource-allocation)
  * [Take advantage of elasticity](https://docs.cloud.google.com/architecture/framework/performance-optimization/elasticity)
  * [Promote modular design](https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design)
  * [Continuously monitor and improve performance](https://docs.cloud.google.com/architecture/framework/performance-optimization/continuously-monitor-and-improve-performance)



## Contributors

Authors: 

  * [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect
  * [Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect
  * [Luis Urena](https://www.linkedin.com/in/urena-luis) | Developer Relations Engineer
  * [Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist



Other contributors: 

  * [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist
  * [Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist
  * [Ryan Cox](https://www.linkedin.com/in/ryanlcox) | Principal Architect
  * [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer
  * [Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director



[ Next Plan resource allocation  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/performance-optimization/plan-resource-allocation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
