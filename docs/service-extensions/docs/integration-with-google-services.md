---
url: https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services/
title: Integration with Google services \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:38.280909+00:00
---

# Integration with Google services  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Integration with Google services Stay organized with collections  Save and categorize content based on your preferences. 

Service Extensions lets [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services#supported-lbs-gservices) send [Cloud Load Balancing callouts](https://docs.cloud.google.com/service-extensions/docs/callouts-overview) from the data processing path to supported Google services. This page describes such integrations.

For information about other types of callouts, see [Callouts to user-managed services](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-callouts).

## Integration with Model Armor

[Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) enhances the security of AI applications by enforcing runtime controls on LLM prompts and responses. This mitigates critical risks, including prompt injection attacks, the generation of harmful content, and the potential loss of sensitive data.

You can [configure a traffic extension to call the Model Armor Google service](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services#configure-traffic-ma) to uniformly apply and enforce security policies to screen LLM prompts and responses for your networking applications.

See [how this integration works](https://docs.cloud.google.com/security-command-center/docs/model-armor-gke-integration).

## Integration with Agent Gateway

[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) provides centralized networking and governance for AI agent communication. You can use Agent Gateway to enforce access controls and security policies on the traffic between agents and tools, such as third-party Model Context Protocol (MCP) servers.

Agent Gateway supports Service Extensions to evaluate requests and delegate authorization decisions to Google services—such as Identity-Aware Proxy and Model Armor—or custom authorization services. Authorization extensions let you inspect, modify, or block agent traffic in real time before the traffic reaches its destination.

For more information, see [Delegate authorization with Service Extensions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/delegate-authorization).

## Supported Application Load Balancers for callouts to Google services

Service Extensions supports traffic extensions by using callouts to selected Google services for the following [Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer):

Application Load Balancers | Model Armor (traffic extensions by using callouts)  
---|---  
Global external Application Load Balancer |   
Regional external Application Load Balancer |   
Regional internal Application Load Balancer |   
Cross-region internal Application Load Balancer |   
Classic Application Load Balancer |   
  
## What's next

  * [Configure an extension to call a Google service](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services)
  * [Delegate authorization with Service Extensions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/delegate-authorization)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
