---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/custom-constraints/
title: Set up custom constraints \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:51:53.781371+00:00
---

# Set up custom constraints  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/service-routing/custom-constraints/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up custom constraints

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `networksecurity.googleapis.com/AuthorizationPolicy`
  * `networksecurity.googleapis.com/ClientTlsPolicy`
  * `networksecurity.googleapis.com/ServerTlsPolicy`
  * `networkservices.googleapis.com/Mesh`
  * `networkservices.googleapis.com/TcpRoute`
  * `networkservices.googleapis.com/TlsRoute`
  * `networkservices.googleapis.com/HttpRoute`
  * `networkservices.googleapis.com/GrpcRoute`
  * `networkservices.googleapis.com/Gateway`
  * `networkservices.googleapis.com/EndpointPolicy`
  * `networkservices.googleapis.com/ServiceBinding`



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

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Cloud Service Mesh supported resources

The following table lists the Cloud Service Mesh resources that you can reference in custom constraints. 

Resource | Field  
---|---  
networksecurity.googleapis.com/AuthorizationPolicy |  `resource.action`  
`resource.description`  
`resource.name`  
`resource.rules.destinations.hosts`  
`resource.rules.destinations.httpHeaderMatch.headerName`  
`resource.rules.destinations.httpHeaderMatch.regexMatch`  
`resource.rules.destinations.methods`  
`resource.rules.destinations.ports`  
`resource.rules.sources.ipBlocks`  
`resource.rules.sources.principals`  
networksecurity.googleapis.com/ClientTlsPolicy |  `resource.clientCertificate.certificateProviderInstance.pluginInstance`  
`resource.clientCertificate.grpcEndpoint.targetUri`  
`resource.description`  
`resource.name`  
`resource.serverValidationCa.certificateProviderInstance.pluginInstance`  
`resource.serverValidationCa.grpcEndpoint.targetUri`  
`resource.sni`  
networksecurity.googleapis.com/ServerTlsPolicy |  `resource.allowOpen`  
`resource.description`  
`resource.mtlsPolicy.clientValidationCa.certificateProviderInstance.pluginInstance`  
`resource.mtlsPolicy.clientValidationCa.grpcEndpoint.targetUri`  
`resource.mtlsPolicy.clientValidationMode`  
`resource.mtlsPolicy.clientValidationRelaxations`  
`resource.mtlsPolicy.clientValidationTrustConfig`  
`resource.name`  
`resource.serverCertificate.certificateProviderInstance.pluginInstance`  
`resource.serverCertificate.grpcEndpoint.targetUri`  
networkservices.googleapis.com/EndpointPolicy |  `resource.authorizationPolicy`  
`resource.clientTlsPolicy`  
`resource.description`  
`resource.endpointMatcher.metadataLabelMatcher.metadataLabelMatchCriteria`  
`resource.endpointMatcher.metadataLabelMatcher.metadataLabels.labelName`  
`resource.endpointMatcher.metadataLabelMatcher.metadataLabels.labelValue`  
`resource.name`  
`resource.serverTlsPolicy`  
`resource.trafficPortSelector.ports`  
`resource.type`  
networkservices.googleapis.com/Gateway |  `resource.addresses`  
`resource.allowGlobalAccess`  
`resource.allPorts`  
`resource.certificateUrls`  
`resource.description`  
`resource.envoyHeaders`  
`resource.gatewaySecurityPolicy`  
`resource.ipVersion`  
`resource.name`  
`resource.network`  
`resource.ports`  
`resource.routingMode`  
`resource.scope`  
`resource.serverTlsPolicy`  
`resource.subnetwork`  
`resource.type`  
networkservices.googleapis.com/GrpcRoute |  `resource.description`  
`resource.gateways`  
`resource.hostnames`  
`resource.meshes`  
`resource.name`  
`resource.rules.action.destinations.serviceName`  
`resource.rules.action.destinations.weight`  
`resource.rules.action.faultInjectionPolicy.abort.httpStatus`  
`resource.rules.action.faultInjectionPolicy.abort.percentage`  
`resource.rules.action.faultInjectionPolicy.delay.fixedDelay`  
`resource.rules.action.faultInjectionPolicy.delay.percentage`  
`resource.rules.action.idleTimeout`  
`resource.rules.action.retryPolicy.numRetries`  
`resource.rules.action.retryPolicy.retryConditions`  
`resource.rules.action.statefulSessionAffinity.cookieTtl`  
`resource.rules.action.timeout`  
`resource.rules.matches.headers.key`  
`resource.rules.matches.headers.type`  
`resource.rules.matches.headers.value`  
`resource.rules.matches.method.caseSensitive`  
`resource.rules.matches.method.grpcMethod`  
`resource.rules.matches.method.grpcService`  
`resource.rules.matches.method.type`  
networkservices.googleapis.com/HttpRoute |  `resource.description`  
`resource.gateways`  
`resource.hostnames`  
`resource.meshes`  
`resource.name`  
`resource.rules.action.corsPolicy.allowCredentials`  
`resource.rules.action.corsPolicy.allowHeaders`  
`resource.rules.action.corsPolicy.allowMethods`  
`resource.rules.action.corsPolicy.allowOriginRegexes`  
`resource.rules.action.corsPolicy.allowOrigins`  
`resource.rules.action.corsPolicy.disabled`  
`resource.rules.action.corsPolicy.exposeHeaders`  
`resource.rules.action.corsPolicy.maxAge`  
`resource.rules.action.destinations.requestHeaderModifier.add`  
`resource.rules.action.destinations.requestHeaderModifier.remove`  
`resource.rules.action.destinations.requestHeaderModifier.set`  
`resource.rules.action.destinations.responseHeaderModifier.add`  
`resource.rules.action.destinations.responseHeaderModifier.remove`  
`resource.rules.action.destinations.responseHeaderModifier.set`  
`resource.rules.action.destinations.serviceName`  
`resource.rules.action.destinations.weight`  
`resource.rules.action.directResponse.status`  
`resource.rules.action.faultInjectionPolicy.abort.httpStatus`  
`resource.rules.action.faultInjectionPolicy.abort.percentage`  
`resource.rules.action.faultInjectionPolicy.delay.fixedDelay`  
`resource.rules.action.faultInjectionPolicy.delay.percentage`  
`resource.rules.action.idleTimeout`  
`resource.rules.action.redirect.hostRedirect`  
`resource.rules.action.redirect.httpsRedirect`  
`resource.rules.action.redirect.pathRedirect`  
`resource.rules.action.redirect.portRedirect`  
`resource.rules.action.redirect.prefixRewrite`  
`resource.rules.action.redirect.responseCode`  
`resource.rules.action.redirect.stripQuery`  
`resource.rules.action.requestHeaderModifier.add`  
`resource.rules.action.requestHeaderModifier.remove`  
`resource.rules.action.requestHeaderModifier.set`  
`resource.rules.action.requestMirrorPolicy.destination.requestHeaderModifier.add`  
`resource.rules.action.requestMirrorPolicy.destination.requestHeaderModifier.remove`  
`resource.rules.action.requestMirrorPolicy.destination.requestHeaderModifier.set`  
`resource.rules.action.requestMirrorPolicy.destination.responseHeaderModifier.add`  
`resource.rules.action.requestMirrorPolicy.destination.responseHeaderModifier.remove`  
`resource.rules.action.requestMirrorPolicy.destination.responseHeaderModifier.set`  
`resource.rules.action.requestMirrorPolicy.destination.serviceName`  
`resource.rules.action.requestMirrorPolicy.destination.weight`  
`resource.rules.action.requestMirrorPolicy.mirrorPercent`  
`resource.rules.action.responseHeaderModifier.add`  
`resource.rules.action.responseHeaderModifier.remove`  
`resource.rules.action.responseHeaderModifier.set`  
`resource.rules.action.retryPolicy.numRetries`  
`resource.rules.action.retryPolicy.perTryTimeout`  
`resource.rules.action.retryPolicy.retryConditions`  
`resource.rules.action.statefulSessionAffinity.cookieTtl`  
`resource.rules.action.timeout`  
`resource.rules.action.urlRewrite.hostRewrite`  
`resource.rules.action.urlRewrite.pathPrefixRewrite`  
`resource.rules.matches.fullPathMatch`  
`resource.rules.matches.headers.exactMatch`  
`resource.rules.matches.headers.header`  
`resource.rules.matches.headers.invertMatch`  
`resource.rules.matches.headers.prefixMatch`  
`resource.rules.matches.headers.presentMatch`  
`resource.rules.matches.headers.rangeMatch.end`  
`resource.rules.matches.headers.rangeMatch.start`  
`resource.rules.matches.headers.regexMatch`  
`resource.rules.matches.headers.suffixMatch`  
`resource.rules.matches.ignoreCase`  
`resource.rules.matches.prefixMatch`  
`resource.rules.matches.queryParameters.exactMatch`  
`resource.rules.matches.queryParameters.presentMatch`  
`resource.rules.matches.queryParameters.queryParameter`  
`resource.rules.matches.queryParameters.regexMatch`  
`resource.rules.matches.regexMatch`  
networkservices.googleapis.com/Mesh |  `resource.description`  
`resource.envoyHeaders`  
`resource.interceptionPort`  
`resource.name`  
networkservices.googleapis.com/ServiceBinding |  `resource.description`  
`resource.name`  
networkservices.googleapis.com/TcpRoute |  `resource.description`  
`resource.gateways`  
`resource.meshes`  
`resource.name`  
`resource.rules.action.destinations.serviceName`  
`resource.rules.action.destinations.weight`  
`resource.rules.action.idleTimeout`  
`resource.rules.action.originalDestination`  
`resource.rules.matches.address`  
`resource.rules.matches.port`  
networkservices.googleapis.com/TlsRoute |  `resource.description`  
`resource.gateways`  
`resource.meshes`  
`resource.name`  
`resource.rules.action.destinations.serviceName`  
`resource.rules.action.destinations.weight`  
`resource.rules.action.idleTimeout`  
`resource.rules.matches.alpn`  
`resource.rules.matches.sniHost`  
`resource.targetProxies`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.serverTlsPolicy`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
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
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.serverTlsPolicy`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `networkservices.googleapis.com/EndpointPolicy`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.serverTlsPolicy"`. 

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.serverTlsPolicy`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
