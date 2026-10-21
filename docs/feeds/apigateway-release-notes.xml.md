---
url: https://docs.cloud.google.com/feeds/apigateway-release-notes.xml
title: API Gateway - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:07.849241+00:00
---

# API Gateway - Release notes

> Source: https://docs.cloud.google.com/feeds/apigateway-release-notes.xml

tag:google.com,2016:apigateway-release-notesAPI Gateway - Release notesGoogle Cloud Platform2026-09-30T00:00:00-07:00September 30, 2026tag:google.com,2016:apigateway-release-notes#September_30_20262026-09-30T00:00:00-07:00v1 

### Feature

**Authenticate MCP tool discovery with an API key**

API key authentication is now supported for the Model Context Protocol (MCP) `tools/list` method. You can name an API key security scheme in `tools-list.security`, in addition to a JWT security scheme.

For more information, see [Configure Model Context Protocol](https://docs.cloud.google.com/api-gateway/docs/mcp-configure).

]]> September 29, 2026tag:google.com,2016:apigateway-release-notes#September_29_20262026-09-29T00:00:00-07:00v1 

### Feature

**Configure streaming for LLM responses and other traffic**

You can now create API Gateway gateways that stream requests and responses instead of buffering them. This Public Preview feature supports incremental response delivery over HTTP/2 or HTTP/1.1 chunked transfer encoding, Server-Sent Events (SSE), WebSockets, and gRPC bidirectional streaming. A common use is streaming token-by-token responses from a large language model (LLM).

To enable streaming, create a gateway with the `--enable-streaming` flag. The streaming mode is fixed when you create the gateway and can't be changed later.

For more information, see [Configure streaming for LLM responses and other traffic](https://docs.cloud.google.com/api-gateway/docs/streaming-configure).

]]> September 11, 2026tag:google.com,2016:apigateway-release-notes#September_11_20262026-09-11T00:00:00-07:00v1 

### Feature

**Enable Model Context Protocol (MCP)**

You can now configure API Gateway to act as a remote Model Context Protocol (MCP) server. This Public Preview feature allows you to expose your existing REST APIs to AI agents as tools, without requiring changes to your backend services. You can enable MCP by annotating your OpenAPI 3.x specification using custom Google extensions.

For more information, see [Model Context Protocol overview](https://docs.cloud.google.com/api-gateway/docs/mcp-overview) and [Configure Model Context Protocol](https://docs.cloud.google.com/api-gateway/docs/mcp-configure).

]]> September 03, 2026tag:google.com,2016:apigateway-release-notes#September_03_20262026-09-03T00:00:00-07:00v1 

### Change

**New model routing gateways might use a gateway.dev default hostname**

If you create a gateway that uses model routing on or after September 3, 2026, it might receive a `gateway.dev` default hostname instead of a `run.app` one, in the form `https://GATEWAY_ID-PROJECT_NUMBER.REGION.gateway.dev` — for example, `https://my-gateway-123456789012.us-central1.gateway.dev`. This is a second `gateway.dev` format; other gateways keep the existing one.

To get a gateway's URL, read its `defaultHostname` property.

For more information, see [Deploy an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).

]]> August 03, 2026tag:google.com,2016:apigateway-release-notes#August_03_20262026-08-03T00:00:00-07:00v1 

### Feature

**Route LLM requests with model routing**

You can now use model routing in API Gateway as a managed traffic management layer to accept OpenAI-compatible prompt requests, transcode them in-flight, and route them to specific foundation models in Gemini Enterprise Agent Platform Model Garden (including Gemini, Anthropic Claude, and OpenAI GPT models).

Key benefits and capabilities include:

  * **Centralized traffic management** : Consolidate AI traffic routing and lifecycle management at the network edge without hosting standalone client-side proxies.
  * **In-flight transcoding** : Standardize client applications on an OpenAI-compatible REST interface while dynamically dispatching requests to diverse underlying Agent Platform Model Garden endpoints.
  * **OpenAPI 3.x configuration** : Define model routing tables, explicit routing rules, and default model fallbacks using the new `x-google-api-management.ai.models.routing` and `x-google-model-router` OpenAPI 3.x extensions.



For more information, see [Overview of model routing](https://docs.cloud.google.com/api-gateway/docs/model-routing-overview) and [Configure model routing](https://docs.cloud.google.com/api-gateway/docs/model-routing-configure).

]]> June 18, 2026tag:google.com,2016:apigateway-release-notes#June_18_20262026-06-18T00:00:00-07:00v1 

### Change

**Update to the API Gateway runtime architecture**

The API Gateway runtime architecture is being updated to improve its integration with Google Cloud Platform and its services.

This update does not affect existing API Gateway features. However, be aware of the following differences:

  * Status code changes for **gRPC** API Gateways 

Error | New status code | Previous status code  
---|---|---  
Quota exceeded | `ResourceExhausted` | `Unavailable`  
Invalid API key | `InvalidArgument` | `InternalError`  
  * For 4xx client-side quota failures, API Gateway will now reject requests (fail closed). This applies to both **gRPC** and **OpenAPI** API Gateways.




If you experience any other differences in behavior due to this update, contact [Google Cloud Customer Care](https://cloud.google.com/support-hub).

**Note** : Rollouts of this release to production instances might take up to 4 weeks to complete across all Google Cloud zones. Your instances might not be updated until the rollout is complete.

]]> April 27, 2026tag:google.com,2016:apigateway-release-notes#April_27_20262026-04-27T00:00:00-07:00v1 

### Change

**New validations on paths in API configurations**

API Gateway now enforces stricter syntax validations on templated paths when you create new API configurations and gateways.

See [path templating syntax rules](https://docs.cloud.google.com/api-gateway/docs/path-templating#syntax_rules) and [limits](https://docs.cloud.google.com/api-gateway/docs/path-templating#limits) for more information.

]]> February 02, 2026tag:google.com,2016:apigateway-release-notes#February_02_20262026-02-02T00:00:00-08:00v1 

### Change

**Connect API Gateway to Apigee API hub instances that use VPC Service Controls**

API Gateway can now be [connected to Apigee API hub](https://docs.cloud.google.com/api-gateway/docs/api-hub-connect) instances that use [VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc).

]]> January 12, 2026tag:google.com,2016:apigateway-release-notes#January_12_20262026-01-12T00:00:00-08:00v1 

### Feature

**Centralize API Gateway API management using Apigee API hub**

Connect API Gateway to Apigee API hub to enable seamless publishing of API metadata from your API Gateway project to API hub. This integration provides a centralized, unified view of your APIs across different gateways, simplifying API discovery, governance, and management.

Key benefits include:

  * **Centralized API discovery** : All your API Gateway APIs are discoverable in API hub alongside APIs from other sources 
  * **Enhanced visibility** : Gain insights into your API landscape with consolidated metadata 
  * **Streamlined management** : Simplify API governance and lifecycle management across your diverse API ecosystem 



For more detail, see [Centralize API management using API hub](https://docs.cloud.google.com/api-gateway/docs/api-hub-overview).

**Note** : Rollouts of this release to production instances might take up to 5 business days to complete across all Google Cloud zones. Your instances might not have the feature available until the rollout is complete.

]]> November 12, 2025tag:google.com,2016:apigateway-release-notes#November_12_20252025-11-12T00:00:00-08:00v1 

### Feature

**API Gateway now supports OpenAPI version 3.0.**

With this release, API Gateway now supports OpenAPI version 3.0, including all patch versions (3.0.x).

Key Benefits:

  * Simplified Deployment: Directly upload and deploy OpenAPI version 3.0.x specifications without prior conversion to 2.0.
  * Enhanced Compatibility: Seamlessly integrate your OpenAPI version 3.0.x definitions with API Gateway.



For more detail, see [OpenAPI overview](https://docs.cloud.google.com/api-gateway/docs/openapi-overview).

### Announcement

On November 12, 2025, we released a new version of API Gateway.

]]> July 23, 2025tag:google.com,2016:apigateway-release-notes#July_23_20252025-07-23T00:00:00-07:00v1 

### Deprecated

**Deprecation of Transport Layer Security (TLS) v1.0 and v1.1 protocols**

API Gateway now enforces TLS v1.2+. You can opt out of enforcing TLS v1.2+ for your API Gateway's new security settings by reaching out to [Google Cloud Support](https://docs.cloud.google.com/support) to continue using your current protocol.

Connections using TLS 1.1 and earlier will return a `400 Bad Request - The request was malformed` error after a successful TLS handshake, indicating that the connection is established, but the request itself is denied. External SSL-checking sites may verify a successful TLS handshake and incorrectly imply that TLS versions 1.1 and earlier are supported.

### Announcement

On July 23, 2025, we released an updated version of API Gateway.

]]> June 09, 2025tag:google.com,2016:apigateway-release-notes#June_09_20252025-06-09T00:00:00-07:00v1 

### Feature

With this release, the limit on the number of API gateways that can be created per region is increased to **50**.

For more information, see [Quotas and limits](https://docs.cloud.google.com/api-gateway/docs/quotas)

### Announcement

On June 9, 2025, we released an updated version of API Gateway.

]]> April 02, 2025tag:google.com,2016:apigateway-release-notes#April_02_20252025-04-02T00:00:00-07:00v1 

### Announcement

On April 2, 2025, we released an updated version of API Gateway.

### Feature

With this release, API Gateway meets the regulatory and compliance requirements for support of data residency for data at rest. 

For more information, see [Google Cloud Platform Services with Data residency](https://cloud.google.com/terms/data-residency?e=48754805).

]]> March 26, 2025tag:google.com,2016:apigateway-release-notes#March_26_20252025-03-26T00:00:00-07:00v1 

### Announcement

On March 26, 2025, we released an updated version of API Gateway.

### Feature

With this release, customer data in API Gateway is now CMEK-compliant at rest. No configuration is required. 

For more information, see [CMEK compliance in API Gateway](https://docs.cloud.google.com/api-gateway/docs/cmek).

To learn more about CMEK, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

]]> March 25, 2025tag:google.com,2016:apigateway-release-notes#March_25_20252025-03-25T00:00:00-07:00v1 

### Announcement

On March 25, 2025, we released an updated version of API Gateway.

### Feature

API Gateway now supports [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

Workforce Identity Federation lets you use an external identity provider (IdP) to authenticate and authorize a workforce — a group of users, such as employees, partners, and contractors — using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to access API Gateway services.

See [Identity federation: products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services) for more information.

]]> July 01, 2024tag:google.com,2016:apigateway-release-notes#July_01_20242024-07-01T00:00:00-07:00v1 

### Announcement

**As of July 1, 2024, API gateways located in`asia-east1` are decommissioned and will no longer serve traffic.**

Between **October 2021** and **October 2022** , customers with gateways located in `asia-east1` were notified of the planned decommissioning and advised to delete or relocate any gateways in this region. A final reminder was sent in May, 2024.

As of July 1, 2024, any remaining gateways located in `asia-east1` are fully decommissioned.

]]> March 16, 2023tag:google.com,2016:apigateway-release-notes#March_16_20232023-03-16T00:00:00-07:00v1 

### Fixed

Fixed issue where API Gateway used the IP address of the Google Cloud Load Balancer (GCLB) (specifically the address of the forwarding rule) to validate IP-restricted API keys in requests proxied by a GCLB. API gateway now correctly validates IP-restricted API keys using the IP address of the client calling the GCLB.

]]> January 05, 2023tag:google.com,2016:apigateway-release-notes#January_05_20232023-01-05T00:00:00-08:00v1 

### Fixed

Bug ID | Description  
---|---  
266369520 | **Fixed issue where gRPC requests to a gateway resulted in`400` responses following an ESPV2 upgrade.**  
  
### Change

When calling a gateway using gRPC with transcoding, every field provided in a request message must contain a valid value. For every field included in the request message you must either specify a valid integer value or remove the field entirely.

]]> August 09, 2021tag:google.com,2016:apigateway-release-notes#August_09_20212021-08-09T00:00:00-07:00v1 

### Announcement

Released a Preview version of HTTP(S) Load balancing for API Gateway.

The integration of [Google Cloud HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https) support for API Gateway enables your serverless backends to take advantage of all the features provided by Cloud Load Balancing. By combining API Gateway and HTTP(S) Load Balancing using a [serverless Network Endpoint Group (serverless NEG)](https://docs.cloud.google.com/load-balancing/docs/negs/), you can:

  * Host gateways with custom branded domains
  * Configure TLS for gateways using certificates issued by a preferred certificate authority
  * Create a common entry point for a gateway routing to multiple backends
  * Deploy gateways in multiple geographic regions for high availability without managing URLs for each region



To provide feedback or to log issues with this release, see [Getting support](https://docs.cloud.google.com/api-gateway/docs/getting-support).

]]> January 21, 2021tag:google.com,2016:apigateway-release-notes#January_21_20212021-01-21T00:00:00-08:00v1 

### Feature

An updated [REST API reference](https://docs.cloud.google.com/api-gateway/docs/reference/rest) for the `v1` version is available.

### Feature

API Gateway support for the `us-east1` region is now available.

### Feature

API Gateway is added to the gcloud command group. Users should upgrade to the latest `gcloud` release to access the API Gateway command group.

### Feature

gRPC support is available for Cloud Run backend services. For more information, see [Getting started with API Gateway and Cloud Run for gRPC](https://docs.cloud.google.com/api-gateway/docs/get-started-cloud-run-grpc).

### Announcement

Released a GA version of API Gateway.

To provide feedback or to log issues with this release, see [Getting support](https://docs.cloud.google.com/api-gateway/docs/getting-support).

]]> September 08, 2020tag:google.com,2016:apigateway-release-notes#September_08_20202020-09-08T00:00:00-07:00v1beta 

### Issue

Projects with gateways created between July 14, 2020 and August 6, 2020 may encounter an issue when new gateways are created with the beta API. The `*gateway.dev` hostname of the new gateway may return a `404` error response. A resolution to this issue is in progress. In the meantime, we recommend creating or using a new Google Cloud project when using the beta API.

### Feature

The API Gateway API is now publicly visible. Allowlisting is no longer required to view or enable the API in your Google Cloud project.

Deprecated fields are no longer present in alpha versions of the API and the [API Gateway UI](https://console.cloud.google.com/api-gateway) utilizes the beta API.

### Announcement

Released a beta version of API Gateway.

To provide feedback or to log issues with this release, see [Getting support](https://docs.cloud.google.com/api-gateway/docs/getting-support).

### Issue

When creating an API config, and in particular the _first_ config for a new service, the operation may take several minutes to complete as the config is propagated to downstream systems. Creation of a complex API config could take up to ten minutes to complete successfully.

### Issue

Gateways created during alpha with `*.run.app` hostnames (created prior to July 14, 2020) will be turned down shortly after the beta release. We recommend creating new gateways using the `v1beta` API. Gateways created with the beta API will have `*.gateway.dev` hostnames.

### Issue

API configs created prior to June 2, 2020 can no longer be deployed to gateways. These configs will be deleted through an internal process.

### Issue

API Gateway built-in IAM roles are not initially visible. As a result, management permissions are not displayed on the permissions panel within the [API Gateway UI](https://console.cloud.google.com/api-gateway). However, permissions to manage API Gateway resources can be granted as expected via Project Owner, Editor, and Viewer roles. A resolution to this issue is in progress.

### Feature

An updated [REST API reference](https://docs.cloud.google.com/api-gateway/docs/reference/rest) for the `v1beta` version is available.

### Issue

API Gateway does not support custom IAM roles. A resolution to this issue is in progress.

### Feature

API Gateway is added to the `gcloud beta` command group. Alpha users and trusted testers should upgrade to the latest `gcloud` release to access the API Gateway beta command group.

### Feature

Newly created gateways have an updated default hostname pattern:

`https://GATEWAY_ID-HASH.REGION_CODE.gateway.dev`

where **GATEWAY_ID** is the name of the gateway, **HASH** is the unique hash code generated when you deployed the gateway, and **REGION_CODE** is the code for the Google Cloud region where the gateway is deployed.

For more information, see [Deploying an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).

]]> July 01, 2020tag:google.com,2016:apigateway-release-notes#July_01_20202020-07-01T00:00:00-07:00v1alpha2 

### Feature

Updated the [REST API reference](https://docs.cloud.google.com/api-gateway/docs/reference/rest) to the latest Alpha version.

### Issue

When creating a gateway, permissions can take more than a minute to propagate through the system. Therefore, you might see a "missing tokens" error when making a request to an API. If you see this error, wait several minutes, then retry the request.

### Announcement

Released an updated version of the Alpha version of API Gateway.

To provide feedback or to log issues with this release, see [Getting support](https://docs.cloud.google.com/api-gateway/docs/getting-support).

### Feature

Newly created gateways now have an updated default hostname pattern: 

`https://GATEWAY_ID-HASH.REGION_CODE.gateway.dev`

where **GATEWAY_ID** is the name of the gateway, **HASH** is the unique hash code generated when you deployed the gateway, and **REGION_CODE** is the code for the Google Cloud region where the gateway is deployed.

For more information, see [Deploying an API to a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api).

### Feature

OpenAPI specifications for API configs no longer require the `host` property. You can either omit the `host` property entirely or set it to the DNS name of the deployed API. API providers often set it to the DNS name when sharing the OpenAPI Spec with their API consumers. However, the value of the `host` property is not enforced by API Gateway. Do not set the `host` property to **null** or an empty value, as this will result in an error.

For more information, see [OpenAPI overview](https://docs.cloud.google.com/api-gateway/docs/openapi-overview).

### Issue

When creating an API config, and in particular the _first_ config for a new service, the operation may take several minutes to complete as the config is propagated to downstream systems. Creation of a complex API config could take up to ten minutes to complete successfully.

]]> April 01, 2020tag:google.com,2016:apigateway-release-notes#April_01_20202020-04-01T00:00:00-07:00v1alpha2 

### Fixed

Previously, when the `gcloud` command failed while creating an API config, the API config was still created, requiring you to manually delete it. The `gcloud` command no longer requires you to delete the API config when the create command fails.

### Feature

The [`gcloud` command-line tool](http://cloud.google.com/sdk/gcloud) now supports new command options, including:

  * Create, list, update, and delete APIs. That means you no longer have to use [Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs) commands to work with an API. See [Creating an API](https://docs.cloud.google.com/api-gateway/docs/creating-api) for more.

  * Update an API config to modify its labels or display name. See [Updating an API config](https://docs.cloud.google.com/api-gateway/docs/creating-api-config#updating-an-api-config) for more.




### Feature

You can now use the Google Cloud Console UI, a web-based, graphical user interface, to develop your APIs. See the [Quickstart: Use the UI to deploy an API on API Gateway](https://docs.cloud.google.com/api-gateway/docs/quickstart-console) for more.

### Issue

When creating a gateway, permissions can take more than a minute to propagate through the system. Therefore, you might see a "missing tokens" error when making a request to an API. If you see this error, wait several minutes, then retry the request.

### Announcement

Alpha update release of API Gateway

Released an updated version of the Alpha version of API Gateway.

To provide feedback or to log issues with this release, see [Getting support](https://docs.cloud.google.com/api-gateway/docs/getting-support).

### Feature

Updated the [REST API reference](https://docs.cloud.google.com/api-gateway/docs/reference/rest) to the latest Alpha version.

### Issue

Authentication is only supported for Cloud Run and Cloud Functions, not for App Engine.

]]> March 01, 2020tag:google.com,2016:apigateway-release-notes#March_01_20202020-03-01T00:00:00-08:00v1alpha1 

### Issue

When creating a gateway, permissions can take more than a minute to propagate through the system. Therefore, you might see a "missing tokens" error when making a request to an API. If you see this error, wait several minutes, then retry the request.

### Issue

Authentication is only supported for Cloud Run and Cloud Functions, not for App Engine.

### Announcement

Released the Alpha version of API Gateway.

To provide feedback or to log issues with this release, see [Getting support](https://docs.cloud.google.com/api-gateway/docs/getting-support).

]]>
