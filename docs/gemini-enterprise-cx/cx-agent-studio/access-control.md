---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/access-control/
title: Access control with IAM \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:16.199938+00:00
---

# Access control with IAM  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

It is common for multiple team members to collaborate on building an agent and for services to access the agent. Using _roles_ , you can control access and permissions granted to [principals](https://docs.cloud.google.com/docs/authentication#principal).

You can configure access using the [Google Cloud console](https://console.cloud.google.com/) with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs). The Google Cloud console is used to grant IAM roles to principals. See the [IAM quickstart](https://docs.cloud.google.com/iam/docs/grant-role-console) for detailed instructions on adding, editing, and removing permissions.

To access the settings, open the [IAM](https://console.cloud.google.com/iam-admin/iam) page in the Google Cloud console.

### Add a user or service account to the project

You can provide permissions to either users or service accounts by granting them roles on your Google Cloud project. Users are added by providing their email address. Service accounts are also added by providing their associated email address. You need to add service accounts when you want to use one service account for multiple projects. To find the email address associated with your service account, see the [IAM Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page in the Google Cloud console.

### Add a principal

To add a principal, do the following:

  1. Click **add** at the top of the page.
  2. Enter the principal's email address.
  3. Select a role.
  4. Click **Save**.



### Change permissions

To change permissions, do the following:

  1. Click **edit** for the principal.
  2. Select a different role.
  3. Click **Save**.



### Remove a principal

To remove a principal, click  **delete** for the principal.

## IAM roles

The following roles are available to access CX Agent Studio.

### Gemini Enterprise for Customer Experience Admin (`ces.googleapis.com/admin`)

This provides full access to resources.

Base roles:

  * `ces.googleapis.com/viewer`
  * `ces.googleapis.com/client`
  * `contactcenterinsights.googleapis.com/admin`



Additional permissions:

  * `ces.googleapis.com/operations.delete`
  * `ces.googleapis.com/operations.cancel`
  * `ces.googleapis.com/apps.create`
  * `ces.googleapis.com/apps.update`
  * `ces.googleapis.com/apps.delete`
  * `ces.googleapis.com/apps.import`
  * `ces.googleapis.com/apps.export`
  * `ces.googleapis.com/apps.runEvaluation`
  * `ces.googleapis.com/agents.create`
  * `ces.googleapis.com/agents.update`
  * `ces.googleapis.com/agents.updateCallbacks`
  * `ces.googleapis.com/agents.updateInstructions`
  * `ces.googleapis.com/agents.updateTools`
  * `ces.googleapis.com/agents.updateGeneral`
  * `ces.googleapis.com/agents.delete`
  * `ces.googleapis.com/examples.create`
  * `ces.googleapis.com/examples.update`
  * `ces.googleapis.com/examples.delete`
  * `ces.googleapis.com/tools.create`
  * `ces.googleapis.com/tools.update`
  * `ces.googleapis.com/tools.delete`
  * `ces.googleapis.com/guardrails.create`
  * `ces.googleapis.com/guardrails.update`
  * `ces.googleapis.com/guardrails.delete`
  * `ces.googleapis.com/toolsets.create`
  * `ces.googleapis.com/toolsets.update`
  * `ces.googleapis.com/toolsets.delete`
  * `ces.googleapis.com/deployments.create`
  * `ces.googleapis.com/deployments.update`
  * `ces.googleapis.com/deployments.delete`
  * `ces.googleapis.com/conversations.delete`
  * `ces.googleapis.com/evaluations.create`
  * `ces.googleapis.com/evaluations.update`
  * `ces.googleapis.com/evaluations.delete`
  * `ces.googleapis.com/evaluationResults.delete`
  * `ces.googleapis.com/evaluationDatasets.create`
  * `ces.googleapis.com/evaluationDatasets.update`
  * `ces.googleapis.com/evaluationDatasets.delete`
  * `ces.googleapis.com/evaluationRuns.delete`
  * `ces.googleapis.com/scheduledEvaluationRuns.create`
  * `ces.googleapis.com/scheduledEvaluationRuns.update`
  * `ces.googleapis.com/scheduledEvaluationRuns.delete`
  * `ces.googleapis.com/appVersions.create`
  * `ces.googleapis.com/appVersions.delete`
  * `ces.googleapis.com/appVersions.restore`
  * `ces.googleapis.com/omnichannels.create`
  * `ces.googleapis.com/omnichannels.update`
  * `ces.googleapis.com/omnichannels.delete`
  * `ces.googleapis.com/apps.createTagBinding`
  * `ces.googleapis.com/apps.deleteTagBinding`
  * `ces.googleapis.com/apps.listTagBindings`
  * `ces.googleapis.com/apps.listEffectiveTags`
  * `ces.googleapis.com/assistantSessions.create`
  * `ces.googleapis.com/routes.create`
  * `ces.googleapis.com/routes.update`
  * `ces.googleapis.com/routes.delete`
  * `ces.googleapis.com/endpointConfigs.create`
  * `ces.googleapis.com/endpointConfigs.update`
  * `ces.googleapis.com/endpointConfigs.delete`
  * `ces.googleapis.com/sipDomains.create`
  * `ces.googleapis.com/sipDomains.update`
  * `ces.googleapis.com/sipDomains.delete`
  * `ces.googleapis.com/securitySettings.update`



### Gemini Enterprise for Customer Experience Viewer (`ces.googleapis.com/viewer`)

This provides read-only access to resources.

Base roles:

  * `contactcenterinsights.googleapis.com/viewer`



Additional permissions:

  * `cloudresourcemanager.googleapis.com/projects.get`
  * `cloudresourcemanager.googleapis.com/projects.list`
  * `ces.googleapis.com/operations.list`
  * `ces.googleapis.com/operations.get`
  * `ces.googleapis.com/locations.list`
  * `ces.googleapis.com/locations.get`
  * `ces.googleapis.com/apps.list`
  * `ces.googleapis.com/apps.get`
  * `ces.googleapis.com/agents.list`
  * `ces.googleapis.com/agents.get`
  * `ces.googleapis.com/examples.list`
  * `ces.googleapis.com/examples.get`
  * `ces.googleapis.com/tools.list`
  * `ces.googleapis.com/tools.get`
  * `ces.googleapis.com/guardrails.list`
  * `ces.googleapis.com/guardrails.get`
  * `ces.googleapis.com/toolsets.list`
  * `ces.googleapis.com/toolsets.get`
  * `ces.googleapis.com/deployments.list`
  * `ces.googleapis.com/deployments.get`
  * `ces.googleapis.com/conversations.list`
  * `ces.googleapis.com/conversations.get`
  * `ces.googleapis.com/appVersions.list`
  * `ces.googleapis.com/appVersions.get`
  * `ces.googleapis.com/evaluations.list`
  * `ces.googleapis.com/evaluations.get`
  * `ces.googleapis.com/evaluationResults.list`
  * `ces.googleapis.com/evaluationResults.get`
  * `ces.googleapis.com/evaluationDatasets.list`
  * `ces.googleapis.com/evaluationDatasets.get`
  * `ces.googleapis.com/evaluationRuns.list`
  * `ces.googleapis.com/evaluationRuns.get`
  * `ces.googleapis.com/scheduledEvaluationRuns.list`
  * `ces.googleapis.com/scheduledEvaluationRuns.get`
  * `ces.googleapis.com/changelogs.list`
  * `ces.googleapis.com/changelogs.get`
  * `ces.googleapis.com/omnichannels.get`
  * `ces.googleapis.com/omnichannels.list`
  * `ces.googleapis.com/apps.listTagBindings`
  * `ces.googleapis.com/apps.listEffectiveTags`
  * `ces.googleapis.com/assistantSessions.list`
  * `ces.googleapis.com/assistantSessions.get`
  * `ces.googleapis.com/routes.list`
  * `ces.googleapis.com/routes.get`
  * `ces.googleapis.com/endpointConfigs.list`
  * `ces.googleapis.com/endpointConfigs.get`
  * `ces.googleapis.com/sipDomains.list`
  * `ces.googleapis.com/sipDomains.get`
  * `ces.googleapis.com/securitySettings.get`



### Gemini Enterprise for Customer Experience Client (`ces.googleapis.com/client`)

This provides query access to agents.

Permissions:

  * `ces.googleapis.com/sessions.runSession`
  * `ces.googleapis.com/sessions.bidiRunSession`
  * `ces.googleapis.com/tools.execute`



### Gemini Enterprise for Customer Experience App Editor (`ces.googleapis.com/appEditor`)

Full control over app-level settings. Manages global logging, audio/voice configurations, storage buckets, and app versions.

Base roles:

  * `ces.googleapis.com/viewer`



Additional permissions:

  * `ces.googleapis.com/apps.create`
  * `ces.googleapis.com/apps.update`
  * `ces.googleapis.com/apps.delete`
  * `ces.googleapis.com/apps.import`
  * `ces.googleapis.com/apps.export`
  * `ces.googleapis.com/apps.runEvaluation`
  * `ces.googleapis.com/apps.createTagBinding`
  * `ces.googleapis.com/apps.deleteTagBinding`
  * `ces.googleapis.com/appVersions.create`
  * `ces.googleapis.com/appVersions.delete`
  * `ces.googleapis.com/appVersions.restore`



### Gemini Enterprise for Customer Experience Agent Editor (`ces.googleapis.com/agentEditor`)

Full control over Agent node structures, flows, instructions, and callbacks. Can add/remove tools from agents (but not create new tools).

Base roles:

  * `ces.googleapis.com/viewer`
  * `ces.googleapis.com/client`



Additional permissions:

  * `ces.googleapis.com/agents.create`
  * `ces.googleapis.com/agents.update`
  * `ces.googleapis.com/agents.updateCallbacks`
  * `ces.googleapis.com/agents.updateInstructions`
  * `ces.googleapis.com/agents.updateTools`
  * `ces.googleapis.com/agents.updateGeneral`
  * `ces.googleapis.com/agents.delete`
  * `ces.googleapis.com/examples.create`
  * `ces.googleapis.com/examples.update`
  * `ces.googleapis.com/examples.delete`



### Gemini Enterprise for Customer Experience Tools Editor (`ces.googleapis.com/toolsEditor`)

Full control over Tools, Toolsets, and Integrations.

Base roles:

  * `ces.googleapis.com/viewer`
  * `ces.googleapis.com/client`



Additional permissions:

  * `ces.googleapis.com/tools.create`
  * `ces.googleapis.com/tools.update`
  * `ces.googleapis.com/tools.delete`
  * `ces.googleapis.com/toolsets.create`
  * `ces.googleapis.com/toolsets.update`
  * `ces.googleapis.com/toolsets.delete`



### Gemini Enterprise for Customer Experience Guardrails Editor (`ces.googleapis.com/guardrailsEditor`)

Full control over safety settings and guardrails.

Base roles:
    
    
    - ces.googleapis.com/viewer
    - ces.googleapis.com/client
    

Additional permissions:
    
    
    - ces.googleapis.com/guardrails.create
    - ces.googleapis.com/guardrails.update
    - ces.googleapis.com/guardrails.delete
    

### Gemini Enterprise for Customer Experience Evals Editor (`ces.googleapis.com/evalsEditor`)

Full control over Evaluation datasets, runs, and results.

Base roles:

  * `ces.googleapis.com/viewer`
  * `ces.googleapis.com/client`



Additional permissions:

  * `ces.googleapis.com/evaluations.create`
  * `ces.googleapis.com/evaluations.update`
  * `ces.googleapis.com/evaluations.delete`
  * `ces.googleapis.com/evaluationResults.delete`
  * `ces.googleapis.com/evaluationDatasets.create`
  * `ces.googleapis.com/evaluationDatasets.update`
  * `ces.googleapis.com/evaluationDatasets.delete`
  * `ces.googleapis.com/evaluationRuns.delete`
  * `ces.googleapis.com/scheduledEvaluationRuns.create`
  * `ces.googleapis.com/scheduledEvaluationRuns.update`
  * `ces.googleapis.com/scheduledEvaluationRuns.delete`



### Gemini Enterprise for Customer Experience Security Settings Editor (`ces.googleapis.com/securitySettingsEditor`)

Full control over project-wide Security Settings.

Base roles:

  * `ces.googleapis.com/viewer`



Additional permissions:

  * `ces.googleapis.com/securitySettings.update`



### Gemini Enterprise for Customer Experience Deployment Editor (`ces.googleapis.com/deploymentEditor`)

Ability to manage environments and deploy specific App Versions to them.

Base roles:

  * `ces.googleapis.com/viewer`



Additional permissions:

  * `ces.googleapis.com/deployments.create`
  * `ces.googleapis.com/deployments.update`
  * `ces.googleapis.com/deployments.delete`



## Customer Experience Insights

CX Agent Studio integrates with CX Insights, and you must provide the following CX Insights permissions to principals that access CX Agent Studio:

  * `contactcenterinsights.googleapis.com/conversations.get`
  * `contactcenterinsights.googleapis.com/conversations.list`



These permissions are automatically included by the child roles of `ces.googleapis.com/admin` and `ces.googleapis.com/viewer`. However, if you are defining custom roles, be sure to include these permissions in custom role definitions.

Alternatively, you can grant one of the following [CX Insights roles](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights) to relevant principals:

  * `contactcenterinsights.googleapis.com/viewer`: Provides read-only access to conversations
  * `contactcenterinsights.googleapis.com/admin`: Grants full access to conversations



In addition to roles, you may need to follow steps for [Discovery engine setup](https://docs.cloud.google.com/contact-center/insights/priv/docs/de-setup#before_you_begin).

## Requests that involve Cloud Storage access

Some CX Agent Studio requests access objects in [Cloud Storage](https://docs.cloud.google.com/storage/docs) for reading or writing data. When you call one of these requests, CX Agent Studio accesses the Cloud Storage data on the caller's behalf. This means that your request authentication must have permissions to access CX Agent Studio as well as the Cloud Storage objects.

When using a Google client library and IAM roles, see the [Cloud Storage access control guide](https://docs.cloud.google.com/storage/docs/access-control) for information on Cloud Storage roles.

When implementing your own client and using OAuth, you must use the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform` (access to all project resources)



## Add a condition to restrict access to one agent application

When adding or editing a principal, you can create [conditional role bindings](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings) that restrict access to one agent application.

The following condition provides access to a specific agent application as well as top-level resources within the project needed by the agent application:
    
    
    resource.name == "projects/PROJECT_ID" ||
    resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION_ID/apps/APP_ID") ||
    resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION_ID/operations") ||
    resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION_ID/sipDomains") ||
    resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION_ID/omnichannels") ||
    resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION_ID/dataStores") ||
    resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION_ID/routes") ||
    resource.name.startsWith("projects/PROJECT_ID/locations/LOCATION_ID/endpointConfigs")
    

In order to have access to Customer Experience Insights, you should grant Customer Experience Insights roles in addition to conditional granting.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
