---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create/
title: gcloud iam policy-bindings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:15:38.658391+00:00
---

# gcloud iam policy-bindings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam policy-bindings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam policy-bindings create - create PolicyBinding instance 
SYNOPSIS
    

`gcloud iam policy-bindings create` (`POLICY_BINDING` : `--folder`=`FOLDER` `--location`=`LOCATION` `--organization`=`ORGANIZATION`) `--policy`=`POLICY` (`--target-principal-set`=`TARGET_PRINCIPAL_SET` | `--target-resource`=`TARGET_RESOURCE`) [`--annotations`=[`ANNOTATIONS`,…]] [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--etag`=`ETAG`] [`--policy-kind`=`POLICY_KIND`] [`--condition-description`=`CONDITION_DESCRIPTION` `--condition-expression`=`CONDITION_EXPRESSION` `--condition-location`=`CONDITION_LOCATION` `--condition-title`=`CONDITION_TITLE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create PolicyBinding instance. 
EXAMPLES
     To create a policy binding instance called `my-binding` that references a principal access boundary policy run: 
    
    
    gcloud iam policy-bindings create my-binding --organization=123 --location=global --policy=organizations/123/locations/global/principalAccessBoundaryPolicies/my-policy --target-principal-set=//cloudresourcemanager.googleapis.com/organizations/123

POSITIONAL ARGUMENTS
    

PolicyBinding resource - Identifier. The name of the policy binding, in the format `{binding_parent/locations/{location}/policyBindings/{policy_binding_id}`. The binding parent is the closest Resource Manager resource (project, folder, or organization) to the binding target. 

Format: 

  * `projects/{project_id}/locations/{location}/policyBindings/{policy_binding_id}`
  * `projects/{project_number}/locations/{location}/policyBindings/{policy_binding_id}`
  * `folders/{folder_id}/locations/{location}/policyBindings/{policy_binding_id}`
  * `organizations/{organization_id}/locations/{location}/policyBindings/{policy_binding_id}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 



To set the `project` attribute: 

  * provide the argument `policy_binding` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [iam.folders.locations.policyBindings, iam.organizations.locations.policyBindings, iam.projects.locations.policyBindings]. 



This must be specified. 

`POLICY_BINDING`
     ID of the policyBinding or fully qualified identifier for the policyBinding. 

To set the `policy_binding` attribute: 

  * provide the argument `policy_binding` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     The folder id of the policyBinding resource. 

To set the `folder` attribute: 

  * provide the argument `policy_binding` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [iam.folders.locations.policyBindings]. 


`--location`=`LOCATION`
     The location id of the policyBinding resource. 

To set the `location` attribute: 

  * provide the argument `policy_binding` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization id of the policyBinding resource. 

To set the `organization` attribute: 

  * provide the argument `policy_binding` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [iam.organizations.locations.policyBindings]. 


REQUIRED FLAGS
    

`--policy`=`POLICY`
     The resource name of the policy to be bound. The binding parent and policy must belong to the same organization. 
The full resource name of the resource to which the policy will be bound. Immutable once set. 

This must be specified. 

Arguments for the target. 

At most one of these can be specified: 

`--target-principal-set`=`TARGET_PRINCIPAL_SET`
     The full resource name that's used for principal access boundary policy bindings. The principal set must be directly parented by the policy binding's parent or same as the parent if the target is a project, folder, or organization. 

Examples: 

  * For bindings parented by an organization: 
    * Organization: `//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID`
    * Workforce Identity: `//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID`
    * Workspace Identity: `//iam.googleapis.com/locations/global/workspace/WORKSPACE_ID`
  * For bindings parented by a folder: 
    * Folder: `//cloudresourcemanager.googleapis.com/folders/FOLDER_ID`
  * For bindings parented by a project: 
    * Project: 
      * `//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER`
      * `//cloudresourcemanager.googleapis.com/projects/PROJECT_ID`
    * Workload Identity Pool: `//iam.googleapis.com/projects/PROJECT_NUMBER/locations/LOCATION/workloadIdentityPools/WORKLOAD_POOL_ID`


`--target-resource`=`TARGET_RESOURCE`
     The full resource name that's used for access policy bindings. 

Examples: 

  * Organization: `//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID`
    * Folder: `//cloudresourcemanager.googleapis.com/folders/FOLDER_ID`
      * Project: 
        * `//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER`
        * `//cloudresourcemanager.googleapis.com/projects/PROJECT_ID`


OPTIONAL FLAGS
    

`--annotations`=[`ANNOTATIONS`,…]
     User-defined annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitations. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --annotations=string=string

`JSON Example:`
    
    
    --annotations='{"string": "string"}'

`File Example:`
    
    
    --annotations=path_to_file.(yaml|json)

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     The description of the policy binding. Must be less than or equal to 63 characters. 
`--etag`=`ETAG`
     The etag for the policy binding. If this is provided on update, it must match the server's etag. 
`--policy-kind`=`POLICY_KIND`
     The kind of the policy to attach in this binding. This field must be one of the following: 

  * Left empty (will be automatically set to the policy kind) 
  * The input policy kind. 



`POLICY_KIND` must be one of: 

`access`
     Access policy kind. 
`principal-access-boundary`
     Principal access boundary policy kind 
Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at <https://github.com/google/cel-spec>. 

Example (Comparison): 
    
    
    title: "Summary size limit"
    description: "Determines if a summary is less than 100 chars"
    expression: "document.summary.size() < 100"

Example (Equality): 
    
    
    title: "Requestor is owner"
    description: "Determines if requestor is the document owner"
    expression: "document.owner == request.auth.claims.email"

Example (Logic): 
    
    
    title: "Public documents"
    description: "Determine whether the document should be publicly visible"
    expression: "document.type != 'private' && document.type != 'internal'"

Example (Data Manipulation): 
    
    
    title: "Notification string"
    description: "Create a notification string with a timestamp."
    expression: "'New message received at ' + string(document.create_time)"

The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information. 

`--condition-description`=`CONDITION_DESCRIPTION`
     Description of the expression. This is a longer text which describes the expression, e.g. when hovered over it in a UI. 
`--condition-expression`=`CONDITION_EXPRESSION`
     Textual representation of an expression in Common Expression Language syntax. 
`--condition-location`=`CONDITION_LOCATION`
     String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. 
`--condition-title`=`CONDITION_TITLE`
     Title for the expression, i.e. a short string describing its purpose. This can be used e.g. in UIs which allow to enter the expression. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v3` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This variant is also available: 
    
    
    [gcloud beta iam policy-bindings create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/policy-bindings/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
