---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow/
title: Dialogflow roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:58.619971+00:00
---

# Dialogflow roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Dialogflow roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Dialogflow. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Dialogflow roles

Role | Permissions  
---|---  
  
#### Dialogflow API Admin 

(`roles/dialogflow.admin`) Grant to Dialogflow API admins that need full access to Dialogflow-specific resources. Also see [Dialogflow access control](https://docs.cloud.google.com/dialogflow/docs/access-control).  **Caution:** Users with permissions to create or modify Dialogflow agent components, such as tools and webhooks, can configure these components to authenticate as the Dialogflow Service Agent using ID tokens. This capability can be used to interact with other Google Cloud services that accept ID token authentication using the permissions granted to the [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent). Carefully control who is granted permissions to configure these Dialogflow agent components.  Lowest-level resources where you can grant this role:

  * Project 

|  `dialogflow.*`

  * `dialogflow.agents.create`
  * `dialogflow.agents.delete`
  * `dialogflow.agents.export`
  * `dialogflow.agents.get`
  * `dialogflow.agents.import`
  * `dialogflow.agents.list`
  * `dialogflow.agents.restore`
  * `dialogflow.agents.search`
  * `dialogflow.agents.searchResources`
  * `dialogflow.agents.train`
  * `dialogflow.agents.update`
  * `dialogflow.agents.validate`
  * `dialogflow.answerrecords.delete`
  * `dialogflow.answerrecords.get`
  * `dialogflow.answerrecords.list`
  * `dialogflow.answerrecords.update`
  * `dialogflow.callMatchers.create`
  * `dialogflow.callMatchers.delete`
  * `dialogflow.callMatchers.list`
  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`
  * `dialogflow.companionAgents.create`
  * `dialogflow.companionAgents.delete`
  * `dialogflow.companionAgents.get`
  * `dialogflow.companionAgents.list`
  * `dialogflow.companionAgents.update`
  * `dialogflow.contexts.create`
  * `dialogflow.contexts.delete`
  * `dialogflow.contexts.get`
  * `dialogflow.contexts.list`
  * `dialogflow.contexts.update`
  * `dialogflow.conversationDatasets.create`
  * `dialogflow.conversationDatasets.delete`
  * `dialogflow.conversationDatasets.get`
  * `dialogflow.conversationDatasets.import`
  * `dialogflow.conversationDatasets.list`
  * `dialogflow.conversationModels.create`
  * `dialogflow.conversationModels.delete`
  * `dialogflow.conversationModels.deploy`
  * `dialogflow.conversationModels.get`
  * `dialogflow.conversationModels.list`
  * `dialogflow.conversationModels.undeploy`
  * `dialogflow.conversationProfiles.create`
  * `dialogflow.conversationProfiles.delete`
  * `dialogflow.conversationProfiles.get`
  * `dialogflow.conversationProfiles.list`
  * `dialogflow.conversationProfiles.update`
  * `dialogflow.conversations.addPhoneNumber`
  * `dialogflow.conversations.complete`
  * `dialogflow.conversations.create`
  * `dialogflow.conversations.get`
  * `dialogflow.conversations.list`
  * `dialogflow.conversations.update`
  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`
  * `dialogflow.documents.create`
  * `dialogflow.documents.delete`
  * `dialogflow.documents.get`
  * `dialogflow.documents.list`
  * `dialogflow.encryptionspec.get`
  * `dialogflow.encryptionspec.update`
  * `dialogflow.entityTypes.create`
  * `dialogflow.entityTypes.createEntity`
  * `dialogflow.entityTypes.delete`
  * `dialogflow.entityTypes.deleteEntity`
  * `dialogflow.entityTypes.get`
  * `dialogflow.entityTypes.list`
  * `dialogflow.entityTypes.update`
  * `dialogflow.entityTypes.updateEntity`
  * `dialogflow.environments.create`
  * `dialogflow.environments.delete`
  * `dialogflow.environments.get`
  * `dialogflow.environments.getHistory`
  * `dialogflow.environments.list`
  * `dialogflow.environments.lookupHistory`
  * `dialogflow.environments.runContinuousTest`
  * `dialogflow.environments.update`
  * `dialogflow.examples.create`
  * `dialogflow.examples.delete`
  * `dialogflow.examples.get`
  * `dialogflow.examples.list`
  * `dialogflow.examples.update`
  * `dialogflow.experiments.create`
  * `dialogflow.experiments.delete`
  * `dialogflow.experiments.get`
  * `dialogflow.experiments.list`
  * `dialogflow.experiments.update`
  * `dialogflow.flows.create`
  * `dialogflow.flows.delete`
  * `dialogflow.flows.get`
  * `dialogflow.flows.list`
  * `dialogflow.flows.train`
  * `dialogflow.flows.update`
  * `dialogflow.flows.validate`
  * `dialogflow.fulfillments.get`
  * `dialogflow.fulfillments.update`
  * `dialogflow.generators.create`
  * `dialogflow.generators.delete`
  * `dialogflow.generators.get`
  * `dialogflow.generators.list`
  * `dialogflow.generators.update`
  * `dialogflow.integrations.create`
  * `dialogflow.integrations.delete`
  * `dialogflow.integrations.get`
  * `dialogflow.integrations.list`
  * `dialogflow.integrations.update`
  * `dialogflow.intents.create`
  * `dialogflow.intents.delete`
  * `dialogflow.intents.get`
  * `dialogflow.intents.list`
  * `dialogflow.intents.update`
  * `dialogflow.interactionMonitoringAlerts.ack`
  * `dialogflow.interactionMonitoringAlerts.get`
  * `dialogflow.knowledgeBases.create`
  * `dialogflow.knowledgeBases.delete`
  * `dialogflow.knowledgeBases.get`
  * `dialogflow.knowledgeBases.list`
  * `dialogflow.knowledgeBases.update`
  * `dialogflow.messages.list`
  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`
  * `dialogflow.operations.get`
  * `dialogflow.pages.create`
  * `dialogflow.pages.delete`
  * `dialogflow.pages.get`
  * `dialogflow.pages.list`
  * `dialogflow.pages.update`
  * `dialogflow.participants.analyzeContent`
  * `dialogflow.participants.create`
  * `dialogflow.participants.get`
  * `dialogflow.participants.list`
  * `dialogflow.participants.suggest`
  * `dialogflow.participants.update`
  * `dialogflow.phoneNumberOrders.cancel`
  * `dialogflow.phoneNumberOrders.create`
  * `dialogflow.phoneNumberOrders.get`
  * `dialogflow.phoneNumberOrders.list`
  * `dialogflow.phoneNumberOrders.update`
  * `dialogflow.phoneNumbers.delete`
  * `dialogflow.phoneNumbers.list`
  * `dialogflow.phoneNumbers.undelete`
  * `dialogflow.phoneNumbers.update`
  * `dialogflow.playbooks.create`
  * `dialogflow.playbooks.delete`
  * `dialogflow.playbooks.get`
  * `dialogflow.playbooks.list`
  * `dialogflow.playbooks.update`
  * `dialogflow.securitySettings.create`
  * `dialogflow.securitySettings.delete`
  * `dialogflow.securitySettings.get`
  * `dialogflow.securitySettings.list`
  * `dialogflow.securitySettings.update`
  * `dialogflow.sessionEntityTypes.create`
  * `dialogflow.sessionEntityTypes.delete`
  * `dialogflow.sessionEntityTypes.get`
  * `dialogflow.sessionEntityTypes.list`
  * `dialogflow.sessionEntityTypes.update`
  * `dialogflow.sessions.detectIntent`
  * `dialogflow.sessions.streamingDetectIntent`
  * `dialogflow.smartMessagingEntries.create`
  * `dialogflow.smartMessagingEntries.delete`
  * `dialogflow.smartMessagingEntries.get`
  * `dialogflow.smartMessagingEntries.list`
  * `dialogflow.testcases.calculateCoverage`
  * `dialogflow.testcases.create`
  * `dialogflow.testcases.delete`
  * `dialogflow.testcases.export`
  * `dialogflow.testcases.get`
  * `dialogflow.testcases.import`
  * `dialogflow.testcases.list`
  * `dialogflow.testcases.run`
  * `dialogflow.testcases.update`
  * `dialogflow.tools.create`
  * `dialogflow.tools.delete`
  * `dialogflow.tools.get`
  * `dialogflow.tools.list`
  * `dialogflow.tools.update`
  * `dialogflow.transitionRouteGroups.create`
  * `dialogflow.transitionRouteGroups.delete`
  * `dialogflow.transitionRouteGroups.get`
  * `dialogflow.transitionRouteGroups.list`
  * `dialogflow.transitionRouteGroups.update`
  * `dialogflow.versions.create`
  * `dialogflow.versions.delete`
  * `dialogflow.versions.get`
  * `dialogflow.versions.list`
  * `dialogflow.versions.load`
  * `dialogflow.versions.update`
  * `dialogflow.webhooks.create`
  * `dialogflow.webhooks.delete`
  * `dialogflow.webhooks.get`
  * `dialogflow.webhooks.list`
  * `dialogflow.webhooks.update`

`resourcemanager.projects.get`  
  
#### Dialogflow Viewer 

(`roles/dialogflow.viewer`) Viewer role for dialogflow  |  `dialogflow.agents.export` `dialogflow.agents.get` `dialogflow.agents.list` `dialogflow.agents.search` `dialogflow.agents.searchResources` `dialogflow.answerrecords.get` `dialogflow.answerrecords.list` `dialogflow.callMatchers.list` `dialogflow.changelogs.*`

  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`

`dialogflow.companionAgents.get` `dialogflow.companionAgents.list` `dialogflow.contexts.get` `dialogflow.contexts.list` `dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.get` `dialogflow.conversations.list` `dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.encryptionspec.get` `dialogflow.entityTypes.get` `dialogflow.entityTypes.list` `dialogflow.environments.get` `dialogflow.environments.getHistory` `dialogflow.environments.list` `dialogflow.environments.lookupHistory` `dialogflow.examples.get` `dialogflow.examples.list` `dialogflow.experiments.get` `dialogflow.experiments.list` `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.fulfillments.get` `dialogflow.generators.get` `dialogflow.generators.list` `dialogflow.integrations.get` `dialogflow.integrations.list` `dialogflow.intents.get` `dialogflow.intents.list` `dialogflow.interactionMonitoringAlerts.get` `dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.modelEvaluations.*`

  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`

`dialogflow.operations.get` `dialogflow.pages.get` `dialogflow.pages.list` `dialogflow.participants.get` `dialogflow.participants.list` `dialogflow.participants.suggest` `dialogflow.phoneNumberOrders.get` `dialogflow.phoneNumberOrders.list` `dialogflow.phoneNumbers.list` `dialogflow.playbooks.get` `dialogflow.playbooks.list` `dialogflow.securitySettings.get` `dialogflow.securitySettings.list` `dialogflow.sessionEntityTypes.get` `dialogflow.sessionEntityTypes.list` `dialogflow.smartMessagingEntries.get` `dialogflow.smartMessagingEntries.list` `dialogflow.testcases.calculateCoverage` `dialogflow.testcases.export` `dialogflow.testcases.get` `dialogflow.testcases.list` `dialogflow.tools.get` `dialogflow.tools.list` `dialogflow.transitionRouteGroups.get` `dialogflow.transitionRouteGroups.list` `dialogflow.versions.get` `dialogflow.versions.list` `dialogflow.webhooks.get` `dialogflow.webhooks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### CX Premium Admin 

(`roles/dialogflow.aamAdmin`) An admin has access to all resources and can perform all administrative actions in an AAM project.  |  `dialogflow.agents.export` `dialogflow.agents.get` `dialogflow.agents.list` `dialogflow.agents.search` `dialogflow.agents.searchResources` `dialogflow.answerrecords.get` `dialogflow.answerrecords.list` `dialogflow.callMatchers.list` `dialogflow.changelogs.*`

  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`

`dialogflow.companionAgents.get` `dialogflow.companionAgents.list` `dialogflow.contexts.get` `dialogflow.contexts.list` `dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.get` `dialogflow.conversations.list` `dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.encryptionspec.get` `dialogflow.entityTypes.get` `dialogflow.entityTypes.list` `dialogflow.environments.get` `dialogflow.environments.list` `dialogflow.examples.get` `dialogflow.examples.list` `dialogflow.experiments.get` `dialogflow.experiments.list` `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.fulfillments.get` `dialogflow.generators.get` `dialogflow.generators.list` `dialogflow.integrations.get` `dialogflow.integrations.list` `dialogflow.intents.get` `dialogflow.intents.list` `dialogflow.interactionMonitoringAlerts.get` `dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.modelEvaluations.*`

  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`

`dialogflow.operations.get` `dialogflow.pages.get` `dialogflow.pages.list` `dialogflow.participants.get` `dialogflow.participants.list` `dialogflow.phoneNumberOrders.get` `dialogflow.phoneNumberOrders.list` `dialogflow.phoneNumbers.list` `dialogflow.playbooks.get` `dialogflow.playbooks.list` `dialogflow.securitySettings.get` `dialogflow.securitySettings.list` `dialogflow.sessionEntityTypes.get` `dialogflow.sessionEntityTypes.list` `dialogflow.smartMessagingEntries.get` `dialogflow.smartMessagingEntries.list` `dialogflow.testcases.get` `dialogflow.testcases.list` `dialogflow.tools.get` `dialogflow.tools.list` `dialogflow.transitionRouteGroups.get` `dialogflow.transitionRouteGroups.list` `dialogflow.versions.get` `dialogflow.versions.list` `dialogflow.webhooks.get` `dialogflow.webhooks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### CX Premium Conversational Architect 

(`roles/dialogflow.aamConversationalArchitect`) A Conversational Architect can label conversational data, approve taxonomy changes and design virtual agents for a customer's use cases.  |  `dialogflow.agents.export` `dialogflow.agents.get` `dialogflow.agents.list` `dialogflow.agents.search` `dialogflow.agents.searchResources` `dialogflow.answerrecords.get` `dialogflow.answerrecords.list` `dialogflow.callMatchers.list` `dialogflow.changelogs.*`

  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`

`dialogflow.companionAgents.get` `dialogflow.companionAgents.list` `dialogflow.contexts.get` `dialogflow.contexts.list` `dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.get` `dialogflow.conversations.list` `dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.encryptionspec.get` `dialogflow.entityTypes.get` `dialogflow.entityTypes.list` `dialogflow.environments.get` `dialogflow.environments.list` `dialogflow.examples.get` `dialogflow.examples.list` `dialogflow.experiments.get` `dialogflow.experiments.list` `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.fulfillments.get` `dialogflow.generators.get` `dialogflow.generators.list` `dialogflow.integrations.get` `dialogflow.integrations.list` `dialogflow.intents.get` `dialogflow.intents.list` `dialogflow.interactionMonitoringAlerts.get` `dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.modelEvaluations.*`

  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`

`dialogflow.operations.get` `dialogflow.pages.get` `dialogflow.pages.list` `dialogflow.participants.get` `dialogflow.participants.list` `dialogflow.phoneNumberOrders.get` `dialogflow.phoneNumberOrders.list` `dialogflow.phoneNumbers.list` `dialogflow.playbooks.get` `dialogflow.playbooks.list` `dialogflow.securitySettings.get` `dialogflow.securitySettings.list` `dialogflow.sessionEntityTypes.get` `dialogflow.sessionEntityTypes.list` `dialogflow.smartMessagingEntries.get` `dialogflow.smartMessagingEntries.list` `dialogflow.testcases.get` `dialogflow.testcases.list` `dialogflow.tools.get` `dialogflow.tools.list` `dialogflow.transitionRouteGroups.get` `dialogflow.transitionRouteGroups.list` `dialogflow.versions.get` `dialogflow.versions.list` `dialogflow.webhooks.get` `dialogflow.webhooks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### CX Premium Dialog Designer 

(`roles/dialogflow.aamDialogDesigner`) A Dialog Designer can label conversational data and propose taxonomy changes for virtual agent modeling.  |  `dialogflow.agents.export` `dialogflow.agents.get` `dialogflow.agents.list` `dialogflow.agents.search` `dialogflow.agents.searchResources` `dialogflow.answerrecords.get` `dialogflow.answerrecords.list` `dialogflow.callMatchers.list` `dialogflow.changelogs.*`

  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`

`dialogflow.companionAgents.get` `dialogflow.companionAgents.list` `dialogflow.contexts.get` `dialogflow.contexts.list` `dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.get` `dialogflow.conversations.list` `dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.encryptionspec.get` `dialogflow.entityTypes.get` `dialogflow.entityTypes.list` `dialogflow.environments.get` `dialogflow.environments.list` `dialogflow.examples.get` `dialogflow.examples.list` `dialogflow.experiments.get` `dialogflow.experiments.list` `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.fulfillments.get` `dialogflow.generators.get` `dialogflow.generators.list` `dialogflow.integrations.get` `dialogflow.integrations.list` `dialogflow.intents.get` `dialogflow.intents.list` `dialogflow.interactionMonitoringAlerts.get` `dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.modelEvaluations.*`

  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`

`dialogflow.operations.get` `dialogflow.pages.get` `dialogflow.pages.list` `dialogflow.participants.get` `dialogflow.participants.list` `dialogflow.phoneNumberOrders.get` `dialogflow.phoneNumberOrders.list` `dialogflow.phoneNumbers.list` `dialogflow.playbooks.get` `dialogflow.playbooks.list` `dialogflow.securitySettings.get` `dialogflow.securitySettings.list` `dialogflow.sessionEntityTypes.get` `dialogflow.sessionEntityTypes.list` `dialogflow.smartMessagingEntries.get` `dialogflow.smartMessagingEntries.list` `dialogflow.testcases.get` `dialogflow.testcases.list` `dialogflow.tools.get` `dialogflow.tools.list` `dialogflow.transitionRouteGroups.get` `dialogflow.transitionRouteGroups.list` `dialogflow.versions.get` `dialogflow.versions.list` `dialogflow.webhooks.get` `dialogflow.webhooks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### CX Premium Lead Dialog Designer 

(`roles/dialogflow.aamLeadDialogDesigner`) A Dialog Designer Lead can label conversational data and approve taxonomy changes for virtual agent modeling.  |  `dialogflow.agents.export` `dialogflow.agents.get` `dialogflow.agents.list` `dialogflow.agents.search` `dialogflow.agents.searchResources` `dialogflow.answerrecords.get` `dialogflow.answerrecords.list` `dialogflow.callMatchers.list` `dialogflow.changelogs.*`

  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`

`dialogflow.companionAgents.get` `dialogflow.companionAgents.list` `dialogflow.contexts.get` `dialogflow.contexts.list` `dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.get` `dialogflow.conversations.list` `dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.encryptionspec.get` `dialogflow.entityTypes.get` `dialogflow.entityTypes.list` `dialogflow.environments.get` `dialogflow.environments.list` `dialogflow.examples.get` `dialogflow.examples.list` `dialogflow.experiments.get` `dialogflow.experiments.list` `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.fulfillments.get` `dialogflow.generators.get` `dialogflow.generators.list` `dialogflow.integrations.get` `dialogflow.integrations.list` `dialogflow.intents.get` `dialogflow.intents.list` `dialogflow.interactionMonitoringAlerts.get` `dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.modelEvaluations.*`

  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`

`dialogflow.operations.get` `dialogflow.pages.get` `dialogflow.pages.list` `dialogflow.participants.get` `dialogflow.participants.list` `dialogflow.phoneNumberOrders.get` `dialogflow.phoneNumberOrders.list` `dialogflow.phoneNumbers.list` `dialogflow.playbooks.get` `dialogflow.playbooks.list` `dialogflow.securitySettings.get` `dialogflow.securitySettings.list` `dialogflow.sessionEntityTypes.get` `dialogflow.sessionEntityTypes.list` `dialogflow.smartMessagingEntries.get` `dialogflow.smartMessagingEntries.list` `dialogflow.testcases.get` `dialogflow.testcases.list` `dialogflow.tools.get` `dialogflow.tools.list` `dialogflow.transitionRouteGroups.get` `dialogflow.transitionRouteGroups.list` `dialogflow.versions.get` `dialogflow.versions.list` `dialogflow.webhooks.get` `dialogflow.webhooks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### CX Premium Viewer 

(`roles/dialogflow.aamViewer`) A user can view the taxonomy and data reports in an AAM project.  |  `dialogflow.agents.export` `dialogflow.agents.get` `dialogflow.agents.list` `dialogflow.agents.search` `dialogflow.agents.searchResources` `dialogflow.answerrecords.get` `dialogflow.answerrecords.list` `dialogflow.callMatchers.list` `dialogflow.changelogs.*`

  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`

`dialogflow.companionAgents.get` `dialogflow.companionAgents.list` `dialogflow.contexts.get` `dialogflow.contexts.list` `dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.get` `dialogflow.conversations.list` `dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.encryptionspec.get` `dialogflow.entityTypes.get` `dialogflow.entityTypes.list` `dialogflow.environments.get` `dialogflow.environments.list` `dialogflow.examples.get` `dialogflow.examples.list` `dialogflow.experiments.get` `dialogflow.experiments.list` `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.fulfillments.get` `dialogflow.generators.get` `dialogflow.generators.list` `dialogflow.integrations.get` `dialogflow.integrations.list` `dialogflow.intents.get` `dialogflow.intents.list` `dialogflow.interactionMonitoringAlerts.get` `dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.modelEvaluations.*`

  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`

`dialogflow.operations.get` `dialogflow.pages.get` `dialogflow.pages.list` `dialogflow.participants.get` `dialogflow.participants.list` `dialogflow.phoneNumberOrders.get` `dialogflow.phoneNumberOrders.list` `dialogflow.phoneNumbers.list` `dialogflow.playbooks.get` `dialogflow.playbooks.list` `dialogflow.securitySettings.get` `dialogflow.securitySettings.list` `dialogflow.sessionEntityTypes.get` `dialogflow.sessionEntityTypes.list` `dialogflow.smartMessagingEntries.get` `dialogflow.smartMessagingEntries.list` `dialogflow.testcases.get` `dialogflow.testcases.list` `dialogflow.tools.get` `dialogflow.tools.list` `dialogflow.transitionRouteGroups.get` `dialogflow.transitionRouteGroups.list` `dialogflow.versions.get` `dialogflow.versions.list` `dialogflow.webhooks.get` `dialogflow.webhooks.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dialogflow Agent Assist Client 

(`roles/dialogflow.agentAssistClient`) Can create and handle live conversations using Agent Assist features.  |  `dialogflow.answerrecords.*`

  * `dialogflow.answerrecords.delete`
  * `dialogflow.answerrecords.get`
  * `dialogflow.answerrecords.list`
  * `dialogflow.answerrecords.update`

`dialogflow.companionAgents.*`

  * `dialogflow.companionAgents.create`
  * `dialogflow.companionAgents.delete`
  * `dialogflow.companionAgents.get`
  * `dialogflow.companionAgents.list`
  * `dialogflow.companionAgents.update`

`dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.*`

  * `dialogflow.conversations.addPhoneNumber`
  * `dialogflow.conversations.complete`
  * `dialogflow.conversations.create`
  * `dialogflow.conversations.get`
  * `dialogflow.conversations.list`
  * `dialogflow.conversations.update`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.generators.get` `dialogflow.interactionMonitoringAlerts.*`

  * `dialogflow.interactionMonitoringAlerts.ack`
  * `dialogflow.interactionMonitoringAlerts.get`

`dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.participants.*`

  * `dialogflow.participants.analyzeContent`
  * `dialogflow.participants.create`
  * `dialogflow.participants.get`
  * `dialogflow.participants.list`
  * `dialogflow.participants.suggest`
  * `dialogflow.participants.update`

`dialogflow.sessions.detectIntent`  
  
#### Dialogflow API Client 

(`roles/dialogflow.client`) Grant to Dialogflow API clients that perform Dialogflow-specific edits and detect intent calls using the API. Also see [Dialogflow access control](https://docs.cloud.google.com/dialogflow/docs/access-control).  Lowest-level resources where you can grant this role:

  * Project 

|  `dialogflow.contexts.*`

  * `dialogflow.contexts.create`
  * `dialogflow.contexts.delete`
  * `dialogflow.contexts.get`
  * `dialogflow.contexts.list`
  * `dialogflow.contexts.update`

`dialogflow.conversations.*`

  * `dialogflow.conversations.addPhoneNumber`
  * `dialogflow.conversations.complete`
  * `dialogflow.conversations.create`
  * `dialogflow.conversations.get`
  * `dialogflow.conversations.list`
  * `dialogflow.conversations.update`

`dialogflow.environments.runContinuousTest` `dialogflow.messages.list` `dialogflow.participants.*`

  * `dialogflow.participants.analyzeContent`
  * `dialogflow.participants.create`
  * `dialogflow.participants.get`
  * `dialogflow.participants.list`
  * `dialogflow.participants.suggest`
  * `dialogflow.participants.update`

`dialogflow.sessionEntityTypes.*`

  * `dialogflow.sessionEntityTypes.create`
  * `dialogflow.sessionEntityTypes.delete`
  * `dialogflow.sessionEntityTypes.get`
  * `dialogflow.sessionEntityTypes.list`
  * `dialogflow.sessionEntityTypes.update`

`dialogflow.sessions.*`

  * `dialogflow.sessions.detectIntent`
  * `dialogflow.sessions.streamingDetectIntent`

  
  
#### Dialogflow Console Agent Editor 

(`roles/dialogflow.consoleAgentEditor`) Grant to Dialogflow Console editors that edit existing agents. Also see [Dialogflow access control](https://docs.cloud.google.com/dialogflow/docs/access-control).  **Caution:** Users with permissions to create or modify Dialogflow agent components, such as tools and webhooks, can configure these components to authenticate as the Dialogflow Service Agent using ID tokens. This capability can be used to interact with other Google Cloud services that accept ID token authentication using the permissions granted to the [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent). Carefully control who is granted permissions to configure these Dialogflow agent components.  Lowest-level resources where you can grant this role:

  * Project 

|  `actions.agentVersions.create` `dialogflow.*`

  * `dialogflow.agents.create`
  * `dialogflow.agents.delete`
  * `dialogflow.agents.export`
  * `dialogflow.agents.get`
  * `dialogflow.agents.import`
  * `dialogflow.agents.list`
  * `dialogflow.agents.restore`
  * `dialogflow.agents.search`
  * `dialogflow.agents.searchResources`
  * `dialogflow.agents.train`
  * `dialogflow.agents.update`
  * `dialogflow.agents.validate`
  * `dialogflow.answerrecords.delete`
  * `dialogflow.answerrecords.get`
  * `dialogflow.answerrecords.list`
  * `dialogflow.answerrecords.update`
  * `dialogflow.callMatchers.create`
  * `dialogflow.callMatchers.delete`
  * `dialogflow.callMatchers.list`
  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`
  * `dialogflow.companionAgents.create`
  * `dialogflow.companionAgents.delete`
  * `dialogflow.companionAgents.get`
  * `dialogflow.companionAgents.list`
  * `dialogflow.companionAgents.update`
  * `dialogflow.contexts.create`
  * `dialogflow.contexts.delete`
  * `dialogflow.contexts.get`
  * `dialogflow.contexts.list`
  * `dialogflow.contexts.update`
  * `dialogflow.conversationDatasets.create`
  * `dialogflow.conversationDatasets.delete`
  * `dialogflow.conversationDatasets.get`
  * `dialogflow.conversationDatasets.import`
  * `dialogflow.conversationDatasets.list`
  * `dialogflow.conversationModels.create`
  * `dialogflow.conversationModels.delete`
  * `dialogflow.conversationModels.deploy`
  * `dialogflow.conversationModels.get`
  * `dialogflow.conversationModels.list`
  * `dialogflow.conversationModels.undeploy`
  * `dialogflow.conversationProfiles.create`
  * `dialogflow.conversationProfiles.delete`
  * `dialogflow.conversationProfiles.get`
  * `dialogflow.conversationProfiles.list`
  * `dialogflow.conversationProfiles.update`
  * `dialogflow.conversations.addPhoneNumber`
  * `dialogflow.conversations.complete`
  * `dialogflow.conversations.create`
  * `dialogflow.conversations.get`
  * `dialogflow.conversations.list`
  * `dialogflow.conversations.update`
  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`
  * `dialogflow.documents.create`
  * `dialogflow.documents.delete`
  * `dialogflow.documents.get`
  * `dialogflow.documents.list`
  * `dialogflow.encryptionspec.get`
  * `dialogflow.encryptionspec.update`
  * `dialogflow.entityTypes.create`
  * `dialogflow.entityTypes.createEntity`
  * `dialogflow.entityTypes.delete`
  * `dialogflow.entityTypes.deleteEntity`
  * `dialogflow.entityTypes.get`
  * `dialogflow.entityTypes.list`
  * `dialogflow.entityTypes.update`
  * `dialogflow.entityTypes.updateEntity`
  * `dialogflow.environments.create`
  * `dialogflow.environments.delete`
  * `dialogflow.environments.get`
  * `dialogflow.environments.getHistory`
  * `dialogflow.environments.list`
  * `dialogflow.environments.lookupHistory`
  * `dialogflow.environments.runContinuousTest`
  * `dialogflow.environments.update`
  * `dialogflow.examples.create`
  * `dialogflow.examples.delete`
  * `dialogflow.examples.get`
  * `dialogflow.examples.list`
  * `dialogflow.examples.update`
  * `dialogflow.experiments.create`
  * `dialogflow.experiments.delete`
  * `dialogflow.experiments.get`
  * `dialogflow.experiments.list`
  * `dialogflow.experiments.update`
  * `dialogflow.flows.create`
  * `dialogflow.flows.delete`
  * `dialogflow.flows.get`
  * `dialogflow.flows.list`
  * `dialogflow.flows.train`
  * `dialogflow.flows.update`
  * `dialogflow.flows.validate`
  * `dialogflow.fulfillments.get`
  * `dialogflow.fulfillments.update`
  * `dialogflow.generators.create`
  * `dialogflow.generators.delete`
  * `dialogflow.generators.get`
  * `dialogflow.generators.list`
  * `dialogflow.generators.update`
  * `dialogflow.integrations.create`
  * `dialogflow.integrations.delete`
  * `dialogflow.integrations.get`
  * `dialogflow.integrations.list`
  * `dialogflow.integrations.update`
  * `dialogflow.intents.create`
  * `dialogflow.intents.delete`
  * `dialogflow.intents.get`
  * `dialogflow.intents.list`
  * `dialogflow.intents.update`
  * `dialogflow.interactionMonitoringAlerts.ack`
  * `dialogflow.interactionMonitoringAlerts.get`
  * `dialogflow.knowledgeBases.create`
  * `dialogflow.knowledgeBases.delete`
  * `dialogflow.knowledgeBases.get`
  * `dialogflow.knowledgeBases.list`
  * `dialogflow.knowledgeBases.update`
  * `dialogflow.messages.list`
  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`
  * `dialogflow.operations.get`
  * `dialogflow.pages.create`
  * `dialogflow.pages.delete`
  * `dialogflow.pages.get`
  * `dialogflow.pages.list`
  * `dialogflow.pages.update`
  * `dialogflow.participants.analyzeContent`
  * `dialogflow.participants.create`
  * `dialogflow.participants.get`
  * `dialogflow.participants.list`
  * `dialogflow.participants.suggest`
  * `dialogflow.participants.update`
  * `dialogflow.phoneNumberOrders.cancel`
  * `dialogflow.phoneNumberOrders.create`
  * `dialogflow.phoneNumberOrders.get`
  * `dialogflow.phoneNumberOrders.list`
  * `dialogflow.phoneNumberOrders.update`
  * `dialogflow.phoneNumbers.delete`
  * `dialogflow.phoneNumbers.list`
  * `dialogflow.phoneNumbers.undelete`
  * `dialogflow.phoneNumbers.update`
  * `dialogflow.playbooks.create`
  * `dialogflow.playbooks.delete`
  * `dialogflow.playbooks.get`
  * `dialogflow.playbooks.list`
  * `dialogflow.playbooks.update`
  * `dialogflow.securitySettings.create`
  * `dialogflow.securitySettings.delete`
  * `dialogflow.securitySettings.get`
  * `dialogflow.securitySettings.list`
  * `dialogflow.securitySettings.update`
  * `dialogflow.sessionEntityTypes.create`
  * `dialogflow.sessionEntityTypes.delete`
  * `dialogflow.sessionEntityTypes.get`
  * `dialogflow.sessionEntityTypes.list`
  * `dialogflow.sessionEntityTypes.update`
  * `dialogflow.sessions.detectIntent`
  * `dialogflow.sessions.streamingDetectIntent`
  * `dialogflow.smartMessagingEntries.create`
  * `dialogflow.smartMessagingEntries.delete`
  * `dialogflow.smartMessagingEntries.get`
  * `dialogflow.smartMessagingEntries.list`
  * `dialogflow.testcases.calculateCoverage`
  * `dialogflow.testcases.create`
  * `dialogflow.testcases.delete`
  * `dialogflow.testcases.export`
  * `dialogflow.testcases.get`
  * `dialogflow.testcases.import`
  * `dialogflow.testcases.list`
  * `dialogflow.testcases.run`
  * `dialogflow.testcases.update`
  * `dialogflow.tools.create`
  * `dialogflow.tools.delete`
  * `dialogflow.tools.get`
  * `dialogflow.tools.list`
  * `dialogflow.tools.update`
  * `dialogflow.transitionRouteGroups.create`
  * `dialogflow.transitionRouteGroups.delete`
  * `dialogflow.transitionRouteGroups.get`
  * `dialogflow.transitionRouteGroups.list`
  * `dialogflow.transitionRouteGroups.update`
  * `dialogflow.versions.create`
  * `dialogflow.versions.delete`
  * `dialogflow.versions.get`
  * `dialogflow.versions.list`
  * `dialogflow.versions.load`
  * `dialogflow.versions.update`
  * `dialogflow.webhooks.create`
  * `dialogflow.webhooks.delete`
  * `dialogflow.webhooks.get`
  * `dialogflow.webhooks.list`
  * `dialogflow.webhooks.update`

`resourcemanager.projects.get`  
  
#### Dialogflow Console Simulator User 

(`roles/dialogflow.consoleSimulatorUser`) Can perform query of dialogflow suggestions in the simulator in web console.  |  `dialogflow.companionAgents.*`

  * `dialogflow.companionAgents.create`
  * `dialogflow.companionAgents.delete`
  * `dialogflow.companionAgents.get`
  * `dialogflow.companionAgents.list`
  * `dialogflow.companionAgents.update`

`dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.*`

  * `dialogflow.conversations.addPhoneNumber`
  * `dialogflow.conversations.complete`
  * `dialogflow.conversations.create`
  * `dialogflow.conversations.get`
  * `dialogflow.conversations.list`
  * `dialogflow.conversations.update`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.interactionMonitoringAlerts.*`

  * `dialogflow.interactionMonitoringAlerts.ack`
  * `dialogflow.interactionMonitoringAlerts.get`

`dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.participants.*`

  * `dialogflow.participants.analyzeContent`
  * `dialogflow.participants.create`
  * `dialogflow.participants.get`
  * `dialogflow.participants.list`
  * `dialogflow.participants.suggest`
  * `dialogflow.participants.update`

`dialogflow.sessions.detectIntent` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dialogflow Console Smart Messaging Allowlist Editor 

(`roles/dialogflow.consoleSmartMessagingAllowlistEditor`) Can edit allowlist for smart messaging associated with conversation model in the agent assist console  |  `dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.list` `dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.operations.get` `dialogflow.smartMessagingEntries.*`

  * `dialogflow.smartMessagingEntries.create`
  * `dialogflow.smartMessagingEntries.delete`
  * `dialogflow.smartMessagingEntries.get`
  * `dialogflow.smartMessagingEntries.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dialogflow Conversation Manager 

(`roles/dialogflow.conversationManager`) Can manage all the resources related to Dialogflow Conversations.  |  `dialogflow.conversationProfiles.*`

  * `dialogflow.conversationProfiles.create`
  * `dialogflow.conversationProfiles.delete`
  * `dialogflow.conversationProfiles.get`
  * `dialogflow.conversationProfiles.list`
  * `dialogflow.conversationProfiles.update`

`dialogflow.conversations.*`

  * `dialogflow.conversations.addPhoneNumber`
  * `dialogflow.conversations.complete`
  * `dialogflow.conversations.create`
  * `dialogflow.conversations.get`
  * `dialogflow.conversations.list`
  * `dialogflow.conversations.update`

`dialogflow.participants.*`

  * `dialogflow.participants.analyzeContent`
  * `dialogflow.participants.create`
  * `dialogflow.participants.get`
  * `dialogflow.participants.list`
  * `dialogflow.participants.suggest`
  * `dialogflow.participants.update`

  
  
#### Dialogflow Entity Type Admin 

(`roles/dialogflow.entityTypeAdmin`) Can read & write entity types.  |  `dialogflow.entityTypes.*`

  * `dialogflow.entityTypes.create`
  * `dialogflow.entityTypes.createEntity`
  * `dialogflow.entityTypes.delete`
  * `dialogflow.entityTypes.deleteEntity`
  * `dialogflow.entityTypes.get`
  * `dialogflow.entityTypes.list`
  * `dialogflow.entityTypes.update`
  * `dialogflow.entityTypes.updateEntity`

  
  
#### Dialogflow Environment editor 

(`roles/dialogflow.environmentEditor`) Can read & update environment and its sub-resources.  |  `dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.environments.get` `dialogflow.environments.getHistory` `dialogflow.environments.list` `dialogflow.environments.lookupHistory` `dialogflow.environments.runContinuousTest` `dialogflow.environments.update` `dialogflow.experiments.*`

  * `dialogflow.experiments.create`
  * `dialogflow.experiments.delete`
  * `dialogflow.experiments.get`
  * `dialogflow.experiments.list`
  * `dialogflow.experiments.update`

  
  
#### Dialogflow Flow editor 

(`roles/dialogflow.flowEditor`) Can read & update flow and its sub-resources.  |  `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.flows.train` `dialogflow.flows.update` `dialogflow.flows.validate` `dialogflow.pages.*`

  * `dialogflow.pages.create`
  * `dialogflow.pages.delete`
  * `dialogflow.pages.get`
  * `dialogflow.pages.list`
  * `dialogflow.pages.update`

`dialogflow.transitionRouteGroups.*`

  * `dialogflow.transitionRouteGroups.create`
  * `dialogflow.transitionRouteGroups.delete`
  * `dialogflow.transitionRouteGroups.get`
  * `dialogflow.transitionRouteGroups.list`
  * `dialogflow.transitionRouteGroups.update`

`dialogflow.versions.*`

  * `dialogflow.versions.create`
  * `dialogflow.versions.delete`
  * `dialogflow.versions.get`
  * `dialogflow.versions.list`
  * `dialogflow.versions.load`
  * `dialogflow.versions.update`

  
  
#### Dialogflow Integration Manager 

(`roles/dialogflow.integrationManager`) Can add, remove, enable and disable Dialogflow integrations.  |  `dialogflow.integrations.*`

  * `dialogflow.integrations.create`
  * `dialogflow.integrations.delete`
  * `dialogflow.integrations.get`
  * `dialogflow.integrations.list`
  * `dialogflow.integrations.update`

  
  
#### Dialogflow Intent Admin 

(`roles/dialogflow.intentAdmin`) Can read & write intents.  |  `dialogflow.intents.*`

  * `dialogflow.intents.create`
  * `dialogflow.intents.delete`
  * `dialogflow.intents.get`
  * `dialogflow.intents.list`
  * `dialogflow.intents.update`

  
  
#### Dialogflow API Reader 

(`roles/dialogflow.reader`) Grant to Dialogflow API clients that perform Dialogflow-specific read-only calls using the API. Also see [Dialogflow access control](https://docs.cloud.google.com/dialogflow/docs/access-control).  Lowest-level resources where you can grant this role:

  * Project 

|  `dialogflow.agents.export` `dialogflow.agents.get` `dialogflow.agents.list` `dialogflow.agents.search` `dialogflow.agents.searchResources` `dialogflow.answerrecords.get` `dialogflow.answerrecords.list` `dialogflow.callMatchers.list` `dialogflow.changelogs.*`

  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`

`dialogflow.companionAgents.get` `dialogflow.companionAgents.list` `dialogflow.contexts.get` `dialogflow.contexts.list` `dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.get` `dialogflow.conversationProfiles.list` `dialogflow.conversations.get` `dialogflow.conversations.list` `dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.encryptionspec.get` `dialogflow.entityTypes.get` `dialogflow.entityTypes.list` `dialogflow.environments.get` `dialogflow.environments.list` `dialogflow.examples.get` `dialogflow.examples.list` `dialogflow.experiments.get` `dialogflow.experiments.list` `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.fulfillments.get` `dialogflow.generators.get` `dialogflow.generators.list` `dialogflow.integrations.get` `dialogflow.integrations.list` `dialogflow.intents.get` `dialogflow.intents.list` `dialogflow.interactionMonitoringAlerts.get` `dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.modelEvaluations.*`

  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`

`dialogflow.operations.get` `dialogflow.pages.get` `dialogflow.pages.list` `dialogflow.participants.get` `dialogflow.participants.list` `dialogflow.phoneNumberOrders.get` `dialogflow.phoneNumberOrders.list` `dialogflow.phoneNumbers.list` `dialogflow.playbooks.get` `dialogflow.playbooks.list` `dialogflow.securitySettings.get` `dialogflow.securitySettings.list` `dialogflow.sessionEntityTypes.get` `dialogflow.sessionEntityTypes.list` `dialogflow.smartMessagingEntries.get` `dialogflow.smartMessagingEntries.list` `dialogflow.testcases.get` `dialogflow.testcases.list` `dialogflow.tools.get` `dialogflow.tools.list` `dialogflow.transitionRouteGroups.get` `dialogflow.transitionRouteGroups.list` `dialogflow.versions.get` `dialogflow.versions.list` `dialogflow.webhooks.get` `dialogflow.webhooks.list` `resourcemanager.projects.get`  
  
#### Dialogflow Test Case Admin 

(`roles/dialogflow.testCaseAdmin`) Can read & write test cases.  |  `dialogflow.testcases.*`

  * `dialogflow.testcases.calculateCoverage`
  * `dialogflow.testcases.create`
  * `dialogflow.testcases.delete`
  * `dialogflow.testcases.export`
  * `dialogflow.testcases.get`
  * `dialogflow.testcases.import`
  * `dialogflow.testcases.list`
  * `dialogflow.testcases.run`
  * `dialogflow.testcases.update`

  
  
#### Dialogflow Webhook Admin 

(`roles/dialogflow.webhookAdmin`) Can read & write webhooks.  **Caution:** Users with permissions to create or modify Dialogflow agent components, such as tools and webhooks, can configure these components to authenticate as the Dialogflow Service Agent using ID tokens. This capability can be used to interact with other Google Cloud services that accept ID token authentication using the permissions granted to the [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#dialogflow-service-agent). Carefully control who is granted permissions to configure these Dialogflow agent components.  |  `dialogflow.webhooks.*`

  * `dialogflow.webhooks.create`
  * `dialogflow.webhooks.delete`
  * `dialogflow.webhooks.get`
  * `dialogflow.webhooks.list`
  * `dialogflow.webhooks.update`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Dialogflow Service Agent 

(`roles/dialogflow.serviceAgent`) Gives Dialogflow Service Account access to resources on behalf of user project for Integrations (Facebook Messenger, Slack, Telephony, etc.), BigQuery, Discovery Engine, Integration Connectors, Application Integration, and Vertex.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.endpoints.get` `aiplatform.endpoints.predict` `aiplatform.extensions.execute` `aiplatform.extensions.get` `aiplatform.models.get` `bigquery.datasets.create` `bigquery.jobs.create` `bigquery.tables.create` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.updateData` `ces.apps.get` `ces.sessions.*`

  * `ces.sessions.bidiRunSession`
  * `ces.sessions.runSession`

`ces.tools.execute` `ces.tools.get` `ces.toolsets.get` `cloudfunctions.functions.invoke` `connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.executeSqlQuery` `connectors.connections.generateOpenAPISpec` `connectors.connections.get` `connectors.entities.*`

  * `connectors.entities.create`
  * `connectors.entities.delete`
  * `connectors.entities.deleteEntitiesWithConditions`
  * `connectors.entities.get`
  * `connectors.entities.list`
  * `connectors.entities.update`
  * `connectors.entities.updateEntitiesWithConditions`

`connectors.entityTypes.list` `connectors.operations.get` `connectors.versions.get` `dialogflow.agents.export` `dialogflow.agents.get` `dialogflow.agents.list` `dialogflow.agents.search` `dialogflow.agents.searchResources` `dialogflow.answerrecords.get` `dialogflow.answerrecords.list` `dialogflow.callMatchers.list` `dialogflow.changelogs.*`

  * `dialogflow.changelogs.get`
  * `dialogflow.changelogs.list`

`dialogflow.companionAgents.get` `dialogflow.companionAgents.list` `dialogflow.contexts.*`

  * `dialogflow.contexts.create`
  * `dialogflow.contexts.delete`
  * `dialogflow.contexts.get`
  * `dialogflow.contexts.list`
  * `dialogflow.contexts.update`

`dialogflow.conversationDatasets.get` `dialogflow.conversationDatasets.list` `dialogflow.conversationModels.get` `dialogflow.conversationModels.list` `dialogflow.conversationProfiles.*`

  * `dialogflow.conversationProfiles.create`
  * `dialogflow.conversationProfiles.delete`
  * `dialogflow.conversationProfiles.get`
  * `dialogflow.conversationProfiles.list`
  * `dialogflow.conversationProfiles.update`

`dialogflow.conversations.*`

  * `dialogflow.conversations.addPhoneNumber`
  * `dialogflow.conversations.complete`
  * `dialogflow.conversations.create`
  * `dialogflow.conversations.get`
  * `dialogflow.conversations.list`
  * `dialogflow.conversations.update`

`dialogflow.deployments.*`

  * `dialogflow.deployments.get`
  * `dialogflow.deployments.list`

`dialogflow.documents.get` `dialogflow.documents.list` `dialogflow.encryptionspec.get` `dialogflow.entityTypes.get` `dialogflow.entityTypes.list` `dialogflow.environments.get` `dialogflow.environments.list` `dialogflow.environments.runContinuousTest` `dialogflow.examples.get` `dialogflow.examples.list` `dialogflow.experiments.get` `dialogflow.experiments.list` `dialogflow.flows.get` `dialogflow.flows.list` `dialogflow.fulfillments.get` `dialogflow.generators.get` `dialogflow.generators.list` `dialogflow.integrations.get` `dialogflow.integrations.list` `dialogflow.intents.get` `dialogflow.intents.list` `dialogflow.interactionMonitoringAlerts.get` `dialogflow.knowledgeBases.get` `dialogflow.knowledgeBases.list` `dialogflow.messages.list` `dialogflow.modelEvaluations.*`

  * `dialogflow.modelEvaluations.get`
  * `dialogflow.modelEvaluations.list`

`dialogflow.operations.get` `dialogflow.pages.get` `dialogflow.pages.list` `dialogflow.participants.*`

  * `dialogflow.participants.analyzeContent`
  * `dialogflow.participants.create`
  * `dialogflow.participants.get`
  * `dialogflow.participants.list`
  * `dialogflow.participants.suggest`
  * `dialogflow.participants.update`

`dialogflow.phoneNumberOrders.get` `dialogflow.phoneNumberOrders.list` `dialogflow.phoneNumbers.list` `dialogflow.playbooks.get` `dialogflow.playbooks.list` `dialogflow.securitySettings.get` `dialogflow.securitySettings.list` `dialogflow.sessionEntityTypes.*`

  * `dialogflow.sessionEntityTypes.create`
  * `dialogflow.sessionEntityTypes.delete`
  * `dialogflow.sessionEntityTypes.get`
  * `dialogflow.sessionEntityTypes.list`
  * `dialogflow.sessionEntityTypes.update`

`dialogflow.sessions.*`

  * `dialogflow.sessions.detectIntent`
  * `dialogflow.sessions.streamingDetectIntent`

`dialogflow.smartMessagingEntries.get` `dialogflow.smartMessagingEntries.list` `dialogflow.testcases.get` `dialogflow.testcases.list` `dialogflow.tools.get` `dialogflow.tools.list` `dialogflow.transitionRouteGroups.get` `dialogflow.transitionRouteGroups.list` `dialogflow.versions.get` `dialogflow.versions.list` `dialogflow.webhooks.get` `dialogflow.webhooks.list` `discoveryengine.collections.get` `discoveryengine.collections.list` `discoveryengine.dataStores.create` `discoveryengine.dataStores.get` `discoveryengine.dataStores.list` `discoveryengine.documents.create` `discoveryengine.documents.get` `discoveryengine.documents.import` `discoveryengine.documents.list` `discoveryengine.documents.update` `discoveryengine.engines.create` `discoveryengine.engines.delete` `discoveryengine.engines.get` `discoveryengine.engines.update` `discoveryengine.schemas.get` `discoveryengine.schemas.list` `discoveryengine.servingConfigs.search` `dlp.deidentifyTemplates.get` `dlp.deidentifyTemplates.list` `dlp.inspectTemplates.get` `dlp.inspectTemplates.list` `integrations.integrationVersions.get` `integrations.integrations.generateOpenApiSpec` `logging.logEntries.create` `logging.logEntries.route` `pubsub.snapshots.seek` `pubsub.subscriptions.consume` `pubsub.topics.attachSubscription` `pubsub.topics.publish` `resourcemanager.projects.get` `resourcemanager.projects.list` `run.jobs.run` `run.routes.invoke` `serviceusage.services.use` `speakerid.phrases.*`

  * `speakerid.phrases.create`
  * `speakerid.phrases.delete`
  * `speakerid.phrases.get`
  * `speakerid.phrases.list`

`speakerid.speakers.*`

  * `speakerid.speakers.create`
  * `speakerid.speakers.delete`
  * `speakerid.speakers.get`
  * `speakerid.speakers.list`
  * `speakerid.speakers.verify`

`speech.adaptations.execute` `speech.customClasses.get` `speech.customClasses.list` `speech.phraseSets.get` `speech.phraseSets.list` `speech.recognizers.get` `speech.recognizers.list` `storage.folders.get` `storage.folders.list` `storage.managedFolders.get` `storage.managedFolders.list` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list`  
  
## Dialogflow permissions

Permission | Included in roles  
---|---  
  
#### `dialogflow.agents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.agents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.agents.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.agents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.agents.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.agents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.agents.restore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.agents.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.agents.searchResources`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.agents.train`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.agents.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.agents.validate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.answerrecords.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.answerrecords.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.answerrecords.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.answerrecords.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.callMatchers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.callMatchers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.callMatchers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.changelogs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.changelogs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.companionAgents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)   
  
#### `dialogflow.companionAgents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)   
  
#### `dialogflow.companionAgents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.companionAgents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.companionAgents.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)   
  
#### `dialogflow.contexts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.contexts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.contexts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.contexts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.contexts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationDatasets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.conversationDatasets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.conversationDatasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationDatasets.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.conversationDatasets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationModels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.conversationModels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.conversationModels.deploy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.conversationModels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationModels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationModels.undeploy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.conversationProfiles.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationProfiles.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationProfiles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationProfiles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversationProfiles.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversations.addPhoneNumber`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversations.complete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.conversations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.deployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.deployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.documents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.documents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 

  
  
#### `dialogflow.documents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.documents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.encryptionspec.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.encryptionspec.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.entityTypes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Entity Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.entityTypeAdmin) (`roles/dialogflow.entityTypeAdmin`)   
  
#### `dialogflow.entityTypes.createEntity`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Entity Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.entityTypeAdmin) (`roles/dialogflow.entityTypeAdmin`)   
  
#### `dialogflow.entityTypes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Entity Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.entityTypeAdmin) (`roles/dialogflow.entityTypeAdmin`)   
  
#### `dialogflow.entityTypes.deleteEntity`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Entity Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.entityTypeAdmin) (`roles/dialogflow.entityTypeAdmin`)   
  
#### `dialogflow.entityTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Entity Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.entityTypeAdmin) (`roles/dialogflow.entityTypeAdmin`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.entityTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Entity Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.entityTypeAdmin) (`roles/dialogflow.entityTypeAdmin`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.entityTypes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Entity Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.entityTypeAdmin) (`roles/dialogflow.entityTypeAdmin`)   
  
#### `dialogflow.entityTypes.updateEntity`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Entity Type Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.entityTypeAdmin) (`roles/dialogflow.entityTypeAdmin`)   
  
#### `dialogflow.environments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.environments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.environments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.environments.getHistory`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dialogflow.environments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.environments.lookupHistory`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dialogflow.environments.runContinuousTest`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.environments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)   
  
#### `dialogflow.examples.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.examples.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.examples.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.examples.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.examples.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.experiments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)   
  
#### `dialogflow.experiments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)   
  
#### `dialogflow.experiments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.experiments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.experiments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Environment editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.environmentEditor) (`roles/dialogflow.environmentEditor`)   
  
#### `dialogflow.flows.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.flows.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.flows.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.flows.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.flows.train`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.flows.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.flows.validate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.fulfillments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.fulfillments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.generators.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.generators.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.generators.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.generators.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.generators.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.integrations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Integration Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.integrationManager) (`roles/dialogflow.integrationManager`)   
  
#### `dialogflow.integrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Integration Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.integrationManager) (`roles/dialogflow.integrationManager`)   
  
#### `dialogflow.integrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Integration Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.integrationManager) (`roles/dialogflow.integrationManager`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.integrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Integration Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.integrationManager) (`roles/dialogflow.integrationManager`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.integrations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Integration Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.integrationManager) (`roles/dialogflow.integrationManager`)   
  
#### `dialogflow.intents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Intent Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.intentAdmin) (`roles/dialogflow.intentAdmin`)   
  
#### `dialogflow.intents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Intent Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.intentAdmin) (`roles/dialogflow.intentAdmin`)   
  
#### `dialogflow.intents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Intent Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.intentAdmin) (`roles/dialogflow.intentAdmin`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.intents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Intent Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.intentAdmin) (`roles/dialogflow.intentAdmin`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.intents.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Intent Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.intentAdmin) (`roles/dialogflow.intentAdmin`)   
  
#### `dialogflow.interactionMonitoringAlerts.ack`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)   
  
#### `dialogflow.interactionMonitoringAlerts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.knowledgeBases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.knowledgeBases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.knowledgeBases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.knowledgeBases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.knowledgeBases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.messages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.modelEvaluations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.modelEvaluations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.pages.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.pages.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.pages.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.pages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.pages.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.participants.analyzeContent`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.participants.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.participants.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.participants.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.participants.suggest`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.participants.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  [Dialogflow Conversation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.conversationManager) (`roles/dialogflow.conversationManager`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.phoneNumberOrders.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.phoneNumberOrders.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.phoneNumberOrders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.phoneNumberOrders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.phoneNumberOrders.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.phoneNumbers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.phoneNumbers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.phoneNumbers.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.phoneNumbers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.playbooks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.playbooks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.playbooks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.playbooks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.playbooks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.securitySettings.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.securitySettings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.securitySettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.securitySettings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.securitySettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.sessionEntityTypes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.sessionEntityTypes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.sessionEntityTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.sessionEntityTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.sessionEntityTypes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.sessions.detectIntent`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Agent Assist Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.agentAssistClient) (`roles/dialogflow.agentAssistClient`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Simulator User](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSimulatorUser) (`roles/dialogflow.consoleSimulatorUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Contact Center AI Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.serviceAgent) (`roles/contactcenterinsights.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `dialogflow.sessions.streamingDetectIntent`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow API Client](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.client) (`roles/dialogflow.client`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.smartMessagingEntries.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)   
  
#### `dialogflow.smartMessagingEntries.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)   
  
#### `dialogflow.smartMessagingEntries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.smartMessagingEntries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Console Smart Messaging Allowlist Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleSmartMessagingAllowlistEditor) (`roles/dialogflow.consoleSmartMessagingAllowlistEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.testcases.calculateCoverage`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dialogflow.testcases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)   
  
#### `dialogflow.testcases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)   
  
#### `dialogflow.testcases.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dialogflow.testcases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.testcases.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)   
  
#### `dialogflow.testcases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.testcases.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)   
  
#### `dialogflow.testcases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Test Case Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.testCaseAdmin) (`roles/dialogflow.testCaseAdmin`)   
  
#### `dialogflow.tools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.tools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.tools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.tools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.tools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)   
  
#### `dialogflow.transitionRouteGroups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.transitionRouteGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.transitionRouteGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.transitionRouteGroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.transitionRouteGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.versions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.versions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.versions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.versions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.versions.load`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.versions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Flow editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.flowEditor) (`roles/dialogflow.flowEditor`)   
  
#### `dialogflow.webhooks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Webhook Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.webhookAdmin) (`roles/dialogflow.webhookAdmin`)   
  
#### `dialogflow.webhooks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Webhook Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.webhookAdmin) (`roles/dialogflow.webhookAdmin`)   
  
#### `dialogflow.webhooks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Dialogflow Webhook Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.webhookAdmin) (`roles/dialogflow.webhookAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.webhooks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.viewer) (`roles/dialogflow.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [CX Premium Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamAdmin) (`roles/dialogflow.aamAdmin`)  [CX Premium Conversational Architect](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamConversationalArchitect) (`roles/dialogflow.aamConversationalArchitect`)  [CX Premium Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamDialogDesigner) (`roles/dialogflow.aamDialogDesigner`)  [CX Premium Lead Dialog Designer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamLeadDialogDesigner) (`roles/dialogflow.aamLeadDialogDesigner`)  [CX Premium Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.aamViewer) (`roles/dialogflow.aamViewer`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.reader) (`roles/dialogflow.reader`)  [Dialogflow Webhook Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.webhookAdmin) (`roles/dialogflow.webhookAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `dialogflow.webhooks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dialogflow API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.admin) (`roles/dialogflow.admin`)  [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)  [Dialogflow Webhook Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.webhookAdmin) (`roles/dialogflow.webhookAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
