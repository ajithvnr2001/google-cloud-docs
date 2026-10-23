---
url: https://docs.cloud.google.com/secret-manager/docs/etags/
title: Use entity tags for optimistic concurrency control \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:21.242157+00:00
---

# Use entity tags for optimistic concurrency control  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/etags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Use entity tags for optimistic concurrency control Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager supports using [entity tags](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) (ETags) for optimistic concurrency control.

In some cases, two processes updating the same resource in parallel may interfere with one another, where the latter process overwrites the effort of the former one.

ETags provide a means for optimistic concurrency control by allowing processes to see if a resource has been modified before taking action on that resource.

## Use ETags with Secret Manager

The following resource modification requests support ETags:

  * [projects.secrets.patch](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/patch)

  * [projects.secrets.delete](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/delete)

  * [projects.secrets.versions.enable](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/enable)

  * [projects.secrets.versions.disable](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/disable)

  * [projects.secrets.versions.destroy](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions/destroy)




In a [secrets.patch](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/patch) request, the request ETag is embedded in the [Secret](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets#Secret.FIELDS) data. All other requests accept an optional `etag` parameter.

If an ETag is provided and matches the current resource ETag, the request succeeds; otherwise, it fails with a `FAILED_PRECONDITION` error and an HTTP status code 400\. If an ETag isn't provided, the request proceeds without checking the currently stored ETag value.

Resource ETags are generated at resource creation ([projects.secrets.create](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/create), [projects.secrets.addVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/addVersion)) and updated for each of the above-listed modification requests. A modification request only updates the ETag of the resource to which it applies. That is, updating a secret version doesn't affect the secret ETag, and similarly, updating the ETag doesn't affect the secret version.

Even when an update doesn't change a resource's state, it still updates the resource ETag.

Consider the following example:

  * User 1 tries to enable a secret version unaware that it's already enabled. The system processes this, changing nothing but the version's ETag.

  * User 2, using the old ETag, tries to disable the version.

  * This fails because the system recognizes the newer ETag, which indicates a more recent intent to keep the version enabled.




Even seemingly minor updates matter due to ETag changes. This ensures data consistency, especially with multiple users or systems interacting with the same resource.

The resource `etag` is returned in the response whenever a resource ([Secret](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets#resource:-secret) or [SecretVersion](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#resource:-secretversion)) is included.

**Important:** To use Secret Manager with workloads running on Compute Engine or Google Kubernetes Engine, the underlying instance or node must have the `cloud-platform` OAuth scope. See [accessing the Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes) for more information. 

## Delete a secret with ETags

This section describes using ETags when deleting a secret. If the secret has been modified by another process, the delete operation fails.

### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret.
  * ETAG: the entity tag of the secret. The ETag must include the surrounding quotes. For example, if the ETag value was `"abc"`, the shell-escaped value would be `"\"abc\""`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets delete SECRET_ID \
        --etag "ETAG"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets delete SECRET_ID `
        --etag "ETAG"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets delete SECRET_ID ^
        --etag "ETAG"

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * SECRET_ID: the ID of the secret.
  * ETAG: the entity tag of the secret. The ETag is specified as part of the URL's querystring and must be URL-encoded. For example, if the ETag value is `"abc"`, the URL-encoded value would be `%22abc%22` because the quote character is encoded as `%22`.



HTTP method and URL: 
    
    
    DELETE https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?etag=ETAG

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?etag=ETAG"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?etag=ETAG" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

## Update a secret with ETags

This section describes using ETags when updating a secret. If the secret has been modified by another process, the update operation will fail.

### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret.
  * KEY: the label name.
  * VALUE: the corresponding label value.
  * ETAG: the entity tag of the secret. The ETag must include the surrounding quotes. For example, if the ETag value was `"abc"`, the shell-escaped value would be `"\"abc\""`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID \
        --update-labels "KEY=VALUE" \
        --etag "ETAG"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID `
        --update-labels "KEY=VALUE" `
        --etag "ETAG"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID ^
        --update-labels "KEY=VALUE" ^
        --etag "ETAG"

The response returns the secret. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * SECRET_ID: the ID of the secret.
  * ETAG: the entity tag of the secret. The ETag is specified as a field on the [Secret](https://docs.cloud.google.com/docs/reference/rest/v1/projects.secrets#resource:-secret) and must include the surrounding quotes. For example, if the ETag value was `"abc"`, the JSON-escaped value would be `{"etag":"\"abc\""}`.
  * KEY: the label name.
  * VALUE: the corresponding label value.



HTTP method and URL: 
    
    
    PATCH https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=labels

Request JSON body: 
    
    
    {"etag":"ETAG", "labels":{"KEY": "VALUE"}}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=labels"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=labels" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T04:06:00.660420Z",
      "labels": {
        "KEY": "VALUE"
      },
      "etag": "\"162145a4f894d5\""
    }
    

## Update a secret version with ETags

This section describes using ETags when updating a secret version. If the secret version has been modified by another process, the update operation will fail.

The code sample here describes disabling a secret version with ETags. You can also specify ETags during other secret mutation operations, such as when enabling disabled versions or destroying secret versions. Refer to the [code samples](https://docs.cloud.google.com/secret-manager/docs/samples) for Secret Manager.

### gcloud

Before using any of the command data below, make the following replacements: 

  * VERSION_ID: the ID of the secret version.
  * SECRET_ID: the ID of the secret.
  * ETAG: the entity tag. The ETag must include the surrounding quotes. For example, if the ETag value was `"abc"`, the shell-escaped value would be `"\"abc\""`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions disable VERSION_ID \
      --secret SECRET_ID \
      --etag "ETAG"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions disable VERSION_ID `
      --secret SECRET_ID `
      --etag "ETAG"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions disable VERSION_ID ^
      --secret SECRET_ID ^
      --etag "ETAG"

The response returns the secret. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * SECRET_ID: the ID of the secret.
  * VERSION_ID: the ID of the secret version.
  * ETAG: the entity tag of the secret version. The ETag is specified as a field on the [SecretVersion](https://docs.cloud.google.com/docs/reference/rest/v1/projects.secrets#Secret.FIELDS) and must include the surrounding quotes. For example, if the ETag value was `"abc"`, the JSON-escaped value would be `{"etag":"\"abc\""}`.



HTTP method and URL: 
    
    
    POST https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:disable"

Request JSON body: 
    
    
    {"etag":"ETAG"}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:disable""

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
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID:disable"" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions/VERSION_ID",
      "createTime": "2024-09-04T06:41:57.859674Z",
      "state": "DISABLED",
      "etag": "\"1621457b3c1459\""
    }
    

## What's next

  * Learn how to [set up rotation schedules for secrets](https://docs.cloud.google.com/secret-manager/docs/secret-rotation).
  * Learn how to [edit secrets](https://docs.cloud.google.com/secret-manager/docs/editsecrets).
  * Learn how to [set up notifications on a secret](https://docs.cloud.google.com/secret-manager/docs/event-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
