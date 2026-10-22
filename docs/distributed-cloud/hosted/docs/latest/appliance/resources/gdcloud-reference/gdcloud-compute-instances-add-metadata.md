---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-instances-add-metadata/
title: gdcloud compute instances add-metadata \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:13.657287+00:00
---

# gdcloud compute instances add-metadata  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-instances-add-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud compute instances add-metadata Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute instances add-metadata - Add metadata for a virtual machine instance.

## SYNOPSIS
    
    
    gdcloud compute instances add-metadata INSTANCE_NAME [flags]
    

### EXAMPLES
    
    
    To add metadata for key "example-key" for a virtual machine instance named "example-instance" in project "example-project", run:
    
        gdcloud compute instances add-metadata example-instance --project example-project --metadata=example-key="example value"
    
    To add metadata under key "important-data" to an instance named "example-instance" using file "example-file"
        gdcloud compute instances add-metadata example-instance --project example-project \
        --metadata-from-file=important-data=example-file.txt
    

### OPTIONAL FLAGS
    
    
          --metadata stringToString             List of comma-separated key-value pair metadata to add to the virtual machine instance.
                                                 For example, --metadata=key1="val1",key2="val2". At least one of the flags --metadata or --metadata-from-file is required. (default [])
          --metadata-from-file stringToString   List of comma-separated KEY=LOCAL_FILE_PATH metadata to add to the virtual machine instance. The value of the key is read from the file provided.
                                                 For example, --metadata-from-file=key1=filepath1,key2=filepath2. At least one of the flags --metadata or --metadata-from-file is required. (default [])
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
