---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings/
title: Configure settings \u00a0|\u00a0 Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:22.576487+00:00
---

# Configure settings  |  Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Configure settings Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure general settings for Mainframe Assessment Tool and modify default AI features for new assessments.

The modified settings don't apply to existing assessments. To use the modified settings, create a new assessment.

## Configure general settings

To configure general settings for your assessment, follow these steps:

  1. Click the settings**Settings** icon.

  2. To edit your preferences for Cloud Logging and Google Analytics, in the **General settings** section, do the following:

     * To turn off Logging, click the **Enable Cloud Logging** toggle to the off position. By default, this setting is enabled.

For more information, see [Cloud Logging documentation](https://docs.cloud.google.com/logging/docs).

**Note:** You might incur additional costs for using Logging.
     * To turn off Google Analytics, click the **Enable Google Analytics** toggle to the off position. By default, Google Analytics is enabled. Changes to this setting only take effect after you reload the page.

  3. View the **Google Cloud project** field to see the Google Cloud project ID used by Mainframe Assessment Tool. You cannot edit this field in the UI. To use a different project, see Override the Google Cloud project.

**Note:** If you configured a project ID in a previous version of Mainframe Assessment Tool (version 3.4.0 or earlier), that saved setting is used by default instead of the project where the instance is deployed.
  4. For **Serving tier** , select a Gemini Enterprise Agent Platform serving tier. Default is [Standard](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo).

The serving tier setting determines the inference and consumption model applied to Gemini model calls during mainframe assessments. For more information about Gemini Enterprise Agent Platform serving tiers, see [PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo).

  5. Click **Save settings**.




## Override the Google Cloud project

By default, Mainframe Assessment Tool uses the Google Cloud project where your instance is deployed. To override the project used for your assessments, follow the instructions for your deployment environment.

### Before you begin

To prepare for overriding the Google Cloud project, complete the following tasks:

  * **Grant necessary permissions.** The permissions you need depend on how you deployed Mainframe Assessment Tool: 
    * On a Compute Engine VM instance, you need permission to set custom metadata on the instance. For details on the required roles, see [Set and remove custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).
    * On a GKE cluster, you need permission to update deployments in the cluster, and you must configure the `kubectl` command-line tool to connect to the cluster. For more information, see [Configure cluster access for kubectl](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).
  * **Provide target project access.** Grant the service account used by Mainframe Assessment Tool the [required roles in the target project](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-your-project#assign-roles).



### Override the project on a Compute Engine VM instance

To override the Google Cloud project on a Compute Engine VM instance, add the `MAT_GCP_PROJECT_OVERRIDE` metadata key and set its value to your target project ID by running the following `gcloud` command:
    
    
    gcloud compute instances add-metadata INSTANCE_NAME \
        --metadata=MAT_GCP_PROJECT_OVERRIDE=PROJECT_ID \
        --zone=ZONE
    

To remove the override, remove the metadata key by running the following `gcloud` command:
    
    
    gcloud compute instances remove-metadata INSTANCE_NAME \
        --keys=MAT_GCP_PROJECT_OVERRIDE \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of your VM instance.
  * `PROJECT_ID`: your target Google Cloud project ID.
  * `ZONE`: the zone where your VM instance is located.



Mainframe Assessment Tool then falls back to your saved project ID, if you have one, or to the project where the instance is deployed. If you set or remove the metadata key on a running VM, you must restart the VM for the changes to take effect.

### Override the project on a GKE cluster

To override the Google Cloud project on a GKE deployment, set the `MAT_GCP_PROJECT_OVERRIDE` environment variable on the `backend` container:
    
    
    kubectl set env deployment/mat-apps --containers=backend \
        MAT_GCP_PROJECT_OVERRIDE=PROJECT_ID --namespace=VERSION
    

To remove the override, unset the environment variable by appending a hyphen (`-`):
    
    
    kubectl set env deployment/mat-apps --containers=backend \
        MAT_GCP_PROJECT_OVERRIDE- --namespace=VERSION
    

Replace the following:

  * `PROJECT_ID`: your target Google Cloud project ID.
  * `VERSION`: the Mainframe Assessment Tool version deployed on the cluster (for example, `mainframe-assessment-3-5-0`).



Mainframe Assessment Tool then falls back to your saved project ID, if you have one, or to the project where the instance is deployed. Updating the environment variable restarts the pod with the project override applied. Because Mainframe Assessment Tool runs as a single pod, it is briefly unavailable while the new pod starts.

## Configure default AI features for new assessments

Mainframe Assessment Tool lets you customize the default parameters for AI insights in your assessments. By default, AI insights are enabled.

To configure AI features in new assessments, follow these steps:

  1. Click the settings**Settings** icon.

  2. To generate paragraph-level summaries for COBOL code, select **Detailed summaries**.

By default, this option is selected when AI analysis is enabled.

  3. To generate test cases for the assessment specifications generated by Gemini, select **Test cases**.

By default, this option is not selected when AI analysis is enabled.

  4. For **Additional generation guidance** , enter text to add to the Gemini prompts during AI generation.

  5. Click **Save settings**.




## Check system health

Mainframe Assessment Tool checks whether your project can run assessments. The check confirms that the service account holds the required IAM roles, and that every Gemini model responds at each endpoint that an assessment can use. Mainframe Assessment Tool runs the check at startup. The check doesn't block assessments.

To review the results of the check, follow these steps:

  1. Click the settings**Settings** icon.

  2. In the **System health** section, review the following:

     * **Checked identity** : the service account that the check ran as.

     * **IAM permissions** : whether that service account holds each required role.

     * **Models** : the endpoints that each model responds at. For a model that doesn't respond, Mainframe Assessment Tool names the endpoint, the cause, and the action to take.

  3. Optional: To run the check again, for example after you grant a role or change your network configuration, click **Re-check**.




If the check finds an issue, Mainframe Assessment Tool shows a notification on every page until you fix or dismiss the issue.

If the Cloud Resource Manager API isn't enabled on your project, Mainframe Assessment Tool can't verify IAM permissions and reports this in the **System health** section. To enable the API, see [Enable APIs](https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-your-project#enable-apis).

## Optional: Perform actions

This section describes how to perform actions, such as clearing the Gemini cache and downloading your logs.

To perform actions, follow these steps:

  1. Click the settings**Settings** icon.

  2. To clear the Gemini cache, click **Clear model cache**.

**Note:** To improve performance and accuracy for subsequent assessments on the same files, don't clear the cache. Gemini uses the cache data for subsequent assessments.
  3. To download your Mainframe Assessment Tool logs, click **Download support bundle**.

The support bundle contains the Mainframe Assessment Tool logs as a zip file, which you can share with Google Cloud support to troubleshoot issues.




## Disable AI insights for assessments

You can disable AI analysis to prevent AI insights from appearing on the **Assessments** page.

To disable AI analysis for assessments, follow these steps:

  1. In the **Default AI features in new assessments** section, clear **Enable AI insights**.

  2. Click **Save settings**.




## Track Agent Platform costs using custom metadata labels

Mainframe Assessment Tool automatically adds custom metadata labels to all Agent Platform requests to help you track and analyze costs. In your billing report, you can use these labels to filter costs to better understand and optimize your Agent Platform usage. The costs are updated in the billing report within 24 hours of usage, but in some cases can take longer.

Filter costs in your billing report with the following labels:

  * `mat-version`: version of Mainframe Assessment Tool.
  * `mat-host`: host environment of the Mainframe Assessment Tool instance. For example, Compute Engine VM or Google Kubernetes Engine.
  * `mat-action-type`: type of action performed by Mainframe Assessment Tool.
  * `mat-schema`: type of asset processed. For example, `COBOL` or `JCL`.
  * `mat-target`: deployment target of the Mainframe Assessment Tool instance.
  * `mat-run-id`: unique ID of the assessment.



To track usage by using one or more of these filters in the billing report, see [Use filters to refine data](https://docs.cloud.google.com/billing/docs/how-to/reports#filters).

For more information about labels in Agent Platform, see [Custom metadata labels](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/add-labels-to-api-calls).

## What's next

  * Learn how to [create an assessment](https://docs.cloud.google.com/mainframe-assessment-tool/docs/perform-assessment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
