---
url: https://docs.cloud.google.com/bare-metal/docs/bms-organize-storage/
title: Organize storage volumes using labels \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:37.919985+00:00
---

# Organize storage volumes using labels  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-organize-storage/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Organize storage volumes using labels

To help organize your storage volumes, you can use labels. Labels are key-value pairs that you can attach to each storage volume, then filter the storage volumes based on their labels. For example, you can use labels to group storage volumes by purpose, environment, location, department, and so on. Labels are optional.

## Add or update labels for storage volumes

You can add or update labels for the existing storage volumes.

###  Console 

  1. Go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.

  2. For the storage volume that you want to label, click more_vert.

  3. Click edit**Edit labels**.

  4. On the **Labels editor** page:

     1. Click add**Add label** and add the key-value pair.
     2. To update labels, select the existing labels and modify their values.
     3. Click **Submit**.
  5. After you return to the **Volumes** page, refresh the page to view your changes.




###  gcloud 

To add or update labels for a storage volume, use the `gcloud bms volumes update` command with the `--update-labels` option.

The following sample command adds the labels **environment = dev** and **location = branch** :
    
    
    gcloud bms volumes update VOLUME_NAME --project=PROJECT_ID --region=REGION --update-labels environment=dev,location=branch
    

If you provide a new value for a label that already exists, the system updates the existing label with the new value. If you provide a new label, the system adds the new label to the list of labels.

###  API 

To add or update labels for a storage volume, enter your project ID, region, volume name, and a list of labels in the following `curl` command. Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key.

The following sample command assigns a label of **environment = test**.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    -H "Content-Type: application/json" \
    "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME?updateMask=labels"
     -d "{
      'labels' : {'environment': 'test'}
    }"
    

## Remove labels from storage volumes

You can remove labels from the storage volumes.

###  Console 

  1. Go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.

  2. For a storage volume with labels that you want to remove, click more_vert.

  3. Click edit**Edit labels**.

  4. On the **Labels editor** page:

     1. To delete a label, click delete.
     2. Click **Submit**.
  5. After you return to the **Volumes** page, refresh the page to view your changes.




###  gcloud 

To remove labels from a storage volume, use the `gcloud bms volumes update` command with the following options:

  * `--remove-labels`: Removes the specified label.
  * `--clear-labels`: Removes all the labels.



The following sample command removes the label **department** from a storage volume:
    
    
    gcloud bms volumes update VOLUME_NAME --project=PROJECT_ID --region=REGION --remove-labels=department
    

The following sample command removes all the labels from a storage volume:
    
    
    gcloud bms volumes update VOLUME_NAME --project=PROJECT_ID --region=REGION --clear-labels
    

###  API 

To remove labels from a storage volume, enter your project ID, region, and storage volume name in the following `curl` command. Provide an empty list of labels to remove all labels, or provide a list of labels you want to keep (omitting the labels you want to remove). Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key.

The following sample command removes all the labels except **environment = test**.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    -H "Content-Type: application/json" \
    "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME?updateMask=labels"
     -d "{
      'labels' : {'environment': 'test'}
    }"
    

## Filter storage volumes using labels

You can search your storage volumes and filter results by using labels.

###  Console 

  1. Go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.

  2. Click in the filter_list **Filter** bar above the list of storage volumes.

  3. From the **Properties** list, select **Labels**.

  4. Enter the key, value, or key-value pair for your label.

For example, to view only storage volumes with the label `env:dev`, you can enter any of the following:

     * Enter the key: `env`
     * Enter the value: `dev`
     * Enter the key-value pair: `env:dev`
  5. To apply the label filter, click anywhere outside the filter bar.




###  gcloud 

To filter storage volumes by using labels, use the `gcloud bms volumes list` command with the `--filter` option.

The value of `--filter` option must be in the `labels.KEY=VALUE` format. For example, if you want to filter on a label with `env` as the key and `dev` as the value, issue this command:
    
    
    gcloud bms volumes list --project=PROJECT_ID --region=REGION --filter labels.environment=dev
    

For more information about the filter syntax in the gcloud CLI, see the [`gcloud topic filters` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

###  API 

To filter storage volumes by using labels, enter your project ID and region along with `filter=labels` and a key-value pair label. Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key.

The following sample command limits the output to find storage volumes with the key-value pair label **environment = test**.
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    -H "Content-Type: application/json" \
    "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes"?filter=labels.environment=test
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
