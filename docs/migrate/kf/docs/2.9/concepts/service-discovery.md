---
url: https://docs.cloud.google.com/migrate/kf/docs/2.9/concepts/service-discovery/
title: Service discovery \u00a0|\u00a0 Kf 2.9 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:07.108960+00:00
---

# Service discovery  |  Kf 2.9  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.9/concepts/service-discovery/

Version 2.9

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
  * [ 2.9 ](https://docs.cloud.google.com/migrate/kf/docs/2.9)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.9/getting-started)



Send feedback 

#  Service discovery Stay organized with collections  Save and categorize content based on your preferences. 

This document is an overview of Kubernetes DNS-based service discovery and how it can be used with Kf.

## When to use Kubernetes service discovery with Kf

Kubernetes service discovery can be used by applications that need to locate backing services in a consistent way regardless of where the application is deployed. For example, a team might want to use a common URI in their configuration that always points at the local SMTP gateway to decouple code from the environment it ran in.

Service discovery helps application teams by:

  * Reducing the amount of per-environment configuration.
  * Decoupling client and server applications.
  * Allowing applications to be portable to new environments.



You can use Kubernetes service discovery when:

  * Applications use their container's DNS configurations to resolve hosts.
  * Applications are deployed with their backing services in the same Kubernetes cluster or namespace.
  * Backing services have an associated [Kubernetes service](https://kubernetes.io/docs/concepts/services-networking/service/). Kf creates these for each app.
  * Kubernetes NetworkPolicies allow traffic between an application and the Kubernetes service it needs to communicate with. Kf creates these policies in each Kf space.



You **should not** use Kubernetes service discovery if:

  * Applications need to failover between multiple clusters.
  * You override the DNS resolver used by your application.
  * Applications need specific types of load balancing.



## How Kubernetes service discovery works

Kubernetes service discovery works by [modifying the DNS configuration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery) of containers running on a Kubernetes node. When an application looks up an unqualified domain name, the local DNS resolver will first attempt to resolve the name in the local cluster.

Domains without multiple parts will be resolved against the names of Kubernetes services in the container's namespace. Each Kf app creates a Kubernetes service with the same name. If two Kf apps `ping` and `pong` were deployed in the same Kf space, then `ping` could use the URL `http://pong` to send traffic to the other service.

Domains with a single dot will be resolved against the Kubernetes services in the Kubernetes namespace with the same name as the label after the dot. For example, if there was a PostgreSQL database with a `customers` service in the `database` namespace, an application in another namespace could resolve it using `postgres://customers.database`.

## How to use service discovery with Kf

Kubernetes DNS based service discovery can be used in any Kf app. Each Kf app creates a Kubernetes service of the same name, and each Kf space creates a Kubernetes namespace with the same name.

  * Refer to a Kf app in the current space using `protocol://app-name`.
  * Refer to a Kf app in a different space using `protocol://app-name.space-name`.
  * Refer to a Kf app in the current space listening on a custom port using `protocol://app-name:port`.
  * Refer to a Kf app in a different space listening a custom port using `protocol://app-name.space-name:port`.

**Note:** For Kubernetes services managed by Kf, TCP port 80 always maps to the same port in the app's `PORT` environment variable. This is even true if the Kf app doesn't serve HTTP traffic.

## Best practices

Applications that are going to be the target of DNS based service discovery should have frequent [health checks](https://docs.cloud.google.com/migrate/kf/docs/2.9/how-to/manifest#health_check_types) to ensure they are rapidly added and removed from the pool of hosts that accept connections.

Applications using DNS based service discovery should not cache the IP addresses of the resolved services because they are not guaranteed to be stable.

If environment specific services exist outside of the cluster, they can be resolved using Kubernetes DNS if you set up [ExternalName Kubernetes services](https://kubernetes.io/docs/concepts/services-networking/service/#externalname). These Kubernetes services provide the same resolution capabilities, but return a CNAME record to redirect requests to an external authority.

## Comparison to Eureka

Eureka is an open source client-side load-balancer created by Netflix. It is commonly used as part of the [Spring Cloud Services](https://docs.pivotal.io/spring-cloud-services/3-1/common/service-registry/index.html) service broker. Eureka was [built to be a regional load balancer and service discovery mechanism](https://github.com/Netflix/eureka/wiki/Eureka-at-a-glance#what-is-eureka) for services running in an environment that caused frequent disruptions to workloads leading to unstable IP addresses.

Eureka is designed as a client/server model. Clients register themselves with the server indicating which names they want to be associated with and periodically send the server heartbeats. The server allows all connected clients to resolve names.

In general, you should use Kubernetes DNS rather than Eureka in Kubernetes for the following reasons:

  * DNS works with all programming languages and applications without the need for libraries.
  * Your application's existing health check will be reused reducing combinations of errors.
  * Kubernetes manages the DNS server, allowing you to rely on fewer dependencies.
  * Kubernetes DNS respects the same policy and RBAC constraints as the rest of Kubernetes.



There are a few times when deploying a Eureka server would be advantageous:

  * You need service discovery across Kubernetes and VM based applications.
  * You need client based load-balancing.
  * You need independent health checks.



## What's next

  * [Read more about service discovery in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery).
  * Learn about [Service Directory](https://docs.cloud.google.com/service-directory), a managed offering similar to Eureka.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
