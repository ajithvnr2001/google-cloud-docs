---
url: https://docs.cloud.google.com/security-command-center/docs/iac-validation-github-actions/
title: Integrate IaC validation with GitHub Actions \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:57.588348+00:00
---

# Integrate IaC validation with GitHub Actions  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/iac-validation-github-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Integrate IaC validation with GitHub Actions Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

You can use the [Analyze Code Security action](https://github.com/marketplace/actions/analyze-code-security) to validate the infrastructure as code (IaC) that is part of your GitHub Actions workflow. Validating IaC lets you determine whether your Terraform resource definitions violate the existing organization policies and Security Health Analytics detectors that are applied to your Google Cloud resources.

For more information about IaC validation, see [Validate your IaC against your Google Cloud organization's policies](https://docs.cloud.google.com/security-command-center/docs/validate-iac).

## Before you begin

Complete these tasks to get started with IaC validation with GitHub Actions.

### Activate the Security Command Center Premium tier or Enterprise tier

Verify that the [Security Command Center Premium tier or Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) is activated at the organization level.

Activating Security Command Center enables the `securityposture.googleapis.com` and `securitycentermanagement.googleapis.com` APIs.

### Create a service account

Create a service account that you can use for the Analyze Code Security action.

Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  1. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
  2. Select your project. 
  3. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

  4. Click **Create and continue**. 
  5. Grant the **Security Posture Shift-Left Validator** role to the service account. 

To grant the role, find the **Select a role** list, then select **Security Posture Shift-Left Validator**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
  6. Click **Continue**. 
  7. Click **Done** to finish creating the service account. 




For more information about IaC validation permissions, see [IAM for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org).

### Set up authentication

  1. Configure Workload Identity Federation with your GitHub identity provider. For instructions, see [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).

  2. Obtain the URL for your Workload Identity Federation ID token. For example, `https://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID/providers/PROVIDER_ID`.

Consider the following:

     * `PROJECT_NUMBER` is the project number for the Google Cloud project that you set up Workload Identity Federation in.
     * `POOL_ID` is the pool name.
     * `PROVIDER_ID` is the name of your identity provider.
  3. Add the [Authenticate to Google Cloud action](https://github.com/marketplace/actions/authenticate-to-google-cloud) to your workflow to authenticate the IaC validation action.




### Define your policies

Define your [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) and [Security Health Analytics detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics). To define these policies using a security posture, complete the tasks in [Create and deploy a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#create_and_deploy_a_posture).

## Create your Terraform plan JSON file

  1. Create your Terraform code. For instructions, see [Create your Terraform code](https://docs.cloud.google.com/security-command-center/docs/validate-iac#create_your_terraform_code).

  2. In your GitHub Actions, initialize Terraform. For example, if you're using the [HashiCorp - Setup Terraform action](https://github.com/marketplace/actions/hashicorp-setup-terraform), run the following command:
         
         - name: Terraform Init
           id: init
           run: terraform init
         

  3. Create a Terraform plan file:
         
         - name: Create Terraform Plan
           id: plan
           run: terraform plan -out=TF_PLAN_FILE
         

Replace `TF_PLAN_FILE` with the name for the Terraform plan file. For example, `myplan.tfplan`.

  4. Convert your plan file into JSON format:
         
         - name: Convert Terraform Plan to JSON
           id: convert
           run: terraform show -no-color -json TF_PLAN_FILE > TF_PLAN_JSON_FILE
         

Replace `TF_PLAN_JSON_FILE` with the name for the Terraform plan file, in JSON format. For example, `mytfplan.json`.




## Add the action to your GitHub Actions workflow

  1. In the GitHub repository, browse to your workflow.
  2. Open the workflow editor.
  3. In the GitHub Marketplace sidebar, search for **Analyze Code Security**.
  4. In the **Installation** section, copy the syntax.
  5. Paste the syntax as a new step into your workflow.
  6. Replace the following values:

     * `workload_identity_provider` with the link to the URL for your Workload Identity Federation ID token.
     * `service_account` with the email address of the service account that you created for the action.
     * `organization_id` with your Google Cloud organization ID.
     * `scan_file_ref` with the path to your Terraform plan file, in JSON format.
     * `failure_criteria` with the failure threshold criteria that determines when the action fails. The threshold criteria is based on the number of critical, high, medium, and low severity issues that the IaC validation scan encounters. `failure_criteria` specifies how many issues of each severity are permitted and how the issues are aggregated (either `AND` or `OR`). For example, if you want the action to fail if it encounters one critical issue _or_ one high severity issue, set the `failure_criteria` to `Critical:1,High:1,Operator:OR`. The default is `Critical:1,High:1,Medium:1,Low:1,Operator:OR`, which means that if the IaC validation scan encounters any issue, the action must fail.



You can now run the workflow to validate your Terraform plan file. To run the workflow manually, see [Manually running a workflow](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow).

## View the IaC violation report

  1. In your GitHub repository, click **Actions** and select your workflow.

  2. Click the most recent run for your workflow.

In the **Artifacts** section, the violation report (`ias-scan-sarif.json`) is available in a zip file. The report includes the following fields:

     * A `rules` field that describes which policies were violated by the Terraform plan. Each rule includes a `ruleID` that you can match with the results that are included in the report.
     * A `results` field that describes the proposed asset modifications that violate a specific rule.
  3. Resolve any violations within your Terraform code before applying it.




## What's next

  * View the [analyze-code-security-scc action source code](https://github.com/google-github-actions/analyze-code-security-scc/) in GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
