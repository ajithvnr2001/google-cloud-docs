---
url: https://docs.cloud.google.com/dns/docs/zones/operations/
title: View operations on managed zones \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:45:19.369190+00:00
---

# View operations on managed zones  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  View operations on managed zones Stay organized with collections  Save and categorize content based on your preferences. 

Cloud DNS records managed zone updates that you make (modifying descriptions or configuring DNSSEC state) as operations. Managed zone creation and deletion are not recorded; deletion of a managed zone also deletes recorded operations on the zone.

These operations are independent of [changes that you make](https://docs.cloud.google.com/dns/docs/monitoring#dns-propagation) to the resources within the managed zone. You can use the Google Cloud CLI or the REST API to see the history of these updates.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.managedZoneOperations.list`
  * `dns.managedZoneOperations.get`



**Roles**

  * `roles/dns.admin`



## Display audit log of operations

###  gcloud 

Run the following command:
    
    
    gcloud dns operations list --zones="ZONE_NAME"
    

Replace `ZONE_NAME` with the name of a DNS zone in your project.

This command prints the JSON formatted resource record sets for the first 100 records. You can specify an additional parameter:

  * `--limit`: maximum number of operations to list



###  Python 
    
    
    from apiclient import errors
    from apiclient.discovery import build
    
    PROJECT_NAME='PROJECT_NAME'
    ZONE_NAME='ZONE_NAME'
    
    try:
      service = build('dns', 'v1')
      response = service.operations().list(project=PROJECT_NAME,
                                           managedZone=ZONE_NAME).execute()
      print(response)
    except errors.HttpError, error:
      print('An error occurred: %s' % error)
    

Replace the following:

  * `PROJECT_NAME`: the name of your project
  * `ZONE_NAME`: the name of a DNS zone in your project



## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).
  * For the Cloud DNS command-line, see the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/dns) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
