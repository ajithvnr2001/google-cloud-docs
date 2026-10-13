---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit/
title: Audit your environment with Compliance Manager \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:53.165593+00:00
---

# Audit your environment with Compliance Manager  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Audit your environment with Compliance Manager Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Compliance Manager lets you run audits against its frameworks so that you can understand the state of compliance of your Google Cloud environment. Auditing your environment lets you complete the following:

  * Automate compliance assessments to evaluate how well your Google Cloud workloads align with your compliance obligations.
  * Collect evidence for compliance audits.
  * Identify gaps to help remediate violations.



Compliance Manager can provide assessments for any Google Cloud folder or project.

The auditing process creates the following artifacts that Compliance Manager stores in Cloud Storage buckets:

  * An audit summary report that provides the following: 
    * An overview of how well your folder or project aligns with the cloud controls in a framework.
    * A responsibilities matrix to help you understand your shared responsibilities with Google.
  * A control overview report that describes the results of the evaluation for a specific cloud control. This report provides assessment details for each compliance check, including observations and expected values.
  * The evidence used to create the report, which includes all the resources evaluated for each cloud control, including a raw dump of asset data.



## Before you begin

  * To get the permissions that you need to audit your environment, ask your administrator to grant you the following IAM roles on your organization, folder, or project: 

    * [Compliance Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.admin) (`roles/cloudsecuritycompliance.admin`)
    * On the project that the Cloud Storage bucket is located, one of: 
      * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
      * [Storage Legacy Bucket Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)
    * To enroll an organization, one of: 
      * [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)
      * [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)
    * To enroll a project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
    * To enroll a folder, one of: 
      * [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)
      * [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)
      * [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`)
      * [Folder IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderIamAdmin) (`roles/resourcemanager.folderIamAdmin`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

The roles for enrolling an organization contain the required `resourcemanager.organizations.setIamPolicy` permission. The roles for enrolling a folder contain the required `resourcemanager.folders.setIamPolicy` permission. 

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 



  * Identify or create Cloud Storage buckets where you can store the audit data. For instructions, see [Create a bucket](https://docs.cloud.google.com/storage/docs/discover-object-storage-console#create_a_bucket).
  * [Apply the frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) that you want to audit to the appropriate organization, folders, and projects.
  * If you [restrict resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), verify that the organization policy includes the [locations](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit-locations) where you want to process your audit.
  * If you're using VPC Service Controls service perimeters, configure the [appropriate ingress and egress rules](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-configure-vpc-sc).
  * Enable [Audit Manager](https://docs.cloud.google.com/audit-manager/docs/enable-audit-manager).



## Enroll resources

Before you can audit your environment, you must enroll the organization, folders, or projects that you want to audit and specify a Cloud Storage bucket. Compliance Manager stores the audit data in the Cloud Storage bucket.

You can enroll resources and set up Cloud Storage buckets for auditing using [Audit Manager](https://docs.cloud.google.com/audit-manager/docs/enroll-resource) or Compliance Manager. The resources and buckets that you enroll are available for both Audit Manager and Compliance Manager to use for auditing purposes.

  1. In the console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance/audit)

  2. Select your organization or project.

  3. In the **Audit** tab, click **Audit settings**.

  4. Find the projects or folders that you want to audit.

  5. Click **Enroll**. Inheritance works as follows:

     * If you enroll an organization, you can audit all folders and projects.
     * If you enroll a folder, you can audit the folders and projects within that folder.
  6. Select the Cloud Storage bucket that you want to use to store audit data, or create a new bucket.

  7. Click **Enroll**.




## Update your resource enrollment

You can change the Cloud Storage bucket after you enroll a resource.

  1. In the console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance/audit)

  2. Select your organization or project.

  3. In the **Audit** tab, click **Audit settings**.

  4. Find the project or folder that you want to change.

  5. Click **Update**.

  6. Modify the bucket information.

  7. Click **Enroll**.




## Audit your environment

Complete the following task to start an audit of a folder or project.

  1. In the console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance/audit)

  2. Select your organization or project.

  3. In the **Audit** tab, click **Run audit**.

  4. Select the resource that you want to audit. You can select only one folder or project for each audit.

  5. Select a framework.

  6. Select the location where the audit assessment must be processed. For the list of supported locations, see [Audit locations for Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit-locations). If you don't see the location that you're looking for, select **global**. Click **Next**.

  7. Review the assessment plan. This plan provides information about the audit scope based on the framework that you selected. To download the OpenDocument Spreadsheet (ODS) file, click the link.

  8. Click **Next**.

  9. Select the Cloud Storage bucket that you want to store your audit reports in. Click **Done**.

  10. Click **Run Audit**. The audit might take some time to complete. Refresh the main **Audit** page to view progress.




To watch for changes to the Cloud Storage bucket, you can set up notifications using an [event-driven function](https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage) or [Pub/Sub](https://docs.cloud.google.com/storage/docs/pubsub-notifications).

## View audit information

When an audit is completed, Compliance Manager creates and stores the artifacts in the destination storage buckets for you to view.

  1. In the console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance/audit)

  2. Select your organization or project.

  3. In the **Audit** tab, to view the audit summary, click the link in the **Status** column.

The **Basic information** page displays the information about compliance controls in scope and the status of the automated compliance:

     * **Compliant:** Shows the configurations that meet all the requirements.
     * **Violations:** Shows the misconfigurations that are detected against a given control.
     * **Manual review needed:** Shows the configurations that you must validate manually to determine whether the configurations are compliant.
     * **Skipped:** Shows the configurations that Compliance Manager skipped for a given control.
  4. Depending on the type of audit information that you want to view, follow the instructions in the corresponding tab.

### Audit summary report

     1. To see the details of a status, click **View**.
     2. To export the audit summary report, click  file_upload**Export**.

The audit summary report is exported in the ODS format.

## Control overview report

You can view the control overview report based on a control or status.

To view the control overview page based on a control, do the following:

     1. In the filtered list, expand the required control.

     2. Click the corresponding hyperlink. The control page shows the responsibility, findings, and requirements.

To view the control overview report based on a status, do the following:

     1. For the required status, click **View**.

     2. From the list of controls, click the required hyperlink. The control overview page shows the responsibility, findings, and requirements.

     3. To view information about your responsibilities and Google's responsibilities for this control, click **View Shared Responsibility**.

To export the control overview report, click  file_upload**Export**. The control overview report is exported in the ODS format.

### Evidence

You can view the evidence based on control or status.

To view the evidence based on a control, do the following:

     1. Expand the required control.

     2. To view the detailed compliance assessment against each rule, click the corresponding hyperlink.

The controls page shows the responsibility, findings, and requirements.

To view the evidence based on a status, do the following:

     1. For the required status, click **View**.

     2. From the list of controls, click the required hyperlink.

The controls page shows the responsibility, findings, and requirements.

To view the evidence for a finding, in the filtered list, click **Click here to open the evidence**. The **Object details** page with the evidence details opens in a separate tab.

To download the evidence, click download **Download**. The evidence is downloaded in JSON format.




Alternatively, you can download the required report and evidence directly from the destination storage bucket. For more information, see [Download an object from a bucket](https://docs.cloud.google.com/storage/docs/downloading-objects#console-download-object).

### Audit summary report

The audit summary report is a comprehensive report that provides an overview of all compliance controls and a responsibilities matrix to help you understand the compliance of the Google Cloud folder or project. The audit summary report is available in OpenDocument Spreadsheet (ODS) format.

In the destination storage bucket, the audit summary report uses the following naming convention:

`audit-reports/audit_FRAMEWORK_NAME_TIMESTAMP/UNIQUE_ID/overall_report.ods`

The values are the following:

  * `FRAMEWORK_NAME`: the name of the framework.
  * `TIMESTAMP`: a [timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) that indicates when the report was generated.
  * `UNIQUE_ID`: a unique ID for the report.



For each applicable control type, the following fields are populated in the audit summary report:

Control type | Description  
---|---  
Control Info | A description and requirement for the control.  
Google Responsibility | Google Cloud responsibility and implementation details.  
Customer Responsibility | Your responsibility and implementation details.  
Assessment Status |  Status of compliance for the control. Status can be one of the following types:

  * **Non-Compliant** : Compliance drift detected.
  * **Compliant** : System is compliant.
  * **Manual Review Needed** : Artifacts are produced but user input is required to finalize the status of compliance.
  * **Skipped** : Compliance Manager can't evaluate the cloud control.

  
Control Report Link | A link to the control overview report.  
  
### Control overview report

A control overview report contains a detailed description of the compliance evaluation for a single control. The report provides assessment details for each compliance check with observations and expected values.

In the destination storage bucket, the control overview report uses the following naming convention:

`audit-reports/audit_FRAMEWORK_NAME_TIMESTAMP/UNIQUE_ID/CONTROL_ID.ods`

The values are the following:

  * `FRAMEWORK_NAME`: the name of the framework.
  * `TIMESTAMP`: a timestamp when the report was generated.
  * `UNIQUE_ID`: a unique ID for the report.
  * `CONTROL_ID`: the ID for the control.



Within the report, dates use the MM/DD/YYYY format.

A control overview report looks similar to the following example:

Control ID: COMPLIANT  
---  
Service name | # of resources | Status | **Resource Evaluation Details**  
Resource ID | Measured Field | Current Value | Expected Value | Status | Evidence Resource URI | Evidence Timestamp | Evidence for Project/Folder | Evidence Link  
Total services in scope for this control | Total resources in audit scope | Compliance status | Resource identifier | Configuration to be measured for audit | Observed values | Compliant values | Individual compliance status |  | Timestamp when evidence was collected |  |   
product1.googleapis.com | 2 | COMPLIANT | folder_123456 | abc | 10 | >=10 | COMPLIANT | Resource 1 | 10/05/2025 12:55:16 | Project 1 | Link 1  
|  |  |  | def | 15 | =15 | COMPLIANT | Resource 4 | 10/05/2025 13:55:16 | Project 1 | Link 4  
|  |  | project_123456 | xyz | 20 | =20 | COMPLIANT | Resource 2 | 10/05/2025 14:55:16 | Project 1 | Link 2  
product2.googleapis.com | 1 | COMPLIANT | project_123456 | def | 5 | >=5 | COMPLIANT | Resource 3 | 10/05/2025 15:55:16 | Project 1 | Link 3  
  
### Evidence

Evidence includes all the resources evaluated for each control, including a raw dump of asset data along with the command that was run to produce the output.

In the destination storage bucket, evidence is in JSON format and uses the following naming convention:

`audit-reports/audit_FRAMEWORK_NAME_TIMESTAMP/UNIQUE_ID/evidences/evidenceEVIDENCE_ID.json`

The values are the following:

  * `FRAMEWORK_NAME`: the name of the framework.
  * `TIMESTAMP`: a timestamp when the report was generated.
  * `UNIQUE_ID`: a unique ID for the report.
  * `EVIDENCE_ID`: a unique ID for the evidence.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
