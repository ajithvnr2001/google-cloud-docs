---
url: https://docs.cloud.google.com/assured-workloads/docs/monitor-folder/
title: Monitor an Assured Workloads folder for violations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:40.868755+00:00
---

# Monitor an Assured Workloads folder for violations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/monitor-folder/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor an Assured Workloads folder for violations

Assured Workloads actively monitors your Assured Workloads folders for compliance violations by comparing the requirements of a folder's [control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) with the following details:

  * **Organization policy** : Each Assured Workloads folder is configured with specific organization policy constraint settings that help to ensure compliance. When these settings are changed in a non-compliant manner, a violation occurs. See the Monitored organization policy violations section for more information.
  * **Resources** : Depending on your Assured Workloads folder's organization policy settings, the resources beneath the folder may be restricted, such as their type and location. See the Monitored resource violations section for more information. If any resources are non-compliant, a violation occurs.



When a violation occurs, you can resolve them or create exceptions for them where appropriate. A violation can have one of three statuses:

  * **Unresolved:** The violation hasn't been addressed, or was previously granted an exception before non-compliant changes were made on the folder or resource.
  * **Resolved:** The violation has been addressed by following steps to remediate the issue.
  * **Exception:** The violation has been granted an exception, and a business justification has been provided.



Assured Workloads monitoring is automatically enabled when you create an Assured Workloads folder.

## Before you begin

### Required IAM roles and permissions

To view organization policy violations or resource violations, you must be granted an IAM role on the parent organization of the Assured Workloads folder that contains the following permissions:

  * `assuredworkloads.violations.get`
  * `assuredworkloads.violations.list`



These permissions are included in the following Assured Workloads IAM roles:

  * **Assured Workloads Administrator** (`roles/assuredworkloads.admin`)
  * **Assured Workloads Editor** (`roles/assuredworkloads.editor`)
  * **Assured Workloads Reader** (`roles/assuredworkloads.reader`)



To enable resource violation monitoring, you must be granted an IAM role on the parent organization of the Assured Workloads folder that contains the following permissions:

  * `assuredworkloads.workload.update`: This permission is included in the following roles:

    * **Assured Workloads Administrator** (`roles/assuredworkloads.admin`)
    * **Assured Workloads Editor** (`roles/assuredworkloads.editor`)
  * `resourcemanager.folders.setIamPolicy`: This permission is included in administrative roles, such as the following:

    * **Organization Administrator** (`roles/resourcemanager.organizationAdmin`)
    * **Security Admin** (`roles/iam.securityAdmin`)



To provide exceptions for compliance violations, you must be granted an IAM role on the parent organization of the Assured Workloads folder that contains the following permission:

  * `assuredworkloads.violations.update`: This permission is included in the following roles:

    * **Assured Workloads Administrator** (`roles/assuredworkloads.admin`)
    * **Assured Workloads Editor** (`roles/assuredworkloads.editor`)



Additionally, to resolve organization policy violations and to view audit logs, the following IAM roles must be granted:

  * **Organization Policy Administrator** (`roles/orgpolicy.policyAdmin`)
  * **Logs Viewer** (`roles/logging.viewer`)

**Note:** When [granting a role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) in the Google Cloud console, the **Organization Policy Administrator** role is only visible if you switch to an organization first, or if you click **Manage roles**.

## Set up violation email notifications

**Note:** Email notifications are not available for resource violations.

When an organization compliance violation occurs or is resolved or when an exception is made, members of the **Legal** category in [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) are emailed by default. This behavior is necessary because your legal team needs to be kept up to date with any regulatory compliance issues.

Your team who manages the violations, whether that be a security team or otherwise, should also be [added to the Legal category as contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#add). This ensures that they are sent email notifications as changes occur.

### Enable or disable notifications

To enable or disable notifications for a specific Assured Workloads folder:

  1. Go to the **Assured Workloads** page in the Google Cloud console:

[Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

  2. In the **Name** column, click the name of the Assured Workloads folder whose notification settings you want to change.

  3. In the **Assured Workloads Monitoring** card, clear the **Enable notifications** checkbox to disable notifications, or select it to enable notifications for the folder.




On the **Assured Workloads folders** page, folders that have notifications disabled show unsubscribe **Monitoring email notifications disabled**.

## View violations in your organization

You can view violations across your organization in both the Google Cloud console and the gcloud CLI.

###  Console 

You can view how many violations there are across your organization on either the **Assured Workloads** page in the **Compliance** section of the Google Cloud console or the **Monitoring** page in the **Compliance** section.

### Assured Workloads page

Go to the **Assured Workloads** page to view violations at a glance:

[Go to Assured Workloads](https://console.cloud.google.com/compliance/assuredworkloads)

At the top of the page, a summary of organization policy violations and resource violations is shown. Click the **View** link to go to the **Monitoring** page.

For each Assured Workloads folder in the list, any violations are shown in the **Org policy violations** and **Resource violations** columns. Unresolved violations have the error icon active, and exceptions have the warning icon active. You can select a violation or exception to see more details.

If resource violation monitoring is not enabled on a folder, the settings icon is active in the **Updates** column with an **Enable Resource violation monitoring** link. Click the link to enable the feature. You can also enable it by clicking the **Enable** button on the Assured Workloads folder details page.

**Note:** You receive an error message if you don't have the required permissions to enable resource violation monitoring. Grant a role that contains the required permissions and try again.

### Monitoring page

Go to the **Monitoring** page to view violations in more detail:

[Go to Monitoring](https://console.cloud.google.com/compliance/monitoring)

Two tabs are shown: **Organization Policy Violations** and **Resource Violations**. If more than one unresolved violation exists, the error icon is active on the tab.

In either tab, unresolved violations are shown by default. See the View violation details section below for more information.

###  gcloud CLI 

To list the current compliance violations in your organization, run the following command:
    
    
    gcloud assured workloads violations list --location=LOCATION --organization=ORGANIZATION_ID --workload=WORKLOAD_ID
    

Where:

  * LOCATION is the [location](https://docs.cloud.google.com/assured-workloads/docs/locations) of the Assured Workloads folder.

  * ORGANIZATION_ID is the [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) to query.

  * WORKLOAD_ID is the parent workload ID, which can be found by [listing your workloads](https://docs.cloud.google.com/sdk/gcloud/reference/assured/workloads/list).




The response includes the following information for each violation:

  * An audit log link for the violation.
  * The first time the violation occurred.
  * The type of violation.
  * A description of the violation.
  * The name of the violation, which can be used to retrieve more details.
  * The affected organization policy, and the related policy constraint.
  * The violation's current state. Valid values are unresolved, resolved, or exception.



For optional flags, see the [Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/list).

## View violation details

To view specific compliance violations and their details, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/compliance/monitoring)

On the **Monitoring** page, the **Organization Policy Violations** tab is selected by default. This tab displays all unresolved organization policy violations across Assured Workloads folders in the organization.

The **Resource Violations** tab displays all unresolved violations associated with the resource across all Assured Workloads folders in the organization.

  2. For either tab, use the **Quick filters** options to filter by violation status, violation type, control package type, violation type, specific folders, specific organization policy constraints, or specific resource types.

  3. For either tab, if there are existing violations, click a violation ID to see more detailed information.




From the **Violation details** page, you can perform the following tasks:

  * Copy the violation ID.

  * View the Assured Workloads folder where the violation has happened, and what time it first occurred.

  * View the audit log, which includes:

    * When the violation happened.

    * Which policy was modified to cause the violation, and which user made that modification.

    * If an exception was granted, which user granted it.

    * Where applicable, view the specific resource the violation occurred on.

  * View the affected organization policy.

  * View and add compliance violation exceptions. A list of previous exceptions for the folder or resource are shown, including the user that granted the exception and its user-provided justification.


**Note:** If any additional non-compliant changes are made beyond the scope of the original exception, a new unresolved violation will occur. Information about the new unresolved violation and its cause will be shown on this page.

  * Follow the remediation steps to resolve the exception.



For organization policy violations, you can also see the following:

  * **Affected organization policy** : To view the specific policy associated with the compliance violation, click **View Policy**.
  * **Child resource violations** : Resource-based organization policy violations can cause child resource violations. To view or resolve child resource violations, click the **Violation ID**.



For resource violations, you can also see the following:

  * **Parent organization policy violations** : When parent organization policy violations are the cause of a child resource violation, they need to be addressed at the parent level. To see the parent violation details, click **View Violation**.
  * Any other violations on the specific resource that is causing the resource violation are also visible.



###  gcloud CLI 

To view a compliance violation's details, run the following command:
    
    
    gcloud assured workloads violations describe VIOLATION_PATH
    

Where VIOLATION_PATH is in the following format:
    
    
    ORGANIZATION_ID/locations/LOCATION/workloads/WORKLOAD_ID/violations/VIOLATION_ID
    

The VIOLATION_PATH is returned in the list response's `name` field for each violation.

The response includes the following information:

  * An audit log link for the violation.

  * The first time the violation occurred.

  * The type of violation.

  * A description of the violation.

  * The affected organization policy, and the related policy constraint.

  * Remediation steps to resolve the violation.

  * The violation's current state. Valid values are `unresolved`, `resolved`, or `exception`.




For optional flags, see the [Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/describe).

## Resolve violations

To remediate a violation, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/compliance/monitoring)

  2. Click the violation ID to see more detailed information.

  3. In the **Remediation** section, follow the instructions for the Google Cloud console or CLI to address the issue.




###  gcloud CLI 

  1. View the violation details using the gcloud CLI.

  2. Follow the remediation steps in the response to resolve the violation.




## Add violation exceptions

Sometimes a violation might be valid for a particular situation. You can acknowledge one or more violations by completing the following steps to add an exception.

**Note:** If you've previously granted a violation exception, its state can change back to **unresolved** if any additional non-compliant changes are made.

###  Console 

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/compliance/monitoring)

  2. From the list of violations, select one or more that you want to add an exception for. You can acknowledge up to 100 organization policy violations and up to 400 resource violations in a single operation. Click **Acknowledge**.

  3. Enter a business justification for the exception. If you selected more than one violation, this exception will apply to all of them. For organization policy violations, if you want the exception to apply to all child resources, select the **Apply to all existing child resource violations** checkbox. Click **Submit**.




The violation status is now set to **Exception**.

###  gcloud CLI 

To add an exception for a violation, run the following command:
    
    
    gcloud assured workloads violations acknowledge VIOLATION_PATH --comment="BUSINESS_JUSTIFICATION"
    

Where BUSINESS_JUSTIFICATION is the reason for the exception, and VIOLATION_PATH is in the following format:
    
    
    ORGANIZATION_ID/locations/LOCATION/workloads/WORKLOAD_ID/violations/VIOLATION_ID
    

The VIOLATION_PATH is returned in the list response's `name` field for each violation.

After successfully sending the command, the violation status is set to **Exception**.

## Monitored organization policy violations

Assured Workloads monitors different organization policy constraint violations, depending on the control package applied to your Assured Workloads folder. Use the following list to filter violations by their affected control package.

Data Boundary for CJISData Boundary for FedRAMP ModerateData Boundary for FedRAMP HighUS Data Boundary for Healthcare and Life SciencesUS Data Boundary for Healthcare and Life Sciences with SupportData Boundary for Data Boundary for Impact Level 2 (IL2)Data Boundary for Impact Level 4 (IL4)Data Boundary for Impact Level 5 (IL5)Data Boundary for International Traffic in Arms Regulations (ITAR)Australia Data BoundaryAustralia Data Boundary and SupportBrazil Data BoundaryCanada Data BoundaryCanada Data Boundary and SupportData Boundary for Canada Protected BChile Data BoundaryEU Data BoundaryEU Data Boundary and SupportEU Data Boundary with Access JustificationsHong Kong Data BoundaryIndia Data BoundaryIndonesia Data BoundaryIsrael Data BoundaryIsrael Data Boundary and SupportJapan Data BoundaryQatar Data BoundarySingapore Data BoundarySouth Africa Data BoundarySouth Korea Data BoundarySwitzerland Data BoundaryTaiwan Data BoundaryUK Data BoundaryUS Data BoundaryUS Data Boundary and SupportLocal Controls by S3NS (Sovereign Controls by Partners)Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)T-Systems Sovereign Cloud (Sovereign Controls by Partners)Show all control packages

**Organization policy constraint** | **Violation type** | **Description** | **Affected control packages**  
---|---|---|---  
Non-compliant access to Cloud SQL data | Access |  Occurs when non-compliant access to non-compliant Cloud SQL diagnostic data is allowed. This violation is caused by changing the control package's compliant value for the **`sql.restrictNoncompliantDiagnosticDataAccess` ** constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant access to Compute Engine data | Access |  Occurs when non-compliant access to Compute Engine instance data is allowed. This violation is caused by changing the control package's compliant value for the `compute.disableInstanceDataAccessApis` constraint. |  |   
---  
Data Boundary for Criminal Justice Information Systems (CJIS)  
EU Data Boundary with Access Justifications  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant Cloud Storage authentication types | Access |  Occurs when non-compliant authentication types are allowed for use with Cloud Storage. This violation is caused by changing the control package's compliant value for the `storage.restrictAuthTypes` constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant access to Cloud Storage buckets | Access |  Occurs when non-compliant non-uniform bucket-level access to Cloud Storage is allowed. This violation is caused by changing the control package's compliant value for the `storage.uniformBucketLevelAccess` constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant access to GKE data | Access |  Occurs when non-compliant access to GKE diagnostic data is allowed. This violation is caused by changing the control package's compliant value for the `container.restrictNoncompliantDiagnosticDataAccess` constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Data Boundary for Impact Level 4 (IL4)  
Impact Level 5 (IL5)  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant Compute Engine diagnostic features | Configuration |  Occurs when non-compliant Compute Engine diagnostic features have been enabled. This violation is caused by changing the control package's compliant value for the `compute.enableComplianceMemoryProtection` constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant Compute Engine global load balancing setting | Configuration |  Occurs when a non-compliant value has been set for the global load balancing setting in Compute Engine. This violation is caused by changing the control package's compliant value for the `compute.disableGlobalLoadBalancing` constraint. |  |   
---  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Non-compliant Compute Engine FIPS setting | Configuration |  Occurs when a non-compliant value has been set for the FIPS setting in Compute Engine. This violation is caused by changing the control package's compliant value for the `compute.disableNonFIPSMachineTypes` constraint. |  |   
---  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Non-compliant Compute Engine SSL setting | Configuration |  Occurs when a non-compliant value has been set for global self-managed certificates. This violation is caused by changing the control package's compliant value for the `compute.disableGlobalSelfManagedSslCertificate` constraint. |  |   
---  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Non-compliant Compute Engine SSH in browser setting | Configuration |  Occurs when a non-compliant value has been set for the SSH in browser feature in Compute Engine. This violation is caused by changing the control package's compliant value for the `compute.disableSshInBrowser` constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant Cloud SQL resource creation | Configuration |  Occurs when non-compliant Cloud SQL resource creation is allowed. This violation is caused by changing the control package's compliant value for the `sql.restrictNoncompliantResourceCreation` constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Missing Cloud KMS key restriction | Encryption |  Occurs when no projects are specified to provide encryption keys for [ CMEK ](https://docs.cloud.google.com/kms/docs/cmek).  This violation is caused by changing the control package's compliant value for the `gcp.restrictCmekCryptoKeyProjects` constraint, which helps to prevent unapproved folders or projects from providing encryption keys. |  |   
---  
EU Data Boundary with Access Justifications  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Data Boundary for Criminal Justice Information Systems (CJIS)  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant non-CMEK-enabled service | Encryption |  Occurs when a service that does not support [ CMEK ](https://docs.cloud.google.com/kms/docs/cmek) is enabled for the workload.  This violation is caused by changing the control package's compliant value for the `gcp.restrictNonCmekServices` constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Data Boundary for Criminal Justice Information Systems (CJIS)  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant Cloud KMS protection levels | Encryption |  Occurs when non-compliant protection levels are specified for use with Cloud Key Management Service (Cloud KMS). See the [ Cloud KMS reference ](https://docs.cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel) for more information.  This violation is caused by changing the control package's compliant value for the `cloudkms.allowedProtectionLevels` constraint. |  |   
---  
EU Data Boundary with Access Justifications  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant resource locations | Resource location |  Occurs when resources of supported services for a given Assured Workloads control package are either created outside of the allowed region for the workload or moved from an allowed location to a disallowed location. This violation is caused by changing the control package's compliant value for the [ `gcp.resourceLocations` ](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) constraint.  |  |   
---  
Data Boundary for Criminal Justice Information Systems (CJIS)  
Data Boundary for FedRAMP Moderate  
Data Boundary for FedRAMP High  
US Data Boundary for Healthcare and Life Sciences  
US Data Boundary for Healthcare and Life Sciences with Support  
Data Boundary for Impact Level 2 (IL2)  
Data Boundary for Impact Level 4 (IL4)  
Data Boundary for Impact Level 5 (IL5)  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Australia Data Boundary  
Australia Data Boundary and Support  
Brazil Data Boundary  
Canada Data Boundary  
Canada Data Boundary and Support  
Data Boundary for Canada Protected B  
Chile Data Boundary  
EU Data Boundary  
EU Data Boundary and Support  
EU Data Boundary with Access Justifications  
Hong Kong Data Boundary  
India Data Boundary  
Indonesia Data Boundary  
Israel Data Boundary  
Israel Data Boundary and Support  
Japan Data Boundary  
Qatar Data Boundary  
Singapore Data Boundary  
South Africa Data Boundary  
South Korea Data Boundary  
Switzerland Data Boundary  
Taiwan Data Boundary  
UK Data Boundary  
US Data Boundary  
US Data Boundary and Support  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant services | Service usage |  Occurs when a user enables a service that is not supported by a given Assured Workloads control package in an Assured Workloads folder. This violation is caused by changing the control package's compliant value for the `gcp.restrictServiceUsage` constraint. |  |   
---  
Data Boundary for Criminal Justice Information Systems (CJIS)  
Data Boundary for FedRAMP Moderate  
Data Boundary for FedRAMP High  
US Data Boundary for Healthcare and Life Sciences  
US Data Boundary for Healthcare and Life Sciences with Support  
Data Boundary for Impact Level 2 (IL2)  
Data Boundary for Impact Level 4 (IL4)  
Data Boundary for Impact Level 5 (IL5)  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Australia Data Boundary  
Australia Data Boundary and Support  
Brazil Data Boundary  
Canada Data Boundary  
Canada Data Boundary and Support  
Data Boundary for Canada Protected B  
Chile Data Boundary  
EU Data Boundary  
EU Data Boundary and Support  
EU Data Boundary with Access Justifications  
Hong Kong Data Boundary  
India Data Boundary  
Indonesia Data Boundary  
Israel Data Boundary  
Israel Data Boundary and Support  
Japan Data Boundary  
Qatar Data Boundary  
Singapore Data Boundary  
South Africa Data Boundary  
South Korea Data Boundary  
Switzerland Data Boundary  
Taiwan Data Boundary  
UK Data Boundary  
US Data Boundary  
US Data Boundary and Support  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
  
## Monitored resource violations

Assured Workloads monitors different resource violations, depending on the control package applied to your Assured Workloads folder. To see which resource types are monitored, see [Supported resource types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types#supported_resource_types) in the Cloud Asset Inventory documentation. Use the following list to filter violations by their affected control package:

Data Boundary for Criminal Justice Information Systems (CJIS)Data Boundary for FedRAMP ModerateData Boundary for FedRAMP HighUS Data Boundary for Healthcare and Life SciencesUS Data Boundary for Healthcare and Life Sciences with SupportData Boundary for Impact Level 2 (IL2)Data Boundary for Impact Level 4 (IL4)Data Boundary for Impact Level 5 (IL5)Data Boundary for International Traffic in Arms Regulations (ITAR)Australia Data BoundaryAustralia Data Boundary and SupportBrazil Data BoundaryCanada Data BoundaryCanada Data Boundary and SupportData Boundary for Canada Protected BChile Data BoundaryEU Data BoundaryEU Data Boundary and SupportEU Data Boundary with Access JustificationsHong Kong Data BoundaryIndia Data BoundaryIndonesia Data BoundaryIsrael Data BoundaryIsrael Data Boundary and SupportJapan Data BoundaryQatar Data BoundarySingapore Data BoundarySouth Africa Data BoundarySouth Korea Data BoundarySwitzerland Data BoundaryTaiwan Data BoundaryUK Data BoundaryUS Data BoundaryUS Data Boundary and SupportLocal Controls by S3NS (Sovereign Controls by Partners)Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)T-Systems Sovereign Cloud (Sovereign Controls by Partners)Show all control packages

**Organization policy constraint** | **Description** | **Affected control packages**  
---|---|---  
Non-compliant resource location |  Occurs when a resource's location is in a non-compliant region. This violation is caused by the **`gcp.resourceLocations` ** constraint. |  |   
---  
Australia Data Boundary and Support  
Data Boundary for Canada Protected B  
Canada Data Boundary and Support  
Data Boundary for Criminal Justice Information Systems (CJIS)  
EU Data Boundary and Support  
EU Data Boundary with Access Justifications  
Data Boundary for FedRAMP Moderate  
Data Boundary for FedRAMP High  
US Data Boundary for Healthcare and Life Sciences  
US Data Boundary for Healthcare and Life Sciences with Support  
Data Boundary for Impact Level 4 (IL4)  
Data Boundary for Impact Level 5 (IL5)  
Israel Data Boundary and Support  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Japan Data Boundary  
US Data Boundary and Support  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Non-compliant resources in folder |  Occurs when a resource for an unsupported service is created in the Assured Workloads folder. This violation is caused by the **`gcp.restrictServiceUsage` ** constraint. |  |   
---  
Data Boundary for Criminal Justice Information Systems (CJIS)  
Data Boundary for FedRAMP Moderate  
Data Boundary for FedRAMP High  
US Data Boundary for Healthcare and Life Sciences  
US Data Boundary for Healthcare and Life Sciences with Support  
Data Boundary for Impact Level 2 (IL2)  
Data Boundary for Impact Level 4 (IL4)  
Data Boundary for Impact Level 5 (IL5)  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Australia Data Boundary  
Australia Data Boundary and Support  
Brazil Data Boundary  
Canada Data Boundary  
Canada Data Boundary and Support  
Data Boundary for Canada Protected B  
Chile Data Boundary  
EU Data Boundary  
EU Data Boundary and Support  
EU Data Boundary with Access Justifications  
Hong Kong Data Boundary  
India Data Boundary  
Indonesia Data Boundary  
Israel Data Boundary  
Israel Data Boundary and Support  
Japan Data Boundary  
Qatar Data Boundary  
Singapore Data Boundary  
South Africa Data Boundary  
Switzerland Data Boundary  
Taiwan Data Boundary  
UK Data Boundary  
US Data Boundary  
US Data Boundary and Support  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
Unencrypted (non-CMEK) resources |  Occurs when a resource is created without CMEK encryption for a service that requires CMEK encryption. This violation is caused by the **`gcp.restrictNonCmekServices` ** constraint. |  |   
---  
Data Boundary for Criminal Justice Information Systems (CJIS)  
EU Data Boundary with Access Justifications  
Data Boundary for Impact Level 5 (IL5)  
Data Boundary for International Traffic in Arms Regulations (ITAR)  
Local Controls by S3NS (Sovereign Controls by Partners)  
Sovereign Controls by SIA/Minsait (Sovereign Controls by Partners)  
T-Systems Sovereign Cloud (Sovereign Controls by Partners)  
  
## What's next

  * Understand the [control packages](https://docs.cloud.google.com/assured-workloads/docs/control-packages) for Assured Workloads.
  * Learn which [products are supported](https://docs.cloud.google.com/assured-workloads/docs/supported-products) for each control package.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
