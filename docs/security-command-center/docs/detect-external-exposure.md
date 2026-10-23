---
url: https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure/
title: Detect exposed resources with External Exposure \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:34.640534+00:00
---

# Detect exposed resources with External Exposure  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/detect-external-exposure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Detect exposed resources with External Exposure Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

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




## Before you begin

This section describes how to prepare your environment to use External Exposure.

### Enable the Security Center Management API

If you plan to use Security Command Center APIs, you must enable the Security Center Management API for your quota project and, if organization policies are in use that restrict API usage, ensure that the Security Center Management API is allowed. The Security Center Management API is used to control the enablement state of Security Command Center services like External Exposure.

  1. In a terminal, enable the Security Center Management API for your quota project:
         
         gcloud services enable securitycentermanagement.googleapis.com \
             --project=QUOTA_PROJECT_ID
         

Replace QUOTA_PROJECT_ID with the ID of the project that you use to manage quota.

  2. If you have organization policies that restrict API usage, ensure that the Security Center Management API is allowed. For more information, see [Review organization policies](https://docs.cloud.google.com/security-command-center/docs/activate-premium-tier#review-org-policies).

  3. If you want to receive network exposure path insights in your findings, ensure that you activate External Exposure at the organization or folder level.




### Required roles

To get the permissions that you need to configure External Exposure and view dashboard data, ask your administrator to grant you the following IAM roles on your organization, folder, or project: 

  * Configure External Exposure settings in Security Command Center and view dashboard data: [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`) 
  * Grant roles to service agents, like the `externalexposure.serviceAgent` role: [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) 
  * Create and manage service accounts: [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) 
  * View dashboard data only: [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`) 
  * View the External Exposure dashboard and scan metrics in the console, CLI, or API: [External Exposure Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/externalexposure#externalexposure.viewer) (`roles/externalexposure.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** Until the required scan metrics permissions (`externalexposure.scanMetrics.get`) are fully integrated into the standard Security Center roles, all users must also be assigned the External Exposure Viewer role to view the External Exposure dashboard on the Risk Overview page in the console.

The following Google Cloud CLI commands can be used to assign the preceding roles to a user:

#### Assign roles by using gcloud CLI

  * To grant the Security Center Admin role to a user, run the following command:
        
        gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
            --member=user:USER_EMAIL_ID \
            --role=roles/securitycenter.admin
        

  * To grant the Security Center Admin Viewer role to a user, run the following command:
        
        gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
            --member=user:USER_EMAIL_ID \
            --role=roles/securitycenter.adminViewer
        

  * To grant the External Exposure Viewer role to a user for CLI or API metrics access, run the following command:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member=user:USER_EMAIL_ID \
            --role=roles/externalexposure.viewer
        

Replace the following:

    * ORGANIZATION_ID: the numeric organization ID
    * PROJECT_ID: the project ID
    * USER_EMAIL_ID: the email address of the user who requires access



## Enable and configure the service

To enable and configure External Exposure, complete the tasks in the following sections.

You can enable and configure the service at the organization, folder, or project level. When using the API, if you want to configure settings at the folder or organization level rather than the project level, replace `projects/PROJECT_ID` with `folders/FOLDER_ID` or `organizations/ORGANIZATION_ID` in all the request URLs and the JSON data parameters.

### Activate External Exposure

Activate External Exposure for your organization, folder, or project.

After you activate the service, make sure to grant the service agent the required permissions as described in Grant service agent permissions.

### Console

  1. In the Google Cloud console, go to the **Service Enablement** page for External Exposure.

[Go to Service Enablement](https://console.cloud.google.com/projectselector2/security/command-center/config/services/external-exposure/enablement?supportedpurview=project,folder,organizationId)

  2. Select your organization or project.

  3. On the **Service Enablement** tab, in the **External Exposure** column, select the enablement status of the organization, folder, or project that you want to modify, and then select one of the following:

     * **Enable** : enable External Exposure.
     * **Disable** : disable External Exposure.
     * **Inherit** : Inherit settings from the parent resource unless overridden on the child resource.



### gcloud

Enable the Security Center Management API and activate External Exposure for your target scope.

  1. In a terminal, enable the API for your quota project:
         
         gcloud services enable securitycentermanagement.googleapis.com \
             --project=QUOTA_PROJECT_ID
         

  2. In a terminal, enable External Exposure by using the Security Center Management API:
         
         curl --request PATCH \
           "https://securitycentermanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityCenterServices/external_exposure?updateMask=intended_enablement_state" \
           --header "Authorization: Bearer $(gcloud auth print-access-token)" \
           --header "X-Goog-User-Project: QUOTA_PROJECT_ID" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
           --data '{
             "intendedEnablementState": "ENABLED",
             "name": "projects/PROJECT_ID/locations/global/securityCenterServices/external_exposure"
           }' \
           --compressed
         

Replace the following:

     * QUOTA_PROJECT_ID: the ID of the project that you use to manage quota.
     * PROJECT_ID: the ID of the project where you want to enable External Exposure.
**Note:** To enable External Exposure at the folder or organization level, replace `projects/PROJECT_ID` with `folders/FOLDER_ID` or `organizations/ORGANIZATION_ID` in the request URL and the JSON data parameter.



### Grant service agent permissions

Depending on the resource level where you enable the service, Google Cloud generates a service agent:

  * **Organization or folder level** : An organization-level or folder-level service agent is created.
  * **Project level** : A project-level service agent is created.



To grant permissions at the organization level, in a terminal, run the following `gcloud` command:
    
    
    gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
        --member="serviceAccount:service-org-ORGANIZATION_ID@gcp-sa-ee-hpsa.iam.gserviceaccount.com" \
        --role=roles/externalexposure.serviceAgent
    

Replace ORGANIZATION_ID with the numeric ID of your organization.

To grant permissions at the folder level, in a terminal, run the following `gcloud` command:
    
    
    gcloud resource-manager folders add-iam-policy-binding FOLDER_ID \
        --member="serviceAccount:service-folder-FOLDER_ID@gcp-sa-ee-hpsa.iam.gserviceaccount.com" \
        --role=roles/externalexposure.serviceAgent
    

Replace FOLDER_ID with the numeric ID of your folder.

### Grant inbound access to service perimeters

If you use VPC Service Controls, grant the External Exposure service agent inbound access to any service perimeters that protect projects that you want to scan. If you don't grant inbound access, External Exposure can't perform scans or generate findings for projects that are protected by service perimeters.

Depending on the resource level where the service is enabled, the service account identifier uses one of the following email address formats:

  * For organizations or folders:
        
        service-RESOURCE_KEYWORD-RESOURCE_ID@gcp-sa-ee-hpsa.iam.gserviceaccount.com
        

  * For projects:
        
        service-project-PROJECT_NUMBER@gcp-sa-ee.iam.gserviceaccount.com
        




Replace the following:

  * `RESOURCE_KEYWORD`: the keyword `org` or `folder`
  * `RESOURCE_ID`: the organization ID or folder ID
  * `PROJECT_NUMBER`: the project number



If you have both organization-level and project-level service accounts, apply the following steps to both of them.

To grant access, add an ingress rule to each blocking service perimeter:

  1. In the Google Cloud console, go to the **VPC Service Controls** page:

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. Select the blocking access policy and the service perimeter.

  3. Click **Edit** and then **Ingress policy**.

  4. Click **Add ingress rule** and configure the **From** block:

     1. For **Identity** , select **Selected identities & groups**.
     2. Enter the email address of the External Exposure service account.
     3. For **Source** , select **All sources**.
  5. Configure the rule's **To** block:

     1. For **Project** , select **All projects**.
     2. For **Operations or IAM roles** , select **All operations**.
  6. Click **Save**.




### Configure custom ports

Configure up to 32 custom ports per project to be scanned in addition to the standard ports listed in Performance and limitations:

### Console

  1. In the Google Cloud console, go to the **Service Enablement** page:

[Go to Service Enablement](https://console.cloud.google.com/projectselector2/security/command-center/config/services/external-exposure/enablement?supportedpurview=project,folder,organizationId)

  2. Select your organization or project.

  3. In the **External Exposure** column of the row that you want to modify, click **Settings**.

  4. In the **Custom ports** field, enter the port numbers separated by commas.

  5. Click **Save**.




### gcloud

To configure custom ports for scanning, include `service_config` in the `updateMask`, and specify the port integers in the `ports` array wrapper under the `serviceConfig` object. The following example configures custom ports `8081` and `8188` for scanning:
    
    
    curl --request PATCH \
      "https://securitycentermanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityCenterServices/external_exposure?updateMask=service_config" \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      --header "X-Goog-User-Project: QUOTA_PROJECT_ID" \
      --header "Accept: application/json" \
      --header "Content-Type: application/json" \
      --data '{
        "serviceConfig": {
          "ports": [8081, 8188]
        },
        "name": "projects/PROJECT_ID/locations/global/securityCenterServices/external_exposure"
      }' \
      --compressed
    

Replace the following:

  * QUOTA_PROJECT_ID: the ID of the project that you use to manage quota.
  * PROJECT_ID: the ID of the project where you want to configure custom ports.



### Configure scanning modules

Configure specific scanning modules to be turned on or off:

### Console

  1. In the Google Cloud console, go to the **Service Enablement** page:

[Go to Service Enablement](https://console.cloud.google.com/projectselector2/security/command-center/config/services/external-exposure/enablement?supportedpurview=project,folder,organizationId)

  2. Select your organization or project.

  3. In the **External Exposure** column of the row that you want to modify, click **Settings**.

  4. In the **Scanning modules** section, select the checkbox to enable or disable each module (such as exposed interfaces, APIs, weak credentials, or RCE).

  5. Click **Save**.




### gcloud

To enable or disable specific modules, include `modules` in the `updateMask`, and specify the enablement state for each module in the `modules` object. The following example enables `EXTERNALLY_EXPOSED_RCE_VULNERABILITY` and disables `EXTERNALLY_EXPOSED_WEAK_CREDENTIALS`:
    
    
    curl --request PATCH \
      "https://securitycentermanagement.googleapis.com/v1/projects/PROJECT_ID/locations/global/securityCenterServices/external_exposure?updateMask=modules" \
      --header "Authorization: Bearer $(gcloud auth print-access-token)" \
      --header "X-Goog-User-Project: QUOTA_PROJECT_ID" \
      --header "Accept: application/json" \
      --header "Content-Type: application/json" \
      --data '{
        "modules": {
          "EXTERNALLY_EXPOSED_RCE_VULNERABILITY": {
            "intendedEnablementState": "ENABLED"
          },
          "EXTERNALLY_EXPOSED_WEAK_CREDENTIALS": {
            "intendedEnablementState": "DISABLED"
          }
        },
        "name": "projects/PROJECT_ID/locations/global/securityCenterServices/external_exposure"
      }' \
      --compressed
    

Replace the following:

  * QUOTA_PROJECT_ID: the ID of the project that you use to manage quota.
  * PROJECT_ID: the ID of the project where you want to configure modules.



You can configure enablement states only for the following modules:

  * `EXTERNALLY_EXPOSED_UI`
  * `EXTERNALLY_EXPOSED_API`
  * `EXTERNALLY_EXPOSED_WEAK_CREDENTIALS`
  * `EXTERNALLY_EXPOSED_RCE_VULNERABILITY`
  * `EXTERNALLY_EXPOSED_ARBITRARY_DATA_READ`



All other External Exposure modules (including database, serverless workload, and load balancer storage checks) are enabled by default and don't appear on the modules configuration page.

**Note:** Active vulnerability detectors, such as remote code execution (RCE) checks, send small, safe, and well-vetted payloads that are developed and vetted by Google. We recommend keeping these active detectors enabled to ensure that critical exploitability risks are uncovered.

After External Exposure is enabled, continuous batch scans run automatically to identify exposed external IP addresses, probe running services, and validate active vulnerabilities.

## Investigate findings

After you enable External Exposure, you can view findings in the Google Cloud console or by using the CLI.

### View findings on the Findings page

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select the **External Exposure** view.



The **External Exposure** view shows only findings where the `finding_class` field is `EXTERNAL_EXPOSURE`.

### View findings on the External Exposure dashboard

To access the External Exposure dashboard, in the Google Cloud console, go to the **Risk overview > External Exposure** page:

[Go to External Exposure](https://console.cloud.google.com/projectselector2/security/command-center/overview/external-exposure?supportedpurview=organizationId,folder,project)

This dashboard is available when your scope is set to an organization, folder, or project.

For more information about this dashboard, see [Assess risk using Risk overview dashboards](https://docs.cloud.google.com/security-command-center/docs/assess-risk#external-exposure).

### Fetch findings using the CLI

To fetch active External Exposure findings using the CLI, run the following command:
    
    
    gcloud scc findings list projects/PROJECT_ID \
        --location=global \
        --filter="state=\"ACTIVE\" AND finding_class=\"EXTERNAL_EXPOSURE\""
    

Replace PROJECT_ID with the ID of the project where you want to view findings.

### Understand findings details

Findings that belong to the `EXTERNAL_EXPOSURE` class identify the type of risk and how the resource is exposed.

For a list of the granular risk categories that are generated for these findings (such as `EXTERNALLY_EXPOSED_VM_INSTANCE` or `EXTERNALLY_EXPOSED_SERVERLESS_WORKLOAD`), see [External Exposure findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#external-exposure-findings).

All `EXTERNAL_EXPOSURE` class findings include the following details:

  * **Exposed service** : The specific web application, server software, or protocol identified on the active port.
  * **Network path insights** : The network path tracing connectivity from the public internet through load balancers, forwarding rules, and backend services down to the target asset.
  * **Exposed endpoint** : The underlying target resource (for example, a Compute Engine instance or Google Kubernetes Engine (GKE) Pod).



If the exposed service or software version can be identified, the finding also lists any CVE vulnerabilities affecting it.

#### Prioritize findings with attack exposure scores

External Exposure findings integrate with attack path simulations. For more information, see [Overview of attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn). When a confirmed exposure connects to a potential lateral movement path (for example, an exposed service account that can reach a sensitive BigQuery database or Cloud Storage bucket), the finding receives an attack exposure score. You can use this score to prioritize remediating exposures that pose the greatest risk to your high-value resources.

### Monitor scan metrics

To help you confirm that External Exposure is operating successfully across your environment, the console displays continuous batch scan metrics:

  * **Last scan** : The timestamp of the most recently completed scan cycle, confirming that findings reflect a current view of your resources.
  * **Next scan** : The scheduled start time of the subsequent scan cycle.
  * **Successful projects** : The total count of projects that are successfully analyzed during the latest scan cycle.
  * **Projects excluded** : The total count of projects that were skipped because organization policies or VPC Service Controls constraints restrict the scanner from accessing the resources. When a project is skipped, Security Command Center generates one or more findings of the `SCC_ERROR` class.
  * **Exposed resources** : The total count of unique resource targets identified as publicly reachable.
  * **Exposed public ports** : The total count of distinct active external ports detected across your exposed resources.



### Identify scanner traffic in your logs

When External Exposure actively scans your external-facing resources, you might observe incoming scan requests in your service logs, such as Cloud Run request logs in Cloud Logging.

To verify that incoming requests originate from External Exposure rather than unauthorized third parties, inspect the log entry for the `userAgent` field under `httpRequest`. All active requests from the service identify themselves with the user agent `TsunamiSecurityScanner`.

The following example shows a Cloud Logging request log entry that is generated when External Exposure scans an exposed Cloud Run service:
    
    
    {
      "httpRequest": {
        "latency": "0.004745622s",
        "protocol": "HTTP/1.1",
        "remoteIp": "2600:1900:4180:5b2:0:1ae::",
        "requestMethod": "POST",
        "requestSize": "441",
        "requestUrl": "https://SERVICE_URL/mcp",
        "responseSize": "131",
        "serverIp": "2600:1900:4244:200::",
        "status": 405,
        "userAgent": "TsunamiSecurityScanner"
      },
      "insertId": "6a16af86000c7e0d0fdc1c58",
      "labels": {
        "goog-managed-by": "cloudfunctions",
        "goog-serve-source": "user-container"
      },
      "logName": "projects/PROJECT_ID/logs/run.googleapis.com%2Frequests",
      "receiveTimestamp": "2026-05-27T08:47:03.025492782Z",
      "resource": {
        "labels": {
          "configuration_name": "SERVICE_NAME",
          "location": "us-central1",
          "project_id": "PROJECT_ID",
          "revision_name": "REVISION_NAME",
          "service_name": "SERVICE_NAME"
        },
        "type": "cloud_run_revision"
      },
      "severity": "WARNING",
      "timestamp": "2026-05-27T08:47:02.811254Z"
    }
    

#### Understand HTTP status codes from scanner requests

When External Exposure probes your endpoints, you might observe spikes in HTTP `403 Forbidden` or HTTP `401 Unauthorized` responses in your request logs. This behavior is expected when access controls attempt to protect endpoints:

  * **Endpoints requiring authentication** : If you configure a workload, such as Cloud Run or Cloud Run functions, to require authentication through Identity and Access Management or Identity-Aware Proxy, then the endpoint rejects unauthenticated probes from External Exposure with an HTTP `403 Forbidden` or HTTP `401 Unauthorized` response. If you receive an HTTP `403` response, your access control policy is preventing unauthorized access.
  * **Endpoints protected by security policies** : If your load balancers or backend services use Google Cloud Armor security policies or web application firewalls, then probe requests that match deny rules return an `HTTP 403 Forbidden` response.



For more information about troubleshooting scanner logs, see [Spikes in `403 Forbidden` request logs from `TsunamiSecurityScanner`](https://docs.cloud.google.com/security-command-center/docs/troubleshooting#tsunami-scanner-403).

#### Query scanner traffic in Cloud Logging

To inspect or filter scanner traffic, you can use the following sample queries in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/building-queries):

  * Find all requests from the scanner:
        
        httpRequest.userAgent="TsunamiSecurityScanner"
        

  * Find 403 Forbidden responses from the scanner:
        
        httpRequest.userAgent="TsunamiSecurityScanner" AND httpRequest.status=403
        

  * Exclude scanner traffic from general error monitoring or alert policies:
        
        NOT httpRequest.userAgent="TsunamiSecurityScanner"
        




## Performance and limitations

  * **Supported resources:** Compute Engine instances, Google Kubernetes Engine (GKE) services and Ingress controllers, databases including Cloud SQL and AlloyDB for PostgreSQL, Managed Service for Apache Spark clusters, Cloud Run, Cloud Storage, and Gemini Enterprise Agent Platform Workbench.
  * **Refresh interval:** For information about the scan frequency of External Exposure, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview).
  * **Ports scanned:** External Exposure automatically scans for services running on a predefined baseline of common ports, grouped primarily by service type or protocol: 
    * **Administrative / shell** : 22 (SSH), 23 (Telnet), 3389 (RDP)
    * **Web / HTTP(S)** : 80, 443, 8000, 8080, 8081, 8443, 8800, 9000, 9443
    * **Databases** : 1433, 1521, 3306, 5432, 9200, 11211, 27017, 6379
    * **Kubernetes and service gateways** : 6443, 10250, 10255, 15020, 15021
    * **Other common developer tools and services** : 1099, 1880, 2323, 2375, 2376, 2379, 2746, 3000, 3100, 4040, 5000, 5173, 5678, 6006, 6274, 7001, 7002, 7077, 7860, 8001, 8042, 8083, 8088, 8090, 8111, 8123, 8153, 8154, 8188, 8265, 8500, 8501, 8787, 8888, 8890, 8983, 9001, 9010, 9090, 9091, 9092, 9100, 9870, 9876, 11434, 15672, 18080, 54321, and 61616.
  * **Custom ports** : In addition to the standard ports, you can configure up to 32 custom ports per project for scanning. For more information, see Configure custom ports.
  * **Network path insights** : Findings report one network path for an exposed resource.
  * **Load balanced VMs** : If multiple VM instances are connected to a load balancer, findings are reported for only one of the VM instances.
  * **Cloud Run finding prioritization** : Because every Cloud Run deployment receives a public URL by default, findings are evaluated against IAM and Identity-Aware Proxy (IAP) policies. If a workload is protected by IAM or IAP (returning an HTTP `403 unauthorized` response), the finding severity is downgraded to `LOW` to reduce informational noise.
  * **Network exposure path insights** : Findings do not include network exposure path insights when External Exposure is activated at the project level. To receive network exposure path insights, activate the service at the organization or folder level.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
