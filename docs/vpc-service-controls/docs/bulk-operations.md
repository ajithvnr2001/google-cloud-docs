---
url: https://docs.cloud.google.com/vpc-service-controls/docs/bulk-operations/
title: Making bulk changes to service perimeters \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:41.084908+00:00
---

# Making bulk changes to service perimeters  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/bulk-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Making bulk changes to service perimeters Stay organized with collections  Save and categorize content based on your preferences. 

Using Access Context Manager, you can make bulk updates to resources that belong to your organization's [access policy](https://docs.cloud.google.com/access-context-manager/docs/overview#access-policies), such as [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) and [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters). Changes to your resources are applied only if all parts of the bulk operation are successful.

This topic describes only bulk replacement of service perimeters. For more information about bulk replacement of access levels, [refer to the Access Context Manager documentation](https://docs.cloud.google.com/access-context-manager/docs/bulk-operations).

**Note:** The Google Cloud console cannot be used for bulk operations.

## Get a list of service perimeters

Because bulk operations affect _all_ service perimeters for your organization, you can obtain a complete list of your perimeters. Also, you can format this list as YAML and use it to make bulk changes to your perimeters.

To get a formatted list of service perimeters, refer to [List service perimeters (formatted)](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#formatted-list).

When overriding all service perimeter configurations with the `replace-all` command, you must not set the `etag` fields within perimeters. Etags are likely to change between fetching and updating the perimeters, causing the `replace-all` command to return an etag mismatch error. However, you can set an `etag` for the entire `replace-all` request with the top-level `--etag` parameter if you want to enforce the etag check.

Instead of manually removing each of the `etag` properties within the perimeters, you can fetch the perimeters without `etag` properties by specifying a `--format` with all fields except `etag`.
    
    
    gcloud access-context-manager perimeters list \
      --policy=POLICY_NAME \
      --format="json(name,title,description,perimeterType,status,spec,useExplicitDryRunSpec)"

## Bulk replace service perimeters

The following section details how to bulk replace your service perimeters.

**Warning:** Bulk replace operations affect _all_ your service perimeters. If existing service perimeters aren't included in the operation, those service perimeters are deleted.

###  gcloud 

To bulk replace all service perimeters, use the `replace-all` command.
    
    
    gcloud access-context-manager perimeters replace-all POLICY_NAME \
      --source-file=FILE \
      --etag=ETAG \

Where:

  * POLICY_NAME is the name of your organization's access policy. This value is required only if you haven't set a [default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).

  * FILE is the name of a .yaml file that defines the new settings for your existing service perimeters.

For example:
        
        - name: accessPolicies/11271009391/servicePerimeters/storage_perimeter
          title: Storage Perimeter
          description: Perimeter to protect Storage resources.
          perimeterType: PERIMETER_TYPE_REGULAR
          status:
            restrictedServices:
            - storage.googleapis.com
        - name: accessPolicies/11271009391/servicePerimeters/bigquery_perimeter
          title: BigQuery Perimeter
          description: Perimeter to protect BigQuery resources.
          perimeterType: PERIMETER_TYPE_REGULAR
          status:
            restrictedServices:
            - bigquery.googleapis.com
        

For more information about formatting the YAML file, refer to the JSON structure of Access Context Manager's [`ServicePerimeterConfig` object](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeterConfig).

  * ETAG (optional) is a string that represents the target version of your organization's access policy. If you do not include an etag, the bulk operation targets the latest version of the your organization's access policy.

To obtain the latest etag of your access policy, [`list` your access policies](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy).




###  API 

To bulk replace all service perimeters, call [`servicePerimeters.replaceAll`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/replaceAll).
    
    
    POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_NAME/servicePerimeters.replaceAll?alt=json
    

Where:

  * POLICY_NAME is the name of your organization's access policy.



### Request body

The request body must include a list of [`ServicePerimeterConfig`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeterConfig) objects that specify the changes you want to make.

Optionally, to target a specific version of your organization's access policy, you can include an etag. If you do not include an etag, the bulk operation targets the latest version of your organization's access policy.

For example:
    
    
    {
      "servicePerimeters": [
        object (ServicePerimeterConfig),
        object (ServicePerimeterConfig),
        ...
      ]
      "etag": string
    }

### Response body

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the post operation.

Example response:
    
    
    {
      "name": "operations/accessPolicies/11271009391/replacePerimeters/1583523447707087",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse",
        "servicePerimeters": [
          {
            "name": "accessPolicies/11271009391/servicePerimeters/storage_perimeter",
            "title": "Storage Perimeter",
            "description": "Perimeter to protect Storage resources.",
            "status": {
              "accessLevels": [
                "accessPolicies/11271009391/accessLevels/corpnet_access"
              ],
              "restrictedServices": [
                "bigtable.googleapis.com"
              ]
            }
          },
          {
            "name": "accessPolicies/11271009391/servicePerimeters/storage_perimeter",
            "title": "BigQuery Perimeter",
            "description": "Perimeter to protect BigQuery resources.",
            "status": {
              "accessLevels": [
                "accessPolicies/11271009391/accessLevels/prodnet_access"
              ],
              "restrictedServices": [
                "bigtable.googleapis.com"
              ]
            }
          }
        ]
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
