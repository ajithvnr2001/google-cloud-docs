---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics/
title: Use Security Health Analytics \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:49.369608+00:00
---

# Use Security Health Analytics  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Security Health Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to manage Security Health Analytics findings using Security Command Center.

Security Health Analytics is a built-in service in Security Command Center that scans the resources in your cloud environment and generates findings for any misconfigurations that it detects.

To receive Security Health Analytics findings, the service must be enabled in Security Command Center [Services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center) settings.

To create findings related to Amazon Web Services (AWS) resources, Security Command Center must be [connected to AWS](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws).

Findings from Security Health Analytics detectors are searchable in the Google Cloud console and using the Security Command Center API.

For information about the types of scans, see [Security Health Analytics scan types](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-scan-types).

For information about when to expect findings, see [Security Health Analytics detection latency](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-scan-latency).

## Before you begin

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To get the permissions that you need to manage Security Health Analytics findings, ask your administrator to grant you the following IAM roles on your organization, folder, or project: 

  * Enable and disable detectors: [Security Center Settings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`) 
  * View and filter findings: [Security Center Findings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`) 
  * Manage mute rules: [Security Center Mute Configurations Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsEditor) (`roles/securitycenter.muteConfigsEditor`) 
  * Manage security marks: [Security Center Finding Security Marks Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingSecurityMarksWriter) (`roles/securitycenter.findingSecurityMarksWriter`) 
  * Programmatically manage findings: [Security Center Findings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`) 
  * Grant inbound access to a VPC Service Controls service perimeter: [Access Context Manager Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) 
  * Complete any task on this page: [Security Center Settings Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsAdmin) (`roles/securitycenter.settingsAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable and disable detectors

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Disabling detectors can impact the state of active findings. When a detector is disabled, existing findings are automatically marked as inactive.

When you activate Security Command Center at the organization level, you can disable Security Health Analytics or specific detectors for specific folders or projects. If Security Health Analytics or detectors are turned off for folders and projects, any existing findings attached to assets in those resources are marked as inactive.

The following Security Health Analytics detectors for Google Cloud are disabled by default:

  * `ALLOYDB_AUTO_BACKUP_DISABLED`
  * `ALLOYDB_CMEK_DISABLED`
  * `BIGQUERY_TABLE_CMEK_DISABLED`
  * `BUCKET_CMEK_DISABLED`
  * `CLOUD_ASSET_API_DISABLED`
  * `DATAPROC_CMEK_DISABLED`
  * `DATASET_CMEK_DISABLED`
  * `DISK_CMEK_DISABLED`
  * `DISK_CSEK_DISABLED`
  * `NODEPOOL_BOOT_CMEK_DISABLED`
  * `PUBSUB_CMEK_DISABLED`
  * `SQL_CMEK_DISABLED`
  * `SQL_NO_ROOT_PASSWORD`
  * `SQL_WEAK_ROOT_PASSWORD`
  * `VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED`



**Note:** If you disable Security Health Analytics, Security Command Center also disables the individual Security Health Analytics modules and stores their previous enablement states. If you re-enable Security Health Analytics, Security Command Center restores the modules to their previous enablement states. 

### Console

If the Security Health Analytics service is enabled, you can set the enablement state of its individual modules.

  1. In the Google Cloud console, go to the **Modules** page for Security Health Analytics. 

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/security-health-analytics/modules?supportedpurview=organizationId,project)

  2. Select your organization or project.
  3. On the **Modules** tab, in the **Status** column, select the current status of the module that you want to enable or disable, and then select one of the following: 
     * **Enable** : Enable the module.
     * **Disable** : Disable the module.



### gcloud

The [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command updates the state of a Security Command Center service or module. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organization`, `folder`, or `project`). 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Security Health Analytics built-in detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-detectors-built-in). 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



Save the following content in a file called `request.json`: 
    
    
    {
      "MODULE_NAME": {
        "intendedEnablementState": "NEW_STATE"
      }
    }

Execute the [`gcloud scc manage services update`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc manage services update security-health-analytics \
        --RESOURCE_TYPE=RESOURCE_ID \
        --module-config-file=request.json

#### Windows (PowerShell)
    
    
    gcloud scc manage services update security-health-analytics `
        --RESOURCE_TYPE=RESOURCE_ID `
        --module-config-file=request.json

#### Windows (cmd.exe)
    
    
    gcloud scc manage services update security-health-analytics ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --module-config-file=request.json

You should receive a response similar to the following. For brevity, this example shows a subset of all Security Health Analytics modules. 
    
    
    effectiveEnablementState: ENABLED
    intendedEnablementState: ENABLED
    modules:
      ACCESS_AWSCLOUDSHELLFULLACCESS_RESTRICTED:
        effectiveEnablementState: DISABLED
      ACCESS_KEYS_ROTATED_90_DAYS_LESS:
        effectiveEnablementState: ENABLED
      ACCESS_TRANSPARENCY_DISABLED:
        effectiveEnablementState: ENABLED
      ADMIN_SERVICE_ACCOUNT:
        effectiveEnablementState: ENABLED
      ALLOYDB_AUTO_BACKUP_DISABLED:
        effectiveEnablementState: DISABLED
    name: projects/1070293378382/locations/global/securityCenterServices/SECURITY_HEALTH_ANALYTICS
    updateTime: '2026-02-11T21:15:41.269584764Z'
    

### REST

The Security Command Center Management API's `[RESOURCE_TYPE.locations.securityCenterServices.patch](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch)` method updates the state of a Security Command Center service or module. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: the type of resource to update (`organizations`, `folders`, or `projects`). 
  * `QUOTA_PROJECT`: the project ID to use for billing and quota tracking. 
  * `RESOURCE_ID`: the numeric identifier for the organization, folder, or project to update. For projects, you can also use the alphanumeric project ID. 
  * `MODULE_NAME`: the name of the module to enable or disable. For valid values, see [Security Health Analytics built-in detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-detectors-built-in). 
  * `NEW_STATE`: `ENABLED` to enable the module; `DISABLED` to disable the module; or `INHERITED` to inherit the enablement status of the parent resource (valid only for projects and folders). 



HTTP method and URL: 
    
    
    PATCH https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/security-health-analytics?updateMask=modules

Request JSON body: 
    
    
    {
      "modules": {
        "MODULE_NAME": {
          "intendedEnablementState": "NEW_STATE"
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: QUOTA_PROJECT" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/security-health-analytics?updateMask=modules"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "QUOTA_PROJECT" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://securitycentermanagement.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global/securityCenterServices/security-health-analytics?updateMask=modules" | Select-Object -Expand Content

You should receive a response similar to the following. For brevity, this example shows a subset of all Security Health Analytics modules. 
    
    
    {
      "effectiveEnablementState": "ENABLED",
      "intendedEnablementState": "ENABLED",
      "modules": {
        "ACCESS_AWSCLOUDSHELLFULLACCESS_RESTRICTED": {
          "effectiveEnablementState": "DISABLED"
        },
        "ACCESS_KEYS_ROTATED_90_DAYS_LESS": {
          "effectiveEnablementState": "ENABLED"
        },
        "ACCESS_TRANSPARENCY_DISABLED": {
          "effectiveEnablementState": "ENABLED"
        },
        "ADMIN_SERVICE_ACCOUNT": {
          "effectiveEnablementState": "ENABLED"
        },
        "ALLOYDB_AUTO_BACKUP_DISABLED": {
          "effectiveEnablementState": "DISABLED"
        }
      },
      "name": "projects/1070293378382/locations/global/securityCenterServices/SECURITY_HEALTH_ANALYTICS",
      "updateTime": "2026-02-11T21:15:41.269584764Z"
    }
    

## Filtering findings in the Google Cloud console

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

A large organization might have many vulnerability findings across their deployment to review, triage, and track. By using filters that are available on the Security Command Center **Vulnerabilities** and **Findings** pages in the Google Cloud console, you can focus on the highest severity vulnerabilities across your organization, and review vulnerabilities by asset type, project, and more.

For more information about filtering vulnerability findings, see [Filter vulnerability findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/filter-vulnerability-findings).

## Manage findings with cases

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Security Command Center automatically opens a _case_ in the Security Operations console for threats, toxic combinations, and findings related to toxic combinations. A single case can contain multiple related findings.

Use the case, which can be integrated with your preferred ticketing system, to manage the investigation and remediation of findings, by assigning owners, reviewing related information, and, with playbooks, automate your response workflow.

If a finding has a corresponding case, you can find a link to its case on the details page of the finding. Open the details page for a finding from the **Findings** page.

For more information about cases, see [Cases overview](https://docs.cloud.google.com/security-command-center/docs/cases-overview).

## Mute findings

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

To control the volume of findings in Google Cloud console, you can manually or programmatically mute individual findings, or create mute rules that automatically mute findings based on filters you define. There are two types of mute rules you can use to control finding volume:

  * Static mute rules that indefinitely mute _future_ findings.
  * Dynamic mute rules that contain an option to temporarily mute current _and_ future findings.



We recommend using dynamic mute rules exclusively to reduce the number of findings you review manually. To avoid confusion, we don't recommend using both static and dynamic mute rules simultaneously. For a comparison of the two rule types, see [Types of mute rules](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings#mute-types).

Findings that you mute in the Google Cloud console are hidden and silenced, but continue to be logged for audit and compliance purposes. You can view muted findings or unmute them at any time. To learn more, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

## Marking assets and findings with security marks

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

You can add custom properties to findings and assets in Security Command Center by using security marks. Security marks enable you to identify high-priority areas of interest like production projects, tag findings with bug and incident tracking numbers, and more.

For assets, you can add security marks only to those assets that Security Command Center supports. For the list of supported assets, see [Supported asset types in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types).

### Add assets to allowlists

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

**Allowlists with security marks deprecated** : Security Command Center deprecated this feature, and it becomes unavailable for all users on or after April 15, 2025. Until then, this feature is available only in instances of Security Command Center that you activated before June 26, 2023. If you activated Security Command Center on or after June 26, 2023, use the mute feature to suppress findings for certain assets.

For more information, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

Although it is not a recommended method, you can suppress unneeded findings by adding dedicated security marks to assets so that the Security Health Analytics detectors don't create security findings for those assets.

The recommended and most effective approach for controlling finding volume is to Mute findings. Mute findings that you don't need to review, because they are either for assets that are isolated or because the findings fall within acceptable business parameters.

When you apply dedicated security marks to assets, the assets are added to an allowlist in Security Health Analytics, which marks any findings for those assets as resolved during the next batch scan.

Dedicated security marks must be applied directly to assets, not findings, as described in How allowlists work later on this page. If you apply a mark to a finding, the underlying asset can still generate findings.

#### How allowlists work

Each Security Health Analytics detector has a dedicated mark type for allowlists, in the form of `allow_FINDING_TYPE:true`. Adding this dedicated mark to an asset that is supported by Security Command Center lets you exclude the asset from the detection policy.

For example, to exclude the finding type `SSL_NOT_ENFORCED`, set the security mark, `allow_ssl_not_enforced:true`, on the related Cloud SQL instance. The specified detector won't create findings for marked assets.

**Note:** Assets on allowlists are still scanned by detectors, but findings are suppressed and not written to Security Command Center.

For a complete list of finding types, see the [Security Health Analytics detectors list](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors). To learn more about asset security marks and techniques for using them, see [Annotate assets with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets).

#### Asset types

This section describes how security marks work for different assets.

  * **Allowlist assets:** When you add a dedicated mark to an asset, like a Cloud Storage bucket or firewall, the associated finding is marked as resolved when the next batch scan runs. The detector won't generate new findings or update existing findings for the asset until the mark is removed.

  * **Allowlist projects** : When you add a mark to a project resource, findings for which the project itself is the scanned, or target, resource are resolved. However, assets contained within the project, such as virtual machines or crypto keys, can still generate findings. This security mark is only available if you activate Security Command Center Premium tier at the organization level.

  * **Allowlist folders** : When you add a mark to a folder resource, findings for which the folder itself is the scanned, or target, resource are resolved. However, assets contained within the folder, including projects, can still generate findings. This security mark is only available if you activate Security Command Center Premium tier at the organization level.

  * **Detectors that support multiple assets** : If a detector supports more than one asset type, you must apply the dedicated mark to each asset. For example, the `KMS_PUBLIC_KEY` detector supports `CryptoKey` and `KeyRing` Cloud Key Management Service assets. If you apply the mark `allow_kms_public_key:true` to the `CryptoKey` asset, then `KMS_PUBLIC_KEY` findings for that asset are resolved. However, findings can still be generated for the `KeyRing` asset.




Security marks are only updated during batch scans, not real-time scans. If a dedicated security mark is removed, and the asset has a vulnerability, it might take up to 24 hours before the mark is deleted and a finding is written.

### Special-case detector: Customer Supplied Encryption Keys

The [`DISK_CSEK_DISABLED`](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics-findings#compute-instance-findings) detector isn't on by default. To use this detector, you must mark the assets for which you want to use self-managed encryption keys.

To enable the `DISK_CSEK_DISABLED` detector for specific assets, [apply the security mark](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets) `enforce_customer_supplied_disk_encryption_keys` to the asset with a value of `true`.

## Viewing active finding count by finding type

You can use the Google Cloud console or the Google Cloud CLI to view active finding counts by finding type.

###  Console 

The Google Cloud console lets you view a count of active findings for each finding type.

To view Security Health Analytics findings by finding type, do the following:

  1. To display Security Health Analytics findings, go to the legacy **Vulnerabilities** page.

[Go to Vulnerabilities](https://console.cloud.google.com/security/command-center/vulnerabilities)

  2. To sort findings by the number of active findings for each finding type, click the **Active** column header.




###  gcloud 

To use the gcloud CLI to get a count of all active findings, you query Security Command Center to get the Security Health Analytics source ID. Then you use the source ID to query the active findings count.

### Step 1: Get the source ID

To get the source ID, run one of the following commands:

  * If you activated Security Command Center at the organization level, run the following command:
        
        gcloud scc sources describe organizations/ORGANIZATION_ID \
            --source-display-name="Security Health Analytics"
        

  * If you activated Security Command Center at the project level, run the following command:
        
        gcloud scc sources describe projects/PROJECT_ID \
            --source-display-name="Security Health Analytics"
        




If you haven't already enabled the Security Command Center API, you are prompted to enable it. When the Security Command Center API is enabled, run the previous command again. The command should display output like the following:
    
    
    description: Scans for deviations from a GCP security baseline.
    displayName: Security Health Analytics
    name: organizations/ORGANIZATION_ID/sources/SOURCE_ID
    

Note the `SOURCE_ID` to use in the next step.

### Step 2: Get the active findings count

Use the `SOURCE_ID` you noted in the previous step to filter findings from Security Health Analytics. The following gcloud CLI commands return a count of findings by category.

  * If you activated Security Command Center at the organization level, run the following command:
        
        gcloud scc findings group organizations/ORGANIZATION_ID/sources/SOURCE_ID \
            --group-by=category --page-size=PAGE_SIZE
        

  * If you activated Security Command Center at the project level, run the following command:
        
        gcloud scc findings group projects/PROJECT_ID/sources/SOURCE_ID \
            --group-by=category --page-size=PAGE_SIZE
        




You can set the page size to any value up to 1000. The command should display output like the following, with results from your organization:
    
    
    groupByResults:
    - count: '1'
    properties:
      category: MFA_NOT_ENFORCED
    - count: '3'
    properties:
      category: ADMIN_SERVICE_ACCOUNT
    - count: '2'
    properties:
      category: API_KEY_APIS_UNRESTRICTED
    - count: '1'
    properties:
      category: API_KEY_APPS_UNRESTRICTED
    - count: '2'
    properties:
      category: API_KEY_EXISTS
    - count: '10'
    properties:
      category: AUDIT_CONFIG_NOT_MONITORED
    - count: '10'
    properties:
      category: AUDIT_LOGGING_DISABLED
    - count: '1'
    properties:
      category: AUTO_UPGRADE_DISABLED
    - count: '10'
    properties:
      category: BUCKET_IAM_NOT_MONITORED
    - count: '10'
    properties:
      category: BUCKET_LOGGING_DISABLED
    nextPageToken: TOKEN
    readTime: '2023-08-05T21:56:13.862Z'
    totalSize: 50
    

## Programmatically manage findings

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Using the Google Cloud CLI and the Security Command Center client libraries, you can automate almost anything you can do with Security Command Center in the Google Cloud console. You can also remediate many findings using the gcloud CLI. For more information, review the documentation for the resource types described in each finding:

  * [Listing security findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings)
  * [Creating, modifying, and querying security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-api-add-manage-security-marks)
  * [Creating and updating security findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-findings)
  * [Creating, updating, and listing finding sources](https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-security-sources)
  * [Configuring organization settings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-configure-asset-discovery)



To export or list assets programmatically, use the Cloud Asset Inventory API. For more information, see [Export asset history and metadata](https://docs.cloud.google.com/asset-inventory/docs/overview#export_asset_history_and_metadata).

The asset methods and fields of the Security Command Center API are deprecated and will be removed on or after June 26, 2024.

Until they are removed, users who activated Security Command Center before June 26, 2023 can use the asset methods of the Security Command Center API to list assets, but these methods support only the assets that [Security Command Center supports](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types).

For information about using the deprecated asset API methods, see [listing assets](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-assets).

## Scanning projects protected by a service perimeter

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

If you have a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview) that blocks access to certain projects and services, you must grant the Security Command Center service account inbound and outbound access to that service perimeter. Otherwise, Security Health Analytics can't produce findings related to the protected projects and services.

**Note:** Security Command Center provides error detectors, which report configuration errors that prevent Security Command Center and its services from working properly. If you have a `VPC Service Controls Restriction` (`VPC_SC_RESTRICTION`) error finding, see [VPC Service Controls Restriction](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#vpc_service_controls_restriction).

### Console

#### Navigate to the service perimeter

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/projectselector2/security/service-perimeter?supportedpurview=organizationId)

  2. Select your organization.
  3. In the drop-down list, select the access policy that contains the service perimeter that you want to grant access to.

The service perimeters associated with the access policy appear in the list.

  4. Click the name of the service perimeter that you want to update.

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
         
         accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME

  5. Click edit **Edit**.



#### Add an egress rule

  1. Click **Egress policy**.
  2. Click **Add an egress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/security-command-center/docs/access-control-org#service-agent). This address has the following format: 
            
            service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com

Replace `ORGANIZATION_ID` with your organization ID.

     4. Select the service agent or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **All projects**.
     2. For **Operations or IAM roles** , select **Select operations**. 
     3. Click **Add operations** , and then add the following operations:

        * Add the **bigquery.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **binaryauthorization.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudkms.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **logging.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **monitoring.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudresourcemanager.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **storage.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **compute.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **iam.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **container.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.



#### Add an ingress rule

  1. Click **Ingress policy**.
  2. Click **Add an ingress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/security-command-center/docs/access-control-org#service-agent). This address has the following format: 
            
            service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com

Replace `ORGANIZATION_ID` with your organization ID.

     4. Select the service agent or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **All projects**.
     2. For **Operations or IAM roles** , select **Select operations**. 
     3. Click **Add operations** , and then add the following operations:

        * Add the **bigquery.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **binaryauthorization.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudkms.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **logging.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **monitoring.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **cloudresourcemanager.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **storage.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **compute.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **iam.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
        * Add the **container.googleapis.com** service. 
          1. Click **All methods**.
          2. Click **Add all methods**.
  5. Click **Save**.



### gcloud

**Warning:** The `--set-ingress-policies` and `--set-egress-policies` flags replace all existing ingress or egress policies in the perimeter. If you have existing policies, you must retrieve them first, add the new policy to the appropriate ingress or egress YAML file, and then run the update command. 

  1. If a quota project isn't already set, then set it. Choose a project that has the Access Context Manager API enabled. 
         
         gcloud config set billing/quota_project QUOTA_PROJECT_ID

Replace `QUOTA_PROJECT_ID` with the ID of the project that you want to use for billing and quota. 

  2. Create a file named `egress-rule.yaml` with the following contents:
         
         - egressFrom:
             identities:
             - serviceAccount:service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com
           egressTo:
             operations:
             - serviceName: bigquery.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: binaryauthorization.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudkms.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: logging.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: monitoring.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudresourcemanager.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: storage.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: iam.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: container.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - '*'

Alternatively, you can use `operations` to specify services for which VPC Service Controls violations appear and `resources` to specify the project that appeared in the finding. 

Replace `ORGANIZATION_ID` with your organization ID.

  3. Create a file named `ingress-rule.yaml` with the following contents:
         
         - ingressFrom:
             identities:
             - serviceAccount:service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: bigquery.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: binaryauthorization.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudkms.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: logging.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: monitoring.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: cloudresourcemanager.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: storage.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: compute.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: iam.googleapis.com
               methodSelectors:
               - method: '*'
             - serviceName: container.googleapis.com
               methodSelectors:
               - method: '*'
             resources:
             - '*'

Alternatively, you can use `operations` to specify services for which VPC Service Controls violations appear and `resources` to specify the project that appeared in the finding. 

Replace `ORGANIZATION_ID` with your organization ID.

  4. Add the egress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-egress-policies=egress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME

  5. Add the ingress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-ingress-policies=ingress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME




### Terraform

To configure the perimeter using Terraform, see the following sample:
    
    
    locals {
      access_policy_id    = "123456789012"
      perimeter_name      = "my_service_perimeter"
      project_number      = "123456789012"
      sha_service_account = "service-{project_number}@gcp-sa-scc.iam.gserviceaccount.com"
    }
    
    resource "google_access_context_manager_service_perimeter_ingress_policy" "scc_sha_ingress" {
      perimeter = "accessPolicies/${local.access_policy_id}/servicePerimeters/${local.perimeter_name}"
    
      ingress_from {
        identities = [
          "serviceAccount:${local.sha_service_account}"
        ]
        sources {
          access_level = "*"
        }
      }
    
      ingress_to {
        resources = [
          "projects/${local.project_number}"
        ]
        # Add operations for each service SHA scans (e.g., compute, storage, bigquery)
        operations {
          service_name = "compute.googleapis.com"
          method_selectors {
            # Least privilege is recommended. For broad scanning, broad access might be retained,
            # but consider replacing "*" with specific read methods (e.g., compute.v1.InstancesService.Get)
            method = "*"
          }
        }
        operations {
          service_name = "storage.googleapis.com"
          method_selectors {
            method = "*"
          }
        }
      }
    }
    
    resource "google_access_context_manager_service_perimeter_egress_policy" "scc_sha_egress" {
      perimeter = "accessPolicies/${local.access_policy_id}/servicePerimeters/${local.perimeter_name}"
    
      egress_from {
        identities = [
          "serviceAccount:${local.sha_service_account}"
        ]
      }
    
      egress_to {
        resources = [
          "projects/${local.project_number}"
        ]
        operations {
          service_name = "compute.googleapis.com"
          method_selectors {
            method = "*"
          }
        }
        operations {
          service_name = "storage.googleapis.com"
          method_selectors {
            method = "*"
          }
        }
      }
    }

For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). 

### Services that Security Health Analytics calls

To function, Security Health Analytics requires access to the Google Cloud APIs of the services that it scans, as well as core infrastructure services. Depending on your configuration, you might need to allow ingress or egress for the following services in your VPC Service Controls perimeters:

  * BigQuery API (`bigquery.googleapis.com`)
  * Binary Authorization API (`binaryauthorization.googleapis.com`)
  * Cloud Key Management Service API (`cloudkms.googleapis.com`)
  * Cloud Logging API (`logging.googleapis.com`)
  * Cloud Monitoring API (`monitoring.googleapis.com`)
  * Cloud Resource Manager API (`cloudresourcemanager.googleapis.com`)
  * Cloud Storage API (`storage.googleapis.com`)
  * Compute Engine API (`compute.googleapis.com`)
  * Identity and Access Management API (`iam.googleapis.com`)
  * Kubernetes Engine API (`container.googleapis.com`)



## What's next

  * Learn about [Security Health Analytics detectors and findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).
  * Read recommendations for [remediating Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings).
  * Learn how to [use Security Command Center security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings).
  * Learn about [cases](https://docs.cloud.google.com/security-command-center/docs/cases-overview).
  * Learn more about [using Security Command Center Standard or Premium in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center) to review assets and findings.
  * Learn more about [using Security Command Center Enterprise in the Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/scce-consoles-overview). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
