---
url: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql/
title: gcloud database-migration connection-profiles create postgresql \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:47.999338+00:00
---

# gcloud database-migration connection-profiles create postgresql  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud database-migration connection-profiles create postgresql Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud database-migration connection-profiles create postgresql - create a Database Migration Service connection profile for PostgreSQL 
SYNOPSIS
    

`gcloud database-migration connection-profiles create postgresql` (`CONNECTION_PROFILE` : `--region`=`REGION`) [`--no-async`] [`--display-name`=`DISPLAY_NAME`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--role`=`ROLE`] [`--ssl-flags`=[`FLAG`=`VALUE`,…]] [`--alloydb-cluster`=`ALLOYDB_CLUSTER` `--cloudsql-instance`=`CLOUDSQL_INSTANCE` `--database`=`DATABASE` `--host`=`HOST` `--port`=`PORT` `--enable-iam-authentication` | `--username`=`USERNAME` (`--password`=`PASSWORD` | `--prompt-for-password`)] [`--ca-certificate`=`CA_CERTIFICATE` `--ssl-type`=`SSL_TYPE` `--client-certificate`=`CLIENT_CERTIFICATE` `--private-key`=`PRIVATE_KEY`] [`--private-connection`=`PRIVATE_CONNECTION` | `--psc-service-attachment`=`PSC_SERVICE_ATTACHMENT` | `--static-ip-connectivity` | [`--forward-ssh-hostname`=`FORWARD_SSH_HOSTNAME` `--forward-ssh-username`=`FORWARD_SSH_USERNAME` (`--forward-ssh-password`=`FORWARD_SSH_PASSWORD` | `--forward-ssh-private-key`=`FORWARD_SSH_PRIVATE_KEY`) : `--forward-ssh-port`=`FORWARD_SSH_PORT`; default=22]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Database Migration Service connection profile for PostgreSQL. 
EXAMPLES
     To create a connection profile my-profile for PostgreSQL: 
    
    
    gcloud database-migration connection-profiles create postgresql my-profile --region=us-central1 --password=123456 --username=my-user --host=1.2.3.4 --port=5432

If the source is a Cloud SQL database, run: 
    
    
    gcloud database-migration connection-profiles create postgresql my-profile --region=us-central1 --password=123456 --username=my-user --host=1.2.3.4 --port=5432 --cloudsql-instance=my-instance

POSITIONAL ARGUMENTS
    

Connection profile resource - The connection profile to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `connection_profile` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CONNECTION_PROFILE`
     ID of the connection_profile or fully qualified identifier for the connection_profile. 

To set the `connection_profile` attribute: 

  * provide the argument `connection_profile` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The Cloud region for the connection_profile. 

To set the `region` attribute: 

  * provide the argument `connection_profile` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


FLAGS
    

`--no-async`
     Waits for the operation in progress to complete before returning. 
`--display-name`=`DISPLAY_NAME`
     A user-friendly name for the connection profile. The display name can include letters, numbers, spaces, and hyphens, and must start with a letter. 
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

`--role`=`ROLE`
     The role of the connection profile. `ROLE` must be one of: `SOURCE`, `DESTINATION`. 
`--ssl-flags`=[`FLAG`=`VALUE`,…]
     List of SSL flags used for establishing SSL connection to the database. Use an equals sign to separate the flag name and value. By default, flags are separated by commas. Example: `--ssl-flags ssl_mode=enable,server_certificate_hostname=server.com`. 

If flag values contain commas (such as RFC 2253 distinguished names for `server_certificate_dn`), use an alternative delimiter with the `^DELIM^` prefix syntax. Example: `--ssl-flags="^;^server_certificate_dn=CN=db.example.com,OU=RDS,O=Amazon.com,C=US"`. 

`--alloydb-cluster`=`ALLOYDB_CLUSTER`
     If the destination is an AlloyDB cluster, use this field to provide the AlloyDB cluster ID. 
`--cloudsql-instance`=`CLOUDSQL_INSTANCE`
     If the source or destination is a Cloud SQL database, then use this field to provide the respective Cloud SQL instance ID. 
`--database`=`DATABASE`
     The name of the specific database within the host. For Native Logical Postgres migrations, one of the replicating databases must be specified. 
`--host`=`HOST`
     IP or hostname of the database. 
    
    
    For PostgreSQL or MySQL destination profiles with Cloud SQL or AlloyDB, this
    flag is optional if the instance or cluster is provided.
    
    
    When `--psc-service-attachment` is also specified, this field value
    should be:
    
    
    1. For Cloud SQL PSC enabled instance - the dns_name field
       (e.g <uid>.<region>.sql.goog.).
    2. For Cloud SQL PSA instance (vpc peering) - the private ip of the
       instance.
    
    
    3. For AlloyDB PSC enabled cluster - the dns_name field of the primary
       instance (e.g <uid>.<region>.alloydb-psc.goog.).
    
    
    4. For AlloyDB PSA cluster - the private ip of the primary instance.

`--port`=`PORT`
     Network port of the database. 
    
    
    For PostgreSQL or MySQL destination profiles with Cloud SQL or AlloyDB, this
    flag is optional if the instance or cluster is provided.

Authentication method. 

At most one of these can be specified: 

`--enable-iam-authentication`
     Use IAM database authentication to connect to the database. The username will be overridden by the DMS service agent principal. This flag is only supported for PostgreSQL Destinations. 
Or at least one of these can be specified: 

`--username`=`USERNAME`
     Username that Database Migration Service uses to connect to the database. Database Migration Service encrypts the value when storing it. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Exactly one of these must be specified: 

`--password`=`PASSWORD`
     Password for the user that Database Migration Service uses to connect to the database. Database Migration Service encrypts the value when storing it, and the field is not returned on request. 
`--prompt-for-password`
     Prompt for the password used to connect to the database. 
`--ca-certificate`=`CA_CERTIFICATE`
     x509 PEM-encoded certificate of the CA that signed the database server's certificate. The value for this flag needs to be the content of the certificate file, not the path to the file. For example, on a Linux machine you can use command substitution: <code>\--ca-certificate=$(</path/to/certificate_file.pem)</code>. Database Migration Service will use this certificate to verify it's connecting to the correct host. Database Migration Service encrypts the value when storing it. 
`--ssl-type`=`SSL_TYPE`
     The type of SSL configuration. `SSL_TYPE` must be one of: `SERVER_ONLY`, `SERVER_CLIENT`, `REQUIRED`, `NONE`. 
`--client-certificate`=`CLIENT_CERTIFICATE`
     x509 PEM-encoded certificate that will be used by the replica to authenticate against the database server. The value for this flag needs to be the content of the certificate file, not the path to the file. For example, on a Linux machine you can use command substitution: <code>\--client-certificate=$(</path/to/certificate_file.pem)</code>. Database Migration Service encrypts the value when storing it. 
`--private-key`=`PRIVATE_KEY`
     Unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate. The value for this flag needs to be the content of the certificate file, not the path to the file. For example, on a Linux machine you can use command substitution: <code>\--private-key=$(</path/to/private_key_file.pem)</code>. Database Migration Service encrypts the value when storing it. 
At most one of these can be specified: 

Private connection resource - Resource ID of the private connection. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--private-connection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--private-connection` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 



`--private-connection`=`PRIVATE_CONNECTION`
     ID of the private_connection or fully qualified identifier for the private_connection. 

To set the `private_connection` attribute: 

* provide the argument `--private-connection` on the command line. 
Or at least one of these can be specified: 

Service attachment resource - Resource ID of the service attachment. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

* provide the argument `--psc-service-attachment` on the command line with a fully specified name; 
* provide the argument `--project` on the command line; 
* set the property `core/project`. 

To set the `region` attribute: 

  * provide the argument `--psc-service-attachment` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 



`--psc-service-attachment`=`PSC_SERVICE_ATTACHMENT`
     ID of the service_attachment or fully qualified identifier for the service_attachment. 

To set the `service_attachment` attribute: 

* provide the argument `--psc-service-attachment` on the command line. 
`--static-ip-connectivity`
     use static ip connectivity 
Or at least one of these can be specified: 

`--forward-ssh-hostname`=`FORWARD_SSH_HOSTNAME`
     Hostname for the SSH tunnel. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--forward-ssh-username`=`FORWARD_SSH_USERNAME`
     Username for the SSH tunnel. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--forward-ssh-port`=`FORWARD_SSH_PORT`; default=22
     Port for the SSH tunnel, default value is 22. 
Exactly one of these must be specified: 

`--forward-ssh-password`=`FORWARD_SSH_PASSWORD`
     SSH password. 
`--forward-ssh-private-key`=`FORWARD_SSH_PRIVATE_KEY`
     SSH private key.. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
