---
url: https://docs.cloud.google.com/access-context-manager/docs/manage-access-bindings/
title: Manage access bindings \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:50.656993+00:00
---

# Manage access bindings  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/manage-access-bindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Manage access bindings Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to manage your existing access bindings, which define how access policies are applied to your user groups or service accounts. You can view, modify, and delete these bindings as needed. Access bindings determine how access levels and session controls are applied to a user group or service account.

For information about how to create access bindings for users, and for more details on access levels and session controls, see [Apply policies to user groups with access bindings](https://docs.cloud.google.com/access-context-manager/docs/apply-policies-to-user-groups).

For more information about how to create access bindings for service accounts, see [Configure Context-Aware Access for service accounts](https://docs.cloud.google.com/access-context-manager/docs/set-up-caa-service-accounts).

**Preview — Session controls feature only**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## List access bindings

To list all previously created access bindings for user groups, do the following:

###  gcloud 

To list all access bindings for users by using the gcloud CLI, run the following command. To list access bindings for service accounts, you must use a filter.
    
    
    gcloud access-context-manager cloud-bindings list \
      --organization ORGANIZATION_ID
    

ORG_ID: Your organization ID. If the `access-context-manager/organization` property hasn't been set, replace `ORG_ID` in the optional `--organization` flag with the ID for the organization that you used when creating the `GcpAccessAdmin` role. 

To list access bindings on specific resources, you can use a filter flag.
    
    
      --filter="FILTER"
    

Replace `FILTER` with a filter that describes the resource that the access policy is bound to—for example:

  * User groups: `principal:group_key`



  * Service accounts: `principal:service_account OR principal:service_account_project_number`

**Note:** For service accounts, this is the only acceptable filter.



### REST API

To list all `USER_LOGIN` access bindings, run the following command:
    
    
    curl -H "X-Goog-User-Project: PROJECT_ID" -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://accesscontextmanager.googleapis.com/v1/organizations/ORGANIZATION_ID/gcpUserAccessBindings"
    

To list access bindings on specific resources, you can use a filter parameter.
    
    
    curl -H "X-Goog-User-Project: PROJECT_ID" -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://accesscontextmanager.googleapis.com/v1/organizations/ORGANIZATION_ID/gcpUserAccessBindings?filter=FILTER"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project
  * `ORGANIZATION_ID`: the ID of the organization
  * `FILTER`: a filter that describes the resource that the access policy is bound to—for example:

    * User groups: `principal:group_key`

    * Service accounts: `principal:service_account OR principal:service_account_project_number`

**Note:** For service accounts, this is the only acceptable filter.



## View an access binding

After the access bindings are created for a group of users, access to the Google Cloud console and Google Cloud APIs is controlled based on satisfaction of the bound access level.

You can view the details of the access binding that you created, edit it, or delete it.

###  Console 

  1. In the Google Cloud console, go to the **Access Context Manager** page.

[Go to Access Context Manager](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select a project. The access bindings are listed on the Access Context Manager page.




###  gcloud 

To view the details of an access binding, run the following command:
    
    
      gcloud access-context-manager cloud-bindings describe \
      --binding=BINDING_ID
    

`BINDING_ID` is the ID of the access-binding or fully qualified identifier for the access binding. 

###  API 

View the details of an access binding:

HTTP method and URL: 
    
    
    GET https://accesscontextmanager.googleapis.com/v1/BINDING_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://accesscontextmanager.googleapis.com/v1/BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://accesscontextmanager.googleapis.com/v1/BINDING_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "organizations/427391306986/gcpUserAccessBindings/aAQS-YRSviv2hC12vZFUN3AZzvwa6KV2hJ89iMytB_nHUcT1l",
      "groupKey": "045jfvxd0ybeul8",
      "accessLevels": [
        "accessPolicies/305009197125/accessLevels/device_lock"
      ],
      "dryRunAccessLevels": [
        "accessPolicies/305009197125/accessLevels/another"
      ]
    }
    
    

## Update an access binding

You can update an access binding to do the following:

  * Add, remove, or change which applications have a policy.
  * Modify the access levels for an application within a user group.
  * Add a new dry run access level or promote an existing one to a live level.

**Important:** You can't change the user group after an access binding is created. You must create a new access binding if you need to change the user group.

###  Console 

  1. In the Google Cloud console, go to the **Access Context Manager** page.

[Go to Access Context Manager](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select a project.

  3. On the Access Context Manager page, select an access binding and then click **Edit** to update it.




You cannot update access bindings with dry run access levels or session controls in the Google Cloud console.

###  gcloud 

  1. Create a YAML binding file.
         
         gcloud access-context-manager cloud-bindings update \
           --binding=ACCESS_BINDING \
           --binding-file=BINDING_FILE_PATH \
           --level=DEFAULT_ACCESS_LEVEL \
           --dry-run-level=DEFAULT_DRY_RUN_ACCESS_LEVEL
         [  --session-length=DEFAULT_SESSION_LENGTH                ]
         [  --session-reauth-method=DEFAULT_SESSION_REAUTH_METHOD  ]
         

Replace the following:

     * `ACCESS_BINDING` is in the form `organizations/ORG_ID/gcpUserAccessBindings/ACCESS_BINDING_NAME`. 
     * BINDING_FILE_PATH: The path to the YAML file that contains the access binding scheme. The binding file supports only `scopedAccessSettings`. 
     * DEFAULT_ACCESS_LEVEL: The optional access level name, which takes the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`. Replace `POLICY_ID` with the access policy ID, and `ACCESS_LEVEL_NAME` with the access level name. 
     * DEFAULT_DRY_RUN_ACCESS_LEVEL_2: An optional access level name in the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`. Include this flag to apply the specified dry run access level to all applications by default if they aren't specified in the YAML. 
     * DEFAULT_SESSION_LENGTH: The optional session duration in the hour format, such as `15h` for 15 hours, or `2h` for two hours. 
     * DEFAULT_SESSION_REAUTH_METHOD: The optional method to challenge users to re-verify their identity, which must be one of the following: 
       * `LOGIN`: Apply the standard login, which can include MFA or other Workspace-defined factors.
       * `PASSWORD`: Only require a password, even if other factors are defined. If passwords are managed using an external IdP, users are redirected to the IdP. If the IdP session is live, users are implicitly re-authenticated. If the IdP is not live, users must sign in through the IdP.
       * `SECURITY_KEY`: Require a hardware security key.

#### How the `--level` and `--binding-file` arguments work together

     * If you only use `--binding-file`, only the applications in the file have the policies applied.
     * If you only use `--level`, the access level applies to all applications.
     * If you use both, the rules are combined. The `--level` value applies to all applications, whereas the policies in the YAML file specified by `--binding-file` only apply to the applications as defined in the file.

#### Working with session controls

     * To set default session controls for all applications, use `--session-length` and `--session-reauth-method`.
     * If you also define session controls in the YAML file, those session controls override the default settings for those specific applications.
     * You must use `--session-length` and `--session-reauth-method` together.

To remove a default access level or a default dry run access level, provide an empty string, such as `--level=` or `--dry-run-level=`. When these arguments are not provided, the `update` command won't make any changes.

To remove a session control, set `--session-length=0`.




###  API 

  1. Create a JSON body.
         
         {
           "accessLevels": [
             "DEFAULT_ACCESS_LEVEL"
           ],
           "scopedAccessSettings": [
             {
               "scope": {
                 "clientScope": {
                   "restrictedClientApplication": {
                     "clientId": "CLIENT_ID"
                   }
                 }
               },
               "activeSettings": {
                 "accessLevels": [
                   "ACCESS_LEVEL_A"
                 ],
                 "sessionSettings": {
                   "sessionLength": "SESSION_LENGTH",
                   "sessionReauthMethod": "SESSION_REAUTH_METHOD",
                   "sessionLengthEnabled": true
                 }
               }
             },
             {
               "scope": {
                 "clientScope": {
                   "restrictedClientApplication": {
                     "name": "CLIENT_NAME"
                   }
                 }
               },
               "activeSettings": {
                 "accessLevels": [
                   "ACCESS_LEVEL_C"
                 ]
               }
             }
           ]
         }
         

Replace the following:

     * DEFAULT_ACCESS_LEVEL: The optional access level name, which takes the form `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`. Replace `POLICY_ID` with the access policy ID, and `ACCESS_LEVEL_NAME` with the access level name. 
     * CLIENT_ID: The OAuth client ID. You can use either `clientId` or `name` when an application contains `sessionSettings`.
     * ACCESS_LEVEL_A: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.
     * SESSION_LENGTH: The session duration using ISO 8601 duration format, such as `30m` for 30 minutes, or `2h` for two hours.
     * SESSION_REAUTH_METHOD: The optional method to challenge users to re-verify their identity, which must be one of the following:

       * `LOGIN`: Apply the standard login, which can include MFA or other Workspace-defined factors.
       * `PASSWORD`: Only require a password, even if other factors are defined. If passwords are managed using an external IdP, users are redirected to the IdP. If the IdP session is live, users are implicitly re-authenticated. If the IdP is not live, users must sign in through the IdP.
       * `SECURITY_KEY`: Require a hardware security key.
     * CLIENT_NAME: The client name. You can use either `name` or `clientId` when an application contains `sessionSettings`.

     * ACCESS_LEVEL_C: An access level name in the format `accessPolicies/POLICY_ID/accessLevels/ACCESS_LEVEL_NAME`.

  2. Send the PATCH request.
         
         PATCH https://accesscontextmanager.googleapis.com/v1/ACCESS_BINDING?updateMask=FIELD_MASK
         

Replace the following:

     * `ACCESS_BINDING` is in the form `organizations/ORG_ID/gcpUserAccessBindings/ACCESS_BINDING_NAME`. 
     * FIELD_MASK: A required, comma-separated list of fields that you want to update. This tells the API which parts of the access binding to modify.

`fieldMask` should contain the top-level JSON keys in the request body that you want to update, which can contain `accessLevels`, `dryRunAccessLevels`, and `scopedAccessSettings`.

**Important:** If you don't include a `fieldMask`, nothing is updated.

If successful, you should receive a representation of the JSON object. If there is a problem, you receive an error message.




## Delete access bindings

###  Console 

  1. In the Google Cloud console, go to the **Access Context Manager** page.

[Go to Access Context Manager](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select a project.

  3. On the Access Context Manager page, select an access binding, and then click **Delete**.




###  gcloud 
    
    
       gcloud access-context-manager cloud-bindings delete \
           --binding ACCESS_BINDING
    

Replace the following:

  * `ACCESS_BINDING` is in the form `organizations/ORG_ID/gcpUserAccessBindings/ACCESS_BINDING_NAME`. 
  * `ACCESS_BINDING_NAME` is the unique string returned for the `name` identifier when the access binding was created. 



###  API 

Before using any of the request data, make the following replacements: 

  * `ACCESS_BINDING_NAME` is the unique string returned for the `name` identifier when the access binding was created. 



HTTP method and URL: 
    
    
    DELETE https://accesscontextmanager.googleapis.com/v1/ACCESS_BINDING_NAME

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://accesscontextmanager.googleapis.com/v1/ACCESS_BINDING_NAME"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://accesscontextmanager.googleapis.com/v1/ACCESS_BINDING_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
