---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/connection-overview/
title: Container orchestrator connection overview \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:20:17.894202+00:00
---

# Container orchestrator connection overview  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/connection-overview/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  Container orchestrator connection overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/connection-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/connection-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/connection-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/connection-overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/connection-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/connection-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/connection-overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/connection-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/connection-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/connection-overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/connection-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/connection-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/connection-overview)

This overview describes the critical connection and access configurations for AlloyDB Omni databases deployed on a Kubernetes cluster, and it details how to establish flexible and secure connectivity. Connection includes the following areas: 

  * **Networking:** learn how to configure AlloyDB Omni database clusters for either internal access using a Kubernetes `ClusterIP` Service or external access using a `LoadBalancer`, including how to restrict external traffic using source Classless Inter-Domain Routing (CIDR) ranges.
  * **Connection pooling:** use the `PgBouncer` Custom Resource to implement connection pooling for efficient connection management and reduced load on database instances.
  * **Authentication and authorization:** secure access using supported methods like password-based and Active Directory and Kerberos integration, alongside fine-grained control implemented through Kubernetes network policies and PostgreSQL roles.



## Networking

You can configure AlloyDB Omni database clusters—managed by the `DBCluster` custom resource—for internal or external access.

For more details on `DBCluster` networking options, refer to the [DBCluster CRD Reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.6.0/dbcluster).

### Internal connectivity

By default, AlloyDB Omni instances are exposed using a Kubernetes `ClusterIP` Service. This ensures that the instances are only accessible to other applications running in the same Kubernetes cluster. You can find the endpoint for the primary instance in the `DBCluster` status.

### External connectivity

To allow connections from outside the Kubernetes cluster, update the `DBCluster` specification:

  * **Enable external traffic:** set `spec.allowExternalIncomingTraffic: true`, which typically provisions a `LoadBalancer` Service.
  * **Implement fine-grained control:** use `spec.primarySpec.dbLoadBalancerOptions`. For example, on Google Cloud, set `gcp.loadBalancerType: "External"` to obtain an IP address accessible from the public internet.



### Restrict access

To secure external connections, use `spec.primarySpec.sourceCidrRanges` to define a list of allowed CIDR ranges. The system blocks any connections originating from IP addresses outside these ranges.

## Connection pooling with PgBouncer

To manage connections efficiently and reduce instance load, use PgBouncer. The AlloyDB Omni Operator provides a `PgBouncer` Custom Resource (CR) to simplify this operation.

For comprehensive details on configuring PgBouncer, see the [PgBouncer CRD Reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer).

### Deployment and configuration

Create a `PgBouncer` resource and reference your database cluster in `spec.dbclusterRef`. Key parameters in `spec.parameters` include the following:

  * `pool_mode`: determines when connections are reused (`session`, `transaction`, or `statement`).
  * `default_pool_size`: server connections per user and database.
  * `max_client_conn`: maximum allowed client connections.
  * `max_db_connections`: maximum connections opened to the AlloyDB Omni instance.



### Expose PgBouncer

Use `spec.serviceOptions.type` to control visibility.

  * `ClusterIP`: internal cluster access only.
  * `LoadBalancer`: external access. You can restrict this with `spec.serviceOptions.loadBalancerSourceRanges` using CIDR blocks.



## Authentication and authorization

AlloyDB Omni supports multiple methods to verify identities and control access.

### Authentication methods

  * **Password-based:** Standard PostgreSQL username and password authentication. The administrator password is typically provided using a Kubernetes Secret, as shown in the [Full DBCluster Sample](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/samples#full_dbcluster).
  * **Active Directory and Kerberos:** Managed using the `UserDefinedAuthentication` CR. This supports GSSAPI and LDAP group synchronization using the following:

    * `spec.keytabSecretRef`: for Kerberos keytabs.
    * `spec.ldapConfiguration`: for group mapping and LDAP settings.
    * `spec.pgHbaEntries`: to configure `pg_hba.conf` rules–for example, `gss` or `ldap`.

For more information, see the [UserDefinedAuthentication CRD Reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.6.0/userdefinedauthentication).

  * **Certificate-based (planned):** support for passwordless TLS certificate authentication is planned for a future release.




### Authorization and access control

  * **Kubernetes network policies:** define pod-level rules to secure traffic between applications and AlloyDB Omni or `PgBouncer` pods.
  * **Source CIDR ranges:** restrict traffic at the `LoadBalancer` level.
  * **PostgreSQL roles:** use standard database roles and privileges to manage user permissions after the users are authenticated.



## What's next

  * Review the [DBCluster CRD Reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.6.0/dbcluster) for all configuration options.
  * Learn to deploy connection pooling with the [PgBouncer CRD Reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.6.0/pgbouncer).
  * Understand Active Directory integration in the [UserDefinedAuthentication CRD Reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.6.0/userdefinedauthentication).
  * See a complete example in the [Full DBCluster Sample](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/samples#full_dbcluster).
  * Consult Kubernetes documentation on [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
