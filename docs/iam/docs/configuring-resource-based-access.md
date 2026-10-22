---
url: https://docs.cloud.google.com/iam/docs/configuring-resource-based-access/
title: Configure resource-based access \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:51.752436+00:00
---

# Configure resource-based access  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/configuring-resource-based-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure resource-based access Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage access to specific resources using conditional role bindings in your allow policies. By using [resource attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource) in a condition expression, you can control whether a principal can use a permission to access a resource based on the resource's name, type, and Google Cloud service.

**Note:** The examples on this page show how to modify access to a [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). However, you can adapt these steps to modify access to any Google Cloud resource that accepts IAM allow policies. For a list of these resource types, see [Resource types that accept allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies). 

## Before you begin

  * Read the [Identity and Access Management (IAM) Conditions overview](https://docs.cloud.google.com/iam/docs/conditions-overview) to understand the basics of IAM conditional role bindings.
  * Review the [resource attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource) that can be used in a condition expression.
  * The resource name attribute can control access to the following Google Cloud services: 
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

**Important:** Review Important usage considerations for resource-based conditions at the bottom of this page before applying a condition of this type in a production environment.

### Required roles

To get the permissions that you need to manage conditional role bindings, ask your administrator to grant you the following IAM roles: 

  * To manage access to projects: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project 
  * To manage access to folders: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) on the folder 
  * To manage access to projects, folders, and organizations: [Organization Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) on the organization 
  * To manage access to almost all Google Cloud resources: [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) on the project, folder, or organization whose resources you want to manage access to 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage conditional role bindings. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage conditional role bindings:

  * To manage access to projects: 
    * `resourcemanager.projects.getIamPolicy` on the project
    * `resourcemanager.projects.setIamPolicy` on the project
  * To manage access to folders: 
    * `resourcemanager.folders.getIamPolicy` on the folder
    * `resourcemanager.folders.setIamPolicy` on the folder
  * To manage access to organizations: 
    * `resourcemanager.organizations.getIamPolicy` on the organization
    * `resourcemanager.organizations.setIamPolicy` on the organization



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Grant access to a group of resources based on resource name prefixes

A conditional role binding can be used to grant access to principals for resources whose resource names match a prefix, such as Compute Engine virtual machine (VM) instances whose names start with a certain string. The resource name prefix is typically used to group resources intended for certain purpose or that have certain properties.

**Note:** Conditional role bindings do not override role bindings with no conditions. If a principal is bound to a role, and the role binding does not have a condition, then the principal always has that role. Adding the principal to a conditional binding for the same role has no effect. 

For example, imagine that you run workloads on certain VM instances that may operate on sensitive healthcare data. Other non-sensitive workloads must run in the same project, and you want to ensure that your developers have limited access to VM instances that operate on sensitive data. To accomplish this goal, you name data-sensitive VM instances with a `sensitiveAccess` prefix, and other VM instances with a `devAccess` prefix. Then, you use conditional role bindings to ensure that the developers can remain productive with normal `devAccess` VM instances, but without granting them access to `sensitiveAccess` VM instances.

While you can use the `resource.name` condition attribute alone to manage access, it's common to use the `resource.type` and `resource.service` attributes as well. When you use these additional attributes, you make it less likely that a condition will affect access to different resource types with similar names. In addition, you can limit the scope of the condition so that principals can still use permissions in the role to access other resource types or services. The example in this section controls access using both the `resource.name` and `resource.type` attributes. For more information about scoping conditions at the container resource level, see the Inherited conditions section of this document.

**Note:** You cannot use conditions when you grant [legacy basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic), including Owner (`roles/owner`), Editor (`roles/editor`), and Viewer (`roles/viewer`). Also, you cannot use conditions when you grant roles to all users ([`allUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allusers)) or all authenticated users ([`allAuthenticatedUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allauthenticatedusers)). 

To grant access based on a name prefix to Compute Engine disks and instances in a project:

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. From the list of principals, locate the desired principal and click the _edit_ button.

  3. From the **Edit permissions** panel, locate the desired role to configure a condition for. Then under **IAM condition (optional)** , click **Add IAM condition**.

  4. In the **Edit condition** panel, enter a title and optional description for the condition.

  5. You can add a condition expression using either the **Condition builder** or the **Condition editor**. The condition builder provides an interactive interface to select your desired condition type, operator, and other applicable details about the expression. The condition editor provides a text-based interface to manually enter an expression using CEL syntax.

**Condition builder** :

     1. Delete any existing condition fields from the condition builder. The only field in the condition builder should be the **Add** button.
     2. Create a grouped condition expression that evaluates to `true` if the resource is a disk that starts with the specified prefix: 
        1. Click the **Add** drop-down and then click **Grouped conditions**.
        2. From the **Condition type** drop-down, select **Resource > Type**.
        3. From the **Operator** drop-down, select **is**.
        4. From the **Resource Type** drop-down, select **compute.googleapis.com/Disk**.
        5. Click the first **Add** button immediately beneath the condition you just entered to add another clause to the expression.
        6. From the **Condition type** drop-down, select **Resource > Name**.
        7. From the **Operator** drop-down, select **Starts with**.
        8. In the **Value** field, enter the [resource name](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource_name_format), including the desired prefix, in the appropriate format. For example, use `projects/PROJECT_ID/region/ZONE_ID/disks/PREFIX` to identify disks in the project `PROJECT_ID` and the zone `ZONE_ID` whose names start with `PREFIX`.
        9. To the left of each condition type, click **And** to ensure both clauses must be true.
     3. Create a grouped condition expression that evaluates to `true` if the resource is an instance that starts with the specified prefix: 
        1. Click the **Add** button outside of the existing condition group and then click **Grouped conditions**.
        2. From the **Condition type** drop-down, select **Resource > Type**.
        3. From the **Operator** drop-down, select **is**.
        4. From the **Resource Type** drop-down, select **compute.googleapis.com/Instance**.
        5. In the same condition group, click **Add**.
        6. From the **Condition type** drop-down, select **Resource > Name**.
        7. From the **Operator** drop-down, select **Starts with**.
        8. In the **Value** field, enter the [resource name](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource_name_format), with the desired prefix, in the appropriate format. For example, use `projects/PROJECT_ID/zones/ZONE_ID/instances/PREFIX` to identify instances in the project `PROJECT_ID` and the zone `ZONE_ID` whose names start with `PREFIX`.
        9. Ensure that the logic operator connecting the conditions in the group is set to **And**.
     4. Create a grouped condition expression that evaluates to `true` if the resource isn't a disk or an instance: 
        1. Click the **Add** button outside of the existing condition groups and then click **Grouped conditions**.
        2. From the **Condition type** drop-down, select **Resource > Type**.
        3. From the **Operator** drop-down, select **is not**.
        4. From the **Resource Type** drop-down, select **compute.googleapis.com/Disk**.
        5. In the same condition group, click **Add**.
        6. From the **Condition type** drop-down, select **Resource > Type**.
        7. From the **Operator** drop-down, select **is not**.
        8. From the **Resource Type** drop-down, select **compute.googleapis.com/Instance**.
        9. Ensure that the logic operator connecting the conditions in the group is set to **And**.
     5. Ensure that the logic operator connecting all of the groups of condition expressions is **Or**.

When you're finished, the condition builder should look similar to the following:

![](https://docs.cloud.google.com/static/iam/img/nested-conditions.png)

![](https://docs.cloud.google.com/static/iam/img/nested-conditions.png)

     6. Click **Save** to apply the condition.

     7. After the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.

**Condition editor** :

     1. Click the **Condition editor** tab and enter the following expression:
            
            (resource.type == "compute.googleapis.com/Disk" &&
            resource.name.startsWith("projects/PROJECT_ID/zones/ZONE_ID/disks/PREFIX")) ||
            (resource.type == "compute.googleapis.com/Instance" &&
            resource.name.startsWith("projects/PROJECT_ID/zones/ZONE_ID/instances/PREFIX")) ||
            (resource.type != "compute.googleapis.com/Disk" &&
            resource.type != "compute.googleapis.com/Instance")

     2. After entering your expression, you can optionally choose to [lint](https://docs.cloud.google.com/iam/docs/linting-policies) the CEL syntax by clicking **Run Linter** above the text box on the top-right.

     3. Click **Save** to apply the condition.

     4. Once the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.




### gcloud

Allow policies are set using the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern.

Execute the [`gcloud projects get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy) command to get the current allow policy for the project. In the following example, the JSON version of the allow policy is downloaded to a path on disk.

Command:
    
    
    gcloud projects get-iam-policy project-id --format=json > filepath
    

The JSON format of the allow policy is downloaded:
    
    
    {
      "bindings": [
        {
          "members": [
            "user:my-user@example.com"
          ],
          "role": "roles/owner"
        },
        {
          "members": [
            "group:my-group@example.com"
          ],
          "role": "roles/compute.instanceAdmin"
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 1
    }
    

To configure the allow policy with a resource name prefix condition, add the following highlighted condition expression. The gcloud CLI updates the version automatically:
    
    
    {
      "bindings": [
        {
          "members": [
            "user:my-user@example.com"
          ],
          "role": "roles/owner"
        },
        {
          "members": [
            "group:my-group@example.com"
          ],
          "role": "roles/compute.instanceAdmin",
          **"condition" : {
              "title": "PREFIX_only",
              "description": "Only gives access to VMs with the PREFIX prefix",
              "expression":
                "(resource.type == 'compute.googleapis.com/Disk' &&
                resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/PREFIX')) ||
                (resource.type == 'compute.googleapis.com/Instance' &&
                resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/instances/PREFIX')) ||
                (resource.type != 'compute.googleapis.com/Instance' &&
                resource.type != 'compute.googleapis.com/Disk')"
          }**
        }
      ],
      "etag": "BwWKmjvelug=",
      **"version" : 3**
    }

Next, set the new allow policy by executing the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command:
    
    
    gcloud projects set-iam-policy project-id filepath
    

The new conditional role binding grants the group permissions in the following way:

  * Members in the role binding can only use disk and instance permissions to access disks and instances whose names start with the specified prefix
  * Members in the role binding can use all other permissions in the Instance Admin role (`roles/compute.instanceAdmin`) to access all resources besides disks and instances



### REST

Use the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern to allow access to specific resources.

**First, read the allow policy for the project:**

The Resource Manager API's `[projects.getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy)` method gets a project's allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `POLICY_VERSION`: The policy version to be returned. Requests should specify the most recent policy version, which is policy version 3\. See [Specifying a policy version when getting a policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) for details.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy

Request JSON body: 
    
    
    {
      "options": {
        "requestedPolicyVersion": POLICY_VERSION
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/owner",
          "members": [
            "user:my-user@example.com
          ]
        },
        {
          "members": [
            "group:my-group@example.com"
          ],
          "role": "roles/compute.instanceAdmin"
        }
      ]
    }
    

**Next, modify the allow policy so that it allows access to specific resources.** Make sure to change the `version` field to the value `3`:
    
    
    {
      **"version" : 3**,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/owner",
          "members": [
            "user:my-user@example.com"
          ]
        },
        {
          "role": "roles/compute.instanceAdmin",
          "members": [
            "group:my-group@example.com"
          ],
          **"condition" : {
              "title": "PREFIX_only",
              "description": "Only gives access to VMs with the PREFIX prefix",
              "expression":
                "(resource.type == 'compute.googleapis.com/Disk' &&
                resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/PREFIX')) ||
                (resource.type == 'compute.googleapis.com/Instance' &&
                resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/instances/PREFIX')) ||
                (resource.type != 'compute.googleapis.com/Instance' &&
                resource.type != 'compute.googleapis.com/Disk')"
          }**
        }
      ]
    }

**Finally, write the updated allow policy:**

The Resource Manager API's `[projects.setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)` method sets the allow policy in the request as the project's new allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "version": 3,
        "etag": "BwWKmjvelug=",
        "bindings": [
          {
            "role": "roles/owner",
            "members": [
              "user:my-user@example.com"
            ]
          },
          {
            "role": "roles/compute.instanceAdmin",
            "members": [
              "group:my-group@example.com"
            ],
            "condition": {
              "title": "Dev_access_only",
              "description": "Only access to devAccess* VMs",
              "expression":
                "(resource.type == 'compute.googleapis.com/Disk' &&
                resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/PREFIX')) ||
                (resource.type == 'compute.googleapis.com/Instance' &&
                resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/instances/PREFIX')) ||
                (resource.type != 'compute.googleapis.com/Instance' &&
                resource.type != 'compute.googleapis.com/Disk')"
            }
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the updated allow policy.

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request.   


**Note** : Resource names for Compute Engine VM instances contain zone information for the instance. To give access to instances with a specific prefix across different zones, enumerate all zone IDs in the condition expression. For example, the following expression specifies instances with the prefix `devAccess` in both `ZONE_1` and `ZONE_2`: 
    
    
    resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_1_ID/instances/devAccess') ||
     resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_2_ID/instances/devAccess')
    

## Extract values from resource names

The previous examples show boolean comparisons between the resource name, or the beginning of the resource name, and another value. In some cases, though, you might need to compare a value with a specific part of the resource name that is not at the beginning of the name.

You can use the [`extract()` function](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#extract) and specify an _extraction template_ to extract the relevant part of the resource name as a string. If necessary, you can convert the extracted string to another type, such as a timestamp. After you extract a value from the resource name, you can compare that value with other values.

**Note:** If you use the Google Cloud console to edit conditions, the `extract()` function is available in the condition editor, but not in the expression builder.

The following examples show condition expressions that use the `extract()` function. For details about the `extract()` function, see the [IAM Conditions attribute reference](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#extract).

### Example: Match orders from the last 30 days

Suppose you store order information in multiple Cloud Storage buckets, and the objects in each bucket are organized by date. A typical object name might look similar to this example:
    
    
    projects/_/buckets/acme-orders-aaa/objects/data_lake/orders/order_date=2019-11-03/aef87g87ae0876
    

You want to allow a principal to access any order from the last 30 days. The following condition matches the Cloud Storage objects for these orders. It uses the `duration()` and `date()` functions to subtract 30 days (2,592,000 seconds) from the request time, then compare that timestamp with the order date:
    
    
    resource.type == 'storage.googleapis.com/Object' &&
      request.time - duration('2592000s') < date(resource.name.extract('/order_date={date_str}/'))
    

For details about the `date()` and `duration()` functions, see the [date/time attribute reference](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time).

### Example: Match Compute Engine VMs in any location

Suppose you want to grant a project-level role to a principal for any Compute Engine VM whose name starts with `dev-`, regardless of the VM's location. You also want the principal to be able to use that role for all other resource types.

The resource name for a VM uses a format similar to `projects/PROJECT_ID/zones/ZONE_ID/instances/INSTANCE_ID`. The following condition evaluates to `true` for VMs with an instance name that starts with the string `dev-`, and for all resource types other than VMs:
    
    
    resource.type != 'compute.googleapis.com/Instance' ||
      resource.name.extract('/instances/{name}').startsWith('dev-')
    

The text in curly brackets identifies the part of the resource name that is extracted for comparison. In this example, the extraction template extracts any characters after the first occurrence of the string `/instances/`.

## Important usage considerations for resource-based conditions

When adding a resource-based condition, it's important to consider how the condition will affect the principal's permissions.

### Inherited conditions

In addition to adding conditions to the allow policies of some service-specific resources, it's possible to add conditional role bindings to resources at the organization, folder, or project level. When added at the container resource level, the conditional role bindings are inherited by other resources through the [resource hierarchy](https://docs.cloud.google.com/iam/docs/overview#policy_hierarchy). Inherited conditions are useful when a resource doesn't allow [conditions in their allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-conditional-roles) or doesn't have an allow policy.

When you use attributes at the organization, folder, or project level, keep in mind that most attributes are available only for specific resource types. If part of a condition uses an attribute that isn't available for a resource, then that part of the condition is never interpreted as granting access. For example, the condition `resource.name.endsWith == devResource` never grants access to any IAM resource because IAM resources don't provide the resource name.

To prevent this issue, use the [resource type](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-type) and [resource service](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-service) attributes to limit the scope of the condition. For example, the following condition evaluates to `true` for all resource types other than Compute Engine instances; in contrast, for Compute Engine instances, the condition checks resource name:
    
    
    resource.type != 'compute.googleapis.com/Disk' ||
        resource.name.endsWith('devResource')
    

### Custom roles

Consider the following example, which involves [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles). An administrator wants to create a custom role that grants access to create VM instances, but only allows the user to create VM instances in a project with a resource name that starts with the name prefix `staging`, using the disks with the same name prefix.

To accomplish this goal, ensure that the granted role contains the [required permissions](https://docs.cloud.google.com/compute/docs/access/iam) to create a VM instance, which means permissions on disk and instance resource types. Then, ensure that the condition expression checks the resource name for _both_ disks and instances. Beyond these two types, other permissions in the role are not granted.

The following condition expression will result in unexpected behavior. Permissions to operate on Compute Engine VMs are blocked:
    
    
    resource.type == 'compute.googleapis.com/Disk' &&
     resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/staging')
    

The following condition expression includes both disks and instances, and will manage access based on the resource name for these two types:
    
    
    (resource.type == 'compute.googleapis.com/Disk' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/staging')) ||
     (resource.type == 'compute.googleapis.com/Instance' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/instances/staging'))
    

The following condition expression includes both disks and instances, and will manage access based on the resource name for these two types. For any other resource type, the condition expression grants the role regardless of the resource name:
    
    
    (resource.type == 'compute.googleapis.com/Disk' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/staging')) ||
     (resource.type == 'compute.googleapis.com/Instance' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/instances/staging')) ||
     (resource.type != 'compute.googleapis.com/Disk' &&
      resource.type != 'compute.googleapis.com/Instance')
    

### Parent-only permissions

In Google Cloud's resource hierarchy, some of the permissions in a role that affect a child resource are intended to be enforced at the parent level only. For example, to list projects in an organization, a user must be granted the `resourcemanager.projects.list` permission on the organization whose projects they want to list, not on the projects themselves. These kinds of permissions are called _parent-only permissions_ , and only apply to `list` operations.

To properly grant access to `*.*.list` permissions when using conditions, the condition expression should set the `resource.service` and `resource.type` attributes according to the parent resource type of the target resources to be listed.

**Note:** To grant parent-only permissions on a resource, the service that owns the resource must recognize the resource attributes used in the condition. For example, you cannot use the `resource.name` attribute in a condition at the project level, because Resource Manager, which manages projects, does not recognize the `resource.name` attribute. For details about which services recognize these attributes, see the [resource attribute reference](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource).

Consider the following examples. Using the Compute Engine example from the preceding section, the following expression prevents access to `compute.disks.list` and `compute.instances.list` permissions, since the resource on which this permissions are checked have `resource.type` attribute value of `cloudresourcemanager.googleapis.com/Project`.
    
    
    (resource.type == 'compute.googleapis.com/Disk' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/PREFIX')) ||
     (resource.type == 'compute.googleapis.com/Instance' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/instances/PREFIX'))
    

It is common that these `list` permissions are granted together with other permissions for regular operations on the resource. To increase to scope of grant in this case, you can either extend the scope for the `cloudresourcemanager.googleapis.com/Project` type only, or extend the scope to all other permissions not of type instance or disk.
    
    
    (resource.type == 'compute.googleapis.com/Disk' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/PREFIX')) ||
     (resource.type == 'compute.googleapis.com/Instance' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/instances/PREFIX')) ||
     resource.type == 'cloudresourcemanager.googleapis.com/Project'
    

or
    
    
    (resource.type == 'compute.googleapis.com/Disk' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/disks/PREFIX')) ||
     (resource.type == 'compute.googleapis.com/Instance' &&
      resource.name.startsWith('projects/PROJECT_ID/zones/ZONE_ID/instances/PREFIX')) ||
     (resource.type != 'compute.googleapis.com/Disk' &&
      resource.type != 'compute.googleapis.com/Instance')
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
