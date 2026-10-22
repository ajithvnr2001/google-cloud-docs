---
url: https://docs.cloud.google.com/certificate-authority-service/docs/updating-certificate-authorities/
title: Update certificate authorities \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:04.883432+00:00
---

# Update certificate authorities  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/updating-certificate-authorities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update certificate authorities

This page explains how you can update the configuration for a certificate authority (CA).

## Update labels on a CA

### Console

  1. In the Google Cloud console, go to the **Certificate authorities** page.

[Go to Certificate authorities](https://console.cloud.google.com/security/cas/certificateAuthorities)

  2. Under **Certificate authorities** , pick your target CA.

     1. In the **Summary** section, click **Edit**.
     2. Click **Add labels**.
     3. In the panel on the right side, click **Add Item**.
     4. Add the **Key** and **Value** for your label.
     5. Click **Save**.



### gcloud
    
    
    gcloud privateca roots update CA_NAME --location LOCATION --pool POOL_NAME --update-labels foo=bar
    

Where:

  * CA_NAME: the unique identifier of the CA.
  * LOCATION: the location of the certificate authority.
  * POOL_NAME: the unique identifier of the CA pool.
  * `--update-labels` flag mentions the key-value pairs to update.



For more information about the `gcloud privateca roots update` command, see [gcloud privateca roots update](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/update).

## What's next

  * Learn how to [manage the CA state](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-state).
  * Learn how to [delete CAs](https://docs.cloud.google.com/certificate-authority-service/docs/deleting-certificate-authorities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
