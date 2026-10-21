---
url: https://docs.cloud.google.com/feeds/apigee-x-release-notes.xml
title: Apigee X - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:39:15.552528+00:00
---

# Apigee X - Release notes

> Source: https://docs.cloud.google.com/feeds/apigee-x-release-notes.xml

tag:google.com,2016:apigee-x-release-notesApigee X - Release notesGoogle Cloud Platform2026-10-02T00:00:00-07:00October 02, 2026tag:google.com,2016:apigee-x-release-notes#October_02_20262026-10-02T00:00:00-07:00Announcement 

On October 2, 2026, we released an updated version of Apigee (1-18-0-apigee-6).

**Note:** Rollouts of this release began today and can take four or more business days to complete across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.

### Security

Bug ID | Description  
---|---  
**564386425** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway (ASM) to patch security vulnerabilities.  
**561666530** | **Security fix for Apigee.** Upgraded the Prometheus library to patch the following vulnerabilities: 

  * [CVE-2026-42151](https://nvd.nist.gov/vuln/detail/CVE-2026-42151)
  * [CVE-2026-42154](https://nvd.nist.gov/vuln/detail/CVE-2026-42154)
  * [CVE-2026-44903](https://nvd.nist.gov/vuln/detail/CVE-2026-44903)
  * [CVE-2026-40179](https://nvd.nist.gov/vuln/detail/CVE-2026-40179)

  
**N/A** | **Security fix for Apigee infrastructure.**  
  
### Fixed

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
]]> September 21, 2026tag:google.com,2016:apigee-x-release-notes#September_21_20262026-09-21T00:00:00-07:00Announcement 

On September 21st, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-4** , your instance will be updated to **1-18-0-apigee-4** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

### Announcement

On September 21st, 2026, we released an updated version of Apigee (1-18-0-apigee-5).

**Note:** Rollouts of this release began today and can take four or more business days to be completed across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.

### Security

Bug ID | Description  
---|---  
**560130499** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy.  
**547681234** | **Security fix for Apigee.** Patched [CVE-2026-69247](https://nvd.nist.gov/vuln/detail/CVE-2026-69247) by upgrading a third-party library used by the Apigee model-security engine.  
**556568593** | **Security fix for Apigee.** Patched [CVE-2026-84304](https://nvd.nist.gov/vuln/detail/CVE-2026-84304) by upgrading gRPC.  
**N/A** | **Security fix for Apigee infrastructure.**  
  
### Fixed

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
]]> September 10, 2026tag:google.com,2016:apigee-x-release-notes#September_10_20262026-09-10T00:00:00-07:00Fixed 

Addendum to Apigee release notes dated August 27, 2026 (1-18-0-apigee-4).

Bug ID | Description  
---|---  
**502540992** | Fixed an issue where the SemanticCacheLookup policy was incompatible with Vertex AI Vector Search Private Service Connect (PSC) endpoints.  
]]> September 09, 2026tag:google.com,2016:apigee-x-release-notes#September_09_20262026-09-09T00:00:00-07:00Feature 

**SemanticCacheLookup policy supports non-default Vector Search distance measures**

Available in Apigee `1-18-0-apigee-4` and later. A new optional `<DistanceMeasureType>` element accepts `DOT_PRODUCT_DISTANCE` (the default, and the existing behavior), `COSINE_DISTANCE`, `SQUARED_L2_DISTANCE` and `L1_DISTANCE`. The policy now compares `<Threshold>` in the direction the declared measure implies, so declaring a non-default measure requires re-tuning the threshold in the same edit. The 0-to-1 restriction on `<Threshold>` is also removed.

]]> August 27, 2026tag:google.com,2016:apigee-x-release-notes#August_27_20262026-08-27T00:00:00-07:00Announcement 

On August 27th, 2026, we released an updated version of Apigee (1-18-0-apigee-4).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Fixed

Bug ID | Description  
---|---  
**507878328** | Upgraded the Apigee runtime to run on JDK 17, while maintaining backward compatibility with JDK 11.  
**530965355** | Added an opt-in Message Processor connection-failure back-off (CWC property HTTPClient.backoff.enabled, defaults to false) that prevents the Message Processor from consuming excessive CPU when a target is completely unavailable.  
**532793298** | Fixed an API product bug where combining a payloadOperationGroup with a REST or llmOperationGroup rejected REST/LLM traffic with a 401.  
**534420582** | The JSONThreatProtection policy adds a new optional child element <RejectDuplicateKeys> that rejects request bodies containing duplicate JSON keys within the same object. Defaults to false to preserve existing behavior.  
**N/A** | Updates to infrastructure and libraries.  
  
This list is incomplete; see entries for September 9, 2026 and September 10, 2026.

### Security

Bug ID | Description  
---|---  
**544570126** | **Security fix for Apigee.** Fixed a security issue in the PythonScript policy.  
**N/A** | **Security fix for Apigee infrastructure.**  
]]> August 13, 2026tag:google.com,2016:apigee-x-release-notes#August_13_20262026-08-13T00:00:00-07:00Announcement 

On August 13th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-18-0-apigee-2** , your instance will be updated to **1-18-0-apigee-2** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

### Announcement

On August 13th, 2026, we released an updated version of Apigee (1-18-0-apigee-3).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Fixed

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
  
### Security

Bug ID | Description  
---|---  
**535928300** | **Security fix for Apigee.** Fixed a security issue in JWT refresh token revocation handling.  
**539515020** | **Security fix for Apigee.** Fixed a security issue in the MessageValidation policy.  
**535928530** | **Security fix for Apigee.** Fixed a security issue in the OAuthV2 policy.  
**535683286** | **Security fix for Apigee.** Fixed a security issue in HTTP target interim-response handling.  
**N/A** | **Security fix for Apigee infrastructure.**  
]]> July 27, 2026tag:google.com,2016:apigee-x-release-notes#July_27_20262026-07-27T00:00:00-07:00Announcement 

On July 27th, 2026, we released an updated version of Apigee (1-18-0-apigee-2).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Feature

**SanitizeUserPrompt and SanitizeModelResponse policies now support function calling**

The SanitizeUserPrompt and SanitizeModelResponse policies now handle LLM function calling (tool use) flows. Two new optional XML elements extract function calling content for Model Armor sanitization:

  * `<FunctionResponseSource>` in SanitizeUserPrompt: extracts function/tool response data from user turns. Used as a fallback when `<UserPromptSource>` returns empty on function calling turns.
  * `<FunctionCallSource>` in SanitizeModelResponse: extracts function call arguments from model responses. Used as a fallback when `<LLMResponseSource>` returns empty.



Default templates target the Gemini format and require no additional configuration. For OpenAI and Anthropic formats, configure custom JSONPath templates. For more information, see [FunctionResponseSource](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-user-prompt-policy#functionresponsesource) and [FunctionCallSource](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/sanitize-llm-response-policy#functioncallsource).

### Security

Bug ID | Description  
---|---  
**534852923** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy.  
**N/A** | **Security fix for Apigee infrastructure.**  
  
### Fixed

Bug ID | Description  
---|---  
**N/A** | Updates to infrastructure and libraries.  
]]> July 16, 2026tag:google.com,2016:apigee-x-release-notes#July_16_20262026-07-16T00:00:00-07:00Announcement 

On July 16th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-10** , your instance will be updated to **1-17-0-apigee-10** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

]]> July 15, 2026tag:google.com,2016:apigee-x-release-notes#July_15_20262026-07-15T00:00:00-07:00Announcement 

On July 15th, 2026, we released an updated version of Apigee (1-18-0-apigee-1).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Fixed

Bug ID | Description  
---|---  
**527586459** | Fixed a cache policy throttling bug (CacheThrottlerV2 key poisoning) to enhance reliability.  
**525697701** | Fixed an issue where API proxy deployments could get stuck during basepath migrations in Apigee X.  
**N/A** | Updates to infrastructure and libraries.  
  
### Security

Bug ID | Description  
---|---  
**527415966, 524656652** | **Security fix for Apigee.** Upgraded the Apigee ingress gateway (ASM) to patch security vulnerabilities.  
**527956223** | **Security fix for Apigee.** Enhanced security in the Java Callout policy to prevent sandbox escape.  
**519729209** | **Security fix for Apigee.** Fixed a SAML XML Signature Wrapping (XSW) vulnerability in the ValidateSAMLAssertion policy.  
**530886487** | **Security fix for Apigee.** Upgraded the apigee-connect-agent to patch [CVE-2026-25680](https://nvd.nist.gov/vuln/detail/CVE-2026-25680).  
**N/A** | **Security fix for Apigee infrastructure.**  
]]> July 08, 2026tag:google.com,2016:apigee-x-release-notes#July_08_20262026-07-08T00:00:00-07:00Security 

An Improper Input Validation vulnerability in BigQuery DAO in Google Cloud Apigee versions prior to 2026-06-12 on Google Cloud Platform allowed an authenticated attacker to exfiltrate cross-tenant data.

This vulnerability was patched on 12 June 2026 on the Apigee Servers, and no customer action is needed. Apigee hybrid was not affected.

For more information, see [CVE-2026-12879](http://cve.org/CVERecord?id=CVE-2026-12879).

]]> July 06, 2026tag:google.com,2016:apigee-x-release-notes#July_06_20262026-07-06T00:00:00-07:00Feature 

**Support for payload operations matching in API Products**

Apigee now supports payload operations matching (`payloadOperationGroup`) in API Products, powered by the new **ParsePayload** policy.

Payload operations matching allows you to define API Product operations that match fields within request payloads, such as JSON-RPC requests used by the Model Context Protocol (MCP). Apigee can then route, monetize, authorize, and apply distinct quota limits to traffic based on the derived payload operation.

This feature is available to all Apigee X customers in all supported regions with no additional charge. For more information, see [Manage MCP tool access with API products](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/manage-mcp-tool-access) and the [ParsePayload policy reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/parse-payload-policy).

]]> June 24, 2026tag:google.com,2016:apigee-x-release-notes#June_24_20262026-06-24T00:00:00-07:00Announcement 

**Apigee Emulator**

### Apigee Emulator v2.0.1

On June 24, 2026, we released Apigee Emulator version 2.0.1.

This is a security-only hotfix release on top of v2.0.0 that addresses 10 security vulnerabilities in the Netty networking library and the embedded Cassandra Go standard library health-check binary. There are no functional, API, or configuration changes -- v2.0.1 is a drop-in replacement for v2.0.0.

The emulator image is available at [Google Artifact Registry](https://console.cloud.google.com/artifacts/docker/apigee-release/us/gcr.io/hybrid%2Fapigee-emulator).

To upgrade, update the emulator version in your VS Code Cloud Code settings to `2.0.1`. See [Manage the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#choose_the_emulator_version) for details.

### Feature

**Apigee Emulator**

#### Changed in this release

  * Upgraded Netty to `4.1.135.Final` (from `4.1.133.Final`) and pinned all transitive `netty-*` artifacts via `netty-bom`.
  * Refreshed the Cassandra base image to pick up Go standard library `1.25.11` (from `1.25.10`) in the embedded health-check binary.
  * Updated `netty-tcnative-boringssl-static` classifier variants from `2.0.53.Final` to `2.0.77.Final`.



### Security

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
]]> June 22, 2026tag:google.com,2016:apigee-x-release-notes#June_22_20262026-06-22T00:00:00-07:00Announcement 

On June 22nd, 2026, we released an updated version of Apigee (1-17-0-apigee-10).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Security

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
  
### Fixed

Bug ID | Description  
---|---  
**515788622** | Upgraded the default outbound TLS protocol from TLSv1.2 to TLSv1.3 on JVMs that support it. Per-proxy `<SSLInfo><Protocols>` settings continue to take precedence, and the new `HTTPClient.outbound.tls.protocol` override lets operators force a specific protocol.  
**184266748** | Fixed an issue where ApigeeDatastore TLS certificate creation could fail in namespaces with longer names when the certificate common name exceeded the 64-byte limit.  
**286069772** | Added a per-gateway `proxyProtocol.mode` property (strict, permissive, disable) on Apigee ingress gateway components to opt in to HAProxy PROXY-protocol parsing. The property defaults to disable.  
**N/A** | Updates to infrastructure and libraries.  
]]> June 18, 2026tag:google.com,2016:apigee-x-release-notes#June_18_20262026-06-18T00:00:00-07:00Announcement 

On June 18th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-9** , your instance will be updated to **1-17-0-apigee-9** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

]]> June 08, 2026tag:google.com,2016:apigee-x-release-notes#June_08_20262026-06-08T00:00:00-07:00Announcement 

On June 8th, 2026, we released an updated version of Apigee (1-17-0-apigee-9).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Security

Bug ID | Description  
---|---  
**514384893** | **Security fix for Apigee.** Hardened the Script policy to block server-side request forgery (SSRF) to link-local addresses.  
**N/A** | **Security fix for Apigee infrastructure.**  
  
### Fixed

Bug ID | Description  
---|---  
**512850756** | Added observability metrics for the OpenTelemetry trace export pipeline, reporting spans exported, export latency, batch size, and dropped spans.  
**515039499** | Fixed an issue where OpenTelemetry trace export over HTTP could fail to authenticate when sent through a forward proxy that requires basic authentication.  
]]> June 02, 2026tag:google.com,2016:apigee-x-release-notes#June_02_20262026-06-02T00:00:00-07:00Announcement 

On June 2nd, 2026, we released an updated version of Apigee Cassandra.

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Security

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

  
]]> May 29, 2026tag:google.com,2016:apigee-x-release-notes#May_29_20262026-05-29T00:00:00-07:00Announcement 

On May 29, 2026, we released an updated version of the Apigee UI.

### Feature

**Apigee EventFlow now supports the DataCapture policy**

You can now use the DataCapture policy within an EventFlow to extract and persist data from server-sent events (SSE) streams, such as token counts and other fields from streaming LLM responses. For more information, see [Use the DataCapture policy to capture token counts](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events#datacapture-token-counts).

### Feature

**Manage Spaces in the Apigee UI**

You can now create, view, update, and delete spaces, and manage their Identity and Access Management (IAM) policies directly in the Apigee UI. Previously, these actions could only be performed using the Apigee API. For more information, see [Apigee Spaces overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview).

]]> May 22, 2026tag:google.com,2016:apigee-x-release-notes#May_22_20262026-05-22T00:00:00-07:00Announcement 

**Apigee Emulator**

### Apigee Emulator v2.0.0

On May 22, 2026, we released Apigee Emulator version 2.0.0.

Starting with this release, the Apigee Emulator is versioned and released independently from Apigee hybrid. This enables faster delivery of security patches and updates without waiting for hybrid release cycles. The emulator image continues to be available at [Google Artifact Registry](https://console.cloud.google.com/artifacts/docker/apigee-release/us/gcr.io/hybrid%2Fapigee-emulator).

To use the new version, update the emulator version in your VS Code Cloud Code settings to `2.0.0`. See [Manage the Apigee Emulator](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/vscode/manage-apigee-emulator#choose_the_emulator_version) for details.

### Feature

**Apigee Emulator**

#### Changed in this release

  * The Apigee Emulator now follows independent semantic versioning (MAJOR.MINOR.PATCH), decoupled from Apigee hybrid versioning.
  * Updated base Cassandra image to version 4.0.19.
  * Updated Java runtime to Eclipse Temurin JRE 11.0.31.



### Security

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

]]> May 21, 2026tag:google.com,2016:apigee-x-release-notes#May_21_20262026-05-21T00:00:00-07:00Announcement 

On May 21st, 2026, we released an updated version of Apigee (1-17-0-apigee-8).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Fixed

Bug ID | Description  
---|---  
**514973778** | Fixed Model Armor response parsing to gracefully handle unknown fields, so future Model Armor field additions no longer cause policy failures.  
]]> May 20, 2026tag:google.com,2016:apigee-x-release-notes#May_20_20262026-05-20T00:00:00-07:00Security 

**On May 20, 2026, we published a security bulletin for Apigee.**

A vulnerability was found in Apigee ([CVE-2026-2264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2264)) where the `IntegrationRegion` parameter in the `SetIntegrationRequest` policy lacks validation, allowing for Server-Side Request Forgery (SSRF) and service account token exfiltration. The issue arises when an attacker can control a flow variable used for `IntegrationRegion`, leading to requests being sent to an attacker-controlled host with the service account token.

**Security bulletin published:[GCP-2026-034](https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins#gcp-2026-034)**

]]> May 12, 2026tag:google.com,2016:apigee-x-release-notes#May_12_20262026-05-12T00:00:00-07:00Announcement 

On May 12th, 2026, we released an updated version of Apigee (1-17-0-apigee-7).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Security

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

  
  
### Fixed

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
]]> April 29, 2026tag:google.com,2016:apigee-x-release-notes#April_29_20262026-04-29T00:00:00-07:00Announcement 

On April 29th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-17-0-apigee-4** , your instance will be updated to **1-17-0-apigee-4** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

]]> April 09, 2026tag:google.com,2016:apigee-x-release-notes#April_09_20262026-04-09T00:00:00-07:00Change 

**Relaxed limitation on header name for Client IP resolution**

The client IP can now be resolved from any header, not just the `X-Forwarded-For` header. The most common headers are `X-Forwarded-For` or `True-Client-Ip`.

For more information, see [Client IP resolution](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution).

]]> April 06, 2026tag:google.com,2016:apigee-x-release-notes#April_06_20262026-04-06T00:00:00-07:00Fixed 

**Correction toApril 2, 2026 release note: Deployment disruption for Apigee Drupal Portal via Google Cloud Marketplace**

For the deployment disruption announced on April 2, the announcement noted that deployment and management functionality using Google Cloud Deployment Manager would definitely be unavailable during the transition. This statement is incorrect. The functionality _might_ be unavailable.

See the [Known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258) for more information.

### Change

On April 6th, 2026, we released an updated version of Apigee.

This change introduces the new `apigee.coreServiceAgent` IAM role for Apigee. **Effective immediately, use`apigee.coreServiceAgent` instead of the `apigee.serviceAgent` role.**

For information on the new role, see [`apigee.coreServiceAgent`](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent).

]]> April 02, 2026tag:google.com,2016:apigee-x-release-notes#April_02_20262026-04-02T00:00:00-07:00Breaking 

**Deployment disruption for Apigee Drupal Portal via Google Cloud Marketplace**

Google Cloud Deployment Manager was deprecated as of March 31, 2026. We are currently transitioning the Apigee Drupal Portal Marketplace solution to use Infrastructure Manager. During this transition period, some deployment and management functionalities are unavailable.

**Impact:**

  * **New Deployments:** Starting April 1, 2026, attempting to deploy a new Apigee Drupal Portal instance using the "Deploy" button on the Google Cloud Marketplace will fail.
  * **Existing Deployments:** Your underlying resources (such as VMs and Cloud SQL databases) are unaffected and will continue to run normally. However, you can no longer use Deployment Manager-based features to manage the deployment via the Marketplace UI or the `gcloud deployment-manager` tool.



**Workaround & Resolution:** Any configuration changes or management tasks must be performed directly on the individual Google Cloud resources (Compute Engine, Cloud SQL, etc.) rather than through the Marketplace UI.

We are actively working to release the updated Infrastructure Manager-based solution.

]]> March 31, 2026tag:google.com,2016:apigee-x-release-notes#March_31_20262026-03-31T00:00:00-07:00Announcement 

On March 31st, 2026, we released an updated version of Apigee.

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Feature

**General Availability (GA) launch of Model Context Protocol (MCP) in Apigee**

With this release, Model Context Protocol (MCP) in Apigee is [generally available](https://docs.cloud.google.com/products#product-launch-stages), enabling you to expose your Apigee APIs as MCP tools to agentic applications.

Any MCP client that supports remote MCP endpoints over HTTP/S can access these tools. Because the endpoints are managed, you don't need to install or manage local MCP servers, remote MCP servers, or additional infrastructure to enable agentic applications to access your services.

MCP in Apigee is available for Subscription, Pay-as-you-go, and Evaluation organizations, including organizations with Data Residency and VPC Service Controls enabled.

For more information on using MCP in Apigee, see [MCP in Apigee overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview).

### Feature

**Enhanced OAS server URL path handling for MCP in Apigee**

With this feature enhancement, your OpenAPI specification (OAS) configurations behave exactly as defined in the OAS standard, automatically combining the `server.url` base path value with individual operation paths.

For example, a server URL of`https://example.com/api/v1` paired with a path of `/users` will now correctly route to `https://example.com/api/v1/users` without additional manual intervention.

If you previously prepended base paths to your OAS paths entries, remove the path segment from your `servers.url` field to prevent duplication. For example, change `https://example.com/api/v1` to `https://example.com`.

For more information, see [Create an OpenAPI 3.0 specification](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-quickstart#create-an-openapi-3.0.x-specification-describing-your-api-operations).

### Change

**Updated MCP server target endpoint for MCP Discovery Proxies**

With the GA launch of Model Context Protocol (MCP) in Apigee, the structure of the MCP server target endpoint for MCP Discover Proxies has changed to `ORG_NAME.mcp.apigee.internal`.

Private preview customers using the previous format (`mcp.apigee.internal`) are encouraged to update their proxies to reflect the new structure. Existing endpoints using the old format will continue to work, but new endpoints will use the new structure.

### Issue

**Known Issue 496552286: Deployment fails for MCP Discovery Proxies in regions with capacity limitations.**

For more information, see [Apigee known issues](https://docs.cloud.google.com/apigee/docs/release/known-issues).

]]> March 26, 2026tag:google.com,2016:apigee-x-release-notes#March_26_20262026-03-26T00:00:00-07:00Announcement 

On March 26th, 2026, we released an updated version of Apigee (1-17-0-apigee-6).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Security

Bug ID | Description  
---|---  
**495897297, 495909767** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities: 

  * [CVE-2026-33210](https://nvd.nist.gov/vuln/detail/CVE-2026-33210)
  * [CVE-2026-25679](https://nvd.nist.gov/vuln/detail/CVE-2026-25679)
  * [CVE-2026-27139](https://nvd.nist.gov/vuln/detail/CVE-2026-27139)
  * [CVE-2026-27142](https://nvd.nist.gov/vuln/detail/CVE-2026-27142)
  * [2026-33186](https://nvd.nist.gov/vuln/detail/CVE-2026-33186)

  
  
### Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to infrastructure and libraries.**  
]]> March 19, 2026tag:google.com,2016:apigee-x-release-notes#March_19_20262026-03-19T00:00:00-07:00Announcement 

On March 19th, 2026, we began maintenance updates of Apigee instances [configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

If you set a preferred window for maintenance for your instance, and your instance version is below **1-16-0-apigee-6** , your instance will be updated to **1-16-0-apigee-6** within the next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will **not** be updated: 

  * Your instance has a DNS misconfiguration, as described in [Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues).
  * Your instance uses an Apigee Java Library that has been removed, as described in [Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).



For more information on participating in scheduled maintenance windows, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance) and [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

]]> March 17, 2026tag:google.com,2016:apigee-x-release-notes#March_17_20262026-03-17T00:00:00-07:00Announcement 

On March 17th, 2026, we released an updated version of Apigee (1-17-0-apigee-5).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to infrastructure and libraries.**  
]]> March 10, 2026tag:google.com,2016:apigee-x-release-notes#March_10_20262026-03-10T00:00:00-07:00Announcement 

On March 10th, 2026, we released an updated version of Apigee (1-17-0-apigee-4).

**Note:** Rollouts of this release began today and may take four or more business days to be completed across all Google Cloud zones. Your instances may not have the features and fixes available until the rollout is complete.

### Fixed

Bug ID | Description  
---|---  
**N/A** | **Updates to infrastructure and libraries.**  
  
### Security

Bug ID | Description  
---|---  
**483769763, 481735779** | **Security fix for Apigee infrastructure.** This addresses the following vulnerabilities: 

  * [CVE-2025-61726](https://nvd.nist.gov/vuln/detail/CVE-2025-61726)
  * [CVE-2025-61728](https://nvd.nist.gov/vuln/detail/CVE-2025-61728)
  * [CVE-2025-61730](https://nvd.nist.gov/vuln/detail/CVE-2025-61730)
  * [CVE-2025-61731](https://nvd.nist.gov/vuln/detail/CVE-2025-61731)
  * [CVE-2025-61732](https://nvd.nist.gov/vuln/detail/CVE-2025-61732)
  * [CVE-2026-24051](https://nvd.nist.gov/vuln/detail/CVE-2026-24051)
  * [CVE-2026-25765 ](https://nvd.nist.gov/vuln/detail/CVE-2026-25765%20)

  
]]>
