---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations
title: REST Resource: projects.configurations \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:56.198691+00:00
---

# REST Resource: projects.configurations  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  REST Resource: projects.configurations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Configuration
    * JSON representation
  * State
  * ConfigurationDetail
    * JSON representation
  * CustomerProfileConfig
    * JSON representation
  * CustomerProfileIndustry
    * JSON representation
  * CustomerProfileCompany
    * JSON representation
  * CustomerProfileProduct
    * JSON representation
  * CustomerProfileLocation
    * JSON representation
  * CustomerProfilePerson
    * JSON representation
  * CustomerProfileWebPresence
    * JSON representation
  * CustomerProfileSecurityConsiderations
    * JSON representation
  * CustomerProfileContactInfo
    * JSON representation
  * CustomerProfileCitation
    * JSON representation
  * CustomerProfileSummary
    * JSON representation
  * CustomerProfileCitedString
    * JSON representation
  * TechnologyWatchListConfig
    * JSON representation
  * TechnologyWatchListAlertThreshold
    * JSON representation
  * Methods



## Resource: Configuration

A configuration represents a behavior an engine should follow when producing new findings.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "audit": {
        object ([Audit](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/Audit))
      },
      "provider": string,
      "state": enum ([State](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#State)),
      "detail": {
        object ([ConfigurationDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#ConfigurationDetail))
      },
      "version": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Server generated name for the configuration. format is projects/{project}/configurations/{configuration}  
`displayName` |  `string` Output only. Human readable name for the configuration.  
`audit` |  `object (`[Audit](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/Audit)`)` Output only. Audit information for the configuration.  
`provider` |  `string` Required. Name of the service that provides the configuration.  
`state` |  `enum (`[State](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#State)`)` Optional. State of the configuration.  
`detail` |  `object (`[ConfigurationDetail](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#ConfigurationDetail)`)` Required. Domain specific details for the configuration.  
`version` |  `string` Optional. A user-manipulatable version. Does not adhere to a specific format  
`description` |  `string` Optional. A description of the configuration.  
  
## State

State of the configuration.

Enums  
---  
`STATE_UNSPECIFIED` | Configuration state is unspecified. This is not expected to occur.  
`ENABLED` | Configuration is enabled for the customer.  
`DISABLED` | Configuration is disabled for the customer.  
`DEPRECATED` | Configuration is deprecated, no new configs are allowed to be created.  
  
## ConfigurationDetail

Wrapper class that contains the union struct for all the various configuration detail specific classes.

JSON representation  
---  
      
    
    {
      "detailType": string,
    
      // Union field detail can be only one of the following:
      "customerProfile": {
        object ([CustomerProfileConfig](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileConfig))
      },
      "technologyWatchlist": {
        object ([TechnologyWatchListConfig](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#TechnologyWatchListConfig))
      }
      // End of list of possible types for union field detail.
    }  
  
Fields  
---  
`detailType` |  `string` Output only. Name of the detail type. Will be set by the server during creation to the name of the field that is set in the detail union.  
Union field `detail`. Domain specific details object. `detail` can be only one of the following:  
`customerProfile` |  `object (`[CustomerProfileConfig](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileConfig)`)` Customer Profile detail config.  
`technologyWatchlist` |  `object (`[TechnologyWatchListConfig](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#TechnologyWatchListConfig)`)` Technology Watchlist detail config.  
  
## CustomerProfileConfig

CustomerProfileConfig is the configuration for the customer profile. See [Get Started](https://docs.cloud.google.com/threat-intelligence/guides/get-started#customer-profile) for more details on creating and managing configurations.

JSON representation  
---  
      
    
    {
      "org": string,
      "orgSummary": string,
      "industries": [
        {
          object ([CustomerProfileIndustry](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileIndustry))
        }
      ],
      "parentCompanies": [
        {
          object ([CustomerProfileCompany](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCompany))
        }
      ],
      "products": [
        {
          object ([CustomerProfileProduct](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileProduct))
        }
      ],
      "locations": [
        {
          object ([CustomerProfileLocation](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileLocation))
        }
      ],
      "executives": [
        {
          object ([CustomerProfilePerson](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfilePerson))
        }
      ],
      "webPresences": [
        {
          object ([CustomerProfileWebPresence](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileWebPresence))
        }
      ],
      "technologyPresence": string,
      "securityConsiderations": {
        object ([CustomerProfileSecurityConsiderations](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileSecurityConsiderations))
      },
      "contactInfo": [
        {
          object ([CustomerProfileContactInfo](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileContactInfo))
        }
      ],
      "citations": [
        {
          object ([CustomerProfileCitation](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitation))
        }
      ],
      "summary": {
        object ([CustomerProfileSummary](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileSummary))
      }
    }  
  
Fields  
---  
`org` |  `string` Required. The name of the organization.  
`orgSummary` |  `string` Optional. A summary of the organization.  
`industries[]` |  `object (`[CustomerProfileIndustry](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileIndustry)`)` Optional. The industries the organization is involved in.  
`parentCompanies[]` |  `object (`[CustomerProfileCompany](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCompany)`)` Optional. The parent companies of the organization.  
`products[]` |  `object (`[CustomerProfileProduct](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileProduct)`)` Optional. Product information for the organization.  
`locations[]` |  `object (`[CustomerProfileLocation](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileLocation)`)` Optional. Locations the organization is present or conducts business in.  
`executives[]` |  `object (`[CustomerProfilePerson](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfilePerson)`)` Optional. Executives of the organization.  
`webPresences[]` |  `object (`[CustomerProfileWebPresence](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileWebPresence)`)` Optional. Web presence of the organization.  
`technologyPresence` |  `string` Optional. Technology presence of the organization.  
`securityConsiderations` |  `object (`[CustomerProfileSecurityConsiderations](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileSecurityConsiderations)`)` Optional. Security considerations for the organization.  
`contactInfo[]` |  `object (`[CustomerProfileContactInfo](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileContactInfo)`)` Optional. Contact information for the organization.  
`citations[]` |  `object (`[CustomerProfileCitation](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitation)`)` Optional. Citations for the organization profile.  
`summary` |  `object (`[CustomerProfileSummary](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileSummary)`)` Optional. A summarized version of the customer profile.  
  
## CustomerProfileIndustry

Industry information for the customer profile.

JSON representation  
---  
      
    
    {
      "industry": string,
      "citationIds": [
        string
      ]
    }  
  
Fields  
---  
`industry` |  `string` Required. The name of the industry.  
`citationIds[]` |  `string` Optional. The citation ids for the industry.  
  
## CustomerProfileCompany

Company information for the customer profile.

JSON representation  
---  
      
    
    {
      "company": string,
      "citationIds": [
        string
      ]
    }  
  
Fields  
---  
`company` |  `string` Required. The name of the company.  
`citationIds[]` |  `string` Optional. The citation ids for the company.  
  
## CustomerProfileProduct

Product information for the customer profile.

JSON representation  
---  
      
    
    {
      "product": string,
      "brand": string,
      "citationIds": [
        string
      ]
    }  
  
Fields  
---  
`product` |  `string` Required. The name of the product.  
`brand` |  `string` Required. The brand of the product.  
`citationIds[]` |  `string` Optional. The citation ids for the product.  
  
## CustomerProfileLocation

Location information for the customer profile.

JSON representation  
---  
      
    
    {
      "facilityType": string,
      "brand": string,
      "address": string,
      "citationIds": [
        string
      ]
    }  
  
Fields  
---  
`facilityType` |  `string` Optional. The type of location.  
`brand` |  `string` Required. The brand of the location.  
`address` |  `string` Required. The address of the location.  
`citationIds[]` |  `string` Optional. The citation ids for the location.  
  
## CustomerProfilePerson

Person information for the customer profile.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "citationIds": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the person.  
`title` |  `string` Optional. The title of the person.  
`citationIds[]` |  `string` Optional. The citation ids for the person.  
  
## CustomerProfileWebPresence

Web presence information for the customer profile.

JSON representation  
---  
      
    
    {
      "domain": string,
      "citationIds": [
        string
      ]
    }  
  
Fields  
---  
`domain` |  `string` Required. The domain name of the web presence.  
`citationIds[]` |  `string` Optional. The citation ids for the web presence.  
  
## CustomerProfileSecurityConsiderations

Security considerations for the customer profile.

JSON representation  
---  
      
    
    {
      "note": string,
      "considerations": [
        string
      ]
    }  
  
Fields  
---  
`note` |  `string` Optional. A note about the security considerations.  
`considerations[]` |  `string` Optional. A series of considerations for the security of the organization, such as "high risk of compromise" or "vulnerable to cyberbullying".  
  
## CustomerProfileContactInfo

Contact information for the customer profile.

JSON representation  
---  
      
    
    {
      "label": string,
      "citationIds": [
        string
      ],
    
      // Union field contact_info can be only one of the following:
      "email": string,
      "phone": string,
      "address": string,
      "other": string
      // End of list of possible types for union field contact_info.
    }  
  
Fields  
---  
`label` |  `string` Optional. The name of the contact.  
`citationIds[]` |  `string` Optional. The citation ids for the contact information.  
Union field `contact_info`. The contact information for the customer profile. `contact_info` can be only one of the following:  
`email` |  `string` The email address of the contact.  
`phone` |  `string` The phone number of the contact.  
`address` |  `string` The address of the contact.  
`other` |  `string` The other contact information.  
  
## CustomerProfileCitation

Citation information for the customer profile.

JSON representation  
---  
      
    
    {
      "citationId": string,
      "uri": string,
      "retrievalTime": string,
      "source": string,
      "document": string
    }  
  
Fields  
---  
`citationId` |  `string` Required. The citation id for the citation. Should be unique within the profile.  
`uri` |  `string` Optional. The url of the citation.  
`retrievalTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the citation was retrieved.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`source` |  `string` Required. The source of the citation.  
`document` |  `string` Required. The name of the document the citation is from.  
  
## CustomerProfileSummary

A summarized version of the customer profile. Generated by the backend.

JSON representation  
---  
      
    
    {
      "title": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "entityType": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "industry": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "founded": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "headquarters": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "areaServed": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "keyPeopleSummary": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "productsSummary": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "servicesSummary": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "brands": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "parentCompany": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      },
      "primaryWebsite": {
        object ([CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString))
      }
    }  
  
Fields  
---  
`title` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. The official name of the customer.  
`entityType` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. The entity type of the customer.  
`industry` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. The industry the customer is in.  
`founded` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. The date the customer was founded.  
`headquarters` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. The headquarters of the customer.  
`areaServed` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. The area the customer serves.  
`keyPeopleSummary` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. A narrative summary of key people.  
`productsSummary` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. A narrative summary of products.  
`servicesSummary` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. A narrative summary of services.  
`brands` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. A narrative summary of brands.  
`parentCompany` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. The parent company of the customer.  
`primaryWebsite` |  `object (`[CustomerProfileCitedString](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#CustomerProfileCitedString)`)` Optional. The primary website of the customer.  
  
## CustomerProfileCitedString

A string with citation ids.

JSON representation  
---  
      
    
    {
      "value": string,
      "citationIds": [
        string
      ]
    }  
  
Fields  
---  
`value` |  `string` Required. The value of the string.  
`citationIds[]` |  `string` Optional. The citation ids for the string.  
  
## TechnologyWatchListConfig

TechnologyWatchListConfig is the configuration for the technology watchlist threat scenario. See [Get Started](https://docs.cloud.google.com/threat-intelligence/guides/get-started#threat-scenario-configurations) for more details on creating and managing threat scenario configurations.

JSON representation  
---  
      
    
    {
      "technologies": [
        string
      ],
      "alertThreshold": {
        object ([TechnologyWatchListAlertThreshold](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#TechnologyWatchListAlertThreshold))
      }
    }  
  
Fields  
---  
`technologies[]` |  `string` Optional. List of vendor, technology or cpe fingerprint. example: Microsoft office 360 Apache Server 3.5 cpe:2.3:a:microsoft:outlook:*:*:*:*:*:*:*:*  
`alertThreshold` |  `object (`[TechnologyWatchListAlertThreshold](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#TechnologyWatchListAlertThreshold)`)` Optional. Alert thresholds to effectively reduce noise.  
  
## TechnologyWatchListAlertThreshold

TechnologyWatchListAlertThreshold contains the thresholds for alerting.

JSON representation  
---  
      
    
    {
      "priorityMinimum": enum ([Priority](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/Priority)),
      "cvssScoreMinimum": number,
      "epssScoreMinimum": number,
      "exploitationStates": [
        enum ([ExploitationState](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/ExploitationState))
      ],
      "riskRatingMinimum": enum ([RiskRating](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RiskRating))
    }  
  
Fields  
---  
`priorityMinimum` |  `enum (`[Priority](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/Priority)`)` Optional. The minimum priority for the alert.  
`cvssScoreMinimum` |  `number` Optional. The minimum CVSS score for the alert. Evaluates to CVSS v3 when available with a fallback to v2 and v4. Ex: 7.0. Valid range is [0.0, 10.0].  
`epssScoreMinimum` |  `number` Optional. The minimum epss score for the alert. Ex: 0.8. Valid range is [0.0, 1.0].  
`exploitationStates[]` |  `enum (`[ExploitationState](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/ExploitationState)`)` Optional. The exploitation states of the alert.  
`riskRatingMinimum` |  `enum (`[RiskRating](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RiskRating)`)` Optional. The minimum risk rating for the alert.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations/get)`

|  Get a configuration by name.  
  
### `[list](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations/list)`

|  Get a list of configurations that meet the filter criteria.  
  
### `[upsert](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations/upsert)`

|  Creates or updates a configuration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
