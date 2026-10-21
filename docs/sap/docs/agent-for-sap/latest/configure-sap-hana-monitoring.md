---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-sap-hana-monitoring/
title: Configure SAP HANA Monitoring metrics collection \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:50.721769+00:00
---

# Configure SAP HANA Monitoring metrics collection  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-sap-hana-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure SAP HANA Monitoring metrics collection Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure Google Cloud's Agent for SAP to collect the SAP HANA monitoring metrics from your SAP HANA systems.

For information about this feature, see [Monitoring SAP HANA using Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana).

**Note:** The collection of SAP HANA monitoring metrics is supported only on Linux. It is not supported on Windows.

## Before you begin

  * Validate your installation of Google Cloud's Agent for SAP. For instructions, see the [installation guide for your scenario](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config).
  * If you have installed the agent on a Bare Metal Solution server, then make sure that you have completed the required prerequisites and set up a service account. For instructions, see [Configure Google Cloud's Agent for SAP on Linux](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms#configure_agent4sap).



### Required IAM roles

To ensure that the service account has the necessary permissions to let Google Cloud's Agent for SAP collect SAP HANA monitoring metrics, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Collect the SAP HANA monitoring metrics from the Compute Engine instance that hosts your SAP system: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * Write the collected metrics to Cloud Monitoring: [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) 
  * If you are using Secret Manager to store the password to connect to the SAP HANA database: [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to let Google Cloud's Agent for SAP collect SAP HANA monitoring metrics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to let Google Cloud's Agent for SAP collect SAP HANA monitoring metrics:

  * Collect the SAP HANA monitoring metrics from the host Compute Engine instance and write them to Cloud Monitoring: 
    * `monitoring.timeSeries.create`
    * `compute.nodeGroups.get`
    * `compute.nodeGroups.list`
  * If you are using Secret Manager to store the password to connect to the SAP HANA database, then to access the secret: `secretmanager.versions.access`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required SAP HANA roles

To let the agent collect metrics from your SAP HANA database, make sure that the SAP HANA user that you specify in the agent's configuration file has the `MONITORING` role.

For information about this role, see the SAP document [Standard Database Roles](https://help.sap.com/docs/SAP_HANA_ONE/102d9916bf77407ea3942fef93a47da8/de421861bb571014846288086be76719.html).

## Enable SAP HANA Monitoring metrics collection

To enable the collection of SAP HANA Monitoring metrics using Google Cloud's Agent for SAP, follow these steps:

  1. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.

  2. Open the agent's configuration file:
         
         /etc/google-cloud-sap-agent/configuration.json

Alternatively, you can also perform this configuration by running commands. For more information, see [Configuration commands for Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/config-commands).

  3. In the `hana_monitoring_configuration` section, perform the following:

     * For the parameter `enabled`, set the value `true`.
     * In the `hana_instances` section, specify the SAP HANA instances that you want the agent to monitor.
     * Optionally, define custom queries. For information about defining custom queries and see examples, see [Defining custom queries](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#defining_custom_queries).
     * Optionally, disable the built-in or default queries. For instructions, see Disable a SQL query.

For information about the configuration parameters, see Configuration parameters.

  4. Optionally, under the `cloud_properties` section, you can update the parameter values that are set automatically. To do so, add the `cloud_properties` section to your configuration file, and then specify the required parameters and their values.

  5. Save the configuration file.

  6. Restart the agent for the new settings to take effect:

**Note:** From version 3.7, you need not restart the agent because any changes to the agent's configuration are automatically applied within the next 30 seconds.
         
         sudo systemctl restart google-cloud-sap-agent




### Example configuration files

### Compute Engine instance

The following examples are completed configuration files of Google Cloud's Agent for SAP running on a Compute Engine instance, where the collection of SAP HANA monitoring metrics is enabled. Note that the custom query included in these examples, named `custom_query`, follows the custom query definition guidelines specified in [Defining custom queries](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#defining_custom_queries).

The following example uses a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication:
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": false,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
        "collect_process_metrics": false
      },
      "discovery_configuration": {
        "enable_discovery": true,
        "enable_workload_discovery": true
      },
      "hana_monitoring_configuration": {
        "enabled": true,
        "sample_interval_sec": 60,
        "query_timeout_sec": 30,
        "execution_threads": 20,
        "hana_instances": [
          {
            "name": "local",
            "sid": "DEH",
            "user": "system",
            "hdbuserstore_key": "user_store_key"
          },
          {
            "name": "remote",
            "sid": "DEH",
            "user": "system",
            "hdbuserstore_key": "user_store_key"
          }
        ],
        "queries": [
          {
            "name": "custom_query",
            "enabled": true,
            "sql": "SELECT * FROM MyTable;",
            "columns": [
              {
                "name": "string",
                "metric_type": "METRIC_LABEL",
                "value_type": "VALUE_STRING"
              },
              {
                "name": "bool",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_BOOL"
              },
              {
                "name": "int",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_INT64"
              },
              {
                "name": "double",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_DOUBLE"
              }
            ]
          },
          {
            "name": "default_host_queries",
            "enabled": false
          }
        ]
      }
    }

The following example uses a username and Secret Manager secret for SAP HANA authentication:
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": false,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
        "collect_process_metrics": false
      },
      "discovery_configuration": {
        "enable_discovery": true,
        "enable_workload_discovery": true
      },
      "hana_monitoring_configuration": {
        "enabled": true,
        "sample_interval_sec": 60,
        "query_timeout_sec": 30,
        "execution_threads": 20,
        "hana_instances": [
          {
            "name": "local",
            "sid": "DEH",
            "host": "localhost",
            "port": "30015",
            "user": "system",
            "secret_name": "password-secret-name"
          },
          {
            "name": "remote",
            "sid": "DEH",
            "host": "10.123.0.12",
            "port": "30015",
            "user": "system",
            "secret_name": "password-secret-name"
          }
        ],
        "queries": [
          {
            "name": "custom_query",
            "enabled": true,
            "sql": "SELECT * FROM MyTable;",
            "columns": [
              {
                "name": "string",
                "metric_type": "METRIC_LABEL",
                "value_type": "VALUE_STRING"
              },
              {
                "name": "bool",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_BOOL"
              },
              {
                "name": "int",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_INT64"
              },
              {
                "name": "double",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_DOUBLE"
              }
            ]
          },
          {
            "name": "default_host_queries",
            "enabled": false
          }
        ]
      }
    }

The following example uses a username and password for SAP HANA authentication. We recommend that you instead use a Secret Manager secret or [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication.
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": false,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
        "collect_process_metrics": false
      },
      "discovery_configuration": {
        "enable_discovery": true,
        "enable_workload_discovery": true
      },
      "hana_monitoring_configuration": {
        "enabled": true,
        "sample_interval_sec": 60,
        "query_timeout_sec": 30,
        "execution_threads": 20,
        "hana_instances": [
          {
            "name": "local",
            "sid": "DEH",
            "host": "localhost",
            "port": "30015",
            "user": "system",
            "password": "TempPa55word"
          },
          {
            "name": "remote",
            "sid": "DEH",
            "host": "10.123.0.12",
            "port": "30015",
            "user": "system",
            "password": "TempPa55word"
          }
        ],
        "queries": [
          {
            "name": "custom_query",
            "enabled": true,
            "sql": "SELECT * FROM MyTable;",
            "columns": [
              {
                "name": "string",
                "metric_type": "METRIC_LABEL",
                "value_type": "VALUE_STRING"
              },
              {
                "name": "bool",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_BOOL"
              },
              {
                "name": "int",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_INT64"
              },
              {
                "name": "double",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_DOUBLE"
              }
            ]
          },
          {
            "name": "default_host_queries",
            "enabled": false
          }
        ]
      }
    }

### Bare Metal Solution server

The following examples are completed configuration files of Google Cloud's Agent for SAP running on a Bare Metal Solution server, where the collection of SAP HANA monitoring metrics is enabled. Note that the custom query included in these examples, named `custom_query`, follows the custom query definition guidelines specified in [Defining custom queries](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#defining_custom_queries).

The following example uses a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication:
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": true,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
        "collect_process_metrics": false
      },
      "cloud_properties": {
        "project_id": "my-project",
        "instance_name": "bms-machine-1",
        "region": "us-central1",
        "image": "rhel-8"
      },  
      "discovery_configuration": {
        "enable_discovery": true,
        "enable_workload_discovery": true
      },
      "hana_monitoring_configuration": {
        "enabled": true,
        "sample_interval_sec": 60,
        "query_timeout_sec": 30,
        "execution_threads": 20,
        "hana_instances": [
          {
            "name": "local",
            "sid": "DEH",
            "user": "system",
            "hdbuserstore_key": "user_store_key"
          },
          {
            "name": "remote",
            "sid": "DEH",
            "user": "system",
            "hdbuserstore_key": "user_store_key"
          }
        ],
        "queries": [
          {
            "name": "custom_query",
            "enabled": true,
            "sql": "SELECT * FROM MyTable;",
            "columns": [
              {
                "name": "string",
                "metric_type": "METRIC_LABEL",
                "value_type": "VALUE_STRING"
              },
              {
                "name": "bool",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_BOOL"
              },
              {
                "name": "int",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_INT64"
              },
              {
                "name": "double",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_DOUBLE"
              }
            ]
          },
          {
            "name": "default_host_queries",
            "enabled": false
          }
        ]
      }
    }

The following example uses a username and Secret Manager secret for SAP HANA authentication:
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": true,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
        "collect_process_metrics": false
      },
      "cloud_properties": {
        "project_id": "my-project",
        "instance_name": "bms-machine-1",
        "region": "us-central1",
        "image": "rhel-8"
      },  
      "discovery_configuration": {
        "enable_discovery": true,
        "enable_workload_discovery": true
      },
      "hana_monitoring_configuration": {
        "enabled": true,
        "sample_interval_sec": 60,
        "query_timeout_sec": 30,
        "execution_threads": 20,
        "hana_instances": [
          {
            "name": "local",
            "sid": "DEH",
            "host": "localhost",
            "port": "30015",
            "user": "system",
            "secret_name": "password-secret-name"
          },
          {
            "name": "remote",
            "sid": "DEH",
            "host": "10.123.0.12",
            "port": "30015",
            "user": "system",
            "secret_name": "password-secret-name"
          }
        ],
        "queries": [
          {
            "name": "custom_query",
            "enabled": true,
            "sql": "SELECT * FROM MyTable;",
            "columns": [
              {
                "name": "string",
                "metric_type": "METRIC_LABEL",
                "value_type": "VALUE_STRING"
              },
              {
                "name": "bool",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_BOOL"
              },
              {
                "name": "int",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_INT64"
              },
              {
                "name": "double",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_DOUBLE"
              }
            ]
          },
          {
            "name": "default_host_queries",
            "enabled": false
          }
        ]
      }
    }

The following example uses a username and password for SAP HANA authentication. We recommend that you instead use a Secret Manager secret or [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication.
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": true,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
        "collect_process_metrics": false
      },
      "cloud_properties": {
        "project_id": "my-project",
        "instance_name": "bms-machine-1",
        "region": "us-central1",
        "image": "rhel-8"
      },  
      "discovery_configuration": {
        "enable_discovery": true,
        "enable_workload_discovery": true
      },
      "hana_monitoring_configuration": {
        "enabled": true,
        "sample_interval_sec": 60,
        "query_timeout_sec": 30,
        "execution_threads": 20,
        "hana_instances": [
          {
            "name": "local",
            "sid": "DEH",
            "host": "localhost",
            "port": "30015",
            "user": "system",
            "password": "TempPa55word"
          },
          {
            "name": "remote",
            "sid": "DEH",
            "host": "10.123.0.12",
            "port": "30015",
            "user": "system",
            "password": "TempPa55word"
          }
        ],
        "queries": [
          {
            "name": "custom_query",
            "enabled": true,
            "sql": "SELECT * FROM MyTable;",
            "columns": [
              {
                "name": "string",
                "metric_type": "METRIC_LABEL",
                "value_type": "VALUE_STRING"
              },
              {
                "name": "bool",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_BOOL"
              },
              {
                "name": "int",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_INT64"
              },
              {
                "name": "double",
                "metric_type": "METRIC_GAUGE",
                "value_type": "VALUE_DOUBLE"
              }
            ]
          },
          {
            "name": "default_host_queries",
            "enabled": false
          }
        ]
      }
    }

### Define a custom SQL query

Google Cloud's Agent for SAP collects the SAP HANA monitoring metrics by running SQL queries on your SAP HANA instances. In addition to these default queries, you can define and run custom SQL queries by completing the following steps:

  1. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.

  2. Open the agent's configuration file:
         
         /etc/google-cloud-sap-agent/configuration.json

  3. Under the `hana_monitoring_configuration.queries` section, define your custom query.

For information about defining custom queries and see examples, see [Defining custom queries](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#defining_custom_queries).

  4. To enable a custom query, set its `enabled` parameter to `true`.

  5. If you're using version 3.7 of the agent, then for SAP HANA HA systems deployed with the [Active/Active (Read Enabled)](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/fe5fc53706a34048bf4a3a93a5d7c866.html) configuration, you can specify if the query is to be run on the primary, secondary, or both nodes of your HA system:

     * To run a query on the primary node, include `"run_on": "PRIMARY"`.
     * To run a query on the primary node, include `"run_on": "SECONDARY"`.
     * To run a query on the primary node, include `"run_on": "ALL"`.

For more information, see Set up node-specific monitoring for an SAP HANA HA system.

  6. Save the configuration file.

  7. Restart the agent for the new settings to take effect:

**Note:** From version 3.7, you need not restart the agent because any changes to the agent's configuration are automatically applied within the next 30 seconds.
         
         sudo systemctl restart google-cloud-sap-agent




### Disable a SQL query

If you don't want to run any of the built-in SQL queries that Google Cloud's Agent for SAP provides by default, or any of the custom queries that you define, then you can disable the SQL query by completing the following steps:

  1. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.

  2. Open the agent's configuration file:
         
         /etc/google-cloud-sap-agent/configuration.json

  3. To disable a built-in or default query, include the following under the `hana_monitoring_configuration.queries` section:
         
         {
         "name": "default_QUERY_NAME",
         "enabled": false
         }

Replace `QUERY_NAME` with the name of the default query. For information about the default queries, see [Default query reference](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#default_query_reference).

  4. To disable a custom query, set the `enabled` parameter to `false` for that custom query.

  5. Save the configuration file.

  6. Restart the agent for the new settings to take effect:

**Note:** From version 3.7, you need not restart the agent because any changes to the agent's configuration are automatically applied within the next 30 seconds.
         
         sudo systemctl restart google-cloud-sap-agent




### Set up tenant-specific monitoring for a multi-tenant SAP HANA database

From version 3.7 of Google Cloud's Agent for SAP, you can set up tenant-specific monitoring for multi-tenant SAP HANA databases. To do this, complete the following steps:

  1. Make sure that you're using version 3.7 or later of Google Cloud's Agent for SAP.
  2. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.
  3. Open the agent's configuration file:
         
         /etc/google-cloud-sap-agent/configuration.json

  4. In the `hana_monitoring_configuring.hana_instances` section, for each SAP HANA that you've defined, apply the appropriate configuration:

     * To run a specific set of queries on an SAP HANA instance, include the `queries_to_run.query_name` parameter as follows.
     * To run all queries on an SAP HANA instance, include `queries_to_run.run_all` parameter as follows.

The following snippet shows examples of these options:
    
    "hana_monitoring_configuration": {
       "enabled": true,
       ...
       "hana_instances": [
         {
           "name": "TENANT_DB_1_NAME",
           "sid": "SID",
           ...
           "queries_to_run": {
             **"query_name": [" QUERY_NAME_1", "QUERY_NAME_2", ...]**
           }
         },
         {
           "name": "TENANT_DB_2_NAME",
           "sid": "SID",
           ...
           "queries_to_run": {
             **"run_all": true**
           }
         }
         ...
       ]
     }

  5. Save the configuration file.

  6. Within the next 30 seconds, the new configuration takes effect. Alternatively, you can manually [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).




### Set up node-specific monitoring for an SAP HANA HA system

From version 3.7 of Google Cloud's Agent for SAP, for SAP HANA HA systems deployed with the [Active/Active (Read Enabled)](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/fe5fc53706a34048bf4a3a93a5d7c866.html) configuration, you can specify if the queries defined in your agent's configuration file are to be run on the primary node, the secondary node, or both. To do this, complete the following steps:

  1. Make sure that you're using version 3.7 or later of Google Cloud's Agent for SAP.
  2. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.
  3. Open the agent's configuration file:
         
         /etc/google-cloud-sap-agent/configuration.json

  4. In the `hana_monitoring_configuring.queries` section, for each query that you've defined, apply the appropriate configuration:

     * To run a query on the primary node, include `"run_on": "PRIMARY"`.
     * To run a query on the primary node, include `"run_on": "SECONDARY"`.
     * To run a query on the primary node, include `"run_on": "ALL"`.
  5. In the `hana_monitoring_configuration.hana_instances` section, for each SAP HANA instance that you've defined, specify the `instance_num` and `is_local` parameters.

The following snippet shows examples of all scenarios:
         
         "hana_monitoring_configuration": {
            "enabled": true,
            ...
            "hana_instances": [
              {
                 "name": "INSTANCE_NAME",
                 "sid": "SID",
                 **"instance_num": "10",
                 "is_local": true** ,
                 "hdbuserstore_key": "USER_STORE_KEY"
              },
              {
                 "name": "INSTANCE_NAME",
                 "sid": "SID",
                 **"instance_num": "11"
                 "is_local": true** ,
                 "hdbuserstore_key": "USER_STORE_KEY"
              },
              ...
            ],
            ...
            "queries": [
              {
                 "name": "QUERY_NAME_1",
                 "enabled": true,
                 **"run_on": "PRIMARY"** ,
                 ...
              },
              {
                 "name": "QUERY_NAME_2",
                 "enabled": true,
                 **"run_on": "SECONDARY"** ,
                 ...
              },
              {
                 "name": "QUERY_NAME_3",
                 "enabled": true,
                 **"run_on": "ALL"** ,
                 ...
              }
              ...
            ]
          }

  6. Save the configuration file.

  7. Within the next 30 seconds, the new configuration takes effect. Alternatively, you can manually [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).




### Configuration parameters

The following table explains the configuration parameters of Google Cloud's Agent for SAP that are specific to the collection of the SAP HANA Monitoring metrics.

Parameters  
---  
`provide_sap_host_agent_metrics` |  `Boolean` To enable the collection of the metrics required by the SAP Host Agent, specify `true`. Default is `true`.   
Don't set `provide_sap_host_agent_metrics` to `false` unless you are directed by Cloud Customer Care or SAP Support.   
`bare_metal` |  `Boolean` When the agent is installed on a Bare Metal Solution server, specify `true`. Default is `false`.  
`log_level` |  `String` To set the logging level of the agent, set the required value. The available log levels are as follows:

  * `DEBUG`
  * `INFO`
  * `WARNING`
  * `ERROR`

Default is `INFO`. Don't change the logging level unless you are directed by Cloud Customer Care.  
`log_to_cloud` |  `Boolean` To redirect the agent's logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), specify `true`. The default is `true`.  
`cloud_properties.project_id` | `String` If your SAP system is running on a Bare Metal Solution server, then specify the project ID of the Google Cloud project that you are using with Bare Metal Solution.  
  
When the agent runs on a Compute Engine instance, by default, the agent detects the project ID automatically.  
`cloud_properties.instance_name` |  `String` If your SAP system is running on a Compute Engine instance, then specify the name that compute instance. The agent automatically detects the compute instance name upon installation. If your SAP system is running on a Bare Metal Solution server, then specify the name of that server.  
`cloud_properties.region` | `String` If your SAP system is running on a Bare Metal Solution server, then specify the region where you've deployed the Bare Metal Solution server.  
  
When the agent runs on a compute instance, by default, the agent uses the region where the compute instance is deployed. | `cloud_properties.zone` | `String` When the agent runs on a compute instance, by default, the agent uses the zone where the compute instance is deployed.  
`cloud_properties.image` | `String` Specify the OS image name of the instance.  
  
When the agent runs on a compute instance, by default, the agent automatically detects the OS image used by the compute instance.  
`cloud_properties.numeric_project_id` | `String` Specify the numeric ID of the Google Cloud project where the SAP system is running.  
  
When the agent runs on a compute instance, by default, the agent automatically detects project number.  
`discovery_configuration.enable_workload_discovery` |  `Boolean` To let the agent collect the names and versions of the SAP products running on the host, specify `true`. The default value is `true`. For more information, see the agent's codebase in the `google-cloud-sap-agent` GitHub repository under [GoogleCloudPlatform/sapagent](https://github.com/GoogleCloudPlatform/sapagent).   
`discovery_configuration.enable_discovery` |  `Boolean` To send to Cloud Logging the information that the agent collects about the SAP products running on the host, specify `true`. The default value is `true`. If you specify the value `false`, then the agent stores the collected information on the host and doesn't send it to Cloud Logging.   
`hana_monitoring_configuration.enabled` |  `Boolean` Optional. To enable Google Cloud's Agent for SAP to collect the SAP HANA monitoring metrics, specify `true`. The default value is `false`. The following child parameters are applicable only when you specify `hana_monitoring_configuration.enabled: true`.   
`hana_monitoring_configuration.sample_interval_sec` |  `Int` Optional. Specify the sample interval, in seconds, which determines the frequency at which Google Cloud's Agent for SAP queries your SAP HANA instances to collect the SAP HANA monitoring metrics. The default value is 300 seconds. For each query defined in the configuration file of Google Cloud's Agent for SAP, you can overwrite the global sample interval by specifying the required interval to the parameter `sample_interval_sec`. Sample intervals must be 5 seconds or longer.  
`hana_monitoring_configuration.query_timeout_sec` |  `Int` Optional. Specify the timeout for each query made to the SAP HANA instances. The default value is 300 seconds.  
`hana_monitoring_configuration.execution_threads` |  `Int` Optional. Specify the number of threads used to send queries to the SAP HANA instances. Each query runs on its own thread. The default value is 10.  
`hana_monitoring_configuration.send_query_response_time` |  `Boolean` Optional. Specify `true` to have the agent capture the response time for every SAP HANA monitoring query defined in the agent's configuration file.  
`hana_monitoring_configuration.hana_instances.name` |  `String` Specify the name identifier for your SAP HANA instance.  
`hana_monitoring_configuration.hana_instances.sid` |  `String` Specify the SID of your SAP HANA instance. This string is added as a label to all the metrics resulting from querying your SAP HANA instances.  
`hana_monitoring_configuration.hana_instances.host` |  `String` Specify the identifier for the machine, either local or remote, that hosts your SAP HANA instance. The following are the supported values:

  * If the host is a local machine, then specify the string `localhost` or the localhost loopback IP address, like `127.0.0.1`.
  * If the host is a remote machine, then specify its internal or external IP address.

  
`hana_monitoring_configuration.hana_instances.port` |  `String` Specify the port on which your SAP HANA instance accepts queries. For the first or only tenant database instance, the port is `3NN15`, where `NN` is the instance number of the SAP HANA instance.  
`hana_monitoring_configuration.hana_instances.user` |  `String` Specify the user account that is used to query the SAP HANA instance. Make sure that this user has the privilege to read the monitoring views in your SAP HANA database. If this privilege is not granted, then the SAP HANA monitoring metrics related to the monitoring views contain no data.  
`hana_monitoring_configuration.hana_instances.password` |  `String` Optional. Specify the password, as plain text, that authenticates the user account for querying the SAP HANA instance. For authentication, you must specify one of the following:

  * The plain text password to the parameter `password`.
  * (Recommended) If you use [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the password as a secret, then you must specify the corresponding secret name to the parameter `secret_name`.
  * (Recommended) An [`hdbuserstore` key](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) to the parameter `hdbuserstore_key`.

For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `password` parameter, which is preferred over the `secret_name` parameter. We recommend that you set only one authentication option in your configuration file.  
`hana_monitoring_configuration.hana_instances.secret_name` |  `String` Optional. Specify the name of the secret in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) that stores the user account's password. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `hdbuserstore_key` configuration parameter is preferred over the `password` parameter, which is preferred over the `secret_name` parameter. We recommend that you set only one authentication option in your configuration file.  
`hana_monitoring_configuration.hana_instances.hdbuserstore_key` |  `String` To securely connect to an SAP HANA system, specify a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key that you've created for that system.  To use an `hdbuserstore` key for authentication, ensure the following:

  * The SAP tools `hdbsql` and `hdbuserstore` are installed on the compute instance hosting the agent.
  * The `hdbuserstore` key corresponds to one specific SAP HANA instance. You can't use keys that contain hostnames of multiple SAP HANA instances.
  * The `SIDadm` user can query the SAP HANA database using this key. Here `SID` refers to the value that you've specified for the `sid` parameter. You can verify this by running the following command as the `SIDadm` user: 
        
        hdbsql -U HDB_USERSTORE_KEY "SELECT * FROM DUMMY"


This configuration parameter is supported from version 3.3 of the agent. If you specify `hdbuserstore_key`, then you can skip specifying the `host` and `port` parameters.  
`hana_monitoring_configuration.hana_instances.is_local` |  `Boolean` For monitoring HA systems, specify `true` to tell the agent that the defined SAP HANA instance is hosted on the same Compute Engine instance as the agent. This then makes the agent check at runtime if the defined SAP HANA instance is the primary or the secondary node in that HA system. This awareness is required by the agent to run the SAP HANA monitoring queries on the SAP HANA instance type that you specify for the `queries.run_on` parameter. The default value for this parameter is `false`, which makes the agent run all the enabled SAP HANA monitoring queries on the corresponding SAP HANA instance. For more information, see [Monitoring for multi-tenant and HA systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#monitoring_for_multi-tenant_and_ha_systems). This parameter is supported from version 3.7 of the agent.  
`hana_monitoring_configuration.hana_instances.instance_num` |  `String` Specify the instance number that you've set for your SAP HANA instance. This information is required for the agent to discover your SAP HANA instance. This parameter is supported from version 3.7 of the agent.  
`hana_monitoring_configuration.hana_instances.queries_to_run.run_all` |  `Boolean` Optional. Specify `true` to run all the SAP HANA monitoring queries, default and custom, that are enabled in the agent's configuration file on the specified SAP HANA instance. The default value is `false`.  
`hana_monitoring_configuration.hana_instances.queries_to_run.query_name` |  `String` Optional. Specify the queries that you want to run on the specified SAP HANA instance. If you're running a multi-tenant SAP HANA database, then you can set up tenant specific monitoring by using this configuration parameter. In the following example configuration, two queries are run on `HANA_TENANT_1` and all queries defined in the configuration are run on `HANA_TENANT_2`:
    
    
        "hana_instances": [
          {
            "name": "HANA_TENANT_1,
            "queries_to_run": {
              "query_name": ["QUERY_NAME_1", "QUERY_NAME_2"]
            }
          },
          {
            "name": "HANA_TENANT_2,
            "queries_to_run": {
              "run_all": true
            }
          }
          ...
        ]  
  
`hana_monitoring_configuration.hana_instances.enable_ssl` |  `Boolean` Optional. Specifies whether or not SSL is enabled in your SAP HANA instance. The default value is `false`.  
`hana_monitoring_configuration.hana_instances.host_name_in_certificate` |  `String` If you specify `enable_ssl: true` for an SAP HANA instance, then you must specify the hostname that is set in the SSL certificate.  
`hana_monitoring_configuration.hana_instances.tls_root_ca_file` |  `String` If you specify `enable_ssl: true` for an SAP HANA instance, then you must specify the path for your security certificate.  
`hana_monitoring_configuration.queries.enabled` |  `Boolean` Optional. To enable a SQL query for all your SAP HANA instances, specify the value `true` for the parameter `enabled` for that SQL query.  
`hana_monitoring_configuration.queries.name` |  `String` If you have defined custom queries in your configuration file, then you must specify a unique name for each custom query. The query name must be unique because it is used to build the metric's default URL in Monitoring.  
`hana_monitoring_configuration.queries.run_on` |  `String` Optional. Specify this parameter if you're monitoring an SAP HANA HA system and want to run the SAP HANA monitoring queries on either the primary or the secondary node. Supported values: `PRIMARY`, `SECONDARY`, `ALL`. When you specify the value `ALL`, the agent runs the SAP HANA monitoring queries on both the primary and secondary nodes in your HA cluster. This parameter is supported from version 3.7 of the agent. Also, to run the queries on the secondary node, make sure that your HA system is deployed with the [Active/Active (Read Enabled)](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/fe5fc53706a34048bf4a3a93a5d7c866.html) configuration.   
`hana_monitoring_configuration.queries.sql` |  `String` Specify the SQL statement that the agent issues to your SAP HANA instances. The SQL statement must conform to the SQL syntax defined by SAP in [SAP HANA SQL and System Views Reference](https://help.sap.com/viewer/4fe29514fd584807ac9f2a04f6754767/2.0.02).   
`hana_monitoring_configuration.queries.sample_interval_sec` |  `Int` Optional. Specify the sample interval for the SQL query. This overrides the global sample interval. The value must be 5 seconds or longer.  
`hana_monitoring_configuration.queries.columns.name` |  `String` Specify a name that uniquely identifies each column. The column name must be unique because it is used to build the metric's default URL in Monitoring.  
`hana_monitoring_configuration.queries.columns.metric_type` |  `String` For handling by Monitoring, specify one of the following metric types: `METRIC_LABEL`, `METRIC_GAUGE`, or `METRIC_CUMULATIVE`. Metrics of type `METRIC_LABEL` are appended as labels to all the `METRIC_GAUGE` and `METRIC_CUMULATIVE` metrics that are sent to Monitoring.  
`hana_monitoring_configuration.queries.columns.value_type` |  `String` For handling by Monitoring, specify a data type that is supported by the metric type. The supported data types are as follows: `VALUE_BOOL`, `VALUE_INT64`, `VALUE_STRING`, or `VALUE_DOUBLE`. For more information, see [Supported combination](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types#kind-type-combos).  
`hana_monitoring_configuration.queries.columns.name_override` |  `String` Optional. For handling by Monitoring, specify the path that you want to show in the metric URL instead of the query and column names. For example:

  * Metric's default URL: `workload.googleapis.com/sap/hanamonitoring/QUERY_NAME/COLUMN_NAME`
  * Metric URL using custom path: `workload.googleapis.com/sap/hanamonitoring/CUSTOM_PATH`

  
  
## Validate the setup for SAP HANA monitoring metrics collection

You can validate if you have the correct Google Cloud setup for the collection of the SAP HANA Monitoring metrics by running the agent's `status` command. This command is supported from version 3.7 of the agent.

To do this, complete the following steps:

  1. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.
  2. Run the following command:
         
         sudo /usr/bin/google_cloud_sap_agent status -f="hana_monitoring"
         

If your Google Cloud setup for SAP HANA Monitoring metrics collection is correct, then the output includes the following. Your configuration might have values other than the **`default`** ones.
         
         Agent Status:
             ...
             Systemd Service Enabled: True
             Systemd Service Running: True
             Cloud API Full Scopes: True
             Configuration File: /etc/google-cloud-sap-agent/configuration.json
             Configuration Valid: True
         ...
         ----------------------------------------------------------------------------
         HANA Monitoring Metrics: Enabled
             Status: Fully Functional
             IAM Permissions: All granted
             Configuration:
                 connection_timeout:       120   (default)
                 enabled:                  true  (configuration file)
                 execution_threads:        10    (default)
                 max_connect_retries:      1     (default)
                 query_timeout_sec:        300   (default)
                 sample_interval_sec:      300   (default)
                 send_query_response_time: false (default)
         ...
         

  3. If your output conveys that some setup is missing, then review the information provided in the preceding sections, perform the required actions, and then re-run the `status` command to re-validate the setup.




## View the collected metrics

To visualize the [SAP HANA Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana) that the agent collects, you can use the following custom dashboards that Google Cloud provides:

  * **Agent for SAP - Detailed HANA Overview** : This dashboard provides charts that display status overview for the following metrics: Instance memory, service memory used, schema estimated maximum memory, rowstore memory total size, schema read outliers, schema write outliers, schema last compressed record count outliers, system connections, alerts, CPU percentage for the top 5 compute instances, memory percentage for the top 5 compute instances, and the hosts by region.

The JSON file for this dashboard is `agent-for-sap-hana-detailed-overview.json`.

  * **Agent for SAP - HANA performance** : This dashboard provides charts that display raw metric values for the following metrics: Instance memory, schema read and write outliers, schema performance, memory usage, schema record count outliers, service total memory used, rowstore memory size, system idle and running connections, connection and rowstore memory, schema total records, and the schema estimated maximum total size.

The JSON file for this dashboard is `agent-for-sap-hana-performance.json`.




### Install dashboards

To install a custom dashboard, complete the following steps:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Monitoring** page:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the Monitoring navigation panel, click **Dashboards**.

  3. Click the **Sample library** tab.

![Display of the sample library tab selected.](https://docs.cloud.google.com/static/sap/docs/images/dashboard-select-sample-library.png)

  4. To filter the agent-specific custom dashboards, in the **Filter** field, type `Agent for SAP`.

  5. (Optional) To view details about a dashboard or to preview its contents, click **Preview**.

  6. Select the dashboard that you want to install.

  7. Click **Import** , and then click **Confirm**.

The dashboard is added to the available dashboards in your Google Cloud project. To see your dashboard, follow the instructions in View the installed dashboard.




###  Google Cloud CLI 

  1. Open the Cloud Shell:

[Open Cloud Shell](https://console.cloud.google.com/monitoring?cloudshell=true)

  2. In the Cloud Shell, clone or download the repository:
         
         git clone https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/

  3. In the Cloud Shell, install the required dashboard using the corresponding JSON file:
         
         gcloud monitoring dashboards create --config-from-file=CONFIG_FROM_FILE

Replace `CONFIG_FROM_FILE` with the path to the JSON file that contains the dashboard configuration. Dashboard configuration files can be located at path: `monitoring-dashboard-samples/dashboards/google-cloud-agent-for-sap`.

The dashboard is added to the available dashboards in your Google Cloud project. To see your dashboard, follow the instructions in View the installed dashboard.




### View the installed dashboards

To view the installed dashboards, follow these steps:

  1. In the Google Cloud console, go to the **Monitoring** page:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the Monitoring navigation panel, click **Dashboards**.

  3. Click the dashboard name in the list.




If you have a lot of dashboards, then you can filter for custom dashboards or for the name of the new dashboard. For information on filtering this list, see [View custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#view-dashboard).

The following image is an example that shows a part of the custom dashboard for SAP HANA metrics in Monitoring.

![Screen capture shows the custom dashboard for SAP HANA metrics
in Monitoring](https://docs.cloud.google.com/static/sap/docs/images/agent-for-sap-hana-detailed-overview.01.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
