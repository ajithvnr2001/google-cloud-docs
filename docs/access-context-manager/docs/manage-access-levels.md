---
url: https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels/
title: Managing access levels \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:16.562233+00:00
---

# Managing access levels  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Managing access levels Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage existing access levels. You can:

  * List access levels

  * List access levels (formatted)

  * Describe an access level

  * Update an access level

  * Delete an access level




## Before you begin

**Warning:** If you share an access level across Google Cloud and Google Workspace, modifying or deleting that access level can impact user access. For more information, see the [Google Workspace documentation](https://support.google.com/a/answer/13570967).

  * [Set your default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default) for using the `gcloud` command-line tool.

_-or-_

[Get the name of your policy.](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy) The policy name is required for commands using the `gcloud` command-line tool and making API calls. If you set a default access policy, you do not need to specify the policy for the `gcloud` command-line tool.

  * Ensure that you have an Identity and Access Management (IAM) role at the organization level that lets you manage access levels. Ask your administrator to grant you one of the following roles, or a custom role with the same permissions:

    * **To view access levels:** [Access Context Manager Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyReader) (`roles/accesscontextmanager.policyReader`)

    * **To view and change access levels:** [Access Context Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyEditor) (`roles/accesscontextmanager.policyEditor`) or [Access Context Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accesscontextmanager#accesscontextmanager.policyAdmin) (`roles/accesscontextmanager.policyAdmin`)




## List access levels

###  Console 

To list all access levels, open the **Access Context Manager** page in the Google Cloud console and then, if prompted, select your organization. Your organization's access levels are displayed in a grid on the page, including details about the configuration of each access level.

[Open the Access Context Manager page](https://console.cloud.google.com/security/access-level)

###  gcloud 

To list all access levels, use the [`list`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/list) command.
    
    
    gcloud access-context-manager levels list \
      [--policy=POLICY_NAME]

Replace the following:

  * `POLICY_NAME` is the name of your organization's access policy. This value is required only if you haven't set a [default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).



The output will look something like:
    
    
    NAME             TITLE                  LEVEL_TYPE
    Device_Trust     Device_Trust Extended  Basic
    Service_Group_A  Service_Group_A        Basic
    

###  API 

To list all the access levels for a policy, call [`accessLevels.list`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/list).
    
    
    GET https://accesscontextmanager.googleapis.com/v1alpha/accessPolicies/POLICY_NAME/accessLevels
    

Replace the following:

  * `POLICY_NAME` is the name of your organization's access policy.



### Request body

The request body must be empty.

### Optional parameters

Optionally, include one or more of the following query parameters.

Parameters  
---  
`pageSize` |  `number` By default, the list of [ access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) returned by `accessLevels.list` is paginated. Each page is limited to 100 access levels.  You can use this parameter to modify the number of access levels that are returned per page.   
`pageToken` |  `string` If the number of access levels returned by your call exceeded the page size, the response body will include a page token.  You can use this parameter in a subsequent call to obtain the next page of results.   
`accessLevelFormat` |  `enum([LevelFormat](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/LevelFormat))` Normally, access levels are returned as they are defined, either as `BasicLevel` or `CustomLevel`.  You can specify the value `CEL` for this parameter to return `BasicLevels` as `CustomLevels` in Cloud Common Expression Language.   
  
### Response body

If successful, the response body for the call contains an [`AccessLevels`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel) object that lists the access levels, and a [`nextPageToken`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/list#body.ListAccessLevelsResponse.FIELDS.next_page_token) string. `nextPageToken` only has a value if the number of access levels returned exceeds the page size. Otherwise, `nextPageToken` is returned as an empty string.

## List access levels (formatted)

Using the `gcloud` command-line tool, you can obtain a list of your access levels in YAML or JSON format.

To get a formatted list of access levels, use the [`list`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/list) command.
    
    
    gcloud access-context-manager levels list \
      --format=FORMAT \
      [--policy=POLICY_NAME]

Replace the following:

  * FORMAT is one of the following values:

    * `list` (YAML format)

    * `json` (JSON format)

  * `POLICY_NAME` is the name of your organization's access policy. This value is required only if you haven't set a [default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).




The YAML output will look something like: 
    
    
    - basic: {'conditions': [{'ipSubnetworks': ['8.8.0.0/24']}]}
      description: Level for corp access.
      name: accessPolicies/165717541651/accessLevels/corp_level
      title: Corp Level
    - basic: {'combiningFunction': 'OR', 'conditions': [{'ipSubnetworks': ['8.8.0.0/24']}]}
      description: Level for net access.
      name: accessPolicies/165717541651/accessLevels/net_level
      title: Net Level

The JSON output will look something like: 
    
    
    [
      {
        "basic": {
          "conditions": [
            {
              "ipSubnetworks": [
                "8.8.0.0/24"
              ]
            }
          ]
        },
        "description": "Level for corp access.",
        "name": "accessPolicies/165717541651/accessLevels/corp_level",
        "title": "Corp Level"
      },
      {
        "basic": {
          "combiningFunction": "OR",
          "conditions": [
            {
              "ipSubnetworks": [
                "8.8.0.0/24"
              ]
            }
          ]
        },
        "description": "Level for net access.",
        "name": "accessPolicies/165717541651/accessLevels/net_level",
        "title": "Net Level"
      }
    ]

## Describe an access level

###  Console 

Using Google Cloud console, refer to the steps to list access levels. When you list your access levels, details are provided in the grid that appears.

###  gcloud 

Listing access levels only provides their name, title, and level type. To get detailed information about what a level actually does, use the `describe` command.
    
    
    gcloud access-context-manager levels describe LEVEL_NAME \
        [--policy=POLICY_NAME]

Replace the following:

  * `LEVEL_NAME` is the name of the access level you want to describe.

  * `POLICY_NAME` is the name of your organization's access policy. This value is required only if you haven't set a [default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).




The command will print information about the level formatted as YAML. For example, if the level restricted access to certain operating system versions, the output might look something like:
    
    
    basic:
      conditions:
      - devicePolicy:
          allowedEncryptionStatuses:
          - ENCRYPTED
          osConstraints:
          - minimumVersion: 10.13.6
            osType: DESKTOP_MAC
          - minimumVersion: 10.0.18219
            osType: DESKTOP_WINDOWS
          - minimumVersion: 68.0.3440
            osType: DESKTOP_CHROME_OS
          requireScreenlock: true
    name: accessPolicies/330193482019/accessLevels/Device_Trust
    title: Device_Trust Extended

**Note:** To use the output of the describe command to update or create a basic access level, send the response to a .yaml file, and then edit the file to remove the `name`, `title`, `description`, `basic`, and `conditions` lines. 

###  API 

Listing access levels only provides the name, title, and type of the levels. To get detailed information about an access level, call [`accessLevels.get`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/get).
    
    
    GET https://accesscontextmanager.googleapis.com/v1alpha/accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME
    

Replace the following:

  * `POLICY_NAME` is the name of your organization's access policy.

  * `LEVEL_NAME` is the name of the access level you want to describe.




### Request body

The request body must be empty.

### Optional parameters

Optionally, include the `accessLevelFormat` query parameter. Normally, access levels are returned as they are defined, either as `BasicLevel` or `CustomLevel`.

You can specify the value `CEL` for this parameter to return `BasicLevels` as `CustomLevels` in Cloud Common Expression Language.

### Response body

If successful, the response body for the call contains an [`AccessLevel`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel) resource that includes details about what the access level does, the last time the level was updated, and more.

## Update an access level

This section describes how to update individual access levels. To update all of your organization's access levels in one operation, see [Making bulk changes to access levels](https://docs.cloud.google.com/access-context-manager/docs/bulk-operations).

###  Console 

To update an access level:

  1. Open the **Access Context Manager** page in the Google Cloud console.

[Open the Access Context Manager page](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select your organization.

  3. In the grid, click the name of the access level that you want to update.

  4. In the **Edit Access Level** pane, make changes to the access level.

For a complete list of the attributes that you can add or modify, read about [access level attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes).

  5. Click **Save**.

In addition to updating or removing any existing conditions, you can add new conditions and add new attributes to existing conditions.




###  gcloud 

Use the [`update`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/update) command to update an access level.

**Basic access level:**
    
    
    gcloud access-context-manager levels update LEVEL_NAME \
        --basic-level-spec=FILE \
        [--policy=POLICY_NAME]

**Custom access level:**
    
    
    gcloud access-context-manager levels update LEVEL_NAME \
        --custom-level-spec=FILE \
        [--policy=POLICY_NAME]

Replace the following:

  * `LEVEL_NAME` is the name of the access level that you want to update.

  * FILE is the name of a .yaml file that defines [the conditions for the access level](https://docs.cloud.google.com/access-context-manager/docs/example-yaml-file) (for basic access levels) or a [CEL expression](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec) that resolves to a single boolean value (for custom access levels).

For a complete list of the attributes that you can use in your basic access level conditions, read about [access level attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes).

  * `POLICY_NAME` is the name of your organization's access policy. This value is required only if you haven't set a [default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).

  * You can include one or more of the following options.

Options  
---  
`combine-function` |  This option is only used for _basic access levels_. Determines how conditions are combined. Valid values: `AND`, `OR`  
`description` |  A long-form description of the access level.  
`title` |  A short title for the access level. The access level's title is displayed in the Google Cloud console.  
  
You can include any of the [gcloud-wide flags](https://docs.cloud.google.com/sdk/gcloud/reference).




### Example command
    
    
    gcloud access-context-manager levels update Device_Trust \
        --basic-level-spec=corpdevspec.yaml \
        --combine-function=OR \
        --description='Access level that conforms to updated corporate spec.' \
        --title='Device_Trust Extended' \
        --policy=1034095178592

###  API 

To update an access level, call [`accessLevels.patch`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/patch).
    
    
    PATCH https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME?updateMask=FIELDS
    

Replace the following:

  * `POLICY_NAME` is the name of your organization's access policy.

  * `LEVEL_NAME` is the name of the access level you want to describe.

  * FIELDS is a comma-separated list of [fully-qualified field names](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/patch#query-parameters) that you are updating.




### Request body

The request body must include an [`AccessLevel`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels#AccessLevel) resource that specifies the changes you want to make to the access level.

### Response body

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the patch operation.

## Delete an access level

This section describes how to delete Access Context Manager access levels. Deleting an access level is a two-step process:

  1. Check access level dependencies.

  2. Delete an individual access level.




### Check access level dependencies

Before you delete an access level, ensure that it's not referenced by other access levels.

**Note:** Access levels can reference each other. Attempting to delete an access level that is referenced by another results in an error.

To find all access levels that reference the one that you want to delete, do the following:

  1. Make sure that you have installed `jq`. To verify that `jq` is installed, run `jq --version`. [Install `jq`](https://jqlang.org/download/).

  2. Check for access level dependencies. This command lists all access levels, then uses `jq` to filter for access levels that reference LEVEL_NAME in basic or custom level definitions.
         
         echo "Searching for Access Levels referencing: accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME"
         echo ""
         
         gcloud access-context-manager levels list \
           --policy="POLICY_NAME" \
           --format=json | \
         jq -r '
           .[] |
           select(
             # Check basic levels: Is the target access level present as an element in any requiredAccessLevels array?
             (.basic.conditions // []) | .[] | .requiredAccessLevels | index("accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME") != null
             or
             # Check custom levels: Does the expression string contain the target access level?
             (.custom.expr.expression // "") | contains("accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME")
           ) |
           "  - \(.title) (Name: \(.name))"
         '
         
         echo ""
         echo "If any levels are listed, they reference LEVEL_NAME. You must update these referencing levels before you delete LEVEL_NAME."

Replace the following:

     * `POLICY_NAME` is the name of your organization's access policy. This value is required only if you haven't set a [default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).

     * `LEVEL_NAME` is the name of the access level that you want to delete—for example, `my_level`.

In the output, any access levels that reference `accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME` are listed, along with their `title` and `name`. This includes both basic levels (where `accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME` is in `requiredAccessLevels`) and custom levels (where `accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME` appears in the `custom.expr.expression` string).

  3. If the command lists any referencing access levels, you must first update those levels to remove the dependency. For instructions, see Update an access level.




After all references are removed, you can proceed with deleting the individual access level.

### Delete an individual access level

###  Console 

To delete an access level:

  1. Open the **Access Context Manager** page in the Google Cloud console

[Open the Access Context Manager page](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select your organization.

  3. In the grid, in the row for the access level that you want to delete, click the _more_vert_ button.

  4. Click **Delete**.

  5. In the dialog box that appears, confirm that you want to delete the access level.




###  gcloud 

To delete an access level:

  1. Use the [`delete`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/delete) command to delete an access level.
         
         gcloud access-context-manager levels delete LEVEL_NAME \
             [--policy=POLICY_NAME]

Replace the following:

     * `LEVEL_NAME` is the name of the access level that you want to delete.

     * `POLICY_NAME` is the name of your organization's access policy. This value is required only if you haven't set a [default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).

  2. Confirm that you want to delete the access level.

For example:
         
         You are about to delete level Device_Trust
         
         Do you want to continue (Y/n)?
         

You should see output similar to the following:
         
         Waiting for operation [accessPolicies/330193482019/accessLevels/Device_Trust/delete/1531171874311645] to complete...done.
         Deleted level [Device_Trust].
         




###  API 

To delete an access level, call [`accessLevels.delete`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels/delete).
    
    
    DELETE https://accesscontextmanager.googleapis.com/v1alpha/accessPolicies/POLICY_NAME/accessLevels/LEVEL_NAME
    

Replace the following:

  * `POLICY_NAME` is the name of your organization's access policy.

  * `LEVEL_NAME` is the name of the access level you want to describe.




### Request body

The request body must be empty.

### Response body

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the delete operation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
