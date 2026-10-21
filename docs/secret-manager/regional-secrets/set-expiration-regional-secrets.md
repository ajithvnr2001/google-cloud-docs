---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/set-expiration-regional-secrets/
title: Set expiration date for a regional secret \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:51.999797+00:00
---

# Set expiration date for a regional secret  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/set-expiration-regional-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Set expiration date for a regional secret Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set an expiration date for a new or existing secret, change the expiration date of an existing secret, and remove any previously set expiration date from a secret.

## Overview

By default, secrets stored in Secret Manager exist until a user deletes them. If a secret must only be stored for a known, limited amount of time, you can attach an expiration time to it. At a secret's configured expiration time, it is automatically deleted.

If you don't have requirements that the secret must be deleted, consider using IAM Conditions or the _Disabled_ version state to revoke access in a safe way.

**Warning:** At expiration time, the secret and all of its secret versions are irreversibly deleted without warning. See [Safely using expiring secrets](https://docs.cloud.google.com/secret-manager/regional-secrets/set-expiration-regional-secrets#safely-use-expiring-secrets) for more information. 

You can enter an expiration time as either a timestamp or a duration. When secret metadata is retrieved, the expiration is always returned as a timestamp, regardless of how it was given.

An expiration can be added, updated, or removed from a secret at any time.

## Limitations

  * A secret's expiration cannot be less than 60 seconds away or more than 100 years away.




## Safely use expiring secrets

When a secret expires in Secret Manager, it is _irreversibly deleted_. The best way to detect soon-to-expire secrets is by using [IAM Conditions](https://docs.cloud.google.com/secret-manager/regional-secrets/access-control-rs#iam-conditions) to remove permissions from the accounts that use the secret prior to expiration.

To manage access to secrets effectively, set a time-based condition on the permissions granted.

  * Set an expiration date: Permissions should expire shortly before the secret itself is set to expire. This allows you to identify any workflows or processes that might still be using the secret unexpectedly.

  * Monitor for disruptions: If any workflows stop working after permissions are revoked, you can quickly restore access to minimize any impact.

  * Adjust as needed: If you find you need more time, you can extend the expiration date of the secret or even remove it altogether if it's no longer needed.


This approach helps ensure that access to secrets is tightly controlled and only available for as long as necessary, reducing the risk of unauthorized access or misuse. For example, imagine a scenario where a service account needs to access a secret every day for 30 days. You can configure the secret to expire 60 days after it's created. This gives a buffer period after the expected usage. You can also set up a conditional IAM binding to grant the service account the Secret Accessor role for 45 days. If the service account attempts to access the secret after 45 days, it's denied permission. Any workflows relying on this secret stop working. An administrator can quickly restore access by granting the Secret Accessor role back to the service account. This allows them time to investigate why the secret is still needed after the expected 30-day period, as the secret itself won't be deleted for another 15 days. **Caution:** If an account has project-level permissions, it can access all secrets within that project, even if you try to set specific expiration dates or restrictions on individual secrets. This means that using IAM Conditions alone won't help you detect when secrets are expiring. To effectively manage expiring secrets, assign permissions at the secret level rather than the project level. This ensures that access to each secret is controlled independently and any expiration settings you apply are enforced. 

Additionally, it is possible to create alerts based on logs warning of secrets that are expiring soon. For information, see the [Expiration logging](https://docs.cloud.google.com/secret-manager/regional-secrets/set-expiration-regional-secrets#expiration-logging) section of this document.

## Specify timestamps and durations

  * Timestamp values must be formatted as [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt), for example `2100-01-01T09:00:00-05:00`.

  * Duration values must be formatted as the number of seconds including the _s_ suffix, for example `86400s`.




## Set a secret's expiration date

You can set an expiration date and time on a secret using the Google Cloud console, the Google Cloud CLI, or the Secret Manager API.

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab, and then click **Create regional secret**.

  3. On the **Create regional secret** page, enter a name for the secret in the **Name** field.

  4. Enter a value for the secret (for example, `abcd1234`). You can also upload a text file containing the secret value using the **Upload file** option. This action automatically creates the secret version.

  5. Choose the location where you want your regional secret to be stored from the **Region** list.

  6. Go to **Expiration** , and then select the **Set expiration date** checkbox.

  7. Enter the expiration date and time in the _Month/Day/Year, Hour:Minute AM/PM_ format, for example, `7/31/20, 1:00 AM`. You can also use the date and time picker to enter the expiration date and time.

  8. Click **Create secret**.




### gcloud

#### Create an expiring secret using a timestamp

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * TIMESTAMP: the expiration time in RFC 3339 format, for example `2100-01-01T09:00:00-05:00`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION \
        --expire-time "TIMESTAMP"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION `
        --expire-time "TIMESTAMP"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION ^
        --expire-time "TIMESTAMP"

#### Create an expiring secret using a duration

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * DURATION: the expiration duration in seconds, for example `86400s`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION \
      --ttl "DURATION"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION `
      --ttl "DURATION"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION ^
      --ttl "DURATION"

### REST

#### Create an expiring secret using a timestamp

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * TIMESTAMP: the expiration time in RFC 3339 format, for example `2100-01-01T09:00:00-05:00`



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/$PROJECT_ID/locations/LOCATION/secrets?secretId=$SECRET_ID

Request JSON body: 
    
    
    {"expire_time": "TIMESTAMP"}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/$PROJECT_ID/locations/LOCATION/secrets?secretId=$SECRET_ID"

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
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/$PROJECT_ID/locations/LOCATION/secrets?secretId=$SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T03:58:38.200877Z",
      "expireTime": "2024-09-04T09:25:39Z",
      "etag": "\"162143305d282d\""
    }
    
    

#### Create an expiring secret using a duration

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * DURATION: the expiration duration in seconds, for example `86400s`



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID

Request JSON body: 
    
    
    {"ttl": "DURATION"}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID"

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
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T03:58:38.200877Z",
      "expireTime": "2024-09-04T09:25:39Z",
      "etag": "\"162143305d282d\""
    }
    
    

## Update a secret's expiration date

To update the secret's expiration date and time, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab.

  3. To edit a secret, locate the secret in the list, and then click the more_vert**Actions** menu associated with that secret. In the **Actions** menu, click **Edit**.

  4. Go to the **Expiration** section. Update the expiration date and time, and click **Update secret**.




### gcloud

#### Update a secret's expiration using a timestamp

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [region](https://docs.cloud.google.com/secret-manager/docs/locations#regional_endpoint_locations) where you have stored the secret data
  * TIMESTAMP: the expiration time in RFC 3339 format, for example `2100-01-01T09:00:00-05:00`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION \
      --expire-time "TIMESTAMP"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION `
      --expire-time "TIMESTAMP"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION ^
      --expire-time "TIMESTAMP"

#### Update a secret's expiration using a duration

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * DURATION: the expiration duration in seconds, for example `86400s`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION \
        --ttl "DURATION"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION `
        --ttl "DURATION"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION ^
        --ttl "DURATION"

### REST

#### Update a secret's expiration using a timestamp

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * TOKEN: your own Oauth2.0 access token
  * TIMESTAMP: the expiration time in RFC 3339 format, for example `2100-01-01T09:00:00-05:00`



HTTP method and URL: 
    
    
    PATCH https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=expire_time

Request JSON body: 
    
    
    {"expire_time": "TIMESTAMP"}
    

To send your request, choose one of these options:

#### curl

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer TOKEN" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=expire_time"

#### PowerShell

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $headers = @{ "Authorization" = "Bearer TOKEN" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=expire_time" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T03:58:38.200877Z",
      "expireTime": "2024-09-04T09:25:39Z",
      "etag": "\"162143305d282d\""
    }
    
    

#### Update a secret's expiration using a duration

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * DURATION: the expiration duration in seconds, for example `86400s`



HTTP method and URL: 
    
    
    PATCH https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=ttl

Request JSON body: 
    
    
    {"ttl": "DURATION"}
    

To send your request, choose one of these options:

#### curl

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer TOKEN" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=ttl"

#### PowerShell

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $headers = @{ "Authorization" = "Bearer TOKEN" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=ttl" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T03:58:38.200877Z",
      "expireTime": "2024-09-04T09:25:39Z",
      "etag": "\"162143305d282d\""
    }
    
    

## Remove a secret's expiration date

To remove the secret's expiration date and time, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab.

  3. To edit a secret, locate the secret in the list, and then click the more_vert**Actions** menu associated with that secret. In the **Actions** menu, click **Edit**.

  4. Go to the **Expiration** section. Clear the **Set expiration date** checkbox, and then click **Update secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION \
      --remove-expiration

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION `
      --remove-expiration

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION ^
      --remove-expiration

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * TOKEN: your own Oauth2.0 access token



HTTP method and URL: 
    
    
    PATCH https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=ttl

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer TOKEN" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=ttl"

#### PowerShell

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $headers = @{ "Authorization" = "Bearer TOKEN" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=ttl" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-04T03:58:38.200877Z",
      "etag": "\"162143305d282d\""
    }
    
    

## Expiration logging

Cloud Audit Logs are _not_ produced when a secret automatically expires. Instead Secret Manager writes logs to the [Secret Manager Secret resource](https://docs.cloud.google.com/monitoring/api/resources#tag_secretmanager.googleapis.com/Secret) at specific intervals leading up to a secret's expiration.

Log Timing | Secret Event Type  
---|---  
30 days before expiration | `EXPIRES_IN_30_DAYS`  
7 days before expiration | `EXPIRES_IN_7_DAYS`  
1 day before expiration | `EXPIRES_IN_1_DAY`  
6 hours before expiration | `EXPIRES_IN_6_HOURS`  
1 hour before expiration | `EXPIRES_IN_1_HOUR`  
at expiration | `EXPIRED`  
  
See the [Logging Quickstart guide](https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud) for information about how to view these logs. You can create [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) and use them to create alerts for upcoming expirations.

## What's next

  * [Create rotation schedules](https://docs.cloud.google.com/secret-manager/regional-secrets/rotate-regional-secrets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
