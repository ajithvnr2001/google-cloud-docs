---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/grant-access-open-models/
title: Grant user access to open models \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:16.263753+00:00
---

# Grant user access to open models  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/grant-access-open-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Grant user access to open models Stay organized with collections  Save and categorize content based on your preferences. 

For you to enable open models and make a prompt request, a Google Cloud administrator must set the required permissions and verify the organization policy allows the use of required APIs.

## Set required permissions to use open models

The following roles and permissions are required to use open models:

  * You must have the Consumer Procurement Entitlement Manager Identity and Access Management (IAM) role. Anyone who's been granted this role can enable open models in Model Garden.

  * You must have the `aiplatform.endpoints.predict` permission. This permission is included in the Agent Platform User IAM role. For more information, see [Gemini Enterprise Agent Platform User](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.user) and [Access control](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/access-control#permissions).




###  Console 

  1. To grant the Consumer Procurement Entitlement Manager IAM roles to a user, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam)

  2. In the **Principal** column, find the user [principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity) for which you want to enable access to open models, and then click edit **Edit principal** in that row.

  3. In the **Edit access** pane, click add **Add another role**.

  4. In **Select a role** , select **Consumer Procurement Entitlement Manager**.

  5. In the **Edit access** pane, click add **Add another role**.

  6. In **Select a role** , select **Agent Platform User**.

  7. Click **Save**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Grant the Consumer Procurement Entitlement Manager role that's required to enable open models in Model Garden
         
         gcloud projects add-iam-policy-binding  PROJECT_ID \
         --member=PRINCIPAL --role=roles/consumerprocurement.entitlementManager
         

  3. Grant the Agent Platform User role that includes the `aiplatform.endpoints.predict` permission which is required to make prompt requests:
         
         gcloud projects add-iam-policy-binding  PROJECT_ID \
         --member=PRINCIPAL --role=roles/aiplatform.user
         

Replace `PRINCIPAL` with the identifier for the principal. The identifier takes the form `user|group|serviceAccount:email` or `domain:domain`—for example, `user:cloudysanfrancisco@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`.

The output is a list of policy bindings that includes the following:
         
         -   members:
           -   user:PRINCIPAL
           role: roles/roles/consumerprocurement.entitlementManager
         

For more information, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) and [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).




## Set the organization policy for open model access

To enable open models, your organization policy must allow the following API: Cloud Commerce Consumer Procurement API - `cloudcommerceconsumerprocurement.googleapis.com`

If your organization sets an organization policy to [restrict service usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources), then an organization administrator must verify that `cloudcommerceconsumerprocurement.googleapis.com` is allowed by [setting the organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources#setting_the_organization_policy).

Also, if you have an organization policy that restricts model usage in Model Garden, the policy must allow access to open models. For more information, see [Control model access](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/control-model-access).

## What's next

  * Learn how to make a [Call MaaS APIs for open models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/call-open-model-apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
