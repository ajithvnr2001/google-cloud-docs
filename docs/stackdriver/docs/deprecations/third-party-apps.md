---
url: https://docs.cloud.google.com/stackdriver/docs/deprecations/third-party-apps/
title: Third-party integrations deprecation \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:21.082809+00:00
---

# Third-party integrations deprecation  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/deprecations/third-party-apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Third-party integrations deprecation Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** There will be no new feature development or support for new operating systems for the legacy Monitoring agent. We recommend that you use the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) for new workloads and eventually transition your existing VMs to use the Ops Agent. We strongly recommend against using the Monitoring agent on Windows. 

The following table lists the third-party integrations that are unsupported in the legacy Monitoring Agent starting at version `6.0.0` and their related decommission schedules.

You can continue to collect metrics for most of these applications by [migrating](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition#migrate_legacy) to Ops Agent's [3rd party application integrations](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party).

Integration name | Deprecated | Unsupported as of | Details  
---|---|---|---  
Cassandra | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
CouchDB | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
Elasticsearch | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
HBase | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
Kafka | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
MongoDB | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
PostgreSQL | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
RabbitMQ | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
Riak | February 28, 2019 | April 09, 2020 | No alternative solution available  
Tomcat | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
Varnish | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
ZooKeeper | February 28, 2019 | April 09, 2020 | Migrate to use [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
