---
url: https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListRolesRequestOrBuilder
title: Interface ListRolesRequestOrBuilder (3.94.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:40.496277+00:00
---

# Interface ListRolesRequestOrBuilder (3.94.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListRolesRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListRolesRequestOrBuilder (3.94.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.94.0 (latest)  3.90.0  3.89.0  3.88.0  3.86.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.73.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.65.0  3.63.0  3.62.0  3.59.0  3.58.0  3.57.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.0.0  1.2.5  1.1.8  0.2.0 
    
    
    public interface ListRolesRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPageSize()
    
    
    public abstract int getPageSize()

Optional limit on the number of roles to include in the response.

The default is 300, and the maximum is 1,000.

`int32 page_size = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

Optional pagination token returned in an earlier ListRolesResponse.

`string page_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

Optional pagination token returned in an earlier ListRolesResponse.

`string page_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getParent()
    
    
    public abstract String getParent()

The `parent` parameter's value depends on the target resource for the request, namely [`roles`](https://cloud.google.com/iam/reference/rest/v1/roles), [`projects`](https://cloud.google.com/iam/reference/rest/v1/projects.roles), or [`organizations`](https://cloud.google.com/iam/reference/rest/v1/organizations.roles). Each resource type's `parent` value format is described below:

  * [`roles.list()`](https://cloud.google.com/iam/reference/rest/v1/roles/list): An empty string. This method doesn't require a resource; it simply returns all [predefined roles](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles) in Cloud IAM. Example request URL: `<https://iam.googleapis.com/v1/roles>`

  * [`projects.roles.list()`](https://cloud.google.com/iam/reference/rest/v1/projects.roles/list): `projects/{PROJECT_ID}`. This method lists all project-level [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles). Example request URL: `https://iam.googleapis.com/v1/projects/{PROJECT_ID}/roles`

  * [`organizations.roles.list()`](https://cloud.google.com/iam/reference/rest/v1/organizations.roles/list): `organizations/{ORGANIZATION_ID}`. This method lists all organization-level [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles). Example request URL: `https://iam.googleapis.com/v1/organizations/{ORGANIZATION_ID}/roles`

Note: Wildcard (*) values are invalid; you must specify a complete project ID or organization ID.




`string parent = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

The `parent` parameter's value depends on the target resource for the request, namely [`roles`](https://cloud.google.com/iam/reference/rest/v1/roles), [`projects`](https://cloud.google.com/iam/reference/rest/v1/projects.roles), or [`organizations`](https://cloud.google.com/iam/reference/rest/v1/organizations.roles). Each resource type's `parent` value format is described below:

  * [`roles.list()`](https://cloud.google.com/iam/reference/rest/v1/roles/list): An empty string. This method doesn't require a resource; it simply returns all [predefined roles](https://cloud.google.com/iam/docs/understanding-roles#predefined_roles) in Cloud IAM. Example request URL: `<https://iam.googleapis.com/v1/roles>`

  * [`projects.roles.list()`](https://cloud.google.com/iam/reference/rest/v1/projects.roles/list): `projects/{PROJECT_ID}`. This method lists all project-level [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles). Example request URL: `https://iam.googleapis.com/v1/projects/{PROJECT_ID}/roles`

  * [`organizations.roles.list()`](https://cloud.google.com/iam/reference/rest/v1/organizations.roles/list): `organizations/{ORGANIZATION_ID}`. This method lists all organization-level [custom roles](https://cloud.google.com/iam/docs/understanding-custom-roles). Example request URL: `https://iam.googleapis.com/v1/organizations/{ORGANIZATION_ID}/roles`

Note: Wildcard (*) values are invalid; you must specify a complete project ID or organization ID.




`string parent = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getShowDeleted()
    
    
    public abstract boolean getShowDeleted()

Include Roles that have been deleted.

`bool show_deleted = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The showDeleted.  
  
### getView()
    
    
    public abstract RoleView getView()

Optional view for the returned Role objects. When `FULL` is specified, the `includedPermissions` field is returned, which includes a list of all permissions in the role. The default value is `BASIC`, which does not return the `includedPermissions` field.

`.google.iam.admin.v1.RoleView view = 4;`

**Returns**  
---  
**Type** | **Description**  
`[RoleView](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.RoleView)` | The view.  
  
### getViewValue()
    
    
    public abstract int getViewValue()

Optional view for the returned Role objects. When `FULL` is specified, the `includedPermissions` field is returned, which includes a list of all permissions in the role. The default value is `BASIC`, which does not return the `includedPermissions` field.

`.google.iam.admin.v1.RoleView view = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for view.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
