---
url: https://docs.cloud.google.com/secret-manager/docs/filtering/
title: Filter lists of secrets and secret versions \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:35.344694+00:00
---

# Filter lists of secrets and secret versions  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/filtering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Filter lists of secrets and secret versions Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the process of filtering secrets and secret versions in Secret Manager. In environments with numerous secrets, filtering helps quickly identify specific secrets or versions without manually scrolling through the entire list. You can filter based on criteria like labels, creation dates, or specific patterns within secret names, allowing for focused management of specific groups of secrets.

In Secret Manager, you can filter secrets and secret versions using the **Filter** option in the Google Cloud console or by specifying filter criteria within an API call. In the Google Cloud CLI, you can filter secrets and secret versions by including a `filter` string when listing secrets.

## Filter secrets

To filter a secret, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. In the **Secrets** table, click in the **Filter** field.

  3. Choose a filter property and its corresponding value, for example `Location:asia-east1`.

The table is automatically filtered based on the values entered. The results are sorted by name in the ascending order.




### gcloud

Before using any of the command data below, make the following replacements: 

  * FILTER: the filter string, for example `name:asecret OR name:bsecret`. gcloud CLI also supports regular expressions, for example `name ~ "secret_ab.*"`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets list --filter="FILTER"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets list --filter="FILTER"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets list --filter="FILTER"

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * FILTER: the filter string. Filters are specified as the `filter` querystring parameter and must be URL-encoded. For example, the filter `name:asecret OR name:bsecret` would be URL-encoded as `name%3Aasecret+OR+name%3Absecret`. Regular expressions aren't supported in the API.



HTTP method and URL: 
    
    
    GET https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?filter=FILTER

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?filter=FILTER"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets?filter=FILTER" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "secrets": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
          "createTime": "2024-09-02T07:14:00.281541Z",
          "etag": "\"16211dd90b37e7\""
        }
      ]
    }
    
    

### Filter a secret version

To filter a secret version, do the following:

  * In the Google Cloud console, select a secret to access its versions, and then use the **Filter** option in the **Versions** table.

  * If you're using the Google Cloud CLI or the Secret Manager API, include a `filter` string when listing secret versions.




## Examples of filters

Use case | Filter  
---|---  
Secrets whose name contains the `mysecret` substring | `name:mysecret`  
Secrets with a specific label | `labels.environment=production`  
Secrets created within date/time range | `create_time<2021-01-01T06:00:00Z AND create_time>2021-01-01T01:00:00Z`  
Secrets with automatic replication | `replication.automatic:*`  
Secrets with user-managed replication but not stored in either of the given regions | `replication.user_managed.replicas.location:* AND NOT replication.user_managed.replicas.location:(us-central1 OR us-east1)`  
Secrets encrypted with CMEK keys | `replication.user_managed.replicas.customerManagedEncryption:*`  
Secrets encrypted with a specific CMEK key | `replication.user_managed.replicas.customerManagedEncryption.kmsKeyName=projects/p/locations/us-central1/keyRings/kr/cryptoKeys/my-cmek-key`  
Secrets without a rotation period | `NOT rotation.next_rotation_time:*`  
Secrets with a rotation period > 30d | `rotation.rotation_period>259200s`  
Secrets with expiration set | `expire_time:*`  
Secrets expiring before a date | `expire_time<2021-07-31`  
Versions that are enabled or disabled | `state:(ENABLED OR DISABLED)`  
Destroyed versions, destroyed after date | `state:DESTROYED AND destroy_time>2021-01-01`  
  
## Filter syntax

The filter syntax consists of an expression on one or more fields of the objects being filtered.

You can use the following expression operators.

Operator | Description  
---|---  
`=` | Equality.  
`>` | Greater than.  
`<` | Less than.  
`>=` | Greater than or equal to.  
`<=` | Less than or equal to.  
`!=`  
`-`  
`NOT`  
|  Inequality. The following are equivalent:  
`name!="topsecret"`  
`-name="topsecret"`  
`NOT name="topsecret"`  
`:` |  Containment. This is a case-insensitive substring match.  For example, `name:"myapp"` filters on resources that contain `myapp` (case-insensitive) in the resource name.   
`AND` |  Logical AND. A space is equivalent to `AND`, so the following are equivalent:  
`name:"myapp" AND name:"secret1"`  
`name:"myapp" name:"secret1"`  
`OR` | Logical OR.  
`*` |  Wildcard. Can be used as a standalone where `field:*` indicates that `field` is set.   
  
Consistent with the Cloud Search API, `OR` operations are evaluated before `AND` operations unless parentheses are used to explicitly define a different order.

When filtering on `time` values, encode the time as a string in the [RFC 3399](https://datatracker.ietf.org/doc/html/rfc3339) format, such as `2020-10-15T01:30:15Z`.

When accessing a subfield, use dot syntax. For example, the [Secret](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets) resource may include the `labels` field whose value is a key-value `map`. If a `color` label is used, you can filter `Secret` results on the subfield `labels.color` as follows:
    
    
    labels.color=red
    

If you want to list only secrets with `color` label set, use a wildcard:
    
    
    labels.color:*
    

A quoted string is interpreted as a single value rather than a sequence of values.

## Filter fields

You can filter on any field of `Secret` or `SecretVersion` object.

List method | Link to filterable fields  
---|---  
`projects.secrets.list` |  [Secret fields](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets#Secret.FIELDS)  
`projects.secrets.versions.list` |  [SecretVersion fields](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets.versions#SecretVersion.FIELDS)  
  
## Total result count

If `filter` is set in a list request, the response does not indicate the total result count (`total_size=0` in the response). 

## What's next

  * Learn how to [edit secrets](https://docs.cloud.google.com/secret-manager/docs/edit-secrets).
  * Learn how to [set an expiration date for a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-managing-expiring-secrets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
