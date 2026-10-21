---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-install-files/
title: Prepare SAP installation files for deployment \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:32.715181+00:00
---

# Prepare SAP installation files for deployment  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-install-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Prepare SAP installation files for deployment Stay organized with collections  Save and categorize content based on your preferences. 

The installation files required for your SAP system must be stored in a Cloud Storage bucket before you deploy the SAP workload using Workload Manager.

This document lists all the required SAP installation files for deployment and it also describes the procedure to upload the files to Cloud Storage.

## Before you begin

To prepare the SAP installation files, you need the following:

  * [SAP Support Portal](http://support.sap.com) account and access to download files. If your SAP account does not allow access to the software, contact the [SAP Global Support Customer Interaction Center](http://support.sap.com/contactus).
  * Enable Cloud Storage API in the project where you're deploying the SAP workload.



## Download SAP installation files

  1. Open the [SAP Software Download Center](http://support.sap.com/swdc). Make sure that you're logged in and you've access to download the SAP software.
  2. Review the list of SAP S/4HANA files and download all the required files for your SAP product version.

     1. Click the direct link to the SAP file in the table.
     2. Navigate to your Download Basket and confirm that it lists all the required files.
     3. Select all files and then download these files to an accessible location.

**Note:** Don't extract or modify the files after downloading.



## Upload the installation files to your Cloud Storage bucket

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) for storing the SAP HANA installation files. Note that the bucket name must be unique across Google Cloud.
  2. Configure bucket permissions for the new bucket. To give access, see [Using IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).
  3. Upload all SAP S/4HANA files to the bucket you created. For more information, see [upload objects to a bucket](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object) Make sure that you upload only the required files, and not any folders or files that you might have downloaded.

Note the name of the bucket that you uploaded the binaries to. You need to use it when you deploy the SAP S/4HANA application.




## SAP S/4HANA files

The following table lists the installation files required for SAP S/4HANA. Note that the filenames listed in the column **Example Filename** are for reference only and it includes the latest filename as of April 4, 2024. You must use the latest version of the file, if applicable.

Workload Manager: Guided Deployment Automation tool has been tested for the specific versions of each component listed in the following table. The table lists the preferred versions of the SAP products. The installation process of the Guided Deployment Automation tool uses wildcard matches. Therefore, alternative product versions might also work but requires additional support and troubleshooting.

For example, the preferred SAP Host Agent version is V7.22, but you can upload version V7.21 of SAP Host Agent as long as the file format matches the wildcard of `SAPHOSTAGENT*.SAR`. If you accidentally upload multiple versions of the same file, Workload Manager attempts to use the latest version.

The following table lists SAP products for Linux x86_64, unless specified otherwise.

### SAP S/4HANA 2021

**Component** | **Version** | **Example Filename**  
(Example shows latest file as of April 4, 2024) | **Link to SAP Software Download Center** | **Min Version** | **Wildcard match**  
---|---|---|---|---|---  
SAP HANA Platform Edition | V2 SPS05+ | 51056441.ZIP | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0030000000139442023) | Revision 59.0 for SPS05 | Known files:  
51054623.ZIP  
51056441.ZIP  
51056451.ZIP  
HANA Server | V2 SPS05+ | IMDB_SERVER20_059_12-80002031.SAR | [link](https://me.sap.com/softwarecenter/object/0020000000259442024) | Revision 53.0 for SPS05 | IMDB_SERVER*.SAR  
HANA Client | V2.5 | IMDB_CLIENT20_005_111-80002082.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001649042020) | Patch 110 | IMDB_CLIENT20*.SAR  
SAPCAR | V7.22 | SAPCAR_1115-70006178.EXE | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000098642022) | Patch 1115 | SAPCAR*.*  
SAP Host Agent | V7.22 | SAPHOSTAGENT56_56-80004822.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000591682022) | SP56 | SAPHOSTAGENT*.SAR  
Kernel Part I | 7.85 64-BIT Unicode | SAPEXE_200-80005374.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001080892022) | Patch Level 75 | SAPEXE_*.SAR  
Kernel Part II | 7.85 64-BIT Unicode | SAPEXEDB_200-80005373.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001080682022) | Patch Level 75 | SAPEXEDB_*.SAR  
IGS | V7.81 | igsexe_3-70005417.sar | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000632872023) | Patch 1 | igsexe_*.sar  
IGS Fonts & Textures | Latest | igshelper_17-10010245.sar | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000703122018) | Patch 17 | igshelper_*.sar  
SWPM | V2.0 | SWPM20SP17_2-80003424.SAR | [link](https://me.sap.com/softwarecenter/object/0020000000394222024) | SP10 | SWPM20SP*.SAR  
S/4HANA Exports | S/4HANA 2021 (Core106) | S4CORE106_INST_EXPORT_1.zip | [link](https://launchpad.support.sap.com/#/softwarecenter/search/S4CORE106_INST_EXPORT_)  
  
Select all and click the cart icon to add all files to the basket. |  | Must match exactly as shown.  
S4CORE106_INST_EXPORT_2.zip  
S4CORE106_INST_EXPORT_3.zip  
S4CORE106_INST_EXPORT_4.zip  
S4CORE106_INST_EXPORT_5.zip  
S4CORE106_INST_EXPORT_6.zip  
S4CORE106_INST_EXPORT_7.zip  
S4CORE106_INST_EXPORT_8.zip  
S4CORE106_INST_EXPORT_9.zip  
S4CORE106_INST_EXPORT_10.zip  
S4CORE106_INST_EXPORT_11.zip  
S4CORE106_INST_EXPORT_12.zip  
S4CORE106_INST_EXPORT_13.zip  
S4CORE106_INST_EXPORT_14.zip  
S4CORE106_INST_EXPORT_15.zip  
S4CORE106_INST_EXPORT_16.zip  
S4CORE106_INST_EXPORT_17.zip  
S4CORE106_INST_EXPORT_18.zip  
S4CORE106_INST_EXPORT_19.zip  
S4CORE106_INST_EXPORT_20.zip  
S4CORE106_INST_EXPORT_21.zip  
S4CORE106_INST_EXPORT_22.zip  
S4CORE106_INST_EXPORT_23.zip  
S4CORE106_INST_EXPORT_24.zip  
S4CORE106_INST_EXPORT_25.zip  
S4CORE106_INST_EXPORT_26.zip  
S4CORE106_INST_EXPORT_27.zip  
S4CORE106_INST_EXPORT_28.zip  
  
### SAP S/4HANA 2022

**Component** | **Version** | **Example Filename**  
(Example shows latest file as of April 4, 2024) | **Link to SAP Software Download Center** | **Min Version** | **Wildcard match**  
---|---|---|---|---|---  
SAP HANA Platform Edition | V2 SPS05+ | 51056441.ZIP | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0030000000139442023) | Revision 59.0 for SPS05 | Known files:  
51054623.ZIP  
51056441.ZIP  
51056451.ZIP  
HANA Server | V2 SPS05+ | IMDB_SERVER20_059_12-80002031.SAR | [link](https://me.sap.com/softwarecenter/object/0020000000259442024) | Revision 53.0 for SPS05 | IMDB_SERVER*.SAR  
HANA Client | V2.5 | IMDB_CLIENT20_005_111-80002082.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001649042020) | Patch 110 | IMDB_CLIENT20*.SAR  
SAPCAR | V7.22 | SAPCAR_1115-70006178.EXE | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000098642022) | Patch 1115 | SAPCAR*.*  
SAP Host Agent | V7.22 | SAPHOSTAGENT56_56-80004822.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000591682022) | SP56 | SAPHOSTAGENT*.SAR  
Kernel Part I | 7.85 64-BIT Unicode | SAPEXE_200-80005374.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001080892022) | Patch Level 75 | SAPEXE_*.SAR  
Kernel Part II | 7.85 64-BIT Unicode | SAPEXEDB_200-80005373.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001080682022) | Patch Level 75 | SAPEXEDB_*.SAR  
IGS | V7.81 | igsexe_3-70005417.sar | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000632872023) | Patch 1 | igsexe_*.sar  
IGS Fonts & Textures | Latest | igshelper_17-10010245.sar | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000703122018) | Patch 17 | igshelper_*.sar  
SWPM | V2.0 | SWPM20SP17_2-80003424.SAR | [link](https://me.sap.com/softwarecenter/object/0020000000394222024) | SP10 | SWPM20SP*.SAR  
S/4HANA Exports | S/4HANA 2022 (Core107) | S4CORE107_INST_EXPORT_1.zip | [link](https://launchpad.support.sap.com/#/softwarecenter/search/S4CORE107_INST_EXPORT_)  
  
Select all and click the cart icon to add all files to the basket. |  | Must match exactly as shown.  
S4CORE107_INST_EXPORT_2.zip  
S4CORE107_INST_EXPORT_3.zip  
S4CORE107_INST_EXPORT_4.zip  
S4CORE107_INST_EXPORT_5.zip  
S4CORE107_INST_EXPORT_6.zip  
S4CORE107_INST_EXPORT_7.zip  
S4CORE107_INST_EXPORT_8.zip  
S4CORE107_INST_EXPORT_9.zip  
S4CORE107_INST_EXPORT_10.zip  
S4CORE107_INST_EXPORT_11.zip  
S4CORE107_INST_EXPORT_12.zip  
S4CORE107_INST_EXPORT_13.zip  
S4CORE107_INST_EXPORT_14.zip  
S4CORE107_INST_EXPORT_15.zip  
S4CORE107_INST_EXPORT_16.zip  
S4CORE107_INST_EXPORT_17.zip  
S4CORE107_INST_EXPORT_18.zip  
S4CORE107_INST_EXPORT_19.zip  
S4CORE107_INST_EXPORT_20.zip  
S4CORE107_INST_EXPORT_21.zip  
S4CORE107_INST_EXPORT_22.zip  
S4CORE107_INST_EXPORT_23.zip  
S4CORE107_INST_EXPORT_24.zip  
S4CORE107_INST_EXPORT_25.zip  
S4CORE107_INST_EXPORT_26.zip  
S4CORE107_INST_EXPORT_27.zip  
S4CORE107_INST_EXPORT_28.zip  
S4CORE107_INST_EXPORT_29.zip  
S4CORE107_INST_EXPORT_30.zip  
  
### SAP S/4HANA 2023

**Component** | **Version** | **Example Filename**  
(Example shows latest file as of April 4, 2024) | **Link to SAP Software Download Center** | **Min Version** | **Wildcard match**  
---|---|---|---|---|---  
SAP HANA Platform Edition | V2 SPS05+ | 51056441.ZIP | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0030000000139442023) | Revision 59.0 for SPS05 | Known files:  
51054623.ZIP  
51056441.ZIP  
51056451.ZIP  
HANA Server | V2 SPS05+ | IMDB_SERVER20_059_12-80002031.SAR | [link](https://me.sap.com/softwarecenter/object/0020000000259442024) | Revision 53.0 for SPS05 | IMDB_SERVER*.SAR  
HANA Client | V2.5 | IMDB_CLIENT20_005_111-80002082.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001649042020) | Patch 110 | IMDB_CLIENT20*.SAR  
SAPCAR | V7.22 | SAPCAR_1115-70006178.EXE | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000098642022) | Patch 1115 | SAPCAR*.*  
SAP Host Agent | V7.22 | SAPHOSTAGENT56_56-80004822.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000591682022) | SP56 | SAPHOSTAGENT*.SAR  
Kernel Part I | 7.85 64-BIT Unicode | SAPEXE_200-80005374.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001080892022) | Patch Level 75 | SAPEXE_*.SAR  
Kernel Part II | 7.85 64-BIT Unicode | SAPEXEDB_200-80005373.SAR | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000001080682022) | Patch Level 75 | SAPEXEDB_*.SAR  
IGS | V7.81 | igsexe_3-70005417.sar | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000632872023) | Patch 1 | igsexe_*.sar  
IGS Fonts & Textures | Latest | igshelper_17-10010245.sar | [link](https://launchpad.support.sap.com/#/softwarecenter/object/0020000000703122018) | Patch 17 | igshelper_*.sar  
SWPM | V2.0 | SWPM20SP17_2-80003424.SAR | [link](https://me.sap.com/softwarecenter/object/0020000000394222024) | SP10 | SWPM20SP*.SAR  
S/4HANA Exports | S/4HANA 2023 (Core108) | S4CORE108_INST_EXPORT_1.zip | [link](https://launchpad.support.sap.com/#/softwarecenter/search/S4CORE108_INST_EXPORT_)  
  
Select all and click the cart icon to add all files to the basket. |  | Must match exactly as shown.  
S4CORE108_INST_EXPORT_2.zip  
S4CORE108_INST_EXPORT_3.zip  
S4CORE108_INST_EXPORT_4.zip  
S4CORE108_INST_EXPORT_5.zip  
S4CORE108_INST_EXPORT_6.zip  
S4CORE108_INST_EXPORT_7.zip  
S4CORE108_INST_EXPORT_8.zip  
S4CORE108_INST_EXPORT_9.zip  
S4CORE108_INST_EXPORT_10.zip  
S4CORE108_INST_EXPORT_11.zip  
S4CORE108_INST_EXPORT_12.zip  
S4CORE108_INST_EXPORT_13.zip  
S4CORE108_INST_EXPORT_14.zip  
S4CORE108_INST_EXPORT_15.zip  
S4CORE108_INST_EXPORT_16.zip  
S4CORE108_INST_EXPORT_17.zip  
S4CORE108_INST_EXPORT_18.zip  
S4CORE108_INST_EXPORT_19.zip  
S4CORE108_INST_EXPORT_20.zip  
S4CORE108_INST_EXPORT_21.zip  
S4CORE108_INST_EXPORT_22.zip  
S4CORE108_INST_EXPORT_23.zip  
S4CORE108_INST_EXPORT_24.zip  
S4CORE108_INST_EXPORT_25.zip  
S4CORE108_INST_EXPORT_26.zip  
S4CORE108_INST_EXPORT_27.zip  
S4CORE108_INST_EXPORT_28.zip  
S4CORE108_INST_EXPORT_29.zip  
S4CORE108_INST_EXPORT_30.zip  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
