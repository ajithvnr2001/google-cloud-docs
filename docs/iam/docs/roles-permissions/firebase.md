---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/firebase/
title: Firebase roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:18.869430+00:00
---

# Firebase roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/firebase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase roles

Role | Permissions  
---|---  
  
#### Firebase Admin 

(`roles/firebase.admin`) Full access to Firebase products.  |  `apikeys.keys.get` `apikeys.keys.getKeyString` `apikeys.keys.list` `apikeys.keys.lookup` `appengine.applications.get` `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `automl.*`

  * `automl.annotationSpecs.create`
  * `automl.annotationSpecs.delete`
  * `automl.annotationSpecs.get`
  * `automl.annotationSpecs.list`
  * `automl.annotationSpecs.update`
  * `automl.annotations.approve`
  * `automl.annotations.create`
  * `automl.annotations.list`
  * `automl.annotations.manipulate`
  * `automl.annotations.reject`
  * `automl.columnSpecs.get`
  * `automl.columnSpecs.list`
  * `automl.columnSpecs.update`
  * `automl.datasets.create`
  * `automl.datasets.delete`
  * `automl.datasets.export`
  * `automl.datasets.get`
  * `automl.datasets.getIamPolicy`
  * `automl.datasets.import`
  * `automl.datasets.list`
  * `automl.datasets.setIamPolicy`
  * `automl.datasets.update`
  * `automl.examples.delete`
  * `automl.examples.get`
  * `automl.examples.list`
  * `automl.examples.update`
  * `automl.files.delete`
  * `automl.files.list`
  * `automl.humanAnnotationTasks.create`
  * `automl.humanAnnotationTasks.delete`
  * `automl.humanAnnotationTasks.get`
  * `automl.humanAnnotationTasks.list`
  * `automl.locations.get`
  * `automl.locations.getIamPolicy`
  * `automl.locations.list`
  * `automl.locations.setIamPolicy`
  * `automl.modelEvaluations.create`
  * `automl.modelEvaluations.get`
  * `automl.modelEvaluations.list`
  * `automl.models.create`
  * `automl.models.delete`
  * `automl.models.deploy`
  * `automl.models.export`
  * `automl.models.get`
  * `automl.models.getIamPolicy`
  * `automl.models.list`
  * `automl.models.predict`
  * `automl.models.setIamPolicy`
  * `automl.models.undeploy`
  * `automl.operations.cancel`
  * `automl.operations.delete`
  * `automl.operations.get`
  * `automl.operations.list`
  * `automl.tableSpecs.get`
  * `automl.tableSpecs.list`
  * `automl.tableSpecs.update`

`clientauthconfig.brands.get` `clientauthconfig.brands.list` `clientauthconfig.brands.update` `clientauthconfig.clients.create` `clientauthconfig.clients.delete` `clientauthconfig.clients.get` `clientauthconfig.clients.list` `clientauthconfig.clients.update` `cloudaicompanion.instances.completeTask` `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudconfig.*`

  * `cloudconfig.configs.get`
  * `cloudconfig.configs.update`

`cloudfunctions.*`

  * `cloudfunctions.functions.call`
  * `cloudfunctions.functions.create`
  * `cloudfunctions.functions.delete`
  * `cloudfunctions.functions.generationUpgrade`
  * `cloudfunctions.functions.get`
  * `cloudfunctions.functions.getIamPolicy`
  * `cloudfunctions.functions.invoke`
  * `cloudfunctions.functions.list`
  * `cloudfunctions.functions.setIamPolicy`
  * `cloudfunctions.functions.sourceCodeGet`
  * `cloudfunctions.functions.sourceCodeSet`
  * `cloudfunctions.functions.update`
  * `cloudfunctions.locations.list`
  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `cloudmessaging.*`

  * `cloudmessaging.messages.create`
  * `cloudmessaging.topicSubscriptions.create`
  * `cloudmessaging.topicSubscriptions.delete`
  * `cloudmessaging.topicSubscriptions.get`
  * `cloudmessaging.topicSubscriptions.list`
  * `cloudmessaging.topicSubscriptions.update`

`cloudnotifications.activities.list` `cloudtestservice.environmentcatalog.get` `cloudtestservice.matrices.*`

  * `cloudtestservice.matrices.create`
  * `cloudtestservice.matrices.get`
  * `cloudtestservice.matrices.update`

`cloudtoolresults.*`

  * `cloudtoolresults.executions.create`
  * `cloudtoolresults.executions.get`
  * `cloudtoolresults.executions.list`
  * `cloudtoolresults.executions.update`
  * `cloudtoolresults.histories.create`
  * `cloudtoolresults.histories.get`
  * `cloudtoolresults.histories.list`
  * `cloudtoolresults.settings.create`
  * `cloudtoolresults.settings.get`
  * `cloudtoolresults.settings.update`
  * `cloudtoolresults.steps.create`
  * `cloudtoolresults.steps.get`
  * `cloudtoolresults.steps.list`
  * `cloudtoolresults.steps.update`

`databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.studioQueries.*`

  * `databasesconsole.studioQueries.create`
  * `databasesconsole.studioQueries.delete`
  * `databasesconsole.studioQueries.get`
  * `databasesconsole.studioQueries.list`
  * `databasesconsole.studioQueries.search`
  * `databasesconsole.studioQueries.update`

`datastore.*`

  * `datastore.backupSchedules.create`
  * `datastore.backupSchedules.delete`
  * `datastore.backupSchedules.get`
  * `datastore.backupSchedules.list`
  * `datastore.backupSchedules.update`
  * `datastore.backups.delete`
  * `datastore.backups.get`
  * `datastore.backups.list`
  * `datastore.backups.restoreDatabase`
  * `datastore.databases.bulkDelete`
  * `datastore.databases.clone`
  * `datastore.databases.create`
  * `datastore.databases.createTagBinding`
  * `datastore.databases.delete`
  * `datastore.databases.deleteTagBinding`
  * `datastore.databases.export`
  * `datastore.databases.get`
  * `datastore.databases.getMetadata`
  * `datastore.databases.import`
  * `datastore.databases.list`
  * `datastore.databases.listEffectiveTags`
  * `datastore.databases.listTagBindings`
  * `datastore.databases.update`
  * `datastore.entities.allocateIds`
  * `datastore.entities.create`
  * `datastore.entities.delete`
  * `datastore.entities.get`
  * `datastore.entities.list`
  * `datastore.entities.update`
  * `datastore.insights.get`
  * `datastore.keyVisualizerScans.get`
  * `datastore.keyVisualizerScans.list`
  * `datastore.locations.get`
  * `datastore.locations.list`
  * `datastore.namespaces.get`
  * `datastore.namespaces.list`
  * `datastore.operations.cancel`
  * `datastore.operations.delete`
  * `datastore.operations.get`
  * `datastore.operations.list`
  * `datastore.schemas.create`
  * `datastore.schemas.delete`
  * `datastore.schemas.get`
  * `datastore.schemas.list`
  * `datastore.schemas.update`
  * `datastore.statistics.get`
  * `datastore.statistics.list`
  * `datastore.userCreds.create`
  * `datastore.userCreds.delete`
  * `datastore.userCreds.get`
  * `datastore.userCreds.list`
  * `datastore.userCreds.update`

`errorreporting.groups.list` `eventarc.*`

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

`fcmdata.deliverydata.list` `firebase.*`

  * `firebase.billingPlans.get`
  * `firebase.billingPlans.update`
  * `firebase.clients.create`
  * `firebase.clients.delete`
  * `firebase.clients.get`
  * `firebase.clients.list`
  * `firebase.clients.undelete`
  * `firebase.clients.update`
  * `firebase.links.create`
  * `firebase.links.delete`
  * `firebase.links.list`
  * `firebase.links.update`
  * `firebase.playLinks.get`
  * `firebase.playLinks.list`
  * `firebase.playLinks.update`
  * `firebase.projects.delete`
  * `firebase.projects.get`
  * `firebase.projects.update`

`firebaseabt.*`

  * `firebaseabt.experimentresults.get`
  * `firebaseabt.experiments.create`
  * `firebaseabt.experiments.delete`
  * `firebaseabt.experiments.get`
  * `firebaseabt.experiments.list`
  * `firebaseabt.experiments.update`
  * `firebaseabt.projectmetadata.get`

`firebaseanalytics.*`

  * `firebaseanalytics.resources.googleAnalyticsEdit`
  * `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`

`firebaseappcheck.*`

  * `firebaseappcheck.appAttestConfig.get`
  * `firebaseappcheck.appAttestConfig.update`
  * `firebaseappcheck.appCheckTokens.verify`
  * `firebaseappcheck.automations.create`
  * `firebaseappcheck.automations.delete`
  * `firebaseappcheck.automations.get`
  * `firebaseappcheck.automations.list`
  * `firebaseappcheck.automations.resume`
  * `firebaseappcheck.automations.suspend`
  * `firebaseappcheck.automations.update`
  * `firebaseappcheck.debugTokens.get`
  * `firebaseappcheck.debugTokens.update`
  * `firebaseappcheck.deviceCheckConfig.get`
  * `firebaseappcheck.deviceCheckConfig.update`
  * `firebaseappcheck.playIntegrityConfig.get`
  * `firebaseappcheck.playIntegrityConfig.update`
  * `firebaseappcheck.recaptchaEnterpriseConfig.get`
  * `firebaseappcheck.recaptchaEnterpriseConfig.update`
  * `firebaseappcheck.recaptchaV3Config.get`
  * `firebaseappcheck.recaptchaV3Config.update`
  * `firebaseappcheck.resourcePolicies.get`
  * `firebaseappcheck.resourcePolicies.update`
  * `firebaseappcheck.safetyNetConfig.get`
  * `firebaseappcheck.safetyNetConfig.update`
  * `firebaseappcheck.services.get`
  * `firebaseappcheck.services.update`
  * `firebaseappcheck.tokens.mint`

`firebaseappdistro.*`

  * `firebaseappdistro.groups.list`
  * `firebaseappdistro.groups.update`
  * `firebaseappdistro.releases.list`
  * `firebaseappdistro.releases.update`
  * `firebaseappdistro.testers.list`
  * `firebaseappdistro.testers.update`

`firebaseapphosting.*`

  * `firebaseapphosting.backends.create`
  * `firebaseapphosting.backends.delete`
  * `firebaseapphosting.backends.get`
  * `firebaseapphosting.backends.list`
  * `firebaseapphosting.backends.update`
  * `firebaseapphosting.builds.create`
  * `firebaseapphosting.builds.delete`
  * `firebaseapphosting.builds.get`
  * `firebaseapphosting.builds.list`
  * `firebaseapphosting.builds.update`
  * `firebaseapphosting.domains.create`
  * `firebaseapphosting.domains.delete`
  * `firebaseapphosting.domains.get`
  * `firebaseapphosting.domains.list`
  * `firebaseapphosting.domains.update`
  * `firebaseapphosting.locations.get`
  * `firebaseapphosting.locations.list`
  * `firebaseapphosting.operations.cancel`
  * `firebaseapphosting.operations.delete`
  * `firebaseapphosting.operations.get`
  * `firebaseapphosting.operations.list`
  * `firebaseapphosting.rollouts.create`
  * `firebaseapphosting.rollouts.delete`
  * `firebaseapphosting.rollouts.get`
  * `firebaseapphosting.rollouts.list`
  * `firebaseapphosting.rollouts.update`
  * `firebaseapphosting.traffic.get`
  * `firebaseapphosting.traffic.update`

`firebaseauth.*`

  * `firebaseauth.configs.create`
  * `firebaseauth.configs.get`
  * `firebaseauth.configs.getHashConfig`
  * `firebaseauth.configs.getSecret`
  * `firebaseauth.configs.update`
  * `firebaseauth.users.create`
  * `firebaseauth.users.createSession`
  * `firebaseauth.users.delete`
  * `firebaseauth.users.get`
  * `firebaseauth.users.sendEmail`
  * `firebaseauth.users.update`

`firebasecrash.*`

  * `firebasecrash.issues.update`
  * `firebasecrash.reports.get`

`firebasecrashlytics.*`

  * `firebasecrashlytics.config.get`
  * `firebasecrashlytics.config.update`
  * `firebasecrashlytics.data.get`
  * `firebasecrashlytics.issues.get`
  * `firebasecrashlytics.issues.list`
  * `firebasecrashlytics.issues.update`
  * `firebasecrashlytics.sessions.get`

`firebasedatabase.*`

  * `firebasedatabase.instances.create`
  * `firebasedatabase.instances.delete`
  * `firebasedatabase.instances.disable`
  * `firebasedatabase.instances.get`
  * `firebasedatabase.instances.list`
  * `firebasedatabase.instances.reenable`
  * `firebasedatabase.instances.undelete`
  * `firebasedatabase.instances.update`

`firebasedataconnect.*`

  * `firebasedataconnect.connectorRevisions.delete`
  * `firebasedataconnect.connectorRevisions.get`
  * `firebasedataconnect.connectorRevisions.list`
  * `firebasedataconnect.connectors.create`
  * `firebasedataconnect.connectors.delete`
  * `firebasedataconnect.connectors.get`
  * `firebasedataconnect.connectors.impersonateMutation`
  * `firebasedataconnect.connectors.impersonateQuery`
  * `firebasedataconnect.connectors.list`
  * `firebasedataconnect.connectors.update`
  * `firebasedataconnect.locations.get`
  * `firebasedataconnect.locations.list`
  * `firebasedataconnect.operations.cancel`
  * `firebasedataconnect.operations.delete`
  * `firebasedataconnect.operations.get`
  * `firebasedataconnect.operations.list`
  * `firebasedataconnect.schemaRevisions.delete`
  * `firebasedataconnect.schemaRevisions.get`
  * `firebasedataconnect.schemaRevisions.list`
  * `firebasedataconnect.schemas.create`
  * `firebasedataconnect.schemas.delete`
  * `firebasedataconnect.schemas.get`
  * `firebasedataconnect.schemas.list`
  * `firebasedataconnect.schemas.migrate`
  * `firebasedataconnect.schemas.update`
  * `firebasedataconnect.services.create`
  * `firebasedataconnect.services.delete`
  * `firebasedataconnect.services.executeGraphql`
  * `firebasedataconnect.services.executeGraphqlRead`
  * `firebasedataconnect.services.generateQuery`
  * `firebasedataconnect.services.generateSchema`
  * `firebasedataconnect.services.get`
  * `firebasedataconnect.services.introspectGraphql`
  * `firebasedataconnect.services.list`
  * `firebasedataconnect.services.update`

`firebasedynamiclinks.*`

  * `firebasedynamiclinks.destinations.list`
  * `firebasedynamiclinks.destinations.update`
  * `firebasedynamiclinks.domains.create`
  * `firebasedynamiclinks.domains.delete`
  * `firebasedynamiclinks.domains.get`
  * `firebasedynamiclinks.domains.list`
  * `firebasedynamiclinks.domains.update`
  * `firebasedynamiclinks.links.create`
  * `firebasedynamiclinks.links.get`
  * `firebasedynamiclinks.links.list`
  * `firebasedynamiclinks.links.update`
  * `firebasedynamiclinks.stats.get`

`firebaseextensions.*`

  * `firebaseextensions.configs.create`
  * `firebaseextensions.configs.delete`
  * `firebaseextensions.configs.list`
  * `firebaseextensions.configs.update`

`firebaseextensionspublisher.*`

  * `firebaseextensionspublisher.extensions.create`
  * `firebaseextensionspublisher.extensions.delete`
  * `firebaseextensionspublisher.extensions.get`
  * `firebaseextensionspublisher.extensions.list`

`firebasehosting.*`

  * `firebasehosting.sites.create`
  * `firebasehosting.sites.delete`
  * `firebasehosting.sites.get`
  * `firebasehosting.sites.list`
  * `firebasehosting.sites.update`

`firebaseinappmessaging.*`

  * `firebaseinappmessaging.campaigns.create`
  * `firebaseinappmessaging.campaigns.delete`
  * `firebaseinappmessaging.campaigns.get`
  * `firebaseinappmessaging.campaigns.list`
  * `firebaseinappmessaging.campaigns.update`

`firebasemessagingcampaigns.*`

  * `firebasemessagingcampaigns.campaigns.create`
  * `firebasemessagingcampaigns.campaigns.delete`
  * `firebasemessagingcampaigns.campaigns.get`
  * `firebasemessagingcampaigns.campaigns.list`
  * `firebasemessagingcampaigns.campaigns.start`
  * `firebasemessagingcampaigns.campaigns.stop`
  * `firebasemessagingcampaigns.campaigns.update`

`firebaseml.*`

  * `firebaseml.models.create`
  * `firebaseml.models.delete`
  * `firebaseml.models.get`
  * `firebaseml.models.list`
  * `firebaseml.models.update`
  * `firebaseml.modelversions.create`
  * `firebaseml.modelversions.get`
  * `firebaseml.modelversions.list`
  * `firebaseml.modelversions.update`

`firebasenotifications.*`

  * `firebasenotifications.messages.create`
  * `firebasenotifications.messages.delete`
  * `firebasenotifications.messages.get`
  * `firebasenotifications.messages.list`
  * `firebasenotifications.messages.update`

`firebaseperformance.*`

  * `firebaseperformance.config.update`
  * `firebaseperformance.data.get`

`firebaserules.*`

  * `firebaserules.releases.create`
  * `firebaserules.releases.delete`
  * `firebaserules.releases.get`
  * `firebaserules.releases.getExecutable`
  * `firebaserules.releases.list`
  * `firebaserules.releases.update`
  * `firebaserules.rulesets.create`
  * `firebaserules.rulesets.delete`
  * `firebaserules.rulesets.get`
  * `firebaserules.rulesets.list`
  * `firebaserules.rulesets.test`

`firebasestorage.*`

  * `firebasestorage.buckets.addFirebase`
  * `firebasestorage.buckets.get`
  * `firebasestorage.buckets.list`
  * `firebasestorage.buckets.removeFirebase`
  * `firebasestorage.defaultBucket.create`
  * `firebasestorage.defaultBucket.delete`
  * `firebasestorage.defaultBucket.get`

`firebasevertexai.*`

  * `firebasevertexai.configs.get`
  * `firebasevertexai.configs.update`
  * `firebasevertexai.promptTemplates.create`
  * `firebasevertexai.promptTemplates.delete`
  * `firebasevertexai.promptTemplates.get`
  * `firebasevertexai.promptTemplates.list`
  * `firebasevertexai.promptTemplates.update`
  * `firebasevertexai.promptTemplates.updateLock`

`logging.logEntries.download` `logging.logEntries.list` `logging.views.access` `logging.views.listLogs` `logging.views.listResourceKeys` `logging.views.listResourceValues` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`oauthconfig.verification.get` `orgpolicy.policy.get` `recommender.cloudFunctionsPerformanceInsights.*`

  * `recommender.cloudFunctionsPerformanceInsights.get`
  * `recommender.cloudFunctionsPerformanceInsights.list`
  * `recommender.cloudFunctionsPerformanceInsights.update`

`recommender.cloudFunctionsPerformanceRecommendations.*`

  * `recommender.cloudFunctionsPerformanceRecommendations.get`
  * `recommender.cloudFunctionsPerformanceRecommendations.list`
  * `recommender.cloudFunctionsPerformanceRecommendations.update`

`recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.*`

  * `recommender.runServiceCostInsights.get`
  * `recommender.runServiceCostInsights.list`
  * `recommender.runServiceCostInsights.update`

`recommender.runServiceCostRecommendations.*`

  * `recommender.runServiceCostRecommendations.get`
  * `recommender.runServiceCostRecommendations.list`
  * `recommender.runServiceCostRecommendations.update`

`recommender.runServiceIdentityInsights.*`

  * `recommender.runServiceIdentityInsights.get`
  * `recommender.runServiceIdentityInsights.list`
  * `recommender.runServiceIdentityInsights.update`

`recommender.runServiceIdentityRecommendations.*`

  * `recommender.runServiceIdentityRecommendations.get`
  * `recommender.runServiceIdentityRecommendations.list`
  * `recommender.runServiceIdentityRecommendations.update`

`recommender.runServicePerformanceInsights.*`

  * `recommender.runServicePerformanceInsights.get`
  * `recommender.runServicePerformanceInsights.list`
  * `recommender.runServicePerformanceInsights.update`

`recommender.runServicePerformanceRecommendations.*`

  * `recommender.runServicePerformanceRecommendations.get`
  * `recommender.runServicePerformanceRecommendations.list`
  * `recommender.runServicePerformanceRecommendations.update`

`recommender.runServiceSecurityInsights.*`

  * `recommender.runServiceSecurityInsights.get`
  * `recommender.runServiceSecurityInsights.list`
  * `recommender.runServiceSecurityInsights.update`

`recommender.runServiceSecurityRecommendations.*`

  * `recommender.runServiceSecurityRecommendations.get`
  * `recommender.runServiceSecurityRecommendations.list`
  * `recommender.runServiceSecurityRecommendations.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`remotebuildexecution.blobs.get` `resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `run.*`

  * `run.configurations.get`
  * `run.configurations.list`
  * `run.executions.cancel`
  * `run.executions.delete`
  * `run.executions.get`
  * `run.executions.list`
  * `run.instances.create`
  * `run.instances.delete`
  * `run.instances.get`
  * `run.instances.getIamPolicy`
  * `run.instances.invoke`
  * `run.instances.list`
  * `run.instances.setIamPolicy`
  * `run.instances.sshRead`
  * `run.instances.sshRoot`
  * `run.instances.start`
  * `run.instances.stop`
  * `run.instances.update`
  * `run.jobs.create`
  * `run.jobs.createTagBinding`
  * `run.jobs.delete`
  * `run.jobs.deleteTagBinding`
  * `run.jobs.get`
  * `run.jobs.getIamPolicy`
  * `run.jobs.list`
  * `run.jobs.listEffectiveTags`
  * `run.jobs.listTagBindings`
  * `run.jobs.run`
  * `run.jobs.runWithOverrides`
  * `run.jobs.setIamPolicy`
  * `run.jobs.sshRead`
  * `run.jobs.sshRoot`
  * `run.jobs.update`
  * `run.locations.list`
  * `run.locations.uploadSource`
  * `run.operations.delete`
  * `run.operations.get`
  * `run.operations.list`
  * `run.prompts.get`
  * `run.revisions.delete`
  * `run.revisions.get`
  * `run.revisions.list`
  * `run.routes.get`
  * `run.routes.invoke`
  * `run.routes.list`
  * `run.services.create`
  * `run.services.createTagBinding`
  * `run.services.delete`
  * `run.services.deleteTagBinding`
  * `run.services.get`
  * `run.services.getIamPolicy`
  * `run.services.list`
  * `run.services.listEffectiveTags`
  * `run.services.listTagBindings`
  * `run.services.setIamPolicy`
  * `run.services.sshRead`
  * `run.services.sshRoot`
  * `run.services.update`
  * `run.tasks.get`
  * `run.tasks.list`
  * `run.workerpools.create`
  * `run.workerpools.delete`
  * `run.workerpools.get`
  * `run.workerpools.getIamPolicy`
  * `run.workerpools.list`
  * `run.workerpools.setIamPolicy`
  * `run.workerpools.sshRead`
  * `run.workerpools.sshRoot`
  * `run.workerpools.update`

`runtimeconfig.configs.create` `runtimeconfig.configs.delete` `runtimeconfig.configs.get` `runtimeconfig.configs.list` `runtimeconfig.configs.update` `runtimeconfig.operations.*`

  * `runtimeconfig.operations.get`
  * `runtimeconfig.operations.list`

`runtimeconfig.variables.create` `runtimeconfig.variables.delete` `runtimeconfig.variables.get` `runtimeconfig.variables.list` `runtimeconfig.variables.update` `runtimeconfig.variables.watch` `runtimeconfig.waiters.create` `runtimeconfig.waiters.delete` `runtimeconfig.waiters.get` `runtimeconfig.waiters.list` `runtimeconfig.waiters.update` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

  * `storage.anywhereCaches.create`
  * `storage.anywhereCaches.disable`
  * `storage.anywhereCaches.get`
  * `storage.anywhereCaches.list`
  * `storage.anywhereCaches.pause`
  * `storage.anywhereCaches.resume`
  * `storage.anywhereCaches.update`

`storage.bucketOperations.*`

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`

`storage.buckets.*`

  * `storage.buckets.create`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.delete`
  * `storage.buckets.deleteTagBinding`
  * `storage.buckets.enableObjectRetention`
  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.getIpFilter`
  * `storage.buckets.getObjectInsights`
  * `storage.buckets.list`
  * `storage.buckets.listEffectiveTags`
  * `storage.buckets.listTagBindings`
  * `storage.buckets.relocate`
  * `storage.buckets.restore`
  * `storage.buckets.setIamPolicy`
  * `storage.buckets.setIpFilter`
  * `storage.buckets.update`
  * `storage.buckets.viewIntelligenceDetails`
  * `storage.buckets.viewSecurityIntelligenceDetails`

`storage.featureConfigs.*`

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.delete`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.update`

`storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.intelligenceConfigs.*`

  * `storage.intelligenceConfigs.get`
  * `storage.intelligenceConfigs.update`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

`storagebatchoperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`
  * `storagebatchoperations.jobs.cancel`
  * `storagebatchoperations.jobs.create`
  * `storagebatchoperations.jobs.delete`
  * `storagebatchoperations.jobs.get`
  * `storagebatchoperations.jobs.list`
  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`
  * `storagebatchoperations.operations.cancel`
  * `storagebatchoperations.operations.delete`
  * `storagebatchoperations.operations.get`
  * `storagebatchoperations.operations.list`

  
  
#### Firebase Editor 

(`roles/firebase.editor`) Editor access to Firebase products.  |  `apikeys.keys.get` `apikeys.keys.list` `automl.annotationSpecs.get` `automl.annotationSpecs.list` `automl.annotations.list` `automl.columnSpecs.get` `automl.columnSpecs.list` `automl.datasets.get` `automl.datasets.list` `automl.examples.get` `automl.examples.list` `automl.files.list` `automl.humanAnnotationTasks.get` `automl.humanAnnotationTasks.list` `automl.locations.get` `automl.locations.list` `automl.modelEvaluations.get` `automl.modelEvaluations.list` `automl.models.get` `automl.models.list` `automl.operations.get` `automl.operations.list` `automl.tableSpecs.get` `automl.tableSpecs.list` `clientauthconfig.brands.get` `clientauthconfig.brands.list` `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudconfig.*`

  * `cloudconfig.configs.get`
  * `cloudconfig.configs.update`

`cloudfunctions.functions.get` `cloudfunctions.functions.getIamPolicy` `cloudfunctions.functions.list` `cloudfunctions.locations.list` `cloudfunctions.operations.*`

  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`cloudmessaging.topicSubscriptions.get` `cloudmessaging.topicSubscriptions.list` `cloudnotifications.activities.list` `cloudtestservice.*`

  * `cloudtestservice.devicesession.cancel`
  * `cloudtestservice.devicesession.create`
  * `cloudtestservice.devicesession.get`
  * `cloudtestservice.devicesession.list`
  * `cloudtestservice.devicesession.update`
  * `cloudtestservice.devicesession.use`
  * `cloudtestservice.environmentcatalog.get`
  * `cloudtestservice.matrices.create`
  * `cloudtestservice.matrices.get`
  * `cloudtestservice.matrices.update`

`cloudtoolresults.*`

  * `cloudtoolresults.executions.create`
  * `cloudtoolresults.executions.get`
  * `cloudtoolresults.executions.list`
  * `cloudtoolresults.executions.update`
  * `cloudtoolresults.histories.create`
  * `cloudtoolresults.histories.get`
  * `cloudtoolresults.histories.list`
  * `cloudtoolresults.settings.create`
  * `cloudtoolresults.settings.get`
  * `cloudtoolresults.settings.update`
  * `cloudtoolresults.steps.create`
  * `cloudtoolresults.steps.get`
  * `cloudtoolresults.steps.list`
  * `cloudtoolresults.steps.update`

`datastore.backups.get` `datastore.backups.list` `datastore.databases.get` `datastore.databases.getMetadata` `datastore.databases.list` `datastore.entities.get` `datastore.entities.list` `datastore.namespaces.*`

  * `datastore.namespaces.get`
  * `datastore.namespaces.list`

`datastore.schemas.get` `datastore.schemas.list` `datastore.statistics.*`

  * `datastore.statistics.get`
  * `datastore.statistics.list`

`datastore.userCreds.get` `datastore.userCreds.list` `errorreporting.groups.list` `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleChannelConfigs.get` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.messageBuses.get` `eventarc.messageBuses.getIamPolicy` `eventarc.messageBuses.list` `eventarc.messageBuses.use` `eventarc.multiProjectSources.collectGoogleApiEvents` `eventarc.operations.get` `eventarc.operations.list` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `fcmdata.deliverydata.list` `firebase.billingPlans.get` `firebase.clients.*`

  * `firebase.clients.create`
  * `firebase.clients.delete`
  * `firebase.clients.get`
  * `firebase.clients.list`
  * `firebase.clients.undelete`
  * `firebase.clients.update`

`firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebase.projects.update` `firebaseabt.*`

  * `firebaseabt.experimentresults.get`
  * `firebaseabt.experiments.create`
  * `firebaseabt.experiments.delete`
  * `firebaseabt.experiments.get`
  * `firebaseabt.experiments.list`
  * `firebaseabt.experiments.update`
  * `firebaseabt.projectmetadata.get`

`firebaseanalytics.*`

  * `firebaseanalytics.resources.googleAnalyticsEdit`
  * `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`

`firebaseappcheck.appAttestConfig.get` `firebaseappcheck.automations.get` `firebaseappcheck.automations.list` `firebaseappcheck.debugTokens.get` `firebaseappcheck.deviceCheckConfig.get` `firebaseappcheck.playIntegrityConfig.get` `firebaseappcheck.recaptchaEnterpriseConfig.get` `firebaseappcheck.recaptchaV3Config.get` `firebaseappcheck.resourcePolicies.get` `firebaseappcheck.safetyNetConfig.get` `firebaseappcheck.services.get` `firebaseappdistro.*`

  * `firebaseappdistro.groups.list`
  * `firebaseappdistro.groups.update`
  * `firebaseappdistro.releases.list`
  * `firebaseappdistro.releases.update`
  * `firebaseappdistro.testers.list`
  * `firebaseappdistro.testers.update`

`firebaseapphosting.backends.get` `firebaseapphosting.backends.list` `firebaseapphosting.builds.get` `firebaseapphosting.builds.list` `firebaseapphosting.domains.get` `firebaseapphosting.domains.list` `firebaseapphosting.locations.*`

  * `firebaseapphosting.locations.get`
  * `firebaseapphosting.locations.list`

`firebaseapphosting.operations.get` `firebaseapphosting.operations.list` `firebaseapphosting.rollouts.get` `firebaseapphosting.rollouts.list` `firebaseapphosting.traffic.get` `firebaseauth.*`

  * `firebaseauth.configs.create`
  * `firebaseauth.configs.get`
  * `firebaseauth.configs.getHashConfig`
  * `firebaseauth.configs.getSecret`
  * `firebaseauth.configs.update`
  * `firebaseauth.users.create`
  * `firebaseauth.users.createSession`
  * `firebaseauth.users.delete`
  * `firebaseauth.users.get`
  * `firebaseauth.users.sendEmail`
  * `firebaseauth.users.update`

`firebasecrash.*`

  * `firebasecrash.issues.update`
  * `firebasecrash.reports.get`

`firebasecrashlytics.*`

  * `firebasecrashlytics.config.get`
  * `firebasecrashlytics.config.update`
  * `firebasecrashlytics.data.get`
  * `firebasecrashlytics.issues.get`
  * `firebasecrashlytics.issues.list`
  * `firebasecrashlytics.issues.update`
  * `firebasecrashlytics.sessions.get`

`firebasedatabase.*`

  * `firebasedatabase.instances.create`
  * `firebasedatabase.instances.delete`
  * `firebasedatabase.instances.disable`
  * `firebasedatabase.instances.get`
  * `firebasedatabase.instances.list`
  * `firebasedatabase.instances.reenable`
  * `firebasedatabase.instances.undelete`
  * `firebasedatabase.instances.update`

`firebasedataconnect.connectorRevisions.get` `firebasedataconnect.connectorRevisions.list` `firebasedataconnect.connectors.get` `firebasedataconnect.connectors.list` `firebasedataconnect.locations.*`

  * `firebasedataconnect.locations.get`
  * `firebasedataconnect.locations.list`

`firebasedataconnect.operations.get` `firebasedataconnect.operations.list` `firebasedataconnect.schemaRevisions.get` `firebasedataconnect.schemaRevisions.list` `firebasedataconnect.schemas.get` `firebasedataconnect.schemas.list` `firebasedataconnect.services.generateQuery` `firebasedataconnect.services.generateSchema` `firebasedataconnect.services.get` `firebasedataconnect.services.introspectGraphql` `firebasedataconnect.services.list` `firebasedynamiclinks.destinations.list` `firebasedynamiclinks.domains.create` `firebasedynamiclinks.domains.get` `firebasedynamiclinks.domains.list` `firebasedynamiclinks.domains.update` `firebasedynamiclinks.links.*`

  * `firebasedynamiclinks.links.create`
  * `firebasedynamiclinks.links.get`
  * `firebasedynamiclinks.links.list`
  * `firebasedynamiclinks.links.update`

`firebasedynamiclinks.stats.get` `firebaseextensions.configs.list` `firebaseextensionspublisher.*`

  * `firebaseextensionspublisher.extensions.create`
  * `firebaseextensionspublisher.extensions.delete`
  * `firebaseextensionspublisher.extensions.get`
  * `firebaseextensionspublisher.extensions.list`

`firebasehosting.*`

  * `firebasehosting.sites.create`
  * `firebasehosting.sites.delete`
  * `firebasehosting.sites.get`
  * `firebasehosting.sites.list`
  * `firebasehosting.sites.update`

`firebaseinappmessaging.*`

  * `firebaseinappmessaging.campaigns.create`
  * `firebaseinappmessaging.campaigns.delete`
  * `firebaseinappmessaging.campaigns.get`
  * `firebaseinappmessaging.campaigns.list`
  * `firebaseinappmessaging.campaigns.update`

`firebasemessagingcampaigns.campaigns.get` `firebasemessagingcampaigns.campaigns.list` `firebaseml.*`

  * `firebaseml.models.create`
  * `firebaseml.models.delete`
  * `firebaseml.models.get`
  * `firebaseml.models.list`
  * `firebaseml.models.update`
  * `firebaseml.modelversions.create`
  * `firebaseml.modelversions.get`
  * `firebaseml.modelversions.list`
  * `firebaseml.modelversions.update`

`firebasenotifications.*`

  * `firebasenotifications.messages.create`
  * `firebasenotifications.messages.delete`
  * `firebasenotifications.messages.get`
  * `firebasenotifications.messages.list`
  * `firebasenotifications.messages.update`

`firebaseperformance.*`

  * `firebaseperformance.config.update`
  * `firebaseperformance.data.get`

`firebaserules.*`

  * `firebaserules.releases.create`
  * `firebaserules.releases.delete`
  * `firebaserules.releases.get`
  * `firebaserules.releases.getExecutable`
  * `firebaserules.releases.list`
  * `firebaserules.releases.update`
  * `firebaserules.rulesets.create`
  * `firebaserules.rulesets.delete`
  * `firebaserules.rulesets.get`
  * `firebaserules.rulesets.list`
  * `firebaserules.rulesets.test`

`firebasestorage.buckets.get` `firebasestorage.buckets.list` `firebasestorage.defaultBucket.get` `firebasevertexai.configs.get` `firebasevertexai.promptTemplates.get` `firebasevertexai.promptTemplates.list` `logging.logEntries.download` `logging.logEntries.list` `logging.views.access` `logging.views.listLogs` `logging.views.listResourceKeys` `logging.views.listResourceValues` `monitoring.timeSeries.list` `oauthconfig.verification.get` `recommender.cloudFunctionsPerformanceInsights.get` `recommender.cloudFunctionsPerformanceInsights.list` `recommender.cloudFunctionsPerformanceRecommendations.get` `recommender.cloudFunctionsPerformanceRecommendations.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.get` `recommender.runServiceCostInsights.list` `recommender.runServiceCostRecommendations.get` `recommender.runServiceCostRecommendations.list` `recommender.runServiceIdentityInsights.get` `recommender.runServiceIdentityInsights.list` `recommender.runServiceIdentityRecommendations.get` `recommender.runServiceIdentityRecommendations.list` `recommender.runServicePerformanceInsights.get` `recommender.runServicePerformanceInsights.list` `recommender.runServicePerformanceRecommendations.get` `recommender.runServicePerformanceRecommendations.list` `recommender.runServiceSecurityInsights.get` `recommender.runServiceSecurityInsights.list` `recommender.runServiceSecurityRecommendations.get` `recommender.runServiceSecurityRecommendations.list` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `run.configurations.*`

  * `run.configurations.get`
  * `run.configurations.list`

`run.executions.get` `run.executions.list` `run.instances.get` `run.instances.getIamPolicy` `run.instances.list` `run.jobs.get` `run.jobs.getIamPolicy` `run.jobs.list` `run.jobs.listEffectiveTags` `run.jobs.listTagBindings` `run.locations.list` `run.operations.get` `run.operations.list` `run.prompts.get` `run.revisions.get` `run.revisions.list` `run.routes.get` `run.routes.list` `run.services.get` `run.services.getIamPolicy` `run.services.list` `run.services.listEffectiveTags` `run.services.listTagBindings` `run.tasks.*`

  * `run.tasks.get`
  * `run.tasks.list`

`run.workerpools.get` `run.workerpools.getIamPolicy` `run.workerpools.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list` `storage.objects.get` `storage.objects.getIamPolicy` `storage.objects.list`  
  
#### Firebase Viewer 

(`roles/firebase.viewer`) Read-only access to Firebase products.  |  `apikeys.keys.get` `apikeys.keys.list` `automl.annotationSpecs.get` `automl.annotationSpecs.list` `automl.annotations.list` `automl.columnSpecs.get` `automl.columnSpecs.list` `automl.datasets.get` `automl.datasets.list` `automl.examples.get` `automl.examples.list` `automl.files.list` `automl.humanAnnotationTasks.get` `automl.humanAnnotationTasks.list` `automl.locations.get` `automl.locations.list` `automl.modelEvaluations.get` `automl.modelEvaluations.list` `automl.models.get` `automl.models.list` `automl.operations.get` `automl.operations.list` `automl.tableSpecs.get` `automl.tableSpecs.list` `clientauthconfig.brands.get` `clientauthconfig.brands.list` `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudconfig.configs.get` `cloudfunctions.functions.get` `cloudfunctions.functions.getIamPolicy` `cloudfunctions.functions.list` `cloudfunctions.locations.list` `cloudfunctions.operations.*`

  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`cloudmessaging.topicSubscriptions.get` `cloudmessaging.topicSubscriptions.list` `cloudnotifications.activities.list` `cloudtestservice.environmentcatalog.get` `cloudtestservice.matrices.get` `cloudtoolresults.executions.get` `cloudtoolresults.executions.list` `cloudtoolresults.histories.get` `cloudtoolresults.histories.list` `cloudtoolresults.settings.get` `cloudtoolresults.steps.get` `cloudtoolresults.steps.list` `datastore.backups.get` `datastore.backups.list` `datastore.databases.get` `datastore.databases.getMetadata` `datastore.databases.list` `datastore.entities.get` `datastore.entities.list` `datastore.namespaces.*`

  * `datastore.namespaces.get`
  * `datastore.namespaces.list`

`datastore.schemas.get` `datastore.schemas.list` `datastore.statistics.*`

  * `datastore.statistics.get`
  * `datastore.statistics.list`

`datastore.userCreds.get` `datastore.userCreds.list` `errorreporting.groups.list` `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleChannelConfigs.get` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.messageBuses.get` `eventarc.messageBuses.getIamPolicy` `eventarc.messageBuses.list` `eventarc.messageBuses.use` `eventarc.multiProjectSources.collectGoogleApiEvents` `eventarc.operations.get` `eventarc.operations.list` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `fcmdata.deliverydata.list` `firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseabt.experimentresults.get` `firebaseabt.experiments.get` `firebaseabt.experiments.list` `firebaseabt.projectmetadata.get` `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze` `firebaseappcheck.appAttestConfig.get` `firebaseappcheck.automations.get` `firebaseappcheck.automations.list` `firebaseappcheck.debugTokens.get` `firebaseappcheck.deviceCheckConfig.get` `firebaseappcheck.playIntegrityConfig.get` `firebaseappcheck.recaptchaEnterpriseConfig.get` `firebaseappcheck.recaptchaV3Config.get` `firebaseappcheck.resourcePolicies.get` `firebaseappcheck.safetyNetConfig.get` `firebaseappcheck.services.get` `firebaseappdistro.groups.list` `firebaseappdistro.releases.list` `firebaseappdistro.testers.list` `firebaseapphosting.backends.get` `firebaseapphosting.backends.list` `firebaseapphosting.builds.get` `firebaseapphosting.builds.list` `firebaseapphosting.domains.get` `firebaseapphosting.domains.list` `firebaseapphosting.locations.*`

  * `firebaseapphosting.locations.get`
  * `firebaseapphosting.locations.list`

`firebaseapphosting.operations.get` `firebaseapphosting.operations.list` `firebaseapphosting.rollouts.get` `firebaseapphosting.rollouts.list` `firebaseapphosting.traffic.get` `firebaseauth.configs.get` `firebaseauth.users.get` `firebasecrash.reports.get` `firebasecrashlytics.config.get` `firebasecrashlytics.data.get` `firebasecrashlytics.issues.get` `firebasecrashlytics.issues.list` `firebasecrashlytics.sessions.get` `firebasedatabase.instances.get` `firebasedatabase.instances.list` `firebasedataconnect.connectorRevisions.get` `firebasedataconnect.connectorRevisions.list` `firebasedataconnect.connectors.get` `firebasedataconnect.connectors.list` `firebasedataconnect.locations.*`

  * `firebasedataconnect.locations.get`
  * `firebasedataconnect.locations.list`

`firebasedataconnect.operations.get` `firebasedataconnect.operations.list` `firebasedataconnect.schemaRevisions.get` `firebasedataconnect.schemaRevisions.list` `firebasedataconnect.schemas.get` `firebasedataconnect.schemas.list` `firebasedataconnect.services.generateQuery` `firebasedataconnect.services.generateSchema` `firebasedataconnect.services.get` `firebasedataconnect.services.introspectGraphql` `firebasedataconnect.services.list` `firebasedynamiclinks.destinations.list` `firebasedynamiclinks.domains.get` `firebasedynamiclinks.domains.list` `firebasedynamiclinks.links.get` `firebasedynamiclinks.links.list` `firebasedynamiclinks.stats.get` `firebaseextensions.configs.list` `firebaseextensionspublisher.extensions.get` `firebaseextensionspublisher.extensions.list` `firebasehosting.sites.get` `firebasehosting.sites.list` `firebaseinappmessaging.campaigns.get` `firebaseinappmessaging.campaigns.list` `firebasemessagingcampaigns.campaigns.get` `firebasemessagingcampaigns.campaigns.list` `firebaseml.models.get` `firebaseml.models.list` `firebaseml.modelversions.get` `firebaseml.modelversions.list` `firebasenotifications.messages.get` `firebasenotifications.messages.list` `firebaseperformance.data.get` `firebaserules.releases.get` `firebaserules.releases.getExecutable` `firebaserules.releases.list` `firebaserules.rulesets.get` `firebaserules.rulesets.list` `firebasestorage.buckets.get` `firebasestorage.buckets.list` `firebasestorage.defaultBucket.get` `firebasevertexai.configs.get` `firebasevertexai.promptTemplates.get` `firebasevertexai.promptTemplates.list` `logging.logEntries.download` `logging.logEntries.list` `logging.views.access` `logging.views.listLogs` `logging.views.listResourceKeys` `logging.views.listResourceValues` `monitoring.timeSeries.list` `oauthconfig.verification.get` `recommender.cloudFunctionsPerformanceInsights.get` `recommender.cloudFunctionsPerformanceInsights.list` `recommender.cloudFunctionsPerformanceRecommendations.get` `recommender.cloudFunctionsPerformanceRecommendations.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.get` `recommender.runServiceCostInsights.list` `recommender.runServiceCostRecommendations.get` `recommender.runServiceCostRecommendations.list` `recommender.runServiceIdentityInsights.get` `recommender.runServiceIdentityInsights.list` `recommender.runServiceIdentityRecommendations.get` `recommender.runServiceIdentityRecommendations.list` `recommender.runServicePerformanceInsights.get` `recommender.runServicePerformanceInsights.list` `recommender.runServicePerformanceRecommendations.get` `recommender.runServicePerformanceRecommendations.list` `recommender.runServiceSecurityInsights.get` `recommender.runServiceSecurityInsights.list` `recommender.runServiceSecurityRecommendations.get` `recommender.runServiceSecurityRecommendations.list` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `run.configurations.*`

  * `run.configurations.get`
  * `run.configurations.list`

`run.executions.get` `run.executions.list` `run.instances.get` `run.instances.getIamPolicy` `run.instances.list` `run.jobs.get` `run.jobs.getIamPolicy` `run.jobs.list` `run.jobs.listEffectiveTags` `run.jobs.listTagBindings` `run.locations.list` `run.operations.get` `run.operations.list` `run.prompts.get` `run.revisions.get` `run.revisions.list` `run.routes.get` `run.routes.list` `run.services.get` `run.services.getIamPolicy` `run.services.list` `run.services.listEffectiveTags` `run.services.listTagBindings` `run.tasks.*`

  * `run.tasks.get`
  * `run.tasks.list`

`run.workerpools.get` `run.workerpools.getIamPolicy` `run.workerpools.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list` `storage.objects.get` `storage.objects.getIamPolicy` `storage.objects.list`  
  
#### Firebase Analytics Admin 

(`roles/firebase.analyticsAdmin`) Full access to Google Analytics for Firebase.  |  `cloudnotifications.activities.list` `firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseanalytics.*`

  * `firebaseanalytics.resources.googleAnalyticsEdit`
  * `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`

`firebaseextensions.configs.list` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list`  
  
#### Firebase Analytics Viewer 

(`roles/firebase.analyticsViewer`) Read access to Google Analytics for Firebase.  |  `cloudnotifications.activities.list` `firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze` `firebaseextensions.configs.list` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list`  
  
#### Firebase Develop Admin 

(`roles/firebase.developAdmin`) Full access to Firebase Develop products and Analytics.  |  `apikeys.keys.get` `apikeys.keys.getKeyString` `apikeys.keys.list` `apikeys.keys.lookup` `appengine.applications.get` `artifactregistry.attachments.get` `artifactregistry.attachments.list` `artifactregistry.dockerimages.*`

  * `artifactregistry.dockerimages.get`
  * `artifactregistry.dockerimages.list`

`artifactregistry.files.download` `artifactregistry.files.get` `artifactregistry.files.list` `artifactregistry.locations.*`

  * `artifactregistry.locations.get`
  * `artifactregistry.locations.list`

`artifactregistry.mavenartifacts.*`

  * `artifactregistry.mavenartifacts.get`
  * `artifactregistry.mavenartifacts.list`

`artifactregistry.npmpackages.*`

  * `artifactregistry.npmpackages.get`
  * `artifactregistry.npmpackages.list`

`artifactregistry.packages.get` `artifactregistry.packages.list` `artifactregistry.projectconfigs.get` `artifactregistry.projectsettings.get` `artifactregistry.pythonpackages.*`

  * `artifactregistry.pythonpackages.get`
  * `artifactregistry.pythonpackages.list`

`artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.exportArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.list` `artifactregistry.repositories.listEffectiveTags` `artifactregistry.repositories.listTagBindings` `artifactregistry.repositories.readViaVirtualRepository` `artifactregistry.rules.get` `artifactregistry.rules.list` `artifactregistry.tags.get` `artifactregistry.tags.list` `artifactregistry.versions.get` `artifactregistry.versions.list` `automl.*`

  * `automl.annotationSpecs.create`
  * `automl.annotationSpecs.delete`
  * `automl.annotationSpecs.get`
  * `automl.annotationSpecs.list`
  * `automl.annotationSpecs.update`
  * `automl.annotations.approve`
  * `automl.annotations.create`
  * `automl.annotations.list`
  * `automl.annotations.manipulate`
  * `automl.annotations.reject`
  * `automl.columnSpecs.get`
  * `automl.columnSpecs.list`
  * `automl.columnSpecs.update`
  * `automl.datasets.create`
  * `automl.datasets.delete`
  * `automl.datasets.export`
  * `automl.datasets.get`
  * `automl.datasets.getIamPolicy`
  * `automl.datasets.import`
  * `automl.datasets.list`
  * `automl.datasets.setIamPolicy`
  * `automl.datasets.update`
  * `automl.examples.delete`
  * `automl.examples.get`
  * `automl.examples.list`
  * `automl.examples.update`
  * `automl.files.delete`
  * `automl.files.list`
  * `automl.humanAnnotationTasks.create`
  * `automl.humanAnnotationTasks.delete`
  * `automl.humanAnnotationTasks.get`
  * `automl.humanAnnotationTasks.list`
  * `automl.locations.get`
  * `automl.locations.getIamPolicy`
  * `automl.locations.list`
  * `automl.locations.setIamPolicy`
  * `automl.modelEvaluations.create`
  * `automl.modelEvaluations.get`
  * `automl.modelEvaluations.list`
  * `automl.models.create`
  * `automl.models.delete`
  * `automl.models.deploy`
  * `automl.models.export`
  * `automl.models.get`
  * `automl.models.getIamPolicy`
  * `automl.models.list`
  * `automl.models.predict`
  * `automl.models.setIamPolicy`
  * `automl.models.undeploy`
  * `automl.operations.cancel`
  * `automl.operations.delete`
  * `automl.operations.get`
  * `automl.operations.list`
  * `automl.tableSpecs.get`
  * `automl.tableSpecs.list`
  * `automl.tableSpecs.update`

`clientauthconfig.brands.get` `clientauthconfig.brands.list` `clientauthconfig.brands.update` `clientauthconfig.clients.get` `clientauthconfig.clients.list` `cloudaicompanion.instances.completeTask` `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudfunctions.*`

  * `cloudfunctions.functions.call`
  * `cloudfunctions.functions.create`
  * `cloudfunctions.functions.delete`
  * `cloudfunctions.functions.generationUpgrade`
  * `cloudfunctions.functions.get`
  * `cloudfunctions.functions.getIamPolicy`
  * `cloudfunctions.functions.invoke`
  * `cloudfunctions.functions.list`
  * `cloudfunctions.functions.setIamPolicy`
  * `cloudfunctions.functions.sourceCodeGet`
  * `cloudfunctions.functions.sourceCodeSet`
  * `cloudfunctions.functions.update`
  * `cloudfunctions.locations.list`
  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `cloudnotifications.activities.list` `databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.studioQueries.*`

  * `databasesconsole.studioQueries.create`
  * `databasesconsole.studioQueries.delete`
  * `databasesconsole.studioQueries.get`
  * `databasesconsole.studioQueries.list`
  * `databasesconsole.studioQueries.search`
  * `databasesconsole.studioQueries.update`

`datastore.*`

  * `datastore.backupSchedules.create`
  * `datastore.backupSchedules.delete`
  * `datastore.backupSchedules.get`
  * `datastore.backupSchedules.list`
  * `datastore.backupSchedules.update`
  * `datastore.backups.delete`
  * `datastore.backups.get`
  * `datastore.backups.list`
  * `datastore.backups.restoreDatabase`
  * `datastore.databases.bulkDelete`
  * `datastore.databases.clone`
  * `datastore.databases.create`
  * `datastore.databases.createTagBinding`
  * `datastore.databases.delete`
  * `datastore.databases.deleteTagBinding`
  * `datastore.databases.export`
  * `datastore.databases.get`
  * `datastore.databases.getMetadata`
  * `datastore.databases.import`
  * `datastore.databases.list`
  * `datastore.databases.listEffectiveTags`
  * `datastore.databases.listTagBindings`
  * `datastore.databases.update`
  * `datastore.entities.allocateIds`
  * `datastore.entities.create`
  * `datastore.entities.delete`
  * `datastore.entities.get`
  * `datastore.entities.list`
  * `datastore.entities.update`
  * `datastore.insights.get`
  * `datastore.keyVisualizerScans.get`
  * `datastore.keyVisualizerScans.list`
  * `datastore.locations.get`
  * `datastore.locations.list`
  * `datastore.namespaces.get`
  * `datastore.namespaces.list`
  * `datastore.operations.cancel`
  * `datastore.operations.delete`
  * `datastore.operations.get`
  * `datastore.operations.list`
  * `datastore.schemas.create`
  * `datastore.schemas.delete`
  * `datastore.schemas.get`
  * `datastore.schemas.list`
  * `datastore.schemas.update`
  * `datastore.statistics.get`
  * `datastore.statistics.list`
  * `datastore.userCreds.create`
  * `datastore.userCreds.delete`
  * `datastore.userCreds.get`
  * `datastore.userCreds.list`
  * `datastore.userCreds.update`

`errorreporting.groups.list` `eventarc.*`

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

`firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseanalytics.*`

  * `firebaseanalytics.resources.googleAnalyticsEdit`
  * `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`

`firebaseappcheck.*`

  * `firebaseappcheck.appAttestConfig.get`
  * `firebaseappcheck.appAttestConfig.update`
  * `firebaseappcheck.appCheckTokens.verify`
  * `firebaseappcheck.automations.create`
  * `firebaseappcheck.automations.delete`
  * `firebaseappcheck.automations.get`
  * `firebaseappcheck.automations.list`
  * `firebaseappcheck.automations.resume`
  * `firebaseappcheck.automations.suspend`
  * `firebaseappcheck.automations.update`
  * `firebaseappcheck.debugTokens.get`
  * `firebaseappcheck.debugTokens.update`
  * `firebaseappcheck.deviceCheckConfig.get`
  * `firebaseappcheck.deviceCheckConfig.update`
  * `firebaseappcheck.playIntegrityConfig.get`
  * `firebaseappcheck.playIntegrityConfig.update`
  * `firebaseappcheck.recaptchaEnterpriseConfig.get`
  * `firebaseappcheck.recaptchaEnterpriseConfig.update`
  * `firebaseappcheck.recaptchaV3Config.get`
  * `firebaseappcheck.recaptchaV3Config.update`
  * `firebaseappcheck.resourcePolicies.get`
  * `firebaseappcheck.resourcePolicies.update`
  * `firebaseappcheck.safetyNetConfig.get`
  * `firebaseappcheck.safetyNetConfig.update`
  * `firebaseappcheck.services.get`
  * `firebaseappcheck.services.update`
  * `firebaseappcheck.tokens.mint`

`firebaseapphosting.*`

  * `firebaseapphosting.backends.create`
  * `firebaseapphosting.backends.delete`
  * `firebaseapphosting.backends.get`
  * `firebaseapphosting.backends.list`
  * `firebaseapphosting.backends.update`
  * `firebaseapphosting.builds.create`
  * `firebaseapphosting.builds.delete`
  * `firebaseapphosting.builds.get`
  * `firebaseapphosting.builds.list`
  * `firebaseapphosting.builds.update`
  * `firebaseapphosting.domains.create`
  * `firebaseapphosting.domains.delete`
  * `firebaseapphosting.domains.get`
  * `firebaseapphosting.domains.list`
  * `firebaseapphosting.domains.update`
  * `firebaseapphosting.locations.get`
  * `firebaseapphosting.locations.list`
  * `firebaseapphosting.operations.cancel`
  * `firebaseapphosting.operations.delete`
  * `firebaseapphosting.operations.get`
  * `firebaseapphosting.operations.list`
  * `firebaseapphosting.rollouts.create`
  * `firebaseapphosting.rollouts.delete`
  * `firebaseapphosting.rollouts.get`
  * `firebaseapphosting.rollouts.list`
  * `firebaseapphosting.rollouts.update`
  * `firebaseapphosting.traffic.get`
  * `firebaseapphosting.traffic.update`

`firebaseauth.*`

  * `firebaseauth.configs.create`
  * `firebaseauth.configs.get`
  * `firebaseauth.configs.getHashConfig`
  * `firebaseauth.configs.getSecret`
  * `firebaseauth.configs.update`
  * `firebaseauth.users.create`
  * `firebaseauth.users.createSession`
  * `firebaseauth.users.delete`
  * `firebaseauth.users.get`
  * `firebaseauth.users.sendEmail`
  * `firebaseauth.users.update`

`firebasedatabase.*`

  * `firebasedatabase.instances.create`
  * `firebasedatabase.instances.delete`
  * `firebasedatabase.instances.disable`
  * `firebasedatabase.instances.get`
  * `firebasedatabase.instances.list`
  * `firebasedatabase.instances.reenable`
  * `firebasedatabase.instances.undelete`
  * `firebasedatabase.instances.update`

`firebasedataconnect.*`

  * `firebasedataconnect.connectorRevisions.delete`
  * `firebasedataconnect.connectorRevisions.get`
  * `firebasedataconnect.connectorRevisions.list`
  * `firebasedataconnect.connectors.create`
  * `firebasedataconnect.connectors.delete`
  * `firebasedataconnect.connectors.get`
  * `firebasedataconnect.connectors.impersonateMutation`
  * `firebasedataconnect.connectors.impersonateQuery`
  * `firebasedataconnect.connectors.list`
  * `firebasedataconnect.connectors.update`
  * `firebasedataconnect.locations.get`
  * `firebasedataconnect.locations.list`
  * `firebasedataconnect.operations.cancel`
  * `firebasedataconnect.operations.delete`
  * `firebasedataconnect.operations.get`
  * `firebasedataconnect.operations.list`
  * `firebasedataconnect.schemaRevisions.delete`
  * `firebasedataconnect.schemaRevisions.get`
  * `firebasedataconnect.schemaRevisions.list`
  * `firebasedataconnect.schemas.create`
  * `firebasedataconnect.schemas.delete`
  * `firebasedataconnect.schemas.get`
  * `firebasedataconnect.schemas.list`
  * `firebasedataconnect.schemas.migrate`
  * `firebasedataconnect.schemas.update`
  * `firebasedataconnect.services.create`
  * `firebasedataconnect.services.delete`
  * `firebasedataconnect.services.executeGraphql`
  * `firebasedataconnect.services.executeGraphqlRead`
  * `firebasedataconnect.services.generateQuery`
  * `firebasedataconnect.services.generateSchema`
  * `firebasedataconnect.services.get`
  * `firebasedataconnect.services.introspectGraphql`
  * `firebasedataconnect.services.list`
  * `firebasedataconnect.services.update`

`firebaseextensions.configs.list` `firebasehosting.*`

  * `firebasehosting.sites.create`
  * `firebasehosting.sites.delete`
  * `firebasehosting.sites.get`
  * `firebasehosting.sites.list`
  * `firebasehosting.sites.update`

`firebaseml.*`

  * `firebaseml.models.create`
  * `firebaseml.models.delete`
  * `firebaseml.models.get`
  * `firebaseml.models.list`
  * `firebaseml.models.update`
  * `firebaseml.modelversions.create`
  * `firebaseml.modelversions.get`
  * `firebaseml.modelversions.list`
  * `firebaseml.modelversions.update`

`firebaserules.*`

  * `firebaserules.releases.create`
  * `firebaserules.releases.delete`
  * `firebaserules.releases.get`
  * `firebaserules.releases.getExecutable`
  * `firebaserules.releases.list`
  * `firebaserules.releases.update`
  * `firebaserules.rulesets.create`
  * `firebaserules.rulesets.delete`
  * `firebaserules.rulesets.get`
  * `firebaserules.rulesets.list`
  * `firebaserules.rulesets.test`

`firebasestorage.*`

  * `firebasestorage.buckets.addFirebase`
  * `firebasestorage.buckets.get`
  * `firebasestorage.buckets.list`
  * `firebasestorage.buckets.removeFirebase`
  * `firebasestorage.defaultBucket.create`
  * `firebasestorage.defaultBucket.delete`
  * `firebasestorage.defaultBucket.get`

`firebasevertexai.*`

  * `firebasevertexai.configs.get`
  * `firebasevertexai.configs.update`
  * `firebasevertexai.promptTemplates.create`
  * `firebasevertexai.promptTemplates.delete`
  * `firebasevertexai.promptTemplates.get`
  * `firebasevertexai.promptTemplates.list`
  * `firebasevertexai.promptTemplates.update`
  * `firebasevertexai.promptTemplates.updateLock`

`logging.logEntries.list` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`oauthconfig.verification.get` `orgpolicy.policy.get` `recommender.cloudFunctionsPerformanceInsights.*`

  * `recommender.cloudFunctionsPerformanceInsights.get`
  * `recommender.cloudFunctionsPerformanceInsights.list`
  * `recommender.cloudFunctionsPerformanceInsights.update`

`recommender.cloudFunctionsPerformanceRecommendations.*`

  * `recommender.cloudFunctionsPerformanceRecommendations.get`
  * `recommender.cloudFunctionsPerformanceRecommendations.list`
  * `recommender.cloudFunctionsPerformanceRecommendations.update`

`recommender.iamPolicyInsights.*`

  * `recommender.iamPolicyInsights.get`
  * `recommender.iamPolicyInsights.list`
  * `recommender.iamPolicyInsights.update`

`recommender.iamPolicyRecommendations.*`

  * `recommender.iamPolicyRecommendations.get`
  * `recommender.iamPolicyRecommendations.list`
  * `recommender.iamPolicyRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.*`

  * `recommender.runServiceCostInsights.get`
  * `recommender.runServiceCostInsights.list`
  * `recommender.runServiceCostInsights.update`

`recommender.runServiceCostRecommendations.*`

  * `recommender.runServiceCostRecommendations.get`
  * `recommender.runServiceCostRecommendations.list`
  * `recommender.runServiceCostRecommendations.update`

`recommender.runServiceIdentityInsights.*`

  * `recommender.runServiceIdentityInsights.get`
  * `recommender.runServiceIdentityInsights.list`
  * `recommender.runServiceIdentityInsights.update`

`recommender.runServiceIdentityRecommendations.*`

  * `recommender.runServiceIdentityRecommendations.get`
  * `recommender.runServiceIdentityRecommendations.list`
  * `recommender.runServiceIdentityRecommendations.update`

`recommender.runServicePerformanceInsights.*`

  * `recommender.runServicePerformanceInsights.get`
  * `recommender.runServicePerformanceInsights.list`
  * `recommender.runServicePerformanceInsights.update`

`recommender.runServicePerformanceRecommendations.*`

  * `recommender.runServicePerformanceRecommendations.get`
  * `recommender.runServicePerformanceRecommendations.list`
  * `recommender.runServicePerformanceRecommendations.update`

`recommender.runServiceSecurityInsights.*`

  * `recommender.runServiceSecurityInsights.get`
  * `recommender.runServiceSecurityInsights.list`
  * `recommender.runServiceSecurityInsights.update`

`recommender.runServiceSecurityRecommendations.*`

  * `recommender.runServiceSecurityRecommendations.get`
  * `recommender.runServiceSecurityRecommendations.list`
  * `recommender.runServiceSecurityRecommendations.update`

`recommender.storageBucketSoftDeleteInsights.*`

  * `recommender.storageBucketSoftDeleteInsights.get`
  * `recommender.storageBucketSoftDeleteInsights.list`
  * `recommender.storageBucketSoftDeleteInsights.update`

`recommender.storageBucketSoftDeleteRecommendations.*`

  * `recommender.storageBucketSoftDeleteRecommendations.get`
  * `recommender.storageBucketSoftDeleteRecommendations.list`
  * `recommender.storageBucketSoftDeleteRecommendations.update`

`remotebuildexecution.blobs.get` `resourcemanager.hierarchyNodes.listEffectiveTags` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `run.*`

  * `run.configurations.get`
  * `run.configurations.list`
  * `run.executions.cancel`
  * `run.executions.delete`
  * `run.executions.get`
  * `run.executions.list`
  * `run.instances.create`
  * `run.instances.delete`
  * `run.instances.get`
  * `run.instances.getIamPolicy`
  * `run.instances.invoke`
  * `run.instances.list`
  * `run.instances.setIamPolicy`
  * `run.instances.sshRead`
  * `run.instances.sshRoot`
  * `run.instances.start`
  * `run.instances.stop`
  * `run.instances.update`
  * `run.jobs.create`
  * `run.jobs.createTagBinding`
  * `run.jobs.delete`
  * `run.jobs.deleteTagBinding`
  * `run.jobs.get`
  * `run.jobs.getIamPolicy`
  * `run.jobs.list`
  * `run.jobs.listEffectiveTags`
  * `run.jobs.listTagBindings`
  * `run.jobs.run`
  * `run.jobs.runWithOverrides`
  * `run.jobs.setIamPolicy`
  * `run.jobs.sshRead`
  * `run.jobs.sshRoot`
  * `run.jobs.update`
  * `run.locations.list`
  * `run.locations.uploadSource`
  * `run.operations.delete`
  * `run.operations.get`
  * `run.operations.list`
  * `run.prompts.get`
  * `run.revisions.delete`
  * `run.revisions.get`
  * `run.revisions.list`
  * `run.routes.get`
  * `run.routes.invoke`
  * `run.routes.list`
  * `run.services.create`
  * `run.services.createTagBinding`
  * `run.services.delete`
  * `run.services.deleteTagBinding`
  * `run.services.get`
  * `run.services.getIamPolicy`
  * `run.services.list`
  * `run.services.listEffectiveTags`
  * `run.services.listTagBindings`
  * `run.services.setIamPolicy`
  * `run.services.sshRead`
  * `run.services.sshRoot`
  * `run.services.update`
  * `run.tasks.get`
  * `run.tasks.list`
  * `run.workerpools.create`
  * `run.workerpools.delete`
  * `run.workerpools.get`
  * `run.workerpools.getIamPolicy`
  * `run.workerpools.list`
  * `run.workerpools.setIamPolicy`
  * `run.workerpools.sshRead`
  * `run.workerpools.sshRoot`
  * `run.workerpools.update`

`runtimeconfig.configs.create` `runtimeconfig.configs.delete` `runtimeconfig.configs.get` `runtimeconfig.configs.list` `runtimeconfig.configs.update` `runtimeconfig.operations.*`

  * `runtimeconfig.operations.get`
  * `runtimeconfig.operations.list`

`runtimeconfig.variables.create` `runtimeconfig.variables.delete` `runtimeconfig.variables.get` `runtimeconfig.variables.list` `runtimeconfig.variables.update` `runtimeconfig.variables.watch` `runtimeconfig.waiters.create` `runtimeconfig.waiters.delete` `runtimeconfig.waiters.get` `runtimeconfig.waiters.list` `runtimeconfig.waiters.update` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `stackdriver.projects.get` `stackdriver.resourceMetadata.list` `storage.anywhereCaches.*`

  * `storage.anywhereCaches.create`
  * `storage.anywhereCaches.disable`
  * `storage.anywhereCaches.get`
  * `storage.anywhereCaches.list`
  * `storage.anywhereCaches.pause`
  * `storage.anywhereCaches.resume`
  * `storage.anywhereCaches.update`

`storage.bucketOperations.*`

  * `storage.bucketOperations.cancel`
  * `storage.bucketOperations.get`
  * `storage.bucketOperations.list`

`storage.buckets.*`

  * `storage.buckets.create`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.delete`
  * `storage.buckets.deleteTagBinding`
  * `storage.buckets.enableObjectRetention`
  * `storage.buckets.get`
  * `storage.buckets.getIamPolicy`
  * `storage.buckets.getIpFilter`
  * `storage.buckets.getObjectInsights`
  * `storage.buckets.list`
  * `storage.buckets.listEffectiveTags`
  * `storage.buckets.listTagBindings`
  * `storage.buckets.relocate`
  * `storage.buckets.restore`
  * `storage.buckets.setIamPolicy`
  * `storage.buckets.setIpFilter`
  * `storage.buckets.update`
  * `storage.buckets.viewIntelligenceDetails`
  * `storage.buckets.viewSecurityIntelligenceDetails`

`storage.featureConfigs.*`

  * `storage.featureConfigs.create`
  * `storage.featureConfigs.delete`
  * `storage.featureConfigs.get`
  * `storage.featureConfigs.list`
  * `storage.featureConfigs.update`

`storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.intelligenceConfigs.*`

  * `storage.intelligenceConfigs.get`
  * `storage.intelligenceConfigs.update`

`storage.managedFolders.*`

  * `storage.managedFolders.create`
  * `storage.managedFolders.delete`
  * `storage.managedFolders.get`
  * `storage.managedFolders.getIamPolicy`
  * `storage.managedFolders.list`
  * `storage.managedFolders.setIamPolicy`
  * `storage.managedFolders.update`

`storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

`storagebatchoperations.*`

  * `storagebatchoperations.bucketOperations.get`
  * `storagebatchoperations.bucketOperations.list`
  * `storagebatchoperations.jobs.cancel`
  * `storagebatchoperations.jobs.create`
  * `storagebatchoperations.jobs.delete`
  * `storagebatchoperations.jobs.get`
  * `storagebatchoperations.jobs.list`
  * `storagebatchoperations.locations.get`
  * `storagebatchoperations.locations.list`
  * `storagebatchoperations.operations.cancel`
  * `storagebatchoperations.operations.delete`
  * `storagebatchoperations.operations.get`
  * `storagebatchoperations.operations.list`

  
  
#### Firebase Develop Viewer 

(`roles/firebase.developViewer`) Read access to Firebase Develop products and Analytics.  |  `apikeys.keys.get` `apikeys.keys.list` `automl.annotationSpecs.get` `automl.annotationSpecs.list` `automl.annotations.list` `automl.columnSpecs.get` `automl.columnSpecs.list` `automl.datasets.get` `automl.datasets.list` `automl.examples.get` `automl.examples.list` `automl.files.list` `automl.humanAnnotationTasks.get` `automl.humanAnnotationTasks.list` `automl.locations.get` `automl.locations.list` `automl.modelEvaluations.get` `automl.modelEvaluations.list` `automl.models.get` `automl.models.list` `automl.operations.get` `automl.operations.list` `automl.tableSpecs.get` `automl.tableSpecs.list` `clientauthconfig.brands.get` `clientauthconfig.brands.list` `cloudasset.assets.searchAllResources` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.locations.*`

  * `cloudbuild.locations.get`
  * `cloudbuild.locations.list`

`cloudbuild.operations.*`

  * `cloudbuild.operations.get`
  * `cloudbuild.operations.list`

`cloudfunctions.functions.get` `cloudfunctions.functions.getIamPolicy` `cloudfunctions.functions.list` `cloudfunctions.locations.list` `cloudfunctions.operations.*`

  * `cloudfunctions.operations.get`
  * `cloudfunctions.operations.list`

`cloudnotifications.activities.list` `datastore.backups.get` `datastore.backups.list` `datastore.databases.get` `datastore.databases.getMetadata` `datastore.databases.list` `datastore.entities.get` `datastore.entities.list` `datastore.namespaces.*`

  * `datastore.namespaces.get`
  * `datastore.namespaces.list`

`datastore.schemas.get` `datastore.schemas.list` `datastore.statistics.*`

  * `datastore.statistics.get`
  * `datastore.statistics.list`

`datastore.userCreds.get` `datastore.userCreds.list` `errorreporting.groups.list` `eventarc.channelConnections.get` `eventarc.channelConnections.getIamPolicy` `eventarc.channelConnections.list` `eventarc.channelConnections.listEffectiveTags` `eventarc.channelConnections.listTagBindings` `eventarc.channels.get` `eventarc.channels.getIamPolicy` `eventarc.channels.list` `eventarc.channels.listEffectiveTags` `eventarc.channels.listTagBindings` `eventarc.enrollments.get` `eventarc.enrollments.getIamPolicy` `eventarc.enrollments.list` `eventarc.googleApiSources.get` `eventarc.googleApiSources.getIamPolicy` `eventarc.googleApiSources.list` `eventarc.googleChannelConfigs.get` `eventarc.kafkaSources.get` `eventarc.kafkaSources.getIamPolicy` `eventarc.kafkaSources.list` `eventarc.locations.*`

  * `eventarc.locations.get`
  * `eventarc.locations.list`

`eventarc.messageBuses.get` `eventarc.messageBuses.getIamPolicy` `eventarc.messageBuses.list` `eventarc.messageBuses.use` `eventarc.multiProjectSources.collectGoogleApiEvents` `eventarc.operations.get` `eventarc.operations.list` `eventarc.pipelines.get` `eventarc.pipelines.getIamPolicy` `eventarc.pipelines.list` `eventarc.providers.*`

  * `eventarc.providers.get`
  * `eventarc.providers.list`

`eventarc.triggers.get` `eventarc.triggers.getIamPolicy` `eventarc.triggers.list` `eventarc.triggers.listEffectiveTags` `eventarc.triggers.listTagBindings` `firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze` `firebaseappcheck.appAttestConfig.get` `firebaseappcheck.automations.get` `firebaseappcheck.automations.list` `firebaseappcheck.debugTokens.get` `firebaseappcheck.deviceCheckConfig.get` `firebaseappcheck.playIntegrityConfig.get` `firebaseappcheck.recaptchaEnterpriseConfig.get` `firebaseappcheck.recaptchaV3Config.get` `firebaseappcheck.resourcePolicies.get` `firebaseappcheck.safetyNetConfig.get` `firebaseappcheck.services.get` `firebaseapphosting.backends.get` `firebaseapphosting.backends.list` `firebaseapphosting.builds.get` `firebaseapphosting.builds.list` `firebaseapphosting.domains.get` `firebaseapphosting.domains.list` `firebaseapphosting.locations.*`

  * `firebaseapphosting.locations.get`
  * `firebaseapphosting.locations.list`

`firebaseapphosting.operations.get` `firebaseapphosting.operations.list` `firebaseapphosting.rollouts.get` `firebaseapphosting.rollouts.list` `firebaseapphosting.traffic.get` `firebaseauth.configs.get` `firebaseauth.users.get` `firebasedatabase.instances.get` `firebasedatabase.instances.list` `firebasedataconnect.connectorRevisions.get` `firebasedataconnect.connectorRevisions.list` `firebasedataconnect.connectors.get` `firebasedataconnect.connectors.list` `firebasedataconnect.locations.*`

  * `firebasedataconnect.locations.get`
  * `firebasedataconnect.locations.list`

`firebasedataconnect.operations.get` `firebasedataconnect.operations.list` `firebasedataconnect.schemaRevisions.get` `firebasedataconnect.schemaRevisions.list` `firebasedataconnect.schemas.get` `firebasedataconnect.schemas.list` `firebasedataconnect.services.generateQuery` `firebasedataconnect.services.generateSchema` `firebasedataconnect.services.get` `firebasedataconnect.services.introspectGraphql` `firebasedataconnect.services.list` `firebaseextensions.configs.list` `firebasehosting.sites.get` `firebasehosting.sites.list` `firebaseml.models.get` `firebaseml.models.list` `firebaseml.modelversions.get` `firebaseml.modelversions.list` `firebaserules.releases.get` `firebaserules.releases.getExecutable` `firebaserules.releases.list` `firebaserules.rulesets.get` `firebaserules.rulesets.list` `firebasestorage.buckets.get` `firebasestorage.buckets.list` `firebasestorage.defaultBucket.get` `firebasevertexai.configs.get` `firebasevertexai.promptTemplates.get` `firebasevertexai.promptTemplates.list` `logging.logEntries.list` `monitoring.timeSeries.list` `oauthconfig.verification.get` `recommender.cloudFunctionsPerformanceInsights.get` `recommender.cloudFunctionsPerformanceInsights.list` `recommender.cloudFunctionsPerformanceRecommendations.get` `recommender.cloudFunctionsPerformanceRecommendations.list` `recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.runServiceCostInsights.get` `recommender.runServiceCostInsights.list` `recommender.runServiceCostRecommendations.get` `recommender.runServiceCostRecommendations.list` `recommender.runServiceIdentityInsights.get` `recommender.runServiceIdentityInsights.list` `recommender.runServiceIdentityRecommendations.get` `recommender.runServiceIdentityRecommendations.list` `recommender.runServicePerformanceInsights.get` `recommender.runServicePerformanceInsights.list` `recommender.runServicePerformanceRecommendations.get` `recommender.runServicePerformanceRecommendations.list` `recommender.runServiceSecurityInsights.get` `recommender.runServiceSecurityInsights.list` `recommender.runServiceSecurityRecommendations.get` `recommender.runServiceSecurityRecommendations.list` `remotebuildexecution.blobs.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `run.configurations.*`

  * `run.configurations.get`
  * `run.configurations.list`

`run.executions.get` `run.executions.list` `run.instances.get` `run.instances.getIamPolicy` `run.instances.list` `run.jobs.get` `run.jobs.getIamPolicy` `run.jobs.list` `run.jobs.listEffectiveTags` `run.jobs.listTagBindings` `run.locations.list` `run.operations.get` `run.operations.list` `run.prompts.get` `run.revisions.get` `run.revisions.list` `run.routes.get` `run.routes.list` `run.services.get` `run.services.getIamPolicy` `run.services.list` `run.services.listEffectiveTags` `run.services.listTagBindings` `run.tasks.*`

  * `run.tasks.get`
  * `run.tasks.list`

`run.workerpools.get` `run.workerpools.getIamPolicy` `run.workerpools.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list` `storage.objects.get` `storage.objects.getIamPolicy` `storage.objects.list`  
  
#### Firebase Grow Admin 

(`roles/firebase.growthAdmin`) Full access to Firebase Grow products and Analytics.  |  `apikeys.keys.get` `apikeys.keys.list` `clientauthconfig.clients.get` `clientauthconfig.clients.list` `cloudconfig.*`

  * `cloudconfig.configs.get`
  * `cloudconfig.configs.update`

`cloudmessaging.*`

  * `cloudmessaging.messages.create`
  * `cloudmessaging.topicSubscriptions.create`
  * `cloudmessaging.topicSubscriptions.delete`
  * `cloudmessaging.topicSubscriptions.get`
  * `cloudmessaging.topicSubscriptions.list`
  * `cloudmessaging.topicSubscriptions.update`

`cloudnotifications.activities.list` `fcmdata.deliverydata.list` `firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseabt.*`

  * `firebaseabt.experimentresults.get`
  * `firebaseabt.experiments.create`
  * `firebaseabt.experiments.delete`
  * `firebaseabt.experiments.get`
  * `firebaseabt.experiments.list`
  * `firebaseabt.experiments.update`
  * `firebaseabt.projectmetadata.get`

`firebaseanalytics.*`

  * `firebaseanalytics.resources.googleAnalyticsEdit`
  * `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`

`firebasedynamiclinks.*`

  * `firebasedynamiclinks.destinations.list`
  * `firebasedynamiclinks.destinations.update`
  * `firebasedynamiclinks.domains.create`
  * `firebasedynamiclinks.domains.delete`
  * `firebasedynamiclinks.domains.get`
  * `firebasedynamiclinks.domains.list`
  * `firebasedynamiclinks.domains.update`
  * `firebasedynamiclinks.links.create`
  * `firebasedynamiclinks.links.get`
  * `firebasedynamiclinks.links.list`
  * `firebasedynamiclinks.links.update`
  * `firebasedynamiclinks.stats.get`

`firebaseextensions.configs.list` `firebaseinappmessaging.*`

  * `firebaseinappmessaging.campaigns.create`
  * `firebaseinappmessaging.campaigns.delete`
  * `firebaseinappmessaging.campaigns.get`
  * `firebaseinappmessaging.campaigns.list`
  * `firebaseinappmessaging.campaigns.update`

`firebasemessagingcampaigns.*`

  * `firebasemessagingcampaigns.campaigns.create`
  * `firebasemessagingcampaigns.campaigns.delete`
  * `firebasemessagingcampaigns.campaigns.get`
  * `firebasemessagingcampaigns.campaigns.list`
  * `firebasemessagingcampaigns.campaigns.start`
  * `firebasemessagingcampaigns.campaigns.stop`
  * `firebasemessagingcampaigns.campaigns.update`

`firebasenotifications.*`

  * `firebasenotifications.messages.create`
  * `firebasenotifications.messages.delete`
  * `firebasenotifications.messages.get`
  * `firebasenotifications.messages.list`
  * `firebasenotifications.messages.update`

`monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Firebase Grow Viewer 

(`roles/firebase.growthViewer`) Read access to Firebase Grow products and Analytics.  |  `apikeys.keys.get` `apikeys.keys.list` `cloudconfig.configs.get` `cloudmessaging.topicSubscriptions.get` `cloudmessaging.topicSubscriptions.list` `cloudnotifications.activities.list` `fcmdata.deliverydata.list` `firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseabt.experimentresults.get` `firebaseabt.experiments.get` `firebaseabt.experiments.list` `firebaseabt.projectmetadata.get` `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze` `firebasedynamiclinks.destinations.list` `firebasedynamiclinks.domains.get` `firebasedynamiclinks.domains.list` `firebasedynamiclinks.links.get` `firebasedynamiclinks.links.list` `firebasedynamiclinks.stats.get` `firebaseextensions.configs.list` `firebaseinappmessaging.campaigns.get` `firebaseinappmessaging.campaigns.list` `firebasemessagingcampaigns.campaigns.get` `firebasemessagingcampaigns.campaigns.list` `firebasenotifications.messages.get` `firebasenotifications.messages.list` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Firebase Quality Admin 

(`roles/firebase.qualityAdmin`) Full access to Firebase Quality products and Analytics.  |  `apikeys.keys.get` `apikeys.keys.list` `cloudnotifications.activities.list` `firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseanalytics.*`

  * `firebaseanalytics.resources.googleAnalyticsEdit`
  * `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`

`firebaseappdistro.*`

  * `firebaseappdistro.groups.list`
  * `firebaseappdistro.groups.update`
  * `firebaseappdistro.releases.list`
  * `firebaseappdistro.releases.update`
  * `firebaseappdistro.testers.list`
  * `firebaseappdistro.testers.update`

`firebasecrash.*`

  * `firebasecrash.issues.update`
  * `firebasecrash.reports.get`

`firebasecrashlytics.*`

  * `firebasecrashlytics.config.get`
  * `firebasecrashlytics.config.update`
  * `firebasecrashlytics.data.get`
  * `firebasecrashlytics.issues.get`
  * `firebasecrashlytics.issues.list`
  * `firebasecrashlytics.issues.update`
  * `firebasecrashlytics.sessions.get`

`firebaseextensions.configs.list` `firebaseperformance.*`

  * `firebaseperformance.config.update`
  * `firebaseperformance.data.get`

`logging.logEntries.download` `logging.views.access` `logging.views.listLogs` `logging.views.listResourceKeys` `logging.views.listResourceValues` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Firebase Quality Viewer 

(`roles/firebase.qualityViewer`) Read access to Firebase Quality products and Analytics.  |  `apikeys.keys.get` `apikeys.keys.list` `cloudnotifications.activities.list` `firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.links.list` `firebase.playLinks.get` `firebase.playLinks.list` `firebase.projects.get` `firebaseanalytics.resources.googleAnalyticsReadAndAnalyze` `firebaseappdistro.groups.list` `firebaseappdistro.releases.list` `firebaseappdistro.testers.list` `firebasecrash.reports.get` `firebasecrashlytics.config.get` `firebasecrashlytics.data.get` `firebasecrashlytics.issues.get` `firebasecrashlytics.issues.list` `firebasecrashlytics.sessions.get` `firebaseextensions.configs.list` `firebaseperformance.data.get` `logging.logEntries.download` `logging.views.access` `logging.views.listLogs` `logging.views.listResourceKeys` `logging.views.listResourceValues` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.contentsecuritypolicy.get` `serviceusage.effectivemcppolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.mcppolicy.get` `serviceusage.operations.get` `serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Firebase App Distribution Admin SDK Service Agent 

(`roles/firebase.appDistributionSdkServiceAgent`) Read and write access to Firebase App Distribution with the Admin SDK  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `firebaseappdistro.*`

  * `firebaseappdistro.groups.list`
  * `firebaseappdistro.groups.update`
  * `firebaseappdistro.releases.list`
  * `firebaseappdistro.releases.update`
  * `firebaseappdistro.testers.list`
  * `firebaseappdistro.testers.update`

  
  
#### Firebase Service Management Service Agent 

(`roles/firebase.managementServiceAgent`) Access to create new service agents for Firebase projects; assign roles to service agents; provision GCP resources as required by Firebase services.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `apikeys.keys.create` `apikeys.keys.get` `apikeys.keys.getKeyString` `apikeys.keys.list` `apikeys.keys.update` `appengine.applications.create` `appengine.applications.get` `appengine.applications.update` `appengine.operations.get` `appengine.services.list` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.datasets.getIamPolicy` `bigquery.datasets.setIamPolicy` `bigquery.datasets.update` `bigquery.transfers.*`

  * `bigquery.transfers.get`
  * `bigquery.transfers.update`

`clientauthconfig.brands.create` `clientauthconfig.brands.get` `clientauthconfig.brands.list` `clientauthconfig.brands.update` `clientauthconfig.clients.create` `clientauthconfig.clients.delete` `clientauthconfig.clients.get` `clientauthconfig.clients.getWithSecret` `clientauthconfig.clients.list` `clientauthconfig.clients.update` `datastore.databases.create` `datastore.databases.get` `datastore.databases.getMetadata` `datastore.databases.list` `datastore.databases.update` `datastore.locations.*`

  * `datastore.locations.get`
  * `datastore.locations.list`

`datastore.operations.get` `datastore.operations.list` `firebase.clients.create` `firebase.clients.delete` `firebase.clients.get` `firebase.clients.undelete` `firebase.clients.update` `firebase.projects.*`

  * `firebase.projects.delete`
  * `firebase.projects.get`
  * `firebase.projects.update`

`firebaseabt.experiments.delete` `firebaseappcheck.recaptchaEnterpriseConfig.*`

  * `firebaseappcheck.recaptchaEnterpriseConfig.get`
  * `firebaseappcheck.recaptchaEnterpriseConfig.update`

`firebaseappcheck.recaptchaV3Config.get` `firebaseappcheck.services.*`

  * `firebaseappcheck.services.get`
  * `firebaseappcheck.services.update`

`firebaseapphosting.domains.create` `firebaseapphosting.domains.get` `firebaseapphosting.domains.list` `firebaseapphosting.domains.update` `firebaseauth.configs.create` `firebaseauth.configs.get` `firebaseauth.configs.update` `firebasedataconnect.locations.*`

  * `firebasedataconnect.locations.get`
  * `firebasedataconnect.locations.list`

`firebasedataconnect.operations.get` `firebasedataconnect.operations.list` `firebasedataconnect.services.create` `firebasehosting.sites.create` `firebasehosting.sites.get` `firebasehosting.sites.list` `firebasehosting.sites.update` `firebaserules.releases.create` `firebaserules.releases.delete` `firebaserules.releases.get` `firebaserules.releases.list` `firebaserules.releases.update` `firebaserules.rulesets.create` `firebaserules.rulesets.get` `firebaserules.rulesets.list` `firebasestorage.defaultBucket.get` `firebasevertexai.configs.*`

  * `firebasevertexai.configs.get`
  * `firebasevertexai.configs.update`

`iam.roles.get` `iam.serviceAccounts.create` `iam.serviceAccounts.get` `iam.serviceAccounts.list` `recaptchaenterprise.keys.create` `recaptchaenterprise.keys.get` `recaptchaenterprise.keys.list` `recaptchaenterprise.keys.update` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.setIamPolicy` `resourcemanager.projects.update` `servicemanagement.services.bind` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `storage.bucketOperations.get` `storage.bucketOperations.list` `storage.buckets.create` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list` `storage.buckets.setIamPolicy` `storage.buckets.update`  
  
#### Firebase Admin SDK Administrator Service Agent 

(`roles/firebase.sdkAdminServiceAgent`) Read and write access to Firebase products available in the Admin SDK  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `appengine.applications.get` `cloudconfig.*`

  * `cloudconfig.configs.get`
  * `cloudconfig.configs.update`

`cloudmessaging.messages.create` `databasesconsole.locations.*`

  * `databasesconsole.locations.get`
  * `databasesconsole.locations.list`

`databasesconsole.studioQueries.create` `databasesconsole.studioQueries.delete` `databasesconsole.studioQueries.search` `databasesconsole.studioQueries.update` `datastore.backupSchedules.get` `datastore.backupSchedules.list` `datastore.backups.get` `datastore.backups.list` `datastore.databases.get` `datastore.databases.getMetadata` `datastore.databases.list` `datastore.databases.listEffectiveTags` `datastore.databases.listTagBindings` `datastore.entities.*`

  * `datastore.entities.allocateIds`
  * `datastore.entities.create`
  * `datastore.entities.delete`
  * `datastore.entities.get`
  * `datastore.entities.list`
  * `datastore.entities.update`

`datastore.insights.get` `datastore.keyVisualizerScans.*`

  * `datastore.keyVisualizerScans.get`
  * `datastore.keyVisualizerScans.list`

`datastore.namespaces.*`

  * `datastore.namespaces.get`
  * `datastore.namespaces.list`

`datastore.operations.get` `datastore.operations.list` `datastore.schemas.get` `datastore.schemas.list` `datastore.statistics.*`

  * `datastore.statistics.get`
  * `datastore.statistics.list`

`datastore.userCreds.get` `datastore.userCreds.list` `firebase.clients.*`

  * `firebase.clients.create`
  * `firebase.clients.delete`
  * `firebase.clients.get`
  * `firebase.clients.list`
  * `firebase.clients.undelete`
  * `firebase.clients.update`

`firebase.projects.get` `firebase.projects.update` `firebaseappcheck.*`

  * `firebaseappcheck.appAttestConfig.get`
  * `firebaseappcheck.appAttestConfig.update`
  * `firebaseappcheck.appCheckTokens.verify`
  * `firebaseappcheck.automations.create`
  * `firebaseappcheck.automations.delete`
  * `firebaseappcheck.automations.get`
  * `firebaseappcheck.automations.list`
  * `firebaseappcheck.automations.resume`
  * `firebaseappcheck.automations.suspend`
  * `firebaseappcheck.automations.update`
  * `firebaseappcheck.debugTokens.get`
  * `firebaseappcheck.debugTokens.update`
  * `firebaseappcheck.deviceCheckConfig.get`
  * `firebaseappcheck.deviceCheckConfig.update`
  * `firebaseappcheck.playIntegrityConfig.get`
  * `firebaseappcheck.playIntegrityConfig.update`
  * `firebaseappcheck.recaptchaEnterpriseConfig.get`
  * `firebaseappcheck.recaptchaEnterpriseConfig.update`
  * `firebaseappcheck.recaptchaV3Config.get`
  * `firebaseappcheck.recaptchaV3Config.update`
  * `firebaseappcheck.resourcePolicies.get`
  * `firebaseappcheck.resourcePolicies.update`
  * `firebaseappcheck.safetyNetConfig.get`
  * `firebaseappcheck.safetyNetConfig.update`
  * `firebaseappcheck.services.get`
  * `firebaseappcheck.services.update`
  * `firebaseappcheck.tokens.mint`

`firebaseauth.configs.create` `firebaseauth.configs.get` `firebaseauth.configs.getSecret` `firebaseauth.configs.update` `firebaseauth.users.*`

  * `firebaseauth.users.create`
  * `firebaseauth.users.createSession`
  * `firebaseauth.users.delete`
  * `firebaseauth.users.get`
  * `firebaseauth.users.sendEmail`
  * `firebaseauth.users.update`

`firebasedatabase.*`

  * `firebasedatabase.instances.create`
  * `firebasedatabase.instances.delete`
  * `firebasedatabase.instances.disable`
  * `firebasedatabase.instances.get`
  * `firebasedatabase.instances.list`
  * `firebasedatabase.instances.reenable`
  * `firebasedatabase.instances.undelete`
  * `firebasedatabase.instances.update`

`firebasedataconnect.connectorRevisions.*`

  * `firebasedataconnect.connectorRevisions.delete`
  * `firebasedataconnect.connectorRevisions.get`
  * `firebasedataconnect.connectorRevisions.list`

`firebasedataconnect.connectors.*`

  * `firebasedataconnect.connectors.create`
  * `firebasedataconnect.connectors.delete`
  * `firebasedataconnect.connectors.get`
  * `firebasedataconnect.connectors.impersonateMutation`
  * `firebasedataconnect.connectors.impersonateQuery`
  * `firebasedataconnect.connectors.list`
  * `firebasedataconnect.connectors.update`

`firebasedataconnect.locations.*`

  * `firebasedataconnect.locations.get`
  * `firebasedataconnect.locations.list`

`firebasedataconnect.operations.*`

  * `firebasedataconnect.operations.cancel`
  * `firebasedataconnect.operations.delete`
  * `firebasedataconnect.operations.get`
  * `firebasedataconnect.operations.list`

`firebasedataconnect.schemaRevisions.*`

  * `firebasedataconnect.schemaRevisions.delete`
  * `firebasedataconnect.schemaRevisions.get`
  * `firebasedataconnect.schemaRevisions.list`

`firebasedataconnect.schemas.create` `firebasedataconnect.schemas.delete` `firebasedataconnect.schemas.get` `firebasedataconnect.schemas.list` `firebasedataconnect.schemas.update` `firebasedataconnect.services.create` `firebasedataconnect.services.delete` `firebasedataconnect.services.executeGraphql` `firebasedataconnect.services.executeGraphqlRead` `firebasedataconnect.services.get` `firebasedataconnect.services.introspectGraphql` `firebasedataconnect.services.list` `firebasedataconnect.services.update` `firebasehosting.*`

  * `firebasehosting.sites.create`
  * `firebasehosting.sites.delete`
  * `firebasehosting.sites.get`
  * `firebasehosting.sites.list`
  * `firebasehosting.sites.update`

`firebaseml.*`

  * `firebaseml.models.create`
  * `firebaseml.models.delete`
  * `firebaseml.models.get`
  * `firebaseml.models.list`
  * `firebaseml.models.update`
  * `firebaseml.modelversions.create`
  * `firebaseml.modelversions.get`
  * `firebaseml.modelversions.list`
  * `firebaseml.modelversions.update`

`firebasenotifications.*`

  * `firebasenotifications.messages.create`
  * `firebasenotifications.messages.delete`
  * `firebasenotifications.messages.get`
  * `firebasenotifications.messages.list`
  * `firebasenotifications.messages.update`

`firebaserules.releases.get` `firebaserules.releases.list` `firebaserules.releases.update` `firebaserules.rulesets.create` `firebaserules.rulesets.delete` `firebaserules.rulesets.get` `firebaserules.rulesets.list` `identitytoolkit.*`

  * `identitytoolkit.tenants.create`
  * `identitytoolkit.tenants.delete`
  * `identitytoolkit.tenants.get`
  * `identitytoolkit.tenants.getIamPolicy`
  * `identitytoolkit.tenants.list`
  * `identitytoolkit.tenants.setIamPolicy`
  * `identitytoolkit.tenants.update`

`monitoring.timeSeries.create` `orgpolicy.policy.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `resourcemanager.projects.update` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.buckets.update` `storage.folders.*`

  * `storage.folders.create`
  * `storage.folders.delete`
  * `storage.folders.get`
  * `storage.folders.list`
  * `storage.folders.rename`

`storage.managedFolders.create` `storage.managedFolders.delete` `storage.managedFolders.get` `storage.managedFolders.list` `storage.managedFolders.update` `storage.multipartUploads.*`

  * `storage.multipartUploads.abort`
  * `storage.multipartUploads.create`
  * `storage.multipartUploads.list`
  * `storage.multipartUploads.listParts`

`storage.objects.*`

  * `storage.objects.create`
  * `storage.objects.createContext`
  * `storage.objects.delete`
  * `storage.objects.deleteContext`
  * `storage.objects.get`
  * `storage.objects.getIamPolicy`
  * `storage.objects.list`
  * `storage.objects.move`
  * `storage.objects.overrideUnlockedRetention`
  * `storage.objects.restore`
  * `storage.objects.setIamPolicy`
  * `storage.objects.setRetention`
  * `storage.objects.update`
  * `storage.objects.updateContext`

  
  
#### Firebase SDK Provisioning Service Agent 

(`roles/firebase.sdkProvisioningServiceAgent`) Access to provision apps with the Admin SDK.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `apikeys.keys.list` `clientauthconfig.clients.list` `cloudmessaging.messages.create` `firebase.clients.create` `servicemanagement.services.bind` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Firebase permissions

Permission | Included in roles  
---|---  
  
#### `firebase.billingPlans.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Firebase Analytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsAdmin) (`roles/firebase.analyticsAdmin`)  [Firebase Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsViewer) (`roles/firebase.analyticsViewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebase.billingPlans.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)   
  
#### `firebase.clients.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [OAuth Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Firebase SDK Provisioning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkProvisioningServiceAgent) (`roles/firebase.sdkProvisioningServiceAgent`) 

  
  
#### `firebase.clients.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebase.clients.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Remote Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.admin) (`roles/cloudconfig.admin`)  [Firebase Remote Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.viewer) (`roles/cloudconfig.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase A/B Testing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.viewer) (`roles/firebaseabt.viewer`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase App Distribution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.viewer) (`roles/firebaseappdistro.viewer`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Firebase Authentication Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.viewer) (`roles/firebaseauth.viewer`)  [Firebase Cloud Messaging API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.viewer) (`roles/firebasecloudmessaging.viewer`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Crashlytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.viewer) (`roles/firebasecrashlytics.viewer`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Realtime Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.viewer) (`roles/firebasedatabase.viewer`)  [Firebase Dynamic Links Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.admin) (`roles/firebasedynamiclinks.admin`)  [Firebasedynamiclinks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.editor) (`roles/firebasedynamiclinks.editor`)  [Firebase Dynamic Links Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.viewer) (`roles/firebasedynamiclinks.viewer`)  [Firebaseextensions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.editor) (`roles/firebaseextensions.editor`)  [Firebase Extensions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.viewer) (`roles/firebaseextensions.viewer`)  [Firebaseextensionspublisher Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.admin) (`roles/firebaseextensionspublisher.admin`)  [Firebaseextensionspublisher Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.viewer) (`roles/firebaseextensionspublisher.viewer`)  [Firebase Hosting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasehosting#firebasehosting.admin) (`roles/firebasehosting.admin`)  [Firebase Hosting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasehosting#firebasehosting.viewer) (`roles/firebasehosting.viewer`)  [Firebase In-App Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseinappmessaging#firebaseinappmessaging.admin) (`roles/firebaseinappmessaging.admin`)  [Firebase In-App Messaging Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseinappmessaging#firebaseinappmessaging.viewer) (`roles/firebaseinappmessaging.viewer`)  [Firebase ML Kit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseml#firebaseml.admin) (`roles/firebaseml.admin`)  [Firebase ML Kit Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseml#firebaseml.viewer) (`roles/firebaseml.viewer`)  [Firebase Cloud Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin) (`roles/firebasenotifications.admin`)  [Firebase Cloud Messaging Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.viewer) (`roles/firebasenotifications.viewer`)  [Firebase Performance Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseperformance#firebaseperformance.admin) (`roles/firebaseperformance.admin`)  [Firebase Performance Reporting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseperformance#firebaseperformance.viewer) (`roles/firebaseperformance.viewer`)  [Cloud Storage for Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.admin) (`roles/firebasestorage.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [OAuth Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`)  [OAuth Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.viewer) (`roles/oauthconfig.viewer`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Firebase Test Lab Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testViewer) (`roles/cloudtestservice.testViewer`)  [Firebase Analytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsAdmin) (`roles/firebase.analyticsAdmin`)  [Firebase Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsViewer) (`roles/firebase.analyticsViewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Firebase Crash Symbol Uploader](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrash.symbolMappingsAdmin) (`roles/firebasecrash.symbolMappingsAdmin`)  [Firebase Extensions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.developer) (`roles/firebaseextensions.developer`)  [Firebase Extensions Publisher - Extensions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.extensionsAdmin) (`roles/firebaseextensionspublisher.extensionsAdmin`)  [Firebase Extensions Publisher - Extensions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.extensionsViewer) (`roles/firebaseextensionspublisher.extensionsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebase.clients.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Remote Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.admin) (`roles/cloudconfig.admin`)  [Firebase Remote Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.viewer) (`roles/cloudconfig.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase A/B Testing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.viewer) (`roles/firebaseabt.viewer`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase App Distribution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.viewer) (`roles/firebaseappdistro.viewer`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Firebase Authentication Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.viewer) (`roles/firebaseauth.viewer`)  [Firebase Cloud Messaging API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.viewer) (`roles/firebasecloudmessaging.viewer`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Crashlytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.viewer) (`roles/firebasecrashlytics.viewer`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Realtime Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.viewer) (`roles/firebasedatabase.viewer`)  [Firebase Dynamic Links Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.admin) (`roles/firebasedynamiclinks.admin`)  [Firebasedynamiclinks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.editor) (`roles/firebasedynamiclinks.editor`)  [Firebase Dynamic Links Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.viewer) (`roles/firebasedynamiclinks.viewer`)  [Firebaseextensions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.editor) (`roles/firebaseextensions.editor`)  [Firebase Extensions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.viewer) (`roles/firebaseextensions.viewer`)  [Firebaseextensionspublisher Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.admin) (`roles/firebaseextensionspublisher.admin`)  [Firebaseextensionspublisher Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.viewer) (`roles/firebaseextensionspublisher.viewer`)  [Firebase Hosting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasehosting#firebasehosting.admin) (`roles/firebasehosting.admin`)  [Firebase Hosting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasehosting#firebasehosting.viewer) (`roles/firebasehosting.viewer`)  [Firebase In-App Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseinappmessaging#firebaseinappmessaging.admin) (`roles/firebaseinappmessaging.admin`)  [Firebase In-App Messaging Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseinappmessaging#firebaseinappmessaging.viewer) (`roles/firebaseinappmessaging.viewer`)  [Firebase ML Kit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseml#firebaseml.admin) (`roles/firebaseml.admin`)  [Firebase ML Kit Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseml#firebaseml.viewer) (`roles/firebaseml.viewer`)  [Firebase Cloud Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin) (`roles/firebasenotifications.admin`)  [Firebase Cloud Messaging Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.viewer) (`roles/firebasenotifications.viewer`)  [Firebase Performance Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseperformance#firebaseperformance.admin) (`roles/firebaseperformance.admin`)  [Firebase Performance Reporting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseperformance#firebaseperformance.viewer) (`roles/firebaseperformance.viewer`)  [Cloud Storage for Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.admin) (`roles/firebasestorage.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [OAuth Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`)  [OAuth Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.viewer) (`roles/oauthconfig.viewer`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Firebase Test Lab Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testViewer) (`roles/cloudtestservice.testViewer`)  [Firebase Analytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsAdmin) (`roles/firebase.analyticsAdmin`)  [Firebase Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsViewer) (`roles/firebase.analyticsViewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Firebase Crash Symbol Uploader](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrash.symbolMappingsAdmin) (`roles/firebasecrash.symbolMappingsAdmin`)  [Firebase Extensions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.developer) (`roles/firebaseextensions.developer`)  [Firebase Extensions Publisher - Extensions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.extensionsAdmin) (`roles/firebaseextensionspublisher.extensionsAdmin`)  [Firebase Extensions Publisher - Extensions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.extensionsViewer) (`roles/firebaseextensionspublisher.extensionsViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebase.clients.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebase.clients.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [OAuth Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/oauthconfig#oauthconfig.editor) (`roles/oauthconfig.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebase.links.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)   
  
#### `firebase.links.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)   
  
#### `firebase.links.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Analytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsAdmin) (`roles/firebase.analyticsAdmin`)  [Firebase Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsViewer) (`roles/firebase.analyticsViewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebase.links.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)   
  
#### `firebase.playLinks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Analytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsAdmin) (`roles/firebase.analyticsAdmin`)  [Firebase Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsViewer) (`roles/firebase.analyticsViewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebase.playLinks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Analytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsAdmin) (`roles/firebase.analyticsAdmin`)  [Firebase Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsViewer) (`roles/firebase.analyticsViewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebase.playLinks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)   
  
#### `firebase.projects.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 

  
  
#### `firebase.projects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Actions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/actions#actions.Admin) (`roles/actions.Admin`)  [Actions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/actions#actions.Viewer) (`roles/actions.Viewer`)  [Firebase Remote Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.admin) (`roles/cloudconfig.admin`)  [Firebase Remote Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.viewer) (`roles/cloudconfig.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase A/B Testing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.viewer) (`roles/firebaseabt.viewer`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase App Distribution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.viewer) (`roles/firebaseappdistro.viewer`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Firebase Authentication Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.viewer) (`roles/firebaseauth.viewer`)  [Firebase Cloud Messaging API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.viewer) (`roles/firebasecloudmessaging.viewer`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Crashlytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.viewer) (`roles/firebasecrashlytics.viewer`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Realtime Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.viewer) (`roles/firebasedatabase.viewer`)  [Firebase Dynamic Links Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.admin) (`roles/firebasedynamiclinks.admin`)  [Firebasedynamiclinks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.editor) (`roles/firebasedynamiclinks.editor`)  [Firebase Dynamic Links Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedynamiclinks#firebasedynamiclinks.viewer) (`roles/firebasedynamiclinks.viewer`)  [Firebaseextensions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.editor) (`roles/firebaseextensions.editor`)  [Firebase Extensions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.viewer) (`roles/firebaseextensions.viewer`)  [Firebaseextensionspublisher Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.admin) (`roles/firebaseextensionspublisher.admin`)  [Firebaseextensionspublisher Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.viewer) (`roles/firebaseextensionspublisher.viewer`)  [Firebase Hosting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasehosting#firebasehosting.admin) (`roles/firebasehosting.admin`)  [Firebase Hosting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasehosting#firebasehosting.viewer) (`roles/firebasehosting.viewer`)  [Firebase In-App Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseinappmessaging#firebaseinappmessaging.admin) (`roles/firebaseinappmessaging.admin`)  [Firebase In-App Messaging Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseinappmessaging#firebaseinappmessaging.viewer) (`roles/firebaseinappmessaging.viewer`)  [Firebase ML Kit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseml#firebaseml.admin) (`roles/firebaseml.admin`)  [Firebase ML Kit Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseml#firebaseml.viewer) (`roles/firebaseml.viewer`)  [Firebase Cloud Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin) (`roles/firebasenotifications.admin`)  [Firebase Cloud Messaging Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.viewer) (`roles/firebasenotifications.viewer`)  [Firebase Performance Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseperformance#firebaseperformance.admin) (`roles/firebaseperformance.admin`)  [Firebase Performance Reporting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseperformance#firebaseperformance.viewer) (`roles/firebaseperformance.viewer`)  [Cloud Storage for Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasestorage#firebasestorage.admin) (`roles/firebasestorage.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Firebase Test Lab Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testViewer) (`roles/cloudtestservice.testViewer`)  [Firebase Analytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsAdmin) (`roles/firebase.analyticsAdmin`)  [Firebase Analytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.analyticsViewer) (`roles/firebase.analyticsViewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Firebase Extensions Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensions#firebaseextensions.developer) (`roles/firebaseextensions.developer`)  [Firebase Extensions Publisher - Extensions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.extensionsAdmin) (`roles/firebaseextensionspublisher.extensionsAdmin`)  [Firebase Extensions Publisher - Extensions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseextensionspublisher#firebaseextensionspublisher.extensionsViewer) (`roles/firebaseextensionspublisher.extensionsViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Infrastructure Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.infrastructureAdmin) (`roles/iam.infrastructureAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage HMAC Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.hmacKeyAdmin) (`roles/storage.hmacKeyAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Cloud Composer API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.serviceAgent) (`roles/composer.serviceAgent`) 
  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Datapipelines Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datapipelines#datapipelines.serviceAgent) (`roles/datapipelines.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [DLP API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.serviceAgent) (`roles/dlp.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ml#ml.serviceAgent) (`roles/ml.serviceAgent`) 
  * [Visual Inspection AI Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/visualinspection#visualinspection.serviceAgent) (`roles/visualinspection.serviceAgent`) 

  
  
#### `firebase.projects.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Actions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/actions#actions.Admin) (`roles/actions.Admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
