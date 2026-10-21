---
url: https://docs.cloud.google.com/infrastructure-manager/docs/terraform-version-deprecation/
title: Terraform version management policy \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:18:54.490664+00:00
---

# Terraform version management policy  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/terraform-version-deprecation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Terraform version management policy Stay organized with collections  Save and categorize content based on your preferences. 

Infrastructure Manager uses specific versions of Terraform to provision and manage your Google Cloud resources. To provide access to new features and address security vulnerabilities, Infra Manager periodically updates the available Terraform versions. 

This document describes the policy for managing the lifecycle of these versions. The Terraform version management policy provides a transparent and predictable process for introducing new versions and deprecating versions for Infra Manager.

## How the policy works

Infra Manager publishes a list of available Terraform versions and their support status. Each version progresses through a lifecycle that includes _availability_ , _deprecation_ , and _end of support_.

This table shows the Terraform version deprecation information:

Terraform version | Date available | Deprecation date | End of support date | Auto-migrate to version  
---|---|---|---|---  
`1.2.3` | 8/21/2023 | 1/8/2026 | 2/8/2026 | `1.5.7`  
`1.3.10` | 3/14/2024 | TBD | TBD | TBD  
`1.4.7` | 3/14/2024 | TBD | TBD | TBD  
`1.5.7` | 3/14/2024 | TBD | TBD | TBD  
  
The columns in the table represent the following:

  * **Terraform version** : the identifier of the Terraform version.
  * **Date available** : the date when the version becomes available in Infra Manager.
  * **Deprecation date** : the date when the version is scheduled for deprecation. After this date, using the version to create or update deployments generates a warning.
  * **End of support date** : the date when the version is no longer supported. This period ends 180 days (or longer) after deprecation.

**Note:** For Terraform version `1.2.3`, this period ends one month after deprecation.
  * **Auto-migrate to version** : the version to which deployments are automatically migrated to after the end of support date (if you've opted into auto-migration).




To view the current list of supported versions and their lifecycle dates, see [Supported Terraform versions](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions).

## Version deprecation process

When a Terraform version reaches its deprecation date, it enters a deprecation period before its end of support date.

When a version is deprecated:

  * The public documentation is updated with the **Deprecation date** and **End of support date**.
  * Creating or updating a deployment or preview with the deprecated version returns a warning. This warning states that the version is deprecated and includes the end of support date.



After a version end of support date passes, the version is marked as obsolete. If you attempt to use an obsolete version to create a new deployment, the operation will fail with an error. If you attempt to update an existing deployment that references an obsolete version, the behavior depends on your organization's policy for auto-migration.

### Version availability process

When a new stable version of Terraform is available, it's added to the list of supported versions. The new Terraform version becomes available for use in the Google Cloud console, the gcloud CLI, and the API. The version management table is updated with the new version and its availability date, and an Infra Manager [release note](https://docs.cloud.google.com/infrastructure-manager/docs/release-notes) is created.

## Auto-migration

When you update an existing deployment that uses an unsupported version, Infra Manager can automatically update the deployment to a supported version. This auto-migration feature is an opt-in process that you configure through an organization policy.

If you haven't opted in to auto-migration, any update operation you perform on a deployment that uses an unsupported version will fail. To proceed, you must manually modify the deployment configuration to specify a supported version and then retry the operation.

### Configure your auto-migration policy

You can configure the auto-migration policy for Terraform versions on Infra Manager using Google Cloud CLI.

**Note:** You need to apply the auto-migration policy for each location in your project.

To enable your auto-migration policy:
    
    
    gcloud infra-manager automigrationconfig enable-auto-migration --project=PROJECT_ID --location=LOCATION
    

To describe your auto-migration policy:
    
    
    gcloud infra-manager automigrationconfig describe --project=PROJECT_ID --location=LOCATION
    

## What's next

  * To view the current list of supported versions and their lifecycle dates, see [Supported Terraform versions](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform#terraform_versions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
