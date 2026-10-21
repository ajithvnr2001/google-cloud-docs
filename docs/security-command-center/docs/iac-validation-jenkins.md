---
url: https://docs.cloud.google.com/security-command-center/docs/iac-validation-jenkins/
title: Integrate IaC validation with Jenkins \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:50.752666+00:00
---

# Integrate IaC validation with Jenkins  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/iac-validation-jenkins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Integrate IaC validation with Jenkins Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

You can use the [Google Analyze Code Security plugin for Jenkins](https://plugins.jenkins.io/google-analyze-code-security/) to validate the infrastructure as code (IaC) that is part of your Jenkins project. Validating IaC lets you determine whether your Terraform resource definitions violate the existing organization policies and Security Health Analytics detectors that are applied to your Google Cloud resources.

For more information about IaC validation, see [Validate your IaC against your Google Cloud organization's policies](https://docs.cloud.google.com/security-command-center/docs/validate-iac).

IaC validation only works with [Jenkins freestyle projects](https://www.jenkins.io/doc/book/using/working-with-projects/).

## Before you begin

Complete these tasks to get started with IaC validation with Jenkins.

### Activate the Security Command Center Premium tier or Enterprise tier

Verify that the [Security Command Center Premium tier or Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) is activated at the organization level.

Activating Security Command Center enables the `securityposture.googleapis.com` and `securitycentermanagement.googleapis.com` APIs.

### Create a service account

Create a service account that you can use for the Google Analyze Code Security plugin for Jenkins.

Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Security Posture Shift-Left Validator** role to the service account. 

To grant the role, find the **Select a role** list, then select **Security Posture Shift-Left Validator**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 

Create a service account key: 

     1. In the Google Cloud console, click the email address for the service account that you created. 
     2. Click **Keys**. 
     3. Click **Add key** , and then click **Create new key**. 
     4. Click **Create**. A JSON key file is downloaded to your computer. 
     5. Click **Close**. 



For more information about IaC validation permissions, see [IAM for organization-level activations](https://docs.cloud.google.com/security-command-center/docs/access-control-org).

### Define your policies

Define your [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) and [Security Health Analytics detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics). To define these policies using a security posture, complete the tasks in [Create and deploy a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#create_and_deploy_a_posture).

## Install and configure the plug-in

  1. In the Jenkins console, click **Manage Jenkins** > **Manage Plugins**.
  2. In the **Available** tab, search for **google-analyze-code-security**.
  3. Complete the installation steps.
  4. Click **Manage Jenkins** > **Configure System**.
  5. In the **Google Analyze Code Security** section, click **Add credential**.
  6. In **Organization ID** , enter the organization ID for the Google Cloud organization that includes the Terraform resources that you want to create or modify.
  7. In **Security Command Center Credential** , add the service account key.
  8. Test the connection to verify the service account credentials.
  9. Click **Save**.



## Create your Terraform plan JSON file

  1. Create your Terraform code. For instructions, see [Create your Terraform code](https://docs.cloud.google.com/security-command-center/docs/validate-iac#create_your_terraform_code).

  2. Install the [Terraform plugin for Jenkins](https://plugins.jenkins.io/terraform/).

  3. In the Jenkins console, in your Jenkins freestyle project, go to the **Configuration** page.

  4. Click **Source Code Management**.

  5. In **Repository URL** , enter the URL to the Terraform code that you created.

  6. Click **Build steps**.

  7. Add the following steps:

     1. Initialize Terraform:
            
            terraform init
            

     2. Create a Terraform plan file.
            
            terraform plan -out=TF_PLAN_FILE
            

Replace `TF_PLAN_FILE` with the name for the Terraform plan file. For example, `myplan.tfplan`.

     3. Convert your plan file into JSON format:
            
            terraform show -no-color -json TF_PLAN_FILE > TF_PLAN_JSON_FILE
            

Replace `TF_PLAN_JSON_FILE` with the name for the Terraform plan file, in JSON format. For example, `mytfplan.json`.




## Add the plug-in to your Jenkins project

  1. In the Jenkins console, in your Jenkins freestyle project, go to the **Configuration** page.
  2. In **Build Steps** , click **Add build step** > **Perform Code Scan during Build**.
  3. Enter your organization ID.
  4. Provide the path to your Terraform plan file, in JSON format.
  5. Optional: Set the build failure criteria. The failure criteria is based on the number of critical, high, medium, and low severity issues that the IaC validation scan encounters. You can specify how many issues of each severity are permitted and how the issues are aggregated (either **AND** or **OR**).

     1. Click **Fail on Asset Violation**.

     2. If you want the build to fail only if the count of issues from all severity levels is reached, select **AND**. If you want the build to fail if the count of issues from any severity level is reached, select **OR**. For example, if you want the build to fail if it encounters one critical issue _or_ one high severity issue, set the aggregate value to **OR**.

     3. Indicate the number of issues at the various severity levels that you want to permit before the build fails.

If you don't want to specify a failure criteria, select **Ignore Asset Violation**.

  6. Click **Save**.




You can now run the build to validate your Terraform plan file.

## View the IaC violation report

  1. In the Jenkins console, click the most recent workflow for your build.

  2. Click **Status**. The following HTML files are available as build artifacts:

     * If the plug-in ran, the violation report (`GoogleAnalyzeCodeSecurity_ViolationSummary.html`)

The report groups violations by severity. The violation section describes which rule wasn't met and the asset ID from the Terraform plan that violated the rule.

     * If the build failed, an error summary report
  3. Resolve any violations within your Terraform code before applying it.




## What's next

  * View the [Google Analyze Code Security plugin](https://plugins.jenkins.io/google-analyze-code-security/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
