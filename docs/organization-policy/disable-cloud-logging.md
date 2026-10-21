---
url: https://docs.cloud.google.com/organization-policy/disable-cloud-logging/
title: Disable Cloud Logging for the Cloud Healthcare API \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:04.663272+00:00
---

# Disable Cloud Logging for the Cloud Healthcare API  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/disable-cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Disable Cloud Logging for the Cloud Healthcare API Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Overview

This guide explains how to set a constraint (`constraints/gcp.disableCloudLogging`) that disables Cloud Logging for the Cloud Healthcare API at the level of an organization, a project, or a folder. The constraint does not affect Cloud Audit Logs. Logs that are generated before the constraint takes effect are not deleted and can be accessed after the constraint takes effect.

**Note:** The constraint is only supported in the Cloud Healthcare API.

## Disabling Cloud Logging for the Cloud Healthcare API

To disable Cloud Logging for the Cloud Healthcare API, you must have the [Organization Administrator](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#adding_an_organization_administrator) (`roles/resourcemanager.organizationAdmin`) role. This role can only be granted at the Organization level. You must have the **Organization Policy Administrator** (`roles/orgpolicy.policyAdminrole`) to set or change organization policies.

### Console

To disable Cloud Logging for the Cloud Healthcare API:

  1. Sign in to the Google Cloud console as a Google Workspace or Cloud Identity super administrator and go to the **Organization policies** page:

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Click **Select** , and then select the project, folder, or organization for which you want to view organization policies. The **Organization policies** page displays a filterable list of organization policy constraints that are available.

  3. In the list of policies that appears, select **Disable Cloud Logging for Cloud Healthcare API**. The **Disable Cloud Logging for Cloud Healthcare API** policy uses the `constraints/gcp.disableCloudLogging` ID. The **Policy details** page that appears describes the constraint and provides information about how the constraint is applied.

  4. To update the organization policy, click **Manage policy**.

  5. On the **Edit policy** page, select **Override parent's policy**.

  6. Click **Add a rule**.

  7. Under **Enforcement** , select an enforcement option:

     * To enable the constraint and disable Cloud Logging for the Cloud Healthcare API, select **On**.
     * To disable the constraint and enable Cloud Logging for the Cloud Healthcare API, select **Off**.
  8. To enforce the policy, click **Set policy**.




### gcloud

  1. Get the current policy on the organization resource using the `describe` command:
         
         gcloud org-policies describe gcp.disableCloudLogging \
           --organization=ORGANIZATION_ID
         

Replace the [ORGANIZATION_ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id): with the unique identifier for the organization resource. You can also apply the organization policy to a folder or a project with the `--folder` or the `--project` flags, and the [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#folder-access) and [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects), respectively.

Because a policy isn't set, this returns a `NOT_FOUND` error:
         
         ERROR: (gcloud.org-policies.describe) NOT_FOUND: Requested entity was not found.
         

  2. Set the policy on the organization using the `set-policy` command.

     1. Create a temporary file `/tmp/policy.yaml` to store the policy:
            
            name: organizations/ORGANIZATION_ID/policies/gcp.disableCloudLogging
            spec:
              rules:
              - enforce: true
            

     2. Run the `set-policy` command:
            
            gcloud org-policies set-policy /tmp/policy.yaml
            

  3. View the current effective policy using the `describe --effective` command:
         
         gcloud org-policies describe \
           gcp.disableCloudLogging --effective \
           --organization=ORGANIZATION_ID
         

After running the command, the following output displays:
         
         name: organizations/ORGANIZATION_ID/policies/gcp.disableCloudLogging
         spec:
           rules:
           - enforce: true
         




## What's next

See [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies) for more information on creating an organization policy with a particular constraint.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
