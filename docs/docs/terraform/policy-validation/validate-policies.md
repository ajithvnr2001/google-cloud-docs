---
url: https://docs.cloud.google.com/docs/terraform/policy-validation/validate-policies/
title: Validate policies \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:02.786112+00:00
---

# Validate policies  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/policy-validation/validate-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Validate policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

### Install `Google Cloud CLI`

To use `gcloud beta terraform vet` you must first install Google Cloud CLI:

  1. Install Google Cloud CLI but skip the `gcloud init` command.

  2. Run the following commands to install the terraform-tools component:
         
         gcloud components update
         gcloud components install terraform-tools
         

  3. Verify that the gcloud CLI is installed by running the following command:
         
         gcloud beta terraform vet --help
         




### Get required permissions

The Google Cloud account that you use for validation must have the following permissions:

  * `getIamPolicy`: `gcloud beta terraform vet` needs to get full Identity and Access Management (IAM) policies and merge them with members and bindings to get an accurate end state to validate.
  * `resourcemanager.projects.get`: `gcloud beta terraform vet` needs to get project ancestry from the API in order to accurately construct a full CAI Asset Name for any projects that validated resources are related to.
  * `resourcemanager.folders.get`: `gcloud beta terraform vet` needs to get folder ancestry from the API in order to accurately construct a full CAI Asset Name if the validated resources contain any folder-related resources.



### Set up a policy library

You need to [create a policy library](https://docs.cloud.google.com/docs/terraform/policy_validation/create_policy_library) to use this tool.

## Validate policies

### 1\. Generate a Terraform plan

`gcloud beta terraform vet` is compatible with Terraform 0.12+. `gcloud beta terraform vet` takes `terraform plan` JSON as its input. You can generate the JSON file by running the following commands in your Terraform directory:
    
    
    terraform plan -out=tfplan.tfplan
    terraform show -json ./tfplan.tfplan > ./tfplan.json
    

### 2\. Run `gcloud beta terraform vet`

`gcloud beta terraform vet` lets you validate your `terraform plan` JSON against your organization's POLICY_LIBRARY_REPO. For example:
    
    
    git clone POLICY_LIBRARY_REPO POLICY_LIBRARY_DIR
    gcloud beta terraform vet tfplan.json --policy-library=POLICY_LIBRARY_DIR
    

When you execute this command, `gcloud beta terraform vet` retrieves project data by using Google Cloud APIs that are necessary for an accurate validation of your plan.

#### Flags

  * `--policy-library=POLICY_LIBRARY_DIR` \- Directory that contains a policy library.
  * `--project=PROJECT_ID` \- `gcloud beta terraform vet` accepts an optional `--project` flag. This flag specifies the [default project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) when building the ancestry (from the Google Cloud resource hierarchy) for any resource that doesn't have an explicit project set.
  * `--format=FORMAT` \- The default is yaml. The supported formats are: `default`, `json`, `none`, `text`, `yaml`. For more details run $ [gcloud topic formats](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats).



#### Exit code and output

  * If all constraints are validated, the command returns exit code 0 and does not display violations.
  * If violations are found, `gcloud beta terraform vet` returns exit code 2, and displays a list of violations. For example, JSON output might look like:


    
    
    [
      {
        "constraint": "GCPIAMAllowedPolicyMemberDomainsConstraintV2.service_accounts_only",
        "constraint_config": {
          "api_version": "constraints.gatekeeper.sh/v1alpha1",
          "kind": "GCPIAMAllowedPolicyMemberDomainsConstraintV2",
          "metadata": {
            "annotations": {
              "description": "Checks that members that have been granted IAM roles belong to allowlisted domains.",
              "validation.gcp.forsetisecurity.org/originalName": "service_accounts_only",
              "validation.gcp.forsetisecurity.org/yamlpath": "policies/constraints/iam_service_accounts_only.yaml"
            },
            "name": "service-accounts-only"
          },
          "spec": {
            "match": {
              "target": [
                "organizations/**"
              ]
            },
            "parameters": {
              "domains": [
                "gserviceaccount.com"
              ]
            },
            "severity": "high"
          }
        },
        "message": "IAM policy for //cloudresourcemanager.googleapis.com/projects/PROJECT_ID contains member from unexpected domain: user:me@example.com",
        "metadata": {
          "ancestry_path": "organizations/ORG_ID/projects/PROJECT_ID",
          "constraint": {
            "annotations": {
              "description": "Checks that members that have been granted IAM roles belong to allowlisted domains.",
              "validation.gcp.forsetisecurity.org/originalName": "service_accounts_only",
              "validation.gcp.forsetisecurity.org/yamlpath": "policies/constraints/iam_service_accounts_only.yaml"
            },
            "labels": {},
            "parameters": {
              "domains": [
                "gserviceaccount.com"
              ]
            }
          },
          "details": {
            "member": "user:me@example.com",
            "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID"
          }
        },
        "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
        "severity": "high"
      }
    ]
    

## CI/CD example

A bash script for using `gcloud beta terraform vet` in a CI/CD pipeline might look like this:
    
    
    terraform plan -out=tfplan.tfplan
    terraform show -json ./tfplan.tfplan > ./tfplan.json
    git clone POLICY_LIBRARY_REPO POLICY_LIBRARY_DIR
    VIOLATIONS=$(gcloud beta terraform vet tfplan.json --policy-library=POLICY_LIBRARY_DIR --format=json)
    retVal=$?
    if [ $retVal -eq 2 ]; then
      # Optional: parse the VIOLATIONS variable as json and check the severity level
      echo "$VIOLATIONS"
      echo "Violations found; not proceeding with terraform apply"
      exit 1
    fi
    if [ $retVal -ne 0]; then
      echo "Error during gcloud beta terraform vet; not proceeding with terraform apply"
      exit 1
    fi
    
    echo "No policy violations detected; proceeding with terraform apply"
    
    terraform apply

Developers can also use `gcloud beta terraform vet` locally to test Terraform changes prior to running your CI/CD pipeline.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
