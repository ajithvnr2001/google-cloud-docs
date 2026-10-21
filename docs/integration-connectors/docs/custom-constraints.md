---
url: https://docs.cloud.google.com/integration-connectors/docs/custom-constraints/
title: Manage Integration Connectors resources using custom constraints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:46.950591+00:00
---

# Manage Integration Connectors resources using custom constraints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Manage Integration Connectors resources using custom constraints

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `connectors.googleapis.com/Connection`
  * `connectors.googleapis.com/EndpointAttachment`
  * `connectors.googleapis.com/ManagedZone`
  * `connectors.googleapis.com/EventSubscription`
  * `connectors.googleapis.com/RegionalSettings`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the following IAM roles: 

  * [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization resource
  * To create or update an Integration Connectors connection: [](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin)[Integration Connectors Admin](https://docs.cloud.google.com/integration-connectors/docs/reference/iam/roles) (`roles/connectors.admin`) on the project resource 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage organization policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policies:

  * `orgpolicy.*` on the organization resource
  * To create or update an Integration Connectors connection: 
    * `connectors.connections.create` on the project resource
    * `connectors.connections.get` on the project resource
    * `connectors.connections.list` on the project resource
    * `connectors.connections.update` on the project resource



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Integration Connectors supported resources

The following table lists the Integration Connectors resources that you can reference in custom constraints. 

Resource | Field  
---|---  
connectors.googleapis.com/Connection |  `resource.asyncOperationsEnabled`  
`resource.authConfig.additionalVariables.boolValue`  
`resource.authConfig.additionalVariables.encryptionKeyValue.kmsKeyName`  
`resource.authConfig.additionalVariables.encryptionKeyValue.type`  
`resource.authConfig.additionalVariables.intValue`  
`resource.authConfig.additionalVariables.key`  
`resource.authConfig.additionalVariables.secretValue.secretVersion`  
`resource.authConfig.additionalVariables.stringValue`  
`resource.authConfig.authKey`  
`resource.authConfig.authType`  
`resource.authConfig.oauth2AuthCodeFlow.authCode`  
`resource.authConfig.oauth2AuthCodeFlow.authUri`  
`resource.authConfig.oauth2AuthCodeFlow.clientId`  
`resource.authConfig.oauth2AuthCodeFlow.clientSecret.secretVersion`  
`resource.authConfig.oauth2AuthCodeFlow.enablePkce`  
`resource.authConfig.oauth2AuthCodeFlow.pkceVerifier`  
`resource.authConfig.oauth2AuthCodeFlow.redirectUri`  
`resource.authConfig.oauth2AuthCodeFlow.scopes`  
`resource.authConfig.oauth2AuthCodeFlowGoogleManaged.authCode`  
`resource.authConfig.oauth2AuthCodeFlowGoogleManaged.redirectUri`  
`resource.authConfig.oauth2AuthCodeFlowGoogleManaged.scopes`  
`resource.authConfig.oauth2ClientCredentials.clientId`  
`resource.authConfig.oauth2ClientCredentials.clientSecret.secretVersion`  
`resource.authConfig.oauth2JwtBearer.clientKey.secretVersion`  
`resource.authConfig.oauth2JwtBearer.jwtClaims.audience`  
`resource.authConfig.oauth2JwtBearer.jwtClaims.issuer`  
`resource.authConfig.oauth2JwtBearer.jwtClaims.subject`  
`resource.authConfig.sshPublicKey.certType`  
`resource.authConfig.sshPublicKey.sshClientCert.secretVersion`  
`resource.authConfig.sshPublicKey.sshClientCertPass.secretVersion`  
`resource.authConfig.sshPublicKey.username`  
`resource.authConfig.userPassword.password.secretVersion`  
`resource.authConfig.userPassword.username`  
`resource.authOverrideEnabled`  
`resource.configVariables.boolValue`  
`resource.configVariables.encryptionKeyValue.kmsKeyName`  
`resource.configVariables.encryptionKeyValue.type`  
`resource.configVariables.intValue`  
`resource.configVariables.key`  
`resource.configVariables.secretValue.secretVersion`  
`resource.configVariables.stringValue`  
`resource.connectorVersion`  
`resource.description`  
`resource.destinationConfigs.destinations.host`  
`resource.destinationConfigs.destinations.port`  
`resource.destinationConfigs.key`  
`resource.euaOauthAuthConfig.additionalVariables.boolValue`  
`resource.euaOauthAuthConfig.additionalVariables.encryptionKeyValue.kmsKeyName`  
`resource.euaOauthAuthConfig.additionalVariables.encryptionKeyValue.type`  
`resource.euaOauthAuthConfig.additionalVariables.intValue`  
`resource.euaOauthAuthConfig.additionalVariables.key`  
`resource.euaOauthAuthConfig.additionalVariables.secretValue.secretVersion`  
`resource.euaOauthAuthConfig.additionalVariables.stringValue`  
`resource.euaOauthAuthConfig.authKey`  
`resource.euaOauthAuthConfig.authType`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlow.authCode`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlow.authUri`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlow.clientId`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlow.clientSecret.secretVersion`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlow.enablePkce`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlow.pkceVerifier`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlow.redirectUri`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlow.scopes`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlowGoogleManaged.authCode`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlowGoogleManaged.redirectUri`  
`resource.euaOauthAuthConfig.oauth2AuthCodeFlowGoogleManaged.scopes`  
`resource.euaOauthAuthConfig.oauth2ClientCredentials.clientId`  
`resource.euaOauthAuthConfig.oauth2ClientCredentials.clientSecret.secretVersion`  
`resource.euaOauthAuthConfig.oauth2JwtBearer.clientKey.secretVersion`  
`resource.euaOauthAuthConfig.oauth2JwtBearer.jwtClaims.audience`  
`resource.euaOauthAuthConfig.oauth2JwtBearer.jwtClaims.issuer`  
`resource.euaOauthAuthConfig.oauth2JwtBearer.jwtClaims.subject`  
`resource.euaOauthAuthConfig.sshPublicKey.certType`  
`resource.euaOauthAuthConfig.sshPublicKey.sshClientCert.secretVersion`  
`resource.euaOauthAuthConfig.sshPublicKey.sshClientCertPass.secretVersion`  
`resource.euaOauthAuthConfig.sshPublicKey.username`  
`resource.euaOauthAuthConfig.userPassword.password.secretVersion`  
`resource.euaOauthAuthConfig.userPassword.username`  
`resource.eventingConfig.additionalVariables.boolValue`  
`resource.eventingConfig.additionalVariables.encryptionKeyValue.kmsKeyName`  
`resource.eventingConfig.additionalVariables.encryptionKeyValue.type`  
`resource.eventingConfig.additionalVariables.intValue`  
`resource.eventingConfig.additionalVariables.key`  
`resource.eventingConfig.additionalVariables.secretValue.secretVersion`  
`resource.eventingConfig.additionalVariables.stringValue`  
`resource.eventingConfig.allowedEventTypes`  
`resource.eventingConfig.authConfig.additionalVariables.boolValue`  
`resource.eventingConfig.authConfig.additionalVariables.encryptionKeyValue.kmsKeyName`  
`resource.eventingConfig.authConfig.additionalVariables.encryptionKeyValue.type`  
`resource.eventingConfig.authConfig.additionalVariables.intValue`  
`resource.eventingConfig.authConfig.additionalVariables.key`  
`resource.eventingConfig.authConfig.additionalVariables.secretValue.secretVersion`  
`resource.eventingConfig.authConfig.additionalVariables.stringValue`  
`resource.eventingConfig.authConfig.authKey`  
`resource.eventingConfig.authConfig.authType`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlow.authCode`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlow.authUri`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlow.clientId`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlow.clientSecret.secretVersion`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlow.enablePkce`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlow.pkceVerifier`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlow.redirectUri`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlow.scopes`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlowGoogleManaged.authCode`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlowGoogleManaged.redirectUri`  
`resource.eventingConfig.authConfig.oauth2AuthCodeFlowGoogleManaged.scopes`  
`resource.eventingConfig.authConfig.oauth2ClientCredentials.clientId`  
`resource.eventingConfig.authConfig.oauth2ClientCredentials.clientSecret.secretVersion`  
`resource.eventingConfig.authConfig.oauth2JwtBearer.clientKey.secretVersion`  
`resource.eventingConfig.authConfig.oauth2JwtBearer.jwtClaims.audience`  
`resource.eventingConfig.authConfig.oauth2JwtBearer.jwtClaims.issuer`  
`resource.eventingConfig.authConfig.oauth2JwtBearer.jwtClaims.subject`  
`resource.eventingConfig.authConfig.sshPublicKey.certType`  
`resource.eventingConfig.authConfig.sshPublicKey.sshClientCert.secretVersion`  
`resource.eventingConfig.authConfig.sshPublicKey.sshClientCertPass.secretVersion`  
`resource.eventingConfig.authConfig.sshPublicKey.username`  
`resource.eventingConfig.authConfig.userPassword.password.secretVersion`  
`resource.eventingConfig.authConfig.userPassword.username`  
`resource.eventingConfig.deadLetterConfig.projectId`  
`resource.eventingConfig.deadLetterConfig.topic`  
`resource.eventingConfig.enrichmentConfig.appendAcl`  
`resource.eventingConfig.enrichmentEnabled`  
`resource.eventingConfig.listenerAuthConfig.additionalVariables.boolValue`  
`resource.eventingConfig.listenerAuthConfig.additionalVariables.encryptionKeyValue.kmsKeyName`  
`resource.eventingConfig.listenerAuthConfig.additionalVariables.encryptionKeyValue.type`  
`resource.eventingConfig.listenerAuthConfig.additionalVariables.intValue`  
`resource.eventingConfig.listenerAuthConfig.additionalVariables.key`  
`resource.eventingConfig.listenerAuthConfig.additionalVariables.secretValue.secretVersion`  
`resource.eventingConfig.listenerAuthConfig.additionalVariables.stringValue`  
`resource.eventingConfig.listenerAuthConfig.authKey`  
`resource.eventingConfig.listenerAuthConfig.authType`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlow.authCode`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlow.authUri`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlow.clientId`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlow.clientSecret.secretVersion`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlow.enablePkce`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlow.pkceVerifier`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlow.redirectUri`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlow.scopes`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlowGoogleManaged.authCode`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlowGoogleManaged.redirectUri`  
`resource.eventingConfig.listenerAuthConfig.oauth2AuthCodeFlowGoogleManaged.scopes`  
`resource.eventingConfig.listenerAuthConfig.oauth2ClientCredentials.clientId`  
`resource.eventingConfig.listenerAuthConfig.oauth2ClientCredentials.clientSecret.secretVersion`  
`resource.eventingConfig.listenerAuthConfig.oauth2JwtBearer.clientKey.secretVersion`  
`resource.eventingConfig.listenerAuthConfig.oauth2JwtBearer.jwtClaims.audience`  
`resource.eventingConfig.listenerAuthConfig.oauth2JwtBearer.jwtClaims.issuer`  
`resource.eventingConfig.listenerAuthConfig.oauth2JwtBearer.jwtClaims.subject`  
`resource.eventingConfig.listenerAuthConfig.sshPublicKey.certType`  
`resource.eventingConfig.listenerAuthConfig.sshPublicKey.sshClientCert.secretVersion`  
`resource.eventingConfig.listenerAuthConfig.sshPublicKey.sshClientCertPass.secretVersion`  
`resource.eventingConfig.listenerAuthConfig.sshPublicKey.username`  
`resource.eventingConfig.listenerAuthConfig.userPassword.password.secretVersion`  
`resource.eventingConfig.listenerAuthConfig.userPassword.username`  
`resource.eventingConfig.privateConnectivityAllowlistedProjects`  
`resource.eventingConfig.privateConnectivityEnabled`  
`resource.eventingConfig.proxyDestinationConfig.destinations.host`  
`resource.eventingConfig.proxyDestinationConfig.destinations.port`  
`resource.eventingConfig.proxyDestinationConfig.key`  
`resource.eventingConfig.registrationDestinationConfig.destinations.host`  
`resource.eventingConfig.registrationDestinationConfig.destinations.port`  
`resource.eventingConfig.registrationDestinationConfig.key`  
`resource.eventingConfig.sslConfig.additionalVariables.boolValue`  
`resource.eventingConfig.sslConfig.additionalVariables.encryptionKeyValue.kmsKeyName`  
`resource.eventingConfig.sslConfig.additionalVariables.encryptionKeyValue.type`  
`resource.eventingConfig.sslConfig.additionalVariables.intValue`  
`resource.eventingConfig.sslConfig.additionalVariables.key`  
`resource.eventingConfig.sslConfig.additionalVariables.secretValue.secretVersion`  
`resource.eventingConfig.sslConfig.additionalVariables.stringValue`  
`resource.eventingConfig.sslConfig.clientCertificate.secretVersion`  
`resource.eventingConfig.sslConfig.clientCertType`  
`resource.eventingConfig.sslConfig.clientPrivateKey.secretVersion`  
`resource.eventingConfig.sslConfig.clientPrivateKeyPass.secretVersion`  
`resource.eventingConfig.sslConfig.privateServerCertificate.secretVersion`  
`resource.eventingConfig.sslConfig.serverCertType`  
`resource.eventingConfig.sslConfig.trustModel`  
`resource.eventingConfig.sslConfig.type`  
`resource.eventingConfig.sslConfig.useSsl`  
`resource.eventingEnablementType`  
`resource.fallbackOnAdminCredentials`  
`resource.lockConfig.locked`  
`resource.lockConfig.reason`  
`resource.logConfig.enabled`  
`resource.logConfig.level`  
`resource.nodeConfig.maxNodeCount`  
`resource.nodeConfig.minNodeCount`  
`resource.serviceAccount`  
`resource.sslConfig.additionalVariables.boolValue`  
`resource.sslConfig.additionalVariables.encryptionKeyValue.kmsKeyName`  
`resource.sslConfig.additionalVariables.encryptionKeyValue.type`  
`resource.sslConfig.additionalVariables.intValue`  
`resource.sslConfig.additionalVariables.key`  
`resource.sslConfig.additionalVariables.secretValue.secretVersion`  
`resource.sslConfig.additionalVariables.stringValue`  
`resource.sslConfig.clientCertificate.secretVersion`  
`resource.sslConfig.clientCertType`  
`resource.sslConfig.clientPrivateKey.secretVersion`  
`resource.sslConfig.clientPrivateKeyPass.secretVersion`  
`resource.sslConfig.privateServerCertificate.secretVersion`  
`resource.sslConfig.serverCertType`  
`resource.sslConfig.trustModel`  
`resource.sslConfig.type`  
`resource.sslConfig.useSsl`  
`resource.suspended`  
`resource.trafficShapingConfigs.duration`  
`resource.trafficShapingConfigs.quotaLimit`  
connectors.googleapis.com/EndpointAttachment |  `resource.description`  
`resource.endpointGlobalAccess`  
`resource.serviceAttachment`  
connectors.googleapis.com/EventSubscription |  `resource.destinations.endpoint.endpointUri`  
`resource.destinations.endpoint.headers.key`  
`resource.destinations.endpoint.headers.value`  
`resource.destinations.pubsub.attributes`  
`resource.destinations.pubsub.configVariables.boolValue`  
`resource.destinations.pubsub.configVariables.encryptionKeyValue.kmsKeyName`  
`resource.destinations.pubsub.configVariables.encryptionKeyValue.type`  
`resource.destinations.pubsub.configVariables.intValue`  
`resource.destinations.pubsub.configVariables.key`  
`resource.destinations.pubsub.configVariables.secretValue.secretVersion`  
`resource.destinations.pubsub.configVariables.stringValue`  
`resource.destinations.pubsub.projectId`  
`resource.destinations.pubsub.topicId`  
`resource.destinations.serviceAccount`  
`resource.destinations.type`  
`resource.eventTypeId`  
`resource.filter`  
`resource.jms.name`  
`resource.jms.type`  
`resource.name`  
`resource.subscriber`  
`resource.subscriberLink`  
`resource.triggerConfigVariables.boolValue`  
`resource.triggerConfigVariables.encryptionKeyValue.kmsKeyName`  
`resource.triggerConfigVariables.encryptionKeyValue.type`  
`resource.triggerConfigVariables.intValue`  
`resource.triggerConfigVariables.key`  
`resource.triggerConfigVariables.secretValue.secretVersion`  
`resource.triggerConfigVariables.stringValue`  
connectors.googleapis.com/ManagedZone |  `resource.description`  
`resource.dns`  
`resource.targetProject`  
`resource.targetVpc`  
connectors.googleapis.com/RegionalSettings |  `resource.encryptionConfig.encryptionType`  
`resource.encryptionConfig.kmsKeyName`  
`resource.networkConfig.egressMode`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.allowedConnectionLocations`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE  
      - UPDATE 
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.allowedConnectionLocations`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `connectors.googleapis.com/Connection`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"!(resource.location == 'us-central1' || resource.location == 'europe-west1')"`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Possible values are `ALLOW` and `DENY`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

The deny action means that if the condition evaluates to true, the operation to create or update the resource is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




## Enforce a custom organization policy

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.allowedConnectionLocations`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint and policy that restricts new Integration Connectors connections in a specific project to only be created in `us-central1` or `europe-west1`.

Before you begin, you must have the following:

  * Your organization ID
  * A project ID



### Create the constraint

To create a custom constraint, follow these steps:

  1. Create the following YAML file and save it as `constraint-allowed-locations.yaml`:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.allowedConnectionLocations
         resourceTypes:
         - connectors.googleapis.com/Connection
         methodTypes:
         - CREATE
         condition: "!(resource.location == 'us-central1' || resource.location == 'europe-west1')"
         actionType: DENY
         displayName: Restrict connection locations
         description: Connections can only be created in us-central1 or europe-west1.
         

Replace `ORGANIZATION_ID` with your organization ID.

This defines a constraint where for every new connection, if the location is not `us-central1` or `europe-west1`, the operation is denied.

  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint ~/constraint-allowed-locations.yaml
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output is similar to the following:
         
         CUSTOM_CONSTRAINT                       ACTION_TYPE  METHOD_TYPES   RESOURCE_TYPES                     DISPLAY_NAME
         custom.allowedConnectionLocations       DENY         CREATE         connectors.googleapis.com/Connection    Restrict connection locations
         ...
         




### Create the policy

Now create a policy and apply it to the custom constraint that you created.

  1. Save the following file as `policy-allowed-locations.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.allowedConnectionLocations
         spec:
           rules:
           - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy ~/policy-allowed-locations.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT                         LIST_POLICY    BOOLEAN_POLICY    ETAG
         custom.allowedConnectionLocations  -              SET               COCsm5QGENiXi2E=
         




After you apply the policy, wait for about two minutes for Google Cloud to start enforcing the policy.

### Test the policy

Try to create an Integration Connectors connection in a disallowed location such as `us-east1`. You can do this using the Google Cloud console, Google Cloud CLI, or the REST API. For example, if using gcloud CLI, create a connection in `us-east1`:
    
    
    gcloud connectors connections create test-connection --location=us-east1 --connector-version=<var>CONNECTOR_VERSION</var> ...
    

Replace `CONNECTOR_VERSION` with a valid connector version in your project, and include other required flags for connection creation.

The output is the following:
    
    
    Operation denied by custom org policies: ["customConstraints/custom.allowedConnectionLocations": "Connections can only be created in us-central1 or europe-west1."]
    

## Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints.

Description | Constraint syntax  
---|---  
Restrict connection locations to `us-central1` or `europe-west1` | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.allowedConnectionLocations
        resourceTypes:
        - connectors.googleapis.com/Connection
        methodTypes:
        - CREATE
        condition: "!(resource.location == 'us-central1' || resource.location == 'europe-west1')"
        actionType: DENY
        displayName: Restrict connection locations
        description: Connections can only be created in us-central1 or europe-west1.
          
  
## What's next

  * Learn how to [Manage connections](https://docs.cloud.google.com/integration-connectors/docs/manage-connections).
  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
