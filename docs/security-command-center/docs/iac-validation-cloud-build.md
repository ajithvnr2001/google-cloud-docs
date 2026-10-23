---
url: https://docs.cloud.google.com/security-command-center/docs/iac-validation-cloud-build/
title: Integrate IaC validation with Cloud Build \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:11.174322+00:00
---

# Integrate IaC validation with Cloud Build  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/iac-validation-cloud-build/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Integrate IaC validation with Cloud Build Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

You can write a [build config](https://docs.cloud.google.com/build/docs/build-config-file-schema) that instructs Cloud Build to validate the infrastructure as code (IaC) that is part of your build. Validating IaC lets you determine whether your Terraform resource definitions violate the existing organization policies and Security Health Analytics detectors that are applied to your Google Cloud resources.

For more information about IaC validation, see [Validate your IaC against your Google Cloud organization's policies](https://docs.cloud.google.com/security-command-center/docs/validate-iac).

## Before you begin

Complete these tasks to get started with IaC validation using Cloud Build.

### Activate the Security Command Center Premium tier or Enterprise tier

Verify that the [Security Command Center Premium tier or Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview) is activated at the organization level.

Activating Security Command Center enables the `securityposture.googleapis.com` and `securitycentermanagement.googleapis.com` APIs.

### Set up permissions

Make sure that you have the following role or roles on the organization: 

     * Security Posture Shift-Left Validator
     * Log Writer
     * Storage Writer
     * Storage Reader

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

### Enable the Cloud Build API

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)




### Define your policies

Define your [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) and [Security Health Analytics detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-security-health-analytics). To define these policies using a security posture, complete the tasks in [Create and deploy a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#create_and_deploy_a_posture).

### Create your Terraform code

For instructions, see [Create your Terraform code](https://docs.cloud.google.com/security-command-center/docs/validate-iac#create_your_terraform_code).

## Validate your IAC in Cloud Build

**Note:** The samples in this section are YAML samples. IaC validation also supports JSON buildconfigs.

Add the following tasks to your `cloudbuild.yaml` file:

  1. Initialize Terraform:
         
         - name: hashicorp/terraform
           args:
             - '-c'
             - |
               terraform init \
                 -backend-config="bucket=STATE_BUCKET" \
                 -backend-config="prefix=REPOSITORY_NAME" \
           dir: FOLDER
           id: Terraform Init
           entrypoint: sh
         

Replace the following:

     * `STATE_BUCKET` with the name of the Cloud Storage bucket to [store the Terraform state](https://docs.cloud.google.com/docs/terraform/resource-management/store-state) in
     * `REPOSITORY_NAME` with the repository that hosts your Terraform code.
     * `FOLDER` with the name of the folder to save the Terraform artifacts to.
  2. Create a plan file:
         
         - name: hashicorp/terraform
           args:
             - '-c'
             - |
               terraform plan -out tf.plan
           dir: FOLDER
           id: Terraform Plan
           entrypoint: sh
         

  3. Convert the plan file to JSON format:
         
         - name: hashicorp/terraform
           args:
             - '-c'
             - |
               terraform show -json tf.plan > plan.json
           dir: FOLDER
           id: Terraform Show
           entrypoint: sh
         

  4. Create the IaC validation report:
         
         - name: gcr.io/cloud-builders/gcloud
           args:
             - '-c'
             - |
               gcloud scc iac-validation-reports create \
               organizations/ORGANIZATION_ID/locations/global --tf-plan-file=plan.json \
               --format="json(response.iacValidationReport)" > IaCScanReport_$BUILD_ID.json
           dir: FOLDER
           id: Run IaC scan
           entrypoint: /bin/bash
         

Replace `ORGANIZATION_ID` with your organization's ID.

  5. If you're using Cloud Storage, upload the JSON results file to Cloud Storage:
         
         - name: gcr.io/cloud-builders/gcloud
           args:
             - storage
             - cp
             - IaCScanReport_$BUILD_ID.json
             - SCAN_RESULT_FILE_BUCKET
           dir: FOLDER
           id: Upload report file
         

Replace `SCAN_RESULT_FILE_BUCKET` with the Cloud Storage bucket to upload the results file to.

  6. To view the results in SARIF format, complete the following:

     1. Convert the file:
            
            - name: golang
              args:
                - '-c'
                - |
                  go run github.com/google/gcp-scc-iac-validation-utils/SARIFConverter@latest \
                    --inputFilePath=IaCScanReport_$BUILD_ID.json
                    --outputFilePath=IaCScanReport_$BUILD_ID.sarif.json
              dir: FOLDER
              id: Convert to SARIF format
              entrypoint: /bin/bash
            

     2. Optional: upload the file to Cloud Storage:
            
            - name: gcr.io/cloud-builders/gcloud
              args:
                - storage
                - cp
                - IaCScanReport_$BUILD_ID.sarif.json
                - SCAN_RESULT_FILE_BUCKET
              dir: FOLDER
              id: Upload report file
            

  7. Validate the results. Complete this step on the results JSON file that you haven't converted to SARIF format:
         
         - name: golang
           args:
             - '-c'
             - |
               go run github.com/google/gcp-scc-iac-validation-utils/ReportValidator@latest \
                 --inputFilePath=IaCScanReport_$BUILD_ID.json --failure_expression=FAILURE_CRITERIA
           dir: FOLDER
           id: Validate results
           entrypoint: /bin/bash
         

Replace `FAILURE_CRITERIA` with the failure threshold criteria that determines when the build fails. The threshold criteria is based on the number of critical, high, medium, and low severity issues that the IaC validation scan encounters. `FAILURE_CRITERIA` specifies how many issues of each severity are permitted, and also specifies how the issues are aggregated (either `AND` or `OR`). For example, if you want the build to fail if it encounters one critical issue _or_ one high severity issue, set the `FAILURE_CRITERIA` to `Critical:1,High:1,Operator:OR`. The default is `Critical:1,High:1,Medium:1,Low:1,Operator:OR`, which means that if the IaC validation scan encounters a violation of any severity, the build must fail.

  8. If the build fails, resolve any violations within your Terraform code.




## What's next

  * View the [IaC validation report in Cloud Storage](https://docs.cloud.google.com/storage/docs/listing-objects#list-objects).
  * Review the [IaC validation scripts in GitHub](https://github.com/google/gcp-scc-iac-validation-utils).
  * Review the [`cloud.yaml` sample](https://github.com/google/devops-governance/blob/main/examples/guardrails/cloudbuild/folder-factory/.cloudbuild/workflows/cloudbuild.yaml).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
