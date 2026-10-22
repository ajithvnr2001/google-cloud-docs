---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/remote-agent-security/
title: Remote Agent security \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:44.044726+00:00
---

# Remote Agent security  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/remote-agent-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Remote Agent security

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document describes how Google Security Operations secures communication between its components, specifically focusing on the agents and the Publisher service. The system employs a multi-layered approach using encryption, digital signatures, and one-way communication to ensure data integrity and confidentiality.

## High-level security measures

The following outlines the security measures flow:

  * **Encrypted communication** : All data is encrypted in transit between Google SecOps, the Publisher, and the agents.
  * **Agent authentication** : The Publisher maintains a strict allowlist of agents who are authorized to communicate with it. Each agent has a unique application key for authentication. Unauthorized agents are blocked from communication.
  * **Digital signatures** : All data sent from the agent is digitally signed. This signature ensures the data's integrity and authenticity, guaranteeing it hasn't been tampered with in transit.
  * **One-way communication** : Communication is one-way, initiated by the agents or the Google SecOps server. Neither the server nor the agents have open inbound ports; the Publisher can't initiate a connection to them unless it has been polled.
  * **Data deletion** : All data is automatically deleted from the Publisher after a configurable period, which is set to three days by default.
  * **Penetration testing** : All the data on both the Publisher and the agent is tested.



## Data exchange flow

The following steps outline the end-to-end process for an agent to collect and deliver data:

  1. Google SecOps server publishes remote tasks and pushes them to the Publisher.
  2. The Agent polls for new tasks and collects them from the Publisher.
  3. The agent executes the new task, collects the requested data, and pushes it back to the Publisher.
  4. The Google SecOps server polls the Publisher for new data and pulls it to the server.



## Encryption flow

The communication employs a hybrid encryption model to ensure secure data exchange:

  * A unique symmetric key is generated for each job.
  * Google SecOps uses the agent's pre-provisioned public key to encrypt the symmetric key.
  * The agent receives the encrypted key and uses its corresponding private key to decrypt it.
  * The agent then uses this decrypted symmetric key for the bulk encryption of the job's data.
  * The Publisher handles only encrypted data; it doesn't have access to any encryption keys.



## Jobs polling

  * The Remote Agent polls every five seconds to check for pending jobs.
  * Once a job is completed, its details are removed from the system.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
