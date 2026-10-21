---
url: https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update/
title: gcloud datastream streams update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:28:03.100329+00:00
---

# gcloud datastream streams update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/datastream/streams/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud datastream streams update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud datastream streams update - updates a Datastream stream 
SYNOPSIS
    

`gcloud datastream streams update` (`STREAM` : `--location`=`LOCATION`) [`--display-name`=`DISPLAY_NAME`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--rule-sets`=`RULE_SETS`] [`--state`=`STATE`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--update-mask`=`UPDATE_MASK`] [`--backfill-none` | `--backfill-all` `--mongodb-excluded-objects`=`MONGODB_EXCLUDED_OBJECTS` | `--mysql-excluded-objects`=`MYSQL_EXCLUDED_OBJECTS` | `--oracle-excluded-objects`=`ORACLE_EXCLUDED_OBJECTS` | `--postgresql-excluded-objects`=`POSTGRESQL_EXCLUDED_OBJECTS` | `--saas-excluded-objects`=`SAAS_EXCLUDED_OBJECTS` | `--salesforce-excluded-objects`=`SALESFORCE_EXCLUDED_OBJECTS` | `--spanner-excluded-objects`=`SPANNER_EXCLUDED_OBJECTS` | `--sqlserver-excluded-objects`=`SQLSERVER_EXCLUDED_OBJECTS`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--destination`=`DESTINATION` `--bigquery-destination-config`=`BIGQUERY_DESTINATION_CONFIG` | `--gcs-destination-config`=`GCS_DESTINATION_CONFIG`] [`--force` | `--validate-only`] [`--source`=`SOURCE` `--dataverse-source-config`=`DATAVERSE_SOURCE_CONFIG` | `--mongodb-source-config`=`MONGODB_SOURCE_CONFIG` | `--mysql-source-config`=`MYSQL_SOURCE_CONFIG` | `--oracle-source-config`=`ORACLE_SOURCE_CONFIG` | `--postgresql-source-config`=`POSTGRESQL_SOURCE_CONFIG` | `--salesforce-marketing-cloud-source-config`=`SALESFORCE_MARKETING_CLOUD_SOURCE_CONFIG` | `--salesforce-source-config`=`SALESFORCE_SOURCE_CONFIG` | `--servicenow-source-config`=`SERVICENOW_SOURCE_CONFIG` | `--spanner-source-config`=`SPANNER_SOURCE_CONFIG` | `--sqlserver-source-config`=`SQLSERVER_SOURCE_CONFIG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Datastream stream. If successful, the response body contains a newly created instance of Operation. To get the operation result, call: describe OPERATION 
EXAMPLES
     To update a stream with a new source and new display name: 
    
    
    gcloud datastream streams update STREAM --location=us-central1 --display-name=my-stream --source=source --update-mask=display_name,source

To update a stream's state to RUNNING: 
    
    
    gcloud datastream streams update STREAM --location=us-central1 --state=RUNNING --update-mask=state

To update a stream's oracle source config: 
    
    
    gcloud datastream streams update STREAM --location=us-central1 --oracle-source-config=good_oracle_cp.json --update-mask=oracle_source_config.include_objects

POSITIONAL ARGUMENTS
    

Stream resource - The stream to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Friendly name for the stream. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
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

`--state`=`STATE`
     Stream state, can be set to: "RUNNING" or "PAUSED". 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--update-mask`=`UPDATE_MASK`
     Used to specify the fields to be overwritten in the stream resource by the update. If the update mask is used, then a field will be overwritten only if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This is a comma-separated list of fully qualified names of fields, written as snake_case or camelCase. Example: "display_name, source_config.oracle_source_config". 
At most one of these can be specified: 

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

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud datastream streams update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud datastream streams update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
Connection profile resource - Resource ID of the destination connection profile. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--destination` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--destination` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--destination`=`DESTINATION`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `--destination` on the command line. 


At most one of these can be specified: 

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

At most one of these can be specified: 

`--force`
     Update the stream without validating it. 
`--validate-only`
     Only validate the stream, but do not update any resources. The default is false. 
Connection profile resource - Resource ID of the source connection profile. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--source` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--source`=`SOURCE`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `--source` on the command line. 


At most one of these can be specified: 

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

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "includeObjects": {},
        "excludeObjects":  {
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
      }

`--oracle-source-config`=`ORACLE_SOURCE_CONFIG`
     Path to a YAML (or JSON) file containing the configuration for Oracle Source Config. 

The JSON file is formatted as follows, with camelCase field naming: 
    
    
      {
        "includeObjects": {},
        "excludeObjects": {
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

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This variant is also available: 
    
    
    [gcloud beta datastream streams update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/streams/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
