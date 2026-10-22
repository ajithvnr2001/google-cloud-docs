---
url: https://docs.cloud.google.com/cloud-assist/create-investigation/
title: Create a Gemini Cloud Assist investigation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:15.641690+00:00
---

# Create a Gemini Cloud Assist investigation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/create-investigation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Create a Gemini Cloud Assist investigation Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** As of April 10, 2026, creating, running, and editing investigations are only available to users that have a [Premium Support contract](https://cloud.google.com/support/premium) or who have requested access through their account team. If you ran an investigation prior to April 10, 2026, the results of the investigation continue to be available to you in the Google Cloud console.   
  
Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/services?e=48754805), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview?e=48754805).

Gemini Cloud Assist investigations let you diagnose and troubleshoot issues across your cloud resources. You can create and review investigations to identify potential root causes and evaluate remediation plans.

## Before you begin

  1. Verify you have [set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

  2. (Optional) Verify you have enabled recommended APIs:

     * `logging.googleapis.com`
     * `monitoring.googelapis.com`
     * `cloudresourcemanager.googleapis.com`

See [Enabling and disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable) for instructions on how to enable APIs.

  3. In order to get the required permissions for creating an investigation, ask your administrator to grant you the [Investigation Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationCreator) (`roles/geminicloudassist.investigationCreator`) IAM role on the project.

This predefined role contains the permission required to create an investigation within your project. When you create an investigation, you're granted the [Investigation Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationOwner) (`roles/geminicloudassist.investigationOwner`) IAM role on that investigation, which lets you review the results of the investigation.

  4. Have access to the product being investigated.

When you perform an investigation, Gemini Cloud Assist [uses your credentials](https://docs.cloud.google.com/cloud-assist/investigations#oauth) to access APIs and information. This means that the investigation's access is limited to the access that you have.

  5. If you plan to perform an investigation on an application, the application must be contained within a [folder configured for application management](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder). Gemini Cloud Assist doesn't support applications created in a [ host project or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).




## Create an investigation

### Console

**Important:** The Investigations feature is integrated into multiple Google Cloud services and workflows. Your experience creating an investigation might have small differences from those outlined in this document. For example, some services can autofill information such as the **Start time** or the field for describing the issue.

  1. To create a new investigation, click the **Investigate** button associated with your [entry point](https://docs.cloud.google.com/cloud-assist/investigations#entry-points). A typical entry point for creating an investigation is the **Cloud Assist Investigations** page.

[Go to Cloud Assist Investigations](https://console.cloud.google.com/troubleshooting/investigations/list)

  2. Expand the **Configure investigation** drop-down.

  3. (Optional) Enter an **Investigation name** for your investigation.

The name you choose identifies this investigation in your [investigation history](https://docs.cloud.google.com/cloud-assist/manage-investigations#list). A name for the investigation is generated automatically if you skip this step.

  4. Use the **Select time range** drop-down to select the span of time you want to investigate.

An accurate start time enables time-based correlations to be made across seemingly unrelated events and adds more weight to events that occurred close to the start time. If you're unsure of the time range, you can run multiple investigations simultaneously with different time ranges.

  5. **Describe the issue** that you're experiencing.

You can copy and paste the exact error message you received, you can use natural language to explain the issue that you're experiencing, or you can include both.

  6. If application investigations are supported by your [entry point](https://docs.cloud.google.com/cloud-assist/investigations#entry-points), then use the **Application** field to choose an application to investigate.

  7. (Optional) Click **\+ Add resource** to select the resources that are affected by the issue you're experiencing.

You can add resources either by using the resource picker or by inputting them manually. When inputting resources manually, you should consult the resource's reference documentation to ensure you use the correct format.

You can't proceed with an investigation if you include any of the following:

     * Resources that are in a project or application that is outside the scope of the investigation.
     * Resources that are [not supported](https://docs.cloud.google.com/cloud-assist/investigations#products).
     * Resources that are not recognized.
  8. Click **Create** to begin the investigation.




The **Details** page for the investigation opens, and results appear in the page as they become available. It can take up to several minutes for the investigation to complete. If you leave the investigation's details page, you can check the status of the investigation by clicking the **Notifications** button (_notifications_).

**Note:** The user or service account that creates an investigation is granted the [Investigation Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationOwner) (`roles/geminicloudassist.investigationOwner`) IAM role for that specific investigation as part of the creation process.

## Review an Investigation

When working with investigations in the Google Cloud console, you can view the investigation details from the entry point where you initiated the investigation or from your project's [investigation history](https://docs.cloud.google.com/cloud-assist/manage-investigations#list).

An investigation contains the following sections:

  1. The **Investigation recap**

This section contains a high-level summary of the issue, the strategy Gemini took to investigate, and the key findings of the investigation.

  2. The **Hypotheses**

This section contains one or more hypothesis cards based on the data the investigation collected and the observations it made. You can find details for each hypothesis by click the **View** button in the relevant card.

     * The details for a hypothesis contain a **What** section describing what the issue could be and a **Next steps** section describing actions that either help you correct the issue or that provide you additional troubleshooting steps to confirm or refute the hypothesis.

       * If a remediation is supported for the issue that was identified in the hypothesis, a **Generate plan** button is included in the remediation steps. Clicking **Generate Plan** creates a step-by-step remediation plan, which includes concrete actions such as `gcloud` commands or Kubernetes manifests. After reviewing the plan, you can click **Run** to perform the actions described in the plan.
  3. The **Findings**

This section contains observations generated by the investigation and lists the Google Cloud resources involved in the investigation. Observations are based on reviews of procedural runbooks, logs, outage messages, and alerts.

The findings section shows you what information Gemini used to generate the hypotheses and can be helpful for refining your investigation.




You can [revise your investigation input](https://docs.cloud.google.com/cloud-assist/manage-investigations#edit) using the **Edit** button, which lets you re-run the investigation with updated information. When an investigation has multiple runs associated with it, you can review the results of previous runs of the investigation using the **Revision** drop-down selector.

If you have a [support package](https://docs.cloud.google.com/support), you can click the **Request support** button found in the investigation's details page in order to file a support case. When you do, you can automatically populate the case details and share the investigation results with the support engineer.

## What's next

  * Learn more about [investigations](https://docs.cloud.google.com/cloud-assist/investigations).
  * [View and manage existing investigations](https://docs.cloud.google.com/cloud-assist/manage-investigations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
