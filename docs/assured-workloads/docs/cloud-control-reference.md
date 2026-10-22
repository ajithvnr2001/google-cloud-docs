---
url: https://docs.cloud.google.com/assured-workloads/docs/cloud-control-reference/
title: Assured Workloads cloud controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:14.051944+00:00
---

# Assured Workloads cloud controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/cloud-control-reference/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Assured Workloads cloud controls

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Applicable only for[Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview)_

This page provides reference content for the built-in cloud controls that are included in Assured Workloads frameworks. Cloud controls can apply to folders or projects.

## Google Cloud cloud controls

###  Activate Security Command Center

Activate Security Command Center to evaluate security and data attack surfaces and help mitigate and remediate risks related to misconfigurations, vulnerabilities, and threats.

Enforcement mode | Audit   
---|---  
Finding category | `SCC_NOT_ACTIVATED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To activate Security Command Center, see [Overview of activating Security Command Center](https://cloud.google.com/security-command-center/docs/activate-scc-overview).

###  Activate Security Command Center for Continuous Monitoring

Use Security Command Center to define security policies and deploy and monitor them.

Enforcement mode | Audit   
---|---  
Finding category | `SECURITY_COMMAND_CENTER_NOT_ACTIVATED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Activate [Security Command Center](https://cloud.google.com/security-command-center/docs/security-command-center-overview).

  * Create and deploy frameworks with cloud controls that align with your security policies.

  * [Review and resolve findings](https://cloud.google.com/security-command-center/docs/review-manage-findings).

  * Integrate with notification channels such as [email and chat](https://cloud.google.com/security-command-center/docs/how-to-enable-real-time-notifications).




###  Allocate Audit Log Storage Capacity

Allocate sufficient audit log storage capacity to accommodate audit logs

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `INSUFFICIENT_AUDIT_LOG_STORAGE`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Verify that you can [see audit logs](https://cloud.google.com/logging/docs/audit/understanding-audit-logs#viewing_audit_logs).

  * Verify that logs are being exported to the Cloud Storage bucket.

  * Verify the retention period for your [log buckets](https://cloud.google.com/logging/docs/buckets).

  * Verify log storage capacity. In the console, got to **Logging > Metrics** and enter the following: ` custom.googleapis.com/log_storage_capacity `

  * Verify the [alerting policy](https://cloud.google.com/monitoring/alerts/manage-alerts#view-details) for low log storage in your bucket.

  * Verify that [storage capacity is sufficient](https://cloud.google.com/storage/docs/getting-bucket-size) for the Cloud Storage bucket (the usage is less than 90%).

  * Review the [bucket retention period](https://cloud.google.com/logging/docs/buckets#custom-retention) to ensure that regular review and adjustment of log storage capacity is complete.




###  Allow Only IL5 Compliant APIs for Gemini Enterprise Agent Platform

Restrict your folder or project to permit only Gemini Enterprise Agent Platform APIs that are compliant with Impact Level 5 (IL5).

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `GEMINI_ENTERPRISE_AGENT_PLATFORM_ALLOW_IL5_COMPLIANT_APIS`  
Category name in the API | CC_CATEGORY_INFRASTRUCTURE  
Revision number |  1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/vertexai.allowOnlyIL5CompliantAPIs`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `vertexai.allowOnlyIL5CompliantAPIs` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Allow Only ITAR Compliant APIs for Gemini Enterprise Agent Platform

Restrict your folder or project to permit only Gemini Enterprise Agent Platform APIs that are compliant with International Traffic in Arms Regulations (ITAR).

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `GEMINI_ENTERPRISE_AGENT_PLATFORM_ALLOW_ITAR_COMPLIANT_APIS`  
Category name in the API | CC_CATEGORY_INFRASTRUCTURE  
Revision number |  1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/vertexai.allowOnlyITARCompliantAPIs`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `vertexai.allowOnlyITARCompliantAPIs` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Apply Security Engineering Principles

Apply system security and privacy engineering principles in the specification, design, development, implementation, and modification of the system components.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_SECURITY_ENGINEERING_PRINCIPLES`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Address security requirements when building and applying security engineering principles to new development and operations of its data and information systems.

  * Include defense in depth at every phase of your system development life cycle, secure coding, security control tailoring, threat modeling, and risk management of your data and information system.




###  Assess Actions that Don't Require Identification or Authentication

Allow specific user actions without identification or authentication if they are deemed unnecessary, such as accessing public websites. The exception applies when identification and authentication have not occurred, not when they are simply not repeated.

Enforcement mode | Audit   
---|---  
Finding category | `ACTIONS_WITHOUT_IDENTIFICATION_AUTHENTICATION`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Review permissions assigned to service accounts, users, and roles.

  * [Monitor service accounts](https://cloud.google.com/iam/docs/service-account-usage-tools), especially those with elevated privileges.

  * Review IAM allow policies to ensure only authorized entities have necessary permissions.

  * Review [external IP addresses](https://cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#list_ip) and [firewall rules](https://cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-insights-recommendation-hub) to help prevent unauthorized access.

  * Identify the user actions that don't require identification or authentication.

  * Review system designs and use cases to understand the scenarios.

  * Evaluate potential risks and impact for exemption.

  * Document your rationale for exemptions.

  * Identify the security controls to mitigate potential risks.

  * Align exemptions with your organization's compliance requirements.




###  Assess the Availability of Compute and GKE Resources

Protect the availability of Compute VM instances and Google Kubernetes Engine (GKE) containers by allocating sufficient resources based on priority, quota, and security safeguards.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_RESOURCE_ASSESSMENT`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Use Cloud Monitoring and other [observability tools](https://cloud.google.com/stackdriver/docs) to monitor for demand and performance.

  * In the [Cloud Monitoring dashboard](https://cloud.google.com/monitoring/dashboards), review the VM configuration.

  * Review deployment scripts and orchestration tools to confirm that they allocate resources as intended.

  * Review [GKE system metrics](https://cloud.google.com/monitoring/api/metrics_kubernetes) for resource allocations.




###  Assign Correct Bucket Label

Bucket labels let you create key:value pairs that are stored as part of the bucket's metadata. You can use these labels to help identify the purpose of the bucket to your organization.

Enforcement mode | Audit   
---|---  
Finding category | `BUCKET_LABEL_INCORRECT`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set correct label for Cloud Storage buckets. For more information, see [Add, modify, or remove a bucket's labels](https://cloud.google.com/storage/docs/using-bucket-labels#set-label).

###  Assign Redis Role at Project Level

Assign the Redis Identity and Access Management (IAM) roles at the project level. Redis IAM roles assigned at the organization or folder level are overly broad. This control checks the IAM allow policy in the resource metadata for principals that are assigned roles/redis.admin, roles/redis.editor, roles/redis.viewer at the organization or folder level.

Enforcement mode | Detective   
---|---  
Severity | `MEDIUM`  
Finding category | `REDIS_ROLE_USED_ON_ORG`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

In the Google Cloud console, go to the **IAM** page and remove Redis IAM roles from the organization or folder level and add them on individual projects. For more information, see [Manage access to projects, folders, and organizations](https://cloud.google.com/iam/docs/granting-changing-revoking-access).

###  Authorize and Monitor Privileged Remote Access

Authorize the use of privileged commands execution and access to security information through remote access.

Enforcement mode | Audit   
---|---  
Finding category | `PRIVILEGED_REMOTE_ACCESS_NOT_AUTHORIZED_MONITORED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Create custom roles for privileged access or consider [temporary elevated access](https://cloud.google.com/iam/docs/temporary-elevated-access).

  * Grant only specific roles to service accounts for automated systems that require remote access.

  * Use SSH for remote access to VMs.

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit) for services that store sensitive data.

  * [Configure VPC Flow Logs](https://cloud.google.com/vpc/docs/using-flow-logs) to capture network traffic.

  * Enable [Binary Authorization](https://cloud.google.com/binary-authorization/docs/overview) to enforce policies when deploying images.

  * Use [Secret Manager](https://cloud.google.com/secret-manager/docs/overview) to create and store secrets.

  * Configure [alerting policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for unusual or unauthorized activities.




###  Authorize Wireless Access to Production Systems

Authorize wireless access to applications in production environments.

Enforcement mode | Audit   
---|---  
Finding category | `WIRELESS_ACCESS_PRODUCTION_SYSTEMS_NOT_AUTHORIZED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Establish configuration requirements, connection requirements, and implementation guidance for each type of wireless access to your systems. Authorize wireless access to your systems before you allow such connections.

###  Automate Account Management System

Ensure that you have IAM policy structures to automate IAM role assignments based on resources and context-specific conditions.

Enforcement mode | Audit   
---|---  
Finding category | `ACCOUNT_MANAGEMENT_SYSTEMS_NOT_SUPPORTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To retrieve log entries, see [List log entries](https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list).

To get a ServiceAccount, see [Get a ServiceAccount](https://cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/get).

To get the definition of a role, see [Get Role Definition](https://cloud.google.com/iam/docs/reference/rest/v1/roles/get).

###  Automate Integrity Verification

Employ integrity verification tools to detect unauthorized changes to your software, firmware, and information.

Enforcement mode | Audit   
---|---  
Finding category | `IMPROPER_INTEGRITY_VERIFICATION_MECHANISMS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Configure your OS Policy to perform integrity verification. For more information, see [OS policy and OS policy assignment](https://cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#os-policy), [Create an OS policy assignment](https://cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment), and [Manage OS policy assignments](https://cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy).

  * Create custom tools that regularly check the integrity of software and configurations.




###  Automate Near Real-time Event Analysis

Use automated tools to support near real-time analysis of events.

Enforcement mode | Audit   
---|---  
Finding category | `REAL_TIME_EVENT_ANALYSIS_NOT_AUTOMATED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement automated real-time event analysis:

  * Use [Cloud Monitoring](https://cloud.google.com/monitoring/docs) and [Cloud Logging](https://cloud.google.com/logging/docs) to collect, monitor, and analyze event data, such as system and application logs, performance metrics, and other relevant information.

  * Create [custom monitoring metrics](https://cloud.google.com/monitoring/custom-metrics/creating-metrics) in Cloud Monitoring to track specific parameters that are critical.

  * Set up [alerting policies](https://cloud.google.com/monitoring/alerts) in Cloud Monitoring to receive notifications when metrics or logs indicate unusual or unauthorized activities.

  * Use Pub/Sub to create topics and subscriptions for real-time event processing. For more information, see [Publish message overview](https://cloud.google.com/pubsub/docs/publish-message-overview) and [Subscription overview](https://cloud.google.com/pubsub/docs/subscription-overview).




###  Avoid RSASHA1 for DNSSEC Signing

Don't use the RSASHA1 algorithm for key signing when enabling DNSSEC for Cloud DNS zones.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `RSASHA1_FOR_SIGNING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Replace the algorithm. For more information, see [Using advanced signing options](https://cloud.google.com/dns/docs/dnssec-advanced#advanced-signing-options).

###  BigQuery compliance settings

BigQuery compliance settings

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `BIGQUERY_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Parameters

`framework` |  `STRING` Required.  
---|---  
  
###  Block Administrator Roles from Service Accounts

A service account with Administrator, Owner, or Editor privileges has broad access to your Google Cloud environment, which can impact its security.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ADMIN_SERVICE_ACCOUNT`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **IAM policy** page in the Google Cloud console, click **Edit principal** , and remove the excessive role or roles.

###  Block Automatic IAM Grants to Default Service Accounts

Use the "Disable Automatic IAM Grants for Default Service Accounts" (iam.automaticIamGrantsForDefaultServiceAccounts) organization policy constraint to prevent automatic role grants to default service accounts.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_AUTOMATIC_IAM_GRANTS_TO_DEFAULT_SERVICE_ACCOUNTS_ENABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To disable the automatic role grant, see [Disable automatic role grants to default service accounts](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants).

###  Block Default VPC Network for Agent Platform Workbench Instances

Don't create Gemini Enterprise Agent Platform Workbench Instances in the default VPC network to help prevent the use of its over-permissive default firewall rules.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_WORKBENCH_DEFAULT_VPC_NETWORK_USED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't change the network on an Agent Platform Workbench Instance after it's created. Delete the existing instances, create another VPC network, and create new instances that use the new VPC network.

  1. Delete the instances. For instructions to shut down the instance before deleting it, see [Shut down an Agent Platform Workbench instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/shut-down).

  2. Create a VPC network and subnet for the project. For instructions, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). For information about Agent Platform Workbench networking requirements, see [Network configuration options](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create#network-options).

  3. Create the instances. For instructions, see [Create an Agent Platform Workbench Instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/create). In the **Networking** section, select the VPC network and subnet that you created.




###  Block External IP Address Access on Compute Engine VM Instances

Use the "Define allowed external IPs for VM instances" (compute.vmExternalIpAccess) organization policy constraint to block public access to your VMs.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `ORG_POLICY_EXTERNAL_IP_ACCESS_ALLOWED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To block external IP addresses on Compute Engine VM instances, see [Restrict external IP addresses to specific instances](https://cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip).

###  Block File Downloading in JupyterLab Console

Don't permit file downloading from the JupyterLab console in Workbench instances to reduce data exfiltration risks and help prevent malware distribution.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `VERTEX_AI_JUPYTERLAB_FILE_DOWNLOADING_ENABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn off file downloading for the instance.

  1. In the Google Cloud console, go to the [**Instances** page](https://console.cloud.google.com/vertex-ai/workbench/instances).

  2. Click the instance that you want to configure.

  3. In the **Software and security** tab, add the `notebook-disable-downloads` metadata key and set the value to `TRUE`.




For more information, see [Update an instance's metadata](https://cloud.google.com/vertex-ai/docs/workbench/instances/manage-metadata#update).

###  Block Generic Access to Cassandra Ports

Block connections on TCP ports 7000, 70001, 7199, 8888, 9042, 9160, 61620, and 61621 from all IP addresses to help prevent unwanted traffic and attacks on Apache Cassandra services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_CASSANDRA_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:7000`, `tcp:70001`, `tcp:7199`, `tcp:8888`, `tcp:9042`, `tcp:9160`, `tcp:61620`, and `tcp:61621` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to CiscoSecure/WebSM Ports

Block incoming connections on TCP port 9090 from all IP addresses to help prevent undesired traffic and attacks on CiscoSecure/WebSM services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_CISCOSECURE_WEBSM_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:9090` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to Directory Service Ports

Block incoming connections on TCP port 445 or UDP port 445 from all IP addresses to help prevent undesired traffic and attacks on Directory Services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_DIRECTORY_SERVICES_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:445` and `udp:445` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to DNS Ports from All IP Addresses

Block incoming connections on TCP port 53 or UDP port 53 from all IP addresses to help prevent undesired traffic and attacks on DNS services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_DNS_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:53` and `udp:53` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to Elasticsearch Ports from All IP Addresses

Block incoming connections on TCP ports 9200 and 9300 from all IP addresses to help prevent undesired traffic and attacks on Elasticsearch services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_ELASTICSEARCH_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:9200` and `tcp:9300` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to FTP Ports

Block incoming connections on TCP port 21 from all IP addresses to help prevent undesired traffic and attacks on FTP services. This control doesn't apply to GKE firewalls.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_FTP_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:21` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to HTTP Ports

Block incoming connections on TCP port 80 from all IP addresses to help prevent undesired traffic and attacks on HTTP services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_HTTP_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:80` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to LDAP Ports

Block incoming connections on TCP ports 389 and 636 and UDP port 389 from all IP addresses to help prevent undesired traffic and attacks on LDAP services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_LDAP_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:389`, `tcp:636`, and `udp:389` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to Memcached Ports

Block incoming connections on TCP ports 11211, 11214, and 11215 or UDP ports 11211, 11214, and 11215 from all IP addresses to help prevent undesired traffic and attacks on Memcached services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_MEMCACHED_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:11211`, `tcp:11214`, `tcp:11215`, `udp:11211`, `udp:11214`, and `udp:11215` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to MongoDB Ports

Block connections on TCP ports 27017, 27018, and 27019 from all IP addresses to help prevent undesired traffic and attacks on MongoDB services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_MONGODB_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:27017`, `tcp:27018` and `tcp:27019` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to MySQL Ports

Block incoming connections on TCP port 3306 from all IP addresses to help prevent undesired traffic and attacks on MySQL services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_MYSQL_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:3306` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to NetBIOS Ports from All IP Addresses

Block incoming connections from all IP addresses to TCP and UDP ports 137, 138, and 139 to help prevent undesired traffic and attacks on NetBIOS services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_NETBIOS_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to ports `tcp:137-139` and `udp:137-139` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to Oracle Database Ports

Block incoming connections on TCP ports 1521, 2483, and 2484 or UDP ports 2483 and 2484 from all IP addresses to help prevent undesired traffic and attacks on Oracle databases.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_ORACLEDB_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:1521`, `tcp:2483`, `tcp:2484`, `udp:2483`, and `udp:2484` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access these ports instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to POP3 Server Ports

Block incoming connections on TCP port 110 from all IP addresses to help prevent undesired traffic and attacks on POP3 services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_POP3_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:110` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access this port instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to PostgreSQL Server Ports from All IP Addresses

Block incoming connections on TCP port 5432 from all IP addresses to help prevent undesired traffic and attacks on PostgreSQL services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_POSTGRESQL_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:5432` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access this port instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to RDP Ports

Block incoming connections on TCP port 3389 or UDP port 3389 from all IP addresses to help prevent undesired traffic and attacks on RDP server.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_RDP_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Remove public access from the RDP port. Go to the **Firewall policies** page in the Google Cloud console and edit the firewall rule. Under **Source IP ranges** ; delete 0.0.0.0/0 and add specific IP addresses or IP ranges that you want to let connect to the instance. Select **TCP** and **UDP** , and enter port **3389** for both.

###  Block Generic Access to Redis Server Ports from All IP Addresses

Block incoming connections on TCP port 6379 from all IP addresses to help prevent undesired traffic and attacks on Redis services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_REDIS_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:6379` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access this port instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to SMTP Server Ports

Block incoming connections on TCP port 25 from all IP addresses to help prevent undesired traffic and attacks on SMTP services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_SMTP_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:25` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access this port instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Generic Access to SSH Ports

Block incoming connections on TCP port 22 or SCTP port 22 from all IP addresses to help prevent undesired traffic and attacks on SSH server.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_SSH_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Remove public access from the SSH port. Go to the **Firewall policies** page in the Google Cloud console and edit the firewall rule. Under **Source IP ranges** ; delete 0.0.0.0/0 and add specific IP addresses or IP ranges that you want to let connect to the instance. Select **TCP** and **SCTP** , and enter port **22** for both.

###  Block Generic Access to Telnet Servers

Block incoming connections on TCP port 23 from all IP addresses to help prevent undesired traffic and attacks on Telnet services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_TELNET_PORT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to deny access to port `tcp:23` from the source IP range `0.0.0.0/0`. Create a firewall rule that permits specific IP address ranges to access this port instead. For more information, see [Use VPC firewall rules](https://cloud.google.com/firewall/docs/using-firewalls).

###  Block Internet Access for Runtime Templates in Agent Platform Colab Enterprise

Don't permit internet access in runtime templates in Colab Enterprise on Gemini Enterprise Agent Platform to reduce the external attack surface and help prevent potential data exfiltration.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_RUNTIME_TEMPLATE_IDLE_SHUTDOWN_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't change this setting after the runtime template is created. Delete the existing runtime template and create a new one with internet access turned off.

  1. Delete the runtime template. For instructions, see [Delete a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template#delete).

  2. Create a runtime template. For instructions, see [Create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template). To turn off internet access, in the **Networking and security** section, clear **Enable public internet access**.




###  Block Internet Access for Runtime Templates in Agent Platform Colab Enterprise

Don't permit internet access in runtime templates in Colab Enterprise on Gemini Enterprise Agent Platform to reduce the external attack surface and help prevent potential data exfiltration.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_RUNTIME_TEMPLATE_INTERNET_ACCESS_ENABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't change this setting after the runtime template is created. Delete the existing runtime template and create a new one with internet access turned off.

  1. Delete the runtime template. For instructions, see [Delete a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template#delete).

  2. Create a runtime template. For instructions, see [Create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template). To turn off internet access, in the **Networking and security** section, clear **Enable public internet access**.




###  Block Legacy Authorization on GKE Clusters

Disable Legacy Authorization to use role-based access control (RBAC). RBAC helps improve security by defining specific permissions at the cluster and namespace levels.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `LEGACY_AUTHORIZATION_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Select the cluster, click **Edit** and select **Disabled** from the **Legacy Authorization** dropdown list.

###  Block Overly Permissive Firewall Rules

Firewall rules that permit connections from all IP addresses, like 0.0.0.0/0, or from all ports expose resources to attacks from unintended sources. This control creates a violation for ingress firewall rules with "allow" actions if one of the following items are true: First, the source ranges includes 0.0.0.0/0 and allowed protocols don't specify ICMP and TCP protocols with port 443. Second, the allowed rule permits all protocols or permits TCP or UDP protocols without port restrictions.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `OPEN_FIREWALL`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Firewall** page in the Google Cloud console. Click the firewall rule name, then click **Edit**. Edit the firewall rule to update access from the source IP range `0.0.0.0/0` and add specific protocols and port ranges. For more information, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).

###  Block Project-Wide SSH Keys on Compute Engine Instances

Project-wide SSH keys provide access to all VM instances within the project, which might lead to unauthorized access. This control reads the metadata from Compute Engine. It checks the metadata.items object for the key-value pair 'block-project-ssh-keys' set to 'TRUE', or for the presence of the 'sshKeys' key. This control doesn't apply to GKE instances, Dataflow jobs, or Windows instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `COMPUTE_PROJECT_WIDE_SSH_KEYS_ALLOWED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Block SSH keys on the VM instance. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console. Click the instance name in the finding. On the **VM instance details** page, click **Edit**. Under **SSH Keys** , select **Block project-wide SSH keys**. Note that you can't edit instances that are created using instance templates. To make changes to an instance template's configuration, see [How to update instance templates](https://docs.cloud.google.com/compute/docs/instance-templates#how_to_update_instance_templates).

###  Block Public IP Address for Agent Platform Workbench Instances

Don't permit external IP addresses for Gemini Enterprise Agent Platform Workbench Instances to reduce exposure to the internet and minimize the risk of unauthorized access.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_WORKBENCH_PUBLIC_IP_ENABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't change this setting after the Agent Platform Workbench Instance is created. Delete the existing instance and create instances with the appropriate IP configuration.

  1. Delete the instance. For instructions to shut down the instance before deleting it, see [Shut down an Agent Platform Workbench instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/shut-down).

  2. In the Google Cloud console, go to the [**Instances** page](https://console.cloud.google.com/agent-platform/workbench/instances).

  3. Create a new instance. In the **Networking** section, clear **Assign external IP address**.

  4. Consider setting the Define allowed external IPs for VM instances (`constraints/compute.vmExternalIpAccess`) organization policy constraint at the organization level to prevent VM instances from using external IP addresses. For more information, see [Restrict external IP addresses to specific instances](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip).




###  Block Public IP Addresses for AlloyDB Cluster Instances

AlloyDB for PostgreSQL database instances with private IP addresses help to reduce your organization's attack surface and improve network security.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOYDB_PUBLIC_IP`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **AlloyDB** > **Clusters** in the Google Cloud console. Click the cluster from the **Resource Name** column, and edit the instance. Go to **Connectivity** , and clear **Enable Public IP**.

###  Block Public IP Addresses for Cloud SQL Instances

Don't assign public IP addresses to Cloud SQL database instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_PUBLIC_IP`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console. Click **Connections** > **Networking** , and clear the **Public IP** checkbox for the instance. Use a private IP address instead. For more information, see [Configuring private IP for an existing instance](https://cloud.google.com/sql/docs/mysql/configure-private-ip#existing-private-instance).

###  Block Root Access on Agent Platform Workbench Instances

Don't permit root access on Gemini Enterprise Agent Platform Workbench Instances to help prevent unauthorized modification of critical system files or installation of malicious software.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `VERTEX_AI_WORKBENCH_ROOT_ACCESS_ENABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn off root access on the Agent Platform Workbench Instance.

  1. In the Google Cloud console, go to the [**Instances** page](https://console.cloud.google.com/agent-platform/workbench/instances).

  2. Click the instance that you want to configure.

  3. In the **Software and security** tab, clear the **Root access to the instance** setting.

  4. Click **Submit**.




###  Block Root Access on Agent Platform Workbench Instances

Use the "Disable root access on new Vertex AI Workbench user-managed notebooks and instances" `ainotebooks.disableRootAccess` organization policy constraint to help prevent newly created Gemini Enterprise Agent Platform Workbench user-managed notebooks and instances from enabling root access.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_ROOT_ACCESS_ON_VERTEXAI_ENABLED`  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Disable root access on new Vertex AI Workbench user-managed notebooks and instances** (`ainotebooks.disableRootAccess)` organization policy constraint to `true` to block root access on new Agent Platform Workbench user-managed notebooks and instances. For more information, see [Updating policies with boolean rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints).

###  Block Serial Ports for Compute Engine Instances

Serial console support on an instance poses a security risk as clients might connect from any IP address. Disabling serial ports helps protect from such exposures.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `COMPUTE_SERIAL_PORTS_ENABLED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Block serial ports. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console. Click the VM instance name listed in the finding. On the **VM instance details** page, click **Edit**. Under **Remote access** , turn off **Enable connecting to serial ports**.

###  Block Service Account Key Creation

Use the "Disable service account key creation" (iam.disableServiceAccountKeyCreation) organization policy constraint to prevent the creation of service account external keys and Cloud Storage HMAC keys.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_SERVICE_ACCOUNT_KEY_CREATION_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enforce the organization policy, see [Disable service account key creation](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation).

###  Block Service Account Key Uploads

Use the "Disable Service Account Key Upload" (iam.disableServiceAccountKeyUpload) organization policy constraint to prevent the upload of public keys to service accounts.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_SERVICE_ACCOUNT_KEY_UPLOAD_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enforce the organization policy, see [Disable service account key upload](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_upload_managed).

###  Block Terminal Access on Agent Platform Workbench Instances

Use the "Disable terminal on new Vertex AI Workbench instances" (ainotebooks.disableTerminal) organization policy constraint to help prevent the creation of Gemini Enterprise Agent Platform Workbench instances with the terminal enabled.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `TERMINAL_ACCESS_ON_VERTEXAI_ENABLED`  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Disable terminal on new Vertex AI Workbench instances** (`ainotebooks.disableTerminal`) organization policy constraint to `true` to block the terminal on new Agent Platform Workbench instances. For more information, see [Updating policies with boolean rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints).

###  Centrally Track Remediation of Vulnerabilities

Ensures a centralized system is in place for tracking the remediation of identified security vulnerabilities.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_CENTRALIZED_REMEDIATION_OF_VULNERABILITIES`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement a centralized system to track, prioritize, and manage the mitigation and remediation of identified vulnerabilities. This can be achieved by establishing a well-defined internal process that leverages Security Command Center for identification, prioritization, and verification. For more information about workflows, see the [Security Command Center documentation](https://cloud.google.com/security-command-center/docs).

###  Changes impacting CSC

Include provisions limiting changes directly impacting CSCs owned environments/tenants to explicitly authorized requests within service level agreements between CSPs and CSCs.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `MAINTENANCE_POLICY_NOT_CONFIGURED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Identify the resource type from the finding details. Go to the resource in Google Cloud Console and configure a maintenance policy or maintenance window. For guidance, refer to the maintenance documentation for Redis (https://cloud.google.com/memorystore/docs/redis/about-maintenance), Memcache (https://cloud.google.com/memorystore/docs/memcached/about-maintenance), GKE (https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), Cloud SQL (https://cloud.google.com/sql/docs/mysql/set-maintenance-window), or Cloud Composer (https://cloud.google.com/composer/docs/composer-2/specify-maintenance-windows).

###  Cloud Databases Context Store Regulatory Settings

Enforces that the Cloud Databases Context Store Regulatory Settings are configured correctly.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_DATABASES_CONTEXT_STORE_ENABLED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Cloud Databases Context Store Regulatory Settings 

###  CMEK Dedicated Project Restricted

Checking whether the Organization Policy constraints/gcp.restrictCmekCryptoKeyProjects is set.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `CMEK_PROJECT_NOT_RESTRICTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To restrict which projects can be used for CMEK crypto keys, configure the `constraints/gcp.restrictCmekCryptoKeyProjects` organization policy and add the project, folder, or organization IDs that are approved to host CMEK crypto keys to the `allowedValues` list of the policy. See https://cloud.google.com/kms/docs/cmek-org-policy for details.

###  CMEK Keys Imported and Stored In HSM

Verify whether the CMEKs have been imported to GCP, noting that the exact origin of these keys cannot be technically checked; also, confirm if the CMEKs are kept in an HSM within Google Cloud

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `CMEK_KEY_NOT_IMPORTED_OR_NOT_HSM`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that CMEK keys are imported into Cloud KMS (https://cloud.google.com/kms/docs/key-import) and are stored in a Hardware Security Module (HSM) by setting the protection level to 'HSM' (https://cloud.google.com/kms/docs/protection-levels).

###  CMEK Usage

Many Google Cloud services protect various types of data with Customer-Managed Encryption Keys (CMEKs) or offer encryption at rest, including: Vertex AI services such as Datasets, Models, Endpoints, CustomJobs, HyperparameterTuningJobs, TrainingPipelines, BatchPredictionJobs, ModelDeploymentMonitoringJobs, PipelineJobs, MetadataStore, TensorBoard, Featurestore, Index, IndexEndpoint, NotebookRuntimes, and NotebookExecutionJobs; Artifact Registry data in repositories; BigQuery data at rest; Bigtable data at rest and backups; Cloud Composer environment data; GCE instances, persistent regional disks, persistent disks, snapshots, custom images, and machine images; Google Kubernetes Engine data on VM disks and data in GKE backups; Dataflow pipeline state data; Dataproc Metastore data at rest; Document AI data at rest and in use; Cloud Logging data in the Log Router and Logging storage; Pub/Sub data associated with topics; Cloud Run functions (1st and 2nd gen, and 1st gen specifically); Secret Manager secrets and secret versions; Spanner data at rest and backups; Cloud SQL data written to databases, backups, and BackupRun configurations; data in storage buckets; AlloyDB clusters and backups; Apigee Instances, Organization Runtime, Organization Consumer Data, and Organization Control Plane; Cloud Data Fusion environment data; Dataform repositories; Datastream data in transit; Filestore data at rest and backups; Memorystore for Redis data at rest in Clusters; Speech-to-Text Config Data and Recogniser Data at rest; Workflows data at rest; Google Cloud NetApp Storage Pools and Volumes; and Cloud Workstations data on VM disks.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `CMEK_NOT_USED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

The resource is not encrypted with a Customer-Managed Encryption Key (CMEK). Configure CMEK encryption for the resource to meet compliance requirements. See https://cloud.google.com/kms/docs/cmek for more details on CMEK.

###  Conduct Role-specific Training

Ensure role-specific training is provided for high-risk roles.

Enforcement mode | Audit   
---|---  
Severity | `LOW`  
Finding category | `MISSING_ROLE_SPECIFIC_TRAINING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Mandate role-specific training for high-risk roles, in particular for roles with privileged access. Incorporate lessons learned from internal or external security incidents or breaches into role-based training.

###  Conduct Security Awareness Training

Ensure employees receive security awareness training.

Enforcement mode | Audit   
---|---  
Severity | `LOW`  
Finding category | `MISSING_SECURITY_AWARENESS_TRAINING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Continuously educate your employees on cybersecurity measures, testing them regularly to ensure their knowledge is satisfactory.

###  Configure a Wireless Intrusion Detection Mechanism

Employ a wireless intrusion detection system to identify rogue wireless devices and detect attack attempts and potential system breaches.

Enforcement mode | Audit   
---|---  
Finding category | `WIRELESS_INTRUSION_DETECTION_MECHANISM_NOT_CONFIGURED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

This control doesn't apply to Google Cloud as Google doesn't use or permit wireless networks in our production environment. Additionally, access to Google's data centers is highly restricted and all unused ports are disabled on switches. During the inspection process for unauthorized wireless devices, the Google Security Team walks through data centers to ensure connected devices are authorized and meet Google configuration management requirements. Verify that you have set up appropriate wireless intrusion detection systems in your environment, if applicable.

###  Configure Access Controls for the Network Boundary

Control external communication over the network using firewall rules.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_ACCESS_CONTROLS_NETWORK_BOUNDARY`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Verify these ports are blocked:



Cassandra: TCP 7000, 7001, 7199, 8888, 9042, 9160, 61620, 61621

CiscoSecure/WebSM: TCP 9090

Directory Services: TCP 445; UDP 445

DNS services: TCP 53; UDP 53

Elasticsearch: TCP 9200, 9300

FTP: TCP 21

HTTP: TCP 80

LDAP: TCP 389, 636; UDP 389

Memcached: TCP 11211, 11214, 11215; UDP 11211, 11214, 11215

MongoDB: TCP 27017-27019

MySQL: TCP 3306

NetBIOS13: TCP 137-139; UDP 137-139

OracleDB: TCP 1521, 2483, 2484; UDP 2483, 2484

POP3: TCP 110

PostgreSQL: TCP 5432

RDP: TCP 3389; UDP 3389

Redis: TCP 6379

SMTP: TCP 25

SSH: TCP 22; SCTP 22

Telnet: TCP 23

  * Verify SSL.

  * Verify NAT to instances without public IPs.

  * Configure logging and VPC Flow Logs.

  * Verify GKE network policy and Dataplane V2.

  * Verify VMs don’t have public IPs. For stopped instances, ensure network doesn’t permit external access.

  * Verify Compute Engine default service account isn’t used.




###  Configure Dataplex to Support Data Boundaries

Configure Dataplex to support data boundaries that help you meet your regulatory requirements.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `DATAPLEX_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Dataplex Compliance Settings 

#### Parameters

`framework` |  `STRING` Required. Ensures additional compliance setting for the underlying services are correctly configured to meet the compliance level of the selected framework.  
---|---  
  
###  Configure Dataproc to Support Data Boundaries

Configure Dataproc to support data boundaries that help you meet your regulatory requirements.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `DATAPROC_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Dataproc Compliance Settings 

###  Configure DLP API for Gemini on Agent Platform

Configure Data Loss Prevention (DLP) filters when using Gemini on Gemini Enterprise Agent Platform. DLP helps address sensitive data leakage, in case the Gemini on Agent Platform model has access to sensitive data. DLP also lets you create custom block lists.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `DLP_DATA_FILTERS_NOT_CONFIGURED_IN_VERTEX_AI`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For more information about using DLP for generative AI models like Gemini on Agent Platform, see [Safety in Agent Platform](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/safety-overview).

###  Configure Google Agent Platform to Support Data Boundaries

Configure Google Agent Platform to support data boundaries that help you meet your regulatory requirements.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `AGENT_PLATFORM_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Vertex AI Compliance Settings 

###  Configure Google Cloud Serverless for Apache Spark to Support Data Boundaries

Configure Google Cloud Serverless for Apache Spark to support data boundaries that help you meet your regulatory requirements.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `SERVERLESS_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Serverless Compliance Settings 

###  Configure Log Metrics and Alerts for Audit Logging Changes

Configure log metrics and alerts to monitor changes to IAM allow policies. Log metrics and alerts configured to monitor IAM allow policy changes helps to identify over-privileged users or suspicious activity.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `AUDIT_CONFIG_NOT_MONITORED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to **Logs-based Metrics** within the **Logging** page in the Google Cloud console. Click **Create metric**. In the **User-defined metrics** section, click inside the **Filter** box, select **Filter** , and paste the following text, replacing the existing text: ` resource.type=global AND protoPayload.methodName=SetIamPolicy AND protoPayload.serviceData.policyDelta.auditConfigDeltas:*` Click **Create metric** and set the alert policy.

###  Configure Log Metrics and Alerts for Cloud SQL Configuration Changes

Configure log metrics and alerts to monitor configuration changes for Cloud SQL instances. Monitoring changes helps detect misconfigurations.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SQL_INSTANCE_NOT_MONITORED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to **Logs-based Metrics** within the **Logging** page in the Google Cloud console. Click **Create metric**. In the **User-defined metrics** section, click inside the **Filter** box, select **Filter** , and paste the following text, replacing the existing text: `protoPayload.methodName=cloudsql.instances.update` Click **Create metric** and set the alert policy.

###  Configure Log Metrics and Alerts for Cloud Storage IAM Policy Changes

Log metrics and alerts configured to monitor Cloud Storage IAM permission changes helps to identify over-privileged users or suspicious activity.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `BUCKET_IAM_NOT_MONITORED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Log-based Metrics** page within **Logging** in the Google Cloud console. Click **Create metric** in the **User-defined metrics** section. In the **User-defined metrics** section, click inside the **Filter** box, select **Filter** , and paste the following text, replacing the existing text: ` resource.type=gcs_bucket AND protoPayload.methodName=storage.setIamPermissions` After you create the metric, go to the **Actions** menu and click **Create alert from metric** to set alert policies. For more information, see [Log-based metrics overview](https://cloud.google.com/logging/docs/logs-based-metrics).

###  Configure Log Metrics and Alerts for Custom Role Changes

Configure log metrics and alerts to monitor custom role changes. Monitoring role creation, deletion, and update activities helps to identify over-privileged roles at early stages.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `CUSTOM_ROLE_NOT_MONITORED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to **Logs-based Metrics** within the **Logging** page in the Google Cloud console. Click **Create metric**. In the **User-defined metrics** section, click inside the **Filter** box, select **Filter** , and paste the following text, replacing the existing text: ` resource.type=iam_role AND protoPayload.methodName=google.iam.admin.v1.CreateRole OR protoPayload.methodName=google.iam.admin.v1.DeleteRole OR protoPayload.methodName=google.iam.admin.v1.UpdateRole` Click **Create metric** and set the alert policy.

###  Configure Log Metrics and Alerts for VPC Network Changes

Configure log metrics and alerts to monitor VPC network changes. Monitoring network changes helps detect incorrect or unauthorized changes to your network setup.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `NETWORK_NOT_MONITORED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Logs-based Metrics** page within **Logging** in the Google Cloud console. Click **Create metric**. In the **Metric type** field, select **Counter**. In the **Details** section, set **Units** to **1**. In the **Builder filter** box, copy and paste the following text, replacing the existing text: `resource.type=\"gce_network\" AND (protoPayload.methodName:\"compute.networks.insert\" OR protoPayload.methodName:\"compute.networks.patch\" OR protoPayload.methodName:\"compute.networks.delete\" OR protoPayload.methodName:\"compute.networks.removePeering\" OR protoPayload.methodName:\"compute.networks.addPeering\")`  
Click **Create metric** and set the alert policy.

###  Configure Log Metrics and Alerts for VPC Network Firewall Changes

Configure log metrics and alerts to monitor VPC network firewall rule changes. Monitoring VPC network firewall rule changes helps detect suspicious activity and helps to provide better insight into network access changes.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `FIREWALL_NOT_MONITORED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to **Logs-based Metrics** within the **Logging** page in the Google Cloud console. Click **Create metric**. In the **Metric type** field, select **Counter**. In the **Details** section, set **Units** to **1**. In the **Builder filter** box, copy and paste the following text, replacing the existing text: ` resource.type=\"gce_firewall_rule\" AND (protoPayload.methodName:\"compute.firewalls.insert\" OR protoPayload.methodName:\"compute.firewalls.patch\" OR protoPayload.methodName:\"compute.firewalls.delete\")` Click **Create metric** and set the alert policy.

###  Configure Log Metrics and Alerts for VPC Route Changes

Configure log metrics and alerts to monitor VPC network route changes. Monitoring VPC route changes is important for smooth VPC traffic flow.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `ROUTE_NOT_MONITORED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to **Logs-based Metrics** within the **Logging** page in the Google Cloud console. Click **Create metric**. In the **User-defined metrics** section, click inside the Filter box, select Filter, and paste the following text, replacing the existing text: `resource.type="gce_route" AND (protoPayload.methodName:"compute.routes.delete" OR protoPayload.methodName:"compute.routes.insert")` Click **Create metric** and set the alert policy.

###  Configure Log Sinks

Configure log sinks and export the log entries to extend storage periods.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `LOG_NOT_EXPORTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

See [Overview of log exports](https://cloud.google.com/logging/docs/export) and [Create a log sink](https://cloud.google.com/logging/docs/export/configure_export_v2#creating_sink).

###  Configure Model Armor to Detect PII on Model Outputs

Model Armor filters both input (prompts) and output (responses) to help prevent from exposure to or generation of malicious or sensitive content.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MODEL_ARMOR_PII_IN_OUTPUTS_DETECTION_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure Model Armor to help detect personal data in output types such as audio and video. For more information, see [Model Armor overview](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview).

###  Configure Model Armor with Harmful Data Filters

Enable Model Armor to filter harmful data in prompts such as obscenity, extremism, or violence. Model Armor offers filters for content safety, addressing content that is sexually explicit or dangerous or that contains harassment or hate speech content.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MODEL_ARMOR_HARMFUL_DATA_FILTERS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For more information, see [Model Armor overview](https://cloud.google.com/security-command-center/docs/model-armor-overview).

###  Configure Model Armor with Sensitive Data Filters

Enable Model Armor to filter personally identifiable information (PII) or sensitive data in AI applications. To prevent unauthorized exposure in an LLM, Model Armor can discover, classify, and protect sensitive data.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `MODEL_ARMOR_SENSITIVE_DATA_FILTERS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For more information, see [Model Armor overview](https://cloud.google.com/security-command-center/docs/model-armor-overview).

###  Configure Network Devices to Fail in a Secure State

Configure all your managed boundary protection devices and systems to fail in a secure state.

Enforcement mode | Audit   
---|---  
Finding category | `NETWORK_DEVICES_NOT_CONFIGURED_SECURE_FAILURE`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure all boundary protection devices such as VPC Service Controls, VPCs, firewalls, load balancers, proxy servers, and other security mechanisms that control traffic to and from your cloud resources to fail in a secure state.

###  Configure Network Traffic Monitoring

To best monitor network traffic, use separate subnetworks with managed interfaces to physically separate security tools, mechanisms, and support components from other internal system components.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SECURITY_TOOLS_MECHANISMA_NOT_SEPARATED_PHYSICALLY`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Review [firewall rules](https://cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-insights-recommendation-hub) and allowed and denied ports.

  * Verify SSL certificates.

  * Verify NAT configurations are set to provide outbound connectivity to instances without public IPs.

  * Verify logging.

  * Verify VPC Flow Logs.




###  Configure Remote Access Inactivity Timeout

Set the inactivity timeout for remote access sessions to 15 minutes or less. You can use the **HTTP Keep Alive Timeout** configuration to disconnect or disable remote access to your system.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `REMOTE_ACCESS_INACTIVITY_TIMEOUT_NOT_CONFIGURED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **httpKeepAliveTimeoutSec** for Compute Engine instance's target HTTP proxies to less than or equal to 900 seconds. For more information, see [Target proxies overview](https://cloud.google.com/load-balancing/docs/target-proxies).

###  Configure Security Logging Policies for Google Cloud Services

Define and deploy a security logging policy.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `UNDEFINED_AUDIT_LOGGING_POLICY`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit).

  * Create a [security alerting policy file](https://cloud.google.com/monitoring/alerts) in YAML or JSON format. For example: ` logging: auditLog: LOGS_BUCKET_NAME retentionPeriod: 30d `

  * Apply the policy using Deployment Manager. For example: ` gcloud deployment-manager deployments create POLICY_DEPLOYMENT_NAME --config=POLICY_FILE.yaml `

  * Configure Cloud Storage [bucket logging](https://cloud.google.com/storage/docs/access-logs) and [retention policies](https://cloud.google.com/storage/docs/using-bucket-lock).

  * Automate policy checks and enforcement using organization policy constraints.




###  Configure Spanner to Support Data Boundaries

Configure Spanner to support data boundaries that help you meet your regulatory requirements

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_SPANNER_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Cloud Spanner AW Control 

###  Configure the Allowed Ingress Settings for Cloud Run Organization Policy Constraint

Configure the permitted ingress settings for Cloud Run using the "Allowed Ingress Settings (Cloud Run)" (constraints/run.allowedIngress) organization policy. When this constraint is enforced, services are required to have ingress settings that match one of the allowed values.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOWED_INGRESS_ORG_POLICY`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure the the Allowed Ingress Settings (Cloud Run) constraint to ensure that Cloud Run services comply with the allowed ingress settings. For more information, see [Constraints for specific services](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).

###  Configure the Allowed VPC Egress Settings for Cloud Run Organization Policy Constraint

Configure the permitted VPC egress settings for Cloud Run using the "Allowed VPC Egress Settings (Cloud Run)" (constraints/run.allowedVPCEgress) organization policy constraint. When this constraint is enforced, services are required to have VPC egress settings that match one of the allowed values.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOWED_VPC_EGRESS_ORG_POLICY`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure the Allowed VPC Egress Settings (Cloud Run) constraint to ensure that Cloud Run services comply with the allowed VPC egress settings. For more information, see [Constraints for specific services](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).

###  Configure the Disable VM Serial Port Logging to Stackdriver Organization Policy

Configure the Disable VM serial port logging to Stackdriver (constraints/compute.disableSerialPortLogging) organization policy to block serial port logging to Cloud Logging from Compute Engine VMs.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DISABLED_SERIAL_PORT_ACCESS_ORG_POLICY`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Disable VM serial port logging to Stackdriver** organization policy to **True** and ensure that serial port logging to Cloud Logging from Compute Engine VMs is blocked. For more information, see [Constraints for specific services](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).

###  Configure the Disable VPC External IPv6 Usage Organization Policy

Configure the Disable VPC External IPv6 usage (constraints/compute.disableVpcExternalIpv6) organization policy to block VPC subnetworks from using external IPv6 addresses.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DISABLE_VPC_EXTERNAL_IP_V6_ORG_POLICY`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Disable VPC External IPv6 Usage** organization policy to **True** and ensure that all VPC subnetworks don't use external IPv6 addresses. For more information, see [Constraints for specific services](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).

###  Configure the Disable VPC Internal IPv6 Usage Organization Policy

Configure the Disable VPC Internal IPv6 usage (constraints/compute.disableVpcInternalIpv6) organization policy to block VPC subnetworks from using internal IPv6 addresses. A subnetwork with an internal IPv6 address might be exposed to potential risks due to its current limited support.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `COMPUTE_INTERNAL_IP_V6_ORG_POLICY_ENABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Disable VPC Internal IPv6 Usage** organization policy to **True** and ensure that all VPC subnetworks don't use internal IPv6 addresses. For more information, see [Constraints for specific services](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#constraints-for-specific-services).

###  Configure VPC Firewall Rules, Subnets, and VPN Gateway

Manage the flow of data by verifying VPC firewall rules, subnet configurations, and VPN gateway configuration.

Enforcement mode | Audit   
---|---  
Finding category | `VPC_FIREWALL_SUBNET_VPNGATEWAY_NOT_SETUP`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Create isolated networks using VPC.

  * Define granular [IPv4 subnet ranges](https://cloud.google.com/vpc/docs/subnets#ipv4-ranges) and IPv6 subnet ranges.

  * Define [routes](https://cloud.google.com/vpc/docs/routes) and [firewall rules](https://cloud.google.com/firewall/docs/firewalls).

  * Configure a [VPN gateway](https://cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn) to your on-premises network.

  * Configure a global load balancer for your Google-managed services.

  * Configure Cloud NAT to connect to your API backend servers and clients.

  * [Tune Cloud NAT](about:invalid#zCSafez) and the [backend services](https://cloud.google.com/load-balancing/docs/backend-service) for the load balancer to control the flow of traffic between your backend services and your users.

  * Configure VPC Network Peering or another inter-VPC communication method to enable communication between VPC networks and your projects.




###  Confirm FedRAMP Authorization of Services

Services must be FedRAMP authorized and securely configured.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `NON_FEDRAMP_AUTHORIZED_SERVICE`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Conduct regular evaluations to confirm that services which handle or impact federal information are FedRAMP authorized and securely configured.

###  Control Integrations with External Systems

Establish policies to integrate applications on your system with external products and services.

Enforcement mode | Audit   
---|---  
Finding category | `INTEGRATIONS_EXTERNAL_SYSTEMS_NOT_CONTROLLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You must configure your applications to meet your compliance obligations.

###  Control Remote Device Connections

Prevent remote devices from simultaneously establishing non-remote connections with your system and accessing external networks through other connections.

Enforcement mode | Audit   
---|---  
Finding category | `REMOTE_DEVICE_CONNECTION_CONTROL_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use firewall and border router ACLs to implement managed network interfaces and control inbound and outbound traffic. For more information, see [VPC firewall rules](https://cloud.google.com/firewall/docs/firewalls).

###  Correlate Audit Records

Analyze and correlate audit records across different repositories to gain organization-wide situational awareness.

Enforcement mode | Audit   
---|---  
Finding category | `UNCORRELATED_AUDIT_LOG_RECORDS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * [Correlate logs](https://cloud.google.com/logging/docs/view/correlate-logs) and review them in Log Explorer.

  * [Create log-based metrics](https://cloud.google.com/logging/docs/logs-based-metrics) to capture trends and patterns.

  * [Configure labels on log-based metrics](https://cloud.google.com/logging/docs/logs-based-metrics/labels) to add additional information to the entries.




###  Create Alerts for Monitoring Security Command Center Errors

Alerts about Security Command Center provide visibility into your organization and notify you about issues with Security Command Center so you can take appropriate action.

Enforcement mode | Audit   
---|---  
Finding category | `SCC_MONITORING_ALERTS_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create an alerting policy in Cloud Logging to alert on errors related to the Security Command Center service agent. For instructions, see [Configure alerts through Cloud Logging](https://cloud.google.com/logging/docs/alerting/log-based-alerts).

###  Create and Manage Asymmetric Keys

Manage asymmetric keys using NSA-approved key management, either through Public Key Infrastructure (PKI) or pre-positioned keying material protected by hardware security tokens.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `NONCOMPLIANT_ASYMMETRIC_KEY_MANAGEMENT`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the [Certificate Authority Service](https://cloud.google.com/certificate-authority-service/docs/ca-service-overview) for hardware-protected private keys which are FIPS 140-2 Level 3 validated.

###  Create Artifact Registry Cleanup Policies

Artifact Registry cleanup policies define criteria for automatically deleting artifact versions that you no longer need or keeping artifacts that you want to store indefinitely.

Enforcement mode | Audit   
---|---  
Finding category | `ARTIFACT_REGISTRY_CLEANUP_POLICY_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Define clear policies to maintain specific versions of policies and implement a cleanup policy to clear other artifacts. For more information, see [Configure cleanup policies](https://cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) and [Enabling service](https://cloud.google.com/artifact-registry/docs/enable-service#enable).

###  Create CMEK Project and Key Ring

Create a new key management project and key ring to store customer managed encryption keys (CMEKs). If the target deployment resource is a project, the target deployment project is used as the key management project and only a new key ring is created.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Category name in the API | CC_CATEGORY_ENCRYPTION  
Revision number |  2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Parameters

`cmek_project_key_ring_id` |  `STRING` Required. The ID of the Cloud KMS key ring to create in the CMEK project. The key ring is created in the location that you selected when you deployed the framework.  
---|---  
`cmek_project_name` |  `STRING` Optional. Name of the key management project to create. When the target deployment resource is a project, this field must be left empty because the target project is automatically used for key management. In this scenario, specifying a project name results in an error. Specify a project name when the target deployment resource is not a project.  
`cmek_project_id` |  `STRING` Optional. ID of the project to create that will contain encryption keys. Avoid using PII identifiers or other customer data as this information is visible within the logs. When the target deployment resource is a project, leave this this field empty because the target project is automatically used for key management. In this scenario, specifying a project ID results in an error. When the target deployment resource is not a project and you don't specify a project ID, a project ID is generated automatically.  
`cmek_project_billing_account` |  `STRING` Optional. The billing account to link to the new CMEK project. Any charges incurred for this project are billed to this account. When the target deployment resource is a project, leave this field empty because the target project is automatically used for key management. In this scenario, specifying a billing account results in an error. Specify a billing account when the target deployment resource is not a project.  
  
###  Create GKE Clusters with Limited Privileges

Avoid broad access scopes for a Google Kubernetes Engine (GKE) node service account. This control checks node pools to determine whether they're using custom service accounts or, if the default service account is used, that all the OAuth scopes are part of the allowed list, which consists of https://www.googleapis.com/auth/devstorage.read_only, https://www.googleapis.com/auth/logging.write, and https://www.googleapis.com/auth/monitoring.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `OVER_PRIVILEGED_SCOPES`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use custom service accounts or limit the OAuth access scope for GKE nodes. For more information, see [Use a least privileged service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa) and [Access scopes in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes).

###  Create Inventory of Security Data Assets

Ensure security-relevant information (sensitive data, APIs, services, databases, and infrastructure components) are clearly documented and classified.

Enforcement mode | Audit   
---|---  
Finding category | `DATA_CLASSIFICATION_MISSING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Find and classify security-relevant data in Google Cloud, such as sensitive data and configuration data.

  * Create an inventory of the resources that aren’t publicly available. For example, APIs, services, databases, and infrastructure components.




###  Create Super Admin Login Alerts

Create alerts to receive notifications when a super administrator logs into their account.

Enforcement mode | Audit   
---|---  
Finding category | `SUPERADMIN_LOGIN_ALERT_NOT_FOUND`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create alerts when a super administrator logs into their account. For instructions, see [Configure log-based alerting policies](https://cloud.google.com/logging/docs/alerting/log-based-alerts).

###  Define a Security Policy to Mitigate for DDoS Events

Create a security policy using Google Cloud Web Armor to mitigate DDoS risks to your applications.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_SECURITY_POLICY_DDOS_EVENTS`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Configure a [security policy](https://cloud.google.com/armor/docs/security-policy-overview) for backend services.

  * Enable [advanced network DDoS protection](https://cloud.google.com/armor/docs/advanced-network-ddos).

  * Verify the [load balancing scheme](https://cloud.google.com/load-balancing/docs/choosing-load-balancer#summary-gclb).

  * Review [firewall rules](https://cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-insights-recommendation-hub) and allowed and denied ports.




*Verify the [autoscaling policy](https://cloud.google.com/compute/docs/autoscaler) for autoscalers.

###  Define Agent Platform Workbench Instance Access Mode

Use the "Define access mode for Vertex AI Workbench notebooks and instances" (ainotebooks.accessMode) organization policy constraint to define the modes of access that are allowed for Agent Gemini Enterprise Platform Workbench Instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_VERTEXAI_ACCESSMODE_NOT_DEFINED`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Define an allow or deny list using the **Define access mode for Vertex AI Workbench notebooks and instances** (`ainotebooks.accessMode`) constraint. The allow or deny list can specify multiple users with the `service-account` mode or single-user access with the `single-user` mode. For more information, see [Updating policies with list rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#list_constraints).

###  Define Allowed Services for Service Perimeter

Define which services are available within the service perimeter to limit the set of services that are accessible from network endpoints inside your service perimeter.

Enforcement mode | Audit   
---|---  
Finding category | `SERVICE_PERIMETER_ALLOWED_SERVICES_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Add a list of services to your service perimeter. For more information, see [Add a service to the VPC accessible services](https://cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add_a_service_to_the_vpc_accessible_services).

###  Define an Acquisition Contract

Define an acquisition contract for information systems, system components, or information system services.

Enforcement mode | Audit   
---|---  
Finding category | `UNDEFINED_ACQUISITION_CONTRACT`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Meet all the requirements and criteria that apply to your regulatory frameworks when creating an acquisition contract. For example, outline comprehensive security and privacy requirements; and include functional needs, mechanism strength, necessary controls, and documentation. List needs for safeguarding documents, detailing system setups, and assigning security, privacy, and supply chain risk management duties. Specify acceptance criteria for the system in the contract.

###  Define Change Management Procedures

Document the change management procedures and ensure that they align with the regulatory guidelines.

Enforcement mode | Audit   
---|---  
Severity | `LOW`  
Finding category | `MISSING_CHANGE_MANAGEMENT_PROCEDURE`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Clearly define and outline the change management procedures for your applications and services.

###  Define Cloud Billing Budget Threshold

Budgets let you track your actual Google Cloud project costs against your planned costs. Set a budget amount and budget alert threshold rules that trigger email notifications.

Enforcement mode | Audit   
---|---  
Finding category | `CLOUD_BILLING_BUDGET_THRESHOLD_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set alerts and thresholds on your cloud project bills. See [Set budget threshold rules and actions](https://cloud.google.com/billing/docs/how-to/budgets#budget-actions).

###  Define Cloud KMS Crypto Keys Protection Level

Set the protection level for Cloud KMS keys to SOFTWARE, HSM, EXTERNAL, or EXTERNAL_VPC.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CRYPTOKEY_PROTECTION_LEVEL_DENIED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To set the protection level, see [Protection levels](https://cloud.google.com/kms/docs/protection-levels).

###  Define Cloud KMS Crypto Keys Purpose

Set the purpose of Cloud KMS keys to ENCRYPT_DECRYPT. The key's purpose defines its allowed cryptographic operations.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CRYPTOKEY_PURPOSE_RESTRICTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For information on the key purpose, see [Key purposes and algorithms](https://cloud.google.com/kms/docs/algorithms#key_purposes) and [CryptoKeyPurpose](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#cryptokeypurpose).

###  Define Essential Contacts

Essential Contacts are individuals or groups designated to receive crucial Google Cloud notifications, ensuring personnel who are informed about critical events like security attacks, vulnerabilities, and data incidents.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `ESSENTIAL_CONTACTS_NOT_CONFIGURED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **IAM & Admin** > **Essential Contacts** page in the Google Cloud console. Click **+Add contact** and enter all the details of the contact to designate essential contacts.

###  Define External Build Integrations for Cloud Build

Use the "Allowed Integrations (Cloud Build)" (cloudbuild.allowedIntegrations) organization policy constraint to define the external services (for example, GitHub) that can invoke build triggers for Cloud Build.

Enforcement mode | Audit   
---|---  
Finding category | `EXTERNAL_BUILD_INTEGRATION_NOT_DEFINED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To configure allowed webhooks for Cloud Build integrations of the project, see [Setting up organization policy for allowed integrations](https://cloud.google.com/build/docs/securing-builds/gate-builds-organization-policy#setting_up_organization_policy_for_allowed_integrations).

###  Define IsLive Attribute for Delete Action Lifestyle Rule on Bucket

A lifecycle rule defines actions based on object conditions. The isLive attribute is used with Object Versioning and applies to the live object version. Without versioning, all objects are live and match isLive:true.

Enforcement mode | Audit   
---|---  
Finding category | `LIFESTYLE_CONDITION_MISSING_ON_LIFESTYLE_BUCKET_ACTION`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the `isLive` attribute to `true` for a lifecycle rule with a Delete action on Cloud Storage buckets. See [isLive](https://cloud.google.com/storage/docs/lifecycle#islive).

###  Define Locations for Cloud Logging Buckets

Define the regions where log buckets for Cloud Logging can be located. Restrict the location to regions that are supported by your regulatory framework

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_LOGGING_STORAGE_LOCATION_NOT_RESTRICTED`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  2.1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Parameters

`cloudLoggingStorageLocations` |  `STRINGLIST` Required. A list of Google Cloud regions (e.g., 'us-central1', 'europe-west1') where Cloud Logging buckets are permitted to be created. Attempts to create buckets in any other region will be blocked by this control.  
---|---  
  
###  Define Locations for Technical Support Services

Define the regions where your Customer Care support cases are routed and where Google personnel can access your audit logs. To define these regions, you must set the regulatory framework that your service supports.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `ENABLE_RESTRICT_TECHNICAL_SUPPORT_SERVICES`  
Category name in the API | CC_CATEGORY_ADMIN_ACCESS  
Revision number |  3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Assurant Settings 

#### Parameters

`framework` |  `STRING` Required. Ensures additional compliance setting for the underlying services are correctly configured to meet the compliance level of the selected framework.  
---|---  
  
###  Define Mobile Code Policies and Controls

Establish and enforce policies for mobile code usage that align with your compliance obligations.

Enforcement mode | Audit   
---|---  
Finding category | `UNDEFINED_MOBILE_CODE_POLICIES_CONTROLS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Create a mobile code policy that defines what technologies are acceptable and unacceptable.

  * Use [IAM allow policies](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to control access to your mobile code resources.

  * Use organization policy constraints to restrict resource deployments. For example, create a [custom constraint](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints) that restricts the use of specific programming languages or libraries.

  * Configure [firewall rules](https://cloud.google.com/firewall/docs/firewalls) that control communication. For example, restrict outbound traffic from mobile code to specific allowlisted destinations only.




###  Define Owner Labels for Cloud Storage Buckets

Verify the labels for the bucket owner and assign the right owner.

Enforcement mode | Audit   
---|---  
Finding category | `BUCKET_LABEL_OWNER_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify that the right owner is defined for the bucket and that the bucket has a label.

###  Define Recovery Time and Recovery Point Objectives

Define Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) to ensure minimal service disruption and data loss during incidents and contingencies.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_RTO_AND_RPO`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To remediate this finding, establish and document the Recovery Time Objective (RTO) and Recovery Point Objective (RPO) for the affected application or system.\n1. Conduct a Business Impact Analysis (BIA) to identify critical systems and the business impact of an outage.\n2. Based on the BIA, define the maximum acceptable downtime (RTO) and data loss (RPO) for the application.\n3. Document these RTO and RPO values in your organization's business continuity or disaster recovery plan.

###  Define Retention Period for Cloud Storage Buckets

Set a bucket retention policy to ensure objects are deleted after 90 days.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `STORAGE_BUCKET_RETENTION_PERIOD_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For Cloud Storage buckets, set the retention period greater than or equal to 90 days or 7776000.0 seconds. For more information, see [Retention periods](https://cloud.google.com/storage/docs/bucket-lock#retention-periods).

###  Define Rotation Period for Cloud KMS Keys

Rotate the keys regularly to enhance security. Set the rotation period for Cloud KMS keys to 90 days.

Enforcement mode | Audit   
---|---  
Finding category | `KMS_KEY_NOT_ROTATED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For instructions, see [Configure automatic rotation](https://cloud.google.com/kms/docs/rotate-key#automatic).

###  Define Secret Manager Replication Policy

Configure an automated replication policy to ensure that you back up secrets without a restriction on location.

Enforcement mode | Audit   
---|---  
Finding category | `SECRET_MANAGER_REPLICATION_POLICY_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To set a replication policy, see [Choose a replication policy](https://cloud.google.com/secret-manager/docs/choosing-replication).

###  Define Secret Manager Replication Policy

Configure an automated replication policy to ensure that you back up secrets without a restriction on location.

Enforcement mode | 

  * Audit 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `SECRET_MANAGER_REPLICATION_POLICY_NOT_SET`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To set a replication policy, see [Choose a replication policy](https://cloud.google.com/secret-manager/docs/choosing-replication).

###  Define Secret Manager Rotation Schedule

Secret Manager lets you schedule periodic rotations of your secrets by sending notifications to Pub/Sub topics associated with your secrets, based on the rotation frequency and time that you specify.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SECRET_MANAGER_ROTATION_SCHEDULE_NOT_SET`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For Secret Manager secrets, configure a rotation schedule. For more information, see [Create rotation schedules in Secret Manager](https://cloud.google.com/secret-manager/docs/secret-rotation).

###  Define Security Policies

Ensure that security policies are documented.

Enforcement mode | Audit   
---|---  
Severity | `LOW`  
Finding category | `MISSING_SECURITY_POLICIES`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create a detailed document that defines the security objectives and policies of all information resources for applications and services.

###  Define Service Perimeters in VPC Service Controls

Configure service perimeters at the organization level to help protect Google Cloud services and mitigate the risk of data exfiltration.

Enforcement mode | Audit   
---|---  
Finding category | `SERVICE_PERIMETER_NOT_DEFINED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't change the perimeter type after you create a service perimeter. Delete the existing perimeter, and create a new one with the perimeter type set to **Regular**. See [Create a service perimeter](https://cloud.google.com/vpc-service-controls/docs/create-service-perimeters#create-perimeter).

###  Define Set Storage Class Lifestyle Action on Bucket

Use the SetStorageClass action to change the storage class of an object and update the object's modification time when the object meets all conditions specified in the lifecycle rule. This action helps you optimize your storage costs.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SET_STORAGE_CLASS_LIFESTYLE_ACTION_NOT_CONFIGURED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the lifecycle rule action type to `SetStorageClass` for Cloud Storage buckets. For more information, see [SetStorageClass](https://cloud.google.com/storage/docs/lifecycle#setstorageclass).

###  Define Storage Class Lifestyle Action

The lifecycle configuration defines the rules that change the storage class of an object depending on its age, current storage class, and name to protect your data.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `STORAGE_CLASS_TYPE_NOT_UPDATED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For Cloud Storage buckets, set the storage class within the lifecycle rule action to `STANDARD`, `NEARLINE`, `COLDLINE`, or `ARCHIVE`. For more information, see [Change an object's storage class](https://cloud.google.com/storage/docs/lifecycle-configurations#change_an_objects_storage_class).

###  Define the Maximum Number of Concurrent Sessions for System Accounts in Workforce Identity Pools

In the Workforce identity pools, define the maximum number of concurrent sessions for system accounts globally, by account type, by account, or any combination thereof.

Enforcement mode | Audit   
---|---  
Finding category | `MAXIMUM_NUMBER_OF_CONCURRENT_SESSIONS_LIMIT_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Create separate Workforce identity pools for privileged and non-privileged accounts.

  * Set the concurrent session limits (3 for privileged access; 2 for non-privileged access).

  * Review and adjust session limits regularly.

  * Communicate to users the session limits for their account types.

  * Monitor concurrent sessions and ensure compliance with session limits. `gcloud logging read "resource.type=global AND logName=projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity" --project=PROJECT_ID --format=json`

  * Automate the closure of excess sessions and session limit enforcement.

  * Integrate session limits into your deployment pipelines..

  * Document the session limit policies.

  * Include session limits in access reviews and audits.




###  Define the Permitted Versions for Cloud Run Functions

Define the versions (1st gen or 2nd gen) of Cloud Run functions that can or can't run in your folder or project. In Cloud Run functions (1st gen), a function is deployed from source code. In Cloud Run functions (2nd gen), a function is a Cloud Run service that's deployed from source code. This control lets you specify the values that define the cloudfunctions.restrictAllowedGenerations organization policy constraint.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_FUNCTION_GENERATION_NOT_SPECIFIED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  3.1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/cloudfunctions.restrictAllowedGenerations`  
---|---  
  
#### Parameters

Required union field `generations`.  The list of allowed or denied versions of Cloud Run functions. Possible values are 1stGen and 2ndGen. `generations` can be only one of the following:   
---  
`allowedGenerations` |  `STRINGLIST` The list of allowed versions of Cloud Run functions. Possible values are 1stGen and 2ndGen.  
`deniedGenerations` |  `STRINGLIST` The list of denied versions of Cloud Run functions. Possible values are 1stGen and 2ndGen.  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `cloudfunctions.restrictAllowedGenerations` constraint to the required values:

    * Allowed values: $allowedGenerations
    * Denied values: $deniedGenerations

See [Updating policies with list rules](https://docs.cloud.google.com/organization-policy/apply-policies#list_constraints) and [Restrict new deployments by product version](https://docs.cloud.google.com/functions/docs/securing/gen-org-policy).




###  Define VoIP Usage Policy

Establish usage restrictions and implementation guidance for Voice over Internet Protocol (VoIP) technologies.

Enforcement mode | Audit   
---|---  
Finding category | `UNDEFINED_VOIP_USAGE_POLICY`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Create a VoIP usage policy that defines acceptable use of VoIP technologies.

  * Use organization policy constraints to restrict resource deployments. For example, create a custom constraint that allows only authorized personnel to deploy and manage VoIP resources.

  * Configure [firewall rules](https://cloud.google.com/firewall/docs/firewalls) that control inbound and outbound traffic related to VoIP services.

  * Use IAM allow policies to control access to VoIP resources.

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit).

  * Activate Security Command Center.

  * Create alerts for unusual or unauthorized activities.

  * Configure Cloud Monitoring to monitor network traffic.

  * Perform vulnerability scanning and penetration testing on VoIP resources.

  * Use TLS for VoIP communication.

  * Implement best practices to prevent eavesdropping.

  * Create an incident response plan for VoIP incidents.




###  Define VPC Connector Egress For Cloud Run Functions

Use the "Require VPC Connector (Cloud Functions)" (constraints/cloudfunctions.requireVPCConnector) organization policy constraint to require Cloud Function (1st gen) to use a VPC connector.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_REQUIRE_VPC_CONNECTOR_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the value for the **Require VPC Connector (Cloud Functions)** (`constraints/cloudfunctions.requireVPCConnector`) constraint to `true`. For instructions, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

###  Define Worker Pools for Cloud Builds

Use the "Allowed Worker Pools (Cloud Build)" (cloudbuild.allowedWorkerPools) organization policy constraint to define allowed worker pools for builds in your project.

Enforcement mode | Audit   
---|---  
Finding category | `CLOUD_BUILD_WORKER_POOL_NOT_DEFINED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To create a private pool, see [Creating a new private pool](https://cloud.google.com/build/docs/private-pools/create-manage-private-pools#creating_a_new_private_pool). For permitted values, see [Allowed Worker Pools (Cloud Build)](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints?constraints%2Fcloudbuild.allowedWorkerPools#:~:text=Allowed%20Worker%20Pools%20\(Cloud%20Build\)).

###  Describe Design and Implementation Details of Security Controls

Ensure developers in your system provide the design and implementation details of the security controls employed.

Enforcement mode | Audit   
---|---  
Finding category | `DESIGN_IMPLEMENTATION_DETAILS_SECURITY_CONTROLS_MISSING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Describe design and implementation details of security controls with security-relevant external system interfaces, high-level design, low-level design, source code, or network and data flow diagrams.

###  Describe the Functional Properties of Security Controls

Ensure developers in your system document the functional properties of the security controls employed.

Enforcement mode | Audit   
---|---  
Finding category | `FUNCTIONAL_DESCRIPTIONS_SECURITY_CONTROLS_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure developers document the functional properties of security controls such as capabilities, functions, or mechanisms that are visible at the interfaces of the controls. Developers do not need to document functionality and data structures that are internal to the operation of the controls.

###  Detect IP Infringement in Agent Platform Training Data

Configure Gemini Enterprise Agent Platform to help detect Intellectual Property (IP) infringement in model training data and maintain compliance.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `IP_INFRINGEMENT_DETECTION_DISABLED`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that Agent Platform can evaluate model training data for intellectual property infringement. For more information, see [Safety in Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/safety-overview#available-safety-tools).

###  Detect Misinformation and Manipulation of Agent Platform Model Data

Configure Gemini Enterprise Agent Platform to help detect misinformation in model training data and manipulation of model inputs and outputs.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISINFORMATION_DETECTION_DISABLED`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement tools and guidance to identify patterns that are associated with misinformation or manipulation in prompts and outputs. For more information, see [Available safety tools in Gemini on Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/safety-overview#available-safety-tools).

###  Detect Obscenity, Extremism, Violence, and CBRN in Agent Platform Model Training Data

Configure Gemini Enterprise Agent Platform to help detect harmful model training data such as obscenity, extremism, violence, and chemical, biological, radiological, or nuclear (CBRN) information.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `HARMFUL_TRAINING_DATA_DETECTION_DISABLED`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that Agent Platform can evaluate model training data for extremism, violence, or CBRN information. For more information, see [Safety and content filters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/configure-safety-filters).

###  Determine High-level Security and Privacy Needs

Determine high-level security and privacy requirements during the planning phase.

Enforcement mode | Audit   
---|---  
Finding category | `SECURITY_PRIVACY_NEEDS_NOT_IDENTIFIED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Identify your high-level security and privacy requirements for the system or system service.

  * Determine, document, and allocate the resources that are required to protect the system or system service.

  * Budget for security and privacy.




###  Develop a Recovery Plan

Develop and maintain a recovery plan that aligns with the defined recovery objectives.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_RECOVERY_PLAN`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Define a contingency plan that identifies critical functions, recovery objectives, restoration priorities, metrics, contingency roles, contact information, and ensure essential function maintenance during disruption or failure. Plan to resume essential mission and business functions within a defined time period of contingency plan activation.

###  Develop Documentation for System Security

Develop and maintain administrator documentation for the information system, system component, or information system services.

Enforcement mode | Audit   
---|---  
Finding category | `SYSTEM_SECURITY_DOCUMENTATION_MISSING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create documentation that describes: • Secure configuration, installation, and operation of the system • Effective use and maintenance of security functions • Known vulnerabilities regarding configuration and use of administrative functions • User-accessible security functions and how to use those functions • How users can interact with the system • What users are responsible for In addition, protect documentation in accordance with your risk management strategy and distribute documentation appropriately.

###  Develop System and Communications Protection Policy and Procedures

Develop, document, and disseminate policies related to systems and communications.

Enforcement mode | Audit   
---|---  
Finding category | `UNDEFINED_SYSTEM_COMMUNICATIONS_PROTECTION_POLICY_PROCEDURES`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create your own policies to meet your compliance obligations.

###  Develop System and Services Acquisition Policy and Procedures

Develop, maintain, and disseminate a system and services acquisition policy and procedures.

Enforcement mode | Audit   
---|---  
Finding category | `SYSTEM_SERVICES_ACQUISITION_POLICY_PROCEDURES_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Develop, document, and disseminate to organization-defined personnel or roles:

    * A system and services acquisition policy that is defined at an organization-level, mission or business process-level, or at system-level. The policy must address purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance. The policy must be consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines.

    * Procedures to facilitate the implementation of the system and services acquisition policy and the associated system and services acquisition controls.

  * Designate an organization-defined official to manage the development, documentation, and dissemination of the system and services acquisition policy and procedures.

  * Review and update the current system and services acquisition policies and procedures as per organization-defined frequencies and events.




###  Disable Alpha Features on GKE Clusters

Google Kubernetes Engine (GKE) Alpha clusters are used to experiment with workloads before they're released, and are auto-deleted after 30 days. For production workloads, create a cluster with alpha features disabled.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALPHA_CLUSTER_ENABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Click **Create** and configure the new cluster. Under the **Features** tab, ensure **Enable Kubernetes alpha features in this cluster** is disabled. Proceed with migrating the workloads. Delete the cluster that has alpha features enabled.

###  Disable Audit Log Exemption

Verify that Audit Log exemption is disabled.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `AUDIT_LOG_EXEMPTION_NOT_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the `constraints/iam.disableAuditLoggingExemption` organization policy to Enforced (true) to ensure audit logging is not exempted for any principal. See https://cloud.google.com/assured-workloads/docs/audit-logging.

###  Disable Client Certificate Authentication for GKE

When creating clusters, don't generate client certificates for legacy authentication to the Kubernetes API server.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `GKE_AUTH_CLIENT_CERTS_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Disable authentication using client certificates for your cluster. For more information, see [Disable authentication with a client certificate](https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication#disabling_authentication_with_a_client_certificate).

###  Disable Compute Instance Data Access APIs

Uses the compute.disableInstanceDataAccessApis organization policy constraint to help prevent unauthorized data access or leaks from Compute Engine VM instances.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `COMPUTE_INSTANCE_DATA_ACCESS_NOT_DISABLED`  
Category name in the API | CC_CATEGORY_INFRASTRUCTURE  
Revision number |  1.3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/compute.disableInstanceDataAccessApis`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `compute.disableInstanceDataAccessApis` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Disable Creation of Global Load Balancers

Uses the compute.disableGlobalLoadBalancing organization policy constraint to prevent users from creating new global load balancers. This constraint also applies to load balancers that distribute traffic across multiple regions. When this constraint is enforced, you can still create regional load balancers, which distribute traffic within a single region.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `GLOBAL_LOAD_BALANCING_NOT_DISABLED`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  2.3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/compute.disableGlobalLoadBalancing`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `compute.disableGlobalLoadBalancing` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints) and [Disable global load balancing](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints#disable_global_load_balancing).



###  Disable Creation of Global Self-managed SSL Certificates

Uses the compute.disableGlobalSelfManagedSslCertificate organization policy constraint to prevent the creation of global self-managed SSL certificates.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `GLOBAL_SELF_MANAGED_SSL_CERTS_NOT_DISABLED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/compute.disableGlobalSelfManagedSslCertificate`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `compute.disableGlobalSelfManagedSslCertificate` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Disable diagnostic and administrative access pathways in Cloud SQL

Enforces the sql.restrictNoncompliantDiagnosticDataAccess organization policy constraint to restrict diagnostic and administrative access pathways in Cloud SQL. This constraint reduces certain aspects of supportability and restricts access paths for diagnostics and other customer support use cases that don't meet advanced sovereignty requirements for Data Boundaries.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `CLOUDSQL_DIAGNOSTIC_ACCESS_NOT_RESTRICTED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/sql.restrictNoncompliantDiagnosticDataAccess`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `sql.restrictNoncompliantDiagnosticDataAccess` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Disable File Downloads on Agent Platform Workbench Instances

Enforce the "Disable file downloads on new Vertex AI Workbench instances" (ainotebooks.disableFileDownloads) organization policy constraint for projects and folders to help prevent the creation of Gemini Enterprise Agent Platform Workbench Instances with the file download option enabled.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICYFILE_DOWNLOADS_ON_VERTEXAI_ENABLED`  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Disable file downloads on new Vertex AI Workbench instances** (`ainotebooks.disableFileDownloads`) organization policy constraint to `true` to turn off file downloads on new Agent Platform Workbench user-managed notebooks and instances. For more information, see [Updating policies with boolean rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints).

###  Disable GKE Diagnostic Administrative Access

Uses the container.restrictNoncompliantDiagnosticDataAccess organization policy to restrict access to diagnostic data that's generated by GKE clusters that are not compliant with the Assured Workloads control package (such as IL4, IL5, or ITAR).

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `GKE_DIAGNOSTIC_ACCESS_NOT_DISABLED`  
Category name in the API | CC_CATEGORY_INFRASTRUCTURE  
Revision number |  1.3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/container.restrictNoncompliantDiagnosticDataAccess`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `container.restrictNoncompliantDiagnosticDataAccess` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Disable Global Cloud Armor Policies

Uses the compute.disableGlobalCloudArmorPolicy organization policy constraint to prevent users from creating new global Cloud Armor security policies. These policies are used to protect HTTP(s) load balancers from various web attacks. You can use this control to restrict the ability to create security policies to a central security team or specific administrators for governance and security purposes.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `GLOBAL_CLOUD_ARMOR_NOT_DISABLED`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  2.3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/compute.disableGlobalCloudArmorPolicy`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `compute.disableGlobalCloudArmorPolicy` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Disable Legacy Metadata Server Endpoints on Compute Engine

Disable legacy metadata server endpoints for all VMs in your project. Disabling Legacy metadata helps to enforce Compute Engine's instance metadata query headers and makes it harder for attackers to access instance metadata.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `LEGACY_METADATA_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

In the Google Cloud console, go to the **Metadata** page. Set `disable-legacy-endpoints` to `true`. For more information, see [Set custom project metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata#set-custom-project-wide-metadata).

###  Disable Pub/Sub Subscription Message Transforms

Uses the pubsub.managed.disableSubscriptionMessageTransforms organization policy constraint to prevent Pub/Sub subscriptions from using message transformation features.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `PUBSUB_SUBSCRIPTION_MESSAGE_TRANSFORMS_NOT_DISABLED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  3.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/pubsub.managed.disableSubscriptionMessageTransforms`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `pubsub.managed.disableSubscriptionMessageTransforms` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).

  * **Remediation for resource violation:** Delete the resource to resolve the resource violation associated with the `pubsub.managed.disableSubscriptionMessageTransforms` constraint.




###  Disable Pub/Sub Topic Message Transforms

Uses the pubsub.managed.disableTopicMessageTransforms organization policy constraint to prevent the use of message transformations on Pub/Sub topics.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `PUBSUB_TOPIC_MESSAGE_TRANSFORMS_NOT_DISABLED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  3.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/pubsub.managed.disableTopicMessageTransforms`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `pubsub.managed.disableTopicMessageTransforms` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).

  * **Remediation for resource violation:** Delete the resource to resolve the resource violation associated with the `pubsub.managed.disableTopicMessageTransforms` constraint.




###  Disable Service Account Key Creation

Uses the 'iam.disableServiceAccountKeyCreation' organization policy constraint to prevents the creation of user-managed service account keys. This constraint helps reduce the security risk associated with long-lived, exportable credentials.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `IAM_SERVICE_ACCOUNT_KEY_CREATION_ENABLED`  
Category name in the API | CC_CATEGORY_IDENTITY_AND_ACCESS_MANAGEMENT  
Revision number |  2.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/iam.disableServiceAccountKeyCreation`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `iam.disableServiceAccountKeyCreation` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Disable Spanner Multi-Region Instances

Uses the spanner.disableMultiRegionInstanceIfNoLocationSelected organization policy constraint to prevent the creation of multi-region Spanner instances unless a specific location is selected for each region in the instance configuration. This control doesn't the creation of single-region Spanner instances, where only one location needs to be specified.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `GLOBAL_SPANNER_MULTI_REGION_NOT_DISABLED`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  1.3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/spanner.disableMultiRegionInstanceIfNoLocationSelected`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `spanner.disableMultiRegionInstanceIfNoLocationSelected` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Disable Suspicious Accounts Automatically

Automatically disable or secure accounts with privileged access in response to suspicious activity.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `SUSPICIOUS_ACCOUNTS_NOT_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure logging and monitoring for automated deactivation of suspicious accounts or secure privileged accounts to help prevent suspicious activities. For more information, see [Create metric-threshold alerting policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) and [Monitor for credential compromise](https://cloud.google.com/docs/security/compromised-credentials#monitor_for_credential_compromise).

###  Disable the Creation and Update of Kafka Connect Clusters

Uses the managedkafka.managed.disableKafkaConnectClusterCreateAndUpdate organization policy constraint to prevent the creation and updating of Managed Service for Apache Kafka Connect clusters.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `MANAGED_KAFKA_CONNECT_CREATE_UPDATE_ALLOWED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/managedkafka.managed.disableKafkaConnectClusterCreateAndUpdate`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `managedkafka.managed.disableKafkaConnectClusterCreateAndUpdate` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Document and Manage Software Supply Chain Security Risk Management

Document risk management decisions for software supply chain security.

Enforcement mode | Audit   
---|---  
Severity | `LOW`  
Finding category | `MISSING_SOFTWARE_SUPPLY_CHAIN_RISK_MANAGEMENT`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure risk management is documented and is an integral part of the continuous monitoring strategy that includes effectiveness monitoring, compliance monitoring, and change monitoring.

###  Document Information Resource Implementations

Document the methods that are used to evaluate information resource implementations.

Enforcement mode | Audit   
---|---  
Severity | `LOW`  
Finding category | `MISSING_INFORMATION_RESOURCE_IMPLEMENTATION_DOCUMENTATION`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Document each assessment method that was used for evaluating compliance with a FedRAMP 20x KSI.

###  Don't Use Kubernetes Web UI

The Kubernetes web UI (dashboard) increases the attack surface. Instead, use the Google Cloud console. Note that the Kubernetes web UI is deprecated and is no longer available by default.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `WEB_UI_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Disable the Kubernetes dashboard. Go to the **Kubernetes clusters** page in the Google Cloud console. Edit the cluster settings, click **Add-ons** , and then disable the **Kubernetes dashboard** add-on. For more information, see [KubernetesDashboard](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.AddonsConfig#Google_Cloud_Container_V1_AddonsConfig_KubernetesDashboard).

###  Don't Use Legacy Networks

Legacy networks are not recommended and can no longer be created. Instead, use VPC networks, which offer a software-defined structure that enhances control and helps improve operational efficiency. This control checks network metadata for the existence of the IPv4Range property. This control doesn't apply to projects where Compute Engine API is disabled and projects where Compute Engine resources are in a frozen state.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `LEGACY_NETWORK`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create a VPC network and delete the legacy network. Go to the **VPC networks** page in the Google Cloud console. Click **Create Network** to create a VPC network. Return to the **VPC networks** page, click **legacy_network** from the list of networks. Delete the legacy network.

###  Don't Use User Connections Flag for SQL Server

Don't configure the user connections flag for a SQL Server instance. SQL Server automatically adjusts user connections if you don't use this flag.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SQL_USER_CONNECTIONS_CONFIGURED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and delete the **User connections** database flag for the SQL Server instance.

###  Don't Use User Options Flag for SQL Server

Don't configure the user options flag for a SQL Server instance. Using the flag might cause unexpected results. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_USER_OPTIONS_CONFIGURED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and delete the **User options** database flag for the SQL Server instance.

###  Employ Dynamic Code Analysis Tools

Employ dynamic code analysis tools to identify common flaws and document the results of the analysis.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_DYNAMIC_CODE_ANALYSIS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use a dynamic code analysis tool to identify common flaws and document the results of the analysis.

###  Employ Monthly Checks for Flaw Remediation Status

Employ monthly automated checks to determine the flaw remediation status of information system components.

Enforcement mode | Audit   
---|---  
Finding category | `IMPROPER_FLAW_REMEDIATION_STATUS_CHECKS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement and manage a flaw remediation system. You can use [Security Command Center](https://cloud.google.com/security-command-center/docs) and [Patch feature in VM Manager](https://cloud.google.com/compute/docs/os-patch-management) to implement certain malicious code protection mechanisms.

###  Employ Spam Protection Mechanisms

Employ spam protection mechanisms at system entry and exit points to detect and act on unsolicited messages.

Enforcement mode | Audit   
---|---  
Finding category | `SPAM_PROTECTION_MECHANISMS_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement spam protection mechanisms such as reCAPTCHA Enterprise, Cloud Armor, or Web Risk API to protect your systems from unsolicited messages.

###  Employ Static Code Analysis Tools

Employ static code analysis tools and web scanning tools to identify common flaws and document the results of the analysis.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_STATIC_CODE_ANALYSIS_TOOLS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Use static code review tools and web security scanners that match your programming languages.

  * Use the [Web Security Scanner](https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) to check vulnerabilities in App Engine, GKE, and Compute Engine web applications.

  * Activate [Security Command Center](https://cloud.google.com/security-command-center/docs/security-command-center-overview) for additional vulnerability and threat detection capabilities.

  * Use [Cloud Build](https://cloud.google.com/build/docs/overview) to manage build security.




###  Enable 3625 Trace Database Flag for SQL Server

Turn on the 3625 (trace flag) for SQL Server to control information returned to non-sysadmin users. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_TRACE_FLAG_3625`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn on the trace flag. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **3625 (trace flag)** flag to **On** for the SQL Server instance.

###  Enable Access Transparency

Access Transparency logs when Google Cloud employees access your projects for support. Enabling it logs who accesses your information, when, and why.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `ACCESS_TRANSPARENCY_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable access transparency, in the Google Cloud console, select your organization or a specific project. Go to **IAM & Admin > Settings**, and click **Enable Access Transparency**.

###  Enable Access Transparency

Enables Access Transparency logs, providing audit logs of Google operator access.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `ACCESS_TRANSPARENCY_NOT_ENABLED`  
Category name in the API | CC_CATEGORY_ADMIN_ACCESS  
Revision number |  1   
Supported target resources | 

  * Folder
  * Project

  
  
###  Enable Account Monitoring for Atypical Usage

Monitor accounts for atypical usage, such as accessing the Google Cloud console at unusual times or from inconsistent locations, and report these instances to designated personnel or roles.

Enforcement mode | Audit   
---|---  
Finding category | `ATYPICAL_USAGE_ACCOUNT_MONITORING_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable audit logging. For instructions, see [Enable Data Access audit logs](https://cloud.google.com/logging/docs/audit/configure-data-access). For more information on checking for atypical usage, see [Monitor for credential compromise](https://cloud.google.com/docs/security/compromised-credentials#monitor_for_credential_compromise).

###  Enable Advanced Service Controls for Spanner

Uses the spanner.assuredWorkloadsAdvancedServiceControls organization policy constraint to enforce additional data sovereignty and supportability controls on Spanner resources that are provisioned within the data boundary.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `SPANNER_ADVANCED_SERVICE_CONTROLS_NOT_ENABLED`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  1.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/spanner.assuredWorkloadsAdvancedServiceControls`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `spanner.assuredWorkloadsAdvancedServiceControls` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Enable Agent Platform Copyright Data Filters

Enable the Gemini Enterprise Agent Platform copyright data filter when using Gemini on Agent Platform.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `COPYRIGHT_DATA_FILTERS_NOT_IN_USE_IN_VERTEX_AI`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use the non-configurable filters in Gemini on Agent Platform to help prevent the generation of copyrighted content (recitation). For more information, see [Safety in Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/safety-overview).

###  Enable AlloyDB Automated Backups on Cluster

Automatic backups help to prevent data loss. Enable them to start automated backups for the AlloyDB for PostgreSQL cluster. This control checks whether the automated_backup_policy.enabled property in the metadata of an AlloyDB for PostgreSQL cluster is set to true. This control doesn't apply to AlloyDB for PostgreSQL secondary clusters.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOYDB_AUTO_BACKUP_DISABLED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable automated backup on AlloyDB for PostgreSQL clusters, see [Enable and configure automated backups](https://cloud.google.com/alloydb/docs/backup/configure#set).

###  Enable AlloyDB Backups on Cluster

AlloyDB backups help to prevent data loss. Enable continuous or automated backups for the AlloyDB for PostgreSQL primary cluster. This control doesn't apply to secondary clusters.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOYDB_BACKUPS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **AlloyDB for PostgreSQL clusters** page in the Google Cloud console. Click the cluster in the **Resource Name** column. Go to **Data protection** , and set up a backup policy. For more information, see [Manage continuous backup and recovery](https://cloud.google.com/alloydb/docs/backup/configure#continuous).

###  Enable Artifact Analysis Vulnerability Scanning

Vulnerability scanning in Artifact Analysis helps to check your container images for known vulnerabilities.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ARTIFACT_ANALYSIS_VULNERABILITY_SCANNING_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To understand artifact analysis and enable vulnerability scanning, see [Artifact analysis and vulnerability scanning](https://cloud.google.com/artifact-registry/docs/analysis) and [Scan OS packages automatically](https://cloud.google.com/artifact-analysis/docs/scan-os-automatically).

###  Enable Audit Logging for Agent Platform

Enable audit logging to track the actions that your Gemini Enterprise Agent Platform agents perform.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `GOOGLE_AGENT_PLATFORM_AUDIT_LOGGING_NOT_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable audit logging for Agent Platform, see [Agent Platform audit logging information](https://docs.cloud.google.com/vertex-ai/docs/general/audit-logging).

###  Enable Audit Logging for Agent Platform at Organization Level

Enable audit logging to track the actions that your Gemini Enterprise Agent Platform agents perform.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `GOOGLE_AGENT_PLATFORM_AUDIT_LOGGING_NOT_ENABLED`  
Revision number |  2   
Supported target resources |  Organization   
  
#### Remediation steps

To enable audit logging for Agent Platform, see [Agent Platform audit logging information](https://docs.cloud.google.com/vertex-ai/docs/general/audit-logging).

###  Enable Audit Logs Bucket Enumeration

Enable audit logs monitoring for enumeration of Cloud Storage buckets by service accounts to help investigate if a malicious actor has gained access to a service account.

Enforcement mode | Audit   
---|---  
Finding category | `SERVICE_ACCOUNT_STORAGE_BUCKET_ENUMERATION`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Monitor Audit Logs and look for enumeration of Cloud Storage buckets by service accounts. See [Configure Data Access audit logs with the Google Cloud console](https://cloud.google.com/logging/docs/audit/configure-data-access#config-console).

###  Enable Audit Logs for All Services

Enable Data Access audit logs with the DATA_READ, DATA_WRITE, and ADMIN_READ permissions for the services in use, or for all services.

Enforcement mode | Audit   
---|---  
Finding category | `AUDIT_LOGS_ENABLEMENT_ALLSERVICES_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To configure all data access services, see [Configure Data Access audit logs with the Google Cloud console](https://cloud.google.com/logging/docs/audit/configure-data-access#config-console).

###  Enable Audit Logs for Google Cloud Services

Enable audit logs for services such as Compute Engine and Cloud Storage.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `AUDIT_LOGS_NOT_ENABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit).

  * Define a retention period for your [log buckets](https://cloud.google.com/logging/docs/buckets).

  * Use [Cloud Logging libraries](https://cloud.google.com/logging/docs/setup) in your application code to create custom log entries.

  * Monitor logs using Cloud Monitoring or Cloud Logging dashboards.

  * Grant only necessary IAM roles to service accounts that are associated with applications.

  * Regularly review logs to detect and respond to suspicious activity.




###  Enable Auto Repair for GKE Clusters

The auto repair feature in Google Kubernetes Engine (GKE) clusters makes periodic checks on the health state of each node and helps to keep them in a healthy state. This control checks the management property of a node pool to determine if autoRepair is set to true.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `AUTO_REPAIR_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable the auto-repair option for the node pools. Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Click the cluster name and go to the **Nodes** tab. For each node pool, click its name to access its details page and then select **Edit**. In the **Management** section, ensure the **Enable auto-repair** checkbox is selected.

###  Enable Auto Upgrade on GKE Clusters

The auto upgrade feature in Google Kubernetes Engine (GKE) clusters helps to keep clusters and node pools on the latest stable Kubernetes version.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `AUTO_UPGRADE_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable the auto-upgrade option for the node pools. Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Click the cluster name and go to the **Nodes** tab. For each node pool, click its name to access its details page and then select **Edit**. In the **Management** section, select **Enable auto-upgrade**.

###  Enable Automatic Backups for Cloud SQL Databases

Turn on automatic backups for your Cloud SQL instances and set a start backup time to help prevent data loss. This control doesn't apply to on-premises instances or read replicas.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `AUTO_BACKUP_DISABLED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable automatic backups on your Cloud SQL instances. For more information, see [Create and manage on-demand and automatic backups](https://cloud.google.com/sql/docs/mysql/backup-recovery/backing-up).

###  Enable Automatic Upgrades for Agent Platform WorkBench Instances

Enable automatic upgrades for Gemini Enterprise Agent Platform Workbench Instances to ensure access to the latest features, framework updates, and security patches.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_WORKBENCH_AUTO_UPGRADE_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable auto-upgrade for Agent Platform Workbench Instances.

  1. In the Google Cloud console, go to the [**Instances** page](https://console.cloud.google.com/agent-platform/workbench/instances).

  2. Click the instance that you want to configure.

  3. On the **Instance details** page, select the **Environment auto-upgrade** setting. Choose whether to upgrade your instance weekly or monthly.

  4. Click **Submit**. For more information, see [Upgrade the environment of an instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/upgrade).




###  Enable Cloud Asset Inventory Service

Cloud Asset Inventory provides a comprehensive view of Google Cloud resources. It lets you view, search, export, monitor, and analyze your Google Cloud asset metadata to enhance security analysis, resource change tracking, and compliance auditing. We recommend that you enable the Cloud Asset Inventory service for all projects.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `CLOUD_ASSET_API_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable **Cloud Asset API** in the **Library** page of **APIs & Services** in the Google Cloud console.

###  Enable Cloud DNS Logs Monitoring

Monitoring Cloud DNS logs provides visibility to DNS names within the VPC network and lets you monitor for anomalous domain names.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DNS_LOGGING_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **VPC Network** > **VPC networks** page in the Google Cloud console. Select the VPC network, go to the **DNS configuration** tab, and either edit the existing **DNS server policy** to enable DNS logging or create a server policy if one doesn't exist.

###  Enable Cloud Logging Compliance with FedRAMP or DoD Impact Levels

Configure Cloud Logging within a data boundary that supports FedRAMP Moderate, FedRAMP High, Department of Defence Impact Level 2 (IL2), or Impact Level 4 (IL4).

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_LOGGING_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Cloud Logging Compliance Settings 

#### Parameters

`framework` |  `STRING` Required. Select the regulatory framework that your services must be in compliance with.  
---|---  
  
###  Enable Cloud Logging on GKE Clusters

Cloud Logging on Google Kubernetes Engine (GKE) clusters gives you access logs for all requests made on a specific cluster and storage logs with information about the storage used by that cluster. This control checks whether the loggingService property of a cluster contains the location that Cloud Logging should use to write logs.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `CLUSTER_LOGGING_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Click the cluster name. In the **Features** section, click the **Edit** icon against **Logging**. In the **Components** drop-down list, add the components for which you want to enable logging.

###  Enable Cloud Monitoring on GKE Clusters

Cloud Monitoring on Google Kubernetes Engine (GKE) clusters helps investigate security issues and track cluster usage by providing security and usage information.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `CLUSTER_MONITORING_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Select the cluster. In the **Features** section, click the **Edit** icon against **Cloud Monitoring**. In the **Components** drop-down list, add the components for which you want to enable monitoring.

###  Enable CMEK for Agent Platform Custom Jobs

Require customer-managed encryption keys (CMEK) on Gemini Enterprise Agent Platform custom training jobs to gain more control over the encryption of job inputs and outputs.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_CUSTOM_JOB_CMEK_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform custom training job after it's been created. Delete the job and create a new job with CMEK enabled.

  1. Delete the existing custom job on the [**Training pipelines** page](https://console.cloud.google.com/agent-platform/training/training-pipelines).

  2. Create a new custom job. For instructions, see (Create a serverless training job)[https://docs.cloud.google.com/vertex-ai/docs/training/create-custom-job]. When creating the custom job, enter the name of the Cloud KMS key in the *_encryptionSpec_ field.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform Datasets

Require customer-managed encryption keys (CMEK) for Gemini Enterprise Agent Platform datasets to gain more control over data encryption and key management.

Enforcement mode | Detective   
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_DATASET_CMEK_DISABLED`  
Category names in the API | 

  * CC_CATEGORY_ARTIFICIAL_INTELLIGENCE
  * CC_CATEGORY_DATA_SECURITY

  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform dataset after it's been created. Delete the dataset and create a new dataset with CMEK enabled.

  1. Delete the existing dataset. For instructions, see [Delete a dataset or annotation set](https://docs.cloud.google.com/vertex-ai/docs/datasets/delete-annotation-set).

  2. Create a new dataset. In the Google Cloud console, go to the [**Datasets** page](https://console.cloud.google.com/agent-platform/datasets).

  3. Click **Create dataset**.

  4. In the dataset creation details, expand **Advanced options**.

  5. Select **Cloud KMS key** and provide your CMEK.

  6. Click **Create**.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform Feature Store

Require customer-managed encryption keys (CMEK) for Feature Store on Gemini Enterprise Agent Platform to gain more control over data encryption and access.

Enforcement mode | Detective   
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_FEATURESTORE_CMEK_DISABLED`  
Category names in the API | 

  * CC_CATEGORY_ARTIFICIAL_INTELLIGENCE
  * CC_CATEGORY_DATA_SECURITY

  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform Feature Store after it's been created. Delete the Feature Store and create a new Feature Store with CMEK enabled.

  1. Delete the Feature Store. For instructions, see (Delete a Feature Store)[https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#delete_a_featurestore].

  2. Create a Feature Store that uses CMEK. For instructions, see [Create a Feature Store that uses a CMEK](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores#create_a_featurestore_that_uses_a_cmek).




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform Hyperparameter Tuning Jobs

Require customer-managed encryption keys (CMEK) on Gemini Enterprise Agent Platform hyperparameter tuning jobs to gain more control over the encryption of model training data and job configuration.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_HYPERPARAMETER_TUNING_JOB_CMEK_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform hyperparameter tuning job after it's been created. Delete this job and create a new job with CMEK enabled.

  1. Delete the existing tuning job. For instructions, see (Delete a hyperparameter tuning job)[https://docs.cloud.google.com/vertex-ai/docs/training/using-hyperparameter-tuning#delete_a_hyperparameter_tuning_job].

  2. Create a new hyperparameter tuning job. For instructions, see (Create a hyperparameter tuning job)[https://docs.cloud.google.com/vertex-ai/docs/training/using-hyperparameter-tuning]. When creating the hyperparameter tuning job, enter the name of the Cloud KMS key in the **encryptionSpec** field.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform instances

Enable customer-managed encryption keys (CMEK) for the Gemini Enterprise Agent Platform to gain more control over data encryption and key management.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `AGENT_PLATFORM_CMEK_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform instance after it's been created. Delete the instance and create a new instance with CMEK enabled. For instructions, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform Metadata Stores

Require customer-managed encryption keys (CMEK) for Gemini Enterprise Agent Platform metadata stores to gain more control over the encryption of metadata and control access.

Enforcement mode | Detective   
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_METADATA_STORE_CMEK_DISABLED`  
Category names in the API | 

  * CC_CATEGORY_ARTIFICIAL_INTELLIGENCE
  * CC_CATEGORY_DATA_SECURITY

  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform metadata store after it's been created. Delete the store and create a new store with CMEK enabled.

  1. Delete the metadata store. For instructions, see [Method: metadataStores.delete](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores/delete).

  2. Create a metadata store. For instructions, see [Configure your project's metadata store](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/configure). To enable CMEK, enter the Cloud KMS key name in the **encryptionSpec** field.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform Model Endpoints

Require customer-managed encryption keys (CMEK) for Gemini Enterprise Agent Platform model endpoints to gain more control over the encryption of deployed models and control data access.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_ENDPOINT_CMEK_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform model endpoint after it's been created. Delete the endpoint and create a new endpoint with CMEK enabled.

  1. Delete the existing endpoint. For instructions, see [Undeploy a model and delete the endpoint](https://docs.cloud.google.com/vertex-ai/docs/predictions/undeploy-model).

  2. Create a new endpoint. In the Google Cloud console, navigate to the [**Endpoints** page](https://console.cloud.google.com/agent-platform/online-prediction/endpoints).

  3. Click **Create endpoint**.

  4. In the **Define Your Endpoint** section, expand **Advanced options**.

  5. Select **Cloud KMS key** and provide your CMEK.

  6. Click **Create**.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform Models

Require customer-managed encryption keys (CMEK) for Gemini Enterprise Agent Platform models to gain more control over data encryption and key management.

Enforcement mode | Detective   
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_MODEL_CMEK_DISABLED`  
Category names in the API | 

  * CC_CATEGORY_ARTIFICIAL_INTELLIGENCE
  * CC_CATEGORY_DATA_SECURITY

  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform model after it's been created. Delete the model and create a new model with CMEK enabled.

  1. Delete the existing model. For instructions, see [Delete a model from Agent Platform Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/delete-model).

  2. Create a new model. In the Google Cloud console, go to the [**Models** page](https://console.cloud.google.com/agent-platform/models).

  3. Click **Create model**.

  4. In the model details, expand **Advanced options**.

  5. Select **Cloud KMS key** and provide your CMEK.

  6. Click **Create**.




For more information about CMEK support in Agent Platform models, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform TensorBoard

Require customer-managed encryption keys (CMEK) for TensorBoard on Gemini Enterprise Agent Platform to gain more control over the encryption of experiment data and model visualizations.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_TENSORBOARD_CMEK_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform TensorBoard after it's been created. Delete the TensorBoard and create a new TensorBoard with CMEK enabled.

  1. Delete the TensorBoard. For instructions, see [Delete a TensorBoard instance](https://docs.cloud.google.com/vertex-ai/docs/experiments/tensorboard-setup#delete_tensorboard_instance).

  2. Create a TensorBoard. For instructions, see [Set up Vertex AI TensorBoard](https://docs.cloud.google.com/vertex-ai/docs/experiments/tensorboard-setup). To enable CMEK, enter the Cloud KMS key name in the **encryptionSpec** field.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform Training Pipelines

Require customer-managed encryption keys (CMEK) on Gemini Enterprise Agent Platform training pipelines to gain more control over the encryption of training data and resulting artifacts.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_TRAINING_PIPELINE_CMEK_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform training pipeline after it's been created. Delete the pipeline and create a new pipeline with CMEK enabled.

  1. Delete the existing training pipeline from the [**Training Pipelines** page](https://console.cloud.google.com/agent-platform/training/training-pipelines).

  2. Create a new training pipeline. In the Google Cloud console, go to the [**Training Pipelines page](https://console.cloud.google.com/agent-platform/training/training-pipelines).

  3. Click **Create training pipeline**.

  4. In the **Model Details** section, expand **Advanced options**.

  5. Select **Cloud KMS key** and provide your CMEK.

  6. Click **Create**.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK for Agent Platform Workbench Instance Disks

Require customer-managed encryption keys (CMEK) for Gemini Enterprise Agent Platform Workbench Instance disks to gain more control over data encryption.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_INSTANCE_DISK_CMEK_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform Workbench Instance disk after it's been created. Delete the existing instance and create a new instance with CMEK enabled.

  1. Delete the instance. For instructions to shut down the instance before deleting it, see [Shut down an Agent Platform Workbench Instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/shut-down).

  2. Create an instance. For instructions, see [Create an Agent Platform Workbench Instance with CMEK](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/cmek#create_a_instance_with_cmek). To enable CMEK, enter the Cloud KMS key name in the **diskEncryption** field.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/cmek).

###  Enable CMEK for AlloyDB Clusters

Enable customer-managed encryption keys (CMEK) in the AlloyDB cluster to gain more control over data encryption and key management. This control checks the encryption_type field in the cluster metadata to determine whether CMEK is enabled.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOYDB_CMEK_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on a AlloyDB cluster after it's been created. Delete the cluster and create a new cluster with CMEK enabled. To enable AlloyDB CMEK, see [Enable CMEK](https://cloud.google.com/alloydb/docs/cmek#enable_cmek).

###  Enable CMEK for BigQuery Datasets

Require customer-managed encryption keys (CMEK) for BigQuery datasets to gain more control over data encryption and key management. This control checks whether the kmsKeyName field in the defaultEncryptionConfiguration property is empty.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DATASET_CMEK_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on a dataset after it's been created. Go to the **BigQuery** page in the Google Cloud console and [create a dataset](https://cloud.google.com/bigquery/docs/datasets#create-dataset). To enable CMEK on the new dataset, [set a default CMEK key](https://cloud.google.com/bigquery/docs/customer-managed-encryption#dataset_default_key). Copy the original tables to your new CMEK-enabled dataset, and then delete the original datasets.

###  Enable CMEK for BigQuery Tables

The control provides the governance for the encryption key configuration for keys that protect the sensitive data for BigQuery tables. Using the control, you can detect when the data that is in scope is not protected by Customer Managed Encryption Key (CMEK). The CMEK gives you ownership and control of the keys that protect your sensitive data at rest in Google Cloud.

Enforcement mode | Detective   
---|---  
Severity | `HIGH`  
Finding category | `BIGQUERY_TABLE_CMEK_DISABLED`  
Category name in the API | CC_CATEGORY_DATA_SECURITY  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that the table is configured to use a default CMEK key. Please see [_https://cloud.google.com/bigquery/docs/customer-managed-encryption#switch-encryption_](https://cloud.google.com/bigquery/docs/customer-managed-encryption#switch-encryption).

###  Enable CMEK for BigQuery Tables

Require customer-managed encryption keys (CMEK) for BigQuery tables to gain more control over data encryption and key management. This control checks whether the kmsKeyName field in the encryptionConfiguration property is empty.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `BIGQUERY_TABLE_CMEK_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on a BigQuery table after it's been created. Create a new table with CMEK enabled, move the data over, and delete the original table. Go to the BigQuery page in the Google Cloud console and create a table. To enable CMEK on the new table, set a default CMEK key. Copy original data to your new CMEK-enabled table, and then delete the original table. For more information, see [Create a table protected by Cloud KMS](https://cloud.google.com/bigquery/docs/customer-managed-encryption#create_table).

###  Enable CMEK for Cloud SQL Databases

Require customer-managed encryption keys (CMEK) for Cloud SQL database instances to gain more control over data encryption and key management. This control checks the kmsKeyName field in the diskEncryptionKey object, in instance metadata, for the resource name of your CMEK. This control doesn't apply to on-premises databases.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_CMEK_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on a Cloud SQL database after it's been created. Create a new database with CMEK enabled, move the data over, and delete the original database. For more information, see [Cloud SQL for MySQL](https://cloud.google.com/sql/docs/mysql/configure-cmek), [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres/configure-cmek), and [Cloud SQL for SQL Server](https://cloud.google.com/sql/docs/sqlserver/configure-cmek).

###  Enable CMEK for Cloud Storage Buckets

Require customer-managed encryption keys (CMEK) for Cloud Storage buckets to gain more control over data encryption and key management. This control checks the encryption field in the bucket metadata for the resource name of your CMEK.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `BUCKET_CMEK_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Cloud Storage** > **Buckets** page in the Google Cloud console. In the list of buckets, click the name of the bucket and then click the **Configuration** tab. Edit **Encryption type** and enable CMEK for the bucket. For more information, see [Use customer-managed encryption keys](https://cloud.google.com/storage/docs/encryption/using-customer-managed-keys).

###  Enable CMEK for Runtime Templates in Agent Platform Colab Enterprise

Requires customer-managed encryption keys (CMEK) for runtime templates in Colab Enterprise on Gemini Enterprise Agent Platform to help secure runtime environments and associated data.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_WORKBENCH_RUNTIME_TEMPLATE_CMEK_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on an Agent Platform Colab Enterprise runtime template after it's been created. Delete the runtime template and create a new runtime template with CMEK enabled.

  1. Delete the runtime template. For instructions, see [Delete a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template#delete).

  2. Create a runtime template. For instructions, see [Create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template). To enable CMEK, enter the Cloud KMS key name in the **encryptionSpec** field.




For more information about CMEK support in Agent Platform, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/docs/general/cmek).

###  Enable CMEK on Compute Engine Persistent Disks

Require customer-managed encryption keys (CMEK) for Persistent Disks to encrypt your data on the VM, providing enhanced control over data encryption and key management. This control checks the kmsKeyName field in the diskEncryptionKey object, in disk metadata, for the resource name of your CMEK. This control doesn't apply to disks related to Cloud Composer environments, Dataflow jobs, and GKE instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DISK_CMEK_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on a Persistent Disk after it's been created. Delete the disk and create a new disk with CMEK enabled. Go to **Disks** within the **Compute Engine** page in the Google Cloud console. From the **Manage disk** page, delete the disk, and create a CMEK-enabled Persistent Disk. For more information, see [Encrypt a new persistent disk with your own keys](https://cloud.google.com/compute/docs/disks/customer-managed-encryption#encrypt_a_new_pd_cmek).

###  Enable CMEK on GKE Node Pool Boot Disks

Require customer-managed encryption keys (CMEK) for the boot disks for GKE node pools to gain more control over data encryption and key management.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `NODEPOOL_BOOT_CMEK_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You cannot enable CMEKs for node boot disks on an existing cluster. Create a new node pool with CMEK enabled, migrate your workloads, and delete the older node pool. Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Click the cluster name. In the **Nodes** tab, create new node pools with CMEK enabled. Migrate your workloads from the existing non-conforming node pool to the new node pools and then remove the old node pool. For more information, see [Create a node pool with CMEK-protected node boot disks](https://cloud.google.com/kubernetes-engine/docs/how-to/using-cmek#update_a_cluster_with_cmek-protected_node_boot_disks).

###  Enable Compliance Regulatory Settings for Cloud Deploy

Configures Cloud Deploy compliance settings.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUDDEPLOY_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Cloud Deploy AW Settings 

###  Enable Compliance Settings for Cloud Identity

Enables Access Transparency controls for Cloud Identity.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_IDENTITY_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_IDENTITY_AND_ACCESS_MANAGEMENT  
Revision number |  3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Parameters

`framework` |  `STRING` Required. Ensures additional compliance setting for the underlying services are correctly configured to meet the compliance level of the selected framework.  
---|---  
  
###  Enable Compliance Settings for Cloud Monitoring

Configures Cloud Monitoring compliance settings.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_MONITORING_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Cloud Monitoring Compliance Settings 

###  Enable Confidential Computing for Compute Engine Instances

Confidential Computing is the protection of data in use. It uses a hardware-based Trusted Execution Environment (TEE) to create secure and isolated environments that help prevent unauthorized access. This control checks the confidentialInstanceConfig property of instance metadata for the key-value pair 'enableConfidentialCompute' set to 'true'. This control doesn't apply to GKE instances, Serverless VPC Access, Dataflow jobs, or Compute Engine instances that are not of type N2D.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CONFIDENTIAL_COMPUTING_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable Confidential Computing on a VM instance after it's been created. Delete the current VM instance and create a Confidential VM from the **VM instances** page of **Compute Engine**. For more information, see [Create a Confidential VM instance](https://cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance).

###  Enable Control Plane Authorized Networks on GKE Clusters

Use authorized networks to help improve cluster security by blocking unauthorized IP addresses from accessing your cluster's control plane.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `MASTER_AUTHORIZED_NETWORKS_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure authorized networks for the cluster. Go to the **Clusters** > **Kubernetes Engine** in the Google Cloud console. Select the cluster and click **Edit**. Select **Enabled** on the **Control Plane Authorized Networks** drop-down list. Click **Add authorized network** and specify the authorized networks.

###  Enable CSEK On Compute Engine Persistent Disks

Require customer-supplied encryption keys (CSEK) to use your own encryption keys with Compute Engine. Only users who provide the correct key can access resources protected by a CSEK.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DISK_CSEK_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CSEK on a Persistent Disk after it's been created. Delete the disk and create a new disk with CSEK enabled. Go to **Disks** within the **Compute Engine** page in the Google Cloud console. From the **Manage disk** page, delete the disk, and create a CSEK-enabled disk. For more information, see [Encrypt disks with customer-supplied encryption keys](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption).

###  Enable Data Access Logs for AlloyDB

Data access logs must be enabled for AlloyDB streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOYDB_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for AlloyDB, go to IAM & Admin -> Audit Logs. Filter for 'AlloyDB API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for AlloyDB at Organization Level

Data access logs must be enabled for AlloyDB streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOYDB_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for AlloyDB, go to IAM & Admin -> Audit Logs. Filter for 'AlloyDB API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Bigtable

Data access logs must be enabled for Bigtable streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `BIGTABLE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for Bigtable, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Bigtable API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Bigtable at Organization Level

Data access logs must be enabled for Bigtable streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `BIGTABLE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for Bigtable, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Bigtable API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Cloud SQL

Data access logs must be enabled for Cloud SQL streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CLOUD_SQL_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for Cloud SQL, go to IAM & Admin -> Audit Logs. Filter for 'Cloud SQL Admin API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Cloud SQL at Organization Level

Data access logs must be enabled for Cloud SQL streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CLOUD_SQL_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for Cloud SQL, go to IAM & Admin -> Audit Logs. Filter for 'Cloud SQL Admin API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Cloud Storage

Data access logs must be enabled for Cloud Storage streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `STORAGE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for Cloud Storage, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Storage API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Cloud Storage at Organization Level

Data access logs must be enabled for Cloud Storage streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `STORAGE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for Cloud Storage, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Storage API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Datastore

Data access logs must be enabled for Datastore streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DATASTORE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for Datastore, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Datastore API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Datastore at Organization Level

Data access logs must be enabled for Datastore streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DATASTORE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for Datastore, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Datastore API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Filestore

Data access logs must be enabled for Filestore streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `FILESTORE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for Filestore, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Filestore API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Filestore at Organization Level

Data access logs must be enabled for Filestore streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `FILESTORE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for Filestore, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Filestore API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Firestore

Data access logs must be enabled for Firestore streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `FIRESTORE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for Firestore, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Firestore API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Firestore at Organization Level

Data access logs must be enabled for Firestore streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `FIRESTORE_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for Firestore, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Firestore API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Secret Manager

Data access logs must be enabled for Secret Manager streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SECRET_MANAGER_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for Secret Manager, go to IAM & Admin -> Audit Logs. Filter for 'Secret Manager API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Secret Manager at Organization Level

Data access logs must be enabled for Secret Manager streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SECRET_MANAGER_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for Secret Manager, go to IAM & Admin -> Audit Logs. Filter for 'Secret Manager API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Spanner

Data access logs must be enabled for Spanner streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SPANNER_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable data access logs for Spanner, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Spanner API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Access Logs for Spanner at Organization Level

Data access logs must be enabled for Spanner streamed to monitoring service.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SPANNER_DATA_ACCESS_LOGS_DISABLED`  
Revision number |  1   
Supported target resources |  Organization   
  
#### Remediation steps

To enable data access logs for Spanner, go to IAM & Admin -> Audit Logs. Filter for 'Cloud Spanner API' and enable 'Admin Read', 'Data Read', and 'Data Write' log types, then click Save.

###  Enable Data Lineage API

Enable the Data Lineage API to better track data flow through generative AI systems.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `DATA_LINEAGE_API_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable data lineage for Google Cloud projects. For more information, see [About data lineage](https://cloud.google.com/dataplex/docs/about-data-lineage).

###  Enable Data Write Audit Logs for Organization Policy

Ensure that Organization Policy Service audit logs for the DATA_WRITE permission type are enabled for all users.

Enforcement mode | Audit   
---|---  
Finding category | `ORGPOLICY_AUDIT_LOGS_DATA_WRITE_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that you can monitor Data Access logs for organization policy constraint changes. To enable the DATA_WRITE permission, see [Configure Data Access audit logs with the Google Cloud console](https://cloud.google.com/logging/docs/audit/configure-data-access#config-console).

###  Enable Delete to Trash Feature for Agent Platform Workbench Instances

Enable the Delete to Trash metadata feature for Gemini Enterprise Agent Platform Workbench Instances to provide a crucial recovery safety net and help prevent accidental data loss.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_WORKBENCH_DELETE_TO_TRASH_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable delete to trash for the existing instance.

  1. In the Google Cloud console, go to the [**Instances** page](https://console.cloud.google.com/agent-platform/workbench/instances).

  2. Click the instance that you want to configure.

  3. In the **Software and security** tab, add the `notebook-enable-delete-to-trash` metadata key and set the value to `TRUE`.




For more information, see [Update an instance's metadata](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/manage-metadata#update).

###  Enable DNSSEC for Cloud DNS

Domain Name System Security Extensions (DNSSEC) helps prevent attackers from signing in to DNS records in your Cloud DNS zones.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DNSSEC_DISABLED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable DNSSEC for Cloud DNS zones. Go to the **Network Services** > **Cloud DNS** page in the Google Cloud console and enable **DNSSEC** for the Cloud DNS zones. For more information, see [Enable DNSSEC for existing managed public zones](https://cloud.google.com/dns/docs/dnssec-config#enabling).

###  Enable Encryption for Mobile Devices

Configure full-device encryption or container encryption to protect the confidentiality and integrity of information stored on mobile devices.

Enforcement mode | Audit   
---|---  
Finding category | `MOBILE_DEVICES_ENCRYPTION_NOT_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Enable full-device encryption. For Android devices, use device settings. On iOS devices, full-device encryption is enabled by default when a passcode is set.

  * Implement a mobile device management solution that enforces encryption. Consider [advanced mobile management](https://support.google.com/a/answer/7396025).

  * To encrypt containers for BYOD or work profiles, use a mobile device management solution.

  * On Google Cloud, [Grant IAM roles](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to mobile device users.




###  Enable Encryption on GKE Clusters

Enable application-layer secrets encryption on a Google Kubernetes Engine (GKE) cluster to create an additional layer of security for sensitive workloads.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CLUSTER_SECRETS_ENCRYPTION_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Determine whether to use an existing Cloud KMS key or create a new key. For more information, see [Creating a Cloud KMS key](https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets#creating-key). Next, [enable application-layer secrets encryption](https://cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets#enabling).

###  Enable Enhanced IAM Audit Logging

Enable audit logs for the IAM API, Security Token Service API, and Service Account Credentials API. Include the ADMIN_READ, DATA_READ, and DATA_WRITE types.

Enforcement mode | Audit   
---|---  
Finding category | `IAM_AUDITLOG_PRIVILEGED_ACCESS_MANAGEMENT_VIOLATION`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable `DATA_READ`, `DATA_WRITE`, and `ADMIN_READ` for the following APIs: `iam.googleapis.com`, `iamcredentials.googleapis.com`, and `sts.googleapis.com`. For more information, see the following:

  * [Service Account Credentials audit logging](https://cloud.google.com/iam/docs/audit-logging/audit-logging-iamcreds)

  * [Security Token Service audit logging](https://cloud.google.com/iam/docs/audit-logging/audit-logging-sts)

  * [Identity and Access Management audit logging](https://cloud.google.com/iam/docs/audit-logging)




###  Enable Firewall Rule Logging

Firewall rules logging lets you audit, verify, and analyze the effects of your firewall rules, and provide an early warning that the network is being used in an unapproved manner. This control checks the logConfig property in the firewall metadata to see if it's empty or contains the key-value pair "enable" set to "false". This control doesn't apply to GKE instances, firewall rules created by GKE or Serverless VPC Access.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `FIREWALL_RULE_LOGGING_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **VPC Network** > **Firewall** page in the Google Cloud console. For more information, see [Enable firewall rules logging](https://cloud.google.com/firewall/docs/using-firewall-rules-logging#enable).

###  Enable Flow Logs for VPC Subnet

VPC Flow Logs provides information that you can use for network monitoring, forensics, real-time security analysis, and expense optimization. This control doesn't check whether VPC Flow Logs are enabled for Serverless VPC Access or Cloud Load Balancing subnets.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable flow logs for the VPC network. Go to the **VPC Network** > **VPC networks** page in the Google Cloud console. Click the network name. On the **VPC network details** page, click the **Subnets** tab. Click the subnet name and edit it to enable **Flow logs**.

###  Enable Integrity Monitoring for Agent Platform Workbench Instances

Enable integrity monitoring on Gemini Enterprise Agent Platform Workbench Instances to continuously attest the boot integrity of your VMs against a trusted baseline.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_WORKBENCH_INTEGRITY_MONITORING_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable integrity monitoring for the Agent Platform Workbench Instance.

  1. Stop your instance:



`gcloud workbenck instances stop INSTANCE_NAME --location=LOCATION --format="yaml(state)"`

  2. Enable the vTPM feature:



`gcloud workbench instances update INSTANCE_NAME --location=LOCATION --shielded-vtpm true --format="yaml(gceSetup.shieldedInstanceConfig.enableVtpm)" `

  3. Enable integrity monitoring:



`gcloud workbench instances update INSTANCE_NAME --location=LOCATION --shielded-integrity-monitoring true --format="yaml(gceSetup.shieldedInstanceConfig.enableIntegrityMonitoring)"`

  4. Restart the instance:



`gcloud workbench instances start INSTANCE_NAME --location=LOCATION --format="yaml(state)"`

###  Enable Integrity Monitoring on GKE Clusters

Integrity monitoring lets you respond to integrity failures and help prevent compromised nodes from being deployed into the cluster. This control checks the shieldedInstanceConfig property of the nodeConfig object for the key-value pair "enableIntegrityMonitoring" set to "true".

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `INTEGRITY_MONITORING_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable integrity monitoring on a GKE node pool after it's been created. Create a new node pool with integrity monitoring enabled, migrate your workloads, and delete the older node pool:

  1. Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Click the cluster name.

  2. Click **Add Node Pool**.

  3. In the **Security** tab, select **Enable integrity monitoring** and click **Create**.

  4. Migrate your workloads from the existing non-conforming node pool to the new node pools and then remove the old node pool.




To migrate workloads, see [Vertically scale by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes).

###  Enable integrity verification of software and firmware components

Enforce software and firmware integrity verification to detect unauthorized changes using developer-provided tools, techniques, and mechanisms.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_FIRMWARE_INTEGRITY_VERIFICATION_CONTROLS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Mandate integrity verification of software and firmware components for critical risk information systems, system components, or information system services. Examples of critical risk systems, system components, or information system services include validating the integrity of the BIOS and other firmware updates.

###  Enable Intranode Visibility for GKE Clusters

Intranode visibility makes Pod-to-Pod traffic visible for monitoring and lets you use VPC flow logging or other VPC features to monitor or control intranode traffic.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `INTRANODE_VISIBILITY_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. In the **Networking** section, click **Edit intranode visibility** in the **Intranode visibility** row, and select **Enable Intranode visibility**.

###  Enable IP Alias Range for GKE Clusters

Google Cloud alias IP ranges let you assign ranges of internal IP addresses as aliases, so your cluster is scalable and interacts better with Google Cloud products and entities.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `IP_ALIAS_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For instructions on how to create a cluster enabled with alias IP range, see [Create a VPC-native cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).

###  Enable L7 DDoS Protection

Ensure that L7 DDoS protection is enabled.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `L7_DDOS_PROTECTION_NOT_VERIFIED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure advanced network DDoS protection is enabled. For more information, see [Configure advanced network DDoS protection](https://cloud.google.com/armor/docs/advanced-network-ddos).

###  Enable Load Balancer Logging

Logging for a Cloud Load Balancing backend service provides visibility into the HTTP(S) network traffic towards your web applications. This control checks whether the enableLogging property of the backend service on the load balancer is set to true.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `LOAD_BALANCER_LOGGING_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable logging on a backend service, see [Enabling logging on an existing backend service](https://cloud.google.com/load-balancing/docs/https/https-logging-monitoring#enabling_logging_on_an_existing_backend_service).

###  Enable Log Checkpoints Flag for PostgreSQL

This control checks the databaseFlags property in the instance metadata for the key-value pair 'log_checkpoints' set to 'on'. Enabling log_checkpoints causes checkpoints and restart points to be logged in the server log. Some statistics are included in the log messages, including the number of buffers written and the time spent writing them.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_CHECKPOINTS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_checkpoints** database flag to **On** for the instance.

###  Enable Log Connections Flag for PostgreSQL

Turn on the log_connections flag for the PostgreSQL instance. This control checks the databaseFlags property of instance metadata for the key-value pair "log_connections" set to "on". Enabling the log_connections setting causes attempted connections to the server to be logged, along with successful completion of client authentication. The logs can be useful in troubleshooting issues and confirming unusual connection attempts to the server. This control doesn't apply to on-premises databases.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_CONNECTIONS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn the **log_connections** flag on. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_connections** database flag to **On** for the instance.

###  Enable Log Disconnections Flag for PostgreSQL

Turn on the log_disconnections flag for the PostgreSQL instance. When set, end-of-session events are logged. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_DISCONNECTIONS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn the **logs_disconnections** flag on. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_disconnections** database flag to **On** for the instance.

###  Enable Log Duration Flag for PostgreSQL instance

Turn on the log_duration flag to log the duration of every completed statement. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_DURATION_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_duration** database flag to **On** for the instance.

###  Enable Log Error Verbosity Flag for PostgreSQL

Turn on verbose or default logging using the log_error_verbosity flag for the PostgreSQL instance. When set, the flag controls detail in logged messages. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_ERROR_VERBOSITY`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **log_error_verbosity** flag. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_error_verbosity** database flag to **default** or **verbose** for the instance.

###  Enable Log Events Data Sharing

The Google Admin console lets you share log events data from your Google Workspace or Cloud Identity with services in Google Cloud. Turn on log events sharing to view this data in Cloud Audit logs.

Enforcement mode | Audit   
---|---  
Finding category | `LOG_EVENTS_DATA_SHARING_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To change data sharing options for Google Cloud audit logs in the Google Admin console, go to **Menu > Account > Account settings > Legal and compliance > Sharing options**. For more information, see [Share data with Google Cloud services](https://support.google.com/a/answer/9320190).

###  Enable Log Locks Wait Flag for PostgreSQL instance

Turn on the log_lock_waits flag for PostgreSQL to generate log entries for unusually long session waits.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_LOCK_WAITS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_lock_waits** database flag to **On** for the Cloud SQL instance.

###  Enable Log Min Error Statement Flag for PostgreSQL

Configure the log_min_error_statement flag as per your organization's logging policy for the PostgreSQL instance. This flag controls logging of SQL statements that cause errors. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_MIN_ERROR_STATEMENT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_min_error_statement** database flag for the Cloud SQL instance. The value of this flag must be set as per your organization's logging policy. Possible values are info, notice, warning, error, debug1, debug2, debug3, debug4, and debug5.

###  Enable Log Min Messages Flag for PostgreSQL

Set the log_min_messages flag to warning or lower levels for the PostgreSQL instance. This flag controls message levels recorded in logs. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SQL_LOG_MIN_MESSAGES_INCORRECT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **log_min_messages** flag. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_min_messages** database flag for the Cloud SQL instance to one of Notice, Info, Debug1, Debug2, Debug3, Debug4, or Debug5.

###  Enable Log Statement Flag for PostgreSQL

Set the log_statement flag to ddl for the PostgreSQL instance. When set to ddl, all data definition statements are logged for forensic analysis.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SQL_LOG_STATEMENT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_statement** database flag to **ddl** for the Cloud SQL instance.

###  Enable Log Temp Files Flag for PostgreSQL instance

Set the log_temp_files flag to 0 for PostgreSQL. When set to 0, all temp files are logged. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_TEMP_FILES`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_temp_files** database flag to **0** for the Cloud SQL instance.

###  Enable Looker (Google Cloud core) Compliance with FedRAMP or DoD Impact Levels

Configure Looker (Google Cloud core) within a data boundary that supports FedRAMP Moderate, FedRAMP High, Department of Defence Impact Level 2 (IL2) and that's FIPS 140-2 level 1 compliant.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `LOOKER_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Looker Core AW Settings 

#### Parameters

`framework` |  `STRING` Required. Required: Select the regulatory framework that your services must be in compliance with.  
---|---  
  
###  Enable Model Armor

Enable Model Armor to help mitigate risks that are associated with Vertex AI endpoints.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `MODEL_ARMOR_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable Model Armor, see the [Model Armor overview](https://docs.cloud.google.com/security/docs/model-armor-overview).

###  Enable Network Policy on GKE Clusters

Restrict network connections between pods with a NetworkPolicy resource. A NetworkPolicy resource acts as pod-level firewall and only permits explicitly allowed connections. This control checks the networkPolicy field of the addonsConfig property for the key-value pair, "disabled" set to "true".

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `NETWORK_POLICY_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. Click the cluster name, and in the **Networking** section, edit the **Calico Kubernetes Network policy** to enable it for both the control plane and nodes. For more information, see [Restrict network traffic among Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#restrict_with_network_policy).

###  Enable Object Versioning on Buckets

Versioning lets you track changes to objects and to enable recovery of specific versions of an object.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `OBJECT_VERSIONING_DISABLED_ON_BUCKETS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable versioning for Cloud Storage buckets, see [Set Object Versioning on a bucket](https://cloud.google.com/storage/docs/using-object-versioning#set).

###  Enable OS Login

Enable OS Login to centralize SSH key management with Identity and Access Management (IAM).

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `OS_LOGIN_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable OS Login. Go to the **Metadata** page for the Compute Engine from the Google Cloud console. Click **Edit** and add an item with the key set to **enable-oslogin** , value set to **TRUE**.

###  Enable OS Login for All Instances at Project Level

Enable OS Login to centralize SSH key management with Identity and Access Management (IAM).

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `OS_LOGIN_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable OS Login for the project. On the **Metadata** page in the Google Cloud console, add the key **enable-oslogin** and value **TRUE**. For more information, see [Enable OS Login for all VMs in a project](https://cloud.google.com/compute/docs/oslogin/set-up-oslogin#enable_os_login_for_all_vms_in_a_project).

###  Enable PodSecurityPolicies for GKE Clusters

Define and authorize a PodSecurityPolicy to validate requests to create and update pods on a Google Kubernetes Engine (GKE) cluster. This control checks whether the GKE cluster version is 1.25 or later because PodSecurityPolicy is deprecated. If the GKE cluster version is less than 1.25, the securityPostureConfig.mode must be BASIC or ENTERPRISE.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `POD_SECURITY_POLICY_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable the PodSecurityPolicy controller on the GKE clusters. For more information, see [PodSecurityPolicy](https://cloud.google.com/kubernetes-engine/docs/deprecations/podsecuritypolicy).

###  Enable Private Clusters for GKE

Use private clusters in Google Kubernetes Engine (GKE) to limit outbound internet access and node discoverability. This control checks whether the networkConfig.defaultEnablePrivateNodes or privateClusterConfig.enablePrivateNodes property is set to false.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `PRIVATE_CLUSTER_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't change an existing cluster into a private cluster. Create a private cluster, move your workloads, and delete the older cluster. Go to the **Kubernetes clusters** page in the Google Cloud console and create a cluster with **Private cluster** turned on. For more information, see [Create a private cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/legacy/network-isolation). Migrate your workloads and then remove the old cluster.

###  Enable Private Google Access for VPC Subnets

Allow VM instances with only internal (private) IP addresses to reach Google public APIs with Private Google Access. This control checks whether the privateIpGoogleAccess property of Compute Engine subnetworks is set to false.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `PRIVATE_GOOGLE_ACCESS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable Private Google Access for the subnets that don't have access to Google public APIs and services. For more information, see [Enable Private Google Access](https://cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga).

###  Enable Private Google Access on an instance

Private Google Access enables VM instances with only private, internal IP addresses to reach the public IP addresses of Google APIs and services. Configuring cluster hosts to use only private IPs helps improve security.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CLUSTER_PRIVATE_GOOGLE_ACCESS_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable Private Google Access on the cluster. Complete the following steps:

  1. Go to the **VPC Network** > **VPC networks** page in the Google Cloud console.
  2. Click the network name.
  3. On the **VPC network details** page, click **Subnets** tab.
  4. Click the subnet name associated with the Kubernetes cluster in the finding.
  5. On the **Subnet details** page, click **Edit**.
  6. Under **Private Google Access** , select **On**.



###  Enable Provenance Tracking of Agent Platform Synthetic Datasets

Attach labels to synthetic data for Gemini Enterprise Agent Platform so that you can track their provenance.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `LABELS_NOT_ENABLED_FOR_SYNTHETIC_VERTEX_AI_DATASETS`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use labels to track Agent Platform synthetic datasets. For more information, see [Adding labels to resources](https://docs.cloud.google.com/bigquery/docs/adding-labels) and [Tags and labels](https://docs.cloud.google.com/storage/docs/tags-and-labels).

###  Enable Regulatory Settings for Apigee

Enforce compliance settings for Apigee by disabling specific features to meet regulatory requirements. The following Apigee features are disabled: Portal, Looker Studio, Classic UI, Apigee Hybrid, and Apigee Eval.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `APIGEE_REGULATORY_SETTINGS_NOT_ENFORCED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Apigee Compliance Settings 

###  Enable Regulatory Settings for Cloud DNS

Configure Cloud DNS to help you meet your regulatory requirements.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_DNS_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Cloud DNS Compliance Settings 

###  Enable Regulatory Settings for Gemini Enterprise

Configure the Gemini Enterprise compliance level for Assured Workloads.

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `GEMINI_ENTERPRISE_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** Agentspace AW Config 

#### Parameters

`framework` |  `STRING` Required. Ensures additional compliance setting for the underlying services are correctly configured to meet the compliance level of the selected framework.  
---|---  
  
###  Enable Response Grounding in Agent Platform

Use grounding techniques to connect model output to verifiable sources of information so that the Gemini Enterprise Agent Platform model produces outputs based on reliable data and reduces the possibility of producing misinformation.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_GROUNDING_DISABLED`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure Agent Platform grounding features to ground responses. For more information, see [Grounding overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview).

###  Enable SDP for Data Discovery

The Sensitive Data Protection (SDP) discovery service helps you protect data across your organization by identifying where sensitive and high-risk data resides.

Enforcement mode | 

  * Audit 
  * Detective 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SDP_TO_DISCOVER_DATA_DISABLED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use SDP to discover the data and address critical findings. For instructions on using SDP, see [Inspect Google Cloud storage and databases for sensitive data](https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage).

###  Enable Secure Boot for Agent Platform Workbench Instances

Enable secure boot for Gemini Enterprise Agent Platform Workbench Instances to help prevent the execution of unauthorized or malicious software during the boot process.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_WORKBENCH_SECURE_BOOT_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable secure boot.

  1. Stop your Agent Platform WorkBench Instance:



`gcloud workbenck instances stop INSTANCE_NAME --location=LOCATION --format="yaml(state)"`

  2. Enable the secure boot feature:



```gcloud workbench instances update INSTANCE_NAME --location=LOCATION --shielded-secure-boot true --format="yaml(gceSetup.shieldedInstanceConfig.enableSecureBoot)"``

  3. Restart the instance:



`gcloud workbench instances start INSTANCE_NAME --location=LOCATION --format="yaml(state)"`

###  Enable Secure Boot for Runtime Templates in Agent Platform Colab Enterprise

Enable secure boot in runtime templates in Colab Enterprise on Gemini Enterprise Agent Platform to help prevent unauthorized code execution and help protect operating system integrity.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_RUNTIME_TEMPLATE_SECURE_BOOT_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't change this setting after the runtime template is created. Delete the existing runtime template and create a new one with secure boot enabled.

  1. Delete the runtime template. For instructions, see [Delete a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template#delete).

  2. Create a runtime template. For instructions, see [Create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template). To enable secure boot, in the **Configure compute** section, select **Secure Boot**.




###  Enable Secure Boot for Shielded GKE Nodes

Enable Secure Boot to authenticate the boot components of your node VMs, such as the kernel and the bootloader, during the boot process. This control checks the shieldedInstanceConfig property of the nodeConfig object to determine if enableSecureBoot is set to true.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `NODEPOOL_SECURE_BOOT_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create a node pool with Secure Boot and migrate your workloads from the existing non-conforming node pools to the new node pools. After moving the workloads, delete the original non-conforming node pool. For more information, see [Secure boot](https://cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes#secure_boot).

###  Enable Secure Boot on Compute Engine Instances

Secure Boot helps to protect VM instances against advanced threats such as rootkits and bootkits. This control doesn't apply to GKE instances, Compute Engine disks that have GPU accelerators and don't use Container-Optimized OS, Compute Engine guest operating systems that don't use Unified Extensible Firmware Interface (UEFI), or Serverless VPC Access resources.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `COMPUTE_SECURE_BOOT_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn on Secure Boot. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console. Select the instance name. On the **VM instance details** page, stop the instance. Click **Edit**. Enable Secure Boot under **Shielded VM** , and start the instance.

###  Enable Security Command Center

Activate Security Command Center to help mitigate and remediate risks related to misconfigurations, vulnerabilities, and threats.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `SCC_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To activate Security Command Center (SCC), see [Overview of activating Security Command Center](https://cloud.google.com/security-command-center/docs/activate-scc-overview).

###  Enable Sensitive Data Protection to Detect PII in Agent Platform Training Data

Enable Sensitive Data Protection data for Gemini Enterprise Agent Platform datasets and configure the inspection template to detect personally identifiable information (PII) and sensitive personally identifiable information (SPII) infotypes. Also set the profiling frequency to minimize the risks that are associated with linking AI-generated content back to individual human subjects.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SDP_DISABLED_FOR_VERTEX_DATASETS`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For more information, see [Enable sensitive data discovery for Agent Platform](https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-vertex-ai).

###  Enable Shielded GKE Nodes on a Cluster

Shielded Google Kubernetes Engine (GKE) nodes help to protect against Pod vulnerabilities by preventing attackers from accessing cluster secrets. This control checks the shieldedNodes property for the key-value pair named "enabled".

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CLUSTER_SHIELDED_NODES_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable Shielded GKE nodes for the cluster:

  1. Go to the **Clusters** page of **Kubernetes Engine** in the Google Cloud console.

  2. Select the cluster from the list.

  3. Under **Security** , edit **Shielded GKE nodes** and select the **Enable Shielded GKE nodes** checkbox.




###  Enable Shielded VM for Compute Engine Instances

Ensure Compute Engine instances are created with Shielded VM enabled.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SHIELDED_VM_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable Shielded VM for the instance. For more information, see [Enable Shielded VM options](https://cloud.google.com/compute/shielded-vm/docs/quickstart#enable_all_shielded_vm_options).

###  Enable Skip Show Database Flag for MySQL

Turn on the skip_show_database flag for the MySQL instance to prevent users without privilege from using SHOW DATABASES. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_SKIP_SHOW_DATABASE_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn on the **skip_show_database** flag. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **skip_show_database** flag to **On** for the MySQL instance.

###  Enable SSL Encryption On AlloyDB Instances

Enforce Secure Sockets Layer (SSL) to permit only authenticated and encrypted connections to AlloyDB instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `ALLOYDB_SSL_NOT_ENFORCED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enforce SSL for the AlloyDB cluster:

1 Go to the **AlloyDB** > **Clusters** page in the Google Cloud console.

  2. Click the cluster from the **Resource Name** column, and edit the primary instance.

  3. Enable **Only allow SSL connections**.




###  Enable Subnet Flow Logs

Monitor sub network flows using VPC Flow Logs for security analysis, forensics, and expense optimization.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `FLOW_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To configure VPC Flow Logs for a subnet, see [Enable VPC Flow Logs for a subnet](https://cloud.google.com/vpc/docs/using-flow-logs#enable-subnet).

###  Enable System Use Notifications on VMs

Implement system use notifications (messages or warning banners) before users log in. The notifications are retained on the screen until users acknowledge the usage conditions and take explicit actions to log on to or further access the information system.

Enforcement mode | Audit   
---|---  
Finding category | `SYSTEM_USE_NOTIFICATIONS_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create a banner text file and transfer it to your VMs using the Secure Copy Protocol (SCP) file transfer utility. For example: `gcloud compute scp banner.txt YOUR_VM_NAME:~ --zone YOUR_INSTANCE_ZONE` For more information, see [Transfer files to Linux VMs](https://cloud.google.com/compute/docs/instances/transfer-files).

###  Enable the Confidential VM Organization Policy Constraint

To help protect against memory attacks, enable the Restrict Non-Confidential Computing (compute.restrictNonConfidentialComputing) organization policy constraint so that each virtual machine (VM) is a Confidential VM.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_CONFIDENTIAL_VM_POLICY`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable the Restrict Non-Confidential Computing organization policy. For instructions, see [Enforce Confidential VM use](https://cloud.google.com/confidential-computing/confidential-vm/docs/enforce-confidential-vm-use).

###  Enable the Restrict Authorized Networks on Cloud SQL Instances Organization Policy Constraint

Enable the Restrict Authorized Networks on Cloud SQL instances (constraints/sql.restrictAuthorizedNetworks) organization policy constraint to restrict adding Authorized Networks for unproxied database access to Cloud SQL instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `RESTRICT_AUTHORIZED_NETWORKS_ORG_POLICY`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable the Restrict Authorized Networks on Cloud SQL instances constraint in the **Organization Policies** page from the Google Cloud console. For more information, see [Organization policy constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) and [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

###  Enable Uniform Bucket-Level Access on Cloud Storage Buckets

When uniform bucket-level access is enabled, only bucket-level Identity and Access Management (IAM) permissions grant access to that bucket and the objects that it contains.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `BUCKET_POLICY_ONLY_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Cloud Storage** > **Buckets** in the Google Cloud console. In the list of buckets, click the name of the bucket and then click the **Configuration** tab. In the **Permissions** section, click **Edit access control model** , and select **Uniform**. For more information, see [Uniform bucket-level access](https://cloud.google.com/storage/docs/uniform-bucket-level-access).

###  Enable VM Manager

Enforce the compute.requireOsConfig organization policy constraint to ensure that VM Manager (the OS Config API) is enabled on all new projects. This constraint also prevents disabling VM Manager at the project or instance level.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `COMPUTE_REQUIRE_OSCONFIG_NOT_ENFORCED`  
Category name in the API | CC_CATEGORY_INFRASTRUCTURE  
Revision number |  1.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/compute.requireOsConfig`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `compute.requireOsConfig` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Enable VPC Flow Logs for Compute Engine Instances

VPC Flow Logs provides you visibility into network throughput and performance.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `COMPUTE_VPC_ADVANCED_FLOW_LOGS_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To configure VPC Flow Logs, see [Configure VPC Flow Logs](https://cloud.google.com/vpc/docs/using-flow-logs).

###  Enable vTPM on Agent Platform Workbench Instances

Enable the virtual trusted platform module (vTPM) on Gemini Enterprise Agent Platform Workbench Instances to safeguard the boot process and gain more control over encryption.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_WORKBENCH_VTPM_DISABLED`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable vTPM for the Agent Platform Workbench Instance.

  1. Stop your instance:



`gcloud workbenck instances stop INSTANCE_NAME --location=LOCATION --format="yaml(state)"`

  2. Enable the vTPM feature:



`gcloud workbench instances update INSTANCE_NAME --location=LOCATION --shielded-vtpm true --format="yaml(gceSetup.shieldedInstanceConfig.enableVtpm)" `

  3. Restart the instance:



`gcloud workbench instances start INSTANCE_NAME --location=LOCATION --format="yaml(state)"`

###  Enable Workload Identity Federation for GKE on clusters

Access Google Cloud services from within Google Kubernetes Engine (GKE) using Workload Identity Federation for GKE for improved security and manageability. This control checks whether the workloadIdentityConfig property of a cluster or the workloadMetadataConfig property of a node pool is set to GKE_METADATA. This control requires the roles/container.clusterViewer permission.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `WORKLOAD_IDENTITY_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable Workload Identity Federation for GKE. For more information, see [Enable Workload Identity Federation for GKE on clusters and node pools](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools).

###  Enabled Backups

Backups are performed according to the scope and frequency defined in backup plans and according to the asset criticality (summarized in labels/tags).

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `BACKUPS_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable backups for the resource to ensure data is protected and recoverable. For guidance, see documentation for GKE backups (https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install), Cloud SQL backups (https://cloud.google.com/sql/docs/mysql/backup-recovery/backups), or AlloyDB backups (https://cloud.google.com/alloydb/docs/backup/overview).

###  Encrypt Data at Rest with CMEK

Encrypt data at rest with customer-managed encryption keys (CMEK).

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DATA_AT_REST_CMEK_ENCRYPTION_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Check the encryption status for Cloud Storage buckets and ensure the KMS key name is set. For Compute Engine instances, the **kmsKeyName** for instance and attached disks must not be empty. For Cloud SQL instances, the **kmsKeyName** within **diskEncryptionConfiguration** must not be empty.

###  Encrypt Pub/Sub topic with CMEK

Encrypt a Pub/Sub topic with customer-managed encryption keys (CMEKs) to gain more control over data encryption and key management.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `PUBSUB_CMEK_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on a Pub/Sub topic after it's been created. Delete the topic and create a new topic with CMEK enabled. In the Google Cloud console, go to the Pub/Sub **Topics** page. Delete and recreate the Pub/Sub topic with CMEK. For more information, see [Delete topics](https://cloud.google.com/pubsub/docs/delete-topic) and [Configure a topic with CMEK](https://cloud.google.com/pubsub/docs/encryption#configure_a_topic_with_cmek).

###  Enforce 2-Step Verification for Super Admin Accounts

Google recommends using Titan security keys as the second factor for Super Admin accounts. The Titan security key helps protect against unauthorized access.

Enforcement mode | Audit   
---|---  
Finding category | `SUPER_ADMIN_ACCOUNTS_MFA_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enforce 2-Step Verification, sign in to the Google Admin console (admin.google.com), navigate to **Security** > **Authentication** > ** 2-Step Verification**, and turn on enforcement for the organizational unit or group containing the super administrators.

###  Enforce Agent Platform Environment Options

Use the "Restrict environment options on new Vertex AI Workbench user-managed notebooks" (ainotebooks.environmentOptions) organization policy constraint to define the allowed VM and container image options for creating new Gemini Enterprise Agent Platform Workbench notebooks and instances.

Enforcement mode | Audit   
---|---  
Finding category | `ORG_POLICY_VERTEXAI_ENVIRONMENT_OPTIONS_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Restrict environment options on new Vertex AI Workbench user-managed notebooks** (`ainotebooks.environmentOptions`) organization policy for both projects and folders. The expected format for VM instances is `ainotebooks-vm/PROJECT_ID/IMAGE_TYPE/CONSTRAINED_VALUE`. Replace IMAGE_TYPE with image-family or image-name.

The expected format for container images must be `ainotebooks-container/CONTAINER_REPOSITORY:TAG`.

###  Enforce allowed CMEK crypto key projects

Enforces that CMEK crypto keys can only be used from a specific set of projects.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `CMEK_CRYPTO_KEY_PROJECTS_NOT_RESTRICTED`  
Category name in the API | CC_CATEGORY_ENCRYPTION  
Revision number |  1.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/gcp.restrictCmekCryptoKeyProjects`  
---|---  
  
#### Parameters

`allowedCmekCryptoKeyProjects` |  `STRINGLIST` Required. List of projects, folders, and organizations from which CMEK crypto keys can be selected. For example: 'under:projects/PROJECT_ID', 'under:folders/FOLDER_ID', 'under:organizations/ORGANIZATION_ID'. Use 'under:$TARGET_RESOURCE$' to include the deployment target as a source of CMEK keys.  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `gcp.restrictCmekCryptoKeyProjects` constraint to the required values:

    * Allowed values: $allowedCmekCryptoKeyProjects

See [Updating policies with list rules](https://docs.cloud.google.com/organization-policy/apply-policies#list_constraints) and [Limit the use of Cloud KMS keys for CMEK](https://docs.cloud.google.com/kms/docs/cmek-org-policy#project-constraint).




###  Enforce CMEK

Use customer-managed encryption keys (CMEKs) for increased ownership and control of the keys that protect your data at rest in Google Cloud.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CMEK_NOT_ENFORCED`  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Configure CMEK across your services.

  * Consider the [Certificate Authority Service](https://cloud.google.com/certificate-authority-service/docs/ca-service-overview) for hardware-protected private keys which are FIPS 140-2 Level 3 validated.




###  Enforce CMEK for Supported Services

Use the "Restrict which services may create resources without CMEK" (gcp.restrictNonCmekServices) organization policy constraint to define which Google Cloud services must use customer-managed encryption keys (CMEKs).

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORGPOLICY_RESTRICT_NON_CMEK_SERVICES_VIOLATED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To configure this constraint, see [Require CMEK protection](https://cloud.google.com/kms/docs/cmek-org-policy#require-cmek).

###  Enforce Compute Session Inactive Policy

Monitor user inactivity on Compute Engine instances and end sessions after a session has been inactive for 30 minutes.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `COMPUTE_SESSION_INACTIVITY_POLICY_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Set the [`httpkeepAliveTimeoutSec` attribute]https://cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute#update-keepalive-timeout) to the session timout.

  * Verify you’re monitoring user activity for your Compute Engine VMs. For example, the following script sets a metadata flag (terminate-session=true) if the idle time exceeds 30 minutes: ` !/bin/ # Logic to check user activity if [ $(idle_time_minutes) -gt 30 ]; then gcloud compute instances add-metadata INSTANCE_NAME --metadata terminate-session=true fi `

  * Verify session termination scripts are implemented. For example, the following script ends the session based on your conditions: ` !/bin/ # Logic to terminate the user session # (This may involve logging out the user, killing user processes, etc.) # Clear the metadata flag gcloud compute instances add-metadata INSTANCE_NAME --metadata terminate-session=false `




###  Enforce Configuration Management for IAC

Ensure configuration management for your infrastructure as code (IAC) during system, component, or service development. Consider version control and change tracking.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_IAC_CONFIGURATION_MANAGEMENT`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Use Deployment Manager or Terraform to define and manage your IAC files. Use a Git repository to track changes and for version control.

  * Implement a change management process that includes code reviews and approvals.

  * Create a change implementation process and use IAM to ensure only authorized personnel can modify configuration items.

  * Document approved changes and implement logging and monitoring.

  * Track security issues and resolutions using vulnerability scanning, Security Command Center, monitoring alerting policies, and reporting practices.




###  Enforce Deny All Egress Firewall Rule

The deny-all egress firewall rule helps to prevent unwanted outbound network connections.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `EGRESS_DENY_RULE_NOT_SET`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the firewall rule to deny egress traffic.

  1. Go to **Firewall** > **VPC Network** page in the Google Cloud console.

  2. Click **Create firewall rule**.

  3. For **Direction of traffic** , select **Egress**.

  4. In **Action on match** field, select **Deny**.

  5. In the **Targets** drop-down menu, select **All instances in the network**.

  6. In the **Destination filter** drop-down menu, select **IP ranges** , and type `0.0.0.0/0` into the **Destination IP ranges** box.

  7. In **Protocols and ports** field, select **Deny all**.

  8. Click **Disable Rule**.

  9. In **Enforcement** , select **Enabled** and click **Create**.




For more information, see [Add a firewall rule to deny egress traffic originating from all other VPC networks](https://cloud.google.com/firewall/docs/quickstarts/configure-hfwpolicy-allow-egress-vpc#create-fw-rule-deny-egress-all-vpc).

###  Enforce Domain Restricted Sharing

Configure the "Domain restricted sharing" (iam.allowedPolicyMemberDomains) organization policy constraint to allow principals only from specified customer or organization IDs to be added to IAM policies. This policy lets you limit resource sharing based on a domain or organization resource.

Enforcement mode | Audit   
---|---  
Finding category | `ORG_POLICY_ALLOWED_IAM_MEMBER_DOMAINS_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify that the **Domain restricted sharing** (`iam.allowedPolicyMemberDomains`) constraint is set to your customer ID. Only principals that belong to the allowed customer IDs can be added to IAM policies. For more information, see [Restricting identities by domain](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-domains#managed-constraint).

###  Enforce HTTPS Traffic Only

Configure your HTTP(S) load balancers to permit only HTTPS traffic to maintain data integrity and secure communications against tampering.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `HTTP_LOAD_BALANCER`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Restrict traffic to HTTPS only. Go to the **Network Services** > **Load balancing** page in the Google Cloud console. In the **Target proxies** tab, select the target proxy and configure it to use HTTPS traffic only. For more information, see [Target proxies](https://cloud.google.com/load-balancing/docs/https#target-proxies).

###  Enforce IAM Least Privilege

Maintain the principle of least privilege by assigning Org-Policy IAM to a restricted number of security professionals.

Enforcement mode | Audit   
---|---  
Finding category | `IAM_LEAST_PRIVILEGE_ORGPOLICY_VIOLATED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Assign Org-Policy IAM to a limited number of security professionals to maintain least privilege.

###  Enforce In-Transit Regions for Pub/Sub Messages

Uses the pubsub.enforceInTransitRegions organization policy constraint to ensure that your data flows only within permitted regions, as specified in the message storage policy for the topic.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `PUBSUB_ENFORCE_IN_TRANSIT_NOT_ENABLED`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  1.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/pubsub.enforceInTransitRegions`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `pubsub.enforceInTransitRegions` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Enforce Least Privilege

Ensure that access controls in Google Cloud abide by the principle of least privilege.

Enforcement mode | Audit   
---|---  
Finding category | `ACCESS_CONTROL_BY_LEAST_PRIVILEGE_POLICY_NEEDS_REVIEW`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Review best practices in [Least privilege](https://cloud.google.com/iam/docs/using-iam-securely#least_privilege).

  * Automate enforcement using Deployment Manager or Terraform.




###  Enforce Least Privilege Guide

Employ the principle of least privilege, allowing only authorized accesses for users (or processes acting on behalf of users) that are necessary to accomplish assigned organizational tasks.

Enforcement mode | Audit   
---|---  
Finding category | `LEAST_PRIVILEGE_GUIDE_NOT_IMPLEMENTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Define the minimum permissions required for tasks.

  * Identify the users and roles that require administrator permissions.

  * Create a [security group](https://cloud.google.com/identity/docs/how-to/update-group-to-security-group) for administrators.

  * Grant IAM roles to the security group.

  * [Limit Google Cloud console access to the security group only](https://support.google.com/a/answer/9050643).

  * Use IAM conditions to restrict access based on specific criteria.

  * [Enable audit logging](https://cloud.google.com/logging/docs/audit/configure-data-access).

  * Review access regularly using IAM recommender or Access Approval.

  * Configure [MFA](https://cloud.google.com/docs/authentication/mfa-requirement) for users in the security group.

  * Implement [IAM best practices](https://cloud.google.com/iam/docs/using-iam-securely).

  * [Analyze](https://cloud.google.com/policy-intelligence/docs/policy-analyzer-overview) and adjust IAM roles regularly.




###  Enforce Password for MySQL Database

Set a strong password for accounts connecting to MySQL database instances.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `SQL_NO_ROOT_PASSWORD`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console, select the instance, and set the password for the user.

###  Enforce Public Access Prevention

Use the "Enforce Public Access Prevention" (storage.publicAccessPrevention) organization policy constraint to help prevent Cloud Storage buckets and objects from being accidentally exposed to the public.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `ORGPOLICY_PUBLIC_ACCESS_PREVENTION_NOT_SET`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure public access prevention for Cloud Storage Buckets at the project and folder levels. For instructions, see [Use public access prevention](https://cloud.google.com/storage/docs/using-public-access-prevention#pap-org).

###  Enforce Separation of Duties

Separation of duties addresses the potential for abuse of authorized privileges and helps to reduce the risk of malevolent activity without collusion.

Enforcement mode | Audit   
---|---  
Finding category | `SEPARATION_OF_DUTIES_NOT_IMPLEMENTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * [Understand IAM roles](https://cloud.google.com/iam/docs/understanding-roles).

  * Review [IAM best practices](https://cloud.google.com/iam/docs/using-iam-securely).

  * Define your separation-of-duties policy.

  * [Create groups](https://cloud.google.com/iam/docs/groups-in-cloud-console), where [appropriate](https://cloud.google.com/iam/docs/groups-best-practices).

  * [Find](https://cloud.google.com/iam/docs/choose-predefined-roles) and [grant roles](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to your groups.

  * Regularly [analyze](https://cloud.google.com/policy-intelligence/docs/policy-analyzer-overview) and adjust assigned roles.

  * Use [custom roles](https://cloud.google.com/iam/docs/creating-custom-roles), where necessary.




###  Enforce Session Lock Policy

Enforce session lock policies after 15 minutes of user activity. Session locks temporarily prevent logical access to organizational systems when users are away but don't want to log out.

Enforcement mode | Audit   
---|---  
Finding category | `SESSION_LOCK_POLICY_NOT_ENFORCED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Define criteria for your session lock policy.

  * Configure session locks in your Workforce identity pool. `gcloud iam workforce-pools update WORKFORCE_POOL_ID --location=LOCATION --session-duration=900s`

  * Create scripts to monitor user activity and session lockouts.

  * Require reauthentication after a session locks. * Lock sessions on user request.

  * Notify users about the session lock policy.

  * Enable monitoring for session lock events and user-initiated requests. `gcloud logging read "resource.type=global AND logName=projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity" --project=PROJECT_ID --format=json`

  * Automate the session unlock process using authentication.

  * Include the session lock configuration in your deployment pipelines.

  * Document the process for reestablishing access.




###  Enforce SSL Encryption for Remote Access

Implement cryptographic mechanisms to help protect the confidentiality and integrity of remote access sessions.

Enforcement mode | Audit   
---|---  
Finding category | `REMOTE_ACCESS_PROTECTION_OF_CONFIDENTIALITY_AND_INTEGRITY_POLICY_VIOLATED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following.

  * Verify the [SSL certificates](https://cloud.google.com/load-balancing/docs/ssl-certificates) in use.

  * [Encrypt disks](https://cloud.google.com/compute/docs/disks/disk-encryption).

  * Use [SSH](https://cloud.google.com/compute/docs/instances/ssh) or HTTPS for remote access. For more information, see [Securely connecting to VM instances](https://cloud.google.com/solutions/connecting-securely).

  * Encrypt the connection between your on-premises network and Google Cloud. For example, enable [HA VPN over Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/how-to/choose-product#ha-vpn) for IPsec encryption.

  * Configure SSL to encrypt application traffic between clients and servers.

  * [Choose an encryption at rest option](https://cloud.google.com/kms/docs/key-management-service#choose).




###  Enforce SSL for all Incoming Database Connections

Use SSL for all incoming connections to your SQL database instance to secure data in transit. This control doesn't apply to on-premises databases or external instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `SSL_NOT_ENFORCED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and select the instance. On the **Connections** tab, click either **Allow only SSL connections** or **Require trusted client certificates**. If you chose **Require trusted client certificates** , create a new client certificate. For more information, see [Create a new client certificate](https://cloud.google.com/sql/docs/mysql/configure-ssl-instance#new-client).

###  Enforce Two-Step Verification

Two-step verification (2SV) helps to protect accounts from unauthorized access and against compromised login credentials.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MFA_NOT_ENFORCED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enforce 2-Step Verification (2SV) for all organizational units in the Google Admin console. For more information, see [Protect your business with 2-Step Verification](https://support.google.com/a/answer/175197).

###  Ensure Minimum TLS 1.2 Version

Enforce minimum TLS 1.2 in the SSL policies for Google Cloud and ensure organizational policies block older TLS versions.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `MINIMUM_TLS_1.2_NOT_ENFORCED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For more information, see **Restrict TLS Versions** in [Organization policy constraints](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).

###  Ensure Minimum TLS Version

Validate that your organization uses at least TLS v1.2.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `MINIMUM_TLS_1.2_NOT_VALIDATED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For more information, see [Restrict TLS versions](https://cloud.google.com/assured-workloads/docs/restrict-tls-versions).

###  Establish an SLA for Flaw Remediation

Measure the time between flaw identification and flaw remediation and set benchmarks for corrective actions.

Enforcement mode | Audit   
---|---  
Finding category | `IMPROPER_FLAW_REMEDIATION_SLA`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Define and implement an SLA for your flaw remediation cycle.

  * Establish benchmarks as appropriate.

  * Consider [Security Command Center](https://cloud.google.com/security-command-center/docs) to implement benchmarks.




###  Evaluate Data Bias in Training Data on Agent Platform

Evaluate data bias in training data on Gemini Enterprise Agent Platform.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `DATA_BIAS_IN_TRAINING_DATA`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use Agent Platform data bias metrics to evaluate training data. For more information, see [Data bias metrics for Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/evaluation/data-bias-metrics).

###  Evaluate Risk and Impact of Changes

Review the risk and impact of changes.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_REVIEW_OF_RISK_AND_IMPACT_OF_CHANGES`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Evaluate the risk and potential impact of any changes on your applications and services.

###  Evaluate Synthetic Data for Data Quality

Assess synthetic data to ensure its responsible use and data quality.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `SYNTHETIC_DATA_QUALITY_NOT_CHECKED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that re-identification risk, bias, and homogenization for synthetic data is measured. For more information, see [Model Armor filters](https://cloud.google.com/security-command-center/docs/model-armor-overview#ma-filters) and [Measuring re-identification and disclosure risk](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis).

###  Extract External IP Addresses for VM Instances

Identify external IP addresses that are assigned to Compute Engine VM instances.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_REVIEW_OF_COMPUTE_EXTERNAL_IPS`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Evaluate all Compute Engine VM instances to ensure that external IP addresses are assigned only when necessary. Unintended external IPs can create security risks, as they expose your instances directly to the internet. For more information, see [View the network configuration for an instance](https://cloud.google.com/compute/docs/instances/view-network-properties).

###  Extract GKE Public IP Addresses List

Identify public IP addresses assigned to Google Kubernetes Engine (GKE) instances for review.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_REVIEW_OF_GKE_PUBLIC_IPS`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Evaluate all Google Kubernetes Engine (GKE) instances to ensure that public IP addresses are assigned only when necessary. Unintended public IPs can create security risks, as they expose your instances directly to the internet.

###  Extract Public IP Addresses for Cloud SQL

Identify the public IP addresses that are assigned to Cloud SQL instances for review.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_REVIEW_OF_CLOUD_SQL_PUBLIC_IPs`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Evaluate all Cloud SQL instances to ensure that public IP addresses are assigned only when necessary. Unintended public IPs can create security risks, as they expose your instances directly to the internet.

###  FW Rule Disable Tags and Wide Internet Ingress

Check that an Ingress Firewall rule is not exposing any TCP/UDP ports to the wide Internet (0.0.0.0/0 or ::/0) and is not using network tags for identifying target instances

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `FW_RULE_ALLOWS_PUBLIC_ACCESS_OR_USES_TAGS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Modify the firewall rule to restrict ingress from wide IP ranges such as 0.0.0.0/0 or ::/0. If network tags are used, replace them with service accounts for identifying target instances as recommended for more secure firewall policies (https://cloud.google.com/vpc/docs/firewalls).

###  GCP Foundation GCS Has Retention Deletion Rules

Check that object lifecycle management is appropriately configured with retention & deletion rules on Google Cloud Storage in accordance with business requirements, applicable laws and regulations.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `GCS_RETENTION_POLICY_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure retention and deletion rules for the GCS bucket. This may include enabling Object Versioning (https://cloud.google.com/storage/docs/object-versioning), setting a Retention Policy (https://cloud.google.com/storage/docs/bucket-lock), enabling Soft Delete (https://cloud.google.com/storage/docs/soft-delete), or configuring Object Lifecycle Management (https://cloud.google.com/storage/docs/control-data-lifecycles).

###  GCP Foundation Landing Zone Constraints Regions To Europe

The landing zone constraints regions to Europe-west 3 (Frankfurt), Europe-west 4 (Netherlands), Europe-west 6 (Milan) and Europe-west 8 (Zurich) only that workloads can be deployed to.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `RESOURCE_LOCATION_NOT_CONSTRAINED_TO_EUROPE`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the `constraints/gcp.resourceLocations` organization policy to only allow resources in EU regions: europe-west3, europe-west4, europe-west6, and europe-west8. See https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints for details.

###  GCP Foundation No Preliminary Approved Services Enabled

Checking whether there are any services enabled, that have not been preliminary approved.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `DISALLOWED_SERVICE_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

A service is enabled that is not in the list of approved services. Disable the service if it is not required (https://cloud.google.com/service-usage/docs/enable-disable), or review and update the list of approved services if the service is approved for use.

###  GCP Foundation Resource With Label Has Label Assigned

Checking whether the resource, supporting a label, has the label assigned.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `RESOURCE_MISSING_LABELS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

The resource is missing required labels. Assign the necessary labels to the resource for proper classification and management. See https://cloud.google.com/resource-manager/docs/creating-managing-labels.

###  GCP Foundation Resources Not Running Outside Europe

Checking whether any of the resources are running outside of europe-west3, europe-west4, europe-west6, europe-west8 regions.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `RESOURCE_LOCATION_OUTSIDE_EUROPE`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

A resource is located outside of the allowed EU regions (europe-west3, europe-west4, europe-west6, europe-west8). To comply, migrate or redeploy the resource to an allowed region, or delete it if it is not needed. You can prevent resources from being created in disallowed locations by configuring the `constraints/gcp.resourceLocations` organization policy: https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints.

###  GCP Foundation Trusted Image Org Policy Enabled For All Projects

Trusted image org policy is enabled for all projects in GCP.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `TRUSTED_IMAGE_POLICY_NOT_ENFORCED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Manually review the extracted 'compute.trustedImageProjects' policy data. If trusted images are not properly restricted, update the organization policy to explicitly specify the projects authorized to host trusted images. See https://cloud.google.com/compute/docs/images/restricting-image-access.

###  Generate After Action Reports

Verify that after-action reports are generated.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_AFTER_ACTION_REPORTS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create after-action reports and integrate the lessons learned into the operations of your applications and services periodically.

###  Generate Auditable Events

Generate audit events for all components of the production environment and applications.

Enforcement mode | Audit   
---|---  
Finding category | `AUDIT_EVENTS_NOT_GENERATED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit).

  * Use IAM allow policies to control access to logs and log configurations. Grant different users read-only access and admin access to audit logs.

  * Create a [security alerting policy file](https://cloud.google.com/monitoring/alerts) in YAML or JSON format that defines which events are audited and the retention period. For example: ` logging: auditLog: LOGS_BUCKET_NAME retentionPeriod: 30d `

  * Apply the policy using Deployment Manager. For example: ``` gcloud deployment-manager deployments create POLICY_DEPLOYMENT_NAME --config=POLICY_FILE.yaml

  * Review log entries to ensure that expected auditable events are being logged.

  * [Automate log analysis](https://cloud.google.com/logging/docs/analyze/query-and-view) using Cloud Monitoring, or other analysis tools.

  * Regularly review the security alerting policy and IAM roles.




###  GKE Node Pool Autoscaling

Verify that GKE node pools have autoscaling enabled to handle variable workloads.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_GKE_AUTOSCALING`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Edit the GKE Node Pool and enable 'Autoscaling'. Set appropriate Minimum and Maximum node counts.

###  Guidance for Immutable Infrastructure on Google Cloud

Provide guidance for deploying immutable infrastructure on Google Cloud.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_IMMUTABLE_INFRASTRUCTURE`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement immutable infrastructure using an end-to-end CI/CD pipeline, leveraging services such as Artifact Registry, Cloud Build, and Kubernetes Engine. For detailed guidance, refer to the measurement guide.

###  Identify SDLC Functions and Services

Identify the functions, ports, protocols, and services intended for organizational use early in the system development life cycle (SDLC).

Enforcement mode | Audit   
---|---  
Finding category | `SDLC_FUNCTIONS_SERVICES_NOT_IDENTIFIED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Require developers to document the functions, ports, protocols, and services required for the SDLC lifecycle.

###  Identify Supply Chain Risks

Identify and prioritize potential risks to the supply chains that are used by your applications and services.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_SUPPLY_CHAIN_RISK_MANAGEMENT`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Assess supply chain risks that might impact confidentiality, integrity, or availability of a system and its information. Employ risk mitigation strategies and update the supply chain risk assessment whenever there are significant changes in the supply chain.

###  Identify Third-Party Information Resources

Identify all third-party information resources to understand, monitor, and manage supply chain risks.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_THIRD_PARTY_INFORMATION_RESOURCES`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify the third-party individuals or systems that transfer information to your applications and services.

###  Implement Alerting for Incidence Response

Define indicators of security compromise and alert the appropriate personnel or roles when they are detected.

Enforcement mode | Audit   
---|---  
Finding category | `INSUFFICIENT_ALERTING_FOR_INCIDENT_RESPONSE`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure alerts to the appropriate personnel so that they can respond to indicators of compromise.

###  Implement Audit Lifecycle Management

Implement audit record review, analysis, and reporting processes to establish an audit lifecycle management process for your systems.

Enforcement mode | Audit   
---|---  
Finding category | `AUDIT_LIFECYCLE_MANAGEMENT_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit), including for Cloud Storage.

  * [Create metrics](https://cloud.google.com/logging/docs/logs-based-metrics) to capture relevant events.

  * Configure [alerting policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui) for your metrics.

  * Create [notification channels](https://cloud.google.com/monitoring/support/notification-options) to receive alerts.

  * Regularly [analyze logs](https://cloud.google.com/logging/docs/view/logs-explorer-interface) for anomalies.

  * Consider [exporting logs through Pub/Sub](https://cloud.google.com/logging/docs/export/pubsub) for integration with other systems.

  * Integrate logs with a SIEM.

  * Create an incident response plan for anomalies.

  * Regularly review and update [alerting policies](https://cloud.google.com/monitoring/alerts).

  * Enable Security Command Center.




###  Implement Authorized Decision Makers for Access Requests

Permit authorized individuals to integrate applications on your system with external products and services.

Enforcement mode | Audit   
---|---  
Finding category | `AUTHORIZED_DECISION_MAKERS_NOT_IMPLEMENTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Identify the personnel in your organization who can make access authorization decisions. Set up mechanisms that can help them make these decisions.

###  Implement Best Practices for Cloud Deployments

Adhere to the recommended guidelines and best practices for cloud-native resources deployments.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_BEST_PRACTICE_IMPLEMENTATION`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement cloud information resources in accordance with Google's documented guidance and best practices that provides specific, informed guidance on helping secure Google Cloud deployments and describe recommended configurations, architectures, suggested settings, and other operational advice.

###  Implement Centralized Intrusion Detection

Connect and configure individual intrusion detection tools into an information system-wide intrusion detection system.

Enforcement mode | Audit   
---|---  
Finding category | `INTRUSION_DETECTION_NOT_CENTRALIZED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Connect and configure individual intrusion detection tools into an information system-wide intrusion detection system.

  * Explore implementing [Security Command Center](https://cloud.google.com/security-command-center/docs/security-command-center-overview).




###  Implement Centralized Security Monitoring

Monitor information systems to detect attacks and indicators of potential attacks, identify unauthorized use of information systems, and deploy monitoring devices.

Enforcement mode | Audit   
---|---  
Finding category | `SECURITY_MONITORING_NOT_CENTRALIZED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Identify what unauthorized use means. Consider legal and regulatory requirements.

  * Deploy monitoring devices across your system.

  * Use Cloud Logging and Cloud Monitoring to analyze logs and metrics, and implement alerts.

  * Enable VPC Flow Logs.

  * Consider Google Cloud Armor and Security Scanner to protect web applications.

  * Configure firewall rules with allowed and denied ports.

  * Implement a SIEM such as Security Command Center.

  * Use IAM allow policies to control access.

  * Implement Google Cloud security best practices, such as the CIS GCP Benchmark.

  * Enable audit logging.




###  Implement certificate lifecycle management

Use a certificate policy or an approved service provider to issue public key certificates. Perform end-to-end key management for encrypted network connections.

Enforcement mode | Audit   
---|---  
Finding category | `CERTIFICATE_LIFECYCLE_MANAGEMENT_NOT_IMPLEMENTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Issue public key certificates using certificate policies or obtain public key certificates from an approved vendor. Consider the [Certificate Authority Service](https://cloud.google.com/certificate-authority-service/docs/ca-service-overview) for hardware-protected private keys which are FIPS 140-2 Level 3 validated.

  * Use Cloud KMS to create and manage your keys.

  * Configure SSL certificates for your web servers that are running on VMs, GKE clusters, or Google App Engine.




###  Implement Continuous Network Traffic Monitoring

Monitor inbound and outbound communications traffic continuously for unusual or unauthorized activities or conditions.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `CONTINUOUS_NETWORK_TRAFFIC_MONITORING_NOT_IMPLEMENTED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Enable [VPC Flow Logs](https://cloud.google.com/vpc/docs/flow-logs).

  * Review [firewall rules](https://cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-insights-recommendation-hub) and allowed and denied ports.

  * Verify logging.




###  Implement Data Classification and Segmentation

Separate information flows logically or physically using organization-defined mechanisms and/or techniques to accomplish required separations by types of information. Enforcing the separation of information flows by type helps to enhance protection by ensuring that information is not commingled while in transit.

Enforcement mode | Audit   
---|---  
Finding category | `DATA_CLASSIFICATION_SEGMENTATION_NOT_IMPLEMENTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Define how you’ll classify your data based on severity and segmentation requirements.

  * Create VPC networks to isolate different components. For example, create VPC networks for specific data flows.

  * Use [subnets](https://cloud.google.com/vpc/docs/subnets) to logically segment data flows.

  * Create [firewall rules](https://cloud.google.com/firewall/docs/firewalls) that control traffic between different subnets.

  * Enable VPC Network Peering or Cloud VPN to communicate between different VPC networks.

  * Grant [IAM allow policies](https://cloud.google.com/iam/docs/allow-policies) to specific users to control access to data.

  * Configure Sensitive Data Protection.

  * Use Cloud KMS keys to protect sensitive data.




###  Implement Error Handling Mechanism

Configure applications to generate error messages that provide sufficient information for corrective actions.

Enforcement mode | Audit   
---|---  
Finding category | `ERROR_HANDLING_MECHANISM_NOT_IMPLEMENTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Build applications to generate appropriate error messages. Consider [Cloud Logging](https://cloud.google.com/logging/docs/overview) for your log management system.

  * Use [IAM allow policies](https://cloud.google.com/logging/docs/access-control) to control who can see error messages.




###  Implement Event Logging for Google Cloud Services

Implement event logging for all Google Cloud services to capture event logs, API calls, and actions that modify the environment.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `EVENT_LOGS_NOT_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Review Admin Activity audit logs.

  * Enable audit logging.

  * Configure [usage logs](https://cloud.google.com/storage/docs/access-logs) for Cloud Storage buckets.

  * Export logs for analysis to BigQuery.

  * Export Admin Activity audit logs to Cloud Storage.

  * [Create custom logs for your applications, if required](https://cloud.google.com/logging/docs/setup).

  * Use IAM allow policies to control access to logs and log configurations.

  * Regularly review logs using your log analysis tool (for example, Cloud Logging or BigQuery).

  * Implement [IAM best practices](https://cloud.google.com/iam/docs/using-iam-securely) to secure access to your resources and audit logs.

  * Review audit logs regularly.

  * Ensure application logs include timestamps and other information for traceability.

  * Use [logging filters](https://cloud.google.com/logging/docs/analyze/find-logs-error-groups) to identify successful and unsuccessful events.

  * Review logs for failed data access events.




###  Implement Host-based Intrusion and Detection Systems

Implement Cloud IDS, which lets you set up host intrusion prevention and intrusion detection systems. Or, minimally, a host-based firewall at defined systems and components.

Enforcement mode | Audit   
---|---  
Finding category | `HOST_BASED_INTRUSION_DETECTION_NOT_IMPLEMENTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Onboard your projects to Cloud IDS and secure the cloud resources. For more information, see [Configure Cloud IDS](https://cloud.google.com/intrusion-detection-system/docs/configuring-ids). Optionally, use third-party tools to implement host intrusion prevention systems (HIPS) and host intrusion detection systems (HIDS) on your workloads.

###  Implement Host-based Monitoring Mechanism

Implement host-based monitoring mechanisms in your environment.

Enforcement mode | Audit   
---|---  
Finding category | `HOST_BASED_MONITORING_NOT_IMPLEMENTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement host-based monitoring mechanisms:

  * Use Cloud [Monitoring](https://cloud.google.com/monitoring/docs) and [Cloud Logging](https://cloud.google.com/logging/docs) to collect, monitor, and analyze host-based data, such as system and application logs, performance metrics, and other relevant information.

  * Create [custom monitoring metrics](https://cloud.google.com/monitoring/custom-metrics/creating-metrics) in Cloud Monitoring to track specific host-based parameters that are critical.

  * Set up [alerting policies](https://cloud.google.com/monitoring/alerts) in Cloud Monitoring to receive notifications when host-based metrics or logs indicate unusual or unauthorized activities.




###  Implement On-Demand Audit Log Access

Implement an on-demand audit record review, analysis, and reporting requirement capability.

Enforcement mode | Audit   
---|---  
Finding category | `ON_DEMAND_AUDIT_LOG_ACCESS_NOT_IMPLEMENTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit).

  * [Export audit logs](https://cloud.google.com/logging/docs/export/configure_export_v2) to Cloud Storage, BigQuery, or Pub/Sub for further analysis.

  * [Review log entries](https://cloud.google.com/logging/docs/view/logs-explorer-interface).

  * Original content integrity is maintained by Cloud Audit Logs.

  * Use [IAM allow policies](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to control access to logs and log configurations.

  * Enable Security Command Center.




###  Implement Remote Access Policy

Establish and document usage restrictions, configuration requirements, and implementation guidance for permitted remote access.

Enforcement mode | Audit   
---|---  
Finding category | `REMOTE_ACCESS_POLICY_NOT_IMPLEMENTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Define and configure usage restrictions, connection requirements, and implementation guidance for each type of remote access allowed. For example, consider VPNs to ensure authorization of remote access to your systems. Remote access methods include, for example, dial-up, broadband, and wireless.

###  Implement Secure Development Lifecycle

Manage information systems with integrated security processes.

Enforcement mode | Audit   
---|---  
Finding category | `THREAT_DEFENSE`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Manage the information system using methods such as secure SDLC.

  * Define and document your information security roles and responsibilities throughout the system development life cycle.

  * Identify individuals that have information security roles and responsibilities.

  * Integrate your risk management process into system development life cycle activities.




###  Implement Secure Domain Name Resolution Service

Use DNS Security Extensions (DNSSEC) to add an extra layer of security to your DNS resolution. Enforce secure connections to prevent DNS-related attacks.

Enforcement mode | Audit   
---|---  
Finding category | `WEAK_DOMAIN_NAME_RESOLUTION_SERVICE`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Enable DNSSEC.

  * Use Cloud DNS.

  * Enforce HTTPS between web browsers and Google Cloud services.

  * Use SSL certificates from trusted CAs.

  * Consider web servers to use HTTPS.

  * Configure web applications to use secure URLs.

  * Configure end user devices to use trusted DNS servers.

  * Use the IP addresses for trusted DNS servers in the network settings for each device.

  * For corporate networks, configure a private DNS resolver.

  * Implement firewall rules and network security groups.

  * Consider VPC Service Controls.

  * Regularly perform audits and vulnerability assessments.

  * Use Cloud Logging and Cloud Monitoring to detect and respond to incidents.

  * Use Google's security best practices.

  * Train personnel on security protocols.

  * Regularly review your SSL certificates.

  * Implement fault tolerance by setting up multiple instances of your DNS.

  * Assign private IP addresses to your instances.

  * Use IAM allow policies to control access.




###  Implement Security Alert Advisory Management

Implement procedures for end-to-end management of security alerts, advisories, and directives.

Enforcement mode | Audit   
---|---  
Finding category | `SECURITY_ALERT_ADVISORY_MANAGEMENT_NOT_IMPLEMENTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement procedures to:

  1. Receive information system security alerts, advisories, and directives on an ongoing basis.
  2. Generate internal security alerts, advisories, and directives as deemed necessary.
  3. Disseminate security alerts, advisories, and directives to include system security personnel and administrators with configuration/patch-management responsibilities.
  4. Implement security directives in accordance with established time frames, or notify the issuing organization of the degree of noncompliance.



###  Implement Security Audits and Monitoring

Employ automated mechanisms to integrate audit review, analysis, and reporting processes to support organizational processes.

Enforcement mode | Audit   
---|---  
Finding category | `SECURITY_AUDIT_PROCESSES_NOT_INTEGRATED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Enable audit logging including for Cloud Storage.

  * Export logs to Cloud Storage, BigQuery, or Pub/Sub for further analysis.

  * Configure alerting policies for exported logs.

  * Create [notification channels](https://cloud.google.com/monitoring/support/notification-options) to receive alerts.

  * Consider exporting logs through Pub/Sub for integration with other systems.

  * [Automate log analysis](https://cloud.google.com/logging/docs/analyze/query-and-view) using Cloud Storage, BigQuery, or other analysis tools.

  * Enable Security Command Center.

  * Automate incident response using tools like Cloud Functions to trigger automated responses to detected issues. For example: ` gcloud functions deploy my-incident-response --runtime=nodejs20 --trigger-topic=audit-alerts --allow-unauthenticated `

  * Regularly review and update alerting policies.

  * Develop custom scripts for incident investigation and response.




###  Implement Security Event Correlation

Employ mechanisms to correlate information from monitoring tools deployed throughout your information system.

Enforcement mode | Audit   
---|---  
Finding category | `SECURITY_EVENTS_CORRELATION_MISSING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify that you can correlate various events across your systems. Consider tools such as Google SecOps or Security Command Center.

###  Implement Software Development Lifecycle Security Considerations

Develop and manage Software Development Lifecycle (SDLC) that incorporates information security and privacy considerations. Define, document, and assign information security and privacy roles and responsibilities throughout the SDLC and enforce separation of duties through access control mechanisms and identity management activities.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_SDLC_SECURITY`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Build security considerations into the Software Development Lifecycle (SDLC) and align with Cybersecurity and Infrastructure Security Agency's (CISA) Secure By Design principles.

###  Implement Zero-Trust Principles

Evaluate system architecture to identify the applicable zero-trust principles.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_ZERO_TRUST_PRINCIPLES`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Design and implement a zero-trust architecture for all applications and services that includes enforcing technical checks (robust authentication, granular authorization, certificate validation, and endpoint verification) to establish and maintain context awareness. For more information, see [BeyondCorp Enterprise](https://cloud.google.com/beyondcorp), [IAM](https://cloud.google.com/iam/docs/tags-access-control), [Cloud KMS](https://cloud.google.com/kms/docs/key-management-service), and [Certificate Manager](https://cloud.google.com/certificate-manager/docs/overview).

###  Import Google Workspace Audit Logs

Google Workspace lets you share its logs with the Google Cloud logging service. Google Workspace collects Login logs, Admin logs, and Group logs.

Enforcement mode | Audit   
---|---  
Finding category | `IMPORT_GOOGLE_WORKSPACE_LOGS_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To import Google Workspace audit logs, see [Share audit logs with Google Cloud](https://cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs#share_audit_logs).

###  Incorporate Integrity Monitoring into Incident Response

Incorporate unauthorized security-relevant changes to your systems into the organizational incident response capability.

Enforcement mode | Audit   
---|---  
Finding category | `INCIDENT_RESPONSE_WITHOUT_INTEGRITY_MONITORING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that you can detect unauthorized security-related changes and respond accordingly:

  * Create an [OS policy](https://cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies) and include integrity verification and response actions when unauthorized changes are detected.

  * Monitor for file integrity and unauthorized changes using various tools.

  * Regularly review and monitor the results and reports.




###  Inspect the External Load Balancer and SSL Connections

Ensure communications at the external boundary and at key internal boundaries use managed interfaces and are monitored and controlled.

Enforcement mode | Audit   
---|---  
Finding category | `EXTERNAL_LOADBALANCER_SSL_NOT_INSPECTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Verify the [load balancing scheme](https://cloud.google.com/load-balancing/docs/choosing-load-balancer#summary-gclb).

  * Review [firewall rules](https://cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-insights-recommendation-hub) and allowed and denied ports.

  * Verify [forwarding rules](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts) have appropriate targets.

  * Verify [routes](https://cloud.google.com/vpc/docs/routes) for all services.

  * Verify SSL certificates.




###  Label Dataset Sensitivity Based on Sensitive Data Protection Findings

Ensure Gemini Enterprise Agent Platform training data has the relevant labels for sensitive data to prevent the use of personally identifiable information (PII) or sensitive data in training.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `LABELS_NOT_ENABLED_FOR_VERTEX_AI_DATASETS`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use labels to track sensitive Agent Platform datasets. For more information, see [Adding labels to resources](https://docs.cloud.google.com/bigquery/docs/adding-labels) and [Tags and labels](https://docs.cloud.google.com/storage/docs/tags-and-labels).

###  Limit KMS Crypto Keys Users to Three

Limit the number of principal users that can use cryptographic keys to three or less.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `TOO_MANY_KMS_USERS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Security** > **Key Management** page in the Google Cloud console. Next, click the key ring that contains the key, and then click **Show Info Panel**. Reduce the number of principals having permissions to encrypt, decrypt, or sign data to three or less. To revoke permissions, click **Delete**. The following predefined roles grant permissions to encrypt, decrypt, or sign data using cryptographic keys: `roles/owner`, `roles/cloudkms.cryptoKeyEncrypterDecrypter`, `roles/cloudkms.cryptoKeyEncrypter`, `roles/cloudkms.cryptoKeyDecrypter`, `roles/cloudkms.signer`, and `roles/cloudkms.signerVerifier`. For more information, see [Permissions and roles](https://cloud.google.com/kms/docs/reference/permissions-and-roles).

###  Limit Super Admin Accounts

Google recommends limiting the number of super administrators to a minimum of two and a maximum of twenty users (depending on the size of your organization) and avoiding their use for daily tasks to enhance security. Super administrators have broad permissions, so limiting their number helps reduce the potential attack surface. You can configure alerts in Cloud Logging to track super administrator activity.

Enforcement mode | Audit   
---|---  
Finding category | `EXCESSIVE_SUPER_ADMIN_ACCOUNTS`  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To remediate this finding, reduce the number of super administrators to a minimum. Follow the principle of least privilege and use less permissive roles for daily administrative tasks. For more information, see the [best practices for administrator accounts](https://support.google.com/cloudidentity/answer/9011373?hl=en).

###  Location Policy EW3 EW6 EW8

Verify that resources are only allowed in europe-west3, europe-west4, europe-west6, and europe-west8 regions.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `RESOURCE_LOCATION_NOT_ALLOWED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the `constraints/gcp.resourceLocations` organization policy to only allow resources in EU regions: europe-west3, europe-west4, europe-west6, and europe-west8. See https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints for details.

###  Lock Storage Bucket Retention Policies

Use the Bucket Lock feature to permanently lock retention policies on buckets.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `STORAGE_BUCKET_LOCKED_RETENTION_POLICY_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To lock the retention policy on a bucket, see [Lock a bucket](https://cloud.google.com/storage/docs/using-bucket-lock#lock-bucket).

###  Maintain a Vulnerability Disclosure Program

Define and implement a process for tracking and reporting vulnerability identification and remediation activities. Establish communication channels for receiving reports of vulnerabilities in systems and information resources, including personnel.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_VULNERABILITY_DISCLOSURE_PROGRAM`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Create a vulnerability disclosure program that is well-documented, actionable, and integrated with your internal security and development teams.

###  Maintain Resource Inventory

Keep the resource inventory up-to-date.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `INVENTORY_NOT_MAINTAINED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Maintain an up-to-date inventory of all information resources, including deployed assets, software, and services, or the code that defines them. For more information, see [Cloud Asset Inventory overview](https://cloud.google.com/asset-inventory/docs/asset-inventory-overview), [Artifact Registry overview](https://cloud.google.com/artifact-registry/docs/overview), [Deployment Manager Fundamentals](https://cloud.google.com/deployment-manager/docs/fundamentals), and [Overview of Terraform on Google Cloud](https://cloud.google.com/docs/terraform/terraform-overview).

###  Maintain Resource Isolation

Implement resource isolation using a combination of VPC networks, firewall rules, a CI/CD pipeline, Google Kubernetes Engine (GKE), and IAM.

Enforcement mode | Audit   
---|---  
Finding category | `RESOURCE_ISOLATION_NOT_MAINTAINED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Use VPC networks to logically isolate resources.

  * Use firewall rules to control network traffic.

  * Implement a CI/CD pipeline using Cloud Build with version control systems like GitHub.

  * Use GKE for resource scheduling and management.

  * Use IAM allow policies to control access.

  * Isolate containers using Docker and container registries.




###  Manage Access to Audit Logs

Protect audit information and audit logging tools from unauthorized access, modification, and deletion.

Enforcement mode | Audit   
---|---  
Finding category | `AUDIT_LOG_ACCESS_NOT_MANAGED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit), including for Cloud Storage.

  * Use [IAM allow policies](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to control access to logs and log configurations.

  * Enable [uniform bucket-level access](https://cloud.google.com/storage/docs/uniform-bucket-level-access) on the bucket that stores audit logs.

  * Implement access controls in your application code to restrict access to audit functionality.




###  Manage Access to Google Cloud Resources from Mobile Devices

Manage access to Google Cloud resources from mobile devices.

Enforcement mode | Audit   
---|---  
Finding category | `ACCESS_FROM_MOBILE_DEVICES_NOT_MANAGED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Create custom roles for mobile device access.

  * Enable Cloud Identity Aware Proxy for mobile device access.

  * Implement endpoint verification for mobile devices and enforce context awareness. See [Chrome Enterprise Premium overview](https://cloud.google.com/beyondcorp-enterprise/docs/overview).

  * Implement a [device management solution](https://support.google.com/a/answer/7396025) that enforces security policies on mobile devices.

  * Create a [VPN tunnel](https://cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel) for your mobile devices.

  * Create [firewall rules](https://cloud.google.com/firewall/docs/firewalls) to permit mobile traffic. For example: `gcloud compute firewall-rules create allow-mobile --allow=tcp:80,tcp:443 --source-ranges=MOBILE_IP_RANGE`

  * Implement [OAuth](https://developers.google.com/identity/protocols/oauth2) and API access controls.

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit).




###  Manage Configurations Centrally

Implement and centrally manage configurations to align with security objectives for all information resources.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_CENTRAL_CONFIGS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Evaluate your system environments to identify the most effective way to centrally manage the configurations. Implement automated audits. Review and update the baseline configuration of the systems and retain previous configurations. Maintain system documentation. Implement required security alerts, advisories, and directives. Conduct regular inspection of systems or components.

###  Manage Data Handling and Retention

Manage data handling and data retention for information on Google Cloud as required by your business regulatory requirements.

Enforcement mode | Audit   
---|---  
Finding category | `DATA_HANDLING_RETENTION_MECHANISM_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Admin Activity and System Event audit logs are retained for 400 days, while Data Access audit logs are retained for 30 days by default. Move the audit logs to another storage location at the end of this period. Explore and use any product in [Storage](https://cloud.google.com/docs/storage) and [Database](https://cloud.google.com/docs/databases) that meet your data retention needs.

###  Manage Malicious Code Protection Mechanisms

Automate patching and updates for code protection. Regularly scan for and quarantine malicious code, and address false positives.

Enforcement mode | Audit   
---|---  
Finding category | `INSUFFICIENT_MALICIOUS_CODE_PROTECTION_MECHANISMS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement and manage a code protection system. You can use [Security Command Center](https://cloud.google.com/security-command-center/docs) and [Patch feature in VM Manager](https://cloud.google.com/compute/docs/os-patch-management) to implement certain malicious code protection mechanisms.

###  Manage Publicly Accessible Content

Review and manage the data that's posted on publicly accessible systems that are hosted on Google Cloud.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_STRATEGY_PUBLIC_CONTENT_ACCESS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Designate individuals who are authorized to post information onto a publicly accessible information system.

  * Train authorized individuals to ensure that publicly accessible information doesn’t contain nonpublic information.

  * Review the proposed content before posting it to the publicly accessible information system to ensure that nonpublic information is not included.

  * Regularly review the content on the publicly accessible information system for nonpublic information and remove such information, if discovered.




###  Manage System Integrity Policies and Procedures

Manage the development, documentation, and dissemination of system and information integrity policies and procedures.

Enforcement mode | Audit   
---|---  
Finding category | `IMPROPER_SYSTEM_INTEGRITY_POLICY_MANAGEMENT`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Document and maintain relevant security policies for your organization.

  * Designate an organization-defined official to manage the development, documentation, and dissemination of the system and information integrity policy and procedures.




###  Monitor the Threat Environment and Review Audit Logs

Security teams must monitor the threat environment and review audit logs for the production environment.

Enforcement mode | Audit   
---|---  
Finding category | `REGULAR_THREAT_MONITORING_NOT_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that your security team reviews and updates audited events annually or whenever there is a change in the threat environment for your system or applications.

###  Monitor Third-Party Information Resources for Upstream Vulnerabilities

Monitor third-party software components, libraries, or information resources that your services use.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_THIRD_PARTY_MONITORING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Establish a process to continuously monitor third-party software information resources for upstream vulnerabilities. This can include contractual notification requirements or active monitoring services.

###  Perform Authenticated Vulnerability Scans

Use authenticated vulnerability scans.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_AUTHENTICATED_SCANS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that authenticated vulnerability scanning is performed on information resources. For more information, see [Setting up custom scans using Web Security Scanner](https://cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans).

###  Perform Integrity Checks Every Month

Perform integrity checks of software, firmware, and information at startup, at specific security-relevant events, and at minimum once a month.

Enforcement mode | Audit   
---|---  
Finding category | `IRREGULAR_INTEGRITY_CHECKS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure your OS policy to perform integrity verification of your system every month. For more information, see [OS policy and OS policy assignment](https://cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies), [Create an OS policy assignment](https://cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment), and [Manage OS policy assignments](https://cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy).

###  Perform System Backups

Maintain continuous backup of your systems.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_SYSTEM_BACKUPS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that the system backups are aligned with recovery objectives and performed at regular intervals. For more information on Google backup services, see [Cloud SQL](https://cloud.google.com/sql/docs/postgres/backup-recovery/backing-up), [Spanner](https://cloud.google.com/spanner/docs/backup), [Bigtable](https://cloud.google.com/bigtable/docs/managing-backups), [Cloud Storage](https://cloud.google.com/storage/docs/availability-durability), [Filestore](https://cloud.google.com/filestore/docs/snapshots), and [BigQuery](https://cloud.google.com/bigquery/docs/table-snapshots-intro).

###  Perform Threat Modeling and Vulnerability Analyses

Perform threat modeling and vulnerability analyses during development and testing phases of a system or its components.

Enforcement mode | Audit   
---|---  
Finding category | `THREAT_MODELING_VULNERABILITY_ANALYSIS_NOT_PERFORMED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Create the requirements for threat and vulnerability analysis and testing.

  * [Grant appropriate IAM roles](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to developers.

  * Define and communicate your security standards.

  * Encourage developers to use Google Cloud threat and analysis tools (such as Security Command Center, Google Threat Intelligence, Google SecOps, and Cloud NGFW).

  * For vulnerability testing, use [Web Security Scanner](https://cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview).

  * For penetration testing, collaborate with qualified testing teams or use third-party tools.




###  Plan Security Assessments and Remediation

Develop and implement ongoing security and privacy control assessments. Set up a remediation process to resolve any findings.

Enforcement mode | Audit   
---|---  
Finding category | `SECURITY_ASSESSMENTS_REMEDIATIONS_MISSING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Create a security assessment plan.

  * Perform unit, integration, system, and regression testing.

  * Document the security assessment plan execution and the results of the security testing.

  * Establish a verifiable flaw remediation process.

  * Address any security flaws identified during testing or evaluation.




###  Prevent Automatic Creation of Default Network

Uses the 'compute.skipDefaultNetworkCreation' organization policy constraint to skip the creation of the default network and related resources (like default firewall rules) when a Google Cloud project is created. This constraint helps ensures a more secure default network posture by requiring explicit network configuration.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DEFAULT_NETWORK_EXISTS`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  2.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/compute.skipDefaultNetworkCreation`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `compute.skipDefaultNetworkCreation` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Prevent Automatic Granting of Editor Role to Default Service Accounts

Uses the 'iam.automaticIamGrantsForDefaultServiceAccounts' organization policy constraint to block the automatic granting of the IAM Editor role to default service accounts when services are enabled or used for the first time in a project. This constraint enforces the principle of least privilege, requiring explicit and more granular role assignments.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `IAM_DEFAULT_SERVICE_ACCOUNT_AUTO_EDITOR_GRANT_ALLOWED`  
Category name in the API | CC_CATEGORY_IDENTITY_AND_ACCESS_MANAGEMENT  
Revision number |  2.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/iam.automaticIamGrantsForDefaultServiceAccounts`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `iam.automaticIamGrantsForDefaultServiceAccounts` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Prevent IP Forwarding on Compute Engine Instances

Don't permit IP forwarding of data packets for your VMs to prevent potential data loss or unauthorized disclosure. Preventing IP forwarding restricts the routing of data packets.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `IP_FORWARDING_ENABLED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't turn off IP forwarding for an existing VM instance. Delete the VM and create a new VM with IP forwarding turned off. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console. Click the instance name. Select the instance name and delete it. Create a new instance. To ensure IP forwarding is turned off, go to **Management, disks, networking, SSH keys** and click **Networking**. In the **Network interfaces** section, click **Edit** and ensure **IP forwarding** is turned off.

###  Prevent Nested Virtualization for Compute Engine VMs

Use the "Disable VM nested virtualization" (compute.disableNestedVirtualization) organization policy constraint to turn off hardware-accelerated nested virtualization for all Compute Engine VMs. Turning off nested virtualization can reduce the attack surface and improve the overall security posture of the Google Cloud environment.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `COMPUTE_NESTED_VIRTUALIZATION_CONSTRAINT_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Disable VM nested virtualization** (`constraints/compute.disableNestedVirtualization`) organization policy constraint to `true`. For more information, see [Manage the nested virtualization constraint](https://cloud.google.com/compute/docs/instances/nested-virtualization/managing-constraint).

###  Protect System Memory

Implement appropriate failsafe measures to protect system memory from unauthorized code execution.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_CONTROL_TO_PROTECT_SYSTEM_MEMORY`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

This control does not apply to Google Cloud. Verify that you have appropriate fail-safe procedures to protect memory from unauthorized code execution for your systems.

###  Provide Dedicated Resources for Security

Determine, document, and allocate the resources required for security and privacy. Resource allocation must include funding for staff, system and services acquisition, sustainment, and supply chain-related risks.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_DEDICATED_SECURITY_RESOURCES`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Maintain a dedicated staff and budget for security, with executive support, that is aligned with the size, complexity, scope, and risk of the service offering.

###  Remove Inactive Accounts

Verify that all inactive accounts are removed from Google Cloud.

Enforcement mode | Audit   
---|---  
Finding category | `INACTIVE_ACCOUNTS_ENABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Find unused service accounts and remove them. See [Identify and disable unused service accounts](https://cloud.google.com/iam/docs/best-practices-service-accounts#identify-unused-accounts). Consider [Find unused service accounts](https://cloud.google.com/policy-intelligence/docs/service-account-insights).

###  Remove Temporary Accounts

Verify that access for any account that's meant to be temporary is removed within 24 hours.

Enforcement mode | Audit   
---|---  
Finding category | `TEMPORARY_ACCOUNTS_ENABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Review the service accounts and remove the roles that are meant to be temporary. For instructions, see [List and edit service accounts](https://cloud.google.com/iam/docs/service-accounts-list-edit) and [Revoke a single IAM role](https://cloud.google.com/iam/docs/granting-changing-revoking-access#revoke-single-role). [Configure temporary access](https://cloud.google.com/iam/docs/configuring-temporary-access) for your accounts, where possible. [Monitor service account usage](https://cloud.google.com/policy-intelligence/docs/service-account-usage-tools).

###  Report Security Incidents to US-CERT

Adhere to the incident reporting guidelines defined by FedRAMP.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_INCIDENT_REPORTS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Report security incident information to CISA when suspected incidents are detected within Google Cloud. Ensure that your contact information in the Google Cloud console is accurate and up-to-date to receive email notifications from Google regarding any customer-impacting data incidents.

###  Require Additional Logging for Sensitive Buckets

Logging access to a sensitive data bucket helps provide audit traceability from who gained access and when, which might be used when appropriate due to the high volume of logs the buckets generate.

Enforcement mode | Audit   
---|---  
Finding category | `AUDIT_LOGS_FOR_SENSITIVE_BUCKETS_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable additional logging around particular storage objects based on their use case. For more information, see [Cloud Audit Logs with Cloud Storage](https://cloud.google.com/storage/docs/audit-logging).

###  Require Audit Logging for Privileged Activities

Require audit logs for privileged activities such as data access and IAM conditions.

Enforcement mode | Audit   
---|---  
Finding category | `AUDIT_LOGS_FOR_PRIVILEGED_ACTIVITIES_NOT_IMPLEMENTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * [Enable IAM audit logging](https://cloud.google.com/iam/docs/audit-logging) for data access and IAM conditions (implemented using policy bindings).

  * [Configure alerts](https://cloud.google.com/monitoring/alerts).




###  Require Auto Upgrade Schedule Set for Agent Platform Workbench

Use the "Require automatic scheduled upgrades on new Gemini Enterprise Agent Platform Workbench user-managed notebooks and instances" (ainotebooks.requireAutoUpgradeSchedule) organization policy constraint to benefit from framework updates, package updates, and bug fixes.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `ORG_POLICY_AUTO_UPGRADE_SCHEDULE_NOT_SET`  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Require automatic scheduled upgrades on new Vertex AI Workbench user-managed notebooks and instances** (`ainotebooks.requireAutoUpgradeSchedule`) value to `true` to require automatic scheduled upgrades on new Agent Platform Workbench user-managed notebooks and instances. For more information, see [Updating policies with boolean rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints).

###  Require Automated Testing and Validation of Changes

Implement automated testing and validation of changes before deploying applications and services.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_AUTOMATED_TESTING_OF_CHANGES`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement automated testing and validation procedure for application and service changes before deployment. Consider using the following services: [Cloud Build](https://cloud.google.com/build/docs), [Artifact Registry](https://cloud.google.com/artifact-registry/docs), [Cloud Deploy](https://cloud.google.com/deploy/docs), and [Binary Authorization](https://cloud.google.com/binary-authorization/docs).

###  Require Binary Authorization on a Cluster

Binary Authorization helps to enhance supply chain security by ensuring only signed container images are deployed.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `BINARY_AUTHORIZATION_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable Binary Authorization on the cluster. Go to the **Kubernetes Engine** > **Clusters** page in the Google Cloud console. In the **Security** section, edit the **Binary authorization** row and enable it.

###  Require Cloud Storage Bucket Logging

Enable access logs and storage information for your Cloud Storage buckets to help investigate security issues and monitor storage consumption. This control checks whether the logBucket field in the bucket's logging property is empty.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `BUCKET_LOGGING_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For instructions to set up logging for a bucket, see [Usage logs & storage logs](https://cloud.google.com/storage/docs/access-logs).

###  Require CMEK on Dataproc Clusters

A Dataproc cluster with customer-managed encryption keys (CMEK) gives you more control over data encryption and key management.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DATAPROC_CMEK_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

You can't enable CMEK on a Dataproc cluster after it's been created. Create a new cluster with CMEK enabled, migrate your workloads, and delete the older cluster. To create a new cluster:

  1. Go to the **Dataproc** > **Clusters** page in the Google Cloud console.

  2. Click **Create Cluster** to recreate the Dataproc cluster.

  3. In the **Manage security** section, click **Encryption** and select **Customer-managed key** to enable CMEK.

  4. After the cluster is created, migrate your workloads from the older cluster to the new cluster, and delete the older cluster.




###  Require CMEK Protection

Restricts the creation of resources without CMEK protection for specified services.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `REQUIRED_CMEK_PROTECTION_NOT_ENABLED`  
Category name in the API | CC_CATEGORY_ENCRYPTION  
Revision number |  5.1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/gcp.restrictNonCmekServices`  
---|---  
  
#### Parameters

`services` |  `STRINGLIST` Required. List of service names that must use CMEK. E.g. 'bigquerydatatransfer.googleapis.com'  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `gcp.restrictNonCmekServices` constraint to the required values:

    * Denied services: $services

See [Updating policies with list rules](https://docs.cloud.google.com/organization-policy/apply-policies#list_constraints) and [Require CMEK protection](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek).

  * **Remediation for resource violation:** Delete the resource and recreate it using a customer-managed encryption key (CMEK). For information, see [CMEK integrations](https://docs.cloud.google.com/kms/docs/compatible-services#cmek_integrations).




###  Require Container-Optimized OS for a GKE Cluster

Google recommends Container-Optimized OS for containers due to its enhanced security, minimal OS footprint, and automatic updates for quick vulnerability patching.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `COS_NOT_USED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable Container-Optimized OS for the cluster. Go to the **Kubernetes clusters** page in the Google Cloud console. Click the cluster's name. Click the **Nodes** tab. For each node pool, click the name to open its details page. Click **Edit**. Under **Nodes > Image type**, click **Change**. Select **Container-Optimized OS** and click **Change**.

###  Require Documentation for Models

Document the model and explain it to ensure responsible use and proper governance.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `DOCUMENTATION_FOR_MODELS_NOT_DEFINED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Document the AI model details. Ensure the documentation includes the following: proposed use and organizational value, assumptions, and limitations; data collection methodologies; data provenance; data quality; model architecture (for example, convolutional neural network and transformers); optimization objectives; training algorithms; reinforcement learning from human feedback (RLHF) approaches; fine-tuning or retrieval-augmented generation approaches; evaluation data; ethical considerations; and legal and regulatory requirements.

###  Require Documentation for Training Data

Establish and document policies to curate training data and trace the origin and provenance of AI-generated content.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `DOCUMENTATION_FOR_TRAINING_DATA_NOT_DEFINED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Document training curation policies, sources, and types of training data and their origins, and potential biases present in the data that's related to the AI application. Document its content provenance, architecture, training process of the pre-trained model including information on hyperparameters, training duration, and any fine-tuning processes that were applied.

###  Require GKE Sandbox for GKE clusters

Configure GKE Sandbox to help protect the host kernel on your nodes.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `GKE_SANDBOX_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Update your GKE cluster to use GKE Sandbox. For more information, see [Enable GKE Sandbox on an existing Standard cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods#enabling-existing).

###  Require IAM Logs

Require audit logs for all projects and folders.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `IAM_AUDIT_LOGS_NOT_COLLECTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable IAM audit logs, see [Identity and Access Management audit logging](https://cloud.google.com/iam/docs/audit-logging).

###  Require Incident Logs

Maintain logs for your incidents.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_INCIDENT_LOGS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Maintain a detailed log of all incidents and regularly review these logs to identify patterns and potential vulnerabilities.

###  Require Least Privilege

Use Cloud IAM to implement least privilege.

Enforcement mode | Audit   
---|---  
Finding category | `LEAST_PRIVILEGE_NOT_IMPLEMENTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

See [Cloud IAM](https://cloud.google.com/iam/docs/overview) to help achieve least privilege. For viewing permissions and predefined roles, see [Permissions](https://cloud.google.com/iam/docs/reference/rest/v1/permissions/queryTestablePermissions) and [Pre-defined roles](https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles/list).

###  Require Object Versioning for Cloud Storage Buckets

Log buckets that use Object Versioning support the retrieval of deleted or overwritten objects that helps to protect data from accidental deletion.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `OBJECT_VERSIONING_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Update the bucket to use Object Versioning. In the Google Cloud console, go to the **Buckets** page. Select the bucket. In the **Protection** tab, configure object versioning. See [Set Object Versioning on a bucket](https://cloud.google.com/storage/docs/using-object-versioning#set).

###  Require OS Login on Compute Engine Instances

OS Login centralizes SSH key management with IAM and disables metadata-based SSH key configuration on all project instances. This control doesn't apply to GKE instances, Dataflow jobs, and Serverless VPC Access.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `INSTANCE_OS_LOGIN_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn on OS Login for the VM instance.

  1. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console. Click the instance name.

  2. On the **Instance details** page, click **Stop**.

  3. Edit the instance and set **enable-oslogin** to **True** in the **Custom metadata** section.




For more information, see [Set up OS Login](https://cloud.google.com/compute/docs/oslogin/set-up-oslogin).

###  Require Private Nodes in GKE Clusters

Ensure that GKE clusters use private nodes to prevent external clients from accessing the nodes.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `GKE_PRIVATE_NODES_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Update your cluster to use private nodes. For more information, see [Enable private nodes](https://cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#enable-private-nodes).

###  Require Procedures to Handle Training Data

Develop procedures for handling training data to help protect the data from potential risks.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `PROCEDURES_FOR_TRAINING_DATA_NOT_DEFINED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Develop and implement policies for the collection and retention of training data. Maintain a minimum quality of data with privacy and AI-specific risks in mind and conduct appropriate diligence on training data.

###  Require Rotation of API Key

Rotating API keys at least every 90 days reduces risk from stolen API keys that can be used to access data on a compromised or terminated account.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `API_KEY_NOT_ROTATED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following steps to rotate API keys:

  1. Go to the **APIs & Services** > **Credentials** page in the Google Cloud console.

  2. Under **API Keys** , edit each key using the **Actions** menu.

  3. On the **Edit API key** page, click **Rotate key** if the creation date is older than 90 days.




###  Require Security Hardening

Adhere to the security best practices to harden configurations.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_RECOMMENDED_HARDENING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use the following services to ensure that the cloud information resources are implemented based on the best practices and documented guidance: [Security Command Center](https://cloud.google.com/security-command-center/docs/security-command-center-overview), CIS Benchmarks, and [Cloud Security Best Practices Center](https://cloud.google.com/security/best-practices).

###  Require Service Account Key Rotation

Rotate your service account keys every 90 days or less to help protect data if a key gets compromised.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SERVICE_ACCOUNT_KEY_NOT_ROTATED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Rotate your service account key. For instructions, see [Service account key rotation](https://cloud.google.com/iam/docs/key-rotation). When possible, avoid using service account keys. For other options, see [Choose the right authentication method for your use case](https://cloud.google.com/docs/authentication#auth-decision-tree).

###  Require Unique Super Admin Account

Use a unique email address for super administrator accounts to manage and track administrator actions.

Enforcement mode | Audit   
---|---  
Finding category | `DEDICATED_SUPERADMIN_ACCOUNT_NOT_CONFIGURED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify that the super admin accounts use unique email addresses that aren't specific to a user. For more information, see [Super administrator account best practices](https://cloud.google.com/resource-manager/docs/super-admin-best-practices).

###  Require Workload Identity Federation for GKE and the GKE Metadata Server

Enable Workload Identity Federation for GKE with the GKE metadata server. Workload Identity Federation for GKE uses IAM policies to grant Kubernetes workloads in your GKE cluster access to specific Google Cloud APIs without needing manual configuration or less secure methods.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `GKE_METADATA_SERVER_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Move your applications to use Workload Identity Federation for GKE. For more information, see [Migrate existing workloads to Workload Identity Federation for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#migrate_applications_to).

###  Restrict Access Control Points for Authorized and Managed Remote Access

Route remote access through authorized and managed network access control points to help reduce the attack surface for organizations.

Enforcement mode | Audit   
---|---  
Finding category | `ACCESS_CONTROL_POINTS_TO_ROUTE_REMOTE_ACCESS_UNRESTRICTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Consider Dedicated Interconnect to isolate your organization's data and traffic from the internet.

  * Configure Cloud VPN to further protect information in transit.

  * Implement Cloud Load Balancing for additional encryption protection to applications.

  * Enable Cloud Identity Aware Proxy to manage and restrict remote access to applications.

  * Implement endpoint verification for devices that connect to Google Cloud services and enforce context awareness. See [Chrome Enterprise Premium overview](https://cloud.google.com/beyondcorp-enterprise/docs/overview).

  * Implement a [device management solution](https://support.google.com/a/answer/7396025) that enforces security policies on devices that access Google Cloud resources.

  * Enforce security keys for user authentication and use hardware security keys (such as Titan Security Keys) for multi-factor authentication.




###  Restrict Access to Audit Logs

Restrict access to audit management information to privileged users.

Enforcement mode | Audit   
---|---  
Finding category | `UNRESTRICTED_ACCESS_TO_AUDIT_LOGS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Use [IAM allow policies](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to control access to logs and log configurations. Grant different users read-only access and admin access to audit logs.

  * Create [custom roles](https://cloud.google.com/iam/docs/creating-custom-roles), if required.

  * Enable [uniform bucket-level access](https://cloud.google.com/storage/docs/uniform-bucket-level-access) on the bucket that stores audit logs.

  * Implement a request and approval process for accessing audit logs.

  * Create a machine ACL system group and grant it viewer access to the project where your audit logs are stored.

  * Configure appropriate access for your auditing tools.

  * [Monitor access](https://cloud.google.com/logging/docs/alerting/monitoring-logs) to your audit logs.

  * Implement [IAM best practices](https://cloud.google.com/iam/docs/using-iam-securely) to secure access to your audit logs.




###  Restrict Access to VM Core Memory

Uses the compute.enableComplianceMemoryProtection organization policy constraint to enable controls settings required to eliminate potential access paths to VM core memory. It limits the ability to access VM core memory by disabling access pathways and restricts internal data collection when an error occurs.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `VM_CORE_MEMORY_PROTECTION_NOT_ENABLED`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  1.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/compute.enableComplianceMemoryProtection`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `compute.enableComplianceMemoryProtection` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Restrict API Access to Google Cloud APIs for Compute Engine Instances

Compute Engine instances that use the default service account and have full access to all Google Cloud APIs are overly permissive. This control retrieves the scopes field in the serviceAccounts property to check whether a default service account is used and if it is assigned the cloud-platform scope.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `FULL_API_ACCESS`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Reset the access permissions to APIs for the VM instance. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console. Click the instance name. Click **Edit**. Navigate to **Security and access** > **Service accounts** , select **Compute Engine default service account**. In the **Access scopes** section, select **Set access for each API** , set **Cloud Platform** to **None**. Enable the specific APIs that the default VM service account requires access to.

###  Restrict API Keys for Required APIs Only

Restricting API keys limits their access to only the APIs that are required by the application.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `API_KEY_APIS_UNRESTRICTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **APIs & Services** > **Credentials** page in the Google Cloud console. Under **API Keys** , edit each key using the **Actions** menu and then restrict the APIs in the **API restrictions section**.

###  Restrict Cloud Shell Access Settings

Administrators can use Cloud Shell to access and manage Google Cloud resources, including sensitive data and projects. Disabling Cloud Shell for Cloud Identity managed user accounts helps reduce the potential attack surface for unauthorized access.

Enforcement mode | Audit   
---|---  
Finding category | `CLOUDSHELL_MANAGED_USERS_ACCESS_ENABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

In the Google Admin console, navigate to **Apps > Additional Google services > Google Cloud Platform > Cloud Shell Settings** and disable **Cloud Shell Access Settings**. To disable Cloud Shell for specific users, you'll need to use access groups: add individual users to the group and turn off the group's Cloud Shell access setting. For more information, see [Turn Google Cloud on or off for users](https://support.google.com/a/answer/9197205).

###  Restrict Cloud SQL Resource Creation

Uses the 'sql.restrictNoncompliantResourceCreation' organization policy constraint to block the creation of Cloud SQL resources that don't meet the advanced sovereignty and compliance requirements of the IL5 regime. This constraint might include restrictions on public IP addresses and network configurations, and often requires the use of customer-managed encryption keys (CMEK).

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `SQL_NONCOMPLIANT_RESOURCE_CREATION_ALLOWED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  2.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/sql.restrictNoncompliantResourceCreation`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `sql.restrictNoncompliantResourceCreation` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Restrict CMEK Crypto Key Projects

Define the projects that Cloud KMS can store customer managed encryption keys (CMEKs) using the "Restrict which projects may supply KMS CryptoKeys for CMEK" (gcp.restrictCmekCryptoKeyProjects) organization policy constraint.

Enforcement mode | Audit   
---|---  
Finding category | `ORG_POLICY_CMEK_RESTRICTED_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Define the projects that can store CMEKs using the **Restrict which projects may supply KMS CryptoKeys for CMEK** (`constraints/gcp.restrictCmekCryptoKeyProjects`) constraint. For more information, see [Limit the use of Cloud KMS keys for CMEK](https://cloud.google.com/kms/docs/cmek-org-policy#project-constraint).

###  Restrict Default Network Creation for Compute Engine Instances

Use the "Skip default network creation" (compute.skipDefaultNetworkCreation) organization policy constraint to skip the creation of the default network and related resources when creating projects.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SKIP_DEFAULT_NETWORK_CREATION_ORG_POLICY`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Skip default network creation** (`constraints/compute.skipDefaultNetworkCreation`) constraint to `true`. For more information, see [Organization policy constraints](https://cloud.google.com/vpc/docs/vpc#org-policies).

###  Restrict External IP Addresses to Specific VM Instances

Use the "Define allowed external IPs for VM instances" (compute.vmExternalIpAccess) organization policy constraint to block public access to your VMs.

Enforcement mode | Audit   
---|---  
Finding category | `ORG_POLICY_EXTERNAL_IP_FOR_VM_INSTANCES_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To block external IP addresses on Compute Engine VM instances, see [Restrict external IP addresses to specific instances](https://cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip).

###  restrict firestore access to firestore agent

restrict firestore permissions to firestore agent only

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `EXCESSIVE_PERMISSIONS`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Roles containing 'firestore' or 'datastore' in their names indicate permissions to Cloud Firestore or Datastore. To follow the principle of least privilege, these roles should only be granted to the Firestore service agent ('*@gcp-sa-firestore.iam.gserviceaccount.com'). Remove any grants of these roles to other principals in IAM policy.

###  Restrict Insecure SSL Policies for Compute Engine Instances

Avoid weak or insecure SSL policies for Compute Engine instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `WEAK_SSL_POLICY`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure TLS 1.2 and strong cipher suites on your load balancers. If a weak cipher suite or down-level TLS version is used, edit the SSL policy and change **Minimum TLS version** to **TLS 1.2** and **Profile** to **Modern** or **Restricted**. If a default Google Cloud SSL policy is used, create a new SSL policy and apply it to the appropriate forwarding rules. In both the cases, ensure the following cipher suites are disabled if you want to use a custom profile: `TLS_RSA_WITH_AES_128_GCM_SHA256`, `TLS_RSA_WITH_AES_256_GCM_SHA384`, `TLS_RSA_WITH_AES_128_CBC_SHA`, `TLS_RSA_WITH_AES_256_CBC_SHA`, and `TLS_RSA_WITH_3DES_EDE_CBC_SHA`. For more information, see [Use SSL policies for SSL and TLS protocols](https://cloud.google.com/load-balancing/docs/use-ssl-policies).

###  Restrict Legacy IAM Roles

To implement the principle of least privilege, avoid the overly permissive legacy roles like Owner, Editor, and Viewer. This control checks the IAM allow policy in the resource metadata for any user-created service accounts (indicated by the prefix iam.gserviceaccount.com), that are assigned roles/Owner, roles/Editor, or roles/Viewer. This control doesn't apply to Container Registry service accounts (containerregistry.iam.gserviceaccount.com), Google APIs service agent (cloudservices.gserviceaccount.com), and Security Command Center service accounts (security-center-api.iam.gserviceaccount.com).

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `PRIMITIVE_ROLES_USED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **IAM** page in the Google Cloud console and replace primitive roles with more granular roles.

###  Restrict Legacy TLS Versions

Use the "Restrict TLS Versions" (gcp.restrictTLSVersion) organization policy constraint to deny access from older TLS versions such as TLS 1.0 or TLS 1.1.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_RESTRICT_TLS_VERSION_NOT_SET`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Update the organization policy to restrict TLS versions for resources within the folder or project. For instructions, see [Restrict a TLS version](https://cloud.google.com/assured-workloads/docs/restrict-tls-versions#restrict).

###  Restrict Non CMEK Services

Use the "Restrict which services may create resources without CMEK" (gcp.restrictNonCmekServices) organization policy constraint to block services that don't use CMEK encryption.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_NON_CMEK_SERVICES_ALLOWED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure the **Restrict which services may create resources without CMEK** (`constraints/gcp.restrictNonCmekServices`) constraint. For instructions, see [Require CMEK protection](https://docs.cloud.google.com/kms/docs/cmek-org-policy#require-cmek).

###  Restrict Non-Privileged Users from Executing Privileged Functions

Enable audit logs for the IAM API, Security Token Service API, and Service Account Credentials API. Include the ADMIN_READ, DATA_READ, and DATA_WRITE types.

Enforcement mode | Audit   
---|---  
Finding category | `IAM_AUDIT_LOGS_NOT_IMPLEMENTED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Enable `DATA_READ`, `DATA_WRITE`, and `ADMIN_READ` for the following APIs: `iam.googleapis.com`, `iamcredentials.googleapis.com`, and `sts.googleapis.com`. For more information, see the following: * [Service Account Credentials audit logging](https://cloud.google.com/iam/docs/audit-logging/audit-logging-iamcreds) * [Security Token Service audit logging](https://cloud.google.com/iam/docs/audit-logging/audit-logging-sts) * [Identity and Access Management audit logging](https://cloud.google.com/iam/docs/audit-logging)

###  Restrict Public Access to BigQuery Datasets

Restrict public access to BigQuery datasets to avoid data exposure risk.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `PUBLIC_DATASET`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Remove the principals **allUsers** and **allAuthenticatedUsers** from the dataset permissions. For more information, see [Revoke access to a dataset](https://cloud.google.com/bigquery/docs/control-access-to-resources-iam#revoke_access_to_a_dataset).

###  Restrict Public Access to Cloud SQL Database Instances

Restrict public access to Cloud SQL database instances. If a Cloud SQL instance has '0.0.0.0/0' as an allowed network, any IPv4 client can attempt a login. This control doesn't apply to on-premises database instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `PUBLIC_SQL_INSTANCE`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **Cloud SQL Instances** page in the Google Cloud console. Click the instance name. Select **Connections**. Under **Authorized networks** , delete 0.0.0.0/0. Add a specific IP addresses or IP ranges that you want to let connect to your instance.

For more information, see [Authorize with authorized networks](https://cloud.google.com/sql/docs/sqlserver/authorize-networks).

###  Restrict Public Access to Cloud Storage Buckets

Restrict public access to Cloud Storage bucket to avoid data exposure risk. This control checks the IAM allow policy of a bucket for public roles, allUsers, or allAuthenticatedUsers.

Enforcement mode | Detective   
---|---  
Severity | `HIGH`  
Finding category | `PUBLIC_BUCKET_ACL`  
Revision number |  5   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Restrict anonymous public access to objects in Cloud Storage buckets. For more information, see [Remove public access for all objects within a bucket](https://cloud.google.com/storage/docs/access-control/making-data-public#remove-public-access).

###  Restrict Public Access to Data Stored in Buckets

Use the 'storage.publicAccessPrevention' organization policy constraint to block public access to Cloud Storage buckets and objects. This constraint prevents grants to 'allUsers' and 'allAuthenticatedUsers' from making data publicly accessible.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `GCS_BUCKET_PUBLICLY_ACCESSIBLE`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  2.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/storage.publicAccessPrevention`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `storage.publicAccessPrevention` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints) and [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention).



###  Restrict Public IP Addresses on Agent Platform Workbench Notebooks and Instances

Use the "Restrict public IP access on new Vertex AI Workbench notebooks and instances" (ainotebooks.restrictPublicIp) organization policy constraint to restrict public IP access to new Gemini Enterprise Agent Platform Workbench notebooks and instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `ORG_POLICY_PUBLIC_IP_ACCESS_ALLOWED_ON_VERTEXAI_WORKBENCH`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Restrict public IP access on new Vertex AI Workbench notebooks and instances** (`ainotebooks.restrictPublicIp`) constraint to `true` to restrict public IP access on new Agent Platform Workbench notebooks and instances. For more information, see [Updating policies with boolean rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints).

###  Restrict Public IP Addresses to Compute Engine Instances

Don't assign public IP addresses to Compute Engine instances. A Compute Engine instance with a public IP address increases attack surface. This control checks network interfaces to determine whether they define external IP addresses. This control doesn't check GKE or Dataflow instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `PUBLIC_IP_ADDRESS`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **VM instances** page in the Google Cloud console. Find the instances with a public IP address. For each interface under **Network interfaces** , set **External IP** to **None**. To block public IP addresses across Compute Engine, use the **Define allowed external IPs for VM instances** (`constraints/compute.vmExternalIpAccess`) organization policy. Configure an empty allowlist of external IP addresses that the VM can use and deny all others.

###  Restrict Resource Locations

Use the "Restrict Resource Locations" (`constraints/gcp.resourceLocations`) organization policy constraint to define the locations that you can create resources in.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `ORG_POLICY_RESOURCE_LOCATION_DENIED`  
Category name in the API | CC_CATEGORY_DATA_RESIDENCY  
Revision number |  3.4   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/gcp.resourceLocations`  
---|---  
  
#### Parameters

Required union field `locations`.  List of allowed or denied Google Cloud regions or multi-regions. `locations` can be only one of the following:   
---  
`allowedLocations` |  `STRINGLIST` List of allowed Google Cloud regions or multi-regions (e.g., 'us-central1', 'us').  
`deniedLocations` |  `STRINGLIST` List of denied Google Cloud regions or multi-regions (e.g., 'us-central1', 'us').  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `gcp.resourceLocations` constraint to the required values:

    * Allowed locations: $allowedLocations
    * Denied locations: $deniedLocations

See [Updating policies with list rules](https://docs.cloud.google.com/organization-policy/apply-policies#list_constraints) and [Restrict resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations).

  * **Remediation for resource violation:** Delete the resource to resolve the resource violation associated with the `gcp.resourceLocations` constraint.




###  Restrict Resource Service Usage

Use the "Restrict Resource Service Usage" (gcp.restrictServiceUsage) organization policy constraint to define which Google Cloud services can be used within an organization, folder, or project.

Enforcement mode | Audit   
---|---  
Finding category | `ORG_POLICY_RESOURCE_SERVICE_USAGE_NOT_ALLOWED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure the **Restrict Resource Service Usage** (`gcp.restrictServiceUsage`) constraint. For instructions, see [Setting the organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-resources#setting_the_organization_policy).

###  Restrict Service Usage

Use the "Restrict Resource Service Usage" (`constraints/gcp.restrictServiceUsage`) organization policy constraint to define which Google Cloud services can be used within an organization, folder, or project.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_RESTRICT_SERVICE_USAGE_NOT_FOLLOWED`  
Category name in the API | CC_CATEGORY_RESOURCE_USAGE_RESTRICTION  
Revision number |  1.3   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/gcp.restrictServiceUsage`  
---|---  
  
#### Parameters

Required union field `serviceUsage`.  Define which Google Cloud services can be used. You can provide an allowed list or a denied list. `serviceUsage` can be only one of the following:   
---  
`allowedServices` |  `STRINGLIST` List of allowed Google Cloud services and APIs.  
`deniedServices` |  `STRINGLIST` List of denied Google Cloud services and APIs.  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `gcp.restrictServiceUsage` constraint to the required values:

    * Allowed services: $allowedServices
    * Denied services: $deniedServices

See [Updating policies with list rules](https://docs.cloud.google.com/organization-policy/apply-policies#list_constraints) and [Restrict service usage](https://docs.cloud.google.com/organization-policy/restrict-services).

  * **Remediation for resource violation:** Delete the resource to resolve the resource violation associated with the `gcp.restrictServiceUsage` constraint.




###  Restrict Service Usage

Use the "Restrict Resource Service Usage" (`constraints/gcp.restrictServiceUsage`) organization policy constraint to define which Google Cloud services can be used within an organization, folder, or project.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ORG_POLICY_RESTRICT_SERVICE_USAGE_NOT_SET`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Configure the **Restrict Resource Service Usage** (`constraints/gcp.restrictServiceUsage`) organization policy. For instructions, see [Setting the organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-resources#setting_the_organization_policy).

###  Restrict the BigQuery Data Transfer Service API

Restrict BigQuery Data Transfer API calls to configure support for data boundaries

Enforcement mode | Preventive   
---|---  
Severity | `HIGH`  
Finding category | `CLOUD_DATATRANSFER_REGULATORY_SETTINGS_NON_COMPLIANT`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.1   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

**CSS name:** BQ Data Transfer AW Settings 

###  Restrict the Use of Default Service Account for Agent Platform Workbench Instances

Restricts the usage of the highly permissive default service account for Gemini Enterprise Agent Platform Workbench Instances to reduce the risk of unauthorized access to Google Cloud services.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `VERTEX_AI_DEFAULT_SERVICE_ACCOUNT_IN_USE`  
Category name in the API | CC_CATEGORY_ARTIFICIAL_INTELLIGENCE  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Change the service account associated with the Agent Platform Workbench Instance:

  1. If required, create a service account with appropriate privileges. For instructions see [Manage access to an instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/manage-access).

  2. In the Google Cloud console, go to the [**Instances** page](https://console.cloud.google.com/agent-platform/workbench/instances).

  3. Click the instance that you want to configure.

  4. Stop the instance.

  5. In the **Systems** section, click **VM details**.

  6. Edit the Compute Engine instance and select a service account that uses appropriate privileges.

  7. Restart the instance.




###  Restrict TLS Versions

Restricts the minimum TLS version allowed for connections.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `TLS_VERSIONS_NOT_RESTRICTED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  1.4   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/gcp.restrictTLSVersion`  
---|---  
  
#### Parameters

`deniedTlsVersions` |  `STRINGLIST` Required. List of TLS versions to deny (e.g., 'TLS_1_0', 'TLS_1_1').  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `gcp.restrictTLSVersion` constraint to the required values:

    * Denied values: $deniedTlsVersions

See [Updating policies with list rules](https://docs.cloud.google.com/organization-policy/apply-policies#list_constraints) and [Restrict TLS versions](https://docs.cloud.google.com/docs/security/compliance/restrict-tls-versions).




###  Restrict Usage of Shared and Group Accounts

Restrict the use of shared or group accounts to help maintain a secure environment.

Enforcement mode | Audit   
---|---  
Finding category | `SECURE_MANAGEMENT_OF_SHARED_AND_GROUP_ACCOUNTS_POLICY_NEEDS_REVIEW`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Define policies for the use of shared or group accounts.

  * Use role-based access control (RBAC) and IAM roles. Assign roles based on responsibilities.

  * Use individual accounts whenever possible.

  * Regularly audit and review activities associated with shared or group accounts.

  * Use strong authentication practices such as 2-step verification for shared or group accounts.

  * Review access regularly to ensure that shared accounts are still required.

  * Document and communicate your policies regarding shared or group accounts.

  * Train users on these policies.

  * Use automation, such as Deployment Manager or Terraform, to enforce your policies and configuration. For more best practices, see [Best practices for using Google groups](https://cloud.google.com/iam/docs/groups-best-practices).




###  Restrict User Managed Service Account Keys

Avoid having user-managed keys for user-managed service accounts.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `USER_MANAGED_SERVICE_ACCOUNT_KEY`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Determine a secure alternative and delete the user-managed service account keys. For information about alternatives, see [Choose the right authentication method for your use case](https://cloud.google.com/docs/authentication#auth-decision-tree). To delete the user-managed service account keys, go to the **Service Accounts** page in the Google Cloud console. Select and delete the user-managed service account keys. For more information on service account key management, see [Best practices for managing service account keys](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

###  Restrict VM IP Forwarding for Compute Engine Instances

Use the "Restrict VM IP Forwarding" (compute.vmCanIpForward) organization policy constraint to define the set of VM instances that can enable IP forwarding.

Enforcement mode | Audit   
---|---  
Finding category | `ORG_POLICY_COMPUTE_IPFORWARD_LIST_VIOLATED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Specify the VM instances that can enable IP forwarding in the **Restrict VM IP Forwarding** (`compute.vmCanIpForward`) constraint. Use one of the following forms: * `under:organizations/ORGANIZATION_ID` * ` under:folders/FOLDER_ID` * `under:projects/PROJECT_ID` * `projects/PROJECT_ID/zones/ZONE/instances/INSTANCE-NAME`. For more information, see [Enable IP forwarding for instances](https://cloud.google.com/vpc/docs/using-routes#canipforward).

###  Restrict VPC Networks on Agent Platform Workbench Instances

Use the "Restrict VPC networks on new Vertex AI Workbench instances" (ainotebooks.restrictVpcNetworks) organization policy constraint to define the VPC networks that a user can select when creating new Gemini Enterprise Agent Platform Workbench instances.

Enforcement mode | Audit   
---|---  
Finding category | `ORG_POLICY_VERTEXAI_VPC_NETWORK_POLICY_NOT_SET`  
Revision number |  1.2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **Restrict VPC networks on new Vertex AI Workbench instances** (`ainotebooks.restrictVpcNetworks`) constraint to the allowed or denied list of networks. Use one of the following formats: `under:organizations/ORGANIZATION_ID`, `under:folders/FOLDER_ID`, `under:projects/PROJECT_ID`, or `projects/PROJECT_ID/global/networks/NETWORK_NAME`.

###  Retain Audit Records

Retain audit records for 90 days or more to provide support for after-the-fact investigations of incidents.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `AUDIT_RECORDS_NOT_RETAINED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Enable [audit logging](https://cloud.google.com/logging/docs/audit).

  * [Export audit logs](https://cloud.google.com/logging/docs/export/configure_export_v2) to Cloud Storage, BigQuery, or Pub/Sub for retention for at least 90 days.

  * Create a process to archive logs to an cost-effective, offline storage system.

  * [Configure the lifecycle](https://cloud.google.com/storage/docs/managing-lifecycles) for your Cloud Storage bucket.

  * Regularly review and monitor exports to logs.

  * Regularly test your backup and restore procedures.




###  Retrieve Binary Authorization Configurations

Review Binary Authorization configurations to ensure that they align with the regulatory requirements.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_BINARY_AUTHORIZATION_CONFIGURATIONS`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that the Binary Authorization configuration includes cryptographic mechanisms for resource integrity verification that adheres to FedRAMP Key Security Indicators (KSIs).

###  Retrieve Cloud KMS Configurations

Review Cloud KMS configurations to review the keys, ensure that automatic key rotation is enabled and access to Cloud KMS keys is restricted to help protect and manage digital keys and certificates.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_CLOUD_KMS_CONFIGURATIONS_REVIEW`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Regularly review all Cloud KMS keys to ensure that only authorized individuals have access to the Cloud KMS keys, review the custom KMS bindings, confirm their continued necessity and ensure their rotation aligns with organizational requirements. For more information, see [Key rotation](https://cloud.google.com/kms/docs/key-rotation) and [Cloud Key Management Service overview](https://cloud.google.com/kms/docs/key-management-service).

###  Retrieve Cloud NAT Configurations

Retrieve NAT configurations to review if outbound traffic is routed and managed.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_CLOUD_NAT_CONFIGURATIONS`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Evaluate the Cloud NAT gateway configuration to ensure outbound traffic is correctly routed and managed. For more information, see [View a Public NAT configuration](https://cloud.google.com/nat/docs/set-up-manage-network-address-translation#showing_the_nat_configuration_ipport-ranges_and_status).

###  Retrieve GKE Availability

Retrieve the status of Google Kubernetes Engine (GKE) clusters to verify they are healthy (RUNNING) and ready to serve requests.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `GKE_CLUSTER_AVAILABILITY`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

If a cluster is not in RUNNING state, check the [Cluster Status documentation](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#cluster_status) for troubleshooting steps.

###  Retrieve VPC Network Peering Configurations

Retrieve VPC network peering configurations to facilitate manual review. Ensure that peerings are established only with trusted networks.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `REVIEW_VPC_PEERING_CONFIGURATIONS`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Review the extracted peering configurations. If an unauthorized peering is found, verify the target network and remove the peering if necessary. See [VPC Network Peering](https://cloud.google.com/vpc/docs/vpc-peering).

###  Review Artifact Registry Images

Extract the source images of Artifact Registry containers and verify if hardened images are created and used.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_REVIEW_OF_ARTIFACT_REGISTRY_IMAGES`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To get source images, see [Push and pull images](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling).

###  Review Authentication, Authorization, User Account Management

Manage and review user authentication, authorization, and account management practices.

Enforcement mode | Audit   
---|---  
Finding category | `IAM_USERACCOUNT_MANAGEMENT_UNAUTHORIZED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * Enable SSO.

  * Synchronize user accounts using Google Cloud Directory Sync.

  * Configure Google Sign-In authentication for anyone with the legacy basic Owners role.

  * Grant the legacy basic Owners role to your account managers. Maintain assignments as required.

  * Define and maintain group and role membership conditions in your user directories.

  * Grant appropriate roles to users and groups in your organization.

  * Implement an approval process in your user directories for account creation.

  * Manage service accounts according to your organization's processes.

  * Enable audit logging and review logs for account usage.

  * Notify account managers about account deactivations and transfers. Consider exporting audit logs to BigQuery.

  * Ensure all Google Cloud access is by valid accounts and for intended usage.

  * Review IAM roles and account configuration for compliance with your internal and external policies.

  * Revoke and reissue shared credentials when a user is removed from a group.




###  Review Cloud Run Images

Identify Cloud Run container images to facilitate manual review for compliance with hardening standards.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_REVIEW_OF_CLOUD_RUN_IMAGES`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To get source images, see [View revision details](https://cloud.google.com/run/docs/managing/revisions#view_revision_details). Click the **Container image URL** in the **DETAILS panel**.

###  Review Hardened Compute Images

Extract the OS images of VM instances and verify that hardened images are created and used for VM instances.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_REVIEW_OF_COMPUTE_IMAGES`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Review Compute Engine VM images to ensure that they are hardened. For more information, see [View the source image of a VM](https://cloud.google.com/compute/docs/instances/view-vm-image).

###  Review Log and Alert Configuration

Review alerting policies, log filters, and metrics.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_AUDIT_PROCESSING_FAILURES_ALERTS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * [Verify that alerting policies](https://cloud.google.com/monitoring/alerts/manage-alerts#manage-policies) are set up by checking if they have associated notification channels.

  * [Enable audit logging](https://cloud.google.com/logging/docs/audit).

  * [Review log entries](https://cloud.google.com/logging/docs/view/logs-explorer-interface).

  * [Review Service Management audit logs](https://cloud.google.com/service-infrastructure/docs/audit-logging).

  * [Create metrics](https://cloud.google.com/logging/docs/logs-based-metrics) to capture relevant events.




###  Review Organization Administrator Assignments

Review the users in your organization who have the roles/resourcemanager.organizationAdmin role. Ensure at least one user has this role.

Enforcement mode | Audit   
---|---  
Finding category | `ORGANIZATION_ADMIN_ROLE_NOT_ASSIGNED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify the Organization Administrator (`roles/resourcemanager.organizationAdmin`) role assignments and grant it to additional users as required. For more information, see [Viewing existing access for an organization resource](https://cloud.google.com/resource-manager/docs/access-control-org#viewing-access) and [Grant an IAM role by using the Google Cloud console](https://cloud.google.com/iam/docs/grant-role-console).

###  Review Resource Inventory

Review the extracted asset inventory list.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_RESOURCE_INVENTORY`  
Revision number |  5   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify if all assets are included in the extracted inventory list and ensure that their status reflects a desired transitional state.

###  Separate User and Administrator Roles

Define separate user and admin roles.

Enforcement mode | Audit   
---|---  
Finding category | `USER_ADMIN_ROLES_NOT_SEPARATED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Define different roles and accounts for users and administrators.

  * Enable two-factor or multi-factor authentication for users, especially administrators, to enhance account security.




###  Set Application Restriction on API Keys

Unrestricted API keys pose a security risk as any untrusted application can use them. Implement restrictions on API keys to specific hosts, HTTP referrers, and applications to help enhance security. This control checks the restrictions property of all API keys in a project to determine if any values are set to cloudapis.googleapis.com.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `API_KEY_APPS_UNRESTRICTED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **APIs & Services** > **Credentials** page in the Google Cloud console. Under **API Keys** , edit each key using the **Actions** menu, and then restrict applications under the **Application restrictions** section.

###  Set Ingress and Egress Controls for Compute

Limit the number of external network connections to your system.

Enforcement mode | Audit   
---|---  
Finding category | `INGRESS_EGRESS_CONTROLS_NOT_SET`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Create [firewall rules](https://cloud.google.com/firewall/docs/firewalls) to limit incoming external connections and outgoing external connections.

  * Create a rule that denies all traffic that you haven’t explicitly allowed.




###  Set Log Bucket Flag for Bucket Logging

The log-bucket flag enables usage logs and storage logging for Cloud Storage buckets.

Enforcement mode | Audit   
---|---  
Finding category | `LOGBUCKET_SET_INCORRECTLY`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the correct log bucket for Cloud Storage buckets. See [Set up log delivery](https://cloud.google.com/storage/docs/access-logs#delivery).

###  Set Log Error Verbosity Flag for AlloyDB Instances

The log_error_verbosity flag for AlloyDB for PostgreSQL helps to ensure adequate coverage of message types in the log. This control checks if the log_error_verbosity field of the databaseFlags property is set to verbose or default.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOYDB_LOG_ERROR_VERBOSITY`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **log_error_verbosity** flag to **default** or **verbose**.

  1. Go to the **AlloyDB for PostgreSQL clusters** page in the Google Cloud console.

  2. Click a cluster in the **Resource Name** column.

  3. Under the **Instances in your cluster** section, click **Edit** for the instance.

  4. Click **Advanced Configuration Options**.

  5. Under the **Flags** section, set the `log_error_verbosity` flag to _default_ or _verbose_.




###  Set Log Min Error Statement Flag for AlloyDB Instances

The log_min_error_statement flag for AlloyDB for PostgreSQL instance helps to identify the SQL statements that cause an error condition to be recorded in the server log. At a minimum, set the value to error.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `ALLOYDB_LOG_MIN_ERROR_STATEMENT_SEVERITY`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **log_min_error_statement** flag to **error**.

  1. Go to the **AlloyDB for PostgreSQL clusters** page in the Google Cloud console.

  2. Click the cluster in the **Resource Name** column.

  3. Under the **Instance in your cluster** section, click **Edit** for the instance.

  4. Click **Advanced Configuration Options** , and set the `log_min_error_statement` flag under the **Flags** section to a recommended value like error.




###  Set Log Min Messages Flag for AlloyDB Instances

The log_min_messages flag for AlloyDB for PostgreSQL instance helps to control message levels recorded in server logs. Permitted values are debug5, debug4, debug3, debug2, debug1, info, notice, or warning. At a minimum, set the value to warning.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `ALLOYDB_LOG_MIN_MESSAGES`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **log_min_messages** flag to **warning**.

  1. Go to the **AlloyDB for PostgreSQL clusters** page in the Google Cloud console.

  2. Click the cluster in the **Resource Name** column.

  3. Under the **Instance in your cluster** section, click **Edit**.

  4. Click **Advanced Configuration Options**.

  5. Set the `log_min_messages` flag under the **Flags** section to one of Notice, Info, Debug1, Debug2, Debug3, Debug4, or Debug5.




###  Set Uniform Bucket Level Access for Cloud Storage Buckets

Enable fine-grained access control for Cloud Storage buckets by using the "Enforce uniform bucket-level access" (`storage.uniformBucketLevelAccess`) organization policy constraint or setting the access controls for a bucket to Uniform.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `UNIFORM_BUCKET_LEVEL_ACCESS_ORG_POLICY`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete one or both of the following:

  * Set the access control for a bucket to **Uniform**. For more information, see [Set uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access#set).

  * Set the **Enforce uniform bucket-level access** (`storage.uniformBucketLevelAccess`) organization policy constraint to `true`. For more information, see [Require uniform bucket-level access](https://docs.cloud.google.com/storage/docs/org-policy-constraints#uniform-access).




###  Set Up Job Scheduling and Configurations

Set up proper job scheduling and configurations to manage security tasks.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING SCHEDULING AND CONFIGURATIONS_SECURITY_TASKS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Configure job scheduling and configurations to manage tasks. Consider using [Cloud Scheduler](https://cloud.google.com/scheduler/docs/overview).

  * [Grant appropriate IAM roles](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to different groups.

  * Enable multi-factor authentication (MFA) or two-factor authentication (2FA) for production access.

  * Create separate projects to segregate resources.




###  Set Zonal DNS as Default for Compute Engine

Uses the 'compute.setNewProjectDefaultToZonalDNSOnly/' organization policy constraint to enforce zonal DNS on new projects. Zonal DNS improves reliability by isolating DNS outages to a single zone, which is a best practice for robust systems.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `MEDIUM`  
Finding category | `GCE_GLOBAL_DNS_DEFAULT_ENABLED`  
Category name in the API | CC_CATEGORY_SERVICE_SPECIFIC  
Revision number |  2.2   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/compute.setNewProjectDefaultToZonalDNSOnly`  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `compute.setNewProjectDefaultToZonalDNSOnly` constraint to `true`. See [Updating policies with boolean rules](https://docs.cloud.google.com/organization-policy/apply-policies#boolean_constraints).



###  Specify Cloud KMS Key Protection Levels

Uses the cloudkms.allowedProtectionLevels constraint to restrict the allowed protection levels (for example, SOFTWARE, HSM, or EXTERNAL) for Cloud KMS keys. Protection levels let you define your encryption requirements for the services in your project or folder.

Enforcement mode | 

  * Preventive 
  * Detective 

  
---|---  
Severity | `HIGH`  
Finding category | `KMS_PROTECTION_LEVELS_UNSPECIFIED`  
Category name in the API | CC_CATEGORY_ENCRYPTION  
Revision number |  1.4   
Supported target resources | 

  * Folder
  * Project

  
  
#### Rules

Organization policy constraint |  `constraints/cloudkms.allowedProtectionLevels`  
---|---  
  
#### Parameters

`allowedLevels` |  `STRINGLIST` Required. Required. The list of allowed protection levels. Possible values are SOFTWARE, HSM, HSM_SINGLE_TENANT, EXTERNAL, or EXTERNAL_VPC.  
---|---  
  
#### Remediation steps

  * **Remediation for organization policy violation:** Set the `cloudkms.allowedProtectionLevels` constraint to the required values:

    * Allowed values: $allowedLevels

See [Updating policies with list rules](https://docs.cloud.google.com/organization-policy/apply-policies#list_constraints) and [Allowed protection levels](https://docs.cloud.google.com/kms/docs/org-policy-constraints#allowed-protection-levels).




###  SQL No Additional Local Users

Ensure additional local users are not created within SQL databases.

Enforcement mode | Detective   
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_ADDITIONAL_LOCAL_USERS_FOUND`  
Revision number |  1   
  
#### Remediation steps

Ensure that at most one user of type 'BUILT_IN' exists for each Cloud SQL instance.

###  Store Audit Logs in a Separate Repository

Back up audit logs in a separate physical repository and configure a retention schedule, integrity checks, monitoring, and access controls.

Enforcement mode | Audit   
---|---  
Finding category | `IMPROPER_STORAGE_AUDIT_LOGS`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Enable audit logging.

  * Export logs to your backup. You can use a Cloud Storage bucket or export to an external storage system.

  * Configure retention periods.

  * Review and monitor exported logs.

  * Use checksums to verify integrity.

  * Use Cloud Monitoring and Pub/Sub to set up custom monitoring and alerting policies for exported logs.

  * Test your backup and restore procedures.

  * If storing logs outside of Google Cloud, configure security settings for your backup system.

  * Follow Google Cloud best practices for [audit logging](https://cloud.google.com/logging/docs/audit/best-practices), export, and backup configurations.

  * Configure access controls for the backup destination.




###  Subscribe a GKE Cluster to a Release Channel

Subscribe to a release channel to automate Google Kubernetes Engine (GKE) cluster version upgrades.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `RELEASE_CHANNEL_DISABLED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Subscribe the GKE cluster to a release channel. For more information, see [Enroll a new cluster in a release channel](https://cloud.google.com/kubernetes-engine/docs/how-to/release-channels#enrolling_a_cluster_in_a_release_channel) and [Enroll an existing cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster).

###  Synchronize System Clocks

Ensure that all clocks use the same timezone (for example, UTC) so that you can use audit logs.

Enforcement mode | Audit   
---|---  
Finding category | `SYSTEM_CLOCKS_NOT_SYNCHRONIZED`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Set all system clocks to UTC.

  * For applications that generate custom logs, generate the timestamp in UTC.

  * Use [Google Cloud logging libraries](https://cloud.google.com/logging/docs/apis), which automatically generate timestamps in the system⒙s timezone.

  * Verify that the timestamp for [audit logs](https://cloud.google.com/logging/docs/audit/understanding-audit-logs) is in UTC.

  * Verify the [timestamp in logs](https://cloud.google.com/logging/docs/analyze/query-and-view).

  * Consider manually synchronizing with [Google⒙s time servers](https://developers.google.com/time).

  * Synchronize system clocks with Google's NTP servers. For example: ` sudo chronyc makestep `




###  Tags Attached To Projects

For all applications running/deployed in cloud, the landing zone deploys separate production and non-production environments.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `REQUIRED_TAGS_MISSING`  
Revision number |  2.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

The resource is missing the required tag key/value combination for environment specification. Ensure the tag with key ID 'tagKeys/281480036376309' is attached and has one of the allowed values. See https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing.

###  Terminate Network Connections

Terminate the network connection associated with a communications session at the end of the session or after 600 seconds (10 minutes) of inactivity.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `NETWORK_CONNECTION_TERMINATION_PROCEDURE_MISSING`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify the HTTP keepalive timeout for your clients. For instructions, see [Update client HTTP keepalive timeout](https://cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute#update-keepalive-timeout).

###  Test Incident Response Capabilities

Test your capability to recover from incidents and contingencies.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_INCIDENT_RESPONSE_TESTING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Test the contingency plan for your system, review the contingency plan test results, and initiate corrective actions, if needed. Conduct regular system backups and test the reliability and integrity of the backups. Test the effectiveness of the incident response capability for your systems.

###  Track and Report Model Card Features

Configure Security Command Center to track and report on model card features to help maintain information integrity.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `TRACKING_OF_MODEL_CARD_FEATURES_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure that you can ingest and use information in model cards or model card equivalents when evaluating your security posture in Security Command Center and Compliance Manager. For more information, see [Model Armor overview](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) and [Create and manage Model Armor templates](https://docs.cloud.google.com/security-command-center/docs/manage-model-armor-templates).

###  Track TEVV Provenance and Quality

Configure data management to help track the provenance and quality of test, evaluation, validation, and verification (TEVV) protocols.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `PROVENANCE_TRACKING_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Include options to track training processes for all data types to help ensure comprehensive provenance and training history that include records of origin, date of acquisition or collection, and a complete chain of custody for all data types.

###  Triage and Remediate System Flaws

Identify, report, and correct system flaws. Incorporate flaw remediation into the organizational configuration management process.

Enforcement mode | Audit   
---|---  
Finding category | `WEAK_TRIAGING_REMEDIATION_MECHANISM_SYSTEM_FLAWS`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Consider the following:

  * Verify the images that you use for VMs and containers.

  * Triage and correct information system flaws. Use [Security Command Center)](https://cloud.google.com/security-command-center/docs) and [Patch feature in VM Manager](https://cloud.google.com/compute/docs/os-patch-management).

  * Test software and firmware updates before installation.

  * Install security software and firmware updates within 30 days of release.

  * Include flaw remediation into your configuration management processes.




###  Turn Off Contained Database Authentication Flag for SQL Server

Turn off the contained database authentication flag for SQL Server instances. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_CONTAINED_DATABASE_AUTHENTICATION`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set **contained database authentication** database flag to **Off** for the instance.

###  Turn Off Cross Database Ownership Chaining Flag for SQL Server

Turn off the cross_db_ownership_chaining flag for SQL Server. Enabling this flag is not recommended unless all databases hosted by the SQL Server instance participate in cross-database ownership chaining and you are aware of the security implications of this setting. This control doesn't apply to on-premises databases.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_CROSS_DB_OWNERSHIP_CHAINING`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn the **cross db ownership chaining** flag off. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **cross db ownership chaining** database flag to **Off** for the instance. For cross-database access, use the Microsoft [Tutorial: Signing Stored Procedures with a Certificate](https://learn.microsoft.com/en-us/sql/relational-databases/tutorial-signing-stored-procedures-with-a-certificate?view=sql-server-ver16) instead.

###  Turn Off External Scripts Flag for SQL Server

When activated, this setting enables the execution of scripts with certain remote language extensions. This control checks the databaseFlags property of instance metadata for the key-value pair "external scripts enabled" set to "off".

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_EXTERNAL_SCRIPTS_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn the **external scripts enabled** flag off. Go to the **SQL** > **Instances** page in the Google Cloud console and set **external scripts enabled** database flag to **Off** for the instance.

###  Turn Off Local Infile Flag for MySQL

Turn off the local_infile flag for the MySQL instance. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOCAL_INFILE`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **local_infile** database flag to **Off** for the instance.

###  Turn Off Log Executor Stats Flag for PostgreSQL

Turn off the log_executor_stats flag for PostgreSQL instances to reduce performance overhead. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SQL_LOG_EXECUTOR_STATS_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_executor_stats** database flag to **Off** for the Cloud SQL instance.

###  Turn off Log Hostname Flag for PostgreSQL

Turn off the log_hostname flag for PostgreSQL instances to reduce performance overhead.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SQL_LOG_HOSTNAME_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_hostname** database flag to **Off** for the Cloud SQL instance.

###  Turn Off Log Min Duration Statement Flag for PostgreSQL

Turn off the log_min_duration_statement flag by setting it to -1 for PostgreSQL instances. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_MIN_DURATION_STATEMENT_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_min_duration_statement** database flag to **-1** for the Cloud SQL instance.

###  Turn off Log Parser Stats Flag for PostgreSQL

Turn off the log_parser_stats flag for PostgreSQL to reduce performance overhead. This control checks if the databaseFlags property of instance metadata for the log_parser_stats field is set to on.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_LOG_PARSER_STATS_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **log_parser_stats** flag to **Off**. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_parser_stats** database flag to **Off** for the Cloud SQL instance.

###  Turn off Log Planner Stats Flag for PostgreSQL

Turn off the log_planner_stats flag for PostgreSQL to reduce performance overhead. This control checks if the databaseFlags property of instance metadata for the log_planner_stats field is set to on.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SQL_LOG_PLANNER_STATS_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the **log_planner_stats** flag to **Off**. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_planner_stats** database flag to **Off** for the Cloud SQL instance.

###  Turn off Log Statement Stats Flag for PostgreSQL

Turn off the log_statement_stats flag for PostgreSQL instance to reduce performance overhead. This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `LOW`  
Finding category | `SQL_LOG_STATEMENT_STATS_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **SQL** > **Instances** page in the Google Cloud console and set the **log_statement_stats** database flag to **Off** for the Cloud SQL instance.

###  Turn Off Remote Access Flag for SQL Server

Turn off the remote access flag for the SQL Server instance to avoid security risks. This control checks the databaseFlags property of the instance metadata for the key-value "remote access" set to "off". This control doesn't apply to on-premises instances.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `SQL_REMOTE_ACCESS_ENABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Turn off the **remote_access** flag. Go to the **SQL** > **Instances** page in the Google Cloud console and set the **Remote access** flag to **Off** for the SQL Server instance.

###  Use Central SIEM

Use a centralized Security Information and Event Management (SIEM).

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_CENTRAL_SIEM`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Manage a Security Information and Event Management (SIEM) or similar systems for centralized, tamper-resistant logging of events, activities, and changes.

###  Use Custom Service Accounts for Compute Engine Instances

Default Compute Engine service accounts have broad editor roles, granting read and write access to most Google Cloud services. Custom service accounts help prevent privilege escalation and unauthorized access. This control doesn't apply to GKE instances or Dataflow jobs.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DEFAULT_SERVICE_ACCOUNT_USED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Change the service account that the VM instance uses.

  1. Go to the **Compute Engine** > **VM instances** page in the Google Cloud console.

  2. Click the instance name.

  3. Select the instance, and click **Stop** on the **Instance details** page.

  4. After the instance stops, edit it, and select a non-default service account with least privileges.




###  Use Custom VPC Networks

Create a VPC network with custom firewall rules to help enhance security and provide better control over network access.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DEFAULT_NETWORK`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Go to the **VPC Network** > **VPC networks** page in the Google Cloud console and delete the default VPC network. Create a network with custom firewall rules. For more information, see [Create networks](https://cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).

###  Use Default Encryption

Verify that Cloud SQL instances, Cloud Storage, Compute Engine VM instances, and Compute Engine disks are encrypted. This control doesn't require that you enable customer-managed encryption keys (CMEKs).

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `DEFAULT_ENCRYPTION_NOT_VERIFIED`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Ensure core content data is encrypted between clients and Google networks, between Google data centers, and at rest. For more information, see [Default encryption at rest](https://cloud.google.com/docs/security/encryption/default-encryption).

###  Use Differentially Private Techniques to Generate Synthetic Data

Generate synthetic data using differentially private (DP) techniques.

Enforcement mode | Audit   
---|---  
Severity | `MEDIUM`  
Finding category | `DP_SYNTHETIC_TRAINING_DATA_NOT_GENERATED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use differentially private synthetic data generation to create anonymized data for training. For more information, see [Use differential privacy](https://docs.cloud.google.com/bigquery/docs/differential-privacy).

###  Use FIPS 201 Approved Products

Use information technology products on the Federal Information Processing Standards (FIPS) 201-approved products list for Personal Identity Verification (PIV) capability.

Enforcement mode | Audit   
---|---  
Finding category | `FIPS 201_APPROVED_PRODUCTS_NOT_USED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Complete the following:

  * Use only services and products that comply with FIPS-201 standards.

  * Implement a user account system or SSO solution for authentication.

  * Configure 2FA using a PIV card.

  * Use [IAM allow policies](https://cloud.google.com/iam/docs/granting-changing-revoking-access) to control access to your resources.




###  Use Google Groups for Kubernetes RBAC

Set up Google Groups to work with Kubernetes role-based access control (RBAC) in your GKE clusters.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `GKE_AUTHENTICATOR_GROUPS_DISABLED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Update your cluster to use Google Groups for RBAC. For more information, see [Update an existing cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac#update-existing).

###  Use IAM Tags

Use tags to create annotations for resources, and in some cases conditionally allow or deny policies based on whether a resource has a specific tag.

Enforcement mode | Audit   
---|---  
Finding category | `IAM_TAGS_NOT_FOUND`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

  * To create a tag key, run the following command: `gcloud resource-manager tags keys create SHORT_NAME --parent=organizations/ORGANIZATION_ID`.

  * To create a tag value, run the following command: `gcloud resource-manager tags values create SHORT_NAME --parent=PARENT`.

  * To attach a tag to a resource, run the following command: `gcloud resource-manager tags bindings create --tag-value=TAG_VALUE --parent=RESOURCE_ID --location=LOCATION`.




###  Use labels for Agent Platform agents

Apply labels to data points, tools, and agent configurations for agents that you deploy using Gemini Enterprise Agent Platform. These labels must provide information about the data classification and the environment (for example, staging or production) that the data is located in.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `GEMINI_ENTERPRISE_AGENT_PLATFORM_AGENTS_NOT_LABELED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To set metadata labels, see [Custom metadata labels](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/add-labels-to-api-calls).

###  Use Latest Image Versions on Dataproc Clusters

Ensure that Dataproc clusters don't use outdated image versions that are impacted by the Log4j vulnerability. This control checks whether the softwareConfig.imageVersion field in the config property of a Cluster is earlier than 1.3.95 or is a subminor image version earlier than 1.4.77, 1.5.53, or 2.0.27.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `DATAPROC_IMAGE_OUTDATED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Recreate and update the affected cluster with the latest sub-minor image versions. See [Steps to recreate a cluster](https://cloud.google.com/dataproc/docs/guides/recreate-cluster#console) for specific image and log4j version information.

###  Use Least Privilege and Just in Time Access

Use a least-privileged, role and attribute-based, and just-in-time security authorization model.

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_LEAST_PRIVILEGE_SECURITY_MODEL`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement a least-privileged, role and attribute-based, and just-in-time security authorization model for all user and non-user accounts and services within Google Cloud.

###  Use Least Privilege Service Accounts for GKE Clusters

Restrict Google Kubernetes Engine (GKE) node pools from using service accounts that have broad access and are over-privileged. This control checks the config property of a node pool to verify that a service account is specified and that the default service account isn't used.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `OVER_PRIVILEGED_ACCOUNT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use a service account with the minimal permissions required to run your GKE nodes. For more information, see [Use least privilege IAM service accounts](https://cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

###  Use Multifactor or Passwordless Authentication

Use secure passwordless methods or strong passwords with multifactor authentication (MFA).

Enforcement mode | Audit   
---|---  
Severity | `HIGH`  
Finding category | `MISSING_MFA_OR_PASSWORDLESS_AUTHENTICATION`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Implement secure passwordless methods for user authentication and authorization when feasible or enforce strong passwords with MFA. To configure this, in the Google Admin console, go to **Security > Authentication > 2-Step verification**.

###  Use Secure Web Proxy for Network Traffic Control

Configure Secure Web Proxy to route all network traffic and ensure the routing complies with regulatory standards for Compute Engine instances and Google Kubernetes Engine (GKE) clusters.

Enforcement mode | Audit   
---|---  
Finding category | `WEB_PROXY_NOT_CONFIGURED_TRAFFIC_CONTROL`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Use [Secure Web Proxy](https://cloud.google.com/secure-web-proxy/docs/overview) and set up appropriate rules to ensure that all the internal and external traffic routing is in compliance with the regulatory standards.

###  Use TLS 1.2 or Higher

Use TLS 1.2 or higher for encryption.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `IMPROPER_TLS_VERSION_IN_USE`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the minimum TLS version for Compute Engine instances to TLS 1.2 at both the global and regional levels. For more information, see [Use SSL policies for SSL and TLS protocols](https://cloud.google.com/load-balancing/docs/use-ssl-policies).

###  Validate Information Inputs

Validate information inputs and document exceptions when they occur.

Enforcement mode | Audit   
---|---  
Finding category | `INPUT_VALIDATION_MISSING`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Verify that you have the appropriate input checks set up and a way to document your exceptions.

###  Validate the Integrity of Data Stored in External Systems

Provide the capability to check the integrity of information while it resides in an external system.

Enforcement mode | Audit   
---|---  
Finding category | `MISSING_CONTROLS_DATA_STORED_EXTERNAL_SYSTEM`  
Revision number |  1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

This control doesn't apply to Google Cloud. Verify that you have the appropriate controls set up in external systems, as appropriate.

###  Verify Cloud KMS Key Version Algorithm

Check whether the key algorithms for Cloud KMS keys match the algorithms that you specify.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `CRYPTOKEY_ALGORITHM_VERSION_RESTRICTED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Default values are RSA_SIGN_PSS_2048_SHA256, RSA_SIGN_PSS_3072_SHA256, RSA_SIGN_PSS_4096_SHA256, RSA_DECRYPT_OAEP_2048_SHA256, RSA_DECRYPT_OAEP_4096_SHA256, RSA_DECRYPT_OAEP_2048_SHA1, and RSA_DECRYPT_OAEP_4096_SHA1. For more information, see [Key purposes and algorithms](https://cloud.google.com/kms/docs/algorithms).

###  Verify Cloud SQL Failover Replication

Verify that the Cloud SQL instance has at least one active read replica enabled for read scaling or disaster recovery.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_SQL_REPLICATION`  
Revision number |  4   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable replication, go to the [Cloud SQL Instances page](https://console.cloud.google.com/sql/instances). Select your instance and click Replicas > Create Read Replica. Choose your region and click Create.

###  Verify Cloud Storage Bucket Classification

Set the appropriate classification label for Cloud Storage buckets.

Enforcement mode | Audit   
---|---  
Finding category | `INCORRECT_CLOUD_STORAGE_CLASSIFICATION_ASSIGNED`  
Revision number |  1.1   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Set the right classification for the storage. See [Storage classes](https://cloud.google.com/storage/docs/storage-classes).

###  Verify Cloud Storage Regional Deployment

Retrieve the Cloud Storage bucket location type to confirm regional deployment.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `MEDIUM`  
Finding category | `MISSING_STORAGE_REGIONAL_DEPLOYMENT`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

For more information, see [Get bucket metadata](https://cloud.google.com/storage/docs/getting-bucket-metadata).

###  Verify GKE Container Optimized OS

Extract the source images of Google Kubernetes Engine (GKE) containers and verify if hardened images are created and used.

Enforcement mode | 

  * Detective 
  * Audit 

  
---|---  
Severity | `HIGH`  
Finding category | `MISSING_REVIEW_OF_GKE_IMAGES`  
Revision number |  3   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

Update the node pool to use the Container-Optimized OS with containerd (COS_CONTAINERD) image type.

###  VPC Flow Logs Disabled for Workstation Subnet

VPC Flow Logs must be enabled in the workstation subnet. The subnet used for cloud workstation should have VPC flow enabled

Enforcement mode | Detective   
---|---  
Severity | `MEDIUM`  
Finding category | `WORKSTATION_SUBNET_FLOW_LOGS_DISABLED`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To enable VPC Flow Logs for a subnet:

  1. In the Google Cloud console, go to the **VPC networks** page.
  2. Click the name of the subnet used by your workstation cluster.
  3. On the **Subnet details** page, click **Edit**.
  4. In the **Flow logs** section, select **On**.
  5. Click **Save**.



###  Workstation DNS Not Using Customer Managed DNS Zone

DNS resolution on Cloud Workstation must use the owner/customer managed DNS zone.

Enforcement mode | Detective   
---|---  
Severity | `MEDIUM`  
Finding category | `WORKSTATION_DNS_NOT_USING_CUSTOMER_MANAGED_DNS_ZONE`  
Revision number |  2   
Supported target resources | 

  * Organization
  * Folder
  * Project

  
  
#### Remediation steps

To ensure DNS resolution on Cloud Workstation uses a customer-managed DNS zone, configure your workstation cluster to use a custom hostname that falls under a domain managed by a Cloud DNS managed zone.

## What's next

  * Learn how to [Manage cloud controls](https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
