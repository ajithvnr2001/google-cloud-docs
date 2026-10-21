---
url: https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:39:17.349598+00:00
---

# Security bulletins  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/security-bulletins/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes security bulletins related to Apigee.

To get the latest security bulletins delivered to you, do one of the following:

  * Add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators).
  * Add the feed URL directly to your feed reader: `https://cloud.google.com/feeds/apigee-security-bulletins.xml`



## GCP-2026-041

**Published:** 2026-06-24

### Description

Description | Severity | Notes  
---|---|---  
A recent security investigation was conducted regarding log4j vulnerabilities (CVE-2026-34480 and CVE-2026-34477) reported in Apigee Edge for Private Cloud. Google has determined that Apigee Edge for Private Cloud is **not vulnerable** to these CVEs. **No customer action is required.** **CVE-2026-34480:** Apache Log4j Core's `XmlLayout` fails to sanitize characters forbidden by the XML 1.0 specification, producing invalid XML output whenever a log message or MDC value contains such characters. **CVE-2026-34477:** Addressed hostname verification issues where TLS connections could be left vulnerable to interception when using SMTP, Socket, or Syslog appenders. **Mitigation Note:** Apigee Edge for Private Cloud only ships the log4j library in gateway components but doesn't actually use them, as logback is used instead. Furthermore, Apigee Edge for Private Cloud does not use SMTP, Socket, or Syslog appender features of log4j. As a result, neither of these vulnerabilities is applicable to Apigee Edge for Private Cloud. **Affected Products**

  * Apigee Edge for Private Cloud

**What Should I Do?**

#### Apigee Edge for Private Cloud

No customer action is required. Apigee Edge for Private Cloud is not affected by these vulnerabilities. Customers running vulnerability scanners against Apigee Edge for Private Cloud deployments may see CVE-2026-34480 and CVE-2026-34477 flagged because the log4j library is present on disk. Customers can cite this security bulletin in their scanner-finding exception process to mark these CVEs as Not Applicable for their Apigee Edge for Private Cloud deployment. | High |  [CVE-2026-34480](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-34480)  
[CVE-2026-34477](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-34477)  
  
## GCP-2026-034

**Published:** 2026-05-20

### Description

Description | Severity | Notes  
---|---|---  
A vulnerability was found in Apigee where the `IntegrationRegion` parameter in the `SetIntegrationRequest` policy lacks validation, allowing for Server-Side Request Forgery (SSRF) and service account token exfiltration. The issue arises when an attacker can control a flow variable used for `IntegrationRegion`, leading to requests being sent to an attacker-controlled host with the service account token. **Affected Products** Impact is confined to the `SetIntegrationRequest` policy. This includes deployments on the following Apigee platforms:

  * Apigee
  * Apigee Hybrid

**What Should I Do?** Take the following actions for each affected product:

#### Apigee

No action is required for customers using the Google Cloud version of Apigee. Vulnerability fixes have been applied to Apigee release [1-16-0-apigee-5](https://docs.cloud.google.com/apigee/docs/release-notes#January_20_2026).

#### Apigee Hybrid

You must upgrade to one of the following security patch releases: | Hybrid major version | Security patch release for the affected minor version  
---|---  
1.14 | [1.14.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#April_27_2026)  
1.15 | [1.15.2](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1152)  
1.16 | [1.16.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#April_20_2026)  
High |  [CVE-2026-2264](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-2264)  
  
## GCP-2026-010

**Published:** 2026-02-13

### Description

Description | Severity | Notes  
---|---|---  
A vulnerability was identified in the Apigee platform that could have allowed a malicious actor with administrative or developer-level permissions in their own Apigee environment to elevate privileges and access cross-tenant data. Specifically, a vulnerability in Apigee's sandboxing technology allowed the use of a link-local endpoint to access service account tokens (P4SA) within a customer tenant project. By leveraging this identity, an attacker could theoretically read analytics metadata or tamper with internal monitoring records across other Apigee organizations (tenants). **What should I do?** Take the following actions for each affected product:

#### Apigee

No action is required for customers using the Google Cloud version of Apigee. Vulnerability fixes have been applied to Apigee release [1-16-0-apigee-3](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025).

#### Apigee Hybrid

To resolve this vulnerability, customers must [enable the Pub/Sub-based analytics pipeline](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/data-collection-with-data-residency) and upgrade to a supported hybrid version: | Feature configuration | Minimum remediated version  
---|---  
Standard Apigee Hybrid | v1.14.0 or higher  
With Monetization (Mint) enabled | v1.14.3, v1.15.1, or v1.16.0  
High |  [CVE-2025-13292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-13292)  
  
## GCP-2025-023

**Published:** 2025-05-05

Description | Severity | Notes  
---|---|---  
This bulletin addresses potential security gaps which could be exploited if not addressed in the JavaCallout and PythonScript policies that were discovered and addressed. These policies could lead to unauthorized remote code execution (RCE) and privilege escalation within the Apigee runtime environment. These possible exploits require internal authorized user access (users who have privilege to deploy proxies) to exploit. These potential vulnerabilities stem from insufficient sandboxing for scenarios such as access by reflection and spoofing permission objects to bypass the security manager.  **Affected Products** Impact is confined to the JavaCallout and PythonScript policies. This includes deployments on the following Apigee platforms: 

  * Apigee
  * Apigee Edge for Public Cloud
  * Apigee Hybrid
  * Apigee Edge for Private Cloud

**What Should I Do?** Take the following actions for each affected product:

#### Apigee

No action is required for customers using the Google Cloud version of Apigee. Vulnerability fixes have been applied to Apigee release [1-14-0-apigee-8](https://docs.cloud.google.com/apigee/docs/release-notes#February_28_2025). If the release team is not able to make the release rollout for your orgs, either a TAM or a support representative will reach out to you to fix any affected JavaCallout proxy bundles.

#### Apigee Hybrid

You must upgrade to one of the following security patch releases: | Hybrid major version | Security patch release for the affected minor version  
---|---  
1.12 | [1.12.4](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#March_01_2025)  
1.13 | [1.13.3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1133)  
1.14 | [1.14.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1141)  
1.11 | [1.11.2 hotfix3](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_1112-hotfix3)  
High |   
  
#### Apigee Edge for Public Cloud

No action is required from Apigee Edge customers. Fixes have been applied to the latest Edge runtime. If you are a customer who cannot be updated to the latest Edge release due to known pending action items, a customer support representative will reach out to you.

#### Apigee Edge for Private Cloud

If you are an Edge for Private Cloud user, you should review your JavaCallout and PythonScript policies to ensure you are using code and libraries from trusted sources. Modifications to such policies require internal authorized access (users who have permissions to deploy proxies), so it is recommended that you audit your permissions to ensure only trusted users retain such access. Vulnerability fixes have been applied to Edge Private Cloud releases [4.52.02](https://docs.apigee.com/private-cloud/v4.52.02/installation-requirements) and [4.53.00](https://docs.apigee.com/private-cloud/v4.53.00/installation-requirements).

## GCP-2024-040

**Published:** 2024-07-02

This bulletin includes details specific to each of these Apigee products:

  * Edge Public Cloud
  * Edge Private Cloud
  * Edge Microgateway
  * Apigee
  * Apigee Hybrid



### Edge Public Cloud

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, Apigee Edge for Public Cloud is not exploitable and mitigations are in place. Even though this CVE is not exploitable, Apigee will upgrade the workloads to address the above CVE. **What should I do?** No action item is required from Apigee users. Patching for workloads will be done in the upcoming days and the security bulletin will be updated once the patching is completed. | Critical |   
  
### Edge Private Cloud

Description | Severity  
---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to VM nodes. Edge Private Cloud customers own and manage the VMs/Physical hosts where Edge Private Cloud is deployed. | Version | Impact  
---|---  
OpenSSH < 4.4p1 | Vulnerable  
4.4p1 <= OpenSSH < 8.5p1 | Not Vulnerable  
8.5p1 <= OpenSSH < 9.8p1 | Vulnerable  
  
**What should I do?**

Review the OpenSSH version by issuing the command `ssh -V` and validate the OpenSSH version. If you are running on any OpenSSH versions that are impacted, update to a version which is NOT vulnerable to this CVE. OpenSSH has released [9.8p1](https://www.openssh.com/releasenotes.html#9.8p1) on July 1, 2024.

Critical |   
  
### Edge Microgateway

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to VM nodes. Edge Microgateway customers own and manage the VMs/Physical hosts where Edge Microgateway is deployed. | Version | Impact  
---|---  
OpenSSH < 4.4p1 | Vulnerable  
4.4p1 <= OpenSSH < 8.5p1 | Not Vulnerable  
8.5p1 <= OpenSSH < 9.8p1 | Vulnerable  
  
**What should I do?**

Please review the OpenSSH version by issuing commands `ssh -V` and validate the OpenSSH version. If you are running on any OpenSSH versions which are impacted, please update to a version which is NOT vulnerable to this CVE. OpenSSH has released [9.8p1](https://www.openssh.com/releasenotes.html#9.8p1) on July 1, 2024.

Critical |   
  
### Apigee

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, Apigee is not exploitable and mitigations are in place. Even though this CVE is not exploitable, Apigee will upgrade the workloads to address CVE-2024-6387. **What should I do?** No action item is required from Apigee users. Patching for workloads will be done in the upcoming days and the security bulletin will be updated once the patching is completed. Note: If Managed Instance Groups are deployed in a customer project for [northbound load balancing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#configure-routing), specifically [InternalRouting (VPC)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#internal-routing-vpc) and [ExternalRouting (MIG)](https://cloud.google.com/apigee/docs/api-platform/get-started/install-cli#external-routing-mig), verify the OpenSSH version installed on them. If the version is vulnerable to the CVE, then update to OpenSSH [version 9.8p1](https://www.openssh.com/releasenotes.html#9.8p1) released on July 1, 2024 by yourself, as Apigee does not manage these MIGs. | Critical |   
  
### Apigee Hybrid

Description | Severity | Notes  
---|---|---  
A remote code execution vulnerability, [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387), was recently discovered in OpenSSH. The vulnerability exploits a race condition that could be used to obtain access to a remote shell, enabling attackers to gain root access to GKE nodes. At the time of publication, hybrid images are not vulnerable because OpenSSH is not packaged into any of the hybrid container images. However if your host/GKE-node OS is running with the below vulnerable versions of OpenSSH, your hybrid clusters will be exploitable. | Version | Impact  
---|---  
OpenSSH < 4.4p1 | Vulnerable  
4.4p1 <= OpenSSH < 8.5p1 | Not Vulnerable  
8.5p1 <= OpenSSH < 9.8p1 | Vulnerable  
  
**What should I do?**

This issue has been addressed in Google Cloud Customer Care Security Bulletin [GCP-2024-040](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040). 

For instructions and more details, see the following bulletins:

  * [GKE security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gke)
  * [GKE on VMware security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gdcvmware)
  * [GKE on AWS security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gkeaws)
  * [GKE on Azure security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gkeazure)
  * [GKE on Bare Metal security bulletin](https://docs.cloud.google.com/anthos/clusters/docs/security-bulletins#gcp-2024-040-gdcbm)
  * **AWS** : There is no update yet (As of July 1st 2024 2:22 PM PST). Refer their bulletin page for [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)
  * **Azure** : There is no update yet (As of July 1st 2024 2:22 PM PST). Refer their bulletin page for [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)
  * **OpenShift** : [OpenSSH's server (sshd) [CVE-2024-6387] | Red Hat Customer Portal](https://access.redhat.com/security/cve/cve-2024-6387)

Critical |   
  
## GCP-2024-006

**Published:** 2024-2-5

Description | Severity | Notes  
---|---|---  
When an Apigee API Management proxy connects to a [target endpoint](https://docs.apigee.com/api-platform/reference/api-proxy-configuration-reference#targetendpoint) or [ target server](https://docs.apigee.com/api-platform/deploy/load-balancing-across-backend-servers), the proxy does not perform hostname validation for the certificate presented by the target endpoint or target server by default. If hostname validation is not enabled using one of the following options, Apigee proxies connecting to a target endpoint or target server may be at risk for a man-in-the-middle attack by an authorized user. For more information, see [Configuring TLS from Edge to the backend (Cloud and Private Cloud)](https://docs.apigee.com/api-platform/system-administration/configuring-ssl-edge-backend-service).  **Affected Products** Apigee proxy deployments on the following Apigee platforms are affected:

  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud

**What Should I Do?** Customers can utilize either of the following options to enable this validation: **Option 1 - Add a configuration to your proxy** You can enable validation of your target endpoint or target server by adding a `<CommonName>` configuration to the `SSLInfo` section of the `<HTTPTargetConnection>` element in your [proxy configuration](https://docs.apigee.com/api-platform/reference/api-proxy-configuration-reference#targetendpoint-targetendpointconfigurationelements) as shown:
    
    
    <HTTPTargetConnection>
      <SSLInfo>
        <Enabled>true</Enabled>
        <TrustStore>ref://mytruststoreref</TrustStore>
        <CommonName>*.example.com</CommonName>
      </SSLInfo>
      <URL>https://my.example.com/</URL>
    </HTTPTargetConnection>

If this configuration is present in the `<HTTPTargetConnection>` element of your proxy configuration, Apigee will use the value specified in `<CommonName>`for hostname validation. Wildcards may be used in this field. Apigee recommends this approach. You can test proxies individually to confirm that validation is performing as intended, with minimal potential disruption to traffic. For more information on testing hostname validation in your proxies and viewing faults, see [Using the Trace Tool](https://docs.apigee.com/api-platform/debug/using-trace-tool-0). **Option 2 - Set an organization-level flag** You can set an Apigee organization-level flag to enable hostname validation for all deployed proxies and targets in your organization. If the `features.strictSSLEnforcement` flag is set to `true` in org properties, hostname validation will be enforced each time the proxy connects to a target endpoint or target server. **Note** : While this option can help you enable the feature across the organization, hostname validation failures can occur if your targets do not present the expected certificates.

  * For **Apigee Edge for Public Cloud** deployments**:** Contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support) to have the `features.strictSSLEnforcement` flag set to `true` in org properties. **Note** : Enabling this flag will enforce the SSL check for all environments in an organization and all proxies deployed within those environments.
  * For **Apigee Edge for Private Cloud** deployments: The `features.strictSSLEnforcement `flag can be set to `true` by the organization or system administrator. For more information on setting the flag, see [Updating organization properties](https://apidocs.apigee.com/docs/organizations/1/routes/organizations/%7Borg_name%7D/post). **Note** : When updating organization level flags using the Organizations API, make sure to include _all_ existing flags in your POST request to avoid overwriting earlier configuration settings. Once the flag is set, each message processor must be individually restarted for the change to take effect. Use the following command:
        
        apigee-service edge-message-processor restart

To roll back this change, use the same Organizations API to set the flag to `false` and then restart each message processor. **Note** : Enabling this flag will enforce the SSL check for all environments in an organization and all proxies deployed within those environments. However, if `[<IgnoreValidationErrors>](https://docs.apigee.com/api-platform/system-administration/options-configuring-tls#about-setting-tls-options-in-a-virtual-host-or-target-endpoint-target-server) `is set to `true`, any validation errors detected will be ignored.

Apigee recommends implementing this change in non-production environments first, to ensure that the validation works as intended and does not result in production outages. In the event that hostname validation fails for any targets, the following fault message is returned:
    
    
    {"fault":{"faultstring":"SSL Handshake failed java.security.cert.CertificateException: No subject alternative DNS name matching example.com found.","detail":{"errorcode":"messaging.adaptors.http.flow.SslHandshakeFailed"}}}

| High |   
  
## GCP-2023-032

**Published:** 2023-10-13

**Updated:** 2023-11-03

Description | Severity | Notes  
---|---|---  
**2023-11-03 Update:** Added [ known issue](https://docs.apigee.com/release/known-issues#private-cloud-known-issues) for Apigee Edge for Private Cloud.  A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the Apigee Ingress (Cloud Service Mesh) service used by Apigee X and Apigee hybrid. The vulnerability could lead to a DoS of Apigee API management functionality.  **Affected Products**

  * **Apigee X** Deployments of Apigee X that are accessible through a Google Cloud Network Load Balancer (Layer 4), or a custom layer 4 load balancer, are affected. A hotfix has been applied to all Apigee X instances. 
  * **Apigee hybrid** Apigee hybrid instances that allow HTTP/2 requests to reach the Apigee Ingress are affected. Customers should verify if the load balancers fronting their Apigee hybrid ingresses allow for HTTP/2 requests to reach the Apigee Ingress service. 
  * **Apigee Edge for Private Cloud** The Edge for Private Cloud router and management server components are exposed to the internet and can potentially be vulnerable. Although HTTP/2 is enabled on the management port of other Edge-specific components of Edge for Private Cloud, none of those components are exposed to the internet. On non-Edge components, like Cassandra, Zookeeper and others, HTTP/2 is not enabled. We recommend that you take the steps in [ Known issues with Edge for Private Cloud](https://docs.apigee.com/release/known-issues#private-cloud-known-issues) to address the Edge for Private Cloud vulnerability. 

**Unaffected products**

  * **Apigee X** Apigee X instances which are accessed only via Google Cloud Application Load Balancers (Layer 7) are not affected. This includes deployments that have HTTP/2 enabled for gRPC proxies. 
  * **Google Cloud API Gateway** Google Cloud API Gateway is not affected.
  * **Apigee Edge Cloud** Apigee Edge Cloud is not impacted by this vulnerability.

**What Should I Do?**

  * **Apigee X** **November 3, 2023 Update:** the vulnerability has been addressed via the update to Apigee X instances that was released on October 13, 2023. See the [ Release notes](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_13_2023) for details. 
  * **Apigee hybrid** Apigee hybrid customers will need to upgrade to one of the following patch versions: 
    * [ v1.10.3-hotfix.2](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1103-hotfix2) released on Friday, October 13, 2023 
    * [ v1.9.4-hotfix.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v194-hotfix1) released on Friday, October 13, 2023 
  * **Apigee Edge for Private Cloud** Apigee Edge for Private Cloud users can follow the instructions published in [ Known issues with Edge for Private Cloud](https://docs.apigee.com/release/known-issues#private-cloud-known-issues) for explicit disablement of HTTP/2 for exposed components. 

**What Vulnerabilities Are Addressed By These Patches?** The vulnerability, CVE-2023-44487, could lead to a DoS of Apigee API management functionality.  | High |  [ CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
