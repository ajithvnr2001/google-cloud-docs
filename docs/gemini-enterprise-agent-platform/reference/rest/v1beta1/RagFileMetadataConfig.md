---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagFileMetadataConfig/
title: RagFileMetadataConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:34:42.000224+00:00
---

# RagFileMetadataConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagFileMetadataConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  RagFileMetadataConfig Stay organized with collections  Save and categorize content based on your preferences. 

metadata config for RagFile.

Fields  
  
`metadata_schema_source` `Union type`  
  
Specifies the metadata schema source. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`gcsMetadataSchemaSource` `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GcsSource)`)` Google Cloud Storage location. Supports importing individual files as well as entire Google Cloud Storage directories. Sample formats: - `gs://bucketName/my_directory/objectName/metadataSchema.json` \- `gs://bucketName/my_directory` If the user provides a directory, the metadata schema will be read from the files that ends with "metadataSchema.json" in the directory. | `googleDriveMetadataSchemaSource` `object (`[GoogleDriveSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles#GoogleDriveSource)`)` Google Drive location. Supports importing individual files as well as Google Drive folders. If the user provides a folder, the metadata schema will be read from the files that ends with "metadataSchema.json" in the directory. | `inlineMetadataSchemaSource` `string` Inline metadata schema source. Must be a JSON string. End of mutually exclusive fields. | `metadata_source` `Union type`  
  
Specifies the metadata source. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`gcsMetadataSource` `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GcsSource)`)` Google Cloud Storage location. Supports importing individual files as well as entire Google Cloud Storage directories. Sample formats: - `gs://bucketName/my_directory/objectName/metadata.json` \- `gs://bucketName/my_directory` If the user provides a directory, the metadata will be read from the files that ends with "metadata.json" in the directory. | `googleDriveMetadataSource` `object (`[GoogleDriveSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles#GoogleDriveSource)`)` Google Drive location. Supports importing individual files as well as Google Drive folders. If the user provides a directory, the metadata will be read from the files that ends with "metadata.json" in the directory. | `inlineMetadataSource` `string` Inline metadata source. Must be a JSON string. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // metadata_schema_source
      "gcsMetadataSchemaSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GcsSource))
      },
      "googleDriveMetadataSchemaSource": {
        object ([GoogleDriveSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles#GoogleDriveSource))
      },
      "inlineMetadataSchemaSource": string
      // Union type
    
      // metadata_source
      "gcsMetadataSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GcsSource))
      },
      "googleDriveMetadataSource": {
        object ([GoogleDriveSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles#GoogleDriveSource))
      },
      "inlineMetadataSource": string
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
