---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/streams/create/
title: gcloud beta datastream streams create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:23:16.942598+00:00
---

# gcloud beta datastream streams create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/streams/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta datastream streams create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta datastream streams create - creates a Datastream stream 
SYNOPSIS
    

`gcloud beta datastream streams create` (`STREAM` : `--location`=`LOCATION`) `--display-name`=`DISPLAY_NAME` (`--backfill-none` | `--backfill-all` `--mongodb-excluded-objects`=`MONGODB_EXCLUDED_OBJECTS` | `--mysql-excluded-objects`=`MYSQL_EXCLUDED_OBJECTS` | `--oracle-excluded-objects`=`ORACLE_EXCLUDED_OBJECTS` | `--postgresql-excluded-objects`=`POSTGRESQL_EXCLUDED_OBJECTS` | `--saas-excluded-objects`=`SAAS_EXCLUDED_OBJECTS` | `--salesforce-excluded-objects`=`SALESFORCE_EXCLUDED_OBJECTS` | `--spanner-excluded-objects`=`SPANNER_EXCLUDED_OBJECTS` | `--sqlserver-excluded-objects`=`SQLSERVER_EXCLUDED_OBJECTS`) (`--destination-name`=`DESTINATION_NAME` (`--bigquery-destination-config`=`BIGQUERY_DESTINATION_CONFIG` | `--gcs-destination-config`=`GCS_DESTINATION_CONFIG`)) (`--source-name`=`SOURCE_NAME` (`--dataverse-source-config`=`DATAVERSE_SOURCE_CONFIG` | `--mongodb-source-config`=`MONGODB_SOURCE_CONFIG` | `--mysql-source-config`=`MYSQL_SOURCE_CONFIG` | `--oracle-source-config`=`ORACLE_SOURCE_CONFIG` | `--postgresql-source-config`=`POSTGRESQL_SOURCE_CONFIG` | `--salesforce-marketing-cloud-source-config`=`SALESFORCE_MARKETING_CLOUD_SOURCE_CONFIG` | `--salesforce-source-config`=`SALESFORCE_SOURCE_CONFIG` | `--servicenow-source-config`=`SERVICENOW_SOURCE_CONFIG` | `--spanner-source-config`=`SPANNER_SOURCE_CONFIG` | `--sqlserver-source-config`=`SQLSERVER_SOURCE_CONFIG`)) [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--rule-sets`=`RULE_SETS`] [`--force` | `--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` Datastream beta version is deprecated. Please use`[gcloud datastream streams create](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/create)` command instead. 

Create a Datastream stream. If successful, the response body contains a newly created instance of Operation. To get the operation result, call: describe OPERATION 

`
EXAMPLES
     To create a stream with an Oracle source and a Google Cloud Storage destination: 
    
    
    gcloud beta datastream streams create STREAM --location=us-central1 --display-name=my-stream --source-name=source --oracle-source-config=source_config.json --destination-name=destination --gcs-destination-config=destination_config.json --backfill-none

To create a stream with a MySQL source and a Cloud Storage destination and that excludes some objects from being backfilled: 
    
    
    gcloud beta datastream streams create STREAM --location=us-central1 --display-name=my-stream --source-name=source --mysql-source-config=source_config.json --destination-name=destination --gcs-destination-config=destination_config.json --backfill-all --mysql-excluded-objects=excluded_objects.json

POSITIONAL ARGUMENTS
    

Stream resource - The stream to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `stream` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`STREAM`
     ID of the stream or fully qualified identifier for the stream. 

To set the `stream` attribute: 

  * provide the argument `stream` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the stream. 

To set the `location` attribute: 

  * provide the argument `stream` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Friendly name for the stream. 
Exactly one of these must be specified: 

`--backfill-none`
     Do not automatically backfill any objects. This flag is equivalent to selecting the Manual backfill type in the Google Cloud console. 
Or at least one of these can be specified: 

`--backfill-all`
     Automatically backfill objects included in the stream source configuration. Specific objects can be excluded. This flag is equivalent to selecting the Automatic backfill type in the Google Cloud console. 
At most one of these can be specified: 

`--mongodb-excluded-objects`=`MONGODB_EXCLUDED_OBJECTS`
     Path to a YAML (or JSON) file containing the MongoDB data sources to avoid backfilling. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "databases": [
          {
            "database":"sample_database",
            "collections": [
              {
                "collection": "sample_collection",
                "fields": [
                  {
                    "field": "sample_field",
                  }
                ]
              }
            ]
          }
        ]
      }

`--mysql-excluded-objects`=`MYSQL_EXCLUDED_OBJECTS`
     Path to a YAML (or JSON) file containing the MySQL data sources to avoid backfilling. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "mysqlDatabases": [
          {
            "database":"sample_database",
            "mysqlTables": [
              {
                "table": "sample_table",
                "mysqlColumns": [
                  {
                    "column": "sample_column",
                  }
                  ]
              }
            ]
          }
        ]
      }

`--oracle-excluded-objects`=`ORACLE_EXCLUDED_OBJECTS`
     Path to a YAML (or JSON) file containing the Oracle data sources to avoid backfilling. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "oracleSchemas": [
          {
            "schema": "SAMPLE",
            "oracleTables": [
              {
                "table": "SAMPLE_TABLE",
                "oracleColumns": [
                  {
                    "column": "COL",
                  }
                ]
              }
            ]
          }
        ]
      }

`--postgresql-excluded-objects`=`POSTGRESQL_EXCLUDED_OBJECTS`
     Path to a YAML (or JSON) file containing the PostgreSQL data sources to avoid backfilling. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "postgresqlSchemas": [
          {
            "schema": "SAMPLE",
            "postgresqlTables": [
              {
                "table": "SAMPLE_TABLE",
                "postgresqlColumns": [
                  {
                    "column": "COL",
                  }
                ]
              }
            ]
          }
        ]
      }

`--saas-excluded-objects`=`SAAS_EXCLUDED_OBJECTS`
     Path to a YAML (or JSON) file containing the SaaS data sources to avoid backfilling. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "objects": [
          {
            "objectName": "Account",
          }
        ]
      }

`--salesforce-excluded-objects`=`SALESFORCE_EXCLUDED_OBJECTS`
     Path to a YAML (or JSON) file containing the Salesforce data sources to avoid backfilling. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "objects": [
          {
            "objectName": "SAMPLE",
          },
          {
            "objectName": "SAMPLE2",
          }
        ]
      }

`--spanner-excluded-objects`=`SPANNER_EXCLUDED_OBJECTS`
     Path to a YAML (or JSON) file containing the Spanner data sources to avoid backfilling. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "schemas": [
          {
            "schema": "SAMPLE_SCHEMA",
            "tables": [
              {
                "table": "SAMPLE_TABLE",
                "columns": [
                  {
                    "column": "SAMPLE_COLUMN",
                  }
                ]
              }
            ]
          }
        ]
      }

`--sqlserver-excluded-objects`=`SQLSERVER_EXCLUDED_OBJECTS`
     Path to a YAML (or JSON) file containing the SQL Server data sources to avoid backfilling. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "schemas": [
          {
            "schema": "SAMPLE",
            "tables": [
              {
                "table": "SAMPLE_TABLE",
                "columns": [
                  {
                    "column": "COL",
                  }
                ]
              }
            ]
          }
        ]
      }

This must be specified. 

Connection profile resource - Resource ID of the destination connection profile. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--destination-name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--destination-name` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--destination-name`=`DESTINATION_NAME`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `--destination-name` on the command line. 


Exactly one of these must be specified: 

`--bigquery-destination-config`=`BIGQUERY_DESTINATION_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for Google BigQuery Destination Config. 

The YAML (or JSON) file should be formatted as follows: 

BigQuery configuration with source hierarchy datasets and merge mode (merge mode is by default): 
    
    
    {
      "sourceHierarchyDatasets": {
        "datasetTemplate": {
          "location": "us-central1",
          "datasetIdPrefix": "my_prefix",
          "kmsKeyName": "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{cryptoKey}"
        }
      },
      "merge": {}
      "dataFreshness": "3600s"
    }

BigQuery configuration with source hierarchy datasets and append only mode:
    
    
    {
      "sourceHierarchyDatasets": {
        "datasetTemplate": {
          "location": "us-central1",
          "datasetIdPrefix": "my_prefix",
          "kmsKeyName": "projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{cryptoKey}"
        }
      },
      "appendOnly": {}
    }

BigQuery configuration with single target dataset and merge mode: 
    
    
    {
      "singleTargetDataset": {
        "datasetId": "projectId:my_dataset"
      },
      "merge": {}
      "dataFreshness": "3600s"
    }

BigQuery configuration with Big Lake table configuration:
    
    
    {
      "singleTargetDataset": {
        "datasetId": "projectId:datasetId"
      },
      "appendOnly": {},
      "blmtConfig": {
        "bucket": "bucketName",
        "tableFormat": "ICEBERG",
        "fileFormat": "PARQUET",
        "connectionName": "projectId.region.connectionName",
        "rootPath": "/root"
      }
    }

`--gcs-destination-config`=`GCS_DESTINATION_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for Google Cloud Storage Destination Config. 

The JSON file is formatted as follows: 
    
    
     {
     "path": "some/path",
     "fileRotationMb":5,
     "fileRotationInterval":"15s",
     "avroFileFormat": {}
     }

This must be specified. 

Connection profile resource - Resource ID of the source connection profile. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source-name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--source-name` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--source-name`=`SOURCE_NAME`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `--source-name` on the command line. 


Exactly one of these must be specified: 

`--dataverse-source-config`=`DATAVERSE_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for Dataverse Source Config. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "pollingInterval": "300s",
        "includeObjects": {},
        "excludeObjects": {
          "objects": [
            {
              "objectName": "Account",
              "properties": [
                {
                  "propertyName": "name",
                }
              ]
            }
          ]
        }
      }

`--mongodb-source-config`=`MONGODB_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for MongoDB Source Config. 

The JSON file is formatted as follows, with snake_case field naming: 
    
    
      {
        "includeObjects": {},
        "excludeObjects": {
          "databases": [
            {
              "database": "sampleDb",
              "collections": [
                {
                  "collection": "sampleCollection",
                  "fields": [
                    {
                      "field": "SAMPLE_FIELD",
                    }
                  ]
                }
              ]
            }
          ]
        }
      }

`--mysql-source-config`=`MYSQL_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for MySQL Source Config. 

The JSON file is formatted as follows, with snake_case field naming: 
    
    
      {
        "allowlist": {},
        "rejectlist":  {
          "mysql_databases": [
              {
                "database_name":"sample_database",
                "mysql_tables": [
                  {
                    "table_name": "sample_table",
                    "mysql_columns": [
                      {
                        "column_name": "sample_column",
                      }
                     ]
                  }
                ]
              }
            ]
          }
      }

`--oracle-source-config`=`ORACLE_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for Oracle Source Config. 

The JSON file is formatted as follows, with snake_case field naming: 
    
    
      {
        "allowlist": {},
        "rejectlist": {
          "oracle_schemas": [
            {
              "schema_name": "SAMPLE",
              "oracle_tables": [
                {
                  "table_name": "SAMPLE_TABLE",
                  "oracle_columns": [
                    {
                      "column_name": "COL",
                    }
                  ]
                }
              ]
            }
          ]
        }
      }

`--postgresql-source-config`=`POSTGRESQL_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for PostgreSQL Source Config. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "includeObjects": {},
        "excludeObjects": {
          "postgresqlSchemas": [
            {
              "schema": "SAMPLE",
              "postgresqlTables": [
                {
                  "table": "SAMPLE_TABLE",
                  "postgresqlColumns": [
                    {
                      "column": "COL",
                    }
                  ]
                }
              ]
            }
          ]
        },
        "replicationSlot": "SAMPLE_REPLICATION_SLOT",
        "publication": "SAMPLE_PUBLICATION"
      }

`--salesforce-marketing-cloud-source-config`=`SALESFORCE_MARKETING_CLOUD_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for Salesforce Marketing Cloud Source Config. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "pollingInterval": "300s",
        "fullRefreshPollingInterval": "86400s",
        "includeObjects": {},
        "excludeObjects": {
          "objects": [
            {
              "objectName": "Subscriber",
              "properties": [
                {
                  "propertyName": "EmailAddress",
                }
              ]
            }
          ]
        }
      }

`--salesforce-source-config`=`SALESFORCE_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for Salesforce Source Config. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "pollingInterval": "3000s",
        "includeObjects": {},
        "excludeObjects": {
          "objects": [
            {
              "objectName": "SAMPLE",
              "fields": [
                {
                  "fieldName": "SAMPLE_FIELD",
                }
              ]
            }
          ]
        }
      }

`--servicenow-source-config`=`SERVICENOW_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for ServiceNow Source Config. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "pollingInterval": "300s",
        "includeObjects": {},
        "excludeObjects": {
          "objects": [
            {
              "objectName": "incident",
              "properties": [
                {
                  "propertyName": "short_description",
                }
              ]
            }
          ]
        }
      }

`--spanner-source-config`=`SPANNER_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for Spanner Source Config. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      "changeStreamName": "SAMPLE_CHANGE_STREAM_NAME",
      {
        "includeObjects": {},
        "excludeObjects": {
          "schemas": [
            {
              "schema": "SAMPLE",
              "tables": [
                {
                  "table": "SAMPLE_TABLE",
                  "columns": [
                    {
                      "column": "COL",
                    }
                  ]
                }
              ]
            }
          ]
        },
        "maxConcurrentCdcTasks": 1000,
        "maxConcurrentBackfillTasks": 10,
        "backfillDataBoostEnabled": false,
        "fgacRole": "SAMPLE_FGAC_ROLE",
        "spannerRpcPriority": "MEDIUM"
      }

`--sqlserver-source-config`=`SQLSERVER_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for SQL Server Source Config. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "includeObjects": {},
        "excludeObjects": {
          "schemas": [
            {
              "schema": "SAMPLE",
              "tables": [
                {
                  "table": "SAMPLE_TABLE",
                  "columns": [
                    {
                      "column": "COL",
                    }
                  ]
                }
              ]
            }
          ]
        },
        "maxConcurrentCdcTasks": 2,
        "maxConcurrentBackfillTasks": 10,
        "transactionLogs": {}  # Or changeTables
      }

OPTIONAL FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--rule-sets`=`RULE_SETS`
     Path to a JSON file containing a list of rule sets to be applied to the stream. 
    
    
    The JSON file is formatted as follows, with camelCase field naming:
    
    
    [
      {
        "objectFilter": {
          "sourceObjectIdentifier": {
            "oracleIdentifier": {
              "schema": "schema1",
              "table": "table1"
            }
          }
        },
        "customizationRules": [
          {
            "bigqueryClustering": {
              "columns": ["COL_A"]
            }
          }
        ]
      },
      {
        "objectFilter": {
          "sourceObjectIdentifier": {
            "oracleIdentifier": {
              "schema": "schema2",
              "table": "table2"
            }
          }
        },
        "customizationRules": [
          {
            "bigqueryPartitioning": {
              "timeUnitPartition": {
                "column": "TIME_COL",
                "partitioningTimeGranularity": "PARTITIONING_TIME_GRANULARITY_DAY"
              }
            }
          }
        ]
      }
    ]

At most one of these can be specified: 

`--force`
     Create the stream without validating it. 
`--validate-only`
     Only validate the stream, but do not create any resources. The default is false. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud datastream streams create](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
