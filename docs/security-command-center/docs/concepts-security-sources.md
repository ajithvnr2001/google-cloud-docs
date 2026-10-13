---
url: https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources/
title: Choose the services to enable \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:48.285113+00:00
---

# Choose the services to enable  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Choose the services to enable Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document contains a list of the detection services, sometimes also referred to as _security sources_ , that Security Command Center uses to detect security issues in your cloud environments.

When these services detect an issue, they generate a _finding_ , which is a record that identifies the security issue and provides you with the information you need to prioritize and resolve the issue.

You can view findings in the Google Cloud console and filter them in many different ways, such as by finding type, resource type, or for a specific asset. Each security source might provide more filters to help you organize your findings.

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Vulnerability and misconfiguration detection services

These detection services include built-in and integrated services that detect software vulnerabilities, resource misconfigurations, and posture violations in your cloud environments. In finding definitions, these issues are categorized into distinct finding classes, such as `Vulnerability`, `Misconfiguration`, `Observation`, and `Posture violation`.

### AI Protection

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

AI Protection helps you manage the security posture of your AI workloads by detecting threats and helping you to mitigate risks to your AI asset inventory.

AI Protection provides the following detection capabilities:

  * **Assess your AI asset inventory** : Provides visibility into your AI systems and assets, such as models, data sources, endpoints, and AI agents.
  * **Identify vulnerabilities** : Detects software vulnerabilities (CVEs) in agentic workloads deployed with Agent Runtime.
  * **Identify risks** : Uses Attack Path Simulation and security graph rules to identify agentic risks and their potential impact on your environment.
  * **Detect over-privileged agents** : Identifies AI agents that have been granted excessive permissions.
  * **Detect and manage threats** : Detects and responds to potential threats targeting your AI systems and assets through integrated rules from other Security Command Center services, such as Event Threat Detection and Agent Platform Threat Detection.
  * **Detect Model Armor protection** : Detects whether Model Armor protects models.



For more information, see [AI Protection overview](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview).

### Artifact Registry vulnerability assessment

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Artifact Registry vulnerability assessment is a detection service that alerts you to vulnerabilities in your deployed container images.

This detection service generates vulnerability findings for container images under the following conditions:

  * The container image is stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).
  * The container image is deployed to one of the following assets:

    * Google Kubernetes Engine cluster
    * Cloud Run service
    * Cloud Run job
    * App Engine



For more information, see [Overview of Artifact Registry vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-ar-overview).

### Agent Platform Vulnerability Assessment

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Agent Platform Vulnerability Assessment identifies the following:

  * vulnerabilities in agentic workloads that you deployed with Agent Platform.
  * plaintext secrets, such as credentials, keys, access tokens, or certificates, in Gemini Enterprise Agent Platform container images.



#### Vulnerability detection

Agent Platform Vulnerability Assessment identifies software vulnerabilities (CVEs) in agentic workloads that you deployed with Agent Platform.

This scanner automatically assesses custom code and dependencies within the operational instance during deployment or update.

#### Enable Agent Platform Vulnerability Assessment

Agent Platform Vulnerability Assessment is automatically enabled for new activations of AI Protection.

If you are an existing customer, you can enable the scanner in the **AI Protection settings** page. For more information, see [Configure Agent Platform Vulnerability Assessment](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection#configure-agent-vulnerability-scanner).

#### Agent Platform Vulnerability Assessment detectors

Detector | Summary  
---|---  
  
#### `Software vulnerability`

Category name in the API: `SOFTWARE_VULNERABILITY` Class: `VULNERABILITY` Severity: `CRITICAL` or `HIGH` |  **Finding description** : A software vulnerability (CVE) was detected in an agentic workload that was deployed with Agent Platform. This scanner automatically assesses custom code and dependencies within the operational instance. **Pricing tier** : [Premium or Enterprise](https://cloud.google.com/security-command-center/pricing) **Fix this finding build**: Review the finding details to identify the impacted package and version. To resolve the finding, update your agent's requirements or custom container definition to use a secure version of the package, and then redeploy the Agent Platform instance. Redeploying the Agent Platform instance triggers a new scan. If the vulnerability is not present in the new deployment, the finding is marked as `INACTIVE`.  
  
#### `Secrets in Agent Platform`

Category name in the API: `SECRETS_IN_AGENT_ENGINE` Class: `SECRET` Severity: `CRITICAL` |  **Finding description** : Plaintext credential of type `<TYPE>` was found in image layer at path: `<PATH>`. **Pricing tier** : [Premium or Enterprise](https://cloud.google.com/security-command-center/pricing) **Fix this finding build**:

  * Investigate the finding to confirm details about the secret, and then revoke or rotate the exposed credential.
  * Remove the plaintext secret from the Dockerfile, source code, or configuration files used to build the image.
  * Implement a secure secret management solution, such as [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview), to store and access secrets securely at runtime.
  * Rebuild and redeploy the Agent Platform instance with the corrected image.

Redeploying the Agent Platform container image triggers a new scan. If the secret is not present in the new deployment, the finding is marked as `INACTIVE`.  
  
#### View Agent Platform Vulnerability Assessment findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Vulnerability Assessment for Agent Platform**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### Artifact guard

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

[Artifact guard](https://docs.cloud.google.com/security-command-center/docs/artifact-guard-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)) is a service that helps you prevent the deployment of vulnerable packages during the build process. It supports three policy scopes: CI/CD platform, registry and runtime. The [CI/CD integration](https://docs.cloud.google.com/security-command-center/docs/configure-cicd-integration) lets you configure connectors to CI/CD platforms. You can use these connectors to configure artifact guard policies to identify vulnerabilities in your CI/CD pipelines.

### Compliance Manager findings

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Compliance Manager creates findings for the detective and preventive cloud controls that you deploy in your Google Cloud environment. You can view these findings on the **Findings** page in Security Command Center.

Compliance Manager provides a different set of capabilities for each service tier. For more information, see [Compliance Manager overview](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview).

#### View Compliance Manager findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Compliance Evaluation Service**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### Data Security Posture Management

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

[Data Security Posture Management (DSPM)](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security) creates findings for potential violations of the data security frameworks and cloud controls that you apply in your environment. You can view these findings on the **Data Security & Compliance** page, the **Risk Overview** page (under the **Data** tab), or in the **Findings** page in Security Command Center. DSPM provides a different set of capabilities for each service tier. For more information, see [Data Security Posture Management (DSPM) overview](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security).

#### View DSPM findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud organization.

  3. Use the following query to view the findings for DSPM:
         
         state="ACTIVE" AND NOT mute="MUTED" AND resource.name="//aiplatform.googleapis.com/projects/478190632149/locations/us-central1/models/1244151282898305024" AND category="DATA_SECURITY_POSTURE_ACCESS_VIOLATION" OR category="DATA_SECURITY_POSTURE_FLOW_VIOLATION" OR category="DATA_SECURITY_POSTURE_DELETION_VIOLATION" OR category="DATA_SECURITY_POSTURE_PROTECTION_KEY_GOVERNANCE" OR category="BIGQUERY_TABLE_CMEK_DISABLED" OR category="VERTEX_AI_MODEL_CMEK_DISABLED" OR category="VERTEX_AI_METADATA_STORE_CMEK_DISABLED" OR category="VERTEX_AI_DATASET_CMEK_DISABLED" OR category="VERTEX_AI_FEATURE_STORE_TABLE_CMEK_DISABLED" OR category="DATA_SECURITY_POSTURE_CMEK_POLICY_MISCONFIGURED" OR category="DATA_SECURITY_POSTURE_CMEK_POLICY_DELETED" OR category="DATA_SECURITY_POSTURE_CMEK_VIOLATION" OR category="SENSITIVE_DATA_PUBLIC_SQL_INSTANCE" OR category="SENSITIVE_DATA_PUBLIC_DATASET" OR category="SENSITIVE_DATA_BIGQUERY_TABLE_CMEK_DISABLED" OR category="SENSITIVE_DATA_DATASET_CMEK_DISABLED" OR category="SENSITIVE_DATA_SQL_CMEK_DISABLED" OR category="PUBLIC_DATASET" OR category="PUBLIC_SQL_INSTANCE" OR category="SQL_PUBLIC_IP" OR category="ACCESS_TRANSPARENCY_DISABLED" OR category="ORG_POLICY_LOCATION_RESTRICTION" OR category="BUCKET_POLICY_ONLY_DISABLED" OR category="DATA_EXFILTRATION_BIG_QUERY" OR category="DATA_EXFILTRATION_BIG_QUERY_EXTRACTION" OR category="DATA_EXFILTRATION_BIG_QUERY_TO_GOOGLE_DRIVE"
         

  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab.

  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding.

  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.




### External Exposure

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Command Center External Exposure is a Google Cloud service that helps you manage and reduce your external attack surface through automated discovery and risk validation.

Because automated scanners can target internet-exposed assets within minutes, External Exposure proactively uncovers accidental exposures and shadow resources before attackers can discover and exploit them.

By analyzing your environment from an external perspective, the service attempts to confirm what is truly reachable from the internet and identifies which exposures are actually exploitable.

External Exposure continually scans for external-facing IP addresses, hostnames, domain names, and URLs across your Google Cloud environment. This feature uses network scanning to confirm which resources and applications are reachable from the public internet.

For each confirmed exposure, External Exposure does the following:

  * Traces and displays the Google Cloud network path for external load balancers, Google Cloud Armor policies, firewall rules, Private Service Connect, Cloud Interconnect, and backend services down to the exposed resource.

This resource can be a Compute Engine instance or a Google Kubernetes Engine (GKE) Pod, including an exposed service or application.

This deep integration with the Google networking fabric helps provide actionable context so you can immediately apply preventive mitigations, such as locking down a specific firewall rule or configuring Google Cloud Armor.

  * Performs fingerprinting to attempt to identify the specific web application or server software that is running on each exposed asset.

  * If it can identify the exposed service or software, identifies any vulnerabilities that are known to affect it.

  * Uses advanced passive and active detectors to test for real-world exploitability by validating vulnerabilities, misconfigurations, and use of default or weak credentials.




#### Review External Exposure findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **External Exposure**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### GKE security posture dashboard

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Google Kubernetes Engine (GKE) security posture dashboard is a page in the Google Cloud console that provides you with prescriptive and actionable findings about potential security issues in your GKE clusters.

The GKE security posture dashboard integrates with Security Command Center to provide the following benefits:

  * **Unified visibility:** View security findings for your GKE clusters alongside findings from other Security Command Center services in the Security Command Center console.
  * **Attack exposure scores:** Prioritize findings by viewing their potential impact on your environment through attack exposure scores.
  * **Compliance reporting:** Generate compliance reports based on the findings.



To see these findings, enable any of the following GKE security posture dashboard features:

GKE security posture dashboard pane | Security Command Center finding class  
---|---  
[Workload configuration auditing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning#what-checks)1 | `MISCONFIGURATION`  
Top threats2 | `THREAT`  
[Container OS vulnerability scanning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-workload-vulnerability-scanning#about-container-os-scanning)1 | `VULNERABILITY`  
[Language package vulnerability scanning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-workload-vulnerability-scanning#language-package-scanning)1 | `VULNERABILITY`  
[Actionable security bulletins](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-configuration-scanning#security-bulletins)1 ([Preview](https://cloud.google.com/products/#product-launch-stages))  | `VULNERABILITY`  
Top software vulnerabilities2 | `VULNERABILITY`  
  
  1. Available only if you enable this feature in GKE. 
  2. Available for Security Command Center Premium and Enterprise [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers). 



The findings display information about the security issue and provide recommendations to resolve them in your workloads or clusters.

**Important** : Security bulletin findings that are published in Security Command Center _don't_ include a `cve` field that lists the associated CVEs. To view the CVEs, check the finding's `description` field, or review the security bulletin in the security posture dashboard. 

#### View GKE security posture dashboard findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **GKE Security Posture**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### IAM recommender

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

[IAM recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) generates recommendations that you can follow to improve security by removing or replacing IAM roles from principals when the roles contain IAM permissions that the principal does not need.

IAM recommender is automatically enabled when you activate Security Command Center.

#### Enable or disable IAM recommender findings

To enable or disable IAM recommender findings in Security Command Center, follow these steps:

  1. Go to the **Integrated services** tab of the Security Command Center **Settings** page in the Google Cloud console:

[Go to Integrated Services](https://console.cloud.google.com/projectselector2/security/command-center/config/integrated-services?supportedpurview=organizationId)

  2. Go to the **IAM recommender** entry.

  3. To the right of the entry, select **Enable** or **Disable**.




Findings from IAM recommender are classified as vulnerabilities.

To remediate an IAM recommender finding, expand the following section to see a table of the IAM recommender findings. The remediation steps for each finding are included in the table entry.

#### IAM recommender detectors

Detector | Summary  
---|---  
  
#### `IAM role has excessive permissions`

Category name in the API: `IAM_ROLE_HAS_EXCESSIVE_PERMISSIONS` |  **Finding description** : IAM recommender detected a service account that has one or more IAM roles that give excessive permissions to the user account. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets** :

  * [ google.cloud.resourcemanager.Project](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#Project)
  * [ google.cloud.resourcemanager.Folder](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders#Folder)
  * [ google.cloud.resourcemanager.Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations#Organization)

**Fix this finding build**: Use IAM recommender to apply the recommended fix for this finding by following these steps:

  1. In the **Next steps** section of the finding details in the Google Cloud console, copy and paste the URL for the **IAM** page into a browser address bar and press `Enter`. The **IAM** page loads. 
  2. Near the top of the **IAM** page on the right side, click **View recommendations in table**. The recommendations are displayed in a table. 
  3. In the **Security insights** column, click any recommendation that relates to excess permissions. The recommendation details panel opens. 
  4. Review the recommendation for the actions that you can take to resolve the issue. 
  5. Click **Apply**.

After the issue is fixed, IAM recommender updates the status of the finding to `INACTIVE` within 10 days.  
  
#### `Service agent role replaced with basic role`

Category name in the API: `SERVICE_AGENT_ROLE_REPLACED_WITH_BASIC_ROLE` |  **Finding description** : IAM recommender detected that the original default IAM role granted to a service agent was replaced with one of the basic IAM roles: **Owner** , **Editor** , or **Viewer**. Basic roles are excessively permissive legacy roles and should not be granted to service agents. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets** :

  * [ google.cloud.resourcemanager.Project](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#Project)
  * [ google.cloud.resourcemanager.Folder](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders#Folder)
  * [ google.cloud.resourcemanager.Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations#Organization)

**Fix this finding build**: Use IAM recommender to apply the recommended fix for this finding by following these steps:

  1. In the **Next steps** section of the finding details in the Google Cloud console, copy and paste the URL for the **IAM** page into a browser address bar and press `Enter`. The **IAM** page loads. 
  2. Near the top of the **IAM** page on the right side, click **View recommendations in table**. The recommendations are displayed in a table. 
  3. In the **Security insights** column, click any permission that relates to excess permissions. The recommendation details panel opens. 
  4. Review the excess permissions.
  5. Click **Apply**.

After the issue is fixed, IAM recommender updates the status of the finding to `INACTIVE` within 10 days.  
  
#### `Service agent granted basic role`

Category name in the API: `SERVICE_AGENT_GRANTED_BASIC_ROLE` |  **Finding description** : IAM recommender detected IAM that a service agent was granted one of the basic IAM roles: **Owner** , **Editor** , or **Viewer**. Basic roles are excessively permissive legacy roles and should not be granted to service agents. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets** :

  * [ google.cloud.resourcemanager.Project](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#Project)
  * [ google.cloud.resourcemanager.Folder](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders#Folder)
  * [ google.cloud.resourcemanager.Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations#Organization)

**Fix this finding build**: Use IAM recommender to apply the recommended fix for this finding by following these steps:

  1. In the **Next steps** section of the finding details in the Google Cloud console, copy and paste the URL for the **IAM** page into a browser address bar and press `Enter`. The **IAM** page loads. 
  2. Near the top of the **IAM** page on the right side, click **View recommendations in table**. The recommendations are displayed in a table. 
  3. In the **Security insights** column, click any permission that relates to excess permissions. The recommendation details panel opens. 
  4. Review the excess permissions.
  5. Click **Apply**.

After the issue is fixed, IAM recommender updates the status of the finding to `INACTIVE` within 10 days.  
  
#### `Unused IAM role`

Category name in the API: `UNUSED_IAM_ROLE` |  **Finding description** : IAM recommender detected a user account that has an IAM role that has not been used in the last 90 days. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets** :

  * [ google.cloud.resourcemanager.Project](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#Project)
  * [ google.cloud.resourcemanager.Folder](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders#Folder)
  * [ google.cloud.resourcemanager.Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations#Organization)

**Fix this finding build**: Use IAM recommender to apply the recommended fix for this finding by following these steps:

  1. In the **Next steps** section of the finding details in the Google Cloud console, copy and paste the URL for the **IAM** page into a browser address bar and press `Enter`. The **IAM** page loads. 
  2. Near the top of the **IAM** page on the right side, click **View recommendations in table**. The recommendations are displayed in a table. 
  3. In the **Security insights** column, click any permission that relates to excess permissions. The recommendation details panel opens. 
  4. Review the excess permissions.
  5. Click **Apply**.

After the issue is fixed, IAM recommender updates the status of the finding to `INACTIVE` within 10 days.  
  
#### View IAM recommender findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **IAM Recommender**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



In Security Command Center Premium, you can also view the IAM recommender findings on the legacy [**Vulnerabilities**](https://console.cloud.google.com/security/command-center/vulnerabilities) page by selecting the **IAM recommender** query preset.

### Mandiant Attack Surface Management

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (not available if [data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) are enabled)

Mandiant is a world leader in frontline threat intelligence. Mandiant Attack Surface Management identifies vulnerabilities and misconfigurations in your external attack surfaces to help you stay up-to-date against the latest cyber attacks.

Mandiant Attack Surface Management is automatically enabled when you activate the Security Command Center Enterprise tier and findings are available in the Google Cloud console.

For information about how the standalone Mandiant Attack Surface Management product differs from the Mandiant Attack Surface Management integration within Security Command Center, see [ASM and Security Command Center](https://docs.mandiant.com/home/asm-scc) on the Mandiant documentation portal. This link requires Mandiant authentication.

#### Review Mandiant Attack Surface Management findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Mandiant Attack Surface Management**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



Neither Security Command Center nor Mandiant Attack Surface Management marks findings as resolved. Once you resolve an issue, you can manually mark the issue resolved. If it is not identified in the next Mandiant Attack Surface Management scan, it stays resolved.

### Model Armor findings

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Model Armor is a fully managed Google Cloud service that enhances the security and safety of AI applications by screening LLM prompts and responses.

Finding | Summary  
---|---  
  
#### `Floor settings violation`

Category name in the API: `FLOOR_SETTINGS_VIOLATION` |  **Finding description** : A floor setting violation that occurs when a Model Armor template fails to meet the minimum security standards defined by the resource hierarchy floor settings. **Finding class** : Misconfiguration **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) [ Fix this findingbuild](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#remediate-ma-findings): This finding requires that you update the Model Armor template to be in conformance with the floor settings defined at the resource hierarchy.   
  
### Notebook Security Scanner

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Notebook Security Scanner is a built-in package vulnerability detection service of Security Command Center. After Notebook Security Scanner is enabled, it automatically scans Colab Enterprise notebooks (files with the `ipynb` filename extension) every 24 hours to detect vulnerabilities in Python packages and publishes these findings to the Security Command Center **Findings** page.

You can use Notebook Security Scanner for Colab Enterprise notebooks that are created in the following regions: `us-central1`, `us-east4`, `us-west1`, and `europe-west4`.

To get started with Notebook Security Scanner, see [Enable and use Notebook Security Scanner](https://docs.cloud.google.com/security-command-center/docs/enable-notebook-security-scanner).

### Policy Controller

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

[Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview) enables the application and enforcement of programmable policies for your Kubernetes clusters. These policies act as _guardrails_ and can help with best practices, security, and compliance management of your clusters and fleet.

If you [install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller), and enable any of the [Policy Controller bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles), Policy Controller automatically writes cluster violations to Security Command Center as `Misconfiguration` class findings. The finding description and next steps in the Security Command Center findings are the same as the constraint description and remediation steps of the corresponding Policy Controller bundle.

The Policy Controller findings come from the following Policy Controller bundles:

  * [CIS Kubernetes Benchmark v.1.5.1](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-k8s-benchmark), a set of recommendations for configuring Kubernetes to support a strong security posture. You can also view information about this bundle in the [GitHub repository for `cis-k8s-v1.5.1`](https://github.com/GoogleCloudPlatform/acm-policy-controller-library/tree/main/bundles/cis-k8s-v1.5.1).
  * [PCI-DSS v3.2.1](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pci-dss-v3), a bundle that evaluates the compliance of your cluster resources against some aspects of the Payment Card Industry Data Security Standard (PCI-DSS) v3.2.1. You can also view information about this bundle in the [GitHub repository for `pci-dss-v3`](https://github.com/GoogleCloudPlatform/acm-policy-controller-library/tree/main/anthos-bundles/pci-dss-v3.2.1).



To find and remediate Policy Controller findings, see [Remediating Policy Controller findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#policy-controller-findings).

### Risk Engine

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Security Command Center Risk Engine assesses the risk exposure of your cloud deployments, assigns attack exposure scores to vulnerability findings and your high-value resources, and diagrams paths that a potential attacker could take to reach your high-value resources.

In the Enterprise or Premium tier of Security Command Center, the Risk Engine detects groups of security issues that, when they occur together in a particular pattern, create a path to one or more of your high-value resources that a determined attacker could potentially use to reach and compromise those resources.

When Risk Engine detects one of these combinations, it generates a `TOXIC_COMBINATION` class finding. In the finding, Risk Engine is listed as the source of the finding.

Risk Engine also identifies common resources or resource groups where multiple attack paths converge, and then generates a `CHOKEPOINT` class finding.

For more information, see [Toxic combinations and chokepoints overview](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview).

### Security Health Analytics

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Health Analytics is a built-in detection service of Security Command Center that provides managed scans of your cloud resources to detect common misconfigurations.

When a misconfiguration is detected, Security Health Analytics generates a finding. Most Security Health Analytics findings are mapped to security standard controls so that you can assess compliance.

Security Health Analytics scans your resources on Google Cloud. If you are using the Enterprise tier and establish connections to other cloud platforms, Security Health Analytics can also scan your resources on those cloud platforms.

Depending on the Security Command Center [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) you are using, the available detectors differ:

  * In the Standard-legacy tier, Security Health Analytics includes only a basic group of medium-severity and high-severity vulnerability detectors.
  * The Premium tier includes all vulnerability detectors for Google Cloud.
  * The Enterprise tier includes additional detectors for other cloud platforms.



Security Health Analytics is automatically enabled when you activate Security Command Center.

For more information, see the following:

  * [Security Health Analytics overview](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics)
  * [How to use Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics)
  * [Remediating Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings)
  * [Reference of Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors)



### Security posture service

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The [security posture service](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview) is a built-in service for the Security Command Center Premium tier that lets you define, assess, and monitor the overall status of your security in Google Cloud. It provides information about how your environment aligns with the policies that you define in your security posture.

The security posture service isn't related to the _GKE security posture dashboard_ , which only shows findings in GKE clusters.

#### Security posture service findings

Finding | Summary  
---|---  
  
#### `SHA Canned Module Drifted`

Category name in the API: `SECURITY_POSTURE_DETECTOR_DRIFT` |  **Finding description** : The security posture service detected a change to a Security Health Analytics detector that occurred outside of a posture update. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Fix this finding build**: This finding requires that you accept the change or revert the change so that the detector settings in your posture and your environment match. You have two options to resolve this finding: you can update the Security Health Analytics detector or you can update the posture and posture deployment. To revert the change, update the Security Health Analytics detector in the Google Cloud console. For instructions, see [ Enable and disable detectors](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#enable_and_disable_detectors). To accept the change, complete the following:

  1. Update the `posture.yaml` file with the change.
  2. Run the `gcloud scc postures update` command. For instructions, see [ Update the policy definitions in a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture). 
  3. Deploy the updated posture with the new revision ID. For instructions, see [ Update a posture deployment](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture-deployment). 

  
  
#### `SHA Custom Module Drifted`

Category name in the API: `SECURITY_POSTURE_DETECTOR_DRIFT` |  **Finding description** : The security posture service detected a change to a Security Health Analytics custom module that occurred outside of a posture update. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Fix this finding build**: This finding requires that you accept the change or revert the change so that the custom module settings in your posture and your environment match. You have two options to resolve this finding: you can update the Security Health Analytics custom module or you can update the posture and posture deployment. To revert the change, update the Security Health Analytics custom module in the Google Cloud console. For instructions, see [ Update a custom module](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create#update_a_custom_module). To accept the change, complete the following:

  1. Update the `posture.yaml` file with the change.
  2. Run the `gcloud scc postures update` command. For instructions, see [ Update the policy definitions in a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture). 
  3. Deploy the updated posture with the new revision ID. For instructions, see [ Update a posture deployment](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture-deployment). 

  
  
#### `SHA Custom Module Deleted`

Category name in the API: `SECURITY_POSTURE_DETECTOR_DELETE` |  **Finding description** : The security posture service detected that a Security Health Analytics custom module was deleted. This deletion occurred outside of a posture update. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Fix this finding build**: This finding requires that you accept the change or revert the change so that the custom module settings in your posture and your environment match. You have two options to resolve this finding: you can update the Security Health Analytics custom module or you can update the posture and posture deployment. To revert the change, update the Security Health Analytics custom module in the Google Cloud console. For instructions, see [ Update a custom module](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create#update_a_custom_module). To accept the change, complete the following:

  1. Update the `posture.yaml` file with the change.
  2. Run the `gcloud scc postures update` command. For instructions, see [ Update the policy definitions in a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture). 
  3. Deploy the updated posture with the new revision ID. For instructions, see [ Update a posture deployment](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture-deployment). 

  
  
#### `Org Policy Canned Constraint Drifted`

Category name in the API: `SECURITY_POSTURE_POLICY_DRIFT` |  **Finding description** : The security posture service detected a change to an organization policy that occurred outside of a posture update. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Fix this finding build**: This finding requires that you accept the change or revert the change so that the organization policy definitions in your posture and your environment match. You have two options to resolve this finding: you can update the organization policy or you can update the posture and posture deployment. To revert the change, update the organization policy in the Google Cloud console. For instructions, see [ Creating and editing policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies). To accept the change, complete the following:

  1. Update the `posture.yaml` file with the change.
  2. Run the `gcloud scc postures update` command. For instructions, see [ Update the policy definitions in a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture). 
  3. Deploy the updated posture with the new revision ID. For instructions, see [ Update a posture deployment](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture-deployment). 

  
  
#### `Org Policy Canned Constraint Deleted`

Category name in the API: `SECURITY_POSTURE_POLICY_DELETE` |  **Finding description** : The security posture service detected that an organization policy was deleted. This deletion occurred outside of a posture update. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Fix this finding build**: This finding requires that you accept the change or revert the change so that the organization policy definitions in your posture and your environment match. You have two options to resolve this finding: you can update the organization policy or you can update the posture and posture deployment. To revert the change, update the organization policy in the Google Cloud console. For instructions, see [ Creating and editing policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies). To accept the change, complete the following:

  1. Update the `posture.yaml` file with the change.
  2. Run the `gcloud scc postures update` command. For instructions, see [ Update the policy definitions in a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture). 
  3. Deploy the updated posture with the new revision ID. For instructions, see [ Update a posture deployment](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture-deployment). 

  
  
#### `Org Policy Custom Constraint Drifted`

Category name in the API: `SECURITY_POSTURE_POLICY_DRIFT` |  **Finding description** : The security posture service detected a change to a custom organization policy that occurred outside of a posture update. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Fix this finding build**: This finding requires that you accept the change or revert the change so that the custom organization policy definitions in your posture and your environment match. You have two options to resolve this finding: you can update the custom organization policy or you can update the posture and posture deployment. To revert the change, update the custom organization policy in the Google Cloud console. For instructions, see [ Update a custom constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#update_custom_constraint). To accept the change, complete the following:

  1. Update the `posture.yaml` file with the change.
  2. Run the `gcloud scc postures update` command. For instructions, see [ Update the policy definitions in a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture). 
  3. Deploy the updated posture with the new revision ID. For instructions, see [ Update a posture deployment](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture-deployment). 

  
  
#### `Org Policy Custom Constraint Deleted`

Category name in the API: `SECURITY_POSTURE_POLICY_DELETE` |  **Finding description** : The security posture service detected that a custom organization policy was deleted. This deletion occurred outside of a posture update. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Fix this finding build**: This finding requires that you accept the change or revert the change so that the custom organization policy definitions in your posture and your environment match. You have two options to resolve this finding: you can update the custom organization policy or you can update the posture and posture deployment. To revert the change, update the custom organization policy in the Google Cloud console. For instructions, see [ Update a custom constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#update_custom_constraint). To accept the change, complete the following:

  1. Update the `posture.yaml` file with the change.
  2. Run the `gcloud scc postures update` command. For instructions, see [ Update the policy definitions in a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture). 
  3. Deploy the updated posture with the new revision ID. For instructions, see [ Update a posture deployment](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#update-posture-deployment). 

  
  
### Sensitive Data Protection

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Sensitive Data Protection is a fully managed Google Cloud service that helps you discover, classify, and protect your sensitive data. You can use Sensitive Data Protection to determine whether you're storing sensitive or personally identifiable information (PII), like the following:

  * Person names
  * Credit card numbers
  * National or state ID numbers
  * Health insurance ID numbers
  * Secrets



In Sensitive Data Protection, each type of sensitive data that you search for is called an [_infoType_](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes).

If you configure your Sensitive Data Protection operation to send results to Security Command Center, you can see the findings directly in the Security Command Center section of the Google Cloud console, in addition to the Sensitive Data Protection section.

If you use VPC Service Controls service perimeters and you want to discover sensitive data within those perimeters, see [Allow sensitive data discovery within service perimeters](https://docs.cloud.google.com/sensitive-data-protection/docs/allow-discovery-vpcsc). If you don't perform this task, you might receive warnings.

#### Sensitive Data Protection scan latency

Depending on the size of your organization, Sensitive Data Protection findings can start appearing in Security Command Center within a few minutes after you enable sensitive data discovery. For larger organizations or organizations with specific configurations that affect finding generation, it can take up to 12 hours before initial findings appear in Security Command Center.

Subsequently, Sensitive Data Protection generates findings in Security Command Center within a few minutes after the discovery service scans your resources.

#### Vulnerability findings from the Sensitive Data Protection discovery service

The Sensitive Data Protection discovery service helps you determine whether you are storing highly sensitive data that is not protected.

Category | Summary  
---|---  
  
#### `Public sensitive data`

Category name in the API: `PUBLIC_SENSITIVE_DATA` |  **Finding description** : The specified resource has [ high-sensitivity data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#sensitivity-level) that can be accessed by anyone on the internet. **Note:** Sensitive Data Protection might produce a data access audit log entry when analyzing (_profiling_) a tuning job within a Cloud Storage bucket. The action is performed by an internal Sensitive Data Protection service account. **Supported assets** :

  * `aiplatform.googleapis.com/Dataset`
  * `aiplatform.googleapis.com/TuningJob`
  * `bigquery.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Table`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`
  * Amazon S3 bucket
  * Azure Blob Storage container

**Remediation** : For Google Cloud data, remove `allUsers` and `allAuthenticatedUsers` from the data asset's IAM policy. For Amazon S3 data, configure block public access settings or update the object's ACL to deny public read access. For more information, see [ Configuring block public access settings for your S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html) and [Configuring ACLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/managing-acls.html) in the AWS documentation. For Azure Blob Storage data, remove public access to the container and the blobs. For more information, see [Overview: Remediating anonymous read access for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-overview) in the Azure documentation. **Compliance standards** : Not mapped  
  
#### `Secrets in environment variables`

Category name in the API: `SECRETS_IN_ENVIRONMENT_VARIABLES` |  **Finding description** : There are [ secrets](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets)—such as passwords, authentication tokens, and Google Cloud credentials—in environment variables. To enable this detector, see [ Report secrets in environment variables to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/secrets-discovery) in the Sensitive Data Protection documentation. **Supported assets** : 

  * [ `cloudfunctions.googleapis.com/CloudFunction` ](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions)
  * [ `run.googleapis.com/Revision` ](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services.revisions)

**Remediation** : For Cloud Run functions environment variables, remove the secret from the environment variable and [store it in Secret Manager](https://docs.cloud.google.com/functions/docs/configuring/secrets) instead. For Cloud Run service revision environment variables, move all traffic off of the revision, and then delete the revision. **Compliance standards** :

  * **CIS GCP Foundation 1.3** : 1.18
  * **CIS GCP Foundation 2.0** : 1.18

  
  
#### `Secrets in storage`

Category name in the API: `SECRETS_IN_STORAGE` |  **Finding description** : There are [ secrets](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets)—such as passwords, authentication tokens, and cloud credentials—in the specified resource. **Supported assets** :

  * `aiplatform.googleapis.com/Dataset`
  * `aiplatform.googleapis.com/TuningJob`
  * `bigquery.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Table`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`
  * Amazon S3 bucket
  * Azure Blob Storage container

**Remediation** :

  1. For Google Cloud data, use Sensitive Data Protection to [ run a deep inspection scan of the specified resource](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage) to identify all affected resources. For Cloud SQL data, export that data to a CSV or AVRO file in a Cloud Storage bucket and run a deep inspection scan of the bucket. For data from other cloud providers, manually inspect the specified bucket or container.
  2. Remove the detected secrets.
  3. Consider resetting the credentials.
  4. For Google Cloud data, consider storing the detected secrets in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) instead. 

**Compliance standards** : Not mapped  
  
#### Misconfiguration findings from the Sensitive Data Protection discovery service

The Sensitive Data Protection discovery service helps you determine whether you have misconfigurations that might expose sensitive data.

Category | Summary  
---|---  
  
#### `Sensitive data CMEK disabled`

Category name in the API: `SENSITIVE_DATA_CMEK_DISABLED` |  **Finding description** : The specified resource has [ high-sensitivity or moderate-sensitivity data](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#sensitivity-level) and the resource isn't using a customer-managed encryption key (CMEK). **Supported assets** :

  * `aiplatform.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Table`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`
  * Amazon S3 bucket
  * Azure Blob Storage container

**Remediation** :

  * For BigQuery data, [use CMEK on the table or dataset](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption).
  * For Cloud SQL data, see the CMEK documentation for [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/cmek) or [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/cmek).
  * For Cloud Storage data, [use CMEK on the bucket](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).

**Compliance standards** : Not mapped  
  
#### Observation findings from Sensitive Data Protection

This section describes the observation findings that Sensitive Data Protection generates in Security Command Center.

The Sensitive Data Protection discovery service helps you determine whether your data contains specific infoTypes and where they reside in your organization, folders, and projects. It generates the following observation finding categories in Security Command Center: 

Category | Summary  
---|---  
  
#### `Data sensitivity`

Category name in the API: `DATA_SENSITIVITY` |  **Finding description** : An indication of the sensitivity level of the data in a particular data asset. Data is sensitive if it contains PII or other elements that might require additional control or management. The severity of the finding is the [sensitivity level that Sensitive Data Protection calculated](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#sensitivity-level) when generating the data profile.  
  
#### `Data risk`

Category name in the API: `DATA_RISK` |  **Finding description** : The risk associated with the data in its current state. When calculating data risk, Sensitive Data Protection considers the sensitivity level of the data in the data asset and the presence of access controls to protect that data. The severity of the finding is the [data risk level that Sensitive Data Protection calculated](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#data-risk) when generating the data profile.  
  
For information about how to send data profile results to Security Command Center, see [Enable sensitive data discovery](https://docs.cloud.google.com/security-command-center/docs/activate-sensitive-data-discovery).

##### Observation findings from the Sensitive Data Protection inspection service

A Sensitive Data Protection inspection job identifies each instance of data of a specific infoType in a storage system like a Cloud Storage bucket or a BigQuery table. For example, you can run an inspection job that searches for all strings that match the `CREDIT_CARD_NUMBER` infoType detector in a Cloud Storage bucket.

For each infoType detector that has one or more matches, Sensitive Data Protection generates a corresponding Security Command Center finding. The finding category is the name of the infoType detector that had a match—for example, `Credit card number`. The finding includes the number of matching strings that were detected in text or images in the resource.

For security reasons, the actual strings that were detected aren't included in the finding. For example, a `Credit card number` finding shows how many credit card numbers were found, but doesn't show the actual credit card numbers.

Because there are more than 150 built-in infoType detectors in Sensitive Data Protection, all possible Security Command Center finding categories aren't listed here. For a full list of infoType detectors, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

For information on how to send the results of an inspection job to Security Command Center, see [Send Sensitive Data Protection inspection job results to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-cscc).

#### Review Sensitive Data Protection findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Sensitive Data Protection**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### VM Manager

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

[VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) is a suite of tools that can be used to manage operating systems for large virtual machine (VM) fleets running Windows and Linux on Compute Engine.

To use VM Manager with [project-level activations](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#project-level-activation-overview) of Security Command Center Premium, activate the Security Command Center Standard-legacy tier in the parent organization.

If you [enable VM Manager](https://docs.cloud.google.com/compute/docs/manage-os) with the Security Command Center Premium tier, VM Manager automatically writes `high` and `critical` findings from its [vulnerability reports](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management#vulnerability-reports), which are in preview, to Security Command Center. The reports identify vulnerabilities in operating systems (OS) that are installed on VMs, including [Common Vulnerabilities and Exposures (CVEs)](https://wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures).

Vulnerability reports are not available for the Security Command Center Standard-legacy tier.

Findings simplify the process of using VM Manager's Patch Compliance feature ([Preview](https://cloud.google.com/products/#product-launch-stages)). When integrated with the Security Command Center Premium tier, the feature enables organization-level visibility and [patch management](https://docs.cloud.google.com/compute/docs/os-patch-management) across all your projects. Although individual patch jobs are configured within VM Manager at the project level, Security Command Center provides a consolidated view that helps you manage patch jobs across your organization.

To remediate VM Manager findings, see [Remediating VM Manager findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#remediate_reports).

To stop vulnerability reports from being written to Security Command Center, see [Mute VM Manager findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#disable_reports).

Vulnerabilities of this type all relate to installed operating system packages in supported Compute Engine VMs.

Detector | Summary | Asset scan settings  
---|---|---  
  
#### `OS vulnerability`

Category name in the API: `OS_VULNERABILITY` |  **Finding description** : VM Manager detected a vulnerability in the installed operating system (OS) package for a Compute Engine VM. **Pricing tier** : [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets** [ compute.googleapis.com/Instance](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances) Fix this finding build |  VM Manager's [ vulnerability reports](https://docs.cloud.google.com/compute/docs/instances/os-inventory-management#vulnerability-reports) detail vulnerabilities in installed operating system packages for Compute Engine VMs, including [ Common Vulnerabilities and Exposures (CVEs)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures). For a complete list of supported operating systems, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager). Findings appear in Security Command Center shortly after vulnerabilities are detected. Vulnerability reports in VM Manager are generated as follows:

  * When a package is installed or updated in a VM's operating system, you can expect to see [ Common Vulnerabilities and Exposures (CVEs)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) information for the VM in Security Command Center within two hours after the change. 
  * When new security advisories are published for an operating system, updated CVEs are normally available within 24 hours after the operating system vendor publishes the advisory. 

  
  
### Vulnerability Assessment for AWS

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Vulnerability Assessment for Amazon Web Services (AWS) service detects software vulnerabilities in your workloads that are running on EC2 virtual machines (VMs) on the AWS cloud platform.

For each detected vulnerability, Vulnerability Assessment for AWS generates a `Vulnerability` class finding in the `Software vulnerability` finding category in Security Command Center.

The Vulnerability Assessment for AWS service scans snapshots of the running EC2 machine instances, so production workloads are unaffected. This scan method is called _agentless disk scanning_ , because no agents are installed on the scan targets.

For more information, see the following:

  * [Overview of Vulnerability Assessment for AWS](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview)
  * [Enable and use Vulnerability Assessment for AWS](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-enable)



### Vulnerability Assessment for Google Cloud

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Vulnerability Assessment for Google Cloud service detects software vulnerabilities in the following resources on the Google Cloud platform:

  * Running Compute Engine VM instances
  * Nodes in [GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison) clusters
  * Containers running in GKE Standard and GKE Autopilot clusters



For each detected vulnerability, Vulnerability Assessment for Google Cloud generates a `Vulnerability` class finding in the `Software vulnerability` or `OS vulnerability` finding category in Security Command Center.

The Vulnerability Assessment for Google Cloud service scans your Compute Engine VM instances by cloning their disks approximately every 12 hours, mounting them in a secure VM instance, and assessing them with the [SCALIBR](https://github.com/google/osv-scalibr) scanner.

For more information, see [Vulnerability Assessment for Google Cloud](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-google-cloud).

### Web Security Scanner

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

[Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) provides managed and custom web vulnerability scanning for public App Engine, GKE, and Compute Engine serviced web applications.

#### Managed scans

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Web Security Scanner managed scans are configured and managed by Security Command Center. Managed scans automatically run once each week to detect and scan public web endpoints. These scans don't use authentication and they send GET-only requests so they don't submit any forms on live websites.

Managed scans run separately from custom scans.

If Security Command Center is activated at the [organization level](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation), you can use managed scans to centrally manage basic web application vulnerability detection for projects in your organization, without having to involve individual project teams. When findings are discovered, you can work with those teams to set up more comprehensive custom scans.

When you enable Web Security Scanner as a service, managed scan findings are automatically available in the Security Command Center **Vulnerabilities** page and related reports. For information about how to enable Web Security Scanner managed scans, see [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).

Managed scans support only applications that use the default port, which is 80 for HTTP connections and 443 for HTTPS connections. If your application uses a non-default port, do a custom scan instead.

#### Custom scans

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Web Security Scanner custom scans provide granular information about application vulnerability findings, like outdated libraries, cross-site scripting, or use of mixed content.

You define custom scans at the project level.

Custom scan findings are available in Security Command Center after you complete the guide to [set up Web Security Scanner custom scans](https://docs.cloud.google.com/security-command-center/docs/how-to-web-security-scanner-custom-scans).

#### Detectors and compliance

Web Security Scanner supports categories in the [OWASP Top Ten](https://owasp.org/www-project-top-ten/), a document that ranks and provides remediation guidance for the top 10 most critical web application security risks, as determined by the Open Web Application Security Project (OWASP). For guidance on mitigating OWASP risks, see [Mitigate OWASP Top 10:2025 on Google Cloud](https://docs.cloud.google.com/docs/security/owasp-top-ten-mitigation).

**Note:** The category [A09:2021 Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/) (previously **A10:2017 Insufficient Logging & Monitoring**) is not supported. This category describes insufficiencies that allow attackers to remain undetected. Unlike the other nine OWASP categories, it doesn't pertain to specific vulnerabilities that attackers can exploit. Similarly, Web Security Scanner can't attack web applications to provoke a detectable response. The issues included in this category require human judgment.

The compliance mapping is included for reference and is not provided or reviewed by the OWASP Foundation.

This functionality is only intended for you to monitor for compliance control violations. The mappings are not provided for use as the basis of, or as a substitute for, the audit, certification, or report of compliance of your products or services with any regulatory or industry benchmarks or standards.

For more information, see [Web Security Scanner Overview](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview).

## Threat detection services

Threat detection services include built-in and integrated services that detect events that might indicate potentially harmful events, such as compromised resources or cyberattacks.

### Agent Platform Threat Detection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Agent Platform Threat Detection provides runtime threat detection for agents deployed to Agent Runtime. It monitors running agents for potential attacks and generates findings in Security Command Center.

Agent Platform Threat Detection can generate findings for Agent Runtime including the following categories:

  * **Command and Control** : Steganography Tool Detected
  * **Credential Access** : Find Google Cloud Credentials
  * **Credential Access** : GPG Key Reconnaissance
  * **Credential Access** : Search Private Keys or Passwords
  * **Defense Evasion** : Base64 ELF File Command Line
  * **Defense Evasion** : Base64 Encoded Python Script Executed
  * **Defense Evasion** : Base64 Encoded Shell Script Executed
  * **Defense Evasion** : Launch Code Compiler Tool In Container
  * **Execution** : Netcat Remote Code Execution in Container
  * **Execution** : Possible Arbitrary Command Execution through CUPS (CVE-2024-47177)
  * **Execution** : Possible Remote Command Execution Detected
  * **Execution** : Program Run with Disallowed HTTP Proxy Env
  * **Execution** : Socat Reverse Shell Detected
  * **Execution** : Suspicious OpenSSL Shared Object Loaded
  * **Exfiltration** : Launch Remote File Copy Tools in Container
  * **Impact** : Detect Malicious Cmdlines
  * **Impact** : Remove Bulk Data from Disk
  * **Impact** : Suspicious crypto mining activity using the Stratum Protocol
  * **Privilege Escalation** : Abuse of Sudo For Privilege Escalation (CVE-2019-14287)
  * **Privilege Escalation** : Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)
  * **Privilege Escalation** : Sudo Potential Privilege Escalation (CVE-2021-3156)
  * **Execution** : Malicious Python executed
  * **Execution** : Container Escape
  * **Execution** : Kubernetes Attack Tool Execution
  * **Execution** : Local Reconnaissance Tool Execution
  * **Impact** : Malicious Script Executed
  * **Impact** : Malicious URL Observed
  * **Execution** : Unexpected Child Shell



To learn more, see [Agent Platform Threat Detection](https://docs.cloud.google.com/security-command-center/docs/agent-platform-threat-detection-overview).

### Anomaly Detection

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Anomaly Detection is a built-in service that uses behavior signals from _outside_ your system. It displays granular information about security anomalies detected for your service accounts, such as potential leaked credentials. Anomaly Detection is automatically enabled when you activate Security Command Center Standard-legacy or Premium tier, and findings are available in the Google Cloud console.

Anomaly Detection findings include the following:

Anomaly name | Finding category | Description  
---|---|---  
  
#### `Account has leaked credentials`

| `account_has_leaked_credentials` |  Credentials for a Google Cloud service account are accidentally leaked online or are compromised. **Severity:** Critical  
  
#### Account has leaked credentials

GitHub notified Security Command Center that the credentials that were used for a commit appear to be the credentials for a Google Cloud Identity and Access Management service account.

The notification includes the service account name and the private key identifier. Google Cloud also sends your [designated contact for security and privacy](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) issues a notification by email.

To remediate this issue, take one or more of the following actions:

  * Identify the legitimate user of the key.
  * Rotate the key.
  * Remove the key.
  * Investigate any actions that were taken by the key after the key was leaked to ensure that none of the actions were malicious.



#### JSON: leaked account credentials finding
    
    
    {
      "findings": {
        "access": {},
        "assetDisplayName": "PROJECT_NAME",
        "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
        "canonicalName": "projects/PROJECT_ID/sources/SOURCE_INSTANCE_ID/findings/FINDING_ID",
        "category": "account_has_leaked_credentials",
        "contacts": {
          "security": {
            "contacts": [
              {
                "email": "EMAIL_ADDRESS"
              }
            ]
          }
        },
        "createTime": "2022-08-05T20:59:41.022Z",
        "database": {},
        "eventTime": "2022-08-05T20:59:40Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/cat",
        "indicator": {},
        "kubernetes": {},
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_INSTANCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_INSTANCE_ID",
        "parentDisplayName": "Cloud Anomaly Detection",
        "resourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "severity": "CRITICAL",
        "sourceDisplayName": "Cloud Anomaly Detection",
        "state": "ACTIVE",
        "vulnerability": {},
        "workflowState": "NEW"
      },
      "resource": {
        "name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "display_name": "PROJECT_NAME",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "project_display_name": "PROJECT_NAME",
        "parent_name": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
        "parent_display_name": "ORGANIZATION_NAME",
        "type": "google.cloud.resourcemanager.Project",
        "folders": []
      },
      "sourceProperties": {
        "project_identifier": "PROJECT_ID",
        "compromised_account": "SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com",
        "finding_type": "Potential compromise of a resource in your organization.",
        "summary_message": "We have detected leaked Service Account authentication credentials that could be potentially compromised.",
        "action_taken": "Notification sent",
        "private_key_identifier": "SERVICE_ACCOUNT_KEY_ID",
        "url": "https://github.com/KEY_FILE_PATH/KEY_FILE_NAME.json"
      }
    }
        

### Container Threat Detection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Container Threat Detection can detect the most common container runtime attacks and alert you in Security Command Center and optionally in Cloud Logging. Container Threat Detection includes several detection capabilities, an analysis tool, and an API.

Container Threat Detection detection instrumentation collects low-level behavior in the guest kernel and performs natural language processing on code to detect the following events:

  * `Added Binary Executed`
  * `Added Library Loaded`
  * `Command and Control: Steganography Tool Detected` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Credential Access: Find Google Cloud Credentials`
  * `Credential Access: GPG Key Reconnaissance`
  * `Credential Access: Search Private Keys or Passwords`
  * `Defense Evasion: Base64 ELF File Command Line`
  * `Defense Evasion: Base64 Encoded Python Script Executed`
  * `Defense Evasion: Base64 Encoded Shell Script Executed`
  * `Defense Evasion: Launch Code Compiler Tool In Container` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Execution: Added Malicious Binary Executed`
  * `Execution: Added Malicious Library Loaded`
  * `Execution: Built in Malicious Binary Executed`
  * `Execution: Container Escape`
  * `Execution: Fileless Execution in /memfd:`
  * `Execution: Ingress Nightmare Vulnerability Execution` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Execution: Kubernetes Attack Tool Execution`
  * `Execution: Local Reconnaissance Tool Execution`
  * `Execution: Malicious Python executed`
  * `Execution: Modified Malicious Binary Executed`
  * `Execution: Modified Malicious Library Loaded`
  * `Execution: Netcat Remote Code Execution In Container`
  * `Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)`
  * `Execution: Possible Remote Command Execution Detected` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Execution: Program Run with Disallowed HTTP Proxy Env`
  * `Execution: Socat Reverse Shell Detected`
  * `Execution: Suspicious OpenSSL Shared Object Loaded`
  * `Exfiltration: Launch Remote File Copy Tools in Container`
  * `Impact: Detect Malicious Cmdlines` ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * `Impact: Remove Bulk Data From Disk`
  * `Impact: Suspicious crypto mining activity using the Stratum Protocol`
  * `Malicious Script Executed`
  * `Malicious URL Observed`
  * `Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)`
  * `Privilege Escalation: Fileless Execution in /dev/shm`
  * `Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)`
  * `Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)`
  * `Reverse Shell`
  * `Unexpected Child Shell`



[Learn more about Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).

### Event Threat Detection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Event Threat Detection uses log data from _inside_ your systems. It watches the Cloud Logging stream for projects, and consumes logs as they become available. When a threat is detected, Event Threat Detection writes a finding to Security Command Center and to a Cloud Logging project. Event Threat Detection is automatically enabled when you activate the Security Command Center and findings are available in the Google Cloud console.

#### Event Threat Detection detectors

  * [ `Active Scan: Log4j Vulnerable to RCE`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/log4j-active-scan-success)
  * [ `Brute force SSH`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ssh-brute-force)
  * [ `Cloud IDS: THREAT_IDENTIFIER`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-ids-threat-activity)
  * [ `Command and Control: DNS Tunneling`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-dns-tunneling)
  * [ `Credential Access: AI Agent Anomalous Access to Metadata Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-anomalous-access-to-metadata-service)
  * [ `Credential Access: CloudDB Failed login from Anonymizing Proxy IP`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-db-login-failed-anon-ip)
  * [ `Credential Access: Failed Attempt to Approve Kubernetes Certificate Signing Request (CSR)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-approve-csr-forbidden)
  * [ `Credential Access: Manually Approved Kubernetes Certificate Signing Request (CSR)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-csr-approved)
  * [ `Credential Access: Secrets Accessed In Kubernetes Namespace`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/secrets-accessed-in-kubernetes-namespace)
  * [ `Defense Evasion: Anonymous Sessions Granted Cluster Admin Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-anonymous-sessions-granted-cluster-admin)
  * [ `Defense Evasion: Breakglass Workload Deployment Created`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/binary-authorization-breakglass-workload-create)
  * [ `Defense Evasion: Breakglass Workload Deployment Updated`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/binary-authorization-breakglass-workload-update)
  * [ `Defense Evasion: Folder Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-folder)
  * [ `Defense Evasion: Folder level TokenCreatorRole Added`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/folder-level-service-account-tokencreatorrole-added)
  * [ `Defense Evasion: GCS Bucket IP Filtering Modified`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gcs-bucket-ip-filtering-modified)
  * [ `Defense Evasion: Manually Deleted Certificate Signing Request (CSR)`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-manually-deleted-csr)
  * [ `Defense Evasion: Modify VPC Service Control`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/vpcsc-change-reduces-perimeter-protection)
  * [ `Defense Evasion: Organization Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-org)
  * [ `Defense Evasion: Organization level TokenCreatorRole Added`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/org-level-service-account-tokencreatorrole-added)
  * [ `Defense Evasion: Potential Kubernetes Pod Masquerading`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-pod-masquerading)
  * [ `Defense Evasion: Project HTTP Policy Block Disabled`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/project-http-policy-block-disabled)
  * [ `Defense Evasion: Project Level TokenCreator Role Granted to AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-granted-token-creator-role-project)
  * [ `Defense Evasion: Project level TokenCreatorRole Added`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/project-level-service-account-tokencreatorrole-added)
  * [ `Defense Evasion: Static Pod Created`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-static-pod-created)
  * [ `Defense Evasion: VPC Route Masquerade Attempt`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-vpc-route-masquerade)
  * [ `Discovery: AI Agent Service Account Self-Investigation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-iam-anomalous-behavior-service-account-gets-own-iam-policy)
  * [ `Discovery: AI Agent Unauthorized Service Account API Call`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-unauthorized-service-account-api-call)
  * [ `Discovery: Can get sensitive Kubernetes object check`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-can-get-sensitive-object)
  * [ `Discovery: Evidence of Port Scanning from AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-port-scanning-evidence)
  * [ `Discovery: Information Gathering Tool Used`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-information-gathering-tool-used)
  * [ `Discovery: Service Account Self-Investigation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-behavior-service-account-gets-own-iam-policy)
  * [ `Discovery: Unauthorized Service Account API Call`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-unauthorized-service-account-api-call)
  * [ `Evasion: Access from Anonymizing Proxy`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-ip-google-proxy-intel)
  * [ `Execution: Cryptomining Docker Image`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-run-cryptomining-docker-images)
  * [ `Execution: GKE launch excessively capable container`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-excessively-capable-container-created)
  * [ `Execution: Kubernetes Pod Created with Potential Reverse Shell Arguments`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-reverse-shell-pod)
  * [ `Execution: Suspicious Exec or Attach to a System Pod`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-suspicious-exec-attach)
  * [ `Execution: Workload triggered in sensitive namespace`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-sensitive-namespace-workload-triggered)
  * [ `Exfiltration: AI Agent Initiated BigQuery Data Exfiltration to External Table`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-exfil)
  * [ `Exfiltration: AI Agent Initiated BigQuery Data Extraction`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-exfil-to-cloud-storage)
  * [ `Exfiltration: AI Agent Initiated BigQuery VPC Perimeter Violation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-big-query-vpc-violation)
  * [ `Exfiltration: AI Agent Initiated CloudSQL Exfiltration to External Bucket`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-cloudsql-exfil-export-external)
  * [ `Exfiltration: AI Agent Initiated CloudSQL Exfiltration to Public Bucket`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-cloudsql-exfil-export-public)
  * [ `Exfiltration: BigQuery Data Exfiltration`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil)
  * [ `Exfiltration: BigQuery Data Extraction`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil-to-cloud-storage)
  * [ `Exfiltration: BigQuery Data to Google Drive`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil-to-google-drive)
  * [ `Exfiltration: Cloud SQL Data Exfiltration`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-exfil-export)
  * [ `Exfiltration: Cloud SQL Over-Privileged Grant`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-exfil-user-granted-all-permissions)
  * [ `Exfiltration: Cloud SQL Restore Backup to External Organization`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-exfil-restore-backup-to-external-instance)
  * [ `Exfiltration: Move to Public BigQuery resource`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/big-query-exfil-to-public-dataset)
  * [ `Impact: Billing Disabled`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-billing-disabled-multiple-projects)
  * [ `Impact: Billing Disabled`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-billing-disabled-single-project)
  * [ `Impact: Cryptomining Commands`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-run-jobs-cryptomining-commands)
  * [ `Impact: Deleted Google Cloud Backup and DR Backup`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-delete-vault-backup)
  * [ `Impact: Deleted Google Cloud Backup and DR host`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-hosts-delete-host)
  * [ `Impact: Deleted Google Cloud Backup and DR plan association`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-delete-backup-plan-association)
  * [ `Impact: Deleted Google Cloud Backup and DR Vault`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-delete-vault)
  * [ `Impact: GKE kube-dns modification detected`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-kube-dns-modification)
  * [ `Impact: Google Cloud Backup and DR delete policy`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-templates-delete-policy)
  * [ `Impact: Google Cloud Backup and DR delete profile`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-profiles-delete-profile)
  * [ `Impact: Google Cloud Backup and DR delete storage pool`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-storage-pools-delete)
  * [ `Impact: Google Cloud Backup and DR delete template`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-templates-delete-template)
  * [ `Impact: Google Cloud Backup and DR expire all images`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-expire-images-all)
  * [ `Impact: Google Cloud Backup and DR expire image`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-expire-image)
  * [ `Impact: Google Cloud Backup and DR reduced backup expiration`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-reduce-backup-expiration)
  * [ `Impact: Google Cloud Backup and DR reduced backup frequency`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-reduce-backup-frequency)
  * [ `Impact: Google Cloud Backup and DR remove appliance`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-appliances-remove-appliance)
  * [ `Impact: Google Cloud Backup and DR remove plan`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/backup-remove-plan)
  * [ `Impact: Managed Instance Group Autoscaling Set To Maximum`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-mig-autoscaling-set-to-max)
  * [ `Impact: Service API Disabled`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-service-api-disabled)
  * [ `Impact: Suspicious Kubernetes Container Names - Cryptocurrency Mining`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-suspicious-cryptomining-pod)
  * [ `Impact: VPC Firewall High Priority Block`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-vpc-firewall-high-priority-block)
  * [ `Impact: VPC Firewall Mass Rule Deletion`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-vpc-firewall-mass-rule-deletion)
  * [ `Initial Access: Account Disabled Hijacked`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-account-disabled-hijacked)
  * [ `Initial Access: AI Agent Identity Excessive Permission Denied Actions`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-excessive-failed-attempt)
  * [ `Initial Access: Anonymous GKE Resource Created from the Internet`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-resource-created-anonymously-from-internet)
  * [ `Initial Access: CloudDB Successful login from Anonymizing Proxy IP`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-db-login-succeeded-anon-ip)
  * [ `Initial Access: Database Superuser Writes to User Tables`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloudsql-superuser-writes-to-user-tables)
  * [ `Initial Access: Disabled Password Leak`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-disabled-password-leak)
  * [ `Initial Access: Dormant Service Account Action`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/dormant-service-account-used-in-action)
  * [ `Initial Access: Dormant Service Account Activity in AI Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-dormant-service-account-used-in-action)
  * [ `Initial Access: Dormant Service Account Key Created`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/dormant-service-account-key-created)
  * [ `Initial Access: Excessive Permission Denied Actions`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/excessive-failed-attempt)
  * [ `Initial Access: GKE NodePort service created`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-nodeport-service-created)
  * [ `Initial Access: GKE Resource Modified Anonymously from the Internet`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-data-accessed-anonymously-from-internet)
  * [ `Initial Access: Government Based Attack`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-government-backed-attack)
  * [ `Initial Access: Leaked Service Account Key Used`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/leaked-sa-key-used)
  * [ `Initial Access: Log4j Compromise Attempt`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/log4j-compromise-attempt)
  * [ `Initial Access: Successful API call made from a TOR proxy IP`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-tor-proxy-ip-request)
  * [ `Initial Access: Suspicious Login Blocked`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-suspicious-login-blocked)
  * [ `Lateral Movement: Modified Boot Disk Attached to Instance`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/modify-boot-disk-attach-to-instance)
  * [ `Lateral Movement: OS Patch Execution From Service Account`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-os-patch-execution-from-service-account)
  * [ `Log4j Malware: Bad Domain`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-domain-google-log4j-intel)
  * [ `Log4j Malware: Bad IP`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-ip-google-log4j-intel)
  * [ `Malware: bad domain`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-domain-live-google-intel)
  * [ `Malware: bad IP`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-ip-live-google-intel)
  * [ `Malware: Cryptomining Bad Domain`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-domain-google-crypto-intel)
  * [ `Malware: Cryptomining Bad IP`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/bad-ip-google-crypto-intel)
  * [ `Persistence: GCE Admin Added SSH Key`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gce-admin-add-ssh-key)
  * [ `Persistence: GCE Admin Added Startup Script`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gce-admin-add-startup-script)
  * [ `Persistence: GKE Webhook Configuration Detected`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-webhook-config-created)
  * [ `Persistence: Global Startup Script Added`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-global-startup-script-added)
  * [ `Persistence: IAM Anomalous Grant`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-grant)
  * [ `Persistence: New AI API Method`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-behavior-new-api-method)
  * [ `Persistence: New API Method`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-behavior-new-api-method)
  * [ `Persistence: New Geography`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-behavior-ip-geolocation)
  * [ `Persistence: New Geography for AI Service`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-iam-anomalous-behavior-ip-geolocation)
  * [ `Persistence: New User Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/iam-anomalous-behavior-user-agent)
  * [ `Persistence: Sensitive AI Permission Added to Custom Role`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-ai-permission-added-to-custom-role)
  * [ `Persistence: Sensitive Role Granted by AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-role-granted-by-ai-agent)
  * [ `Persistence: Sensitive Role Granted to External AI Agent`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/external-ai-agent-granted-sensitive-role)
  * [ `Persistence: Service Account Created in sensitive namespace`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-service-account-creation-sensitive-namespace)
  * [ `Persistence: Service Account Key Created`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-service-account-key-creation)
  * [ `Persistence: SSO Enablement Toggle`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-sso-enablement-toggle)
  * [ `Persistence: SSO Settings Changed`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-sso-settings-changed)
  * [ `Persistence: Strong Authentication Disabled`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-strong-authentication-disabled)
  * [ `Persistence: Two Step Verification Disabled`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gsuite-two-step-verification-disabled)
  * [ `Persistence: Unmanaged Account Granted Sensitive Role`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/unmanaged-account-added-in-iam-role)
  * [ `Privilege Escalation: AI Agent Cross-Project Access Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-cross-project-access-token)
  * [ `Privilege Escalation: AI Agent Cross-Project OpenID Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-cross-project-openid)
  * [ `Privilege Escalation: AI Agent Token Generation Using Implicit Delegation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-implicit-delegation)
  * [ `Privilege Escalation: AI Agent Token Generation Using signJwt`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-agent-token-generation-sign-jwt)
  * [ `Privilege Escalation: AlloyDB Database Superuser Writes to User Tables`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/alloydb-superuser-writes-to-user-tables)
  * [ `Privilege Escalation: AlloyDB Over-Privileged Grant`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/alloydb-user-granted-all-permissions)
  * [ `Privilege Escalation: Anomalous Impersonation of Service Account for Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-impersonation-of-sa-admin-activity)
  * [ `Privilege Escalation: Anomalous Impersonation of Service Account for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonation-of-sa-admin-activity)
  * [ `Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-multistep-admin-activity)
  * [ `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-multistep-admin-activity)
  * [ `Privilege Escalation: Anomalous Multistep Service Account Delegation for AI Data Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-multistep-data-access)
  * [ `Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-multistep-data-access)
  * [ `Privilege Escalation: Anomalous Service Account Impersonator for Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-impersonator-admin-activity)
  * [ `Privilege Escalation: Anomalous Service Account Impersonator for AI Admin Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonator-admin-activity)
  * [ `Privilege Escalation: Anomalous Service Account Impersonator for AI Data Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/ai-anomalous-sa-delegation-impersonator-data-access)
  * [ `Privilege Escalation: Anomalous Service Account Impersonator for Data Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/anomalous-sa-delegation-impersonator-data-access)
  * [ `Privilege Escalation: Changes to sensitive Kubernetes RBAC objects`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-edit-sensitive-rbac-object)
  * [ `Privilege Escalation: ClusterRole with Privileged Verbs`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-clusterrole-privileged-verbs)
  * [ `Privilege Escalation: ClusterRoleBinding to Privileged Role`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-crb-clusterrole-aggregation-controller)
  * [ `Privilege Escalation: Create Kubernetes CSR for master cert`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-csr-for-master-cert)
  * [ `Privilege Escalation: Creation of sensitive Kubernetes bindings`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-create-sensitive-binding)
  * [ `Privilege Escalation: Default Compute Engine Service Account SetIAMPolicy`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/cloud-run-services-set-iam-policy)
  * [ `Privilege Escalation: Dormant Service Account Granted Sensitive Role`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/dormant-service-account-added-in-iam-role)
  * [ `Privilege Escalation: Effectively Anonymous Users Granted GKE Cluster Access`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-anonymous-users-granted-access)
  * [ `Privilege Escalation: External Member Added To Privileged Group`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/external-member-added-to-privileged-group)
  * [ `Privilege Escalation: Get Kubernetes CSR with compromised bootstrap credentials`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-get-csr-with-compromised-bootstrap-credentials)
  * [ `Privilege Escalation: Global Shutdown Script Added`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-global-shutdown-script-added)
  * [ `Privilege Escalation: Impersonation Role Granted For Dormant Service Account`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/dormant-service-account-impersonation-role-granted)
  * [ `Privilege Escalation: Launch of privileged Kubernetes container`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-control-plane-launch-privileged-container)
  * [ `Privilege Escalation: New Service Account is Owner or Editor`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-service-account-editor-owner)
  * [ `Privilege Escalation: Privileged Group Opened To Public`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/privileged-group-opened-to-public)
  * [ `Privilege Escalation: Sensitive Role Granted To Hybrid Group`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/sensitive-role-to-group-with-external-member)
  * [ `Privilege Escalation: Suspicious Cross-Project Permission Use`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-suspicious-cross-project-permission-datafusion)
  * [ `Privilege Escalation: Suspicious Kubernetes Container Names - Exploitation and Escape`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/gke-suspicious-exploit-pod)
  * [ `Privilege Escalation: Suspicious Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-suspicious-token-generation-cross-project-access-token)
  * [ `Privilege Escalation: Suspicious Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-suspicious-token-generation-cross-project-openid)
  * [ `Privilege Escalation: Suspicious Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-suspicious-token-generation-implicit-delegation)
  * [ `Privilege Escalation: Suspicious Token Generation`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-suspicious-token-generation-sign-jwt)
  * [ `Privilege Escalation: Workload Created with a Sensitive Host Path Mount`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-sensitive-hostpath)
  * [ `Privilege Escalation: Workload with shareProcessNamespace enabled`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-gke-shareprocessnamespace-pod)
  * [ `Resource Development: Offensive Security Distro Activity`](https://docs.cloud.google.com/security-command-center/docs/findings/threats/yl2-offensive-security-distro-activity)



[Learn more about Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

### Google Cloud Armor

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

[Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) helps protect your application by providing Layer 7 filtering. Cloud Armor scrubs incoming requests for common web attacks or other Layer 7 attributes to potentially block traffic before it reaches your load-balanced backend services or backend buckets.

Cloud Armor exports two findings to Security Command Center:

  * [Allowed Traffic Spike](https://docs.cloud.google.com/armor/docs/cscc-findings#allowed_traffic_spike_finding)

  * [Increasing Deny Ratio](https://docs.cloud.google.com/armor/docs/cscc-findings#increasing_deny_ratio_finding)




### Sensitive Actions Service

Sensitive Actions Service is a built-in service of Security Command Center that detects when actions are performed in your Google Cloud organization, folders, and projects that might be damaging to your business if they are taken by a malicious actor.

Sensitive Actions Service is always enabled and automatically monitors all of your organization's [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity) for sensitive actions. Admin Activity audit logs are always on, so you don't need to enable or configure them.

For more information about Sensitive Actions Service, see [Overview of Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview).

### Virtual Machine Threat Detection

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Virtual Machine Threat Detection is a built-in service of Security Command Center. This service scans virtual machines to detect potentially malicious applications, such as cryptocurrency mining software, kernel-mode rootkits, and malware running in compromised cloud environments.

VM Threat Detection is part of the Security Command Center threat detection suite and is designed to complement the existing capabilities of [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).

For more information about VM Threat Detection, see [VM Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview).

#### VM Threat Detection threat findings

VM Threat Detection can generate the following threat findings.

##### Cryptocurrency mining threat findings

VM Threat Detection detects the following finding categories through hash matching or YARA rules. 

VM Threat Detection cryptocurrency mining threat findings Category | Module | Description  
---|---|---  
  
#### `Execution: Cryptocurrency Mining Hash Match`

|  `CRYPTOMINING_HASH` |  Matches memory hashes of running programs against known memory hashes of cryptocurrency mining software. Findings are classified as **High** severity by default.   
  
#### `Execution: Cryptocurrency Mining YARA Rule`

|  `CRYPTOMINING_YARA` |  Matches memory patterns, such as proof-of-work constants, known to be used by cryptocurrency mining software. Findings are classified as **High** severity by default.   
  
#### `Execution: Cryptocurrency Mining Combined Detection`

| 

  * `CRYPTOMINING_HASH`
  * `CRYPTOMINING_YARA`

|  Identifies a threat that was detected by both the `CRYPTOMINING_HASH` and `CRYPTOMINING_YARA` modules. For more information, see [ Combined detections](https://docs.cloud.google.com/security-command-center/docs/how-to-use-vm-threat-detection#combined_detections). Findings are classified as **High** severity by default.   
  
##### Kernel-mode rootkit threat findings

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

VM Threat Detection analyzes kernel integrity at run time to detect common evasion techniques that are used by malware.

The `KERNEL_MEMORY_TAMPERING` module detects threats by doing a hash comparison on the kernel code and kernel read-only data memory of a virtual machine.

The `KERNEL_INTEGRITY_TAMPERING` module detects threats by checking the integrity of important kernel data structures.

VM Threat Detection kernel-mode rootkit threat findings Category | Module | Description  
---|---|---  
Rootkit  
  
#### `Defense Evasion: Rootkit`

| 

  * `KERNEL_MEMORY_TAMPERING`
  * `KERNEL_INTEGRITY_TAMPERING`

| A combination of signals matching a known kernel-mode rootkit is present. To receive findings of this category, make sure both modules are enabled. Findings are classified as **High** severity by default.   
Kernel memory tampering  
  
#### `Defense Evasion: Unexpected kernel read-only data modification`

| `KERNEL_MEMORY_TAMPERING` | Unexpected modifications of kernel read-only data memory are present. Findings are classified as **High** severity by default.   
Kernel integrity tampering  
  
#### `Defense Evasion: Unexpected ftrace handler`

| `KERNEL_INTEGRITY_TAMPERING` | `ftrace` points are present with callbacks pointing to regions that are not in the expected kernel or module code range. Findings are classified as **High** severity by default.   
  
#### `Defense Evasion: Unexpected interrupt handler`

| `KERNEL_INTEGRITY_TAMPERING` | Interrupt handlers that aren't in the expected kernel or module code regions are present. Findings are classified as **High** severity by default.   
  
#### `Defense Evasion: Unexpected kernel modules`

| `KERNEL_INTEGRITY_TAMPERING` | Kernel code pages that are not in the expected kernel or module code regions are present. Findings are classified as **High** severity by default.   
  
#### `Defense Evasion: Unexpected kprobe handler`

| `KERNEL_INTEGRITY_TAMPERING` | `kprobe` points are present with callbacks pointing to regions that are not in the expected kernel or module code range. Findings are classified as **High** severity by default.   
  
#### `Defense Evasion: Unexpected processes in runqueue`

| `KERNEL_INTEGRITY_TAMPERING` | Unexpected processes in the scheduler run queue are present. Such processes are in the run queue, but not in the process task list. Findings are classified as **High** severity by default.   
  
#### `Defense Evasion: Unexpected system call handler`

| `KERNEL_INTEGRITY_TAMPERING` | System call handlers that aren't in the expected kernel or module code regions are present. Findings are classified as **High** severity by default.   
  
## Errors

Error detectors can help you detect errors in your configuration that prevent security sources from generating findings. Error findings are generated by the `Security Command Center` security source and have the finding class `SCC errors`.

### Inadvertent actions

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

The following finding categories represent errors possibly caused by unintentional actions.

Inadvertent actions Category name | API name | Summary | Severity  
---|---|---|---  
  
#### `API disabled`

| `API_DISABLED` |  **Finding description:** A required API is disabled for the project. The disabled service can't send findings to Security Command Center.  **Pricing tier:** [Premium or Standard](https://cloud.google.com/security-command-center/pricing) **Supported assets**  
[ cloudresourcemanager.googleapis.com/Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects) **Batch scans** : Every 60 hours  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#api_disabled) |  Critical   
  
#### `Attack path simulation: no resource value configs match any resources`

| `APS_NO_RESOURCE_VALUE_CONFIGS_MATCH_ANY_RESOURCES` |  **Finding description:** [Resource value configurations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resource-value-configurations) are defined for attack path simulations, but they do not match any resource instances in your environment. The simulations are using the default high-value resource set instead.  This error can have any of the following causes: 

  * None of the resource value configurations match any resource instances.
  * One or more resource value configurations that specify `NONE` override every other valid configuration.
  * All the defined resource value configurations specify a value of `NONE`.

**Pricing tier:** [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets**  
[ cloudresourcemanager.googleapis.com/Organizations](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations) **Batch scans** : Before every attack path simulation.  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#aps_no_rvcs_match_resources) |  Critical   
  
#### `Attack path simulation: resource value assignment limit exceeded`

| `APS_RESOURCE_VALUE_ASSIGNMENT_LIMIT_EXCEEDED` |  **Finding description:** In the last [attack path simulation](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_path_simulations), the number of high-value resource instances, as identified by the [resource value configurations](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resource-value-configurations), exceeded the limit of 1,000 resource instances in a high-value resource set. As a result, Security Command Center excluded the excess number of instances from the high-value resource set.  The total number of matching instances and the total number of instances excluded from the set are identified in the `SCC Error` finding in the Google Cloud console.  The attack exposure scores on any findings that affect excluded resource instances do not reflect the high-value designation of the resource instances.  **Pricing tier:** [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets**  
[ cloudresourcemanager.googleapis.com/Organizations](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations) **Batch scans** : Before every attack path simulation.  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#aps_value_assignment_limit_exceeded) |  High   
  
#### `Container Threat Detection Image Pull Failure`

| `KTD_IMAGE_PULL_FAILURE` |  **Finding description:** Container Threat Detection can't be enabled on the cluster because a required container image can't be pulled (downloaded) from `gcr.io`, the [Container Registry](https://docs.cloud.google.com/container-registry/docs/overview) image host. The image is needed to deploy the Container Threat Detection DaemonSet that Container Threat Detection requires.  The attempt to deploy the Container Threat Detection DaemonSet resulted in the following error: 

> `Failed to pull image "badurl.gcr.io/watcher-daemonset:ktd_release.watcher_20220831_RC00": rpc error: code = NotFound desc = failed to pull and unpack image "badurl.gcr.io/watcher-daemonset:ktd_release.watcher_20220831_RC00": failed to resolve reference "badurl.gcr.io/watcher-daemonset:ktd_release.watcher_20220831_RC00": badurl.gcr.io/watcher-daemonset:ktd_release.watcher_20220831_RC00: not found`

**Pricing tier:** [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets**  
[ container.googleapis.com/Cluster](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters) **Batch scans** : Every 30 minutes  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#ktd_image_pull_failure) |  Critical   
  
#### `Container Threat Detection Blocked By Admission Controller`

| `KTD_BLOCKED_BY_ADMISSION_CONTROLLER` |  **Finding description:** Container Threat Detection can't be enabled on a Kubernetes cluster. A third-party admission controller is preventing the deployment of a Kubernetes DaemonSet object that Container Threat Detection requires.  When viewed in the Google Cloud console, the finding details include the error message that was returned by Google Kubernetes Engine when Container Threat Detection attempted to deploy a Container Threat Detection DaemonSet Object.  **Pricing tier:** [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets**  
[ container.googleapis.com/Cluster](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters) **Batch scans** : Every 30 minutes  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#ktd_blocked_by_admission_controller) |  High   
  
#### `Container Threat Detection service account missing permissions`

| `KTD_SERVICE_ACCOUNT_MISSING_PERMISSIONS` |  **Finding description:** A service account is missing permissions that Container Threat Detection requires. Container Threat Detection could stop functioning properly because the [ detection instrumentation](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#how-it-works) cannot be enabled, upgraded, or disabled.  **Pricing tier:** [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets**  
[ cloudresourcemanager.googleapis.com/Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects) **Batch scans** : Every 30 minutes  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#container_threat_detection_service_account_missing_permissions) |  Critical   
  
#### `GKE service account missing permissions`

| `GKE_SERVICE_ACCOUNT_MISSING_PERMISSIONS` |  **Finding description:** Container Threat Detection can't generate findings for a Google Kubernetes Engine cluster, because the [ GKE default service account](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview#authentication_and_authorization) on the cluster is missing permissions. This prevents Container Threat Detection from being successfully enabled on the cluster.  **Pricing tier:** [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets**  
[ container.googleapis.com/Cluster](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters) **Batch scans** : Every week  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#gke_service_account_missing_permissions) |  High   
  
#### `Misconfigured Cloud Logging Export`

| `MISCONFIGURED_CLOUD_LOGGING_EXPORT` |  **Finding description:** The project configured for [ continuous export to Cloud Logging](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging) is unavailable. Security Command Center can't send findings to Logging.  **Pricing tier:** [Premium](https://cloud.google.com/security-command-center/pricing#premium-tier-subscription-based-pricing) **Supported assets**  
[ cloudresourcemanager.googleapis.com/Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations) **Batch scans** : Every 30 minutes  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#misconfigured_cloud_logging_export) |  High   
  
#### `VPC Service Controls Restriction`

| `VPC_SC_RESTRICTION` |  **Finding description:** Security Health Analytics can't produce certain findings for a project. The project is protected by a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview), and the Security Command Center service account doesn't have access to the perimeter.  **Pricing tier:** [Premium or Standard](https://cloud.google.com/security-command-center/pricing) **Supported assets**  
[ cloudresourcemanager.googleapis.com/Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects) **Batch scans** : Every 6 hours  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#vpc_service_controls_restriction) |  High   
  
#### `External Exposure VPC Service Controls Restriction`

| `EXTERNAL_EXPOSURE_VPC_SC_RESTRICTION` |  **Finding description:** External Exposure can't perform scans or generate findings for a project. The project is protected by a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview), and the External Exposure service agent doesn't have access to the perimeter.  **Pricing tier:** [Premium](https://cloud.google.com/security-command-center/pricing) **Supported assets**  
[ cloudresourcemanager.googleapis.com/Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects) **Batch scans** : Every 12 hours  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#ee-vpc-service-controls-restriction) |  High   
  
#### `Security Command Center service account missing permissions`

| `SCC_SERVICE_ACCOUNT_MISSING_PERMISSIONS` |  **Finding description:** The Security Command Center service account is missing permissions required to function properly. No findings are produced.  **Pricing tier:** [Premium or Standard](https://cloud.google.com/security-command-center/pricing) **Supported assets**  


  * [ cloudresourcemanager.googleapis.com/Organization](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations)
  * [ cloudresourcemanager.googleapis.com/Project](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects)

**Batch scans** : Every 30 minutes  [ Fix this finding build](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#security_command_center_service_account_missing_permissions) |  Critical   
  
For more information, see [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

## Application Design Center integration

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You can integrate proactive security assessments directly into your application development lifecycle by using Application Design Center (App Design Center) with Security Command Center.

**Note:** Application lifecycle security assessments support built-in compliance frameworks (such as those provided by Security Command Center). Custom controls and custom frameworks are not supported in this release.

This integration focuses on the following primary concepts.

### Design-time and runtime findings

  * **Design-time findings** : Originate from scans of Infrastructure as Code (IaC) templates and applications within App Design Center before resources are deployed. Design-time findings are sent to Security Command Center on demand when you deploy an application. There is no automatic periodic scanning of application designs. For more information, see [Data retention](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).
  * **Runtime findings** : Originate from resources that are deployed in your cloud environment.



Security Command Center shows both types of findings to help provide a unified view of your application's security posture.

### Managed and unmanaged applications

Security Command Center uses the following terms to differentiate applications based on how they're deployed:

Managed applications
    Applications that you design by using App Design Center. These applications support design-time assessments.
Unmanaged applications
    Applications that are registered in App Hub but not managed by App Design Center. These applications support runtime monitoring and risk prioritization in Security Command Center, but don't support design-time assessments.

### Pre-deployment assessment points

You can perform security assessments at several stages of the application lifecycle within App Design Center.

  1. **Design phase** : On-demand assessments within App Design Center when you edit a template or application.
  2. **Publish phase** : Automatic assessments within App Design Center when you publish templates to a Service Catalog.
  3. **Deploy phase** : A final assessment check before you provision resources.



Design-time findings are only sent to Security Command Center when the application is deployed.

#### Review application lifecycle security assessment findings in the console

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Application Design Center**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



## App Hub

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Command Center and Compliance Manager let you view findings, issues, and compliance information for resources within a specific App Hub application. You can filter investigative views to view data for only those resources that are [registered to an App Hub application](https://docs.cloud.google.com/app-hub/docs/register-resources).

You can filter in the following investigative views:

  * **Risk Overview** > **All risk** dashboard
  * **Risk Overview** > **Data** dashboard
  * **Findings** page
  * **Issues** page
  * **Compliance** > **Monitor (New)** tab
  * **Compliance** > **Monitor (New)** > **Framework Details** page



When viewing data at the organization level, you can use the **Select app** menu to filter the view. This menu lists applications that are created in App Hub and deployed in the same organization where Security Command Center is active. Information in the **Select app** menu is retrieved from Cloud Asset Inventory and App Hub.

The **Select app** menu is not available when viewing data for a single project or folder.

## What's next

  * Learn about Security Command Center in the [Security Command Center overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).
  * Learn how to add new security sources by [configuring Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
