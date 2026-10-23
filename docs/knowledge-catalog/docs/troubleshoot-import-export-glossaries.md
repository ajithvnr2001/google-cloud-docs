---
url: https://docs.cloud.google.com/knowledge-catalog/docs/troubleshoot-import-export-glossaries/
title: Troubleshoot business glossary and entry link import errors \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:17.933516+00:00
---

# Troubleshoot business glossary and entry link import errors  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/troubleshoot-import-export-glossaries/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Troubleshoot business glossary and entry link import errors Stay organized with collections  Save and categorize content based on your preferences. 

This guide helps you troubleshoot Knowledge Catalog issues when you [import and export glossaries and entry links](https://docs.cloud.google.com/knowledge-catalog/docs/import-export-glossaries-entrylinks-overview), including missing entry links, invalid glossary URL errors, or when an import job fails.

If you need help resolving an issue that isn't addressed on this page, contact [Google Cloud Support](https://cloud.google.com/support).

## Fix missing entry links in Knowledge Catalog

After you export entry links from Knowledge Catalog to a Google Sheet by running the [export entry link utility](https://docs.cloud.google.com/knowledge-catalog/docs/export-entrylinks-sheets), you notice that some entry links (associations) are missing from the generated Google Sheet.

This issue occurs if the export utility automatically skips entry links because of the following conditions:

  * Insufficient permissions (redacted resources): You don't have the required IAM permissions to view either the source entry or the target entry associated with the link.

  * Invalid entry link type: The entry link uses an unsupported or unrecognized relationship type. Valid types are limited to `definition`, `related`, and `synonym`.

  * Incomplete entry references: The entry metadata is missing required schema fields, causing the validation check to skip the resource.




To resolve this issue, perform the following checks:

  * Verify permissions: Ensure you have permissions to view missing entry links. Confirm that the principal executing the script has been granted the [required roles](https://docs.cloud.google.com/knowledge-catalog/docs/export-entrylinks-sheets#required_roles).

  * Inspect execution logs: Check the terminal or script logs for warnings containing `Skipping redacted entrylink`. The logs output the specific resource IDs of the skipped entry links and the reason they were omitted.

  * Check link schema validity: If you previously modified these links programmatically, verify that their properties match the schema requirements.




## No terms found in the glossary error

When you [export glossaries to a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/export-glossaries-sheets), the execution fails or returns an empty result with the message `No terms found in the glossary`, even though the business glossary contains active terms.

This issue occurs if the script can't locate the specified glossary or lacks the access permissions required to retrieve its contents. Common causes include:

  * Incorrect glossary URL: The glossary URL configured in your execution parameters is incorrect or misspelled.
  * Insufficient IAM permissions: The authenticated service account or user credentials running the script don't have permission to view or list terms within the target glossary.
  * Glossary ID mismatch: The glossary ID specified in your script command doesn't match the actual glossary resource ID in Knowledge Catalog.



To resolve this issue, verify your configuration and permissions:

  * Check the glossary ID: In the Google Cloud console, navigate to the Knowledge Catalog **Glossaries** page, select your glossary, and confirm that the resource ID matches the ID you are passing to the utility script.

  * Verify IAM permissions: Confirm that your authenticated credentials (the service account or your impersonated user account) have been granted the [required roles](https://docs.cloud.google.com/knowledge-catalog/docs/export-glossaries-sheets#required_roles).

  * Validate the glossary URL structure: If you're passing a direct resource path or URL to the script, ensure it follows the correct Knowledge Catalog resource format:

`projects/PROJECT_ID/locations/LOCATION/glossaries/GLOSSARY_ID`




## Entries not found in Knowledge Catalog warning

During an [entry link import](https://docs.cloud.google.com/knowledge-catalog/docs/import-entrylinks-sheets) operation, the script pauses and displays a warning similar to the following:
    
    
    Found X entries not found in Knowledge Catalog. EntryLinks associated with
    these entries will be skipped. Continue with import? [y/N]:
    

This issue occurs if your Google Sheet contains entry links that reference data assets or glossary terms that don't exist in Knowledge Catalog.

To resolve this issue, choose one of the following options:

  * To proceed with a partial import, type `y` at the prompt. The utility imports all valid entry links and skips only the links that reference the missing resources.

  * To cancel and fix the missing resources, type `n` to cancel the execution. Verify that the entry IDs in your source document exactly match the resource names in your Knowledge Catalog. Correct any missing resources or typographical errors, and then run the import script again.




## Troubleshoot Knowledge Catalog import job fails

If an import job is interrupted or fails midway through execution, you don't need to restart the entire process or modify your source Google Sheet.

The utility tracks successfully imported batches using an archive folder in your Cloud Storage staging bucket.

To resume the job, follow these steps:

  1. Re-run the import utility. The utility detects the state of your previous run, it displays the following prompt:
         
         Found X existing file(s) in archive folder from a previous incomplete import
         Continue using existing files? [y/N]:
         

  2. Type `y`. The utility skips the batches that were already successfully imported and processes only the remaining files.




## Script timeouts or SSL errors during execution

While running the import or export utility script, the execution halts, times out, or returns SSL errors in your terminal.

This issue occurs because of the following network-level errors:

  * Corporate proxy or firewall interception: A security proxy or firewall is intercepting and inspecting HTTPS traffic, which invalidates the SSL certificates.
  * Active VPN restrictions: Your VPN configuration restricts outbound traffic to certain Google Cloud APIs or Google Sheets endpoints.
  * Local network instability: A temporary drop in internet connectivity interrupted the session.



To resolve these network issues, try the following steps:

  * Ensure you have a stable network connection.

  * Inspect proxy and firewall settings

  * Check your VPN configuration.

  * Rely on built-in retries: The utility script has built-in retry logic for transient network glitches. If the network drop is momentary, wait for the script to finish its retry attempts before restarting the execution.




## Invalid spreadsheet URL error

When you attempt to run an import or export utility, the command-line interface returns an `Invalid spreadsheet URL` error and halts execution.

This issue occurs if the script can't parse the provided Google Sheet's link or doesn't have authorization to view the file. Common causes include:

  * Malformed URL: The URL doesn't match the standard Google Sheets path format.
  * Missing spreadsheet ID: The path is missing the unique alphanumeric ID that points to your specific sheet.
  * Access restrictions: Your authenticated service account doesn't have permission to view or edit the sheet, preventing the utility from validating the link.



To resolve this issue, verify your spreadsheet link and access settings:

  * Validate the URL prefix: Ensure that the spreadsheet URL you pass to the utility begins with the following standard Google Sheets path: `https://docs.google.com/spreadsheets/`

  * Verify the spreadsheet ID: Confirm that the URL includes your sheet's unique ID. A valid URL should follow this structure: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`

  * Check access permissions: Open the Google Sheet in a browser, click **Share** , and confirm that you have added your service account email as an **Editor**.




## Resolve invalid glossary URL errors

When you attempt to run an import or export utility for glossaries, the command-line interface returns an `Invalid glossary URL` error and halts execution. Verify that there is no invalid glossary URL in your parameters.

This issue occurs if the script can't parse the provided Knowledge Catalog glossary resource path or doesn't have authorization to view the resource. Common causes include:

  * Malformed resource path: The resource path doesn't match the standard Knowledge Catalog glossary path format.
  * Incorrect ID: The path contains an incorrect project ID, region location, or glossary ID.
  * Access restrictions or missing resource: The glossary doesn't exist, or your authenticated service account lacks the IAM permissions required to access it.



To resolve this issue, verify your glossary resource path and credentials:

  * Validate the resource path structure: Ensure that the glossary path you pass to the utility matches the following standard Knowledge Catalog format: `projects/PROJECT_ID/locations/LOCATION/glossaries/GLOSSARY_ID`

  * Verify identifiers in the path: Use the correct project ID, location, and glossary ID.

  * Confirm resource existence and access: Confirm that the glossary exists with the specified ID and your authenticated service account has been granted necessary IAM roles.




## View execution logs

The import and export utilities generate detailed execution logs as they run. If your import job fails, check the logs for specific errors. These logs help you audit the transfer process and identify skipped entries or formatting warnings.

  * Log location: The import and export utilities writes log files to the `logs/` directory in your local execution path.
  * Log format: Each log file is appended with a timestamp so you can locate logs for a specific run.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
