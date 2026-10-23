---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/import-export/
title: Import and export your VMs \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:20.390383+00:00
---

# Import and export your VMs  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/import-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Import and export your VMs Stay organized with collections  Save and categorize content based on your preferences. 

The Migrate to Virtual Machines import and export feature allows you to create, export, and revise migrating VMs using a CSV file.

## Migration prerequisites

Before using the import and export feature, you should review the prerequisites of migrating single VMs or groups of VMs. The same prerequisites apply when managing migrations by CSV.

For more information about migrations, see the Migrate to Virtual Machines documentation on:

  * [Migrate individual VMs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms)
  * [Migrate VM groups](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vm-groups)



## Import and export overview

You can use the export feature to output a CSV file detailing your source VMs or your current VMs and their target details, edit them externally, and then upload the CSV to Migrate to Virtual Machines to define your migrations.

When editing and importing your CSV file, you should keep the end state of your migration in mind. In other words, you can define your settings in your CSV file and the import process will create migrations and groups, change group memberships, and update target details to match the state of your imported CSV file.

To define a CSV file for the import process, you have several options:

  * Export your existing migration details as a CSV file for bulk editing and group uploads
  * Export source VMs from a source inventory as a CSV file
  * Download and edit a template CSV file



If your CSV file is improperly formatted or a specific migration detail is invalid, you will receive an error while uploading it to Migrate to Virtual Machines.

**Note:** You cannot delete your groups or your migrating VMs using the import and export feature.

### CSV file format

Before performing any actions the imported CSV file will be parsed and validated by the following criteria:

  * Migrations and source VMs will be identified as a combination of **source name** , **source region** , and either the **source VM display name** or the **source VM ID**.
  * The same migration or source VM **cannot appear in more than one row**.
  * **No more than 100 migrations or source VMs** can be processed in a single file.
  * If a migration does not exist for the source VM, the existence of the source VM is validated and **a new migration will be created** for it.
  * The import and export migration feature validates **target details columns** **by their type and resource naming restrictions**. You should manually validate the existence of resources in your target project to avoid failure.
  * **Columns missing from the CSV file will be ignored and migrations will not be updated** in those fields. However, empty values will update the respective migration and remove data from that migration.
  * Columns can contain **multiple values per VM** (such as network tags or labels), separated by line breaks. See Export a template file for an example.



Some validation errors will block the continuation of the import. For example, an invalid header row or a file with too many rows will throw a validation error.

**Note:** Line-level warnings can be ignored according to your discretion. Select **Skip errors and continue** on the import page to move forward.

#### CSV file fields

A **header row is expected** and must contain the following columns identifying the migration or source VM. Other columns are optional and will only be updated when imported if they exist. Unknown header columns will be ignored.

**Mandatory fields** for your CSV file include:

  * **Source name**
  * **Region**
  * Either the **Source VM Display name** or **Source VM ID**



For more information about **optional fields** , see [configuring the target for a migrated VM](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/how-to/migrating-vms#configure-target).

**Note:** Metadata values can be very long and contain line brakes. The export and import process only supports simple one-line values. If your migration contains unsupported metadata values, your CSV file will be redacted when exported. Re-importing the same CSV file will ignore redacted metadata columns.

### Template files

You can export a template file to help you define your CSV file. The template CSV file is empty except for a **header row** detailing the mandatory and optional fields and a sample row providing examples of how each column should be formatted. In the template, target details are represented by the columns of the CSV file.

**Note:** The headers row as provided by the template is required for a successful import.

## Export a pre-filled CSV file

To create migrations based on source VMs or to make changes to an existing migration or group of migrations, you should first export a CSV file representing your migrations' present status.

To export a pre-filled CSV file, follow these steps:

  1. Open the [**Migrate to Virtual Machines**](https://console.cloud.google.com/compute/mfce) page in the Google Cloud console.
  2. To export a list of source VMs:

     1. Select the **Sources** tab.
     2. Select the source VMs you would like to export from the inventory.
     3. Click **Export** to download the CSV file.
  3. To export groups of existing migrations:

     1. Select the **Groups** tab.
     2. Select the groups you would like to export from the group list.
     3. Click **Export** to download the CSV file.



## Import your CSV file

When you upload a CSV file, it will be validated. If some lines in the file have errors, these errors will be presented and you can choose to skip these lines and import the rest.

Upon uploading a validated CSV file, an _import plan_ will be presented to approve. Your file will be imported upon approval.

To import your CSV file, follow these steps:

  1. Open the [**Migrate to Virtual Machines**](https://console.cloud.google.com/compute/mfce) page in the Google Cloud console.
  2. Select the **Groups** tab and then select **Import**.
  3. Browse for your import file. It must be a CSV file and 100kB or less.

**Tip:** You cannot upload a CSV file while another import is already in progress.
  4. Select **Upload**.

If there are errors, they will be presented to you at this step. You can choose to **Skip errors and continue**.

  5. You will then be presented with an _import plan_. This will detail which actions are being invoked and which resources are being referenced.

  6. Select **Start import** to approve of the import plan and begin your import. The import plan will update with the progress of each step.

  7. If the import fails to complete, review the error messages as provided. The failure of any one step will stop the entire sequence.

  8. On a successful import, select **Go to groups** to return to the **Groups** page and review your updated resources.

**Note:** **In case of a failure, you can retry importing the same CSV file.** Given the nature of the import process (in which the CSV file represents the ideal state of your migrations), the import and export migration process will skip actions that were already completed and continue from where it failed.



### Review your import plan

An _import plan_ is a list of actions generated according to the changes detected in your import file. The following types of messages may be listed:

  * Create migrations.
  * Create a group.
  * Remove migrations from a group.
  * Add migrations to a group.
  * Update the target details for migrations.



Upon acceptance to the import plan, the status of each item will update as the import progresses. In the report you will be able to see the status, such as **Pending** , **Running** , **Done** , and **Failed** as it correlates to each item.

## Export your migration template file

You can export a migration template file for details about formatting your CSV file correctly.

To export your migration template file, follow these steps:

  1. Open the [**Migrate to Virtual Machines**](https://console.cloud.google.com/compute/mfce) page in the Google Cloud console.
  2. Select the **Groups** tab.
  3. Select **Import**.
  4. Select **Export template** and you will be prompted to download the file `Template.csv`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
