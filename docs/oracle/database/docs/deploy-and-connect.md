---
url: https://docs.cloud.google.com/oracle/database/docs/deploy-and-connect/
title: Create Goldengate deployments and connections \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:47.426184+00:00
---

# Create Goldengate deployments and connections  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/deploy-and-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Create Goldengate deployments and connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a Goldengate deployments and connections in Google Cloud.

Oracle Goldengate enables real-time data integration and replication across diverse cloud and on-premises environments. It lets you seamlessly move, transform, and synchronize data between operational and analytical systems with minimal latency to ensure that your data is always current and available.

Oracle Database@Google Cloud lets you create Goldengate deployment and connections. A Goldengate deployment is a managed runtime environment used to design, orchestrate, and monitor your real-time data replication and data transformation tasks. A connection stores the credentials, network details, and resources needed to securely access and move data between your data source and target.

For a list of regions and zones in which you can create Goldengate resources, see [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).

## Before you begin

  * [Set up your Oracle Database@Google Cloud environment](https://docs.cloud.google.com/oracle/database/docs/setup-oracle-database-environment).

  * Make sure that you have an [ODB Network](https://docs.cloud.google.com/oracle/database/docs/create-odb-network). A Goldengate deployment requires one client subnet.

  * Make sure that you have the required Identity and Access Management (IAM) roles and permissions to create Goldengate resources:

    * `roles/oracledatabase.goldenGateDeploymentAdmin`: to create deployments.
    * `roles/oracledatabase.goldenGateConnectionAdmin`: to create connections.
    * `roles/oracledatabase.goldenGateConnectionAssignmentAdmin`: to create connection assignments.
    * `secretmanager.versions.access` permission: to use a secret for creating a deployment or a connection.

For more information about how to assign roles, see [Apply IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## Create and connect to a Goldengate deployment

You must create your Goldengate resources in the same region and zone as your ODB Network. This ensures optimal performance and seamless communication.

Creating and using a Goldengate deployment and connection for data replication and data transformation involves the following high-level steps:

  1. Create a Goldengate deployment to host your replication and transformation services.

  2. Create a connection to connect with your data source.

  3. Create a connection assignment to link your deployment and connection, and to establish a secure path between your source and target databases.

  4. Test your connection assignment to ensure that your connection works.

  5. Configure Extracts, Replicats, and Transforms. Add an extract to capture data from your source, a replicat to deliver data to your target, or a data transform to move and transform data between sources.




## Create a Goldengate deployment

Oracle Database@Google Cloud lets you create the following types of Goldengate deployments:

  * Data replication: capture and replicate data from a database, application, or cloud. The following technology options are available for data replication:

    * Oracle AI Database
    * Big Data
    * Microsoft SQL Server
    * MySQL
    * PostgreSQL
    * IBM Db2 for i
    * IBM Db2 for z/OS
  * Data transform: move and transform data between different systems using graphical data transformations. The only technology option available is Oracle Data Transforms.




To learn more about the types of deployment, see [Oracle documentation about OCI Goldengate](https://docs.oracle.com/en/cloud/paas/goldengate-service/druyg/#articletitle).

To create a Goldengate deployment, do the following:

### gcloud

Use the `gcloud oracle-database goldengate-deployments create` command to create a deployment.
    
    
    gcloud oracle-database goldengate-deployments create DEPLOYMENT_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --display-name="DEPLOYMENT_NAME" \
        --gcp-oracle-zone=GCP_ORACLE_ZONE \
        --odb-subnet=projects/ODB_NETWORK_PROJECT_ID/locations/ODB_NETWORK_REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/ODB_SUBNET_ID \
        --properties-license-model=LICENSE_MODEL \
        --properties-environment-type=ENVIRONMENT_TYPE \
        --properties-is-auto-scaling-enabled \
        --properties-deployment-type=DEPLOYMENT_TYPE \
        --properties-cpu-core-count=CPU_CORE_COUNT \
        --ogg-data-deployment=DEPLOYMENT \
        --ogg-data-admin-username=USERNAME \
        --ogg-data-admin-password=PASSWORD \
        --maintenance-window-day=DAY \
        --maintenance-window-start-hour=HOUR \
        --maintenance-config-is-interim-release-auto-upgrade-enabled \
        --maintenance-config-interim-release-upgrade-period-days=INTERIM_RELEASE_UPGRADE_PERIOD_DAYS \
        --maintenance-config-bundle-release-upgrade-period-days=BUNDLE_RELEASE_UPGRADE_PERIOD_DAYS \
        --maintenance-config-major-release-upgrade-period-days=MAJOR_RELEASE_UPGRADE_PERIOD_DAYS \
        --maintenance-config-security-patch-upgrade-period-days=SECURITY_PATCH_UPGRADE_PERIOD_DAYS
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which to create the deployment.
  * REGION: the region where you want to create the deployment.
  * DEPLOYMENT_ID: a unique ID for your deployment.
  * DEPLOYMENT_NAME: a name for your deployment. This name appears in the Google Cloud console.
  * GCP_ORACLE_ZONE: the Google Cloud Oracle zone for your deployment. See [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).
  * For the `--odb-subnet` property, replace the following: 
    * ODB_NETWORK_PROJECT_ID: the ID of your Google Cloud project which contains your ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
    * ODB_NETWORK_: the region where your ODB Network is located.
    * ODB_NETWORK_ID: the ID of your ODB Network.
    * ODB_SUBNET_ID: the ID of your ODB Subnet.
  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. The accepted values are `bring-your-own-license` or `license-included`.
  * ENVIRONMENT_TYPE: the type of the environment in which the deployment is to be used:

    * `DEVELOPMENT_OR_TESTING`: set up a deployment with the recommended defaults for a development or testing environment. The default values are as follows:

      * 1 OCPUs
      * 16 GB memory
      * 1 Gbps network bandwidth
      * 500 GB storage
    * `PRODUCTION`: set up a deployment with the recommended defaults for a production environment. The default values are as follows:

      * 4 OCPUs
      * 64 GB memory
      * 4 Gbps network bandwidth
      * 2000 GB storage
  * AUTOSCALING: let the deployment use up to three times the provisioned number of cores as the workload increases. You can increase the number of cores up to 24 cores.

  * DEPLOYMENT_TYPE: the type of deployment. Accepted values are as follows:

    * Oracle AI Database: `DATABASE_ORACLE`
    * Big Data: `BIGDATA`
    * Microsoft SQL Server: `DATABASE_MICROSOFT_SQLSERVER`
    * MySQL: `DATABASE_MYSQL`
    * PostgreSQL: `DATABASE_POSTGRESQL`
    * IBM Db2 for i:`DATABASE_DB2ZOS`
    * IBM Db2 for z/OS:`DATABASE_DB2I`
    * Data transforms: `DATA_TRANSFORMS`
  * CPU_CORE_COUNT: the number of OCPUs. You can allot between 1 and 24 OCPUs.

  * DEPLOYMENT: a name for the instance deployment. The name must be 1 to 32 characters long, contain only alphanumeric characters.

  * USERNAME: the administrator's username.

  * PASSWORD: the administrator's password. Instead of a raw password, you can also use a secret stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

Secret Manager provides a secure storage mechanism. To use a secret, use the following property:
        
        --ogg-data-admin-password-secret-version=projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID
          

Replace the following:

    * PROJECT_ID: the Google Cloud project ID
    * SECRET_ID: the ID of the secret
    * VERSION_ID: the ID of the secret version

For example:
          
          --ogg-data-admin-password-secret-version=projects/test-project/secrets/deployment-password/versions/1
          

  * DAY: the day of the week on which you prefer to perform the maintenance. Accepted value is the name of the day in uppercase. For example, `MONDAY`.

  * HOUR: the time slot of the day when you want to perform the maintenance. A time slot is a four-hour slot. Accepted values are as follows:

Value | Time slot | `0` | 0:00 - 3:59 UTC  
---|---  
`4` | 4:00 - 7:59 UTC  
`8` | 8:00 - 11:59 UTC  
`12` | 12:00 - 15:59 UTC  
`16` | 16:00 - 19:59 UTC  
`20` | 20:00 - 23:59 UTC  
  * AUTO_UPGRADE_ENABLED: enable auto upgrade for interim releases. By default, the auto upgrade is disabled.

  * INTERIM_RELEASE_UPGRADE_PERIOD_DAYS: the auto upgrade period for interim releases (from 0 to 365 days).

  * BUNDLE_RELEASE_UPGRADE_PERIOD_DAYS: the auto upgrade period for bundle releases (from 0 to 180 days).

  * MAJOR_RELEASE_UPGRADE_PERIOD_DAYS: the auto upgrade period for major releases (from 0 to 365 days).

  * SECURITY_PATCH_UPGRADE_PERIOD_DAYS: the auto upgrade period for releases with security fixes (from 0 to 14 days).




###  API 

To create a Goldengate deployment, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateDeployments/DEPLOYMENT_ID"
    -d \
    '{
      "display_name": "DEPLOYMENT_NAME",
      "gcp_oracle_zone": "GCP_ORACLE_ZONE",
      "name": "projects/PROJECT_ID/locations/REGION/goldengateDeployments/DEPLOYMENT_ID",
      "odb_subnet": "projects/ODB_NETWORK_PROJECT_ID/locations/ODB_NETWORK_REGION/odbNetworks/ODB_NETWORK_ID/odbSubnets/ODB_SUBNET_ID",
      "properties": {
        "license_model": "LICENSE_TYPE",
        "environmentType": "ENVIRONMENT_TYPE",
        "isAutoScalingEnabled": "AUTOSCALING",
        "deploymentType": "DEPLOYMENT_TYPE",
        "cpuCoreCount": "CPU_CORE_COUNT",
        "oggData": {
          "deployment": "DEPLOYMENT",
          "adminUsername": "USERNAME",
          "adminPassword": "PASSWORD"
        },
          "maintenanceWindow": {
            "day": "DAY",
            "startHour": "HOUR"
         },
        "maintenanceConfig": {
          "isInterimReleaseAutoUpgradeEnabled": AUTO_UPGRADE_ENABLED,
          "interimReleaseUpgradePeriodDays": INTERIM_RELEASE_UPGRADE_PERIOD_DAYS,
          "bundleReleaseUpgradePeriodDays": BUNDLE_RELEASE_UPGRADE_PERIOD_DAYS,
          "majorReleaseUpgradePeriodDays": MAJOR_RELEASE_UPGRADE_PERIOD_DAYS,
          "securityPatchUpgradePeriodDays": SECURITY_PATCH_UPGRADE_PERIOD_DAYS
         }
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which to create the deployment.
  * REGION: the region where you want to create the deployment.
  * DEPLOYMENT_ID: a unique ID for your deployment.
  * DEPLOYMENT_NAME: a name for your deployment. This name appears in the Google Cloud console.
  * GCP_ORACLE_ZONE: the Google Cloud Oracle zone for your deployment. See [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).
  * For the `odbSubnet` property, replace the following: 
    * ODB_NETWORK_PROJECT_ID: the ID of your Google Cloud project which contains your ODB Network. If you're using a Shared VPC, then this is the ID of your host project.
    * ODB_NETWORK_REGION: the region where your ODB Network is located.
    * ODB_NETWORK_ID: the ID of your ODB Network.
    * ODB_SUBNET_ID: the ID of your ODB Subnet.
  * LICENSE_TYPE: the license type associated with your Oracle Database@Google Cloud order. The accepted values are `bring-your-own-license` or `license-included`.
  * ENVIRONMENT_TYPE: the type of the environment in which the deployment is to be used:

    * `DEVELOPMENT_OR_TESTING`: set up a deployment with the recommended defaults for a development or testing environment. The default values are as follows:

      * 1 OCPUs
      * 16 GB memory
      * 1 Gbps network bandwidth
      * 500 GB storage
    * `PRODUCTION`: set up a deployment with the recommended defaults for a production environment. The default values are as follows:

      * 4 OCPUs
      * 64 GB memory
      * 4 Gbps network bandwidth
      * 2000 GB storage
  * AUTOSCALING: let the deployment use up to three times the provisioned number of cores as the workload increases. You can increase the number of cores up to 24 cores.

  * DEPLOYMENT_TYPE: the type of deployment. Accepted values are as follows:

    * Oracle AI Database: `DATABASE_ORACLE`
    * Big Data: `BIGDATA`
    * Microsoft SQL Server: `DATABASE_MICROSOFT_SQLSERVER`
    * MySQL: `DATABASE_MYSQL`
    * PostgreSQL: `DATABASE_POSTGRESQL`
    * IBM Db2 for i:`DATABASE_DB2ZOS`
    * IBM Db2 for z/OS:`DATABASE_DB2I`
    * Data transforms: `DATA_TRANSFORMS`
  * CPU_CORE_COUNT: the number of OCPUs. You can allot between 1 and 24 OCPUs.

  * For the `oggData` property, replace the following:

    * DEPLOYMENT: a name for the instance deployment. The name must be 1 to 32 characters long, contain only alphanumeric characters.
    * USERNAME: the administrator's username.
    * PASSWORD: the administrator's password. Instead of a raw password, you can also use a secret stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

Secret Manager provides a secure storage mechanism. To use a secret, use the following property:
          
          "admin_password_secret_version": "projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID"
          

Replace the following:

      * PROJECT_ID: the Google Cloud project ID
      * SECRET_ID: the ID of the secret
      * VERSION_ID: the ID of the secret version

For example:
    
    "admin_password_secret_version": "projects/test-project/secrets/deployment-password/versions/1"
    

  * For the `maintenanceWindow` property, replace the following:

    * DAY: the day of the week on which you prefer to perform the maintenance. Accepted value is the name of the day in uppercase. For example, `MONDAY`.
    * HOUR: the time slot of the day when you want to perform the maintenance. A time slot is a four-hour slot. Accepted values are as follows:
Value | Time slot | `0` | 0:00 - 3:59 UTC  
---|---  
`4` | 4:00 - 7:59 UTC  
`8` | 8:00 - 11:59 UTC  
`12` | 12:00 - 15:59 UTC  
`16` | 16:00 - 19:59 UTC  
`20` | 20:00 - 23:59 UTC  
  * For the `maintenanceConfig`, replace the following:

    * AUTO_UPGRADE_ENABLED: enable auto upgrade for interim releases. By default, the auto upgrade is disabled.
    * INTERIM_RELEASE_UPGRADE_PERIOD_DAYS: the auto upgrade period for interim releases (from 0 to 365 days).
    * BUNDLE_RELEASE_UPGRADE_PERIOD_DAYS: the auto upgrade period for bundle releases (from 0 to 180 days).
    * MAJOR_RELEASE_UPGRADE_PERIOD_DAYS: the auto upgrade period for major releases (from 0 to 365 days).
    * SECURITY_PATCH_UPGRADE_PERIOD_DAYS: the auto upgrade period for releases with security fixes (from 0 to 14 days).



When completed, you can [view the deployment](https://docs.cloud.google.com/oracle/database/docs/manage-deployments#view-deployment-details) in the **Deployments** list as "Available". You can also [manage and modify its settings in the OCI console](https://docs.cloud.google.com/oracle/database/docs/manage-deployments#manage-deployments).

## Create a connection

To create a connection, do the following:

### gcloud

Use the `gcloud oracle-database goldengate-connections create` command to create a connection.
    
    
    gcloud oracle-database goldengate-connections create CONNECTION_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --gcp-oracle-zone=GCP_ORACLE_ZONE \
        --properties-display-name="CONNECTION_NAME" \
        --properties-description=DESCRIPTION \
        --properties-connection-type=CONNECTION_TYPE \
        --properties-routing-method=ROUTING_METHOD \
        CONNECTION_SPECIFIC_PROPERTIES
    

Replace the following:

  * CONNECTION_ID: a unique ID for your connection.
  * PROJECT_ID: the ID of your Google Cloud project in which to create the connection. If you're using a Shared VPC, then this is the ID of your host project.
  * REGION: the region where you want to create the connection.
  * CONNECTION_NAME: a name for your connection. This name appears in the Google Cloud console.
  * GCP_ORACLE_ZONE: the Google Cloud Oracle zone for your connection. See [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).
  * DESCRIPTION: a description for your connection.
  * CONNECTION_TYPE: the type of connection that corresponds to your deployment. Accepted values are as follows:

    * `ORACLE`
    * `GOLDENGATE`
    * `GENERIC`
    * `GOOGLE_CLOUD_STORAGE`
    * `GOOGLE_BIGQUERY`
    * `MYSQL`
    * `KAFKA`
    * `KAFKA_SCHEMA_REGISTRY`
    * `OCI_OBJECT_STORAGE`
    * `AZURE_DATA_LAKE_STORAGE`
    * `AZURE_SYNAPSE_ANALYTICS`
    * `POSTGRESQL`
    * `MICROSOFT_SQLSERVER`
    * `AMAZON_S3`
    * `HDFS`
    * `JAVA_MESSAGE_SERVICE`
    * `MONGODB`
    * `ORACLE_NOSQL`
    * `SNOWFLAKE`
    * `AMAZON_REDSHIFT`
    * `ELASTICSEARCH`
    * `AMAZON_KINESIS`
    * `DB2`
    * `REDIS`
    * `DATABRICKS`
    * `GOOGLE_PUBSUB`
    * `MICROSOFT_FABRIC`
    * `ORACLE_AI_DATA_PLATFORM`
    * `ICEBERG`
  * ROUTING_METHOD: the routing method to be used for network traffic:

    * `SHARED_DEPLOYMENT_ENDPOINT`: the network traffic flows from the assigned deployment's private endpoint through the deployment's subnet. This is the default routing method.
    * `DEDICATED_ENDPOINT`: the network traffic flows through a dedicated endpoint in the assigned subnet in your virtual cloud network (VCN). To allow connectivity from this connection's ingress IP addresses, you need a `subnetId`.
  * CONNECTION_SPECIFIC_PROPERTIES: based on the type of connection, you need to set additional properties, as described in the following table. When providing input, consider the following:

    * For connection-specific properties that require a file as input, such as service account key files and certificates, make sure that the file has Base64 encoding.
    * Instead of a raw password, you can also use a secret stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview). Secret Manager provides a secure storage mechanism.

To provide a secret, use the following format:
          
          "projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID"
          

Replace the following:

      * PROJECT_ID: the Google Cloud project ID
      * SECRET_ID: the ID of the secret
      * VERSION_ID: the ID of the secret version

For example:
    
    "projects/test-project/secrets/deployment-password/versions/1"
    

Connection type | Attributes  
---|---  
`ORACLE` | 
    
    technologyType
      username
      password
      authenticationMode
      connectionString
      databaseId
      sessionMode
        
  
`GOLDENGATE` | 
    
    technologyType
      username
      password
      host
      port
      gcpOracleGoldengateDeploymentId
        
  
`GENERIC` | 
    
    technologyType
      host
        
  
`GOOGLE_CLOUD_STORAGE` | 
    
    technologyType
      serviceAccountKeyFile
        
  
`GOOGLE_BIGQUERY` | 
    
    technologyType
      serviceAccountKeyFile
        
  
`MYSQL` | 
    
    technologyType
      username
      password
      securityProtocol
      databaseName
      sslCa
      sslCrl
      sslCert
      sslKey
      sslMode
      host
      port
      dbSystemId
        
  
`KAFKA` | 
    
    technologyType
      username
      password
      trustStore
      trustStorePassword
      keyStore
      keyStorePassword
      sslKeyPassword
      streamPoolId
      clusterId
      bootstrapServers
      securityProtocol
      shouldUseResourcePrincipal
        
  
`KAFKA_SCHEMA_REGISTRY` | 
    
    technologyType
      username
      password
      url
      authenticationType
      trustStore
      trustStorePassword
      keyStore
      keyStorePassword
      sslKeyPassword
        
  
`OCI_OBJECT_STORAGE` | 
    
    technologyType
      privateKeyFile
      privateKeyPassphrase
      tenancyId
      region
      userId
      publicKeyFingerprint
      shouldUseResourcePrincipal
        
  
`AZURE_DATA_LAKE_STORAGE` | 
    
    technologyType
      accountName
      authenticationType
      accountKey
      sasToken
      clientSecret
      azureTenantId
      clientId
      endpoint
      azureAuthorityHost
        
  
`AZURE_SYNAPSE_ANALYTICS` | 
    
    technologyType
      username
      password
      connectionString
        
  
`POSTGRESQL` | 
    
    technologyType
      username
      password
      databaseName
      securityProtocol
      sslCa
      sslCrl
      sslCert
      sslKey
      sslMode
      dbSystemId
        
  
`MICROSOFT_SQLSERVER` | 
    
    technologyType
      username
      password
      databaseName
      host
      port
      securityProtocol
      sslCa
        
  
`AMAZON_S3` | 
    
    technologyType
      accessKeyId
      secretAccessKey
      endpoint
      region
        
  
`HDFS` | 
    
    technologyType
      coreSiteXml
        
  
`JAVA_MESSAGE_SERVICE` | 
    
    technologyType
      username
      password
      shouldUseJndi
      jndiSecurityCredentials
      trustStore
      trustStorePassword
      keyStore
      keyStorePassword
      sslKeyPassword
      jndiConnectionFactory
      jndiProviderUrl
      jndiInitialContextFactory
      jndiSecurityPrincipal
      connectionUrl
      connectionFactory
      securityProtocol
      authenticationType
        
  
`MONGODB` | 
    
    technologyType
      username
      tlsCaFile
      tlsCertificateKeyFile
      tlsCertificateKeyFilePassword
      connectionString
      databaseId
      securityProtocol
        
  
`ORACLE_NOSQL` | 
    
    technologyType
      privateKeyFile
      privateKeyPassphrase
      tenancyId
      region
      userId
      publicKeyFingerprint
      shouldUseResourcePrincipal
        
  
`SNOWFLAKE` | 
    
    technologyType
      username
      password
      connectionUrl
      authenticationType
      privateKeyFile
      privateKeyPassphrase
        
  
`AMAZON_REDSHIFT` | 
    
    technologyType
      username
      password
      connectionUrl
        
  
`ELASTICSEARCH` | 
    
    technologyType
      username
      password
      servers
      securityProtocol
      authenticationType
      fingerprint
        
  
`AMAZON_KINESIS` | 
    
    technologyType
      accessKeyId
      secretAccessKey
      endpoint
      region
        
  
`DB2` | 
    
    technologyType
      username
      password
      host
      port
      databaseName
      securityProtocol
      sslClientKeystoredb
      sslClientKeystash
      sslServerCertificate
        
  
`REDIS` | 
    
    technologyType
      username
      password
      servers
      securityProtocol
      authenticationType
      trustStore
      trustStorePassword
      keyStore
      keyStorePassword
      redisClusterId
        
  
`DATABRICKS` | 
    
    technologyType
      password
      authenticationType
      connectionUrl
      clientSecret
      clientId
      storageCredentialName
        
  
`GOOGLE_PUBSUB` | 
    
    technologyType
      serviceAccountKeyFile
        
  
`MICROSOFT_FABRIC` | 
    
    technologyType
      tenantId
      clientId
      clientSecret
      endpoint
        
  
`ORACLE_AI_DATA_PLATFORM` | 
    
    technologyType
      connectionUrl
      privateKeyFile
      privateKeyPassphrase
      tenancyId
      region
      userId
      publicKeyFingerprint
      shouldUseResourcePrincipal
        
  
`ICEBERG` | 
    
    technologyType
      catalog
      storage
      secretAccessKey (S3)
      serviceAccountKeyFile (GCS)
      accountKey (Azure)
        
  
For more information about these properties, see [Oracle Database@Google Cloud gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/oracle-database).




###  API 

To create a connection, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnections/CONNECTION_ID"
    -d \
    '{
      "gcp_oracle_zone": "GCP_ORACLE_ZONE",
      "name": "projects/PROJECT_ID/locations/REGION/goldengateConnections/CONNECTION_ID",
      "properties": {
        "display_name": "CONNECTION_NAME",
        "description": "DESCRIPTION",
        "connectionType": "CONNECTION_TYPE",
        "routingMethod": "ROUTING_METHOD",
        "CONNECTION_SPECIFIC_PROPERTIES"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which to create the connection.
  * REGION: the region where you want to create the connection.
  * CONNECTION_ID: a unique ID for your connection.
  * GCP_ORACLE_ZONE: the Google Cloud Oracle zone for your connection. See [Supported regions and zones](https://docs.cloud.google.com/oracle/database/docs/regions-and-zones).
  * CONNECTION_NAME: a name for your connection. This name appears in the Google Cloud console.
  * DESCRIPTION: a description for your connection.
  * CONNECTION_TYPE: the type of connection that corresponds to your deployment. Accepted values are as follows:

    * `ORACLE`
    * `GOLDENGATE`
    * `GENERIC`
    * `GOOGLE_CLOUD_STORAGE`
    * `GOOGLE_BIGQUERY`
    * `MYSQL`
    * `KAFKA`
    * `KAFKA_SCHEMA_REGISTRY`
    * `OCI_OBJECT_STORAGE`
    * `AZURE_DATA_LAKE_STORAGE`
    * `AZURE_SYNAPSE_ANALYTICS`
    * `POSTGRESQL`
    * `MICROSOFT_SQLSERVER`
    * `AMAZON_S3`
    * `HDFS`
    * `JAVA_MESSAGE_SERVICE`
    * `MONGODB`
    * `ORACLE_NOSQL`
    * `SNOWFLAKE`
    * `AMAZON_REDSHIFT`
    * `ELASTICSEARCH`
    * `AMAZON_KINESIS`
    * `DB2`
    * `REDIS`
    * `DATABRICKS`
    * `GOOGLE_PUBSUB`
    * `MICROSOFT_FABRIC`
    * `ORACLE_AI_DATA_PLATFORM`
    * `ICEBERG`
  * ROUTING_METHOD: the routing method to be used for network traffic:

    * `SHARED_DEPLOYMENT_ENDPOINT`: the network traffic flows from the assigned deployment's private endpoint through the deployment's subnet. This is the default routing method.
    * `DEDICATED_ENDPOINT`: the network traffic flows through a dedicated endpoint in the assigned subnet in your virtual cloud network (VCN). To allow connectivity from this connection's ingress IP addresses, you need a `subnetId`.
  * CONNECTION_SPECIFIC_PROPERTIES: based on the type of connection, you need to set additional properties, as described in the following table. When providing input, consider the following:

    * For connection-specific properties that require a file as input, such as service account key files and certificates, make sure that the file has Base64 encoding.
    * Instead of a raw password, you can also use a secret stored in [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview). Secret Manager provides a secure storage mechanism.

To provide a secret, use the following format:
          
          "projects/PROJECT_ID/secrets/SECRET_ID/versions/VERSION_ID"
          

Replace the following:

      * PROJECT_ID: the Google Cloud project ID
      * SECRET_ID: the ID of the secret
      * VERSION_ID: the ID of the secret version

For example:
    
    "projects/test-project/secrets/deployment-password/versions/1"
    

Connection type | Attributes  
---|---  
`ORACLE`  
  
`oracleConnectionProperties` | 
    
    technologyType
      username
      password
      authenticationMode
      connectionString
      databaseId
      sessionMode
        
  
`GOLDENGATE`  
  
`goldengateConnectionProperties` | 
    
    technologyType
      username
      password
      host
      port
      gcpOracleGoldengateDeploymentId
        
  
`GENERIC`  
  
`genericConnectionProperties` | 
    
    technologyType
      host
        
  
`GOOGLE_CLOUD_STORAGE`  
  
`googleCloudStorageConnectionProperties` | 
    
    technologyType
      serviceAccountKeyFile
        
  
`GOOGLE_BIGQUERY`  
  
`googleBigQueryConnectionProperties` | 
    
    technologyType
      serviceAccountKeyFile
        
  
`MYSQL`  
  
`mysqlConnectionProperties` | 
    
    technologyType
      username
      password
      securityProtocol
      databaseName
      sslCa
      sslCrl
      sslCert
      sslKey
      sslMode
      host
      port
      dbSystemId
        
  
`KAFKA`  
  
`kafkaConnectionProperties` | 
    
    technologyType
      username
      password
      trustStore
      trustStorePassword
      keyStore
      keyStorePassword
      sslKeyPassword
      streamPoolId
      clusterId
      bootstrapServers
      securityProtocol
      shouldUseResourcePrincipal
        
  
`KAFKA_SCHEMA_REGISTRY`  
  
`kafkaSchemaRegistryConnectionProperties` | 
    
    technologyType
      username
      password
      url
      authenticationType
      trustStore
      trustStorePassword
      keyStore
      keyStorePassword
      sslKeyPassword
        
  
`OCI_OBJECT_STORAGE`  
  
`ociObjectStorageConnectionProperties` | 
    
    technologyType
      privateKeyFile
      privateKeyPassphrase
      tenancyId
      region
      userId
      publicKeyFingerprint
      shouldUseResourcePrincipal
        
  
`AZURE_DATA_LAKE_STORAGE`  
  
`azureDataLakeStorageConnectionProperties` | 
    
    technologyType
      accountName
      authenticationType
      accountKey
      sasToken
      clientSecret
      azureTenantId
      clientId
      endpoint
      azureAuthorityHost
        
  
`AZURE_SYNAPSE_ANALYTICS`  
  
`azureSynapseAnalyticsConnectionProperties` | 
    
    technologyType
      username
      password
      connectionString
        
  
`POSTGRESQL`  
  
`postgresqlConnectionProperties` | 
    
    technologyType
      username
      password
      databaseName
      securityProtocol
      sslCa
      sslCrl
      sslCert
      sslKey
      sslMode
      dbSystemId
        
  
`MICROSOFT_SQLSERVER`  
  
`microsoftSqlserverConnectionProperties` | 
    
    technologyType
      username
      password
      databaseName
      host
      port
      securityProtocol
      sslCa
        
  
`AMAZON_S3`  
  
`amazonS3ConnectionProperties` | 
    
    technologyType
      accessKeyId
      secretAccessKey
      endpoint
      region
        
  
`HDFS`  
  
`hdfsConnectionProperties` | 
    
    technologyType
      coreSiteXml
        
  
`JAVA_MESSAGE_SERVICE`  
  
`javaMessageServiceConnectionProperties` | 
    
    technologyType
      username
      password
      shouldUseJndi
      jndiSecurityCredentials
      trustStore
      trustStorePassword
      keyStore
      keyStorePassword
      sslKeyPassword
      jndiConnectionFactory
      jndiProviderUrl
      jndiInitialContextFactory
      jndiSecurityPrincipal
      connectionUrl
      connectionFactory
      securityProtocol
      authenticationType
        
  
`MONGODB`  
  
`mongodbConnectionProperties` | 
    
    technologyType
      username
      tlsCaFile
      tlsCertificateKeyFile
      tlsCertificateKeyFilePassword
      connectionString
      databaseId
      securityProtocol
        
  
`ORACLE_NOSQL`  
  
`oracleNosqlConnectionProperties` | 
    
    technologyType
      privateKeyFile
      privateKeyPassphrase
      tenancyId
      region
      userId
      publicKeyFingerprint
      shouldUseResourcePrincipal
        
  
`SNOWFLAKE`  
  
`snowflakeConnectionProperties` | 
    
    technologyType
      username
      password
      connectionUrl
      authenticationType
      privateKeyFile
      privateKeyPassphrase
        
  
`AMAZON_REDSHIFT`  
  
`amazonRedshiftConnectionProperties` | 
    
    technologyType
      username
      password
      connectionUrl
        
  
`ELASTICSEARCH`  
  
`elasticsearchConnectionProperties` | 
    
    technologyType
      username
      password
      servers
      securityProtocol
      authenticationType
      fingerprint
        
  
`AMAZON_KINESIS`  
  
`amazonKinesisConnectionProperties` | 
    
    technologyType
      accessKeyId
      secretAccessKey
      endpoint
      region
        
  
`DB2`  
  
`db2ConnectionProperties` | 
    
    technologyType
      username
      password
      host
      port
      databaseName
      securityProtocol
      sslClientKeystoredb
      sslClientKeystash
      sslServerCertificate
        
  
`REDIS`  
  
`redisConnectionProperties` | 
    
    technologyType
      username
      password
      servers
      securityProtocol
      authenticationType
      trustStore
      trustStorePassword
      keyStore
      keyStorePassword
      redisClusterId
        
  
`DATABRICKS`  
  
`databricksConnectionProperties` | 
    
    technologyType
      password
      authenticationType
      connectionUrl
      clientSecret
      clientId
      storageCredentialName
        
  
`GOOGLE_PUBSUB`  
  
`googlePubsubConnectionProperties` | 
    
    technologyType
      serviceAccountKeyFile
        
  
`MICROSOFT_FABRIC`  
  
`microsoftFabricConnectionProperties` | 
    
    technologyType
      tenantId
      clientId
      clientSecret
      endpoint
        
  
`ORACLE_AI_DATA_PLATFORM`  
  
`oracleAiDataPlatformConnectionProperties` | 
    
    technologyType
      connectionUrl
      privateKeyFile
      privateKeyPassphrase
      tenancyId
      region
      userId
      publicKeyFingerprint
      shouldUseResourcePrincipal
        
  
`ICEBERG`  
  
`icebergConnectionProperties` | 
    
    technologyType
      catalog
      storage
      secretAccessKey (S3)
      serviceAccountKeyFile (GCS)
      accountKey (Azure)
        
  
For more information about these properties, see [Oracle Database@Google Cloud API reference](https://docs.cloud.google.com/oracle/database/docs/apis).




When completed, you can [view the connection](https://docs.cloud.google.com/oracle/database/docs/manage-connections#view-connection-details) in the **Connections** list as "Available". Also, after creating a connection in Google Cloud, you can [manage and modify its settings in the OCI console](https://docs.cloud.google.com/oracle/database/docs/manage-connections#manage-connections).

## Create a connection assignment

After your connection becomes available, you must assign the connection to your deployment. You can assign multiple connections to a deployment. Also, you can assign a connection to multiple deployments.

To create a connection assignment, do the following:

### gcloud

Use the `gcloud oracle-database goldengate-connection-assignments create` command to create a deployment.
    
    
    gcloud oracle-database goldengate-connection-assignments create ASSIGNMENT_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --display-name="ASSIGNMENT_NAME" \
        --properties-goldengate-connection=projects/PROJECT_ID/locations/REGION/goldengateConnections/CONNECTION_ID \
        --properties-goldengate-deployment=projects/PROJECT_ID/locations/REGION/goldengateDeployments/DEPLOYMENT_ID
    

Replace the following:

  * ASSIGNMENT_ID: a unique ID for your connection assignment.
  * PROJECT_ID: the ID of your Google Cloud project in which to create the connection assignment.
  * REGION: the region in which to create the connection assignment.
  * ASSIGNMENT_NAME: a name for your connection assignment. This name appears in the Google Cloud console.
  * For the `--properties-goldengate-connection`, replace the following: 
    * PROJECT_ID: the ID of the project that contains your connection.
    * REGION: the region where your connection is located.
    * CONNECTION_ID: the ID of your connection.
  * For the `--properties-goldengate-deployment`, replace the following: 
    * PROJECT_ID: the ID of the project that contains the deployment.
    * REGION: the region where your deployment is located.
    * DEPLOYMENT_ID: the ID of your deployment.



###  API 

To create a connection assignment, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnectionAssignments/ASSIGNMENT_ID"
    -d \
    '{
      "display_name": "ASSIGNMENT_NAME",
      "properties": {
        "goldengate_connection": "projects/PROJECT_ID/locations/REGION/goldengateConnections/CONNECTION_ID",
        "goldengate_deployment": "projects/PROJECT_ID/locations/REGION/goldengateDeployments/DEPLOYMENT_ID"
       }
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project in which to create the connection assignment.
  * REGION: the region in which to create the connection assignment.
  * ASSIGNMENT_ID: a unique ID for your connection assignment.
  * ASSIGNMENT_NAME: a name for your connection assignment. This name appears in the Google Cloud console.
  * For the `goldengate_connection` property, replace the following: 
    * PROJECT_ID: the ID of the project that contains your connection.
    * REGION: the region where your connection is located.
    * CONNECTION_ID: the ID of your connection.
  * For the `goldengate_deployment` property, replace the following: 
    * PROJECT_ID: the ID of the project that contains the deployment.
    * REGION: the region where your deployment is located.
    * DEPLOYMENT_ID: the ID of your deployment.



## Test the connection assignment

After creating the connection assignment, test it to make sure that your connection works.

### gcloud

Use the `gcloud oracle-database goldengate-connection-assignments test` command to test a connection assignment.
    
    
    gcloud oracle-database goldengate-connection-assignments test ASSIGNMENT_ID \
        --project=PROJECT_ID \
        --location=REGION \
        --type="TYPE"
    

Replace the following:

  * ASSIGNMENT_ID: the ID of your connection assignment.
  * PROJECT_ID: the ID of your Google Cloud project.
  * REGION: the region where your connection assignment is located.
  * TYPE: the type of your connection assignment.



###  API 

To test a connection assignment, run the following `curl` command:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://oracledatabase.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/goldengateConnectionAssignments/ASSIGNMENT_ID:test"
    -d \
    '{
      "type": "TYPE",
    }'
    

Replace the following:

  * PROJECT_ID: the ID of your project which contains the connection assignment.
  * REGION: the region where your connection assignment is located
  * ASSIGNMENT_ID: the ID of your connection assignment
  * TYPE: the type of your connection assignment



## Use extracts, replicats, and data transforms

After you create a deployment and connect to it, you can run extract and replicat processes, and data transforms. For more information, see [Oracle documentation: Basic Goldengate taskflows](https://docs.oracle.com/en/cloud/paas/goldengate-service/pmzge/#articletitle).

## What's next

  * Learn how to [manage your Goldengate deployments](https://docs.cloud.google.com/oracle/database/docs/manage-deployments).
  * Learn how to [manage your Goldengate connections](https://docs.cloud.google.com/oracle/database/docs/manage-connections).
  * Learn how to [manage your Goldengate connection assignments](https://docs.cloud.google.com/oracle/database/docs/manage-assignments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
