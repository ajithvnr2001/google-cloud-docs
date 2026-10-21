---
url: https://docs.cloud.google.com/docs/security/owasp-top-ten-mitigation/
title: Mitigate OWASP Top 10:2025 on Google Cloud \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:41.576915+00:00
---

# Mitigate OWASP Top 10:2025 on Google Cloud  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/owasp-top-ten-mitigation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Mitigate OWASP Top 10:2025 on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document identifies the Google Cloud services and mitigation strategies that can help you defend against the application-level attacks that are outlined in [OWASP Top 10:2025](https://owasp.org/Top10/2025/). Created by the [Open Web Application Security (OWASP) Foundation](https://owasp.org/), OWASP Top 10:2025 is a list of the top 10 security risks in a software development lifecycle (SDLC). Although no service can guarantee full protection against these risks, applying these services when they make sense in your architecture can contribute to a strong multi-layer security solution.

[Google infrastructure](https://docs.cloud.google.com/docs/security/infrastructure/design) is designed to help you build, deploy, and operate services with robust security controls. Physical and operational security, data encryption at rest and in transit, and many other foundational infrastructure protections are managed by Google. You inherit these benefits by deploying your applications to Google Cloud, but you might need to take additional measures to help protect your application against specific attacks.

**Note:** Even though Google Cloud provides robust perimeter and runtime defenses, security is a shared responsibility. Mitigating OWASP risks effectively requires integrating security early in your software development lifecycle (SDLC). Use the following services alongside secure-by-default coding frameworks, regular developer training, and proactive threat modeling.

## Compliance matrix

The Google Cloud services listed in the following table can help defend against the top 10 security risks that are identified by OWASP Top 10:2025:

OWASP Top 10:2025 category | Primary Google Cloud and Wiz controls  
---|---  
[A01: Broken Access Control](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/) | Access Context Manager, Agent Gateway, Agent Identity, Apigee, Google Cloud Armor, Firebase App Check, Firebase Security Rules, Cloud Next Generation Firewall (Cloud NGFW), Identity-Aware Proxy (IAP), Identity and Access Management (IAM), Organization Policy Service, VPC Service Controls, Wiz Cloud  
[A02: Security Misconfiguration](https://owasp.org/Top10/2025/A02_2025-Security_Misconfiguration/) | Access Context Manager, Cloud Asset Inventory, Google Security Operations, Organization Policy, Security Command Center Premium, VPC Service Controls, Wiz Cloud  
[A03: Software Supply Chain Failures](https://owasp.org/Top10/2025/A03_2025-Software_Supply_Chain_Failures/) | Artifact Registry, Assured Open Source Software (Assured OSS), Binary Authorization, Cloud Build, Cloud Deploy, Cloud Workstations, CodeMender, Wiz Code  
[A04: Cryptographic Failures](https://owasp.org/Top10/2025/A04_2025-Cryptographic_Failures/) | Apigee, Certificate Authority Service, Certificate Manager, Cloud Key Management Service, Cloud Load Balancing, Cloud Workstations, Confidential Computing, Organization Policy, Secret Manager, Sensitive Data Protection, Wiz Cloud  
[A05: Injection](https://owasp.org/Top10/2025/A05_2025-Injection/) | Apigee, Cloud Armor, CodeMender, Firebase Security Rules, Cloud Next Generation Firewall (Cloud NGFW), Model Armor, Security Command Center Premium, VirusTotal, Wiz Code  
[A06: Insecure Design](https://owasp.org/Top10/2025/A06_2025-Insecure_Design/) | Apigee, CodeMender, Mandiant, Wiz Cloud  
[A07: Authentication Failures](https://owasp.org/Top10/2025/A07_2025-Authentication_Failures/) | Access Context Manager, Agent Identity, Apigee, Cloud Armor, Cloud Identity, Firebase App Check, Firebase Authentication, Google Cloud Fraud Defense, IAM (Privileged Access Manager, Workload Identity Federation, and Workforce Identity Federation), IAP, Identity Platform, Security Command Center Premium, Secret Manager, Titan Security Keys, Wiz Code  
[A08: Software or Data Integrity Failures](https://owasp.org/Top10/2025/A08_2025-Software_or_Data_Integrity_Failures/) | Artifact Analysis, Assured OSS, Binary Authorization, Cloud Armor, Cloud Build, Cloud Deploy, Firebase App Check, Security Command Center Premium, VirusTotal, Wiz Defend  
[A09: Security Logging & Alerting Failures](https://owasp.org/Top10/2025/A09_2025-Security_Logging_and_Alerting_Failures/) | Access Approval and Access Transparency, Apigee, Google SecOps, Cloud Logging, Cloud Monitoring, Sensitive Data Protection, Wiz Defend  
[A10: Mishandling of Exceptional Conditions](https://owasp.org/Top10/2025/A10_2025-Mishandling_of_Exceptional_Conditions/) | Cloud Armor, Cloud Load Balancing, Error Reporting, Model Armor  
  
## Google Cloud services

The following sections describe OWASP Top 10 best practices for core Google Cloud services.

### Access Approval and Access Transparency

[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) and [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) enable verification of cloud provider access. Using Access Transparency, you can record the reason for each access that Google personnel make. Access Approval lets you approve or dismiss requests for access by Google personnel who are working to support your service.

Applies to A09: Security Logging & Alerting Failures.

Review the following best practices:

  * Automate the access approval process. To do so, configure Access Approval to send incoming access approval request metadata to a [Pub/Sub topic](https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys#email-pubsub). Create a Pub/Sub subscription that pushes the JSON payload to your custom webhook endpoint (such as an authenticated Cloud Run service, Cloud Run functions, or an enterprise API gateway) for processing.
  * Treat [Access Transparency logs](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/reading-logs) as critical security telemetry. Create [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) and [alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) in Monitoring to flag your security operations center (SecOps) if Google personnel access sensitive resources without an active, corresponding support ticket.
  * [Export Access Transparency logs directly](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs#export-logs) to Google SecOps or your centralized enterprise SIEM.
  * Create a compliance policy to audit your log streams regularly and verify that `auto_approved` emergency access events correlate to a documented, high-severity incident.
  * For cryptographic control, use [Key Access Justifications](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/key-access-justifications) to force the system to programmatically request a key-decryption approval.



### Access Context Manager

[Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) is Google Cloud's context-aware access engine. Access Context Manager lets you define attribute-based access levels (such as client IP address ranges, device security posture, and geographic location) for IAP, VPC Service Controls, and IAM.

Applies to the following:

  * A01: Broken Access Control
  * A02: Security Misconfiguration
  * A07: Authentication Failures



Review the following best practices for A01: Broken Access Control:

  * Build reusable, tiered security levels for your organization's access policy. Create [basic access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) to test standard attributes. For complex, multi-factor conditions, deploy [custom access levels](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level) to evaluate advanced device states and third-party endpoint signals.
  * Use [Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/overview) or [Chrome Enterprise Core](https://support.google.com/chrome/a/answer/9116814) to enforce device-level constraints such as full-disk encryption, an active screen lock, and an approved operating system version.
  * To help protect high-value data repositories with VPC Service Controls, add [access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) to your VPC Service Controls ingress rules. If a service account key is leaked, an attacker cannot use only the key to query BigQuery or Cloud Storage from an unauthorized public IP address or untrusted machine.
  * To extend zero-trust protection to web applications and VM administrative tunnels, attach [access levels directly to your IAP-secured resources](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto).



Review the following best practices for A02: Security Misconfiguration:

  * Implement [scoped access policies](https://docs.cloud.google.com/access-context-manager/docs/scoped-policies) that are bound to specific folders to delegate local policy management to individual project teams and isolate their changes from the rest of the organization.
  * To keep orphaned ingress rules from becoming silent backdoors, regularly review and remove decommissioned IP ranges, expired partner subnets, and obsolete device attributes.



Review the following best practices for A07: Authentication Failures:

  * Use user access bindings to set strict maximum session durations. Configure the [reauthentication policy](https://docs.cloud.google.com/access-context-manager/docs/session-controls-for-reauthentication) to require `SECURITY_KEY` (FIDO2 or WebAuthn). To apply stricter constraints to high-risk environments, configure [`scopedAccessSettings`](https://docs.cloud.google.com/access-context-manager/docs/manage-access-bindings#update_an_access_binding) to override default session durations for sensitive applications.



### Agent Gateway and Agent Identity

[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) and [Agent Identity](https://docs.cloud.google.com/iam/docs/agent-identity-overview) provide dedicated network policy enforcement, identity lifecycle management, and cryptographic authentication for AI agents and agentic workflows.

Applies to the following:

  * A01: Broken Access Control
  * A07: Authentication Failures



Review the following best practices for A01: Broken Access Control:

  * In environments with multi-agent systems, external MCP tools, or autonomous pipelines, use Agent Gateway as a dedicated network and policy enforcement point to help mitigate agentic access control failures.
  * Configure [granular authorization policies](https://docs.cloud.google.com/iam/docs/agent-identity-overview#security-governance) for agent identities to restrict tool access and data retrieval to only the resources required for the agent's specific workflow.



Review the following best practices for A07: Authentication Failures:

  * To authenticate autonomous agents and tool integrations without embedding static API keys or passwords, [generate and assign an Agent Identity](https://docs.cloud.google.com/iam/docs/create-and-deploy-agent) to each agent.
  * Configure Agent Identity to issue an [X.509 certificate](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-credentials) as the agent's credentials. These certificates help prevent token theft so that if an access token is intercepted, that token is unusable from other environments.



### Apigee

[Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) provides centralized, gateway-level mechanisms using [API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/structure-api-proxies) to enforce cryptographic standards, validate signed payloads, and encrypt application data in transit and at rest. By acting as a reverse-proxy gateway for API traffic, Apigee runs boundary and structure checks to help validate payloads. Apigee provides built-in API authentication, OAuth, and JSON Web Token (JWT) verification policies to establish strong identity boundaries. Apigee includes several ways to perform logging, monitoring, error handling, and audit logging.

Applies to the following:

  * A01: Broken Access Control
  * A04: Cryptographic Failures
  * A05: Injection
  * A06: Insecure Design
  * A07: Authentication Failures
  * A09: Security Logging & Alerting Failures



Review the following best practices for A01: Broken Access Control:

  * Use [API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview) to complete the following:

    * Intercept requests where an attacker attempts to access another user's records by manipulating ID variables in the API request path.

    * Block standard clients from executing restricted administrative methods or high-privilege operations.

  * For the API management plane, enforce [access controls](https://docs.apigee.com/api-platform/system-administration/understanding-roles), [authentication](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview), and secret storage using [encrypted Key Value Maps](https://docs.cloud.google.com/apigee/docs/api-platform/develop/accessing-config-data#when-to-use-key-value-maps), Secret Manager, or [Kubernetes Secrets](https://docs.cloud.google.com/apigee/docs/api-platform/develop/accessing-config-data#when-to-use-kubernetes-secrets) (hybrid deployments only).

  * Use [OAuth policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) and [JWT](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/jwt-policies-overview) tokens to verify signatures. Map sensitive endpoints and actions to high-privilege, granular OAuth scopes (for example, `delete:account` or `write:billing`). Use the [`OAuthV2` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy) to validate these scopes at the API entry point, and return an HTTP `403 Forbidden` status code to any client that doesn't have the correct permissions.

  * Enable [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security/aas-apigee-overview) to analyze traffic for anomalous behavioral patterns and start [security actions](https://docs.cloud.google.com/apigee/docs/api-security/security-actions).




Review the following best practices for A04: Cryptographic Failures:

  * Encrypt sensitive data in your application and enforce strict cryptographic validation before traffic reaches your backend application. Configure your Apigee environment with [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts) using Cloud KMS.
  * Use [one-way and two-way TLS](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/options-configuring-tls) to encrypt sensitive information at the protocol level. For server-to-server or high-risk business integrations, configure [mutual TLS (mTLS)](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/ingress-tls) at the Apigee ingress gateway.
  * Use the [`VerifyJWT` and `VerifyJWS` policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jwt-policy) to require that incoming tokens have a valid cryptographic signature before the request is processed. Use standard [OAuth](https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/secure-calls-your-api-through-oauth-20-client-credentials) techniques and consider implementing HMAC, payload hashing, state or nonce validation, and Proof Key for Code Exchange (PKCE) to cryptographically harden each request.
  * [Mask sensitive data](https://docs.cloud.google.com/apigee/docs/api-platform/security/data-masking) so that data is encrypted and hidden when using the [Apigee Debug tool](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace).



Review the following best practices for A05: Injection:

  * Deploy Apigee threat protection policies to sanitize input parameters and block SQL, NoSQL, and command injection attempts at the gateway layer: 
    * [`JSONThreatProtection`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/json-threat-protection-policy)
    * [`XMLThreatProtection`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-threat-protection-policy)
    * [`RegularExpressionProtection`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/regular-expression-protection)
    * [`SOAPMessageValidation`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-validation-policy)



Review the following best practices for A06: Insecure Design:

  * Validate incoming requests with the [`OASValidation` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oas-validation-policy) for incoming request or response messages against the OpenAPI Specification.
  * Mitigate traffic spikes and backend overload by implementing the [`SpikeArrest` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy) and the [`Quota` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy).
  * Use [Fault handling rules](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/fault-handling) to intercept backend errors (like a database crash) and rewrite them into generic HTTP responses.



Review the following best practices for A07: Authentication Failures:

  * Implement [API key validation](https://docs.cloud.google.com/apigee/docs/api-platform/security/setting-api-key-validation) for your developer-facing APIs so that Apigee can check whether a client application's API key is present, valid, and authorized to access the requested API resource.
  * To help prevent session token theft and replay attacks, [implement Demonstrating Proof-of-Possession (DPoP)](https://discuss.google.dev/t/navigating-the-industry-shift-in-client-authentication-for-apigee-mtls/289627). DPoP binds tokens to the sender's public key to mitigate token replay.
  * Defend token generation and login endpoints against automated brute-force attacks by combining [`SpikeArrest`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy) rate limits with [reCAPTCHA Enterprise integration](https://discuss.google.dev/t/apigee-x-and-recaptcha-enterprise-best-friends-ever/84641).



Review the following best practices for A09: Security Logging & Alerting Failures:

  * Asynchronously stream structured API transaction metadata to Logging or third-party SIEMs. Attach your [`MessageLogging` policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy) to `PostClientFlow`, which runs after the response is delivered to the client.
  * Centralize platform audit logs to track modifications to API proxies, credentials, and deployment environments. To help prevent unauthorized proxy modifications from going unnoticed, integrate Apigee with Cloud Audit Logs. For more information, see [Apigee audit logging](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/audit-logging) and [Apigee API Management audit logging](https://docs.cloud.google.com/apigee/docs/api-observation/audit-logging).
  * Configure [Advanced API Security alerts](https://docs.cloud.google.com/apigee/docs/api-security) in Monitoring to notify SecOps teams of automated scraping campaigns, credential abuse, and security score regressions.
  * Sanitize user-provided variables in your log message templates by wrapping them in the [`escapeJSON()` function](https://docs.cloud.google.com/apigee/docs/api-platform/reference/message-template-intro#character-escape-and-encoding-functions).
  * If you stream log metadata to an external SIEM, configure the `MessageLogging` policy to use Syslog over TLS (TCP port `6514`) to encrypt your data in transit.



### Artifact Registry and Artifact Analysis

[Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) is a single place for your organization to manage container images and language packages. [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) provides integrated vulnerability scanning, Software Bill of Materials (SBOM) generation, and metadata storage for artifacts stored in Artifact Registry.

Applies to the following:

  * A03: Software Supply Chain Failures
  * A08: Software or Data Integrity Failures



Review the following best practices for A03: Software Supply Chain Failures:

  * Reduce attack surface and help prevent the deployment of vulnerable legacy images by configuring [cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy-overview) to delete unversioned, untagged, or stale release candidate images after a predefined retention period.
  * Protect against dependency confusion attacks by configuring [virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview) with upstream [repository priorities](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-overview#repo-priority) that prioritize internal artifact repositories over public registries.
  * Enforce immutable image tags or deploy strictly by cryptographic digest (`sha256:...`) to prevent tag-mutation attacks.



Review the following best practices for A08: Software or Data Integrity Failures:

  * Enable [automatic vulnerability scanning](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) and [SBOM generation](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview) in Artifact Analysis to detect critical CVEs before deployment.
  * Integrate Artifact Analysis metadata with [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) attestations to block the deployment of images that fail security thresholds.



### Assured OSS

[Assured OSS](https://docs.cloud.google.com/assured-open-source-software/docs/overview) lets you incorporate the OSS packages that Google validates and uses into your own developer workflows.

Applies to the following:

  * A03: Software Supply Chain Failures
  * A08: Software or Data Integrity Failures



Review the following best practices for A03: Software Supply Chain Failures:

  * Configure [remote repositories](https://docs.cloud.google.com/security-command-center/docs/aoss-remote-repository-access) to point upstream to Assured OSS.
  * Verify that the open-source libraries in your builds contain a valid Google signature and verifiable SLSA build provenance record. Configure quality gates in Cloud Build to verify these attestations before compiling application binaries.
  * Configure the package managers (such as `pip.conf`, `settings.xml`, or `build.gradle`) in your Cloud Workstations base images to point only to your internal Assured OSS repositories.
  * Use the [metadata that's generated by Assured OSS](https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata) to determine whether a newly disclosed CVE in an open-source package is exploitable in your specific deployment context.



Review the following best practices for A08: Software or Data Integrity Failures:

  * Promote package integrity across build pipelines by configuring [virtual upstream repositories](https://docs.cloud.google.com/assured-open-source-software/docs/overview#aoss-repository-options) in Artifact Registry to enforce Google-verified cryptographic signatures.
  * Use the [Assured OSS Premium tier (part of Security Command Center Premium)](https://docs.cloud.google.com/security-command-center/docs/integrate-aoss-with-scc) to automate repository provisioning, access curated JavaScript (npm) packages, and obtain access to package metadata and vulnerability notifications.



### Binary Authorization

[Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview) verifies the integrity of containers so that only trusted container images are deployed. You can create policies to allow or deny deployments based on the presence or absence of attestations. Binary Authorization applies policies at a cluster level, so you can configure different policies for different environments.

Applies to the following:

  * A03: Software Supply Chain Failures
  * A08: Software or Data Integrity Failures



Review the following best practices for A03: Software Supply Chain Failures:

  * Configure deployment pipelines to reference and enforce container images by their unique, immutable SHA-256 cryptographic digest (such as `@sha256`).
  * Deploy [Binary Authorization Continuous Validation](https://docs.cloud.google.com/binary-authorization/docs/overview-cv) on your GKE clusters to monitor active Pods against your platform policy, and generate alerts in Logging if running containers are no longer compliant.



Review the following best practices for A08: Software or Data Integrity Failures:

  * Enforce [automated attestation generation](https://docs.cloud.google.com/binary-authorization/docs/attestations) in your Cloud Build or GitHub Actions pipelines. Create progressive attestation requirements so that images pass through sequential validation gates as they move closer to production.
  * For high-severity production incidents, enable [breakglass emergency deployments](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass). Configure Monitoring alerting policies on breakglass audit log events to notify your SecOps team when an admission bypass occurs.



### CA Service and Certificate Manager

[Certificate Authority Service (CA Service)](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) simplifies the deployment and management of private certificate authorities (CAs). [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) provides centralized provisioning, renewal, and management of TLS certificates for Cloud Load Balancing and Cloud CDN.

Applies to A04: Cryptographic Failures.

Review the following best practices:

  * Use [CA Service](https://docs.cloud.google.com/certificate-authority-service/docs) to automate the issuance and lifecycle management of private certificates. Deploy root and intermediate CAs backed by [Cloud HSM](https://docs.cloud.google.com/certificate-authority-service/docs/best-practices#hsm) to protect private keys, and use [certificate templates](https://docs.cloud.google.com/certificate-authority-service/docs/issue-certificate-using-template) to enforce cryptographic policies (such as minimum key lengths and allowed extended key usages).
  * Enable [Cloud Audit Logs](https://docs.cloud.google.com/certificate-authority-service/docs/audit-logging) to monitor for high-risk administrative events (such as CA revocation, policy updates, or a sudden spike in certificate requests). Route alerts to Google SecOps to detect potential insider threats or compromised CI/CD pipelines.
  * Configure Certificate Manager to use Google-managed certificates paired with [DNS authorizations](https://docs.cloud.google.com/certificate-manager/docs/domain-authorization). Certificate Manager validates domain ownership, issues the X.509 certificate, and handles renewals 30 days before expiration.
  * Attach [certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps) to target HTTPS proxies to enable dynamic certificate selection and certificate rotation without requiring proxy restarts or load balancer reconfigurations.
  * For internal microservices or hybrid load balancing, configure [certificate maps](https://docs.cloud.google.com/certificate-manager/docs/maps) to issue private certificates directly from a private CA Service CA pool.
  * Configure certificate maps to match incoming Server Name Indication (SNI) requests to specific certificates.



### Cloud Asset Inventory

[Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) lets you monitor your infrastructure on Google Cloud for orphaned or unauthorized IT infrastructure.

Applies to A02: Security Misconfiguration.

Review the following best practices:

  * [Set up notifications](https://docs.cloud.google.com/asset-inventory/docs/monitor-asset-changes) to alert you for unexpected running resources, which might be improperly secured or using outdated software.
  * Use [IAM Policy Analyzer](https://docs.cloud.google.com/asset-inventory/docs/view-resource-policies) to discover misconfigured access controls, such as public storage buckets with the `allUsers` permission, over-privileged service account roles, or orphaned identities.
  * [Export asset snapshots to BigQuery](https://docs.cloud.google.com/asset-inventory/docs/export-bigquery) to audit infrastructure configurations over time and maintain a baseline compliance record across multi-project environments.



### Cloud Armor

[Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) is an adaptive web application firewall (WAF) that you deploy at your Google Cloud network's edge to help defend against DDoS attacks and block SQLi or XSS injection payloads. Cloud Armor includes [preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules) to defend against OWASP Top 10 vulnerabilities, limit the attack surface of your authentication endpoints, and block compromised credentials.

Applies to the following:

  * A01: Broken Access Control
  * A05: Injection
  * A07: Authentication Failures
  * A08: Software or Data Integrity Failures
  * A10: Mishandling of Exceptional Conditions



Review the following best practices for A01: Broken Access Control:

  * Apply [preconfigured WAF rules](https://docs.cloud.google.com/armor/docs/waf-rules) such as `evaluatePreconfiguredWaf('lfi-stable')` to block local file inclusions and path traversal attacks.
  * Enforce geographic access controls (also known as _geo-fencing_) by [configuring a security policy rule](https://docs.cloud.google.com/armor/docs/configure-security-policies) that matches incoming traffic based on its originating country code using the `origin.region_code` attribute.
  * Block known malicious IP addresses using a [threat intelligence feed](https://docs.cloud.google.com/armor/docs/threat-intelligence).
  * Restrict external access to sensitive URLs (such as `/admin`, `/login`, or `/config`) by [writing a match rule](https://docs.cloud.google.com/armor/docs/configure-security-policies#path-traversal-and-normalization).
  * Enable [Cloud Armor path normalization](https://docs.cloud.google.com/armor/docs/configure-security-policies#path-traversal-and-normalization) on your load balancer, forcing Cloud Armor to decode and standardize incoming URLs before evaluating your security policies.



Review the following best practices for A05: Injection:

  * Detect and block SQL injection (`sqli-v422-stable`), cross-site scripting (`xss-v422-stable`), PHP command injection (`php-v422-stable`), and Java injection (`java-v422-stable`) at the network edge.
  * [Tune preconfigured WAF rules to different sensitive levels](https://docs.cloud.google.com/armor/docs/rule-tuning) to address [false positives](https://docs.cloud.google.com/armor/docs/troubleshooting#false-positives) before configuring the rules to actively deny traffic.
  * Enable the preconfigured [remote code execution (RCE) rule (`rce-v422-stable`)](https://docs.cloud.google.com/armor/docs/waf-rules#remote_code_execution_rce) and the [remote file inclusion (RFI) rule (`rfi-v422-stable`)](https://docs.cloud.google.com/armor/docs/waf-rules#remote_file_inclusion_rfi) to catch additional, complex command-injection techniques.
  * For injection attacks other than attacks that target SQL or PHP, create [custom rules](https://docs.cloud.google.com/armor/docs/rules-language-reference#preconfigured-rules). Custom rules let you block requests when specific keywords or escape patterns in protocols are used in the request path or query.



Review the following best practices for A07: Authentication Failures:

  * [Restrict access](https://docs.cloud.google.com/armor/docs/security-policy-overview) to authentication and administrative endpoints to authorized IP addresses or countries.
  * Enable `evaluatePreconfiguredWaf` to intercept and block requests designed to exploit session-state vulnerabilities and session hijacking.
  * Use the [`securityPolicies.patchRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/patchRule) API to block any incoming requests that contain a compromised parameter in the query string or headers at the network edge.



Review the following best practices for A08: Software or Data Integrity Failures:

  * Restrict endpoints that accept high-risk serialized objects from untrusted sources to a set of trusted IP addresses with a deny rule similar to the following:
        
        request.path.contains('/endpoint') && !inIpRange(origin.ip, '192.0.2.1/32')
        

  * Deploy [custom rules](https://docs.cloud.google.com/armor/docs/rules-language-reference) to inspect request body keywords for language-specific execution patterns and unsafe deserialization signatures.




Review the following best practices for A10: Mishandling of Exceptional Conditions:

  * Enable [Google Cloud Armor Adaptive Protection](https://docs.cloud.google.com/armor/docs/adaptive-protection-overview) on your security policies to baseline normal traffic patterns, configure alerts on L7 anomalies, and generate targeted WAF rules with attack signatures.
  * Configure [Cloud Armor rate limiting rules](https://docs.cloud.google.com/armor/docs/rate-limiting-overview) on critical endpoints (for example, `/login`, `/checkout`, or search APIs). Rate limiting rules throttle requests on a per-client IP or HTTP header basis (for example, limiting clients to 100 requests per minute) and return an HTTP `429 Too Many Requests` status code.
  * [Set the lowest-priority default rule](https://docs.cloud.google.com/armor/docs/configure-security-policies#update-policies) in your Cloud Armor security policy to `Deny` (status code: `403` or `404`).



### Cloud Build and Cloud Deploy

[Cloud Build](https://docs.cloud.google.com/build/docs/overview) and [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) provide an integrated, secure continuous integration and continuous delivery (CI/CD) pipeline on Google Cloud. Cloud Build builds artifacts with verifiable SLSA [provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance) and cryptographic attestations, and Cloud Deploy manages progressive rollouts, target approvals, and automated verification across GKE and Cloud Run.

Applies to the following:

  * A03: Software Supply Chain Failures
  * A08: Software or Data Integrity Failures



Review the following best practices for A03: Software Supply Chain Failures:

  * Set `requestedVerifyOption: VERIFIED` in your `cloudbuild.yaml` file to require [verifiable provenance](https://docs.cloud.google.com/build/docs/securing-builds/generate-validate-build-provenance).
  * Deploy [Cloud Build private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) that are peered with your private VPC network for sensitive enterprise builds.
  * Configure [build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers) to run under dedicated, user-managed service accounts. Grant these service accounts only the minimum required IAM allow permissions (such as Artifact Registry Writer (`roles/artifactregistry.writer`) and Logs Writer (`roles/logging.logWriter`)).
  * Require manual approvals on Cloud Build triggers that target staging or production environments.
  * Restrict CI build tools (such as Cloud Build, GitHub Actions, or GitLab) to the [Cloud Deploy Releaser (`roles/clouddeploy.releaser`)](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#clouddeploy.releaser) role so that build pipelines can create releases only.
  * To require manual approvals, configure your [delivery pipeline manifest](https://docs.cloud.google.com/deploy/docs/create-pipeline-targets) (`delivery-pipeline.yaml`) with `requireApproval: true` on your staging and production targets.
  * Configure [execution environments](https://docs.cloud.google.com/deploy/docs/execution-environment#changing_from_the_default_to_custom_execution_service_account) with target-specific service accounts (for example, one service account with permissions limited to the staging namespace, and a separate, audited service account for production).
  * [Deploy custom hooks](https://docs.cloud.google.com/deploy/docs/hooks) to run out-of-band security assertions during the rollout lifecycle. Use pre-deploy hooks to verify whether target clusters satisfy compliance baselines and post-deploy hooks to start automated vulnerability scans against live container endpoints.



Review the following best practices for A08: Software or Data Integrity Failures:

  * Integrate Cloud Build with Cloud KMS and Artifact Analysis to create and sign cryptographic attestations when unit tests and static analysis tests complete successfully.
  * Use immutable cryptographic SHA-256 digests (for example, `golang@sha256:...`) in builder steps in `cloudbuild.yaml`.
  * Store build configurations in version-controlled repositories that are protected by branch protection rules (such as mandating two-person reviews on pull requests). Restrict trigger modification permissions to authorized platform administrators using user-managed service accounts.
  * Promote identical, pre-rendered [deployment manifests](https://docs.cloud.google.com/deploy/docs/using-skaffold/managing-manifests) and immutable container image digests across target stages without letting CI pipelines alter manifests between staging and production.
  * Define automated [deployment verification tasks](https://docs.cloud.google.com/deploy/docs/verify-deployment) inside your `skaffold.yaml` manifest. Cloud Deploy runs these verification containers after pods are deployed to run dynamic health checks, integration tests, and API contract assertions.
  * Use [canary deployment strategies](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary). If a Skaffold verification test fails or Monitoring detects anomaly thresholds during a canary phase, Cloud Deploy halts the rollout and rolls back traffic to the last-known-good release version.
  * Configure GKE clusters and Cloud Run to [enforce Binary Authorization policies](https://docs.cloud.google.com/deploy/docs/securing/binary-authorization). When Cloud Deploy applies the manifests, the target admission controller cryptographically verifies the container image digests and rejects untrusted artifacts.



### Cloud Identity and Titan Security Keys

[Cloud Identity](https://cloud.google.com/identity) provides centralized identity, credential lifecycle, and access management across Google Cloud and Google Workspace. [Titan Security Keys](https://cloud.google.com/security/products/titan-security-key) are hardware-based, phishing-resistant security devices that use public-key cryptography based on FIDO2 or WebAuthn standards.

Applies to A07: Authentication Failures.

Review the following best practices:

  * To help protect against person-in-the-middle (PITM) phishing attacks, [configure 2-Step Verification (2SV)](https://docs.cloud.google.com/docs/authentication/mfa-requirement) and set the allowed method to **Security Keys Only** (FIDO2, WebAuthn, or Titan Security Keys).
  * [Configure SAML 2.0 or OIDC-based single sign-on (SSO)](https://docs.cloud.google.com/architecture/identity/single-sign-on) with your corporate identity provider alongside automated provisioning.
  * Set the [Google Cloud session length policy](https://knowledge.workspace.google.com/admin/security/set-session-length-for-google-cloud-services) to a low maximum threshold to force users to re-authenticate periodically.
  * Register Titan Security Keys as [passkeys](https://www.google.com/account/about/passkeys/) to enable passwordless authentication, significantly reducing brute-force and credential-compromise risks.
  * Mandate 2FA with Titan Security Keys for your privileged identities (such as project owners, billing administrators, and SecOps teams) by enforcing security key policies in Cloud Identity. Enroll high-risk users in the [Advanced Protection Program](https://knowledge.workspace.google.com/admin/security/protect-users-with-the-advanced-protection-program).



### Cloud KMS

[Cloud KMS](https://docs.cloud.google.com/kms/docs/key-management-service) manages symmetric and asymmetric cryptographic keys for compatible Google Cloud services and in your own applications. You can [generate, use, rotate, and destroy](https://docs.cloud.google.com/kms/docs/key-rotation) cryptographic keys for symmetric encryption, asymmetric signing, asymmetric encryption, and MAC signing.

Applies to A04: Cryptographic Failures.

Review the following best practices:

  * Use [Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) to automate provisioning and assignment. With Autokey, you don't need to provision key rings, keys, and service accounts ahead of time. Instead, keys and key rings are generated on-demand as part of resource creation.
  * Use Cloud KMS keys to encrypt sensitive payloads before the payloads are sent to storage buckets or databases. You can use the Cloud KMS API or client libraries to use your Cloud KMS keys for [client-side encryption](https://docs.cloud.google.com/kms/docs/client-side-encryption).
  * [Verify end-to-end data integrity](https://docs.cloud.google.com/kms/docs/data-integrity-guidelines) by validating checksums during transit.
  * For strict compliance and regulatory workloads, store and run your cryptographic operations using [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm). Cloud HSM stores your keys in FIPS 140-3 Level 3 validated hardware security modules.
  * [Configure automatic key rotation schedules](https://docs.cloud.google.com/kms/docs/key-rotation) on a set timeframe (for example, every 90 days).



### Cloud Load Balancing

[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) is a fully distributed, software-defined, managed service that distributes user traffic across multiple backend instances and regions.

Applies to the following:

  * A04: Cryptographic Failures
  * A10: Mishandling of Exceptional Conditions



Review the following best practices for A04: Cryptographic Failures:

  * [Configure and assign custom SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies) to your load balancer's frontend to restrict negotiations to TLS 1.3 or secure TLS 1.2 profiles and disable weak cipher suites.



Review the following best practices for A10: Mishandling of Exceptional Conditions:

  * Configure your external Application Load Balancer with [custom error response pages](https://docs.cloud.google.com/load-balancing/docs/https/custom-error-response) to intercept backend failure codes and serve standardized HTML or JSON error responses.
  * Deploy [multi-region backend services with cross-region failover](https://docs.cloud.google.com/load-balancing/docs/https/applb-failover-overview) so that traffic can reroute to secondary regions if outages or unhandled system crashes occur.



### Google Cloud Observability (Logging, Monitoring, and Error Reporting)

[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) provides full-stack log management with [Logging](https://docs.cloud.google.com/logging/docs), metrics and alerting with [Monitoring](https://docs.cloud.google.com/monitoring/docs), and real-time application crash tracking with [Error Reporting](https://docs.cloud.google.com/error-reporting/docs).

Applies to the following:

  * A09: Security Logging & Alerting Failures
  * A10: Mishandling of Exceptional Conditions



Review the following best practices for A09: Security Logging & Alerting Failures:

  * Enable [Data Access logs](https://docs.cloud.google.com/logging/docs/audit#data-access) for high-value data repositories (such as Cloud Storage, BigQuery, and Spanner) that store sensitive data. Data Access logs let you audit each read, write, and query event for sensitive data.
  * Enforce [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock) and retention policies for the custom Logging bucket to help prevent attackers or unauthorized administrators from deleting logs to cover their tracks.
  * Use [aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview) to collate and route log entries into a single central repository for your SecOps teams. Configure intercepting aggregated sinks to avoid storing high-volume logs like Data Access logs in more than one place.
  * Configure [log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) for critical indicators of compromise, such as Permission Denied IAM errors, unexpected API key creations, or sudden firewall configuration changes.
  * Deploy [log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) in Logs Explorer or Monitoring. Specify exact filters that target high-severity events, such as unauthorized IAM policy modifications or KMS key revocations, so an incident notification is generated when a matching log entry is ingested.
  * Build [log-based counter metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics) in Logging to convert matching log entries into time-series data. Then, build a metric-based alerting policy in Monitoring that starts an incident when the rate exceeds a specific threshold (for example, greater than 50 failed login attempts in five minutes).
  * Configure log-based alerting policies that monitor administrative calls to the Cloud Logging API and alert on unexpected log export sink modifications or bucket deletions.
  * Configure notification channels with clear documentation templates. Include direct deep-links to the [Logs Explorer query](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), standard operating procedures (SOPs) for the on-call engineer, and explicit remediation steps to help enable swift incident containment.



Review the following best practices for A10: Mishandling of Exceptional Conditions:

  * Integrate [Error Reporting SDKs](https://docs.cloud.google.com/error-reporting/docs/setup) directly into your application code or configure Logging to parse structured JSON exception formats.
  * Configure [Error Reporting notification channels](https://docs.cloud.google.com/error-reporting/docs/notifications) or Monitoring alerting policies to notify your SecOps teams when a new exception class appears.



### Cloud NGFW

[Cloud NGFW](https://docs.cloud.google.com/firewall/docs/about-firewalls) is a managed firewall service that enables stateful inspection and Layer 7 application control for north-south traffic and east-west traffic.

Applies to the following:

  * A01: Broken Access Control
  * A05: Injection



Review the following best practices for A01: Broken Access Control:

  * Enforce [network micro-segmentation using global network firewall policies](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/ccn-ncc-vpn-ra#configure-ngfw-policies) and IAM-governed resource tags to isolate backend application tiers and restrict east-west communication between subnets.
  * Use Google-maintained [threat intelligence lists](https://docs.cloud.google.com/firewall/docs/ngfw_tiers#ngfw-tiers-standard) in firewall rules to block inbound connections that originate from known malicious actors, C2 servers, and compromised botnets.



Review the following best practices for A05: Injection:

  * Configure the [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention) with a security profile group that denies threats that match SQL injection, OS command injection, and remote code execution exploit signatures.
  * Configure [Cloud NGFW TLS inspection](https://docs.cloud.google.com/firewall/docs/about-tls-inspection) to decrypt inbound and outbound HTTPS traffic, apply IPS injection signature checks to the plaintext payload, and re-encrypt the session before delivery to the backend.
  * Enforce [FQDN-based egress firewall rules](https://docs.cloud.google.com/firewall/docs/quickstarts/configure-nwfwpolicy-fqdn-egress) on backend databases and Compute subnets. Restrict outbound connections to approved, predefined external domains to help prevent vulnerable applications from creating unauthorized reverse shells.
  * Enable [firewall rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview) on [threat prevention profiles](https://docs.cloud.google.com/firewall/docs/configure-security-profiles) and route these logs into Google SecOps to correlate blocked network injection signatures with host-level telemetry, identifying targeted workloads for priority patching.



### Cloud Workstations

[Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) provides managed development environments on Google Cloud with built-in security and customizations.

Applies to the following:

  * A03: Software Supply Chain Failures
  * A04: Cryptographic Failures



Review the following best practices for A03: Software Supply Chain Failures:

  * Create [custom base container images](https://docs.cloud.google.com/workstations/docs/customize-container-images) stored in Artifact Registry that pre-install security tools, trusted developer extensions, and approved language runtimes.
  * Deploy your [workstation clusters](https://docs.cloud.google.com/workstations/docs/create-cluster) with private IP ingress and egress and inside a VPC Service Controls perimeter.
  * Configure Cloud Workstations to [route session traffic through IAP](https://docs.cloud.google.com/workstations/docs/enable-iap). Require developers to authenticate using corporate credentials with multi-factor authentication (MFA) enabled and enforce least-privilege roles (for example, [Cloud Workstations User (`roles/workstations.user`)](https://docs.cloud.google.com/workstations/docs/access-control#workstations-user)).
  * Configure [workstation configurations](https://docs.cloud.google.com/workstations/docs/overview#configuration_updates) with low timeout limits (for example, auto-stopping after two hours of inactivity). When a workstation restarts, Cloud Workstations pulls the latest security-patched container image, so that developers can work in a clean environment.



Review the following best practices for A04: Cryptographic Failures:

  * Configure your workstation configurations to [encrypt attached persistent disks using CMEK](https://docs.cloud.google.com/workstations/docs/encrypt-workstation-resources-using-cmek).



### CodeMender

[CodeMender](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/) is a specialized, autonomous AI engineering agent. CodeMender can patch newly discovered vulnerabilities and rewrite existing legacy code to address existing vulnerabilities. You can [install and configure CodeMender](https://docs.cloud.google.com/gemini-enterprise-agent-platform/codemender/set-up-environment) in Gemini Enterprise Agent Platform.

Applies to the following:

  * A03: Software Supply Chain Failures
  * A05: Injection
  * A06: Insecure Design



Review the following best practices for A03: Software Supply Chain Failures:

  * Integrate the [CodeMender CLI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/codemender/set-up-environment) into local developer workspaces and CI/CD pipelines to scan targeted modules, verify exploitability, and catch security weaknesses before code is committed.
  * Import [Software Composition Analysis (SCA) and dependency vulnerability reports](https://docs.cloud.google.com/gemini-enterprise-agent-platform/codemender/import-findings) into CodeMender to run proof-of-concept exploit verifications, filtering out false positives before developer review.



Review the following best practices for A05: Injection:

  * Run [automated patch generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/codemender/fix-and-patch) inside isolated local sandboxes to rewrite vulnerable logic (such as sanitizing inputs). Verify that unit tests pass and PoCs are no longer exploitable before creating pull requests.



Review the following best practices for A06: Insecure Design:

  * Refactor legacy or insecure architectural code logic using CodeMender's iterative patch engine, providing explicit coding constraints to enforce secure design patterns across application modules.
  * Maintain [human-in-the-loop review](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) for CodeMender-generated pull requests and diffs to verify that proposed changes align with your secure coding guidelines.



### Confidential Computing

[Confidential Computing](https://cloud.google.com/confidential-computing) helps protect data in use by keeping the data encrypted in memory while the data is being processed. Using hardware-based Trusted Execution Environments (TEEs), Confidential Computing helps ensure that your sensitive data and cryptographic keys cannot be accessed by the hypervisor, the host operating system, or infrastructure administrators.

Applies to A04: Cryptographic Failures.

Review the following best practices:

  * Use [Confidential VMs](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) or [Confidential Google Kubernetes Engine Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes) for highly sensitive workloads (like PII, financial records, or proprietary AI model weights).
  * When multiple organizations must pool sensitive data for analysis or AI training (without exposing the raw data to each other), use [ Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview) to enforce cryptographic attestation and data isolation.



### Firebase (Firebase Authentication, Firebase App Check, and Firebase Security Rules)

[Firebase](https://firebase.google.com/docs) provides developer-focused security controls across identity, client attestation, and database access. [Firebase Authentication](https://firebase.google.com/docs/auth) handles user identity and session management, [App Check](https://firebase.google.com/docs/app-check) validates client app integrity, and [Firebase Security Rules](https://firebase.google.com/docs/rules) enforce attribute-based access control and schema validation for Firestore and Cloud Storage.

Applies to the following:

  * A01: Broken Access Control
  * A05: Injection
  * A07: Authentication Failures
  * A08: Software or Data Integrity Failures



Review the following best practices for A01: Broken Access Control:

  * [Scope reads and writes](https://firebase.google.com/docs/rules/insecure-rules#open_access) to the authenticated user's ID in Firebase Security Rules. Never use permissive default rules like `allow read, write: if true;`.
  * For administrative roles, use Firebase Admin SDKs to set [custom claims](https://firebase.google.com/docs/auth/admin/custom-claims) on users' ID tokens, and validate those claims in your security rules rather than allowing client-side profile writes.
  * [Enforce App Check](https://firebase.google.com/docs/app-check/enable-enforcement) in Firebase Security Rules to block unauthenticated or spoofed client access at the database layer.



Review the following best practices for A05: Injection:

  * Enforce [structural payload validation](https://firebase.google.com/docs/firestore/security/rules-conditions) in Security Rules by checking incoming document field types, string lengths, and object sizes to reject malformed or malicious write payloads before database ingestion.



Review the following best practices for A07: Authentication Failures:

  * Upgrade to Firebase Authentication with Identity Platform to enable enterprise protections such as [MFA with TOTP](https://firebase.google.com/docs/auth/web/totp-mfa) and [blocking functions](https://firebase.google.com/docs/auth/extend-with-blocking-functions).
  * Verify [Firebase ID tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) on your backend using the Firebase Admin SDK before granting access to sensitive application data.
  * Use the [debug provider](https://firebase.google.com/docs/app-check/web/debug-provider) to generate temporary, scoped debug tokens for your developers and CI/CD pipelines in staging environments.



Review the following best practices for A08: Software or Data Integrity Failures:

  * Enforce hardware-backed attestation providers to verify client integrity. Configure App Check to use [Android Play Integrity](https://firebase.google.com/docs/app-check/android/play-integrity-provider) and [Apple App Attest](https://firebase.google.com/docs/app-check/ios/app-attest-provider).
  * Deploy [App Check token verification middleware](https://firebase.google.com/docs/app-check/custom-resource-backend) on Cloud Run and Kubernetes Engine API backends to reject requests that originate from scraped API keys, automated scripts, or emulated environments.



### Fraud Defense

[Fraud Defense](https://cloud.google.com/security/products/fraud-defense) is a unified platform for fraud and abuse defense, including bot, account, and transaction protection for the web. [reCAPTCHA](https://cloud.google.com/security/products/recaptcha), an offering that's part of Fraud Defense, filters for bots and other forms of automation and bulk traffic by scoring the risk level of access attempts.

Applies to A07: Authentication Failures.

Review the following best practices:

  * [Integrate reCAPTCHA with your existing WAF](https://docs.cloud.google.com/recaptcha/docs/waf-overview), such as Google Cloud Armor, to issue automated challenges or block high-risk bot traffic before requests reach authentication endpoints.
  * [Defend accounts](https://docs.cloud.google.com/recaptcha/docs/account-takeovers) on login, password reset, and session renewal endpoints. Obtain account takeover (ATO) risk scores based on user sign-in velocities and device fingerprints.
  * [Defend against SMS toll fraud](https://docs.cloud.google.com/recaptcha/docs/sms-fraud-detection) on registration and 2FA forms by evaluating phone number risk profiles before sending outbound SMS messages.
  * To reduce false positives and train site-specific risk assessment models, regularly [annotate and send transaction feedback](https://docs.cloud.google.com/recaptcha/docs/samples/recaptcha-enterprise-annotate-assessment).
  * [Check passwords](https://docs.cloud.google.com/recaptcha/docs/check-passwords) during user sign-in and account creation flows to detect whether submitted credentials appear in third-party data breach databases across the web.



### Google SecOps

[Google Security Operations](https://cloud.google.com/security/products/security-operations) is a security operations platform that combines security telemetry analysis (SIEM), security orchestration, automation, and response (SOAR), and frontline Mandiant threat intelligence into a single platform.

Applies to the following:

  * A02: Security Misconfiguration
  * A09: Security Logging & Alerting Failures



Review the following best practices for A02: Security Misconfiguration:

  * Ingest findings from Security Command Center into Google SecOps to combine static misconfiguration findings (for example, `PUBLIC_BUCKET_ACL` or `CMEK_DISABLED`) with live network and firewall telemetry.
  * Build [automated SOAR response playbooks](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-overview) to run containment actions.
  * Use [Gemini](https://docs.cloud.google.com/chronicle/docs/secops/gemini-secops) to accelerate misconfiguration triage and to receive synthesized summaries of misconfigured assets, attached IAM roles, and step-by-step remediation guidance.



Review the following best practices for A09: Security Logging & Alerting Failures:

  * Normalize log telemetry to [unified data model (UDM)](https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview) to enable fast, standardized multi-cloud searching and correlation without the overhead of raw log parsing.
  * Write [YARA-L 2.0 detection rules](https://docs.cloud.google.com/chronicle/docs/yara-l/yara-l-2-0-examples) to monitor for high-risk configuration changes such as disabling of OS Login, deletion of Logging sinks, or modifications to VPC Service Controls perimeters.
  * Use [Applied Threat Intelligence curated detections](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections) to evaluate your event data against Mandiant Threat Intelligence data.
  * Use Gemini in Google SecOps to generate YARA-L detection rules from natural language descriptions and summarize complex, multi-stage incident timelines into executive incident summaries.



### Identity-Aware Proxy

[IAP](https://docs.cloud.google.com/iap/docs/concepts-overview) creates a central authorization layer for applications that are accessed by HTTPS and administrative TCP connections. IAP verifies user identity and context before granting access to Cloud Run, App Engine, Compute Engine, GKE, and on-premises resources.

Applies to the following:

  * A01: Broken Access Control
  * A07: Authentication Failures



Review the following best practices for A01: Broken Access Control:

  * Enforce [granular access controls](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto) to web applications, VMs, Google Cloud APIs, and Google Workspace applications based on a user's identity, group membership, and the context of the request.
  * [Integrate with Agent Gateway](https://docs.cloud.google.com/iap/docs/agent-overview) to enforce access controls for your agent identities.
  * Use [IAP TCP Forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) to establish encrypted HTTPS tunnels to your backend instances and remove internet-facing SSH (port `22`) and RDP (port `3389`) endpoints.



Review the following best practices for A07: Authentication Failures:

  * Authenticate users accessing administrative interfaces and web applications through IAP using identities provisioned in [IAM](https://docs.cloud.google.com/iam/docs/overview) or [Cloud Identity](https://cloud.google.com/identity).
  * [Verify the signed JWT assertion](https://docs.cloud.google.com/iap/docs/signed-headers-howto) inside the `x-goog-iap-jwt-assertion` header at the application layer. Validate the signature against Google's public keys and verify that the audience (`aud`) claim matches your backend service ID.
  * To help prevent attackers from bypassing IAP authentication, configure [Cloud Run ingress settings](https://docs.cloud.google.com/run/docs/securing/ingress) to allow internal and Cloud Load Balancing traffic only, blocking direct public access to your backend container URLs. For VMs or GKE nodes, configure [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) to only accept ingress traffic originating from the load balancer's IP ranges.



### Identity and Access Management

[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) lets you manage fine-grained access to services and resources in Google Cloud. IAM includes features such as the following:

  * [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview), which manages on-demand, temporary privilege elevation for sensitive Google Cloud resources
  * [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), lets workloads access to Google Cloud resources by using a federated identity.
  * [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), which lets users access Google Cloud resources using a federated identity.



Applies to the following:

  * A01: Broken Access Control
  * A07: Authentication Failures



Review the following best practices for A01: Broken Access Control:

  * Use predefined roles or custom roles (not [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic)) to restrict permissions to specific resource or user needs.
  * Restrict permissions to grant the Service Account User (`roles/iam.serviceAccountUser`) and Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) roles.
  * Use [IAM Recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) to analyze your organization's active usage logs and remove over-privileged accounts.
  * Write [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) in your role bindings to add context-aware authorization and restrict access by date, time of day, or originating IP address.
  * Deploy [Principal Access Boundary (PAB) policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies) to define the organizations, folders, or projects that a principal set can access. If an attacker steals an active session or a service account is accidentally granted broad IAM roles, PAB blocks access if the specified resource is outside the identity's designated boundary.
  * Attach [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) at the organization or folder level to block high-risk permissions (such as `iam.serviceAccountKeys.create` or `resourcemanager.projects.delete`).
  * When configuring IAM deny rules, declare a dedicated breakglass security group in the `exceptionPrincipals` list. Use [resource tags in your denial conditions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags) (such as `resource.matchTag('env', 'prod')`) so that destructive actions are blocked on production resources while allowing developers operational flexibility in development sandbox projects.



Review the following best practices for A07: Authentication Failures that apply to Privileged Access Manager:

  * Convert critical administrative roles (such as Owner (`roles/owner`), Organization Administrator (`roles/resourcemanager.organizationAdmin`), and Security Admin (`roles/iam.securityAdmin`)) from static IAM bindings into [Privileged Access Manager entitlements](https://docs.cloud.google.com/iam/docs/pam-overview). Configure these entitlements to require an operational justification before elevation is granted.
  * For production environments, [configure Privileged Access Manager entitlement policies](https://docs.cloud.google.com/iam/docs/pam-create-entitlements) with mandatory approvers such as a central SecOps group or team leads.
  * Configure the maximum duration on Privileged Access Manager entitlements to the shortest realistic operational window (for example, two hours for standard maintenance, 30 minutes for breakglass actions). After the timer expires, Google Cloud removes the temporary IAM role binding.
  * Manage Terraform infrastructure using non-authoritative IAM resources (for example, `google_project_iam_member` or `google_folder_iam_member` rather than `google_project_iam_policy` or `google_project_iam_binding`). This practice avoids overwriting your Terraform pipelines or desynchronizing temporary Privileged Access Manager role bindings while an administrator is actively remediating an incident.
  * [Enable Cloud Audit Logs on Privileged Access Manager](https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-pam) to record entitlement actions and expiration events. Ingest these logs into Google SecOps to alert on suspicious elevation patterns, such as multiple off-hour elevation requests or repeated requests from unexpected geolocations.



Review the following best practices for A07: Authentication Failures that apply to Workforce Identity Federation:

  * [Deploy workforce identity pools](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers) using SAML 2.0 or OpenID Connect (OIDC) to federate external identity providers with Google Cloud.
  * Configure the [session duration](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#create-workforce-pool) on your workforce identity pool to limit the lifespan of federated user tokens.
  * Enforce [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) on workforce identity providers to mitigate multi-tenant IdP token forgery or cross-organization impersonation.
  * Map external group memberships to assign IAM roles to federated group principal sets (for example, `principalSet://iam.googleapis.com/.../attribute.group/security-engineers`).



Review the following best practices for A07: Authentication Failures that apply to Workload Identity Federation:

  * [Create workload identity pools and providers](https://docs.cloud.google.com/iam/docs/manage-workload-identity-pools-providers) for external workloads. Use short-lived OIDC tokens, exchanging them dynamically using Security Token Service for temporary access tokens that expire in minutes.
  * Enforce [attribute conditions](https://docs.cloud.google.com/iam/docs/workload-identity-federation#conditions) on workload identity providers so that external multi-tenant platforms cannot authenticate to your pool from unauthorized repositories or accounts.
  * Bind IAM roles directly to specific principal sets that are filtered by custom mapped attributes.
  * When configuring workload access, grant IAM roles directly to the federated `principalSet://` identifier on the target resource.
  * To enforce Workload Identity Federation, set the [`constraints/iam.disableServiceAccountKeyCreation` constraint](https://docs.cloud.google.com/organization-policy/restrict-service-accounts) on your organization.



### Identity Platform

[Identity Platform](https://cloud.google.com/security/products/identity-platform) is the customer identity and access management (CIAM) platform for Google Cloud customers. Identity Platform provides authentication with multi-protocol support by using SDKs and APIs. Identity Platform supports MFA, integration with third-party authentication services, and auditable activity tracking.

Applies to A07: Authentication Failures.

Review the following best practices:

  * Enable [MFA](https://docs.cloud.google.com/identity-platform/docs/how-to) across your user base. Prioritize phishing-resistant methods, such as TOTP (authenticator apps) or WebAuthn (biometrics and security keys).
  * Deploy [blocking Cloud Run functions](https://docs.cloud.google.com/identity-platform/docs/blocking-functions) using `beforeCreate` and `beforeSignIn` triggers to run custom security code before a user is saved or issued a token. This practice lets you block disposable email domains, restrict IP addresses, or mandate email verification.
  * Integrate with [reCAPTCHA Enterprise](https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise) to assess sign-in, sign-up, and password reset requests for bot traffic, credential stuffing attempts, and automated abuse.
  * Configure [password policies](https://docs.cloud.google.com/identity-platform/docs/password-policy) to enforce minimum character lengths, require specific character complexities (such as numbers and symbols), and block predictable sequences.
  * If using phone-based MFA, configure [SMS regions](https://docs.cloud.google.com/identity-platform/docs/admin/sms-regions) and enable [reCAPTCHA SMS defense](https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp) to limit verification messages to the country codes where your target users reside.



### Mandiant AI Security Consulting Solutions

[Mandiant AI Security Consulting Solutions](https://cloud.google.com/security/solutions/mandiant-ai-consulting) can evaluate your proposed software architectures, business processes, and cloud deployments early in the development lifecycle. By applying frontline threat intelligence to your system design, Mandiant consultants help expose hidden logical flaws, missing trust boundaries, and architectural risks before a single line of code is written.

Applies to A06: Insecure Design.

Review the following best practices:

  * Engage Mandiant consultants before development begins to complete architecture workshops and implement security controls from the beginning.
  * Collaborate with threat modeling experts to map out your application's data flow diagrams. Define where sensitive data crosses trust boundaries to identify where strict authentication, encryption, and validation controls must be enforced.
  * Use structured threat modeling frameworks (such as [STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)) during your architecture workshops. Mandiant consultants can help prioritize discovered design flaws based on real-world exploitability and business impact.
  * Establish secure AI governance baselines for agentic workflows and LLM deployments, defining clear trust boundaries between AI agents, MCP servers, and enterprise backend data sources.



### Model Armor

[Model Armor](https://docs.cloud.google.com/model-armor/overview) is designed to screen LLM prompts, responses, and MCP tool calls. Model Armor inspects generative AI payloads to help detect and block prompt injection, jailbreak attempts, malicious URLs, toxic content, and sensitive data leakage.

Applies to the following:

  * A05: Injection
  * A10: Mishandling of Exceptional Conditions



Review the following best practices for A05: Injection:

  * Deploy Model Armor policies inline at the API gateway layer using [Apigee integration](https://cloud.google.com/blog/products/identity-security/how-model-armor-can-help-protect-your-ai-apps) or Agent Gateway to screen incoming prompts and outgoing model responses before traffic reaches inference engines or tool runtimes.
  * [Configure floor settings](https://docs.cloud.google.com/security-command-center/docs/model-armor) at the organization or folder level to create mandatory baseline security guardrails that individual project teams cannot bypass.
  * Build customized [Model Armor templates](https://docs.cloud.google.com/model-armor/overview) with tuned confidence thresholds (for example, `LOW_AND_ABOVE` or `MEDIUM_AND_ABOVE`) for prompt injection and jailbreak detection on public endpoints.
  * Enable malicious URL detection and PDF and file scanning in your Model Armor template to check embedded URLs against Google's threat intelligence databases. Drop prompts that contain malware or phishing vectors before execution.
  * Enable [Sensitive Data Protection in your Model Armor template](https://docs.cloud.google.com/model-armor/sanitize-prompts-responses#basic_sdp_configuration) to inspect model egress traffic. Configure automated de-identification or masking to replace detected sensitive data with placeholders before the response leaves the boundary.



Review the following best practices for A10: Mishandling of Exceptional Conditions:

  * Configure your application code to intercept `MATCH_FOUND` verdicts and return a generic response, so that the system doesn't default to executing the prompt or exposing raw exception traces.
  * Implement a fail-closed (fail-secure) architecture in your application code to reject incoming generative AI prompts if Model Armor API calls encounter network timeouts, rate limits, or unhandled HTTP 5xx errors.



### Organization Policy

The [Organization Policy](https://docs.cloud.google.com/organization-policy/overview) gives you centralized and programmatic control over your organization's Google Cloud resources.

Applies to the following:

  * A01: Broken Access Control
  * A02: Security Misconfiguration
  * A04: Cryptographic Failures



Review the following best practices for A01: Broken Access Control:

  * Enforce [`constraints/storage.publicAccessPrevention`](https://docs.cloud.google.com/storage/docs/public-access-prevention) to override bucket-level IAM policies or ACLs that attempt to grant access to `allUsers` or `allAuthenticatedUsers`.
  * Apply [`constraints/iam.allowedPolicyMemberDomains`](https://docs.cloud.google.com/organization-policy/restrict-domains) to restrict IAM policy bindings strictly to your verified Google Workspace or Cloud Identity customer IDs.
  * Enforce [`constraints/iam.disableServiceAccountKeyCreation`](https://docs.cloud.google.com/organization-policy/restrict-service-accounts) across production folders to help prevent users from downloading service account keys, forcing engineering teams to adopt short-lived alternatives like Workload Identity Federation.
  * Enforce [`constraints/iam.automaticIamGrantsForDefaultServiceAccounts`](https://docs.cloud.google.com/organization-policy/restrict-service-accounts) so that Google Cloud doesn't automatically grant the permissive Editor (`roles/editor`) role to default service accounts.
  * For requirements not covered by predefined constraints, deploy [custom constraints](https://docs.cloud.google.com/organization-policy/overview#custom-constraints) to enforce fine-grained resource configurations. Consider restricting VM creation only to approved machine families, limiting persistent disk provisioning sizes, or mandating specific network firewall tag configurations.



Review the following best practices for A02: Security Misconfiguration:

  * Use [`constraints/compute.requireShieldedVm`](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) to require Shielded VM, helping to protect VMs against kernel rootkits, bootkits, and firmware tampering.
  * Enforce [`constraints/compute.requireOsLogin`](https://docs.cloud.google.com/compute/docs/oslogin/manage-oslogin-in-an-org#set-org-policy) to require Linux instances to use OS Login, which links SSH access directly to the user's IAM identities and 2SV.
  * Enforce [`constraints/compute.disableSerialPortAccess`](https://docs.cloud.google.com/compute/docs/access/organization-policies#managed_constraints_legacy) to block interactive serial console connections across projects.
  * Enforce [`constraints/compute.skipDefaultNetworkCreation`](https://docs.cloud.google.com/compute/docs/access/organization-policies#managed_constraints_legacy) so that the default VPC network isn't created, forcing teams to build custom VPCs with dedicated subnets and strict firewall policies.
  * Enforce [`constraints/sql.restrictPublicIp`](https://docs.cloud.google.com/sql/docs/mysql/recommender-disable-public-ip) so that Cloud SQL instances only receive private RFC 1918 internal IP addresses, and use [`constraints/compute.vmExternalIpAccess`](https://docs.cloud.google.com/compute/docs/access/managed-constraints#available_managed_constraints) to restrict public IPv4 addresses on VMs.
  * Apply [`constraints/gcp.resourceLocations`](https://docs.cloud.google.com/organization-policy/restrict-locations) to restrict resource creation to authorized Google Cloud regions.



Review the following best practices for A04: Cryptographic Failures:

  * To mandate CMEK, apply [`constraints/gcp.restrictNonCmekServices`](https://docs.cloud.google.com/kms/docs/cmek-org-policy) at the organization or top-level folder, set the policy type to `Deny` and list supported Google Cloud services. Before enforcing the constraint, verify that the service agent for each target service exists and is granted the Cloud KMS CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the relevant key rings.
  * Enforce `constraints/gcp.restrictCmekCryptoKeyProjects` to restrict key selection to dedicated Cloud KMS projects.



### Secret Manager

[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) lets applications and pipelines access the values of named secrets based on permissions granted with IAM. When enabled, interactions with Secret Manager create an audit trail that you can use to assist with forensics and compliance needs.

Applies to the following:

  * A04: Cryptographic Failures
  * A07: Authentication Failures



Review the following best practices for A04: Cryptographic Failures:

  * [Encrypt high-value secrets using CMEK](https://docs.cloud.google.com/secret-manager/docs/cmek) to control, rotate, or revoke the primary encryption keys that wrap your secret payloads.
  * [Use data integrity checksums](https://docs.cloud.google.com/secret-manager/docs/data-integrity) to maintain and verify the integrity of your secret's data when [adding](https://docs.cloud.google.com/secret-manager/docs/add-secret-version) and [accessing](https://docs.cloud.google.com/secret-manager/docs/access-secret-version) secret versions.
  * [Replicate secrets across multiple regions](https://docs.cloud.google.com/secret-manager/docs/choosing-replication) for high availability and disaster recovery across geographic deployment zones.



Review the following best practices for A07: Authentication Failures:

  * Remove sensitive values such as API keys from source code, `.env` files, and container build configurations and store the credentials in Secret Manager. Fetch decrypted values at runtime using [Google Cloud client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries), GKE Secret Store CSI drivers, or Cloud Run secret bindings.
  * Apply IAM policy bindings directly to specific individual secrets, granting microservices the Secret Manager Secret Accessor (`roles/secretmanager.secretAccessor`) role only on the specific secrets that they require.
  * Configure [automated rotation schedules](https://docs.cloud.google.com/secret-manager/docs/secret-rotation) on Secret Manager. When a rotation interval starts, Secret Manager publishes a `SECRET_ROTATE` notification to a designated Pub/Sub topic. Configure a Cloud Run functions or Cloud Run service to read the notification, generate a new secret value, add the new version to Secret Manager, and destroy the retired version.
  * Enable [Cloud Audit Logs on Secret Manager](https://docs.cloud.google.com/secret-manager/docs/audit-logging) to track secret version creation, destruction, and payload access events. Route these logs to Google SecOps to alert on suspicious access events, such as a compromised service account accessing secrets outside standard operational hours or attempting to read unapproved secret resources.



### Security Command Center Premium

[Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) lets you find and address security misconfigurations and active runtime threats, including identification and authentication failures, in your Google Cloud environment and web applications. The [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) service can monitor for application vulnerabilities, including XML external entity (XXE) vulnerabilities, with scans [designed to cover the OWASP Top 10 controls](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview#scan_findings).

Applies to the following:

  * A02: Security Misconfiguration
  * A05: Injection
  * A07: Authentication Failures
  * A08: Software or Data Integrity Failures



Review the following best practices for A02: Security Misconfiguration:

  * [Apply built-in frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) (such as the CIS Benchmarks or NIST) using Compliance Manager to assess your cloud configurations against regulatory security frameworks and industry benchmarks.
  * Enable [Cloud Infrastructure Entitlement Management](https://docs.cloud.google.com/security-command-center/docs/ciem-overview) to manage the identities that have access to resources in your cloud deployments and mitigate potential vulnerabilities that result from misconfigurations.
  * Review and remediate [Web Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings) to fix misconfigured HTTP response security headers, invalid CORS origin headers, and mixed-content serving.



Review the following best practices for A05: Injection:

  * [Enable services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#built-in) such as Virtual Machine Threat Detection and Container Threat Detection. These services scan hypervisor memory and kernel events for [malicious scripts](https://docs.cloud.google.com/security-command-center/docs/findings/threats/malicious-script-executed), [reverse shells](https://docs.cloud.google.com/security-command-center/docs/findings/threats/reverse-shell), and malware installations (using the [Added Binary Executed](https://docs.cloud.google.com/security-command-center/docs/findings/threats/added-binary-executed) and [Added Library Loaded](https://docs.cloud.google.com/security-command-center/docs/findings/threats/added-library-loaded) detectors).
  * Configure Web Security Scanner to monitor running applications for [cross-site scripting (XSS)](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#xss) and [SQL injection (SQLi)](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#sql_injection) flaws.
  * [Integrate Security Command Center findings](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports) into Google SecOps or third-party SIEMs for automated triage and incident response.



Review the following best practices for A07: Authentication Failures:

  * Monitor your Logging streams to catch credential-based attacks using the [Brute Force: SSH](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ssh-brute-force) and [Persistence: IAM Anomalous Grant](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-grant) detectors.
  * Use the [Use Multifactor or Passwordless Authentication](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#use-multifactor-or-passwordless-authentication), [Set Application Restriction on API Keys](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#restrict-applications-api-keys), and [Require Rotation of API Key](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls#require-api-key-rotation) cloud controls to detect when MFA isn't being used and monitor API key usage.
  * Remediate [Session ID Leak](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#session_id_leak) findings by configuring web backends to store session tokens in HTTP cookies with `HttpOnly` and `Secure` flags.



Review the following best practices for A08: Software or Data Integrity Failures:

  * Configure Web Security Scanner to scan web endpoints for signature-based execution bugs and generate a high-severity [`STRUTS_INSECURE_DESERIALIZATION`](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#struts_insecure_deserialization) finding if an application is running a vulnerable Apache Struts version.
  * Remediate the `STRUTS_INSECURE_DESERIALIZATION` finding by upgrading the vulnerable framework library version or deploying Assured OSS to pull a Google-verified replacement.



### Sensitive Data Protection

[Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) lets you scan for any potentially sensitive data stored in buckets, databases, generative AI prompts, or streaming application payloads to help prevent unintended information leakage. If disallowed data is identified, Sensitive Data Protection can [flag or redact](https://docs.cloud.google.com/sensitive-data-protection/docs/classification-redaction) it.

Applies to the following:

  * A04: Cryptographic Failures
  * A09: Security Logging & Alerting Failures



Review the following best practices for A04: Cryptographic Failures:

  * Enable [sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-profiles) to continuously scan your storage and database assets, generate data profiles, and report metrics for audit reports.
  * Use format-preserving encryption, cryptographic hashing, or key-based tokenization to [de-identify sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify).
  * Deploy reusable, centrally managed [de-identification templates](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-deid) to enforce consistent cryptographic masking and inspection policies across development teams.
  * [Analyze prompt payloads](https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-vertex-ai) to help prevent sensitive corporate data or PII from leaking into generative AI training pipelines.



Review the following best practices for A09: Security Logging & Alerting Failures:

  * Configure your Logging sink to send application logs to a Pub/Sub topic. Attach a Cloud Run subscriber that uses the [Sensitive Data Protection API](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data) to scan and de-identify the log payload before writing clean logs to your final Logging bucket.
  * Use [exclusion filters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exclude-logs) in your Logging sinks to route only high-risk, unstructured logs (such as raw application errors, user registration payloads, and transaction logs) through the sanitization pipeline.



### VirusTotal

The [VirusTotal API](https://www.virustotal.com/gui/home/upload) is a threat intelligence and file-scanning platform that analyzes suspicious files, URLs, domains, and IP addresses to detect malware, trojans, and malicious payloads. Integrating the VirusTotal API into file ingestion pipelines lets you scan untrusted uploads before files are processed by application systems.

Applies to the following:

  * A08: Software or Data Integrity Failures
  * A05: Injection



Review the following best practices for A08: Software or Data Integrity Failures:

  * Deploy custom [YARA-X signature-matching rules](https://virustotal.github.io/yara/) to scan incoming file structures for known malicious binary and textual patterns, enabling detection of mutated malware variants.



Review the following best practices for A05: Injection:

  * Use the [VirusTotal Private Scanning module](https://docs.virustotal.com/docs/private-scanning) to scan sensitive uploads in isolation and not share uploaded files with third parties.
  * Implement API rate-limiting and exception handling in your ingestion code to catch HTTP `429 Too Many Requests` status codes.



### VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) lets you create perimeters around your Google Cloud resources to help prevent data exfiltration and mitigate Server-Side Request Forgery (SSRF) attacks. VPC Service Controls denies API calls that cross perimeter boundaries unless explicitly permitted by ingress and egress rules.

Applies to the following:

  * A01: Broken Access Control
  * A02: Security Misconfiguration



Review the following best practices for A01: Broken Access Control:

  * Include critical services (such as Cloud Storage, BigQuery, Spanner, and Agent Platform) in a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to restrict API access to authorized VPC networks and trusted identities.
  * Configure [egress perimeter rules](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls) on serverless resources to block unauthorized data exfiltration that's caused by outbound API calls to external, non-perimeter destinations.
  * Restrict cross-perimeter and cross-organization API access using explicit ingress and egress rules that specify approved project sources, target APIs, and caller identities.



Review the following best practices for A02: Security Misconfiguration:

  * Group projects into dedicated perimeters that are organized by environment security tier (for example, a production perimeter). Use [VPC-accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) to restrict which internal Google APIs can be invoked inside the perimeter.
  * Route outbound API requests from serverless workloads through the VPC network. Configure Cloud Run services and Cloud Run functions to use direct VPC egress or a Serverless VPC Access Connector with ingress set strictly to internal-only.
  * Bind [Access Context Manager access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) to your perimeter ingress rules that evaluate a combination of corporate IP subnets, authenticated identity claims, and Endpoint Verification device health signals.
  * Maintain a pre-approved breakglass administrative process for emergency incident response, and set up [Monitoring alerts](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging) on any unexpected perimeter violation events.



## Wiz services

The following sections describe OWASP Top 10 best practices for [Wiz](https://www.wiz.io/) services that integrate with Google Cloud.

### Wiz Code

[Wiz Code](https://www.wiz.io/platform/wiz-code) extends cloud security into developer workflows and CI/CD pipelines. Wiz Code correlates code-to-cloud telemetry, scans Infrastructure as Code (IaC), analyzes dependencies (SCA), detects exposed credentials, and performs static application security testing (SAST).

Applies to the following:

  * A03: Software Supply Chain Failures
  * A05: Injection
  * A07: Authentication Failures



Review the following best practices for A03: Software Supply Chain Failures:

  * Integrate the Wiz CLI into CI/CD pipelines to block pull requests from merging if they introduce critical CVEs, exposed secrets, or severe IaC misconfigurations into protected branches.
  * Generate and export a SBOM for every build to maintain continuous supply chain visibility in Wiz Cloud.
  * Deploy Wiz Code IDE extensions to provide real-time developer feedback, catching vulnerable packages, hardcoded API keys, and syntax errors before code commit.
  * Integrate Wiz Code with CodeMender in CI/CD pipelines to generate, test, and submit pull requests when vulnerable third-party dependencies are detected.



Review the following best practices for A05: Injection:

  * Block pull requests from merging if the SAST scanner detects untrusted user input flowing into database queries or OS commands without proper sanitization.
  * Integrate the Wiz Code plugin into developer IDEs to provide real-time alerts if developers type unsafe, concatenating SQL query or command execution patterns.
  * When Wiz Code flags an injection flaw, route data-flow traces to CodeMender to draft a verified remediation patch.



Review the following best practices for A07: Authentication Failures:

  * Implement automated secret scanning on developer IDEs, local pre-commit hooks, and in CI/CD pipelines to catch exposed credentials.
  * To mitigate credential theft, replace static, long-lived credentials with dynamic, short-lived tokens and identity-bound access (such as [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) or OIDC-based authentication).
  * Implement an automated incident response playbook to remove detected secrets from code, environment variables, and build logs.



### Wiz Cloud

[Wiz Cloud](https://www.wiz.io/platform) analyzes multi-cloud environments to identify security misconfigurations, sensitive data exposures, and identity risks. Using the [Wiz Security Graph](https://www.wiz.io/lp/wiz-security-graph), Wiz Cloud correlates risk factors across infrastructure layers to highlight critical attack paths.

Applies to the following:

  * A01: Broken Access Control
  * A02: Security Misconfiguration
  * A04: Cryptographic Failures
  * A06: Insecure Design



Review the following best practices for A01: Broken Access Control:

  * Trace and flag complex, multi-hop privilege escalation paths across IAM roles and policies to identify where attackers could move laterally or elevate privileges.
  * Map active access permissions across user accounts, service accounts, and AI agents to critical data stores, and revoke over-privileged entitlements.
  * Integrate identity entitlement findings with orchestration platforms to replace permanent administrative role bindings with just-in-time (JIT) access.
  * Monitor and visualize data movement to detect when production PII is copied or synced down into insecure staging or development environments.



Review the following best practices for A02: Security Misconfiguration:

  * Assess and prioritize cloud configuration risk by correlating misconfigurations with multiple attack factors using the Wiz Security Graph.
  * Apply built-in compliance frameworks (such as OWASP Top 10, CIS Benchmarks, and NIST) to measure cloud configurations against industry standards.
  * Integrate the [Wiz CLI scanner](https://www.wiz.io/lp/wiz-cli) into CI/CD pipelines to review builds or remediate IaC misconfigurations before deployment.



Review the following best practices for A04: Cryptographic Failures:

  * Prioritize the remediation of databases and storage buckets that contain plaintext credentials, unhashed keys, or sensitive data stored without encryption.
  * Run Wiz Cloud data discovery across AI training directories, vector databases, and RAG pipelines to verify that proprietary data and PII are redacted before LLM ingestion.
  * Scan environments to identify unmanaged data assets and delete redundant data to minimize your attack surface.



Review the following best practices for A06: Insecure Design:

  * Direct Wiz Red Agent to analyze logical architectural interfaces and simulate attack paths to find insecure design flaws before production deployment.
  * Pass validated attack chain context from Wiz Red Agent to CodeMender to identify root causes and generate tested architectural pull requests.



### Wiz Defend

[Wiz Defend](https://www.wiz.io/platform/wiz-defend) provides cloud detection and response (CDR), workload runtime protection, and Kubernetes admission security. Wiz Defend monitors control plane activity, detects runtime anomalies, enforces container admission policies, and triggers automated containment.

Applies to the following:

  * A08: Software or Data Integrity Failures
  * A09: Security Logging & Alerting Failures



Review the following best practices for A08: Software or Data Integrity Failures:

  * Configure Wiz Defend admission rules to inspect and reject Kubernetes deployment manifests that attempt to run containers with root privileges, request host network namespaces, or enable `privileged: true`.
  * Configure critical security admission webhooks with [`failurePolicy: Fail` (fail-closed)](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#failure-policy) in production to block untrusted containers if the webhook is unreachable.



Review the following best practices for A09: Security Logging & Alerting Failures:

  * Export Google Cloud audit logs using a log sink to a Pub/Sub topic so that Wiz Defend can ingest and analyze control-plane activities and workload events.
  * Deploy the Wiz Runtime Sensor on GKE clusters and high-value Compute Engine VMs to detect runtime threats, in-memory exploits, and active compromises.
  * Automate containment playbooks to immediately disable compromised IAM service accounts or isolate compromised workloads.
  * Use Wiz Blue Agent to investigate runtime detections, correlating live process telemetry and identity context to determine root causes and affected assets.



## Maintain compliance with OWASP Top 10:2025

Wiz includes an [OWASP Top 10 2025 compliance framework](https://www.wiz.io/academy/compliance/cloud-compliance-fast-track-guide) that lets you assess and monitor your posture. The OWASP Top 10 2025 compliance framework maps built-in Wiz policies to the relevant OWASP risk categories and creates findings if a control is non-compliant. You can track your compliance score over time. If required, you can customize the OWASP Top 10 2025 compliance framework to meet your business requirements.

## What's next

Review the [security best practices catalog](https://docs.cloud.google.com/docs/security/security-best-practices-catalog) for additional best practices.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
