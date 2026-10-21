---
url: https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads/
title: Restrict artifact downloads with download rules \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:26.132104+00:00
---

# Restrict artifact downloads with download rules  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Restrict artifact downloads with download rules Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to restrict artifact downloads from your Artifact Registry repositories by creating and managing download rules.

_Download rules_ let you allow or deny artifact downloads from your repositories and packages. You can also set conditions so the rule applies to specific tags or versions.

For details on how downloads rules work, see the [Restrict artifact downloads](https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts#restrict_artifact_downloads) section of the Control access and protect artifacts overview.

## Before you begin

  1. If you don't already have one, [create a Docker-format standard repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. (Optional) [Configure defaults for Google Cloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).



### Required roles

To get the permissions that you need to Create and manage download rules, ask your administrator to grant you the following IAM roles on the repository: 

  * Create, update, get, list and delete rules: [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`) 
  * Get and list rules: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create download rules

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * `RULE_NAME`: the name of the rule. The name must be unique within your repository, have a max length of 256 characters, and consist of alpha-numeric characters, percent-encoded characters, or characters in the list [`-`, `.`, `_`, `~`, `:`, `@`, `+`, `^`].
  * `ACTION`: the action applied to a download that matches this rule. Choose between `ALLOW`, where the rule allows matching downloads to occur, and `DENY`, where the rule blocks matching downloads from occurring.
  * `PACKAGE`: (optional) the name of the package. If supplied, the rule applies only to the specified package instead of the whole repository.
  * `CONDITION`: (optional) a [CEL expression](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads#CEL) that defines a matching rule. If supplied, only applies the rule to downloads that match the specified condition. For example, `pkg.version.id < '3.0'`.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the repository ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules create RULE_NAME \
        --action=ACTION \
        --project=PROJECT \
        --location=LOCATION \
        --repository=REPOSITORY \
        --package=PACKAGE \
        --condition="CONDITION"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules create RULE_NAME `
        --action=ACTION `
        --project=PROJECT `
        --location=LOCATION `
        --repository=REPOSITORY `
        --package=PACKAGE `
        --condition="CONDITION"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules create RULE_NAME ^
        --action=ACTION ^
        --project=PROJECT ^
        --location=LOCATION ^
        --repository=REPOSITORY ^
        --package=PACKAGE ^
        --condition="CONDITION"

A new rule is created with the following output: 
    
    
    Created rule [RULE_NAME].

For more information, see the [`gcloud artifacts rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/rules/create) command. 

###  API 

Before using any of the request data, make the following replacements: 

  * `RULE_NAME`: the name of the rule. The name must be unique within your repository, have a max length of 256 characters, and consist of alpha-numeric characters, percent-encoded characters, or characters in the list [`-`, `.`, `_`, `~`, `:`, `@`, `+`, `^`].
  * `ACTION`: the action applied to a download that matches this rule. Choose between `ALLOW`, where the rule allows matching downloads to occur, and `DENY`, where the rule blocks matching downloads from occurring.
  * `PACKAGE`: (optional) the name of the package. If supplied, the rule applies only to the specified package instead of the whole repository.
  * `CONDITION`: (optional) a [CEL expression](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads#CEL) that defines a matching rule. If supplied, only applies the rule to downloads that match the specified condition. For example, `pkg.version.id < '3.0'`.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the repository ID.



HTTP method and URL: 
    
    
    POST https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules?ruleID=RULE_NAME

Request JSON body: 
    
    
    {
      "action":"ACTION",
      "packageId":"PACKAGE",
      "condition":
      {
        "expression":"CONDITION"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules?ruleID=RULE_NAME"

#### PowerShell (Windows)

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json" `  
        -InFile request.json `  
        -Uri "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules?ruleID=RULE_NAME" | Select-Object -Expand Content

A new rule is created with the following output: 
    
    
    {
      "name": "projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME",
      "action": ACTION,
      "operation": "DOWNLOAD"
    }
    

For more information, see the [REST reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/create). 

## List download rules

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules list \
        --project=PROJECT \
        --location=LOCATION \
        --repository=REPOSITORY

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules list `
        --project=PROJECT `
        --location=LOCATION `
        --repository=REPOSITORY

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules list ^
        --project=PROJECT ^
        --location=LOCATION ^
        --repository=REPOSITORY

A list of rules for the specified project, location, and repository is displayed similar to the following: 
    
    
    RULE: my-rule
    PACKAGE: example.com/foo
    ACTION: DENY
    OPERATION: DOWNLOAD
    CONDITION: pkg.version.id < '3.0'
    

For more information, see the [`gcloud artifacts rules list`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/rules/list) command. 

###  API 

Before using any of the request data, make the following replacements: 

  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository.



HTTP method and URL: 
    
    
    GET https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules" | Select-Object -Expand Content

A list of rules for the specified project, location, and repository is displayed similar to the following: 
    
    
    {
      "rules": [
        {
          "name": "projects/my-project/locations/us-central1/repositories/my-repo/rules/my-rule",
          "action": "DENY",
          "operation": "DOWNLOAD",
          "condition": {
            "expression": "pkg.version.id \u003c '3.0'"
          },
          "packageId": "example.com/foo"
        }
      ]
    }
    

For more information, see the [REST reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/list). 

## Describe download rules

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * `RULE_NAME`: the name of the rule. The name must be unique within your repository.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules describe RULE_NAME \
        --project=PROJECT \
        --location=LOCATION \
        --repository=REPOSITORY

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules describe RULE_NAME `
        --project=PROJECT `
        --location=LOCATION `
        --repository=REPOSITORY

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules describe RULE_NAME ^
        --project=PROJECT ^
        --location=LOCATION ^
        --repository=REPOSITORY

Rule details are displayed similar to the following: 
    
    
    RULE: my-rule
    PACKAGE: example.com/foo
    ACTION: DENY
    OPERATION: DOWNLOAD
    CONDITION: pkg.version.id < '3.0'
    

For more information, see the [`gcloud artifacts rules describe`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/rules/describe) command. 

###  API 

Before using any of the request data, make the following replacements: 

  * `RULE_NAME`: the name of the rule. The name must be unique within your repository.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository.



HTTP method and URL: 
    
    
    GET https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME" | Select-Object -Expand Content

Rule details are displayed similar to the following: 
    
    
    {
      "rules": [
        {
          "name": "projects/my-project/locations/us-central1/repositories/my-repo/rules/my-rule",
          "action": "DENY",
          "operation": "DOWNLOAD",
          "condition": {
            "expression": "pkg.version.id \u003c '3.0'"
          },
          "packageId": "example.com/foo"
        }
      ]
    }
    

For more information, see the [REST reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/get). 

## Update download rules

###  gcloud 

Remove any variables you don't want to update.

Before using any of the command data below, make the following replacements: 

  * `RULE_NAME`: the name of the rule. The name must be unique within your repository.
  * `ACTION`: the action applied to a download that matches this rule. Choose between `ALLOW` and `DENY`.
  * `PACKAGE`: the name of the package. If not supplied, the rule applies to the whole repository.
  * `CONDITION`: a [CEL expression](https://docs.cloud.google.com/artifact-registry/docs/download-rules#CEL) that defines a matching rule. If supplied, only applies the rule to downloads that match the specified condition. For example, `pkg.version.id < '3.0'`.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules update RULE_NAME \
        --action=ACTION \
        --project=PROJECT \
        --location=LOCATION \
        --repository=REPOSITORY \
        --package=PACKAGE \
        --condition="CONDITION"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules update RULE_NAME `
        --action=ACTION `
        --project=PROJECT `
        --location=LOCATION `
        --repository=REPOSITORY `
        --package=PACKAGE `
        --condition="CONDITION"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules update RULE_NAME ^
        --action=ACTION ^
        --project=PROJECT ^
        --location=LOCATION ^
        --repository=REPOSITORY ^
        --package=PACKAGE ^
        --condition="CONDITION"

Updated rule details are shown similar to the following: 
    
    
    Updated rule [RULE_NAME].
    action: ACTION
    condition:
      expression: CONDITION
    name: projects/PROJECT/locationsLOCATION/repositories/REPOSITORY/rules/RULE_NAME
    operation: DOWNLOAD
    

For more information, see the [`gcloud artifacts rules update`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/rules/update) command. 

###  API 

Remove any variables you don't want to update.

Before using any of the request data, make the following replacements: 

  * `RULE_NAME`: the name of the rule. The name must be unique within your repository.
  * `ACTION`: the action applied to a download that matches this rule. Choose between `ALLOW` and `DENY`.
  * `PACKAGE`: the name of the package. If not supplied, the rule applies to the whole repository.
  * `CONDITION`: a [CEL expression](https://docs.cloud.google.com/artifact-registry/docs/download-rules#CEL) that defines a matching rule. If supplied, only applies the rule to downloads that match the specified condition. For example, `pkg.version.id < '3.0'`.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository.



HTTP method and URL: 
    
    
    PATCH https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME

Request JSON body: 
    
    
    {
      "action":"ACTION",
      "packageId":"PACKAGE",
      "condition":
      {
        "expression":"CONDITION"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME"

#### PowerShell (Windows)

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json" `  
        -InFile request.json `  
        -Uri "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME" | Select-Object -Expand Content

Updated rule details are shown similar to the following: 
    
    
    {
      "name": "projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME",
      "action": ACTION,
      "operation": "DOWNLOAD"
    }
    

For more information, see the [REST reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/update). 

## Delete download rules

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * `RULE_NAME`: the name of the rule. The name must be unique within your repository.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules delete RULE_NAME \
        --project=PROJECT \
        --location=LOCATION \
        --repository=REPOSITORY

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules delete RULE_NAME `
        --project=PROJECT `
        --location=LOCATION `
        --repository=REPOSITORY

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts rules delete RULE_NAME ^
        --project=PROJECT ^
        --location=LOCATION ^
        --repository=REPOSITORY

The rule is deleted with the following output: 
    
    
    You are about to delete rule [RULE_NAME]
    
    Do you want to continue (Y/n)?  Y
    
    Deleted rule [RULE_NAME].
    

For more information, see the [`gcloud artifacts rules delete`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/rules/delete) command. 

###  API 

Before using any of the request data, make the following replacements: 

  * `RULE_NAME`: the name of the rule. The name must be unique within your repository.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository.



HTTP method and URL: 
    
    
    DELETE https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://artifactregistry.googleapis.com/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/rules/RULE_NAME" | Select-Object -Expand Content

For more information, see the [REST reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories.rules/delete). 

## Use CEL to define conditions

You can define conditions for your download rules with [Common Expression Language](https://github.com/google/cel-spec) (CEL), which is an open-source language for expression evaluation. Artifact Registry provides the `pkg` object that contains the following attributes:

  * **`pkg.id`** : a string representing the package name of the artifact. Can be used with rules set at the repository level.
  * **`pkg.version.id`** : a string representing the version of the artifact.
  * **`pkg.version.tag`** : a string representing the tag of the artifact. Use only in a Docker repository.



You can use logical operators and built-in functions with CEL. The following are some example CEL expressions that might be useful in your download rules:

  * Useful for rules set at the repository level:
        
        pkg.id == 'myPackage'  #Artifact package matches 'myPackage'
          pkg.id.startsWith('my') #Artifact package must start with 'my'
        

  * Useful for rules set on packages:
        
        pkg.version.id != '1.0.0' #Artifact version is not '1.0.0'
          pkg.version.id > '1.0.1' || pkg.version.id < '0.0.1' #Artifact version is greater than '1.0.1' or less than '0.0.1'
          pkg.version.id.startsWith('1.0.') #Artifact version must start with '1.0.'
          pkg.version.id in ['1.0.0', '1.2.0'] #Artifact version must be a member of the list ['1.0.0', '1.2.0']
          pkg.version.tag == 'tag1' #Artifact tag must be 'tag1'
          pkg.version.tag.startsWith('tag') #Artifact tag must start with 'tag'
          pkg.version.tag in ['tag1', 'tag2'] #Artifact tag must be a member of the list ['tag1', 'tag2']
        




When adding rules with tag-based conditions such as `pkg.version.tag == 'latest'` in your Docker repositories, be aware of the following:

  * When pulling by digest, the client doesn't provide a tag. Conditions using tags will be matched against an empty tag and might result in unexpected behavior.
  * For multi-arch container images, conditions using tags might not work as expected and should be avoided.

**Note:** Download rules only apply to artifact downloads. Container pushes and metadata listings are separate operations, and can't be evaluated in the CEL schema.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
