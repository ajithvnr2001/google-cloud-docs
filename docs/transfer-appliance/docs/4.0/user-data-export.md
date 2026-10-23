---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/user-data-export/
title: Exporting User Data \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:37.755346+00:00
---

# Exporting User Data  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/user-data-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)



Send feedback 

#  Exporting User Data Stay organized with collections  Save and categorize content based on your preferences. 

You can get a copy of all the information provided to order and use the Transfer Appliance service. Follow the given steps to get the information.

  1. Within the Google Cloud Console, Click Activate Cloud Shell.

![Starting devshell from the menu bar.](https://docs.cloud.google.com/static/transfer-appliance/docs/4.0/images/devshell.png)

  2. Run the export command:

     * Copy and paste the following command into the terminal. Make sure to replace {resource_name} with the actual appliance name. Appliance name can be found on the appliance details page of the ordered appliance on Google Cloud Console.
           
           curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" https://transferappliance.googleapis.com/v1alpha1/{resource_name}:export
           




### Notes:

  1. Data copied onto the Transfer Appliance won't be immediately accessible for export. It will only become available in the Cloud Storage bucket upon completion of the data transfer process.

  2. Data wiped out automatically from our systems won't be available for export.

  3. This feature is different from [Exporting your Data from Cloud Storage to another location](https://docs.cloud.google.com/transfer-appliance/docs/4.0/data-export)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
