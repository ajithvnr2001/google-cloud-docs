---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbooks-use-cases/
title: Explore playbook use cases \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:52.423288+00:00
---

# Explore playbook use cases  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbooks-use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Explore playbook use cases

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document discusses some basic use cases that you can automate within your playbooks.

##  Send emails within a playbook 

You can incorporate interactive email correspondence into your playbooks. Using the built-in email actions, you can send outbound emails from the Google SecOps platform and automatically track, ingest, and log user responses directly to the case, ensuring that all communication and user input are recorded for further playbook processing.

### Before you begin

Before you begin, you'll need to enable email capabilities, which requires you to install one of these integrations:

  * [Microsoft Graph Mail](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-mail)–Use for Exchange Online.
  * [Gmail](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/gmail)–Use for Gmail accounts.



### Send an email

To send an email and log its response in Google SecOps, follow these steps: 

  1. Select the **Send Mail** action to send an email. 
  2. Add the **Wait For Mail From User** action to periodically query the mailbox for a response. This action identifies the correspondence by using a unique ID. 



Once the response is received, it's fetched into the platform. 

The response can be seen on the case wall and used as an input for other actions in the playbook.

##  Scan multiple URLs in VirusTotal 

The **VirusTotal Scan URL** action iterates over the selected scope entities, and initiates a request to VirusTotal for each entity of type URL. When finished, the action enriches the URL entities with a VirusTotal report and also posts the result on the case wall. An `is_risky` value is exposed so that you can add further conditions to the playbook for high-risk URLs. For details on how to use the **Scan Hash** action to scan file hashes with VirusTotal, mark entities as suspicious, and show insights, see the [Scan Hash](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/virustotal#scan_hash) action for VirusTotal. 

##  Scan URLs received by email 

You can build a security automation workflow that extracts and scans URLs from inbound emails to detect phishing or malicious links. This process ensures that any dangerous links are neutralized before they pose a risk, letting your playbook take immediate action, such as blocking the URL or quarantining the email.

### Before you begin

You must have the following integration installed and configured in your environment:

  * Email integration: Microsoft Graph Mail or Gmail (to read and extract data from the email/alert).
  * Reputation integration: VirusTotal or a similar URL analysis tool.



To scan URLs received by email, you'll need to configure a connector that monitors an email box (with the **Email** or **Exchange** integrations).

### Build the scan logic in your playbook

Use the following steps to build the scanning logic in your playbook:

  1. Use the email integration's action (for example, `Gmail_Search For Emails`) to get the full email body or event data. Use the Expression Builder to parse the email and extract the specific URL(s) you want to scan. For details, see [Use the Expression Builder](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder).  
When emails start coming into Google Security Operations SOAR, their content can be either parsed by the mapping feature or extracted by the **Create Entity** playbook action (if playbooks are attached to the incoming emails).
  2. Add your selected action (for example, `VirusTotal_Scan` URL) and use a placeholder to input the extracted URL from the previous step.
  3. Add a Condition flow immediately after the scan action. For details, see [Use flows in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-flows-in-playbooks).
  4. Configure the branches of the condition to evaluate the JSON Result from the reputation scan:
     * Branch 1 (Malicious): If `Scan Result` is reported as malicious (for example, score > 5, or specific engine found a threat).
     * Branch 2 (Clean/Unknown): If `Scan Result` is clean or if the condition fails to find malicious indicators.



Once all URLs are extracted, you can use them in manual actions and in playbooks.

##  Send messages to a phone number 

To send messages to a phone number, you must have the Twilio integration installed and an active account with Twilio. 

Once configured in the Content Hub, Twilio actions will let you send SMS messages and even fork playbooks according to an SMS response. 

## Put elements of the case data into an email

Placeholders are dynamic expressions used in playbook actions to insert specific case data, entity attributes, or alert details into text fields (like an email message). At runtime, the placeholder is replaced by the actual data extracted from the Google Security Operations platform. 

### Placeholder structure

A placeholder always starts and ends with square brackets [ ], which contain the specific data path (for example, `[Alert.Name]` references the alert's name).

The following placeholders won't render for any automatic operation: 

  * General.CurrentUserEmail
  * General.CurrentUserID
  * General.CurrentUserFullName
  * General.CurrentUserRole



### Use a placeholder

To use a placeholder, follow these steps:

  1. Click  data_array  **Placeholder** next to a text field (for example, the message field in a **Send Email** action).
  2. Select the preferred content path to insert the placeholder (for example, `[Alert.Name]`).



You can combine multiple placeholders with static text to create rich, custom content.

## Build a playbook to extract text from case PDF files

This use case explains how you can build a playbook to extract text from PDF files attached to cases. It uses a remote agent to convert the PDF to an image, and then use Optical Character Recognition (OCR) to extract the text. The playbook uses the **FileUtilities** integration to handle the attachment and the **ImageUtilities** integration to extract the text. You can use the extracted text in subsequent playbook steps.

### Before you begin

  1. In the Content Hub, go to **Power Ups**.
  2. Install the **FileUtilities** and **ImageUtilities** integrations.
  3. Configure a remote agent:
     1. Verify that you have a remote agent set up and running.
     2. You must configure **FileUtilities** and **ImageUtilities** Power Ups to run on the remote agent.
     3. Install dependencies on the remote agent:
For CentOS 7/RHEL: 
        * `1 sudo yum update -y`
        * `2 sudo yum install -y epel-release`
        * `3 sudo yum install -y poppler-utils _# Provides pdftoppm for PDF conversion_`
        * `4 sudo yum install -y tesseract _# OCR engine_`
For Ubuntu: 
        * `sudo apt-get update`
        * `sudo apt-get install -y poppler-utils _# Provides pdftoppm for PDF conversion_`
        * `sudo apt-get install -y tesseract-ocr _# OCR engine_`



### Build the playbook

To build the playbook, do the following:

  1. Use **FileUtilities** to get an attachment using the `Get Attachment` action.
  2. Use the **FileUtilities** `Save Base64 to File` action to save the file as follows:
     * **File extension** : `.pdf`
     * **Base64 input** : `[Get Attachment.JsonResult| "base64_blob"]`
     * **Filename** : `[Get Attachment.JsonResult| "evidenceName"]`
  3. Use **ImageUtilities** to convert the file:
     * **Input file format** : `PDF`
     * **Input file path** : `[Save file to Remote Agent.JsonResult| "files.file_path"]`
     * **Output file format** : `PNG`
  4. Use the **ImageUtilities** `OCR Image` action to begin the OCR process: 
     * **File path:** `[Convert PDF to PNG.JsonResult| "file_path"]`
  5. Use the **Siemplify** `Case Comment // Any` action to extract the result 
     * **Comment:** `[OCR Image.JsonResult| "extracted_text"]`



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
