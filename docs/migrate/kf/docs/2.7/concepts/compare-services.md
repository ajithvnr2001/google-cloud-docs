---
url: https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/compare-services/
title: Compare Cloud Foundry and Kf services \u00a0|\u00a0 Kf 2.7 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:18:04.350598+00:00
---

# Compare Cloud Foundry and Kf services  |  Kf 2.7  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/compare-services/

Version 2.7

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.7 ](https://docs.cloud.google.com/migrate/kf/docs/2.7)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.7/getting-started)



Send feedback 

#  Compare Cloud Foundry and Kf services Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a side-by-side comparison of the various services available on Cloud Foundry (CF) and those that Kf integrates with on Google Cloud.

**Note:** This guide does not attempt to compare the syntax or semantics of the SDK, APIs, or command-line tools provided by CF and Kf.Service category | Service | CF | Kf  
---|---|---|---  
Platform | Infrastructure Orchestrator | BOSH | [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine)  
| PaaS | CF Application Runtime (CFAR) | [Kf](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
Data management | Google Cloud Service Broker | Google Cloud Service Broker Tile | [Kf Cloud Service Broker for Google Cloud](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/cloud-sb-overview)  
| AWS Service Broker | AWS Service Broker Tile | [AWS Service Broker Helm Chart](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/aws-sb)  
| MySQL | MySQL Tile | [Service Brokers](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/about-service-brokers)  
| MongoDB | MongoDB Tile | [Service Brokers](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/about-service-brokers)  
| RabbitMQ | RabbitMQ Tile | [Service Brokers](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/about-service-brokers)  
| Redis | Redis Tile | [Service Brokers](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/about-service-brokers)  
| Eureka | Spring Cloud Services Tile | [Service Discovery](https://docs.cloud.google.com/migrate/kf/docs/2.7/concepts/service-discovery)  
| Spring Cloud Config | Spring Cloud Services Tile | [Spring Cloud Config](https://docs.cloud.google.com/migrate/kf/docs/2.7/how-to/deploying-spring-cloud-config)  
Operations tooling | Continuous Integration (CI) | Concourse Tile | [Concourse Helm Chart](https://github.com/concourse/concourse-chart)  
Logging | Google Cloud | Google Cloud Firehose Nozzle | [Cloud Logging](https://docs.cloud.google.com/logging)  
| Elastic | Elastic Firehose Nozzle | [Elastic Stack Agent](https://docs.cloud.google.com/solutions/partners/monitoring-gke-on-prem-with-the-elastic-stack)  
| Splunk | Splunk Firehose Nozzle | [Splunk Connect](https://docs.cloud.google.com/solutions/logging-anthos-with-splunk-connect)  
| Metrics | CF App Metrics | [Cloud Monitoring](https://docs.cloud.google.com/monitoring)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
