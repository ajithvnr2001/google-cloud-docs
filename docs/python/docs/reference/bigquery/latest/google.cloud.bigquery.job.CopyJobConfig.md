---
url: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJobConfig
title: Class CopyJobConfig (3.46.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:56.489235+00:00
---

# Class CopyJobConfig (3.46.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CopyJobConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CopyJobConfig (3.46.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.46.1 (latest)  3.46.0  3.45.2  3.44.0  3.43.0  3.42.3  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.31.0  3.30.0  3.29.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.1  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.2  3.16.0  3.15.0  3.14.1  3.13.0  3.12.0  3.11.4  3.4.0  3.3.6  3.2.0  3.1.0  3.0.1  2.34.4  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.27.1  2.26.0  2.25.2  2.24.1  2.23.3  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.0  1.28.2  1.27.2  1.26.1  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0 
    
    
    CopyJobConfig(**kwargs)

Configuration options for copy jobs.

All properties in this class are optional. Values which are :data:`None` -> server defaults. Set properties on the constructed configuration by using the property name as the name of a keyword argument.

## Properties 

### create_disposition

[google.cloud.bigquery.job.CreateDisposition](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.CreateDisposition): Specifies behavior for creating tables.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationTableCopy.FIELDS.create_disposition>

### destination_encryption_configuration

[google.cloud.bigquery.encryption_configuration.EncryptionConfiguration](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.encryption_configuration.EncryptionConfiguration): Custom encryption configuration for the destination table.

Custom encryption configuration (e.g., Cloud KMS keys) or :data:`None` if using default encryption.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationTableCopy.FIELDS.destination_encryption_configuration>

### destination_expiration_time

google.cloud.bigquery.job.DestinationExpirationTime: The time when the destination table expires. Expired tables will be deleted and their storage reclaimed.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationTableCopy.FIELDS.destination_expiration_time>

### job_timeout_ms

Optional parameter. Job timeout in milliseconds. If this time limit is exceeded, BigQuery might attempt to stop the job. <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfiguration.FIELDS.job_timeout_ms> e.g.
    
    
    job_config = bigquery.QueryJobConfig( job_timeout_ms = 5000 )
    or
    job_config.job_timeout_ms = 5000
    

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `value` type is invalid.  
  
### labels

Dict[str, str]: Labels for the job.

This method always returns a dict. Once a job has been created on the server, its labels cannot be modified anymore.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `value` type is invalid.  
  
### max_slots

The maximum rate of slot consumption to allow for this job.

If set, the number of slots used to execute the job will be throttled to try and keep its slot consumption below the requested rate. This feature is not generally available.

### operation_type

The operation to perform with this copy job.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationTableCopy.FIELDS.operation_type>

### reservation

str: Optional. The reservation that job would use.

User can specify a reservation to execute the job. If reservation is not set, reservation is determined based on the rules defined by the reservation assignments. The expected format is projects/{project}/locations/{location}/reservations/{reservation}.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `value` type is not None or of string type.  
  
### write_disposition

[google.cloud.bigquery.job.WriteDisposition](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.job.WriteDisposition): Action that occurs if the destination table already exists.

See <https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationTableCopy.FIELDS.write_disposition>

## Methods 

### __setattr__
    
    
    __setattr__(name, value)

Override to be able to raise error if an unknown property is being set

### from_api_repr
    
    
    from_api_repr(resource: dict) -> google.cloud.bigquery.job.base._JobConfig

Factory: construct a job configuration given its API representation

**Parameter**  
---  
**Name** | **Description**  
`resource` |  `Dict`   
A job configuration in the same representation as is returned from the API.  
**Returns**  
---  
**Type** | **Description**  
`google.cloud.bigquery.job._JobConfig` | Configuration parsed from `resource`.  
  
### to_api_repr
    
    
    to_api_repr() -> dict

Build an API representation of the job config.

**Returns**  
---  
**Type** | **Description**  
`Dict` | A dictionary in the format used by the BigQuery API.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
