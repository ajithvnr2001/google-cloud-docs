---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.iocAssociations/fetchRelated/
title: Method: iocAssociations.fetchRelated \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:45.384129+00:00
---

# Method: iocAssociations.fetchRelated  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.iocAssociations/fetchRelated/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: iocAssociations.fetchRelated Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.iocAssociations.fetchRelated

List related Associations (Threat Actors or Malware Families) for a given threat resource.

### HTTP request

`GET https://{endpoint}/v1alpha/{parent}/iocAssociations:fetchRelated`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the Associations (Threat Actors or Malware Families). Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Query parameters

Parameters  
---  
`associationType` |  `enum (`[AssociationType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.iocAssociations#IocAssociation.AssociationType)`)` Required. The type (Threat Actor or Malware Family) of related Associations to return.  
`pageSize` |  `integer` Optional. The maximum number of Associations (Threat Actors or Malware Families) to return. The default is 10, and the maximum value is 40.  
`pageToken` |  `string` Optional. A page token, received from a previous `iocAssociations.fetchRelated` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `iocAssociations.fetchRelated` must match the call that provided the page token.  
`orderBy` |  `string` Optional. The order to sort the returned Associations by. Default is descending last_modification_date. The supported order syntax matches the fields defined in the GTI API docs here: <https://gtidocs.virustotal.com/reference/list-threats#allowed-orders>Supported orders: - name: sorts objects alphabetically by name, ascending + or descending -. Name in this context refers to the threatDisplayName for an Association. - last_modification_date: sorts objects descending - by most recently modified objects first, or ascending + by firstly modified objects first. This refers to the lastReferenceTime field for an Association.  
The threat resource to get the related associations (Threat Actors or Malware Families) for. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`iocAssociation` |  `string` Optional. The name of the IocAssociation resource (Threat Actor or Malware Family) to get the related associations (Threat Actors or Malware Families) for. Format: projects/{project}/locations/{location}/instances/{instance}/iocAssociations/{iocAssociation}  
`ioc` |  `string` Optional. The name of the ioc resource to get the related associations (Threat Actors or Malware Families) for. Format: projects/{project}/locations/{location}/instances/{instance}/iocs/{ioc}  
`threatCollection` |  `string` Optional. The name of the ThreatCollection resource (GTI Campaign or Report) to get the related associations (Threat Actors or Malware Families) for. Format: projects/{project}/locations/{location}/instances/{instance}/threatCollections/{threatCollection}  
End of mutually exclusive fields.  
  
### Request body

The request body must be empty.

### Response body

Response containing a list of related associations (Threat Actors or Malware Families) for a given threat resource.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "iocAssociations": [
        {
          object ([IocAssociation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.iocAssociations#IocAssociation))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`iocAssociations[]` |  `object (`[IocAssociation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.iocAssociations#IocAssociation)`)` Output only. The list of related associations (Threat Actors or Malware Families).  
`nextPageToken` |  `string` Output only. A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`totalSize` |  `integer` Output only. The total number of associations (Threat Actors or Malware Families) that match the request. The count of `iocAssociations` returned by pagination may be less than the `totalSize` that matches.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `chronicle.iocAssociations.fetchRelated`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
