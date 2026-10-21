---
url: https://docs.cloud.google.com/scheduler/docs/limiting/
title: Limit target types \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:00.424204+00:00
---

# Limit target types  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/limiting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Limit target types Stay organized with collections  Save and categorize content based on your preferences. 

Each cron job created using Cloud Scheduler is sent to a target according to a specified schedule, where the work for the task is accomplished. By default, all job target types are allowed. To limit which target type—HTTP, Pub/Sub, or App Engine HTTP—can be created in an organization, you can apply the `cloudscheduler.allowedTargetTypes` constraint when configuring an [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#how_organization_policy_works).

### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Apply the constraint

You can use the Google Cloud console or the Google Cloud CLI to apply the constraint to your organization policy.

###  Console 

  1. In the Google Cloud console, go to the **IAM & Admin** > **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. On the console toolbar, use the resource selector to select the project, folder, or organization for which you want to view organization policies.

A list of organization policy constraints that are available for this resource is displayed.

  3. Filter the list by the **Allowed target types for jobs** constraint name.

  4. In the row for the constraint, click more_vert **Actions** > **Edit policy**.

  5. On the Edit policy page, select **Override parent's policy**.

You can choose whether the policy includes rules from the parent folder or replaces the parent policy entirely.

  6. Under **Rules** , click **Add a rule**.

     1. In the **Policy values** list, select **Custom**.

     2. In the **Policy type** list, select **Allow**.

     3. Add a custom value of `APPENGINE`, `HTTP`, or `PUBSUB`.

     4. To add multiple job types, click add **Add value**.

     5. Click **Done**.

  7. To enforce the policy, click **Set policy**.




###  gcloud 

  1. To view the existing configuration of the constraint, use the [`gcloud org-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/describe) command:
         
         gcloud org-policies describe constraints/cloudscheduler.allowedTargetTypes \
             --RESOURCE_TYPE_FLAG=RESOURCE_ID
         

Replace the following:

     * `RESOURCE_TYPE_FLAG`: depending on where in the hierarchy the policy is attached, either `folder`, `organization`, or `project`.
     * `RESOURCE_ID`: the applicable folder, organization, or project ID.

The output should be similar to the following:
    
    etag: CJTvgc0GENDs+50B-
    name: projects/PROJECT_NUMBER/policies/cloudscheduler.allowedTargetTypes
    spec:
      etag: CJTvgc0GENDs+50B
      inheritFromParent: true
      rules:
      - values:
          allowedValues:
          - PUBSUB
      updateTime: '2026-02-26T16:40:52.331282Z'
    

  2. Set the policy on the resource using the [`gcloud org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) command. This overwrites the constraint attached to the resource.

     1. Create a temporary file, `/tmp/policy.yaml`, to store the policy. For example:
            
            name: projects/PROJECT_NUMBER/policies/cloudscheduler.allowedTargetTypes
            spec:
              rules:
              - values:
                  allowedValues:
                  - TARGET_TYPE
            

Replace the following:

        * `PROJECT_NUMBER`: your Google Cloud project number.
        * `TARGET_TYPE`: the job target type; either `APPENGINE`, `HTTP`, or `PUBSUB`.
     2. Run the `set-policy` command:
            
            gcloud org-policies set-policy /tmp/policy.yaml
            

  3. You can reset the constraint to its default using the [`gcloud org-policies reset`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/reset) command:
         
         gcloud org-policies reset constraints/cloudscheduler.allowedTargetTypes \
             --RESOURCE_TYPE_FLAG=RESOURCE_ID
         




Changes to organization policies can take up to 15 minutes to be fully enforced.

## What's next

  * [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints)
  * [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
