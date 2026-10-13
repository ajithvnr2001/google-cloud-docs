---
url: https://docs.cloud.google.com/security-command-center/docs/validate-iac/
title: Validate your IaC against your Google Cloud organization's policies \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:02.399315+00:00
---

# Validate your IaC against your Google Cloud organization's policies  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/validate-iac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Validate your IaC against your Google Cloud organization's policies Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document describes how to validate your [infrastructure as code (IaC)](https://en.wikipedia.org/wiki/Infrastructure_as_code) against the [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy) and [Security Health Analytics detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics#sha-detection-modules) that you have defined in your Google Cloud organization. IaC lets you create and manage your cloud resources using languages such as Terraform so that you can deploy the resources using a development workflow. The IaC validation feature supports organization policies and Security Health Analytics detectors only.

Validating your IaC lets you determine whether your new or modified resource definitions violate the existing policies that are applied to your Google Cloud resources (for example, cluster, bucket, or instance). You can define these policies using [security postures](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview), but the IaC validation feature analyzes the code and compares the code against any effective policies defined in postures that are deployed on your Google Cloud organization. IaC validation helps your developers identify and fix any security issues in the IaC configuration of assets or resources before they are applied to your Google Cloud environment.

The IaC validation feature supports Terraform plan files. You can validate your Terraform plan using Google Cloud CLI, or you can integrate the validation process into your Cloud Build, Jenkins, or GitHub Actions developer workflow.

## Before you begin

Complete these tasks to get started with IaC validation.

### Activate the Security Command Center Premium tier or Enterprise tier

Verify that the [Security Command Center Premium tier or Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) is activated at the organization level.

### Set up permissions

Make sure that you have the following role or roles on the organization: Security Posture Shift-Left Validator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
     2. Select the organization. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
     2. Select the organization. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



For more information about IaC validation permissions, see [IAM for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org).

### Set up Google Cloud CLI

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

To set up the gcloud CLI to use service account impersonation to authenticate to Google APIs, rather than your user credentials, run the following command: 
    
    
    gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL

For more information, see [Service account impersonation](https://docs.cloud.google.com/security-command-center/docs/reference/authentication#sa-impersonation). 

### Enable APIs

Enable the Security Posture and Security Center Management APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=securityposture.googleapis.com,securitycentermanagement.googleapis.com)

### Define your policies

Define your [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) and [Security Health Analytics detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics). To define these policies using a security posture, complete the tasks in [Create and deploy a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#create_and_deploy_a_posture).

## Create your Terraform code

Use your developer workflows and tools to create a Terraform file that includes the Google Cloud assets that you want to create or modify.

Consider the following:

  * Populate the parent attribute (the project, folder, or organization) of every resource or asset in the Terraform configuration.
  * Modify assets and policies separately. The API doesn't support validation of Terraform plan files which modify both assets and policies at the same time.
  * Use supported asset types and policies only. For a list of supported asset types and policies, see [Supported asset types and policies for IaC validation](https://docs.cloud.google.com/security-command-center/docs/supported-iac-assets-policies).
  * Review the [limitations for IaC validation](https://docs.cloud.google.com/security-command-center/quotas#infrastructure_as_code_validation_limitations).
  * Don't include sensitive information such as passwords or other personally identifiable information in your Terraform plan file. If the validation feature encounters fields marked as sensitive in the resource changes, the fields are removed.



After you create your Terraform code, you can run the IaC validation report. You can use the gcloud CLI, [Cloud Build](https://docs.cloud.google.com/security-command-center/docs/iac-validation-cloud-build), [Jenkins](https://docs.cloud.google.com/security-command-center/docs/iac-validation-jenkins), or [GitHub Actions](https://docs.cloud.google.com/security-command-center/docs/iac-validation-github-actions).

## Use Google Cloud CLI to create an IaC validation report

To create an IaC validation report, complete the following:

  1. In gcloud CLI, run `terraform init`.

Verify that you're running Terraform provider version v5.5 or later. If required, upgrade to the latest Google provider version:
         
         terraform init -upgrade
         

  2. Convert the Terraform plan file to JSON format:
         
         terraform plan -out TF_PLAN_FILENAME
         terraform show -json TF_PLAN_FILENAME > TF_PLAN_JSON_FILENAME.json
         

Replace the following:

     * `TF_PLAN_FILENAME`: The name for the Terraform plan file.
     * `TF_PLAN_JSON_FILENAME`: The name of the file that will contain the Terraform plan in JSON format.
  3. Create the IaC validation report:
         
         gcloud scc iac-validation-reports create PARENT \
           --tf-plan-file=TF_PLAN_JSON_FILENAME.json
         

Replace the following:

     * `PARENT`: The Google Cloud organization in which to create the IaC Validation report. The format is `organizations/ORGANIZATION_ID/locations/LOCATION`. `LOCATION` is `global`.
     * `TF_PLAN_JSON_FILENAME`: The path to the JSON file that contains the IaC plan that you want to validate.

For example, to create an IaC validation report under the `organizations/3589215982/locations/global` organization with an IaC plan included in `planFile.json`, run the following command:
    
    gcloud scc iac-validation-reports create organizations/3589215982/locations/global --tf-plan-file=planFile.json
    

This command returns the operation details for creating the IAC validation report. To get information about the operation, see [View information about a posture deployment operation](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#view-operation).




## What's next

  * [Review the sample tutorial](https://docs.cloud.google.com/security-command-center/docs/iac-validation-tutorial).
  * Integrate IaC validation with your [Cloud Build workflow](https://docs.cloud.google.com/security-command-center/docs/iac-validation-cloud-build).
  * Integrate IaC validation with your [GitHub Actions](https://docs.cloud.google.com/security-command-center/docs/iac-validation-github-actions) or your [Jenkins project](https://docs.cloud.google.com/security-command-center/docs/iac-validation-jenkins).
  * [Manage your security posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
