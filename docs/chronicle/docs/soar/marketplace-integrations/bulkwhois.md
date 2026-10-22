---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/bulkwhois/
title: Bulk Whois \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:16.641948+00:00
---

# Bulk Whois  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/bulkwhois/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bulk Whois

This document describes how to integrate Bulk Whois with Google Security Operations.

## Configure Bulk Whois to work with Google Security Operations

### How to obtain API credentials

  1. To obtain API credentials, sign in to your [Bulk Whois API account](https://bulk-whois-api.com/log/in).

  2. Navigate to the **My Account** section and select **API Credentials** in the left side menu where your API Key is ready for use.




### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure Bulk Whois integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Api Key | String | N/A | Yes | API key generated in Bulk Whois console.  
Api Secret | String | N/A | Yes | Generated in Bulk Whois console with API Key.  
Verify SSL | Checkbox | Checked | No | Use this checkbox, if your Bulk Whois connection requires an SSL verification (unchecked by default).  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
null | N/A | N/A  
  
### WhoIs Details

#### Description

Get domain/IP Whois info.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * IP Address



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
RegistrarWHOISServer | Returns if it exists in JSON result  
UpdatedDate | Returns if it exists in JSON result  
Reseller | Returns if it exists in JSON result  
DNSSEC | Returns if it exists in JSON result  
DomainName | Returns if it exists in JSON result  
RegistrarIANAID | Returns if it exists in JSON result  
RegistrantCountry | Returns if it exists in JSON result  
RegistrarAbuseContactEmail | Returns if it exists in JSON result  
RegistryDomainID | Returns if it exists in JSON result  
DomainStatus | Returns if it exists in JSON result  
RegistrarAbuseContactPhone | Returns if it exists in JSON result  
RegistryExpiryDate | Returns if it exists in JSON result  
Registrar | Returns if it exists in JSON result  
RegistrantOrganization | Returns if it exists in JSON result  
NameServer | Returns if it exists in JSON result  
CreationDate | Returns if it exists in JSON result  
RegistrarURL | Returns if it exists in JSON result  
RegistrantStateProvince | Returns if it exists in JSON result  
RegistrarRegistrationExpirationDate | Returns if it exists in JSON result  
LastupdateofWHOISdatabase | Returns if it exists in JSON result  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_enriched | True/False | is_enriched:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult": {
                "RegistrarWHOISServer": " ",
                "UpdatedDate": "2018-05-22T09",
                "Reseller": " ",
                "DNSSEC": "unsigned",
                "DomainName": "GOOGLE.CO.IN",
                "RegistrarIANAID": "292",
                "RegistrantCountry": "US",
                "RegistrarAbuseContactEmail": " ",
                "RegistryDomainID": "D8357-AFIN",
                "DomainStatus": "clientUpdateProhibited",
                "RegistrarAbuseContactPhone": " ",
                "RegistryExpiryDate": "2019-06-23T14",
                "Registrar": "MarkMonitorInc.",
                "RegistrantOrganization": "GoogleInc.",
                "NameServer": "NS4.GOOGLE.COM",
                "CreationDate": "2003-06-23T14",
                "RegistrarURL": "http",
                "RegistrantState/Province": "CA",
                "RegistrarRegistrationExpirationDate": " ",
                ">>>LastupdateofWHOISdatabase": "2019-01-15T06"
            },
            "Entity": "GOOGLE.CO.IN"
        }
    ]
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
