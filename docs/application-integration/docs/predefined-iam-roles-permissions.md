---
url: https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions/
title: Predefined Application Integration IAM roles \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:28.709306+00:00
---

# Predefined Application Integration IAM roles  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/predefined-iam-roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Predefined Application Integration IAM roles

Predefined roles give granular access to specific Google Cloud resources. These roles are created and maintained by Google. Google automatically updates their permissions as necessary, such as when Google Cloud adds new features or services. 

The following table lists all the predefined IAM roles for Application Integration: 

Application IntegrationCloud Integrations roles and permissions

This page lists the IAM roles and permissions for Cloud Integrations. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Integrations roles

Role | Permissions  
---|---  
  
#### Integrations Admin 

(`roles/integrations.admin`) Admin role for integrations  |  `integrations.*`

  * `integrations.apigeeAuthConfigs.create`
  * `integrations.apigeeAuthConfigs.delete`
  * `integrations.apigeeAuthConfigs.get`
  * `integrations.apigeeAuthConfigs.list`
  * `integrations.apigeeAuthConfigs.update`
  * `integrations.apigeeCertificates.create`
  * `integrations.apigeeCertificates.delete`
  * `integrations.apigeeCertificates.get`
  * `integrations.apigeeCertificates.list`
  * `integrations.apigeeCertificates.update`
  * `integrations.apigeeExecutions.list`
  * `integrations.apigeeIntegrationVers.create`
  * `integrations.apigeeIntegrationVers.delete`
  * `integrations.apigeeIntegrationVers.deploy`
  * `integrations.apigeeIntegrationVers.get`
  * `integrations.apigeeIntegrationVers.list`
  * `integrations.apigeeIntegrationVers.update`
  * `integrations.apigeeIntegrations.invoke`
  * `integrations.apigeeIntegrations.list`
  * `integrations.apigeeSfdcChannels.create`
  * `integrations.apigeeSfdcChannels.delete`
  * `integrations.apigeeSfdcChannels.get`
  * `integrations.apigeeSfdcChannels.list`
  * `integrations.apigeeSfdcChannels.update`
  * `integrations.apigeeSfdcInstances.create`
  * `integrations.apigeeSfdcInstances.delete`
  * `integrations.apigeeSfdcInstances.get`
  * `integrations.apigeeSfdcInstances.list`
  * `integrations.apigeeSfdcInstances.update`
  * `integrations.apigeeSuspensions.lift`
  * `integrations.apigeeSuspensions.list`
  * `integrations.apigeeSuspensions.resolve`
  * `integrations.authConfigs.create`
  * `integrations.authConfigs.delete`
  * `integrations.authConfigs.get`
  * `integrations.authConfigs.list`
  * `integrations.authConfigs.update`
  * `integrations.certificates.create`
  * `integrations.certificates.delete`
  * `integrations.certificates.get`
  * `integrations.certificates.list`
  * `integrations.certificates.update`
  * `integrations.executions.cancel`
  * `integrations.executions.get`
  * `integrations.executions.list`
  * `integrations.executions.replay`
  * `integrations.integrationVersions.create`
  * `integrations.integrationVersions.delete`
  * `integrations.integrationVersions.deploy`
  * `integrations.integrationVersions.get`
  * `integrations.integrationVersions.invoke`
  * `integrations.integrationVersions.list`
  * `integrations.integrationVersions.update`
  * `integrations.integrations.create`
  * `integrations.integrations.delete`
  * `integrations.integrations.deploy`
  * `integrations.integrations.generateOpenApiSpec`
  * `integrations.integrations.get`
  * `integrations.integrations.invoke`
  * `integrations.integrations.list`
  * `integrations.integrations.update`
  * `integrations.securityAuthConfigs.create`
  * `integrations.securityAuthConfigs.delete`
  * `integrations.securityAuthConfigs.get`
  * `integrations.securityAuthConfigs.list`
  * `integrations.securityAuthConfigs.update`
  * `integrations.securityExecutions.cancel`
  * `integrations.securityExecutions.get`
  * `integrations.securityExecutions.list`
  * `integrations.securityIntegTempVers.create`
  * `integrations.securityIntegTempVers.get`
  * `integrations.securityIntegTempVers.list`
  * `integrations.securityIntegrationVers.create`
  * `integrations.securityIntegrationVers.delete`
  * `integrations.securityIntegrationVers.deploy`
  * `integrations.securityIntegrationVers.get`
  * `integrations.securityIntegrationVers.list`
  * `integrations.securityIntegrationVers.update`
  * `integrations.securityIntegrations.invoke`
  * `integrations.securityIntegrations.list`
  * `integrations.sfdcChannels.create`
  * `integrations.sfdcChannels.delete`
  * `integrations.sfdcChannels.get`
  * `integrations.sfdcChannels.list`
  * `integrations.sfdcChannels.update`
  * `integrations.sfdcInstances.create`
  * `integrations.sfdcInstances.delete`
  * `integrations.sfdcInstances.get`
  * `integrations.sfdcInstances.list`
  * `integrations.sfdcInstances.update`
  * `integrations.suspensions.lift`
  * `integrations.suspensions.list`
  * `integrations.suspensions.resolve`
  * `integrations.templates.create`
  * `integrations.templates.delete`
  * `integrations.templates.get`
  * `integrations.templates.list`
  * `integrations.templates.share`
  * `integrations.templates.unshare`
  * `integrations.templates.update`
  * `integrations.templates.use`
  * `integrations.testCases.create`
  * `integrations.testCases.delete`
  * `integrations.testCases.get`
  * `integrations.testCases.invoke`
  * `integrations.testCases.list`
  * `integrations.testCases.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Integrations Viewer 

(`roles/integrations.viewer`) Viewer role for integrations  |  `integrations.apigeeAuthConfigs.get` `integrations.apigeeAuthConfigs.list` `integrations.apigeeCertificates.get` `integrations.apigeeCertificates.list` `integrations.apigeeExecutions.list` `integrations.apigeeIntegrationVers.get` `integrations.apigeeIntegrationVers.list` `integrations.apigeeIntegrations.list` `integrations.apigeeSfdcChannels.get` `integrations.apigeeSfdcChannels.list` `integrations.apigeeSfdcInstances.get` `integrations.apigeeSfdcInstances.list` `integrations.apigeeSuspensions.list` `integrations.authConfigs.get` `integrations.authConfigs.list` `integrations.certificates.get` `integrations.certificates.list` `integrations.executions.get` `integrations.executions.list` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrations.generateOpenApiSpec` `integrations.integrations.get` `integrations.integrations.list` `integrations.securityAuthConfigs.get` `integrations.securityAuthConfigs.list` `integrations.securityExecutions.get` `integrations.securityExecutions.list` `integrations.securityIntegTempVers.get` `integrations.securityIntegTempVers.list` `integrations.securityIntegrationVers.get` `integrations.securityIntegrationVers.list` `integrations.securityIntegrations.list` `integrations.sfdcChannels.get` `integrations.sfdcChannels.list` `integrations.sfdcInstances.get` `integrations.sfdcInstances.list` `integrations.suspensions.list` `integrations.templates.get` `integrations.templates.list` `integrations.templates.share` `integrations.templates.unshare` `integrations.templates.use` `integrations.testCases.get` `integrations.testCases.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Apigee Integration Admin 

(`roles/integrations.apigeeIntegrationAdminRole`) A user that has full access to all Apigee integrations.  |  `connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.executeSqlQuery` `connectors.entities.*`

  * `connectors.entities.create`
  * `connectors.entities.delete`
  * `connectors.entities.deleteEntitiesWithConditions`
  * `connectors.entities.get`
  * `connectors.entities.list`
  * `connectors.entities.update`
  * `connectors.entities.updateEntitiesWithConditions`

`connectors.entityTypes.list` `integrations.apigeeAuthConfigs.*`

  * `integrations.apigeeAuthConfigs.create`
  * `integrations.apigeeAuthConfigs.delete`
  * `integrations.apigeeAuthConfigs.get`
  * `integrations.apigeeAuthConfigs.list`
  * `integrations.apigeeAuthConfigs.update`

`integrations.apigeeCertificates.*`

  * `integrations.apigeeCertificates.create`
  * `integrations.apigeeCertificates.delete`
  * `integrations.apigeeCertificates.get`
  * `integrations.apigeeCertificates.list`
  * `integrations.apigeeCertificates.update`

`integrations.apigeeExecutions.list` `integrations.apigeeIntegrationVers.*`

  * `integrations.apigeeIntegrationVers.create`
  * `integrations.apigeeIntegrationVers.delete`
  * `integrations.apigeeIntegrationVers.deploy`
  * `integrations.apigeeIntegrationVers.get`
  * `integrations.apigeeIntegrationVers.list`
  * `integrations.apigeeIntegrationVers.update`

`integrations.apigeeIntegrations.*`

  * `integrations.apigeeIntegrations.invoke`
  * `integrations.apigeeIntegrations.list`

`integrations.apigeeSfdcChannels.*`

  * `integrations.apigeeSfdcChannels.create`
  * `integrations.apigeeSfdcChannels.delete`
  * `integrations.apigeeSfdcChannels.get`
  * `integrations.apigeeSfdcChannels.list`
  * `integrations.apigeeSfdcChannels.update`

`integrations.apigeeSfdcInstances.*`

  * `integrations.apigeeSfdcInstances.create`
  * `integrations.apigeeSfdcInstances.delete`
  * `integrations.apigeeSfdcInstances.get`
  * `integrations.apigeeSfdcInstances.list`
  * `integrations.apigeeSfdcInstances.update`

`integrations.apigeeSuspensions.*`

  * `integrations.apigeeSuspensions.lift`
  * `integrations.apigeeSuspensions.list`
  * `integrations.apigeeSuspensions.resolve`

`integrations.authConfigs.*`

  * `integrations.authConfigs.create`
  * `integrations.authConfigs.delete`
  * `integrations.authConfigs.get`
  * `integrations.authConfigs.list`
  * `integrations.authConfigs.update`

`integrations.certificates.*`

  * `integrations.certificates.create`
  * `integrations.certificates.delete`
  * `integrations.certificates.get`
  * `integrations.certificates.list`
  * `integrations.certificates.update`

`integrations.executions.get` `integrations.executions.list` `integrations.integrationVersions.create` `integrations.integrationVersions.delete` `integrations.integrationVersions.deploy` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrationVersions.update` `integrations.integrations.create` `integrations.integrations.delete` `integrations.integrations.deploy` `integrations.integrations.get` `integrations.integrations.invoke` `integrations.integrations.list` `integrations.integrations.update` `integrations.sfdcChannels.*`

  * `integrations.sfdcChannels.create`
  * `integrations.sfdcChannels.delete`
  * `integrations.sfdcChannels.get`
  * `integrations.sfdcChannels.list`
  * `integrations.sfdcChannels.update`

`integrations.sfdcInstances.*`

  * `integrations.sfdcInstances.create`
  * `integrations.sfdcInstances.delete`
  * `integrations.sfdcInstances.get`
  * `integrations.sfdcInstances.list`
  * `integrations.sfdcInstances.update`

`integrations.suspensions.*`

  * `integrations.suspensions.lift`
  * `integrations.suspensions.list`
  * `integrations.suspensions.resolve`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Apigee Integration Deployer 

(`roles/integrations.apigeeIntegrationDeployerRole`) A developer that can deploy/undeploy Apigee integrations to the integration runtime.  |  `integrations.apigeeIntegrationVers.deploy` `integrations.apigeeIntegrationVers.get` `integrations.apigeeIntegrationVers.list` `integrations.apigeeIntegrations.list` `integrations.integrationVersions.deploy` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrations.deploy` `integrations.integrations.get` `integrations.integrations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Apigee Integration Editor 

(`roles/integrations.apigeeIntegrationEditorRole`) A developer that can list, create and update Apigee integrations.  |  `connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.executeSqlQuery` `connectors.entities.*`

  * `connectors.entities.create`
  * `connectors.entities.delete`
  * `connectors.entities.deleteEntitiesWithConditions`
  * `connectors.entities.get`
  * `connectors.entities.list`
  * `connectors.entities.update`
  * `connectors.entities.updateEntitiesWithConditions`

`connectors.entityTypes.list` `integrations.apigeeAuthConfigs.create` `integrations.apigeeAuthConfigs.get` `integrations.apigeeAuthConfigs.list` `integrations.apigeeAuthConfigs.update` `integrations.apigeeCertificates.create` `integrations.apigeeCertificates.get` `integrations.apigeeCertificates.list` `integrations.apigeeCertificates.update` `integrations.apigeeExecutions.list` `integrations.apigeeIntegrationVers.*`

  * `integrations.apigeeIntegrationVers.create`
  * `integrations.apigeeIntegrationVers.delete`
  * `integrations.apigeeIntegrationVers.deploy`
  * `integrations.apigeeIntegrationVers.get`
  * `integrations.apigeeIntegrationVers.list`
  * `integrations.apigeeIntegrationVers.update`

`integrations.apigeeIntegrations.*`

  * `integrations.apigeeIntegrations.invoke`
  * `integrations.apigeeIntegrations.list`

`integrations.apigeeSfdcChannels.create` `integrations.apigeeSfdcChannels.get` `integrations.apigeeSfdcChannels.list` `integrations.apigeeSfdcChannels.update` `integrations.apigeeSfdcInstances.create` `integrations.apigeeSfdcInstances.get` `integrations.apigeeSfdcInstances.list` `integrations.apigeeSfdcInstances.update` `integrations.authConfigs.create` `integrations.authConfigs.get` `integrations.authConfigs.list` `integrations.authConfigs.update` `integrations.certificates.get` `integrations.executions.get` `integrations.executions.list` `integrations.integrationVersions.create` `integrations.integrationVersions.delete` `integrations.integrationVersions.deploy` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrationVersions.update` `integrations.integrations.create` `integrations.integrations.get` `integrations.integrations.invoke` `integrations.integrations.list` `integrations.integrations.update` `integrations.sfdcChannels.*`

  * `integrations.sfdcChannels.create`
  * `integrations.sfdcChannels.delete`
  * `integrations.sfdcChannels.get`
  * `integrations.sfdcChannels.list`
  * `integrations.sfdcChannels.update`

`integrations.sfdcInstances.*`

  * `integrations.sfdcInstances.create`
  * `integrations.sfdcInstances.delete`
  * `integrations.sfdcInstances.get`
  * `integrations.sfdcInstances.list`
  * `integrations.sfdcInstances.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Apigee Integration Invoker 

(`roles/integrations.apigeeIntegrationInvokerRole`) A role that can invoke Apigee integrations.  |  `connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.executeSqlQuery` `connectors.entities.*`

  * `connectors.entities.create`
  * `connectors.entities.delete`
  * `connectors.entities.deleteEntitiesWithConditions`
  * `connectors.entities.get`
  * `connectors.entities.list`
  * `connectors.entities.update`
  * `connectors.entities.updateEntitiesWithConditions`

`connectors.entityTypes.list` `integrations.apigeeExecutions.list` `integrations.apigeeIntegrationVers.get` `integrations.apigeeIntegrationVers.list` `integrations.apigeeIntegrations.*`

  * `integrations.apigeeIntegrations.invoke`
  * `integrations.apigeeIntegrations.list`

`integrations.executions.get` `integrations.executions.list` `integrations.integrationVersions.get` `integrations.integrationVersions.invoke` `integrations.integrationVersions.list` `integrations.integrations.get` `integrations.integrations.invoke` `integrations.integrations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Apigee Integration Viewer 

(`roles/integrations.apigeeIntegrationsViewer`) A developer that can list and view Apigee integrations.  |  `integrations.apigeeAuthConfigs.list` `integrations.apigeeCertificates.list` `integrations.apigeeIntegrationVers.get` `integrations.apigeeIntegrationVers.list` `integrations.apigeeIntegrations.list` `integrations.apigeeSfdcChannels.list` `integrations.apigeeSfdcInstances.list` `integrations.authConfigs.get` `integrations.authConfigs.list` `integrations.certificates.get` `integrations.certificates.list` `integrations.executions.get` `integrations.executions.list` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrations.get` `integrations.integrations.list` `integrations.sfdcChannels.list` `integrations.sfdcInstances.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Apigee Integration Approver 

(`roles/integrations.apigeeSuspensionResolver`) A role that can approve / reject Apigee integrations that contain a suspension/wait task.  |  `integrations.apigeeSuspensions.*`

  * `integrations.apigeeSuspensions.lift`
  * `integrations.apigeeSuspensions.list`
  * `integrations.apigeeSuspensions.resolve`

`integrations.suspensions.*`

  * `integrations.suspensions.lift`
  * `integrations.suspensions.list`
  * `integrations.suspensions.resolve`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Certificate Viewer 

(`roles/integrations.certificateViewer`) A developer that can list and view Certificates.  |  `integrations.certificates.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Integration Admin 

(`roles/integrations.integrationAdmin`) A user that has full access (CRUD) to all integrations.  |  `integrations.apigeeAuthConfigs.*`

  * `integrations.apigeeAuthConfigs.create`
  * `integrations.apigeeAuthConfigs.delete`
  * `integrations.apigeeAuthConfigs.get`
  * `integrations.apigeeAuthConfigs.list`
  * `integrations.apigeeAuthConfigs.update`

`integrations.apigeeCertificates.*`

  * `integrations.apigeeCertificates.create`
  * `integrations.apigeeCertificates.delete`
  * `integrations.apigeeCertificates.get`
  * `integrations.apigeeCertificates.list`
  * `integrations.apigeeCertificates.update`

`integrations.apigeeExecutions.list` `integrations.apigeeIntegrationVers.*`

  * `integrations.apigeeIntegrationVers.create`
  * `integrations.apigeeIntegrationVers.delete`
  * `integrations.apigeeIntegrationVers.deploy`
  * `integrations.apigeeIntegrationVers.get`
  * `integrations.apigeeIntegrationVers.list`
  * `integrations.apigeeIntegrationVers.update`

`integrations.apigeeIntegrations.*`

  * `integrations.apigeeIntegrations.invoke`
  * `integrations.apigeeIntegrations.list`

`integrations.apigeeSfdcChannels.*`

  * `integrations.apigeeSfdcChannels.create`
  * `integrations.apigeeSfdcChannels.delete`
  * `integrations.apigeeSfdcChannels.get`
  * `integrations.apigeeSfdcChannels.list`
  * `integrations.apigeeSfdcChannels.update`

`integrations.apigeeSfdcInstances.*`

  * `integrations.apigeeSfdcInstances.create`
  * `integrations.apigeeSfdcInstances.delete`
  * `integrations.apigeeSfdcInstances.get`
  * `integrations.apigeeSfdcInstances.list`
  * `integrations.apigeeSfdcInstances.update`

`integrations.apigeeSuspensions.*`

  * `integrations.apigeeSuspensions.lift`
  * `integrations.apigeeSuspensions.list`
  * `integrations.apigeeSuspensions.resolve`

`integrations.authConfigs.*`

  * `integrations.authConfigs.create`
  * `integrations.authConfigs.delete`
  * `integrations.authConfigs.get`
  * `integrations.authConfigs.list`
  * `integrations.authConfigs.update`

`integrations.certificates.*`

  * `integrations.certificates.create`
  * `integrations.certificates.delete`
  * `integrations.certificates.get`
  * `integrations.certificates.list`
  * `integrations.certificates.update`

`integrations.executions.*`

  * `integrations.executions.cancel`
  * `integrations.executions.get`
  * `integrations.executions.list`
  * `integrations.executions.replay`

`integrations.integrationVersions.create` `integrations.integrationVersions.delete` `integrations.integrationVersions.deploy` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrationVersions.update` `integrations.integrations.*`

  * `integrations.integrations.create`
  * `integrations.integrations.delete`
  * `integrations.integrations.deploy`
  * `integrations.integrations.generateOpenApiSpec`
  * `integrations.integrations.get`
  * `integrations.integrations.invoke`
  * `integrations.integrations.list`
  * `integrations.integrations.update`

`integrations.sfdcChannels.*`

  * `integrations.sfdcChannels.create`
  * `integrations.sfdcChannels.delete`
  * `integrations.sfdcChannels.get`
  * `integrations.sfdcChannels.list`
  * `integrations.sfdcChannels.update`

`integrations.sfdcInstances.*`

  * `integrations.sfdcInstances.create`
  * `integrations.sfdcInstances.delete`
  * `integrations.sfdcInstances.get`
  * `integrations.sfdcInstances.list`
  * `integrations.sfdcInstances.update`

`integrations.suspensions.*`

  * `integrations.suspensions.lift`
  * `integrations.suspensions.list`
  * `integrations.suspensions.resolve`

`integrations.templates.*`

  * `integrations.templates.create`
  * `integrations.templates.delete`
  * `integrations.templates.get`
  * `integrations.templates.list`
  * `integrations.templates.share`
  * `integrations.templates.unshare`
  * `integrations.templates.update`
  * `integrations.templates.use`

`integrations.testCases.*`

  * `integrations.testCases.create`
  * `integrations.testCases.delete`
  * `integrations.testCases.get`
  * `integrations.testCases.invoke`
  * `integrations.testCases.list`
  * `integrations.testCases.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Integration Deployer 

(`roles/integrations.integrationDeployer`) A developer that can deploy/undeploy integrations to the integration runtime.  |  `integrations.apigeeIntegrationVers.deploy` `integrations.apigeeIntegrationVers.get` `integrations.apigeeIntegrationVers.list` `integrations.apigeeIntegrations.list` `integrations.integrationVersions.deploy` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrations.deploy` `integrations.integrations.get` `integrations.integrations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Integration Editor 

(`roles/integrations.integrationEditor`) A developer that can list, create and update integrations.  |  `integrations.apigeeAuthConfigs.create` `integrations.apigeeAuthConfigs.get` `integrations.apigeeAuthConfigs.list` `integrations.apigeeAuthConfigs.update` `integrations.apigeeCertificates.create` `integrations.apigeeCertificates.get` `integrations.apigeeCertificates.list` `integrations.apigeeCertificates.update` `integrations.apigeeExecutions.list` `integrations.apigeeIntegrationVers.*`

  * `integrations.apigeeIntegrationVers.create`
  * `integrations.apigeeIntegrationVers.delete`
  * `integrations.apigeeIntegrationVers.deploy`
  * `integrations.apigeeIntegrationVers.get`
  * `integrations.apigeeIntegrationVers.list`
  * `integrations.apigeeIntegrationVers.update`

`integrations.apigeeIntegrations.*`

  * `integrations.apigeeIntegrations.invoke`
  * `integrations.apigeeIntegrations.list`

`integrations.apigeeSfdcChannels.create` `integrations.apigeeSfdcChannels.get` `integrations.apigeeSfdcChannels.list` `integrations.apigeeSfdcChannels.update` `integrations.apigeeSfdcInstances.create` `integrations.apigeeSfdcInstances.get` `integrations.apigeeSfdcInstances.list` `integrations.apigeeSfdcInstances.update` `integrations.authConfigs.create` `integrations.authConfigs.get` `integrations.authConfigs.list` `integrations.authConfigs.update` `integrations.certificates.get` `integrations.executions.*`

  * `integrations.executions.cancel`
  * `integrations.executions.get`
  * `integrations.executions.list`
  * `integrations.executions.replay`

`integrations.integrationVersions.create` `integrations.integrationVersions.delete` `integrations.integrationVersions.deploy` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrationVersions.update` `integrations.integrations.create` `integrations.integrations.generateOpenApiSpec` `integrations.integrations.get` `integrations.integrations.invoke` `integrations.integrations.list` `integrations.integrations.update` `integrations.sfdcChannels.*`

  * `integrations.sfdcChannels.create`
  * `integrations.sfdcChannels.delete`
  * `integrations.sfdcChannels.get`
  * `integrations.sfdcChannels.list`
  * `integrations.sfdcChannels.update`

`integrations.sfdcInstances.*`

  * `integrations.sfdcInstances.create`
  * `integrations.sfdcInstances.delete`
  * `integrations.sfdcInstances.get`
  * `integrations.sfdcInstances.list`
  * `integrations.sfdcInstances.update`

`integrations.templates.*`

  * `integrations.templates.create`
  * `integrations.templates.delete`
  * `integrations.templates.get`
  * `integrations.templates.list`
  * `integrations.templates.share`
  * `integrations.templates.unshare`
  * `integrations.templates.update`
  * `integrations.templates.use`

`integrations.testCases.*`

  * `integrations.testCases.create`
  * `integrations.testCases.delete`
  * `integrations.testCases.get`
  * `integrations.testCases.invoke`
  * `integrations.testCases.list`
  * `integrations.testCases.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Integration Invoker 

(`roles/integrations.integrationInvoker`) A role that can invoke integrations.  |  `integrations.apigeeExecutions.list` `integrations.apigeeIntegrationVers.get` `integrations.apigeeIntegrationVers.list` `integrations.apigeeIntegrations.*`

  * `integrations.apigeeIntegrations.invoke`
  * `integrations.apigeeIntegrations.list`

`integrations.executions.*`

  * `integrations.executions.cancel`
  * `integrations.executions.get`
  * `integrations.executions.list`
  * `integrations.executions.replay`

`integrations.integrationVersions.get` `integrations.integrationVersions.invoke` `integrations.integrationVersions.list` `integrations.integrations.get` `integrations.integrations.invoke` `integrations.integrations.list` `integrations.testCases.get` `integrations.testCases.invoke` `integrations.testCases.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Integration Viewer 

(`roles/integrations.integrationViewer`) A developer that can list and view integrations.  |  `integrations.apigeeAuthConfigs.list` `integrations.apigeeCertificates.list` `integrations.apigeeIntegrationVers.get` `integrations.apigeeIntegrationVers.list` `integrations.apigeeIntegrations.list` `integrations.apigeeSfdcChannels.list` `integrations.apigeeSfdcInstances.list` `integrations.authConfigs.get` `integrations.authConfigs.list` `integrations.certificates.get` `integrations.certificates.list` `integrations.executions.get` `integrations.executions.list` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrations.generateOpenApiSpec` `integrations.integrations.get` `integrations.integrations.list` `integrations.sfdcChannels.list` `integrations.sfdcInstances.list` `integrations.templates.get` `integrations.templates.list` `integrations.testCases.get` `integrations.testCases.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Security Integration Admin Beta

(`roles/integrations.securityIntegrationAdmin`) A user that has full access to all Security integrations.  |  `integrations.securityAuthConfigs.*`

  * `integrations.securityAuthConfigs.create`
  * `integrations.securityAuthConfigs.delete`
  * `integrations.securityAuthConfigs.get`
  * `integrations.securityAuthConfigs.list`
  * `integrations.securityAuthConfigs.update`

`integrations.securityExecutions.*`

  * `integrations.securityExecutions.cancel`
  * `integrations.securityExecutions.get`
  * `integrations.securityExecutions.list`

`integrations.securityIntegTempVers.*`

  * `integrations.securityIntegTempVers.create`
  * `integrations.securityIntegTempVers.get`
  * `integrations.securityIntegTempVers.list`

`integrations.securityIntegrationVers.*`

  * `integrations.securityIntegrationVers.create`
  * `integrations.securityIntegrationVers.delete`
  * `integrations.securityIntegrationVers.deploy`
  * `integrations.securityIntegrationVers.get`
  * `integrations.securityIntegrationVers.list`
  * `integrations.securityIntegrationVers.update`

`integrations.securityIntegrations.*`

  * `integrations.securityIntegrations.invoke`
  * `integrations.securityIntegrations.list`

  
  
#### Application Integration SFDC Instance Admin 

(`roles/integrations.sfdcInstanceAdmin`) A user that has full access (CRUD) to all SFDC instances.  |  `integrations.sfdcChannels.*`

  * `integrations.sfdcChannels.create`
  * `integrations.sfdcChannels.delete`
  * `integrations.sfdcChannels.get`
  * `integrations.sfdcChannels.list`
  * `integrations.sfdcChannels.update`

`integrations.sfdcInstances.*`

  * `integrations.sfdcInstances.create`
  * `integrations.sfdcInstances.delete`
  * `integrations.sfdcInstances.get`
  * `integrations.sfdcInstances.list`
  * `integrations.sfdcInstances.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Integration SFDC Instance Editor 

(`roles/integrations.sfdcInstanceEditor`) A developer that can list, create and update integrations.  |  `integrations.sfdcChannels.create` `integrations.sfdcChannels.get` `integrations.sfdcChannels.list` `integrations.sfdcChannels.update` `integrations.sfdcInstances.create` `integrations.sfdcInstances.get` `integrations.sfdcInstances.list` `integrations.sfdcInstances.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Integration SFDC Instance Viewer 

(`roles/integrations.sfdcInstanceViewer`) A developer that can list and view SFDC instances.  |  `integrations.sfdcChannels.get` `integrations.sfdcChannels.list` `integrations.sfdcInstances.get` `integrations.sfdcInstances.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Application Integration Approver 

(`roles/integrations.suspensionResolver`) A role that can resolve suspended integrations.  |  `integrations.apigeeSuspensions.*`

  * `integrations.apigeeSuspensions.lift`
  * `integrations.apigeeSuspensions.list`
  * `integrations.apigeeSuspensions.resolve`

`integrations.suspensions.*`

  * `integrations.suspensions.lift`
  * `integrations.suspensions.list`
  * `integrations.suspensions.resolve`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Application Integration Service Agent 

(`roles/integrations.serviceAgent`) Service agent that grants access to execute an integration.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudfunctions.functions.invoke` `cloudscheduler.jobs.create` `cloudscheduler.jobs.delete` `cloudscheduler.jobs.enable` `cloudscheduler.jobs.fullView` `cloudscheduler.jobs.get` `cloudscheduler.jobs.pause` `cloudscheduler.jobs.run` `cloudscheduler.jobs.update` `cloudscheduler.locations.*`

  * `cloudscheduler.locations.get`
  * `cloudscheduler.locations.list`

`connectors.actions.*`

  * `connectors.actions.execute`
  * `connectors.actions.list`

`connectors.connections.executeSqlQuery` `connectors.connections.get` `connectors.entities.*`

  * `connectors.entities.create`
  * `connectors.entities.delete`
  * `connectors.entities.deleteEntitiesWithConditions`
  * `connectors.entities.get`
  * `connectors.entities.list`
  * `connectors.entities.update`
  * `connectors.entities.updateEntitiesWithConditions`

`connectors.entityTypes.list` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `integrations.apigeeAuthConfigs.*`

  * `integrations.apigeeAuthConfigs.create`
  * `integrations.apigeeAuthConfigs.delete`
  * `integrations.apigeeAuthConfigs.get`
  * `integrations.apigeeAuthConfigs.list`
  * `integrations.apigeeAuthConfigs.update`

`integrations.apigeeCertificates.*`

  * `integrations.apigeeCertificates.create`
  * `integrations.apigeeCertificates.delete`
  * `integrations.apigeeCertificates.get`
  * `integrations.apigeeCertificates.list`
  * `integrations.apigeeCertificates.update`

`integrations.apigeeExecutions.list` `integrations.apigeeIntegrationVers.*`

  * `integrations.apigeeIntegrationVers.create`
  * `integrations.apigeeIntegrationVers.delete`
  * `integrations.apigeeIntegrationVers.deploy`
  * `integrations.apigeeIntegrationVers.get`
  * `integrations.apigeeIntegrationVers.list`
  * `integrations.apigeeIntegrationVers.update`

`integrations.apigeeIntegrations.*`

  * `integrations.apigeeIntegrations.invoke`
  * `integrations.apigeeIntegrations.list`

`integrations.apigeeSfdcChannels.*`

  * `integrations.apigeeSfdcChannels.create`
  * `integrations.apigeeSfdcChannels.delete`
  * `integrations.apigeeSfdcChannels.get`
  * `integrations.apigeeSfdcChannels.list`
  * `integrations.apigeeSfdcChannels.update`

`integrations.apigeeSfdcInstances.*`

  * `integrations.apigeeSfdcInstances.create`
  * `integrations.apigeeSfdcInstances.delete`
  * `integrations.apigeeSfdcInstances.get`
  * `integrations.apigeeSfdcInstances.list`
  * `integrations.apigeeSfdcInstances.update`

`integrations.apigeeSuspensions.*`

  * `integrations.apigeeSuspensions.lift`
  * `integrations.apigeeSuspensions.list`
  * `integrations.apigeeSuspensions.resolve`

`integrations.authConfigs.*`

  * `integrations.authConfigs.create`
  * `integrations.authConfigs.delete`
  * `integrations.authConfigs.get`
  * `integrations.authConfigs.list`
  * `integrations.authConfigs.update`

`integrations.certificates.*`

  * `integrations.certificates.create`
  * `integrations.certificates.delete`
  * `integrations.certificates.get`
  * `integrations.certificates.list`
  * `integrations.certificates.update`

`integrations.executions.list` `integrations.integrationVersions.create` `integrations.integrationVersions.delete` `integrations.integrationVersions.deploy` `integrations.integrationVersions.get` `integrations.integrationVersions.list` `integrations.integrationVersions.update` `integrations.integrations.create` `integrations.integrations.delete` `integrations.integrations.deploy` `integrations.integrations.get` `integrations.integrations.invoke` `integrations.integrations.list` `integrations.integrations.update` `integrations.sfdcChannels.*`

  * `integrations.sfdcChannels.create`
  * `integrations.sfdcChannels.delete`
  * `integrations.sfdcChannels.get`
  * `integrations.sfdcChannels.list`
  * `integrations.sfdcChannels.update`

`integrations.sfdcInstances.*`

  * `integrations.sfdcInstances.create`
  * `integrations.sfdcInstances.delete`
  * `integrations.sfdcInstances.get`
  * `integrations.sfdcInstances.list`
  * `integrations.sfdcInstances.update`

`integrations.suspensions.*`

  * `integrations.suspensions.lift`
  * `integrations.suspensions.list`
  * `integrations.suspensions.resolve`

`pubsub.messageTransforms.validate` `pubsub.schemas.attach` `pubsub.schemas.create` `pubsub.schemas.delete` `pubsub.schemas.get` `pubsub.schemas.list` `pubsub.schemas.validate` `pubsub.snapshots.create` `pubsub.snapshots.delete` `pubsub.snapshots.get` `pubsub.snapshots.list` `pubsub.snapshots.seek` `pubsub.snapshots.update` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.list` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.detachSubscription` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.publish` `pubsub.topics.update` `pubsub.topics.updateTag` `resourcemanager.projects.get` `resourcemanager.projects.list` `run.jobs.run` `run.routes.invoke` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.create` `storage.buckets.get` `storage.buckets.list` `storage.buckets.update` `storage.objects.create` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Cloud Integrations permissions

Permission | Included in roles  
---|---  
  
#### `integrations.apigeeAuthConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeAuthConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeAuthConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeAuthConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeAuthConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeCertificates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeCertificates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeCertificates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeCertificates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeCertificates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeExecutions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeIntegrationVers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeIntegrationVers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeIntegrationVers.deploy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeIntegrationVers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeIntegrationVers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeIntegrationVers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeIntegrations.invoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeIntegrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcChannels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcChannels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcChannels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcChannels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcChannels.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcInstances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcInstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcInstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcInstances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSfdcInstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSuspensions.lift`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeSuspensionResolver) (`roles/integrations.apigeeSuspensionResolver`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.suspensionResolver) (`roles/integrations.suspensionResolver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSuspensions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeSuspensionResolver) (`roles/integrations.apigeeSuspensionResolver`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.suspensionResolver) (`roles/integrations.suspensionResolver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.apigeeSuspensions.resolve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeSuspensionResolver) (`roles/integrations.apigeeSuspensionResolver`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.suspensionResolver) (`roles/integrations.suspensionResolver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.authConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.authConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.authConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.authConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.authConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.certificates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.certificates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.certificates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Certificate Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.certificateViewer) (`roles/integrations.certificateViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.certificates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.certificates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.executions.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)   
  
#### `integrations.executions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)   
  
#### `integrations.executions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.executions.replay`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)   
  
#### `integrations.integrationVersions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrationVersions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrationVersions.deploy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrationVersions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrationVersions.invoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `integrations.integrationVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrationVersions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrations.deploy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrations.generateOpenApiSpec`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Dialogflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.serviceAgent) (`roles/dialogflow.serviceAgent`) 

  
  
#### `integrations.integrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrations.invoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Customer Engagement Suite Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/ces#ces.serviceAgent) (`roles/ces.serviceAgent`) 
  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationDeployerRole) (`roles/integrations.apigeeIntegrationDeployerRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationInvokerRole) (`roles/integrations.apigeeIntegrationInvokerRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Deployer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationDeployer) (`roles/integrations.integrationDeployer`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 
  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.integrations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.securityAuthConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityAuthConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityAuthConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityAuthConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityAuthConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityExecutions.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Integration Executor Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.integrationExecutorServiceAgent) (`roles/securitycenter.integrationExecutorServiceAgent`) 

  
  
#### `integrations.securityExecutions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityExecutions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Integration Executor Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.integrationExecutorServiceAgent) (`roles/securitycenter.integrationExecutorServiceAgent`) 

  
  
#### `integrations.securityIntegTempVers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegTempVers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegTempVers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegrationVers.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegrationVers.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegrationVers.deploy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegrationVers.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegrationVers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegrationVers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.securityIntegrations.invoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Security Center Integration Executor Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.integrationExecutorServiceAgent) (`roles/securitycenter.integrationExecutorServiceAgent`) 

  
  
#### `integrations.securityIntegrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Security Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.securityIntegrationAdmin) (`roles/integrations.securityIntegrationAdmin`)   
  
#### `integrations.sfdcChannels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  [Application Integration SFDC Instance Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceEditor) (`roles/integrations.sfdcInstanceEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcChannels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcChannels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  [Application Integration SFDC Instance Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceEditor) (`roles/integrations.sfdcInstanceEditor`)  [Application Integration SFDC Instance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceViewer) (`roles/integrations.sfdcInstanceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcChannels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  [Application Integration SFDC Instance Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceEditor) (`roles/integrations.sfdcInstanceEditor`)  [Application Integration SFDC Instance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceViewer) (`roles/integrations.sfdcInstanceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcChannels.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  [Application Integration SFDC Instance Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceEditor) (`roles/integrations.sfdcInstanceEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcInstances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  [Application Integration SFDC Instance Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceEditor) (`roles/integrations.sfdcInstanceEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcInstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcInstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  [Application Integration SFDC Instance Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceEditor) (`roles/integrations.sfdcInstanceEditor`)  [Application Integration SFDC Instance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceViewer) (`roles/integrations.sfdcInstanceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcInstances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Apigee Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationsViewer) (`roles/integrations.apigeeIntegrationsViewer`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  [Application Integration SFDC Instance Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceEditor) (`roles/integrations.sfdcInstanceEditor`)  [Application Integration SFDC Instance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceViewer) (`roles/integrations.sfdcInstanceViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.sfdcInstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationEditorRole) (`roles/integrations.apigeeIntegrationEditorRole`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration SFDC Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceAdmin) (`roles/integrations.sfdcInstanceAdmin`)  [Application Integration SFDC Instance Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.sfdcInstanceEditor) (`roles/integrations.sfdcInstanceEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.suspensions.lift`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeSuspensionResolver) (`roles/integrations.apigeeSuspensionResolver`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.suspensionResolver) (`roles/integrations.suspensionResolver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.suspensions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeSuspensionResolver) (`roles/integrations.apigeeSuspensionResolver`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.suspensionResolver) (`roles/integrations.suspensionResolver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.suspensions.resolve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Apigee Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeIntegrationAdminRole) (`roles/integrations.apigeeIntegrationAdminRole`)  [Apigee Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.apigeeSuspensionResolver) (`roles/integrations.apigeeSuspensionResolver`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.suspensionResolver) (`roles/integrations.suspensionResolver`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Application Integration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.serviceAgent) (`roles/integrations.serviceAgent`) 

  
  
#### `integrations.templates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
  
#### `integrations.templates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
  
#### `integrations.templates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)   
  
#### `integrations.templates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)   
  
#### `integrations.templates.share`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
  
#### `integrations.templates.unshare`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
  
#### `integrations.templates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
  
#### `integrations.templates.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
  
#### `integrations.testCases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
  
#### `integrations.testCases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
  
#### `integrations.testCases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `integrations.testCases.invoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `integrations.testCases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Integrations Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.viewer) (`roles/integrations.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)  [Application Integration Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationInvoker) (`roles/integrations.integrationInvoker`)  [Application Integration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationViewer) (`roles/integrations.integrationViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `integrations.testCases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Integrations Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.admin) (`roles/integrations.admin`)  [Application Integration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)  [Application Integration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`)   
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


