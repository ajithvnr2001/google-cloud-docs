---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/service-config/
title: Runtime service configuration overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:25.632001+00:00
---

# Runtime service configuration overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/service-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Runtime service configuration overview Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/service-config.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/service-config.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/service-config.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/service-config.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/service-config.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/service-config.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/service-config.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/service-config.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/service-config.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/service-config.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/service-config.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/service-config.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/service-config.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/service-config.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/service-config.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/service-config.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/service-config.html)



The Apigee hybrid runtime plane is made up of a variety of services. Each service is deployed on nodes within your Kubernetes cluster, and each one can be configured using the [`overrides.yaml` file](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/customize-services).

#### Runtime architectural diagram

The following image shows how each of the runtime services interacts with other services in hybrid:

![alt_text](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.17/images/arch-runtime-apigee-connect.png)

The following table summarizes the runtime services:

Service | Description | Configuration Object | Implemented As | Scope  
---|---|---|---|---  
[Apigee Connect](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#connectagent) | Apigee Connect allows the Apigee hybrid management plane to connect securely to the MART service in the runtime plane without requiring you to expose the MART endpoint on the internet. If you use Apigee Connect, you do not need to configure the MART ingress gateway with a host alias and an authorized DNS certificate. | [`connectAgent`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#connectagent) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Kubernetes cluster  
[Apigee Ingress Gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/managing-ingress) | Apigee Ingress gateway routes incoming traffic through that endpoint to the correct message processor. By default, it generates a `LoadBalancer` service with external endpoints. | [`apigeeIngressGateway`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#apigeeingressgateway)  
[`ingressGateways`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ingressgateways) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Kubernetes cluster  
[Apigee Operators](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/apigee-deployment-services) | Apigee Operators (AO) creates and updates low level Kubernetes and Istio resources that are required to deploy and maintain the ApigeeDeployment (AD) configuration. For example, the controller carries out the release of message processors and validates the AD configuration before making it persistent in Kubernetes cluster. | [`ao`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#ao) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Kubernetes cluster  
[Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-config) | Acts as a runtime datastore that provides Apigee local persistent storage for KMS, OAuth, KVMs, and caching for the runtime plane. You can have separate Cassandra rings for KMS, OAuth, KVMs, and caching.  
**apigee-cassandra-default** pods are the pods running the Hybrid Cassandra database on a Kubernetes cluster. One or more pods together make a cluster that reads, writes, and stores persistent data for Apigee Hybrid.  
**apigee-cassandra-user-setup** pod initializes and configures the users and roles for the Cassandra database. These roles are used by Cassandra and Runtime components to read and write data to the Hybrid Cassandra database.  
**apigee-cassandra-schema-setup** pod initializes and configures the database schema of the Hybrid Cassandra database. This pod is for setting up Cassandra keyspace and table definitions with the Hybrid Cassandra database. | [`cassandra`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#cassandra) | [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) | Organization (one or more orgs)  
[Guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/guardrails) | Validates that required conditions are satisfied before allowing Runtime services to be created. Guardrails pods are created when you apply the Apigee hybrid charts with Helm `install` or `update` commands. | [guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/guardrails) | [Kubernetes pod](https://kubernetes.io/docs/concepts/workloads/pods/) | Cluster (one or more organizations in the same cluster)  
[Logger](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/logging) | Extracts log files and sends the data to the monitoring application associated with your Google Cloud account (currently Cloud Operations). | [`logger`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#logger) | [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) | Cluster (one or more organizations in the same cluster)  
[Management API for Runtime data (MART)](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/what-is-hybrid#mart) | Exposes an endpoint to administer data entities on the runtime plane, such as KMS (API keys and OAuth tokens), quotas, KVMs, and API products. MART services are scoped to a single organization. | [`mart`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#mart) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Organization  
[Message Processor](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/what-is-hybrid#about-the-runtime-plane) | Consumes rolling updates from the management plane to provide API request processing and policy execution on the runtime plane. Each Message Processor is scoped to a single environment. | [`runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#runtime) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Environment  
[Metrics](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/metrics-collection) | Collects operations metrics that you can use to monitor the health of hybrid services, to set up alerts, and so on. | [`metrics`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#metrics) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Cluster (one or more organizations in the same cluster)  
[Redis](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/what-is-hybrid) | Redis is used for storing cluster-level rate limit counts used for distributed rate limiting used for SpikeArrest policies that use effectiveCount option to synchronize request counts across message processors. | [`redis`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#redis) | [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) and [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) (both) | Cluster (one or more organizations in the same cluster)  
[Synchronizer](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/what-is-hybrid#synchronizer) | Fetches configuration data about an API environment from the management plane to the runtime plane. A Synchronizer can poll one or more environments in the same or different organizations. | [`synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#sync) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Environment  
[Universal Data Collection Agent (UDCA)](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/other-data-collection) | Extracts analytics and deployment status data and sends it to the UAP service in the management plane so that you can access it with the management UI. | [`udca`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#udca) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Environment  
[Watcher](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/what-is-hybrid) | Watcher periodically executes task in the runtime cluster such as reconfiguring Ingress routes, checking ingress status for new proxy deployments, fetching deployment status from Message Processors and Ingress in order to report status to Management Plane. | [`watcher`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#watcher) | [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) | Cluster (one or more organizations in the same cluster)  
  
Most services make socket connections with other internal or external services that you should be aware of. For more information, see [Hybrid ports](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/ports).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
