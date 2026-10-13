---
url: https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Compute.Metadata.Readers.StreamReader
title: Google Cloud PHP shared dependency, providing functionality useful to all components. Client - Class StreamReader (1.74.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:48.810465+00:00
---

# Google Cloud PHP shared dependency, providing functionality useful to all components. Client - Class StreamReader (1.74.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Compute.Metadata.Readers.StreamReader

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud PHP shared dependency, providing functionality useful to all components. Client - Class StreamReader (1.74.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.74.0 (latest)  1.73.5  1.72.4  1.71.2  1.70.0  1.69.0  1.68.2  1.67.0  1.66.0  1.65.0  1.64.3  1.63.0  1.62.3  1.61.0  1.60.1  1.59.1  1.58.2  1.53.0  1.52.11  1.51.2  1.50.0  1.49.3  1.48.1 

Reference documentation and code samples for the Google Cloud PHP shared dependency, providing functionality useful to all components. Client class StreamReader.

A class only reading the metadata URL with an appropriate header.

This class makes it easy to test the MetadataStream class.

## Namespace

Google \ Cloud \ Core \ Compute \ Metadata \ Readers

## Implements

[ReaderInterface](https://docs.cloud.google.com/php/docs/reference/cloud-core/latest/Compute.Metadata.Readers.ReaderInterface)

## Methods 

### __construct

We create the common context in the constructor.

### read

Read the metadata for a given path.

**Parameter**  
---  
**Name** | **Description**  
`path` |  `string`   
The metadata path, relative to `/computeMetadata/v1/`.  
**Returns**  
---  
**Type** | **Description**  
`string` |   
  
## Constants 

### BASE_URL
    
    
    Value: 'http://169.254.169.254/computeMetadata/v1/'

The base PATH for the metadata.

### FLAVOR_HEADER
    
    
    Value: 'Metadata-Flavor: Google'

The header whose presence indicates GCE presence.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
