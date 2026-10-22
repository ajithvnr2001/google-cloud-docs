---
url: https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings/
title: Manage conditional role bindings \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:01.717465+00:00
---

# Manage conditional role bindings  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Manage conditional role bindings Stay organized with collections  Save and categorize content based on your preferences. 

This topic describes how to add, modify, and remove conditional role bindings in your Identity and Access Management (IAM) allow policies.

**Note:** Conditional role bindings do not override role bindings with no conditions. If a principal is bound to a role, and the role binding does not have a condition, then the principal always has that role. Adding the principal to a conditional binding for the same role has no effect. 

## Before you begin

  * Enable the IAM API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Read the [IAM Conditions overview](https://docs.cloud.google.com/iam/docs/conditions-overview) to understand the basics of IAM conditional role bindings.

  * Review the [attribute reference](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference) to learn about the different condition attributes that can be used in an expression.




### Required roles

To manage conditional role bindings in a resource's allow policy, you need permissions to get the resource, and to get and set the allow policy for the resource. These permissions have the following form, where `SERVICE` is the name of the service that owns the resource and `RESOURCE_TYPE` is the name of the resource type that you want to manage access to:

  * `SERVICE.RESOURCE_TYPE.get`
  * `SERVICE.RESOURCE_TYPE.getIamPolicy`
  * `SERVICE.RESOURCE_TYPE.setIamPolicy`



For example, to manage conditional role bindings in a project's allow policy, you need the following permissions:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.getIamPolicy`
  * `resourcemanager.projects.setIamPolicy`



To gain the required permissions, ask your administrator to grant you a predefined or custom role that includes the permissions. For example, your administrator could grant you the Security Admin role (`roles/iam.securityAdmin`), which includes permissions to get almost all Google Cloud resources and manage their allow policies.

## Add a conditional role binding to a policy

Conditional role bindings can be added to new or existing allow policies to further control access to Google Cloud resources. This section shows you how to add a simple [time-based condition](https://docs.cloud.google.com/iam/docs/configuring-temporary-access) to an existing allow policy using the Google Cloud console, the Google Cloud CLI, and the REST API.

**Note:** You cannot use conditions when you grant [legacy basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic), including Owner (`roles/owner`), Editor (`roles/editor`), and Viewer (`roles/viewer`). Also, you cannot use conditions when you grant roles to all users ([`allUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allusers)) or all authenticated users ([`allAuthenticatedUsers`](https://docs.cloud.google.com/iam/docs/principals-overview#allauthenticatedusers)). 

To add a conditional role binding to an existing allow policy:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. From the list of principals, locate the desired principal and click the edit  button.

  3. From the **Edit permissions** panel, locate the desired role to configure a condition for. Then under **IAM condition (optional)** , click **Add IAM condition**.

  4. In the **Edit condition** panel, enter a title and optional description for the condition.

  5. You can add a condition expression using either the **Condition builder** or the **Condition editor**. The condition builder provides an interactive interface to select your desired condition type, operator, and other applicable details about the expression. The condition editor provides a text-based interface to manually enter an expression using [CEL syntax](https://docs.cloud.google.com/iam/docs/conditions-overview#cel).

**Condition builder** :

     1. From the **Condition type** drop-down, select **Expiring Access**.
     2. From the **Operator** drop-down, select **by**.
     3. From the **Time** drop-down, click the  date_range button to select from a date and time range.
     4. Click **Save** to apply the condition.
     5. Once the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.

**Condition editor** :

     1. Click the **Condition editor** tab and enter the following expression (replacing the timestamp with your own):
            
            request.time < timestamp("2019-12-31T12:00:00.000Z")

     2. After entering your expression, you can optionally choose to validate the CEL syntax by clicking **Run Linter** above the text box on the top-right.

     3. Click **Save** to apply the condition.

     4. Once the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.




### gcloud

Allow policies are set using the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern.

Execute the [`gcloud projects get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy) command to get the current allow policy for the project. In the following example, the JSON version of the allow policy is downloaded to a path on disk.

Command:
    
    
    gcloud projects get-iam-policy project-id --format json > file-path

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

Note the allow policy's current `version`, which is `1`. To configure the allow policy with expirable access, add the following highlighted condition expression (replacing the timestamp with your own). The gcloud CLI updates the version automatically:
    
    
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
              "title": "Expires_2019",
              "description": "Expires at noon on 2019-12-31",
              "expression":
                "request.time < timestamp('2019-12-31T12:00:00Z')"
          }**
        }
      ],
      "etag": "BwWKmjvelug=",
      **"version" : 3**
    }

Next, set the new allow policy by executing the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command:
    
    
    gcloud projects set-iam-policy project-id file-path

The new allow policy is applied, and `travis@example.com`'s role binding will expire at the specified time.

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
    

Note the allow policy's current `version`, which is `1`.

**Next, modify the allow policy so that it allows access until a specific time.** Make sure to change the `version` field to the value `3`:
    
    
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
          "role": "roles/iam.securityReviewer",
          **"condition" : {
            "title": "Expires_2019",
            "description": "Expires at noon on 2019-12-31",
            "expression": "request.time < timestamp('2019-12-31T12:00:00Z')"
          },**
          "members": [
            "group:my-group@example.com"
          ]
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


## Modify an existing conditional role binding

After you create a conditional role binding, you can change the condition expression at any time. This section shows you how to update a [time-based condition](https://docs.cloud.google.com/iam/docs/configuring-temporary-access) in an existing allow policy using the Google Cloud console, the Google Cloud CLI, and the REST API.

To modify a conditional role binding in an existing allow policy:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. From the list of principals, locate the desired principal and click the edit  button.

  3. From the **Edit permissions** panel, locate the desired role to configure a condition for. Then under **IAM condition (optional)** , click the name of the existing condition to edit it.

  4. In the **Edit condition** panel, you can either keep or update the existing title and description for the condition.

  5. You can either edit the existing condition expression or add a new one using either the **Condition builder** or the **Condition editor**. The condition builder provides an interactive interface to select your desired condition type, operator, and other applicable details about the expression. The condition editor provides a text-based interface to manually enter an expression using [CEL syntax](https://docs.cloud.google.com/iam/docs/conditions-overview#cel).

**Condition builder** :

     1. Add a new condition expression or modify the existing condition expression.
     2. Click **Save** to apply the condition.
     3. Once the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.

**Condition editor** :

     1. Click the **Condition editor** tab and either add a new condition expression or modify the existing condition expression.
     2. After entering your expression, you can optionally choose to validate the CEL syntax by clicking **Run Linter** above the text box on the top-right.
     3. Click **Save** to apply the condition.
     4. Once the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.



### gcloud

Allow policies are set using the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern.

Execute the [`gcloud projects get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy) command to get the current allow policy for the project. In the following example, the JSON version of the allow policy is downloaded to a path on disk.

Command:
    
    
    gcloud projects get-iam-policy project-id --format json > file-path

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
          "role": "roles/bigquery.dataViewer",
          "condition": {
            "title": "Duration_3_months",
            "description": "Expires in 3 months on 2019-10-12",
            "expression":
              "request.time > timestamp(\"2019-07-12T07:00:00.000Z\") && request.time < timestamp(\"2019-10-12T07:00:00.000Z\")"
          }
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 3
    }

In this example, we will update the `title`, `description`, and timestamp values in the expression to change the duration of the scheduled access condition. Update the following highlighted portion of the condition (replacing the values with your own):
    
    
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
            "title": "Duration_5_months",
            "description": "Expires in 5 months on 2020-01-12",
            "expression":
              "request.time > timestamp('2019-07-12T07:00:00.000Z') && request.time < timestamp('2020-01-12T07:00:00.000Z')"
          }**
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 3
    }

Next, set the new allow policy by executing the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command.
    
    
    gcloud projects set-iam-policy project-id file-path

The updated allow policy is applied, and `fatima@example.com`'s role binding will expire at the new time.

### REST

Use the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern to modify the conditional role binding.

**First, read the allow policy for the project:**

The Resource Manager API's `[projects.getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy)` method gets a project's allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy

Request JSON body: 
    
    
    {
      "options": {
        "requestedPolicyVersion": 3
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
          "condition": {
            "title": "Duration_3_months",
            "description": "Expires in 3 months on 2019-10-12",
            "expression":
              "request.time > timestamp(\"2019-07-12T07:00:00.000Z\") && request.time < timestamp(\"2019-10-12T07:00:00.000Z\")"
          },
          "members": [
            "group:my-group@example.com"
          ]
        }
      ]
    }
    

**Next, modify the conditional role binding in the allow policy.** In this example, we will update the timestamp values to change the duration of the scheduled access condition. Update the following highlighted portion of the condition expression (replacing the timestamp with your own):
    
    
    {
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
          **"condition" : {
            "title": "Duration_5_months",
            "description": "Expires in 5 months on 2020-01-12",
            "expression":
              "request.time > timestamp('2019-07-12T07:00:00.000Z') && request.time < timestamp('2020-01-12T07:00:00.000Z')"
          },**
          "members": [
            "group:my-group@example.com"
          ]
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
            "condition": {
              "title": "Duration_5_months",
              "description": "Expires in 5 months on 2020-01-12",
              "expression":
                "request.time > timestamp('2019-07-12T07:00:00.000Z') && request.time < timestamp('2020-01-12T07:00:00.000Z')"
            },
            "members": [
              "group:my-group@example.com"
            ],
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


## Remove a condition from a role binding

Removing a condition from a role binding doesn't revoke the role. Instead, it lets all principals in that role binding use the permissions in the role unconditionally.

This section shows you how to remove a [time-based condition](https://docs.cloud.google.com/iam/docs/configuring-temporary-access) in an allow policy using the Google Cloud console, the Google Cloud CLI, and the REST API.

To remove a condition from a role binding in an allow policy:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. From the list of principals, locate the desired principal and click the edit  button.

  3. From the **Edit permissions** panel, locate the desired role binding. Then under **IAM condition (optional)** , click the name of an existing condition.

  4. In the **Edit condition** panel, click the  delete button to remove the condition. You will be prompted to confirm deletion of the condition.

  5. Once the **Edit condition** panel is closed, click **Save** again from the **Edit permissions** panel to update your allow policy.




### gcloud

Allow policies are set using the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern.

Execute the [`gcloud projects get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy) command to get the current allow policy for the project. In the following example, the JSON version of the allow policy is downloaded to a path on disk.

Command:
    
    
    gcloud projects get-iam-policy project-id --format json > file-path

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
          "role": "roles/bigquery.dataViewer",
          "condition": {
            "title": "Duration_3_months",
            "description": "Expires in 3 months on 2019-10-12",
            "expression":
              "request.time > timestamp(\"2019-07-12T07:00:00.000Z\") && request.time < timestamp(\"2019-10-12T07:00:00.000Z\")"
          }
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 3
    }

To remove the conditional role binding from the allow policy, remove the `condition` block as shown below:
    
    
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
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 3
    }

Note that the `version` is still set to `3`, despite the fact that unconditional role bindings only require a version `1` allow policy. We recommend that you always use the highest version number when setting an allow policy, both for conditional role bindings and unconditional role bindings. See [version requirements](https://docs.cloud.google.com/iam/docs/allow-policies#versions) for more information. The gcloud CLI updates the version number for the allow policy automatically.

Next, set the updated allow policy by executing the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command:
    
    
    gcloud projects set-iam-policy project-id file-path

The updated allow policy is applied, removing the conditional role binding for `fatima@example.com`. The role binding will no longer expire.

### REST

Use the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern to remove the conditional role binding.

**First, read the allow policy for the project:**

The Resource Manager API's `[projects.getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy)` method gets a project's allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy

Request JSON body: 
    
    
    {
      "options": {
        "requestedPolicyVersion": 3
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
          "condition": {
            "title": "Duration_3_months",
            "description": "Expires in 3 months on 2019-10-12",
            "expression":
              "request.time > timestamp(\"2019-07-12T07:00:00.000Z\") && request.time < timestamp(\"2019-10-12T07:00:00.000Z\")"
          },
          "members": [
            "group:my-group@example.com"
          ]
        }
      ]
    }
    

**Next, modify the allow policy by removing the conditional role binding:**
    
    
    {
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
          ]
        }
      ]
    }

Note that the `version` is still set to `3`, despite the fact that unconditional role bindings only require a version `1` allow policy. We recommend that you always use the highest version number when setting an allow policy, both for conditional role bindings and unconditional role bindings. See [version requirements](https://docs.cloud.google.com/iam/docs/allow-policies#versions) for more information.

**Finally, write the updated allow policy:**

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
            ]
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

  * [Attribute reference for IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference)
  * [Resource types that accept conditional role bindings](https://docs.cloud.google.com/iam/docs/resource-types-with-conditional-roles)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
