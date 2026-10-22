---
url: https://docs.cloud.google.com/datastream/docs/using-datastream-apis/
title: Using Datastream APIs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:02.194005+00:00
---

# Using Datastream APIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/using-datastream-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Using Datastream APIs Stay organized with collections  Save and categorize content based on your preferences. 

Datastream

For businesses with many isolated data sources, access to enterprise data across the organization, especially in a real-time manner, can be difficult. This results in a world of limited and slow data access, preventing the organization's ability to introspect.

Datastream provides near real-time access to change data from a variety of on-premises and cloud-based data sources to create access to organizational data. Datastream provides a unified consumption API which democratizes the organization's access to the freshest enterprise data available across the organization, powering integrated near real-time scenarios.

One such scenario is transferring data from a source database into a Cloud-based storage service or messaging queue and transforming this data into a form that's readable by other applications and services that communicate with this storage service or messaging queue.

In this tutorial, you learn how to use Datastream to transfer schemas, tables, and data from a source Oracle database into a folder in a [Cloud Storage](https://cloud.google.com/storage) bucket. Cloud Storage is a web service for storing and accessing data on Google Cloud. The service combines the performance and scalability of Google's cloud with advanced security and sharing capabilities.

As part of transferring this information into a folder in the destination Cloud Storage bucket, Datastream translates this information into Avro. Avro is defined by a schema that's written in JavaScript Object Notation (JSON). Doing this translation lets you read data across different data sources in a uniform way.

## Objectives

In this tutorial, you learn how to: 

  * Set environment variables. You'll use these variables when you make requests to Datastream to create and manage both [connection profiles](https://docs.cloud.google.com/datastream/docs/behavior-overview#entitycontext) and a [stream](https://docs.cloud.google.com/datastream/docs/behavior-overview#entitycontext).
  * Create and manage connection profiles for a source database and a destination bucket in Cloud Storage. By creating these connection profiles, you're creating records that contain information about the source database and destination Cloud Storage bucket. The stream in Datastream uses the information in the connection profiles to transfer data from the source database into a folder in the destination bucket.
  * Create and manage a stream. Datastream uses this stream to transfer data, schemas, and tables from the source database into a folder in the destination bucket.
  * Verify that Datastream transfers the data and tables associated with a schema of the source Oracle database into a folder in the destination bucket, and translates this data into the Avro file format.
  * Clean up the resources that you created on Datastream so they won't take up quota and you won't be billed for them in the future.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Storage



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Datastream API. 

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datastream.googleapis.com)

  7. Make sure that you have the Datastream Admin role assigned to your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  8. Make sure that you have a source database that Datastream can access. For this tutorial, an [Oracle database](https://docs.cloud.google.com/datastream/docs/sources#setup) is used as the source.
  9. Configure your source database to allow incoming connections from Datastream public IP addresses. See [IP allowlists and regions](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions) to access the locations of all Datastream regions and their associated public IP addresses.
  10. Make sure that you have configured a destination Cloud Storage bucket that Datastream can access by using the IP allowlist, forward SSH tunnel, or VPC peering [network connectivity method](https://docs.cloud.google.com/datastream/docs/network-connectivity-options).
  11. Make sure that you have data, tables, and schemas in the source database that Datastream can transfer into a folder in the destination Cloud Storage bucket.
  12. Download and install [Cloud Shell.](https://cloud.google.com/shell) This client application provides you with command-line access to your cloud resources (including Datastream).
  13. Install and configure the `[jq](https://stedolan.github.io/jq/download/)` utility. This utility is a lightweight and flexible command-line JSON processor. You'll use this processor to display complex `cURL` commands in easy-to-read text.



## Setting environment variables

In this procedure, you'll set the following variables:

  * `$PROJECT`: This variable is associated with your Google Cloud [project](https://cloud.google.com/docs/overview#projects). Any Google Cloud resources that you allocate and use must belong to a project.
  * `$TOKEN`: This variable is associated with an access token. The access token provides a session that Cloud Shell uses to perform tasks in Datastream using REST APIs.


  1. Launch your Cloud Shell application.

  2. After authenticating into your application with your Google Account, enter the following command:
         
         gcloud auth login
         

  3. At the `Do you want to continue (Y/n)?` prompt, enter `Y`.

  4. Open a web browser and copy the URL into the browser.

  5. Authenticate to the Google Cloud SDK with your Google Account. A code appears on the **Sign in** page. This code is your access token.

  6. Copy the access token, paste it into the `Enter verification code:` parameter in your Cloud Shell application, and press `Enter`.

  7. At the prompt, enter `PROJECT=\"YOUR_PROJECT_NAME\"` to set the `$PROJECT` environment variable to your Google Cloud project.

  8. At the prompt, enter `gcloud config set project YOUR_PROJECT_NAME` to set the project that you'd like to work on to your Google Cloud project.

Your command prompt updates to reflect your active project and respects this format: `USERNAME@cloudshell:~ (YOUR_PROJECT_NAME)$`

  9. At the prompt, enter `TOKEN=$(gcloud auth print-access-token)` to retrieve the access token and store it as a variable.

  10. At the prompt, enter the following commands to ensure that your `$PROJECT` and `$TOKEN` variables are set correctly:

     * `echo $PROJECT`
     * `echo $TOKEN`



Now that you set your variables, you can make requests to Datastream to create and manage both connection profiles and a stream.

## Create and manage connection profiles

In this section, you create and manage connection profiles for a source Oracle database and a destination bucket in Cloud Storage.

When you create these connection profiles, you create records that contain information about the source database and destination Cloud Storage bucket. Datastream uses the information in the connection profiles to transfer data from the source database into a folder in the destination bucket.

Creating and managing connection profiles includes:

  * Creating connection profiles for a source Oracle database and a destination bucket in Cloud Storage
  * Retrieving information about a connection profile
  * Modifying a connection profile
  * Performing a discover API call on the source Oracle connection profile. This call lets you to look inside the database to see the objects associated with it. These objects include the schemas and tables that contain the data of the database. When you use Datastream to configure a stream, you may not want to pull all objects out of the database, but rather a subset of the objects (for example, only certain tables and schemas of the database). Use the discover API to help you find (or discover) the subset of database objects that you want to pull.



### Create connection profiles

In this procedure, you create two connection profiles: one to a source Oracle database and another to a destination bucket in Cloud Storage.

  1. Create a connection profile to a source Oracle database. At the prompt, enter the following command:


    
    
    ORACLE="{\"displayName\":\"DISPLAY_NAME\",\"oracle_profile\":{\"hostname\":\"HOSTNAME\",\"username\":\"USERNAME\",\"password\":\"PASSWORD\",\"database_service\":\"DATABASE_SERVICE\",\"port\":"PORT_NUMBER\"},\"no_connectivity\":{}}"
      

Use the following table to help you understand the parameter values for the source Oracle database:

Parameter value| Replace with  
---|---  
DISPLAY_NAME| The display name of the connection profile to the source database.  
HOSTNAME| The hostname of the source database server.  
USERNAME| The username of the account for the source database (for example, ROOT).  
PASSWORD| The password of the account for the source database.  
DATABASE_SERVICE| The service that ensures that the source database is protected and monitored. For Oracle databases, the database service is typically ORCL.  
PORT_NUMBER| The port number reserved for the source database. For an Oracle database, the port number is typically 1521.  
**Note:** For this tutorial, the `no_connectivity` network connectivity method is used because you configured your source Oracle database to allow incoming connections from Datastream public IP addresses. In addition to `no_connectivity`, there are two network connectivity methods supported that you can use to establish a connection between the source database and the folder in the destination Cloud Storage bucket. 

  * IP allowlist: This method works by configuring the source database to accept connections from Datastream's public IP address. If you're using IP allowlist as your network connectivity method, then replace `no_connectivity` with `StaticIpConnectivity`.
  * Forward SSH tunnel: This method establishes connectivity from the source database to Datastream through a secure SSH tunnel. If you're using forward SSH tunnel as your network connectivity method, then replace `no_connectivity` with `forwardSshTunnelConnectivity`. For information about the values you can set for this network connectivity method, see the [reference documentation.](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity).



  1. At the prompt, enter the `echo $ORACLE | jq` command to see the source connection profile you created in easy-to-read text.
         
         {
           "displayName": "DISPLAY_NAME",
           "oracle_profile": {
             "hostname": "HOSTNAME",
             "username": "USERNAME",
             "password": "PASSWORD",
             "database_service": "DATABASE_SERVICE",
             "port": PORT_NUMBER
            },
           "no_connectivity": {}
         }

  2. Submit the Oracle connection profile so that it can be created. At the prompt, enter the following command:
         
         curl -X POST -d $ORACLE -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles?connection_profile_id=SOURCE_CONNECTION_PROFILE_ID

Use the following table to help you understand the parameter values for this command:

Parameter value| Replace with  
---|---  
DATASTREAM_API_VERSION| The current version of the Datastream API (for example, `v1`).  
PROJECT_PATH| The full path of your Google Cloud project (for example, `projects/$PROJECT/locations/YOUR_PROJECT_LOCATION`).  
SOURCE_CONNECTION_PROFILE_ID| The unique identifier reserved for this connection profile (for example, cp-1).  
  3. Verify that you see the following lines of code:
         
         {
           "name": "PROJECT_PATH/operations/operation-SOURCE_CONNECTION_PROFILE_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "datastream.googleapis.com/DATASREAM_VERSION/PROJECT_PATH/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "verb": "create",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

**Note:** The SOURCE_CONNECTION_PROFILE_OPERATION_ID parameter value is an alphanumeric value for the operation that's used to create this connection profile. The DATE_AND_TIME_STAMP parameter value indicates when the connection profile is created, and it follows the `YYYY-MM-DDTHH:MM:SSZ` format.
  4. Create a connection profile to a destination bucket in Cloud Storage. At the prompt, enter the following command:
         
         GOOGLECLOUDSTORAGE="{\"displayName\":\"DISPLAY_NAME\",\"gcs_profile\":{\"bucket\":\"BUCKET_NAME\",\"root_path\":\"/FOLDER_PATH\"},\"no_connectivity\":{}}"

Use the following table to help you understand the parameter values for the destination bucket:

Parameter value| Replace with  
---|---  
DISPLAY_NAME| The display name of the connection profile to the destination bucket.  
BUCKET_NAME| The name of the destination bucket.  
FOLDER_PATH| The folder in the destination bucket into which Datastream will transfer data from the source database (for example, /root/path).  
  5. At the prompt, enter the `echo $GOOGLECLOUDSTORAGE | jq` command to see the destination connection profile you created in easy-to-read text.
         
         {
           "displayName": "DISPLAY_NAME",
           "gcs_profile": {
             "bucket": "BUCKET_NAME",
             "root_path": "/FOLDER_PATH"
           },
           "no_connectivity": {}
         }

  6. Submit the Cloud Storage connection profile so that it can be created. At the prompt, enter the following command:
         
         curl -X POST -d $GOOGLECLOUDSTORAGE -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles?connection_profile_id=DESTINATION_CONNECTION_PROFILE_ID

**Important:** For the DESTINATION_CONNECTION_PROFILE_ID parameter value, make sure that you specify a different identifier for this connection profile (for example, cp-2).
  7. Verify that you see the following lines of code:
         
         {
           "name": "PROJECT_PATH/operations/operation-DESTINATION_CONNECTION_PROFILE_OPERATION_ID",
           "metadata": {
             "@type": "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "datastream.googleapis.com/DATASTREAM_VERSION/PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
             "verb": "create",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

**Note:** The DESTINATION_CONNECTION_PROFILE_OPERATION_ID parameter value is an alphanumeric value for the operation that's used to create this conection profile.
  8. Confirm that both connection profiles are created. At the prompt, enter the following command:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles

**Note:** The `connectionProfiles` string at the end of the command indicates that you want to retrieve information about both connection profiles to confirm that they're created.
  9. Verify that you receive two returned results for both the source and destination connection profiles.
         
         {
           "connectionProfiles": [
             {
               "name": "PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
               "createTime": "DATE_AND_TIME_STAMP",
               "updateTime": "DATE_AND_TIME_STAMP",
               "displayName": "DISPLAY_NAME",
               "gcsProfile": {
                 "bucket": "BUCKET_NAME",
                 "rootPath": "FOLDER_PATH"
               },
               "noConnectivity": {}
             },
            {
             "name": "PROJECT_PATH/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "createTime": "DATE_AND_TIME_STAMP",
             "updateTime": "DATE_AND_TIME_STAMP",
             "displayName": "DISPLAY_NAME",
             "oracleProfile": {
               "hostname": "HOSTNAME",
               "port": PORT_NUMBER,
               "username": "USERNAME",
               "databaseService": "DATABASE_SERVICE"
             },
             "noConnectivity": {}
             }
           ]
         }




### Manage connection profiles

In this procedure, you manage the connection profiles that you created for a source Oracle database and a destination bucket in Cloud Storage. This includes:

  * Retrieving information about the destination Cloud Storage connection profile
  * Modifying this connection profile. For this tutorial, you'll change the folder of the destination Cloud Storage bucket to /root/tutorial. Datastream transfers data from the source database into this folder.
  * Performing a discover API call on the source Oracle connection profile


  1. Retrieve information about the destination Cloud Storage connection profile. At the prompt, enter the following command:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID

  2. Verify that you see information about this connection profile.
         
         {
           "name": "PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
           "createTime": "DATE_AND_TIME_STAMP",
           "updateTime": "DATE_AND_TIME_STAMP",
           "displayName": "DISPLAY_NAME",
           "gcsProfile": {
             "bucket": "BUCKET_NAME",
             "rootPath": "FOLDER_PATH"
           },
           "noConnectivity": {}
         }

  3. Modify this connection profile. To do this, first, set an UPDATE variable. This variable contains the values of the connection profile that you want to change. For this tutorial, you'll change the folder of the destination bucket to /root/tutorial.

To set the variable, at the prompt, enter the following command:
         
         UPDATE="{\"gcsProfile\":{\"rootPath\":\"/root/tutorial\"}}"

  4. At the prompt, enter the following command:
         
         curl -X PATCH -d $UPDATE -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID?update_mask=gcsProfile.rootPath

**Note:** The `update_mask=gcsProfile.rootPath` portion of code indicates that you want to change the value of the rootPath parameter for the Cloud Storage connection profile.
  5. Verify that you see the following lines of code:
         
         {
           "name": "PROJECT_PATH/operations/operation-DESTINATION_CONNECTION_PROFILE_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
             "verb": "update",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

**Note:** The `update` value for the verb parameter indicates that you modified this connection profile.
  6. Confirm that the connection profile is modified. At the prompt, enter the following command:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID

  7. Verify that the folder of the destination bucket of the Cloud Storage connection profile is now /root/tutorial.
         
         {
           "name": "PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
           "createTime": "DATE_AND_TIME_STAMP",
           "updateTime": "DATE_AND_TIME_STAMP",
           "displayName": "DISPLAY_NAME",
           "gcsProfile": {
             "bucket": "BUCKET_NAME",
             **"rootPath" : "/root/tutorial"**
           },
           "noConnectivity": {}
         }

  8. Use the Datastream discover API to discover the schemas and tables of the source Oracle database. Datastream provides access to this database through the source connection profile.

     1. Discover the schemas of the Oracle database. At the prompt, enter the following command:
            
            curl -X POST -d "{\"connection_profile_name\":\"projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID\", \"oracle_rdbms\":{\"oracleSchemas\":[{\"schema\":\"ROOT\"}]}}" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles:discover

**Note:** Replace the YOUR_PROJECT_NUMBER placeholder with the 10-digit identification number of your Google Cloud project. The `connectionProfiles:discover` portion of code indicates that you want to use the connection profile for the source Oracle database to discover all schemas of that database.
     2. Verify that Datastream retrieves all schemas of your database.

     3. Retrieve the tables of a schema in your database. For this tutorial, you'll use the discover API to retrieve the tables of the ROOT schema. However, you can discover the tables of any schema in your database.

At the prompt, enter the following command:
    
    curl -X POST -d "{\"connection_profile_name\":\"projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID\", \"oracle_rdbms\":{\"oracleSchemas\":[{\"schema\":\"ROOT\"}]}}" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles:discover

     1. Verify that Datastream retrieves all tables of the schema that you specified (for this tutorial, the ROOT schema).



Now that you created and managed connection profiles for a source Oracle database and a destination bucket in Cloud Storage, you're ready to create and manage a stream in Datastream.

## Creating and managing a stream

In this section, you create and manage a stream. Datastream uses this stream to transfer data, schemas, and tables from the source database into a folder in the destination Cloud Storage bucket.

Creating and managing a stream includes:

  * Validating a stream to ensure that the stream will run successfully, and that all validation checks pass. These checks include: 
    * Whether the source is configured properly to allow Datastream to stream data from it.
    * Whether the stream can connect to both the source and the destination.
    * The end-to-end configuration of the stream.
  * Creating the stream with the following lists: 
    * An allow list. This list specifies the tables and schemas in the source database that Datastream can transfer into a folder in the destination bucket in Cloud Storage. For this tutorial, this is the /root/tutorial folder.
    * A reject list. This list specifies the tables and schemas in the source database that Datastream is restricted from transferring into the folder in the Cloud Storage destination bucket.
  * Retrieving information about the stream
  * Modifying the stream
  * Starting the stream so that Datastream can transfer data, schemas, and tables from the source database into a folder in the destination Cloud Storage bucket.
  * Using the Fetch Errors API to detect any errors associated with the stream
  * Pausing the stream. When a stream is paused, Datastream won't pull any new data from the source database into the destination bucket.
  * Resuming the paused stream so that Datastream can continue to transfer data into the destination bucket.



### Create a stream

In this procedure, you create a stream from the source Oracle database into a folder in the destination Cloud Storage bucket. The stream you create will include both an allow list and a reject list.

  1. Set a SCHEMAS variable. This variable defines the schemas that contain the data and tables that you want Datastream to retrieve from the source database and transfer into the /root/tutorial folder of the Cloud Storage destination bucket. For this tutorial, you'll set the SCHEMAS variable to be associated with the ROOT schema.

At the prompt, enter the following command:
         
         SCHEMAS="{\"oracleSchemas\":[{\"schema\":\"ROOT\"}]}"

  2. At the prompt, enter the echo $SCHEMAS | jq command to see the ROOT schema that you defined for this variable in easy-to-read text.

  3. Create a stream. At the prompt, enter the following command:
         
         STREAM="{\"display_name\":\"DISPLAY_NAME\",\"source_config\":{\"source_connection_profile_name\":\"PROJECT_PATH/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",\"oracle_source_config\":{\"allowlist\":$SCHEMAS,\"rejectlist\":{}}},\"destination_config\":{\"destination_connection_profile_name\":\"PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID\",\"gcs_destination_config\":{\"file_rotation_mb\":5,\"file_rotation_interval\":{\"seconds\":15},\"avro_file_format\":{}},\"backfill_all\":{}}}"

**Note:** Replace the DISPLAY_NAME parameter value with the display name that you want for your stream (for example, `stream1`).
  4. At the prompt, enter the `echo $STREAM | jq` command to see the stream you created in easy-to-read text.
         
         {
           "display_name": "DISPLAY_NAME",
           "source_config": {
             "source_connection_profile_name": "PROJECT_PATH/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "oracle_source_config": {
               "allowlist": {
                 "oracleSchemas": [
                   {
                     "schema": "ROOT"
                   }
                 ]
               },
               "rejectlist": {}
             }
           },
           "destination_config": {
             "destination_connection_profile_name": "PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
             "gcs_destination_config": {
               "file_rotation_mb": 5,
               "file_rotation_interval": {
                 "seconds": 15
               },
               "avro_file_format": {}
             }
           },
           "backfill_all": {}
         }

Use this table to help you understand the following parameters of the stream:

Parameter| Description  
---|---  
allowlist| The schemas, containing tables and data, that will be transferred from the source database into a folder of the Cloud Storage destination bucket. For this tutorial, all tables and data from the ROOT schema (and only this schema) will be transferred into the /root/tutorial folder of the destination bucket.  
rejectlist| Any schemas, containing tables and data, that won't be transferred into a folder of the Cloud Storage destination bucket. For this tutorial, the {} value signifies that no tables and data from the source database will be prevented from being transferred into the destination bucket.  
file_rotation_mb| The size (in MBytes) of files that contain data that's being transferred from the source database into a folder in the Cloud Storage destination bucket. For this tutorial, as data is being retrieved from the source database, it's written into 5-MB files. If any data exceeds this size, then the data will be segmented into multiple 5-MB files.  
file_rotation_interval| The number of seconds that will elapse before Datastream closes an existing file in a folder of the Cloud Storage destination bucket and opens another file to contain data being transferred from the source database. For this tutorial, the file rotation interval is set to 15 seconds.  
avro_file_format| The format of the files that Datastream will transfer from the source database into a folder of the Cloud Storage destination bucket. For this tutorial, Avro is the file format. In addition to Avro, Datastream now supports the JSON output format for files written to Cloud Storage. Instead of avro_file_format, this is represented by the json_file_format parameter. For the JSON format, you can:
     * Include a Unified Types schema file in the path. As a result, Datastream writes two files to Cloud Storage: a JSON data file and an Avro schema file. The schema file has the same name as the data file, with a `.schema` extension.
     * Enable gzip compression to have Datastream compress the files that are written to Cloud Storage.
Because these two properties don't apply to Avro, the value of the avro_file_format parameter is set to an empty dictionary ({}).  
backfill_all| This parameter is associated with historical backfill. By setting this parameter to an empty dictionary ({}), Datastream will backfill:
     * Historical data, in addition to ongoing changes to the data, from the source database into the destination.
     * Schemas and tables, from the source into the destination.  
  5. Validate the stream to ensure that the stream will run successfully, and that all validation checks pass. At the prompt, enter the following command:
         
         curl -X POST -d $STREAM -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" "https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams?stream_id=STREAM_ID&validate_only=true"

Replace the STREAM_ID parameter value with a unique identifier reserved for this stream (for example, `stream-1`).

The `&validate_only=true` value indicates that you're only validating the stream; you're not creating it. For this request, put the entire URL in quotation marks. This ensures that Datastream will pick up the `&validate_only=true` value to validate the stream.

  6. Verify that you see the `{}` line of code. This indicates that the stream has passed all validation checks and there are no errors associated with the stream.

For any validation check that doesn't pass, information appears as to why it failed and what to do to rectify the problem.

After making the appropriate corrections, make the request again to ensure that all validation checks pass.

  7. Submit the stream so that it can be created. At the prompt, enter the following command: 
         
         curl -X POST -d $STREAM -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams?stream_id=STREAM_ID

  8. Verify that you see the following lines of code:
         
         {
           "name": "PROJECT_PATH/operations/operation-STREAM_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/streams/STREAM_ID",
             "verb": "create",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

**Note:** The STREAM_OPERATION_ID parameter value is an alphanumeric value for the operation that's used to create this stream.
  9. Confirm that the stream is created. At the prompt, enter the following command:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams

**Note:** The `streams` string at the end of the command indicates that you want to retrieve information about the stream to confirm that it's created.
  10. Verify that you receive a returned result for the stream that you created.
         
         {
           "streams": [
             {
               "name": "PROJECT_PATH/streams/STREAM_ID",
               "createTime": "DATE_AND_TIME_STAMP",
               "updateTime": "DATE_AND_TIME_STAMP",
               "displayName": "DISPLAY_NAME",
               "sourceConfig": {
                 "sourceConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
                 "oracleSourceConfig": {
                   "allowlist": {
                     "oracleSchemas": [
                       {
                         "schema": "ROOT"
                       }
                     ]
                   },
                   "rejectlist": {}
                 }
               },
               "destinationConfig": {
                 "destinationConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
               "gcsDestinationConfig": {
                   "fileRotationMb": 5,
                   "fileRotationInterval": "15s"
                   "avroFileFormat": {}
                 }
               },
               "state": "CREATED",
               "backfillAll": {}
             }
           ]
         }




### Manage the stream

In this procedure, you use the stream that you created to transfer data from a source Oracle database into a folder in a Cloud Storage destination bucket. This includes:

  * Retrieving information about the stream
  * Modifying the stream
  * Starting the stream
  * Using the Fetch Errors API to detect any errors associated with the stream
  * Pausing and resuming the stream


  1. Retrieve information about the stream. At the prompt, enter the following command:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID

  2. Verify that you see information about this stream.
         
         {
           "name": "PROJECT_PATH/streams/STREAM_ID",
           "createTime": "DATE_AND_TIME_STAMP",
           "updateTime": "DATE_AND_TIME_STAMP",
           "displayName": "DISPLAY_NAME",
           "sourceConfig": {
             "sourceConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "oracleSourceConfig": {
               "allowlist": {
                 "oracleSchemas": [
                   {
                     "schema": "ROOT"
                   }
                 ]
               },
               "rejectlist": {}
              }
             },
             "destinationConfig": {
               "destinationConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
               "gcsDestinationConfig": {
                 "fileRotationMb": 5,
                 "fileRotationInterval": "15s"
                 "avroFileFormat": {}
               }
             },
             "state": "CREATED",
             "backfillAll": {}
           }

  3. Modify this stream. To do this, first, set an UPDATE variable. This variable contains the values of the stream that you want to change. For this tutorial, change the size (in MBytes) of files that contain data that's being transferred from the source database into a folder in the Cloud Storage destination bucket (from 5 MBytes to 100 MBytes). As data is being retrieved from the source database, it's now written into 100-MB files. If any data exceeds this size, then the data will be segmented into multiple 100-MB files.

To set the variable, at the prompt, enter the following command:
         
         UPDATE="{\"destination_config\":{\"gcs_destination_config\":{\"file_rotation_mb\":100}}}"

  4. At the prompt, enter the following command:
         
         curl -X PATCH -d $UPDATE -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID/?update_mask=destination_config.gcs_destination_config.file_rotation_mb

**Note:** The `update_mask=destination_config.gcs_destination_config.file_rotation_mb` portion of code indicates that you want to change the value of the file_rotation_mb parameter for the Cloud Storage connection profile.
  5. Verify that you see the following lines of code:
         
         {
           "name": "PROJECT_PATH/operations/operation-STREAM_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/streams/STREAM_ID",
             "verb": "update",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

**Note:** The `update` value for the verb parameter indicates that you modified this stream.
  6. Confirm that the stream is modified. At the prompt, enter the following command:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID

  7. Verify that the value of the fileRotationMb parameter for the Cloud Storage connection profile is now `100`.
         
         {
           "name": "PROJECT_PATH/streams/STREAM_ID",
           "createTime": "DATE_AND_TIME_STAMP",
           "updateTime": "DATE_AND_TIME_STAMP",
           "displayName": "DISPLAY_NAME",
           "sourceConfig": {
             "sourceConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "oracleSourceConfig": {
               "allowlist": {
                 "oracleSchemas": [
                   {
                     "schema": "ROOT"
                   }
                 ]
               },
               "rejectlist": {}
              }
             },
             "destinationConfig": {
               "destinationConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
               "gcsDestinationConfig": {
                 **"fileRotationMb" : 100,**
                 "fileRotationInterval": "15s"
                 "avroFileFormat": {}
               }
             },
             "state": "CREATED",
             "backfillAll": {}
           }

  8. Start the stream. To do so:

     1. Change the `UPDATE` variable. At the prompt, enter the following command:
            
            UPDATE="{\"state\":\"RUNNING\"}"

     2. Then, enter the following command:
            
            curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID?updateMask=state

By using the `updateMask` parameter in the request, only the fields that you specify have to be included in the body of the request.

For this example, the field specified is the `state` field, which represents the stream's status (or state). By starting the stream, you're changing its state from `CREATED` to `RUNNING`.

  9. Verify that you see the following lines of code.
         
         {
           "name": "PROJECT_PATH/operations/operation-STREAM_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/streams/STREAM_ID",
             "verb": "start",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

  10. After a few minutes, retrieve information about the stream to confirm that it started:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID

**Note:** It takes a few minutes for the stream to start running. Background resources need to start so that the stream can start.
  11. Verify that the state of the stream has changed from `CREATED` to `RUNNING`.
         
         {
           "name": "PROJECT_PATH/streams/STREAM_ID",
           "createTime": "DATE_AND_TIME_STAMP",
           "updateTime": "DATE_AND_TIME_STAMP",
           "displayName": "DISPLAY_NAME",
           "sourceConfig": {
             "sourceConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "oracleSourceConfig": {
               "allowlist": {
                 "oracleSchemas": [
                   {
                     "schema": "ROOT"
                   }
                 ]
               },
               "rejectlist": {}
             }
           },
           "destinationConfig": {
             "destinationConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
             "gcsDestinationConfig": {
               "fileRotationMb": 100,
               "fileRotationInterval": "15s"
               "avroFileFormat": {}
             }
           },
           **"state" : "RUNNING",**
           "backfillAll": {}
         }

When a stream is started, the status first changes to `STARTING`. This signifies that the stream is in the process of being started and validated.

     * If the stream is valid, then the status of the stream changes from `STARTING` to `RUNNING`.
     * If the stream isn't valid, then the status of the stream changes back from `STARTING` to `CREATED`. [Address the errors](https://docs.cloud.google.com/datastream/docs/troubleshoot-a-stream) related to the stream. For example, if errors are associated with the connectivity information of the stream, then modify the stream definition. After resolving all problems of the stream, start it again. The status changes to `STARTING`, and then to `RUNNING`.

If the state of the stream is still `STARTING`, wait a few seconds, and enter the command to retrieve information about the stream again. The state of the stream should change to `RUNNING`.

  12. Using the Fetch Errors API to retrieve any errors associated with the stream.

     1. At the prompt, enter the following command:
            
            curl -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID:fetchErrors

     2. Verify that you see the following lines of code:
            
            {
                "name": "PROJECT_PATH/operations/operation-FETCH_ERRORS_OPERATION_ID",
                "metadata": {
                  "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
                  "createTime": "DATE_AND_TIME_STAMP",
                  "target": "PROJECT_PATH/streams/STREAM_ID",
                  "verb": "fetchErrors",
                  "requestedCancellation": false,
                  "apiVersion": "DATASTREAM_API_VERSION"
                },
                "done": false
              }
              

**Note:** The `FETCH_ERRORS_OPERATION_ID` parameter value is an alphanumeric value for this operation. You'll use this value to retrieve progress information about the operation that's used to detect errors associated with the stream.
     3. At the prompt, enter the following command:
            
            curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/operations/operation-FETCH_ERRORS_OPERATION_ID

     4. Verify that you see the following lines of code:
            
            {
                "name": "PROJECT_PATH/operations/operation-FETCH_ERRORS_OPERATION_ID",
                "metadata": {
                  "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
                  "createTime": "DATE_AND_TIME_STAMP",
                  "endTime": "DATE_AND_TIME_STAMP",
                  "target": "PROJECT_PATH/streams/STREAM_ID",
                  "verb": "fetchErrors",
                  "requestedCancellation": false,
                  "apiVersion": "DATASTREAM_API_VERSION"
                },
                "done": true,
                "response": {
                  "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.FetchErrorsResponse"
                }
              }
              

**Note:** No errors appear after the `"@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.FetchErrorsResponse` line of code. This indicates that Datastream didn't detect any errors for the stream. You can use the stream to transfer data from the source Oracle database into the `/root/tutorial` folder in the Cloud Storage destination bucket. An example of an error that could be retrieved by using the Fetch Errors API is `BAD_CREDENTIALS`. This error occurs when there's an invalid value in either the source or destination connection profiles, and Datastream can't use the profiles to connect to the source database or the destination bucket in Cloud Storage.
  13. Pause the stream. To do so:

     1. Change the `UPDATE` variable. At the prompt, enter the following command:
            
            UPDATE="{\"state\":\"PAUSED\"}"

     2. Then, enter the following command:
            
            curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID?updateMask=state

By pausing the stream, you're changing its state from `RUNNING` to `PAUSED`.
  14. Verify that you see the following lines of code.
         
         {
           "name": "PROJECT_PATH/operations/operation-STREAM_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/streams/STREAM_ID",
             "verb": "start",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

  15. Retrieve information about the stream to confirm that it's paused.
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID

  16. Verify that the state of the stream has changed from `RUNNING` to `PAUSED`.
         
         {
           "name": "PROJECT_PATH/streams/STREAM_ID",
           "createTime": "DATE_AND_TIME_STAMP",
           "updateTime": "DATE_AND_TIME_STAMP",
           "displayName": "DISPLAY_NAME",
           "sourceConfig": {
             "sourceConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "oracleSourceConfig": {
               "allowlist": {
                 "oracleSchemas": [
                   {
                     "schema": "ROOT"
                   }
                 ]
               },
               "rejectlist": {}
             }
           },
           "destinationConfig": {
             "destinationConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
             "gcsDestinationConfig": {
               "fileRotationMb": 100,
               "fileRotationInterval": "15s"
               "avroFileFormat": {}
             }
           },
           **"state" : "PAUSED",**
           "backfillAll": {}
         }

When a stream is paused, Datastream won't pull any new data from the source database into the destination. However, some data may continue to be written to the destination because "in flight" data will continue to flow. 

Therefore, after you pause a stream, the status of the stream changes from `RUNNING` to `DRAINING`. Draining a stream is the process of emptying the stream so that it doesn't contain any data. After the stream is drained of all data, then the status of the stream changes from `DRAINING` to `PAUSED`.

  17. Resume the paused stream. To do so:

     1. Change the `UPDATE` variable. At the prompt, enter the following command:
            
            UPDATE="{\"state\":\"RUNNING\"}"

     2. Then, enter the following command:
            
            curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID?updateMask=state

By resuming the stream, you're changing its state from `PAUSED` back to `RUNNING`.
  18. Verify that you see the following lines of code.
         
         {
           "name": "PROJECT_PATH/operations/operation-STREAM_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/streams/STREAM_ID",
             "verb": "start",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

  19. After a few seconds, retrieve information about the stream to confirm that it's running again.
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID

  20. Verify that the state of the stream has changed from `PAUSED` back to `RUNNING`.
         
         {
           "name": "PROJECT_PATH/streams/STREAM_ID",
           "createTime": "DATE_AND_TIME_STAMP",
           "updateTime": "DATE_AND_TIME_STAMP",
           "displayName": "DISPLAY_NAME",
           "sourceConfig": {
             "sourceConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "oracleSourceConfig": {
               "allowlist": {
                 "oracleSchemas": [
                   {
                     "schema": "ROOT"
                   }
                 ]
               },
               "rejectlist": {}
             }
           },
           "destinationConfig": {
             "destinationConnectionProfileName": "projects/YOUR_PROJECT_NUMBER/locations/YOUR_PROJECT_LOCATION/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
             "gcsDestinationConfig": {
               "fileRotationMb": 100,
               "fileRotationInterval": "15s"
               "avroFileFormat": {}
             }
           },
           **"state" : "RUNNING",**
           "backfillAll": {}
         }




Now that you created and managed a stream, confirmed that there are no errors associated with the stream, and that the state of the stream is `RUNNING`, you're ready to verify that it can transfer data from the source database into a folder in the Cloud Storage destination bucket.

## Verifying the stream

In this procedure, you confirm that Datastream:

  * Transfers the data from all tables associated with the `ROOT` schema of your source Oracle database into the `/root/tutorial` folder in the Cloud Storage destination bucket.
  * Translates the data into the Avro file format.


  1. Go to the **Storage browser** page in Cloud Storage.

[Go to the Storage browser page](https://console.cloud.google.com/storage/browser)

  2. Click the link that contains your bucket.

  3. If the **OBJECTS** tab isn't active, then click it.

  4. Click the **root** folder, and then click the **tutorial** folder.

**Note:** Datastream created the **root** and **tutorial** folders after you modified the destination connection profile by changing the folder of the destination bucket to `/root/tutorial`.
  5. Verify that you see folders that represent tables of the `ROOT` schema of your source Oracle database.

  6. Click one of the table folders and drill down until you see data that's associated with the table.

  7. Click a file that represents the data and click **DOWNLOAD**.

  8. Open this file in an Avro tool (for example, [Avro Viewer](https://avro-tools.com/avro-viewer-and-converter-to-json-and-csv#:~:text=Avro-tools%20is%20a%20free%20online%20tool%20to%20view%20Avro%20files)) to ensure that the content is readable. This confirms that Datastream also translated the data into the Avro file format.




## Clean up

After you've finished this tutorial, you can clean up the resources that you created on Datastream so they won't take up quota and you won't be billed for them in the future. The following sections describe how to delete or turn off these resources.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the Cloud Storage destination bucket

  1. In the left-hand Navigation Drawer of Cloud Storage, click the **Browser** item.

  2. Select the checkbox to the left of your bucket and click **DELETE**.

  3. In the Delete bucket? window, enter the name of your bucket in the text field and click **CONFIRM**.




### Delete the stream

  1. Make sure that your Cloud Shell application is active.

  2. At the prompt, enter the following command:
         
         curl -X DELETE -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams/STREAM_ID

  3. Verify that you see the following lines of code:
         
         {
           "name": "PROJECT_PATH/operations/operation-STREAM_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/streams/STREAM_ID",
             "verb": "delete",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

  4. Confirm that the stream is deleted. At the prompt, enter the following command:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/streams

  5. Verify that a null `{}` value is returned. This signifies that there aren't any streams in Datastream anymore, and the stream that you created is deleted.




### Delete the connection profiles

  1. Delete the connection profile to the source Oracle database. At the prompt, enter the following command:
         
         curl -X DELETE -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID

  2. Verify that you see the following lines of code:
         
         {
           "name": "PROJECT_PATH/operations/operation-SOURCE_CONNECTION_PROFILE_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/connectionProfiles/SOURCE_CONNECTION_PROFILE_ID",
             "verb": "delete",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

  3. Delete the connection profile to the destination bucket in Cloud Storage. At the prompt, enter the following command:
         
         curl -X DELETE -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID

  4. Verify that you see the following lines of code:
         
         {
           "name": "PROJECT_PATH/operations/operation-DESTINATION_CONNECTION_PROFILE_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.datastream.DATASTREAM_API_VERSION.OperationMetadata",
             "createTime": "DATE_AND_TIME_STAMP",
             "target": "PROJECT_PATH/connectionProfiles/DESTINATION_CONNECTION_PROFILE_ID",
             "verb": "delete",
             "requestedCancellation": false,
             "apiVersion": "DATASTREAM_API_VERSION"
           },
           "done": false
         }

  5. Confirm that both connection profiles are deleted. At the prompt, enter the following command:
         
         curl -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://datastream.googleapis.com/DATASTREAM_API_VERSION/PROJECT_PATH/connectionProfiles

  6. Verify that a null `{}` value is returned. This signifies that there aren't any connection profiles in Datastream anymore, and the profiles that you created are deleted.




## What's next

  * Learn more about [Datastream](https://docs.cloud.google.com/datastream/docs).
  * Try out other Google Cloud features for yourself. Have a look at our [tutorials](https://cloud.google.com/docs/tutorials).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
