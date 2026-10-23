---
url: https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview/
title: Agent Platform Threat Detection overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:12.590032+00:00
---

# Agent Platform Threat Detection overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Agent Platform Threat Detection overview Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides an overview of Agent Platform Threat Detection and its detectors.

Agent Platform Threat Detection is a built-in service of Security Command Center that helps you detect and investigate potential attacks on AI agents that are deployed to [Agent Runtime](https://docs.cloud.google.com/agent-builder/agent-engine/overview). If the Agent Platform Threat Detection service detects a potential attack, it generates a finding in Security Command Center in near-real time.

Agent Platform Threat Detection monitors the [supported AI agents](https://docs.cloud.google.com/security-command-center/docs/use-agent-engine-threat-detection#view-resources) and detects the most common runtime threats. Runtime threats include the execution of malicious binaries or scripts, container escapes, reverse shells, and the use of attack tools within the agent's environment.

In addition, control-plane detectors from [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) analyze various audit logs (including Identity and Access Management, BigQuery, and Cloud SQL logs) and Agent Runtime logs (`stdout` and `stderr`) to detect suspicious activity. Control-plane threats include data exfiltration attempts, excessive permission denials, and suspicious token generation.

## Benefits

Agent Platform Threat Detection offers the following benefits:

  * **Proactively reduce risk for AI workloads.** Agent Platform Threat Detection helps you detect and respond to threats early by monitoring the behavior and environment of your AI agents
  * **Manage AI security in a unified location.** Agent Platform Threat Detection findings appear directly in Security Command Center. You have a central interface to view and manage threat findings alongside other cloud security risks.



## How it works

Agent Platform Threat Detection collects telemetry from the hosted AI agents to analyze processes, scripts, and libraries that might indicate a runtime attack. When Agent Platform Threat Detection detects a potential threat, it does the following:

  1. Agent Platform Threat Detection uses a watcher process to collect event information while the agentic workload is running. The watcher process can take up to one minute to start and collect information.

  2. Agent Platform Threat Detection analyzes the collected event information to determine whether an event indicates an incident. Agent Platform Threat Detection uses natural language processing (NLP) to analyze Bash and Python scripts for malicious code.

     * If Agent Platform Threat Detection identifies an incident, it reports the incident as a finding in Security Command Center.

     * If Agent Platform Threat Detection doesn't identify an incident, it doesn't store any information.

     * All data collected is processed in memory and doesn't persist after analysis unless identified as an incident and reported as a finding.




For information about how to review Agent Platform Threat Detection findings in the Google Cloud console, see [Review findings](https://docs.cloud.google.com/security-command-center/docs/use-agent-engine-threat-detection#review-findings).

## Detectors

This section lists the runtime and control-plane detectors that monitor the AI agents that are deployed to Agent Runtime.

### Runtime detectors

Agent Platform Threat Detection includes the following runtime detectors:

Display name | Module name | Description  
---|---|---  
Command and Control: Steganography Tool Detected ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_STEGANOGRAPHY_TOOL_DETECTED` |  A program identified as a steganography tool was executed, signaling a potential attempt to conceal communication or data transfer.  Attackers might utilize steganographic techniques to embed malicious command and control (C2) instructions or exfiltrated data within seemingly benign digital files, aiming to evade standard security monitoring and detection. Identifying the use of such tools is crucial for uncovering hidden malicious activity.   
Credential Access: Find Google Cloud Credentials ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_FIND_GCP_CREDENTIALS` |  A command was executed to search for Google Cloud private keys, passwords, or other sensitive credentials within the container environment.  An attacker can use stolen Google Cloud credentials to gain unauthorized access to sensitive data or resources within the targeted Google Cloud environment.   
Credential Access: GPG Key Reconnaissance ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_GPG_KEY_RECONNAISSANCE` |  A command was executed to search for GPG security keys.  An attacker can use stolen GPG security keys to gain unauthorized access to encrypted communications or files.   
Credential Access: Search Private Keys or Passwords ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SEARCH_PRIVATE_KEYS_OR_PASSWORDS` |  A command was executed to search for private keys, passwords, or other sensitive credentials within the container environment, indicating a potential attempt to harvest authentication data.  Attackers often search for credential files to gain unauthorized access to systems, escalate privileges, or move laterally within the environment. Detecting such activity is critical to preventing security breaches.   
Defense Evasion: Base64 ELF File Command Line ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_BASE64_ELF_FILE_CMDLINE` |  A process was executed that contains an argument that is an ELF (Executable and Linkable Format) file.  Detecting an encoded ELF file execution signals that an attacker might be trying to encode binary data for transfer to ASCII-only command lines. Attackers can use this technique to evade detection and run malicious code embedded in an ELF file.   
Defense Evasion: Base64 Encoded Python Script Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_BASE64_ENCODED_PYTHON_SCRIPT_EXECUTED` |  A process was executed that contains an argument that is a base64- encoded python script.  If an encoded python script execution is detected, it's a signal that an attacker is trying to encode binary data for transfer to ASCII-only command lines. Attackers can use this technique to evade detection and run malicious code embedded in a python script.   
Defense Evasion: Base64 Encoded Shell Script Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_BASE64_ENCODED_SHELL_SCRIPT_EXECUTED` |  A process was executed that contains an argument that is a base64- encoded shell script.  If an encoded shell script execution is detected, it's a signal that an attacker is trying to encode binary data for transfer to ASCII-only command lines. Attackers can use this technique to evade detection and run malicious code embedded in a shell script.   
Defense Evasion: Launch Code Compiler Tool In Container ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_LAUNCH_CODE_COMPILER_TOOL_IN_CONTAINER` |  A process was initiated to launch a code compiler tool within the container environment, indicating a potential attempt to build or modify executable code in an isolated context.  Attackers might use code compilers within containers to develop malicious payloads, inject code into existing binaries, or create tools to bypass security controls, all while operating in a less scrutinized environment to evade detection on the host system.   
Execution: Added Malicious Binary Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_ADDED_MALICIOUS_BINARY_EXECUTED` |  A process executed a binary that threat intelligence identifies as malicious. This binary was not part of the original agentic workload. This event strongly suggests that an attacker has control of the workload and is running malicious software.   
Execution: Added Malicious Library Loaded ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_ADDED_MALICIOUS_LIBRARY_LOADED` |  A process loaded a library that threat intelligence identifies as malicious. This library was not part of the original agentic workload. This event suggests that an attacker likely has control of the workload and is running malicious software.   
Execution: Added Malicious Skill Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_ADDED_MALICIOUS_SKILL_EXECUTED` |  A process executed a skill that threat intelligence identifies as malicious. This skill was not part of the original agentic workload. This event strongly suggests that an attacker has control of the workload and is running malicious software.   
Execution: Added Malicious Skill Loaded ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_ADDED_MALICIOUS_SKILL_LOADED` |  A process loaded a skill that threat intelligence identifies as malicious. This skill was not part of the original agentic workload. This event suggests that an attacker likely has control of the workload and is running malicious software.   
Execution: Built in Malicious Binary Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_BUILT_IN_MALICIOUS_BINARY_EXECUTED` |  A process executed a binary that threat intelligence identifies as malicious. This binary was part of the original agentic workload. This event might suggest that an attacker is deploying a malicious workload. For example, the actor might have gained control of a legitimate build pipeline and injected the malicious binary into the agentic workload.   
Execution: Container Escape ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_CONTAINER_ESCAPE` |  A process running inside the container attempted to bypass container isolation by using known exploit techniques or binaries, which threat intelligence identifies as potential threats. A successful escape can allow an attacker to access the host system and potentially compromise the entire environment.  This action suggests that an attacker is exploiting vulnerabilities to gain unauthorized access to the host system or broader infrastructure.   
Execution: Fileless Execution in /memfd: ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_FILELESS_EXECUTION_DETECTION_MEMFD` |  A process was executed using an in-memory file descriptor.  A process launched from an in-memory file might indicate an attacker is trying to bypass other detection methods to execute malicious code.   
Execution: Kubernetes Attack Tool Execution ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_KUBERNETES_ATTACK_TOOL_EXECUTION` |  A process executed a Kubernetes-specific attack tool, which threat intelligence identifies as a potential threat.  This action suggests that an attacker has gained access to the cluster and is using the tool to exploit Kubernetes-specific vulnerabilities or configurations.   
Execution: Local Reconnaissance Tool Execution ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_LOCAL_RECONNAISSANCE_TOOL_EXECUTION` |  A process executed a local reconnaissance tool that is not typically part of the agentic workload. Threat intelligence identifies these tools as potential threats.  This event suggests that an attacker is trying to gather internal system information, such as mapping the infrastructure, identifying vulnerabilities, or collecting data on system configurations.   
Execution: Malicious Python Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_MALICIOUS_PYTHON_EXECUTED` |  A machine learning model identified executed Python code as malicious. An attacker can use Python to download tools or files into a compromised environment and execute commands without using binaries.  The detector uses natural language processing (NLP) to analyze the Python code's content. Because this approach isn't based on signatures, detectors can identify known and novel malicious Python code.   
Execution: Modified Malicious Binary Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_MODIFIED_MALICIOUS_BINARY_EXECUTED` |  A process executed a binary that threat intelligence identifies as malicious. This binary was part of the original agentic workload but was modified at runtime. This event suggests that an attacker might have control of the workload and is running malicious software.   
Execution: Modified Malicious Library Loaded ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_MODIFIED_MALICIOUS_LIBRARY_LOADED` |  A process loaded a library that threat intelligence identifies as malicious. This library was part of the original agentic workload but was modified at runtime. This event suggests that an attacker has control of the workload and is running malicious software.   
Execution: Modified Malicious Skill Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_MODIFIED_MALICIOUS_SKILL_EXECUTED` |  A process executed a skill that threat intelligence identifies as malicious. This skill was part of the original agentic workload but was modified at runtime. This event suggests that an attacker might have control of the workload and is running malicious software.   
Execution: Modified Malicious Skill Loaded ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_MODIFIED_MALICIOUS_SKILL_LOADED` |  A process loaded a skill that threat intelligence identifies as malicious. This skill was part of the original agentic workload but was modified at runtime. This event suggests that an attacker has control of the workload and is running malicious software.   
Malicious Script Executed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_MALICIOUS_SCRIPT_EXECUTED` |  A machine learning model identified executed Bash code as malicious. An attacker can use Bash to download tools or files into a compromised environment and execute commands without using binaries.  The detector uses NLP to analyze the Bash code's content. Because this approach is not based on signatures, detectors can identify known and novel malicious Bash code.  
Malicious URL Observed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_MALICIOUS_URL_OBSERVED` |  Agent Platform Threat Detection observed a malicious URL in the argument list of a running process. The detector compares these URLs against the unsafe web resources lists maintained by the Google [Safe Browsing](https://developers.google.com/safe-browsing) service. If you believe that Google incorrectly classified a URL as a phishing site or malware, report the issue at [ Reporting Incorrect Data](https://developers.google.com/safe-browsing/v4/reporting).  
Reverse Shell ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_REVERSE_SHELL` |  A process started with stream redirection to a remote connected socket. The detector looks for `stdin` bound to a remote socket.  A reverse shell allows an attacker to communicate from a compromised workload to an attacker-controlled machine. The attacker can then command and control the workload—for example, as part of a botnet.   
Unexpected Child Shell ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_UNEXPECTED_CHILD_SHELL` |  A process that does not normally invoke shells unexpectedly spawned a shell process. The detector monitors process executions and generates a finding when a known parent process spawns a shell unexpectedly.  
Execution: Netcat Remote Code Execution in Container ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_NETCAT_REMOTE_CODE_EXECUTION_IN_CONTAINER` |  Netcat, a versatile networking utility, was executed within the container environment, potentially indicating an attempt to establish unauthorized remote access or exfiltrate data.  The use of Netcat in a containerized environment might signal an attacker's effort to create a reverse shell, enable lateral movement, or execute arbitrary commands, which can compromise system integrity.   
Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47177) ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_POSSIBLE_ARBITRARY_COMMAND_EXECUTION_THROUGH_CUPS` |  This rule detects the `foomatic-rip` process executing common shell programs, which might indicate that an attacker has exploited CVE-2024-47177. `foomatic-rip` is part of the OpenPrinting CUPS, an open source printing service that is a part of many Linux distributions. Most container images have this printing service disabled or removed. If this detection occurs, evaluate that this is intended behavior or disable the service immediately.   
Execution: Possible Remote Command Execution Detected ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_POSSIBLE_REMOTE_COMMAND_EXECUTION_DETECTED` |  A process was detected spawning common UNIX commands through a network socket connection, indicating a potential attempt to establish unauthorized remote command execution capabilities.  Attackers frequently utilize techniques that mimic reverse shells to gain interactive control over a compromised system, allowing them to execute arbitrary commands remotely and bypass standard network security measures like firewall restrictions. Detecting command execution over a socket is a strong indicator of malicious remote access.   
Execution: Program Run with Disallowed HTTP Proxy Env ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_PROGRAM_RUN_WITH_DISALLOWED_HTTP_PROXY_ENV` |  A program was executed with an HTTP proxy environment variable that is disallowed. This can indicate an attempt to bypass security controls, redirect traffic for malicious purposes, or exfiltrate data through unauthorized channels.  Attackers might configure disallowed HTTP proxies to intercept sensitive information, route traffic through malicious servers, or establish covert communication channels. Detecting the execution of programs with these environment variables is crucial for maintaining network security and preventing data breaches.   
Execution: Socat Reverse Shell Detected ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SOCAT_REVERSE_SHELL_DETECTED` |  The `socat` command has been used to create a reverse shell.  This rule detects the execution `socat` to create a reverse shell by redirecting stdin, stdout, and stderr file descriptors. This is a common technique used by attackers to gain remote access to a compromised system.   
Execution: Suspicious OpenSSL Shared Object Loaded ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_OPENSSL_SHARED_OBJECT_LOADED` |  OpenSSL has been executed to load a custom shared object.  Attackers might load custom libraries and replace existing libraries used by OpenSSL in order to run malicious code. Its use in production is uncommon and should warrant an immediate investigation.   
Exfiltration: Launch Remote File Copy Tools in Container ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_LAUNCH_REMOTE_FILE_COPY_TOOLS_IN_CONTAINER` |  A remote file copy tool execution was detected within the container, indicating potential data exfiltration, lateral movement, or the deployment of malicious payloads.  Attackers often use these tools to transfer sensitive data outside of the container, move laterally within the network to compromise other systems, or introduce malware for further malicious activities. Detecting the use of remote file copy tools is crucial for preventing data breaches, unauthorized access, and further compromise of the container and potentially the host system.   
Impact: Detect Malicious Cmdlines ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_DETECT_MALICIOUS_CMDLINES` |  A command was executed with arguments known to be potentially destructive, such as attempts to delete critical system files or modify password-related configurations.  Attackers might issue malicious command lines to cause system instability, prevent recovery by deleting essential files, or gain unauthorized access by manipulating user credentials. Detecting these specific command patterns is critical to preventing significant system impact.   
Impact: Remove Bulk Data From Disk ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_REMOVE_BULK_DATA_FROM_DISK` |  A process was detected performing bulk data deletion operations, which might indicate an attempt to erase evidence, disrupt services, or execute a data-wiping attack within the container environment.  Attackers might remove large volumes of data to cover their tracks, sabotage operations, or prepare for ransomware deployment. Detecting such activity helps in identifying potential threats before critical data loss occurs.   
Impact: Suspicious cryptocurrency mining activity using the Stratum Protocol ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_DETECT_CRYPTO_MINERS_USING_STRATUM_PROTOCOL` |  A process was detected communicating over the Stratum protocol, which is commonly used by cryptocurrency mining software. This activity suggests potential unauthorized mining operations within the container environment.  Attackers often deploy cryptocurrency miners to exploit system resources for financial gain, leading to degraded performance, increased operational costs, and potential security risks. Detecting such activity helps mitigate resource abuse and unauthorized access.   
Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287) ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_ABUSE_SUDO_FOR_PRIVILEGE_ESCALATION` |  `sudo` has been executed with arguments that attempt to elevate privileges.  This detection notifies an attempt to exploit CVE-2019-14287, which allows privilege escalation by abusing the `sudo` command. `sudo` versions prior to v1.8.28 had an exploit that allowed a non-root user to gain root privileges.   
Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034) ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_POLKIT_LOCAL_PRIVILEGE_ESCALATION_VULNERABILITY` |  A non-root user has executed `pkexec` with environment variables that attempt to escalate privileges.  This rule detects an attempt to exploit a privilege escalation vulnerability (CVE-2021-4034) in Polkit's `pkexec`. By running specially crafted code, a non-root user can use this flaw to gain root privileges on a compromised system.   
Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156) ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUDO_POTENTIAL_PRIVILEGE_ESCALATION` |  A non-root user has executed `sudo` or `sudoedit` with a pattern of arguments that attempt to escalate privileges.  Detects an attempt to exploit a vulnerability affecting `sudo` versions 1.9.5p2 and earlier. Executing `sudo` or `sudoedit` with certain arguments, including one that ends with a single backslash character, as an unprivileged user can elevate the user's privileges to that of a root user.   
  
### Control-plane detectors

This section describes the control-plane detectors from Event Threat Detection that are specifically designed for AI agents deployed to Agent Runtime. Event Threat Detection also has Agent Runtime. Event Threat Detection also has [detectors for general AI-related threats](https://docs.cloud.google.com/security-command-center/docs/ai-threats).

These control-plane detectors are enabled by default. You manage these detectors the same way you do other Event Threat Detection detectors. For more information, see [Use Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection).

The **Sensitive data enrichment** column indicates whether a detector supports [sensitive data enrichment](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#sdp-enrichment).

Display name | API name | Log source types | Description | Sensitive data enrichment  
---|---|---|---|---  
Discovery: Evidence of Port Scanning from AI Agent ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_PORT_SCANNING_EVIDENCE` |  **Agent Engine Logs** :  
[Agent Engine Logs](https://docs.cloud.google.com/agent-builder/agent-engine/manage/logging) |  An AI agent exhibited horizontal or vertical port scanning behavior. Findings are classified as **Low** severity by default.  | —  
Discovery: AI Agent Unauthorized Service Account API Call ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_UNAUTHORIZED_SERVICE_ACCOUNT_API_CALL` |  **Cloud Audit Logs** :  
[Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  A service account made an unauthorized API call to an outside project through an AI agent. This behavior can indicate that an unauthorized user is attempting to gain details about resources, enable or disable services, or perform other unauthorized actions through an AI agent. Findings are classified as **Low** severity by default.  |  Category: `Discovery: AI Agent Unauthorized Service Account API Call Affecting Sensitive Data`  
Severity: Low to Medium   
Discovery: AI Agent Service Account Self-Investigation ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_IAM_ANOMALOUS_BEHAVIOR_SERVICE_ACCOUNT_GETS_OWN_IAM_POLICY` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
**Permissions** :  
`DATA_READ` |  An identity associated with an AI agent was used to investigate the roles and permissions associated with that same service account. Findings are classified as **Low** severity if the request was authorized, or **High** severity if the request was not authorized.  | —  
Credential Access: AI Agent Anomalous Access to Metadata Service ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_ANOMALOUS_ACCESS_TO_METADATA_SERVICE` |  **Agent Engine Logs** :  
[Agent Engine Logs](https://docs.cloud.google.com/agent-builder/agent-engine/manage/logging) |  An AI agent fetched a service account token from a metadata server. Findings are classified as **Low** severity by default.  | —  
Exfiltration: AI Agent Initiated BigQuery VPC Perimeter Violation ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `AGENT_ENGINE_BIG_QUERY_EXFIL_VPC_PERIMETER_VIOLATION`  
|  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions) **Permissions** :  
`DATA_READ` |  Detects an attempt by an AI agent to access BigQuery resources that are protected by VPC Service Controls. Findings are classified as **Low** severity by default.  | —  
Exfiltration: AI Agent Initiated BigQuery Data Exfiltration to External Table ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `AGENT_ENGINE_BIG_QUERY_EXFIL_TO_EXTERNAL_TABLE`  
|  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions) **Permissions** :  
`DATA_READ` |  Detects when resources owned by the protected organization were saved outside of the organization by an AI agent, including copy or transfer operations. Findings are classified as **High** severity by default.  |  Category: `Exfiltration: AI Agent Initiated Sensitive BigQuery Data Exfiltration to External Table`  
Severity: No change (default High)   
Exfiltration: AI Agent Initiated CloudSQL Exfiltration to Public Bucket ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `AGENT_ENGINE_CLOUDSQL_EXFIL_EXPORT_TO_PUBLIC_GCS`  
|  **Cloud Audit Logs** : [MySQL data access logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
[PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[SQL Server data access logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging) |  Detects when live instance data was exported by an AI agent to a Cloud Storage bucket that is owned by the organization and is publicly accessible.  For project-level activations of the Security Command Center Premium tier, this finding is available only if the Standard-legacy tier is enabled in the parent organization.. Findings are classified as **High** severity by default.  | —  
Exfiltration: AI Agent Initiated CloudSQL Exfiltration to External Bucket ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  `AGENT_ENGINE_CLOUDSQL_EXFIL_EXPORT_TO_EXTERNAL_GCS` |  **Cloud Audit Logs** : [MySQL data access logs](https://docs.cloud.google.com/sql/docs/mysql/audit-logging)  
[PostgreSQL data access logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging)  
[SQL Server data access logs](https://docs.cloud.google.com/sql/docs/sqlserver/audit-logging) |  Detects when live instance data was exported by an AI agent to a Cloud Storage bucket outside of the organization.  For project-level activations of the Security Command Center Premium tier, this finding is available only if the Standard-legacy tier is enabled in the parent organization.. Findings are classified as **High** severity by default.  | —  
Exfiltration: AI Agent Initiated BigQuery Data Extraction ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_BIG_QUERY_EXFIL_TO_CLOUD_STORAGE` |  **Cloud Audit Logs** : [ BigQueryAuditMetadata data access logs](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs#versions) **Permissions** :  
`DATA_READ` |  Detects the following scenarios of a BigQuery data extraction initiated by an AI agent:

  * A BigQuery resource owned by the protected organization was saved, through extraction operations, to a Cloud Storage bucket outside the organization. 
  * A BigQuery resource owned by the protected organization was saved, through extraction operations, to a publicly accessible Cloud Storage bucket owned by that organization. 

For project-level activations of the Security Command Center Premium tier, this finding is available only if the Standard-legacy tier is enabled in the parent organization.. Findings are classified as **Low** severity by default. |  Category: `Exfiltration: AI Agent Initiated Sensitive BigQuery Data Extraction`  
Severity: Low to Medium   
Initial Access: AI Agent Identity Excessive Permission Denied Actions ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_EXCESSIVE_FAILED_ATTEMPT` |  **Cloud Audit Logs** : [Admin Activity logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) |  An identity associated with an AI agent repeatedly triggered _permission denied_ errors by attempting changes across multiple methods and services. Findings are classified as **Medium** severity by default.  | —  
Privilege Escalation: AI Agent Token Generation Using signJwt ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_TOKEN_GENERATION_SIGN_JWT` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
|  A service account associated with an AI agent used the [ `serviceAccounts.signJwt`](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signJwt) method to generate an access token for another service account.  Findings are classified as **Low** severity by default. | —  
Privilege Escalation: AI Agent Token Generation Using Implicit Delegation ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_TOKEN_GENERATION_IMPLICIT_DELEGATION` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
|  The `iam.serviceAccounts.implicitDelegation` permission was misused to generate access tokens from a more privileged service account through an AI agent. Findings are classified as **Low** severity by default.  | —  
Privilege Escalation: AI Agent Cross-Project OpenID Token Generation ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_TOKEN_GENERATION_CROSS_PROJECT_OPENID` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
|  The `iam.serviceAccounts.getOpenIdToken` IAM permission was used across projects through an AI agent.  This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
Privilege Escalation: AI Agent Cross-Project Access Token Generation ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `AGENT_ENGINE_SUSPICIOUS_TOKEN_GENERATION_CROSS_PROJECT_ACCESS_TOKEN` |  **Cloud Audit Logs** :  
[IAM Data Access audit logs](https://docs.cloud.google.com/iam/docs/audit-logging)  
|  The `iam.serviceAccounts.getAccessToken` IAM permission was used across projects through an AI agent.  This finding isn't available for project-level activations. Findings are classified as **Low** severity by default. | —  
  
For deprecated and shut down rules, see [Deprecations](https://docs.cloud.google.com/security-command-center/docs/deprecations). 

## What's next

  * Learn how to [use Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/use-agent-engine-threat-detection).
  * Learn how to [test Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-test-agent-engine-threat-detection).
  * Learn how to [use Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection).
  * Learn how to [respond to AI threat findings](https://docs.cloud.google.com/security-command-center/docs/respond-ai-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
