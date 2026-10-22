---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-bwoh-batch-source-plugin/
title: SAP BW Open Hub batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:42.067576+00:00
---

# SAP BW Open Hub batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-bwoh-batch-source-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  SAP BW Open Hub batch source Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to deploy, configure, and run data pipelines that use the SAP BW Open Hub Batch Source plugin. You can use SAP as a source for batch-based and delta-based data extraction in Cloud Data Fusion through the [BW Open Hub Service](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/38/ed95d8780b4d67936b2f25be382a5e/frameset.htm).

This plugin enables bulk data integration from SAP applications with Cloud Data Fusion. You can configure and execute bulk data transfers from SAP [DataSources](https://help.sap.com/viewer/107a6e8a38b74ede94c833ca3b7b6f51/2.0.9/en-US/5ea8f318d3304d6aa633f7757ed92de3.html) without any coding.

For supported SAP applications and objects for extraction, see Support details. For more information about running SAP on Google Cloud, see [Overview of SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).

## Objectives

  * Configure the SAP BW system.
  * Deploy the plugin in your Cloud Data Fusion environment.
  * Download the SAP transport from Cloud Data Fusion and install it in SAP.
  * Use Cloud Data Fusion and SAP BW Open Hub Batch Source to create data pipelines for integrating SAP data.



## Before you begin

To use this plugin, you need domain knowledge in the following areas:

  * Building pipelines in [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)
  * Configuring SAP BW or BW4HANA systems



### User roles

The tasks on this page are performed by people with the following roles in Google Cloud or in their SAP system:

User type | Description  
---|---  
Google Cloud Admin | Users assigned this role are administrators of Google Cloud accounts.  
Cloud Data Fusion User | Users assigned this role are authorized to design and run data pipelines. They are granted, at minimum, the Data Fusion Viewer ([ `roles/datafusion.viewer`](https://docs.cloud.google.com/data-fusion/docs/access-control#roles)) role. If you are using role-based access control, you might need [additional roles](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac#predefined-roles).   
SAP Admin  | Users assigned this role are administrators of the SAP system. They have access to download software from the SAP service site. It is not an IAM role.  
SAP User | Users assigned this role are authorized to connect to an SAP system. It is not an IAM role.  
  
### Prerequisites for SAP BW

You need SAP HANA Studio to create and edit Data Transfer Processes and Process Chains.

### Prerequisites for Cloud Data Fusion

  * A VPC Network is required for Cloud Data Fusion instance creation.
  * A Cloud Data Fusion instance, version 6.8.0 or later, any edition, is required.
  * Required roles must be granted to the service account assigned to the Cloud Data Fusion instance. For more information, see [Granting service account user permission](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission).
  * You must use a peering connection between your VPC and Google's shared VPC network.



## Configure the SAP BW system

The SAP BW Open Hub Batch Source uses a _Remote Function Module_ (RFM), which must be installed on each SAP Server where data gets extracted. This RFM is delivered as an SAP transport.

To configure your SAP system, follow these steps:

  1. The Cloud Data Fusion user must download the zip file containing the SAP transport and provide it to the SAP Admin. For more information, see Set up Cloud Data Fusion.
  2. The SAP Admin must import the SAP transport into the SAP system and verify the objects created. For more information, see Install the SAP transport.
  3. Optional: The SAP user can modify the SAP Standard Authorization Objects of delivered role `/GOOG/BWOH_CDF_AUTH` based on their organization's security policies.



### Install the SAP transport files

To design and run data pipelines in Cloud Data Fusion, the SAP components are delivered in SAP transport files, which are archived in a zip file. The download is available when you [deploy the plugin in the Cloud Data Fusion Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin).

To install the SAP transport, follow these steps:

#### Step 1: Upload the transport request files

  1. Log into the operating system of the SAP Instance.
  2. Use the SAP transaction code `AL11` to get the path for the `DIR_TRANS` folder. Typically, the path is `/usr/sap/trans/`.
  3. Copy the cofiles to the `DIR_TRANS/cofiles` folder.
  4. Copy the data files to the `DIR_TRANS/data` folder.
  5. Set the User and Group of data and cofile to `<sid>adm` and `sapsys`.



#### Step 2: Import the transport request files

The SAP administrator can import the transport request files by using one of the following options:

##### Option 1: Import the transport request files by using the SAP transport management system

  1. Log in to the SAP system as an SAP administrator.
  2. Enter the transaction STMS.
  3. Click **Overview > Imports**.
  4. In the Queue column, double-click the current SID.
  5. Click **Extras > Other Requests > Add**.
  6. Select the transport request ID and click **Continue**.
  7. Select the transport request in the import queue, and then click **Request > Import**.
  8. Enter the Client number.
  9. On the **Options** tab, select **Overwrite Originals** and **Ignore Invalid Component Version**.

Optional: Select **Leave Transports Requests in Queue for Later Import**. This causes requests to be imported again in the correct order with the next import of all the requests. This option is useful if you have to make preliminary imports for individual requests.

  10. Click **Continue**.

  11. Verify that the function module and authorization roles were imported successfully by using any appropriate transactions, such as `SE80` and `PFCG`.




##### Option 2: Import the transport request files at the operating system level

  1. Log in to the SAP system as an SAP administrator.
  2. Add the appropriate requests to the import buffer:
         
         tp addtobuffer TRANSPORT_REQUEST_ID SID
         

For example: `tp addtobuffer BW1K900054 DD1`

  3. Import the transport requests:
         
         tp import TRANSPORT_REQUEST_ID SID client=NNN U1238
         

Replace `NNN` with the client number. For example:
         
         tp import BW1K900054 DD1 client=100 U1238
         

**Note:** `U1238` indicates to set the options described in step 9 in Option 1. The numbers indicate the corresponding option order number in the SAP GUI, which might vary by system. The numbers must be adjusted by your SAP administrator.
  4. Verify that the function module and authorization roles were imported successfully by using any appropriate transactions, such as `SE80` and `PFCG`.




### Required SAP authorizations

To run a data pipeline in Cloud Data Fusion, you need an SAP User. The SAP User must be of the `Communications` or `Dialog` types. To avoid using SAP dialog resources, the `Communications` type is recommended. The SAP Administrator can create users using SAP transaction code `SU01`.

SAP Authorizations are required to configure the connector for SAP. Connector-specific SAP authorization objects are shipped as part of the Transport Request. Import the Authorization Role Transport as described in Install the SAP transport to bring the Role into your system and generate the role from the PFCG transaction code.

For standard SAP authorization objects, your organization manages permissions with its own security mechanism. You can maintain authorization objects based on the security policies of your organization.

## Create a Process Chain (PC) and Data Transfer Process (DTP)

Creating a process chain and data transfer process requires some additional skills and background knowledge.

### Background concepts

  * [_Process Chain_ (PC)](https://help.sap.com/doc/de49c012b53d476eae7af14497eac256/2.3.latest/en-US/4dc570a257444a34ad0b7c9b6cceb875.html)
  * [_Data Transfer Process_ (DTP)](https://help.sap.com/doc/PRODUCTION/saphelp_nw74/7.4.16/en-US/49/996aca00002774e10000000a42189b/content.htm?no_cache=true)



To create or edit a PC and DTP, use SAP HANA Studio.

#### Prerequisite skills

  * You have used transformations to define the data flow between the source and the target object.
  * You are well-versed with basic BW and HANA concepts, such as DataStore Objects (DSO), Data Transformations, InfoCubes, Query optimization, HANA Modeling, and HANA DB features using HANA Studio. For more information about these concepts, see the [SAP tutorials on BW and HANA](https://help.sap.com/docs/SAP_HANA_PLATFORM?version=2.0.01).



#### Extraction type

There are two modes of data extraction for a Data Transfer Process—Full and Delta.

  * **Full** : It selects all the data available in the source based on the Filter conditions mentioned in the DTP. If the source of data is one of the following InfoProviders, only Full extraction mode is available:

    * InfoObjects
    * InfoSets
    * DataStore Objects for Direct Update
  * **Delta** : Unlike InfoPackage, Delta transfer using a DTP does not require an explicit initialization. When a DTP is executed with the Delta extraction mode for the first time, all the existing requests until extraction time are retrieved from the source, and then delta is automatically initialized.

The following options are available for a DTP with the extraction mode Delta:

    * **Only Get Delta Once**
    * **Get All New Data Request By Request**
    * **Retrieve Until No More New Data**



**Package size** : This is the number of data records present in an individual data package. The default value is `50,000`.

### Create a Process Chain

To create a Process Chain (PC), use transaction RSPC in SAP GUI. Define a start process, and then add the process steps and DTP. For more information, see the SAP documentation for [Creating Process Chains](https://help.sap.com/docs/SAP_BW4HANA/107a6e8a38b74ede94c833ca3b7b6f51/c372b0ab181d4ba88d0f8eac11d81a7a.html?version=2.0.3).

Various options are available in HANA Studio to monitor and administer PCs. For more information, see [SAP BW/4HANA Process Chain Operations](https://blog.sap-press.com/sap-bw4hana-process-chain-operations).

### Create a Data Transfer Process using a Process Chain

Go to the **Planning** view of the Process Chain that you want to use for the Data Transfer Process. From the **Planning** view, you can create the DTP using HANA Studio. For more information, see the SAP documentation for [Creating a Data Transfer Process](https://help.sap.com/saphelp_nw73/helpdata/en/4a/28032afa9147dbe10000000a42189c/frameset.htm).

For more information about the configuration options, see [All about Data Transfer Process (DTP) – SAP BW 7](https://blogs.sap.com/2012/09/16/all-about-data-transfer-process-dtp-sap-bw-7/).

#### RFC connection

To notify the callback system, such as the SAP BW Open Hub Batch Source plugin, that the data is available, the Process Chain must be updated to use an RFC destination:

  1. In SM59, create an RFC connection of type **TCP/IP Connections** to notify the target system from BW once the data load is completed in BI.

  2. Ensure the **Program ID** is configured in the RFC connection by double-clicking on the RFC connection. The Program ID must be unique for each RFC destination to avoid runtime listener conflicts.

**Note:** RFC destination connection test ends with `TP _PROGRAM ID_ not registered`. This is expected because the RFC connection only works during a pipeline run, that is, when Cloud Data Fusion registers the `_Program ID_` with SAP Gateway.
  3. Use the newly created TCP/IP connection in the Process Chain to send notification, for a Cloud Data Fusion batch job to be completed. The name of the process chain is not case-sensitive. It must be specified correctly in uppercase in the end-to-end integration process.




### Display the logs of Process Chains and Data Transfer Processes

  1. Go to Tcode : RSPC and click **Process Chains**.

  2. Right-click on the Process Chain for which you want to display logs, and click **Display Logs**.




## Configure the Managed Service for Apache Spark cluster when using Process Chain

**Note:** This is applicable only when using Process Chain based extraction, not Open Hub Destination based extraction.

To enable communication via RFC server, you must add the SAP Gateway port entries in the `/etc/services` file in the Managed Service for Apache Spark cluster nodes. It's recommended to use an `init action`, the script to be executed when the cluster is initialized. For more information, see [Initializations Actions](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/init-actions).

Create a script file and save it to a Cloud Storage bucket. The following example shows the content of the script file:
    
    
    gs://cdf-sap-dependent-files/addgw.sh
    #!/bin/bash
    echo 'sapgw00 3300/tcp' >> /etc/services
    echo 'sapgw01 3301/tcp' >> /etc/services
    echo 'sapgw02 3302/tcp' >> /etc/services
    echo 'sapgw03 3303/tcp' >> /etc/services
    echo 'sapgw04 3304/tcp' >> /etc/services
    

In the preceding example, note the following:

  * The entries are in the form `sapgwxx 33xx/tcp`, where `XX` is the SAP instance number.

  * The ports for SAP instances `00` through `04` are added.




Perform the following steps if you're using an ephemeral, or a newly created persistent, or an existing persistent Managed Service for Apache Spark cluster.

###  Ephemeral Managed Service for Apache Spark cluster 

If you're using an ephemeral Managed Service for Apache Spark cluster, add the `init` script path to the cluster properties:

  1. In the job monitor, from the pipeline page in Cloud Data Fusion, click **Configure**.
  2. Select the Compute profile, and click **Customize**.
  3. Under **Advanced Settings** , in the **Initialization Actions** field, enter the path to the `init` script.



###  New persistent Managed Service for Apache Spark cluster 

If you're using a newly created persistent Dataproc cluster, use the `init` script in the gcloud command to create the cluster. For example:
    
    
    gcloud dataproc clusters create cluster-name \
      --region=${REGION} \
      --initialization-actions=gs://cdf-sap-dependent-files/addgw.sh \
      ... other flags ...
    

###  Existing persistent Managed Service for Apache Spark cluster 

If you're using an existing persistent Dataproc cluster, follow these steps:

If the cluster has already been created without using the `init` script, then add the entries manually in both Master and Worker nodes of the Managed Service for Apache Spark cluster.

  1. SSH to Master and Cluster Node.
  2. Log in to the root user ID.
  3. Navigate to `/etc/` and open the `/etc/services` file in a VI editor.
  4. Add the entry `sapgwxx 33xx/tcp`. Replace `xx` with your SAP instance number.
  5. Save the `/etc/services` file.



## Set up Cloud Data Fusion

The **Cloud Data Fusion user and the Google Cloud admin** perform the tasks in this section. 

Make sure that communication is enabled between the Cloud Data Fusion instance and the SAP server. For private instances, set up [network peering](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#set_up_network_peering). After network peering is established with the project where the SAP systems are hosted, no additional configuration is required to connect to your Cloud Data Fusion instance. Both the SAP system and Cloud Data Fusion instance must be inside of the same project.

### Steps for Cloud Data Fusion users

  1. Go to the instance details: 
     1. In the Google Cloud console, go to the Cloud Data Fusion page.

     2. Click **Instances** , and then click the instance's name to go to the **Instance details** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Check that the instance has been upgraded to version 6.8.0 or later. If the instance is in an earlier version, you must upgrade it.
  3. Open the instance. When the Cloud Data Fusion UI opens, click **Hub**.
  4. Select the **SAP** tab > **SAP BW**. If the SAP tab is not visible, see [Troubleshooting SAP integrations](https://docs.cloud.google.com/data-fusion/docs/how-to/sap-integration-troubleshooting#enable-sap-hub).
  5. Click **Deploy SAP BW Plugin**. The plugin appears in the **Source** menu on the Studio page.



### Steps for SAP Admin and Google Cloud Admin

The SAP Admin downloads the following JCo artifacts from the SAP Support site and gives them to the Google Cloud Admin.

  * One platform-independent (`sapjco3.jar`)
  * One platform-dependent (`libsapjco3.so` on Unix)

**Note:** The minimum JCo version supported is 3.0.20.

To download the files, follow these steps:

  1. Go to the [SAP Connectors](https://support.sap.com/en/product/connectors) page.
  2. Click **SAP Java Connector** /**Tools and Services**. You can select platform-specific links for the download.
  3. Select the platform that your Cloud Data Fusion instance runs on:

     1. If you use standard Google Cloud images for the VMs in your cluster, which is the default for Cloud Data Fusion, select **Linux for Intel-compatible processors 64-bit x86**.
     2. If you use a custom image, select the corresponding platform.
  4. The Google Cloud Admin must copy the JCo files to a readable Cloud Storage bucket. Provide the bucket path to the Cloud Data Fusion user to enter it in the corresponding plugin property in Cloud Data Fusion: **SAP JCo Library GCS Path**. See Configure the plugin.

  5. The Google Cloud Admin must grant read access for the two files to the Cloud Data Fusion service account for the design environment and the Managed Service for Apache Spark service account for the execution environment. For more information, see [Cloud Data Fusion service accounts](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts).




## Configure the plugin

The SAP BW Open Hub Batch Source plugin reads the content of an SAP DataSource.

To filter the records, you can configure the following properties for the SAP BW Open Hub Batch Source.

The following indicators are used to define the fields:

  * (M): Indicates Macros are supported for the respective field
  * (O): Optional field



**Label** : Plugin label on the canvas.

### Basic

In the following list of properties, (M) means that the option supports macros, and they can be used to centrally manage the SAP connections. For example, you can use macros for the connection properties and set the values at runtime using runtime parameters or an Argument Setter plugin.

  * **Reference Name** : Name used to uniquely identify this source for lineage and annotating metadata.
  * **Use connection** (On/Off toggle): Whether to use an existing connection (see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections)). If you choose to use an existing connection, you don't have to provide any SAP connection details.

**Note:** Only BW OH Destinations that have one DTP and one PC are supported.
  * **Connection** (browse connections): Choose the existing connection to use. You can also use the macro function `${conn(connection-name)}`.

  * **SAP Client** (M): The SAP client to use. For example, `100`.

  * **SAP Language** (M): SAP logon language. For example, `EN`.

  * **Connection Type** : SAP connection type—direct or load balanced. Load balanced connections are not supported for the Process Chain based extraction. For more information, see Support details.

Selecting a connection type changes the available fields.

For a direct connection, the following fields are available:

    * **SAP Application Server Host** (M): The SAP server name or IP address.
    * **SAP System Number** (M): The SAP system number. For example, `00`.
    * **SAP Router** (M, O): The router string.

For a load balanced connection, the following fields are available:

    * **SAP Message Server Host** (M): The SAP message hostname or IP address.
    * **SAP Message Server Service or Port Number** (M): The SAP message server service or port number. For example, `sapms02`.
    * **SAP System ID (SID)** (M): The SAP system ID. For example, `N75`.
    * **SAP Logon Group Name** (M): The SAP logon group name. For example, `PUBLIC`.
  * **Use Process Chain** (M): This field contains two options.

If you enable Process Chain using the **Yes** option, then the following properties are enabled:

    * **Automatically Resolve PC and DTP Errors** : Controls behavior when a previously failed run is identified. When disabled, the plugin fails the pipeline with relevant errors. When enabled (default), the plugin checks the Process Chain and the Data Transfer Process status in SAP. If any of the following errors are identified, the plugin automatically attempts to resolve them:

    * `Data Transfer Process in error state`: Plugin deletes the previous request

    * Process Chain in Red state with error `previous request status has not been set`: The plugin deletes the blocking request after getting the request ID from the Process Chain log and then attempts to run the PC.

    * **Process Chain Status Notification Wait Time (in minutes)** (M, O): Waits for the given time, in minutes, for the Process Chain to complete the data staging and notify the pipeline to start the extraction. If you specify `0` or leave it blank, the value is taken as 10 minutes, which is the default.

    * **Process Chain** (M): The SAP Process Chain name. For example, `PC_RFC`.

If you disable Process Chain using the **No** option, then the following properties are enabled:

    * **Open Hub Destination** (M): Open Hub Destination name to read.
    * **Request ID** (M,O): Request ID for the already run Data Transfer Process.



### Credentials

  * **SAP Logon Username** (M): SAP username. **Recommended** : If the SAP logon username changes periodically, use a [macro](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382043060/Using+macros+to+create+a+dynamic+data+pipeline).
  * **SAP Logon Password** (M): SAP user password. **Recommended** : For sensitive values like **User password** , use [secure macros](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/801767425/Using+Secure+Keys)



### SAP JCo details

  * **GCP Project ID** (M): The Google Cloud project ID, which uniquely identifies a project. It can be found on the Dashboard in the Google Cloud console.
  * **SAP JCo Library GCS Path** (M): The Cloud Storage path that contains the user-uploaded SAP JCo library files.
  * **Get Schema** : Click this if you want the plugin to generate a schema based on the metadata from SAP, with automatic mapping of SAP data types to the corresponding Cloud Data Fusion data types. The functionality of this is same as the Validate button.



For more information about the client certificates, see [Using X.509 Client Certificates on SAP NetWeaver Application Server for ABAP](https://help.sap.com/saphelp_nw73/helpdata/en/4e/125e0a1e3d2287e10000000a15822b/frameset.htm).

### Advanced

  * **Number of Splits to Generate** (M, O): The number of splits is used to partition the input data. More partitions increase the level of parallelism, but require more resources and overhead. In the case of an SAP on-premise system, if the value is not specified in the UI, the splits are 50% of the available dialog work processes in SAP. Otherwise, the splits are optimized between user specified and 50% of the available work processes.

**Note:** This property controls the parallelism on the Cloud Data Fusion side. The runtime engine creates the specified number of partitions and SAP connections while extracting the records.

**Recommended** : Leave the property blank, unless you are familiar with your SAP system settings.

  * **Additional SAP Connection Properties** (M, O): Set additional SAP JCo properties that override the SAP JCo default values. For example, setting `jco.destination.pool_capacity = 10` overrides the default connection pool capacity.

The following table lists the supported SAP JCo properties:


Property | Description  
---|---  
`jco.destination.peak_limit` | Maximum number of active connections that can be created for a destination simultaneously.  
`jco.destination.pool_capacity` | Maximum number of idle connections kept open by the destination. A value of `0` has the effect that there is no connection pooling, that is, connections will be closed after each request.  
`jco.destination.expiration_time` | Time in `ms` after that the connections hold by the internal pool can be closed.  
`jco.destination.expiration_check_period` | Interval in `ms` with which the timeout checker thread checks the connections in the pool for expiration.  
`jco.destination.max_get_client_time` | Max time in `ms` to wait for a connection, if the maximum allowed number of connections is allocated by the application.  
  
## Behavior of data extraction modes

The data extraction mode is controlled through the Data Transfer Process settings. The behavior is different when using a Process Chain versus using an Open Hub Destination.

### When using a Process Chain

Settings at the Data Transfer Process level control whether a full or delta load is performed. The Request ID arrives as a notification from SAP to the plugin. The plugin reads packet data associated with this single request ID.

### When using Open Hub Destination with no request ID

**Note:** Only BW OH Destinations that have one DTP and one PC are supported.

Full load: Running the pipeline for the first time gets all the available request IDs in the Open Hub table. The plugin reads packet data associated with these request IDs.

Delta load: Running the same pipeline for the next time fetches all the available delta request IDs, after the last fetched request ID. The plugin reads packet data associated with these request IDs.

### When using Open Hub Destination with request ID

**Note:** Only BW OH Destinations that have one DTP and one PC are supported.

Full Load: Running the pipeline for the first time gets all the next available request IDs greater than the specified request ID. The plugin reads packet data associated with these request IDs.

Delta Load: Running the same pipeline for the next time fetches all the available delta request IDs, after the last fetched request ID. The plugin reads packet data associated with these request IDs.

## Data type mapping

The following table shows the mapping between data types used in SAP BW and Cloud Data Fusion.

BW data type | ABAP type | Description (SAP) | Cloud Data Fusion data type  
---|---|---|---  
**Numeric**  
INT1 | `b` | 1-byte integer | `integer`  
INT2 | `s` | 2-byte integer | `integer`  
INT4 | `i` | 4-byte integer | `integer`  
INT8 | `8` | 8-byte integer | `long`  
DEC | `p` | Packed number in BCD format (DEC) | `decimal`  
DF16_DEC   
DF16_RAW | `a` | Decimal floating point 8 bytes IEEE 754r | `decimal`  
DF34_DEC   
DF34_RAW | `e` | Decimal floating point 16 bytes IEEE 754r | `decimal`  
FLTP | `f` | Binary floating point number | `double`  
**Character**  
CHAR  
LCHR | `c` | Character string | `string`  
SSTRING  
[GEOM_EWKB](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/abenlength_functions.htm) | `string` | Character string | `string`  
STRING | `string` | Character string CLOB | `bytes`  
NUMC  
ACCP | `n` | Numeric text | `string`  
**Byte**  
RAW  
LRAW | `x` | Binary data | `bytes`  
RAWSTRING | `xstring` | Byte string BLOB | `bytes`  
**Date/Time**  
DATS | `d` | Date | `date`  
TIMS | `t` | Time | `time`  
TIMESTAMP | `utcl` | TimeStamp   
[Utclong](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/abenbuiltin_types_date_time.htm) | `timestamp`  
  
## Validation

Click **Validate** or **Get Schema**.

The plugin validates the properties and generates a schema based on the metadata from SAP. It automatically maps the SAP data types to the corresponding Cloud Data Fusion data types.

## Run a data pipeline

  1. After deploying the pipeline, click **Configure**.
  2. Select **Resources**.
  3. If needed, change the **Executor CPU** and **Memory** based on the overall data size and the number of transformations used in the pipeline.
  4. Click **Save**.
  5. To start the data pipeline, click **Run**.



## Optimize performance

### Optimize plugin configuration

Use the following properties for optimal performance when you run the pipeline:

  * **Number of Splits to Generate** in the Cloud Data Fusion plugin properties: This directly controls the parallelism on the Cloud Data Fusion side. The runtime engine creates the specified number of partitions and SAP connections while extracting the table records. Values between `8` and `16` are recommended, but you can increase up to `32` or `64` with the appropriate configuration on the SAP side, by allocating appropriate memory resources for the work processes in SAP.

If the value is `0` or left blank (recommended), then the system automatically chooses an appropriate value based on the number of available SAP work processes, records to be extracted, and the package size.

  * **Package Size** in the BW Data Transfer Process properties: This controls the number of data records present in an individual data package. The default value is `50,000`. Increasing this value might yield better performance, but higher resource load. If you are already using higher values, decrease it to allow better parallelization of the extraction.




### Cloud Data Fusion resource settings

**Recommended** : Use 1 CPU and 4 GB of memory per executor. This value applies to each executor process. Set these values in the **Configure > Resources** dialog.

### Managed Service for Apache Spark cluster settings

**Recommended** : At minimum, allocate a total of CPUs across workers, greater than the intended number of splits. See Plugin configuration.

For example, if you have 16 splits, define 20 or more CPUs in total, across all workers. There is an overhead of 4 CPUs used for coordination.

**Recommended** : Use a persistent Managed Service for Apache Spark cluster to reduce the data pipeline runtime. This eliminates the provisioning step, which might take a few minutes or more. Set this in the Compute Engine configuration section.

## Support details

### Supported SAP products and versions

Supported sources:

  * SAP NW BW 7.5 and later
  * SAP BW4HANA 2.0 SP9 (to include Open Hub Destination API; earlier releases of BW4HANA don't support the Open Hub Destination API)



### Support for SAP load balanced (message server) connection

SAP load balanced (message server) connection is supported for the Open Hub Destination based extraction, where an RFC Server is not used.

SAP load balanced (message server) connection is not supported for the process chain based extraction. The reason is an SAP limitation when providing `data ready` notification to the client system, which requires registering the RFC Server (plugin listener) on each SAP Server in the BW landscape, increasing the footprint of the connector and potentially impacting SAP performance and resource usage. For more information, see [SAP Note 2572564](https://launchpad.support.sap.com/#/notes/2572564) (SAP support login required to view).

### Supported SAP deployment models

The plugin is tested with SAP servers deployed on Google Cloud.

### Supported SAP Objects

Data sources for Open Hub Destination: InfoProviders (InfoObject, InfoCube, DataStore Object, Advanced Data Store Object, Composite Provider)

Process Chains to automatically execute the Data Transfer Process into the Open Hub Destination.

### Separate license to use Oracle HTTP Server to extract data from SAP

You do not need a separate license to use [Oracle HTTP Server (OHS)](https://docs.oracle.com/en/middleware/fusion-middleware/web-tier/index.html) to extract data from SAP; however, check with your SAP representative on your specific agreement and use case.

### Expected plugin throughput

For an environment configured according to the guidelines in Optimize performance, the plugin can extract around 38 GB per hour. The actual performance might vary with the Cloud Data Fusion and SAP system load or network traffic.

## What's next

  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs).
  * Learn more about [SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
