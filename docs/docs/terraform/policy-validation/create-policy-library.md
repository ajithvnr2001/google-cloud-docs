---
url: https://docs.cloud.google.com/docs/terraform/policy-validation/create-policy-library/
title: Create a policy library \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:46.584474+00:00
---

# Create a policy library  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/policy-validation/create-policy-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Create a policy library Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

As an organization administrator, you need to define policies that developers adhere to when applying infrastructure as code. Your organization's set of policies is represented as a policy library. This page helps you create a centralized policy repository and add constraints.

## Before you begin

  * You need an empty Git repository for storing your organization's policy library.
  * You need to configure Git to connect securely. For example, if your git repository is on GitHub, you can follow the process outlined in [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).



## Duplicate the sample library

Google provides a sample repository that includes a set of pre-defined constraint templates which you can modify for your personal use.

  1. Clone the policy library sample repository and duplicate it to your POLICY_LIBRARY_REPO:
         
         git clone https://github.com/GoogleCloudPlatform/policy-library.git
         cd policy-library
         git remote set-url origin POLICY_LIBRARY_REPO
         git push origin main
         

  2. Examine the available constraint templates in `policies/templates`: `ls policies/templates`

  3. Select the constraint templates you want to use. For this example, choose `gcp_storage_location_v1.yaml`, which enforces location for Cloud Storage buckets.

  4. Create constraint YAML files corresponding to those templates under `policies/constraints`.

  5. From inside your local copy of the `policy-library` repository, use the following commands to commit and push your changes:
         
         git add --all .
         git commit -m "Initial commit of policy library constraints"
         git push -u origin main
         




### Library structure

A policy library repository contains the following directories:

  * `policies/` – This directory contains two subdirectories:

    * `constraints/` – This directory is initially empty. Place your constraint files here.
    * `templates/` – This directory contains pre-defined constraint templates.
  * `validator/` – This directory contains the `.rego` files and their associated unit tests. You don't need to touch this directory unless you intend to modify existing constraint templates or create new ones. Running `make build` inlines the Rego content in the corresponding constraint template files.




## Periodic updates

Periodically you should pull any changes from the public repository, which might contain new templates and Rego files.
    
    
    git remote add public https://github.com/GoogleCloudPlatform/policy-library.git
    git pull public main
    git push origin main
    

## Next steps

The policy library contains a number of constraint templates and a `samples` folder with example constraints. Read [Create Terraform constraints](https://docs.cloud.google.com/docs/terraform/policy-validation/create-terraform-constraints) or [Create CAI constraints](https://docs.cloud.google.com/docs/terraform/policy-validation/create-cai-constraints) for details on how to write and use constraint templates and constraints.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
