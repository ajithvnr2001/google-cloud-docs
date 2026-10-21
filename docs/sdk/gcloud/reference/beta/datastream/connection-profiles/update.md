---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/connection-profiles/update/
title: gcloud beta datastream connection-profiles update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:28.802180+00:00
---

# gcloud beta datastream connection-profiles update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/connection-profiles/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta datastream connection-profiles update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta datastream connection-profiles update - update a Datastream connection profile 
SYNOPSIS
    

`gcloud beta datastream connection-profiles update` (`CONNECTION_PROFILE` : `--location`=`LOCATION`) `--type`=`TYPE` [`--display-name`=`DISPLAY_NAME`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--no-connectivity` | `--private-connection-name`=`PRIVATE_CONNECTION_NAME` | `--static-ip-connectivity` | `--forward-ssh-hostname`=`FORWARD_SSH_HOSTNAME` `--forward-ssh-port`=`FORWARD_SSH_PORT`; default=22 `--forward-ssh-username`=`FORWARD_SSH_USERNAME` `--forward-ssh-password`=`FORWARD_SSH_PASSWORD` | `--forward-ssh-private-key`=`FORWARD_SSH_PRIVATE_KEY`] [`--spanner-host`=`SPANNER_HOST` | `--bucket-name`=`BUCKET_NAME` `--root-path`=`ROOT_PATH` | `--database-service`=`DATABASE_SERVICE` `--oracle-hostname`=`ORACLE_HOSTNAME` `--oracle-port`=`ORACLE_PORT` `--oracle-username`=`ORACLE_USERNAME` `--oracle-ca-certificate`=`ORACLE_CA_CERTIFICATE` `--oracle-server-certificate-distinguished-name`=`ORACLE_SERVER_CERTIFICATE_DISTINGUISHED_NAME` `--oracle-password`=`ORACLE_PASSWORD` | `--oracle-prompt-for-password` | `--oracle-secret-manager-stored-password`=`ORACLE_SECRET_MANAGER_STORED_PASSWORD` | `--dataverse-environment-url`=`DATAVERSE_ENVIRONMENT_URL` `--dataverse-oauth-client-id`=`DATAVERSE_OAUTH_CLIENT_ID` `--dataverse-tenant-id`=`DATAVERSE_TENANT_ID` `--dataverse-oauth-client-secret`=`DATAVERSE_OAUTH_CLIENT_SECRET` | `--dataverse-prompt-for-oauth-client-secret` | `--dataverse-secret-manager-stored-oauth-client-secret`=`DATAVERSE_SECRET_MANAGER_STORED_OAUTH_CLIENT_SECRET` | `--mongodb-additional-options`=[`MONGODB_PROFILE_ADDITIONAL_OPTIONS`,…] `--mongodb-direct-connection` `--mongodb-host-addresses`=`IPv4_ADDRESS_OR_HOSTNAME`:`PORT`,[…] `--mongodb-replica-set`=`MONGODB_REPLICA_SET` `--mongodb-username`=`MONGODB_USERNAME` `--mongodb-ca-certificate`=`MONGODB_CA_CERTIFICATE` `--mongodb-tls` `--mongodb-password`=`MONGODB_PASSWORD` | `--mongodb-prompt-for-password` | `--mongodb-secret-manager-stored-password`=`MONGODB_SECRET_MANAGER_STORED_PASSWORD` `--mongodb-srv-connection-format` | `--mongodb-standard-connection-format` | `--mysql-hostname`=`MYSQL_HOSTNAME` `--mysql-port`=`MYSQL_PORT` `--mysql-username`=`MYSQL_USERNAME` `--ca-certificate`=`CA_CERTIFICATE` `--client-certificate`=`CLIENT_CERTIFICATE` `--client-key`=`CLIENT_KEY` `--mysql-password`=`MYSQL_PASSWORD` | `--mysql-prompt-for-password` | `--mysql-secret-manager-stored-password`=`MYSQL_SECRET_MANAGER_STORED_PASSWORD` | `--postgresql-database`=`POSTGRESQL_DATABASE` `--postgresql-hostname`=`POSTGRESQL_HOSTNAME` `--postgresql-port`=`POSTGRESQL_PORT` `--postgresql-username`=`POSTGRESQL_USERNAME` `--postgresql-ca-certificate`=`POSTGRESQL_CA_CERTIFICATE` `--postgresql-server-certificate-hostname`=`POSTGRESQL_SERVER_CERTIFICATE_HOSTNAME` `--postgresql-client-certificate`=`POSTGRESQL_CLIENT_CERTIFICATE` `--postgresql-client-key`=`POSTGRESQL_CLIENT_KEY` `--postgresql-password`=`POSTGRESQL_PASSWORD` | `--postgresql-prompt-for-password` | `--postgresql-secret-manager-stored-password`=`POSTGRESQL_SECRET_MANAGER_STORED_PASSWORD` | `--salesforce-domain`=`SALESFORCE_DOMAIN` `--salesforce-oauth2-client-id`=`SALESFORCE_OAUTH2_CLIENT_ID` `--salesforce-oauth2-client-secret`=`SALESFORCE_OAUTH2_CLIENT_SECRET` | `--salesforce-prompt-for-oauth2-client-secret` | `--salesforce-secret-manager-stored-oauth2-client-secret`=`SALESFORCE_SECRET_MANAGER_STORED_OAUTH2_CLIENT_SECRET` | `--salesforce-username`=`SALESFORCE_USERNAME` `--salesforce-password`=`SALESFORCE_PASSWORD` | `--salesforce-prompt-for-password` | `--salesforce-secret-manager-stored-password`=`SALESFORCE_SECRET_MANAGER_STORED_PASSWORD` `--salesforce-prompt-for-security-token` | `--salesforce-secret-manager-stored-security-token`=`SALESFORCE_SECRET_MANAGER_STORED_SECURITY_TOKEN` | `--salesforce-security-token`=`SALESFORCE_SECURITY_TOKEN` | `--salesforce-marketing-cloud-oauth-client-id`=`SALESFORCE_MARKETING_CLOUD_OAUTH_CLIENT_ID` `--salesforce-marketing-cloud-subdomain`=`SALESFORCE_MARKETING_CLOUD_SUBDOMAIN` `--salesforce-marketing-cloud-oauth-client-secret`=`SALESFORCE_MARKETING_CLOUD_OAUTH_CLIENT_SECRET` | `--salesforce-marketing-cloud-prompt-for-oauth-client-secret` | `--salesforce-marketing-cloud-secret-manager-stored-oauth-client-secret`=`SALESFORCE_MARKETING_CLOUD_SECRET_MANAGER_STORED_OAUTH_CLIENT_SECRET` | `--servicenow-instance`=`SERVICENOW_INSTANCE` `--servicenow-oauth-client-id`=`SERVICENOW_OAUTH_CLIENT_ID` `--servicenow-oauth-client-secret`=`SERVICENOW_OAUTH_CLIENT_SECRET` | `--servicenow-prompt-for-oauth-client-secret` | `--servicenow-secret-manager-stored-oauth-client-secret`=`SERVICENOW_SECRET_MANAGER_STORED_OAUTH_CLIENT_SECRET` | `--servicenow-username`=`SERVICENOW_USERNAME` `--servicenow-password`=`SERVICENOW_PASSWORD` | `--servicenow-prompt-for-password` | `--servicenow-secret-manager-stored-password`=`SERVICENOW_SECRET_MANAGER_STORED_PASSWORD` | `--sqlserver-database`=`SQLSERVER_DATABASE` `--sqlserver-hostname`=`SQLSERVER_HOSTNAME` `--sqlserver-port`=`SQLSERVER_PORT` `--sqlserver-username`=`SQLSERVER_USERNAME` `--sqlserver-password`=`SQLSERVER_PASSWORD` | `--sqlserver-prompt-for-password` | `--sqlserver-secret-manager-stored-password`=`SQLSERVER_SECRET_MANAGER_STORED_PASSWORD`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `(DEPRECATED)` Datastream beta version is deprecated. Please use`[gcloud datastream connection-profiles update](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update)` command instead. 

Updates a Datastream connection profile 

`
EXAMPLES
     To update a connection profile for Oracle: 
    
    
    gcloud beta datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=oracle --oracle-password=fakepassword --oracle-username=fakeuser --display-name=my-profile --oracle-hostname=35.188.150.50 --oracle-port=1521 --database-service=ORCL --static-ip-connectivity

To update a connection profile for MySQL: 
    
    
    gcloud beta datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=mysql --mysql-password=fakepassword --mysql-username=fakeuser --display-name=my-profile --mysql-hostname=35.188.150.50 --mysql-port=3306 --static-ip-connectivity

To update a connection profile for Google Cloud Storage: 
    
    
    gcloud beta datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=google-cloud-storage --bucket-name=fake-bucket --root-path=/root/path --display-name=my-profile --no-connectivity

POSITIONAL ARGUMENTS
    

Connection profile resource - The connection profile to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

`--location`=`LOCATION`
     The Cloud location for the connection_profile. 

To set the `location` attribute: 

  * provide the argument `connection_profile` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--type`=`TYPE`
     Type can be MYSQL, ORACLE, POSTGRESQL, SQLSERVER, SALESFORCE, GOOGLE-CLOUD-STORAGE, BIGQUERY, DATAVERSE, SALESFORCE-MARKETING-CLOUD or SERVICENOW 
OPTIONAL FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Friendly name for the connection profile. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta datastream connection-profiles update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta datastream connection-profiles update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--no-connectivity`
     no connectivity 
Or at least one of these can be specified: 

Private connection resource - Resource ID of the private connection. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--private-connection-name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--private-connection-name` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--private-connection-name`=`PRIVATE_CONNECTION_NAME`
     ID of the private_connection or fully qualified identifier for the private_connection. 

To set the `private_connection` attribute: 

  * provide the argument `--private-connection-name` on the command line. 


`--static-ip-connectivity`
     use static ip connectivity 
Or at least one of these can be specified: 

`--forward-ssh-hostname`=`FORWARD_SSH_HOSTNAME`
     Hostname for the SSH tunnel. 
`--forward-ssh-port`=`FORWARD_SSH_PORT`; default=22
     Port for the SSH tunnel, default value is 22. 
`--forward-ssh-username`=`FORWARD_SSH_USERNAME`
     Username for the SSH tunnel. 
At most one of these can be specified: 

`--forward-ssh-password`=`FORWARD_SSH_PASSWORD`
     SSH password. 
`--forward-ssh-private-key`=`FORWARD_SSH_PRIVATE_KEY`
     SSH private key.. 
At most one of these can be specified: 

`--spanner-host`=`SPANNER_HOST`
     The regional Spanner endpoint. Format: https://spanner.{region}.rep.googleapis.com. 
`--bucket-name`=`BUCKET_NAME`
     The full project and resource path for Cloud Storage bucket including the name. 
`--root-path`=`ROOT_PATH`
     The root path inside the Cloud Storage bucket. 
`--database-service`=`DATABASE_SERVICE`
     Database service for the Oracle connection. 
`--oracle-hostname`=`ORACLE_HOSTNAME`
     IP or hostname of the oracle source database. 
`--oracle-port`=`ORACLE_PORT`
     Network port of the oracle source database. 
`--oracle-username`=`ORACLE_USERNAME`
     Username Datastream will use to connect to the database. 
`--oracle-ca-certificate`=`ORACLE_CA_CERTIFICATE`
     PEM-encoded certificate of the CA that signed the source database server's certificate. 
`--oracle-server-certificate-distinguished-name`=`ORACLE_SERVER_CERTIFICATE_DISTINGUISHED_NAME`
     The distinguished name (DN) mentioned in the server certificate. This corresponds to the SSL_SERVER_CERT_DN sqlnet parameter. If this field is not provided, the DN matching is not enforced. 
At most one of these can be specified: 

`--oracle-password`=`ORACLE_PASSWORD`
     Password for the user that Datastream will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Datastream. 
`--oracle-prompt-for-password`
     Prompt for the password used to connect to the database. 
`--oracle-secret-manager-stored-password`=`ORACLE_SECRET_MANAGER_STORED_PASSWORD`
     Path to secret manager, storing the password for the user used to connect to the database. 
`--dataverse-environment-url`=`DATAVERSE_ENVIRONMENT_URL`
     Environment URL of the Microsoft Dataverse instance. Example: 'myenv.crm.dynamics.com' 
`--dataverse-oauth-client-id`=`DATAVERSE_OAUTH_CLIENT_ID`
     OAuth 2.0 Client ID used to connect to Dataverse. 
`--dataverse-tenant-id`=`DATAVERSE_TENANT_ID`
     Tenant ID of the Microsoft Dataverse instance. 
At most one of these can be specified: 

`--dataverse-oauth-client-secret`=`DATAVERSE_OAUTH_CLIENT_SECRET`
     OAuth 2.0 Client secret used to connect to Dataverse. 
`--dataverse-prompt-for-oauth-client-secret`
     Prompt for the OAuth 2.0 Client secret used to connect to Dataverse. 
`--dataverse-secret-manager-stored-oauth-client-secret`=`DATAVERSE_SECRET_MANAGER_STORED_OAUTH_CLIENT_SECRET`
     Path to secret manager, storing the OAuth 2.0 Client secret used to connect to Dataverse. 
`--mongodb-additional-options`=[`MONGODB_PROFILE_ADDITIONAL_OPTIONS`,…]
     Specifies additional options for the MongoDB connection. 
`--mongodb-direct-connection`
     Connect to the mongodb hosts directly and do not try to resolve any of the replicas from the replica set. 
`--mongodb-host-addresses`=`IPv4_ADDRESS_OR_HOSTNAME`:`PORT`,[…]
     IP or hostname and port of the MongoDB source database. 
`--mongodb-replica-set`=`MONGODB_REPLICA_SET`
     Replica set of the MongoDB source database. 
`--mongodb-username`=`MONGODB_USERNAME`
     Username Datastream will use to connect to the database. 
`--mongodb-ca-certificate`=`MONGODB_CA_CERTIFICATE`
     x509 PEM-encoded certificate of the CA that signed the source database server's certificate. The replica will use this certificate to verify it's connecting to the right host. 
`--mongodb-tls`
     Enable Transport Layer Security for the monogodb connection. 
At most one of these can be specified: 

`--mongodb-password`=`MONGODB_PASSWORD`
     Password for the user that Datastream will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Datastream. 
`--mongodb-prompt-for-password`
     Prompt for the password used to connect to the database. 
`--mongodb-secret-manager-stored-password`=`MONGODB_SECRET_MANAGER_STORED_PASSWORD`
     Path to secret manager, storing the password for the user used to connect to the database. 
At most one of these can be specified: 

`--mongodb-srv-connection-format`
     SRV Connection format for the MongoDB source database. 
`--mongodb-standard-connection-format`
     Standard connection format for the MongoDB source database. 
`--mysql-hostname`=`MYSQL_HOSTNAME`
     IP or hostname of the MySQL source database. 
`--mysql-port`=`MYSQL_PORT`
     Network port of the MySQL source database. 
`--mysql-username`=`MYSQL_USERNAME`
     Username Datastream will use to connect to the database. 
`--ca-certificate`=`CA_CERTIFICATE`
     x509 PEM-encoded certificate of the CA that signed the source database server's certificate. The replica will use this certificate to verify it's connecting to the right host. 
`--client-certificate`=`CLIENT_CERTIFICATE`
     x509 PEM-encoded certificate that will be used by the replica to authenticate against the source database server. 
`--client-key`=`CLIENT_KEY`
     Unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate. 
At most one of these can be specified: 

`--mysql-password`=`MYSQL_PASSWORD`
     Password for the user that Datastream will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Datastream. 
`--mysql-prompt-for-password`
     Prompt for the password used to connect to the database. 
`--mysql-secret-manager-stored-password`=`MYSQL_SECRET_MANAGER_STORED_PASSWORD`
     Path to secret manager, storing the password for the user used to connect to the database. 
`--postgresql-database`=`POSTGRESQL_DATABASE`
     Database service for the PostgreSQL connection. 
`--postgresql-hostname`=`POSTGRESQL_HOSTNAME`
     IP or hostname of the PostgreSQL source database. 
`--postgresql-port`=`POSTGRESQL_PORT`
     Network port of the PostgreSQL source database. 
`--postgresql-username`=`POSTGRESQL_USERNAME`
     Username Datastream will use to connect to the database. 
`--postgresql-ca-certificate`=`POSTGRESQL_CA_CERTIFICATE`
     x509 PEM-encoded certificate of the CA that signed the source database server's certificate. The replica will use this certificate to verify it's connecting to the right host. 
`--postgresql-server-certificate-hostname`=`POSTGRESQL_SERVER_CERTIFICATE_HOSTNAME`
     The hostname mentioned in the Subject or SAN extension of the server certificate. If this field is not provided, the hostname in the server certificate is not validated. 
`--postgresql-client-certificate`=`POSTGRESQL_CLIENT_CERTIFICATE`
     x509 PEM-encoded certificate that will be used by the replica to authenticate against the source database server. 
`--postgresql-client-key`=`POSTGRESQL_CLIENT_KEY`
     Unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate. 
At most one of these can be specified: 

`--postgresql-password`=`POSTGRESQL_PASSWORD`
     Password for the user that Datastream will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Datastream. 
`--postgresql-prompt-for-password`
     Prompt for the password used to connect to the database. 
`--postgresql-secret-manager-stored-password`=`POSTGRESQL_SECRET_MANAGER_STORED_PASSWORD`
     Path to secret manager, storing the password for the user used to connect to the database. 
`--salesforce-domain`=`SALESFORCE_DOMAIN`
     Domain of the Salesforce organization. For example, 'myorg.my.salesforce.com' 
At most one of these can be specified: 

`--salesforce-oauth2-client-id`=`SALESFORCE_OAUTH2_CLIENT_ID`
     OAuth 2.0 Client ID used to connect to Salesforce. 
At most one of these can be specified: 

`--salesforce-oauth2-client-secret`=`SALESFORCE_OAUTH2_CLIENT_SECRET`
     OAuth 2.0 Client secret used to connect to Salesforce. 
`--salesforce-prompt-for-oauth2-client-secret`
     Prompt for the OAuth 2.0 Client secret used to connect to Salesforce. 
`--salesforce-secret-manager-stored-oauth2-client-secret`=`SALESFORCE_SECRET_MANAGER_STORED_OAUTH2_CLIENT_SECRET`
     Path to secret manager, storing the OAuth 2.0 Client secret used to connect to Salesforce. 
`--salesforce-username`=`SALESFORCE_USERNAME`
     Username Datastream will use to connect to the database. 
At most one of these can be specified: 

`--salesforce-password`=`SALESFORCE_PASSWORD`
     Password for the user that Datastream will be using to connect to Salesforce. This field is not returned on request, and the value is encrypted when stored in Datastream. 
`--salesforce-prompt-for-password`
     Prompt for the password used to connect to Salesforce. 
`--salesforce-secret-manager-stored-password`=`SALESFORCE_SECRET_MANAGER_STORED_PASSWORD`
     Path to secret manager, storing the password for the user used to connect to Salesforce. 
At most one of these can be specified: 

`--salesforce-prompt-for-security-token`
     Prompt for the security token used to connect to Salesforce. 
`--salesforce-secret-manager-stored-security-token`=`SALESFORCE_SECRET_MANAGER_STORED_SECURITY_TOKEN`
     Path to secret manager, storing the security token used to connect to Salesforce. 
`--salesforce-security-token`=`SALESFORCE_SECURITY_TOKEN`
     Security token for the user that Datastream will be using to connect to Salesforce. 
`--salesforce-marketing-cloud-oauth-client-id`=`SALESFORCE_MARKETING_CLOUD_OAUTH_CLIENT_ID`
     OAuth 2.0 Client ID used to connect to Salesforce Marketing Cloud. 
`--salesforce-marketing-cloud-subdomain`=`SALESFORCE_MARKETING_CLOUD_SUBDOMAIN`
     Subdomain for the Salesforce Marketing Cloud connection. 
At most one of these can be specified: 

`--salesforce-marketing-cloud-oauth-client-secret`=`SALESFORCE_MARKETING_CLOUD_OAUTH_CLIENT_SECRET`
     OAuth 2.0 Client secret used to connect to Salesforce Marketing Cloud. 
`--salesforce-marketing-cloud-prompt-for-oauth-client-secret`
     Prompt for the OAuth 2.0 Client secret used to connect to Salesforce Marketing Cloud. 
`--salesforce-marketing-cloud-secret-manager-stored-oauth-client-secret`=`SALESFORCE_MARKETING_CLOUD_SECRET_MANAGER_STORED_OAUTH_CLIENT_SECRET`
     Path to secret manager, storing the OAuth 2.0 Client secret used to connect to Salesforce Marketing Cloud. 
`--servicenow-instance`=`SERVICENOW_INSTANCE`
     The instance of the ServiceNow account. 
At most one of these can be specified: 

`--servicenow-oauth-client-id`=`SERVICENOW_OAUTH_CLIENT_ID`
     OAuth 2.0 Client ID used to connect to ServiceNow. 
At most one of these can be specified: 

`--servicenow-oauth-client-secret`=`SERVICENOW_OAUTH_CLIENT_SECRET`
     OAuth 2.0 Client secret used to connect to ServiceNow. 
`--servicenow-prompt-for-oauth-client-secret`
     Prompt for the OAuth 2.0 Client secret used to connect to ServiceNow. 
`--servicenow-secret-manager-stored-oauth-client-secret`=`SERVICENOW_SECRET_MANAGER_STORED_OAUTH_CLIENT_SECRET`
     Path to secret manager, storing the OAuth 2.0 Client secret used to connect to ServiceNow. 
`--servicenow-username`=`SERVICENOW_USERNAME`
     Username used to connect to ServiceNow. 
At most one of these can be specified: 

`--servicenow-password`=`SERVICENOW_PASSWORD`
     Password used to connect to ServiceNow. 
`--servicenow-prompt-for-password`
     Prompt for the password used to connect to ServiceNow. 
`--servicenow-secret-manager-stored-password`=`SERVICENOW_SECRET_MANAGER_STORED_PASSWORD`
     Path to secret manager, storing the password used to connect to ServiceNow. 
`--sqlserver-database`=`SQLSERVER_DATABASE`
     Database service for the SQL Server connection. 
`--sqlserver-hostname`=`SQLSERVER_HOSTNAME`
     IP or hostname of the SQL Server source database. 
`--sqlserver-port`=`SQLSERVER_PORT`
     Network port of the SQL Server source database. 
`--sqlserver-username`=`SQLSERVER_USERNAME`
     Username Datastream will use to connect to the database. 
At most one of these can be specified: 

`--sqlserver-password`=`SQLSERVER_PASSWORD`
     Password for the user that Datastream will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Datastream. 
`--sqlserver-prompt-for-password`
     Prompt for the password used to connect to the database. 
`--sqlserver-secret-manager-stored-password`=`SQLSERVER_SECRET_MANAGER_STORED_PASSWORD`
     Path to secret manager, storing the password for the user used to connect to the database. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud datastream connection-profiles update](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
