---
url: https://docs.cloud.google.com/iam/docs/configuring-temporary-access/
title: Configure temporary access \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:59.412029+00:00
---

# Configure temporary access  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/configuring-temporary-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure temporary access Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to set temporary (expiring) access to Google Cloud resources using conditional role bindings in your allow policies. By using the [date/time attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time), you can enforce time-based controls when accessing a given resource. For example, you can grant temporary access to a project that starts and stops at a specified time or on a scheduled and recurring basis.

**Note:** The examples on this page show how to modify access to a [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). However, you can adapt these steps to modify access to any Google Cloud resource that accepts IAM allow policies. For a list of these resource types, see [Resource types that accept allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies). 

## Before you begin

  * Read [Conditions Overview](https://docs.cloud.google.com/iam/docs/conditions-overview) to understand the basics of Identity and Access Management (IAM) conditional role bindings.
  * Review the [date/time attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#date-time) that can be used in a condition expression. Date/time attributes are recognized by all Google Cloud services.



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

## Grant temporary access

A conditional role binding can be used to grant time-bounded access to a resource, ensuring that a user can no longer access the resource after the specified expiry date and time.

**Note:** Conditional role bindings do not override role bindings with no conditions. If a principal is bound to a role, and the role binding does not have a condition, then the principal always has that role. Adding the principal to a conditional binding for the same role has no effect. 

Consider the following scenario: the company ExampleCo's information security rules emphasize that no employee should have indefinite access to resources in production projects. Previously, the admins have been manually setting and deleting IAM role bindings to meet the engineers' emergency needs. To reduce administrative overhead, ExampleCo can instead configure a conditional role binding with a date/time condition to set an end date for the binding.

**Note:** You cannot use conditions when you grant [legacy basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic), including Owner (`roles/owner`), Editor (`roles/editor`), and Viewer (`roles/viewer`). Also, you cannot use conditions when you grant roles to all users ([`allUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allusers)) or all authenticated users ([`allAuthenticatedUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allauthenticatedusers)). 

To grant expirable access to a project resource:

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. From the list of principals, locate the desired principal and click the _edit_ button.

  3. From the **Edit permissions** panel, locate the desired role to configure a condition for. Then under **IAM condition (optional)** , click **Add IAM condition**.

  4. In the **Edit condition** panel, enter a title and optional description for the condition.

  5. You can add a condition expression using either the **Condition builder** or the **Condition editor**. The condition builder provides an interactive interface to select your desired condition type, operator, and other applicable details about the expression. The condition editor provides a text-based interface to manually enter an expression using [CEL syntax](https://docs.cloud.google.com/iam/docs/conditions-overview#cel).

**Condition builder** :

     1. From the **Condition type** drop-down, select **Expiring Access**.
     2. From the **Operator** drop-down, select **by**.
     3. From the **Time** drop-down, click the _ date_range_ button to select from a date and time range.
     4. Click **Save** to apply the condition.
     5. After the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.

**Condition editor** :

     1. Click the **Condition editor** tab and enter the following expression (replacing the timestamp with your own):
            
            request.time < timestamp("2020-07-01T00:00:00.000Z")

     2. After entering your expression, you can optionally choose to validate the CEL syntax by clicking **Run Linter** above the text box on the top-right.

     3. Click **Save** to apply the condition.

     4. After the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.




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
          "role": "roles/iam.securityReviewer"
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 1
    }
    

To configure the allow policy with expirable access, add the following highlighted condition expression (replacing the timestamp with your own). The gcloud CLI updates the version automatically:
    
    
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
          "role": "roles/iam.securityReviewer",
          **"condition" : {
            "title": "Expires_July_1_2020",
            "description": "Expires on July 1, 2020",
            "expression":
              "request.time < timestamp('2020-07-01T00:00:00.000Z')"
          }**
        }
      ],
      "etag": "BwWKmjvelug=",
      **"version" : 3**
    }

Next, set the new allow policy by executing the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command:
    
    
    gcloud projects set-iam-policy project-id filepath
    

The new allow policy is applied, and the group's role grant will expire at the specified time.

### REST

Use the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern to allow access until a specific time.

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
      **"version": 1** ,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/owner",
          "members": [
            "user:my-user@example.com"
          ]
        },
        {
          "role": "roles/iam.securityReviewer",
          "members": [
            "group:my-group@example.com"
          ]
        }
      ]
    }
    

**Next, modify the allow policy so that it allows access until a specific time.** Make sure to change the `version` field to the value `3`:
    
    
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
          "role": "roles/iam.securityReviewer",
          "members": [
            "group:my-group@example.com"
          ],
          **"condition" : {
            "title": "Expires_July_1_2020",
            "description": "Expires on July 1, 2020",
            "expression":
              "request.time < timestamp('2020-07-01T00:00:00.000Z')"
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
            "role": "roles/iam.securityReviewer",
            "members": [
              "group:my-group@example.com"
            ],
            "condition": {
              "title": "Expires_July_1_2020",
              "description": "Expires on July 1, 2020",
              "expression":
                "request.time < timestamp('2020-07-01T00:00:00.000Z')"
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


## Manage access based on days/hours of the week

A conditional role binding can be used to grant access to a resource only within certain days or hours of the week on a recurring basis.

Consider the following scenario: the company ExampleCo has a quality assurance project. The entire QA team is required to have highly-privileged roles to complete their work. ExampleCo has to abide by labor laws in their location, which limit work hours to Monday through Friday from 9 AM to 5 PM. ExampleCo can use date/time conditions to ensure that their employees are only able to access Google Cloud during the work week and during scheduled work hours.

**Note:** You cannot use conditions when you grant [legacy basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic), including Owner (`roles/owner`), Editor (`roles/editor`), and Viewer (`roles/viewer`). Also, you cannot use conditions when you grant roles to all users ([`allUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allusers)) or all authenticated users ([`allAuthenticatedUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allauthenticatedusers)). 

To grant access to a project resource for only certain days or hours of the week on a recurring basis:

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. From the list of principals, locate the desired principal and click the _edit_ button.

  3. From the **Edit permissions** panel, locate the desired role to configure a condition for. Then under **IAM condition (optional)** , click **Add IAM condition**.

  4. In the **Edit condition** panel, enter a title and optional description for the condition.

  5. You can add a condition expression using either the **Condition builder** or the **Condition editor**. The condition builder provides an interactive interface to select your desired condition type, operator, and other applicable details about the expression. The condition editor provides a text-based interface to manually enter an expression using [CEL syntax](https://docs.cloud.google.com/iam/docs/conditions-overview#cel).

**Condition builder** :

     1. Click **Add**.
     2. From the **Condition type** drop-down, select **Time** _arrow_right_ **Schedule** _arrow_right_ **Day of Week**.
     3. From the **Operator** drop-down, select **After or On**.
     4. From the **Day of Week** drop-down, select **Monday**.
     5. From the **Choose a time zone** drop-down, select your desired time zone from the list.
     6. Ensure that the **And** operator is selected on the left, and then click **Add** again.
     7. From the **Condition type** drop-down, select **Time** _arrow_right_ **Schedule** _arrow_right_ **Day of Week**.
     8. From the **Operator** drop-down, select **Before or On**.
     9. From the **Day of Week** drop-down, select **Friday**.
     10. From the **Choose a time zone** drop-down, select your desired time zone from the list.

At this point, you've configured access only on Monday through Friday. Now, you will configure access from 9 AM (09:00) to 5 PM (17:00).

     1. Ensure that the **And** operator is selected on the left, and then click **Add** again.
     2. From the **Condition type** drop-down, select **Time** _arrow_right_ **Schedule** _arrow_right_ **Hour of Day**.

        1. From the **Operator** drop-down, select **After or On**.
        2. From the **Hour of Day** drop-down, select **9** (9 AM).
        3. From the **Choose a time zone** drop-down, select your desired time zone from the list.
        4. From the **Condition type** drop-down, select **Time** _arrow_right_ **Schedule** _arrow_right_ **Hour of Day**.
        5. From the **Operator** drop-down, select **Before or On**. Note that for this selection, "on" will logically evaluate to all times between 17:00 (5 PM) and 17:59 (5:59 PM). To set access to expire at 4:59 PM, ensure the hour is set to 16 instead of 17.
        6. From the **Hour of Day** drop-down, select **17** (5 PM).
        7. From the **Choose a time zone** drop-down, select your desired time zone from the list.
        8. Click **Save** to apply the condition.
        9. Once the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.

You've now configured access from Monday to Friday, 9 AM to 5 PM.

**Condition editor** :

        1. Click the **Condition editor** tab and enter the following expression (replacing the placeholder values with your own):
               
               request.time.getHours("Europe/Berlin") >= 9 &&
               request.time.getHours("Europe/Berlin") <= 17 &&
               request.time.getDayOfWeek("Europe/Berlin") >= 1 &&
               request.time.getDayOfWeek("Europe/Berlin") <= 5
               

        2. After entering your expression, you can optionally choose to validate the CEL syntax by clicking **Run Linter** above the text box on the top-right.

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
          "role": "roles/bigquery.dataViewer"
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 1
    }
    

To configure the allow policy with scheduled access, add the following highlighted condition expression (replacing the timestamp with your own). The gcloud CLI updates the version automatically:
    
    
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
          "role": "roles/bigquery.dataViewer",
          **"condition" : {
            "title": "Business_hours",
            "description": "Business hours Monday-Friday",
            "expression": "request.time.getHours('Europe/Berlin') >= 9 && request.time.getHours('Europe/Berlin') <= 17 && request.time.getDayOfWeek('Europe/Berlin') >= 1 && request.time.getDayOfWeek('Europe/Berlin') <= 5"
          }**
        }
      ],
      "etag": "BwWKmjvelug=",
      **"version" : 3**
    }

Next, set the new allow policy by executing the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command:
    
    
    gcloud projects set-iam-policy project-id filepath
    

The new allow policy is applied, and the group's role grant will allow access between the specified days and times.

### REST

Use the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern to allow scheduled access. 

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
      **"version": 1** ,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/owner",
          "members": [
            "user:my-user@example.com"
          ]
        },
        {
          "role": "roles/bigquery.dataViewer",
          "members": [
            "group:my-group@example.com"
          ]
        }
      ]
    }
    

**Next, modify the allow policy to allow scheduled access.**

Add the following highlighted condition expression (replacing the timestamp with your own). Ensure that you've updated the `version` value to `3`:
    
    
    {
      "etag": "BwWKmjvelug=",
      **"version" : 3,**
      "bindings": [
        {
          "role": "roles/owner",
          "members": [
            "user:my-user@example.com"
          ]
        },
        {
          "role": "roles/bigquery.dataViewer",
          "members": [
            "group:my-group@example.com"
          ],
          **"condition" : {
            "title": "Business_hours",
            "description": "Business hours Monday-Friday",
            "expression":
              "request.time.getHours('Europe/Berlin') >= 9 &&
              request.time.getHours('Europe/Berlin') <= 17 &&
              request.time.getDayOfWeek('Europe/Berlin') >= 1 &&
              request.time.getDayOfWeek('Europe/Berlin') <= 5"
          }**
        }
      ]
    }

The Resource Manager API's `[projects.setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)` method sets the allow policy in the request as the project's new allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "etag": "BwWKmjvelug=",
        "version": 3,
        "bindings": [
          {
            "role": "roles/owner",
            "members": [
              "user:my-user@example.com"
            ]
          },
          {
            "role": "roles/bigquery.dataViewer",
            "members": [
              "group:my-group@example.com"
            ],
            "condition": {
              "title": "Business_hours",
              "description": "Business hours Monday-Friday",
              "expression": "request.time.getHours('Europe/Berlin') >= 9 && request.time.getHours('Europe/Berlin') <= 17 && request.time.getDayOfWeek('Europe/Berlin') >= 1 && request.time.getDayOfWeek('Europe/Berlin') <= 5"
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


## What's next

  * Learn how to [manage conditional role bindings](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings).
  * Learn how to [lint allow policies](https://docs.cloud.google.com/iam/docs/linting-policies).
  * Learn how to use conditional role bindings to [manage just-in-time privileged access to projects](https://docs.cloud.google.com/architecture/manage-just-in-time-privileged-access-to-project).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
