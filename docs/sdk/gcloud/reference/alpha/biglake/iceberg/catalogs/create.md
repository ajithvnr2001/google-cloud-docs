---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/iceberg/catalogs/create/
title: gcloud alpha biglake iceberg catalogs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:20.125570+00:00
---

# gcloud alpha biglake iceberg catalogs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/iceberg/catalogs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha biglake iceberg catalogs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha biglake iceberg catalogs create - create a BigLake Iceberg REST catalog 
SYNOPSIS
    

`gcloud alpha biglake iceberg catalogs create` `CATALOG` `--catalog-type`=`CATALOG_TYPE` [`--credential-mode`=`CREDENTIAL_MODE`; default="end-user"] [`--cross-cloud-cache`=`MODE`] [`--default-location`=`DEFAULT_LOCATION`] [`--description`=`DESCRIPTION`] [`--federated-catalog-identity-mode`=`FEDERATED_CATALOG_IDENTITY_MODE`] [`--federated-catalog-type`=`FEDERATED_CATALOG_TYPE`] [`--glue-aws-region`=`GLUE_AWS_REGION`] [`--glue-aws-role-arn`=`GLUE_AWS_ROLE_ARN`] [`--glue-warehouse`=`GLUE_WAREHOUSE`] [`--metadata-service-directory-name`=`METADATA_SERVICE_DIRECTORY_NAME`] [`--namespace-filters`=[`NAMESPACE`,…]] [`--primary-location`=`PRIMARY_LOCATION`] [`--refresh-interval`=`REFRESH_INTERVAL`] [`--restricted-locations`=[`LOCATION`,…]] [`--secret-name`=`SECRET_NAME`] [`--service-directory-name`=`SERVICE_DIRECTORY_NAME`] [`--snowflake-account-identifier`=`SNOWFLAKE_ACCOUNT_IDENTIFIER`] [`--snowflake-role`=`SNOWFLAKE_ROLE`] [`--snowflake-warehouse`=`SNOWFLAKE_WAREHOUSE`] [`--unity-catalog-name`=`UNITY_CATALOG_NAME`] [`--unity-instance-name`=`UNITY_INSTANCE_NAME`] [`--unity-service-principal-application-id`=`UNITY_SERVICE_PRINCIPAL_APPLICATION_ID`] [`--workday-base-url`=`WORKDAY_BASE_URL`] [`--workday-tenant`=`WORKDAY_TENANT`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a BigLake Iceberg REST catalog. 
EXAMPLES
     To add a catalog using a Cloud Storage bucket `my-catalog-bucket`, run: 
    
    
    gcloud alpha biglake iceberg catalogs create my-catalog-bucket --catalog-type=gcs-bucket

To create a catalog using a Cloud Storage bucket `my-catalog-bucket` with vended credentials, run: 
    
    
    gcloud alpha biglake iceberg catalogs create my-catalog-bucket --catalog-type=gcs-bucket --credential-mode=vended-credentials

To create a catalog `my-lakehouse-catalog` with catalog type lakehouse, run: 
    
    
    gcloud alpha biglake iceberg catalogs create my-lakehouse-catalog --catalog-type=lakehouse --default-location=gs://my-bucket

To create a catalog `my-lakehouse-catalog` with cross-cloud cache enabled, run: 
    
    
    gcloud alpha biglake iceberg catalogs create my-lakehouse-catalog --catalog-type=lakehouse --default-location=gs://my-bucket --cross-cloud-cache=enabled

To create a catalog `my-lakehouse-catalog` with CMEK encryption, run: 
    
    
    gcloud alpha biglake iceberg catalogs create my-lakehouse-catalog --catalog-type=lakehouse --default-location=gs://my-bucket --kms-key=projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key

To create a unity federated catalog `my-federated-catalog`, run: 
    
    
    gcloud alpha biglake iceberg catalogs create my-federated-catalog --catalog-type=federated --federated-catalog-type=unity --service-directory-name=projects/my-project/locations/us/namespaces/my-namespace/services/my-service --unity-catalog-name=my-catalog --unity-instance-name=instance.cloud.databricks.com --unity-service-principal-application-id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --primary-location=us

POSITIONAL ARGUMENTS
    

Catalog resource - The Iceberg Catalog to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `catalog` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CATALOG`
     ID of the catalog or fully qualified identifier for the catalog. 

To set the `catalog` attribute: 

  * provide the argument `catalog` on the command line. 


REQUIRED FLAGS
    

`--catalog-type`=`CATALOG_TYPE`
     Catalog type to create the catalog with. `CATALOG_TYPE` must be one of: 

`biglake`
     BigLake Iceberg catalog. Catalog type which allows namespaces and tables within a catalog to be mapped to locations beyond the catalog's designated default. Note: biglake and lakehouse catalog types are the same. 
`federated`
     BigLake federated catalog mirroring a remote catalog. 
`gcs-bucket`
     A catalog backed by a Cloud Storage bucket. 
`lakehouse`
     BigLake Iceberg catalog. Catalog type which allows namespaces and tables within a catalog to be mapped to locations beyond the catalog's designated default. Note: biglake and lakehouse catalog types are the same. 
OPTIONAL FLAGS
    

`--credential-mode`=`CREDENTIAL_MODE`; default="end-user"
     Credential mode to create the catalog with. `CREDENTIAL_MODE` must be one of: 

`end-user`
     Use end user credentials to access the catalog. 
`vended-credentials`
     Use vended credentials to access the catalog. 
`--cross-cloud-cache`=`MODE`
     Whether to enable caching of remote data on Google Cloud. This may result in data being temporarily persisted on Google Cloud. `MODE` must be one of: `enabled`, `disabled`. 
`--default-location`=`DEFAULT_LOCATION`
     Can only be used with BigLake catalogs. The default storage location for the catalog, e.g., `gs://my-bucket/…`. 
`--description`=`DESCRIPTION`
     Description of the resource. 
`--federated-catalog-identity-mode`=`FEDERATED_CATALOG_IDENTITY_MODE`
     The identity mode for the federated catalog. `FEDERATED_CATALOG_IDENTITY_MODE` must be one of: 

`service-identity`
     Queries execute using the BigLake service account. 
`user-identity-federation`
     Queries execute using the end user's identity and are propagated to the remote catalog. Identity federation must be configured in the remote catalog. 
`--federated-catalog-type`=`FEDERATED_CATALOG_TYPE`
     Type of the federated catalog. `FEDERATED_CATALOG_TYPE` must be one of: `unity`, `glue`, `snowflake`, `workday`. 
`--glue-aws-region`=`GLUE_AWS_REGION`
     The AWS region of the Glue catalog to connect to. 
`--glue-aws-role-arn`=`GLUE_AWS_ROLE_ARN`
     The AWS role ARN of the Glue catalog that the BigLake federated catalog will assume to access the catalog. 
`--glue-warehouse`=`GLUE_WAREHOUSE`
     The warehouse to connect to in AWS Glue Iceberg REST Catalog. 
`--metadata-service-directory-name`=`METADATA_SERVICE_DIRECTORY_NAME`
     The service directory resource name used to route metadata layer traffic with the remote catalog over a private network connection, in the format `projects/{project_id}/locations/{location}/namespaces/{namespace}/services/{service_name}`. This is used to retrieve catalog metadata (such as Iceberg configurations, namespaces, and tables) and to fetch OAuth tokens. See <https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse#setup-cci>. 
`--namespace-filters`=[`NAMESPACE`,…]
     Filters to determine which namespaces are included in the refresh process. Empty list means include all namespaces. 
`--primary-location`=`PRIMARY_LOCATION`
     Primary location for mirroring the remote catalog metadata. It must be a BigLake-supported location, and it should be proximate to the remote catalog's location for better performance and lower cost. 
`--refresh-interval`=`REFRESH_INTERVAL`
     The interval for refreshing metadata from the remote catalog (e.g., "1hr5m30s"). Defaults to seconds if no unit is specified. If unset, the refresh interval will be set to 0s (background refresh disabled). 
`--restricted-locations`=[`LOCATION`,…]
     Additional Google Cloud Storage buckets and locations (e.g., `gs://my-other-bucket/…`) that are permitted for use by resources within a catalog. This field is currently only used for BigLake catalogs.If `restricted_locations` is empty and unrestricted catalog creation is enabled, all accessible locations are allowed. Otherwise, only `default_location` and locations in this list are allowed. 
`--secret-name`=`SECRET_NAME`
     The secret resource name in Secret Manager, in the format `projects/{project_id}/locations/{location}/secrets/{secret_id}` or `projects/{project_id}/locations/{location}/secrets/{secret_id}/versions/{version_id}`. 
`--service-directory-name`=`SERVICE_DIRECTORY_NAME`
     The service directory resource name for request routing, in the format `projects/{project_id}/locations/{location}/namespaces/{namespace}/services/{service_name}`. see <https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse#setup-cci>. 
`--snowflake-account-identifier`=`SNOWFLAKE_ACCOUNT_IDENTIFIER`
     The account identifier of the Snowflake catalog to connect to. 
`--snowflake-role`=`SNOWFLAKE_ROLE`
     The specific role to request for the Snowflake catalog. 
`--snowflake-warehouse`=`SNOWFLAKE_WAREHOUSE`
     The warehouse to connect to in Snowflake. 
`--unity-catalog-name`=`UNITY_CATALOG_NAME`
     Name of the catalog in Unity Catalog. 
`--unity-instance-name`=`UNITY_INSTANCE_NAME`
     The instance name is the first part of the URL when you log into your Databricks deployment. For example, for a Databricks on Google Cloud workspace URL https://1.1.gcp.databricks.com, the instance name is 1.1.gcp.databricks.com. 
`--unity-service-principal-application-id`=`UNITY_SERVICE_PRINCIPAL_APPLICATION_ID`
     Optional. The application ID of the Databricks service principal that will be used to access the Unity Catalog in the OIDC authentication flow. With OIDC, the secret-name argument is not used. 
`--workday-base-url`=`WORKDAY_BASE_URL`
     The base URL of the Workday instance. 
`--workday-tenant`=`WORKDAY_TENANT`
     The Workday tenant name. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the catalog. The BigQuery encryption service account (bq-<project_number>@bigquery-encryption.iam.gserviceaccount.com) must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Google Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud biglake iceberg catalogs create](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/create)
    
    
    [gcloud beta biglake iceberg catalogs create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/biglake/iceberg/catalogs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
