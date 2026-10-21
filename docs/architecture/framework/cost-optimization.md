---
url: https://docs.cloud.google.com/architecture/framework/cost-optimization/
title: Well-Architected Framework: Cost optimization pillar \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:12.300438+00:00
---

# Well-Architected Framework: Cost optimization pillar  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/cost-optimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Well-Architected Framework: Cost optimization pillar Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-13 UTC

To view the content in the cost optimization pillar on a single page or to to get a PDF output of the content, see [View on one page](https://docs.cloud.google.com/architecture/framework/cost-optimization/printable). 

The cost optimization pillar in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) describes principles and recommendations to optimize the cost of your workloads in Google Cloud.

The intended audience includes the following:

  * CTOs, CIOs, CFOs, and other executives who are responsible for strategic cost management.
  * Architects, developers, administrators, and operators who make decisions that affect cost at all the stages of an organization's cloud journey.



The cost models for on-premises and cloud workloads differ significantly. On-premises IT costs include capital expenditure (CapEx) and operational expenditure (OpEx). On-premises hardware and software assets are acquired and the acquisition costs are [depreciated](https://en.wikipedia.org/wiki/Depreciation) over the operating life of the assets. In the cloud, the costs for most cloud resources are treated as OpEx, where costs are incurred when the cloud resources are consumed. This fundamental difference underscores the importance of the following core principles of cost optimization.

**Note:** You might be able to classify the cost of some Google Cloud services (like Compute Engine sole-tenant nodes) as capital expenditure. For more information, see [Sole-tenancy accounting FAQ](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-accounting-faq).

For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

## Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the [`google-cloud-waf-cost-optimization`](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-cost-optimization) skill, which is available in the Google Agent Skills repository in GitHub.

To install the skill, run the following command in your agent's client or terminal:
    
    
    npx skills add google/skills --skill google-cloud-waf-cost-optimization
    

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global).

If you've already installed the skill, you can update it to the latest version by running the following command:
    
    
    npx skills update
    

**Note:** If `npx` is not available in your environment, install [Node.js](https://nodejs.org/en/download), which includes `npm` and `npx`.

## Core principles

The recommendations in the cost optimization pillar of the Well-Architected Framework are mapped to the following core principles:

  * [**Align cloud spending with business value**](https://docs.cloud.google.com/architecture/framework/cost-optimization/align-cloud-spending-business-value): Ensure that your cloud resources deliver measurable business value by aligning IT spending with business objectives.
  * [**Foster a culture of cost awareness**](https://docs.cloud.google.com/architecture/framework/cost-optimization/foster-culture-cost-awareness): Ensure that people across your organization consider the cost impact of their decisions and activities, and ensure that they have access to the cost information required to make informed decisions.
  * [**Optimize resource usage**](https://docs.cloud.google.com/architecture/framework/cost-optimization/optimize-resource-usage): Provision only the resources that you need, and pay only for the resources that you consume.
  * [**Optimize continuously**](https://docs.cloud.google.com/architecture/framework/cost-optimization/optimize-continuously): Continuously monitor your cloud resource usage and costs, and proactively make adjustments as needed to optimize your spending. This approach involves identifying and addressing potential cost inefficiencies before they become significant problems.



These principles are closely aligned with the core tenets of [cloud FinOps](https://cloud.google.com/learn/what-is-finops). FinOps is relevant to any organization, regardless of its size or maturity in the cloud. By adopting these principles and following the related recommendations, you can control and optimize costs throughout your journey in the cloud.

## Contributors

Author: [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist

Other contributors: 

  * [Anuradha Bajpai](https://www.linkedin.com/in/anuradhabajpai) | Solutions Architect
  * [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect
  * [Eric Lam](https://www.linkedin.com/in/ericlam) | Head of Google Cloud FinOps
  * [Fernando Rubbo](https://www.linkedin.com/in/fernandorubbo) | Cloud Solutions Architect
  * [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist
  * [Gary Harmson](https://www.linkedin.com/in/garyharmson) | Principal Architect
  * [Jose Andrade](https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist
  * [Kent Hua](https://www.linkedin.com/in/kenthua) | Solutions Manager
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer
  * [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer
  * [Steve McGhee](https://www.linkedin.com/in/stevemcghee) | Reliability Advocate
  * [Sergei Lilichenko](https://www.linkedin.com/in/sergei-lilichenko) | Solutions Architect
  * [Wade Holmes](https://www.linkedin.com/in/wholmes) | Global Solutions Director
  * [Zach Seils](https://www.linkedin.com/in/zachseils) | Networking Specialist



[ Next Align spending with business value  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/cost-optimization/align-cloud-spending-business-value)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
