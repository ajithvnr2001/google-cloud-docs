---
url: https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level/
title: Creating a custom access level \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:16.149648+00:00
---

# Creating a custom access level  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Creating a custom access level Stay organized with collections  Save and categorize content based on your preferences. 

After a custom access level is created, it can be [managed in the same manner as basic access levels](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels).

For details about building Common Expression Language (CEL) expressions for custom access levels, refer to the [custom access level specification](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec).

**Important:** You must have a paid subscription to use [device attributes](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec#device) in custom access level expressions. You can [sign up](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview) if interested.

###  Console 

To create a custom access level:

  1. Open the **Access Context Manager** page in the Google Cloud console.

[Open the Access Context Manager page](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select your organization.

  3. At the top of the **Access Context Manager** page, click **New**.

  4. In the **New Access Level** pane:

     1. In the **Access level title** box, enter a title for the access level. The title must be at most 50 characters, start with a letter, and can contain only numbers, letters, underscores, and spaces.

     2. Following **Create Conditions in** , select **Advanced Mode**.

     3. In the **Conditions** section, enter the expressions for your custom access level. The condition must resolve to a single boolean value.

For examples and more information about Common Expression Language (CEL) support and custom access levels, see the [Custom access level specification](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec).

     4. Click **Save**.




###  gcloud 

### Before you begin

  * If it doesn't exist yet, [create an access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy) for your organization.



To create a custom access level using the `gcloud` command-line tool, use the [`gcloud access-context-manager levels create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/create) command.
    
    
    gcloud access-context-manager levels create LEVEL_NAME \
      --title=TITLE \
      --custom-level-spec=FILE \
      --description=DESCRIPTION \
      --policy=POLICY_NAME

Where:

  * LEVEL_NAME is a unique name for the access level. It must begin with a letter and include only letters, numbers, and underscores. The name can be a maximum of 50 characters.

  * TITLE is the short, human-readable title for the access level.

  * FILE is a .yaml file that contains your CEL expression formatted as a single key-value pair: `expression: "CEL_EXPRESSION"`.

For examples and more information about Common Expression Language (CEL) support and custom access levels, see the [Custom access level specification](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec).

  * DESCRIPTION (optional) is a human-readable description of the access level.

  * POLICY_NAME is the numeric name of your organization's access policy.




Optionally, you can include any of the [`gcloud`-wide flags](https://docs.cloud.google.com/sdk/gcloud/reference).

### `custom-level-spec` YAML file

When you use the `gcloud` command-line tool to create a custom access level, you must provide a .yaml file for the `custom-level-spec` option. The .yaml file defines a CEL expression that resolves to a single boolean value. The .yaml file must contain a single key-value pair formatted as `expression: "CEL_EXPRESSION"`. The value for `expression` must be a string.

#### Example YAML file
    
    
    expression: "device.encryption_status == DeviceEncryptionStatus.ENCRYPTED && (origin.region_code in ['US'] || device.is_admin_approved_device)"
    

### Example command
    
    
    gcloud access-context-manager levels create Custom_Trust \
        --custom-level-spec=customspec.yaml \
        --description="Custom access level for corp." \
        --title="Custom Trust Level" \
        --policy=1521580097614100
    

###  REST 

### Before you begin

  * If it doesn't exist yet, [create an access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy) for your organization.



To create a custom access level, use the [`accessPolicies.accessLevels.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create) method.

## Request body

In the request body for the call, include an instance of the `AccessLevel` object.
    
    
    {
      "name": string,
      "title": string,
      "description": string,
      "custom": {
        "expr": {
          "expression": string,
          "title": string,
          "description": string
        }
      }
    }
    

For the `custom` field, create an object that includes the CEL expressions for your custom access level. The complete expression must resolve to a boolean value. The `title` and `description` fields are optional.

### Example
    
    
    {
      "name": "example_custom_level",
      "title": "Example custom level",
      "description": "An example custom access level.",
      "custom":  {
        "expr": {
          "expression": "device.is_corp_owned == true || (device.os_type != OsType.OS_UNSPECIFIED && device.is_admin_approved_device == true)",
          "title": "Check for known devices",
          "description": "Permits requests from corp-owned devices and admin-approved devices with a known OS."
        }
      }
    }
    

###  RPC 

### Before you begin

  * If it doesn't exist yet, [create an access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy) for your organization.



To create a custom access level, call [`CreateAccessLevel`](https://docs.cloud.google.com/access-context-manager/docs/reference/rpc/google.identity.accesscontextmanager.v1#accesscontextmanager).

For the `access_level` field, include an instance of `AccessLevel`.

Fields   
---  
`name` |  |  **Type** |  string   
---|---  
**Description** |  Required.  The resource name for the access level. The POLICY_ID is the numeric name of your Organization's access policy. The SHORT_NAME must begin with a letter, and include only letters, numbers, and underscores.  **Format:**
    
    
                    accessPolicies/policy_id/accessLevels/short_name
                      
  
`title` |  |  **Type** |  string   
---|---  
**Description** |  A human-readable label for the access level. Access levels must have unique names.   
`description` |  |  **Type** |  string   
---|---  
**Description** |  A description of the access level.   
`custom` |  |  **Type** |  string   
---|---  
**Description** |  The CEL expressions for your custom access level. The complete expression must resolve to a boolean value.   
  
## Examples of custom access levels

This section provides examples of custom access levels.

### Restrict access based on source project

You can restrict access to resources to only allow requests originating from specific Google Cloud projects and related tenant projects. Project-based access restriction is useful for securing service account interactions.

The following expression grants access if the request comes from `projects/123456789`:
    
    
    originatesFromProjects(origin, ["projects/123456789"])
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
