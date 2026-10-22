---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/configuration/format/
title: Format \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:06.213530+00:00
---

# Format  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/configuration/format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Format

This page describes the content of configuration package on Manufacturing Data Engine (MDE)'s directories.

Starting on v1.5.0, Manufacturing Data Engine (MDE) offers a consolidated way to apply configurations by uploading a file-based specifications contained in a directory. This enables an atomic way to apply the MDE configuration for a specific use-case, and it enables the author of the configuration to look at MDE configuration holistically by editing and checking the configuration in full in an editor like VS Code. It also enables GitOps scenarios where the MDE configurations can be checked-in Git and tracked for changes. 

The following shows a sample configuration package structure. The package contains an optional folder with a predefined name for each type of configuration entity the user needs to configure:
    
    
      ./test-configuration-package
      ├── manifest.json
      ├── buckets
      │   ├── default-record-bucket.json
      │   ├── default-tag-bucket.json
      │   └── second-tag-bucket.json
      ├── ingestion-specifications
      │   └── csv-full-ingestion-specs.json
      ├── message-classes
      │   └── message-class.json
      ├── metadata-instances
      │   ├── cloud-natural-key.json
      │   └── machine-natural-key.json
      ├── parsers
      │   └── parser.json
      ├── schemas
      │   ├── cdm-schema.json
      │   └── generic-schema.json
      ├── scripts
      │   └── parser-script.wstl
      └── types
          └── type.json
    

For example, to add buckets to MDE, you need to create a subfolder called `buckets`, which contains the specifications of the buckets that need to be created. If you don't want to create buckets, then there is no need to create the subfolder. 

The package has to include a special file called `manifest.json` that contains the fields which determine the name of the package and its provider. MDE uses the details in the manifest file to create the package, and that gives you the flexibility to name the configuration package directory with any name. 
    
    
    {
        "name": "test-configuration-package",
        "provider": "google"
    }
    
    

**Warning:** Ensure that file and folder names within the configuration package use only lowercase characters, numbers, hyphens (-), and underscores (_). Otherwise, the package will return a validation error.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
