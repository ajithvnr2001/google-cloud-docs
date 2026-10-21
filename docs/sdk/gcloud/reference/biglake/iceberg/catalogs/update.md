---
url: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/update/
title: gcloud biglake iceberg catalogs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:38.420359+00:00
---

# gcloud biglake iceberg catalogs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud biglake iceberg catalogs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud biglake iceberg catalogs update - update a BigLake Iceberg REST catalog 
SYNOPSIS
    

`gcloud biglake iceberg catalogs update` `CATALOG` [`--catalog-type`=`CATALOG_TYPE`] [`--credential-mode`=`CREDENTIAL_MODE`; default="end-user"] [`--cross-cloud-cache`=`MODE`] [`--description`=`DESCRIPTION`] [`--federated-catalog-identity-mode`=`FEDERATED_CATALOG_IDENTITY_MODE`] [`--glue-aws-role-arn`=`GLUE_AWS_ROLE_ARN`] [`--metadata-service-directory-name`=`METADATA_SERVICE_DIRECTORY_NAME`] [`--namespace-filters`=[`NAMESPACE`,…]] [`--refresh-interval`=`REFRESH_INTERVAL`] [`--restricted-locations`=[`LOCATION`,…]] [`--secret-name`=`SECRET_NAME`] [`--service-directory-name`=`SERVICE_DIRECTORY_NAME`] [`--snowflake-role`=`SNOWFLAKE_ROLE`] [`--unity-service-principal-application-id`=`UNITY_SERVICE_PRINCIPAL_APPLICATION_ID`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a BigLake Iceberg REST catalog. 
EXAMPLES
     To update the description of a catalog `my-catalog`, run: 
    
    
    gcloud biglake iceberg catalogs update my-catalog --description="updated description"

To update a catalog `my-lakehouse-catalog` to catalog type lakehouse with restricted locations, run: 
    
    
    gcloud biglake iceberg catalogs update my-lakehouse-catalog --catalog-type=lakehouse --restricted-locations=gs://my-bucket1,gs://my-bucket2

To update a catalog `my-lakehouse-catalog` to enable cross-cloud cache, run: 
    
    
    gcloud biglake iceberg catalogs update my-lakehouse-catalog --cross-cloud-cache=enabled

To update the Cloud KMS key of a catalog `my-catalog`, run: 
    
    
    gcloud biglake iceberg catalogs update my-catalog --kms-key=projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-new-key

To update the refresh interval and namespace filters for a federated catalog `my-federated-catalog`, run: 
    
    
    gcloud biglake iceberg catalogs update my-federated-catalog --refresh-interval=1h --namespace-filters=db1,db2

POSITIONAL ARGUMENTS
    

Catalog resource - The Iceberg Catalog to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `catalog` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CATALOG`
     ID of the catalog or fully qualified identifier for the catalog. 

To set the `catalog` attribute: 

  * provide the argument `catalog` on the command line. 


FLAGS
    

`--catalog-type`=`CATALOG_TYPE`
     Catalog type to update the catalog with. Currently only updating to a BigLake or Lakehouse catalog type is supported. `CATALOG_TYPE` must be one of: 

`biglake`
     BigLake Iceberg catalog. Catalog type which allows namespaces and tables within a catalog to be mapped to locations beyond the catalog's designated default. Note: biglake and lakehouse catalog types are the same. 
`lakehouse`
     BigLake Iceberg catalog. Catalog type which allows namespaces and tables within a catalog to be mapped to locations beyond the catalog's designated default. Note: biglake and lakehouse catalog types are the same. 
`--credential-mode`=`CREDENTIAL_MODE`; default="end-user"
     Credential mode to create the catalog with. `CREDENTIAL_MODE` must be one of: 

`end-user`
     Use end user credentials to access the catalog. 
`vended-credentials`
     Use vended credentials to access the catalog. 
`--cross-cloud-cache`=`MODE`
     Whether to enable caching of remote data on Google Cloud. This may result in data being temporarily persisted on Google Cloud. `MODE` must be one of: `enabled`, `disabled`. 
`--description`=`DESCRIPTION`
     Description of the resource. 
`--federated-catalog-identity-mode`=`FEDERATED_CATALOG_IDENTITY_MODE`
     The identity mode for the federated catalog. `FEDERATED_CATALOG_IDENTITY_MODE` must be one of: 

`service-identity`
     Queries execute using the BigLake service account. 
`user-identity-federation`
     Queries execute using the end user's identity and are propagated to the remote catalog. Identity federation must be configured in the remote catalog. 
`--glue-aws-role-arn`=`GLUE_AWS_ROLE_ARN`
     The AWS role ARN of the Glue catalog that the BigLake federated catalog will assume to access the catalog. 
`--metadata-service-directory-name`=`METADATA_SERVICE_DIRECTORY_NAME`
     The service directory resource name used to route metadata layer traffic with the remote catalog over a private network connection, in the format `projects/{project_id}/locations/{location}/namespaces/{namespace}/services/{service_name}`. This is used to retrieve catalog metadata (such as Iceberg configurations, namespaces, and tables) and to fetch OAuth tokens. See <https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse#setup-cci>. 
`--namespace-filters`=[`NAMESPACE`,…]
     Filters to determine which namespaces are included in the refresh process. Empty list means include all namespaces. 
`--refresh-interval`=`REFRESH_INTERVAL`
     Interval for refreshing metadata from the remote catalog (e.g., "1hr5m30s"). Defaults to seconds if no unit is specified. If unset, the refresh interval will be set to 0s (background refresh disabled). 
`--restricted-locations`=[`LOCATION`,…]
     Additional Google Cloud Storage buckets and locations (e.g., `gs://my-other-bucket/…`) that are permitted for use by resources within a catalog. This field is currently only used for BigLake catalogs.If `restricted_locations` is empty and unrestricted catalog creation is enabled, all accessible locations are allowed. Otherwise, only `default_location` and locations in this list are allowed. 
`--secret-name`=`SECRET_NAME`
     Resource name of the Secret Manager secret, in the format `projects/{project_id}/locations/{location}/secrets/{secret_id}` or `projects/{project_id}/locations/{location}/secrets/{secret_id}/versions/{version_id}`. 
`--service-directory-name`=`SERVICE_DIRECTORY_NAME`
     The service directory resource name for request routing, in the format `projects/{project_id}/locations/{location}/namespaces/{namespace}/services/{service_name}`. see <https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse#setup-cci>. 
`--snowflake-role`=`SNOWFLAKE_ROLE`
     The specific role to request for the Snowflake catalog. 
`--unity-service-principal-application-id`=`UNITY_SERVICE_PRINCIPAL_APPLICATION_ID`
     Optional. The application ID of the Databricks service principal that will be used to access the Unity Catalog in the OIDC authentication flow. With OIDC, the secret-name argument is not used. 
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
     These variants are also available: 
    
    
    [gcloud alpha biglake iceberg catalogs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/iceberg/catalogs/update)
    
    
    [gcloud beta biglake iceberg catalogs update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/biglake/iceberg/catalogs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
