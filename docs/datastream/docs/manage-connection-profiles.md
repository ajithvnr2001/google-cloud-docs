---
url: https://docs.cloud.google.com/datastream/docs/manage-connection-profiles/
title: Manage connection profiles \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:54.481925+00:00
---

# Manage connection profiles  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/manage-connection-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Manage connection profiles Stay organized with collections  Save and categorize content based on your preferences. 

In this page, you learn how to use the Datastream API to:

  * Create connection profiles for a source Oracle database, a source MySQL database, a source PostgreSQL database, a source Salesforce org, a BigQuery destination, and a Cloud Storage destination
  * Retrieve information about, update, and delete connection profiles
  * Discover the structure of source or destination connection profiles



There are two ways that you can use the Datastream API. You can make REST API calls or you can use the Google Cloud CLI (CLI).

For high-level information about using `gcloud` to manage Datastream connection profiles, click [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles).

Refer to the [Using Datastream APIs](https://docs.cloud.google.com/datastream/docs/using-datastream-apis) tutorial to see an end-to-end walkthrough of how to use Datastream's APIs to create and manage connection profiles.

## Create a connection profile for a source Oracle database

The following code shows a request to create a connection profile for an Oracle database using a secret and the IP allowlist connectivity method.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "[connection-profile-display-name]",
      "oracleProfile": {
        "hostname": "HOST_ID_ADDRESS",
        "port": PORT,
        "username": "USERNAME",
        "databaseService": "DATABASE",
        "secretManagerStoredPassword": "SECRET_MANAGER_RESOURCE"
      },
      "staticServiceIpConnectivity": {}
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=myOracleCP
    {
      "displayName": "my Oracle database",
      "oracleProfile": {
        "hostname": "1.2.3.4",
        "port": 1521,
        "username": "admin",
        "databaseService": "ORCL",
        "secretManagerStoredPassword": "projects/myProjectId/secrets/mySecret/versions/latest"
      },
      "staticServiceIpConnectivity": {}
    }

The following code shows a request to create a connection profile for an Oracle database, and specifies the connectivity method as private connectivity (VPC peering).

This method establishes secure connectivity between Datastream and the source database (internally within Google Cloud, or with external sources connected over VPN or Interconnect). This communication happens through a VPC peering connection.
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "[connection-profile-display-name]",
      "oracleProfile": {
        "hostname": "HOST_ID_ADDRESS",
        "port": PORT,
        "username": "USERNAME",
        "password": "PASSWORD",
        "databaseService": "DATABASE"
      },
      "privateConnectivity": {
        "privateConnection": "projects/PROJECT_ID/locations/
        LOCATION/privateConnections/[private-connectivity-configuration-id]"
      }
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=myOracleVPCPeeringCP
    {
      "displayName": "my Oracle database",
      "oracleProfile": {
        "hostname": "1.2.3.4",
        "port": 1521,
        "username": "admin",
        "password": "12345",
        "databaseService": "ORCL",
      },
        "privateConnectivity": {
          "privateConnection": "projects/myProjectId/locations/us-central1/
          privateConnections/myPrivateConnection"
        }
    }

After the connection profile is created, you can view information about it by calling the `connectionProfiles/get` method. Your output appears, similar to the following:
    
    
    {
      "name": "projects/projectId/location/us-central1/connectionProfiles/myOracleVPCPeeringCP",
      "createTime": "2019-12-22T16:17:37.159786963Z",
      "updateTime": "2019-12-22T16:17:37.159786963Z",
      "displayName": "my Oracle database",
      "oracleProfile": {
        "hostname": "1.2.3.4",
        "port": 1521,
        "databaseService": "ORCL",
        "username": "admin"
      },
      "privateConnectivity": {
        "privateConnection": "projects/myProjectId/locations/us-central1/
        privateConnections/myPrivateConnection"
      }
    }

### gcloud

For more information about using `gcloud` to create a connection profile for a source Oracle database, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

## Create a connection profile for a source MySQL database

The following code shows a request to create a connection profile for a MySQL database, and specifies the connectivity method as using static IP addresses (IP allowlist).

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "[connection-profile-display-name]",
      "mysqlProfile": {
        "hostname": "HOST_ID_ADDRESS",
        "port": PORT,
        "username": "USERNAME",
        "password": "PASSWORD"
      },
      "staticServiceIpConnectivity": {}
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=mysql-cp
    {
      "displayName": "my MySQL database",
      "mysqlProfile": {
        "hostname": "1.2.3.4",
        "port": 3306,
        "username": "root",
        "password": "12345"
      },
      "staticServiceIpConnectivity": {}
    }

### gcloud

For more information about using `gcloud` to create a connection profile for a source MySQL database, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

## Create a connection profile for a source PostgreSQL database

The following code shows a request to create a connection profile for a PostgreSQL database.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "[connection-profile-display-name]",
      "postgresqlProfile": {
        "hostname": "HOST_ID_ADDRESS",
        "port": PORT,
        "username": "USERNAME",
        "password": "PASSWORD",
        "database": "DATABASE"
      },
      "staticServiceIpConnectivity": {}
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=postgres-cp
    {
      "displayName": "my PostgreSQL database",
      "postgresqlProfile": {
        "hostname": "1.2.3.4",
        "database": "postgres",
        "port": 5432,
        "username": "root",
        "password": "12345"
      },
      "staticServiceIpConnectivity": {}
    }

### gcloud

For more information about using `gcloud` to create connection profiles, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

## Create a connection profile for a source SQL Server database

The following code shows a request to create a connection profile for a SQL Server database, and specifies the connectivity method as using static IP addresses (IP allowlist).

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "[connection-profile-display-name]",
      "sqlserverProfile": {
        "hostname": "HOST_ID_ADDRESS",
        "port": PORT,
        "username": "USERNAME",
        "password": "PASSWORD",
        "database": "DATABASE"
      },
      "staticServiceIpConnectivity": {}
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=sqlserver-cp
    {
      "displayName": "my SQL Server database",
      "sqlserverProfile": {
        "hostname": "1.2.3.4",
        "port": 1433,
        "username": "root",
        "password": "12345"
        "database": "database1"
      },
      "staticServiceIpConnectivity": {}
    }

### gcloud

For more information about using `gcloud` to create connection profiles, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

## Create a connection profile for a Salesforce source

The following code shows a request to create a connection profile for a source Salesforce instance using a username and a password as the authentication method.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "CONNECTION_PROFILE_NAME",
      "salesforceProfile": {
        "domain": "DOMAIN_NAME",
        "userCredentials": {
          "username": "USERNAME",
          "password": "PASSWORD",
          "securitytoken": "SECURITY_TOKEN"
        }
      }
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=saleforce-cp
    {
      "displayName": "My Salesforce connection profile",
      "salesforceProfile": {
        "domain": "domain.my.salesforce.com",
        "userCredentials": {
          "username": "mySalesforceUser",
          "password": "12345",
          "securitytoken": "C08120F510542FFB1C3640F57AF19E2D5D700556A25F7D665C3B428407709D8C"
        }
      }
    }
      

### gcloud

For more information about using `gcloud` to create connection profiles, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

The following code shows a request to create a connection profile for a source Salesforce instance using OAuth 2.0 client credentials as the authentication method.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "CONNECTION_PROFILE_NAME",
      "salesforceProfile": {
        "domain": "DOMAIN_NAME",
        "oauth2ClientCredentials": {
          "clientId": "CLIENT_ID",
          "clientSecret": "CLIENT_SECRET"
        }
      }
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=saleforce-cp
    {
      "displayName": "My Salesforce connection profile",
      "salesforceProfile": {
        "domain": "domain.my.salesforce.com",
        "oauth2ClientCredentials": {
          "clientId": "myClientId",
          "clientSecret": "projects/myProject/secrets/sf-client-secret"
        }
      }
    }
      

### gcloud

For more information about using `gcloud` to create connection profiles, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

## Create a connection profile for a MongoDB source

The following code shows a request to create a connection profile for a source MongoDB instance using an SRV connection string format.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "CONNECTION_PROFILE_NAME",
      "mongodbProfile": {
        "hostAddresses": [ {
          "hostname": "HOST_URI"
        } ],
        "username": "USERNAME",
        "password": "PASSWORD",
        "srvConnectionFormat": {}
        },
        "staticServiceIpConnectivity": {}
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=mongodb-cp
    {
      "displayName": "mongodb-cp",
      "mongodbProfile": {
        "hostAddresses": [ {
          "hostname": "cluster85828.ebeek.mongodb.net"
        } ],
        "username": "Cluster85828",
        "password": "password",
        "srvConnectionFormat": {}
        },
        "staticServiceIpConnectivity": {}
    }
      

### gcloud

For more information about using `gcloud` to create connection profiles, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

The following code shows a request to create a connection profile for a source MongoDB instance using a standard connection string format.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "CONNECTION_PROFILE_NAME",
      "mongodbProfile": {
        "hostAddresses": [ {
          "hostname": "HOST_IP",
          "port": "PORT_NUMBER"
        } ],
        "replica_set": "SET_ID",
        "username": "USERNAME",
        "password": "PASSWORD",
        "standardConnectionFormat": {
          "directConnection": false
        }
      },
      "staticServiceIpConnectivity": {}
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=mongodb-cp
    {
      "displayName": "mongodb-cp",
      "mongodbProfile": {
        "hostAddresses": [ {
          "hostname": "34.19.10.194",
          "port": "27017"
        } ],
        "replicaset": "rs0",
        "username": "root",
        "password": "password",
        "standardConnectionFormat": {
          "directConnection": false
        }
      },
      "staticServiceIpConnectivity": {}
    }
      

### gcloud

For more information about using `gcloud` to create connection profiles, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

## Create a connection profile for a BigQuery destination

The following code shows a request to create a connection profile for a BigQuery destination.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/[project-id/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "connection-profile-display-name",
      "bigqueryProfile": {}
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=myBigqueryCP
    {
      "displayName": "my BigQuery destination",
      "bigqueryProfile": {}
    }

### gcloud

For more information about using `gcloud` to create a connection profiles, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

## Create a connection profile for a Cloud Storage destination

The following code shows a request to create a connection profile for a Cloud Storage bucket. Because Cloud Storage is in the same network as Datastream, no special connectivity is required. Therefore, no connectivity method is specified.

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/[project-id/locations/
    LOCATION/connectionProfiles?connectionProfileId=CONNECTION_PROFILE_ID
    {
      "displayName": "connection-profile-display-name",
      "gcsProfile": {
        "bucket": "bucket-name",
        "rootPath": "prefix-inside-bucket"
      }
    }

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles?connectionProfileId=myGcsCP
    {
      "displayName": "my Cloud Storage bucket",
      "gcsProfile": {
        "bucket": "myBucket",
        "rootPath": "prefix-inside-bucket"
      }
    }

### gcloud

For more information about using `gcloud` to create a connection profile for Cloud Storage, see [Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create).

## Get information about a connection profile

The following code shows a request to retrieve information about a connection profile for a source Oracle database, a source MySQL database, a BigQuery destination, or a Cloud Storage destination that has been created.

### REST
    
    
    GET https://datastream.googleapis.com/v1/projects/project-id/locations/
    LOCATION/connectionProfiles/CONNECTION_PROFILE_ID

For example:
    
    
    GET https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles/myOracleCP

### gcloud

For more information about using `gcloud` to retrieve information about your connection profile, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/describe).

## List connection profiles

The following code shows a request to retrieve information about all of your connection profiles.

### REST
    
    
    GET https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles

### gcloud

For more information about using `gcloud` to retrieve information about all of your connection profiles, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/list).

## Update a connection profile

The following code shows a request to change the username and password of an existing connection profile for a source database.

By using the `updateMask` parameter in the request, only the fields that you specify have to be included in the body of the request (for this example, the `username` and `password` fields, represented by the `oracle_profile.username` and `oracle_profile.password` flags, respectively).

Updating a connection profile propagates all changes to any streams using it automatically.

### REST
    
    
    PATCH https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles/CONNECTION_PROFILE_ID?
    updateMask=oracle_profile.username,oracle_profile.password
    {
      "oracleProfile": {
        "username": "USERNAME",
        "password": "PASSWORD"
      }
    }

For example:
    
    
    PATCH https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles/myOracleCP?
    updateMask=oracle_profile.username,oracle_profile.password
    {
      "oracleProfile": {
        "username": "username",
        "password": "password"
      }
    }

The following code shows a request to change the private connectivity configuration that's assigned to a connection profile. This connection profile uses the VPC peering network connectivity method.

For this example, you're assigning the `new_private_connection` configuration to the connection profile.

You'd assign a different private connectivity configuration to a connection profile in case you want to delete the existing configuration.

Also, before associating a private connectivity configuration with a connection profile, make sure that it was created successfully (that is, it has the `CREATED` state).

For more information about the states of a private connectivity configuration, see [Create a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/manage-private-connectivity-configurations#create-a-private-connectivity-configuration). 
    
    
    PATCH -d {\"private_connectivity\":{\"private_connection\":\
    "projects/PROJECT_ID/locations/LOCATION/privateConnections/
    new_private_connection\"}}" -H "Authorization: Bearer $TOKEN" -H 
    "Content-Type: application/json" https://datastream.googleapis.com/v1/
    projects/PROJECT_ID/locations/LOCATION/connectionProfiles/
    CONNECTION_PROFILE_ID?update_mask=private_connectivity.private_connection

For example:
    
    
    PATCH -d {\"private_connectivity\":{\"private_connection\":\
    "projects/myProjectId/locations/us-central1/privateConnections/
    new_private_connection\"}}" -H "Authorization: Bearer $TOKEN" -H 
    "Content-Type: application/json"
    https://datastream.googleapis.com/v1/projects/
    myProjectId/locations/us-central1/connectionProfiles/
    myOracleVPCPeeringCP?update_mask=private_connectivity.private_connection

### gcloud

For more information about using `gcloud` to update your connection profile, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update).

## Delete a connection profile

The following code shows a request to delete a connection profile. After the connection profile is deleted, any streams using it will fail.

### REST
    
    
    DELETE https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles/CONNECTION_PROFILE_ID

For example:
    
    
    DELETE https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles/myOracleCP

### gcloud

For more information about using `gcloud` to delete your connection profile, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/delete).

## Discover the structure of a source database

Use the `discoverConnectionProfile` API to retrieve the list of entities (for example, schemas and tables) from a source, and the metadata associated with the entities.

The API can receive as a parameter either an ID of an existing connection profile or a complete connection profile object definition. The function can return a single level (for example, all schemas in a database or all tables in a schema), or all entities recursively (for example, schemas, tables, and columns).

### REST
    
    
    POST https://datastream.googleapis.com/v1/projects/PROJECT_ID/locations/
    LOCATION/connectionProfiles:discoverConnectionProfile?CONNECTION_PROFILE_ID

For example:
    
    
    POST https://datastream.googleapis.com/v1/projects/myProjectId/locations/
    us-central1/connectionProfiles:discoverConnectionProfile?myOracleCP

### gcloud

For more information about using `gcloud` to discover the structure of your source database, see [Google Cloud SDK documentation](https://docs.cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/discover).

## What's next

  * Learn how to [use the Datastream API to manage streams](https://docs.cloud.google.com/datastream/docs/manage-streams).
  * Learn how to [use the Datastream API to manage private connectivity configurations](https://docs.cloud.google.com/datastream/docs/manage-private-connectivity-configurations).
  * For more information about using the Datastream API, see the [reference documentation](https://docs.cloud.google.com/datastream/docs/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
