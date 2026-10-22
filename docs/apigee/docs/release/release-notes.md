---
url: https://docs.cloud.google.com/apigee/docs/release/release-notes/
title: Apigee release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:30.245224+00:00
---

# Apigee release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/release/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Apigee software in 2022 and later. We recommend that users periodically check this list for any new announcements, or subscribe to this page using a feed reader to get notifications of updates. What is a feed reader?

### What is a feed reader?

Really simple syndication (RSS) feed readers aggregate content from websites that you specify.

Feed reader notifications can be email-, browser-, desktop-, or mobile-based. Some readers are free, or have free versions, and some require a subscription.

A few examples:

  * [Feedly](https://feedly.com)
  * [Feedreader](https://feedreader.com)
  * [Feeder](https://feeder.co/)



More information on RSS:

  * [RSS](https://en.wikipedia.org/wiki/RSS)
  * [ Comparison of feed aggregators](https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators)



Close

See also:

  * [Apigee Edge for Public Cloud release notes](https://docs.cloud.google.com/apigee/docs/edge-public-cloud/release-notes)
  * [Apigee Edge for Private Cloud release notes](https://docs.cloud.google.com/apigee/docs/edge-private-cloud/release-notes)
  * [Apigee 2021 and prior release notes](https://docs.cloud.google.com/apigee/docs/release/notes/apigee-release-notes)
  * [Known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues)

rss_feed Subscribe: 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/apigee-x-release-notes.xml) directly. 

## October 20, 2026

Announcement

On October 20th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-6** , your instance will be updated to **1-18-0-apigee-6** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

## October 15, 2026

Fixed

Bug ID | Description  
---|---  
**466116259** | Updated the startup script for the managed instance group (MIG) that routes external traffic to Apigee. `net.ipv4.ip_forward` is now written to `/etc/sysctl.d/`, so an instance no longer stops forwarding traffic when a reboot or an OS update resets it. The script does not change unrelated `iptables` NAT rules. Instances pick up the change the next time they are restarted or recreated.  
  
## October 02, 2026

Announcement

On October 2, 2026, we released an updated version of Apigee (1-18-0-apigee-6).

**Note:** Rollouts of this release began today and can take four or more business days to complete across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**564386425** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway (ASM) to patch security vulnerabilities.  
**561666530** | **Security fix for Apigee.** Upgraded the Prometheus library to patch the following vulnerabilities: 

  * [CVE-2026-42151](https://nvd.nist.gov/vuln/detail/CVE-2026-42151)
  * [CVE-2026-42154](https://nvd.nist.gov/vuln/detail/CVE-2026-42154)
  * [CVE-2026-44903](https://nvd.nist.gov/vuln/detail/CVE-2026-44903)
  * [CVE-2026-40179](https://nvd.nist.gov/vuln/detail/CVE-2026-40179)

  
**N/A** | **Security fix for Apigee infrastructure.**  
  
Fixed

Bug ID | Description  
---|---  
**432315283** | Fixed a multi-certificate truststore so that its trust anchors take effect without a Message Processor restart when `features.truststore.multi_cert_bundle.enabled` is toggled at runtime; the outbound SSL context is now rebuilt automatically on any trust-anchor change.  
**565072374** | VerifyJWT policies that use a JWKS `uriRef` no longer return `steps.jwt.NoMatchingPublicKey` on the first request after the JWKS cache TTL expires when the identity provider has rotated to a new key ID. The cache now re-fetches synchronously when its entry expires.  
**535395491** | Extension Processor (ext_proc) denials now return the status and body that the policy or FaultRule produced, instead of always returning HTTP 500.  
**558421499** | Apigee runtime runs on JRE 21.  
**517953321** | The `lookupcache.<n>.isEncrypted` and `responsecache.<n>.isEncrypted` flow variables now report the per-entry on-disk encryption state of the L2 cache, rather than approximating whether the cache-encryption key is loaded. L1 cache hits report `false`. Review any policy conditions that rely on these flow variables.  
**563557547** | Fixed EventFlow (Server-Sent Events) coalescing multiple events into a single policy invocation under burst load on the http-adaptor data path, which produced malformed SSE output to the client.  
**562740573** | Apigee Analytics now populates the `processing_mode` dimension, distinguishing proxy traffic from extension-processor traffic. This dimension is not populated in billing-only analytics mode.  
**357042873** | Stopped redirecting `apigee-cassandra-schema-readiness` init container logs to `/dev/null`, improving troubleshooting. Workloads undergo a rolling restart upon upgrade.  
**N/A** | Updates to infrastructure and libraries.  
  
## September 21, 2026

Announcement

On September 21st, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-4** , your instance will be updated to **1-18-0-apigee-4** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

Announcement

On September 21st, 2026, we released an updated version of Apigee (1-18-0-apigee-5).

**Note:** Rollouts of this release began today and can take four or more business days to be completed across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**560130499** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy.  
**547681234** | **Security fix for Apigee.** Patched [CVE-2026-69247](https://nvd.nist.gov/vuln/detail/CVE-2026-69247) by upgrading a third-party library used by the Apigee model-security engine.  
**556568593** | **Security fix for Apigee.** Patched [CVE-2026-84304](https://nvd.nist.gov/vuln/detail/CVE-2026-84304) by upgrading gRPC.  
**N/A** | **Security fix for Apigee infrastructure.**  
  
Fixed

Bug ID | Description  
---|---  
**559009293** | Fixed elevated OAuth and VerifyAPIKey latency and Cassandra read load for AppGroup apps by caching the AppGroup entity in the Message Processor runtime, matching Developer-app behavior.  
**558888960** | Fixed distributed tracing so that the target URL is included as a span attribute in all scenarios.  
**556750755** | Fixed EventFlow (Server-Sent Events) dropping or truncating events that follow a large (greater than 16 KB) event under load on the http-adaptor data path.  
**553931019** | The MCP tools/list method now aggregates tools across all approved API products.  
**531783017** | Implemented the `<Enforce>true</Enforce>` element of SSLInfo for a Syslog endpoint, so that the syslog target's TLS server identity is verified.  
**554114419** | Policies can now change request pseudo-headers (for example, :path and :authority) when HTTP/2 is in use.  
**548763108** | Blocked outbound HTTP from the Message Processor to Kubernetes-internal targets.  
**513032450** | Restored a 15-second TCP keep-alive on the Apigee Connect control-plane connection so that a silently dropped connection recovers in seconds rather than approximately two hours.  
**N/A** | Updates to infrastructure and libraries.  
  
## September 10, 2026

Fixed

Addendum to Apigee release notes dated August 27, 2026 (1-18-0-apigee-4).

Bug ID | Description  
---|---  
**502540992** | Fixed an issue where the SemanticCacheLookup policy was incompatible with Vertex AI Vector Search Private Service Connect (PSC) endpoints.  
  
## September 09, 2026

Feature

**SemanticCacheLookup policy supports non-default Vector Search distance measures**

Available in Apigee `1-18-0-apigee-4` and later. A new optional `<DistanceMeasureType>` element accepts `DOT_PRODUCT_DISTANCE` (the default, and the existing behavior), `COSINE_DISTANCE`, `SQUARED_L2_DISTANCE` and `L1_DISTANCE`. The policy now compares `<Threshold>` in the direction the declared measure implies, so declaring a non-default measure requires re-tuning the threshold in the same edit. The 0-to-1 restriction on `<Threshold>` is also removed.

## August 27, 2026

Announcement

On August 27th, 2026, we released an updated version of Apigee (1-18-0-apigee-4).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**507878328** | Upgraded the Apigee runtime to run on JDK 17, while maintaining backward compatibility with JDK 11.  
**530965355** | Added an opt-in Message Processor connection-failure back-off (CWC property HTTPClient.backoff.enabled, defaults to false) that prevents the Message Processor from consuming excessive CPU when a target is completely unavailable.  
**532793298** | Fixed an API product bug where combining a payloadOperationGroup with a REST or llmOperationGroup rejected REST/LLM traffic with a 401.  
**534420582** | The JSONThreatProtection policy adds a new optional child element <RejectDuplicateKeys> that rejects request bodies containing duplicate JSON keys within the same object. Defaults to false to preserve existing behavior.  
**N/A** | Updates to infrastructure and libraries.  
  
This list is incomplete; see entries for September 9, 2026 and September 10, 2026.

Security

Bug ID | Description  
---|---  
**544570126** | **Security fix for Apigee.** Fixed a security issue in the PythonScript policy.  
**N/A** | **Security fix for Apigee infrastructure.**  
  
## August 13, 2026

Announcement

On August 13th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-2** , your instance will be updated to **1-18-0-apigee-2** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

Announcement

On August 13th, 2026, we released an updated version of Apigee (1-18-0-apigee-3).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**532147587** | To fix forward proxy support.  
**537657987** | Fixed a bug where watcher failed to reconcile all routes if an environment was not found in the control plane.  
**543022076** | Google Cloud BOM upgrade (protobuf 4.x, gRPC 1.81, Guava 33.5). One user-visible change: a malformed inbound gRPC request frame is now reported to the client as grpc-status INTERNAL(13) and recorded in analytics as x-apigee.grpc.status=13, where it was previously an Apigee ServiceUnavailable fault seen as UNAVAILABLE(14) with no x-apigee.grpc.status recorded. Otherwise no user facing impact, but any prod issue related to gcp, protobuf or gRPC may relate to this.  
**542242046** | Fixed LLMTokenQuota metering the request against an arbitrary quota bucket when the API Product declared multiple models and the request carried no model.  
**531731614** | Apigee analytics fields ai_llm_response_token_count, ai_llm_prompt_token_count, ai_llm_model_name, and ai_llm_model_provider are available in the Custom Report when LLMTokenQuota and PromptTokenLimit policies are used in Apigee proxies.  
**492044413** | LLMTokenQuota resolves the model from the API Product LLM Operation when LLMModelSource is omitted and the request body has no model field.  
**67169710** | Adds an opt-in <DynamicClientIdSupported> boolean XML element to the OAuthV2 policy. When true, AbstractOAuthStepExecution.extractClientDetails() preserves any non-empty ClientID/ClientSecret already present on the OAuthClientContext.  
**531731614** | Apigee auto identifies the providers and publishes them to analytics.  
**537396574** | Added feature to rotate the apigee-ca certificate.  
**540861752** | Aligned the ApigeeDeployment conversion hub with its v1alpha3 storage version. Internal change; no effect on existing ApigeeDeployment resources.  
**540861752** | Aligned the ApigeeDeployment custom resource's conversion hub with its v1alpha3 storage version. This internal change does not affect existing ApigeeDeployment resources.  
**N/A** | Updates to infrastructure and libraries.  
  
Security

Bug ID | Description  
---|---  
**535928300** | **Security fix for Apigee.** Fixed a security issue in JWT refresh token revocation handling.  
**539515020** | **Security fix for Apigee.** Fixed a security issue in the MessageValidation policy.  
**535928530** | **Security fix for Apigee.** Fixed a security issue in the OAuthV2 policy.  
**535683286** | **Security fix for Apigee.** Fixed a security issue in HTTP target interim-response handling.  
**N/A** | **Security fix for Apigee infrastructure.**  
  
## July 27, 2026

Announcement

On July 27th, 2026, we released an updated version of Apigee (1-18-0-apigee-2).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**SanitizeUserPrompt and SanitizeModelResponse policies now support function calling**

The SanitizeUserPrompt and SanitizeModelResponse policies now handle LLM function calling (tool use) flows. Two new optional XML elements extract function calling content for Model Armor sanitization:

  * `<FunctionResponseSource>` in SanitizeUserPrompt: extracts function/tool response data from user turns. Used as a fallback when `<UserPromptSource>` returns empty on function calling turns.
  * `<FunctionCallSource>` in SanitizeModelResponse: extracts function call arguments from model responses. Used as a fallback when `<LLMResponseSource>` returns empty.



Default templates target the Gemini format and require no additional configuration. For OpenAI and Anthropic formats, configure custom JSONPath templates. For more information, see [FunctionResponseSource](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#functionresponsesource) and [FunctionCallSource](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#functioncallsource).

Security

Bug ID | Description  
---|---  
**534852923** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy.  
**N/A** | **Security fix for Apigee infrastructure.**  
  
Fixed

Bug ID | Description  
---|---  
**N/A** | Updates to infrastructure and libraries.  
  
## July 16, 2026

Announcement

On July 16th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-10** , your instance will be updated to **1-17-0-apigee-10** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

## July 15, 2026

Announcement

On July 15th, 2026, we released an updated version of Apigee (1-18-0-apigee-1).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**527586459** | Fixed a cache policy throttling bug (CacheThrottlerV2 key poisoning) to enhance reliability.  
**525697701** | Fixed an issue where API proxy deployments could get stuck during basepath migrations in Apigee X.  
**N/A** | Updates to infrastructure and libraries.  
  
Security

Bug ID | Description  
---|---  
**527415966, 524656652** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway (ASM) to patch security vulnerabilities.  
**527956223** | **Security fix for Apigee.** Enhanced security in the Java Callout policy to prevent sandbox escape.  
**519729209** | **Security fix for Apigee.** Fixed a SAML XML Signature Wrapping (XSW) vulnerability in the ValidateSAMLAssertion policy.  
**530886487** | **Security fix for Apigee.** Upgraded the apigee-connect-agent to patch [CVE-2026-25680](https://nvd.nist.gov/vuln/detail/CVE-2026-25680).  
**N/A** | **Security fix for Apigee infrastructure.**  
  
## July 08, 2026

Security

An Improper Input Validation vulnerability in BigQuery DAO in Google Cloud Apigee versions prior to 2026-06-12 on Google Cloud Platform allowed an authenticated attacker to exfiltrate cross-tenant data.

This vulnerability was patched on 12 June 2026 on the Apigee Servers, and no customer action is needed. Apigee hybrid was not affected.

For more information, see [CVE-2026-12879](http://cve.org/CVERecord?id=CVE-2026-12879).

## July 06, 2026

Feature

**Support for payload operations matching in API Products**

Apigee now supports payload operations matching (`payloadOperationGroup`) in API Products, powered by the new **ParsePayload** policy.

Payload operations matching allows you to define API Product operations that match fields within request payloads, such as JSON-RPC requests used by the Model Context Protocol (MCP). Apigee can then route, monetize, authorize, and apply distinct quota limits to traffic based on the derived payload operation.

This feature is available to all Apigee X customers in all supported regions with no additional charge. For more information, see [Manage MCP tool access with API products](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/manage-mcp-tool-access) and the [ParsePayload policy reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-payload-policy).

## June 24, 2026

Announcement

**Apigee Emulator**

### Apigee Emulator v2.0.1

On June 24, 2026, we released Apigee Emulator version 2.0.1.

This is a security-only hotfix release on top of v2.0.0 that addresses 10 security vulnerabilities in the Netty networking library and the embedded Cassandra Go standard library health-check binary. There are no functional, API, or configuration changes -- v2.0.1 is a drop-in replacement for v2.0.0.

The emulator image is available at [Google Artifact Registry](https://console.cloud.google.com/artifacts/docker/apigee-release/us/gcr.io/hybrid%2Fapigee-emulator).

To upgrade, update the emulator version in your VS Code Cloud Code settings to `2.0.1`. See [Manage the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#choose_the_emulator_version) for details.

Feature

**Apigee Emulator**

#### Changed in this release

  * Upgraded Netty to `4.1.135.Final` (from `4.1.133.Final`) and pinned all transitive `netty-*` artifacts via `netty-bom`.
  * Refreshed the Cassandra base image to pick up Go standard library `1.25.11` (from `1.25.10`) in the embedded health-check binary.
  * Updated `netty-tcnative-boringssl-static` classifier variants from `2.0.53.Final` to `2.0.77.Final`.



Security

**Apigee Emulator**

#### Security

This release addresses 10 security vulnerabilities in the Netty networking library and the embedded Go standard library. All Netty fixes come from upgrading to `4.1.135.Final`; all Go standard library fixes come from a Cassandra base image rebuild against Go `1.25.11`.

CVE | Component  
---|---  
[CVE-2026-50010](https://nvd.nist.gov/vuln/detail/CVE-2026-50010) | Netty (`netty-handler`)  
[CVE-2026-50020](https://nvd.nist.gov/vuln/detail/CVE-2026-50020) | Netty (`netty-codec-http`)  
[CVE-2026-50560](https://nvd.nist.gov/vuln/detail/CVE-2026-50560) | Netty (`netty-codec-http2`)  
[CVE-2026-48043](https://nvd.nist.gov/vuln/detail/CVE-2026-48043) | Netty (`netty-codec-http2`)  
[CVE-2026-44249](https://nvd.nist.gov/vuln/detail/CVE-2026-44249) | Netty (`netty-handler`)  
[CVE-2026-45416](https://nvd.nist.gov/vuln/detail/CVE-2026-45416) | Netty (`netty-handler`)  
[CVE-2026-47244](https://nvd.nist.gov/vuln/detail/CVE-2026-47244) | Netty (`netty-codec-http2`)  
[CVE-2026-27145](https://nvd.nist.gov/vuln/detail/CVE-2026-27145) | Go standard library  
[CVE-2026-42504](https://nvd.nist.gov/vuln/detail/CVE-2026-42504) | Go standard library  
[CVE-2026-42507](https://nvd.nist.gov/vuln/detail/CVE-2026-42507) | Go standard library  
  
## June 22, 2026

Announcement

On June 22nd, 2026, we released an updated version of Apigee (1-17-0-apigee-10).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**519996459** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway to patch the following vulnerabilities: 

  * [CVE-2026-27143](https://nvd.nist.gov/vuln/detail/CVE-2026-27143)
  * [CVE-2019-14993](https://nvd.nist.gov/vuln/detail/CVE-2019-14993)
  * [CVE-2021-39155](https://nvd.nist.gov/vuln/detail/CVE-2021-39155)
  * [CVE-2021-39156](https://nvd.nist.gov/vuln/detail/CVE-2021-39156)
  * [CVE-2022-23635](https://nvd.nist.gov/vuln/detail/CVE-2022-23635)
  * [CVE-2026-27140](https://nvd.nist.gov/vuln/detail/CVE-2026-27140)
  * [CVE-2026-27144](https://nvd.nist.gov/vuln/detail/CVE-2026-27144)
  * [CVE-2026-29181](https://nvd.nist.gov/vuln/detail/CVE-2026-29181)
  * [CVE-2026-32280](https://nvd.nist.gov/vuln/detail/CVE-2026-32280)
  * [CVE-2026-32281](https://nvd.nist.gov/vuln/detail/CVE-2026-32281)
  * [CVE-2026-32283](https://nvd.nist.gov/vuln/detail/CVE-2026-32283)
  * [CVE-2026-33811](https://nvd.nist.gov/vuln/detail/CVE-2026-33811)
  * [CVE-2026-33814](https://nvd.nist.gov/vuln/detail/CVE-2026-33814)
  * [CVE-2026-34986](https://nvd.nist.gov/vuln/detail/CVE-2026-34986)
  * [CVE-2026-35469](https://nvd.nist.gov/vuln/detail/CVE-2026-35469)
  * [CVE-2026-39820](https://nvd.nist.gov/vuln/detail/CVE-2026-39820)
  * [CVE-2026-39836](https://nvd.nist.gov/vuln/detail/CVE-2026-39836)
  * [CVE-2026-39883](https://nvd.nist.gov/vuln/detail/CVE-2026-39883)
  * [CVE-2026-4046](https://nvd.nist.gov/vuln/detail/CVE-2026-4046)
  * [CVE-2026-42499](https://nvd.nist.gov/vuln/detail/CVE-2026-42499)
  * [CVE-2026-42501](https://nvd.nist.gov/vuln/detail/CVE-2026-42501)
  * [CVE-2026-42504](https://nvd.nist.gov/vuln/detail/CVE-2026-42504)
  * [CVE-2022-31045](https://nvd.nist.gov/vuln/detail/CVE-2022-31045)
  * [CVE-2026-27145](https://nvd.nist.gov/vuln/detail/CVE-2026-27145)
  * [CVE-2026-32282](https://nvd.nist.gov/vuln/detail/CVE-2026-32282)
  * [CVE-2026-32288](https://nvd.nist.gov/vuln/detail/CVE-2026-32288)
  * [CVE-2026-32289](https://nvd.nist.gov/vuln/detail/CVE-2026-32289)
  * [CVE-2026-39350](https://nvd.nist.gov/vuln/detail/CVE-2026-39350)
  * [CVE-2026-39817](https://nvd.nist.gov/vuln/detail/CVE-2026-39817)
  * [CVE-2026-39819](https://nvd.nist.gov/vuln/detail/CVE-2026-39819)
  * [CVE-2026-39823](https://nvd.nist.gov/vuln/detail/CVE-2026-39823)
  * [CVE-2026-39825](https://nvd.nist.gov/vuln/detail/CVE-2026-39825)
  * [CVE-2026-39826](https://nvd.nist.gov/vuln/detail/CVE-2026-39826)
  * [CVE-2026-41413](https://nvd.nist.gov/vuln/detail/CVE-2026-41413)
  * [CVE-2026-42507](https://nvd.nist.gov/vuln/detail/CVE-2026-42507)
  * [CVE-2026-4437](https://nvd.nist.gov/vuln/detail/CVE-2026-4437)
  * [CVE-2026-4438](https://nvd.nist.gov/vuln/detail/CVE-2026-4438)

  
**N/A** | **Security fix for Apigee infrastructure.**  
  
Fixed

Bug ID | Description  
---|---  
**515788622** | Upgraded the default outbound TLS protocol from TLSv1.2 to TLSv1.3 on JVMs that support it. Per-proxy `<SSLInfo><Protocols>` settings continue to take precedence, and the new `HTTPClient.outbound.tls.protocol` override lets operators force a specific protocol.  
**184266748** | Fixed an issue where ApigeeDatastore TLS certificate creation could fail in namespaces with longer names when the certificate common name exceeded the 64-byte limit.  
**286069772** | Added a per-gateway `proxyProtocol.mode` property (strict, permissive, disable) on Apigee ingress gateway components to opt in to HAProxy PROXY-protocol parsing. The property defaults to disable.  
**N/A** | Updates to infrastructure and libraries.  
  
## June 18, 2026

Announcement

On June 18th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-9** , your instance will be updated to **1-17-0-apigee-9** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

## June 08, 2026

Announcement

On June 8th, 2026, we released an updated version of Apigee (1-17-0-apigee-9).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**514384893** | **Security fix for Apigee.** Hardened the Script policy to block server-side request forgery (SSRF) to link-local addresses.  
**N/A** | **Security fix for Apigee infrastructure.**  
  
Fixed

Bug ID | Description  
---|---  
**512850756** | Added observability metrics for the OpenTelemetry trace export pipeline, reporting spans exported, export latency, batch size, and dropped spans.  
**515039499** | Fixed an issue where OpenTelemetry trace export over HTTP could fail to authenticate when sent through a forward proxy that requires basic authentication.  
  
## June 02, 2026

Announcement

On June 2nd, 2026, we released an updated version of Apigee Cassandra.

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**Apigee Cassandra security update** | **Security fix for Apigee Cassandra infrastructure.** This addresses the following vulnerabilities:

  * [CVE-2026-39820](https://nvd.nist.gov/vuln/detail/CVE-2026-39820)
  * [CVE-2026-42499](https://nvd.nist.gov/vuln/detail/CVE-2026-42499)
  * [CVE-2026-39836](https://nvd.nist.gov/vuln/detail/CVE-2026-39836)
  * [CVE-2026-33814](https://nvd.nist.gov/vuln/detail/CVE-2026-33814)
  * [CVE-2026-42501](https://nvd.nist.gov/vuln/detail/CVE-2026-42501)
  * [CVE-2026-33811](https://nvd.nist.gov/vuln/detail/CVE-2026-33811)
  * [CVE-2026-39825](https://nvd.nist.gov/vuln/detail/CVE-2026-39825)
  * [CVE-2026-39817](https://nvd.nist.gov/vuln/detail/CVE-2026-39817)
  * [CVE-2026-39823](https://nvd.nist.gov/vuln/detail/CVE-2026-39823)
  * [CVE-2026-39819](https://nvd.nist.gov/vuln/detail/CVE-2026-39819)
  * [CVE-2026-39826](https://nvd.nist.gov/vuln/detail/CVE-2026-39826)

  
  
## May 29, 2026

Announcement

On May 29, 2026, we released an updated version of the Apigee UI.

Feature

**Apigee EventFlow now supports the DataCapture policy**

You can now use the DataCapture policy within an EventFlow to extract and persist data from server-sent events (SSE) streams, such as token counts and other fields from streaming LLM responses. For more information, see [Use the DataCapture policy to capture token counts](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events#datacapture-token-counts).

Feature

**Manage Spaces in the Apigee UI**

You can now create, view, update, and delete spaces, and manage their Identity and Access Management (IAM) policies directly in the Apigee UI. Previously, these actions could only be performed using the Apigee API. For more information, see [Apigee Spaces overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).

## May 22, 2026

Announcement

**Apigee Emulator**

### Apigee Emulator v2.0.0

On May 22, 2026, we released Apigee Emulator version 2.0.0.

Starting with this release, the Apigee Emulator is versioned and released independently from Apigee hybrid. This enables faster delivery of security patches and updates without waiting for hybrid release cycles. The emulator image continues to be available at [Google Artifact Registry](https://console.cloud.google.com/artifacts/docker/apigee-release/us/gcr.io/hybrid%2Fapigee-emulator).

To use the new version, update the emulator version in your VS Code Cloud Code settings to `2.0.0`. See [Manage the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#choose_the_emulator_version) for details.

Feature

**Apigee Emulator**

#### Changed in this release

  * The Apigee Emulator now follows independent semantic versioning (MAJOR.MINOR.PATCH), decoupled from Apigee hybrid versioning.
  * Updated base Cassandra image to version 4.0.19.
  * Updated Java runtime to Eclipse Temurin JRE 11.0.31.



Security

**Apigee Emulator**

#### Security

This release addresses 78 security vulnerabilities across Cassandra base image, Go standard library, Java dependencies, and Python packages. Key fixes include:

CVE | Component  
---|---  
[CVE-2022-42003](https://nvd.nist.gov/vuln/detail/CVE-2022-42003) | Jackson Databind  
[CVE-2022-42004](https://nvd.nist.gov/vuln/detail/CVE-2022-42004) | Jackson Databind  
[CVE-2022-38749](https://nvd.nist.gov/vuln/detail/CVE-2022-38749) | SnakeYAML  
[CVE-2022-38750](https://nvd.nist.gov/vuln/detail/CVE-2022-38750) | SnakeYAML  
[CVE-2023-2976](https://nvd.nist.gov/vuln/detail/CVE-2023-2976) | Google Guava  
[CVE-2020-8908](https://nvd.nist.gov/vuln/detail/CVE-2020-8908) | Google Guava  
[CVE-2024-12798](https://nvd.nist.gov/vuln/detail/CVE-2024-12798) | Logback  
[CVE-2025-22866](https://nvd.nist.gov/vuln/detail/CVE-2025-22866) | Go stdlib  
[CVE-2025-22870](https://nvd.nist.gov/vuln/detail/CVE-2025-22870) | Go stdlib  
[CVE-2022-40897](https://nvd.nist.gov/vuln/detail/CVE-2022-40897) | Python setuptools  
  
And 68 additional CVEs fixed through updated upstream dependencies.

## May 21, 2026

Announcement

On May 21st, 2026, we released an updated version of Apigee (1-17-0-apigee-8).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**514973778** | Fixed Model Armor response parsing to gracefully handle unknown fields, so future Model Armor field additions no longer cause policy failures.  
  
## May 20, 2026

Security

**On May 20, 2026, we published a security bulletin for Apigee.**

A vulnerability was found in Apigee ([CVE-2026-2264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2264)) where the `IntegrationRegion` parameter in the `SetIntegrationRequest` policy lacks validation, allowing for Server-Side Request Forgery (SSRF) and service account token exfiltration. The issue arises when an attacker can control a flow variable used for `IntegrationRegion`, leading to requests being sent to an attacker-controlled host with the service account token.

**Security bulletin published:[GCP-2026-034](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-034)**

## May 12, 2026

Announcement

On May 12th, 2026, we released an updated version of Apigee (1-17-0-apigee-7).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**511325186, 505460952, 502250074, 491231600, 497357701, 509560467, 496969438, 495897297, 495033618, 511332617, 505183435, 500735547, 500890221** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities: 

  * [CVE-2026-42587](https://nvd.nist.gov/vuln/detail/CVE-2026-42587)
  * [CVE-2026-5588](https://nvd.nist.gov/vuln/detail/CVE-2026-5588)
  * [CVE-2026-34480](https://nvd.nist.gov/vuln/detail/CVE-2026-34480)
  * [GHSA-72hv-8253-57qq](https://github.com/advisories/GHSA-72hv-8253-57qq)
  * [CVE-2026-33870](https://nvd.nist.gov/vuln/detail/CVE-2026-33870)
  * [CVE-2026-33871](https://nvd.nist.gov/vuln/detail/CVE-2026-33871)
  * [CVE-2026-35611](https://nvd.nist.gov/vuln/detail/CVE-2026-35611)
  * [CVE-2026-33170](https://nvd.nist.gov/vuln/detail/CVE-2026-33170)
  * [CVE-2026-33169](https://nvd.nist.gov/vuln/detail/CVE-2026-33169)
  * [CVE-2026-33176](https://nvd.nist.gov/vuln/detail/CVE-2026-33176)
  * [CVE-2026-33210](https://nvd.nist.gov/vuln/detail/CVE-2026-33210)
  * [CVE-2026-33186](https://nvd.nist.gov/vuln/detail/CVE-2026-33186)
  * [CVE-2026-42499](https://nvd.nist.gov/vuln/detail/CVE-2026-42499)
  * [CVE-2026-35469](https://nvd.nist.gov/vuln/detail/CVE-2026-35469)
  * [CVE-2026-32281](https://nvd.nist.gov/vuln/detail/CVE-2026-32281)
  * [CVE-2026-27144](https://nvd.nist.gov/vuln/detail/CVE-2026-27144)

  
  
Fixed

Bug ID | Description  
---|---  
**480260846** | Improved XML processing security to prevent external entity injection.  
**510061670, 505723451, 503723862, 503817773** | Improved security in OAuthV2 policy.  
**505645076** | Fixed a security issue in OAuthV2 policy to prevent unauthorized token injection.  
**503047744, 410026138, 496021751** | Improved security isolation for PythonScript policy execution.  
**469694040** | Fixed an issue where custom security policies could intermittently fail to apply, and improved security policy resolution to ensure correct policy selection.  
**502971220** | Fixed a concurrency issue to improve stability under high load.  
**509692565** | Fixed content-length header handling in external processing to prevent incorrect values.  
**282207038** | Improved performance while listing apps on scale.  
**501102321** | Fixed recurring fee calculation in monetization to correctly apply rate plan overrides.  
**449729840, 502604752** | Fixed streaming response handling to prevent race conditions in bidirectional flows.  
**507167063** | Fixed preservation of client request IDs during proxy chaining.  
**507580304** | Improved IPv4 address normalization for consistent access control evaluation.  
**502692267** | MCP to handle /.well-known/oauth-protected-resource/mcp resource paths.  
**430170696** | Changed the error response from 500 to 401 for expired consumer keys.  
**480770263** | Fixed SpikeArrest policy to handle edge cases that previously caused 500 errors.  
**500861814** | Gracefully handle connection failures involving the forward proxy, resolving an issue where port exhaustion could trigger aggressive retry storms, excessive CPU usage, and unnecessary scaling.  
**500313309** | Fixed SSE streaming detection logic.  
**494304819** | Hardened message processor management ports by blocking external access to internal management endpoints.  
**469642464** | Improved input validation in AI protection policies to prevent Server-Side Request Forgery.  
**472526232** | Improved SAML assertion validation.  
**494590020** | Added enforcement for product association in OAuthV2 flow. Apps without valid products are now denied.  
**479288727** | Improved performance and reduced redundant work in ingress status watcher.  
**N/A** | Updates to infrastructure and libraries.  
  
## April 29, 2026

Announcement

On April 29th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-4** , your instance will be updated to **1-17-0-apigee-4** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

## April 09, 2026

Change

**Relaxed limitation on header name for Client IP resolution**

The client IP can now be resolved from any header, not just the `X-Forwarded-For` header. The most common headers are `X-Forwarded-For` or `True-Client-Ip`.

For more information, see [Client IP resolution](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution).

## April 06, 2026

Fixed

**Correction toApril 2, 2026 release note: Deployment disruption for Apigee Drupal Portal via Google Cloud Marketplace**

For the deployment disruption announced on April 2, the announcement noted that deployment and management functionality using Google Cloud Deployment Manager would definitely be unavailable during the transition. This statement is incorrect. The functionality _might_ be unavailable.

See the [Known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258) for more information.

Change

On April 6th, 2026, we released an updated version of Apigee.

This change introduces the new `apigee.coreServiceAgent` IAM role for Apigee. **Effective immediately, use`apigee.coreServiceAgent` instead of the `apigee.serviceAgent` role.**

For information on the new role, see [`apigee.coreServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent).

## April 02, 2026

Breaking

**Deployment disruption for Apigee Drupal Portal via Google Cloud Marketplace**

Google Cloud Deployment Manager was deprecated as of March 31, 2026. We are currently transitioning the Apigee Drupal Portal Marketplace solution to use Infrastructure Manager. During this transition period, some deployment and management functionalities are unavailable.

**Impact:**

  * **New Deployments:** Starting April 1, 2026, attempting to deploy a new Apigee Drupal Portal instance using the "Deploy" button on the Google Cloud Marketplace will fail.
  * **Existing Deployments:** Your underlying resources (such as VMs and Cloud SQL databases) are unaffected and will continue to run normally. However, you can no longer use Deployment Manager-based features to manage the deployment via the Marketplace UI or the `gcloud deployment-manager` tool.



**Workaround & Resolution:** Any configuration changes or management tasks must be performed directly on the individual Google Cloud resources (Compute Engine, Cloud SQL, etc.) rather than through the Marketplace UI.

We are actively working to release the updated Infrastructure Manager-based solution.

## March 31, 2026

Announcement

On March 31st, 2026, we released an updated version of Apigee.

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**General Availability (GA) launch of Model Context Protocol (MCP) in Apigee**

With this release, Model Context Protocol (MCP) in Apigee is [generally available](https://docs.cloud.google.com/products#product-launch-stages), enabling you to expose your Apigee APIs as MCP tools to agentic applications.

Any MCP client that supports remote MCP endpoints over HTTP/S can access these tools. Because the endpoints are managed, you don't need to install or manage local MCP servers, remote MCP servers, or additional infrastructure to enable agentic applications to access your services.

MCP in Apigee is available for Subscription, Pay-as-you-go, and Evaluation organizations, including organizations with Data Residency and VPC Service Controls enabled.

For more information on using MCP in Apigee, see [MCP in Apigee overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview).

Feature

**Enhanced OAS server URL path handling for MCP in Apigee**

With this feature enhancement, your OpenAPI specification (OAS) configurations behave exactly as defined in the OAS standard, automatically combining the `server.url` base path value with individual operation paths.

For example, a server URL of`https://example.com/api/v1` paired with a path of `/users` will now correctly route to `https://example.com/api/v1/users` without additional manual intervention.

If you previously prepended base paths to your OAS paths entries, remove the path segment from your `servers.url` field to prevent duplication. For example, change `https://example.com/api/v1` to `https://example.com`.

For more information, see [Create an OpenAPI 3.0 specification](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart#create-an-openapi-3.0.x-specification-describing-your-api-operations).

Change

**Updated MCP server target endpoint for MCP Discovery Proxies**

With the GA launch of Model Context Protocol (MCP) in Apigee, the structure of the MCP server target endpoint for MCP Discover Proxies has changed to `ORG_NAME.mcp.apigee.internal`.

Private preview customers using the previous format (`mcp.apigee.internal`) are encouraged to update their proxies to reflect the new structure. Existing endpoints using the old format will continue to work, but new endpoints will use the new structure.

Issue

**Known Issue 496552286: Deployment fails for MCP Discovery Proxies in regions with capacity limitations.**

For more information, see [Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues).

## March 26, 2026

Announcement

On March 26th, 2026, we released an updated version of Apigee (1-17-0-apigee-6).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**495897297, 495909767** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities: 

  * [CVE-2026-33210](https://nvd.nist.gov/vuln/detail/CVE-2026-33210)
  * [CVE-2026-25679](https://nvd.nist.gov/vuln/detail/CVE-2026-25679)
  * [CVE-2026-27139](https://nvd.nist.gov/vuln/detail/CVE-2026-27139)
  * [CVE-2026-27142](https://nvd.nist.gov/vuln/detail/CVE-2026-27142)
  * [2026-33186](https://nvd.nist.gov/vuln/detail/CVE-2026-33186)

  
  
Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to infrastructure and libraries.**  
  
## March 19, 2026

Announcement

On March 19th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-16-0-apigee-6** , your instance will be updated to **1-16-0-apigee-6** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

## March 17, 2026

Announcement

On March 17th, 2026, we released an updated version of Apigee (1-17-0-apigee-5).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to infrastructure and libraries.**  
  
## March 10, 2026

Announcement

On March 10th, 2026, we released an updated version of Apigee (1-17-0-apigee-4).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to infrastructure and libraries.**  
  
Security

Bug ID | Description  
---|---  
**483769763, 481735779** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities: 

  * [CVE-2025-61726](https://nvd.nist.gov/vuln/detail/CVE-2025-61726)
  * [CVE-2025-61728](https://nvd.nist.gov/vuln/detail/CVE-2025-61728)
  * [CVE-2025-61730](https://nvd.nist.gov/vuln/detail/CVE-2025-61730)
  * [CVE-2025-61731](https://nvd.nist.gov/vuln/detail/CVE-2025-61731)
  * [CVE-2025-61732](https://nvd.nist.gov/vuln/detail/CVE-2025-61732)
  * [CVE-2026-24051](https://nvd.nist.gov/vuln/detail/CVE-2026-24051)
  * [CVE-2026-25765 ](https://nvd.nist.gov/vuln/detail/CVE-2026-25765)

  
  
## February 24, 2026

Announcement

On February 24th, 2026, we released an updated version of Apigee (1-17-0-apigee-3).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**470375542** | Fixed a memory leak which could result in a spike in 503 responses with `no_healthy_upstream` messages.  
**480997525** | Applied a fix for proxy calls failing with `The URI contains illegal characters` error after Netty upgrade.  
**485595627** | Fixed an issue resulting in TLS handshake errors.  
  
Security

Bug ID | Description  
---|---  
**481735779, 457138941, 471232237** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities: 

  * [CVE-2025-61730](https://nvd.nist.gov/vuln/detail/CVE-2025-61730)
  * [CVE-2025-68156](https://nvd.nist.gov/vuln/detail/CVE-2025-68156)
  * [CVE-2025-54388](https://nvd.nist.gov/vuln/detail/CVE-2025-54388)
  * [CVE-2025-61727](https://nvd.nist.gov/vuln/detail/CVE-2025-61727)
  * [CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)

  
  
## February 13, 2026

Announcement

On February 13, 2026, we published a security bulletin for Apigee.

Security

A vulnerability was identified in the Apigee platform ([CVE-2025-13292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-13292)) that could have allowed a malicious actor with administrative or developer-level permissions in their own Apigee environment to elevate privileges and access cross-tenant data.

**Security bulletin published:[GCP-2026-010](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-010)**

## February 10, 2026

Announcement

**Note:** This release was rolled back to address an issue. See the entry for [February 24th, 2026](https://docs.cloud.google.com/apigee/docs/release-notes#February_24_2026) for the updated version number and payload.

On February 10, 2026, we released an updated version of Apigee (1-17-0-apigee-2).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

**Note:** This note is incorrect - these security fixes, including the removal of support for the `TLS_RSA` cipher suites, were rolled back. See the entry for [February 24th, 2026](https://docs.cloud.google.com/apigee/docs/release-notes#February_24_2026) for the updated version number and payload.Bug ID | Description  
---|---  
**481735779, 457138941, 471232237** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities: 

  * [CVE-2025-61730](https://nvd.nist.gov/vuln/detail/CVE-2025-61730)
  * [CVE-2025-68156](https://nvd.nist.gov/vuln/detail/CVE-2025-68156)
  * [CVE-2025-54388](https://nvd.nist.gov/vuln/detail/CVE-2025-54388)
  * [CVE-2025-61727](https://nvd.nist.gov/vuln/detail/CVE-2025-61727)
  * [CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)

  
**470375542** | Fixed a memory leak which could result in a spike in 503 responses with `no_healthy_upstream` messages.  
**480997525** | Applied a fix for proxy calls failing with `The URI contains illegal characters` error after Netty upgrade.  
**485543125** | Apigee no longer supports the following `TLS_RSA` cipher suites:

  * `TLS_RSA_WITH_AES_256_GCM_SHA384`
  * `TLS_RSA_WITH_AES_128_GCM_SHA256`
  * `TLS_RSA_WITH_AES_256_CBC_SHA256`
  * `TLS_RSA_WITH_AES_128_CBC_SHA256`
  * `TLS_RSA_WITH_AES_256_CBC_SHA`
  * `TLS_RSA_WITH_AES_128_CBC_SHA`

  
  
## February 06, 2026

Announcement

On February 6th, 2026, we released an updated version of Apigee.

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**477294854, 477297075, 477297324, 470988850, 471662549** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:

  * [CVE-2025-58187](https://nvd.nist.gov/vuln/detail/CVE-2025-58187)
  * [CVE-2025-61723](https://nvd.nist.gov/vuln/detail/CVE-2025-61723)
  * [CVE-2025-61725](https://nvd.nist.gov/vuln/detail/CVE-2025-61725)
  * [CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)
  * [CVE-2025-61727](https://nvd.nist.gov/vuln/detail/CVE-2025-61727)

  
  
## February 02, 2026

Issue

**Known Issue:** [480997525 - Proxy calls fail with `The URI contains illegal characters` error after Netty upgrade](https://docs.cloud.google.com/apigee/docs/release/known-issues#480997525)

## January 21, 2026

Announcement

On January 21st, 2026, we released an updated version of Apigee (1-17-0-apigee-1).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**471001896, 469829527, 470953822, 462478248, 474415498** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:

  * [CVE-2025-68161](https://nvd.nist.gov/vuln/detail/CVE-2025-68161)
  * [CVE-2025-67735](https://nvd.nist.gov/vuln/detail/CVE-2025-67735)
  * [CVE-2025-47914](https://nvd.nist.gov/vuln/detail/CVE-2025-47914)
  * [CVE-2025-58181](https://nvd.nist.gov/vuln/detail/CVE-2025-58181)
  * [CVE-2025-58767](https://nvd.nist.gov/vuln/detail/CVE-2025-58767)
  * [CVE-2025-4802](https://nvd.nist.gov/vuln/detail/CVE-2025-4802)
  * [CVE-2025-8058](https://nvd.nist.gov/vuln/detail/CVE-2025-8058)
  * [CVE-2025-61727](https://nvd.nist.gov/vuln/detail/CVE-2025-61727)
  * [CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729)
  * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868)
  * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869)
  * [CVE-2025-22870](https://nvd.nist.gov/vuln/detail/CVE-2025-22870)
  * [CVE-2025-22872](https://nvd.nist.gov/vuln/detail/CVE-2025-22872)

  
  
Fixed

Bug ID | Description  
---|---  
**433999957** | **Implemented full TLS validation when fetching JWKS from remote URIs**  
**467762922** | **Quota enforcement logic for Server-Sent Events (SSE) updated** Quotas for SSE are now calculated strictly for events containing explicit token counts. The quota enforcement logic skips SSE that lack token usage metadata.  
**N/A** | **Updates to security, infrastructure, and libraries.**  
  
## December 29, 2025

Announcement

On December 29th, 2025, we released an updated version of Apigee.

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**The Apigee Extension Processor provisioning API is available**

Apigee Extension Processor customers can now use the Extension Processor provisioning API to create traffic extensions. For more information, see [Get started with the Apigee Extension Processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart#create-traffic-ext)

## December 23, 2025

Announcement

On December 23, 2025, we released an updated version of Apigee.

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**New Apigee policies for LLM Token Management are now Generally Available (GA)**

Two new Apigee policies for managing Large Language Model (LLM) workloads are now Generally Available (GA). These policies provide fine-grained control and rate-limiting for AI application traffic as follows:

  * **LLMTokenQuota policy**
    * This policy monitors and enforces limits on **LLM response token usage** to control overall LLM expenditure and resource allocation.
    * It can be configured with `<CountOnly>` (placed in the response flow to track tokens consumed) or `<EnforceOnly>` (placed in the request flow to block calls if the quota is exceeded).
    * If the quota is reached, Apigee returns an `HTTP 429` (Too Many Requests) status code.
    * For more information, see [LLMTokenQuota Policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy).
  * **PromptTokenLimit policy**
    * This policy provides a token-based rate-limiting mechanism analogous to the SpikeArrest policy, specifically for the tokens consumed by the user's prompt message.
    * It calculates the prompt's token count using the widely adopted `o200k_base` encoding technique.
    * If the configured token rate limit is exceeded, the incoming request is blocked, returning an `HTTP 429` (Too Many Requests) status code.
    * For more information, see [PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy).



**Related documents:**

  * [Get started with Apigee AI token policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-ai-token-policies)
  * [Rate-limiting](https://docs.cloud.google.com/apigee/docs/api-platform/develop/rate-limiting)
  * [Comparing rate-limiting policies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/comparing-quota-and-spike-arrest-policies)
  * [Managing API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products)
  * [LLMTokenQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy)
  * [PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy)



## December 10, 2025

Announcement

On December 10th, 2025, we released an updated version of Apigee (1-16-0-apigee-6).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**458417250** | **Multiple authorization headers** Fixed issue where adding multiple authorization headers would cause Apigee to return a `500` error.  
**N/A** | **Updates to security, infrastructure, and libraries.**  
  
## December 04, 2025

Feature

**Mask KVM values**

You can now turn on key value map (KVM) masking to mask values with asterisks (*****). For more information, see [About KVM masking](https://docs.cloud.google.com/apigee/docs/api-platform/cache/key-value-maps#aboutmasking).

## November 17, 2025

Announcement

On November 17, 2025, we released an updated version of Apigee (1-16-0-apigee-5).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**Secure and validate documents using WS-Security with X.509 certificates**  
  
You can now secure and validate SOAP documents using WS-Security with X.509 certificates using crypto object methods. See [Secure SOAP documents using WS-Security with X.509 certificates](https://docs.cloud.google.com/apigee/docs/api-platform/reference/javascript-object-model#cryptoobjectreference-cryptowsSecRsaSign) and [Validate SOAP documents using WS-Security with X.509 certificates](https://docs.cloud.google.com/apigee/docs/api-platform/reference/javascript-object-model#cryptoobjectreference-cryptowsSecRsaValidate).

Change

**New field available in the Apigee Organization API**

With this release, a new field is added to the [Apigee Organization API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#Organization). The new `caCertificates` (plural) field returns the value of the original CA certificate field and can hold additional values. The original `caCertificate` (singular) field is deprecated.

Security

Bug ID | Description  
---|---  
**454672970** | **Added strict input validation to the`SetIntegrationRequest` policy**  
  
Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to security, infrastructure, and libraries.**  
  
## October 31, 2025

Announcement

On October 31, 2025, we released an updated version of Apigee (1-16-0-apigee-4).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**452621774, 452381632, 441266643, 448498138** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:

  * [CVE-2025-53864](https://nvd.nist.gov/vuln/detail/CVE-2025-53864)Updated Nimbus JWT library from 9.37.2 to 9.37.4, which introduced changes in behavior including changes to error string verbiage.
  * [CVE-2025-8916](https://nvd.nist.gov/vuln/detail/CVE-2025-8916)
  * [CVE-2025-5115](https://nvd.nist.gov/vuln/detail/CVE-2025-5115)
  * [CVE-2024-40094](https://nvd.nist.gov/vuln/detail/CVE-2024-53864)

  
  
Fixed

Bug ID | Description  
---|---  
**448647917** | **Fixed a issue where non-SSL connections through a forward proxy could be improperly shared.**  
**N/A** | **Updates to security, infrastructure, and libraries.**  
  
## October 29, 2025

Announcement

On October 29, 2025, we released an updated version of Apigee.

Feature

**Support for API-product scoped quotas**

You can now set quotas at the API product level to limit the number of requests all API proxies in the API product can process within a specified time frame. See [Configuring the quota policy to use API product quota settings](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#configuring-the-quota-policy-to-use-api-product-quota-settings) for information and instructions.

NOTE: API product-scoped quotas are not supported in Apigee hybrid at this time.

Feature

**Enhanced Validation for API products**

Heightened validation logic for creating and updating API products is now available. Apigee now explicitly verifies proxy and environment resources against your organization when creating and updating API products.

Please ensure that all referenced resources exist and are correctly associated with your organization to avoid validation errors.

## October 27, 2025

Announcement

On October 27, 2025, we released an updated version of Apigee.

Feature

**Introduction of the`target.evaluated.url` flow variable**

This release includes a new flow variable, `target.evaluated.url`, which should be used instead of the `target.url` flow variable in cases when the URL is dynamically constructed based on user input.

For more information, see the [target flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#target) documentation.

## October 16, 2025

Security

Bug ID | Description  
---|---  
**440419558, 433759657** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities:

  * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868)
  * [CVE-2025-48924](https://nvd.nist.gov/vuln/detail/CVE-2025-48924)
**Note** : This fix updates a Java library that is included in Apigee. Reliance on Java libraries that are included with Apigee is not supported. Those libraries are for Apigee product functionality only, and there's no guarantee that a library will be available from release to release. For more information, see [Restrictions](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy#Restrictions).
  
**443902061** | **Security fix for Apigee infrastructure** This addresses the following vulnerability:

  * CVE-2025-13292Fixed an issue with improper access control that resulted in cross-tenant analytics modification and access to log data.

  
  
Fixed

Bug ID | Description  
---|---  
**442501403** | **Fixed an issue that caused incorrect target latency metrics in Apigee Analytics when a TargetEndpoint is configured with a <LoadBalancer>.**  
**437999897** | **Reduced the log level for failed geo IP lookups to address excessive log messages for private IP addresses.**  
**436323210** | **Fixed ingress cert keys to allow both`tls.key`/`key` and `tls.crt`/`cert`.**  
**438192028** | **Updated the geolocation database to mitigate stale IP-to-location mappings.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
Announcement

On October 16, 2025, we released an updated version of Apigee (1-16-0-apigee-3).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## October 14, 2025

Deprecated

**Removal of deprecated Gemini Code Assist`@Apigee` tool.**

The Gemini Code Assist `@Apigee` tool is shut down as of October 14, 2025.

See [Gemini Code Assist @Apigee tool deprecation](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-tool) for information.

## October 09, 2025

Deprecated

**Deprecation of the Gemini Code Assist`@Apigee` tool.**

The Gemini Code Assist `@Apigee` tool is deprecated and will be shut down as of October 14, 2025.

See [Gemini Code Assist @Apigee tool deprecation](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-tool) for information.

## October 07, 2025

Breaking

**Previously unreported customer DNS misconfigurations now result in DNS errors**

Apigee removed the automatic DNS fallback functionality that was in 1-16-0-apigee-2. This removal surfaces customer DNS misconfigurations that previously did not show as DNS errors.

See [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues#445936920).

## September 12, 2025

Security

Bug ID | Description  
---|---  
**N/A** | **Security fix for`apigee-runtime`.**  
  
Announcement

On September 12, 2025, we released an updated version of Apigee (1-16-0-apigee-2).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## September 11, 2025

Change

**API hub navigation update**

The **API hub** section is now moved to the top level of the Apigee left navigation menu. This change improves discoverability and access to the API hub features.

## September 09, 2025

Announcement

On September 9, 2025, we released an updated version of Apigee (1-16-0-apigee-1).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Change

Bug ID | Description  
---|---  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## September 04, 2025

Announcement

On September 4, 2025, we released an updated version of Apigee.

Feature

**Apigee policies for LLM/GenAI workloads are Generally Available (GA)**

Four new Apigee policies supporting LLM/GenAI workloads are now [GA](https://cloud.google.com/products#product-launch-stages):

  * [SemanticCacheLookup policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy)
  * [SemanticCachePopulate policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy)
  * [SanitizeUserPrompt](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)
  * [SanitizeModelResponse](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)



The Apigee semantic caching policies enable intelligent response reuse based on semantic similarity. Using these policies in your Apigee API proxies can minimize redundant backend API calls, reduce latency, and lower operational costs. With this release, the semantic caching policies support URL templating, enabling the use of variables for AI model endpoint values.

The Model Armor policies protect your AI applications by sanitizing user prompts to and responses from large language models (LLMs). Using these policies in your Apigee API proxies can mitigate the risks associated with LLM usage by leveraging Model Armor to detect prompt injection, prevent jailbreak attacks, apply responsible AI filters, filter malicious URLs, and protect sensitive data.

For more information on using these policies in your Apigee API proxies, see:

  * [Get started with semantic caching policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies)
  * [Get started with Apigee Model Armor policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies)



## September 03, 2025

Feature

**Apigee Server-Sent Events (SSE) and EventFlows are supported for use with the Apigee Extension Processor.**

The Apigee SSE feature enables continuous response streaming from server-sent event (SSE) endpoints to clients in real time. To learn more about this feature, see [Streaming server-sent events](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).

The Apigee Extension Processor is a [traffic extension](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb) that lets you use Cloud Load Balancing to send callouts from the data processing path of the application load balancer to the Apigee Extension Processor. To learn more, see the [Apigee Extension Processor overview](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview).

Announcement

On September 3, 2025, we released an updated version of Apigee.

## August 27, 2025

Security

Bug ID | Description  
---|---  
**427752569** | **Security fix for Apigee infrastructure.**  
This addresses the following vulnerabilities: 

  * [CVE-2025-22872](https://nvd.nist.gov/vuln/detail/CVE-2025-22872)
  * [CVE-2025-22870](https://nvd.nist.gov/vuln/detail/CVE-2025-22870)
  * [CVE-2025-22868](https://nvd.nist.gov/vuln/detail/CVE-2025-22868)
  * [CVE-2025-22869](https://nvd.nist.gov/vuln/detail/CVE-2025-22869)

  
  
Announcement

On August 27, 2025, we released an updated version of Apigee (1-15-0-apigee-9).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**420901514** | **Enhanced WebSocket authentication.**  
**429245088** | **Implemented option to override endpoints in the PublishMessage policy.**  
**405039175** | **Resolved issue causing duplicate x-b3-* headers when Distributed Trace is enabled.**  
**378686709** | **Resolved issue causing unexpected`404` errors when using wildcards in proxy basepaths.**  
**429245268** | **Implemented option to override endpoints in the MessageLogging policy.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## August 04, 2025

Announcement

On August 4, 2025, we released an updated version of Apigee (1-15-0-apigee-8).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**Server-sent events and EventFlows are[Generally Available (GA)](https://cloud.google.com/products#product-launch-stages)**

Apigee supports continuous response streaming from server-sent event (SSE) endpoints to clients in real time. The Apigee SSE feature is useful for handling large language model (LLM) APIs that operate most effectively by streaming their responses back to the client. SSE streaming reduces latency, and clients can receive response data as soon as it is generated by an LLM. This feature supports the use of AI agents that operate in real time environments, such as customer service bots or workflow orchestrators. For more information, see [Streaming server-sent events](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).

Streaming from SSE endpoints is available in Apigee and in Apigee hybrid v1.15.0 and newer.

Fixed

Bug ID | Description  
---|---  
**435620966** | **Fixed a regression that occurred when upgrading from ASM 1.22 to 1.23 that resulted in 503 errors.**  
**422195061** | **Enhanced cache lookup performance.**  
**269573358** | **Resolved issue with OASValidation policy schema references for parameters without body validation** The OASValidation policy correctly resolves and validates schemas passed by reference (`$ref`) for header, path, and query parameters, even when the <ValidateMessageBody> flag is set to `false`.  
**421141062** | **Increased OAS validation limit to 20MB in JSON payloads to prevent validation failures.**  
**417200603** | **Improved API connection stability to prevent premature timeouts for long-running requests.**  
**423597917** | **`POST` operations for AppGroupApp keys updated** `POST` operations for AppGroup app keys now insert scopes and attributes instead of appending these values. This behavior is consistent with `POST` operations for companies in Apigee Edge for Public Cloud.  
**390234048** | **Resolved issue resulting in missing fields in API responses for Monetization rate plans** The `createdAt` and `lastModifiedAt` fields are now present in responses from the `organizations.apiproducts.rateplans` API.  
**422757662** | **Reverted problematic commit regarding X-b3 trace headers send when using distributed tracing.**  
**409048431** | **Fixed a SAML signature verification bypass vulnerability.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## July 30, 2025

Announcement

On July 30, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

  * Develop > API Proxies
  * Develop > Shared Flows
  * Develop > Offline Debug



See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## July 28, 2025

Feature

**Server-sent events and EventFlows are[Generally Available (GA)](https://cloud.google.com/products#product-launch-stages)**

Apigee supports continuous response streaming from server-sent event (SSE) endpoints to clients in real time. The Apigee SSE feature is useful for handling large language model (LLM) APIs that operate most effectively by streaming their responses back to the client. SSE streaming reduces latency, and clients can receive response data as soon as it is generated by an LLM. This feature supports the use of AI agents that operate in real time environments, such as customer service bots or workflow orchestrators. For more information, see [Streaming server-sent events](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).

Streaming from SSE endpoints is available in Apigee and in Apigee hybrid v1.15.0 and newer.

Announcement

On July 28, 2025, we released an updated version of Apigee (1-15-0-apigee-7).

**Note:** This release has been rolled back to address am issue. See entry for [August 4, 2025](https://docs.cloud.google.com/apigee/docs/release-notes#August_04_2025) for the updated version number and payload.

Fixed

Bug ID | Description  
---|---  
**422195061** | **Enhanced cache lookup performance.**  
**269573358** | **Resolved issue with OASValidation policy schema references for parameters without body validation** The OASValidation policy correctly resolves and validates schemas passed by reference (`$ref`) for header, path, and query parameters, even when the <ValidateMessageBody> flag is set to `false`.  
**421141062** | **Increased OAS validation limit to 20MB in JSON payloads to prevent validation failures.**  
**417200603** | **Improved API connection stability to prevent premature timeouts for long-running requests.**  
**423597917** | **`POST` operations for AppGroupApp keys updated** `POST` operations for AppGroup app keys now insert scopes and attributes instead of appending these values. This behavior is consistent with `POST` operations for companies in Apigee Edge for Public Cloud.  
**390234048** | **Resolved issue resulting in missing fields in API responses for Monetization rate plans** The `createdAt` and `lastModifiedAt` fields are now present in responses from the `organizations.apiproducts.rateplans` API.  
**422757662** | **Reverted problematic commit regarding X-b3 trace headers send when using distributed tracing.**  
**409048431** | **Fixed a SAML signature verification bypass vulnerability.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## July 24, 2025

Announcement

On July 24, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

  * Publish > Portals



See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## June 25, 2025

Announcement

On June 25, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

  * Publish > API products
  * Publish > Developers
  * Publish > Apps
  * Admin > Instances
  * Admin > Data collectors
  * Admin > Environments
  * Admin > Endpoint attachments



See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## June 17, 2025

Announcement

On June 17, 2025 we began redirecting the following Apigee Classic UI navigation items to Apigee UI in the Google Cloud console:

  * Publish > Monetization
  * Analyze > API monitoring
  * Analyze > API metrics
  * Analyze > Developers > Developer Engagement
  * Analyze > Developers > Traffic Composition
  * Analyze > End Users > Devices
  * Analyze > End Users > Geomap
  * Analyze > Custom reports



See [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for a mapping of each Classic Apigee UI feature page to its location in the Apigee UI in Cloud console.

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates.

If you require more time to transition to the Google Cloud console, submit the [exception request form](https://docs.google.com/forms/d/e/1FAIpQLSedFe2Pj2f9B8YxD7cgWOyf8-IjRA8IhRZpZ2jXMZ9DU1uz1g/viewform) by Aug 15, 2025.

## June 03, 2025

Feature

**Apigee API hub is enabled for new Apigee organizations in supported regions.**

With this release, we are enabling [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) for new Apigee organizations [in regions where API hub is supported](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-analytics-regions). All new Apigee organizations, including hybrid organizations, that select an API hub-supported region _for their Apigee Analytics region_ during provisioning will have access to API hub features at no additional cost. 

API hub allows you to view, organize, and manage all of the APIs in your Apigee organization in one central location. To learn more, see [What is Apigee API hub?](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub)

No action on your part is required to provision API hub for your organization, with the following exceptions:

  * If your Apigee organization has Data Residency or VPC Service Controls enabled, you must configure your API hub instance manually to support these services. See [VPC Service Controls for API hub](https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control) and [API hub and data residency](https://docs.cloud.google.com/apigee/docs/apihub/locations#drz-api-hub) for more information.
  * If your Apigee organization uses Customer-Managed Encryption Keys (CMEK), you must deprovision the Apigee API hub instance provided by default and recreate it to support CMEK. See [Deprovision Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/deprovision) and [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision) for step-by-step instructions.



Contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support) for questions or assistance.

Announcement

On June 3, 2025, we released an updated version of Apigee.

## June 02, 2025

Announcement

On June 2, 2025, we released an updated version of Apigee (1-15-0-apigee-5).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**New flow variables available for VerifyAPIKey policy**

Two new flow variables have been added to the [VerifyAPIKey](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) policy.

  * `app_group_app`
  * `app_group_name`



To learn more, see [Using flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/introduction-flow-variables).

Fixed

Bug ID | Description  
---|---  
**410670597** | **Fixed the proxy response count metric (`proxy/response_count`) for EventFlow-enabled streaming proxies.**  
**375360455** | **Resolved issues with connection termination when using HTTP streaming** Added automatic retries for connection reset due to upstream services.  
**N/A** | **Updates to security infrastructure and libraries.**  
**N/A** | **`x-b3` trace headers will be sent only when distributed tracing is enabled.** In previous releases Apigee was sending `x-b3` trace headers even when distributed tracing was disabled. This was an unexpected behavior which is fixed in this release.  
  
## May 30, 2025

Announcement

On May 30, 2025 we released an updated version of Apigee.

Feature

**Announcing the general availability of Gemini Code Assist API development features in Apigee**

With this functionality, you can accelerate your API development lifecycle within VS Code using Gemini Code Assist in Apigee. This feature allows you to use natural language prompts to design, create, iterate, and manage OpenAPI specifications with the following capabilities:

  * **AI-Powered API Design** : Generate high-quality OpenAPI specifications from natural language prompts to the Apigee tool in Gemini Code Assist Chat, leveraging the Gemini model and the enterprise context of your API hub.
  * **Effortless Iteration** : Refine existing or newly generated specifications using the intuitive Gemini chat interface.
  * **Integrated Testing** : Quickly validate your APIs by deploying them to a local or Google Cloud-hosted mock server.
  * **Streamlined Workflow** : Publish your completed API specifications directly to Apigee API hub and kick-start proxy development by creating Apigee proxy bundles from your API specifications.
  * **Duplicate Endpoint Detection** : Proactively identify and prevent the creation of duplicate API endpoints already registered in your API hub.



For more information and usage instructions, see [Designing and editing APIs](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis), [Tutorial: Use Gemini Code Assist to design, develop, and test APIs in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/tutorial-gemini), and [Setting up Apigee API Management in Cloud Code for VS Code](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/setup).

## May 29, 2025

Announcement

On May 29, 2025 we announced the shutdown schedule for the Apigee Classic UI.

Feature

**Public Preview: Apigee Extension Processor support for request and response body processing**

When creating a load balancer service extension, you can customize the behavior of the extension processor proxy to support request body processing, response body processing, or a combination of the two.

For more information, see [Get started with the Apigee Extension Processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart#create-lb-ext).

Announcement

On May 29, 2025, we released an updated version of Apigee.

Deprecated

The Apigee Classic UI will be shutdown as of August 29, 2025.

This is the final phase of moving Apigee to the Google Cloud console. Apigee in the Google Cloud console gives you the ability to manage all of your Apigee functionality in one place.

To prepare for the shutdown of the Apigee Classic UI, familiarize yourself with the new Apigee UI in Google Cloud console by reviewing [UI overview](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview).

See [Apigee Classic UI shutdown](https://docs.cloud.google.com/apigee/docs/deprecations/apigee-classic-ui) for details on shutdown dates and exception request.

## May 22, 2025

Announcement

On May 22, 2025, we released an updated version of Apigee.

Feature

**Public preview of server-sent events**

Apigee now supports continuous response streaming from server-sent event (SSE) endpoints to clients in real time. The Apigee SSE feature is useful for handling large language model (LLM) APIs that operate most effectively by streaming their responses back to the client. SSE streaming reduces latency, and clients can receive response data as soon as it is generated by an LLM. This feature supports the use of AI agents that operate in real time environments, such as customer service bots or workflow orchestrators. For more information, see [Streaming server-sent events](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events).

Feature

**Public Preview of Apigee policies for LLM/GenAI workloads**

Four new Apigee policies supporting LLM/GenAI workloads are now available in [Public Preview](https://cloud.google.com/products#product-launch-stages):

  * [SemanticCacheLookup policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-lookup-policy)
  * [SemanticCachePopulate policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/semantic-cache-populate-policy)
  * [SanitizeUserPrompt](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)
  * [SanitizeModelResponse](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy)



The Apigee semantic caching policies enable intelligent response reuse based on semantic similarity. Using these policies in your Apigee API proxies can minimize redundant backend API calls, reduce latency, and lower operational costs.

The Model Armor policies protect your AI applications by sanitizing user prompts to and responses from large language models (LLMs). Using these policies in your Apigee API proxies can mitigate the risks associated with LLM usage by leveraging Model Armor to detect prompt injection, prevent jailbreak attacks, apply responsible AI filters, filter malicious URLs, and protect sensitive data.

For more information on using these policies in your Apigee API proxies, see:

  * [Get started with semantic caching policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-semantic-caching-policies)
  * [Get started with Apigee Model Armor policies](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-model-armor-policies)



## May 14, 2025

Announcement

On May 14, 2025, we released an updated version of Apigee (1-15-0-apigee-4).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**Large message payload support in Apigee**

Apigee now supports message payloads up to 30MB. For more information, see:

  * [Message payload size](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#size).
  * `Properties` in the [ProxyEndpoint configuration elements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-proxyendpointconfigurationelements) reference.
  * `Properties` in the [TargetEndpoint configuration elements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint-targetendpointconfigurationelements) reference.



Feature

**Improvements to the AppGroups functionality**

Scopes and attributes can now be added to the AppGroup App Key via a POST operation on the key using the appGroupAppKey. See the [updateAppGroupAppKey API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/updateAppGroupAppKey) for details.

Feature

**Improvements to the PublishMessage policy**

The [PublishMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy) now supports two new elements:

  * The **< UseMessageAsSource>** element uses request or response message content as the source of data to be written to [Pub/Sub](https://docs.cloud.google.com/pubsub). For more information, see [<UseMessageAsSource>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#umas).

  * The **< Attributes>** element lets you specify string attributes (key/value pairs) to include with the request or response message that is written to Pub/Sub. For more information, see [<Attributes>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#attributes).




Fixed

Bug ID | Description  
---|---  
**391140293** | **Resolved scaling issue resulting in`503` errors** Added `drainDuration` and updated the values for `terminationDrainDuration` and `terminationGracePeriodSeconds`.  
**391862684** | **Resolved issue with requests stuck at Message Processor causing timeouts.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## May 06, 2025

Announcement

On May 6, 2025, we released a new Apigee REST resource for debug sessions.

Feature

Apigee now offers a Management API that allows users to list all recent debug sessions for a given proxy, regardless of revision or environment and current deployment status. This API is available for use, and is now used to populate all recent debug sessions in the Apigee Debug UI. 

For more information on this method, see: [organizations.apis.debugsessions.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.debugsessions/list)

## May 02, 2025

Feature

**Large message payload support in Apigee**

Apigee now supports message payloads up to 30MB. For more information, see:

  * [Message payload size](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development#size).
  * `Properties` in the [ProxyEndpoint configuration elements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#proxyendpoint-proxyendpointconfigurationelements) reference.
  * `Properties` in the [TargetEndpoint configuration elements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#targetendpoint-targetendpointconfigurationelements) reference.



Announcement

On May 2, 2025, we released an updated version of Apigee (1-15-0-apigee-3).

**Note:** This release has been rolled back to address an issue. 

See entry for [May 14, 2025](https://docs.cloud.google.com/apigee/docs/release-notes#May_14_2025) for the updated version number and payload.

Feature

**Improvements to the PublishMessage policy**

The [PublishMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy) now supports two new elements:

  * The **< UseMessageAsSource>** element uses request or response message content as the source of data to be written to [Pub/Sub](https://docs.cloud.google.com/pubsub). For more information, see [<UseMessageAsSource>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#umas).

  * The **< Attributes>** element lets you specify string attributes (key/value pairs) to include with the request or response message that is written to Pub/Sub. For more information, see [<Attributes>](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy#attributes).




Fixed

Bug ID | Description  
---|---  
**391140293** | **Resolved scaling issue resulting in`503` errors** Added `drainDuration` and updated the values for `terminationDrainDuration` and `terminationGracePeriodSeconds`.  
**391862684** | **Resolved issue with requests stuck at Message Processor causing timeouts.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## April 29, 2025

Announcement

On April 29, 2025, we released an updated version of Apigee.

Feature

**Apigee API hub is enabled for existing Apigee organizations in supported regions.**

With this release, we are enabling [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) for existing Apigee organizations [in regions where API hub is supported](https://docs.cloud.google.com/apigee/docs/apihub/locations#supported-locations). All existing Apigee organizations, including hybrid organizations, that selected an API hub-supported region _for their Apigee Analytics region_ will have access to API hub features at no additional cost. 

API hub allows you to view, organize, and manage all of the APIs in your Apigee organization in one central location. To learn more, see [What is Apigee API hub?](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub)

The process of enabling API hub for these organizations will continue over the next several weeks until all eligible organizations are updated. No action on your part is required to provision API hub for your organization, with the following exceptions:

  * If your Apigee organization has Data Residency or VPC Service Controls enabled, you must configure your API hub instance manually to support these services. See [VPC Service Controls for API hub](https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control) and [API hub and data residency](https://docs.cloud.google.com/apigee/docs/apihub/locations#drz-api-hub) for more information.
  * If your Apigee organization uses Customer-Managed Encryption Keys (CMEK), you must deprovision the Apigee API hub instance provided by default and recreate it to support CMEK. See [Deprovision Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/deprovision) and [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision) for step-by-step instructions.



Contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support) for questions or assistance.

## April 14, 2025

Announcement

On April 14, 2025 we released an updated version of Apigee.

Feature

**Announcing data collectors data residency (DRZ) compliance for Apigee and Apigee hybrid.**

Data collectors can be used with data residency for Subscription and Pay-as-you-go organizations and hybrid versions 1.14.0 and later.

See [Data residency compatibility](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-compatibility) for information.

## April 10, 2025

Announcement

On April 10, 2025, we released an updated version of Apigee.

Feature

The Apigee Extension Processor is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

The Apigee Extension Processor lets Apigee customers add API management capabilities to Google Cloud and third-party products and services exposed using Cloud Load Balancing. Select from a range of Apigee policies that enable you to:

  * Secure access to your workloads.
  * Apply quota enforcement to network traffic.
  * Manage Google access token and Google ID token injection to authenticate requests.
  * Support native protocols like gRPC, SSE, and HTTP/3.



For more information, see the [Apigee Extension Processor overview](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview).

## March 31, 2025

Announcement

On March 31, 2025, we released an updated version of Apigee (1-15-0-apigee-2). 

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**New flow variable suffixes available for accessing base64-encoded message content.**

There are two new read-only flow variable suffixes available for accessing message content in base64-encoded form: 

  * `content.as.base64`
  * `content.as.url.safe.base64`



These variable suffixes can be used with the `request`, `response`, and `message` objects, as well as with any `Message` object created implicitly during API proxy execution when using the AssignMessage or ServiceCallout policies. 

For more information, see [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

Fixed

Bug ID | Description  
---|---  
  
| **N/A** | **Updates to security infrastructure and libraries.**

## March 27, 2025

Announcement

On March 27, 2025, we released an updated version of Apigee.

Feature

**Availability of client IP resolution functionality with Apigee hybrid.**

Client IP resolution functonality is now available with Apigee hybrid versions 1.14.0 and later. 

See [Client IP resolution](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution) for information.

Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to security infrastructure and libraries.**  
  
Change

On March 26, 2025, we released an updated version of Apigee (1-14-0-apigee-5). This Apigee version applies _only_ to organizations using the [**JavaCallout** policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/java-callout-policy) in production environments.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## March 24, 2025

Feature

**Apigee Spaces is now[generally available (GA)](https://cloud.google.com/products#product-launch-stages) for use in Apigee organizations.**

Apigee Spaces enables identity-based isolation and grouping of API resources within an Apigee organization. With Apigee Spaces, you can have granular IAM control over access to your API proxies, shared flows, and API products.

Spaces also provide the option of resource isolation at a team level, providing a clear separation of resources associated with different teams operating within the same Apigee organization. IAM policies can be applied at the Space level, eliminating the need to manage permissions individually for every API proxy, shared flow, and API product.

Spaces are a brand new resource type with resource-level permissions. This means that Space permissions are not subject to the 64k limitation for project-level IAM conditions. Each space has its own 64k limit.

To learn more, see [Apigee Spaces overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).

Announcement

On March 24, 2025, we released an updated version of Apigee.

## March 17, 2025

Announcement

On March 17, 2025, Apigee announced the GA support for DNS peering for Apigee organizations that have VPC peering disabled.

Feature

For Apigee organizations set up without VPC peering, you can now configure Apigee to resolve your private domains by peering your DNS zones with Apigee. See [Connecting with private DNS peering zones](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#connecting-with-private-dns-peering-zones).

## March 12, 2025

Security

Bug ID | Description  
---|---  
**396944778** | **Security fix for Apigee infrastructure.**  
This addresses the following vulnerabilities: 

  * [CVE-2025-23184](https://nvd.nist.gov/vuln/detail/CVE-2025-23184)
  * [CVE-2024-47554](https://nvd.nist.gov/vuln/detail/CVE-2024-47554)
  * [CVE-2025-24970](https://nvd.nist.gov/vuln/detail/CVE-2025-24970)
  * [CVE-2025-25193](https://nvd.nist.gov/vuln/detail/CVE-2025-25193)

  
  
Announcement

On March 12, 2025, we released an updated version of Apigee (1-15-0-apigee-1).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Issue

**The[Nimbus JOSE + JWT](https://connect2id.com/products/nimbus-jose-jwt) library may cause a java.lang.ClassCircularityError when using a JavaCallout policy.**

For more information, see [Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues).

**Note:** If you have a Apigee hybrid-enabled organization with a JavaCallout policy that uses the Nimbus JOSE + JWT library, **do not upgrade to hybrid versions 1.12.4, 1.13.3, or 1.14.1**.

Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## February 28, 2025

Announcement

On February 28, 2025, we released an updated version of Apigee (1-14-0-apigee-8).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**382883585** | **Fixed a vulnerability in the JavaCallout policy.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## February 19, 2025

Announcement

On February 19, 2025, we released an updated version of Apigee (1-14-0-apigee-7).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**391714121** | **Security fix for Apigee infrastructure.**  
This addresses the following vulnerability: 

  * [CVE-2024-45338](https://nvd.nist.gov/vuln/detail/CVE-2024-45338)

  
  
Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## February 06, 2025

Announcement

On February 6, 2025, we released an updated version of Apigee (1-14-0-apigee-6).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**381553288** | **Fixed class initialization issue in JavaCallout policy.**  
**390559772** | **Fixed issue with ResponseCache policy not appearing in debug sessions when added using Apigee APIM Operator for Kubernetes.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## February 03, 2025

Feature

**Public Preview of the Apigee APIM Operator for Kubernetes**

The Apigee APIM Operator for Kubernetes (Preview) allows you to perform API management tasks using Kubernetes tools. It is designed to support cloud-native developers by providing a command-line interface that integrates with familiar Kubernetes tools like `kubectl`. The operator works by using various APIM resources to keep your Google Kubernetes Engine (GKE) cluster synchronized with the Apigee runtime.

For more information, see [Apigee APIM Operator for Kubernetes overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-overview).

## January 24, 2025

Announcement

On January 24, 2025, we released an updated version of Apigee (1-14-0-apigee-4).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**372248577** | **Fixed issue causing`system.pod.name` flow variable to return `null`.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## January 09, 2025

Fixed

Bug ID | Description  
---|---  
**365406457** | **Implemented fix to optimize CPU usage and close sockets when needed.**  
**382967738, 383113773** | **Fixed security vulnerability in PythonScript policy.**  
**382883585** | **Fixed security vulnerability in JavaCallout policy.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
Announcement

On January 9, 2025, we released an updated version of Apigee (1-14-0-apigee-3).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## December 20, 2024

Announcement

On December 20, 2024 we released an updated version of Apigee.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Support for environment-level client IP address resolution**

This release introduces the ability to specify, per environment, how to capture the client IP address on API requests from the X-Forwarded-For header. When configured for the environment, the specified client IP address is used to apply security actions, populate the `ax_resolved_client_ip` Analytics variable and the new `client.resolved.ip` flow variable. The new configuration option can be used to specify the request IP address used in Advanced API Security.

This functionality is not available in Apigee hybrid at this time.

For more information and usage instructions, see the [Client IP resolution customer documentation](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution), [Analytics dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions), and [client flow variable](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#client).

## December 19, 2024

Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to security infrastructure and libraries.**  
  
Announcement

On December 19, 2024, we released an updated version of Apigee (1-14-0-apigee-3) for trial organizations only.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## December 17, 2024

Announcement

On December 17, 2024, we released a new version of Apigee.

Change

With this release, the maximum number of apps per AppGroup is increased from 500 to 30,000.

For more information, see the Apigee [Limits page](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits).

## December 10, 2024

Announcement

On December 10, 2024, we released an updated version of Apigee (1-14-0-apigee-2).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**357880539** | **Resolved issue with missing span in the Apigee UI for distributed trace.**  
**237656263** | **Resolved issue with ServiceCallout policy not working in async mode as expected.**  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## October 23, 2024

Announcement

On October 23, 2024, we released an updated version of Apigee (1-14-0-apigee-1).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**N/A** | Updates to security infrastructure and libraries.  
  
## October 22, 2024

Change

With this release, the following limits for Apigee organizations have changed:

  * The maximum number of deployed API proxies and shared flows per (non-hybrid) organizations is 6000. 
  * The maximum number of proxy deployment units per Apigee instance is 6000.
  * The maximum number of API base paths per Apigee organization is 6000.



For more information, see the Apigee [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits) page.

Announcement

On October 22, 2024, we released a new version of Apigee.

## October 10, 2024

Announcement

On October 10, 2024, we released an updated version of Apigee.

Feature

Apigee no longer limits the number of Cloud projects that can connect to an Apigee instance. Previously, the limit was 50 projects. For each project, you can now create up to 100 Private Service Connect Network Endpoint Groups. The previous limit was 20. For any Apigee instances created before October 10, 2024, you must perform an update to the consumer accept list for an Apigee instance if you want to take advantage of these new limits. See [Updating the consumer accept list for an Apigee instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc#updating-the-consumer-accept-list-for-an-apigee-instance). See also [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#private-service-connect-psc).

## October 08, 2024

Announcement

On October 8, 2024, we released an updated version of Apigee (1-13-0-apigee-6).

This release addresses the security concerns in [GCP-2024-052 from Google Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-052).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**361714906** | **Fixed synchronization issue with Cloud KMS keys** Implemented recovery mechanism for the Apigee dataplane in the event of an extended disruption in the CloudKMS key service.  
**361044374** | **Resolved issue with incorrect payloads shown in debug trace** When using debug trace with the AssignMessage policy, the UI now displays the correct request and response payloads.  
**N/A** | **Updates to security infrastructure and libraries.**  
  
## October 02, 2024

Feature

With this release, all remaining Apigee API Management organizations with Subscription 2021 contracts have been upgraded to introduce standard and extensible API proxy features.

To learn more about:

  * Standard and Extensible API Proxy types, see [API Proxy types](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types).
  * Viewing proxy deployment count, see [View proxy deployment usage](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#view-proxy-deployment-usage).



Change

Subscription Apigee organizations (without hybrid entitlements) upgraded in this release will see changes to the user experience in the [Classic Apigee UI](https://apigee.google.com/edge). To support management of the upgraded functionality now available to these organizations, a number of feature administration pages are now only available in the [Apigee UI in Cloud console](https://docs.cloud.google.com/console/apigee). 

For more information, see [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare).

Announcement

On October 2, 2024, we released an updated version of Apigee.

## September 26, 2024

Announcement

On September 26, 2024 we released an updated version of Apigee.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

If you have CMEK org policy constraints on your Google Cloud project, Apigee will enforce compliance with those constraints and guide you in choosing valid configuration, and prevent you from using Apigee features that are not CMEK-compliant.

The following documents are new and explain how to use CMEK with Apigee:

  * [Using organization policy constraints in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies)
  * [Best practices for Apigee CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-best-practices)



The following documents have been updated with the relevant CMEK information:

  * [Introduction to CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts)
  * [Compare evaluation and paid organizations in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval)
  * [Provisioning an eval org](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/eval-orgs)
  * [Provision a paid org without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo)
  * [About the Apigee encryption keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys)
  * [Compatible services](https://docs.cloud.google.com/kms/docs/compatible-services)
  * [Use Cloud KMS keys in Google Cloud](https://docs.cloud.google.com/kms/docs/use-keys-google-cloud#supported-services)



Issue

A [known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#354716994) was added: Apigee does not support [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

Issue

A [known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#cmek) was added: Apigee does not support key re-encryption, which means even after rotation, the old key version will still be used and you cannot change the CMEK key after org creation.

## September 20, 2024

Announcement

On September 20, 2024, we released an updated version of Apigee (1-13-0-apigee-5).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Change

Bug ID | Description  
---|---  
**366039324** | **Fixed PEM parsing error in JWT/JWS policies** Resolved a PEM parsing error in JWT/JWS policy execution caused by a problematic PEM format.  
**353527851** | **Resolved dropped WebSocket connection** Fixed issue causing a dropped WebSocket connection when using the OAuthV2 policy and the `VerifyJWTAccessToken` operation or VerifyJWT.  
**361166073** | **Fixed issue with JWKS rejection in GenerateJWT policy** Fixed an issue where valid JWKS used to sign encrypted JWTs with the GenerateJWT Policy are incorrectly rejected with `steps.jwt.NoMatchingPublicKey`.  
**352593965** | **Resolved SSL enforcement bug in proxies using the`<SSLInfo>` block** This release fixes an SSL enforcement bug in proxies where an `<SSLInfo>` block specifies both `<IgnoreValidationErrors>` and `<Enforce>` as `true`. The bug results in no enforcement for one specific type of SSL violation - a mismatch between the certificate subject name and the real host name of the target (No Subject Alternative Name, or NSAN). With this fix, `<Enforce>` uniformly overrides `<IgnoreValidationErrors>` in all cases, including NSAN.  
**N/A** | Updates to security infrastructure and libraries.  
  
## September 18, 2024

Announcement

On September 18, 2024 we released an updated version of Apigee

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the feature available until the rollout is complete.

Feature

**Release of Cloud IAM-based authorization and authentication and the VerifyIAM policy.**

This release introduces Cloud IAM-based authorization and authentication for Apigee API access. With this IAM-based solution, access to invoke an API requires the API consumer to have a specific Google Cloud IAM role or permissions.

For information, see [IAM-based API authentication overview](https://docs.cloud.google.com/apigee/docs/api-platform/security/iam/iam-overview) and [VerifyIAM policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-iam-policy).

## September 12, 2024

Announcement

On September 12, 2024, we released an updated version of Apigee.

Feature

With this release, Apigee supports [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

Workforce Identity Federation lets you use an external identity provider (IdP) to authenticate and authorize a workforce — a group of users, such as employees, partners, and contractors — using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to access Apigee services.

See [Access Apigee using Workforce Identity Federation](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/workforce-identity-federation-apigee) for more information.

Fixed

Bug ID | Description  
---|---  
338285095 | Fixed a problem where apps associated with an AppGroup did not appear in the Apps list in the Apigee UI in Cloud Console. As a result, users could not access the app's App Detail page in the console. Using search in the console with a partial app name or API key search for the app was not available.  
  
With this fix, users can now view apps associated with an AppGroup in the Apps list, and view details for each app or delete the app. Users will still not be able to create or edit AppGroup apps.  
  
Apigee hybrid organizations were not impacted by this problem, as they use the Classic UI to view the app details.  
  
Issue

**PEM parsing error in JWT/JWS policies due to non-standard format**

For Apigee and Apigee hybrid versions 1.13 and higher, any deviations in the required PEM format of keys used in [Apigee JWS or JWT policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/jwt-policies-overview) may result in a parsing error.

For more information, see [Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues).

## August 30, 2024

Change

On August 30, 2024, we released an updated version of Apigee (1-13-0-apigee-4).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Change

Bug ID | Description  
---|---  
**N/A** | Updates to security infrastructure and libraries.  
  
## August 27, 2024

Announcement

**Clarification:** On July 26 we announced monetization support with data residency. Please note that monetization support with data residency is for non-hybrid organizations only at this time.

For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

## August 26, 2024

Announcement

On, August 26, 2024, Apigee announced the GA launch of its non-VPC provisioning option.

Feature

With the non-VPC peering provisioning approach, you are not required to provide networks and IP ranges during the Apigee provisioning process. Instead, you use Private Service Connect (PSC) for routing northbound traffic to Apigee and southbound traffic to target services running in your Google Cloud projects. Non-VPC peering is supported for command-line (CLI) steps only. You can perform non-VPC provisioning for [subscription](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered), [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo), and [evaluation](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval) installations of Apigee.

**Note:** The use of VPC Service Controls and Private DNS Peering is not supported. For a complete list of features and networking approaches that are and are not supported for non-VPC peering, see [How to choose a networking option](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options#how-to-choose-a-networking-option).

To learn more, see [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

## August 19, 2024

Issue

**Timeouts when deploying API proxies and shared flows**

The following endpoints may experience timeouts when used with a high volume of queries per second (QPS): 

  * [organizations.environments.apis.revisions.  
deployments.deploy](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy)
  * [organizations.environments.apis.revisions.  
deployments.undeploy](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/undeploy)
  * [organizations.environments.sharedflows.revisions.  
deployments.deploy](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/deploy)
  * [organizations.environments.sharedflows.revisions.  
deployments.undeploy](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/undeploy)



To reduce the likelihood of timeouts, we recommend a target of three QPS when using these endpoints.

To track the status of this issue, see [Apigee Known Issues](https://docs.cloud.google.com/apigee/docs/release/known-issues).

## August 16, 2024

Announcement

On August 16, 2024, we released an updated version of Apigee (1-13-0-apigee-3).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**324418891** | Added improvements to the MessageLogging policy to avoid potential downtime and deployment failures.  
**351068926** | Updated the error format, fault status, and status code returned (from `500` to `404`) in cases where an invalid authorization code causes an error.  
  
## August 15, 2024

Announcement

On August 15, 2024 documentation was added describing how to provision Apigee in the Google Cloud console. 

See [Get started in the Google Cloud console](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/wizard-select-project) for more information.

Feature

Apigee provisioning for Subscription orgs is now performed in the [Google Cloud console](https://console.cloud.google.com/apigee/welcome).

## August 12, 2024

Feature

We changed the maximum number of **Apps per developer** from 10 to 100. See the [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#keys,-developers,-apps) page for more detail.

Note that using more than 10 apps per developer will result in latency when accessing flow variables referencing `developer.apps`.

Announcement

On August 12, 2024, we released a new version of Apigee.

Feature

With this release, Apigee expanded its support for data residency to additional regions in Japan: 

  * `asia-northeast1` (Tokyo)
  * `asia-northeast2` (Osaka)



Data residency for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee data is stored.

For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

## August 08, 2024

Announcement

On August 8, 2024, we announced an increase in the recommended number of API basepaths per Apigee environment or environment group.

The recommended limit of API proxy basepaths per Apigee environment or environment group increased from 1,000 to 3,000. For more information, see the [Environment and organization section of the Limits page](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#environment-and-organization).

Fixed

Bug ID | Description  
---|---  
**329304975** , **301845257** | **Limit on number of basepaths per environment** Fixed issue with the number of total basepaths per environment causing potential failures when deploying API proxy revisions.  
  
## August 07, 2024

Announcement

On August 7, 2024, we published new documentation explaining how to integrate Apigee with a Security Information and Event Management (SIEM) solution. See [Integrate Apigee with your SIEM solution](https://docs.cloud.google.com/apigee/docs/api-platform/security/siem-integration) for more information.

## August 01, 2024

Announcement

On August 1, 2024, we released an updated version of Apigee (1-13-0-apigee-1).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

New [flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference) are now available:

  * `request.headers.names.string `
  * `request.queryparams.names.string `
  * `request.formparams.names.string `
  * `message.headers.names.string `
  * `message.queryparams.names.string `
  * `message.formparams.names.string `
  * `response.headers.names.string `



These context variables can be used to return header, query parameter, and form parameter names in `string` format that can be used in API proxy logic. Each variable returns a comma-separated list of names.

For more information, see the [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference).

Security

Bug ID | Description  
---|---  
**308583363, 332464869** | Security fix for `apigee-mart`. This addresses the following vulnerabilities:

  * [CVE-2023-36478](https://nvd.nist.gov/vuln/detail/CVE-2023-36478)
  * [CVE-2023-36479](https://nvd.nist.gov/vuln/detail/CVE-2023-36479)
  * [CVE-2023-34462](https://nvd.nist.gov/vuln/detail/CVE-2023-34462)
  * [CVE-2023-40167](https://nvd.nist.gov/vuln/detail/CVE-2023-40167)
  * [CVE-2023-26048](https://nvd.nist.gov/vuln/detail/CVE-2023-26048)
  * [CVE-2023-26049](https://nvd.nist.gov/vuln/detail/CVE-2023-26049)
  * [CVE-2023-51775](https://nvd.nist.gov/vuln/detail/CVE-2023-51775)
  * [CVE-2024-28752](https://nvd.nist.gov/vuln/detail/CVE-2024-28752)
  * [CVE-2024-25710](https://nvd.nist.gov/vuln/detail/CVE-2024-25710)
  * [CVE-2024-26308](https://nvd.nist.gov/vuln/detail/CVE-2024-26308)

  
**332465218** | Security fix for `apigee-runtime`.This addresses the following vulnerabilities:

  * [CVE-2023-52428](https://nvd.nist.gov/vuln/detail/CVE-2023-52428)
  * [CVE-2023-44483](https://nvd.nist.gov/vuln/detail/CVE-2023-44483)

  
**341994213, 333971421** | Security fixes for `Cassandra emulator`.These address the following vulnerabilities:

  * [CVE-2017-5929](https://nvd.nist.gov/vuln/detail/CVE-2017-5929)
  * [CVE-2017-18640](https://nvd.nist.gov/vuln/detail/CVE-2017-18640)
  * [CVE-2023-36478](https://nvd.nist.gov/vuln/detail/CVE-2023-36478)
  * [CVE-2019-16869](https://nvd.nist.gov/vuln/detail/CVE-2019-16869)
  * [CVE-2024-22201](https://nvd.nist.gov/vuln/detail/CVE-2024-22201)
  * [CVE-2015-0886](https://nvd.nist.gov/vuln/detail/CVE-2015-0886)
  * [CVE-2024-28752](https://nvd.nist.gov/vuln/detail/CVE-2024-28752)
  * [CVE-2024-29025](https://nvd.nist.gov/vuln/detail/CVE-2024-29025)
  * [CVE-2021-42550](https://nvd.nist.gov/vuln/detail/CVE-2021-42550)
  * [CVE-2023-52428](https://nvd.nist.gov/vuln/detail/CVE-2023-52428)
  * [CVE-2018-10237](https://nvd.nist.gov/vuln/detail/CVE-2018-10237)
  * [CVE-2023-40167](https://nvd.nist.gov/vuln/detail/CVE-2023-41067)
  * [CVE-2021-29425](https://nvd.nist.gov/vuln/detail/CVE-2021-29425)
  * [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487)
  * [CVE-2023-26048](https://nvd.nist.gov/vuln/detail/CVE-2023-26048)
  * [CVE-2023-44483](https://nvd.nist.gov/vuln/detail/CVE-2023-44483)
  * [CVE-2023-26049](https://nvd.nist.gov/vuln/detail/CVE-2023-26049)

  
**329762216** | Security fix for `apigee-installer`.This addresses the following vulnerability: [CVE-2024-24786](https://nvd.nist.gov/vuln/detail/CVE-2024-24786)  
**342630443, 342714341, 343202829** | Security fixes to address the following vulnerabilities:

  * [CVE-2024-29857 ](https://nvd.nist.gov/vuln/detail/CVE-2024-29857)
  * [CVE-2024-30172 ](https://nvd.nist.gov/vuln/detail/CVE-2024-30172)
  * [CVE-2024-30171](https://nvd.nist.gov/vuln/detail/CVE-2024-30171)
  * [CVE-2024-34447](https://nvd.nist.gov/vuln/detail/CVE-2024-34447)
  * [CVE-2023-5072](https://nvd.nist.gov/vuln/detail/CVE-2023-5072)
  * [CVE-2022-4568](https://nvd.nist.gov/vuln/detail/CVE-2022-4568)
  * [CVE-2023-6378](https://nvd.nist.gov/vuln/detail/CVE-2023-6378)
  * [CVE-2021-42550](https://nvd.nist.gov/vuln/detail/CVE-2021-42550)

  
  
Fixed

Bug ID | Description  
---|---  
**293150694** | **`<HTTPMonitor>` now supports the `<UseTargetServerSSLInfo>` element and can trust TLS certs from non-public CAs**.  
**329874359** | **Decreased the default value of`<CacheLookupTimeoutInSeconds>` from 30 seconds to 12 seconds.**  
**334442202** | **Added specific and informative error messaging for App query failures resulting from discrepancies between developers and apps.**  
**333919279** | **Improved reliability for Developer, App and API products APIs.**  
**339169651** | **Fixed potential`HTTP` request smuggling vulnerability when using the `OPTIONS` method.**  
**297539870** | **`<HTTPTargetConnection>` property `io.timeout.millis` is honored when used with WebSockets.**  
**N/A** | **Updated infrastructure and libraries.**  
  
## July 30, 2024

Feature

With this release, Apigee expanded its support for data residency to an additional region in Europe: `europe-west6` (Zurich).

Data residency for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee data is stored.

For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

For a list of supported geographic locations, see [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

Announcement

On July 30, 2024, we released an updated version of Apigee.

## July 25, 2024

Announcement

On July 25, 2024, we released an updated version of Apigee.

Feature

This release includes an update to Advanced API Operations Anomaly Detection functionality: the Anomaly Detection functionality is now available in the Apigee UI in Cloud Console and is renamed to "Operations Anomalies."

For information, see the [Operations Anomalies overview](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/operations-anomalies-overview) for information on the functionality in Apigee UI in Cloud Console.

Feature

Operations Anomalies supports data residency. Data residency meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Operations Anomalies data is stored. For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

## July 11, 2024

Announcement

On July 11, 2024, we released an updated version of Apigee (1-12-0-apigee-8).

This release addresses the security concerns in [GCP-2024-032 from Google Anthos Service Mesh](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2024-032).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**330175485** | **Security fix for apigee-ingress.**  
This addresses the following vulnerabilities: 

  * [CVE-2024-23326](https://nvd.nist.gov/vuln/detail/CVE-2024-23326)
  * [CVE-2024-32974](https://nvd.nist.gov/vuln/detail/CVE-2024-32974)
  * [CVE-2024-32975](https://nvd.nist.gov/vuln/detail/CVE-2024-32975)
  * [CVE-2024-32976](https://nvd.nist.gov/vuln/detail/CVE-2024-32976)
  * [CVE-2024-34362](https://nvd.nist.gov/vuln/detail/CVE-2024-34362)
  * [CVE-2024-34363](https://nvd.nist.gov/vuln/detail/CVE-2024-34363)
  * [CVE-2024-34364](https://nvd.nist.gov/vuln/detail/CVE-2024-34364)

  
  
Fixed

Bug ID | Description  
---|---  
**N/A** | **Updated libraries and infrastructure.**  
  
## July 09, 2024

Issue

**Updated: Limit on number of basepaths per environment**

Apigee is raising the temporary limit of 1000 basepaths per environment to avoid potential failures when deploying API proxy revisions. 

While this limit is in place, you can deploy up to 1000 API proxy revisions (each containing a single basepath) per environment. If your API proxies or revisions contain more than one basepath, the total number of basepaths per environment must not exceed 1000.

To track the status of this issue, see [Apigee Known Issues](https://docs.cloud.google.com/apigee/docs/release/known-issues).

## July 02, 2024

Announcement

On July 2, 2024, we published a security bulletin for Apigee.

Security

A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE or VM nodes.

**Security bulletin published:[GCP-2024-040](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2024-040)**

## June 27, 2024

Announcement

On June 27, 2024, we released an updated version of Apigee.

Feature

Apigee is now available in new regions:

  * Europe - Berlin (`europe-west10`)
  * Africa - Johannesburg (`africa-south1`)



See [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations) for more information about available regions.

## June 26, 2024

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries.**  
  
Announcement

On June 26, 2024, we released an updated version of Apigee (1-12-0-apigee-7).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

These issues were fixed in 1-12-0-apigee-4-hotfix and are included in this release:

Bug ID | Description  
---|---  
**337876238, 330314128, 333762214** | **Resolved issues resulting in an increase in`404/503` responses.**Upgraded storage for the Apigee router to the latest version to resolve `404` responses.Adjusted traffic weight and delays in the older replica set to handle traffic divergence during the release process to address any `5xx` responses.  
**335832119** | **Fixed 404 errors caused during Apigee instance update/rollback.**  
**255772956** | **Turned off asynchronous services callout when the`<Response>` element is not present due to inconsistent scaling of runtime pods.**  
**338717278** | **Reverted problematic commit to address thread pool exhaustion.**  
  
## June 20, 2024

Announcement

On June 20, 2024, we released an updated version of Apigee.

Change

This release includes a change in the user experience of selecting a physical location for control plane hosting when provisioning a Subscription or Pay-as-you-go Apigee organization with data regionalization enabled.

The new provisioning experience provides the opportunity to select a control plane hosting jurisdiction that refers to a location within a geopolitical boundary that may span more than one region. For more information, see [Select an Apigee API control plane hosting jurisdiction](https://docs.cloud.google.com/apigee/docs/locations#select-an-apigee-api-control-plane-hosting-jurisdiction).

## June 17, 2024

Announcement

On June 17, 2024, we released an updated version of Apigee.

Feature

**Update Pay-as-you-go environment types using the Apigee UI in the Google Cloud console**

Apigee Pay-as-you-go customers can modify the type of an existing environment using the Apigee UI in the Cloud console. This feature allows you to add or remove feature capabilities for your environments from the UI.

For more information, see [Update your environment type](https://docs.cloud.google.com/apigee/docs/api-platform/reference/update-environment-types#update-your-environment-type). To learn more about environment types, see [Apigee Pay-as-you-go environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/update-environment-types#update-your-environment-type).

## June 12, 2024

Announcement

On June 12, 2024, we released an updated version of Apigee

Feature

**Feature:[Preview](https://cloud.google.com/products/#product-launch-stages) release of Google Cloud-based mock servers for API Management features in Gemini Code Assist.**

This release introduces the ability to easily deploy a Google Cloud-based remote mock server for Gemini Code Assist API management, which allows interaction with the designed API by anyone with access to the mock server, helping with testing and validating the APIs.

For more information and usage instructions, see [Use Gemini Code Assist](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/gemini-code-assist).

## May 29, 2024

Announcement

On May 29, 2024 we released an updated version of Apigee

Feature

**[Preview](https://cloud.google.com/products/#product-launch-stages) release of API Management features in Gemini Code Assist: generative AI API spec creation with enterprise context and Apigee policy code explanation. This release also includes the preview release of enhanced API hub interaction in Cloud Code.**

This release introduces features for Gemini Code Assist API management:

  * Use Gemini Code Assist to facilitate API design including OpenAPI spec generation with enterprise context from natural language prompts and built in visual API designer to further refine the specification.
  * Code explain for Apigee policies: When adding or editing a proxy policy, highlight part of the policy XML code, such as an element or attribute, to see Gemini Assist-generated information and guidance about the selection.



For more information and usage instructions, see [Use Gemini Code Assist](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/gemini-code-assist).

This release also includes updates to API hub interaction from Cloud Code: An update to the Cloud Code extension enables you to interact with any API in your API hub using a mock server in Cloud Code, make changes to the API, and publish it back to API hub. For information and usage instructions, see [Edit APIs](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/develop-design-edit-apis#edit-apis).

## May 17, 2024

Announcement

On May 17, 2024, we released an updated version of Apigee (1-12-0-apigee-4-hotfix, 1-12-0-apigee-5).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**337876238, 330314128, 333762214** | **Resolved issues resulting in an increase in`404/503` responses.**Upgraded storage for the Apigee router to the latest version to resolve `404` responses.Adjusted traffic weight and delays in the older replica set to handle traffic divergence during the release process to address any `5xx` responses.  
**335832119** | **Fixed 404 errors caused during Apigee instance update/rollback.**  
**255772956** | **Turned off asynchronous services callout when the`<Response>` element is not present due to inconsistent scaling of runtime pods.**  
**338717278** | **Reverted problematic commit to address thread pool exhaustion.**  
  
Change

Navigation menus in the [Classic Apigee UI](https://apigee.google.com/edge) have been restored to support the transition from the Classic console to [Apigee in the Google Cloud console](https://docs.cloud.google.com/console/apigee).

Each menu item in the Classic console now directs you to the corresponding feature location in the Cloud console where you can carry out your task. Please see [Apigee UI in Cloud console navigation](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare) for more details.

Change

**Correction** : Apigee hybrid entitlements are available in Apigee Subscription 2024 plans. For more information, see [Apigee Subscription 2024 entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements#subscription-2024-entitlements).

## May 09, 2024

Issue

**Limit on number of basepaths per environment**

Apigee is enforcing a temporary limit of 500 basepaths per environment to avoid potential failures when deploying API proxy revisions.

While this limit is in place, you can deploy up to 500 API proxy revisions (each containing a single basepath) per environment. If your API proxies or revisions contain more than one basepath, the total number of basepaths per environment must not exceed 500.

To track the status of this issue, see [Apigee Known Issues](https://docs.cloud.google.com/apigee/docs/release/known-issues).

## May 08, 2024

Announcement

On May 8, 2024, we released an updated version of Apigee X.

Feature

This release contains the [General Availability (GA)](https://cloud.google.com/products/#product-launch-stages) release of AppGroups for Apigee and Apigee hybrid (version 1.10.0 and later).

AppGroups represent a relationship between one or more apps that are managed by the same set of people. For information, see [Using AppGroups to organize app ownership](https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership#using-appgroups-to-organize-app-ownership). Client support for AppGroups is available with the latest Drupal Teams module.

## May 07, 2024

Feature

**Environment-level flag for SSL enforcement**

Apigee customers can specify strict SSL southbound enforcement across an Apigee environment, using the `SSLInfo.Enforce` flag.

If `SSLInfo.Enforce` is set to `true` or `false`, the value specified overrides any granular enforcement options specified in `<SSLInfo>` blocks in TargetEndpoint or TargetServer configurations.

If `SSLInfo.Enforce` is unset, SSL enforcement is determined by any values specified using the `<Enforce>` element within individual `<SSLInfo>` blocks. For more information, see [TLS/SSL TargetEndpoint configuration](https://cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#tlsssltargetendpointconfiguration).

Feature

**Two-way HTTPS health monitor support**

Apigee health monitors using `<HTTPMonitor>` can now use all SSL parameters available in the `<SSLInfo>` block of their TargetServer configurations when performing health checks.

To enable access, set `<UseTargetServerSSLInfo>` to `true` in the `<Request>` block of the HTTPMonitor configuration.

For more information, see [Health monitor using HTTP monitor ](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers#healthmonitoring-httpmonitor).

Feature

**Target server SSL enforcement**

With this release, Apigee customers can specify strict SSL southbound enforcement in TargetServer configurations using the object's `enforce` key. If set to `true`, SSL enforcement is applied to service callouts.

The option to specify this behavior is analogous to usage of the `<Enforce>` tag in the `<SSLInfo>` block of the TargetEndpoint configuration.

For more information, see [Configure strict SSL enforcement ](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers#configure-strict-ssl-enforcement).

Announcement

On May 7, 2024, we released an updated version of Apigee.

## April 26, 2024

Feature

**Logging Apigee access logs**

Apigee Subscription and Pay-as-you-go customers can now enable Cloud Logging ingress access logs for each Apigee instance in their organization. Once enabled, this feature allows you to view the logs generated by ingress gateways in your Apigee infrastructure, such as an external Application Load Balancer or an Anthos gateway, to assist in troubleshooting Apigee API calls.

For more information, see [Logging Apigee access logs](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/cloud-logging-ingress-access).

Announcement

On April 26, 2024, we released an updated version of Apigee.

## April 19, 2024

Announcement

On April 19, 2024, we released an updated version of Apigee.

Feature

With this release, Apigee API Management organizations with Subscription 2021 contracts have been upgraded to introduce standard and extensible API proxy features and expanded limits on deployments.

With this upgrade:

  * Standard and extensible API proxy calls are counted equally when calculating overall API call entitlement for Subscription 2021 contracts.
  * The maximum number of shared flow deployments is 75 per environment.
  * There are no limits on the total number of API proxy deployments per environment for Apigee organizations, only limits at the organization level. Limitations on API proxy deployments per environment for hybrid organizations still apply.
  * The maximum limit of total deployment units (API proxies or shared flows) per organization is 4250.



**Note** : The fleetwide upgrade is complete for the majority of Subscription 2021 contract organizations. Organization administrators for the remaining 5% of organizations have been contacted by Apigee representatives regarding timelines for the release.

To learn more about:

  * Standard and Extensible API Proxy types, see [API Proxy types](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types).
  * Expanded limits for API proxy and shared flow deployments, see [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#api-proxies).
  * Account level deployment limits, see [Subscription 2021 entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements#apigee-entitlements).
  * Viewing proxy deployment count, see [View proxy deployment usage](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#view-proxy-deployment-usage).



Change

Subscription Apigee organizations (without hybrid entitlements) upgraded in this release will see changes to the user experience in the [Classic Apigee UI](https://apigee.google.com/edge). To support management of the upgraded functionality now available to these organizations, a number of feature administration pages are now only available in the [Apigee UI in Cloud console](https://docs.cloud.google.com/console/apigee).

For more information, see [Apigee UI in Cloud console navigation](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview#console-compare).

## April 15, 2024

Fixed

Bug ID | Description  
---|---  
**332981542** | **Optimized VerifyAPI policy execution time for high count of API products.**  
  
Announcement

On April 15, 2024, we released an updated version of Apigee (1-12-0-apigee-4).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## April 03, 2024

Feature

With this release, Apigee expanded its support for data residency to additional regions in Asia-Pacific and the Middle East. Data residency for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee data is stored.

For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

For a list of supported geographic locations, see [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

Announcement

On April 3, 2024, we released an updated version of Apigee.

## April 02, 2024

Announcement

On April 2, 2024, we announced an increase in the rate limits for the [Spike Arrest](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy) policy.

The limit on the rate you can specify increased from 1,000 requests per second, 60,000 requests per minute to 4,000 requests per second, 240,000 requests per minute.

See the [Spike Arrest section of the Limits page](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#spikearrest) for information on Spike Arrest limits.

## April 01, 2024

Announcement

On April 1, 2024, we released an updated version of Apigee.

Feature

With this release, Apigee expanded its support for data residency to additional regions in Canada. Data residency for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee data is stored.

For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

For a list of supported geographic locations, see [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

## March 29, 2024

Announcement

On March 29, 2024, we released an updated version of Apigee (1-12-0-apigee-2).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

With this release, Apigee expanded its support for data residency to additional regions in the European Union. Data residency for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee data is stored. 

For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

For a list of supported geographic locations, see [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

Feature

**New Apigee API Monitoring Metrics**

An new suite of metrics for monitoring Apigee proxies and target endpoints is now available. With improved scalability and accuracy, the new suite can support large workloads and withstand underlying infrastructure changes. 

Apigee's [API Monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring) tables and dashboards have been updated to include the following new metrics, which can be used to [configure alerts](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications#metrics-and-filters) and [create custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#create-custom-dashboard):
    
    
    proxy/request_count
    proxy/response_count
    proxy/latencies
    target/request_count
    target/response_count
    target/latencies
    

Fixed

Bug ID | Description  
---|---  
**322843888** | **Fixed issue with incorrect proxy routing when using base paths in proxy chaining.**  
**293933387** | **KVM`list` operation now permits entries with `null` or empty values.**  
**239523766** | **Removed`Unable to evaluate jsonVariable, returning null` error string from ExtractVariable Policy logging.**  
**285592278** | **Fixed issue with deduction of recurring fees from prepaid balances.**  
**237656263** | **Resolved issue with async mode in the ServiceCallout policy when the`<Response>` element is removed.**This note is incorrect; this fix is not included in this release.  
**321744310** | **Added support for caching JSON results retrieved from the ExtractVariables policy.**  
**295341973** | **Resolved issue causing delay in updating southbound SSL certificates in truststore and keystore references.**  
  
## March 26, 2024

Feature

**New Apigee API Monitoring Metrics**

An new suite of metrics for monitoring Apigee proxies and target endpoints is now available. With improved scalability and accuracy, the new suite can support large workloads and withstand underlying infrastructure changes. 

Apigee's [API Monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring) tables and dashboards have been updated to include the following new metrics, which can be used to [configure alerts](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications#metrics-and-filters) and [create custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#create-custom-dashboard):
    
    
    proxy/request_count
    proxy/response_count
    proxy/latencies
    target/request_count
    target/response_count
    target/latencies
    

Announcement

On March 26, 2024, we released an updated version of Apigee (1-12-0-apigee-1).

**Note:** This release was rolled back to address an issue. See entry for [March 29, 2024](https://docs.cloud.google.com/apigee/docs/release-notes#March_29_2024) for the updated version number and payload.

Fixed

Bug ID | Description  
---|---  
**322843888** | **Fixed issue with incorrect proxy routing when using base paths in proxy chaining.**  
**293933387** | **KVM`list` operation now permits entries with `null` or empty values.**  
**239523766** | **Removed`Unable to evaluate jsonVariable, returning null` error string from ExtractVariable Policy logging.**  
**285592278** | **Fixed issue with deduction of recurring fees from prepaid balances.**  
**237656263** | **Resolved issue with async mode in the ServiceCallout policy when the`<Response>` element is removed.**This note is incorrect; this fix is not included in this release.  
**321744310** | **Added support for caching JSON results retrieved from the ExtractVariables policy.**  
**295341973** | **Resolved issue causing delay in updating southbound SSL certificates in truststore and keystore references.**  
  
## March 13, 2024

Announcement

As of March 13, 2024, the conversion of Apigee API Management organizations with Pay-as-you-go pricing provisioned **before** October 1, 2023, to [Pay-as-you-go organizations that use updated attributes](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) for pricing is complete, with the exception of one organization that requires customer action.

The [Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on) is enabled in converted organizations.The Analytics add-on can be [disabled](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on#disable-the-apigee-api-analytics-add-on) if it is not required. In addition, you can [update your Pay-as-you-go environment types using the API](https://docs.cloud.google.com/apigee/docs/api-platform/reference/update-environment-types#update-your-environment-type-using-the-api).

For more information on the updated pricing and enhanced features now available for these organizations, see [Pay-as-you-go (updated attributes) overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview).

Updated pricing attributes will be reflected in March invoices. For billing questions related to this change, contact [Google Cloud Billing support](https://docs.cloud.google.com/support/billing).

## February 12, 2024

Announcement

On February 12, 2024, we released an updated version of Apigee (1-11-0-apigee-17).

This release addresses the security concerns in [GCP-2024-007 from Google Anthos Service Mesh](https://docs.cloud.google.com/support/bulletins#gcp-2024-007).

**Note:** Rollouts of this release to production instances began on February 12 and may take four or more business days to complete across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**322389251** | **Security fix for apigee-ingress.**  
This addresses the following vulnerabilities: 

  * [CVE-2024-23327](https://nvd.nist.gov/vuln/detail/CVE-2024-23327)
  * [CVE-2024-23325](https://nvd.nist.gov/vuln/detail/CVE-2024-23325)
  * [CVE-2024-23324](https://nvd.nist.gov/vuln/detail/CVE-2024-23324)
  * [CVE-2024-23323](https://nvd.nist.gov/vuln/detail/CVE-2024-23323)
  * [CVE-2024-23322](https://nvd.nist.gov/vuln/detail/CVE-2024-23322)

  
  
Fixed

Bug ID | Description  
---|---  
**230082910** | **Fixed issue causing`null` values for `system.timestamp` and `system.time.millisecond` proxy variables.**  
  
This note is incorrect; this fix is not included in this release.

| **285592278** | **Fixed issue with deduction of recurring fees from prepaid balances.**

This note is incorrect; see entry for [March 26, 2024](https://docs.cloud.google.com/apigee/docs/release/release-notes#March_26_2024).

## February 08, 2024

Announcement

On February 8, 2024 we released an updated version of the Apigee APIs.

Feature

**API support for update operations on KeyValueMap entries**

Starting with this release, the Apigee APIs support update operations for KeyValueMap entries. See the API reference page for [REST Resource: organizations.environments.keyvaluemaps.entries](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.keyvaluemaps.entries) for information.

## February 02, 2024

Announcement

On February 2, 2024, we released an updated version of Apigee.

**Note:** Rollouts of this release to production instances began on February 2 and may take up to four business days before it is available across all regions.

Feature

We modified or added these limits: 

  * Changed the maximum API proxy endpoints per API proxy from 5 to 10
  * Specified the maximum API base paths per organization as 21,250



See the [Limits page](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits) for details.

## February 01, 2024

Announcement

On February 1, 2024, we released an updated version of Apigee.

**Note:** Rollouts of this release to production instances will begin on February 1 and will be complete for all organizations by the end of February.

With this release, Apigee API Management organizations with Pay-as-you-go pricing provisioned **before** October 1, 2023, will be converted to [Pay-as-you-go organizations that use updated attributes](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) for pricing.

Prior to the conversion, these organizations were billed for API runtimes based on [Apigee gateway node usage](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go#how-does-apigee-pay-as-you-go-pricing-work) and the total number of API requests processed by [Apigee analytics](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go#how-does-apigee-pay-as-you-go-pricing-work). 

Once converted, these organizations will be billed for the following:

  * Volume of API calls processed by a given proxy type
  * Usage of deployment environments (per hour per region)
  * Usage of additional deployment units (API proxies or shared flows) 
  * Any additional add-on capabilities (Advanced API security, Monetization, Analytics)



The conversion process is expected to last about 5 minutes and traffic will continue to be processed normally during this time. If proxy revision deployments are interrupted during this time frame, revisions can be deployed after conversion completes.

The [Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on) will be enabled by default in converted organizations.The Analytics add-on can be [disabled](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on#disable-the-apigee-api-analytics-add-on) after the pricing change if it is not required. 

For more information on the updated pricing and enhanced features now available for these organizations, see [Pay-as-you-go (updated attributes) overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview).

Updated pricing attributes will be reflected in March invoices. For billing questions related to this change, contact [Google Cloud Billing support](https://docs.cloud.google.com/support/billing).

## January 22, 2024

Fixed

Bug ID | Description  
---|---  
**316093865** | **Fixed issue where empty`LoadBalancer` configuration in the Target Endpoint results in a failed proxy deployment with `NullPointerException`.**  
**312966965** | **Resolved proxy chaining issue resulting in incorrect post-target service callout hostnames.**  
**318909276** | **Fixed issue withLookupCache policy failures under certain circumstances.**  
**262071551** | **Resolved issue with the use of combinators such as`allOf` in the OASValidation Policy.**  
**311049371** | **Resolved issue causing SSL error in proxy chaining and path chaining flows.**  
**308196929** | **Use of`target.header.host` flow variable with gRPC targets is now fixed.**  
  
Announcement

On January 22, 2023, we released an updated version of Apigee (1-11-0-apigee-14).

**Note** : Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## December 15, 2023

Announcement

On December 15, 2023, we released an updated version of Apigee.

Feature

**Update Pay-as-you-go environment types with Apigee APIs.**

Use Apigee APIs to upgrade or downgrade the type of an _existing_ environment to add or remove feature capabilities and manage your Apigee Pay-as-you-go billing and resource usage. For more information, see [Update Pay-as-you-go environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/update-environment-types).

Feature

**Apigee Advanced API Security add-on for Pay-as-you-go organizations is[generally available (GA)](https://cloud.google.com/products/#product-launch-stages).**

With this release, Apigee Advanced API Security is available as a paid add-on capability for Pay-as-you-go organizations. The add-on can be enabled in any Apigee Intermediate or Comprehensive environment from the Apigee UI in Cloud Console or using the Apigee APIs. For more information, see [Manage the Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-security-add-on).

## December 13, 2023

Announcement

On December 13, 2023, we released an updated version of Apigee.

**Note** : Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

Apigee now supports data residency. Data residency for Apigee meets compliance and regulatory requirements by allowing you to specify the geographic locations (regions) where Apigee data is stored. See [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts).

Feature

Apigee now supports Forward Proxying. Forward Proxying provides the ability to forward traffic received in a particular environment to a specified URI. See [Forward proxying](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#forward-proxying).

Feature

You can now restrict the creation of Apigee location based resources (Organization, Instances and EndpointAttachments) to specific locations using an Organization Policy Service constraint. This feature is [generally available](https://cloud.google.com/products/#product-launch-stages). To learn more, see [Restricting Resource Locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).

Feature

Apigee now supports CMEK for the control plane. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use customer-managed encryption keys (CMEK). See [Introduction to CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts).

## December 07, 2023

Announcement

On December 7, 2023, we released an updated version of Apigee X.

**Note:** Rollouts of this release to production instances has begun and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features available until the rollout is complete.

Feature

**[General Availability (GA)](https://cloud.google.com/products/#product-launch-stages) of Apigee gRPC passthrough**

Apigee's gRPC proxy passthrough functionality provides the ability to create proxies which receive gRPC client requests and pass them through to a gRPC target server.

For information, see [Creating gRPC API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy#creating-grpc-api-proxies).

## December 01, 2023

Announcement

On December 1, 2023, we released an updated version of Apigee (1-11-0-apigee-8).

**Note** : Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Change

**Dynamic endpoint target metrics aggregated into a single metric.**

With this release, all request, response, and latency [target metrics](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/TargetV2) for dynamically-configured endpoints are aggregated and presented as a single metric per proxy, using the `endpoint` label `Dynamic Target`. This feature does not change monitoring behavior for statically configured endpoints.

Fixed

Bug ID | Description  
---|---  
**294882858** | **Fixed issue with ServiceCallout policy overriding`target_ip` value in proxy.**  
**279037851** | **Improved performance when running debug sessions with masked payload.**  
**312026988** | **Resolved possible usage counting issue for monetization prepaid developers using proxies with multiple proxy endpoints configured.**  
  
## November 10, 2023

Feature

Apigee is now available in a new region: Middle East - Dammam (`me-central2`).

See [Apigee locations](https://docs.cloud.google.com/apigee/docs/locations) for more information about available regions.

Announcement

On November 10, 2023 we released an updated version of Apigee.

Deprecated

As of November 10, 2023, Configurable API Proxies (preview) is no longer available. For more information, see [Configurable API Proxies (preview) deprecation](https://docs.cloud.google.com/apigee/docs/deprecations/configurable-proxies).

## November 03, 2023

Security

On November 3, 2023, we updated the following security bulletin:

Bug ID | Description  
---|---  
304599411 | **Security bulletin updated**   
[GCP-2023-32](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2023-032)   
A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the Apigee Ingress (Anthos Service Mesh) server used by Apigee X. The vulnerability could lead to a DoS of Apigee API management functionality.  
  
Announcement

The shutdown of the Configurable API Proxy (Preview) feature is approaching. On or after November 10, 2023, the preview feature will no longer be available. For more information, see [Configurable API proxies (preview) deprecation](https://docs.cloud.google.com/apigee/docs/deprecations/configurable-proxies).

## October 24, 2023

Feature

With this release, the `HeaderName` element is available as a child element of `Authentication`. This element appears in the [ServiceCallout](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy#authentication) and [ExternalCallout](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/external-callout-policy) policies, and in the [TargetEndpoint proxy configuration](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#authentication-element-usage).

By default, when an `Authentication` configuration is present, Apigee generates and injects a bearer token into the `Authorization` header, in the message sent to the target system. The new `HeaderName` element allows the configuration to specify the name of a different header to hold that bearer token.

Fixed

Bug ID | Description  
---|---  
**294293907** | **Fixed issue with Google authentication for gRPC-based target servers.**  
**292454825** | **Fixed issue causing Null Pointer Exception when creating or updating an API product.**  
**291784631** | **Implemented fix to permit the use of hyphens (-) in flow variables used to define target URLs in`<HTTPTargetConnection>`.**  
**267229604** | **Fixed issue where updates to a TLS truststore reference were not reflected for in-use southbound target server connections.**  
**277353680** | **Fixed issue causing target server`HealthMonitors` to continue beyond revision or deletion of the proxy.**Target health checks are now terminated as soon as the proxy is removed from the runtime (undeployed or deleted). **Note** : There may be a delay between removal of the proxy and termination of the target server health checks.  
**N/A** | **Upgraded infrastructure and libraries.**  
  
Announcement

On October 24, 2023, we released an updated version of Apigee (1-11-0-apigee-7).

**Note** : Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## October 19, 2023

Announcement

On October 19, 2023, we released an updated version of Apigee

Feature

**Looker Studio Integration**

This release includes the public preview of [Looker Studio Integration](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/looker), which connects Apigee data to Google's [Looker Studio](https://docs.cloud.google.com/looker-studio). Looker Studio is a powerful and flexible tool that you can use to display Apigee data in fully customizable dashboards and reports.

## October 13, 2023

Announcement

On October 13, 2023, we released an updated version of Apigee (1-11-0-apigee-6).

Security

Bug ID | Description  
---|---  
304681330 | **Security fix for apigee-ingress.**  
This addresses the following vulnerability:  
[CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)  
305127632 | **Security bulletin published.**  
[GCP-2023-032](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2023-032)  
  
Issue

**Description**

A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol ([CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)), including the Apigee Ingress (Anthos Service Mesh) server used by Apigee X. The vulnerability could lead to a DoS of Apigee API management functionality.

**Affected Products**

Deployments of Apigee X that are accessible through a Google Cloud Network Load Balancer (Layer 4), or a custom layer 4 load balancer, are affected. A hotfix is being applied to all Apigee X instances. Your Apigee X instances will be automatically updated within the next few days.

**Unaffected products**

Apigee X instances which are accessed only via Google Cloud Application Load Balancers (Layer 7) are not affected. This includes deployments that have HTTP/2 enabled for gRPC proxies.

**What Should I Do?**

All Apigee X instances will be automatically updated within the next few days. Customers do not need to take any actions. 

**What Vulnerabilities Are Addressed By These Patches?**

The vulnerability, [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487), allows an attacker to execute a denial-of-service attack on Apigee ingresses.

## September 29, 2023

Feature

**Standard and extensible API proxies are[generally available (GA)](https://cloud.google.com/products/#product-launch-stages).**

Standard and extensible API proxies are generally available for use with Apigee organizations.

For more information about standard and extensible API proxies, see [API proxy types](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types).

Feature

**One click provisioning for Apigee Pay-as-you-go organizations is[generally available (GA)](https://cloud.google.com/products/#product-launch-stages).**

Simplify your onboarding experience with one click provisioning for new Pay-as-you-go organizations, using smart default configurations. To learn more, see [Provision Apigee with one click](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/one-click).

Announcement

**On September 29, 2023, we released an updated version of Apigee.**

**Note:** Rollouts of this release may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**Apigee API Analytics add-on for Pay-as-you-go organizations is[generally available (GA)](https://cloud.google.com/products/#product-launch-stages).**

With this release, Apigee API Analytics is available as a paid add-on capability for Pay-as-you-go organizations. The add-on can be enabled in any Apigee Intermediate or Comprehensive environment. For more information, see [Manage the Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on).

Feature

**New attributes for Pay-as-you-go pricing are[generally available (GA)](https://cloud.google.com/products/#product-launch-stages).**

Apigee updated its Pay-as-you-go pricing model, making it possible for customers to onboard at a significantly reduced initial cost and right-size their ongoing expenses to usage. 

To learn more about the updated Pay-as-you-go pricing experience, see [Pay-as-you-go (updated attributes) pricing overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview).

Feature

**New environment types are[generally available (GA)](https://cloud.google.com/products/#product-launch-stages).**

With this release, Apigee introduces three distinct environments that have access to varying degrees of Apigee capabilities and costs: Base, Intermediate, and Comprehensive. 

For more information, see [Apigee Pay-as-you-go environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types).

Feature

**HTTPModifier and ReadPropertySet policies and templating support for message elements are [generally available (GA)](https://cloud.google.com/products/#product-launch-stages).**

The HTTPModifier policy can change an existing request or response message and provides a subset of the functionality already available in the AssignMessage policy. See [HTTPModifier policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy).

The ReadPropertySet policy reads property sets and populates flow variables with the results. See [ReadPropertySet policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy).

HTTPModifier and ReadPropertySet are [standard policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types). Proxies built exclusively with standard policies are called standard proxies and can be deployed to any environment type. See [Pay-as-you-go (updated attributes) pricing overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview).

With this release, template support for message  elements is also generally available. See [URL templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#URL-templating).

Feature

**Updated pricing attributes in Subscription plans are available.**

To get started with subscription plans that include new pricing attributes (consistent with Pay-as-you-go pricing), contact your [Google Cloud sales specialist](https://docs.cloud.google.com/contact?direct=true&pre_product=apigee). 

For more information, see [Apigee Subscription 2024 entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements#subscription-2024-entitlements). Apigee hybrid is not available in the new subscription plan at this time.

This note is incorrect; see entry for [May 17, 2024](https://docs.cloud.google.com/apigee/docs/release/release-notes#May_17_2024).

## September 19, 2023

Security

Bug ID | Description  
---|---  
**296506425, 295936113, 295925991, 295688738, 296110120, 281112632** | **Security fix for`apigee-runtime`.**   
This addresses the following vulnerabilities: 

  * [CVE-2023-2976](https://nvd.nist.gov/vuln/detail/CVE-2023-2976)
  * [CVE-2023-3635](https://nvd.nist.gov/vuln/detail/CVE-2023-3635)
  * [CVE-2020-8908](https://nvd.nist.gov/vuln/detail/CVE-2020-8908)
  * [CVE-2022-34169](https://nvd.nist.gov/vuln/detail/CVE-2022-34169)
  * [CVE-2023-28867](https://nvd.nist.gov/vuln/detail/CVE-2023-28867)
  * [CVE-2022-37734](https://nvd.nist.gov/vuln/detail/CVE-2022-37734)

  
**287218068** | **Fixed security vulnerability to prevent header injection using flow variables.**  
  
Fixed

Bug ID | Description  
---|---  
**296296456** | **Implemented fix to ensure that`continueOnError` is honored in the SpikeArest policy.**  
**229615887** | **The flow variable`target.scheme` is now set consistently with the target server URL.**  
**78106145** | **Fixed issue in the RegularExpressionProtection policy to ensure that multiple JSONPaths elements in a JSON payload are checked.**  
**294090782** | **Implemented fix to allow the Apigee runtime to connect to a target server using a wildcard CNAME that references a wildcard A record.**  
**285592278** | **Fixed issue with deduction of recurring fees from prepaid balances.** This note is incorrect; see entry for [March 26, 2024](https://cloud.google.com/apigee/docs/release/release-notes#March_26_2024).  
**N/A** | **Upgraded infrastructure and libraries.**  
  
Announcement

On September 19, 2023, we released an updated version of Apigee X (1-11-0-apigee-5).

**Note:** This release replaces Apigee X (1-11-0-apigee-3). Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## August 15, 2023

Security

Bug ID | Description  
---|---  
**281112632, 294892189** | **Security fix for`apigee-runtime`.**   
This addresses the following vulnerability: 

  * [CVE-2023-28867](https://nvd.nist.gov/vuln/detail/CVE-2023-28867)
  * [CVE-2022-37734](https://nvd.nist.gov/vuln/detail/CVE-2022-37734)
  * [CVE-2023-2976](https://nvd.nist.gov/vuln/detail/CVE-2023-2976)

  
**294891556** | **Security fix for`apigee-emulator`, `apigee-mock-server`, and `apigee-runtime`.**   
This addresses the following vulnerability: 

  * [CVE-2021-31684](https://nvd.nist.gov/vuln/detail/CVE-2021-31684)

  
**287207717** | **Fixed sandbox bypass vulnerability.**  
**286993631** | **Fixed message template injection vulnerability.**  
  
Fixed

Bug ID | Description  
---|---  
**155498623** | **`XPaths` in `maskconfigs` now mask values with special characters.**  
**291746838** | **Implemented fix to prevent service callouts from overwriting timeouts on clients used by other policies or target endpoints.**  
**274663992** | **Fixed issue in AccessControl policy to avoid race condition.**  
**294441215** | **Implemented fix to resolve quota count in the Quota policy.**  
**287659763** | **Fixed issue causing incorrect target endpoint URLs to display in debug sessions.**  
**283285631** | **Fixed issue where base environment debug sessions were not recorded for Pay-as-you-go (updated attributes) organizations.**  
**196216798** | **Fixed issue with access to monetization flow variables in the post client flow.**  
**N/A** | **Upgraded infrastructure and libraries.**  
  
Announcement

On August 15, 2023, we released an updated version of Apigee X (1-11-0-apigee-1).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## August 14, 2023

Announcement

On August 14, 2023, we released an updated version of Apigee X.

**Note:** The changes in this release only apply to the [Apigee UI in Cloud console](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview), but not to the classic Apigee UI.**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

This release includes a major redesign of the Advanced API [Security scores](https://docs.cloud.google.com/apigee/docs/api-security/security-scores) page in the Apigee UI in Cloud console. The Security scores page now:

  * Highlights the top recommendations for improving security scores.
  * Links directly to the Apigee UI [Proxy Editor](https://docs.cloud.google.com/apigee/docs/api-platform/develop/ui-edit-proxy) and [Target Server](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/load-balancing-across-backend-servers) tabs , where you can implement recommended changes to your API proxies and target servers.



## August 09, 2023

Announcement

The Apigee documentation site navigation has been updated to be more consistent with other Google Cloud product documentation sites. The changes include:

  * Added a new [**Overview**](https://docs.cloud.google.com/apigee/docs) tab that provides links to Apigee documentation, training and tutorials, use cases, and videos.
  * Moved the **Getting started** tab content to the [**Guides**](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) tab.

**Note:** While the location of some content in the site's table of contents has changed, page URLs are unchanged. Internal links and any bookmarks you may have created remain unchanged.

## August 07, 2023

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries.**  
  
Announcement

On August 7, 2023, we released an updated version of Apigee X (1-10-0-apigee-7).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## August 03, 2023

Announcement

On August 3, 2023, we released an updated version of Apigee X.

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Change

Previously, [Advanced API Security scores](https://docs.cloud.google.com/apigee/docs/api-security/security-scores) didn't evaluate proxies calling shared flows via flow hooks and the [FlowCallout](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy) policy in the proxy. With this release, security scores take into account proxies calling shared flows this way. As a result, your security scores may change because they now factor in the shared flows in the environment.

## July 24, 2023

Announcement

On July 24, 2023, we released an updated version of Apigee X.

**Note:** Rollouts of this release to production instances has begun and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features available until the rollout is complete.

Feature

**Public preview of Apigee gRPC passthrough**

Apigee's new gRPC proxy passthrough functionality provides the ability to create proxies which receive gRPC client requests and pass them through to a gRPC target server.

For information, see [Creating gRPC API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy#creating-grpc-api-proxies).

## July 21, 2023

Announcement

On July 21, 2023, we released an updated version of Apigee X.

Change

The Advanced API Security Abuse detection [Incident details](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#incident-details) page now displays unique IP addresses, even if more than one incident corresponds to the same IP address. Previously, the Incident details page could display the same IP address more than once for different incidents.

Also, the **Attributes** tab of the Incident details page no longer displays the following attributes:

  * **Top App Key**
  * **Detected Rules**
  * **Top URL**



## July 20, 2023

Announcement

On July 20, 2023, we released an updated version of Apigee X (1-10-0-apigee-6).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**290943249** | **Fixed latency issue between Istio and runtime container.**  
**205666368** | **Fixed issue with default validation of TLS target endpoint certificates.** To enable strict SSL on southbound connections to a proxy target endpoint, add the tag `<Enforce>true</Enforce>` in the target `<SSLInfo>` block.For more information about using `<Enforce>true</Enforce>` in `<SSLInfo>`, see [About setting TLS options in a target endpoint or target server](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls#about-setting-tls-options-in-a-target-endpoint-target-server).  
  
Security

Bug ID | Description  
---|---  
**290709899** | **Security fix for`apigee-runtime`.**   
This addresses the following vulnerability: 

  * [CVE-2022-1471](https://nvd.nist.gov/vuln/detail/CVE-2022-1471)

  
**N/A** | **Security fixes for`apigee-redis` and `apigee-connect-agent`.**   
These address the following vulnerabilities: 

  * [CVE-2023-29405](https://nvd.nist.gov/vuln/detail/CVE-2023-29405)
  * [CVE-2023-24540](https://nvd.nist.gov/vuln/detail/CVE-2023-24540)
  * [CVE-2023-29404](https://nvd.nist.gov/vuln/detail/CVE-2023-29404)
  * [CVE-2023-24538](https://nvd.nist.gov/vuln/detail/CVE-2023-24538)
  * [CVE-2023-29402](https://nvd.nist.gov/vuln/detail/CVE-2023-29402)
  * [CVE-2022-41724](https://nvd.nist.gov/vuln/detail/CVE-2022-41724)
  * [CVE-2023-24539](https://nvd.nist.gov/vuln/detail/CVE-2023-24539)
  * [CVE-2022-41723](https://nvd.nist.gov/vuln/detail/CVE-2022-41723)
  * [CVE-2023-24536](https://nvd.nist.gov/vuln/detail/CVE-2023-24536)
  * [CVE-2022-41725](https://nvd.nist.gov/vuln/detail/CVE-2022-41725)
  * [CVE-2023-24534](https://nvd.nist.gov/vuln/detail/CVE-2023-24534)
  * [CVE-2023-29403](https://nvd.nist.gov/vuln/detail/CVE-2023-29403)
  * [CVE-2023-24537](https://nvd.nist.gov/vuln/detail/CVE-2023-24537)
  * [CVE-2023-29400](https://nvd.nist.gov/vuln/detail/CVE-2023-29400)
  * [CVE-2023-24532](https://nvd.nist.gov/vuln/detail/CVE-2023-24532)
  * [CVE-2022-41717](https://nvd.nist.gov/vuln/detail/CVE-2022-41717)

  
**N/A** | **Security fixes for`apigee-connect-agent`.**   
These address the following vulnerabilities: 

  * [CVE-2022-27664](https://nvd.nist.gov/vuln/detail/CVE-2022-27664)
  * [CVE-2022-21698](https://nvd.nist.gov/vuln/detail/CVE-2022-21698)
  * [CVE-2022-32149](https://nvd.nist.gov/vuln/detail/CVE-2022-32149)
  * [CVE-2022-29526](https://nvd.nist.gov/vuln/detail/CVE-2022-29526)

  
  
## July 12, 2023

Announcement

On July 12, 2023, we released an updated version of Apigee X.

Feature

Preview release of non-VPC peering option for Apigee provisioning Apigee now supports a provisioning option that does not require VPC peering. With this approach, you are not required to provide networks and IP ranges during the Apigee provisioning process. Instead, you use Private Service Connect (PSC) for routing northbound traffic to Apigee and southbound traffic to target services running in your Google Cloud projects.

Non-VPC peering is supported for command-line (CLI) provisioning steps only. You can perform non-VPC provisioning for [subscription](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered), [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo), and [evaluation](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-eval) installations of Apigee.

To learn more, see [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

## July 10, 2023

Announcement

On July 10, 2023, we released an updated version of Apigee X (1-10-0-apigee-5).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
273693152 | **Fixed SAMLAssertion policy parsing to limit the number of entities that will be parsed to 10000.** Any attempt to parse more than 10000 entities will generate an error.  
273695718 | **Fixed DataCapture policy to avoid evaluation of external entities during XML parsing for variable collection.**  
273929507 | **Fixed issue with potential Java security bypass in LookupCache policy.** Certain objects which implement `PostDeserializer` interface are now cached.  
273950705 | **Fixed issue in PythonScript policy to prevent execution of arbitrary Java code.** With this fix, the runtime does not allow execution of python code added to a `.js` resource file.  
  
Fixed

Bug ID | Description  
---|---  
289254725 | **Implemented fix to prevent failure of proxy deployments that include the OASValidation policy.**  
N/A | **Upgraded infrastructure and libraries.**  
  
## July 06, 2023

Announcement

On July 6, 2023, we released an updated version of Apigee X.

Feature

**Preview release of Pay-as-you-go pricing with updated attributes**

Apigee is updating its Pay-as-you-go pricing model, making it possible to start using Apigee at a significantly reduced initial cost and right-size ongoing expenses to match precise usage. 

To learn how to get started with the updated Pay-as-you-go pricing experience, see [Pay-as-you-go (updated attributes) pricing overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview).

Feature

**Preview release of new environment types**

Apigee announces the Preview release of three distinct environment types: Base, Intermediate, and Comprehensive. Each environment type offers varying degrees of capabilities and costs; you can tailor pricing to suit your needs.

For more information, see [Apigee Pay-as-you-go environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types).

Feature

**Preview release of new HTTPModifier and ReadPropertySet policies and templating support for message <URL> elements**

Apigee announces the Preview release of the HTTPModifier and ReadPropertySet policies.

The HTTPModifier policy can change an existing request or response message and provides a subset of the functionality already available in the AssignMessage policy. See [HTTPModifier policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/http-modifier-policy).

The ReadPropertySet policy reads property sets and populates flow variables with the results. See [ReadPropertySet policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/read-property-set-policy).

HTTPModifier and ReadPropertySet are [standard policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types). Proxies built exclusively with standard policies are called standard proxies and can be deployed to any environment type. See [Pay-as-you-go (updated attributes) pricing overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview).

This release also includes template support for message <URL> elements. See [URL templating](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#URL-templating).

Feature

**Preview release of standard and extensible API proxies**

Apigee announces the Preview release of standard and extensible API proxies, available for use with preview organizations using Pay-as-you-go (updated attributes) pricing. 

For more information about standard and extensible API proxies, see [API proxy types](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types).

## June 27, 2023

Announcement

On June 27, 2023 we released an updated version of Apigee X.

**Note:** Rollouts of this release to production instances has begun and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**Public preview of AppGroups**

Introduces the concept of AppGroups, which represent a relationship between one or more apps that are managed by the same set of people. For information, see [Using AppGroups to organize app ownership](https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership#using-appgroups-to-organize-app-ownership).

**Note:** For Apigee hybrid, AppGroups and the organizations.apps API "filter" option to filter apps based on developer or AppGroup are available in hybrid 1.10.0 and later. This generic filtering option can also be used to filter apps based on developerEmail, apiProduct, consumerKey, status, appId and appName. PageSize and PageToken can be used to paginate the dataset.   
  
Client support for AppGroups is available with the latest Drupal Teams module.   
  


Note that the purpose of this release is to support upgrades from Apigee Edge customers who used company-apps without monetization; however, it is available to any Apigee X/hybrid customer during the public preview stage.

## June 20, 2023

Announcement

On June 20, 2023, we released an updated version of Apigee X (1-10-0-apigee-4).

**Note:** Rollouts of this release to production instances will begin within two business days and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Security

Bug ID | Description  
---|---  
**273801301** | **Security fix for`apigee-diagnostics-collector`, `apigee-mart-server`, `apigee-runtime`, and `apigee-synchronizer`.**   
This addresses the following vulnerabilities:

  * [CVE-2022-40150](https://nvd.nist.gov/vuln/detail/CVE-2022-40150)
  * [CVE-2022-40149](https://nvd.nist.gov/vuln/detail/CVE-2022-40149)

  
**281561243** | **Security fix for`apigee-diagnostics-collector`, `apigee-mart-server`, `apigee-runtime`, and `apigee-synchronizer`.**   
This addresses the following vulnerabilities:

  * [CVE-2017-18640](https://nvd.nist.gov/vuln/detail/CVE-2017-18640)
  * [CVE-2022-25857](https://nvd.nist.gov/vuln/detail/CVE-2022-25857)
  * [CVE-2022-38751](https://nvd.nist.gov/vuln/detail/CVE-2022-38751)
  * [CVE-2022-38750](https://nvd.nist.gov/vuln/detail/CVE-2022-38750)
  * [CVE-2022-38749](https://nvd.nist.gov/vuln/detail/CVE-2022-38749)
  * [CVE-2022-41854](https://nvd.nist.gov/vuln/detail/CVE-2022-41854)
  * [CVE-2022-38752](https://nvd.nist.gov/vuln/detail/CVE-2022-38752)

  
  
Fixed

Bug ID | Description  
---|---  
284114575 | **Implemented fix to prevent the execution of untrusted code in Apigee policies.**  
279092925 | **Modified Cloud Logging policy to improve runtime performance.**  
186885918 | **Disabled access to external entities in XML parsing.**  
270764083 | **Default expiration for refresh tokens set to 30 days if not explicitly set in the OAuth policy.**  
N/A | **Upgraded infrastructure and libraries.**  
  
## May 17, 2023

Announcement

On May 17, 2023, we released an updated version of Apigee X (1-10-0-apigee-1).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Breaking

**Fixed issue with incomplete removal of form parameters when using the`<Remove>` element in the Assign Message policy to delete headers and form parameters simultaneously.**

This fix may result in a breaking change for any customer employing an antipattern that attempts to access a form parameter _after_ using the `<Remove>` element to delete _the same form parameter_ and headers simultaneously in the policy flow. 

For more information on the recommended steps for setting and removing form parameters and headers using the Assign Message policy, see the updated documentation for the [Assign Message policy examples](https://cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy#samples).

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries.**  
280695936 | **Fixed issue with incomplete removal of form parameters when using the`<Remove>` element in the Assign Message policy to delete headers and form parameters simultaneously.**  
271217050 | **Fixed issue resulting in missing execution records in debug sessions for the JavaCallout policy.**  
271894110, 273568673, 273571029 | **Fix enables support for TLS 1.3 for southbound targets.**  
271539836 | **Fixed intermittent Cloud Logging failures.**  
277090269 | **Fixed encryption of internal proxy chaining headers to avoid proxy invocation misuse.**  
273561434 | **Fixed issue with incomplete debug session information for proxies deployed in the same environment.**  
158132963 | **Improved capture of relevant target flow variables in trace and analytics in the event of target timeouts.**  
271093461 | **Fixed issue with heap exhaustion when using OASValidation policy.**  
269514256 | **Fixed issue causing`GoogleTokenGeneration` failure.**  
261924658 | **Optimization to reduce latency in Quota policy.**  
252864240 | **Fixed issue to support bot detection with Analytics obfuscation enabled.**  
222024484 | **CORS policy now returns`Access-Control-Allow-Credentials` header in preflight response when `<AllowCredentials>` is set to true.**  
261205290 | **Optimization to reduce resource usage on Cassandra connections.**  
266814873 | **Fixed issue with retrieval of environment-scoped KVM entries containing encryption keys with non-UTF-8 characters.**  
260342163 | **Fixed issue causing 100% CPU usage by runtime pod threads under specific circumstances.**  
273800523, 273800717 | **Security fixes for Apigee.** The fixes address the following vulnerabilities:

  * [CVE-2022-41881](https://nvd.nist.gov/vuln/detail/CVE-2022-41881)
  * [CVE-2022-24823](https://nvd.nist.gov/vuln/detail/CVE-2022-24823)
  * [CVE-2021-43797](https://nvd.nist.gov/vuln/detail/CVE-2021-43797)
  * [CVE-2022-46363](https://nvd.nist.gov/vuln/detail/CVE-2022-46363)
  * [CVE-2022-46364](https://nvd.nist.gov/vuln/detail/CVE-2022-46364)
  * [CVE-2023-0286](https://nvd.nist.gov/vuln/detail/CVE-2023-0286)
  * [CVE-2022-4450](https://nvd.nist.gov/vuln/detail/CVE-2022-4450)
  * [CVE-2021-3999](https://nvd.nist.gov/vuln/detail/CVE-2021-3999)
  * [CVE-2023-0215](https://nvd.nist.gov/vuln/detail/CVE-2023-0215)
  * [CVE-2022-2097](https://nvd.nist.gov/vuln/detail/CVE-2022-2097)
  * [CVE-2022-4304](https://nvd.nist.gov/vuln/detail/CVE-2022-4304)

  
  
## April 26, 2023

Announcement

Effective May 31, 2023, the default value for the OAuthv2 policy `RefreshTokenExpiresIn` element has new behavior. Starting May 31, `RefreshTokenExpiresIn` defaults to **2592000000 ms (30 days)** for all policies where this element is not set.

For information on this element, see [RefreshTokenExpiresIn](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#refreshtokenexpiresinelement).

## April 20, 2023

Announcement

On April 20, 2023 we released an updated version of Apigee.

Feature

This release contains a new Advanced API Security [Detected Traffic](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection#detected-traffic) view, which displays information about API traffic originating from detected bots. This information was previously displayed in the **Abuse metrics** section of the **Security scores** view.

## April 17, 2023

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries.**  
  
Announcement

On April 17, 2023, we released an updated version of Apigee X (1-9-0-apigee-25).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## April 13, 2023

Announcement

On April 13, 2023, we released an updated version of Apigee.

Feature

**New features now supported in Apigee in VS Code for local development**

The following features are now supported with Apigee in VS Code for local development as part of the [Insiders build](https://docs.cloud.google.com/code/docs/vscode/insiders#get) (as of v1.22.1-insiders.3):

  * **Create multi-repository workspaces** \- Choose individual storage locations for artifacts, such as API proxies that are stored as individual SCMs, but develop them together using a single workspace. You no longer have to create a single repository that contains all of your API proxies. See [Understanding the structure of an Apigee multi-repository workspace](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-workspace#understanding_the_structure_of_an_apigee_multi-repository_workspace).
  * **Use keystore** \- Introduces a new environment-level setting for creating the required keystores in the Apigee Emulator by using locally available keys. See [Configuring the keystrokes (keystores.json)](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/deploy-environment#key-stores).
  * **Test API proxies that require service accounts (for example, calling a cloud logging process as part of an API proxy flow)** \- Set up your Apigee Emulators with a service account key to enable service accounts, add policies and targets that rely on service accounts, and deploy the API proxies to the Apigee Emulator to test them. See [Customizing the Apigee Emulator to support service account-based authentication](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#customizing_the_apigee_emulator_to_support_service_account-based_authentication).



## March 23, 2023

Announcement

On March 23, 2023, we released an updated version of Apigee.

Feature

**Public preview release of Advanced API Security abuse detection**

Advanced API Security's new [abuse detection](https://docs.cloud.google.com/apigee/docs/api-security/abuse-detection) feature lets you view security incidents involving your APIs. Abuse detection uses Google's machine learning algorithms to detect API traffic patterns that are a sign of malicious activity targeting your APIs.

Abuse detection includes two new types of detection rules powered by machine learning models:

  * Advanced Anomaly Detection: Detects unusual patterns of API traffic.
  * Advanced API scraper: Detects attempts to extract information from APIs for malicious purposes.



Issue

The two new detection rules, Advanced Anomaly Detection and Advanced API Scraper, are not available for organizations with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls). We are actively working to resolve this issue.

## March 22, 2023

Feature

**Customize SSL certs for access routing when provisioning Apigee Pay-as-you-go organizations.**

Users can now select existing self-managed SSL certs when customizing access routing during Apigee Pay-as-you-go provisioning. For more information, see [Step 4: Customize access routing ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-access#perform-the-step).

Announcement

On March 22, we released an updated version of Apigee X.

Feature

**Receive Cloud console notifications when Pay-as-you-go provisioning completes.**

While provisioning is in progress, users can navigate away from the Apigee provisioning page and monitor notifications in the Cloud console for updates when provisioning completes.

## March 17, 2023

Fixed

With this release we removed certain insecure TLS ciphers for northbound traffic. You can find the full list of supported ciphers in the [FIPS build of Envoy](https://www.envoyproxy.io/docs/envoy/v1.21.5/api-v3/extensions/transport_sockets/tls/v3/common.proto.html). 

**Note** : Apigee only supports the RSA ciphers listed. ECDSA ciphers are not supported.

Announcement

On March 17, we released an updated version of Apigee X (1-9-0-apigee-23).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries.**  
  
## February 08, 2023

Announcement

On February 8, we released an updated version of Apigee X (1-9-0-apigee-21).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

The VerifyAPIKey policy and the `VerifyAccessToken` action of the OAuth2 policy now support `CacheExpiryInSeconds`. Setting this variable enforces TTL on the cache and enables customization of the time period for cached token expiry.

Fixed

Bug ID | Description  
---|---  
181569522 | Fixed the environment recreate scenario without manual cleanup.  
217173784 | **The`HMAC.policy-name.error` variable is populated for HMAC failing policies.**  
257268790 | **Fixed bug where invalid proxy configuration halted Message Processor boot up.**  
250638658 | **Fixed the SetIntegrationRequest policy that fails if the JSON payload contains`{foo}`.**  
265204739 | **Set`externalTrafficPolicy:local` as default for Apigee X instances to mitigate `502` errors.**  
N/A | **Upgraded infrastructure and libraries.**  
  
## December 08, 2022

Announcement

On December 8, we released an updated version of Apigee X.

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

**GA release of Simplified Onboarding for Apigee X (Pay-as-you-go) in the Google Cloud console.**

With this release, new Apigee customers using Pay-as-you-go pricing can quickly configure Apigee using a simplified onboarding flow accessible from the Google Cloud console.

  * The new onboarding UI provides stepped navigation consistent with other products available in the console. 
  * Apigee X (Pay-as-you-go) provisioning is simplified but remains flexible. Default settings are provided, with the option to customize as needed.
  * Improved contextual help streamlines decision-making during onboarding.



See [Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview) and [Get started in the Cloud Console](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-select-project) for more details on provisioning Apigee X with Pay-as-you-go pricing from the Google Cloud console.

## November 18, 2022

Announcement

On November 18, 2022, we released an updated version of Apigee X (1-9-0-apigee-16).

**Note:** Rollouts of this release began on 11/18/22 and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
257268790 | There is an edge case scenario where an invalid resource or bundle configuration resulting in unhandled exception will result in failure that leads to restart of runtime pods or bootup of new runtime pods.  
  
Issue

**Known issue:** [260324159 - API proxies and shared flows deployed by customers could take around 20 to 30 minutes to deploy in the runtime plane.](https://docs.cloud.google.com/apigee/docs/release/known-issues#260324159)

## November 04, 2022

Announcement

On November 4, 2022 we released an updated version of Apigee X.

Feature

Apigee support for using Private Service Connect (PSC) for client-to-Apigee (northbound) traffic is now GA. In addition, we now support using PSC for northbound routing in multi-region configurations. For details, see [Expanding Apigee to multiple regions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/multi-region). See also [Northbound networking with Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc) and [Migrate northbound routing to Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/migrate-from-mig-to-psc).

## October 27, 2022

Announcement

On October 27, 2022 we released an updated version of Apigee X.

Feature

This release contains the General Acceptance (GA) release of [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security), which: 

  * Detects unwanted requests sent to your APIs, including attacks by bots or other malicious agents.
  * Evaluates the security of your API configurations and provides recommendations for improvements.



Advanced API Security is a paid add-on to Apigee. You can try out Advanced API Security for free in any trial org—follow the procedure described in [Enable Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#enable). Contact [Apigee](https://docs.cloud.google.com/contact?direct=true&pre_product=apigee) to learn more.

## October 24, 2022

Announcement

On October 24, 2022, we released an updated version of Apigee X (1-9-0-apigee-5).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Feature

Some runtime error messages have been improved with a reason code. To display only the error codes with a reason code, scroll down to **Search** and type `reason`. The error catalog filters the view. 

See: [Runtime error catalog](https://docs.cloud.google.com/apigee/docs/api-platform/errorcatalog/mp-runtime-errorcatalog)

Fixed

Bug ID | Description  
---|---  
252818300 | **Fixed issue with failing web socket connections.**  
249580739 | This feature introduces a new filter-based mechanism to display API products.  
249521773 | **Endpoint attachment ID naming convention change.** The ID must start with a lowercase letter followed by up to 31 lowercase letters, numbers, or hyphens, and cannot end with a hyphen. The minimum length is 2. See [Create an endpoint attachment](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints#create-an-endpoint-attachment).  
249069616 | Fixed issue where error in DebugSession could interrupt runtime flow.  
248631925 | The Developer List API has been enhanced to support pagination in a Google-wide consistent pattern.  
247540503 | Race condition with encryption key lookup causing KVM lookup failures.  
246774745 | **`io.timeout.millis` not honored, causing `504 Gateway timeout` for dynamic targets.**  
246193561 | Disabling/Destroying of customer cloud KMS key impacted the runtime after 5 minutes and data that was encrypted with the key could not be accessed by Apigee data plane.  
241786534 | MART is able to send logs to UDCA successfully now.  
240618523 | Dynamically setting `target.url` now supports websocket protocols (`ws` and `wss`)  
218567150 | **`X-request-id` headers modified at 14th character.**  
206879901 | Fixed issue where Response headers were not visible from debug screen.  
173566787 | Message Processors behavior is changed. Message Processors will now reuse existing target IP addresses once if DNS resolution fails during DNS cache refresh  
159599332 | The flow variable `servicecallout.requesturi` reflects appropriately if the URI is constructed using multiple variables.  
N/A | **Upgraded infrastructure and libraries**  
  
Security

Bug ID | Description  
---|---  
204965286 | Security fix for [CVE-2022-25647](https://nvd.nist.gov/vuln/detail/CVE-2022-25647)  
193613381 | Security fix for [CVE-2021-21290](https://nvd.nist.gov/vuln/detail/CVE-2021-21290) in netty-transport  
  
Issue

**Known issue:** [257268790 - Unhandled exception results in failure that leads to restart or bootup of new runtime pods.](https://docs.cloud.google.com/apigee/docs/release/known-issues#257268790)

## October 06, 2022

Announcement

On October 6, 2022, Apigee announced the GA launch of Cloud Monitoring for Apigee gateway node usage for Pay-as-you-go customers.

The availability of Apigee gateway node usage metrics in Cloud Monitoring enables Pay-as-you-go customers to view node usage, create dashboards, and configure alerting policies using Cloud Monitoring interfaces. For more information, see [View usage and estimate your bill](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-view-usage).

## September 26, 2022

Announcement

Availability of scripts to recreate Apigee instances created before January 25, 2022.

Feature

If you have an Apigee instance that was created before January 25, 2022, Apigee recommends that you replace it with a new instance. If you do not recreate the older instance, you may experience scaling issues and the number of environments you can add to an instance will continue to be limited to 10.

For more information and detailed instructions, see [Recreating an Apigee instance with zero downtime](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instance-recreate)

## September 14, 2022

Announcement

On September 14, 2022 we released an updated version of the Apigee X software.

Feature

When using local development with Apigee in VS Code, the following pre-release features are available as part of the Insiders build (v1.21.0 and higher):

  * [Using a different version of the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#using_a_different_version_of_the_apigee_emulator)

  * [Customizing the Apigee runtime Docker container](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#customizing_the_apigee_runtime_docker_container)




## September 09, 2022

Announcement

On September 09, 2022, we released an updated version of Apigee X.

Feature

With this release, Apigee support for Private Service Connect (PSC) is GA. PSC allows you to privately connect Apigee to target services running across VPC networks in addition to the peered network. For more information, see [Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints).

## August 30, 2022

Feature

With this release, the Apigee **Pay-as-you-go** pricing model includes a maximum Apigee gateway node count of 1,000 across all environments in a region.

Announcement

On August 30, 2022, Apigee announced the GA launch of **Pay-as-you-go pricing** , a consumption-based model for Google's Apigee Platform.

When you use **Pay-as-you-go pricing** for Apigee, you are charged for the following:

  * The number of Apigee gateway nodes in the Apigee organization
  * The number of API requests processed by Apigee Analytics services
  * The amount of network usage



For more information, see the [Pay-as-you-go overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go) and the [Pay-as-you-go Example pricing](https://cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-examples).

## August 22, 2022

Issue

Value of `io.timeout.millis` is not honored when used with multiple dynamic targets. 

If a proxy sets two or more `io.timeout.millis` values in two or more flows using the same target host, only one ` io.timeout.millis` value is honored.

Announcement

On August 22, 2022, we released an updated version of Apigee X (1-8-0-apigee-33).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries**  
  
## August 11, 2022

Announcement

On August 11, 2022 we released an updated version of Apigee X.

Feature

This release contains the new [Abuse page](https://cloud.google.com/apigee/docs/api-security/security-scores#abuse-page) in Advanced API Security, which displays information about bots that have been detected by analysis of your API traffic. The Abuse page displays the IP addresses of detected bots, as well as their locations, the bot rules that led to their detection, and other details.

## July 25, 2022

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries**  
  
Announcement

On July 25, 2022, we released an updated version of Apigee X (1-8-0-apigee-23).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## July 21, 2022

Announcement

On July 21, 2022 we released an updated version of Apigee X.

Feature

The Advanced API Security's [target assessment](https://cloud.google.com/apigee/docs/api-security/security-scores#target-assessment), which evaluates the security of target servers in your API, is now available. See [Security scores in the Apigee UI](https://cloud.google.com/apigee/docs/api-security/security-scores) to learn more.

## June 30, 2022

Announcement

On June 30, 2022 we released an updated version of Apigee X.

Feature

This release contains the Public Preview of [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security), which protects your APIs from unwanted requests, including attacks by malicious clients such as bots, and evaluates the security level of your API configurations. 

Advanced API Security lets you:

  * Create [_security reports_](https://docs.cloud.google.com/apigee/docs/api-security/security-report-jobs) to detect bots and other threats to your APIs.
  * View [_security scores_](https://docs.cloud.google.com/apigee/docs/api-security/security-scores), which rate the security of your APIs and provide recommendations for improving security.



## June 21, 2022

Fixed

Bug ID | Description  
---|---  
234355351 | **Fixed issue with message processor pods restarting frequently.** Added backoff polling task for Cloud KMS key listener. The listener is paused only when the flush policy is met.  
N/A | **Upgraded infrastructure and libraries.**  
  
Announcement

On June 21, 2022, we released an updated version of Apigee X (1-8-0-apigee-18).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## June 02, 2022

Announcement

On June 2, 2022, we released an updated version of Apigee X.

Feature

Apigee X APIs for managing key value entries in a key value map scoped to an organization, environment, or API proxy are now available. For more information, see the [Apigee API reference documentation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest#rest-resource:-v1.organizations.apis.keyvaluemaps.entries).

## May 23, 2022

Announcement

On May 23, 2022, we released an updated version of Apigee X (1-8-0-apigee-9).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries**  
  
## May 09, 2022

Feature

The `GoogleIDToken.Audience` tag now includes the `useTargetUrl` attribute to simplify audience configuration of Google ID tokens for Apigee policies.

Announcement

On May 9, 2022 we released an updated version of the Apigee X software (1-8-0-apigee-5).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
**221292104** | Fix to address failure to capture requests in Debug sessions involving PostClientFlow ServiceCallouts.  
**228855520** | Upgraded ASM to the latest version.  
  
Security

Bug ID | Description  
---|---  
**217497793** | A security issue was addressed.  
  
## April 22, 2022

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries**  
  
Announcement

On April 22, 2022 we released an updated version of the Apigee X software (1-7-0-apigee-34).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

## March 31, 2022

Announcement

On March 31, 2022, we released an updated version of Apigee X.

Feature

You can now use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) (PSC) to connect to Apigee. This architectural pattern eliminates the need to create managed instance groups to forward requests from the global load balancer to Apigee. For details, see [Using Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/psc-overview).

## March 29, 2022

Announcement

On March 29, 2022, we released an updated version of Apigee X (1-7-0-apigee-28).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries**  
  
## March 28, 2022

Announcement

On March 28, 2022 we released an updated version of Apigee X.

Feature

You can now use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) (PSC) to connect Apigee with backend target services running in VPC networks other than the one that is peered with your Apigee organization. For details, see [Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints).

## March 22, 2022

Announcement

On March 22, 2022, we released an updated version of the Apigee X software.

Feature

**Support for conditions in IAM policies**

You can add resource conditions in your IAM policies. A resource condition lets you have granular control over your Apigee resources. For more information, see [Adding resource conditions in IAM policies](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/add-iam-conditions).

## March 15, 2022

Announcement

On March15, we released **version 1.7x** of Apigee X (1-7-0-apigee-22).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the following features and fixes available until the rollout is complete.

Feature

**[GraphQL policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/graphql-policy) now supports JSON-encoded payloads.**

Issue

**Note:** When using the [GraphQL](https://docs.cloud.google.com/apigee/docs/api-platform/develop/graphql) policy, you can only provide one graphQL schema for verification in an environment.

Feature

**[KVM pagination](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps) support now available (via the API only).**

Fixed

Bug ID | Description  
---|---  
**209622008** | Dynamic updates to rate in spike arrest are now reflected immediately.  
**219523719** | Fix to address CPU and memory consumption when `debug-session` is enabled with `response-status` as the filtering criteria.  
  
## March 03, 2022

Feature

**Southbound mTLS** can be enabled for use with [configurable API proxies ](https://docs.cloud.google.com/apigee/docs/api-platform/develop/configurable-api-proxies).

By adding south bound mTLS functionality to configurable proxies, Apigee customers can seamlessly maintain their current usage of mTLS when transitioning to the use of configurable proxies, or increase security for communications between existing configurable proxies and their backends.

For more information, see [Enable south bound mTLS for configurable proxies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/mtls-configurable-proxies).

Announcement

On March 3, 2022, we released new features for the Public Preview of configurable API proxies. To learn more, see [Introduction to configurable API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/configurable-api-proxies).

Feature

[Configurable API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/configurable-api-proxies) now support the use of **template variables.**

Apigee property sets can be used to specify template variables for configurable API proxies in [archive deployments](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/manage-archive-deployments). This feature enables customers to use string templates in their proxy configuration YAML files. 

For more information, see [Template variables for configurable proxies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/template-variables-configurable-proxies).

Feature

**Google authentication** for securing targets is now supported when using [configurable API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/configurable-api-proxies).

With this feature, configurable API proxy developers can secure their Google backend services using Google OAuth and automatically grant access to authorized API consumers. This offers the advantage of seamless integration with other Google services, without requiring API producers to manage private keys.

For more information, see [Securing targets for configurable proxies](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/configurable-proxy-service-account).

Feature

**HTTP request transforms** are now available for use with [configurable API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/configurable-api-proxies).

With HTTP request transforms, configurable API proxy developers can quickly rewrite HTTP request paths, header, and query parameters using HTTP Request Transforms. Rewriting is enabled using a simple configuration that can reference incoming path template segments, header values, or query parameter values. 

For more information, see [HTTP request transforms for configurable proxies](https://docs.cloud.google.com/apigee/docs/api-platform/develop/transform-headers-configurable-proxies).

## February 15, 2022

Announcement

On February 15, 2022 we released an updated version of the Apigee X software.

Feature

**Backend target routing with Private Service Connect**

You can now use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) (PSC) to connect Apigee with backend target services running in VPC networks other than the one that is peered with your Apigee organization. For details, see [Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints).

## February 08, 2022

Announcement

On February 8, 2022 we released an updated version of the Apigee X software.

Fixed

Bug ID | Description  
---|---  
N/A | **Upgraded infrastructure and libraries**  
  
## January 28, 2022

Announcement

On January 28, 2022 we released an updated version of the Apigee X software.

Feature

**UI updates for service networking and instance creation**

UI updates were made to support changes to network IP CIDR range requirements for service networking and instance creation. These changes simplify Apigee provisioning.

## January 24, 2022

Announcement

On January 24, 2022 we released an updated version of the Apigee X software.

Feature

**Reduce the IP range required to peer your VPC network**

The required IP range needed to peer your VPC network to the Apigee network is now limited to a non-overlapping CIDR range of /22. This change simplifies Apigee provisioning. Note that the provisioning step for [service network configuration](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#service-networking) has been updated to reflect this change. For more information, see [Understanding peering ranges](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
