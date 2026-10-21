---
url: https://docs.cloud.google.com/architecture/agentic-ai-bidirectional-multimodal-streaming/
title: Agentic AI use case: Enable live bidirectional multimodal streaming \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:31.789307+00:00
---

# Agentic AI use case: Enable live bidirectional multimodal streaming  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/agentic-ai-bidirectional-multimodal-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Agentic AI use case: Enable live bidirectional multimodal streaming Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-04-06 UTC

This document provides a high-level architecture for a live, bidirectional multi-agent AI system on Google Cloud. The system helps users complete technical tasks, such as assembling intricate components, diagnosing equipment malfunctions, or navigating complex repair procedures. The agentic AI system provides grounded technical guidance and automated safety monitoring through a continuous, bidirectional stream of multimodal data.

The intended audience for this document includes architects, developers, and administrators who build and manage AI infrastructure and applications in the cloud. This document assumes that you have a foundational understanding of AI agents and models. The document doesn't provide specific guidance for designing and coding AI agents.

The deployment section of this document lists code samples that you can use to learn how to build and deploy multi-agent AI systems.

## Architecture

The following diagram shows a high-level view of an architecture that uses a multi-agent AI system to enable live, bidirectional multimodal data streaming:

![High-level architecture of a multi-agent AI system that enables bidirectional multimodal data streaming.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-bidirectional-multimodal-streaming-high-level.svg)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-bidirectional-multimodal-streaming-high-level.svg)

The architecture in the preceding diagram has two workflows: technical guidance and safety monitoring.

  * The **technical guidance workflow** enables users to receive real-time, narrated solutions to complex technical inquiries. This workflow uses the [Gemini Live model](https://gemini.google/overview/gemini-live/) to process multimodal streams and coordinate with a subagent to retrieve grounded product information from the knowledge database.
  * The **safety monitoring workflow** provides automated hazard detection to ensure user safety during technical procedures. This workflow uses [Gemini](https://gemini.google/about/) to analyze live video segments, identify potential risks, and trigger immediate warnings through the client dashboard.



The following tabs provide architecture diagrams that show the technical guidance and safety monitoring workflows:

### Technical guidance workflow

The following diagram shows a detailed architecture for a technical guidance workflow.

![Architecture that shows the technical guidance workflow.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-bidirectional-multimodal-streaming-technical-guidance.svg)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-bidirectional-multimodal-streaming-technical-guidance.svg)

The preceding diagram shows the following data flow:

  1. A user initiates a session by making a spoken technical inquiry through the client dashboard. For example, a technician might point their camera at a control panel and ask, "Help, what does this flashing red error light mean?"

  2. The client dashboard establishes a persistent [WebSocket](https://docs.cloud.google.com/run/docs/triggering/websockets) connection between the frontend and the backend server.

  3. WebSocket messages package the raw multimedia data into `Blob` objects. The Agent Development Kit (ADK) [`LiveRequestQueue`](https://google.github.io/adk-docs/streaming/dev-guide/part1/#create-liverequestqueue) component continuously streams the input data to the dispatcher agent.

  4. The dispatcher agent detects audio or visual commands that require technical guidance and it sends the input stream to the [Gemini Live model](https://gemini.google/overview/gemini-live/).

  5. The Gemini Live model searches the raw data to identify _events_. Events are audio keywords, such as "assemble" or "help", or visual cues, such as hand gestures.

Gemini evaluates each event to determine whether it's relevant to the user's inquiry. For example, a hand gesture or filler words might not be relevant, therefore Gemini doesn't process those events.

  6. For each relevant event, Gemini enables [function calling](https://ai.google.dev/gemini-api/docs/live-api/tools#function-calling) to evaluate whether it needs additional context. Depending on whether additional context is needed, either Gemini or an architect agent sends a response back to the dispatcher agent.

     1. If it needs more context, Gemini looks up the architect [agent card](https://a2a-protocol.org/latest/topics/agent-discovery/) to understand how to structure its request.

     2. Gemini sends a structured request to the dispatcher agent. The request contains event details, such as the product type, model number, event type, and attributes.

     3. The dispatcher agent uses the [Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/) to send the structured request to the architect agent.

     4. The architect agent sends the query through a [Serverless VPC Access ](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) connector. The connector lets the agent securely access resources in the Virtual Private Cloud (VPC) network that's used for the storage resources in this architecture.

     5. The Serverless VPC Access connector interacts with the cached data that's stored in [ Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run). If the data isn't available in the cached layer, the architect agent interacts with the Compute Engine instances that host the knowledge database.

     6. The architect agent receives the product information from the data cache or knowledge database. The architect agent sends the product information to Gemini to generate a response. For example, "Error code 3B: Fan malfunction. Recommended action: Check for obstructions."

     7. The architect agent sends the product information back to the dispatcher agent.

If it doesn't need more context, Gemini generates a response to the user's request directly.

  7. The dispatcher agent receives the response from Gemini or from the architecture agent, and it generates a multimodal response:

     1. Uses the Gemini Live model and ADK [`run_live`](https://google.github.io/adk-docs/streaming/dev-guide/part3/) function to generate a multimodal response that contains the technical solution.

     2. Stores the response as a `Blob` object.

     3. Sends the technical solution through the streaming buffer and persistent WebSocket connection to deliver the technical solution to the client dashboard.

  8. The client dashboard extracts the `Blob` data from the technical solution to provide immediate narrated guidance and it updates the UI with relevant transcriptions. The request loop is completed while the active bidirectional stream is maintained.




### Safety monitoring workflow

The following diagram shows a detailed architecture for a safety monitoring workflow.

![Architecture that shows the safety monitoring workflow.](https://docs.cloud.google.com/static/architecture/images/agentic-ai-bidirectional-multimodal-streaming-safety-monitoring.svg)![](https://docs.cloud.google.com/static/architecture/images/agentic-ai-bidirectional-multimodal-streaming-safety-monitoring.svg)

The preceding diagram shows the following data flow:

  1. The client dashboard establishes a persistent [WebSocket](https://docs.cloud.google.com/run/docs/triggering/websockets) connection between the frontend and the backend server to observe the live video stream. The WebSocket message packages this raw multimedia data into `Blob` objects, and sends them continuously to the streaming buffer, using the ADK [`LiveRequestQueue`](https://google.github.io/adk-docs/streaming/dev-guide/part1/#create-liverequestqueue) component. 
  2. The streaming buffer directs the input stream to a [streaming tool](https://google.github.io/adk-docs/streaming/streaming-tools/) that runs in a continuous background loop to detect hazards in the video frame. 
  3. The streaming tool sends the latest video frame from the streaming buffer to Gemini.
  4. Gemini observes the video frames for hazards, such as a bright light or steam. 
     * If no hazard is detected, nothing happens.
     * If a hazard is detected, [Gemini](https://gemini.google/about/) generates a multimodal response containing the hazard type, attributes, and its location and stores it as a `Blob` object. Gemini sends the hazard warning response back to the streaming tool. 
  5. The streaming tool forwards the hazard warning response to the streaming buffer. 
  6. The streaming buffer uses the persistent WebSocket connection to deliver the technical solution to the client dashboard. 
  7. The client dashboard extracts the `Blob` data from the technical solution to provide immediate narrated guidance and updates the UI with relevant transcriptions. This completes the request loop while maintaining the active bidirectional stream. 



## Products used

This reference architecture uses the following Google Cloud products and tools:

  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Gemini](https://ai.google.dev/gemini-api/docs/models): A family of multimodal AI models developed by Google. 
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [Agent Development Kit (ADK)](https://google.github.io/adk-docs/): A set of tools and libraries to develop, test, and deploy AI agents.
  * [ Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/): An open protocol that enables communication and interoperability between agents regardless of their programming language and runtime.
  * [ Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access): A service that lets your serverless environments connect to resources in a Virtual Private Cloud network.
  * [ Virtual Private Cloud (VPC)](https://cloud.google.com/vpc): A virtual system that provides global, scalable networking functionality for your Google Cloud workloads. VPC includes VPC Network Peering, Private Service Connect, private services access, and Shared VPC.
  * [ Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview): A fully managed, in-memory data store service for [Redis](https://redis.io/). 
  * [ Compute Engine](https://cloud.google.com/compute): A secure and customizable compute service that lets you create and run VMs on Google's infrastructure.



For information about selecting alternative components for your agentic AI system including framework, agent runtime, tools, memory, and design patterns, see [Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components).

## Use case

This reference architecture is designed for use cases that require the real-time synthesis of continuous, bidirectional multimodal data streams. The following are examples of use cases for the architecture that is described in this document:

  * **Industrial manufacturing and field maintenance** : Enable hands-free repair of complex machinery by providing technicians with an AI assistant that processes live audio and video from smart glasses. The technician converses with the AI assistant to fetch machine schematics. The AI assistant uses an internal database agent that accesses product documentation to ensure grounded repair and assembly instructions. A concurrent background vision tool monitors the bidirectional stream to proactively warn the technician of mechanical hazards or incorrect assembly steps.
  * **Remote technical support** : Improve customer troubleshooting outcomes by letting users share a live phone camera feed with a multimodal agentic AI system. The bidirectional streaming architecture supports a dynamic conversation where the system observes hardware in real time. If a background vision process identifies a faulty connection, such as a cable in the wrong port, the system uses the low-latency stream to immediately interrupt the user with corrective guidance.



## Design considerations

The following sections provides general recommendations for designing the AI agents and implementing this architecture for production.

### AI agent design

To improve the cost and performance of your agents, consider the following recommendations:

  * **Control loop scripts** : Write system prompts for bi-directional live agents as strict state-machine behavior loops rather than just personality guidelines. The system prompt should explicitly command the agent to stay silent until it's triggered. It should enforce brief, action-first responses so that voice interaction is concise and natural.
  * **Separation of concerns** : Use a dedicated background streaming tool to monitor video feeds independently of the primary agent. The root agent in the architecture is bidirectional and it can instantly interrupt its own speech to broadcast these critical safety warnings to the user. Additionally, if you ask a single agent to constantly monitor a video feed, and it can lead to cognitive overload and hallucinations.
  * **Cost-effective prompting** : The length of your prompts (input) and the generated responses (output) directly affect performance and cost. Write prompts that are short, direct, and provide sufficient context. Design your prompts to get concise responses from the model. For example, include phrases such as "summarize in 2 sentences" or "list 3 key points". For more information, see the [best practices for prompt design](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies#best-practices).



### Production design

To implement this architecture for production, consider the following recommendations:

  * **Ingress security** : To control access to the application, [disable the default `run.app` URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url) of the frontend Cloud Run service and [set up a regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless). In addition to load-balancing incoming traffic to the application, the load balancer handles SSL certificate management. For added protection, you can use [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/integrating-cloud-armor#serverless) to provide request filtering, DDoS protection, and rate limiting for the service.
  * **Access control** : When you configure permissions for the resources in your topology, follow the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege).
  * **Asynchronous buffering** : To decouple incoming audio and video packets from the model's inference engine, use a thread-safe, asynchronous [First-In-First-Out (FIFO) buffer](https://en.wikipedia.org/wiki/FIFO_\(computing_and_electronics\)). This buffer acts as a multiplexer that ensures the system remains responsive to user interruptions without freezing the user interface during heavy computation.
  * **Data ingestion costs** : To reduce token costs and prevent context window exhaustion, use a low-frequency frame sampling, such as 2 frames per second, and compress all of the data to Base64 JPEG files.
  * **In-memory caching** : To achieve sub-millisecond read speeds, use an in-memory [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run) database for the architect agent's schematic vault. This implementation minimizes latency, prevents silences during real-time voice interactions, and provides a scalable single source of truth.
  * **WebSocket security** : Protect sensitive multimodal data, such as voice prints and video, by enforcing [TLS encryption](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview) for all bidirectional WebSocket connections.
  * **Secure A2A communication** : 
    * Use [authenticated extended agent cards](https://a2a-protocol.org/latest/specification/#3111-get-extended-agent-card) to secure A2A communication.
    * Attach [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-discovery-1_0.html) identity tokens to requests. The OIDC identity tokens let you use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to validate that only authorized agents access the data.
  * **Resource allocation** : Depending on your performance requirements, configure the [memory limits](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) and [CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu) to be allocated to the Cloud Run service.



For more information about design factors, best practices, and recommendations for building and deploying a multi-agent AI system, see [Multi-agent AI system in Google Cloud](https://docs.cloud.google.com/architecture/multiagent-ai-system#design_considerations).

## Deployment

To deploy a sample implementation of this architecture, try the following Codelabs:

  * [Building an ADK bidirectional streaming agent Codelab](https://codelabs.developers.google.com/way-back-home-level-3/instructions#0): Build a single-agent AI system that processes a live video stream to recognize specific user gestures.
  * [Live bidirectional multi-agent system Codelab](https://codelabs.developers.google.com/way-back-home-level-4/instructions#0): Build a multi-agent AI system that uses bidirectional streaming for real-time voice and video interaction. The system includes a proactive streaming tool for continuous safety monitoring.



## What's next

  * Learn how to [start and manage live sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api/start-manage-session).
  * Explore the [introduction to ADK Gemini Live API Toolkit](https://google.github.io/adk-docs/streaming/dev-guide/part1/).
  * Learn how to [host AI agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents).
  * Learn about how to [choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components).
  * Explore learning resources to build and deploy enterprise-grade agents with [Gemini Enterprise Agent Ready (GEAR)](https://developers.google.com/program/gear).
  * Explore more [agentic AI architecture guides](https://docs.cloud.google.com/architecture/agentic-ai-overview).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Christina Lin](https://www.linkedin.com/in/weimeilin/) | Developer Relations Engineer Manager
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer



Other contributors: 

  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Olivier Bourgeois](https://www.linkedin.com/in/olivi-eh/) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
