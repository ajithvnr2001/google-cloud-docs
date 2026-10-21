---
url: https://docs.cloud.google.com/app-topology/overview/
title: App Topology overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:39:59.179556+00:00
---

# App Topology overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ Guides ](https://docs.cloud.google.com/app-topology/overview)



Send feedback 

#  App Topology overview Stay organized with collections  Save and categorize content based on your preferences. 

App Topology lets you query data about your resources and applications across Google Cloud, and then correlates data in the query results. For example, you can view all agents that have a specific vulnerability.

By bringing together data across multiple sources, App Topology helps you to understand relationships, dependencies, and context in one place.

The App Topology API provides programmatic access for running queries. App Topology also supports running queries and viewing topology graphs of the query results in other Google Cloud products.

App Topology supports queries for Google Cloud resources in a Google Cloud project and queries for [App Hub applications](https://docs.cloud.google.com/app-hub/docs/key-concepts#application) in a project or an app-enabled folder. When you create App Hub applications in a folder, you can view resource relationships across projects in that folder when you run queries in App Topology.

## Domains

The App Topology API provides several domains for specific types of questions. Each domain lets you query a specific set of underlying data.

  * `SRE` \- For Site Reliability Engineers (SREs) and other users who focus on the runtime health and reliability of services. For example, you can view open alerts for deployment events, and analyze traffic between application components or agentic resources. This domain includes all resource data supported by App Topology.

  * `DEVOPS` \- For DevOps engineers who manage the software supply chain and infrastructure configuration. You can check build artifacts for known vulnerabilities before they are deployed, and trace provenance from source code to production.

  * `SECURITY` \- For security engineers and managers who audit access, vulnerabilities, and software supply chain risk. You can examine access paths and identify running services and infrastructure that are affected by vulnerabilities.




## Topologies in other products

The App Topology API lets you query data programmatically. The API also provides data for displaying topology graphs in other Google Cloud products.

Use the following table to help you decide which topology tool to use:

Topology tool | When to use it  
---|---  
App Topology API | Run queries to correlate observability, security, and deployment data using the Google Cloud CLI or the REST API. Agents can use the remote App Topology MCP server to query data.   
[App Topology](https://docs.cloud.google.com/hub/docs/app-topology) in Cloud Hub | Analyze data relationships across observability, security, and deployment domains. 

  * View App Hub services and workloads grouped together by application
  * Use predefined queries or create your own queries
  * View data for individual projects and app-enabled folders

  
[Application topology](https://docs.cloud.google.com/monitoring/docs/application-topology) in Cloud Monitoring | View real-time observability data such as traffic, latency, and service dependencies based on telemetry. 

  * View App Hub services and workloads grouped together by application
  * Register discovered services and workloads
  * Provides a focused view of application performance and traffic
  * View data for individual projects and app-enabled folders

  
[Agent topology](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/topology) | Analyze observability, security, and deployment data for agents and AI applications. 

  * Use predefined queries or custom queries to explore agent health, resource relationships, dependencies, and compliance with policy. 
  * View traffic to and from a selected agent or AI application.

  
  
## Integration with Gemini Cloud Assist

App Topology provides [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) with the context of your resources and their relationships. When you perform an investigation with Gemini Cloud Assist, this contextual information helps improve the relevancy and quality of root cause analysis.

## App Topology pricing

Starting September 15, 2026, the App Topology API transitions to a usage-based billing model that includes a daily free data usage allotment.

The new billing model applies to all App Topology API usage, including topology graphs generated within Cloud Hub, Gemini Enterprise Agent Platform, and Cloud Monitoring. The system will meter and bill your usage according to the following rates:

| Daily Free Allotment (Per Project) | Additional Usage Rates  
---|---|---  
Queries | 100 queries | $0.01 per query  
Nodes in topology graphs | 15,000 nodes | $0.00075 per node  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
