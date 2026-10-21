---
url: https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-organization-policy/
title: Gate builds on organization policy \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:09.859345+00:00
---

# Gate builds on organization policy  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/gate-builds-organization-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Gate builds on organization policy Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build enables you to define an organization policy (`constraints/cloudbuild.allowedIntegrations`) to control which external services can invoke build triggers. For example, if your trigger listens for changes to a GitHub repository and GitHub is denied in the organization policy, your trigger will not run. You can specify any number of allowed or denied values for your organization or project.

This page explains how you can set up the organization policy (`constraints/cloudbuild.allowedIntegrations`) for integrations using Google Cloud console and the `gcloud` command-line tool.

## Before you Begin

  * Enable the Cloud Build and Organization Policy APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,orgpolicy.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/securing-builds/limit-builds-external-services)

  * To use the command-line examples in this guide, install and configure the [Google Cloud SDK](https://docs.cloud.google.com/sdk).

**Note:** If you've installed Google Cloud SDK previously, make sure you have the latest available version by running `gcloud components update`.
  * To set, change, or delete an organization policy, you must have the Organization Policy Administrator (`roles/orgpolicy.policyAdmin`) role. To learn how to add the role to your account, see [Add an organization policy administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin).




## Setting up organization policy for allowed integrations

This section explains how you can set up the organization policy (`constraints/cloudbuild.allowedIntegrations`) to define builds for allowed integrations.

###  Console 

  1. Open the **Organization policies** page in the Google Cloud console.

[Open the Organization policies page](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Click on the row containing the **Allowed Integrations (Cloud Build)** policy.

You will see the **Policy details** page.

  3. To edit the policy, click **Edit**.

You will see the **Edit policy** page.

  4. In the **Applies to** section, select **Customize** to set the definition for your policy.

  5. In the **Policy enforcement** section, select **Replace** to define your own rules for the policy. Otherwise, select **Merge with parent** to ensure that rules at the parent resource are applied to your settings. To learn more, see [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

  6. In the **Rules** section, click **Add rule** to add a new rule for your policy.

  7. Under **Policy values** , select **Allow all** to allow builds from all services, select **Deny all** to deny builds from all services, or select **Custom** to allow or deny builds from specific services.

If you select **Custom** as your value, complete the following steps:

     1. In the **Policy type** section, select **Allow** or **Deny**.

     2. In the **Custom values** section, enter the host URL of the instance or repository you want to allow or deny builds from. For example, to allow or deny builds from GitHub, enter your URL as `github.com` or `www.github.com`.

You can also enter multiple URLs separated by a space. For example, `github.com ghe.staging-test.com`.

Based on the event, the host URL you specify is one of the following:

        * RepoSync event: The host is `source.developers.google.com`.
        * GitHub app event: The host is derived from the `repository.html_url` field in your JSON payload, which is always `github.com`.
        * GitHub Enterprise event: The host is derived from the `repository.html_url` field in your JSON payload. For example, `ghe.staging-test.com`.
        * Pub/Sub event: The host is derived from the source specified in your trigger. If there is no source specified in your trigger, there is no organization policy check.
        * Webhook event: The host is derived from the source specified in your trigger. If there is no source specified in your trigger, there is no organization policy check.
**Note:** You can enter any characters in the **Custom values** section except colons (`:`) and forward slashes (`/`).
  8. To save your rule, click **Done**.

  9. To add another rule, click **Add rule**. Otherwise, to save your policy, click **Save**.




###  gcloud 

  1. Open a terminal window.

  2. If you want to allow or deny builds from all services, create a YAML file with the following contents:
         
         name: projects/PROJECT_NUMBER/policies/cloudbuild.allowedIntegrations
         spec:
           inheritFromParent: INHERIT
           rules:
             - ALLOW_OR_DENY: true
         

Where:

     * `PROJECT_NUMBER` is your project number.
     * `INHERIT` is `true` if you want your policy rules to be inherited from the parent resource. Otherwise, `false`.
     * `ALLOW_OR_DENY` is `allowAll` if you want to allow builds from all host URLs. Otherwise, `denyAll`.
     * `HOST_URL` is your host URL. For example, `github.com`. You can also specify additional URLs on the following lines.

If you want to allow or deny builds from selected services, create a YAML file with the following contents:
    
    name: projects/PROJECT_NUMBER/policies/cloudbuild.allowedIntegrations
    spec:
      inheritFromParent: INHERIT
      rules:
        - values:
            ALLOW_OR_DENY:
              HOST_URL
              ...
    

Where:

     * `PROJECT_NUMBER` is your project number.
     * `INHERIT` is `true` if you want your policy rules to be inherited from the parent resource. Otherwise, `false`.
     * `ALLOW_OR_DENY` is `allowedValues` if you want to specify host URLs to allow builds from. Otherwise, `deniedValues`.
     * `HOST_URL` is your host URL. For example, `github.com`. You can also specify additional URLs on the following lines.
**Note:** You can use any characters when specifying your host URL except colons (`:`) and forward slashes (`/`).
  3. Set your organization policy by running the following command, where FILE_NAME is the name of your YAML file:
         
         gcloud org-policies set-policy FILE_NAME
         

  4. To confirm that your policy has been set, run the following command, where PROJECT_ID is your project ID:
         
         gcloud org-policies describe cloudbuild.allowedIntegrations --effective --project PROJECT_ID
         




## Testing organization policy for allowed integrations

This section explains how you can test your organization policy (`constraints/cloudbuild.allowedIntegrations`) using build triggers.

  1. If you have not already done so, [create a build trigger](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers#build_trigger).

  2. Push a change to your source.

  3. If your policy is set up to allow builds from your source, you will be able to view build executions from your trigger on the [**Build history**](https://console.cloud.google.com/cloud-build/builds) page. Otherwise, your build will not execute. To view history for builds restricted by your policy definition, see the [**Logs Explorer**](https://console.cloud.google.com/logs/query) page for the JSON payload reason and the reason for denial.




## What's next

  * Learn to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn to [gate builds on approval](https://docs.cloud.google.com/build/docs/automating-builds/approve-builds).
  * Learn about [the permissions required to view build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-view-build-logs).
  * Learn about [audit logs created by Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/audit-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
