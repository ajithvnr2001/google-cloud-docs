---
url: https://docs.cloud.google.com/eventarc/advanced/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:24.753830+00:00
---

# Access control with IAM  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

Identity and Access Management (IAM) lets you control access to Eventarc resources by granting specific roles and permissions to principals. You can assign predefined or custom roles to ensure that principals have only the permissions necessary to manage resources and route events.

## Overview

Eventarc uses IAM for access control.

  * For an introduction to IAM and its features, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

  * To learn how to grant and revoke access using allow policies, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



  * To control publishing access in Eventarc Advanced using access policies, see [Control publishing access](https://docs.cloud.google.com/eventarc/advanced/docs/control-publishing-access).



For lists of the permissions and roles that Eventarc supports, see the following sections.

## Eventarc service agent

Some Google Cloud services have [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) that allow the service to access your resources if granted the appropriate permissions. If an API requires a service agent, then Google Cloud creates the service agent at some point after you activate and use the API.

Eventarc uses a provisioning model that creates its service agent only when first needed—for example, when you create an Eventarc resource for the first time—and not when the API is initially enabled. Provisioning the service agent and propagating the changes through the system can take several minutes. For more information about this delay, see [Permission denied while using Eventarc service agent](https://docs.cloud.google.com/eventarc/advanced/docs/troubleshoot#sa-errors). 

## Enable the Eventarc APIs

To view and assign IAM roles for Eventarc, you must enable the Eventarc APIs for your project. You won't be able to see the Eventarc roles in the Google Cloud console until you enable the APIs.

### Console

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Eventarc and Eventarc Publishing APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Eventarc and Eventarc Publishing APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=eventarc.googleapis.com,eventarcpublishing.googleapis.com)




###  gcloud 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Eventarc and Eventarc Publishing APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable eventarc.googleapis.com eventarcpublishing.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Eventarc and Eventarc Publishing APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable eventarc.googleapis.com eventarcpublishing.googleapis.com




## Predefined roles

The following table lists the Eventarc predefined IAM roles with a corresponding list of all the permissions each role includes.

The predefined roles address most typical use cases. If your use case isn't covered by the predefined roles, you can [create an IAM custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).

### Eventarc roles

Role | Permissions  
---|---  
  
#### Eventarc Admin 

(`roles/eventarc.admin`) Full control over all Eventarc resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `eventarc.*`

  * `eventarc.channelConnections.create`
  * `eventarc.channelConnections.createTagBinding`
  * `eventarc.channelConnections.delete`
  * `eventarc.channelConnections.deleteTagBinding`
  * `eventarc.channelConnections.get`
  * `eventarc.channelConnections.getIamPolicy`
  * `eventarc.channelConnections.list`
  * `eventarc.channelConnections.listEffectiveTags`
  * `eventarc.channelConnections.listTagBindings`
  * `eventarc.channelConnections.publish`
  * `eventarc.channelConnections.setIamPolicy`
  * `eventarc.channels.attach`
  * `eventarc.channels.create`
  * `eventarc.channels.createTagBinding`
  * `eventarc.channels.delete`
  * `eventarc.channels.deleteTagBinding`
  * `eventarc.channels.get`
  * `eventarc.channels.getIamPolicy`
  * `eventarc.channels.list`
  * `eventarc.channels.listEffectiveTags`
  * `eventarc.channels.listTagBindings`
  * `eventarc.channels.publish`
  * `eventarc.channels.setIamPolicy`
  * `eventarc.channels.undelete`
  * `eventarc.channels.update`
  * `eventarc.enrollments.create`
  * `eventarc.enrollments.delete`
  * `eventarc.enrollments.get`
  * `eventarc.enrollments.getIamPolicy`
  * `eventarc.enrollments.list`
  * `eventarc.enrollments.setIamPolicy`
  * `eventarc.enrollments.update`
  * `eventarc.events.receiveAuditLogWritten`
  * `eventarc.events.receiveEvent`
  * `eventarc.googleApiSources.create`
  * `eventarc.googleApiSources.delete`
  * `eventarc.googleApiSources.get`
  * `eventarc.googleApiSources.getIamPolicy`
  * `eventarc.googleApiSources.list`
  * `eventarc.googleApiSources.setIamPolicy`
  * `eventarc.googleApiSources.update`
  * `eventarc.googleChannelConfigs.get`
  * `eventarc.googleChannelConfigs.update`
  * `eventarc.kafkaSources.create`
  * `eventarc.kafkaSources.delete`
  * `eventarc.kafkaSources.get`
  * `eventarc.kafkaSources.getIamPolicy`
  * `eventarc.kafkaSources.list`
  * `eventarc.kafkaSources.setIamPolicy`
  * `eventarc.locations.get`
  * `eventarc.locations.list`
  * `eventarc.messageBuses.create`
  * `eventarc.messageBuses.delete`
  * `eventarc.messageBuses.get`
  * `eventarc.messageBuses.getIamPolicy`
  * `eventarc.messageBuses.list`
  * `eventarc.messageBuses.publish`
  * `eventarc.messageBuses.setIamPolicy`
  * `eventarc.messageBuses.update`
  * `eventarc.messageBuses.use`
  * `eventarc.multiProjectSources.collectGoogleApiEvents`
  * `eventarc.operations.cancel`
  * `eventarc.operations.delete`
  * `eventarc.operations.get`
  * `eventarc.operations.list`
  * `eventarc.pipelines.create`
  * `eventarc.pipelines.delete`
  * `eventarc.pipelines.get`
  * `eventarc.pipelines.getIamPolicy`
  * `eventarc.pipelines.list`
  * `eventarc.pipelines.setIamPolicy`
  * `eventarc.pipelines.update`
  * `eventarc.providers.get`
  * `eventarc.providers.list`
  * `eventarc.triggers.create`
  * `eventarc.triggers.createTagBinding`
  * `eventarc.triggers.delete`
  * `eventarc.triggers.deleteTagBinding`
  * `eventarc.triggers.get`
  * `eventarc.triggers.getIamPolicy`
  * `eventarc.triggers.list`
  * `eventarc.triggers.listEffectiveTags`
  * `eventarc.triggers.listTagBindings`
  * `eventarc.triggers.setIamPolicy`
  * `eventarc.triggers.undelete`
  * `eventarc.triggers.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Eventarc Editor 

(`roles/eventarc.editor`) Editor role for eventarc  |  `eventarc.channelConnections.create` `eventarc.channelConnections.delete` `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channelConnections.publish` `eventarc.channels.attach` `eventarc.channels.create` `eventarc.channels.delete` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.channels.publish` `eventarc.channels.undelete` `eventarc.channels.update` `eventarc.enrollments.create` `eventarc.enrollments.delete` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.enrollments.update` `eventarc.events.receiveEvent` `eventarc.googleApiSources.create` `eventarc.googleApiSources.delete` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleApiSources.update` `eventarc.googleChannelConfigs.*`

  * `eventarc.googleChannelConfigs.get`
  * `eventarc.googleChannelConfigs.update`

`eventarc.kafkaSources.create` `eventarc.kafkaSources.delete` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.messageBuses.create` `eventarc.messageBuses.delete` `eventarc.messageBuses.get` `eventarc.messageBuses.getIamPolicy` `eventarc.messageBuses.list` `eventarc.messageBuses.publish` `eventarc.messageBuses.update` `eventarc.messageBuses.use` `eventarc.multiProjectSources.collectGoogleApiEvents` `eventarc.operations.*`

  * `eventarc.operations.cancel`
  * `eventarc.operations.delete`
  * `eventarc.operations.get`
  * `eventarc.operations.list`

`eventarc.pipelines.create` `eventarc.pipelines.delete` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.pipelines.update` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.create` `eventarc.triggers.delete` `eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `eventarc.triggers.undelete` `eventarc.triggers.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Eventarc Event Receiver 

(`roles/eventarc.eventReceiver`) Can receive events from all event providers.  Lowest-level resources where you can grant this role:

  * Project 

|  `eventarc.events.*`

  * `eventarc.events.receiveAuditLogWritten`
  * `eventarc.events.receiveEvent`

  
  
#### Eventarc Viewer 

(`roles/eventarc.viewer`) Can view the state of all Eventarc resources, including IAM policies.  Lowest-level resources where you can grant this role:

  * Project 

|  `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleChannelConfigs.get` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.messageBuses.get` `eventarc.messageBuses.getIamPolicy` `eventarc.messageBuses.list` `eventarc.messageBuses.use` `eventarc.multiProjectSources.collectGoogleApiEvents` `eventarc.operations.get` `eventarc.operations.list` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Eventarc Connection Publisher Beta

(`roles/eventarc.connectionPublisher`) Can publish events to Eventarc channel connections.  Lowest-level resources where you can grant this role:

  * Project 

|  `eventarc.channelConnections.get` `eventarc.channelConnections.list` `eventarc.channelConnections.publish` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Eventarc Developer 

(`roles/eventarc.developer`) Access to read and write Eventarc resources.  Lowest-level resources where you can grant this role:

  * Project 

|  `eventarc.channelConnections.create` `eventarc.channelConnections.createTagBinding` `eventarc.channelConnections.delete` `eventarc.channelConnections.deleteTagBinding` `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channelConnections.publish` `eventarc.channels.attach` `eventarc.channels.create` `eventarc.channels.createTagBinding` `eventarc.channels.delete` `eventarc.channels.deleteTagBinding` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.channels.publish` `eventarc.channels.undelete` `eventarc.channels.update` `eventarc.enrollments.create` `eventarc.enrollments.delete` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.enrollments.update` `eventarc.googleApiSources.create` `eventarc.googleApiSources.delete` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleApiSources.update` `eventarc.googleChannelConfigs.*`

  * `eventarc.googleChannelConfigs.get`
  * `eventarc.googleChannelConfigs.update`

`eventarc.kafkaSources.create` `eventarc.kafkaSources.delete` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.operations.*`

  * `eventarc.operations.cancel`
  * `eventarc.operations.delete`
  * `eventarc.operations.get`
  * `eventarc.operations.list`

`eventarc.pipelines.create` `eventarc.pipelines.delete` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.pipelines.update` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.create` `eventarc.triggers.createTagBinding` `eventarc.triggers.delete` `eventarc.triggers.deleteTagBinding` `eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `eventarc.triggers.undelete` `eventarc.triggers.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Eventarc Message Bus Admin 

(`roles/eventarc.messageBusAdmin`) Full control over Message Buses resources.  |  `eventarc.messageBuses.create` `eventarc.messageBuses.delete` `eventarc.messageBuses.get` `eventarc.messageBuses.getIamPolicy` `eventarc.messageBuses.list` `eventarc.messageBuses.publish` `eventarc.messageBuses.update` `eventarc.messageBuses.use`  
  
#### Eventarc Message Bus User 

(`roles/eventarc.messageBusUser`) Access to publish to or bind to a Message Bus.  |  `eventarc.messageBuses.get` `eventarc.messageBuses.list` `eventarc.messageBuses.publish` `eventarc.messageBuses.use`  
  
#### Eventarc Event Collector Beta

(`roles/eventarc.multiProjectEventCollector`) Can collect events from multiple projects in an org for a source resource.  |  `eventarc.multiProjectSources.collectGoogleApiEvents`  
  
#### Eventarc Publisher Beta

(`roles/eventarc.publisher`) Can publish events to Eventarc channels.  Lowest-level resources where you can grant this role:

  * Project 

|  `eventarc.channels.get` `eventarc.channels.list` `eventarc.channels.publish` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Eventarc Service Agent 

(`roles/eventarc.serviceAgent`) Gives Eventarc service account access to managed resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.instanceGroupManagers.get` `compute.networkAttachments.get` `compute.networkAttachments.update` `compute.regionOperations.get` `container.clusters.connect` `container.clusters.get` `container.deployments.create` `container.deployments.delete` `container.deployments.get` `container.deployments.update` `container.namespaces.create` `container.namespaces.delete` `container.namespaces.get` `container.namespaces.list` `container.serviceAccounts.create` `container.serviceAccounts.delete` `container.serviceAccounts.get` `container.services.get` `dns.networks.targetWithPeeringZone` `eventarc.channels.publish` `eventarc.messageBuses.publish` `eventarc.operations.get` `iam.serviceAccounts.actAs` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.publish` `pubsub.topics.update` `run.jobs.get` `run.services.get` `serviceusage.services.use` `storage.buckets.get` `storage.buckets.update` `workflows.workflows.get`  
  
## Project-level IAM management

At the project level, you can grant, change, and revoke IAM roles using the Google Cloud console, the IAM API, or the Google Cloud CLI. For instructions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
