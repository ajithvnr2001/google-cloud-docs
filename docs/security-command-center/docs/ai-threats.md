---
url: https://docs.cloud.google.com/security-command-center/docs/ai-threats/
title: AI threat findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:59.598524+00:00
---

# AI threat findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/ai-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  AI threat findings Stay organized with collections  Save and categorize content based on your preferences. 

Security Command Center has detectors for general AI-related threats and detectors that are designed for AI agents deployed to Agent Runtime Runtime.

## General AI threats

The following log-based detections are available with [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview):

  * [ `Initial Access: Dormant Service Account Activity in AI Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-dormant-service-account-used-in-action)
  * [ `Persistence: New AI API Method`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-behavior-new-api-method)
  * [ `Persistence: New Geography for AI Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-iam-anomalous-behavior-ip-geolocation)
  * [ `Privilege Escalation: Anomalous Impersonation of Service Account for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonation-of-sa-admin-activity)
  * [ `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-multistep-admin-activity)
  * [ `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Data Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-multistep-data-access)
  * [ `Privilege Escalation: Anomalous Service Account Impersonator for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonator-admin-activity)
  * [ `Privilege Escalation: Anomalous Service Account Impersonator for AI Data Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonator-data-access)



## Threats to agents deployed to Agent Runtime Runtime

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Security Command Center performs runtime and control plane monitoring of AI agents deployed to [Agent Runtime](https://docs.cloud.google.com/agent-builder/agent-engine/overview) Runtime.

### Runtime finding types

The following runtime detections are available with [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview):

  * [ `Command and Control: Steganography Tool Detected`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-steganography-tool-detected)
  * [ `Credential Access: Find Google Cloud Credentials`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-find-gcp-credentials)
  * [ `Credential Access: GPG Key Reconnaissance`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-gpg-key-reconnaissance)
  * [ `Credential Access: Search Private Keys or Passwords`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-search-private-keys-or-passwords)
  * [ `Defense Evasion: Base64 ELF File Command Line`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-base64-elf-file-cmdline)
  * [ `Defense Evasion: Base64 Encoded Python Script Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-base64-encoded-python-script-executed)
  * [ `Defense Evasion: Base64 Encoded Shell Script Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-base64-encoded-shell-script-executed)
  * [ `Defense Evasion: Launch Code Compiler Tool In Container`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-launch-code-compiler-tool-in-container)
  * [ `Execution: Added Malicious Binary Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-added-malicious-binary-executed)
  * [ `Execution: Added Malicious Library Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-added-malicious-library-loaded)
  * [ `Execution: Added Malicious Skill Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-added-malicious-skill-executed)
  * [ `Execution: Added Malicious Skill Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-added-malicious-skill-loaded)
  * [ `Execution: Built in Malicious Binary Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-built-in-malicious-binary-executed)
  * [ `Execution: Container Escape`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-container-escape)
  * [ `Execution: Fileless Execution in /memfd:`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-fileless-execution-detection-memfd)
  * [ `Execution: Kubernetes Attack Tool Execution`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-kubernetes-attack-tool-execution)
  * [ `Execution: Local Reconnaissance Tool Execution`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-local-reconnaissance-tool-execution)
  * [ `Execution: Malicious Python Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-malicious-python-executed)
  * [ `Execution: Modified Malicious Binary Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-modified-malicious-binary-executed)
  * [ `Execution: Modified Malicious Library Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-modified-malicious-library-loaded)
  * [ `Execution: Modified Malicious Skill Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-modified-malicious-skill-executed)
  * [ `Execution: Modified Malicious Skill Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-modified-malicious-skill-loaded)
  * [ `Execution: Netcat Remote Code Execution in Container`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-netcat-remote-code-execution-in-container)
  * [ `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47177)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-possible-arbitrary-command-execution-through-cups)
  * [ `Execution: Possible Remote Command Execution Detected`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-possible-remote-command-execution-detected)
  * [ `Execution: Program Run with Disallowed HTTP Proxy Env`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-program-run-with-disallowed-http-proxy-env)
  * [ `Execution: Socat Reverse Shell Detected`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-socat-reverse-shell-detected)
  * [ `Execution: Suspicious OpenSSL Shared Object Loaded`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-suspicious-openssl-shared-object-loaded)
  * [ `Exfiltration: Launch Remote File Copy Tools in Container`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-launch-remote-file-copy-tools-in-container)
  * [ `Impact: Detect Malicious Cmdlines`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-detect-malicious-cmdlines)
  * [ `Impact: Remove Bulk Data from Disk`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-remove-bulk-data-from-disk)
  * [ `Impact: Suspicious crypto mining activity using the Stratum Protocol`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-detect-crypto-miners-using-stratum-protocol)
  * [ `Malicious Script Executed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-malicious-script-executed)
  * [ `Malicious URL Observed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-malicious-url-observed)
  * [ `Privilege Escalation: Attempt to Abuse Sudo For Privilege Escalation (CVE-2019-14287)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-abuse-sudo-for-privilege-escalation)
  * [ `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-polkit-local-privilege-escalation-vulnerability)
  * [ `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-sudo-potential-privilege-escalation)
  * [ `Reverse Shell`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-reverse-shell)
  * [ `Unexpected Child Shell`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-platform-unexpected-child-shell)



### Control plane finding types

The following control plane detections are available with [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview):

  * [ `Credential Access: AI Agent Anomalous Access to Metadata Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-anomalous-access-to-metadata-service)
  * [ `Defense Evasion: Folder Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-folder)
  * [ `Defense Evasion: Organization Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-org)
  * [ `Defense Evasion: Project Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-project)
  * [ `Discovery: AI Agent Service Account Self-Investigation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-iam-anomalous-behavior-service-account-gets-own-iam-policy)
  * [ `Discovery: AI Agent Unauthorized Service Account API Call`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-unauthorized-service-account-api-call)
  * [ `Discovery: Evidence of Port Scanning from AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-port-scanning-evidence)
  * [ `Exfiltration: AI Agent Initiated BigQuery Data Exfiltration to External Table`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-exfil)
  * [ `Exfiltration: AI Agent Initiated BigQuery Data Extraction`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-exfil-to-cloud-storage)
  * [ `Exfiltration: AI Agent Initiated BigQuery VPC Perimeter Violation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-vpc-violation)
  * [ `Exfiltration: AI Agent Initiated CloudSQL Exfiltration to External Bucket`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-cloudsql-exfil-export-external)
  * [ `Exfiltration: AI Agent Initiated CloudSQL Exfiltration to Public Bucket`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-cloudsql-exfil-export-public)
  * [ `Initial Access: AI Agent Identity Excessive Permission Denied Actions`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-excessive-failed-attempt)
  * [ `Persistence: Sensitive AI Permission Added to Custom Role`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-ai-permission-added-to-custom-role)
  * [ `Persistence: Sensitive Role Granted by AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-role-granted-by-ai-agent)
  * [ `Persistence: Sensitive Role Granted to External AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/external-ai-agent-granted-sensitive-role)
  * [ `Privilege Escalation: AI Agent Cross-Project Access Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-cross-project-access-token)
  * [ `Privilege Escalation: AI Agent Cross-Project OpenID Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-cross-project-openid)
  * [ `Privilege Escalation: AI Agent Token Generation Using Implicit Delegation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-implicit-delegation)
  * [ `Privilege Escalation: AI Agent Token Generation Using signJwt`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-sign-jwt)



## What's next

  * Learn about [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).
  * Learn about [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-engine-threat-detection-overview).
  * Learn how to [respond to AI threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-ai-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
