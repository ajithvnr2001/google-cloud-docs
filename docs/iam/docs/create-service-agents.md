---
url: https://docs.cloud.google.com/iam/docs/create-service-agents/
title: Create and grant roles to service agents \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:53.587612+00:00
---

# Create and grant roles to service agents  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/create-service-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Create and grant roles to service agents Stay organized with collections  Save and categorize content based on your preferences. 

In Google Cloud, project-level, folder-level, and organization-level [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) are created automatically as you enable and use Google Cloud services. Sometimes, these service agents are also automatically granted roles that allow them to create and access resources on your behalf.

If necessary, you can also ask Google Cloud to create project-level, folder-level, and organization-level service agents for a service before you use the service. Asking Google Cloud to create service agents lets you grant roles to service agents before you use a service. If a service agent hasn't been created yet, then you can't grant roles to the service agent.

This option is useful if you use one of the following strategies to manage your allow policies:

  * **A declarative framework like[Terraform](https://www.terraform.io/).** If your Terraform configuration doesn't include the service agents' roles, then those roles are revoked when you apply your configuration. By creating service agents and granting them roles in your Terraform configuration, you ensure that these roles aren't revoked.
  * **A policies-as-code-system** that stores copies of your current allow policies in a code repository. If you let Google Cloud grant roles to service agents automatically, those roles appear in your actual allow policy, but not in your stored copy of the allow policy. To resolve this inconsistency, you might incorrectly revoke these roles. By creating service agents and granting them roles proactively, you can help prevent drift between your code repository and your actual allow policies.



After you trigger service agent creation, you must grant the service agents the roles that they are typically granted automatically. If you don't, some services might not function properly. This is because service agents that are created at a user's request aren't automatically granted roles.

**Note:** To create and grant roles to service agents for service-specific resources, refer to the service's documentation.

## Before you begin

  * Enable the Resource Manager and Workload Identity APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com,workloadidentity.googleapis.com)

  * Understand [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).




### Required roles

To get the permissions that you need to create and grant access to service agents, ask your administrator to grant you the following IAM roles on the projects, folders, and organizations that you're creating service agents for and granting access to: 

  * List available services and their endpoints: [Service Usage Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer) (`roles/serviceusage.serviceUsageViewer`) 
  * Enable service agents: [Workload Identity API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workloadidentity#workloadidentity.admin) (`roles/workloadidentity.admin`) 
  * Grant service agents access to a project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * Grant service agents access to a folder: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) 
  * Grant service agents access to projects, folders, and organizations: [Organization Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and grant access to service agents. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and grant access to service agents:

  * List available services and their endpoints: `serviceusage.services.list`
  * Enable service agents: `workloadidentity.serviceAgents.create`
  * View long-running operations: `workloadidentity.operations.get`
  * Grant service agents access to a project: 
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`
  * Grant service agents access to a folder: 
    * `resourcemanager.folders.getIamPolicy`
    * `resourcemanager.folders.setIamPolicy`
  * Grant service agents access to an organization: 
    * `resourcemanager.organizations.getIamPolicy`
    * `resourcemanager.organizations.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Identify service agents to create

To identify the service agents that you need to create and the resources that you need to create them for, do the following:

  1. Make a list of the services that you use and their API endpoints. To view all available services and their endpoints, use one of the following methods:

### Console

Go to the **API Library** page in the Google Cloud console.

[Go to API Library](https://console.cloud.google.com/apis/library)

The API endpoint is the **Service name** listed in the **Additional details** section.

### gcloud

The `[gcloud services list](https://docs.cloud.google.com/sdk/gcloud/reference/services/list)` command lists all available services for a project. 

Before using any of the command data below, make the following replacements: 

     * `EXPRESSION`: Optional. An expression to filter the results. For example, the following expression filters for all services whose names contain `googleapis.com` but don't contain `sandbox`: 
           
           name ~ googleapis.com AND name !~ sandbox

For a list of filter expressions, see [`gcloud topic filters`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). 

     * `LIMIT`: Optional. The maximum number of results to list. The default is `unlimited`.

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud services list --available --filter='EXPRESSION' --limit=LIMIT

#### Windows (PowerShell)
    
    gcloud services list --available --filter='EXPRESSION' --limit=LIMIT

#### Windows (cmd.exe)

**Note:** If this command uses `'` for quoting content, replace these single quotes with double quotes. If quoting is nested, use `\"` to escape the inner quotes. 
    
    gcloud services list --available --filter='EXPRESSION' --limit=LIMIT

The response contains the names and titles of all available services. The API endpoint is the value in the `NAME` field. 

### REST

The Service Usage API's `[services.list](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/list)` method lists all available services for a project. 

Before using any of the request data, make the following replacements: 

     * `RESOURCE_TYPE`: The type of resource that you want to list available services for. Use `projects`, `folders`, or `organizations`. 
     * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to list available services for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
     * `PAGE_SIZE`: Optional. The number of services to include in the response. The default value is 50, and the maximum value is 200. If the number of services is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results. 
     * `NEXT_PAGE_TOKEN`: Optional. The pagination token returned in an earlier response from this method. If specified, the list of services will start where the previous request ended. 

HTTP method and URL: 
    
    GET https://serviceusage.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/services?pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://serviceusage.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/services?pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://serviceusage.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/services?pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN" | Select-Object -Expand Content

The response contains the names and titles of all available services for the resource. If the number of available services is greater than the page size, the response also contains a pagination token. 

The API endpoint is the value in the `name` field. 

  2. For each API endpoint that you will use, make a list of the resources where you need to create that endpoint's service agents:

     1. On the [service agent reference](https://docs.cloud.google.com/iam/docs/service-agents) page, search for each API endpoint to find all service agents for that endpoint.

Some endpoints might not have associated service agents—you can skip triggering service agent creation for these endpoints.

     2. For each of the endpoint's service agents, use the service agent's email address to determine where you need to create the service agent.

The placeholder in a service agent's email address indicates where you need to create the service agent:

Placeholder | Where to create the service agent  
---|---  
`PROJECT_NUMBER` | Each project where you will use the service  
`FOLDER_NUMBER` | Each folder where you will use the service  
`ORGANIZATION_NUMBER` | Each organization where you will use the service  
     3. For each endpoint, record each unique resource where you need to create service agents for that endpoint.




## Trigger service agent creation

After you know which service agents you need to create, you can ask Google Cloud to create them.

When you ask Google Cloud to create service agents, you provide it with a service and a resource. Then, Google Cloud creates all service agents for that service and that resource.

During this step, if you're using the gcloud CLI or the REST API, you can also create a list of the roles that need to be granted to each service agent. You'll use this information to grant roles to the service agents. If you're using Terraform, then you don't need to manually keep track of the required roles because you can reference the roles programmatically.

### gcloud

Use the [`gcloud workload-identity service-agents generate`](https://docs.cloud.google.com/sdk/gcloud/reference/workload-identity/service-agents/generate) command to create service agents for each endpoint and resource that you identified in Identify service agents to create.

Each time you run the command, review the response. For each role in the response, record the email address of the service agent that the role should be granted to. You will use this information to grant roles to the service agents.

Before using any of the command data below, make the following replacements: 

  * `ENDPOINT`: The endpoint of the API that you want to create service agents for—for example, `aiplatform.googleapis.com`. 
  * `RESOURCE_TYPE`: The type of resource that you want to create service agents for. Use `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The numeric ID of the Google Cloud project, folder, or organization that you want to create service agents for. For example, `123456789012`. 

You can create service agents for one resource at a time. If you need to create service agents for multiple resources, run the command once for each resource. 




Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud workload-identity service-agents generate --service="ENDPOINT" \
        --location="global" --RESOURCE_TYPE="RESOURCE_ID"

#### Windows (PowerShell)
    
    
    gcloud workload-identity service-agents generate --service="ENDPOINT" `
        --location="global" --RESOURCE_TYPE="RESOURCE_ID"

#### Windows (cmd.exe)
    
    
    gcloud workload-identity service-agents generate --service="ENDPOINT" ^
        --location="global" --RESOURCE_TYPE="RESOURCE_ID"

The response contains a list of all of the service agents that were created. For each service agent, the response lists the resource it was created for, the email address of the service agent, the service that the service agent is associated with, and the state of the service agent. If the service agent is typically granted a specific role, the response also lists that role. 

The listed role is _not_ automatically granted to the service agent. For each role in the response, record the email address of the service agent that the role should be granted to. You will use this information to grant roles to the service agents. 

The following is a truncated example of the response for creating service agents for `aiplatform.googleapis.com`. 
    
    
    Provisioned service agents for aiplatform.googleapis.com under projects/123456789012:
    
    container: projects/123456789012
    principal: serviceAccount:service-123456789012@gcp-sa-aiplatform.iam.gserviceaccount.com
    role: roles/aiplatform.serviceAgent
    serviceProducer: aiplatform.googleapis.com
    state: ACTIVE
    ----
    container: projects/123456789012
    principal: serviceAccount:service-123456789012@gcp-ri-aiplatform.iam.gserviceaccount.com
    serviceProducer: aiplatform.googleapis.com
    state: ACTIVE
    ----
    ...
    ----
    container: projects/123456789012
    principal: serviceAccount:service-123456789012@gcp-sa-vertex-vtc.iam.gserviceaccount.com
    role: roles/aiplatform.trainingClusterServiceAgent
    serviceProducer: aiplatform.googleapis.com
    state: ACTIVE
    ----
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

Use the `google_workload_identity_service_agent` resource to trigger service agent creation for each endpoint and resource that you identified in Identify service agents to create.

For example, if you wanted to create all project-level service agents for BigQuery for the default project, you could add the following code to your Terraform configuration:
    
    
    data "google_project" "default" {
    }
    
    # Create all project-level bigquery.googleapis.com service agents
    resource "google_workload_identity_service_agent" "primary" {
      parent = "projects/${data.google_project.default.number}/locations/global/serviceProducers/bigquery.googleapis.com"
    }

### REST

For each endpoint that you need to create service agents for, do the following:

  1. Create service agents for each resource that you identified in Identify service agents to create:

Before using any of the request data, make the following replacements: 

     * `RESOURCE_TYPE`: The type of resource that you want to create service agents for. Use `projects`, `folders`, or `organizations`. 
     * `RESOURCE_NUMERIC_ID`: The numeric ID of the Google Cloud project, folder, or organization that you want to create service agents for. For example, `123456789012`. 

You can create service agents for one resource at a time. If you need to create service agents for multiple resources, send one request for each resource. 

     * `ENDPOINT`: The endpoint of the API that you want to create a service agent for—for example, `aiplatform.googleapis.com`. 

HTTP method and URL: 
    
    POST https://workloadidentity.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUMERIC_ID/locations/global/serviceProducers/ENDPOINT:generateServiceAgents

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://workloadidentity.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUMERIC_ID/locations/global/serviceProducers/ENDPOINT:generateServiceAgents"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://workloadidentity.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_NUMERIC_ID/locations/global/serviceProducers/ENDPOINT:generateServiceAgents" | Select-Object -Expand Content

The response contains an [`Operation`](https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest/v1/projects.locations.operations) indicting the status of your request. For example: 
    
    {
      "name": "projects/123456789012/locations/global/operations/operation-1775250941060-64e94d1baa76d-1aa958f3-07b2ea9c",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.workloadidentity.v1.OperationMetadata",
        "createTime": "2026-04-03T21:15:41.367155118Z",
        "target": "projects/123456789012/locations/global/serviceProducers/bigquery.googleapis.com",
        "verb": "passthroughLro",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

  2. Get the response from the completed operation. For each role in the response, record the email address of the service agent that the role should be granted to. You will use this information to grant roles to the service agents.

Before using any of the request data, make the following replacements: 

     * `OPERATION_NAME`: The name of a generateServiceAgents operation. Copy this value from the `name` field of a `serviceProducers.generateServiceAgents` response. For example: `projects/123456789012/locations/global/operations/operation-1775250941060-64e94d1baa76d-1aa958f3-07b2ea9c`
     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

HTTP method and URL: 
    
    GET https://workloadidentity.googleapis.com/v1/OPERATION_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://workloadidentity.googleapis.com/v1/OPERATION_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://workloadidentity.googleapis.com/v1/OPERATION_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest/v1/projects.locations.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

Ongoing operations return a response like the following:
    
    {
      "name": "projects/123456789012/locations/global/operations/operation-1775258415970-64e968f44b91a-28fcf2f5-38367cfe",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.workloadidentity.v1.OperationMetadata",
        "createTime": "2026-04-03T23:20:15.982631253Z",
        "target": "projects/123456789012/locations/global/serviceProducers/aiplatform.googleapis.com",
        "verb": "passthroughLro",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Completed operations return a response containing a list of service agents that were created. For each service agent, the response lists the resource it was created for, the email address of the service agent, the service that the service agent is associated with, and the state of the service agent. If the service agent is typically granted a specific role, the response also lists that role. 

The listed role is _not_ automatically granted to the service agent. For each role in the response, record the email address of the service agent that the role should be granted to. You will use this information to grant roles to the service agents. 

The following is a truncated example of the response for creating service agents for `aiplatform.googleapis.com`. 
    
    {
      "name": "projects/123456789012/locations/global/operations/operation-1775258415970-64e968f44b91a-28fcf2f5-38367cfe",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.workloadidentity.v1.OperationMetadata",
        "createTime": "2026-04-03T23:20:15.982631253Z",
        "endTime": "2026-04-03T23:20:17.315225515Z",
        "target": "projects/123456789012/locations/global/serviceProducers/aiplatform.googleapis.com",
        "verb": "passthroughLro",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.workloadidentity.v1.GenerateServiceAgentsResponse",
        "serviceAgents": [
          {
            "container": "projects/123456789012",
            "serviceProducer": "aiplatform.googleapis.com",
            "principal": "serviceAccount:service-123456789012@gcp-sa-aiplatform.iam.gserviceaccount.com",
            "role": "roles/aiplatform.serviceAgent",
            "state": "ACTIVE"
          },
          {
            "container": "projects/123456789012",
            "serviceProducer": "aiplatform.googleapis.com",
            "principal": "serviceAccount:service-123456789012@gcp-ri-aiplatform.iam.gserviceaccount.com",
            "state": "ACTIVE"
          },
          ...
          {
            "container": "projects/123456789012",
            "serviceProducer": "aiplatform.googleapis.com",
            "principal": "serviceAccount:service-123456789012@gcp-sa-vertex-vtc.iam.gserviceaccount.com",
            "role": "roles/aiplatform.trainingClusterServiceAgent",
            "state": "ACTIVE"
          }
        ]
      }
    }
    




## Grant roles to service agents

After Google Cloud creates the necessary service agents for your projects, folders, and organizations, you use the service agents' email addresses to grant them roles.

If you asked Google Cloud to create service agents, you must grant those service agents the roles that they are typically granted automatically. If you don't, some services might not function properly. This is because service agents that are created at a user's request aren't automatically granted roles.

### Console

Use the list of roles and service agents that you created in Trigger service agent creation to identify which service agents need to be granted roles. For each service agent that needs a role, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization that you created the service agent for.

  3. Click person_add **Grant Access** , then enter the service agent's email address.

  4. Click **Select a role** , then search for a role to grant based on the following: 

     * The role name
     * The Google Cloud product that you want to grant access to
     * The permission that you want to give
     * The job function to perform
To follow the principle of least privilege, [choose a role](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) that includes only the permissions that your principal needs.
  5. Click **Save**. The service agent is granted the role on the resource.




### gcloud

Use the list of roles and service agents that you created in Trigger service agent creation to identify which service agents need to be granted roles. For each service agent that needs a role, use the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command to grant the role to the service agent.

**Note:** To grant roles to multiple service agents at a time, use the [read, modify, write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#multiple-roles-programmatic) pattern instead of the `add-iam-policy-binding` command.

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you want to manage access to. Use `projects`, `resource-manager folders`, or `organizations`.

  * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

  * `PRINCIPAL`: The email address of the service agent that you want to grant access to, prefaced by `serviceAccount:`. For example, `serviceAccount:service-0123456789012@gcp-sa-aiplatform-cc.iam.gserviceaccount.com`. 

  * `ROLE_NAME`: The name of the role that you want to grant to the service agent. 




Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member=PRINCIPAL --role=ROLE_NAME \
        --condition=CONDITION

#### Windows (PowerShell)
    
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID `
        --member=PRINCIPAL --role=ROLE_NAME `
        --condition=CONDITION

#### Windows (cmd.exe)
    
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID ^
        --member=PRINCIPAL --role=ROLE_NAME ^
        --condition=CONDITION

The response contains the updated IAM allow policy. 

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

To grant roles to service agents, do the following:

  1. For each `google_workload_identity_service_agent` resource, grant any roles that are associated with the service agents. 

For example, if you wanted to grant roles to all service agents for the `google_workload_identity_service_agent.primary` resource, you could add the following code to your Terraform configuration: 
         
         # Grant roles to BigQuery service agents for project
         resource "google_project_iam_member" "service_agents" {
           for_each = {
             for i, agent in google_workload_identity_service_agent.primary.service_agents :
             i => agent if try(agent.role, "") != ""
           }
           project = data.google_project.default.project_id
           role    = each.value.role
           member  = each.value.principal
         }

  2. Run a targeted `terraform apply` command for the `google_workload_identity_service_agent` resource that you added in the Trigger service agent creation section of this page. 

For example, if you added a resource named `google_workload_identity_service_agent.primary`, you would run the following command: 
         
         terraform apply target="google_workload_identity_service_agent.primary"

Running this command ensures that the `google_project_iam_member` resource can reference service agent resources without getting `Known After Apply` errors. 

  3. Run the `terraform plan` command for your Terraform configuration. This command shows the execution plan for granting roles to service agents. If the execution plan looks good, run `terraform apply` to apply the plan. 



### REST

Use the list of roles and service agents that you created in Trigger service agent creation to identify which service agents need to be granted roles. To grant roles to the service agents, use the read-modify-write pattern to update the resource's allow policy:

  1. Read the current allow policy by calling [`getIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy).

Before using any of the request data, make the following replacements: 

     * `API_VERSION`: The API version to use. For projects and organizations, use `v1`. For folders, use `v2`.
     * `RESOURCE_TYPE`: The resource type whose policy you want to manage. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
     * `POLICY_VERSION`: The policy version to be returned. Requests should specify the most recent policy version, which is policy version 3\. See [Specifying a policy version when getting a policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) for details.

HTTP method and URL: 
    
    POST https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:getIamPolicy

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
         "https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:getIamPolicy"

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
        -Uri "https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:getIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the resource's allow policy. For example: 
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/owner",
          "members": [
            "user:my-user@example.com"
          ]
        }
      ]
    }
    

  2. For each service agent that you want to grant a role to, create a role binding granting the service agent the required role. For example, the following role binding grants the AI Platform Custom Code Service Agent the Vertex AI Custom Code Service Agent role (`roles/aiplatform.customCodeServiceAgent`):
         
         {
             "role": "roles/aiplatform.customCodeServiceAgent",
             "members": [
               "serviceAccount:service-PROJECT_NUMBER@gcp-sa-aiplatform-cc.iam.gserviceaccount.com",
             ]
           }
         

If the allow policy already has a role binding for the required role, then add the service agent to the `members` list for that role binding.

  3. Write the updated allow policy by calling [`setIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy).

Before using any of the request data, make the following replacements: 

     * `API_VERSION`: The API version to use. For projects and organizations, use `v1`. For folders, use `v2`.
     * `RESOURCE_TYPE`: The resource type whose policy you want to manage. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
     * `POLICY`: A JSON representation of the policy that you want to set. For more information about the format of a policy, see the [Policy reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).

HTTP method and URL: 
    
    POST https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:setIamPolicy

Request JSON body: 
    
    {
      "policy": POLICY
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:setIamPolicy"

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
        -Uri "https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:setIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the updated allow policy.

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 



## What's next

  * View a list of [all service agents](https://docs.cloud.google.com/iam/docs/service-agents).
  * Explore other ways that you can [grant roles to principals](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn how to [create user-managed service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create), which can act as identities for your workloads.
  * Learn more about [best practices for using Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/best-practices-for-terraform).
  * Explore all [Google Cloud Terraform samples](https://docs.cloud.google.com/docs/samples?language=terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
