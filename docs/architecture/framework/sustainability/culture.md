---
url: https://docs.cloud.google.com/architecture/framework/sustainability/culture/
title: Promote a culture of sustainability \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:18.080402+00:00
---

# Promote a culture of sustainability  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/sustainability/culture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Promote a culture of sustainability Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-28 UTC

This principle in the sustainability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability) provides recommendations to help you build a culture where teams across your organization are aware of and proficient in sustainability practices.

## Principle overview

To apply sustainability practices, you need more than tools and techniques. You need a cultural shift that's driven by education and accountability. Your teams need to be aware of sustainability concerns and they must have practical proficiency in sustainability practices.

  * _Awareness of sustainability_ is the contextual knowledge that every architectural and operational decision has tangible effects on sustainability. Teams must recognize that the cloud isn't an abstract collection of virtual resources, but it's driven by physical resources that consume energy and produce carbon emissions.
  * _Proficiency in sustainability practices_ includes knowledge to interpret carbon emissions data, experience with implementing cloud sustainability governance, and technical skills to refactor code for energy efficiency.



To align sustainability practices with organizational goals, your teams need to understand how energy usage by cloud infrastructure and software contributes to the organization's carbon footprint. Well-planned training helps to ensure that all of your stakeholders—from developers and architects to finance professionals and operations engineers—understand the sustainability context of their daily work. This shared understanding empowers teams to move beyond passive compliance to active optimization, which makes your cloud workloads sustainable-by-design. Sustainability becomes a core non-functional requirement (NFR) like other requirements for security, cost, performance, and reliability.

## Recommendations

To build awareness of sustainability concerns and proficiency in sustainability practices, consider the recommendations in the following sections.

### Provide business context and alignment with organizational goals

Sustainability isn't just a technical exercise; it requires a cultural shift that aligns individual actions with the environmental mission of your organization. When teams understand the _why_ behind sustainability initiatives, they are more likely to adopt the initiatives as core principles rather than as optional tasks.

#### Connect to the big picture

Help your teams understand how individual architectural choices—such as selecting a low-carbon region or optimizing a data pipeline—contribute to the organization's overall sustainability commitments. Explicitly communicate how these choices affect the local community and the industry. Transform abstract carbon metrics into tangible indicators of progress toward corporate social responsibility (CSR) goals.

For example, a message like the following informs teams about the positive outcome and executive recognition of a decision to migrate a workload to a low-carbon region and to use a power-efficient machine type. The message references the [CO2 equivalent](https://en.wikipedia.org/wiki/Global_warming_potential), which helps your team contextualize the impact of carbon reduction measures.

> _"By migrating our data analytics engine to the us-central1![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) region and upgrading our clusters to C4A Axion-based instances, we fundamentally changed our carbon profile. This shift resulted in a 75% reduction in the carbon intensity of our data analytics engine, which translates to a reduction of 12 metric tons of CO2 equivalent this quarter. This migration had a significant impact on our business goals and was included in the Q4 newsletter to our board."_

#### Communicate financial and sustainability goals

Transparency is critical for aligning sustainability practices with goals. To the extent feasible, widely share sustainability goals and progress across the organization. Highlight sustainability progress in the annual financial statements. Such communication ensures that technical teams view their work as a vital part of the organization's public-facing commitments and financial health.

#### Embrace a shared fate mindset

Educate teams about the collaborative nature of cloud sustainability. Google is responsible for the sustainability _of_ the cloud, which includes the efficiency of the infrastructure and data centers. You (the customer) are responsible for sustainability of your resources and workloads _in_ the cloud. When you frame this collaboration as a partnership of shared fate, you reinforce the understanding that your organization and Google work together to achieve optimal environmental outcomes.

### Provide role-based sustainability training

To ensure that sustainability is a practical skill rather than a theoretical concept, tailor the sustainability training to specific job roles. The sustainability tools and techniques that a data scientist can use are very different from those available to a FinOps analyst, as described in the following table:

Role | Training focus  
---|---  
Data scientists and ML engineers | **Carbon-intensity of compute** : Demonstrate the differences between running AI training jobs on [legacy systems](https://en.wikipedia.org/wiki/Legacy_system) versus purpose-built AI accelerators. Highlight how a model with fewer parameters can produce the required accuracy with significantly lower energy consumption.  
Developers | **Code efficiency and resource consumption** : Illustrate how high-latency code or inefficient loops translate directly to extended CPU runtime and increased energy consumption. Emphasize the importance of lightweight containers and the need to optimize application performance to reduce the environmental footprint of software.   
Architects | **Sustainable by design** : Focus on region selection and workload placement. Show how choosing a ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) region with a high percentage of renewable energy (like `northamerica-northeast1`) fundamentally changes the carbon profile of your entire application stack before you write a single line of code.  
Platform engineers and operations engineers | **Maximizing utilization** : Emphasize the environmental cost of idle resources and over-provisioning. Present scenarios for automated scaling and right-sizing to ensure that cloud resources are used efficiently. Explain how to create and track sustainability-related metrics like utilization and how to translate metrics like compute time into equivalent metrics of carbon emissions.   
FinOps | **Unit economics of carbon** : Focus on the relationship between financial spend and environmental impact. Demonstrate how GreenOps practices let an organization track carbon per transaction, which helps to make sustainability a key performance indicator (KPI) that's as critical as conventional KPIs like cost and utilization.  
Product managers | **Sustainability as a feature** : Demonstrate how to integrate carbon-reduction goals into product roadmaps. Show how simplified user journeys can help to reduce the energy consumption by both cloud resources and end-user devices.  
Business leaders | **Strategic alignment and reporting** : Focus on how cloud sustainability affects environmental, social, and governance (ESG) scores and public reputation. Illustrate how sustainability choices help to reduce regulatory risk and fulfill commitments to the community and industry.  
  
### Advocate for sustainability and recognize success

To sustain long-term progress, you need to move beyond internal technical fixes and begin influencing your partners and the industry.

#### Empower managers to advocate for sustainability

Provide managers the data and permissions that they need to prioritize environmental impact similar to other business metrics like speed-to-market and cost. When managers have this data, they begin to view sustainability as a quality and efficiency standard rather than as a nice-to-have capability that slows production. They actively advocate for new cloud provider features—such as more granular carbon data and newer, greener processors in specific regions.

#### Align with industry standards and frameworks

To ensure that your sustainability efforts are credible and measurable, align internal practices with recognized global and regional standards. For more information, see [Align sustainability practices with industry guidelines](https://docs.cloud.google.com/architecture/framework/sustainability/industry-guidelines).

### Incentivize sustainability efforts

To ensure that sustainability becomes an enduring part of the engineering culture, teams must realize the value of prioritizing sustainability. Transition from high-level goals to specific, measurable KPIs that reward improvement and efficiency.

#### Define carbon KPIs and NFRs

Treat sustainability as a core technical requirement. When you define carbon KPIs, such as grams of CO2 equivalent per million requests or carbon-intensity per AI training run, you make the impact on sustainability visible and actionable. For example, integrate sustainability into the NFRs for every new project. In other words, just as a system must meet a specific latency or availability target, the system must also stay within a defined carbon emissions budget.

#### Measure return on effort

Help your teams identify high-impact, low-effort sustainability wins—such as shifting a batch job to a different region—versus a complex code refactoring exercise that might provide minimal gains. Provide visibility into the return on effort (ROE). When a team chooses a more efficient processor family, they must know exactly how much carbon emission they avoided relative to the time and effort that's required to migrate to the new processor.

#### Recognize and celebrate carbon reduction

Sustainability impact is often hidden in the background of infrastructure. To build the momentum for sustainability progress, make successes visible to the entire organization. For example, use annotations in monitoring dashboards to mark when a team deployed a specific sustainability optimization. This visibility lets teams point to data in the dashboard and claim recognition for their successes.

[ Previous arrow_back  Continuously measure and improve  ](https://docs.cloud.google.com/architecture/framework/sustainability/continuously-measure-improve)

[ Next Align with industry guidelines  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/sustainability/industry-guidelines)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-28 UTC."],[],[]] 
