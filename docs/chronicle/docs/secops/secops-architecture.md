---
url: https://docs.cloud.google.com/chronicle/docs/secops/secops-architecture/
title: Google SecOps architecture and data flows \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:27.049798+00:00
---

# Google SecOps architecture and data flows  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/secops-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google SecOps architecture and data flows

Supported in:

Google SecOps 

Modern security environments generate massive amounts of telemetry across cloud-native infrastructure, microservices, and distributed endpoints. Legacy Security Information and Event Management (SIEM) architectures often struggle to scale with these data volumes, resulting in slow queries and fragmented visibility.

The Google Security Operations platform provides a unified, high-performance security analytics layer. Built on the same infrastructure that powers Google's core global services, it ingests and queries petabytes of security telemetry with sub-second latency while eliminating the legacy distinction between hot and cold data tiers.

This document describes the Google SecOps architecture and data flows, covering ingestion, UDM normalization, YARA-L threat detection, and automated response.

## Convergence of intelligence, analytics, and response

Google SecOps unifies historically separate security operations capabilities. It combines SIEM analytics and Security Orchestration, Automation, and Response (SOAR) into a tightly coupled platform. Additionally, it embeds threat intelligence from Google Threat Intelligence and VirusTotal along with generative AI capabilities powered by Gemini directly into investigation and detection workflows.

## Platform architecture overview

Google SecOps operates as a specialized, cloud-native security plane built on top of core Google Cloud infrastructure. It inherits the scalability, durability, and performance properties of underlying Google services, including Spanner and Colossus.

### System context

Google SecOps serves as the central operational plane for your security environment, managing data across three primary stages:

  * **Inputs** : Ingests telemetry from hybrid environments, including on-premises collectors (such as the [BindPlane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent)), cloud provider [APIs](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api), and direct third-party Software-as-a-Service (SaaS) connectors.
  * **Processing core** : Normalizes raw telemetry into the structured UDM schema, evaluates events using the YARA-L detection engine, and orchestrates workflows using the SOAR case management engine.
  * **Outputs** : Delivers actionable security intelligence and AI triage insights to analysts while sending automated containment commands back to target environments through APIs and remote agents.



The following diagram illustrates the system context and data flows.

![High-level platform architecture and ecosystem context](https://docs.cloud.google.com/chronicle/images/architecture/arch-105-high-level-platform-architecture.jpg)

### Infrastructure advantage

A key architectural advantage of Google SecOps is its unified hot storage model. Legacy architectures move older telemetry to cold storage, slowing queries or requiring manual rehydration. In contrast, Google SecOps retains all ingested telemetry in an active, index-searchable hot state for up to 12 months. This design lets you run queries across a full year of historical data with the same performance as querying the last hour.

## Data collection and normalization pipeline

Google SecOps uses a [high-throughput ingestion pipeline](https://docs.cloud.google.com/chronicle/docs/ingestion/log-ingestion-and-parsing) that transforms raw, unstructured logs into the structured [Unified Data Model (UDM)](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview). During normalization, the pipeline enriches each event with contextual metadata from the [Entity Context Graph](https://docs.cloud.google.com/chronicle/docs/event-processing/entity-graph).

### Collection architecture

Data ingestion occurs across three primary vectors:

  * **Collectors** : Agent-based collectors (such as the [BindPlane agent](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent) or OpenTelemetry agents) deployed within local networks to aggregate syslog and packet data. Collectors buffer, compress, and encrypt telemetry at the transport layer (TLS) before forwarding it to Google SecOps.
  * **Ingestion APIs** : Direct [REST API endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api) that ingest structured and unstructured telemetry from cloud services, custom applications, and serverless pipelines.
  * **Third-party integrations** : Built-in, pull-based connectors that retrieve logs, alerts, and directory data directly from external SaaS platforms and cloud APIs (such as Microsoft 365 or Microsoft Entra ID).



### Data collection and preparation pipeline flow

The following diagram details the specific transformation steps from raw data to UDM format.

![Data collection and preparation pipeline flow](https://docs.cloud.google.com/chronicle/images/architecture/arch-212-data-ingest-and-preparation-pipeline-flow.jpg)

## Unified Data Model schema overview

The [Unified Data Model (UDM)](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview) normalizes disparate vendor logs into a single, structured schema. This standard representation simplifies analytics and search by ensuring that equivalent entities (such as IP addresses, usernames, or file hashes) share consistent field paths across all log sources.

### UDM schema architecture

The UDM uses a strongly typed, hierarchical schema to represent security events and entities. It organizes data into the following core logical structures:

  * **Metadata** : Context about the log event itself, including the event timestamp, ingestion time, vendor product name, and event type.
  * **Principal** : The acting entity that initiated the activity (such as the originating user, host, IP address, or process).
  * **Target** : The entity directly affected by the activity (such as the target file, destination host, or user account).
  * **Source, intermediary, and observer** : Secondary network participants (such as forwarding proxies, firewalls, or routing hops) involved in the transaction.
  * **Network** : Network protocol attributes and transaction artifacts (including application protocols, DNS queries, and HTTP request details).
  * **Security result** : The action or severity outcome reported by the security device (such as `ALLOWED`, `BLOCKED`, or `QUARANTINED`).
  * **Extensions** : Vendor-specific custom fields and key-value pairs that fall outside the standard core schema. For details on mapping definitions and parser development, see [Configure custom parsers](https://docs.cloud.google.com/chronicle/docs/event-processing/configure-custom-parsers) and [Important UDM fields](https://docs.cloud.google.com/chronicle/docs/reference/important-udm-fields).



### UDM class diagram

The following diagram provides a structural blueprint of the UDM.

![UDM class diagram](https://docs.cloud.google.com/chronicle/images/architecture/arch-302-udm-class.jpg)

## Search architecture

Google SecOps provides powerful search mechanisms tailored to different investigation workflows. You can query normalized telemetry across hot storage, perform pattern matching against unparsed raw logs, or search structured case data. For optimization guidance, see [UDM search best practices](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search-best-practices).

The following table summarizes the primary search capabilities available across the platform:

Search type | Architectural function  
---|---  
**[UDM search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)** | The primary structured search engine that queries normalized, indexed UDM events across the 12-month hot window. It enables multi-field filtering, aggregations, and correlations across disparate log sources.  
**Raw log scan** | Scans the original, unparsed text strings of ingested logs. This capability supports regular expression (`regex`) and substring searches for artifacts and custom parameters not mapped to specific UDM syntax.  
**[Natural language search](https://docs.cloud.google.com/chronicle/docs/investigation/generate-udm-search-queries-gemini)** | Uses Gemini AI to translate natural language questions directly into formal UDM search syntax, speeding up query authoring and investigation workflows.  
**[Case search](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview)** | A specialized search engine within the response layer that queries investigative cases, alerts, playbooks, and annotated entity metadata within the SOAR database.  
  
## Threat detection and response loop

The Google SecOps architecture creates a continuous feedback loop between detection analytics and automated response. Detection rules generate high-fidelity alerts that trigger response workflows, while investigation outcomes provide feedback used to refine and tune future detection logic.

### Detection funnel architecture

The detection engine uses a multi-stage funnel approach to distill massive volumes of raw security telemetry into high-fidelity alerts:

  1. **Ingestion and normalization** : Raw logs are continuously ingested and formatted into standard UDM event structures.
  2. **Enrichment** : Events are dynamically enriched with alias mappings, contextual asset data, and global threat intelligence from sources like Google Threat Intelligence.
  3. **Detection evaluation** : The stateful [YARA-L 2.0 engine](https://docs.cloud.google.com/chronicle/docs/yara-l/getting-started) evaluates enriched events against behavioral and threat rules across extended time windows. For rule optimization guidelines, see [YARA-L best practices](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-best-practices).
  4. **Prioritization and grouping** : Matched detections are aggregated into alerts, assigned dynamic risk scores, and grouped into unified cases.



By combining contextual asset data with threat intelligence, this funnel strategy filters out harmless anomalies (reducing false positives) and highlights true threats (reducing false negatives), helping your security team focus on actionable incidents.

![Remediation loop](https://docs.cloud.google.com/chronicle/images/architecture/arch-903-remediation-loop.jpg)

### Automated remediation and feedback loop

The detection and response pipeline combines stateful rule evaluation with automated triage and containment:

  1. **Continuous evaluation** : Enriched UDM telemetry streams through the stateful YARA-L 2.0 detection engine.
  2. **Case creation and AI triage** : When a rule condition is met, Google SecOps generates an alert and opens a case. An AI-powered [Triage and Investigation Agent](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent) executes dynamic searches and threat intelligence lookups to evaluate the findings.
  3. **Automated playbook execution** : If the AI triage confirms a true positive, the platform triggers automated response playbooks (such as isolating an endpoint or suspending a user account through remote agents). If classified as a false positive, the case is automatically closed.
  4. **Continuous tuning** : Remediation outcomes and analyst triage verdicts loop back to refine detection thresholds and reduce future false positives.

![Remediation loop](https://docs.cloud.google.com/chronicle/images/architecture/arch-403-remediation-loop.jpg)

## Threat detection layer

The YARA-L 2.0 engine evaluates incoming UDM telemetry using a multi-stage streaming pipeline to detect behavioral anomalies and multi-event attack patterns across extended time windows. You can also [generate and refine YARA-L rules using Gemini](https://docs.cloud.google.com/chronicle/docs/detection/generate-yara-l-with-gemini).

The processing lifecycle for each YARA-L rule follows five distinct evaluation stages:

  1. **Ingestion (`Ingest`)**: Enriched UDM events enter the detection evaluation pipeline in real time.
  2. **Filtering (`Filter`)**: Incoming events are evaluated against the rule's event criteria (`events` section). Events that don't match are discarded, while matching events pass through to stateful evaluation.
  3. **Match windowing (`Window`)**: Matching events are grouped by specified correlation keys across a defined time window (ranging from seconds up to 12 months). The engine tracks multiple concurrent stateful timers (`TimerStart` to `TimerEnd`) as events accumulate.
  4. **Condition evaluation (`Condition`)**: When the match window closes or triggers, the engine evaluates the threshold requirements and mathematical expressions defined in the rule's `condition` section (such as event counts, distinct thresholds, or cross-data joins).
  5. **Triggering (`Trigger`)**: If the condition evaluates to `True`, the engine generates a detection, triggering an alert and opening or updating a case in the response layer. If `False`, the state is cleared without triggering an alert.



### Rule execution state machine

The following diagram illustrates the lifecycle of a rule execution.

![Rule execution state machine](https://docs.cloud.google.com/chronicle/images/architecture/arch-502-rule-execution-lifecycle.jpg)

## Response architecture and remote execution

Google SecOps SOAR represents the response pillar of the platform. It operates as an orchestration engine above the analytics layer to ingest alerts, triage cases, and execute automated response workflows.

### Orchestration, automation, and investigation

The response layer includes specialized tools designed to streamline Security Operations Center (SOC) workflows across investigation, case management, and playbook automation:

  * **Case management** : Group related alerts into [unified cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/cases-overview), sort and filter incident queues, assign tasks, and collaborate on investigations with full audit tracking.
  * **Playbook designer** : Build [automated response playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/whats-on-the-playbooks-screen) using a visual, no-code drag-and-drop canvas with prebuilt integration actions.
  * **Integrated development environment (IDE)** : Use the built-in, code-based [IDE](https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/using-the-ide) to write custom Python scripts, modify existing action integrations, and debug complex automation workflows.
  * **Investigative views and graph investigator** : Visualize attack pathways and entity relationships using graph-based investigation views. Dedicated entity summaries (such as Asset, IP Address, Hash, Domain, and User views) surface relevant timeline events instantly.
  * **Dashboards and reporting** : Track SOC operational metrics, analyst workload, and mean time to respond (MTTR) using out-of-the-box dashboards or custom reporting widgets.



#### SOAR component architecture

The following diagram illustrates how incoming alerts flow into the case management engine and trigger automated remediation workflows across visual playbooks and custom IDE integrations.

![SOAR component architecture](https://docs.cloud.google.com/chronicle/images/architecture/arch-663-soar-component-architecture.jpg)

### Remote agent architecture

To execute remediation actions within private networks (such as on-premises data centers or virtual private clouds), Google SecOps relies on a secure, outbound-only [remote agent architecture](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent).

Under this model, the Google SecOps platform never initiates inbound connections to your private environment:

  1. **Task initiation** : When a playbook action requires local execution, Google SecOps publishes the instruction across a secure publisher queue hosted in Google Cloud.
  2. **Asynchronous polling** : The remote agent deployed inside your private environment continuously polls the publisher queue over an outbound, TLS-encrypted connection.
  3. **Local execution** : When a task instruction is retrieved, the remote agent executes the required action locally against internal security tools or network endpoints (such as disabling an account or blocking a firewall port).
  4. **Status reporting** : Once completed, the remote agent returns the action status and execution logs to the publisher queue over TLS, where it is retrieved and displayed in the SOAR case view.

![Remote agent architecture](https://docs.cloud.google.com/chronicle/images/architecture/arch-603-remote-agent-architecture.jpg)

## Security, compliance, and shared responsibility

As a cloud-native platform, Google SecOps operates under a shared responsibility model: Google is responsible for the security _of_ the platform, while you are responsible for security _in_ the platform.

### Shared responsibility model

Google SecOps inherits the core security design, compute capabilities, and storage architecture of Google Cloud infrastructure. Under this model:

  * **Google manages:** Physical data center security, underlying cloud infrastructure, platform availability, and default encryption of data at rest and in transit.
  * **You manage:** Data governance, [access controls and data RBAC](https://docs.cloud.google.com/chronicle/docs/administration/datarbac-overview) configured through Identity and Access Management (IAM), custom detection rules, and tenant compliance settings.



All compliance requirements, data residency rules, and access policies are inherited and enforced from your organization hierarchy down through folders and projects to your compliance-controlled tenant.

### Compliance and enterprise readiness

To meet strict regulatory and organizational governance requirements, Google SecOps offers compliance-controlled tenants. These tenants enforce rigorous security standards through Assured Workloads, supporting both regulatory compliance frameworks and technical data protection packages.

**Supported regulatory compliance frameworks:**

  * **FedRAMP:** Moderate and High impact levels (`FEDRAMP_MODERATE`, `FEDRAMP_HIGH`)
  * **DoD Impact Levels:** IL4 and IL5 (`IL4_AND_IL5`)
  * **Healthcare and Financial:** HIPAA and PCI DSS (`HIPAA`, `PCI_DSS`)



To deploy a compliance-controlled tenant, link your Google SecOps instance to a Google Cloud project located within an Assured Workloads folder configured for the required control package.

![Assured Workloads configuration](https://docs.cloud.google.com/chronicle/images/architecture/arch-805-compliance-assured-workloads.jpg)

### Data residency and access transparency

Google SecOps enforces strict logical tenant isolation and supports Access Transparency to give you verifiable control and audit visibility over administrative data access.

**Supported data security and residency packages:**

  * **Customer-managed encryption keys (CMEK):** [Control and manage the keys](https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops) used to encrypt data at rest (`CMEK_V1`).
  * **Advanced data residency:** Enforce regional data residency boundaries and administrative access controls (`DRZ_ADVANCED`).
  * **VPC Service Controls:** Establish secure, customized perimeters around your cloud security resources using [VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops) (`VPC-SC`).



The platform's security architecture relies on a four-layer inheritance model, where your administrative security controls build on the hardened foundations of core Google infrastructure:

![Data residency and access transparency](https://docs.cloud.google.com/chronicle/images/architecture/arch-703-data-residency-and-access-transparency.jpg)

**The four-layer security stack:**

  1. **Customer security control layer** : Your top-tier administrative controls, including role-based access controls (RBAC) managed through Identity and Access Management (IAM), Customer-Managed Encryption Keys (CMEK), and regional data residency policies.
  2. **Platform security layer** : Logical tenant isolation, default encryption for data at rest and in transit (TLS), and Access Transparency audit logging.
  3. **Google infrastructure layer** : Core compute and storage infrastructure, including Borg cluster management, Colossus distributed storage, and Spanner global databases.
  4. **Physical security layer** : Foundational security supported by Google enterprise data centers, multi-factor biometric controls, and custom Titan security chips (`roots of trust`).



For example, when Access Transparency is enabled, if a Google support or engineering specialist accesses your tenant data to resolve a support ticket, they must submit a valid cryptographic access justification. This access request is recorded securely and made visible in your audit logs in near real-time.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
