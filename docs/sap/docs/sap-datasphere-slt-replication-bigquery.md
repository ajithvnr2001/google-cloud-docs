---
url: https://docs.cloud.google.com/sap/docs/sap-datasphere-slt-replication-bigquery/
title: Set up SLT-based replication: SAP S/4HANA to BigQuery through SAP Datasphere \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:27.172449+00:00
---

# Set up SLT-based replication: SAP S/4HANA to BigQuery through SAP Datasphere  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-datasphere-slt-replication-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Set up SLT-based replication: SAP S/4HANA to BigQuery through SAP Datasphere Stay organized with collections  Save and categorize content based on your preferences. 

With the [Replication Flow](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/25e2bd7a70d44ac5b05e844f9e913471.html) feature of SAP Datasphere, you can replicate data from SAP S/4HANA to BigQuery.

This guide explains how to replicate data from SAP S/4HANA to BigQuery through SAP Datasphere when you're using [SAP LT Replication Server (SLT)-based](https://help.sap.com/docs/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/007c373fcacb4003b990c6fac29a26e4/8e02678447fc4c1e8eeaf72f53716685.html) replication for SAP S/4HANA.

The high-level steps are as follows:

  1. Connect SAP Datasphere to the SAP S/4HANA source system.
  2. Connect SAP Datasphere to the Google Cloud project that contains the target BigQuery dataset.
  3. Create a replication flow.
  4. Run the replication flow.
  5. Validate the replicated data in BigQuery.



For information about setting up CDS-based replication, see [Set up CDS-based replication: SAP S/4HANA to BigQuery through SAP Datasphere](https://docs.cloud.google.com/sap/docs/sap-datasphere-cds-replication-bigquery). 

## Before you begin

Before you begin, make sure that you or your administrators have completed the following prerequisites:

  * In the **Tenant Configuration** page of your SAP Datasphere tenant, enable the **Premium Outbound Integration** blocks. For information about how to do this, see the SAP documentation [Configure the Size of Your SAP Datasphere Tenant](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/33f8ef4ec359409fb75925a68c23ebc3.html).

  * Validate the latest considerations and limitation of SAP Datasphere replication flows provided in the [SAP Note 3297105 - Important considerations for SAP Datasphere Replication Flows](https://me.sap.com/notes/3297105).

  * Review the information about the required SAP software versions, recommended system landscape, considerations for the supported source objects, and more, provided in the [SAP Note 2890171 - SAP Data Intelligence / SAP Datasphere - ABAP Integration](https://me.sap.com/notes/2890171).

  * The SLT that is embedded in SAP S/4HANA is supported by SAP Datasphere replication flows only starting from SAP S/4HANA 2022. If you're using an earlier version of SAP S/4HANA, or an older NetWeaver-based SAP application such as SAP ECC, then you need to consider a standalone SLT server. For information about the required SAP software versions, recommended system landscape, considerations for the supported source objects, and more, see the [SAP Note 2890171 - SAP Data Intelligence / SAP Datasphere - ABAP Integration](https://me.sap.com/notes/2890171). 

  * You have a Google Cloud account and project.

  * Billing is enabled for your project. For more information, see [how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * Make sure that the BigQuery API is enabled in your Google Cloud project.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/bigquery.googleapis.com)




## Connect SAP Datasphere to the SAP S/4HANA source system

This section provides instructions to establish a connection between SAP Datasphere and the SAP S/4HANA source system.

### Install SAP Cloud Connector

To securely connect your SAP Datasphere tenant to the SAP S/4HANA source system, [SAP Cloud Connector](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/cloud-connector) is required when your SAP S/4HANA source system is running on-premises, hosted on any cloud environment, or if you're using the SAP S/4HANA Cloud Private Edition. However, if you're using the SAP S/4HANA Cloud Public Edition, then the SAP Cloud Connector is not needed. In that case, skip the SAP Cloud Connector installation and configuration, and move to Create a connection to the SAP S/4HANA source system.

If your SAP S/4HANA source system is running on-premises or hosted on any cloud environment, then you need to install and configure the SAP Cloud Connector on your operating system (OS). For information about OS-specific requirements and instructions to install SAP Cloud Connector, see the SAP documentation [Preparing Cloud Connector Connectivity](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/35141e7668774958b5e59495f7a7828e.html).

If you're using the SAP S/4HANA Cloud Private Edition, then the SAP Cloud Connector is pre-installed as part of the SAP S/4HANA setup. In that case, skip the SAP Cloud Connector installation, and move to Configure SAP Cloud Connector.

### Configure SAP Cloud Connector

You configure SAP Cloud Connector to specify the SAP Datasphere subaccount, mapping to the SAP S4/HANA source system in your network, and the accessible resources.

This section highlights the most important steps involved in configuring SAP Cloud Connector. For detailed information about configuring SAP Cloud Connector, see the SAP documentation [Configure Cloud Connector](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/f289920243a34127b0c8b13012a1a4b5.html).

The most important steps are as follows:

  1. In your web browser, access the SAP Cloud Connector administration UI using the host where your SAP Cloud Connector is installed and the port. For example: <http://localhost:8443>.

  2. Log in to SAP Cloud Connector. If you're logging in for the first time after installing SAP Cloud Connector, then use the following default credentials:

     * Username: `Administrator`
     * Password: `manage`

Before proceeding, change the default password. For more information, see the SAP documentation [Initial Configuration](https://help.sap.com/docs/connectivity/sap-btp-connectivity-cf/cloud-connector-initial-configuration).

  3. Specify the following details to connect your SAP Cloud Connector to your SAP BTP subaccount:

     * Details about your SAP Datasphere subaccount, including the subaccount name, region, and subaccount user. For more information about these fields, see the SAP documentation [Configure Cloud Connector](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/f289920243a34127b0c8b13012a1a4b5.html).
     * For the specified subaccount, a location ID that identifies the location of your SAP Cloud Connector.
  4. To provide access to the SAP S/4HANA source system, add the system mapping information, including information about the internal host and the virtual host system.

  5. For accessing data based on tables with SAP LT Replication Server, you must specify the following resources:

     * LTAMB_ -**Prefix**
     * LTAPE_ -**Prefix**
     * RFC_FUNCTION_SEARCH 
  6. Save your configuration.




### Create a mass transfer configuration

Before running the replication from SAP S/4HANA using SLT, you need to create a mass transfer configuration to specify details of your source system connection, target system connection, and transfer settings.

To create a mass transfer configuration, perform the following steps:

  1. In the SAP GUI, enter transaction code `LTRC`.

  2. Click the **Create configuration** icon. The **Create Configuration** wizard opens.

  3. In the **Configuration Name** and **Description** fields, enter a name and a description for the configuration, and then click **Next**.

  4. In the **Source System Connection Details** panel:

     * Select the **RFC Connection** radio button.
     * In the **RFC Destination** field, specify the name of the RFC connection to the SAP S/4HANA source system.

**Note:** Create an RFC destination in transaction `SM59` that points to the SAP S/4HANA system. For instructions, see the SAP documentation [Creating an RFC Destination in the ABAP System](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/4c/4c3b85a12f6f83e10000000a42189e/frameset.htm).
     * Select the checkboxes for **Allow Multiple Usage** and **Read from Single Client** as appropriate. For more information about these options, see the [SAP LT Replication Server documentation](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

     * Click **Next**.

  5. In the **Target System Connection Details** panel:

     * Select the radio button for **Other**.
     * In the **Scenario** field, select **SAP Data Intelligence (Replication Management service)**.
     * Click **Next**.
  6. On the **Specify Transfer Settings** panel:

     1. In the **Data Transfer Settings** section, for the **Initial Load Mode** field, select **Performance Optimized**.

     2. In the **Job options** section, enter starting values for the following fields:

        * **Number of Data Transfer Jobs**
        * **Number of Initial Load Jobs**
        * **Number of Calculation Jobs**
     3. In the **Replication Options** section, select the **Real Time** radio button.

     4. Click **Next**.

  7. Review the configuration, and click **Save**.

  8. Make a note of the three-digit ID in the **Mass Transfer** column. You use it in a later step.




### Create a connection to the SAP S/4HANA source system

In SAP Datasphere, create a source connection to use the SAP S/4HANA source system for data access. You use this connection to create replication flows.

To create a connection to the SAP S/4HANA source system, perform the following steps:

  1. In SAP Datasphere, go to **Data Builder** , and click **New Connection**.

  2. Select the connection type **SAP ABAP**.

  3. Specify the following connection properties:

     * **Protocol** : select **RFC**.
     * **SAP Logon Connection Type** : select **Application Server**.
     * **Use Cloud Connector** : set to **True**.
  4. Specify other properties specific for your application server and SAP system. For more information, see the SAP documentation [SAP ABAP Connections](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/a75c1aacf951449ba3b740c7e46da3a9.html).

  5. To validate the connection between SAP Datasphere and SAP S/4HANA, select your connection, and click the **Validate Connection** icon.




For more information about how to create a connection between SAP Datasphere and SAP S/4HANA, see the SAP documentation [Create a Connection](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/c2165842082c43fc85bad9f0c97572bb.html).

Before you can use the connection for replication flows, check the SAP Notes relevant to replication flows and implement any necessary note on your SAP S/4HANA system. For more information about the required SAP Notes, see:

  * SAP Notes listed under the section [Replication Flows](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/8de01dd25c1e443e8e2de7d2fbe1364d.html?locale=en-US#replication-flows).
  * SAP Notes listed under the section [Source Systems for SAP Data Intelligence](https://help.sap.com/docs/data-intelligence-cloud/sap-data-intelligence-administration/replication-flow-connections#source-systems-for-sap-data-intelligence).



## Connect SAP Datasphere to Google Cloud project

This section provides instructions to establish a connection between SAP Datasphere and your Google Cloud project that contains the target BigQuery dataset.

### Create a service account

For the authentication and authorization of SAP Datasphere, you need an IAM service account in your Google Cloud project. You grant roles to the service account that contains permissions to interact with BigQuery.

You also need to create a JSON key for the service account. You upload the JSON key to SAP Datasphere to authenticate with Google Cloud.

To create a service account, perform the following steps:

  1. In the Google Cloud console, go to the IAM & Admin **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. If prompted, select your Google Cloud project.

  3. Click **Create Service Account**.

  4. Specify a name for the service account and, optionally, a description.

  5. Click **Create and Continue**.

  6. In the **Grant this service account access to project** panel, select the following roles:

     * **BigQuery Data Owner**
     * **BigQuery Job User**
  7. Click **Continue**.

  8. Click **Done**. The service account appears in the list of service accounts for the project.




#### Download JSON key for the service account

To download a JSON key for the service account, perform the following steps:

  1. Click the email address of the service account that you want to create a key for.
  2. Click the **Keys** tab.
  3. Click the **Add key** drop-down menu, then select **Create new key**.
  4. Select **JSON** as the **Key type** and click **Create**.



Clicking **Create** downloads a service account key file. Make sure to store the key file securely, because it can be used to authenticate as your service account. For more information, see [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).

### Create a BigQuery dataset

To create a BigQuery dataset, your user account must have the proper IAM permissions for BigQuery. For more information, see [Required permissions](https://docs.cloud.google.com/bigquery/docs/datasets#required_permissions).

To create a BigQuery dataset, perform the following steps:

  1. In the Google Cloud console, go to the **BigQuery** page:

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Next to your project ID, click the **View actions** icon, more_vert, and then **Create dataset**.

  3. In the **Dataset ID** field, enter a unique name. For more information, see [Name datasets](https://docs.cloud.google.com/bigquery/docs/datasets#dataset-naming).

  4. In the **Location type** field, choose a geographic [location](https://docs.cloud.google.com/bigquery/docs/locations) for the dataset that one you are planning to utilize. After a dataset is created, the location can't be changed.




For more information about how to create BigQuery datasets, see [Create datasets](https://docs.cloud.google.com/bigquery/docs/datasets).

### Upload TLS/SSL certificates to SAP Datasphere

To encrypt the data transmitted between SAP and Google Cloud, you need to upload the required Google TLS/SSL certificates to SAP Datasphere.

To upload the TLS/SSL certificates, perform the following steps:

  1. For connecting to Google services, follow the [Google Trust Services advice](https://pki.goog/faq/#connecting-to-google). At a minimum, you must download all root CA certificates from the [Google Trust Services repository](https://pki.goog/repository/).

To ensure that you're using the latest trusted root CA certificates, we recommend that you update your system's root certificate store every six months. Google announces new and removed root CA certificates at [Google Trust Services](https://pki.goog/updates/). For receiving automatic notifications, subscribe to the RSS feed on [Google Trust Services](https://pki.goog/updates/).

  2. In the SAP Datasphere, go to **System > Configuration > Security**.

  3. Click **Add Certificate**.

  4. Browse your local directory and select the certificates that you downloaded from the Google Trust Services repository.

  5. Click **Upload**.




For more information from SAP about uploading certificates to SAP Datasphere, see [Manage Certificates for Connections](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/46f5467adc5242deb1f6b68083e72994.html).

### Upload the driver for BigQuery to SAP Datasphere

The BigQuery ODBC driver acts as a bridge between SAP Datasphere and BigQuery for replication flows. To enable access to BigQuery, you need to upload the required ODBC driver files to SAP Datasphere.

For more information from SAP about uploading the required ODBC driver files to SAP Datasphere, see [Upload Third-Party ODBC Drivers (Required for Data Flows)](https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/b9b5579054df48c39381d5b17286bf21.html).

To upload the driver files, perform the following steps:

  1. From [ODBC and JDBC drivers for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers), download the required BigQuery ODBC driver.

  2. In the SAP Datasphere, go to **System > Configuration > Data Integration**.

  3. Go to **Third-Party Drivers** and click **Upload**.

  4. Browse your local directory and select the driver file that you downloaded from [ODBC and JDBC drivers for BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/odbc-jdbc-drivers).

  5. Click **Upload**.

  6. Click **Sync** to synchronize the driver changes. After the synchronization is finished, you can use data flows with the connection.




### Create a connection to Google Cloud project

To replicate data from your SAP S/4HANA source system to the target BigQuery dataset, you need to create a replication flow in your SAP Datasphere tenant.

To create a connection to Google Cloud project, perform the following steps:

  1. In SAP Datasphere, go to **Connections** , and create a new connection in your space.

  2. Choose the connection type as **Google BigQuery**.

  3. In the **Connection details** sections, specify the following:

     * **Project ID** : enter your Google Cloud project ID in lowercase.
     * **Location** : enter your Google Cloud project location.
  4. In the **Credential** section, upload the JSON key file that is used for authentication. For more information, see Download JSON key for the service account.

  5. To validate the connection between SAP Datasphere and BigQuery, select your connection, and click the **Validate Connection** icon.




For more information from SAP about the connection to connect to and access data from BigQuery, see [Google BigQuery Connections](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/30ed77de13864368bdc596099b37ed70.html).

## Create a replication flow

You create a replication flow to copy SAP data from your SAP S/4HANA source system to the target BigQuery dataset.

To create a replication flow through SLT, perform the following steps:

  1. In SAP Datasphere, go to **Data Builder** , and click **New Replication Flow**.

  2. Specify the source for your replication flow:

     1. Select the source connection of the type **SAP ABAP** that you created in the section Create a connection to the SAP S/4HANA source system.

     2. Select **SLT-SAP LT Replication Server** as a source container, and then add the mass transfer ID of your configuration that you created in the section Create a mass transfer configuration.

     3. Add source objects as required.

For more information, see the SAP documentation [Add a Source](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/749638060e8746e48b0f9bf0e50c6d0c.html).

  3. Select one of the load types: **Initial only** or **Initial and delta**.

  4. Specify the target environment for your replication flow:

     1. Select the connection to the Google Cloud project that contains the target BigQuery dataset.

     2. Select the container, which is the dataset in BigQuery, to which you want to replicate your data.

For more information, see the SAP documentation [Add a Target](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/ab490fb4d083442197e2ba3b92079734.html).

  5. Create mappings to specify how the source data is to be changed on its way into the target. For more information, see the SAP documentation [Define Mapping](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/2c7948fdd1a14105a27d0c03af82a56b.html).

  6. Save the replication flow.

  7. Deploy the replication flow.




For more information, see the SAP documentation [Creating a Replication Flow](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/25e2bd7a70d44ac5b05e844f9e913471.html).

## Run the replication flow

Once your replication flow is configured and deployed, you can run it.

  * To run a replication flow, select the replication flow, and click **Run**.

Once completed, the **Run Status** section in the **Property** panel is updated. For more information, see the SAP documentation [Running a flow](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/5b591d4998fa4a148750016a29ada91e.html).




### Monitor replication flow status

You can view and monitor the execution details of replication flows.

To monitor replication flow status, perform the following steps:

  1. In the SAP Datasphere, go to **Data Integration Monitor > Flows**.

  2. Select a flow run in the left panel to view its details.




For more information, see the SAP documentation [Monitoring flows](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/b661ea0766a24c7d839df950330a89fd.html).

## Validate the replicated data in BigQuery

After the replication flow run is complete, validate the replicated table and data in BigQuery.

To validate the replicated data in BigQuery, perform the following steps:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** section, expand your project to view the dataset and its tables.

  3. Select the required table. The table information is displayed under a tab in the content pane on the right side of the page.

  4. In the table information section, click the following headings to view the SAP data:

     * **Preview** : shows the data replicated from the SAP S/4HANA source system.
     * **Details** : shows the table size, the total number of rows, and other details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
