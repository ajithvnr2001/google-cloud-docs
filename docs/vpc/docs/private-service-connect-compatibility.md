---
url: https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility/
title: Private Service Connect compatibility \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:21.570326+00:00
---

# Private Service Connect compatibility  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private Service Connect compatibility

Private Service Connect lets service consumers establish private connections to managed services, which are provided by service producers. Because there are multiple types of Private Service Connect connections, understanding their capabilities helps you design a supported network architecture before you deploy Private Service Connect as either a consumer or producer.

For information about Google and third-party services that support Private Service Connect, see the lists of supported Google and third-party services.

To evaluate compatibility and options for different types of Private Service Connect connections—including details about supported load balancers, IP versions, protocols, and other features—see the supported connection types.

## Services

Private Service Connect lets you connect to two types of services:

  * **Published services** : VPC-hosted services that run on Compute Engine VMs in VPC networks. Published services can be managed by Google, third parties, or your own organization.
  * **Google APIs** : APIs and services that run on Google's production infrastructure.



For more information about these service types, see the following sections.

### Google published services

Google published services are services that are deployed in a Google-managed VPC network and made available to service consumers through a service attachment.

**Note:** Although regional endpoints for Google APIs (`SERVICE.REGION.rep.googleapis.com`) can be accessed through a service attachment, the corresponding service runs on Google's production infrastructure, not a VPC network. For a list of regional endpoints, see [Regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

Google service | Access provided  
---|---  
[AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview) | Lets you [connect to AlloyDB for PostgreSQL instances](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect).  
[Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) | Lets you [expose APIs managed by Apigee to the internet](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/psc-overview). Also lets you connect privately from Apigee to [backend target services](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints).  
[BigQuery connections SAP Datasphere](https://docs.cloud.google.com/bigquery/docs/connect-to-sap-datasphere) | Lets you increase security when [using BigQuery to send queries to SAP Datasphere](https://docs.cloud.google.com/bigquery/docs/connections-with-network-attachment).   
[BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) | Lets you [use BigQuery Data Transfer Service for Oracle](https://docs.cloud.google.com/bigquery/docs/oracle-transfer).   
[Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview) | Lets you [connect Cloud Data Fusion instances to resources in VPC networks](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect#configure-psc).  
[Managed Service for Apache Airflow 2](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview) | Lets you [access the Managed Airflow tenant project](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-service-connect).  
[Managed Airflow 3](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview) | Lets you [access the Managed Airflow tenant project](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#comparison).  
[Cloud FTP](https://docs.cloud.google.com/cloud-ftp/overview) | Lets you [transfer files to and from Cloud Storage by using SSH File Transfer Protocol (SFTP)](https://docs.cloud.google.com/cloud-ftp/connect-to-internal-server).  
[Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/introduction) | Lets you [access your Cloud SQL database privately](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect). Lets you [ automate creating connections to Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#create-endpoint-automatically) through service connectivity automation.  
[Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) | Lets you [access private workstation clusters](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters#enable_private_cluster_connectivity).  
[Database Migration Service](https://docs.cloud.google.com/database-migration/docs/overview) | Lets you [migrate your data to Google Cloud](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-private-service-connect).  
[Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/overview) | Lets you [access Dataproc Metastore services](https://docs.cloud.google.com/dataproc-metastore/docs/psc-ilb).  
[Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) | Lets you [receive events from Eventarc](https://docs.cloud.google.com/eventarc/docs/vpc-endpoints/route-vpc-internal-endpoint-events).  
[Google Cloud Contact Center as a Service (CCaaS)](https://docs.cloud.google.com/contact-center/ccai-platform/docs) |  Lets your agents and supervisors [privately access the Google Cloud Contact Center as a Service interface](https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-ingress).  Lets your Google Cloud Contact Center as a Service instance [privately access other systems via a VPC network](https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-egress).   
[Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview) | Lets you [access Managed Service for Apache Kafka clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).  
[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) public clusters and private clusters | Lets you [ privately connect nodes and the control plane for a public or private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#control-plane).  
[Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/about-connectors) | Lets Integration Connectors [access your managed services privately](https://docs.cloud.google.com/integration-connectors/docs/configure-psc).  
[Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) | Lets you [access Looker (Google Cloud core) instances](https://docs.cloud.google.com/looker/docs/looker-core-create-psc).  
[Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/overview) | Lets you [automate creating connections to Memorystore for Redis Cluster instances](https://docs.cloud.google.com/memorystore/docs/cluster/networking) through service connectivity automation.  
[Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview) | Lets you [automate creating connections to Memorystore for Valkey instances](https://docs.cloud.google.com/memorystore/docs/valkey/networking) through service connectivity automation.  
[Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) | Lets you [access supported Vertex AI services](https://docs.cloud.google.com/vertex-ai/docs/general/netsec-overview#access-methods).  
  
### Third-party published services

Third-party published services are services that are deployed in a VPC network that is managed by the third party and is made available to service consumers through a service attachment.

Third-party service | Access provided  
---|---  
[Aiven](https://docs.aiven.io/docs/platform) | Provides [private access to Aiven Kafka clusters](https://docs.aiven.io/docs/platform/howto/use-google-private-service-connect).  
[Axoflow](https://axoflow.com/axoflow-platform) | Provides [private access to Axoflow Platform](https://axoflow.com/docs/axoflow/onboard-hosts/secure-cloud-sources/google-psc).  
[Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/overview) | Provides [private access to Citrix DaaS](https://docs.citrix.com/en-us/citrix-daas/install-configure/connections/connection-gcp).  
[ClickHouse](https://clickhouse.com/docs/en/cloud/overview) | Provides [private access to ClickHouse services](https://clickhouse.com/docs/en/manage/security/gcp-private-service-connect).  
[Confluent Cloud](https://www.confluent.io/) | Provides [private access to Confluent Cloud clusters](https://docs.confluent.io/cloud/current/networking/private-links/gcp-private-service-connect.html#use-gc-private-service-connect).  
[Couchbase](https://docs.couchbase.com/home/cloud.html) | Provides [private access to Capella clusters](https://docs.couchbase.com/cloud/security/add-gcp-private-link.html).  
[Databricks](https://www.databricks.com/) | Provides [private access to Databricks clusters](https://docs.gcp.databricks.com/administration-guide/cloud-configurations/gcp/private-service-connect.html).  
[Datadog](https://www.datadoghq.com) | Provides [private access to Datadog intake services](https://docs.datadoghq.com/agent/guide/gcp-private-service-connect/?site=us5).  
[Datastax Astra](https://www.datastax.com/products/datastax-astra) | Provides [private access to Datastax Astra DB databases](https://docs.datastax.com/en/astra-serverless/docs/manage/devops/devops-gcp-private-endpoints.html).  
[dbt](https://docs.getdbt.com/docs/introduction) | Provides [private access to dbt](https://docs.getdbt.com/docs/platform/secure/private-connectivity/gcp/gcp-overview).  
[Elasticsearch](https://www.elastic.co/) | Provides [private access to Elastic Cloud](https://www.elastic.co/guide/en/cloud/current/ec-traffic-filtering-psc.html).  
[Groq](https://console.groq.com/docs/overview) | Provides [private access to Groq Cloud](https://console.groq.com/docs/security/gcp-private-service-connect).  
[JFrog](https://jfrog.com/) | Provides [private access to JFrog SaaS instances](https://jfrog.com/help/r/jfrog-hosting-models-documentation/setting-up-gcp-private-service-connect).  
[MongoDB Atlas](https://www.mongodb.com/atlas) | Provides [private access to MongoDB Atlas](https://www.mongodb.com/docs/atlas/security-private-endpoint/?cloud-provider=gcp).  
[Neo4j Aura](https://neo4j.com/docs/aura/) | Provides [private access to Neo4j Aura](https://neo4j.com/docs/aura/platform/security/#_gcp_private_endpoints).  
[Pega Cloud](https://docs.pega.com/bundle/pega-cloud/page/pega-cloud/pc/pcs-pega-cloud-introduction.html) | Provides [private access to Pega Cloud](https://docs.pega.com/bundle/pega-cloud/page/pega-cloud/pc/pcs-gcp-private-connectivity-privateserviceconnect.html).  
[Redis Enterprise Cloud](https://docs.redis.com/latest/rc/) | Provides [private access to Redis Enterprise clusters](https://docs.redis.com/latest/rc/security/private-service-connect/).  
[Redpanda](https://www.redpanda.com/) | Provides [private access to Redpanda Cloud](https://docs.redpanda.com/redpanda-cloud/networking/configure-private-service-connect-in-cloud-ui/).  
[Snowflake](https://docs.snowflake.com/user-guide/private-service-connect-google) | Provides [private access to Snowflake](https://docs.snowflake.com/en/user-guide/private-service-connect-google).  
[Splunk Cloud Platform](https://www.splunk.com/en_us/products/splunk-cloud-platform.html) | Provides [private access to Splunk Cloud Platform](https://help.splunk.com/en/splunk-cloud-platform/administer/manage-users-and-security/10.5.2605/private-connectivity/about-private-connectivity).  
[Striim](https://www.striim.com/docs/en/what-is-striim-.html) | Provides [private access to Striim Cloud](https://www.striim.com/docs/en/using-private-service-connect-with-google-cloud-adapters.html).  
[Zenoss](https://docs.zenoss.io/start/get-started.html) | Provides [private access to Zenoss Cloud](https://docs.zenoss.io/cz/collectors/gcp-private-service-connect.html).  
  
### Self-managed published services

You can publish your own services by using the following configurations:

Source of your service | Service producer configuration | Service consumer configuration  
---|---|---  
[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) | [ Publish the service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) | 

  * [ Create an endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) to access the published service
  * [ Create a backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) to access the published service

  
[ Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) |  [ Publish the service:](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net) Route requests to your service through an internal `LoadBalancer` service and publish the service through a `ServiceAttachment` | 

  * [ Create an endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) to access the published service
  * [ Create a backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) to access the published service

  
[Cloud Run](https://docs.cloud.google.com/run/docs/securing/private-networking) and [ Cloud Run functions (2nd gen)](https://docs.cloud.google.com/functions/docs/networking/network-settings) | Choose one of the following:

  * `run.app` URL: you don't need additional configuration
  * `cloudfunctions.net` URL (for Cloud Run functions only): you don't need additional configuration
  * Published service: Route requests to your service through a [ load balancer with a Serverless NEG](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless) and [publish the service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer)

| Choose the consumer option that corresponds with the service producer configuration:

  * `cloudfunctions.net` and `run.app` URLs: [ Create an endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) to access those URLs
  * Published service:
    * [ Create an endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) to access the published service
    * [ Create a backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) to access the published service

  
[ Cloud Run functions (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings) | `cloudfunctions.net` URL: you don't need additional configuration  |  [ Create an endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) to access `cloudfunctions.net` URLs   
[ App Engine](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine) | You don't need additional configuration  | [ Create an endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) to access `appspot.com` URLs  
  
### Global Google APIs

Endpoints can target a bundle of global Google APIs or a single regional Google API. Backends can target a single global Google API or a single regional Google API.

#### Bundles of global Google APIs

You can use Private Service Connect endpoints to send traffic to a bundle of Google APIs.

When you create an endpoint to access Google APIs and services, you choose which bundle of APIs you need access to—**All APIs** (`all-apis`) or **VPC-SC** (`vpc-sc`):

  * The `all-apis` bundle provides access to most Google APIs and services, including all `*.googleapis.com` service endpoints.

  * The `vpc-sc` bundle provides access to [APIs and services that support VPC Service Controls.](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#supported_products)


**Note:** These bundles provide access to the same APIs that are available through the [Private Google Access VIPs](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options)—`all-apis` is equivalent to `private.googleapis.com` and `vpc-sc` is equivalent to `restricted.googleapis.com`. 

The API bundles support only HTTP-based protocols over TCP (HTTP, HTTPS, and HTTP/2). All other protocols, including MQTT and ICMP are not supported.

API bundle | Supported services | Example usage  
---|---|---  
`all-apis` | Enables API access to most Google APIs and services regardless of whether they are supported by VPC Service Controls. Includes API access to Google Maps, Google Ads, Google Cloud, and most other Google APIs, including the lists below. Does not support Google Workspace web applications such as Gmail and Google Docs. Does not support any interactive websites. Domain names that match: 

  * `accounts.google.com` (only supports paths needed for OAuth authentication of service accounts; user account authentication is interactive and not supported)
  * `*.aiplatform-notebook.cloud.google.com`
  * `*.aiplatform-notebook.googleusercontent.com`
  * `appengine.google.com`
  * `*.appspot.com`
  * `*.backupdr.cloud.google.com`
  * `backupdr.cloud.google.com`
  * `*.backupdr.googleusercontent.com`
  * `backupdr.googleusercontent.com`
  * `*.cloudfunctions.net`
  * `*.cloudproxy.app`
  * `*.composer.cloud.google.com`
  * `*.composer.googleusercontent.com`
  * `*.datafusion.cloud.google.com`
  * `*.datafusion.googleusercontent.com`
  * `*.dataproc.cloud.google.com`
  * `dataproc.cloud.google.com`
  * `*.dataproc.googleusercontent.com`
  * `dataproc.googleusercontent.com`
  * `*.developerconnect.dev`
  * `dl.google.com`
  * `gcr.io` or `*.gcr.io`
  * `*.googleapis.com`Excludes `*.rep.googleapis.com` [regional and multi-regional endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).
  * `*.gke.goog`
  * `gstatic.com` or `*.gstatic.com`
  * `*.kernels.googleusercontent.com`
  * `*.ltsapis.goog`
  * `*.notebooks.byoid.googleusercontent.com`
  * `*.notebooks.cloud.google.com`
  * `notebooks.cloud.google.com`
  * `*.notebooks.googleusercontent.com`
  * `packages.cloud.google.com`
  * `pkg.dev` or `*.pkg.dev`
  * `pki.goog` or `*.pki.goog`
  * `*.run.app`
  * `source.developers.google.com`
  * `storage.cloud.google.com`

|  Choose `all-apis` under these circumstances: 

  * You don't use VPC Service Controls.
  * You do use VPC Service Controls, but you also need to access Google APIs and services that are not supported by VPC Service Controls. 1

  
`vpc-sc` | Enables API access to [Google APIs and services that are supported by VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). Blocks access to Google APIs and services that do not support [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). Does not support Google Workspace APIs or Google Workspace web applications such as Gmail and Google Docs. |  Choose `vpc-sc` when you _only_ need access to Google APIs and services that _are_ supported by VPC Service Controls. The `vpc-sc` bundle does not permit access to Google APIs and services that do not support VPC Service Controls. 1  
  
1 If you need to restrict users to just the Google APIs and services that support [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs), use `vpc-sc`, as it provides additional risk mitigation for data exfiltration. Using `vpc-sc` denies access to Google APIs and services that are not supported by VPC Service Controls. See [Setting up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity) in the VPC Service Controls documentation for more details. 

#### Single global Google API

You can use Private Service Connect backends to send requests to a single supported global Google API. The following APIs are supported:

  * [Bigtable](https://docs.cloud.google.com/bigtable/docs/apis): `bigtable.googleapis.com` and `bigtableadmin.googleapis.com`
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/apis): `logging.googleapis.com`
  * [Spanner](https://docs.cloud.google.com/spanner/docs/apis): `spanner.googleapis.com`
  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/apis): `storage.googleapis.com`
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/apis): `pubsub.googleapis.com`



### Regional Google APIs

You can use endpoints or backends to access regional Google APIs. Regional endpoints have this format: `SERVICE.REGION.rep.googleapis.com`. For a list of supported regional Google APIs, see [Regional service endpoints](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints).

## Types

The following tables summarize compatibility information for different Private Service Connect configurations.

In the following tables, a  checkmark indicates that a feature is supported, and a  no symbol indicates that a feature isn't supported.

### Endpoints and published services

This section summarizes the configuration options that are available for consumers and producers when using endpoints to access published services.

#### Consumer configuration

This table summarizes the supported configuration options and capabilities of [endpoints that access published services](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints) based on target producer type. 

Target producer | Consumer configuration (endpoint)  
---|---  
[Consumer global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) | [Hybrid access](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises) | [Automatic DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer)  
(IPv4-only) | [VPC Network Peering access](https://docs.cloud.google.com/vpc/docs/vpc-peering) | [NCC connection propagation](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) (IPv4 only) | [Supported target services for IPv4 endpoints](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#ip-version-translation) | [Supported target services for IPv6 endpoints](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#ip-version-translation)  
[Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) |  |  |  |  |  | 

  * IPv4 services

| 

  * IPv4 services

  
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) | Only if [global access is enabled](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access) on the load balancer ([known issue](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#global-access)) |  |  |  |  | 

  * IPv4 services

| 

  * IPv4 services
  * IPv6 services

  
[Internal protocol forwarding (target instance)](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding) | Only if [global access is enabled](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--allow-global-access) on the producer forwarding rule ([known issue](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#global-access)) |  |  |  |  | 

  * IPv4 services

| 

  * IPv4 services
  * IPv6 services

  
[Port mapping services](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-port-mapping) | Only if [global access is enabled](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--allow-global-access) on the producer forwarding rule |  |  |  |  | 

  * IPv4 services

| 

  * IPv4 services
  * IPv6 services

  
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | Only if [global access is enabled](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access) on the load balancer before the service attachment is created |  |  |  |  | 

  * IPv4 services

| 

  * IPv4 services

  
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) | Only if [global access is enabled](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs#global-access) on the load balancer before the service attachment is created |  |  |  |  | 

  * IPv4 services

| 

  * IPv4 services

  
[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment) |  |  |  |  |  | 

  * IPv4 services

| 

  * IPv4 services

  
  
Endpoints that access a published service have the following limitations: 

  * You can't create an endpoint in the same VPC network as the [published service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) that you are accessing.

  * [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) can't mirror packets for Private Service Connect published services traffic.

  * Not all static routes with load balancer next hops are supported with Private Service Connect. For more information, see [Static routes with load balancer next hops](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#routing).

  * [ Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) can't test connectivity between an IPv6 endpoint and a published service.




#### Producer configuration

This table summarizes the supported configuration options and capabilities of [published services that are accessed by endpoints](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services).

Producer type | Producer configuration (published service)  
---|---  
[Supported producer backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#backends) | [PROXY protocol](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol) (TCP traffic only) | [IP version](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#ip-version-translation)  
[Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | 

  * GCE_VM_IP_PORT zonal NEGs
  * Hybrid NEGs
  * Serverless NEGs
  * Private Service Connect NEGs
  * Instance groups

|  | 

  * IPv4

  
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) | 

  * GCE_VM_IP zonal NEGs
  * Instance groups

|  | 

  * IPv4
  * IPv6

  
[Internal protocol forwarding (target instance)](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding) | 

  * Not applicable

|  | 

  * IPv4
  * IPv6

  
[Port mapping services](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-port-mapping) | 

  * Port mapping NEG

|  | 

  * IPv4
  * IPv6

  
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | 

  * GCE_VM_IP_PORT zonal NEGs
  * Hybrid NEGs
  * Serverless NEGs
  * Private Service Connect NEGs
  * Instance groups
  * Regional internet NEGs

|  | 

  * IPv4

  
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) | 

  * GCE_VM_IP_PORT zonal NEGs
  * Hybrid NEGs
  * Private Service Connect NEGs
  * Instance groups

|  | 

  * IPv4

  
[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment) | 

  * Not applicable

|  | 

  * IPv4

  
  
Published services have the following limitations: 

  * Load balancers that are configured with [ multiple protocols](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-multiple-protocols)—protocol set to `L3_DEFAULT`—are not supported.
  * [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) can't mirror packets for Private Service Connect published services traffic. 
  * You must use the Google Cloud CLI or the API to create a service attachment that points to a forwarding rule that is used for [internal protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding). 



For issues and workarounds, see [Known issues](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#known-issues). 

Different load balancers support different port configurations; some load balancers support a single port, some support a range of ports, and some support all ports. For more information, see [Port specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications). 

### Backends and published services

A [ Private Service Connect backend for published services](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) requires two load balancers—a consumer load balancer and a producer load balancer. This section summarizes the configuration options that are available for consumers and producers when using backends to access published services. 

#### Consumer configuration

This table describes the consumer load balancers that are supported by Private Service Connect backends for published services, including which backend service protocols can be used with each consumer load balancer. The consumer load balancers can access published services that are hosted on supported producer load balancers. 

Consumer load balancer | Protocols | IP version | [Cross-region failover](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#failover)  
---|---|---|---  
[Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | 

  * HTTP
  * HTTPS
  * HTTP2

| IPv4 |   
[Cross-region internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) | 

  * TCP

| IPv4 |   
[Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) **Note:**

  * Classic Application Load Balancer isn't supported.
  * Connecting to producer regional internal proxy Network Load Balancers isn't supported.

| 

  * HTTP
  * HTTPS
  * HTTP2

| IPv4 |   
[Global external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp) To associate this load balancer with a Private Service Connect NEG, use the Google Cloud CLI or send an API request. **Note:** Classic proxy Network Load Balancer is not supported. | 

  * TCP/SSL

| IPv4 |   
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) | 

  * HTTP
  * HTTPS
  * HTTP2

| IPv4 |   
[Regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp) | 

  * TCP

| IPv4 |   
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | 

  * HTTP
  * HTTPS
  * HTTP2

| IPv4 |   
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) | 

  * TCP

| IPv4 |   
  
#### Producer configuration

This table describes the configuration for producer load balancers that are supported by Private Service Connect backends for published services. 

Producer type | Producer configuration (published service)  
---|---  
[Supported producer backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#backends) | Forwarding rule protocols | Forwarding rule ports | [PROXY protocol](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol) | IP version | [Composite Health support](https://docs.cloud.google.com/vpc/docs/about-composite-health)  
[Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | 

  * GCE_VM_IP_PORT zonal NEGs
  * Hybrid NEGs
  * Serverless NEGs
  * Private Service Connect NEGs
  * Instance groups

| 

  * TCP
  * HTTP
  * HTTPS
  * HTTP/2
  * gRPC

| Supports one, multiple, or all ports |  | IPv4 |   
[Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) | 

  * GCE_VM_IP zonal NEGs
  * Instance groups

| 

  * TCP

| See [Producer port configuration](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#producer-ports) |  | IPv4 |   
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | 

  * GCE_VM_IP_PORT zonal NEGs
  * Hybrid NEGs
  * Serverless NEGs
  * Private Service Connect NEGs
  * Instance groups
  * Regional internet NEGs

| 

  * HTTP
  * HTTPS
  * HTTP/2

| Supports a single port |  | IPv4 |   
[Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) **Note:** Connections from consumer global external Application Load Balancers aren't supported. | 

  * GCE_VM_IP_PORT zonal NEGs
  * Hybrid NEGs
  * Private Service Connect NEGs
  * Instance groups

| 

  * TCP

| Supports a single port |  | IPv4 |   
[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment) | 

  * Not applicable

| 

  * Not applicable

| Not applicable |  | IPv4 |   
**Note:** To support access by a Private Service Connect backend in a global or cross-regional load balancer, the producer load balancer must have [ global access turned on](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--allow-global-access) before the service attachment is created. Don't disable global access if there are any global access Private Service Connect NEGs that connect to a producer load balancer [(known issue)](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls#health-check-failures). 

Published services have the following limitations: 

  * Load balancers that are configured with [ multiple protocols](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-multiple-protocols)—protocol set to `L3_DEFAULT`—are not supported.
  * [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring) can't mirror packets for Private Service Connect published services traffic. 
  * You must use the Google Cloud CLI or the API to create a service attachment that points to a forwarding rule that is used for [internal protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding). 



For issues and workarounds, see [Known issues](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#known-issues). 

For an example backend configuration that uses a global external Application Load Balancer, see [Access published services through backends](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls).

To publish a service, see [Publish services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

### Endpoints and global Google APIs

This table summarizes the features that are supported by [endpoints used to access Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints).

To create this configuration, see [Access Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).

Configuration | Details | **Consumer configuration (endpoint)**  
---  
Global reachability |  Uses an internal global IP address  
[Cloud Interconnect traffic](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#on-premises) |   
[Cloud VPN traffic](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#on-premises) |   
[Access through VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) |   
[Connection propagation through NCC](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) ([Preview](https://cloud.google.com/products#product-launch-stages)) |   
[Automatic DNS configuration](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#service-directory) |   
IP version | IPv4  
**Producer******  
Supported services | Supported global Google APIs  
  
**Note:** If you [configure Private Service Connect endpoints for global Google APIs in VPC Service Controls service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/psc-endpoint), endpoints created before September 1, 2026 aren't supported and must be recreated.

### Backends and global Google APIs

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This table describes which load balancers can use a Private Service Connect backend to a global Google API.

Configuration | Details  
---|---  
**Consumer configuration (Private Service Connect backend)**  
Supported consumer load balancers | 

  * Global external Application Load Balancer **Note:** Classic Application Load Balancer is not supported.
  * Cross-region internal Application Load Balancer

  
IP version | IPv4  
**Producer**  
Supported services | 

  * [Bigtable](https://docs.cloud.google.com/bigtable/docs/apis): `bigtable.googleapis.com` and `bigtableadmin.googleapis.com`
  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/apis): `logging.googleapis.com`
  * [Spanner](https://docs.cloud.google.com/spanner/docs/apis): `spanner.googleapis.com`
  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/apis): `storage.googleapis.com`
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/apis): `pubsub.googleapis.com`

  
  
### Endpoints and regional Google APIs

This table summarizes the features that are supported by [endpoints used to access regional Google APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints).

Configuration | Details | **Consumer configuration (endpoint)**  
---  
Global reachability |  If [ global access](https://docs.cloud.google.com/vpc/docs/about-accessing-regional-google-apis-endpoints#global-access) is enabled  
[Cloud Interconnect traffic](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#hybrid-access) |   
[Cloud VPN traffic](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#hybrid-access) |   
[Access through VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) |   
[Connection propagation through NCC](https://docs.cloud.google.com/vpc/docs/about-propagated-connections) |   
DNS configuration | [Manual DNS configuration](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints#configure-dns)  
IP version | IPv4 or IPv6  
**Producer******  
Supported services | [Supported regional Google APIs](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints)  
  
### Backends and regional Google APIs

This table describes which load balancers can use a [Private Service Connect backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) to access regional Google APIs.

For an example backend configuration that uses an internal Application Load Balancer, see [Access regional Google APIs through backends](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls).

Configuration | Details  
---|---  
**Consumer configuration (Private Service Connect backend)**  
Supported consumer load balancers | 

  * Internal Application Load Balancer Protocols: HTTPS
  * Regional external Application Load Balancer Protocols: HTTPS

  
IP version | IPv4  
**Producer**  
Supported services | [Supported regional Google APIs](https://docs.cloud.google.com/vpc/docs/regional-service-endpoints)  
  
## What's next

  * Learn about [accessing published services through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints).
  * Learn about [accessing global Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints).
  * Learn about [accessing regional Google APIs through endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints).
  * Learn about [backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).
  * Learn about [publishing services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
