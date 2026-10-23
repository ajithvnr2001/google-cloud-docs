---
url: https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated/
title: Create short-lived credentials for multiple service accounts \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:35.945096+00:00
---

# Create short-lived credentials for multiple service accounts  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Create short-lived credentials for multiple service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create short-lived credentials for a service account based on a delegation chain of service accounts. You can use this approach when you need to issue a series of token generation calls to obtain a token with the permissions you need to accomplish your task.

After you get a short-lived credential, you can use it to [impersonate the service account](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

If you can generate a token with the required permissions with a single token generation call, you should [create short-lived credentials for that service account directly](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct).

## About creating short-lived credentials

Depending on the type of token you create, you can use short-lived credentials to authenticate calls to Google APIs, third-party APIs, or applications that require ID tokens. Short-lived credentials have a limited lifetime, with durations of just a few hours or shorter, and are not automatically refreshed. Short-lived service account credentials are useful for scenarios where you need to grant limited access to resources for trusted service accounts. They also create less risk than long-lived credentials, such as service account keys.

You can create the following types of short-lived credentials for a service account:

  * OAuth 2.0 access tokens

Access tokens are accepted for authentication by most Google APIs. When you generate an access token for a service account, the access token comes without a refresh token, which means that when the token expires, you must repeat the token creation process to generate a new one.

For more information, see [Access tokens](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens).

  * OpenID Connect (OIDC) ID tokens

ID tokens follow the [OpenID Connect (OIDC) specification](https://openid.net/connect/). ID tokens are accepted by a limited number of services and applications.

For more information, see [ID tokens](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens) and [Authentication for applications hosted on Cloud Run or Cloud Run functions](https://docs.cloud.google.com/docs/authentication/use-cases#run-functions).

  * Self-signed JSON Web Tokens (JWTs)

You can use self-signed JWTs to authenticate to some Google APIs without getting an access token from the Authorization Server. APIs deployed with API Gateway require them.

  * Self-signed binary blobs

Self-signed blobs are useful in scenarios when you need to securely transmit arbitrary binary data, usually for authentication purposes.




## Delegated request flow

The delegated request flow lets you chain [direct requests](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct) using a single request, instead of needing to make several direct requests in sequence. In this flow, the request for a service account credential is delegated to one or more service accounts in a _delegation chain_ before generating a credential for the final service account. The resulting credential only represents the final service account, and not the intermediate service accounts in the delegation chain.

Each service account in the delegation chain must have the required permissions on the next service account in the chain, so that it can pass along the request.

If one service account provides all of the permissions you need, you should use the simpler flow described in [Create short-lived credentials from a service account](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct).

## Before you begin

  * Enable the IAM and Service Account Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Understand [IAM service accounts](https://docs.cloud.google.com/iam/docs/service-accounts)

  * If you haven't already, enable billing and the IAM API by following the steps in the [quickstart](https://docs.cloud.google.com/iam/docs/grant-role-console#before-you-begin).

  * Identify the service accounts you will use in your delegation chain.

You can [create a new service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) and include it in the delegation chain if needed.




## Provide required permissions

A delegated request involves more than two identities: the caller, one or more service accounts in a _delegation chain_ , and finally the service account for which a credential is created. In this flow, consider the following identities:

  * Service Account 1 (`SA_1`), the caller who issues a request for the short-lived credentials.
  * Service Account 2 (`SA_2`), an intermediary service account that will delegate the initial request to `SA_3`. This account only passes on the request—it doesn't give `SA_1` or `SA_3` any additional access.
  * Service Account 3 (`SA_3`), the limited-privilege account for whom the credential is created.



To allow delegation, each account must grant the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) to the previous account in the chain.

In this particular example, `SA_1` must be granted the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) on `SA_2`. This is an example of the `SA_2` service account being treated as a resource: when you grant the role on `SA_2`, you update its allow policy the same way that you would update any other resource.

In this example flow, there is only one intermediary service account. To delegate access through more than one service account, you must also assign this role to any other service account in the chain.

Next, `SA_2` must also be granted the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) on `SA_3`. This allows `SA_2` to create short-lived credentials for `SA_3`.

The following steps use the REST API to grant the roles. However, you can also use the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

###  API 

**First, get the allow policy for` SA_2` (the intermediary service account):**

The `[serviceAccounts.getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)` method gets a service account's allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_2`: The name of Service Account 2.
  * `POLICY_VERSION`: The policy version to be returned. Requests should specify the most recent policy version, which is policy version 3\. See [Specifying a policy version when getting a policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) for details.



HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_2@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy

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
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_2@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_2@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/serviceAccountAdmin",
          "members": [
            "user:my-user@example.com"
          ]
        }
      ]
    }
    

If you have not granted a role to the service account, the response contains only an `etag` value. Include that `etag` value in the next step.

**Next, modify the allow policy to grant` SA_1` the Service Account Token Creator role** (`roles/iam.serviceAccountTokenCreator`).

For example, to modify the sample response from the previous step, add the following:
    
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/serviceAccountAdmin",
          "members": [
            "user:my-user@example.com"
          ]
        },
        **{
          "role": "roles/iam.serviceAccountTokenCreator",
          "members": [
            "serviceAccount:SA_1@PROJECT_ID.iam.gserviceaccount.com"
          ]
        }**
      ]
    }

**Then, write the updated allow policy for` SA_2`:**

The `[serviceAccounts.setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy)` method sets an updated allow policy for the service account. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_2`: The name of Service Account 2.
  * `POLICY`: A JSON representation of the policy that you want to set. For more information about the format of a policy, see the [Policy reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).

For example, to set the allow policy shown in the previous step, replace `POLICY` with the following:
        
        {
          "version": 1,
          "etag": "BwWKmjvelug=",
          "bindings": [
            {
              "role": "roles/serviceAccountAdmin",
              "members": [
                "user:my-user@example.com"
              ]
            },
            {
              "role": "roles/iam.serviceAccountTokenCreator",
              "members": [
                "serviceAccount:SA_1@PROJECT_ID.iam.gserviceaccount.com"
              ]
            }
          ]
        }




HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_2@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy

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
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_2@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_2@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the updated allow policy.

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 

**Now, get the allow policy for` SA_3` (the service account for whom the credential is created):**

The `[serviceAccounts.getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)` method gets a service account's allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_3`: The name of Service Account 3.
  * `POLICY_VERSION`: The policy version to be returned. Requests should specify the most recent policy version, which is policy version 3\. See [Specifying a policy version when getting a policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) for details.



HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_3@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy

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
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_3@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_3@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/serviceAccountAdmin",
          "members": [
            "user:my-user@example.com"
          ]
        }
      ]
    }
    

If you have not assigned a role to the service account, the response contains only an `etag` value. Include that `etag` value in the next step.

**Next, modify the allow policy to grant` SA_2` the Service Account Token Creator role** (`roles/iam.serviceAccountTokenCreator`).

For example, to modify the sample response from the previous step, add the following:
    
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/serviceAccountAdmin",
          "members": [
            "user:my-user@example.com"
          ]
        },
        **{
          "role": "roles/iam.serviceAccountTokenCreator",
          "members": [
            "serviceAccount:SA_2@PROJECT_ID.iam.gserviceaccount.com"
          ]
        }**
      ]
    }

**Finally, write the updated allow policy:**

The `[serviceAccounts.setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy)` method sets an updated allow policy for the service account. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_3`: The name of Service Account 3.
  * `POLICY`: A JSON representation of the policy that you want to set. For more information about the format of a policy, see the [Policy reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).

For example, to set the allow policy shown in the previous step, replace `POLICY` with the following:
        
        {
          "version": 1,
          "etag": "BwWKmjvelug=",
          "bindings": [
            {
              "role": "roles/serviceAccountAdmin",
              "members": [
                "user:my-user@example.com"
              ]
            },
            {
              "role": "roles/iam.serviceAccountTokenCreator",
              "members": [
                "serviceAccount:SA_2@PROJECT_ID.iam.gserviceaccount.com"
              ]
            }
          ]
        }




HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_3@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy

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
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_3@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_3@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the updated allow policy.

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 

## Request short-lived credentials

After you have granted the appropriate roles to each identity, you can request short-lived credentials for the desired service account. The following credential types are supported:

  * OAuth 2.0 access tokens
  * OpenID Connect ID tokens
  * Self-signed JSON Web Tokens (JWTs)
  * Self-signed binary objects (blobs)



To understand how to specify a delegation chain for these requests, see the Specifying a delegation chain section on this page.

### Generate an OAuth 2.0 access token

By default, OAuth 2.0 access tokens are valid for a maximum of 1 hour (3,600 seconds). However, you can extend the maximum lifetime for these tokens to 12 hours (43,200 seconds). To do so, identify the service accounts that need an extended lifetime for tokens, then [add these service accounts to an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#setting_a_list_constraint) that includes the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` list constraint. You can then specify a lifetime up to 43,200 seconds when you create a token for these service accounts.

To generate an OAuth 2.0 access token for a service account, do the following:

###  API 

The Service Account Credentials API's `[serviceAccounts.generateAccessToken](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateAccessToken)` method generates an OAuth 2.0 access token for a service account. 

Before using any of the request data, make the following replacements: 

  * `SA_NAME`: The name of the service account that you want to create a token for.
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `DELEGATES`: If you are using a delegated request flow, see Specifying a delegation chain on this page. If you are using a direct request flow with no delegation, omit the `delegates` field in the request body. 
  * `LIFETIME`: The amount of time until the access token expires, in seconds. For example, `300s`. 

By default, the maximum token lifetime is 1 hour (3,600 seconds). To extend the maximum lifetime for these tokens to 12 hours (43,200 seconds), [ add the service account to an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#setting_a_list_constraint) that includes the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` list constraint. 




HTTP method and URL: 
    
    
    POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:generateAccessToken

Request JSON body: 
    
    
    {
      "delegates": [
        DELEGATES
      ],
      "scope": [
        "https://www.googleapis.com/auth/cloud-platform"
      ],
      "lifetime": "LIFETIME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:generateAccessToken"

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
        -Uri "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:generateAccessToken" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateAccessToken). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If the `generateAccessToken` request was successful, the response body contains an OAuth 2.0 access token and an expiration time. The `accessToken` can then be used to authenticate a request on behalf of the service account until the `expireTime` has been reached: 
    
    
    {
      "accessToken": "eyJ0eXAi...NiJ9",
      "expireTime": "2020-04-07T15:01:23.045123456Z"
    }
    

### Generate OpenID Connect ID tokens

OpenID Connect ID tokens are valid for 1 hour (3,600 seconds). To generate an ID token for a service account, do the following:

###  API 

The Service Account Credentials API's `[serviceAccounts.generateIdToken](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateIdToken)` method generates an OIDC ID token for a service account. 

Before using any of the request data, make the following replacements: 

  * `PRIV_SA`: The email address of the privilege-bearing service account for which the short-lived token is created. 
  * `AUDIENCE_NAME`: The audience for the token, usually the URL of the application or service that the token will be used to access. 



HTTP method and URL: 
    
    
    POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/PRIV_SA:generateIdToken

Request JSON body: 
    
    
    {
      "audience": "AUDIENCE_NAME",
      "includeEmail": "true"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/PRIV_SA:generateIdToken"

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
        -Uri "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/PRIV_SA:generateIdToken" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateIdToken). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If the `generateId` request was successful, the response body contains an ID token that is valid for 1 hour. The `token` can then be used to authenticate a request on behalf of the service account: 
    
    
    {
      "token": "eyJ0eXAi...NiJ9"
    }
    

### Create a self-signed JSON Web Token (JWT)

Self-signed JSON Web Tokens (JWTs) are useful in a variety of scenarios, such as:

  * Authenticating a call to a Google API as described in [Google's Authentication Guide](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#jwt-auth).
  * Securely communicating between Google Cloud or non-Google services, such as App Engine applications. In this scenario, one application can sign a token that can be verified by another application for authentication purposes.
  * Treating a service account as an identity provider by signing a JWT that contains arbitrary claims about a user, account, or device.



To generate a self-signed JWT for a service account, do the following:

###  API 

The Service Account Credentials API's `[serviceAccounts.signJwt](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signJwt)` method signs a JWT using a service account's system-managed private key. 

Before using any of the request data, make the following replacements: 

  * `SA_NAME`: The name of the service account that you want to create a token for.
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `DELEGATES`: If you are using a delegated request flow, see Specifying a delegation chain on this page. If you are using a direct request flow with no delegation, omit the `delegates` field in the request body. 
  * `JWT_PAYLOAD`: The JWT payload to sign, which is a JSON object that contains a JWT Claims Set. Include the claims that are necessary for your desired use case and to meet the validation requirements for the service you are calling. If you are calling a Google API, see [ Google's Authentication Guide](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#jwt-auth) for claim requirements. 

The `exp` (expiration time) claim must be no more than 12 hours in the future. If you are calling a Google API, the `exp` claim must be set no more than 1 hour in the future. 

The following example payload contains claims to call a Google API, where `EXP` is an integer timestamp representing the expiration time: 
        
        { \"iss\": \"SA_NAME@PROJECT_ID.iam.gserviceaccount.com\", \"sub\": \"SA_NAME@PROJECT_ID.iam.gserviceaccount.com\", \"aud\": \"https://firestore.googleapis.com/\", \"iat\": 1529350000, \"exp\": EXP }




HTTP method and URL: 
    
    
    POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:signJwt

Request JSON body: 
    
    
    {
      "delegates": [
        DELEGATES
      ],
      "payload": "JWT_PAYLOAD"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:signJwt"

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
        -Uri "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:signJwt" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signJwt). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If the `signJwt` request was successful, the response body contains a signed JWT and the signing key ID that was used to sign the JWT. You can use the `signedJwt` value as a bearer token to directly authenticate a request on behalf of the service account. The token is valid up to the expiration time specified in the request: 
    
    
    {
      "keyId": "42ba1e...fc0a",
      "signedJwt": "eyJ0eXAi...NiJ9"
    }
    

### Create a self-signed blob

Self-signed blobs are useful in scenarios when you need to securely transmit arbitrary binary data, usually for authentication purposes. For example, if you want to use a custom protocol/token type (not JWT), you can include that data in a signed blob for use by a downstream service.

To generate a self-signed blob for a service account, do the following:

###  API 

The Service Account Credentials API's `[serviceAccounts.signBlob](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signBlob)` method signs a blob using a service account's system-managed private key. 

Before using any of the request data, make the following replacements: 

  * `SA_NAME`: The name of the service account that you want to create a token for.
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `DELEGATES`: If you are using a delegated request flow, see Specifying a delegation chain on this page. If you are using a direct request flow with no delegation, omit the `delegates` field in the request body. 
  * `BLOB_PAYLOAD`: A base64-encoded string of bytes. For example, `VGhlIHF1aWNrIGJyb3duIGZveCBqdW1wZWQgb3ZlciB0aGUgbGF6eSBkb2cu`. 



HTTP method and URL: 
    
    
    POST https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:signBlob

Request JSON body: 
    
    
    {
      "delegates": [
        DELEGATES
      ],
      "payload": "BLOB_PAYLOAD"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:signBlob"

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
        -Uri "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com:signBlob" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signBlob). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If the `signBlob` request was successful, the response body contains a signed blob and the signing key ID that was used to sign the blob. You can use the `signedBlob` value as a bearer token to directly authenticate a request on behalf of the service account. The token is valid until the service account's system-managed private key expires. This key's ID is the value of the `keyId` field in the response. 
    
    
    {
      "keyId": "42ba1e...fc0a",
      "signedBlob": "eyJ0eXAi...NiJ9"
    }
    

### Specify a delegation chain

When using a delegated request flow to create short-lived service account credentials, the request body for each API must specify the service account delegation chain in the correct order and in the following format:

`projects/-/serviceAccounts/SA_ID`

Replace `SA_ID` with either the service account's unique numeric ID or the service account's email address.

For example, in a delegation chain that flows from `SA_1` (caller) to `SA_2` (delegated) to `SA_3` (delegated) to `SA_4`, the `delegates[]` field would contain `SA_2` and `SA_3` in the following order:
    
    
    {
      "delegates": [
        "projects/-/serviceAccounts/SA_2@PROJECT_ID.iam.gserviceaccount.com",
        "projects/-/serviceAccounts/SA_3@PROJECT_ID.iam.gserviceaccount.com"
      ]
    }

The caller and the service account for whom the credential is created are not included in the delegation chain.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
