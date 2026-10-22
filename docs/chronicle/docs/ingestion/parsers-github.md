---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parsers-github/
title: Implement community parsers in GitHub \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:42.663262+00:00
---

# Implement community parsers in GitHub  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parsers-github/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Implement community parsers in GitHub

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

Google Security Operations utilizes an open-source [repository on GitHub](https://github.com/chronicle/content-hub) to enable community, partner, and customer collaboration for parser development and maintenance. This repository lets community contributions expand and maintain the available set of parsers for Google SecOps. 

**Goals**

  * Enable Community contributions: Allow external users, partners, and customers contribute new and updated community parsers.
  * Facilitate adoption: Provide users with a mechanism to adopt community parsers into their custom parser instances.
  * Ensure quality: Maintain a rigorous vetting and testing framework to validate the security and functional quality of all contributions before release.



## Before you begin

  * Make sure you have the `chronicle.parsers.create` permission which is part of the `chronicle.admin` IAM role.
  * To contribute to community parsers, sign a Contributor License Agreement (CLA). For full details, see [Sign our Contributor License Agreement](https://github.com/chronicle/content-hub/blob/main/docs/contributing.md#sign-our-contributor-license-agreement).



## Repository structure

All parsers are organized within the top-level `parsers/` directory in the Content Hub area of the GitHub repository. Each log source has its own dedicated subdirectory.
    
    
    content-hub/
    └── content/
        └── parsers/
            ├── third_party/
            │   ├── community/
            │   │   ├── VENDOR1_PRODUCT1/cbn/
            │   │   └── VENDOR2_PRODUCT2/cbn/
            │   ├── partnerA/
            │   │   └── VENDOR1_PRODUCT1/cbn/
            │   └── partnerB/
            │        └── VENDOR1_PRODUCT1/cbn/
            ...
    

### Folder naming conventions

The folder naming conventions for all subdirectories within the `third_party/community/parser` repository are strictly defined. These standards ensure system compatibility, discoverability for customers, and alignment with internal Google SecOps conventions. 

## Create a community parser in GitHub

The following section details how to create and manage community parsers.

### Locate and download community parsers

  1. Navigate to the required log type folder.
  2. Review the `metadata.json` file to check for references related to the log sources supported by the parser.
  3. Download the `parser.conf` file which contains the core parser logic in CBN syntax.



### Deploy community parsers in Google SecOps

The following step explains how to copy and convert a community parser into your own custom parser instance. Once deployed, the parser operates as a custom parser that you maintain.

  * In your Google SecOps instance, upload or paste the contents of the downloaded `parser.conf` file into the corresponding fields in the **Create Parser** page in **SIEM Settings**.



### Validate the custom parser

After you deploy the parser in your Google SecOps instance, built-in custom parser validations are automatically triggered to check for potential pipeline failures or normalization issues. If these validations fail, you must fix the parser logic or modify your copy of the parser to align with your specific use case. We encourage you to contribute corrections or enhancements back to the community repository and become an active participant in the open-source community. 

For detailed information on contributing new parsers or updating existing ones in GitHub, see [GitHub parser instructions](https://github.com/chronicle/content-hub/tree/main/docs/content_deep_dive).

If you encounter any issues with the integration, [open a case in GitHub](https://github.com/chronicle/content-hub/issues/new/choose). The community parsers are not covered by Google Support.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
