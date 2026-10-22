---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/hashicorp-vault/
title: HashiCorp Vault \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:12.565562+00:00
---

# HashiCorp Vault  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/hashicorp-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# HashiCorp Vault

This document provides guidance on how to integrate HashiCorp Vault with Google SecOps.

## Integrate HashiCorp Vault with Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration inputs

To configure the integration, use the following parameters:

Parameters  
---  
`API Root` | **Required** API root to connect to. Default value is `https://IP_ADDRESS:8200.`  
`Token` | _Optional_ Token to use for the connection. You can authenticate with either a token or the username and password combination.  
`Username` | _Optional_ Username to use for the connection. You can authenticate with either a token or the username and password combination.  
`Password` | _Optional_ Password to use for the connection. You can authenticate with either a token or the username and password combination.   
`Verify SSL` | _Optional_ If checked, the certificate configured for the API root is validated. Unchecked by default.  
`Key-Value Secret Engine Path` | **Required** Path used for the key-value secret storage. Only version 2 is supported. This parameter is used to interact with secrets stored in a storage and construct URLs such as `https://IP_ADDRESS:8200/v1/secret/data/ `.Default value is `secret`.  
  
## Actions

### Generate AWS Credentials

Generate credentials based on AWS role stored in HashiCorp Vault.

#### Entities

This action doesn't run on entities.

#### Action inputs

To configure the integration, use the following parameters:

Parameters  
---  
`AWS Secret Engine Path` | _Optional_ Path used for the AWS secret storage. Only version 2 is supported. This parameter is used to interact with secrets stored in a storage and construct URLs such as `http://IP_ADDRESS:8200/v1/aws/roles/ `.Default value is `aws`.  
`AWS Role Name` | **Required** Role name to generate credentials for.  
`AWS Role ARN` | _Optional_ ARN of the role to assume if the `credential_type` on the vault role is set to `assumed_role`. This parameter should match with one of the allowed role ARNs in the vault role.  
`AWS Role Session Name` | _Optional_ Role session name to attach to the assumed role ARN. If no value is provided, it is generated dynamically by default.  
`TTL (seconds)` | _Optional_ TTL in seconds for the use of the STS token.This parameter is specified as a string with a duration suffix and valid only when the AWS role `credential_type` in a Vault is either `assumed_role` or `federation_token`. When this parameter isn't specified, the `default_sts_ttl` value set for the role is used. If the `default_sts_ttl`value is also not set, the default value of 3600 seconds is used.  
`JSON Expression Builder` | _Optional_ JSON expression to filter a specific subset of data from a secret. Example is as follows: `| "data" | "data" | "key0"`.  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | Available  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
    "request_id": "08fe0196-fd51-8c32-9a90-a245ad6ade29",
    "lease_id": "aws/creds/my-role/MWLgJVdR2n8YwQuuX1dVN3Nv",
    "renewable": true,
    "lease_duration": 2764800,
    "data": {
    "access_key": "AKIAWP5MI7…",
    "secret_key": "CwYA8StJ8r+Oe0AKS8JnBvOWNOF…",
    "security_token": null
    },
    "wrap_info": null,
    "warnings": null,
    "auth": null
    }
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully generated credentials for the ROLE_NAME role.` | Action succeeded.  
`Error executing action "Generate AWS Credentials". Reason: Incorrect JSON value is provided for the Expression Builder.` | Action failed.Check the `JSON Expression Builder` parameter value.  
`Error executing action "Generate AWS Credentials". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
### List AWS Roles

List AWS roles available in the HashiCorp Vault based on provided criteria.

#### Entities

This action doesn't run on entities.

#### Action inputs

To configure the integration, use the following parameters:

Parameters  
---  
`AWS Secret Engine Path` | _Optional_ Path used for the AWS secret storage. Only version 2 is supported. This parameter is used to interact with secrets stored in a storage and construct URLs such as `http://IP_ADDRESS:8200/v1/aws/roles/ `.Default value is `aws`.  
`Max Records To Return` | _Optional_ Number of records to return. If no value is provided, the action returns 50 records by default.  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | Available  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
    "request_id": "7356485b-4186-3873-72e3-d2e588dc6fb6",
    "lease_id": "",
    "renewable": false,
    "lease_duration": 0,
    "data": {
    "keys": [
    "m",
    "my-other-role",
    "my-role"
    ]
    },
    "wrap_info": null,
    "warnings": null,
    "auth": null
    }
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found AWS roles in the AWS_SECRET_ENGINE_PATH store.` | Action succeeded.  
`Error executing action "List AWS Roles". Reason: Invalid value was provided for "Max Records to Return": PROVIDED_VALUE . Positive number should be provided.` | Action failed.Check the `Max Records to Return` parameter value.  
`Error executing action "List AWS Roles". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
### List Key-Value Secret Keys

List secret keys available in the HashiCorp Vault based on provided criteria. The action returns key names stored in a secret path without values. Folder names should be specified for the secret path. The action doesn't work if the secret key is provided.

#### Entities

This action doesn't run on entities.

#### Action inputs

To configure the integration, use the following parameters:

Parameters  
---  
`Key-Value Secret Engine Path` | _Optional_ Path used for the key-value secret storage. Only version 2 is supported. This parameter is used to interact with secrets stored in a storage and construct URLs such as `https://IP_ADDRESS:8200/v1/secret/data/SECRET_TO_FETCH_FROM_THE_KV_STORE`. Default value is `secret`.  
`Secret Path` | _Optional_ Secret path to fetch. The action accepts folder names. Example: if the secret path folder name is `my-secret`, the key-value store path is `secret`, then the full path to fetch is `https://IP_ADDRESS:8200/v1/secret/data/my-secret`. If no value is provided, the action returns all secret keys stored in the secret engine. Default value is `https://IP_ADDRESS:8200.`  
`Max Records To Return` | _Optional_ Number of records to return.Default value is 50.  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | Available  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
     "request_id": "ed5d30ed-0fe9-a3b5-36d1-cc81b9175fe9",
     "lease_id": "",
     "renewable": false,
     "lease_duration": 0,
     "data": {
       "keys": [
         "hello",
         "tesr2",
         "test"
       ]
     },
     "wrap_info": null,
     "warnings": null,
     "auth": null
    }
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found the following secret keys for the provided criteria in the key-value store KEY-VALUE_SECRET_ENGINE_PATH.` | Action succeeded.  
`Error executing action "List Key-Value Secret Keys". Reason: Invalid value was provided for "Max Records to Return": PROVIDED_VALUE. Positive number should be provided.` | Action failed.Check the `Max Records to Return` parameter value.  
`Error executing action "List Key-Value Secret Keys". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
### Ping

Test connectivity to the HashiCorp Vault installation with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Entities

This action doesn't run on entities.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | N/A  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result

N/A

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the HashiCorp Vault installation with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the HashiCorp Vault installation! Error is ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
### Read Key-Value Secret

Read the key-value secret stored in HashiCorp Vault based on provided criteria.

#### Entities

This action doesn't run on entities.

#### Action inputs

To configure the integration, use the following parameters:

Parameters  
---  
`Key-Value Secret Engine Path` | _Optional_ Path used for the key-value secret storage. Only version 2 is supported. This parameter is used to interact with secrets stored in a storage and construct URLs such as `https://IP_ADDRESS:8200/v1/secret/data/SECRET_TO_FETCH_FROM_THE_KV_STORE`. Default value is `secret`.  
`Secret Path` | **Required** Secret path to fetch. The action accepts folder names. Example: if the secret path folder name is `my-secret`, the key-value store path is `secret`, then the full path to fetch is `https://IP_ADDRESS:8200/v1/secret/data/my-secret`. If no value is provided, the action returns all secret keys stored in the secret engine. Default value is `https://IP_ADDRESS:8200.`  
`Secret Version` | _Optional_ Secret version to fetch.  
`JSON Expression Builder` | _Optional_ JSON expression to filter a specific subset of data from a secret. Example is as follows: `| "data" | "data" | "key0"`.  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
Entity insight | N/A  
Insight | N/A  
JSON result | Available  
OOTB widget | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
     "request_id": "8b020faf-808f-34c2-5348-c04871ee6594",
     "lease_id": "",
     "renewable": false,
     "lease_duration": 0,
     "data": {
       "data": {
         "key0": "value0"
       },
       "metadata": {
         "created_time": "2023-04-11T10:56:34.766417394Z",
         "custom_metadata": null,
         "deletion_time": "",
         "destroyed": false,
         "version": 1
       }
     },
     "wrap_info": null,
     "warnings": null,
     "auth": null
    }
    

##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched secret SECRET_PATH.` | Action succeeded.  
`Error executing action "Read Key-Value Secret". Reason: Incorrect JSON value is provided for the Expression Builder.` | Action failed.Check the `JSON Expression Builder` parameter value.  
`Error executing action "Read Key-Value Secret". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
