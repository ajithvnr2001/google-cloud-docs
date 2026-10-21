---
url: https://docs.cloud.google.com/architecture/framework/
title: Google Cloud Well-Architected Framework \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:12.158312+00:00
---

# Google Cloud Well-Architected Framework  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Google Cloud Well-Architected Framework Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-13 UTC

To view all of the content in the Well-Architected Framework on a single page or to to get a PDF output of the content, see [View on one page](https://docs.cloud.google.com/architecture/framework/printable). 

The Well-Architected Framework provides recommendations to help architects, developers, administrators, and other cloud practitioners design and operate a cloud topology that's secure, efficient, resilient, high-performing, cost-effective, and sustainable.

A cross-functional team of experts at Google validates the recommendations in the Well-Architected Framework. The team curates the Well-Architected Framework to reflect the expanding capabilities of Google Cloud, industry best practices, community knowledge, and feedback from you. For a summary of the significant changes to the Well-Architected Framework, see [What's new](https://docs.cloud.google.com/architecture/framework/whats-new).

The Well-Architected Framework is relevant to applications built for the cloud _and_ for workloads migrated from on-premises to Google Cloud, hybrid cloud deployments, and multi-cloud environments.

## Well-Architected Framework pillars and perspectives

The recommendations in the Well-Architected Framework are organized into pillars and cross-pillar perspectives, as shown in the following diagram.

![Well-Architected Framework.](https://docs.cloud.google.com/static/architecture/framework/images/af-infographic.svg)![Well-Architected Framework.](https://docs.cloud.google.com/static/architecture/framework/images/af-infographic.svg)

  * A _pillar_ in the Well-Architected Framework provides principles and recommendations for a specific non-functional focus area: security, reliability, performance, cost, operations, or sustainability.

  * A _perspective_ in the Well-Architected Framework is a cross-pillar view of recommendations for a specific technology, domain, or sector. The recommendations in a perspective align with the general principles and recommendations in the pillars.

For example, the financial services (FS) perspective recommends a disaster recovery strategy that meets regulatory requirements for data residency. This FS-specific recommendation aligns with the reliability pillar's principle about realistic targets, because the data residency requirements influence the choice of failover region and, consequently, the recovery objectives.




### Pillars

construction [Operational excellence](https://docs.cloud.google.com/architecture/framework/operational-excellence)
    Efficiently deploy, operate, monitor, and manage your cloud workloads.
security [Security, privacy, and compliance](https://docs.cloud.google.com/architecture/framework/security)
    Maximize the security of your data and workloads in the cloud, design for privacy, and align with regulatory requirements and standards.
restore [Reliability](https://docs.cloud.google.com/architecture/framework/reliability)
    Design and operate resilient and highly available workloads in the cloud.
payment [Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization)
    Maximize the business value of your investment in Google Cloud.
speed [Performance optimization](https://docs.cloud.google.com/architecture/framework/performance-optimization)
    Design and tune your cloud resources for optimal performance.
eco [Sustainability](https://docs.cloud.google.com/architecture/framework/sustainability)
    Build and manage cloud workloads that are environmentally sustainable.

### Cross-pillar perspectives

saved_search [AI and ML](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
    A cross-pillar view of technology-specific recommendations for AI and ML workloads.
saved_search [Financial services](https://docs.cloud.google.com/architecture/framework/perspectives/fsi)
    A cross-pillar view of recommendations for FS workloads.

## Agent skills

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in each pillar of the Well-Architected Framework, use the `google-cloud-waf-*` agent skills1 that are available in the [Google Agent Skills repository](https://github.com/google/skills) in GitHub.

To install a specific Well-Architected Framework pillar skill, run the following command in your agent's client or terminal. When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global).
    
    
    npx skills add google/skills --skill SKILL_NAME
    

In the preceding command, replace SKILL_NAME with the name of the skill that you want to install, from the following table.

If you've already installed skills, you can update them to the latest version by running the following command:
    
    
    npx skills update
    

**Note:** If `npx` is not available in your environment, install [Node.js](https://nodejs.org/en/download), which includes `npm` and `npx`.Pillar, and link to skill in GitHub | `SKILL_NAME`  
---|---  
[Operational excellence](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-operational-excellence) | `google-cloud-waf-operational-excellence`  
[Security, privacy, and compliance](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-security) |  `google-cloud-waf-security`  
[Reliability](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-reliability) | `google-cloud-waf-reliability`  
[Cost optimization](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-cost-optimization) | `google-cloud-waf-cost-optimization`  
[Performance optimization](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-performance-optimization) | `google-cloud-waf-performance-optimization`  
[Sustainability](https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-sustainability) | `google-cloud-waf-sustainability`  
**Tip:** To install all of the available Google skills across all your agents and workspaces without being prompted to choose the agents and workspaces, run `npx skills add google/skills --all`

Each Well-Architected Framework skill includes the following information for a specific pillar:

  * An overview of the pillar, its core principles, and links to AI-friendly documentation for each principle.
  * Examples of Google Cloud products and features that are relevant to the pillar.
  * Assessment questions that agents can ask to understand the requirements of a workload.
  * A validation checklist that agents can use to evaluate an architecture's alignment with the principles and recommendations in the pillar.



## Core principles

Before you explore the recommendations in each pillar of the Well-Architected Framework, review the following core principles:

### Design for change

No system is static. The needs of its users, the goals of the team that builds the system, and the system itself are constantly changing. With the need for change in mind, build a development and production process that enables teams to regularly deliver small changes and get fast feedback on those changes. Consistently demonstrating the ability to deploy changes helps to build trust with stakeholders, including the teams responsible for the system, and the users of the system. Using [DORA's software delivery metrics](https://dora.dev/guides/dora-metrics-four-keys/) can help your team monitor the speed, ease, and safety of making changes to the system.

### Document your architecture

When you start to move your workloads to the cloud or build your applications, lack of documentation about the system can be a major obstacle. Documentation is especially important for correctly visualizing the architecture of your current deployments.

Quality documentation isn't achieved by producing a specific amount of documentation, but by how clear content is, how useful it is, and how it's maintained as the system changes.

A properly documented cloud architecture establishes a common language and standards, which enable cross-functional teams to communicate and collaborate effectively. The documentation also provides the information that's necessary to identify and guide future design decisions. Documentation should be written with your use cases in mind, to provide context for the design decisions.

Over time, your design decisions will evolve and change. The change history provides the context that your teams require to align initiatives, avoid duplication, and measure performance changes effectively over time. Change logs are particularly valuable when you onboard a new cloud architect who is not yet familiar with your current design, strategy, or history.

[Analysis by DORA](https://dora.dev/capabilities/documentation-quality/) has found a clear link between documentation quality and organizational performance — the organization's ability to meet their performance and profitability goals.

### Simplify your design and use fully managed services

Simplicity is crucial for design. If your architecture is too complex to understand, it will be difficult to implement the design and manage it over time. Where feasible, use fully managed services to minimize the risks, time, and effort associated with managing and maintaining baseline systems.

If you're already running your workloads in production, test with managed services to see how they might help to reduce operational complexities. If you're developing new workloads, then start simple, establish a minimal viable product (MVP), and resist the urge to over-engineer. You can identify exceptional use cases, iterate, and improve your systems incrementally over time.

### Decouple your architecture

[Research from DORA](https://dora.dev/capabilities/loosely-coupled-teams/) shows that architecture is an important predictor for achieving continuous delivery. Decoupling is a technique that's used to separate your applications and service components into smaller components that can operate independently. For example, you might separate a monolithic application stack into individual service components. In a loosely coupled architecture, an application can run its functions independently, regardless of the various dependencies.

A decoupled architecture gives you increased flexibility to do the following:

  * Apply independent upgrades.
  * Enforce specific security controls.
  * Establish reliability goals for each subsystem.
  * Monitor health.
  * Granularly control performance and cost parameters.



You can start the decoupling process early in your design phase or incorporate it as part of your system upgrades as you scale.

### Use a stateless architecture

A stateless architecture can increase both the reliability and scalability of your applications.

Stateful applications rely on various dependencies to perform tasks, such as local caching of data. Stateful applications often require additional mechanisms to capture progress and restart gracefully. Stateless applications can perform tasks without significant local dependencies by using shared storage or cached services. A stateless architecture enables your applications to scale up quickly with minimum boot dependencies. The applications can withstand hard restarts, have lower downtime, and provide better performance for end users.

* * *

  1. For more information about agent skills standard, see [Agent Skills Overview](https://agentskills.io/home). ↩




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
