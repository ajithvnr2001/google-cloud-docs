---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-sap-erp/
title: Configure the SAP ERP system \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:20.170899+00:00
---

# Configure the SAP ERP system  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-sap-erp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Configure the SAP ERP system Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure your SAP system to use one of the SAP plugins in Cloud Data Fusion.

## Install SAP plugin components in SAP using the SAP transport files

To use the SAP plugins in Cloud Data Fusion, add Remote Function Modules (RFMs) and Authorization Roles in your SAP system. The RFMs provide the extraction APIs called by the plugin in Cloud Data Fusion.

### Download the transport file

You get the required SAP code and configurations through SAP transport files, which are archived in a zip file.

The transport zip file is available for download when you [deploy SAP plugins in the Cloud Data Fusion Hub](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin#deploy-sap-plugin).

The transport zip file contains two zip files:

  * The _cofile_ , which has the following naming convention: `KSIX_DIGITS.SID`
  * The _data file_ , which has the following naming convention: `RSIX_DIGITS.SID`



Example:

### ODP

The following example shows the files in the SAP ODP transport zip file:

Zip filename | Transport request ID | Cofile | Datafile | Content  
---|---|---|---|---  
`Google_CDF_connector_SAP_ODP.zip` | `SIDK123456` | `K123456.SID` | `R123456.SID` | SAP RFMs in a Google namespace  
`Authorization_Role_SAP_ODP.zip` | `SIDK123456` | `K123456.SID` | `R123456.SID` | Authorization Role  
  
### Table

The following example shows the files in the SAP Table transport zip file:

Zip filename | Transport request ID | Cofile | Datafile | Content  
---|---|---|---|---  
`SAP_TABLE_READER_TR.zip` | `SIDK123456` | `K123456.SID` | `R123456.SID` | SAP RFMs in a Google namespace  
  
## Import the SAP transport files

To install the SAP transports, follow these steps:

  1. Sign in to the operating system of the SAP Instance.
  2. To get the path for the `DIR_TRANS` folder, use the SAP transaction code `AL11`. Typically, the path is `/usr/sap/trans/`.
  3. Copy the cofile to the `DIR_TRANS/cofiles` folder.
  4. Copy the data files to the `DIR_TRANS/data` folder.
  5. Set the User and Group of data and cofiles folders and files to `SIDadm` and `sapsys`.



An SAP administrator can import the transport request files by using the SAP transport management system or the operating system command line:

### Transport management

  1. Sign in to the SAP system as an SAP administrator.
  2. Enter the transaction `STMS`.
  3. Click **Overview > Imports**.
  4. In the **Queue** column, double-click the current SID.
  5. Click **Extras > Other Requests > Add**.
  6. Select the transport request ID and click **Continue**.
  7. Select the transport request in the import queue and click **Request > Import**.
  8. Enter the client number.
  9. On the **Options** tab, select **Overwrite Originals** and **Ignore Invalid Component Version** (if available).
  10. Optional: To plan for SAP system upgrades and backup restorations, you can choose to import the transports again later. Click **Leave Transports Requests in Queue for Later Import** and **Import Transport Requests Again**.
  11. Click **Continue**.
  12. Verify that the function module and authorization roles were imported successfully by using transactions, such as `SE80` and `PFCG`.



### SAP CLI

  1. Sign in to the SAP system as an SAP administrator.
  2. Add requests to the import buffer:
         
         tp addtobuffer TRANSPORT_REQUEST_ID SID
         

Replace the following:

     * `TRANSPORT_REQUEST_ID` with the transport request ID
     * `SID` with the SAP ID

Example: `tp addtobuffer IB1K903958 DD1`

  3. Import the transport requests:
         
         tp import TRANSPORT_REQUEST_ID SID client=CLIENT_NUMBER U1238
         

Replace `CLIENT_NUMBER` with the client number.

Example: `tp import IB1K903958 DD1 client=800 U1238`

**Note:** `U1238` indicates to set the options described in steps 9-10 in the Transport management tab on this page. The numbers indicate the corresponding option order number in the SAP user interface, which might vary by system. The numbers must be adjusted by an SAP administrator.
  4. Verify that the function module and authorization roles were imported successfully by using appropriate transactions, such as `SE80` and `PFCG`.




After the transport is imported into the SAP system, the following SAP objects are created:

### ODP plugin

  * RFC-enabled function modules: 
    * `/GOOG/ODP_DS_EXTRACT_DATA_V2`
    * `/GOOG/ODP_DS_FETCH_DATA_V2`
    * `/GOOG/ODP_DS_METADATA_V2`
    * `/GOOG/ODP_REPL_CLEANUP_V2`
  * Authorization Role: `/GOOG/ODP_AUTH`



### Table plugin

  * RFC-enabled function modules: 
    * `/GOOG/RFC_READ_TABLE`
    * `/GOOG/RFC_READ_TABLE_SNAPSHOT`
    * `/GOOG/RFC_READ_TABLE_CLEANUP`
    * `/GOOG/RFC_READ_TABLE_JOBSTATUS`
    * `/GOOG/RFC_TABLE_STAGE_READ`
    * `/GOOG/RFC_GET_PACKAGE_SIZE`
    * `/GOOG/RFC_GET_TABLE_LIST`



## Set up authorizations in SAP

To set up user authorizations in SAP, either assign the ODP authorization role that's included in the transport file, or manually create an authorization role.

### From Transport

### SAP ODP plugin

In SAP, assign the Authorization Role, `/GOOG/ODP_AUTH`, which is included in the SAP transports you download when you deploy the SAP ODP plugin.

### Create

To create the Authorization Role manually, follow these steps:

  1. In the SAP GUI, enter the transaction code `PFCG`. The **Role Maintenance** window opens.
  2. In the **Role** field, enter a name for the role—for example, `zcdf_role`.
  3. Click **Single Role**. The **Create Roles** window opens.
  4. In the **Description** field, enter a description—for example, `Authorizations for ODP plugin` or `Authorizations for Table plugin`.
  5. Click **Save**.
  6. Click the **Authorizations** tab. The title of the window changes to **Change Roles**.
  7. In the **Edit Authorization Data and Generate Profiles** section, click edit **Change Authorization Data**. The **Choose Template** window opens.
  8. Click **Do not select templates**. The **Change role: Authorizations** window opens.
  9. Click **Manually**.
  10. Provide the authorizations shown in the following SAP Authorization table.
  11. Click **Save**.
  12. To activate the Authorization Role, click the **Generate** icon.



SAP Authorizations include the following: 

### ODP

**Note:** To restrict a user from running ODP pipelines with specific DataSources, for authorization object S_RO_OSOA, provide the required DataSource names in OLTPSOURCE (for example, `2LIS_02_ITM`, `0MATERIAL_ATTR`). Don't use `*`.

The following authorizations apply for the ODP plugin:

Object class | Object class text | Authorization object | Authorization object text | Authorization | Text | Value  
---|---|---|---|---|---|---  
`AAAB` | `Cross-application Authorization Objects` | `S_RFC` | `Authorization Check for RFC Access` | `ACTVT` | `Activity` | `16`  
`AAAB` | `Cross-application Authorization Objects` | `S_RFC` | `Authorization Check for RFC Access` | `RFC_NAME` | `Name of RFC object to which access is allowed` | 

  * `/GOOG/CDF_ODP_FG`
  * `/GOOG/ODP_DS_EXTRACT_DATA`
  * `/GOOG/ODP_DS_FETCH_DATA`
  * `/GOOG/ODP_DS_METADATA`
  * `DDIF_FIELDINFO_GET`
  * `RFCPING`
  * `RFC_GET_FUNCTION_INTERFACE`
  * `RODPS_REPL_ODP_CLOSE`
  * `RODPS_REPL_SOURCES_GET_LIST`
  * `SAPTUNE_GET_SUMMARY_STATISTIC`
  * `TH_WPINFO`

  
`AAAB` | `Cross-application Authorization Objects` | `S_RFC` | `Authorization Check for RFC Access` | `RFC_TYPE` | `Type of RFC object to which access is allowed` | 

  * `FUGR`
  * `FUNC`

  
`AAAB` | `Cross-application Authorization Objects` | `S_TCODE` | `Transaction Code Check at Transaction Start` | `TCD` | `Transaction Code` | `SM50`  
`BC_A` | `Basis: Administration` | `S_ADMI_FCD` | `System Authorizations` | `S_ADMI_FCD` | `System administration function` | 

  * `PADM`
  * `ST0R`

  
`BC_A` | `Basis: Administration` | `S_BTCH_ADM` | `Background Processing: Background Administrator` | `BTCADMIN` | `Background Administrator ID` | `Y`  
`BC_A` | `Basis: Administration` | `S_BTCH_JOB` | `Background Processing: Operations on Background Jobs` | `JOBACTION` | `Job operations` | `RELE`  
`BC_A` | `Basis: Administration` | `S_BTCH_JOB` | `Background Processing: Operations on Background Jobs` | `JOBGROUP` | `Summary of jobs for a group` | `''`  
`MM_E` | `Materials Management: Purchasing` | `M_BEST_BSA` | `Document Type in Purchase Order` | `ACTVT` | `Activity` | `03`  
`MM_E` | `Materials Management: Purchasing` | `M_BEST_BSA` | `Document Type in Purchase Order` | `BSART` | `Purchasing Document Type` | `*`  
`RO` | `Authorizations: BW Service API` | `S_RO_OSOA` | `SAP DataSource Authorizations` | `ACTVT` | `Activity` | `03`  
`RO` | `Authorizations: BW Service API` | `S_RO_OSOA` | `SAP DataSource Authorizations` | `OLTPSOURCE` | `DataSource (OSOA/OSOD)` | `*`  
`RO` | `Authorizations: BW Service API` | `S_RO_OSOA` | `SAP DataSource Authorizations` | `OSOAAPCO` | `Application Component of a DataSource (OSOA/OSOD)` | `*`  
`RO` | `Authorizations: BW Service API` | `S_RO_OSOA` | `SAP DataSource Authorizations` | `OSOAPART` | `Subobject for DataSource` | `DATA`  
  
### Table

The following authorizations apply for the Table plugin:

Object class | Object class text | Authorization object | Authorization object text | Authorization | Text | Value  
---|---|---|---|---|---|---  
`AAAB` | `Cross-application Authorization Objects` | `S_RFC` | `Cross-application Authorization Objects` | `ACTVT` | `Activity` | `16`  
`AAAB` | `Cross-application Authorization Objects` | `S_RFC` | `Authorization Check for RFC Access` | `RFC_NAME` | `Name of RFC object to which access is allowed` | 

  * `/GOOG/RFC_READ_TABLE`
  * `DDIF_FIELDINFO_GET`
  * `RFC_GET_FUNCTION_INTERFACE`
  * `RFCPING`
  * `SAPTUNE_GET_SUMMARY_STATISTIC`
  * `TH_WPINFO`

  
`AAAB` | `Cross-application Authorization Objects` | `S_RFC` | `Cross-application Authorization Objects` | `RFC_TYPE` | `Type of RFC object to which access is allowed` | `FUNC`  
`AAAB` | `Cross-application Authorization Objects` | `S_TCODE` | `Transaction Code Check at Transaction Start` | `TCD` | `Transaction Code` | `SM50`  
`BC_A` | `Basis: Administration` | `S_ADMI_FCD` | `System Authorizations` | `S_ADMI_FCD` | `System administration function` | `ST0R`  
`BC_A` | `Basis: Administration` | `S_TABU_NAM` | `Table Access by Generic Standard Tools` | `ACTVT` | `Activity` | `03`  
`BC_A` | `Basis: Administration` | `S_TABU_NAM` | `Table Access by Generic Standard Tools` | `TABLE` | `Table Name` | `*`  
  
## Set up the SAP Java Connector

[Download the following SAP Java Connector (SAP JCo) artifacts](http://service.sap.com/connectors). The minimum supported JCo version is `3.0.20`.

  * One platform-independent (`sapjco3.jar`)
  * One platform-dependent (`libsapjco3.so` on Unix)



Copy the files to the Cloud Storage bucket.

## For ODP: Activate data sources for extraction

To extract the data, a DataSource must be activated in the source SAP system. To activate a DataSource in SAP, follow these steps:

  1. Sign into the SAP system.
  2. Go to the transaction code `RSA5`.
  3. Expand the **DataSources** list.

     1. Open the CDS view in the SAP CDS Editor.
     2. In the CDS view, look for the following annotations:

        * `@Analytics.dataCategory`
        * `@Analytics.dataExtraction.enabled`

If the CDS view has both of these annotations, then it's exposed for ODP data extraction. Without them, it isn't exposed.

  4. Click **Search**.

  5. Provide the DataSource name and click check_circle **Enter**.

  6. If the search is successful, the DataSource appears in the result list.

Select the DataSource name and click check_circle **Enter**.

  7. Select the DataSource and click **Activate DataSources**.

  8. In the **Create Object Directory Entry** dialog, enter the Package name and click **Save**.

  9. In the **Prompt for transportable workbench request** dialog, enter the Transport Number in the **Request** field. Click check_circle **Enter**.

The selected DataSource is activated in SAP.




### Check that the DataSource is exposed for extraction

  1. Sign in to the SAP system.
  2. Go to t-code `SE16N`.
  3. Enter the table name, `ROOSATTR`, and enter the DataSource name in `OLTPSOURCE`.
  4. Click **Execute** or press F8.
  5. If the **EXPOSE_EXTERNAL** field has an `X`, the DataSource is exposed and ready for extraction.



If the DataSource doesn't appear in the `ROOSATTR` table, or the **EXPOSE_EXTERNAL** field is blank, follow these steps to expose the DataSource for ODP extraction:

  1. Sign in to the SAP system.
  2. Go to t-code `SA38`.
  3. Enter the program name, `RODPS_OS_EXPOSE`, and click **Execute**.
  4. Enter the DataSource name and click **Release DataSource**.
  5. Save the changes in the transport.



## What's next

  * [Configure the SAP ODP plugin in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/how-to/use-sap-odp-plugin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
