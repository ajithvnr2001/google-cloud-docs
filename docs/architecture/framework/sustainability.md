---
url: https://docs.cloud.google.com/architecture/framework/sustainability/
title: Well-Architected Framework: Sustainability pillar \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:05.145360+00:00
---

# Well-Architected Framework: Sustainability pillar  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/sustainability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Well-Architected Framework: Sustainability pillar Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-13 UTC

To view the content in the sustainability pillar on a single page or to to get a PDF output of the content, see [View on one page](https://docs.cloud.google.com/architecture/framework/sustainability/printable). 

The sustainability pillar in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to design, build, and manage workloads in Google Cloud that are energy-efficient and carbon-aware.

The target audience for this document includes decision-makers, architects, administrators, developers, and operators who design, build, deploy, and maintain workloads in Google Cloud.

Architectural and operational decisions have a significant impact on the energy usage, water impact, and carbon footprint that's driven by your workloads in the cloud. Every workload, whether it's a small website or a large-scale ML model, consumes energy and contributes to carbon emissions and water resource intensity. When you integrate sustainability into your cloud architecture and design process, you build systems that are efficient, cost-effective, _and_ environmentally sustainable. A sustainable architecture is resilient and optimized, which creates a positive feedback loop of higher efficiency, lower cost, and lower environmental impact.

## Sustainable by design: Holistic business outcomes

Sustainability isn't a trade-off against other core business objectives; sustainability practices help to accelerate your other business objectives. Architecture choices that prioritize low-carbon resources and operations help you build systems that are also faster, cheaper, and more secure. Such systems are considered to be _sustainable by design_ , where optimizing for sustainability leads to overall positive outcomes for performance, cost, security, resilience, and user experience.

### Performance optimization

Systems that are [optimized for performance](https://docs.cloud.google.com/architecture/framework/performance-optimization) inherently use fewer resources. An efficient application that completes a task faster requires compute resources for a shorter duration. Therefore, the underlying hardware consumes less kilowatt-hours (kWh) of energy. Optimized performance also leads to lower latency and better user experience. Time and energy aren't wasted by resources waiting on inefficient processes. When you use specialized hardware (for example, GPUs and TPUs), adopt efficient algorithms, and maximize parallel processing, you improve performance _and_ reduce the carbon footprint of your cloud workload.

### Cost optimization

Cloud operational expenditure depends on resource usage. Due to this direct correlation, when you continuously [optimize cost](https://docs.cloud.google.com/architecture/framework/cost-optimization), you also reduce energy consumption and carbon emissions. When you right-size VMs, implement aggressive autoscaling, archive old data, and eliminate idle resources, you reduce resource usage and cloud costs. You also reduce the carbon footprint of your systems, because the data centers consume less energy to run your workloads.

### Security and resilience

[Security](https://docs.cloud.google.com/architecture/framework/security) and [reliability](https://docs.cloud.google.com/architecture/framework/reliability) are prerequisites for a sustainable cloud environment. A compromised system—for example, a system that's affected by a denial of service (DoS) attack or an unauthorized data breach—can dramatically increase resource consumption. These incidents can trigger massive spikes in traffic, create runaway compute cycles for mitigation, and necessitate lengthy, high-energy operations for forensic analysis, cleanup, and data restoration. Strong security measures can help to prevent unnecessary spikes in resource usage, so that your operations remain stable, predictable, and energy-efficient.

### User experience

Systems that prioritize efficiency, performance, accessibility, and minimal use of data can help to reduce energy usage by end users. An application that loads a smaller model or processes less data to deliver results faster helps to reduce the energy that's consumed by network devices and end-user devices. This reduction in energy usage particularly benefits users who have limited bandwidth or who use older devices. Further, sustainable architecture helps to minimize planetary harm and demonstrates your commitment to socially responsible technology.

## Sustainability value of migrating to the cloud

Migrating on-premises workloads to the cloud can help to reduce your organization's environmental footprint. The transition to cloud infrastructure can reduce energy usage and associated emissions by [1.4 to 2 times](https://research.google/blog/good-news-about-the-carbon-footprint-of-machine-learning-training/) when compared to typical on-premises deployments. Cloud data centers are modern, custom-designed facilities that are built for high [power usage effectiveness (PUE)](https://en.wikipedia.org/wiki/Power_usage_effectiveness). Older on-premises data centers often lack the scale that's necessary to justify investments in advanced cooling and power distribution systems.

## Shared responsibility and shared fate

[Shared responsibilities and shared fate on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) describes how security for cloud workloads is a shared responsibility between Google and you, the customer. This shared responsibility model also applies to sustainability.

Google is responsible for the sustainability _of_ Google Cloud, which means the energy efficiency and water stewardship of our data centers, infrastructure, and core services. We invest continuously in renewable energy, climate-conscious cooling, and hardware optimization. For more information about Google's sustainability strategy and progress, see [Google Sustainability 2025 Environmental Report](https://sustainability.google/google-2025-environmental-report/).

You, the customer, are responsible for sustainability _in_ the cloud, which means optimizing your workloads to be energy efficient. For example, you can right-size resources, use serverless services that scale to zero, and manage data lifecycles effectively.

We also advocate a shared fate model: sustainability isn't just a division of tasks but a collaborative partnership between you and Google to reduce the environmental footprint for the entire ecosystem.

## Use AI for business impact

The sustainability pillar of the Well-Architected Framework (this document) includes guidance to help you design sustainable AI systems. However, a comprehensive sustainability strategy extends beyond the environmental impact of AI workloads. The strategy should include ways to use AI to optimize operations and create new business value.

AI serves as a catalyst for sustainability by transforming vast datasets into actionable insights. It enables organizations to transition from reactive compliance to proactive optimization, such as in the following areas:

  * **Operational efficiency** : Streamline operations through improved inventory management, supply chain optimization, and intelligent energy management.
  * **Transparency and risk** : Use data for granular supply chain transparency, regulatory compliance, and climate risk modeling.
  * **Value and growth** : Develop new revenue streams in sustainable finance and [recommerce](https://en.wikipedia.org/wiki/Recommerce).



Google offers the following products and features to help you derive insights from data and build capabilities for a sustainable future:

  * [Google Earth AI](https://ai.google/earth-ai/): Uses planetary-scale geospatial data to analyze environmental changes and monitor supply chain impacts.
  * [WeatherNext](https://deepmind.google/science/weathernext/): Provides advanced weather forecasting and climate risk analytics to help you build resilience against climate volatility.
  * [Geospatial insights with Google Earth](https://mapsplatform.google.com/solutions/visualize-data/): Uses geospatial data to add rich contextual data to locations, which enables smarter site selection, resource planning, and operations.
  * [Google Maps routes optimization](https://mapsplatform.google.com/maps-products/#routes-section): Optimizes logistics and delivery routes to increase efficiency and reduce fuel consumption and transportation emissions.



## Collaborations with partners and customers

Google Cloud and [TELUS](https://www.telus.com) have partnered to advance cloud sustainability by migrating workloads to Google's carbon-neutral infrastructure and leveraging data analytics to optimize operations. This collaboration provides social and environmental benefits through initiatives like smart-city technology, which uses real-time data to reduce traffic congestion and carbon emissions across municipalities in Canada. For more information about this collaboration, see [Google Cloud and TELUS collaborate for sustainability](https://cloud.google.com/blog/topics/sustainability/google-cloud-and-telus-collaborate-for-sustainability).

## Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the [`google-cloud-waf-sustainability`](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-sustainability) skill, which is available in the Google Agent Skills repository in GitHub.

To install the skill, run the following command in your agent's client or terminal:
    
    
    npx skills add google/skills --skill google-cloud-waf-sustainability
    

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global).

If you've already installed the skill, you can update it to the latest version by running the following command:
    
    
    npx skills update
    

**Note:** If `npx` is not available in your environment, install [Node.js](https://nodejs.org/en/download), which includes `npm` and `npx`.

## Core principles

The recommendations in the sustainability pillar of the Well-Architected Framework are mapped to the following core principles:

  * [Use regions that consume low-carbon energy](https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions)
  * [Optimize AI and ML workloads for energy efficiency](https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency)
  * [Optimize resource usage for sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-resource-usage)
  * [Develop energy-efficient software](https://docs.cloud.google.com/architecture/framework/sustainability/energy-efficient-software)
  * [Optimize data and storage for sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/optimize-storage)
  * [Continuously measure and improve sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/continuously-measure-improve)
  * [Promote a culture of sustainability](https://docs.cloud.google.com/architecture/framework/sustainability/culture)
  * [Align sustainability practices with industry guidelines](https://docs.cloud.google.com/architecture/framework/sustainability/industry-guidelines)



## Contributors

Author: [Brett Tackaberry](https://www.linkedin.com/in/tackaberry) | Principal Architect

Other contributors: 

  * [Adrien Feudjio](https://www.linkedin.com/in/adrienfeudjio) | | Product Manager, Carbon Footprint
  * [Alex Stepney](https://www.linkedin.com/in/alexstepney/) | Lead Principal Architect 
  * [Daniel Lees](https://www.linkedin.com/in/daniellees) | Cloud Security Architect
  * [Denise Pearl](https://www.linkedin.com/in/denise-pearl) | Global Marketing Lead, Sustainability
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) | Customer Engineer, FSI
  * [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist
  * [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework



[ Next Use low-carbon regions  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
