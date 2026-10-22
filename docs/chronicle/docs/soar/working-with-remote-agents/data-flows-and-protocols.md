---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/data-flows-and-protocols/
title: Review data flows and protocols \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:19.470919+00:00
---

# Review data flows and protocols  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/data-flows-and-protocols/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Review data flows and protocols

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document details the architecture of the Remote Agent solution, defining the roles of the three core components and illustrating the TLS-secured, asynchronous data flow used for remote action execution and alert ingestion.

## Component architecture

The Remote Agent architecture is built from the following three main components:

Component | Functionality and security | Communication  
---|---|---  
Google SecOps | Initiates tasks and retrieves final results. Doesn't communicate directly with the Remote Agent. | Communicates with the Publisher over TLS on port 443.  
Publisher | Managed service (by Google SecOps) acting as a secure intermediary. Stores temporary, encrypted execution data, metadata, and scripts/dependencies. Logs records (non-sensitive). | Binds to port 443 for communication with Google SecOps and the Remote Agent.  
Remote Agent | Deployed in the remote environment. Communicates with third-party security products to execute actions and pull alerts. Stores connector information (Gzip) and a local config file. | Communicates with the Publisher over TLS on port 443.  
  
## Remote data flow (task execution)

When you configure an integration or connector to run remotely, the data flow is asynchronous and task-based:

  1. **Task publication** : Google SecOps publishes a new task to the Publisher Server.
  2. **Task query** : The Remote Agent (installed in the remote environment) continuously queries the Publisher for new tasks (either for remote actions or remote connector alert pulls).
  3. **Task execution** : When the Remote Agent finds a new task, it fetches the complete task data (containing alert context and action execution data) and begins execution.
  4. **Result publication** : The Remote Agent publishes the action results, including generated attachments, and operations performed, back to the Publisher.
  5. **Result retrieval** : The Google SecOps server polls the Publisher. Once the task status is marked complete, Google SecOps retrieves the final result data and attachments, performing any necessary server-side residual tasks.
  6. **Cleanup (ACK)** : When data is successfully ingested into Google SecOps, an Acknowledgment (ACK) is returned to the Publisher and then relayed to the agent. This ACK confirms data flow completion, triggering file deletion on both the Publisher and the agent.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
