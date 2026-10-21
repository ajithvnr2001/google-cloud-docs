---
url: https://docs.cloud.google.com/iam/docs/conditions-attribute-reference/
title: Attribute reference for IAM Conditions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:26.741856+00:00
---

# Attribute reference for IAM Conditions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/conditions-attribute-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Attribute reference for IAM Conditions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes supported attributes in a [condition expression](https://docs.cloud.google.com/iam/docs/conditions-overview).

**Note:** This page shows common uses of each function and operator. For more details about the allowed syntax for functions and operators, see the [CEL language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md).

## Supported condition attributes

The following sections summarize the supported attributes and indicate which Google Cloud services recognize each attribute.

### Resource attributes

The following attributes relate to the resource that is the subject of the request.

**Attribute** | **Usage summary** | **Supported Google Cloud services**  
---|---|---  
**Resource service attribute** |  Manage access based on the Google Cloud service being used. You can use this attribute in allow policy role bindings. | 

  * Agent Registry
  * Apigee
  * Application Integration
  * Apigee API Hub
  * Backup and DR Service
  * BigQuery
  * BigQuery Reservation API
  * Bigtable
  * Binary Authorization
  * Cloud Deploy
  * Customer Experience Agent Studio
  * Cloud Key Management Service
  * Cloud Logging
  * Cloud SQL
  * Cloud Storage
  * Compute Engine
  * Dataform
  * Cloud DNS
  * Google Kubernetes Engine
  * Firestore
  * Identity-Aware Proxy
  * Integration Connectors
  * Google Cloud Managed Service for Apache Kafka
  * Network Security Integration
  * Parameter Manager
  * Cloud NGFW
  * Pub/Sub Lite
  * Resource Manager
  * Secret Manager
  * Spanner

  
**Resource type attribute** |  Manage access based on the resource type. You can use this attribute in allow policy role bindings. | 

  * Agent Registry
  * Apigee
  * Application Integration
  * Apigee API Hub
  * BigQuery
  * BigQuery Reservation API
  * Bigtable
  * Binary Authorization
  * Customer Experience Agent Studio
  * Cloud Key Management Service
  * Cloud Logging
  * Cloud SQL
  * Cloud Storage
  * Compute Engine
  * Dataform
  * Cloud DNS
  * Google Kubernetes Engine
  * Firestore
  * Cloud NGFW
  * Identity-Aware Proxy
  * Integration Connectors
  * Google Cloud Managed Service for Apache Kafka
  * Network Security Integration
  * Parameter Manager
  * Pub/Sub Lite
  * Resource Manager
  * Secret Manager
  * Spanner

  
**Resource name attribute** |  Manage access based on the name of the resource. You can use this attribute in allow policy role bindings. | 

  * Agent Registry
  * Apigee
  * Application Integration
  * Apigee API Hub
  * Backup and DR Service
  * BigQuery
  * BigQuery Reservation API
  * Bigtable
  * Binary Authorization
  * Cloud Deploy
  * Customer Experience Agent Studio
  * Cloud Key Management Service
  * Cloud Logging
  * Cloud SQL
  * Cloud Storage
  * Compute Engine
  * Dataform
  * Cloud DNS
  * Google Kubernetes Engine
  * Firestore
  * Cloud NGFW
  * Integration Connectors
  * Google Cloud Managed Service for Apache Kafka
  * Network Security Integration
  * Parameter Manager
  * Pub/Sub Lite
  * Secret Manager
  * Spanner

  
**Resource tags** |  Manage access based on the tags attached to the resource. You can use this attribute in the following places:

  * Allow policy role bindings
  * Deny policy deny rules

|  All Google Cloud services (see Support for inherited conditions)  **Note:** Certain areas of the Google Cloud console don't recognize allow policy role bindings with tag-based conditions. As a result, if you have a role with a tag-based condition, then the Google Cloud console might incorrectly prevent you from performing certain actions. If you encounter this issue, then use an alternate method, such as the gcloud CLI, to perform the action.   
  
For more details about resource attributes, see Resource attributes on this page.

### Principal attributes

The following attributes relate to the principal making the request.

**Attribute** | **Usage summary** | **Supported principal types**  
---|---|---  
**Principal type attribute** |  Apply policies based on the type of principal in the request. You can use this attribute in policy bindings for Principal Access Boundary policies.  | 

  * Google Accounts
  * Workforce identity pool identities
  * Workload identity pool identities
  * Service accounts

  
**Principal subject attribute** |  Apply policies based on the identity of the principal in the request. You can use this attribute in policy bindings for Principal Access Boundary policies.  | 

  * Google Accounts
  * Workforce identity pool identities
  * Workload identity pool identities
  * Service accounts

  
  
For more details about principal attributes, see Principal attributes on this page.

### Request attributes

The following attributes relate to the details of the request.

**Attribute** | **Usage summary** | **Supported Google Cloud services**  
---|---|---  
**Access levels attribute** |  Manage access based on specific access level(s).  An access level is a calculated attribute based on raw attributes about the request and requester, such as the origin IP address, device attributes, and time of day. For example, an `onNetwork` access level might require that the device making the request originates from a particular IP address range. Access levels are defined by an organization's administrators.  You can use this attribute in allow policy role bindings. |  Identity-Aware Proxy  
**API attributes** |  Manage access based on data provided by a specific Google Cloud API or service.  You can use this attribute in allow policy role bindings. |  Not all services recognize all API attributes. For a list of services that recognize each attribute, see API attributes.   
**Date/time attributes** |  Set expirable, scheduled, or limited-duration access to Google Cloud resources.  You can use these attributes in allow policy role bindings. |  All Google Cloud services (see Support for inherited conditions)   
**Destination IP/port attributes** |  Manage access based on the destination IP address and/or port of a request. For example, a Compute Engine virtual machine (VM) instance might expose an external IP, such as `10.0.0.2`, but port `22` might be exposed for administrative usage only.  Used for [Identity-Aware Proxy TCP forwarding.](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview) You can use these attributes in allow policy role bindings. |  Identity-Aware Proxy  
**Forwarding rule attributes** |  Specify the types of [forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) that a principal can create. For example, you could allow a principal to create forwarding rules for [internal Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#types-of-cloud-load-balancing), which handle traffic that originates inside a Google Cloud network, but not for external Google Cloud load balancers, which handle traffic that originates from the internet.  You can use these attributes in allow policy role bindings. | 

  * Cloud Load Balancing
  * Cloud VPN
  * Compute Engine [protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding)
  * Cloud Service Mesh

  
**URL path/host attributes** |  Manage access based on the URL path and/or host of a request. For example, a condition could specify that `https://example.com` is the main application accessible by a general domain of users, while `https://hr.example.com/admin` is used to access a page in the application that only Human Resources admins can access.  You can use these attributes in allow policy role bindings. | 

  * Identity-Aware Proxy
  * Cloud Run

  
  
For more details about request attributes, see Request attributes on this page.

### Support for inherited conditions

In addition to adding conditions to the allow policies of some service-specific resources, it's possible to add conditional role bindings to resources at the organization, folder, or project level. When added at the container resource level, the conditional role bindings are inherited by other resources through the [resource hierarchy](https://docs.cloud.google.com/iam/docs/overview#policy_hierarchy). Inherited conditions are useful when a resource doesn't allow [conditions in their allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-conditional-roles) or doesn't have an allow policy.

When you use attributes at the organization, folder, or project level, keep in mind that most attributes are available only for specific resource types. If part of a condition uses an attribute that isn't available for a resource, then that part of the condition is never interpreted as granting access. For example, the condition `resource.name.endsWith == devResource` never grants access to any IAM resource because IAM resources don't provide the resource name.

To prevent this issue, use the [resource type](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-type) and [resource service](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-service) attributes to limit the scope of the condition. For example, the following condition evaluates to `true` for all resource types other than Compute Engine instances; in contrast, for Compute Engine instances, the condition checks resource name:
    
    
    resource.type != 'compute.googleapis.com/Disk' ||
        resource.name.endsWith('devResource')
    

**Important:** If your condition uses the `resource.name` attribute, we strongly recommend that you use the `resource.type` attribute, not the `resource.service` attribute, to explicitly limit which resource types the `resource.name` condition applies to. For details, see `resource.name` attribute on this page.

## Resource attributes

The resource service, resource type, and resource name attributes are typically used to change the scope of an access grant provided by the role binding. When a role contains permissions that apply to different resource-specific attributes, resource-based conditions can be used to grant a subset of the role's permissions for specific type(s) or for specific service(s).

### resource.service attribute

The `resource.service` attribute lets you set a condition based on the Google Cloud service being used. For example, you could set a condition limiting a user's access to resources that use the `cloudresourcemanager.googleapis.com` service. For a list of supported values, see [Resource service values](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-service).

You can use the `resource.service` attribute in allow policy role bindings.

Attribute variable | `resource.service`  
---|---  
Attribute type |  `string` For a list of supported values, see [Resource service values](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-service).   
Supported operators | `==, !=`  
Details |  When you use the `resource.type` attribute in conditions, check for exact equality (`==`) or exact inequality (`!=`) with the attribute. Other comparisons, such as checking for a prefix or suffix, might give you unexpected results.   
Example |  Returns `true` for Compute Engine resources: 
    
    
    resource.service == "compute.googleapis.com"  
  
Supported services | 

  * Agent Registry
  * Apigee
  * Application Integration
  * Apigee API Hub
  * Backup and DR Service
  * BigQuery
  * BigQuery Reservation API
  * Bigtable
  * Binary Authorization
  * Cloud Deploy
  * Customer Experience Agent Studio
  * Cloud Key Management Service
  * Cloud Logging
  * Cloud SQL
  * Cloud Storage
  * Compute Engine
  * Dataform
  * Cloud DNS
  * Google Kubernetes Engine
  * Firestore
  * Identity-Aware Proxy
  * Integration Connectors
  * Google Cloud Managed Service for Apache Kafka
  * Network Security Integration
  * Parameter Manager
  * Cloud NGFW
  * Pub/Sub Lite
  * Resource Manager
  * Secret Manager
  * Spanner

  
  
### resource.type attribute

The `resource.type` attribute lets you set a condition based on the resource's type. For example, you could set a condition limiting a user's access to resources of the type `storage.googleapis.com/Object`. For a list of supported values, see [Resource type values](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-type).

If your condition uses the `resource.name` attribute, we strongly recommend that you use the `resource.type` attribute to control which resource types the condition applies to. For details, see `resource.name` attribute on this page.

You can use the `resource.type` attribute in allow policy role bindings.

Attribute variable | `resource.type`  
---|---  
Attribute type |  `string` For a list of supported values, see [Resource type values](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-type).   
Supported operators | `==, !=`  
Details |  When you use the `resource.type` attribute in conditions, check for exact equality (`==`) or exact inequality (`!=`) with the attribute. Other comparisons, such as checking for a prefix or suffix, might give you unexpected results.   
Examples |  Returns `true` unless the resource is a Compute Engine image: 
    
    
    resource.type != "compute.googleapis.com/Image"

Returns `true` only if the resource is a Compute Engine image or persistent disk: 
    
    
    (resource.type == "compute.googleapis.com/Image" ||
     resource.type == "compute.googleapis.com/Disk")  
  
Supported resource types |  | Agent Registry | 

  * Skills
  * Skill Revisions

  
---|---  
Apigee | 

  * API product attributes
  * API products
  * API proxies
  * API proxy key-value map entries
  * API proxy key-value maps
  * API proxy revisions
  * Caches
  * Developer app attributes
  * Developer apps
  * Developer attributes
  * Developers
  * Environment key-value map entries
  * Environment key-value maps
  * Exports
  * Flow hooks
  * Keystore aliases
  * Keystores
  * Queries
  * Rate plans
  * References
  * Shared flow revisions
  * Shared flows
  * Target servers
  * Trace (debug) sessions

  
Application Integration | 

  * Auth configs
  * Executions
  * Integration versions
  * Integrations
  * Locations
  * Suspensions

  
Apigee API Hub | 

  * APIs
  * API operations
  * Definitions
  * Deployments
  * Specs
  * Versions

  
Backup and DR Service | 

  * Backup vaults

  
BigQuery | 

  * Datasets
  * Models
  * Routines
  * Tables

  
BigQuery Reservation API | 

  * Assignments
  * BI reservations
  * Capacity commitments
  * Locations
  * Reservations

  
Bigtable | 

  * Clusters
  * Instances
  * Tables

  
Binary Authorization | 

  * Attestors
  * Continuous Validation configs
  * Policies

  
Customer Experience Agent Studio | 

  * Apps
  * Operations

  
Cloud Key Management Service | 

  * Crypto key versions
  * Crypto keys
  * Key rings
  * Locations

  
Cloud Logging | 

  * Log buckets
  * Log views

  
Cloud NGFW | 

  * Address groups
  * Firewall Endpoint Associations
  * Firewall Endpoints
  * Security Profile Groups
  * Security Profiles

  
Cloud SQL | 

  * Backup runs
  * Instances

  
Cloud Storage | 

  * Buckets
  * Folders (in buckets with hierarchical namespace enabled)
  * Managed folders
  * Objects

  
Compute Engine | 

  * Backend services (global and regional)
  * Firewalls
  * Forwarding rules (global and regional)
  * Images
  * Instance templates
  * Instances
  * Persistent disks (regional and zonal)
  * Snapshots
  * Target HTTP(S) proxies (global and regional)
  * Target SSL proxies
  * Target TCP proxies

  
Dataform | 

  * Compilation results
  * Locations
  * Release configs
  * Repositories
  * Workflow configs
  * Workflow invocations
  * Workspaces

  
Cloud DNS | 

  * resource record sets

  
Google Cloud | 

  * Locations1

  
Google Kubernetes Engine | 

  * Clusters

  
Firestore | 

  * Databases

  
Identity-Aware Proxy | 

  * All backend services and App Engine apps
  * All tunnel resources
  * All tunnel zones
  * All web services
  * App Engine app service versions
  * App Engine app services
  * Compute Engine backend services
  * Tunnel instances

  
Integration Connectors | 

  * Connections
  * Connection schema metadata
  * Endpoint attachments
  * Event subscriptions
  * Managed zones

  
Google Cloud Managed Service for Apache Kafka | 

  * Clusters
  * Consumer groups
  * Operations
  * Topics

  
Parameter Manager | 

  * Parameter versions
  * Parameters

  
Pub/Sub Lite | 

  * Locations
  * Subscriptions
  * Topics

  
Network Security Integration | 

  * Intercept Deployment Groups
  * Intercept Deployments
  * Intercept Endpoint Groups
  * Intercept Endpoint Group Associations
  * Mirroring Deployment Groups
  * Mirroring Deployments
  * Mirroring Endpoint Groups
  * Mirroring Endpoint Group Associations

  
Resource Manager | 

  * Projects

  
Secret Manager | 

  * Secret versions
  * Secrets

  
Spanner | 

  * Backups
  * Databases
  * Instances

  
  
1 Cloud Key Management Service uses this resource type as the parent of key ring resources.   
  
### resource.name attribute

The `resource.name` attribute lets you set a condition based on all or part of a resource name. For a list of resource name formats, see [Resource name format](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).

The `resource.name` attribute is available only for specific resource types, which are listed in the table in this section. We strongly recommend that you limit the applicability of the condition to the intended resource type. If a role contains permissions for a resource type that does not provide the `resource.name` attribute, you should ensure that those permissions are not restricted by the part of the condition that checks `resource.name`.

The following example shows how to ensure this behavior. In this example, the condition allows access to all resource types except Cloud Storage buckets and objects. In contrast, for buckets and objects, the condition only allows access to the bucket `example-bucket` and the objects it contains:
    
    
    (resource.type != 'storage.googleapis.com/Bucket' &&
     resource.type != 'storage.googleapis.com/Object') ||
    resource.name.startsWith('projects/_/buckets/example-bucket')
    

Note that the first part of the condition checks whether the resource is neither a bucket nor an object. If the resource has a different type, then the entire condition evaluates to `true`, regardless of the resource name.

Also, note that the condition checks the `resource.type` attribute, not the `resource.service` attribute. There are a few benefits of checking the `resource.type` attribute:

  * It limits the `resource.name` check to the appropriate set of resources. For example, if you want to grant access to Compute Engine instances with a specific name, it makes sense to exclude all resource types other than Compute Engine instances.
  * It prevents the scope of the condition from changing if a service adds new resource types in the future.



Finally, note that the condition uses the `startsWith()` function to evaluate the resource name, rather than checking for equality with the `==` operator. Because the condition looks at the start of the resource name, it matches a bucket as well as the objects in that bucket. If it checked for equality, it would only match the bucket.

You cannot use wildcard characters such as `*` to match multiple resource names. Consider these alternatives:

  * Use the `extract()` function to extract a value from a resource name. For example, you can extract a project ID from the resource name of a Compute Engine VM instance, then write a condition expression that refers to the project ID.

For details, see Extracting values from attributes on this page.

  * Use the `startsWith()` or `endsWith()` function to write a condition that evaluates the start or end of the resource name.




You can use the `resource.name` attribute in allow policy role bindings.

Attribute variable | `resource.name`  
---|---  
Attribute type |  `string` Each resource type uses a specific format for the resource name. For a list of formats, see [Resource name format](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).   
Supported functions and operators |  `startsWith(), endsWith(), extract(), ==, !=`  
Details |  The `resource.name` contains the [_relative resource name_](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) for the target resource in the request. The relative resource name is a URI path without a leading forward slash (`/`).  The `startsWith()` function takes the prefix string literal to be evaluated against `resource.name`.  The `endsWith()` function takes the suffix string literal to be evaluated against `resource.name`.  The `extract()` function uses an extraction template to extract part of `resource.name`. For details, see Extracting values from resource names on this page.  The `==` and `!=` operators are for comparison with the entire `resource.name`, or an extracted portion of the `resource.name`.   
Examples |  Returns `true` unless the resource name identifies a Cloud Storage bucket named `secret-bucket-123`: 
    
    
    resource.name != "projects/_/buckets/secret-bucket-123"

Returns `true` if the resource name starts with the specified prefix, in the format used by Compute Engine VM instances: 
    
    
    resource.name.startsWith("projects/project-123/zones/us-east1-b/instances/prod-")

Returns `true` if the resource name starts with the specified prefix, in the format used by Cloud Storage buckets: 
    
    
    resource.name.startsWith("projects/_/buckets/my_bucket/objects/test-object-")

Returns `true` if the resource name ends with the specified suffix—for example, the file extension of a Cloud Storage object: 
    
    
    resource.name.endsWith(".jpg")

Returns the project name or number if it's present: 
    
    
    resource.name.extract("projects/{project}/")  
  
Supported resource types |  | Agent Registry | 

  * Skills
  * Skill Revisions

  
---|---  
Apigee | 

  * API product attributes
  * API products
  * API proxies
  * API proxy key-value map entries
  * API proxy key-value maps
  * API proxy revisions
  * Caches
  * Developer app attributes
  * Developer apps
  * Developer attributes
  * Developers
  * Environment key-value map entries
  * Environment key-value maps
  * Exports
  * Flow hooks
  * Keystore aliases
  * Keystores
  * Queries
  * Rate plans
  * References
  * Shared flow revisions
  * Shared flows
  * Target servers
  * Trace (debug) sessions

  
Application Integration | 

  * Auth configs
  * Executions
  * Integration versions
  * Integrations
  * Locations
  * Suspensions

  
Apigee API Hub | 

  * APIs
  * API operations
  * Definitions
  * Deployments
  * Specs
  * Versions

  
Backup and DR Service | 

  * Backup vaults

  
BigQuery | 

  * Datasets
  * Models
  * Routines
  * Tables

  
BigQuery Reservation API | 

  * Assignments
  * BI reservations
  * Capacity commitments
  * Locations
  * Reservations

  
Bigtable | 

  * Clusters
  * Instances
  * Tables

  
Binary Authorization | 

  * Attestors
  * Continuous Validation configs
  * Policies

  
Cloud Deploy | 

  * Automation runs
  * Automations
  * Custom target types
  * Delivery pipelines
  * Job runs
  * Releases
  * Rollouts
  * Targets

  
Customer Experience Agent Studio | 

  * Apps
  * Operations

  
Cloud Key Management Service | 

  * Crypto keys
  * Crypto key versions
  * Key rings

  
Cloud Logging | 

  * Log buckets
  * Log views

  
Cloud NGFW | 

  * Address groups
  * Firewall Endpoint Associations
  * Firewall Endpoints
  * Security Profile Groups
  * Security Profiles

  
Cloud SQL | 

  * Backup runs
  * Instances

  
Cloud Storage | 

  * Buckets
  * Folders (in buckets with hierarchical namespace enabled)
  * Managed folders
  * Objects

  
Compute Engine | 

  * Backend services (global and regional)
  * Firewalls
  * Forwarding rules (global and regional)
  * Images
  * Instance templates
  * Instances
  * Persistent disks (regional and zonal)
  * Snapshots
  * Target HTTP(S) proxies (global and regional)
  * Target SSL proxies
  * Target TCP proxies

  
Google Kubernetes Engine | 

  * Clusters

  
Firestore | 

  * Databases

  
Dataform | 

  * Compilation results
  * Locations
  * Release configs
  * Repositories
  * Workflow configs
  * Workflow invocations
  * Workspaces

  
Cloud DNS | 

  * resource record sets

  
Integration Connectors | 

  * Connections
  * Connection schema metadata
  * Endpoint attachments
  * Event subscriptions
  * Managed zones

  
Google Cloud Managed Service for Apache Kafka | 

  * Clusters
  * Consumer groups
  * Operations
  * Topics

  
Parameter Manager | 

  * Parameter versions
  * Parameters

  
Pub/Sub Lite | 

  * Locations
  * Subscriptions
  * Topics

  
Network Security Integration | 

  * Intercept Deployment Groups
  * Intercept Deployments
  * Intercept Endpoint Groups
  * Intercept Endpoint Group Associations
  * Mirroring Deployment Groups
  * Mirroring Deployments
  * Mirroring Endpoint Groups
  * Mirroring Endpoint Group Associations

  
Secret Manager | 

  * Secret versions
  * Secrets

  
Spanner | 

  * Backups
  * Databases
  * Instances

  
  
### Resource tags

The resource tag functions let you set a condition based on the tags that are attached to [supported resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services#supported_service_resources) or inherited by those resources' descendants. For example, you can set a condition that grants a role only for resources that have the tag `env: prod` attached. To learn more about controlling access with tags, see [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control).

Each tag consists of a key and a value. There are a few different types of identifiers for each key and value:

  * A _permanent ID_ , which is globally unique and can never be reused. For example, a tag key could have the permanent ID `tagKeys/123456789012`, and a tag value could have the permanent ID `tagValues/567890123456`. 
  * A _short name_. The short name for each key must be unique within the project or organization under which the key is defined, and the short name for each value must be unique for its associated key. For example, a tag key could have the short name `env`, and a tag value could have the short name `prod`. 
  * A _namespaced name_ , which adds your organization's numeric ID or project's ID to the short name of a tag key. For example, a tag key created for an organization could have the namespaced name `123456789012/env`. To learn how to get your organization ID, see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). A tag key created for a project could have the namespaced name `myproject/env`. To learn how to get your project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 



For guidance on choosing which type of identifier to use in your conditions, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).

You can use tag-based conditions to conditionalize access to any resource. This includes resources with their own tags, as well as resources that inherit tags from other resources. To learn more about how tags are inherited through the resource hierarchy, see [Tag inheritance](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance).

However, certain areas of the Google Cloud console don't recognize allow policy role bindings with tag-based conditions. As a result, if you have a role with a tag-based condition, then the Google Cloud console might incorrectly prevent you from performing certain actions. If you encounter this issue, then use an alternate method, such as the gcloud CLI, to perform the action. 

You can use tag-based conditions in the following:

  * Allow policy role bindings
  * Deny policy deny rules



You can use the following functions to set conditions based on tags:

Function | Description  
---|---  
`resource.hasTagKey(  
keyName: string  
)` trending_flat `bool` |  Checks whether the resource for the request has a tag with the specified key. The tag key is looked up by its _namespaced name_. To check for a tag key using its _permanent ID_ , use the function `resource.hasTagKeyId()`. 

Parameter
     `keyName`: The namespaced name of the tag key, with the organization's numeric ID and a forward slash as a prefix. For example, `123456789012/env`. 
Example
     Returns `true` if the resource for the request has a tag with the key `env`: 
    
    
    resource.hasTagKey('123456789012/env')  
  
`resource.hasTagKeyId(  
keyId: string  
)` trending_flat `bool` |  Checks whether the resource for the request has a tag with the specified key. The tag key is looked up by its _permanent ID_. To check for a tag key using its _namespaced name_ , use the function `resource.hasTagKey()`. 

Parameter
     `keyId`: The permanent ID for the tag key. For example, `tagKeys/123456789012`. 
Example
     Returns `true` if the resource for the request has a tag with the key `tagKeys/123456789012`: 
    
    
    resource.hasTagKeyId('tagKeys/123456789012')  
  
`resource.matchTag(  
keyName: string,  
valueShortName: string  
)` trending_flat `bool` |  Checks whether the resource for the request has a tag with the specified key and value. The key is looked up by its _namespaced name_ , and the value is looked up by its _short name_. To check for a tag key and value using their _permanent IDs_ , use the function `resource.matchTagId()`. 

Parameters
    

  * `keyName`: The namespaced name for the tag key, with the organization's numeric ID and a forward slash as a prefix. For example, `123456789012/env`. 
  * `valueShortName`: The short name for the tag value. For example, `prod`. 


Example
     Returns `true` if the resource for the request has a tag with the key `123456789012/env` and the value `prod`: 
    
    
    resource.matchTag('123456789012/env', 'prod')  
  
`resource.matchTagId(  
keyId: string,  
valueId: string  
)` trending_flat `bool` |  Checks whether the resource for the request has a tag with the specified key and value. The key and value are looked up by their _permanent IDs_. To check for a tag key using its _namespaced name_ and a value using its _short name_ , use the function `resource.matchTag()`. 

Parameters
    

  * `keyId`: The permanent ID for the tag key. For example, `tagKeys/123456789012`. 
  * `valueId`: The permanent ID for the tag value. For example, `tagValues/567890123456`. 


Example
     Returns `true` if the resource for the request has a tag with the key `tagKeys/123456789012` and the value `tagValues/567890123456`: 
    
    
    resource.matchTagId('tagKeys/123456789012', 'tagValues/567890123456')  
  
## Principal attributes

The principal attributes let you write conditions based on the principal that issued the request. With these attributes, you can refine the principals that a policy is enforced for.

You can use principal attributes in policy bindings for Principal Access Boundary policies.

### `principal.type` attribute

The `principal.type` attribute lets you set a condition based on the type of principal issuing the request. For example, you could add a condition to a policy binding for a Principal Access Boundary policy to ensure that the policy is only enforced for service accounts.

You can use principal attributes in policy bindings for Principal Access Boundary policies.

Attribute variable | `principal.type`  
---|---  
Attribute type |  `string`  
Supported operators | `==, !=, in`  
Supported principal types | 

Google Accounts
    `iam.googleapis.com/WorkspaceIdentity`
Workforce identity pool identities
    `iam.googleapis.com/WorkforcePoolIdentity`
Workload identity pool identities 
    `iam.googleapis.com/WorkloadPoolIdentity`
Service accounts
    `iam.googleapis.com/ServiceAccount`
Agent identity
    `iam.googleapis.com/AgentPoolIdentity`  
Examples |  Evaluates to `true` if the principal in the request is a service account: 
    
    
    principal.type == "iam.googleapis.com/ServiceAccount"
            

Evaluates to `true` if the principal in the request is an agent identity: 
    
    
    principal.type == "iam.googleapis.com/AgentPoolIdentity"
            

Evaluates to `true` if the principal in the request is a Google Workspace identity or workforce identity pool identity: 
    
    
    principal.type in ["iam.googleapis.com/WorkspaceIdentity", "iam.googleapis.com/WorkforcePoolIdentity"]
              
  
### `principal.subject` attribute

The `principal.subject` attribute lets you set a condition based on the principal issuing the request. For example, you could add a condition to a policy binding for a Principal Access Boundary policy to ensure that the policy is only enforced for principals whose email addresses end with `@example.com`.

If you use the `principal.subject` attribute in a condition, we recommend also using the `principal.type` attribute to control which types of principals the condition applies to. This is because principal identifiers aren't necessarily unique across principal types. For example, the identifier `example-user@example.com` could identify a Google Account or a user in a workforce identity pool.

By using the `principal.type` attribute in addition to the `principal.subject` attribute, you can ensure that the condition only matches principals with the intended type. For example, the following expression matches Google Accounts whose email addresses end with `@example.com`:
    
    
    principal.type == 'iam.googleapis.com/WorkspaceIdentity' &&
    principal.subject.endsWith('@example.com')
    

**Note:** Conditions with this attribute evaluate against a principal's primary email address only—they don't evaluate against a principal's aliases.

You can use principal attributes in policy bindings for Principal Access Boundary policies.

Attribute variable | `principal.subject`  
---|---  
Attribute type |  `string`  
Supported operators |  `==, !=, in, startsWith(), endsWith()` Caution: The `startsWith()` and `endsWith()` functions match _all_ principals that start with or end with the specified value. For example, the expression `startsWith('security-admin')` matches `security-admin@example.com` and `security-admin@example-project.iam.gserviceaccount.com`, but also matches `security-admin-fake@example.com`.   
Supported principal subjects | 

Google Accounts
     Identifier: user's email address  Example: `alex@example.com`
Workforce identity pool identities
     Identifier: identity's subject attribute value  Example: `raha@altostrat.com`
Workload identity pool identities
     Identifier: identity's subject attribute value 
Service accounts
     Identifier: service account's email address  Example: `my-service-account@my-project.iam.gserviceaccount.com`
Agent identity
     Identifier: the agent identity, starting with `resources/` Example: `resources/aiplatform/projects/9876543210/locations/us-central1/reasoningEngines/my-test-agent`  
Example |  Evaluates to `true` if the principal in the request ends with `@example.com`: 
    
    
    principal.subject.endsWith("@example.com")
            

Evaluates to `true` if the principal in the request starts with `resources/aiplatform`, which is true for agent identities that use the Vertex AI platform: 
    
    
    principal.subject.startsWith("resources/aiplatform/")
            

Evaluates to `true` if the principal in the request is `example-service-account@example-project.iam.gserviceaccount.com`: 
    
    
    principal.subject == "example-service-account@example-project.iam.gserviceaccount.com"
              
  
## Request attributes

Request attributes enable you to create conditions that evaluate details about the request, such as its access level, its date and time, the destination IP address and port (for IAP TCP tunneling), or the expected URL path/host (for IAP and Cloud Run).

### Access levels attribute

The access levels attribute enables users to set a condition requiring that a request meets one or more access levels in order to be authorized. You can use the access levels attribute in allow policy role bindings.

The access levels attribute is derived from attributes of the request, such as the origin IP address, device attributes, and the time of day. For example, an access level named `fullyTrusted` might require that the device making the request is owned by the company and has a screen lock. An `onNetwork` access level might require that the device making the request originates from a particular IP address range. See the [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) documentation for more information about access levels.

The access levels attribute is available only when you use Identity-Aware Proxy either to access a tunnel instance or to access a web application that runs on App Engine or Compute Engine backend services. More specifically, the access levels attribute is available only for requests that check one of these permissions:

  * `iap.tunnelInstances.accessViaIAP`
  * `iap.webServiceVersions.accessViaIAP`

**Warning:** If you use the access levels attribute in a role binding, then the binding must grant a role that contains only the `iap.tunnelInstances.accessViaIAP` and `iap.webServiceVersions.accessViaIAP` permissions. If the binding grants a role that contains other permissions, then these additional, unsupported permissions won't work correctly.

You can use the access levels attribute when you conditionally grant the following predefined roles:

  * IAP-secured Tunnel User (`roles/iap.tunnelResourceAccessor`)

Contains a single permission, `iap.tunnelInstances.accessViaIAP`.

  * IAP-secured Web App User (`roles/iap.httpsResourceAccessor`)

Contains a single permission, `iap.webServiceVersions.accessViaIAP`.




You can also use the access levels attribute to conditionally grant a custom role that contains these permissions. The custom role must not contain any other permissions.

#### `request.auth.access_levels` attribute

Attribute variable | `request.auth.access_levels`  
---|---  
Attribute type | `list`<`string`>  
Supported operators | `in`  
Details |  To check whether a request meets a specific access level, use the `in` operator: 
    
    
    ACCESS_LEVEL_FULL_NAME in request.auth.access_levels

The full name of an access level uses the following format: 
    
    
    accessPolicies/POLICY_NUMBER/accessLevels/ACCESS_LEVEL

**Note:** The access level is case sensitive, and it must match exactly what is configured in Access Context Manager. For example, if the condition uses `accesslevels`, in all lowercase, rather than `accessLevels`, with `Levels` capitalized, then the access level in the request will never match the access level in the condition.   
Example |  Returns `true` if the request meets the `CorpNet` access level: 
    
    
    "accessPolicies/199923665455/accessLevels/CorpNet"
        in request.auth.access_levels  
  
Supported resource types |  Available for requests that use Identity-Aware Proxy to access a tunnel instance, tunnel destination group, web application running on Google Cloud load balancing, or web application running on App Engine.   
  
### API attributes

API attributes help you manage access based on data provided by a specific Google Cloud API or service. You can use API attributes in allow policy role bindings.

For example, when you use Cloud Storage to [list the objects in a bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list), you can use the `prefix` parameter in the request to include only objects whose names begin with a specific prefix. If you use [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials) to downscope short-lived credentials, you can create a Credential Access Boundary that limits permissions to list objects by checking the API attribute `storage.googleapis.com/objectListPrefix`. This API attribute contains the value of the `prefix` parameter from the request.

For examples of when you might need to use API attributes in a condition, see the following pages:

  * [Limit permissions when listing objects](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials#example-object-prefix)
  * [Setting limits on granting roles](https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles)



Not all services recognize API attributes. The following sections indicate which services recognize each API attribute.

#### Functions for API attributes

You can use the following function to work with API attributes:

Function | Description  
---|---  
`api.getAttribute(  
attributeName: string,  
defaultValue: V<T>  
)` trending_flat `V<T>` |  Gets the requested API attribute.

Parameters
    

  * `attributeName`: The API attribute to get. For supported values, see Cloud Storage API attributes and IAM API attributes on this page. 
  * `defaultValue`: The default value (`V`) to use if the API attribute is not available. The value `V` is of type `T`, where `T` is the same type as the API attribute's value. For example, if the API attribute's value is a string, you can use an empty string, or a placeholder string such as `undefined`.  **Note:** For the API attribute `iam.googleapis.com/modifiedGrantsByRole`, the default value must be an empty list (`[]`). 


Example
     Returns one of the following: 

  * For requests to grant or revoke a role, returns a list of roles that were modified by the request. 
  * For all other types of requests, returns an empty list. 


    
    
    api.getAttribute("iam.googleapis.com/modifiedGrantsByRole", [])  
  
`hasOnly(  
items: list<T>  
)` trending_flat `bool` |  Checks that a list contains only the allowed items, or a subset of those items. You can call the function on a list returned by `api.getAttribute()`. 

Parameter
     `items`: A list of items with type `T`. Each item is a value that the API attribute is allowed to contain. 
Example
     Checks whether the request would grant or revoke any roles other than Pub/Sub Editor (`roles/pubsub.editor`) or Pub/Sub Publisher (`roles/pubsub.publisher`): 
    
    
    api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', [])
        .hasOnly(['roles/pubsub.editor', 'roles/pubsub.publisher'])

The following shows the result for different request values:  | Granted/revoked roles | Result  
---|---  
None |  `true` If no roles are modified, then `api.getAttribute()` returns the default value. For this attribute, the default value is always an empty list. By definition, an empty list does not contain values that are not on the allowlist.   
`roles/pubsub.editor` |  `true` The role is on the allowlist.   
`roles/pubsub.editor`  
`roles/pubsub.publisher` |  `true` Both roles are on the allowlist.   
`roles/billing.admin` |  `false` The role is not on the allowlist.   
`roles/billing.admin`  
`roles/pubsub.editor` |  `false` One role is on the allowlist, but the other is not.   
  
#### Cloud Storage API attributes

Cloud Storage provides the following API attribute.

**Warning:** API attributes for Cloud Storage are supported only in [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials). If you use Cloud Storage API attributes in a conditional role binding, then Cloud Storage methods will work incorrectly and fail unexpectedly. In addition, it might take longer to check IAM permissions when you access Cloud Storage. Attribute variable | `storage.googleapis.com/objectListPrefix`  
---|---  
Attribute type | `string`  
Details |  For a request to [list objects in a bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list), contains the value of the `prefix` parameter from the request. If the request omits the `prefix` parameter, the attribute is not defined.  For other types of requests, the attribute is not defined.   
Services that recognize this attribute | Cloud Storage  
  
#### IAM API attributes

IAM provides the following API attribute:

Attribute variable | `iam.googleapis.com/modifiedGrantsByRole`  
---|---  
Attribute type | `list<string>`  
Details |  For a request to [set the allow policy](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) of a resource, this attribute contains the role names from the role bindings that the request modifies.  For other types of requests, the attribute is not defined.   
Resource types that accept this attribute |  The following resource types accept conditions with the `modifiedGrantsByRole` attribute in their allow policies: 

  * Projects
  * Folders
  * Organizations

  
Services that recognize this attribute |  The following services recognize the `modifiedGrantsByRole` attribute:  **Caution:** If a service does not recognize the `modifiedGrantsByRole` attribute, you cannot [limit an IAM admin's ability to grant roles](https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles) for that service. If a limited IAM admin tries to grant a role on a resource, and the resource's service does not recognize the `modifiedGrantsByRole` attribute, then the request fails.  The exception to this behavior is [BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets). Datasets don't recognize the `modifiedGrantsByRole` attribute, but limited IAM admins can still grant or revoke roles on datasets. Specifically, if a limited IAM admin's role includes permissions to grant roles on datasets, **they can do so** , regardless of any limits placed on their role granting. 

  * API Gateway
  * AutoML
  * Certificate Authority Service
  * Cloud Run functions
  * Cloud Healthcare API
  * Cloud Key Management Service
  * Cloud Run
  * Cloud Runtime Configuration API
  * Cloud Storage
  * Compute Engine
  * Artifact Analysis
  * Managed Service for Apache Spark
  * Earth Engine
  * Game Servers
  * Identity and Access Management
  * Identity-Aware Proxy
  * Managed Service for Microsoft Active Directory
  * User-managed notebooks
  * Resource Manager
  * Secret Manager
  * Service Management

  
  
#### MCP API attributes

Google Cloud provides the following attributes for controlling access to MCP servers:

Attribute variable | `mcp.googleapis.com/tool.name`  
---|---  
Attribute type | `string`  
Details |  For requests that accesses an MCP tool, this attribute contains name of the tool.  For example, if the request accesses the BigQuery MCP tool [`list_dataset_ids`](https://docs.cloud.google.com/bigquery/docs/reference/mcp/tools_list/list_dataset_ids), then the `tool.name` attribute for the request is `list_dataset_ids`.  For other types of requests, this attribute isn't defined.   
Services that recognize this attribute |  All Google Cloud services with MCP servers recognize this API attribute. For a list of services with MCP servers, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).   
Attribute variable | `mcp.googleapis.com/tool.isReadOnly`  
---|---  
Attribute type | `boolean`  
Details |  For requests that accesses an MCP tool, this attribute indicates whether the tool is a read-only tool.  For other types of requests, this attribute isn't defined.   
Services that recognize this attribute |  All Google Cloud services with MCP servers recognize this API attribute. For a list of services with MCP servers, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).   
  
#### Vertex AI Agent Engine API attributes

Vertex AI Agent Engine provides the following API attributes for its [Memory Bank](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview) and [Session](https://docs.cloud.google.com/agent-builder/agent-engine/sessions/overview) context management services:

Attribute variable | `aiplatform.googleapis.com/memoryScope`  
---|---  
Attribute type | `map<string, string>`  
Details |  For a request that accesses or modifies [Memory Bank](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview) resources, contains the value of the `scope` field within the Memory.  For other types of requests, the attribute is not defined.   
Services that recognize this attribute | Vertex AI Agent Engine  
Attribute variable | `aiplatform.googleapis.com/sessionUserId`  
---|---  
Attribute type | `string`  
Details |  For a request that accesses or modifies [Session](https://docs.cloud.google.com/agent-builder/agent-engine/sessions/overview) resources, contains the value of the `user_id` field within the Session.  For other types of requests, the attribute is not defined.   
Services that recognize this attribute | Vertex AI Agent Engine  
  
### Date/time attribute

The date/time attribute is used to set expirable, scheduled, or limited-duration access to Google Cloud resources. You can use date/time attributes in allow policy role bindings.

This attribute is supported for all Google Cloud services and resource types. To learn how to apply date/time conditions to resources that don't directly support them, see Support for inherited conditions on this page.

The `request.time` attribute contains the timestamp for the request. You can compare this timestamp to another timestamp, or to a duration of time.

The following sections list the functions that you can use to set conditions based on timestamps and durations.

#### Create, compare, and modify timestamps and durations

Function or operator | Description  
---|---  
`date(  
value: string  
)` trending_flat `Timestamp` |  Converts a date from a `string` to a `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. 

Parameter
     `value`: A date in the format `YYYY-MM-DD`, where `YYYY` is the year, `MM` is the two-digit month, and `DD` is the two-digit day. The resulting `Timestamp` contains the specified date and the time `00:00:00.000 UTC`. 
Example
     Creates a `Timestamp` that represents the date `2023-02-01` and the time `00:00:00.000 UTC`: 
    
    
    date("2023-02-01")  
  
`duration(  
value: string  
)` trending_flat `[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration)` |  Converts an amount of time from a `string` to a `[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration)`. 

Parameter
     `value`: A `Duration` in seconds, followed by `s`. 
Examples
     Creates a duration that represents 1.5 minutes:
    
    
    duration("90s")

Creates a duration that represents 30 days:
    
    
    duration("2592000s")  
  
`timestamp(  
value: string  
)` trending_flat `Timestamp` |  Converts a `string` to a `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`.

Parameter
     `value`: A UTC timestamp that complies with [RFC 3339](https://tools.ietf.org/html/rfc3339).  **Important:** If the input parameter is invalid, then the condition will never allow access to any resource. 
Example
     Creates a timestamp that represents April 12, 2023, at 23:20:50.52 in UTC: 
    
    
    timestamp("2023-04-12T23:20:50.52Z")  
  
`<, <=, >, >=` |  Compares two `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)` values.  **Note:** Avoid using the equality (`==`) and inequality (`!=`) operators to compare timestamps. Timestamps have millisecond precision, so it's typically not useful to check for exact matches or mismatches. 

Examples
     Returns `true` if the request time is _before_ April 12, 2022, at 00:00:00 UTC: 
    
    
    request.time < timestamp("2022-04-12T00:00:00.00Z")

Returns `true` if the request time is _before or equal to_ April 12, 2022, at 00:00:00 UTC: 
    
    
    request.time <= timestamp("2022-04-12T00:00:00.00Z")

Returns `true` if the request time is _after_ April 12, 2022, at 00:00:00 UTC: 
    
    
    request.time > timestamp("2022-04-12T00:00:00.00Z")

Returns `true` if the request time is _after or equal to_ April 12, 2022, at 00:00:00 UTC: 
    
    
    request.time >= timestamp("2022-04-12T00:00:00.00Z")  
  
  * `timestamp + duration` trending_flat `Timestamp`
  * `timestamp - duration` trending_flat `Timestamp`

|  Add or subtract a `[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration)` from a `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`.

Examples
     Returns the `Timestamp` that falls 30 minutes after 14:30:00 UTC on 2024-04-12: 
    
    
    timestamp("2024-04-12T14:30:00.00Z") + duration("1800s")

Returns the `Timestamp` that falls 60 days before 14:30:00 UTC on 2024-04-12: 
    
    
    timestamp("2024-04-12T14:30:00.00Z") - duration("5184000s")  
  
#### Extract information from a timestamp

The functions in this section let you extract information from a timestamp, such as the day of the week that the timestamp falls on.

In IAM Conditions, all timestamps are in UTC. However, you might want to extract information based on a different time zone. For example, you might want to know whether a UTC timestamp falls on a Monday in the time zone for Berlin, Germany.

To specify a different time zone, pass the time zone into the function. Use a name or UTC offset from the [IETF Time Zone Database](https://wikipedia.org/wiki/List_of_tz_database_time_zones). For example, you could use `Europe/Berlin` or `+01:00` for Central European Time (CET).

Supported functions and operators | Description  
---|---  
`Timestamp.getDate(  
timeZone: string  
)` trending_flat `int` |  Gets the day of the month from the `Timestamp`. The value uses one-based indexing; the first day of the month is `1`. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC. 
Example
     Returns `true` if the request is sent after the 15th day of the month in UTC: 
    
    
    request.time.getDate() > 15  
  
`Timestamp.getDayOfMonth(  
timeZone: string  
)` trending_flat `int` |  Gets the day of the month from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. The value uses zero-based indexing; the first day of the month is `0`. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC. 
Example
     Returns `true` if the request is sent after the 15th day of the month in UTC: 
    
    
    request.time.getDayOfMonth() > 14  
  
`Timestamp.getDayOfWeek(  
timeZone: string  
)` trending_flat `int` |  Gets the day of the week from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. The value uses zero-based indexing; for example, Sunday is `0`. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC. 
Example
     Returns `true` if the request is sent between Monday and Friday in Berlin, Germany: 
    
    
    request.time.getDayOfWeek("Europe/Berlin") > 0 &&
        request.time.getDayOfWeek("Europe/Berlin") < 6  
  
`Timestamp.getDayOfYear(  
timeZone: string  
)` trending_flat `int` |  Gets the day of the year from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. The value uses zero-based indexing; the first day of the year is `0`. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC. 
Example
     Returns `true` if the request is sent during the first 5 days of the year in Mountain View, California: 
    
    
    request.time.getDayOfYear("America/Los_Angeles") >= 0 &&
        request.time.getDayOfYear("America/Los_Angeles") < 5  
  
`Timestamp.getFullYear(  
timeZone: string  
)` trending_flat `int` |  Gets the year from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC. 
Example
     Returns `true` if the request is sent during the year 2023 in Mountain View, California: 
    
    
    request.time.getFullYear("America/Los_Angeles") == 2023

Returns `true` if the request is sent during the year 2022 in UTC: 
    
    
    request.time.getFullYear() == 2022  
  
`Timestamp.getHours(  
timeZone: string  
)` trending_flat `int` |  Gets the hour of the day from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. The value uses zero-based indexing; values range from `0` to `23`.  You can combine this function with `getDayofWeek()` to grant access only during the permitted working hours in your jurisdiction. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC. 
Example
     Returns `true` if the request is sent between 09:00 (9:00 AM) and 17:00 (5:00 PM) on a weekday in Berlin, Germany: 
    
    
    request.time.getDayOfWeek("Europe/Berlin") >= 1 &&
        request.time.getDayOfWeek("Europe/Berlin") <= 5 &&
        request.time.getHours("Europe/Berlin") >= 9 &&
        request.time.getHours("Europe/Berlin") <= 17  
  
`Timestamp.getMilliseconds(  
timeZone: string  
)` trending_flat `int` |  Gets the number of milliseconds from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. The value uses zero-based indexing; values range from `0` to `999`.  **Note:** In general, when you use IAM Conditions, you won't need to evaluate timestamps with this level of precision. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC.   
`Timestamp.getMinutes(  
timeZone: string  
)` trending_flat `int` |  Gets the number of minutes after the hour from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. The value uses zero-based indexing; values range from `0` to `59`. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC. 
Example
     Returns `true` if the request is sent at or after 09:30 (9:30 AM) in Berlin, Germany: 
    
    
    request.time.getHours("Europe/Berlin") >= 9 &&
        request.time.getMinutes("Europe/Berlin") >= 30  
  
`Timestamp.getMonth(  
timeZone: string  
)` trending_flat `int` |  Gets the month of the year from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. The value uses zero-based indexing; values range from `0` to `11`. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC. 
Example
     Returns `true` if the request is sent during the month of April in Mountain View, California: 
    
    
    request.time.getMonth("America/Los_Angeles") == 3  
  
`Timestamp.getSeconds(  
timeZone: string  
)` trending_flat `int` |  Gets the number of seconds from the `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. The value uses zero-based indexing; values range from `0` to `59`.  **Note:** In general, when you use IAM Conditions, you won't need to evaluate timestamps with this level of precision. 

Parameter
     `timeZone`: The time zone for which to calculate the result. Defaults to UTC.   
`<, <=, >, >=, ==, !=` |  Compares the output of two functions in this table.   
  
### Destination IP/port attributes

The destination IP/port attribute enables users to manage access based on the internal destination IP address and port for a request. You can use destination IP/port attributes in allow policy role bindings.

For example, a Compute Engine VM instance might map the external IP address and port `132.168.42.21:3001` to the internal IP address and port `10.0.0.1:2300` for general usage. In contrast, the internal IP address and port `10.0.0.1:22` might only be available internally for administrative usage. You can use the destination IP/port attributes to grant different amounts of access based on the internal IP address and port.

For more information about TCP forwarding, see the [Identity-Aware Proxy documentation](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview).

#### destination.ip attribute

Attribute variable | `destination.ip`  
---|---  
Attribute type | `string`  
Supported operators | `==, !=`  
Details |  The variable `destination.ip` identifies an internal IP address in IPv4 format.  **Note:** We don't recommend using the `startsWith()` and `endsWith()` functions with the `destination.ip` attribute. These functions might give you unexpected results. In particular, we don't recommend matching a prefix in `destination.ip` to check a CIDR address range.   
Examples |  Returns `true` if the destination IP address is `10.0.0.1`: 
    
    
    destination.ip == "10.0.0.1"

Returns `true` unless the destination IP address is `10.0.0.1`: 
    
    
    destination.ip != "10.0.0.1"  
  
Supported resource types |  Available for requests that use Identity-Aware Proxy to access a tunnel instance   
  
#### destination.port attribute

Attribute variable | `destination.port`  
---|---  
Attribute type | `int`  
Supported operators | `==, !=, <, <=, >, >=`  
Details |  The variable `destination.port` identifies an internal TCP port number.   
Examples |  Returns `true` if the destination port is `21`: 
    
    
    destination.port == 21

Returns `true` if the destination port is less than `3001`: 
    
    
    destination.port < 3001  
  
Supported resource types |  Available for requests that use Identity-Aware Proxy to access a tunnel instance   
  
### Forwarding rule attributes

The forwarding rule attributes enable you to specify the types of [forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) that a principal can create. For example, you could allow a principal to create forwarding rules for [internal Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#types-of-cloud-load-balancing), which handle traffic that originates inside a Google Cloud network, but not for external Google Cloud load balancers, which handle traffic that originates from the internet. You can use forwarding rule attributes in allow policy role bindings.

For Cloud Load Balancing, the forwarding rule attributes don't affect the ability to create other components of a Google Cloud load balancer, such as backend services, target proxies, health checks, and URL maps.

**Note:** In the Google Cloud console, if you want to include the forwarding rule attributes in a condition expression, you must use the Condition editor. The forwarding rule attributes are not available in the Condition builder.

#### Supported functions

Function | Description  
---|---  
`compute.isForwardingRuleCreationOperation()` trending_flat `bool` |  Checks whether the request is creating a [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts). 

Example
     See the example for `compute.matchLoadBalancingSchemes()`.   
`compute.matchLoadBalancingSchemes(  
schemes: list<string>  
)` trending_flat `bool` |  Checks whether the request affects one of the specified types of load balancing scheme. To find the identifier for each load balancing scheme, as well as more details, see [Using IAM Conditions on Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions#conditions-iam).  **Note:** In general, if you use this function in a condition expression, you should also use `compute.isForwardingRuleCreationOperation()`. See the examples in this cell for details. 

Parameter
     `schemes`: The load balancing schemes that the request is allowed to affect. 
Example
     Returns one of the following:

  * If the request _is not_ creating a forwarding rule, returns `true`. 
  * If the request _is_ creating a forwarding rule, returns `true` only if the forwarding rule affects an `INTERNAL`, `INTERNAL_MANAGED`, or `INTERNAL_SELF_MANAGED` load balancing scheme. 


    
    
    !compute.isForwardingRuleCreationOperation() || (
      compute.isForwardingRuleCreationOperation() &&
      compute.matchLoadBalancingSchemes([
        'INTERNAL', 'INTERNAL_MANAGED', 'INTERNAL_SELF_MANAGED'
      ])
    )  
  
#### Supported resource types

This attribute is available for requests to create the following resource types:

Service | Resource types  
---|---  
Cloud Load Balancing |  Forwarding rules   
Cloud VPN |  Forwarding rules (global and regional)   
Compute Engine |  Forwarding rules (for [protocol forwarding)](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding)  
Cloud Service Mesh1 |  Forwarding rules   
  
1 Uses the [resource attributes](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes) for Compute Engine.

### URL path/host attribute

The URL path/host attribute enables users to manage access based on the URL path and host of a request. For example, a condition could specify that `https://example.com` is the main application accessible by a general domain of users, while `https://hr.example.com/admin` is used to access a page in the application where only Human Resources admins can access this portion.

You can use the URL path/host attribute in allow policy role bindings.

#### request.path attribute

Attribute variable | `request.path`  
---|---  
Attribute type | `string`  
Supported functions and operators | `==, startsWith(), endsWith()`  
Details |  We don't recommend using the `!=` operator with this attribute. Instead of checking for inequality, as in `request.path != "/admin"`, check the attribute's prefix, as in `!request.path.startsWith("/admin")`. By checking the prefix, you also protect URL paths within the `/admin` hierarchy, such as `/admin/payroll/`.   
Examples |  Returns `true` if the request path is equal to the specified URL path: 
    
    
    request.path == "/admin"
    
    
    request.path == "/admin/payroll"

Returns `true` if the request path starts with the specified URL path: 
    
    
    request.path.startsWith("/admin")

Returns `true` if the request path ends with the specified URL path: 
    
    
    request.path.endsWith("/payroll.js")  
  
Supported resource types | 

  * Identity-Aware Proxy app service versions (App Engine): Available for requests that use Identity-Aware Proxy to access a web application running on App Engine or Compute Engine 
  * Cloud Run services 

  
  
#### request.host attribute

Attribute variable | `request.host`  
---|---  
Attribute type | `string`  
Supported functions and operators | `==, endsWith()`  
Details |  We don't recommend using the `.startsWith()` function or the `!=` operator with this attribute. These functions and operators might give you unexpected results.   
Examples |  Returns `true` if the hostname is equal to the specified value: 
    
    
    request.host == "www.example.com"
    
    
    request.host == "hr.example.com"

Returns `true` if the hostname ends with the specified value: 
    
    
    request.host.endsWith("example.com")  
  
Supported resource types | 

  * Identity-Aware Proxy app service versions (App Engine): Available for requests that use Identity-Aware Proxy to access an app service version. 
  * Cloud Run services 

  
  
## Extract values from attributes

You can use the `extract()` function to extract a value from an attribute. For example, you can extract an arbitrary part of a resource name, then write a condition expression that refers to the text you extracted.

To use the `extract()` function, you provide an _extraction template_ , which specifies the part of the attribute to extract. For example, if you want to extract a project ID from the resource name of a Compute Engine VM instance, you might use the template `projects/{project}/`.

An extraction template contains the following parts:

  * An _identifier_ , enclosed in curly braces, that identifies the substring to extract.

Choose a short, meaningful identifier that makes it clear what value you want to extract. You can use uppercase and lowercase letters from `A` to `Z`; numeric digits; and underscores (`_`).

In the template `projects/{project}/`, the identifier is `project`.

  * Optional: A _prefix_ , which must appear before the substring to extract.

In the template `projects/{project}/`, the prefix is `projects/`.

  * Optional: A _suffix_ , which must appear after the substring to extract.

In the template `projects/{project}/`, the suffix is `/`.




The `extract()` function extracts different parts of the attribute based on whether the extraction template has a prefix, a suffix, or both:

Has prefix | Has suffix | Extracted value | — | — | The entire attribute  
---|---|---  
check | — |  The characters after the first occurrence of the prefix, or an empty string if there are no characters after the prefix   
— | check |  The characters before the first occurrence of the suffix, or an empty string if there are no characters before the suffix   
check | check |  The characters between the first occurrence of the prefix and the first subsequent occurrence of the suffix, or an empty string if there are no characters between the prefix and the suffix   
  
If you specify a prefix or suffix that don't appear in the attribute, or if the suffix appears only before the prefix, the `extract()` function returns an empty string.

The following examples show the output from several different extraction templates. These examples refer to a resource name for a Cloud Storage object, `projects/_/buckets/acme-orders-aaa/objects/data_lake/orders/order_date=2019-11-03/aef87g87ae0876`:

Extraction template | Output  
---|---  
`/order_date={date}/` | `2019-11-03`  
`buckets/{name}/` | `acme-orders-aaa`  
`/orders/{empty}order_date` | Empty `string`  
`{start}/objects/data_lake` | `projects/_/buckets/acme-orders-aaa`  
`orders/{end}` | `order_date=2019-11-03/aef87g87ae0876`  
`{all}` | `projects/_/buckets/acme-orders-aaa/objects/data_lake/orders/order_date=2019-11-03/aef87g87ae0876`  
`/orders/{none}/order_date=` | Empty `string`  
`/orders/order_date=2019-11-03/{id}/data_lake` | Empty `string`  
  
If you extract a string that represents a date, you can use the date/time functions and operators on this page to convert the extracted value to a `[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp)`. For examples, see [Configuring resource-based access](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access#extract-values).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
