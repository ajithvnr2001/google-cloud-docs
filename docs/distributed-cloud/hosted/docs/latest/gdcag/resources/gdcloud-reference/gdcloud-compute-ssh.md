---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-compute-ssh/
title: gdcloud compute ssh \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:29.932506+00:00
---

# gdcloud compute ssh  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-compute-ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud compute ssh Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute ssh - SSH to a GDC air-gapped virtual machine.

## SYNOPSIS
    
    
    gdcloud compute ssh INSTANCE_NAME [flags]
    

### EXAMPLES
    
    
    To SSH to virtual machine example-instance in project projectA, run:
    
        gdcloud compute ssh example-instance --project projectA
    

### OPTIONAL FLAGS
    
    
          --command string                    A command to run on the virtual machine.
                                              Runs the command on the target instance and then exits. Example:
                                              
                                                gcloud compute ssh example-instance --command="ps -ejH"
          --ssh-flag stringArray              Additional flags to be passed to ssh(1).
                                              It is recommended that flags be passed using an assignment operator and quotes. Example:
                                              
                                                gcloud compute ssh example-instance --ssh-flag="-vvv" --ssh-flag="-L 80:localhost:80"
          --strict-host-key-checking string   Override the default behavior of StrictHostKeyChecking for the connection.
                                              By default, StrictHostKeyChecking is set to 'ask' when '--quiet' is NOT on, otherwise it is set to 'accept-new'.
                                              Must be one of: "yes", "no", "ask", "accept-new". (default "ask")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
