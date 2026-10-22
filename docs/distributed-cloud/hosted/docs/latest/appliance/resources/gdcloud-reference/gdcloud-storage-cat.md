---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-storage-cat/
title: gdcloud storage cat \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:58.795511+00:00
---

# gdcloud storage cat  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-storage-cat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud storage cat Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud storage cat - Output the contents of one or more URLs to stdout.

## SYNOPSIS
    
    
    gdcloud storage cat [URLS ...]
        [--display-url, -d]
        [--range, -r]
        [--format=FORMAT]
        [--log-http]
        [--verbosity=VERBOSITY] [flags]
    

### EXAMPLES
    
    
    The following command writes all text files in a bucket to stdout:
    
        gdcloud storage cat s3://bucket/*.txt
    
    The following command outputs a short header describing file.txt, along with its contents:
    
        gdcloud storage cat -d s3://my-bucket/file.txt
    
    The following command outputs bytes 256-939 of file.txt:
    
        gdcloud storage cat -r 256-939 s3://my-bucket/file.txt
    
    The following command outputs the last 5 bytes of file.txt:
    
        gdcloud storage cat -r -5 s3://my-bucket/file.txt
    

### OPTIONAL FLAGS
    
    
      -d, --display-url        Print the header before each object.
          --log-http           Log all HTTP server requests and responses to stderr.
      -r, --range string       Output just the specified byte range of the
                               object. In a case where "start" = 'x', and "end" = 'y', ranges take the
                               form: x-y (e.g., -r 256-5939), x- (e.g., -r 256-), -y (e.g., -r -5)
                               
                               When offsets start at 0, x-y means to return bytes x through y (inclusive),
                               x- means to return bytes x through the end of the object, and -y changes the
                               role of y. If -y is present, then it returns the last y bytes of the object.
                               
                               If the bytes are out of range of the object, then nothing is printed.
          --verbosity string   Override the default verbosity for this command. VERBOSITY must be one of:
                               debug, info, warning, error, critical, none. (default "warning")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
