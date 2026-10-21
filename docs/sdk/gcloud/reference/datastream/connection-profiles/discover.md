---
url: https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover/
title: gcloud datastream connection-profiles discover \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:48:26.177400+00:00
---

# gcloud datastream connection-profiles discover  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud datastream connection-profiles discover Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud datastream connection-profiles discover - discover a Datastream connection profile 
SYNOPSIS
    

`gcloud datastream connection-profiles discover` `--location`=`LOCATION` (`--connection-profile-name`=`CONNECTION_PROFILE_NAME` | `--connection-profile-object-file`=`CONNECTION_PROFILE_OBJECT_FILE`) [`--endpoint-mode`=`ENDPOINT_MODE`] [`--full-hierarchy` | `--hierarchy-depth`=`HIERARCHY_DEPTH`] [`--mysql-rdbms-file`=`MYSQL_RDBMS_FILE` | `--oracle-rdbms-file`=`ORACLE_RDBMS_FILE` | `--postgresql-rdbms-file`=`POSTGRESQL_RDBMS_FILE` | `--sqlserver-rdbms-file`=`SQLSERVER_RDBMS_FILE`] [`--recursive` | `--recursive-depth`=`RECURSIVE_DEPTH`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Discover data objects accessible from a Datastream connection profile 
EXAMPLES
     To discover an existing connection profile: 
    
    
    gcloud datastream connection-profiles discover CONNECTION_PROFILE --location=us-central1 --connection-profile-name=some-cp --recursive=true

To discover a non-existing connection profile: 
    
    
    gcloud datastream connection-profiles discover CONNECTION_PROFILE --location=us-central1 --connection-profile-object-file=path/to/yaml/or/json/file

REQUIRED FLAGS
    

Location resource - The location you want to list the connection profiles for. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


Exactly one of these must be specified: 

Connection profile resource - Resource ID of the connection profile. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--connection-profile-name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--connection-profile-name` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



`--connection-profile-name`=`CONNECTION_PROFILE_NAME`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

* provide the argument `--connection-profile-name` on the command line. 
`--connection-profile-object-file`=`CONNECTION_PROFILE_OBJECT_FILE`
     Path to a YAML (or JSON) file containing the configuration for a connection profile object. If you pass - as the value of the flag the file content will be read from stdin. 
OPTIONAL FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
At most one of these can be specified: 

`--full-hierarchy`
     Whether to retrieve the full hierarchy of data objects (TRUE) or only the current level (FALSE). 
`--hierarchy-depth`=`HIERARCHY_DEPTH`
     The number of hierarchy levels below the current level to be retrieved. 
At most one of these can be specified: 

`--mysql-rdbms-file`=`MYSQL_RDBMS_FILE`
     Path to a YAML (or JSON) file containing the MySQL RDBMS to enrich with child data objects and metadata. If you pass - as the value of the flag the file content will be read from stdin. 
`--oracle-rdbms-file`=`ORACLE_RDBMS_FILE`
     Path to a YAML (or JSON) file containing the Oracle RDBMS to enrich with child data objects and metadata. If you pass - as the value of the flag the file content will be read from stdin. 
`--postgresql-rdbms-file`=`POSTGRESQL_RDBMS_FILE`
     Path to a YAML (or JSON) file containing the PostgreSQL RDBMS to enrich with child data objects and metadata. If you pass - as the value of the flag the file content will be read from stdin. 
`--sqlserver-rdbms-file`=`SQLSERVER_RDBMS_FILE`
     Path to a YAML (or JSON) file containing the SQL Server RDBMS to enrich with child data objects and metadata. If you pass - as the value of the flag the file content will be read from stdin. 
At most one of these can be specified: 

`--recursive`
     (DEPRECATED) Whether to retrieve the full hierarchy of data objects (TRUE) or only the current level (FALSE). 

The --recursive option is deprecated; use `--full-hierarchy` instead. 

`--recursive-depth`=`RECURSIVE_DEPTH`
     (DEPRECATED) The number of hierarchy levels below the current level to be retrieved. 

The --recursive-depth option is deprecated; use `--hierarchy-depth` instead. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This variant is also available: 
    
    
    [gcloud beta datastream connection-profiles discover](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/connection-profiles/discover)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
