---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create-secondary/
title: gcloud alloydb instances create-secondary \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:31.552183+00:00
---

# gcloud alloydb instances create-secondary  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/create-secondary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alloydb instances create-secondary Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alloydb instances create-secondary - creates a new AlloyDB SECONDARY instance within a given cluster 
SYNOPSIS
    

`gcloud alloydb instances create-secondary` `INSTANCE` `--cluster`=`CLUSTER` `--region`=`REGION` [`--allocated-ip-range-override`=`ALLOCATED_IP_RANGE_OVERRIDE`] [`--allowed-psc-projects`=[`ALLOWED_PSC_PROJECTS`,…]] [`--assign-inbound-public-ip`=`ASSIGN_INBOUND_PUBLIC_IP`] [`--async`] [`--authorized-external-networks`=[`AUTHORIZED_NETWORK`,…]] [`--availability-type`=`AVAILABILITY_TYPE`] [`--connection-pooling-client-connection-idle-timeout`=`CONNECTION_POOLING_CLIENT_CONNECTION_IDLE_TIMEOUT`] [`--connection-pooling-ignore-startup-parameters`=[`STARTUP_PARAMETERS`,…]] [`--connection-pooling-max-client-connections`=`CONNECTION_POOLING_MAX_CLIENT_CONNECTIONS`] [`--connection-pooling-max-pool-size`=`CONNECTION_POOLING_MAX_POOL_SIZE`] [`--connection-pooling-max-prepared-statements`=`CONNECTION_POOLING_MAX_PREPARED_STATEMENTS`] [`--connection-pooling-min-pool-size`=`CONNECTION_POOLING_MIN_POOL_SIZE`] [`--connection-pooling-pool-mode`=`CONNECTION_POOLING_POOL_MODE`] [`--connection-pooling-query-wait-timeout`=`CONNECTION_POOLING_QUERY_WAIT_TIMEOUT`] [`--connection-pooling-server-idle-timeout`=`CONNECTION_POOLING_SERVER_IDLE_TIMEOUT`] [`--connection-pooling-server-lifetime`=`CONNECTION_POOLING_SERVER_LIFETIME`] [`--connection-pooling-stats-users`=[`STATS_USERS`,…]] [`--database-flags`=`FLAG`=`VALUE`,[`FLAG`=`VALUE`,…]] [`--[no-]enable-connection-pooling`] [`--labels`=[`KEY`=`VALUE`,…]] [`--[no-]outbound-public-ip`] [`--psc-auto-connections`=[`network`=`NETWORK`],[`project`=`PROJECT`]] [`--psc-network-attachment-uri`=`PSC_NETWORK_ATTACHMENT_URI`] [`--[no-]require-connectors`] [`--ssl-mode`=`SSL_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a new AlloyDB SECONDARY instance within a given cluster. 
EXAMPLES
     To create a new secondary instance, run: 
    
    
    gcloud alloydb instances create-secondary my-instance --cluster=my-cluster --region=us-central1

POSITIONAL ARGUMENTS
    

`INSTANCE`
     AlloyDB instance ID 
REQUIRED FLAGS
    

`--cluster`=`CLUSTER`
     AlloyDB cluster ID 
`--region`=`REGION`
     Regional location (e.g. `asia-east1`, `us-east1`). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
OPTIONAL FLAGS
    

`--allocated-ip-range-override`=`ALLOCATED_IP_RANGE_OVERRIDE`
     Name of the allocated IP range for the private IP AlloyDB instance, for example: "google-managed-services-default". If set, the instance IPs will be created from this allocated range and will override the IP range used by the parent cluster. The range name must comply with RFC 1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. 
`--allowed-psc-projects`=[`ALLOWED_PSC_PROJECTS`,…]
     Comma-separated list of allowed consumer projects to create endpoints for Private Service Connect (PSC) connectivity for the instance. Only instances in PSC-enabled clusters are allowed to set this field.(e.g., `--allowed-psc-projects=project1,12345678,project2) `
`--assign-inbound-public-ip`=`ASSIGN_INBOUND_PUBLIC_IP`
     Specify to enable or disable public IP on an instance. ASSIGN_INBOUND_PUBLIC_IP must be one of: 

  * `NO_PUBLIC_IP`
    * This disables public IP on the instance. Updating an instance to disable public IP will clear the list of authorized networks. 
  * `ASSIGN_IPV4`
    * Assign an inbound public IPv4 address for the instance. Public IP is enabled. 


`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--authorized-external-networks`=[`AUTHORIZED_NETWORK`,…]
     Comma-separated list of authorized external networks to set on the instance. Authorized networks should use CIDR notation (e.g. 1.2.3.4/30). This flag is only allowed to be set for instances with public IP enabled. 
`--availability-type`=`AVAILABILITY_TYPE`
     Specifies level of availability. `AVAILABILITY_TYPE` must be one of: 

`REGIONAL`
     Provide high availability instances. Recommended for production instances; instances automatically fail over to another zone within your selected region. 
`ZONAL`
     Provide zonal availability instances. Not recommended for production instances; instance does not automatically fail over to another zone. 
`--connection-pooling-client-connection-idle-timeout`=`CONNECTION_POOLING_CLIENT_CONNECTION_IDLE_TIMEOUT`
     The maximum number of seconds a client is allowed to be idle before it is disconnected. 
`--connection-pooling-ignore-startup-parameters`=[`STARTUP_PARAMETERS`,…]
     Comma-separated list of startup parameters that should be ignored by the connection pool. 
`--connection-pooling-max-client-connections`=`CONNECTION_POOLING_MAX_CLIENT_CONNECTIONS`
     The max client connections for managed connection pooling. 
`--connection-pooling-max-pool-size`=`CONNECTION_POOLING_MAX_POOL_SIZE`
     The max pool size for managed connection pooling. 
`--connection-pooling-max-prepared-statements`=`CONNECTION_POOLING_MAX_PREPARED_STATEMENTS`
     The maximum number of prepared statements allowed. 
`--connection-pooling-min-pool-size`=`CONNECTION_POOLING_MIN_POOL_SIZE`
     The min pool size for managed connection pooling. 
`--connection-pooling-pool-mode`=`CONNECTION_POOLING_POOL_MODE`
     The pool mode for managed connection pooling. `CONNECTION_POOLING_POOL_MODE` must be one of: 

`SESSION`
     Session mode for managed connection pooling. 
`TRANSACTION`
     Transaction mode for managed connection pooling. 
`--connection-pooling-query-wait-timeout`=`CONNECTION_POOLING_QUERY_WAIT_TIMEOUT`
     The query wait timeout for managed connection pooling. 
`--connection-pooling-server-idle-timeout`=`CONNECTION_POOLING_SERVER_IDLE_TIMEOUT`
     The server idle timeout for managed connection pooling. 
`--connection-pooling-server-lifetime`=`CONNECTION_POOLING_SERVER_LIFETIME`
     The lifetime of a server connection in seconds. The pooler will close an unused (not currently linked to any client connection) server connection that has been connected longer than this. Setting it to 0 means the connection is to be used only once, then closed. 
`--connection-pooling-stats-users`=[`STATS_USERS`,…]
     Comma-separated list of database users to access connection pooling stats. 
`--database-flags`=`FLAG`=`VALUE`,[`FLAG`=`VALUE`,…]
     Comma-separated list of database flags to set on the instance. Use an equals sign to separate flag name and value. Flags without values, like skip_grant_tables, can be written out without a value after, e.g., skip_grant_tables=`. Use on/off for booleans. View the Instance Resource API for allowed flags. (e.g., `\--database-flags max_allowed_packet=55555,skip_grant_tables=,log_output=1`) `
`--[no-]enable-connection-pooling`
     Enable connection pooling for the instance. Use `--enable-connection-pooling` to enable and `--no-enable-connection-pooling` to disable. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. `

`--[no-]outbound-public-ip`
     Add outbound Public IP connectivity to an AlloyDB instance. Use `--outbound-public-ip` to enable and `--no-outbound-public-ip` to disable. 
`--psc-auto-connections`=[`network`=`NETWORK`],[`project`=`PROJECT`]
     Comma-separated list of consumer project and consumer network pairs to create endpoints for Private Service Connect (PSC) connectivity for the instance. Only instances in PSC-enabled clusters are allowed to set this field. Both project and network must be specified. (e.g., \--psc-auto-connections=project=project1,network=projects/vpc-host-project1/global/networks/network1` `\--psc-auto-connections=project=project2,network=projects/vpc-host-project2/global/networks/network2`). Sets `psc_auto_connections` value. 

`network`
     Required, sets 
`network` value. `
`project`
     Required, sets project` value. `
`Shorthand Example:`
    
    
    --psc-auto-connections=network=string,project=string

`JSON Example:`
    
    
    --psc-auto-connections='{"network": "string", "project": "string"}'

`File Example:`
    
    
    --psc-auto-connections=path_to_file.(yaml|json)

`--psc-network-attachment-uri`=`PSC_NETWORK_ATTACHMENT_URI`
     Full URI of the network attachment that is configured to support outbound connectivity from an AlloyDB instance which uses Private Service Connect (PSC). For example, this would be of the form:psc-network-attachment-uri=projects/test-project/regions/us-central1/networkAttachments/my-na` `
`--[no-]require-connectors`
     Enable or disable enforcing connectors only (ex: AuthProxy) connections to the database. Use `--require-connectors` to enable and `--no-require-connectors` to disable. 
`--ssl-mode`=`SSL_MODE`
     Specify the SSL mode to use when the instance connects to the database. Default SSL mode will match what is set on the primary instance. `SSL_MODE` must be one of: 

`ALLOW_UNENCRYPTED_AND_ENCRYPTED`
     SSL connections are optional. CA verification is not enforced. 
`ENCRYPTED_ONLY`
     SSL connections are required. CA verification is not enforced. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha alloydb instances create-secondary](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/create-secondary)
    
    
    [gcloud beta alloydb instances create-secondary](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/instances/create-secondary)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
