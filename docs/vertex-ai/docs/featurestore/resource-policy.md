---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/resource-policy/
title: Control access to Vertex AI Feature Store (Legacy) resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:56:28.763235+00:00
---

# Control access to Vertex AI Feature Store (Legacy) resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/resource-policy/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Control access to Vertex AI Feature Store (Legacy) resources Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

You can control access to Vertex AI Feature Store (Legacy) resources by setting IAM policies at different levels of the [resource hierarchy](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control). For example:

  * A project-level policy IAM applies to all resources in a project. You can set a project-level policy to grant permissions to users to read all featurestores in your project.

  * A resource-level IAM policy lets you specify which users can access specific resources. For a subset of users, you can set a resource-level policy to grant write permissions to specific featurestores in your project.




You can set resource-level Identity and Access Management (IAM) policies on the following Vertex AI Feature Store (Legacy) resources:

  * **Featurestore** : When you set an Identity and Access Management policy on a featurestore, the policy applies to the featurestore and all entity types created in that featurestore.

  * **Entity type** : When you set an Identity and Access Management policy on an entity type, the policy applies only to the entity type and the featurestore where the entity type is created.




An IAM [policy](https://docs.cloud.google.com/iam/docs/policies#structure) includes one or more role bindings that define which IAM roles are associated with which principals. A role is a collection of permissions that you grant to a principal. Vertex AI provides [predefined roles](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#predefined-roles) that you can use in your policies. Or, you can create your own custom roles.

## Considerations

You can't set conditional resource policies. For example, you can't create a policy that grants access to any resource that has or will have a name starting with a particular string like `testing`.

## Sample use case

As an example, imagine your organization has two sets of users. One set manages your core infrastructure in a DevOps administrator role. Another set manages particular entity types and their features, such as a data engineer.

A DevOps administrator manages featurestores and entity types at the project level. When data engineers request a new entity type, a DevOps admin can create and delegate ownership of that entity type to the data engineers. Data engineers can freely manage features in the entity types they own, but they can't operate on the featurestore or other entity types. This control, for example, lets DevOps admins limit access to entity types that contain sensitive information.

In this scenario, the DevOps administrator has the `aiplatform.featurestoreAdmin` role at the project level. Then, when a data engineer requests a new entity type, the administrator [creates a new entity type](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-entity-types) and then assigns the `aiplatform.entityTypeOwner` role to the data engineer at the entity type level (as a resource-level policy).

### Get IAM policy

You can view the current IAM policy on a featurestore or entity type by using the Google Cloud console or API.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, select a featurestore or an entity type from the **Featurestore** or **Entity type** column.
  4. Click **Permissions**.
  5. To show resource-level permissions, turn off **Show inherited permissions**. 

Principals who have access to the selected resource are grouped by role.

  6. Expand a role to see which principals are assigned to that role.



### REST

To get the IAM policy from a resource, send a POST request that uses the [`getIamPolicy`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/getIamPolicy) method. The following example gets an entity type policy. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:getIamPolicy

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:getIamPolicy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:getIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwXTmICm7mI",
      "bindings": [
        {
          "role": "roles/aiplatform.entityTypeOwner",
          "members": [
            "user:example@example.com"
          ]
        }
      ]
    }
    

### Set an IAM policy

You can set an IAM policy on a featurestore or entity type.

### Web UI

  1. In the Vertex AI section of the Google Cloud console, go to the **Features** page. 

[Go to the Features page](https://console.cloud.google.com/vertex-ai/features)

  2. Select a region from the **Region** drop-down list.
  3. In the features table, select a featurestore or an entity type from the **Featurestore** or **Entity type** column.
  4. Click **Permissions**.
  5. Click **Add principal**.
  6. Specify a principal and one or more roles to associate with the principal.
  7. Click **Save**.



### REST

To set the IAM policy on a resource, send a POST request that uses the [`setIamPolicy`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/setIamPolicy) method. The following example sets a policy on an entity type. 

Setting an IAM policy overrides any existing policy (changes are not appended). If you want to modify a resource's existing policy, use the `getIamPolicy` method to get its existing policy and then make modifications. Include your modified policy along with the `etag` in your `setIamPolicy` request. 

If you receive a `409` error code, there was a concurrent `SetIamPolicy` request that updated the policy. Make a `GetIamPolicy` to get the policy's updated etag, and then retry the `SetIamPolicy` request by including the new etag. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.
  * ROLE: An IAM role that includes the permissions to grant, such as `roles/aiplatform.featurestoreDataViewer`.
  * PRINCIPAL: The principal that is granted the role's permissions, such as `user:myuser@example.com`.
  * ETAG: A string value that is used to prevent simultaneous updates of a policy from overwriting each other. This value is returned as part of the `getIamPolicy` response.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "ROLE",
            "members": [
              "PRINCIPAL"
            ]
          },
          ...
        ],
        "etag": "ETAG"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:setIamPolicy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:setIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwXTmICm7mI",
      "bindings": [
        {
          "role": "roles/aiplatform.entityTypeOwner",
          "members": [
            "user:user1@example.com"
          ]
        },
        {
          "role": "roles/aiplatform.featurestoreDataViewer",
          "members": [
            "user:user2@example.com",
            "user:user3@example.com"
          ]
        },
        {
          "role": "roles/aiplatform.featurestoreDataWriter",
          "members": [
            "user:user4@example.com",
          ]
        }
      ]
    }
    

### Verify IAM permissions for a resource

You can verify whether the authenticated user has specific IAM permissions for a featurestore or entity type.

### REST

To verify whether a user has specific IAM permissions for a resource, send a POST request that uses the [`testIamPermissions`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/testIamPermissions) method. The following example lets you test whether the currently authenticated user has a set of IAM permissions for an entity type. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the featurestore is located, such as `us-central1`.
  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * FEATURESTORE_ID: ID of the featurestore.
  * ENTITY_TYPE_ID: ID of the entity type.



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:testIamPermissions -d

Request JSON body: 
    
    
    {
      "permissions": [
        "aiplatform.googleapis.com/entityTypes.get",
        "aiplatform.googleapis.com/entityTypes.readFeatureValues",
        "aiplatform.googleapis.com/entityTypes.writeFeatureValues"
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:testIamPermissions -d"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featurestores/FEATURESTORE_ID/entityTypes/ENTITY_TYPE_ID:testIamPermissions -d" | Select-Object -Expand Content

You should receive a JSON response similar to the following. The response includes only those permissions from the request JSON body which are available to the currently authenticated user. 
    
    
    {
      "permissions": [
        "aiplatform.googleapis.com/entityTypes.get",
        "aiplatform.googleapis.com/entityTypes.readFeatureValues",
        "aiplatform.googleapis.com/entityTypes.writeFeatureValues"
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
