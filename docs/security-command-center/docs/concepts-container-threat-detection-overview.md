---
url: https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview/
title: Container Threat Detection overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:04.368603+00:00
---

# Container Threat Detection overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Container Threat Detection overview Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides a high-level overview of Container Threat Detection concepts and features.

## What is Container Threat Detection?

Container Threat Detection is a built-in service of Security Command Center that continuously monitors the state of [Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos) node images. The service evaluates all changes and remote access attempts to detect runtime attacks in near-real time.

Container Threat Detection detects the most common container runtime attacks and alerts you in Security Command Center and, optionally, in Cloud Logging. Container Threat Detection includes several detection capabilities, including suspicious binaries and libraries, and uses natural language processing (NLP) to detect malicious Bash and Python code.

Container Threat Detection is available only with the Premium tier or Enterprise tier of Security Command Center.

## How Container Threat Detection works

Container Threat Detection detection instrumentation collects low-level behavior in the guest kernel and executed scripts. The following is the execution path when events are detected:

  1. Container Threat Detection passes event information and information that identifies the container through a user mode DaemonSet to a detector service for analysis. Event collection is configured automatically when Container Threat Detection is enabled.

The watcher DaemonSet passes container information in a best effort manner. Container information can be dropped from the reported finding if the Kubernetes and the container runtime fail to deliver the corresponding container information in time.

  2. The detector service analyzes events to determine whether an event is indicative of an incident. The Bash and Python scripts are analyzed with NLP to determine if the executed code is malicious.

  3. If the detector service identifies an incident, the incident is written as a finding in Security Command Center and, optionally, to Cloud Logging.

     * If the detector service doesn't identify an incident, then finding information isn't stored.
     * All data in the kernel and detector service is ephemeral and isn't persistently stored.



You can view finding details in the Security Command Center console and investigate finding information. Your ability to view and edit findings is determined by the roles you are granted. For more information on Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

## Considerations

Consider the following when using Container Threat Detection.

### Security detection tools

Other security detection tools that are installed in your cluster can impair the performance of Container Threat Detection and cause it to malfunction. We recommend that you not have any other security detection tools installed in your cluster if the cluster is already protected by Container Threat Detection.

### File monitoring detectors

Container Threat Detection includes a number of detectors that monitor file operations looking for access or modification to critical system files. These detectors monitor file operations occurring on the node. Workloads with significant file I/O, such as CI/CD systems, can potentially suffer performance degradation when these detectors are enabled. To avoid any unexpected impacts, these detectors are disabled by default. We recommend that you evaluate the impact on any workload before enabling the file monitoring detectors in production.

### Disabled detectors

The following detectors are disabled by default:

  * `Added Binary Executed`
  * `Added Library Loaded`
  * `Collection: Pam.d Modification` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Credential Access: Access Sensitive Files on Nodes` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Credential Access: Find Google Cloud Credentials`
  * `Defense Evasion: Disable or modify Linux audit system` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Defense Evasion: Launch Code Compiler Tool In Container`
  * `Defense Evasion: Root Certificate Installed` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Execution: Ingress Nightmare Vulnerability Execution` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Execution: Program Run with Disallowed HTTP Proxy Env`
  * `Execution: Suspicious Cron Modification` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Exfiltration: Launch Remote File Copy Tools in Container`
  * `Persistence: Modify ld.so.preload` ([Preview](https://cloud.google.com/products/#product-launch-stages))



To enable these detectors, see [Enable or disable Container Threat Detection modules](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#enable-disable-modules).

## Container Threat Detection detectors

Container Threat Detection includes the following detectors:

Detector | Module | Description | Inputs to detection  
---|---|---|---  
Added Binary Executed | `ADDED_BINARY_EXECUTED` |  A binary that was not part of the original container image was executed.  If an added binary is executed by an attacker, it's a possible sign that an attacker has control of the workload and they are executing arbitrary commands.  Findings are classified as **Low** severity. |  The detector looks for a binary being executed that was not part of the original container image, or was modified from the original container image.   
Added Library Loaded | `ADDED_LIBRARY_LOADED` |  A library that was not part of the original container image was loaded.  If an added library is loaded, it's a possible sign that an attacker has control of the workload and they are executing arbitrary code.  Findings are classified as **Low** severity. |  The detector looks for a library being loaded that was not part of the original container image, or was modified from the original container image.   
Collection: Pam.d Modification ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `PAM_D_MODIFICATION` |  One of the binaries or configuration files in the `pam.d` directory was modified.  PAM is widely used for authentication in Linux. Attackers may modify the binaries or configuration files to establish persistent access.  This is a file monitoring detector and has [ specific GKE version requirements](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).  |  This detector watches for modifications of the PAM shared library files and related authorization config files.   
Command and Control: Steganography Tool Detected | `STEGANOGRAPHY_TOOL_DETECTED` |  A program was executed that is identified as a steganography tool commonly found in Unix-like environments, indicating a potential attempt to conceal communication or data transfer.  Attackers might utilize steganographic techniques to embed malicious command and control (C2) instructions or exfiltrated data within seemingly benign digital files, aiming to evade standard security monitoring and detection. Identifying the use of such tools is crucial for uncovering hidden malicious activity.  Findings are classified as **Critical** severity. |  This detector monitors for the execution of known steganography tools. The presence of such tools suggests a deliberate effort to obfuscate network traffic or exfiltrate data, potentially establishing covert communication channels for malicious purposes.   
Credential Access: Access Sensitive Files On Nodes ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `ACCESS_SENSITIVE_FILES_ON_NODES` |  A program was executed that accessed `/etc/shadow` or SSH `authorized_keys`.  Attackers may access authorization files to copy password hashes.  This is a file monitoring detector and has [ specific GKE version requirements](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).  |  The detector looks for accesses to sensitive system files such as `/etc/shadow` and SSH `authorized_keys` files.   
Credential Access: Find Google Cloud Credentials | `FIND_GCP_CREDENTIALS` |  A command was executed to search for Google Cloud private keys, passwords, or other sensitive credentials within the container environment.  An attacker can use stolen Google Cloud credentials to gain illegitimate access to sensitive data or resources within the targeted Google Cloud environment.  Findings are classified as **Low** severity. |  This detection monitors `find` or `grep` commands that are attempting to locate files that contain Google Cloud credentials.   
Credential Access: GPG Key Reconnaissance | `GPG_KEY_RECONNAISSANCE` |  A command was executed to search for GPG security keys.  An attacker can use stolen GPG security keys to gain unauthorized access to encrypted communications or files.  Findings are classified as **Critical** severity. |  This detector monitors `find` or `grep` commands that are trying to locate GPG security keys.   
Credential Access: Search Private Keys or Passwords | `SEARCH_PRIVATE_KEYS_OR_PASSWORDS` |  A command was executed to search for private keys, passwords, or other sensitive credentials within the container environment, indicating a potential attempt to harvest authentication data.  Attackers often search for credential files to gain unauthorized access to systems, escalate privileges, or move laterally within the environment. Detecting such activity is critical to preventing security breaches.  Findings are classified as **Low** severity. |  This detector monitors for known commands used to locate private keys, passwords, or credential files. The presence of such searches within a containerized environment may suggest reconnaissance efforts or an active compromise.   
Defense Evasion: Base64 ELF File Command Line | `BASE64_ELF_FILE_CMDLINE` |  A process was executed that contains an argument that is an ELF (Executable and Linkable Format) file.  If an encoded ELF file execution is detected, it is a signal that an attacker is trying to encode binary data for transfer to ASCII-only command lines. Attackers can use this technique to evade detection and run malicious code embedded in an ELF file.  Findings are classified as **Medium** severity. |  This detection monitors process arguments that contain `ELF` and are base64 encoded.   
Defense Evasion: Base64 Encoded Python Script Executed | `BASE64_ENCODED_PYTHON_SCRIPT_EXECUTED` |  A process was executed that contains an argument that is a base64 encoded python script.  If an encoded python script execution is detected, it is a signal that an attacker is trying to encode binary data for transfer to ASCII-only command lines. Attackers can use this technique to evade detection and run malicious code embedded in a python script.  Findings are classified as **Medium** severity. |  This detection monitors process arguments that contain various forms of `python -c` and are base64 encoded.   
Defense Evasion: Base64 Encoded Shell Script Executed | `BASE64_ENCODED_SHELL_SCRIPT_EXECUTED` |  A process was executed that contains an argument that is a base64 encoded shell script.  If an encoded shell script execution is detected, it is a signal that an attacker is trying to encode binary data for transfer to ASCII-only command lines. Attackers can use this technique to evade detection and run malicious code embedded in a shell script.  Findings are classified as **Medium** severity. |  This detection monitors process arguments to find any that contain various forms of shell command that are base64 encoded.   
Defense Evasion: Disable or Modify Linux Audit System ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `DISABLE_OR_MODIFY_LINUX_AUDIT_SYSTEM` |  One of the audit system configuration or logging files was modified.  This is a file monitoring detector and has [ specific GKE version requirements](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).  |  This detector monitors for modifications to logging configurations, such as changes to configuration files or specific commands, as well as the disabling of logging services like `journalctl` or `auditctl`.   
Defense Evasion: Launch Code Compiler Tool In Container | `LAUNCH_CODE_COMPILER_TOOL_IN_CONTAINER` |  A process was initiated to launch a code compiler tool within the container environment, indicating a potential attempt to build or modify executable code in an isolated context.  Attackers might use code compilers within containers to develop malicious payloads, inject code into existing binaries, or create tools to bypass security controls, all while operating in a less scrutinized environment to evade detection on the host system.  Findings are classified as **Low** severity. |  This detector monitors for the execution of known code compiler tools inside containers. The presence of such activity suggests a potential effort to perform malicious code development or modification within the container, possibly as a defense evasion tactic to tamper with system components or client software.   
Command and Control: Piped Encoded Download | `PIPED_ENCODED_DOWNLOAD` |  The output of a network tool like `curl` or `wget` was piped to a `base64 --decode` command.  Attackers use this technique to download and decode obfuscated payloads in a single step, potentially bypassing security measures that only inspect the initial download command.  Findings are classified as **Medium** severity. |  This detector monitors for network tool output being piped directly to the `base64 --decode` command.   
Command and Control: Piped Encoded Code Execution Detected | `PIPED_ENCODED_CODE_EXECUTION` |  The output of `base64 --decode` command was piped directly to a shell interpreter (e.g., `python`, `bash`).  This is a strong indicator of malicious activity, where obfuscated code is decoded and executed immediately without being written to disk, evading file-based detection.  Findings are classified as **High** severity. |  This detector monitors for the output of the `base64 --decode` command being piped directly to common interpreters.   
Defense Evasion: Root Certificate Installed ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `ROOT_CERTIFICATE_INSTALLED` |  A root certificate was installed on the node.  Adversaries may install a root certificate to avoid security alerts when establishing connections to their malicious web servers. Attackers can carry out man-in-the-middle attacks, intercepting sensitive data exchanged between the victim and the adversary's servers, without triggering any warnings.  This is a file monitoring detector and has [ specific GKE version requirements](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).  |  This detector monitors modifications to the root certificate file.   
Execution: Added Malicious Binary Executed | `ADDED_MALICIOUS_BINARY_EXECUTED` |  A binary that meets the following conditions was executed:

  * Identified as malicious based on threat intelligence
  * Not part of the original container image

If an added malicious binary is executed, it's a strong sign that an attacker has control of the workload and they are executing malicious software.  Findings are classified as **Critical** severity. |  The detector looks for a binary being executed that was not part of the original container image, and was identified as malicious based on threat intelligence.   
Execution: Added Malicious Library Loaded | `ADDED_MALICIOUS_LIBRARY_LOADED` |  A library that meets the following conditions was loaded:

  * Identified as malicious based on threat intelligence
  * Not part of the original container image

If an added malicious library is loaded, it's a strong sign that an attacker has control of the workload and they are executing malicious software.  Findings are classified as **Critical** severity. |  The detector looks for a library being loaded that was not part of the original container image, and was identified as malicious based on threat intelligence.   
Execution: Added Malicious Skill Executed | `ADDED_MALICIOUS_SKILL_EXECUTED` |  A skill that meets the following conditions was executed:

  * Identified as malicious based on threat intelligence
  * Not part of the original container image

If an added malicious skill is executed, it's a strong sign that an attacker has control of the workload and they're executing malicious software.  Findings are classified as **Critical** severity. |  The detector looks for a skill being executed that was not part of the original container image and was identified as malicious based on threat intelligence.   
Execution: Added Malicious Skill Loaded | `ADDED_MALICIOUS_SKILL_LOADED` |  A skill that meets the following conditions was loaded:

  * Identified as malicious based on threat intelligence
  * Not part of the original container image

If an added malicious skill is loaded, it's a strong sign that an attacker has control of the workload and they're executing malicious software.  Findings are classified as **Critical** severity. |  The detector looks for a skill being loaded that was not part of the original container image, and was identified as malicious based on threat intelligence.   
Execution: Built in Malicious Binary Executed | `BUILT_IN_MALICIOUS_BINARY_EXECUTED` |  A binary that meets the following conditions was executed:

  * Identified as malicious based on threat intelligence
  * Included in the original container image

If a built in malicious binary is executed, it's a sign that the attacker is deploying malicious containers. They may have gained control of a legitimate image repository or container build pipeline and injected a malicious binary into the container image.  Findings are classified as **Critical** severity. |  The detector looks for a binary being executed that was included in the original container image, and was identified as malicious based on threat intelligence.   
Execution: Built-in Malicious Skill Executed | `BUILT_IN_MALICIOUS_SKILL_EXECUTED` |  A skill that meets the following conditions was executed:

  * Identified as malicious based on threat intelligence
  * Included in the original container image

If a built-in malicious skill is executed, it's a sign that the attacker is deploying malicious containers. They might have gained control of a legitimate image repository or container build pipeline and injected a malicious skill into the container image.  Findings are classified as **Critical** severity. |  The detector looks for a skill being executed that was included in the original container image, and was identified as malicious based on threat intelligence.   
Execution: Container Escape | `CONTAINER_ESCAPE` |  A process was executed within the container that attempted to break out of the container's isolation, potentially giving the attacker access to the host system.  If a container escape attempt is detected, it might indicate that an attacker is exploiting vulnerabilities to break out of the container. As a result, the attacker might gain unauthorized access to the host system or broader infrastructure, compromising the entire environment.  Findings are classified as **Critical** severity. |  The detector monitors for processes attempting to exploit container boundaries that use known escape techniques or binaries. These processes are flagged by threat intelligence as potential attacks that target the underlying host system.   
Execution: Fileless Execution in /memfd: | `FILELESS_EXECUTION_DETECTION_MEMFD` |  A process was executed using an in-memory file descriptor.  If a process is launched from an in-memory file, it may indicate that an attacker is trying to bypass other methods of detection in order to execute malicious code.  Findings are classified as **High** severity. |  The detector monitors for processes that are executed from `/memfd:`.   
Execution: Ingress Nightmare Vulnerability Execution ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `INGRESS_NIGHTMARE_VULNERABILITY_EXPLOITATION` |  Execution of [CVE-2025-1974](https://nvd.nist.gov/vuln/detail/CVE-2025-1974) can be detected by monitoring for Nginx executions with arguments that include references to the `/proc` file system in the `ingress-nginx` container indicating a potential remote code execution.  This class of vulnerabilities can allow malicious actors to execute arbitrary code within the `ingress-nginx` controller, potentially leading to the exposure of sensitive Kubernetes [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/) Findings are classified as **Medium** severity. |  This detector monitors the `ingress-nginx` container for Nginx executions that have arguments that include references to the `/proc` file system indicating potential remote code execution.   
Execution: Kubernetes Attack Tool Execution | `KUBERNETES_ATTACK_TOOL_EXECUTION` |  A Kubernetes-specific attack tool was executed within the environment, which can indicate that an attacker is targeting Kubernetes cluster components.  If an attack tool is executed within the Kubernetes environment, it can suggest that an attacker has gained access to the cluster and is using the tool to exploit Kubernetes-specific vulnerabilities or configurations.  Findings are classified as **Critical** severity. |  The detector looks for Kubernetes attack tools that are being executed and are identified as potential threats based on intelligence data. The detector triggers alerts to mitigate potential compromises in the cluster.   
Execution: Local Reconnaissance Tool Execution | `LOCAL_RECONNAISSANCE_TOOL_EXECUTION` |  A local reconnaissance tool not typically associated with the container or environment was executed, suggesting an attempt to gather internal system information.  If a reconnaissance tool is executed, it suggests that the attacker may be trying to map out the infrastructure, identify vulnerabilities, or collect data on system configurations to plan their next steps.  Findings are classified as **Critical** severity. |  The detector monitors for known reconnaissance tools being executed within the environment, identified through threat intelligence, which can indicate preparation for more malicious activities.   
Execution: Malicious Python executed | `MALICIOUS_PYTHON_EXECUTED` |  A machine learning model identified the specified Python code as malicious. Attackers can use Python to transfer tools or other files from an external system into a compromised environment and execute commands without binaries. **Note:** If you enable [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) for a specific location, then this detector can't be enabled and doesn't generate findings in that location.Findings are classified as **Critical** severity. |  The detector uses NLP techniques to evaluate the content of executed Python code. Because this approach is not based on signatures, detectors can identify known and novel Python.   
Execution: Modified Malicious Binary Executed | `MODIFIED_MALICIOUS_BINARY_EXECUTED` |  A binary that meets the following conditions was executed:

  * Identified as malicious based on threat intelligence
  * Included in the original container image
  * Modified from the original container image during the runtime

If a modified malicious binary is executed, it's a strong sign that an attacker has control of the workload and they are executing malicious software.  Findings are classified as **Critical** severity. |  The detector looks for a binary being executed that was originally included in the container image but modified during runtime, and was identified as malicious based on threat intelligence.   
Execution: Modified Malicious Library Loaded | `MODIFIED_MALICIOUS_LIBRARY_LOADED` |  A library that meets the following conditions was loaded:

  * Identified as malicious based on threat intelligence
  * Included in the original container image
  * Modified from the original container image during the runtime

If a modified malicious library is loaded, it's a strong sign that an attacker has control of the workload and they are executing malicious software. Findings are classified as **Critical** severity. |  The detector looks for a library being loaded that was originally included in the container image but modified during runtime, and was identified as malicious based on threat intelligence.   
Execution: Modified Malicious Skill Executed | `MODIFIED_MALICIOUS_SKILL_EXECUTED` |  A skill that meets the following conditions was executed:

  * Identified as malicious based on threat intelligence
  * Included in the original container image
  * Modified from the original container image during runtime

If a modified malicious skill is executed, it's a strong sign that an attacker has control of the workload and they're running malicious software.  Findings are classified as **Critical** severity. |  The detector looks for a skill being executed that was originally included in the container image but modified during runtime, and was identified as malicious based on threat intelligence.   
Execution: Modified Malicious Skill Loaded | `MODIFIED_MALICIOUS_SKILL_LOADED` |  A skill that meets the following conditions was loaded:

  * Identified as malicious based on threat intelligence
  * Included in the original container image
  * Modified from the original container image during runtime

If a modified malicious skill is loaded, it's a strong sign that an attacker has control of the workload and they're executing malicious software.  Findings are classified as **Critical** severity. |  The detector looks for a skill being loaded that was originally included in the container image but modified during runtime, and was identified as malicious based on threat intelligence.   
Execution: Netcat Remote Code Execution in Container | `NETCAT_REMOTE_CODE_EXECUTION_IN_CONTAINER` |  Netcat, a versatile networking utility, was executed within the container environment, potentially indicating an attempt to establish unauthorized remote access or exfiltrate data.  The use of Netcat in a containerized environment may signal an attacker's effort to create a reverse shell, enable lateral movement, or execute arbitrary commands, which can compromise system integrity. Findings are classified as **Low** severity. |  The detector monitors for Netcat execution within the container, because its use in production environments is uncommon and may signal an attempt to bypass security controls or execute remote commands.   
Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076) | `POSSIBLE_ARBITRARY_COMMAND_EXECUTION_THROUGH_CUPS` |  This rule detects the `footmatic-rip` process executing common shell programs, which may indicate that an attacker has exploited CVE-2024-47076. The `foomatic-rip` is a part of the OpenPrinting CUPS, an open source printing service that is a part of many Linux distributions. Most container images have this printing service disabled or removed. If this detection exists, please evaluate whether this is intended behavior or disable the service immediately.  Findings are classified as **Critical** severity. |  The detector looks for any `shell` process that is a child process of the `foomatic-rip` process.   
Execution: Possible Remote Command Execution Detected | `POSSIBLE_REMOTE_COMMAND_EXECUTION_DETECTED` |  A process was detected spawning common UNIX commands through a network socket connection, indicating a potential attempt to establish unauthorized remote command execution capabilities.  Attackers frequently utilize techniques that mimic reverse shells to gain interactive control over a compromised system, allowing them to execute arbitrary commands remotely and bypass standard network security measures like firewall restrictions. Detecting command execution over a socket is a strong indicator of malicious remote access.  Findings are classified as **Medium** severity. |  This detector monitors for the creation of network sockets followed by the execution of standard UNIX shell commands. This pattern suggests an attempt to create a covert channel for remote command execution, potentially enabling further malicious activities on the compromised host.   
Execution: Program Run with Disallowed HTTP Proxy Env | `PROGRAM_RUN_WITH_DISALLOWED_HTTP_PROXY_ENV` |  A program was executed with an HTTP proxy environment variable that is disallowed. This can indicate an attempt to bypass security controls, redirect traffic for malicious purposes, or exfiltrate data through unauthorized channels.  Attackers may configure disallowed HTTP proxies to intercept sensitive information, route traffic through malicious servers, or establish covert communication channels. Detecting the execution of programs with these environment variables is crucial for maintaining network security and preventing data breaches.  Findings are classified as **Low** severity. |  This detector monitors for the execution of programs with HTTP proxy environment variables that are specifically disallowed. The use of these proxies, particularly when unexpected, can signify malicious activity and warrants immediate investigation.   
Execution: Socat Reverse Shell Detected | `SOCAT_REVERSE_SHELL_DETECTED` |  The `socat` command has been used to create a reverse shell.  This rule detects the execution socat to create a reverse shell by redirecting stdin, stdout, and stderr file descriptors. This is a common technique used by attackers to gain remote access to a compromised system.  Findings are classified as **Medium** severity. |  The detector looks for any `shell` process that is the child process of a `socat` process.   
Execution: Suspicious Cron Modification ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `SUSPICIOUS_CRON_MODIFICATION` |  A `cron` configuration file was modified.  Modifications to `cron` jobs are a common tactic used by attackers to establish persistent access to systems. Attackers can leverage unauthorized changes to `cron` jobs to execute malicious commands at specific intervals, enabling them to maintain access and control over the system. Such modifications may go unnoticed and allow attackers to carry out stealthy activities over an extended period.  This is a file monitoring detector and has [ specific GKE version requirements](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).  |  This detector monitors `cron` configuration files for modifications.   
Execution: Suspicious OpenSSL Shared Object Loaded | `SUSPICIOUS_OPENSSL_SHARED_OBJECT_LOADED` |  OpenSSL has been executed to load a custom shared object.  Attackers may load custom libraries and replace existing libraries used by OpenSSL in order to run malicious code. Its use in production is uncommon and should warrant an immediate investigation.  Findings are classified as **Critical** severity. |  This detector monitors for the execution of the `openssl engine` command in order to load custom `.so` files.   
Exfiltration: Launch Remote File Copy Tools in Container | `LAUNCH_REMOTE_FILE_COPY_TOOLS_IN_CONTAINER` |  A remote file copy tool execution was detected within the container, indicating potential data exfiltration, lateral movement, or the deployment of malicious payloads.  Attackers often use these tools to transfer sensitive data outside of the container, move laterally within the network to compromise other systems, or introduce malware for further malicious activities. Detecting the use of remote file copy tools is crucial for preventing data breaches, unauthorized access, and further compromise of the container and potentially the host system. Findings are classified as **Low** severity. |  This detector monitors for the execution of known remote file copy tools within the container environment. Their presence, especially when unexpected, may indicate malicious activity.   
Impact: Detect Malicious Cmdlines | `DETECT_MALICIOUS_CMDLINES` |  A command was executed with arguments known to be potentially destructive, such as attempts to delete critical system files or modify password-related configurations.  Attackers may issue malicious command lines to cause system instability, prevent recovery by deleting essential files, or gain unauthorized access by manipulating user credentials. Detecting these specific command patterns is critical to preventing significant system impact.  Findings are classified as **Critical** severity. |  This detector monitors for the execution of command-line arguments that match patterns associated with system damage or privilege escalation. The presence of such commands indicates a potential active attempt to negatively impact the availability or security of the system.   
Impact: Remove Bulk Data From Disk | `REMOVE_BULK_DATA_FROM_DISK` |  A process was detected performing bulk data deletion operations, which may indicate an attempt to erase evidence, disrupt services, or execute a data-wiping attack within the container environment.  Attackers may remove large volumes of data to cover their tracks, sabotage operations, or prepare for ransomware deployment. Detecting such activity helps in identifying potential threats before critical data loss occurs.  Findings are classified as **Low** severity. |  The detector monitors for commands and processes associated with bulk data deletion, or other data-wiping tools, to identify suspicious activity that can compromise system integrity.   
Impact: Suspicious crypto mining activity using the Stratum Protocol | `SUSPICIOUS_CRYPTO_MINING_ACTIVITY_USING_STRATUM_PROTOCOL` |  A process was detected communicating over the Stratum protocol, which is commonly used by cryptocurrency mining software. This activity suggests potential unauthorized mining operations within the container environment.  Attackers often deploy crypto miners to exploit system resources for financial gain, leading to degraded performance, increased operational costs, and potential security risks. Detecting such activity helps mitigate resource abuse and unauthorized access.  Findings are classified as **High** severity. |  This detector monitors for known Stratum protocol usage within the environment. Because legitimate container workloads typically don't use Stratum, its presence may indicate unauthorized mining operations or a compromised container.   
Malicious Script Executed | `MALICIOUS_SCRIPT_EXECUTED` |  A machine learning model identified the specified Bash code as malicious. Attackers can use Bash to transfer tools or other files from an external system into a compromised environment and execute commands without binaries.  **Note:** If you enable [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) for a specific location, then this detector can't be enabled and doesn't generate findings in that location.Findings are classified as **Critical** severity. |  The detector uses NLP techniques to evaluate the content of executed Bash code. Because this approach is not based on signatures, detectors can identify known and novel malicious bash.   
Malicious URL Observed | `MALICIOUS_URL_OBSERVED` |  Container Threat Detection observed a malicious URL in the argument list of a running process.  Findings are classified as **Medium** severity. |  The detector checks URLs that are observed in the argument list of running processes against the lists of unsafe web resources that are maintained by the Google [ Safe Browsing](https://developers.google.com/safe-browsing) service. If a URL is incorrectly classified as phishing or malware, report it at [ Reporting Incorrect Data](https://developers.google.com/safe-browsing/v4/reporting).   
Persistence: Modify ld.so.preload ([Preview](https://cloud.google.com/products/#product-launch-stages)) | `MODIFY_LD_SO_PRELOAD` |  An attempt was made to modify the `ld.so.preload` file.  Changes to `ld.so.preload` can be used by attackers to preload malicious shared libraries into a system's library set. An attacker can use this to hijack the execution flow by loading their own libraries during program execution, potentially leading to privilege escalation or evasion of defense mechanisms.  This is a file monitoring detector and has [ specific GKE version requirements](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#gke-version).  |  This detector monitors attempts to modify the ld.so.preload file.   
Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287) | `ABUSE_SUDO_FOR_PRIVILEGE_ESCALATION` |  `sudo` has been executed with arguments that attempt to elevate privileges.  This detection notifies an attempt of the exploitation of CVE-2019-14287, which allows privilege escalation through abusing the sudo command. `sudo` versions prior to v1.8.28 had an exploit that allowed a non-root user to gain root privileges.  Findings are classified as **Critical** severity. |  The detector looks for any `sudo` execution that has arguments `-u#-1` or `-u#4294967295`.   
Privilege Escalation: Fileless Execution in /dev/shm | `FILELESS_EXECUTION_DETECTION_SHM` |  A process has been executed from a path within `/dev/shm`.  Executing a file from `/dev/shm`, an attacker can execute malicious code from this directory to evade detection by security tools, allowing them to carry out privilege escalation or process injection attacks.  Findings are classified as **High** severity. |  The detector looks for any process that has been executed from `/dev/shm`  
Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034) | `POLKIT_LOCAL_PRIVILEGE_ESCALATION_VULNERABILITY` |  A non-root user has executed `pkexec` with environment variables that attempt to escalate privileges.  This rule detects an attempt to exploit a privilege escalation vulnerability (CVE-2021-4034) in Polkit's `pkexec`. By running specially crafted code, a non-root user can use this flaw to gain root privileges on a compromised system.  Findings are classified as **Critical** severity. |  The detector looks for any `pkexec` execution that has the environment variable `GCONV_PATH` set.   
Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156) | `SUDO_POTENTIAL_PRIVILEGE_ESCALATION` |  A non-root user has executed `sudo` or `sudoedit` with a pattern of arguments that attempt to escalate privileges.  Detects an attempt to exploit a vulnerability affecting `sudo` versions 1.9.5p2 and earlier. Executing `sudo` or `sudoedit` with certain arguments, including one that ends with a single backslash character, as an unprivileged user can elevate the user's privileges to that of a root user.  Findings are classified as **Critical** severity. |  The detector looks for any `sudo` or `sudoedit` execution attempting to use arguments identified as a part of the CVE-2021-4034 exploit.   
Reverse Shell | `REVERSE_SHELL` |  A process started with stream redirection to a remote connected socket.  With a reverse shell, an attacker can communicate from a compromised workload to an attacker-controlled machine. The attacker can then command and control the workload—for example, as part of a botnet.  Findings are classified as **Critical** severity. |  The detector looks for `stdin` bound to a remote socket.   
Unexpected Child Shell | `UNEXPECTED_CHILD_SHELL` |  A process that does not normally invoke shells spawned a shell process. Findings are classified as **Critical** severity. |  The detector monitors all process executions. When a shell is invoked, the detector generates a finding if the parent process is known to not typically invoke shells.   
  
#### Modules for reporting environment variables and CLI arguments in findings

The following modules let you include or exclude environment variables and CLI arguments in Container Threat Detection findings.

  * Report environment variables (`REPORT_ENVIRONMENT_VARIABLES`)
  * Report CLI arguments (`REPORT_CLI_ARGUMENTS`)



For instructions, see the following:

  * [Exclude environment variables from Container Threat Detection findings](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#exclude-env-vars-ktd-findings).
  * [Exclude CLI arguments from Container Threat Detection findings](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#exclude-cli-args).



## What's next

  * Learn about [using Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection).
  * Learn about [testing Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-test-container-threat-detection).
  * Learn how to [investigate and develop response plans](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) for threats.
  * Learn about [Artifact Analysis and vulnerability scanning](https://docs.cloud.google.com/container-registry/docs/container-analysis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
