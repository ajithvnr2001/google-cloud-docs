---
url: https://docs.cloud.google.com/architecture/agentic-ai-system-with-grounding-using-maps/
title: Build trusted AI agents with Google Maps Platform \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:10:28.737170+00:00
---

# Build trusted AI agents with Google Maps Platform  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/agentic-ai-system-with-grounding-using-maps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Build trusted AI agents with Google Maps Platform Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-21 UTC

This document provides a high-level architecture to build a trusted and effective agentic AI system that's grounded in real-world contextual data from Google Maps Platform and Google Calendar. The system builds travel plans for places that users indicate in their prompt. The plan considers the user's schedule, the geographic location of the places, operating hours, and route distances.

The intended audience for this document includes AI architects, developers, and administrators who build and manage agentic AI applications. The document assumes that you have a foundational understanding of AI and ML concepts and cloud architecture.

The deployment section of this document provides a link to a codelab that you can use to learn how to build and test a functional agentic AI system that's based on this architecture.

## Architecture

The following diagram shows an architecture for an app that uses a multi-agent AI system to generate a travel plan for places that a user wants to visit during a day. Users interact with the app through a chat interface. An orchestrator agent gathers the necessary information by invoking specialized agents and then it creates a day plan. The agents run in Gemini Enterprise and their reasoning is grounded by using real-world data from Google Maps Platform and Calendar.

![An architecture for a multi-agent AI system with grounding using data from Google Maps Platform.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-system-with-grounding-using-maps-architecture.svg)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-system-with-grounding-using-maps-architecture.svg)

The architecture in the preceding diagram contains the following components:

  * **Gemini Enterprise** : The core component of the architecture. It hosts the agentic AI system, which contains the following agents:

    * **Orchestrator agent** : Receives user requests through a chat interface, interprets the goal, and then it coordinates with specialized agents to fulfill the request.
    * **Places agent** : Handles location-based tasks, such as finding places and checking whether they are open.
    * **Routes agent** : Handles routing and travel-planning tasks, such as ensuring sufficient time to travel to the required places.
    * **Schedule agent** : Manages scheduling and calendar-related tasks, such as loading the calendar and moving events to accommodate travel time.

All of the agents in this architecture are built by using Agent Development Kit (ADK). The agents run in Agent Runtime on Gemini Enterprise Agent Platform and they use a Gemini model.

  * **Tools and data** : The agents use the following tools to get the data that they need:

    * [**Grounding with Google Maps**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps): Provides real-world geographic context from Google Maps Platform to the Places and Routes agents.
    * [**Places Insights**](https://developers.google.com/maps/documentation/placesinsights/overview): Provides deep, site-specific analytics and information from Google Maps Platform to help the agents create appropriate artifacts based on the meeting type.
    * **Calendar** : Enables the Schedule agent to access and manage calendar events.
  * **Observability** : This component enables monitoring and debugging of agent operations.

    * Agent events are logged in Cloud Logging and they're published to a Firestore database.
    * The architecture includes an event viewer app that's deployed as a Cloud Run service. Administrators can use this app to monitor the logged events and view the agents' thought flow and actions, such as validation of places and routes.



## Products used

This architecture uses the following Google products and tools:

  * [ Google Maps Platform](https://cloud.google.com/maps-platform): A platform that provides mapping, routing, and location search services. 
  * [ Google Calendar](https://workspace.google.com/products/calendar/): A tool for teams and individuals to manage schedules and events. 
  * [ Gemini Enterprise](https://cloud.google.com/gemini-enterprise): A fully-managed secure platform to deploy and manage AI agents within an enterprise. 
  * [Agent Development Kit (ADK)](https://adk.dev/): A set of tools and libraries to develop, test, and deploy AI agents.
  * [ Cloud Logging](https://cloud.google.com/logging): A real-time log management system with storage, search, analysis, and alerting.
  * [ Firestore](https://cloud.google.com/firestore): A NoSQL document database built for automatic scaling, high performance, and ease of application development. 
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.



## Use cases

The following are examples of use cases for this architecture:

  * **Automated corporate travel planning** : An employee needs to plan a trip for a client summit.

    * A Travel agent finds flights and hotels and it makes reservations.
    * A Customer Relationship Management (CRM) agent retrieves the summit address and attendees list.
    * A Schedule agent schedules meetings in the traveler's calendar. The final output is a complete trip itinerary.
  * **Intelligent field service dispatch** : A customer reports a service outage.

    * A CRM agent identifies the customer's contract and location.
    * A Travel agent finds the nearest available technician and optimizes their travel route.
    * A Schedule agent books a service appointment.
  * **Logistics and supply chain coordination** : A logistics manager needs to redirect a shipment due to a weather event.

    * A Logistics agent monitors real-time traffic and weather by using Google Maps Platform.
    * The Logistics agent finds an alternative route and warehouse.
    * A CRM agent notifies the customer about the revised shipment schedule.



## Design considerations

This section describes design factors, best practices, and recommendations to consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, operational efficiency, cost, and performance.

The guidance in this section isn't exhaustive. For more information about design factors and best practices, and for recommendations about building and deploying a multi-agent AI system, see [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system#design_considerations).

### Security, privacy, and compliance

To help address the unique security risks of AI agents, Google recommends an [approach](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) that combines deterministic security controls with dynamic, reasoning-based defenses:

  * **Human oversight** : Incorporate a human-in-the-loop flow in business-critical systems so human supervisors can review outputs and approve, override, or pause agent actions.
  * **[Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)** : Assign each agent a workload-bound identity to enforce least-privilege access control and centrally manage credentials for external tools.
  * **[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)** : Enforce ingress and egress traffic governance, default-deny access policies, and inline prompt and tool inspection with [Model Armor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor).
  * **[Agent Registry](https://docs.cloud.google.com/agent-registry/overview)** : Verify that agents only connect to approved subagents and MCP tools.



### Reliability

To help ensure that your agent configurations meet your reliability requirements, consider the following recommendations:

  * **Validation for critical actions** : Include [human-in-the-loop (HITL)](https://cloud.google.com/discover/human-in-the-loop) validation for critical tasks like booking non-refundable tickets.
  * **Audit trails** : Create clear audit trails for agent decisions by building an observability pipeline with Logging and Pub/Sub.



### Operational efficiency

Establish strong governance with clear roles for each agent and with guidelines for handling data. Use an iterative development process that includes continuous monitoring. This process helps to refine the agents' behavior and it helps to ensure that the behavior is aligned with business requirements.

### Cost optimization

Manage costs by tightly scoping each agent's tasks to prevent open-ended or unnecessary queries. Reduce API calls by using caching for frequently requested data, such as common routes or popular places.

### Performance optimization

The modular, [multi-agent coordinator pattern](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system#coordinator-pattern) in this architecture helps to improve performance by enabling specialized agents to work in parallel. For example, the Places agent can search for locations while the Schedule agent simultaneously checks for calendar conflicts.

When you design the architecture for your agentic AI workload, consider the best practices and recommendations in [Google Cloud Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml).

## Deployment

To learn how to build and test a functional agentic AI system that's based on this architecture, follow the instructions in the codelab, [Build an Itinerary Planning Agent with ADK and Google Maps Grounding](https://codelabs.developers.google.com/next26/maps-grounding). The codelab guides you through the entire deployment process, including the following tasks:

  * Enabling the necessary Google Cloud services.
  * Using ADK to create agents.
  * Configuring the agents to use Grounding with Google Maps for real-world context.
  * Running and testing your agents through a web interface.



## What's next

  * Learn more about [Grounding with Google Maps](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-google-maps).
  * Learn more about [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Kenneth Nevarez](https://www.linkedin.com/in/kenneth-nevarez-1855721) | Developer Relations Engineer, Google Maps Platform

Other contributors: 

  * [Caio Moreira](https://linkedin.com/in/moreirac) | DevX Engineer
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Mike Pegg](https://www.linkedin.com/in/mpegg) | Manager, Developer Relations



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
