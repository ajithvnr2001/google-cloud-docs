---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/list/
title: Method: organizations.apiproducts.rateplans.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:20.631820+00:00
---

# Method: organizations.apiproducts.rateplans.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.apiproducts.rateplans.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all the rate plans for an API product.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/apiproducts/*}/rateplans`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the API product. Use the following structure in your request: `organizations/{org}/apiproducts/{apiproduct}` Use `organizations/{org}/apiproducts/-` to return rate plans for all API products within the organization.If the API Product resource has the `space` attribute set, IAM permissions are checked against the Space resource path. To learn more, read the [Apigee Spaces Overview](https://cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.rateplans.list`

  
  
### Query parameters

Parameters  
---  
`orderBy` |  `string` Name of the attribute used for sorting. Valid values include:

  * `name`: Name of the rate plan.
  * `state`: State of the rate plan (`DRAFT`, `PUBLISHED`).
  * `startTime`: Time when the rate plan becomes active.
  * `endTime`: Time when the rate plan expires.

**Note** : Not supported by Apigee at this time.  
`startKey` |  `string` Name of the rate plan from which to start displaying the list of rate plans. If omitted, the list starts from the first item.For example, to view the rate plans from 51-150, set the value of `startKey` to the name of the 51st rate plan and set the value of `count` to 100.  
`count` |  `integer` Number of rate plans to return in the API call. Use with the `startKey` parameter to provide more targeted filtering. The maximum limit is 1000. Defaults to 100.  
`expand` |  `boolean` Flag that specifies whether to expand the results. Set to `true` to get expanded details about each API. Defaults to `false`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#State)`)` State of the rate plans (`DRAFT`, `PUBLISHED`) that you want to display.  
  
### Request body

The request body must be empty.

### Response body

Response for [rateplans.list][RatePlan.ListRatePlans].

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ratePlans": [
        {
          object ([RatePlan](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#RatePlan))
        }
      ],
      "nextStartKey": string
    }  
  
Fields  
---  
`ratePlans[]` |  `object (`[RatePlan](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#RatePlan)`)` List of rate plans in an organization.  
`nextStartKey` |  `string` Value that can be sent as `startKey` to retrieve the next page of content. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
