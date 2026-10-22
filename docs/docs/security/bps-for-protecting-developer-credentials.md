---
url: https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials/
title: Best practices for protecting developer credentials \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:46.175965+00:00
---

# Best practices for protecting developer credentials  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Best practices for protecting developer credentials Stay organized with collections  Save and categorize content based on your preferences. 

Learn best practices to secure developer workstations and prevent the theft and misuse of Google Cloud credentials, including Google Cloud CLI [OAuth bearer tokens](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens), Application Default Credentials, and local keys.

This document is intended for security teams or cloud architects who are responsible for securing their cloud resources from illegitimate access. Learn about the available controls that you can use to proactively reduce the impact of compromised developer credentials and remediate your environment after an endpoint has been compromised.

## The risk of compromised credentials

An attacker can compromise credentials if they gain access to an endpoint where a legitimate user account or service account has already authenticated with Google Cloud or the gcloud CLI. The attacker can then copy these tokens to another endpoint that they control to make requests that impersonate the legitimate identity. Even after you remove the attacker's access to the compromised endpoint, the attacker can continue to make authenticated API requests using the copied tokens. To help mitigate this risk, you can control access to your systems by using credentials that are short-lived and context-aware.

## Overview of developer credentials

The following Google Cloud credentials are typically found on developer workstations:

  * gcloud CLI OAuth tokens
  * Application Default Credentials
  * Service account keys
  * SSH keys
  * Browser cookies
  * Workforce Identity Federation access tokens



The following sections describe how each credential type is stored and used.

### gcloud CLI OAuth tokens

The gcloud CLI uses [OAuth 2.0 access tokens](https://oauth.net/2/access-tokens/) to authenticate requests for Google Cloud APIs. The OAuth flow varies by the credential types used, but generally the access token and other credentials are accessible locally. In each case, the access token expires after 60 minutes by default, but can last up to 12 hours under [extended lifetime constraints](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated#sa-credentials-oauth). However, other credential types might be persistent.

When you [authorize the gcloud CLI with a user account](https://docs.cloud.google.com/sdk/docs/authenticate#user-accounts), the gcloud CLI initiates a three-legged OAuth consent flow to access Google Cloud APIs on the user's behalf. After the user completes the consent flow, the gcloud CLI receives an access token and a refresh token that lets it request new access tokens. The long-lived refresh token persists until its [expiration conditions are met](https://developers.google.com/identity/protocols/oauth2#expiration).

When you [authorize the gcloud CLI with a service account](https://docs.cloud.google.com/sdk/docs/authenticate#service-accounts), the gcloud CLI initiates a two-legged OAuth flow to access Google Cloud APIs as the service account identity. After you activate a service account from a private key file, the gcloud CLI uses this key to periodically request an access token. The long-lived private key is stored in the gcloud CLI configuration and remains valid until you disable or delete the service account key.

When you run the gcloud CLI inside a Google Cloud environment, like Compute Engine or Cloud Shell, the application can automatically find credentials and [authenticate as a service account](https://docs.cloud.google.com/docs/authentication#service-accounts). For example, in Compute Engine, an application like the gcloud CLI can query the metadata server for an access token. Google manages and rotates the private signing key that is used to create the access token, and the long-lived credentials aren't exposed to the application.

### Application Default Credentials

Application Default Credentials are used by applications to authenticate with Google Cloud APIs. Developers can generate Application Default Credentials by running `gcloud auth application-default login`. This command writes a plaintext JSON file (`$HOME/.config/gcloud/application_default_credentials.json` or `%APPDATA%\gcloud\application_default_credentials.json`), which contains an OAuth 2.0 refresh token and client credentials for client libraries.

Any client library or custom script can use these credentials to call Google Cloud APIs.

Because Application Default Credentials are saved in plaintext, any untrusted process or script running in the user's context can access the file directly or use commands like `gcloud auth application-default print-access-token` to retrieve active access tokens.

Typical malware often targets the `~/.config/gcloud/` directory to harvest `application_default_credentials.json`.

For more information, see [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

### Service account keys

Service account keys are private JSON key files that are downloaded from the Google Cloud console. These keys are used by applications to authenticate with Google Cloud APIs. Service account keys can be stored in the following locations:

  * gcloud CLI configuration directory after running `gcloud auth activate-service-account`
  * The local file system
  * An internal code repository



Service account keys on developer endpoints aren't bound by 2-Step Verification, have no session limits, and don't expire automatically.

An attacker who steals a service account key can create service account access tokens to maintain persistent access.

For more information, see [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

### SSH keys

SSH keys are used to authenticate with Compute Engine instances. Developers can generate SSH keys using `gcloud compute ssh`. This command generates local private keys in `~/.ssh/google_compute_engine`. SSH keys are long-lived.

An attacker can use a stolen SSH key to access a VM and then query the metadata server to extract an attached service account token. This attack bypasses external perimeter firewalls.

Instead of using SSH keys, consider [OS Login with 2-Step Verification](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin). For more information, see Enforce 2-Step Verification for remote server access.

### Browser cookies

Browser cookies authenticate web HTTP requests to the Google Cloud console and Cloud Shell. Browser cookies are created automatically when a user signs in to the Google Cloud console.

The cookies are stored in the browser's profile directory on the local workstation. For example, Google Chrome stores cookies in `~/.config/google-chrome/` on Linux or `%LOCALAPPDATA%\Google\Chrome\User Data` on Windows.

Browser cookies are long-lived credentials that are only invalidated when a user logs out, when a session timeout occurs, or when an administrator resets the user session in the Admin console.

An attacker who steals these cookies can import them into another browser to hijack active Google Cloud console sessions, bypassing authentication.

To reduce the risk of stolen session cookies, set the session length for Google Cloud services.

### Workforce Identity Federation access tokens

Developers can use Workforce Identity Federation to authenticate through an external identity provider so that they can access Google Cloud resources.

To sign in with a federated identity, developers use a login configuration file (that's created with the `gcloud iam workforce-pools create-login-config` command) and [sign in to the gcloud CLI](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). After authentication with the external identity provider, Security Token Service exchanges the authorization code for a short-lived federated access token and an OAuth refresh token.

The gcloud CLI stores credential metadata and refresh tokens in a local credentials database, and caches active access tokens in the gcloud CLI configuration directory. Federated access tokens are short-lived credentials that expire after a set time (60 minutes by default).

An attacker who compromises an endpoint can extract active federated access tokens or use `gcloud auth print-access-token` to impersonate the workforce principal. If the workforce identity has impersonation rights, the attacker can also request service account access tokens to escalate privileges.

To reduce risk, [configure the session duration on your workforce identity pool](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update#--session-duration) to the minimum necessary duration and align the duration with your external identity provider's re-authentication and session timeout policies. For more information on how to store and manage the credentials, see [best practices for using Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation).

## Impact of compromised credentials

If an attacker manages to compromise an endpoint, credentials such as OAuth tokens are valuable targets because they let attackers persist or escalate their access.

A developer might have a legitimate need to view their own credentials when writing and debugging code. For example, a developer might need to [authenticate REST requests](https://docs.cloud.google.com/docs/authentication/rest) to Google Cloud services when working with an unsupported client library. The developer can view the credentials through various methods, including the following:

  * Viewing the [gcloud CLI configuration files](https://docs.cloud.google.com/sdk/docs/configurations) on the local file system
  * Querying the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview)
  * Using commands like `gcloud auth print-access-token` or `gcloud auth list`



However, an attacker might use these same techniques after they have compromised an endpoint.

If an attacker compromises an endpoint, the primary threat is that the attacker can run gcloud CLI commands or other code with the legitimate credentials of the authenticated identity. In addition, the attacker might copy the credentials to another endpoint that they control to persist their access. When this credential theft happens, a secondary threat occurs. The attacker can still use the long-lived credentials to have persistent access even after you remove access to the compromised endpoint.

If the attacker manages to compromise developer credentials, they can complete the following actions:

  * Impersonate the compromised user or service account. API traffic that uses the compromised tokens is logged as if it came from the compromised user or service account, making it difficult to distinguish between normal and malicious activity in logs.
  * Request access tokens indefinitely by using a persistent OAuth refresh token (from the gcloud CLI or Application Default Credentials) or a private key that's associated with a service account.
  * Bypass authentication with the user's password or 2-Step Verification because the tokens are granted after the sign-in flow.
  * Use stolen SSH keys to access Compute Engine instances and query the metadata server to steal attached service account tokens.
  * Use stolen browser cookies to hijack active Google Cloud console sessions without requiring the user's password or 2-Step Verification.
  * Use stolen federated access tokens to access resources granted to workforce identity pools or escalate privileges by impersonating service accounts.



## Best practices for mitigating risks

Implement the controls described in the following sections to help mitigate the risk of compromised developer credentials. If you're following the security best practices that are described in the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations/authentication-authorization#administrative-controls-for-cloud-identity) or [landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones/decide-security), you might already have these controls in place.

### Set session length for Google Cloud services

To reduce how long an attacker can exploit a compromised token, [set the session length for Google Cloud services](https://support.google.com/a/answer/9368756). For new customers, a [default session length of 16 hours](https://cloud.google.com/blog/products/identity-security/improve-security-posture-with-time-bound-session-length) is automatically enforced. Customers who created their Google Cloud organization before 2023 might have a default setting to never require reauthentication. Review this setting to ensure that you have a reauthentication policy with a session length that is between 1 and 24 hours. The reauthentication policy forces the user to regularly reauthenticate the gcloud CLI with their password or security key.

The session length for Google Cloud services is a distinct setting from the [session length for Google services](https://support.google.com/cloudidentity/answer/7576830), which controls web sessions for sign-in across Google Workspace services but doesn't control reauthentication for Google Cloud. If you use Google Workspace services, set the session length for both.

### Configure VPC Service Controls

Configure [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) across your environment to help ensure that only Google Cloud API traffic that originates within your defined perimeter can access [supported resources](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products). The service perimeter limits the usefulness of compromised credentials because the perimeter blocks requests to restricted services that originate from attacker-controlled endpoints that are outside of your environment.

### Configure Chrome Enterprise Premium

Configure Chrome Enterprise Premium policies to help [secure the Google Cloud console and Google Cloud APIs](https://docs.cloud.google.com/access-context-manager/docs/securing-console-and-apis). Configure a Chrome Enterprise Premium access level and binding to selectively allow attributes that are evaluated on every API request, including IP-based access or [certificate-based access for mutual TLS](https://docs.cloud.google.com/access-context-manager/docs/securing-resources-with-certificate-based-access). Requests that use compromised authorization credentials but don't meet the conditions that are defined in your Chrome Enterprise Premium policy are rejected.

**Note:** Not all [device attributes collected by Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/device-information) are evaluated during every API request.

Chrome Enterprise Premium is a user-centric control that rejects user API traffic that doesn't meet defined conditions. VPC Service Controls is a resource-centric control that defines the perimeters within which resources can communicate. VPC Service Controls applies to all user identities and service account identities, but Chrome Enterprise Premium applies only to user identities within your organization. When used together, Chrome Enterprise Premium and VPC Service Controls reduce the effectiveness of compromised credentials on an attacker-controlled machine that is outside of your environment.

### Enforce 2-Step Verification for remote server access

If you let developers access Compute Engine resources using SSH, configure [OS Login with 2-Step Verification](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#2fa). This enforces an additional checkpoint where a user must reauthenticate with their password or security key. An attacker with compromised OAuth tokens but no password or security key is blocked by this feature.

Remote Desktop Protocol (RDP) access to Windows instances on Compute Engine doesn't support the OS Login service, so 2-Step Verification can't be granularly enforced for RDP sessions. When using [Identity-Aware Proxy (IAP) Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#iap-desktop) or Google Chrome-based RDP plugins, complete the following:

  * Set coarse-grained controls like [session length for Google services](https://support.google.com/a/answer/7576830) and [2-Step Verification](https://support.google.com/a/answer/9176657) settings for the user's web sessions.

  * Disable the **Allow user to trust the device** setting under 2-Step Verification.




### Restrict the use of service account keys

When you use a service account key to authenticate, the key value is stored in the gcloud CLI configuration files, separately from the downloaded key file. An attacker with access to your environment can copy the key from the gcloud CLI configuration or copy the key file from your local file system or internal code repository. Therefore, in addition to your plan to mitigate compromised access tokens, consider how you manage downloaded service account key files.

Review [more secure alternatives for authentication](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) to reduce or eliminate your use cases that depend on a service account key. Also, enforce the [`constraints/iam.disableServiceAccountKeyCreation`](https://docs.cloud.google.com/organization-policy/restrict-service-accounts#disable_service_account_key_creation) and [`constraints/iam.disableServiceAccountKeyUpload`](https://docs.cloud.google.com/organization-policy/restrict-service-accounts#disable_service_account_key_upload) organization policy constraints to disable service account key creation.

### Apply the principle of least privilege

When designing Identity and Access Management (IAM) policies, consider [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least-privilege). Only grant users the roles that they require to accomplish a task at the smallest scope. [Review and apply role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations) to avoid IAM policies with unused and excessive roles in your environment.

### Protect your endpoints

Consider how an attacker might gain physical access or remote access to your endpoints, like developer workstations or Compute Engine instances. Although a plan to address the threat of compromised credentials is important, also consider the risk of an attacker compromising your trusted endpoints. If an attacker has access to your trusted endpoints, they can run gcloud CLI commands or other code directly on the endpoints themselves.

Although comprehensive protection for developer workstations is beyond the scope of this document, evaluate how your security tools and operations can help protect and monitor your endpoints for compromise. Consider the following questions:

  * How is the physical security of developer workstations protected?
  * How do you identify and respond to network breaches?
  * How do users get remote access to SSH or RDP sessions?
  * How might persistent credentials like SSH keys or service account keys be compromised?
  * Are there workflows that use persistent credentials that could be replaced with short-lived credentials?
  * Are there shared devices where someone could read another user's cached gcloud CLI credentials?
  * Can a user authenticate with gcloud CLI from an untrusted device?
  * How does approved traffic connect to resources inside your VPC Service Controls perimeter?



Ensure that your security operations address each of these questions.

### Align your response teams

Ensure in advance that security teams who are responsible for incident response have appropriate access across the Google Cloud console and the Admin console. If separate teams manage the Google Cloud console and the Admin console, you might have a delayed response during an incident.

To assess and respond to a compromise, see [Respond to compromised Google Cloud credentials](https://docs.cloud.google.com/docs/security/compromised-credentials).

## Monitor for credential compromise

To monitor for potential compromise, consider the following:

  * Scan for secrets in your code repositories, using tools such as [Anomaly Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#anomaly_detection) or [secret scanning](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning).

  * In Cloud Audit Logs, configure alerts for the following:

    * `iamcredentials.googleapis.com` methods (such as `GenerateAccessToken`, `GenerateIdToken`, `SignJwt`) to audit service account token generation

These logs require that you enable [Data Access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

    * `protoPayload.authenticationInfo.serviceAccountDelegationInfo.firstPartyPrincipal.principalEmail` to audit user and service account impersonations

    * `sts.googleapis.com` exchange requests for anomalous identity assertions

  * In Security Command Center, monitor for the following [threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) from Event Threat Detection:

    * Persistence: New Geography
    * Persistence: New User Agent
    * Persistence: New API Method
    * Evasion: Access from Anonymizing Proxy
    * Privilege Escalation: Anomalous Impersonation of Service Account for Admin Activity
    * Privilege Escalation: Anomalous Service Account Impersonator for Admin Activity
    * Initial Access: Leaked Service Account Key Used
    * Persistence: Service Account Key Created
    * Initial Access: Suspicious Login Blocked
    * Initial Access: Account Disabled Hijacked

For each threat, [recommended investigation steps](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) are provided to aid in your response.

  * Monitor user logins in [Google Workspace](https://support.google.com/a/answer/6000239) and [Cloud Identity](https://support.google.com/cloudidentity/answer/7420688). To better track issues, consider exporting the logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).

  * Monitor logs from Chrome Enterprise Premium and VPC Service Controls for out-of-perimeter access attempts with stolen tokens.

  * Monitor for anomalies in service account key usage using [Cloud Monitoring](https://docs.cloud.google.com/iam/docs/service-account-monitoring).




Ensure that your security operations center (SOC) is notified promptly and has the playbooks, tools, and access that are required to respond quickly to a suspected credential compromise. You can also integrate [Security Command Center with your existing SIEM](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-splunk) or [import logs into Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs) for further analysis.

## What's next

  * [Respond to compromised Google Cloud credentials](https://docs.cloud.google.com/docs/security/compromised-credentials)
  * [Authenticate for the gcloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate)
  * [Authenticate as a service account](https://docs.cloud.google.com/docs/authentication#service-accounts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
