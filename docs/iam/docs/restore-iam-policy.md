---
url: https://docs.cloud.google.com/iam/docs/restore-iam-policy/
title: Restore a previous version of an IAM allow policy \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:25.566748+00:00
---

# Restore a previous version of an IAM allow policy  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/restore-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Restore a previous version of an IAM allow policy Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to restore a previous version of an IAM allow policy after making any inadvertent changes or accidental deletion.

To restore a previous IAM policy, find the last successful `setIamPolicy` prior to the change or deletion and use it to restore the policy.

You can also use Cloud Asset Inventory to find the IAM change history and use it to restore the policy. 

## Required roles

To get the permissions that you need to restore a previous allow policy, ask your administrator to grant you the following IAM roles on the project, folder, or organization: 

  * Restore allow policies with `setIamPolicy`: 
    * [Logging Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`)
    * [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`)
    * [Owner ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Restore allow policies with Cloud Asset Inventory: [Cloud Asset Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.owner) (`roles/cloudasset.owner`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

When restoring allow policies with `setIamPolicy`, the Organization Administrator role is necessary for organization and folder-level allow policies, and the Owner role is necessary for project-level allow policies. 

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Restore an allow policy with the last successful `setIamPolicy` instance

To restore an allow policy to a previous version, you can review your audit logs for the last successful instance of `setIamPolicy` prior to the change or deletion and use the information from that instance to restore the policy. This process involves the following steps:

  1. Identify the last successful `setIamPolicy` instance for the allow policy and retrieve the `insertId`.
  2. Use the `insertId` from the `setIamPolicy` request to export the allow policy in YAML or JSON format.
  3. Modify the output file to match the previous working allow policy and override the current allow policy.



### Identify the last successful instance of `setIamPolicy` and retrieve the `insertId`

To identify the last successful instance of `setIamPolicy` and retrieve the `isertId`, use the Google Cloud console or the gcloud CLI to review your audit logs.

### Console

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the query editor, enter one of the following queries. These queries search your audit logs for entries that have `SetIamPolicy` in the `methodName` field of the `protoPayload`:

     * To get the logs of all allow policy changes made on a resource, use the following query:
           
           logName="RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity"
           protoPayload.methodName:SetIamPolicy
           

     * To get the logs of allow policy changes that involve a specific user or service account, use the following query:
           
           logName="RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity"
           protoPayload.methodName:SetIamPolicy
           protoPayload.serviceData.policyDelta.bindingDeltas.member:"EMAIL_ADDRESS"
           

Replace the following:

       * `RESOURCE_TYPE`: The resource type that you're listing audit logs for. Valid values are `projects`, `folders`, or `organizations`.
       * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
       * `EMAIL_ADDRESS`: The email address of the user or service account—for example, `example-service-account@example-project.iam.gserviceaccount.com`.
  3. To run the query, click **Run query**.

  4. Use the **Timeline** selector to specify the appropriate time range for the query. Alternatively, you can add a timestamp expression directly to the query editor. For more information, see [View logs by time range](https://docs.cloud.google.com/logging/docs/view/building-queries#queries-with-time-restriction).

  5. Copy the `insertId` from the last successful instance of `setIamPolicy` prior to the change or deletion.




### gcloud

The `[gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read)` command reads log entries. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you are listing audit logs for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `TIME_PERIOD`: The time period that you are listing audit logs for. The entries returned are not older than this value. If left unspecified, the default value is `1d`. For information about time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 
  * `RESOURCE_TYPE_SINGULAR`: The resource type that you are listing audit logs for. Use the value `project`, `folder`, or `organization`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud logging read \
        'logName:RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity
        AND protoPayload.methodName=SetIamPolicy' \
        --freshness=TIME_PERIOD \
        --RESOURCE_TYPE_SINGULAR=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud logging read `
        'logName:RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity
        AND protoPayload.methodName=SetIamPolicy' `
        --freshness=TIME_PERIOD `
        --RESOURCE_TYPE_SINGULAR=RESOURCE_ID

#### Windows (cmd.exe)

**Note:** If this command uses `'` for quoting content, replace these single quotes with double quotes. If quoting is nested, use `\"` to escape the inner quotes. 
    
    
    gcloud logging read ^
        'logName:RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity
        AND protoPayload.methodName=SetIamPolicy' ^
        --freshness=TIME_PERIOD ^
        --RESOURCE_TYPE_SINGULAR=RESOURCE_ID

Copy the `insertId` from the last successful instance of `setIamPolicy` prior to the change or deletion.

### Use the `insertId` to export the allow policy

Use the `insertId` you retrieved from the last successful instance of `setIamPolicy` to run the following command in the gcloud CLI to export the allow policy in JSON or YAML format. You can export allow policies for organizations and projects.

### Organization level

The `[gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read)` command reads log entries. 

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: The organization that you want to view and export the allow policy for. 
  * `INSERT_ID`: The `insertId` of the `setIamPolicy` request. 
  * `FORMAT`: The format for the response. Use `json` or `yaml`. 
  * `TIME_PERIOD`: The time period that you're listing audit logs for. The entries returned are not older than this value. If left unspecified, the default value is `1d`. For information about time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 
  * `OUTPUT_FILE`: The file name and extension for the output. For example, `previous_policy.json` or `previous_policy.yaml`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud logging read organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com
    insertId="INSERT_ID"'
    --organization=ORGANIZATION_ID
    --format="FORMAT(protoPayload.request.policy)"
    --freshness=TIME_PERIOD > OUTPUT_FILE

#### Windows (PowerShell)
    
    
    gcloud logging read organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com
    insertId="INSERT_ID"'
    --organization=ORGANIZATION_ID
    --format="FORMAT(protoPayload.request.policy)"
    --freshness=TIME_PERIOD > OUTPUT_FILE

#### Windows (cmd.exe)

**Note:** If this command uses `'` for quoting content, replace these single quotes with double quotes. If quoting is nested, use `\"` to escape the inner quotes. 
    
    
    gcloud logging read organizations/ORGANIZATION_ID/logs/cloudaudit.googleapis.com
    insertId="INSERT_ID"'
    --organization=ORGANIZATION_ID
    --format="FORMAT(protoPayload.request.policy)"
    --freshness=TIME_PERIOD > OUTPUT_FILE

### Project level

The `[gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read)` command reads log entries. 

Before using any of the command data below, make the following replacements: 

  * `INSERT_ID`: The `insertId` of the `setIamPolicy` request. 
  * `TIME_PERIOD`: The time period that you're listing audit logs for. The entries returned are not older than this value. If left unspecified, the default value is `1d`. For information about time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 
  * `FORMAT`: The format for the response. Use `json` or `yaml`. 
  * `OUTPUT_FILE`: The name of the file where you want to save the output—for example, `previous_policy.json` or `previous_policy.yaml`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud logging read \
    'protoPayload.methodName="SetIamPolicy" AND insertId="INSERT_ID"' \
    --freshness=TIME_PERIOD \
    --format="FORMAT(protoPayload.request.policy)" > OUTPUT_FILE

#### Windows (PowerShell)
    
    
    gcloud logging read `
    'protoPayload.methodName="SetIamPolicy" AND insertId="INSERT_ID"' `
    --freshness=TIME_PERIOD `
    --format="FORMAT(protoPayload.request.policy)" > OUTPUT_FILE

#### Windows (cmd.exe)

**Note:** If this command uses `'` for quoting content, replace these single quotes with double quotes. If quoting is nested, use `\"` to escape the inner quotes. 
    
    
    gcloud logging read ^
    'protoPayload.methodName="SetIamPolicy" AND insertId="INSERT_ID"' ^
    --freshness=TIME_PERIOD ^
    --format="FORMAT(protoPayload.request.policy)" > OUTPUT_FILE

### Modify the output file and override current allow policy

Modify the output file in the following ways and override the current allow policy.

  1. Programmatically or using a text editor, modify the output file by deleting the following lines:
         
         ---
          protoPayload:
             request:
               policy:
         

The resulting file starts with `auditConfigs:`.

  2. Get the current allow policy.

### gcloud

The `[gcloud get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read)` command gets a project's, folder's, or organization's allow policy. 

Before using any of the command data below, make the following replacements: 

     * `RESOURCE_TYPE`: The type of the resource that you want to get the allow policy for. Valid values are `projects`, `resource-manager folders`, or `organizations`.

     * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

     * `FORMAT`: The desired format for the allow policy. Use `json` or `yaml`.

     * `PATH`: The path to a new output file for the allow policy.

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format=FORMAT > PATH

#### Windows (PowerShell)
    
    gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format=FORMAT > PATH

#### Windows (cmd.exe)
    
    gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format=FORMAT > PATH

For example, the following command gets the allow policy for the project `my-project` and saves it to your home directory in JSON format:
    
    gcloud projects get-iam-policy my-project --format json > ~/policy.json

### C#

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy of a folder or organization, review the [Resource Managerclient library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy GetPolicy(string projectId)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            var policy = service.Projects.GetIamPolicy(new GetIamPolicyRequest(),
                projectId).Execute();
            return policy;
        }
    }
    

### Java

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy of a folder or organization, review the [Resource Managerclient library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.admin.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class GetProjectPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
    
        getProjectPolicy(projectId);
      }
    
      // Gets a project's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getProjectPolicy(String projectId) throws IOException {
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
          [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder()
                  .setResource([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId).toString())
                  .build();
          return projectsClient.getIamPolicy(request);
        }
      }
    }

### Python

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy of a folder or organization, review the [Resource Managerclient library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    from google.cloud import resourcemanager_v3
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def get_project_policy(project_id: str) -> policy_pb2.Policy:
        """Get policy for project.
    
        project_id: ID or number of the Google Cloud project you want to use.
        """
    
        client = resourcemanager_v3.ProjectsClient()
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        policy = client.get_iam_policy(request)
        print(f"Policy retrieved: {policy}")
    
        return policy

### REST

The Resource Manager API's `[get-iam-policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy)` method gets a project's, folder's, or organization's allow policy. 

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
    

Save the response in a file of the appropriate type (`json` or `yaml`).

  3. Copy the `etag` value from the current allow policy.

  4. Replace the `etag` value in the output file with the `etag`value that you copied from the current allow policy. The `etag` in the output file must match the current `etag` to initiate a new `setIamPolicy` request. Ensure that the spacing for the etag has not changed in the output file.

  5. Review the file to ensure it matches the previous working allow policy. You might consider creating a new project and applying the policy to ensure it works as intended.

  6. Set the allow policy to override the current allow policy with the one in the output file you created.

### gcloud

The `[gcloud set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read)` command sets the policy in the request as the new allow policy for the project, folder, or organization. 

Before using any of the command data below, make the following replacements: 

     * `RESOURCE_TYPE`: The type of the resource that you want to set the allow policy for. Valid values are `projects`, `resource-manager folders`, or `organizations`.

     * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

     * `PATH`: The path to a file that contains the new allow policy.

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

#### Windows (PowerShell)
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

#### Windows (cmd.exe)
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

The response contains the updated allow policy.

For example, the following command sets the allow policy stored in `policy.json` as the allow policy for the project `my-project`:
    
    gcloud projects set-iam-policy my-project ~/policy.json

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 

### C#
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy SetPolicy(string projectId, Policy policy)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            return service.Projects.SetIamPolicy(new SetIamPolicyRequest
            {
                Policy = policy
            }, projectId).Execute();
        }
    }
    

### Java

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to set the allow policy for a project. To learn how to set the allow policy of a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.admin.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ProjectName.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class SetProjectPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
    
        setProjectPolicy(policy, projectId);
      }
    
      // Sets a project's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) setProjectPolicy([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String projectId)
              throws IOException {
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
          List<String> paths = Arrays.asList("bindings", "etag");
          [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request = [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .setResource([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ProjectName.html).of(projectId).toString())
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(policy)
                  // A FieldMask specifying which fields of the policy to modify. Only
                  // the fields in the mask will be modified. If no mask is provided, the
                  // following default mask is used:
                  // `paths: "bindings, etag"`
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(paths).build())
                  .build();
    
          return projectsClient.setIamPolicy(request);
        }
      }
    }

### Python

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to set the allow policy for a project. To learn how to set the allow policy of a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    from google.cloud import [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest)
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def set_project_policy(
        project_id: str, policy: policy_pb2.Policy, merge: bool = True
    ) -> policy_pb2.Policy:
        """
        Set policy for project. Pay attention that previous state will be completely rewritten.
        If you want to update only part of the policy follow the approach read->modify->write.
        For more details about policies check out https://cloud.google.com/iam/docs/policies
    
        project_id: ID or number of the Google Cloud project you want to use.
        policy: Policy which has to be set.
        merge: The strategy to be used forming the request. CopyFrom is clearing both mutable and immutable fields,
        when MergeFrom is replacing only immutable fields and extending mutable.
        https://googleapis.dev/python/protobuf/latest/google/protobuf/message.html#google.protobuf.message.Message.CopyFrom
        """
        client = [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html)()
    
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
        current_policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_get_iam_policy)(request)
    
        # Etag should as fresh as possible to lower chance of collisions
        policy.ClearField("etag")
        if merge:
            current_policy.MergeFrom(policy)
        else:
            current_policy.CopyFrom(policy)
    
        request = iam_policy_pb2.SetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        # request.etag field also will be merged which means you are secured from collision,
        # but it means that request may fail and you need to leverage exponential retries approach
        # to be sure policy has been updated.
        request.policy.CopyFrom(current_policy)
    
        policy = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_set_iam_policy)(request)
        return policy
    
    

### REST

The Resource Manager API's `[set-iam-policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)` method sets the policy in the request as the new allow policy for the project, folder, or organization. 

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




## Restore an allow policy with Cloud Asset Inventory

To restore an allow policy to a previous version, you can use Cloud Asset Inventory to view the change history of the resource's allow policies and use that information to restore the policy. This process involves the following steps:

  1. Use Cloud Asset Inventory to review the change history of allow policies and identify the allow policy you want to restore.
  2. Copy the allow policy and create a new file in JSON format.
  3. Override the current allow policy with the one in the new file.



### Review allow policy change history with Cloud Asset Inventory

### Console

  1. In the Google Cloud console, go to the **Asset Inventory** page.

[Go to Asset Inventory](https://console.cloud.google.com/iam-admin/asset-inventory/policies)

  2. Click the **IAM Policy** tab.

  3. Run the following query in the **Filter** field:
         
         Resource : RESOURCE_ID

Replace `RESOURCE_ID` with your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

  4. To view the change history of the resource's allow policy, click the resource's name, then select the **Change History** tab.

  5. To compare any changes to the allow policy for the resource, select two different timestamped records from the **Select a record to compare** menu.




### gcloud

The `[gcloud asset get-history](https://docs.cloud.google.com/sdk/gcloud/reference/asset/get-history)` command gets the updated history of allow policies on an asset that overlaps a time window. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you are listing audit logs for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `ASSET_NAME`: A comma-separated list of [formatted resource names](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format) for the resources whose allow policy histories you want to view. For example, `//cloudresourcemanager.googleapis.com/projects/my-project`. These resources can be any of the resource types that [accept allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies). 
  * `START_TIME`: The beginning of the time range. The maximum time range is 7 days. The value must be the current time or a time no more than 35 days in the past. For information about time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 
  * `END_TIME`: Optional. The finishing point of the time range. The maximum time range is 7 days. The value must be the current time or a time no more than 35 days in the past. When not provided, the end time is assumed to be the current time. For information about time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud asset get-history \
        --RESOURCE_TYPE=RESOURCE_ID \
        --asset-names=ASSET_NAME_1,ASSET_NAME_2,... \
        --content-type=iam-policy \
        --start-time=START_TIME \
        --end-time=END_TIME

#### Windows (PowerShell)
    
    
    gcloud asset get-history `
        --RESOURCE_TYPE=RESOURCE_ID `
        --asset-names=ASSET_NAME_1,ASSET_NAME_2,... `
        --content-type=iam-policy `
        --start-time=START_TIME `
        --end-time=END_TIME

#### Windows (cmd.exe)
    
    
    gcloud asset get-history ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --asset-names=ASSET_NAME_1,ASSET_NAME_2,... ^
        --content-type=iam-policy ^
        --start-time=START_TIME ^
        --end-time=END_TIME

The response contains the updated history of allow policies.

### Create a new allow policy file

After you've reviewed the allow policy history and identified the allow policy you want to restore, complete the following steps.

  1. Copy the allow policy that you want to restore starting from the `"bindings"` line to the `"etag"` line.

  2. Paste the allow policy you copied into a new file and use curly braces (`{}`) to enclose the policy. For example, the allow policy might look like the following:
         
         {
           "bindings": [
             {
               "role": "roles/resourcemanager.organizationAdmin",
               "members": [
                 "user:mike@example.com",
                 "group:admins@example.com",
                 "domain:google.com",
                 "serviceAccount:my-service-account@my-project.iam.gserviceaccount.com"
               ]
             },
             {
               "role": "roles/resourcemanager.organizationViewer",
               "members": [
                 "user:eve@example.com"
               ],
               "condition": {
                 "title": "expirable access",
                 "description": "Does not grant access after Sep 2020",
                 "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')",
               }
             }
           ],
           "etag": "BwWWja0YfJA=",
          }
         

  3. Save the file in JSON format. For example, you might name the new file `previous_iam_policy.json`.




### Set the new allow policy

Set the allow policy to override the current allow policy with the one in the output file you created.

### gcloud

The `[gcloud set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/asset/get-history)` command sets the policy in the request as the new allow policy for the project, folder, or organization. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the resource that you want to set the allow policy for. Valid values are `projects`, `resource-manager folders`, or `organizations`.

  * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

  * `PATH`: The path to a file that contains the new allow policy.




Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

#### Windows (PowerShell)
    
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

#### Windows (cmd.exe)
    
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

The response contains the updated allow policy.

For example, the following command sets the allow policy stored in `policy.json` as the allow policy for the project `my-project`:
    
    
    gcloud projects set-iam-policy my-project ~/policy.json

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 

### C#
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy SetPolicy(string projectId, Policy policy)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            return service.Projects.SetIamPolicy(new SetIamPolicyRequest
            {
                Policy = policy
            }, projectId).Execute();
        }
    }
    

### Java

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to set the allow policy for a project. To learn how to set the allow policy of a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.admin.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ProjectName.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class SetProjectPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
    
        setProjectPolicy(policy, projectId);
      }
    
      // Sets a project's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) setProjectPolicy([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String projectId)
              throws IOException {
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
          List<String> paths = Arrays.asList("bindings", "etag");
          [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request = [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .setResource([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ProjectName.html).of(projectId).toString())
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(policy)
                  // A FieldMask specifying which fields of the policy to modify. Only
                  // the fields in the mask will be modified. If no mask is provided, the
                  // following default mask is used:
                  // `paths: "bindings, etag"`
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(paths).build())
                  .build();
    
          return projectsClient.setIamPolicy(request);
        }
      }
    }

### Python

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to set the allow policy for a project. To learn how to set the allow policy of a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    from google.cloud import [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest)
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def set_project_policy(
        project_id: str, policy: policy_pb2.Policy, merge: bool = True
    ) -> policy_pb2.Policy:
        """
        Set policy for project. Pay attention that previous state will be completely rewritten.
        If you want to update only part of the policy follow the approach read->modify->write.
        For more details about policies check out https://cloud.google.com/iam/docs/policies
    
        project_id: ID or number of the Google Cloud project you want to use.
        policy: Policy which has to be set.
        merge: The strategy to be used forming the request. CopyFrom is clearing both mutable and immutable fields,
        when MergeFrom is replacing only immutable fields and extending mutable.
        https://googleapis.dev/python/protobuf/latest/google/protobuf/message.html#google.protobuf.message.Message.CopyFrom
        """
        client = [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html)()
    
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
        current_policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_get_iam_policy)(request)
    
        # Etag should as fresh as possible to lower chance of collisions
        policy.ClearField("etag")
        if merge:
            current_policy.MergeFrom(policy)
        else:
            current_policy.CopyFrom(policy)
    
        request = iam_policy_pb2.SetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        # request.etag field also will be merged which means you are secured from collision,
        # but it means that request may fail and you need to leverage exponential retries approach
        # to be sure policy has been updated.
        request.policy.CopyFrom(current_policy)
    
        policy = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_set_iam_policy)(request)
        return policy
    
    

### REST

The Resource Manager API's `[set-iam-policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)` method sets the policy in the request as the new allow policy for the project, folder, or organization. 

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
