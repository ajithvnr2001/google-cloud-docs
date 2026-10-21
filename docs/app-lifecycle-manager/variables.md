---
url: https://docs.cloud.google.com/app-lifecycle-manager/variables/
title: Variables and variable mapping with App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:17.859411+00:00
---

# Variables and variable mapping with App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/variables/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  Variables and variable mapping with App Lifecycle Manager Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how variables, variable mapping, and dependencies work within App Lifecycle Manager.

App Lifecycle Manager lets you to deploy and manage complex SaaS applications by organizing them into modular _units_. These units, defined by Terraform configurations within _blueprints_ , can be interconnected through _dependencies_ , allowing for sophisticated orchestration and automated provisioning. A key aspect of managing these units and their interactions is through _variables_ and _variable mapping_.

You can build complex, modular, and scalable deployments with automated provisioning, inter-unit communication, and flexible configuration options. Carefully consider your variable hierarchy, dependency relationships, and variable mappings to optimize your SaaS architecture and management workflows within App Lifecycle Manager.

## Units and variables

At the heart of App Lifecycle Manager are units. Units utilize variables to customize their deployment and behavior. These variables are essentially Terraform variables that you can define in your blueprint's `variables.tf` file. They allow you to parameterize your Terraform configurations, making them reusable and adaptable across different environments and deployments.

### Mandatory variables for unit provisioning

While you can define custom variables for your units, App Lifecycle Manager also relies on a set of _mandatory variables_. These variables are automatically recognized and handled by App Lifecycle Manager, even if they are not explicitly defined in your Terraform configuration.

The mandatory variables are:

  * `project_id` and `project_number` (or, `tenant_project_id` and `tenant_project_number`): This variable specifies the Google Cloud project ID where your unit's resources will be deployed. You can use either `project_id` and `project_number`, or `tenant_id` and `tenant_project_number`. This field is necessary for resource creation and management within the correct Google Cloud project.

You can find your project ID in the the Google Cloud console on the [Dashboard page](https://console.cloud.google.com/). Look for the **Project ID** field in the **Project info** card within the **Cloud overview** section.

  * _`project_number`_ or _`tenant_project_number`_ : Similar to `project_id`, this variable represents the Google Cloud project number. You can use `project_number` or `tenant_project_number` interchangeably.

You can find your project number alongside your project ID in the **Project info** card within the **Cloud overview** section of the the Google Cloud console [Dashboard page](https://console.cloud.google.com/).

**Caution:** You must use either `project_id` and `project_number`, or `tenant_project_id` and `tenant_project_number`. Mixing and matching ( `project_id` with `tenant_project_number`, for example) is not supported and may lead to errors.
  * **`actuation_sa`** : This variable represents the email address of the **actuation service account**. This service account is a user-managed service account that App Lifecycle Manager uses (via Infrastructure Manager) to execute your Terraform configurations when provisioning, updating, or deprovisioning units.

We recommend that you use a dedicated actuation service account per tenant (or unit) to implement the principle of least privilege. This limits the potential impact of security breaches and provides better isolation between your deployments.

For more information about configuring and granting permissions to actuation service accounts, see [Product overview](https://docs.cloud.google.com/app-lifecycle-manager/overview#actuation-sa).




## Unit variables hierarchy

Unit variables can be defined and sourced from multiple locations. When you use App Lifecycle Manager, it's important to understand the hierarchy of variable values used during unit operations.

The order is as follows (from _lowest_ to _highest_ precedence):

App Lifecycle Manager resolves variable values in this order:

  1. _Existing input variables on the unit_ : If a variable is already defined on the unit resource itself (from a previous operation or configuration, for example), this value takes the _lowest_ precedence. If a variable value is set directly on the unit, it will be overridden if a value is found from sources higher in the hierarchy.

  2. _Release defaults_ : Release default values are applied if a variable isn't already set on the unit, but they will _override_ existing unit variables.

  3. _Unit operations_ : When you perform a _unit operation_ such as `provision` or `upgrade`, you can explicitly provide input variables as part of the operation request. Variables provided in a unit operation will _override_ release defaults and existing unit variables.

  4. _Dependencies' input variable mappings_ : When a unit has dependencies on other units, _variable mappings_ defined in the _unit kind_ can source variable values from the output variables of dependency units. This is the _highest_ precedence source. Variables obtained through dependency mappings will _override_ values from unit operations, release defaults, and existing unit variables.




This hierarchical approach provides flexibility and control over your variable management. You can establish persistent configurations directly on the unit (lowest priority), define baseline defaults using releases, customize for specific operations, and dynamically source the most important and overriding values from unit dependencies (highest priority).

## Unit dependencies

App Lifecycle Manager lets you to define dependencies between units. This is important for building complex SaaS applications where different components rely on each other. Dependencies ensure that related units are provisioned and managed in a coordinated manner.

You define dependencies within a unit kind. When you create a unit of a particular unit kind, App Lifecycle Manager automatically manages its dependencies.

### Dependency definition in unit kind

In the `UnitKind` definition, you specify a list of dependencies, each referencing another `UnitKind` and assigning it an _alias_. This alias is used for referencing the dependency in variable mappings:
    
    
      message UnitKind {
        // ... other fields ...
    
        // List of other unit kinds that this release will depend on.
        repeated Dependency dependencies = 4
            [(.google.api.field_behavior) = OPTIONAL];
        // ...
      }
    
      message Dependency {
        // The unit kind of the dependency.
        string unit_kind = 1 [
          (.google.api.field_behavior) = REQUIRED,
          (.google.api.field_behavior) = IMMUTABLE,
          (.google.api.resource_reference) = {
            type: "saasservicemgmt.googleapis.com/UnitKind"
          }
        ];
    
        // An alias for the dependency. Used for input variable mapping.
        string alias = 2 [(.google.api.field_behavior) = REQUIRED];
      }
    

### Automatic dependency provisioning

When you request to provision a unit that has dependencies defined in its `UnitKind`, App Lifecycle Manager automatically checks for the existence of those dependency units.

If a dependency unit is not found, App Lifecycle Manager will automatically provision it before provisioning the dependent unit.

App Lifecycle Manager ensures that dependency units are provisioned _before_ their dependent units, maintaining the correct order of operations.

## Variable mapping

_Variable mapping_ is the mechanism to pass data (variable values) between dependent units and their dependencies. This is essential for configuring dependent units based on outputs from their dependencies.

Variable mapping is defined within the dependent unit kind and uses `FromMapping` and `ToMapping`:

  * `FromMapping`: `FromMapping` is used to retrieve output variables from a dependency unit and map them to input variables of the dependent unit. This is how a dependent unit can obtain information from its dependencies, such as connection endpoints or resource IDs.
        
        message VariableMapping {
          // ...
          oneof mapping_type {
            // Output variables which will get their values from dependencies
            FromMapping from = 2 [(.google.api.field_behavior) = OPTIONAL];
            // ...
          }
        }
        
        message FromMapping {
          // Alias of the dependency that the outputVariable will pass its value to
          string dependency = 1 [(.google.api.field_behavior) = REQUIRED];
        
          // Name of the outputVariable on the dependency
          string output_variable = 2 [(.google.api.field_behavior) = REQUIRED];
        }
        

In the provided codelab example, the `App UnitKind` has a `FromMapping` to retrieve the `cluster_endpoint` output variable from the `Cluster UnitKind` dependency. This allows the application to connect to the newly provisioned Kubernetes cluster.

  * `ToMapping`: `ToMapping` is used to pass input variables from the dependent unit to the input variables of a dependency unit. This lets you configure dependency units based on parameters provided for the dependent unit.
        
        message VariableMapping {
          // ...
          oneof mapping_type {
            // ...
            // Input variables whose values will be passed on to dependencies.
            ToMapping to = 3 [(.google.api.field_behavior) = OPTIONAL];
          }
        }
        
        message ToMapping {
          // Alias of the dependency that the inputVariable will pass its value to
          string dependency = 1 [(.google.api.field_behavior) = REQUIRED];
        
          // Name of the inputVariable on the dependency
          string input_variable = 2 [(.google.api.field_behavior) = REQUIRED];
        
          // Tells EasySaaS if this mapping should be used during lookup or not
          bool ignore_for_lookup = 3 [(.google.api.field_behavior) = OPTIONAL];
        }
        

In the codelab, the `App UnitKind` uses `ToMapping` to pass the `tenant_project_id` and `tenant_project_number` input variables to the `Cluster UnitKind` dependency. This ensures that the Kubernetes cluster is created within the correct project.

  * `ignore_for_lookup` in `ToMapping`: The `ignore_for_lookup` field in `ToMapping` controls dependency lookup behavior. It is a boolean value:

    * `false` (or not specified): When set to `false`, App Lifecycle Manager will use the input variables specified in the `ToMapping` as _lookup keys_ to find an existing dependency unit. If a unit with matching input variables is found, it will be reused as the dependency. If no matching unit is found, a new dependency unit will be provisioned. This is useful for reusing shared resources like clusters.
    * `true`: When set to `true`, the input variable in the `ToMapping` won't be used for dependency lookup. This means that a new dependency unit will always be provisioned, even if units with the same input variables already exist. This is useful when you need dedicated, non-shared dependencies for each dependent unit.



### Example: Shared Kubernetes cluster

If you want to reuse a Kubernetes cluster for multiple application units within the same project, you would use `ToMapping` with `ignore_for_lookup` set to `false` and map variables like `tenant_project_id` and `region` to the cluster unit kind. Units in the same project and region would then reuse the same cluster.

### Example: Dedicated Kubernetes cluster per application

If you need a dedicated Kubernetes cluster for each application unit, you would use `ToMapping` with `ignore_for_lookup` set to `true` or avoid `ToMapping` lookup variables altogether. Each application unit would then trigger the provisioning of a new, isolated Kubernetes cluster.

## Manage secrets

App Lifecycle Manager variables are not intended for storing sensitive information like passwords, API keys, or certificates. Storing secrets directly in variables poses security risks. Variable values can be logged and potentially exposed through system outputs, increasing the chance of unauthorized access.

For secure secret management in your App Lifecycle Manager applications, we strongly recommend using [Secret Manager](https://docs.cloud.google.com/secrets/docs).

## What's next

  * To understand more about App Lifecycle Manager, see [App Lifecycle Manager overview](https://docs.cloud.google.com/app-lifecycle-manager/overview).
  * To get try a tutorial see [Deploy a MySQL instance with App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql).
  * For details about defining the App offering with Terraform configurations, see [Blueprints in App Lifecycle Manager](https://docs.cloud.google.com/app-lifecycle-manager/blueprints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
