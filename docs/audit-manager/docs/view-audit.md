---
url: https://docs.cloud.google.com/audit-manager/docs/view-audit/
title: View an audit \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:39.867219+00:00
---

# View an audit  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/view-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  View an audit Stay organized with collections  Save and categorize content based on your preferences. 

When an audit is completed, Audit Manager creates and stores the following audit artifacts in the destination storage buckets for you to view:

  * Audit summary report
  * Control overview report
  * Evidence



## Before you begin

Ensure that you have the following IAM roles:

  * One of the following Audit Manager roles for the resource:

    * [Audit Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.admin) (`roles/auditmanager.admin`)
    * [Audit Manager Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.auditor) (`roles/auditmanager.auditor`)
    * [Compliance Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.viewer) (`roles/cloudsecuritycompliance.viewer`) (required if you're auditing a framework that you've created using Compliance Manager)
  * One of the following Cloud Storage roles for the storage bucket that contains Audit Manager reports:

    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
    * [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)
    * [Storage Legacy Object Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketReader) (`roles/storage.legacyObjectReader`)



## View Audit Manager reports

You can view your compliance score for [controls, cloud controls, and Google Cloud resources](https://docs.cloud.google.com/audit-manager/docs/overview#cloud-controls) on the **Audit report** page in the Google Cloud console.

  1. In the Google Cloud console, go to the **Audit Manager** page.

[Go to Audit Manager](https://console.cloud.google.com/compliance/auditmanager)

  2. In the **Compliance audits** section, click **View audits**.

On the **View audits** page, you can view the status of an in-progress audit or a completed audit from Audit Manager or Compliance Manager.

  3. For more information about an audit, click the audit name.

You can view information about the audit, including its status, what resources were audited, the framework, location, time run, and the storage bucket that includes the audit reports. If applicable, to view the parameters that were specified for the report, click **Overrides**.

The **Audit report** dashboard includes separate tabs for controls, cloud controls, and resources, each with their own unique counts and diagrams. The **Audit report** dashboard shows your compliance score. Each tab's dashboard includes the following:

     * **Compliance summary:** The percentage is determined as follows:
           
           (Number of evaluated items that compliance / Total number of items) * 100
           

An item can be a control, a cloud control, or a resource. The total number of items includes all the items that are in compliance, in violation, and weren't evaluated (skipped).

     * **Total:** The total number of controls or cloud controls in the framework, or the total number of resources that were evaluated.

     * **Compliant:** The number of items that met the evaluation requirements.

     * **Violations:** The number of items that didn't meet the evaluation requirements.

     * **Inconclusive:** The number of items that Audit Manager couldn't determine whether they were in compliance. For example, the configuration or log data that was retrieved didn't clearly match the compliance rules.

     * **Skipped:** The number of items that Audit Manager couldn't evaluate because of an error or system issue that was encountered during the assessment. For example, there were insufficient permissions to inspect a specific resource.

     * **Not supported:** The number of items that Audit Manager couldn't inspect because they require the evaluation of resources that are outside of Google Cloud.

     * **Evidence collected:** The amount of information that was extracted through the technical assessment of the items.

     * **Violating evaluations:** The number of rules or resources that Audit Manager assessed as failing.

  4. To download the audit report from the Cloud Storage bucket as an OpenDocument Spreadsheet (ODS), click **Download report**.

Alternatively, you can download the required report and evidence directly from the destination storage bucket. For the detailed instructions, see [Download an object from a bucket](https://docs.cloud.google.com/storage/docs/downloading-objects#console-download-object).

  5. To view more information about an item's status, click **View** beside the status. The filtered view shows the applicable control, cloud control, or resource.

     * In the **Control** tab, the view is grouped by controls. To see the controls and cloud controls that are grouped within a control, expand the filter.

     * In the **Cloud control** tab, the view is grouped by cloud controls.

     * In the **Resources** tab, the view is grouped by service API name (for example, `cloudresourcemanager.googleapis.com`). To see the applicable resources within a service, expand the filter.

  6. ([Preview](https://cloud.google.com/products/#product-launch-stages)) To view a Gemini-generated summary about the results for cloud controls, controls, or resources, click **Insights generated by Gemini**.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

  7. To view a detailed summary about a particular item, click the item in the filtered view. Depending on the tab that you're on, the following information is displayed:

### Control report

The **Control** report page shows the following:

     * The control ID and family.
     * The shared responsibility status.
     * The review status.
     * The evaluation status.
     * The amount of evidence that was collected during the audit.
     * A summary of the evaluation that's generated by Gemini.
     * Information about the cloud controls that are part of the control, including the number of cloud controls that are passing and evidence summary.
     * A filtered view that provides links to cloud control reports and shared responsibility information.

### Cloud control report

The **Cloud control** report page shows the following:

     * The cloud control name and ID.
     * The review status.
     * The controls (referred to as _regulatory controls_) that the cloud control belongs to.
     * The evaluation status.
     * A summary of the evaluation that's generated by Gemini.
     * The amount of evidence that was collected during the audit.
     * Information about the cloud controls that are part of the control, including the number of evaluations, violations, and evidence.
     * A filtered view that provides links to observation summaries and applicable resource reports.

### Resource report

The **Resource** report page shows the following:

     * The applicable resource and service.
     * The controls (referred to as _regulatory controls_) and cloud controls that were used to evaluate the resource.
     * The evaluation status.
     * A summary of the evaluation that's generated by Gemini.
     * Observations that were found during the audit, which include the number of evaluations, violations, and evidence.
     * A filtered view that provides links to observation summaries and cloud control reports.




### Reports in Cloud Storage

The Audit Manager audit reports are available in folders within Cloud Storage storage buckets that use the following convention:

`audit-reports/audit_RESOURCE_NAME_FRAMEWORK_NAME_TIMESTAMP/UNIQUE_ID`

The placeholder values are described as follows:

  * RESOURCE_NAME: The ID of the folder or project, such as `folders_12345` or `projects_12345`.
  * FRAMEWORK_NAME: The name of the framework, such as `builtin-nist800-53-revision5`.
  * TIMESTAMP: A timestamp when the report was generated.
  * UNIQUE_ID: A unique ID for the report.



Each audit folder includes separate reports available for each control, cloud control, and evidence. Control and cloud control reports are in ODS format and contain detailed descriptions of the compliance evaluation for a single control. These reports provide assessment details for each compliance check with observations and expected values. Evidence reports are in JSON format and include all the resources evaluated for each control, including a raw dump of asset data along with the command that was run to produce the output.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
