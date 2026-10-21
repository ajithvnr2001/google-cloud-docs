---
url: https://docs.cloud.google.com/bigtable/docs/authorized-views-create-manage/
title: Create and manage authorized views \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:14.101581+00:00
---

# Create and manage authorized views  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/authorized-views-create-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage authorized views

Bigtable authorized views let you restrict access to specific subsets of table data, such as individual rows or columns. You can define, create, and manage these views using the Google Cloud CLI, the Google Cloud console, or the Cloud Bigtable [client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries).

Before you begin, review the [Authorized views overview](https://docs.cloud.google.com/bigtable/docs/authorized-views).

## Required roles

To get the permissions that you need to perform administrative operations on an authorized view , ask your administrator to grant you the [Bigtable Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigtable#bigtable.admin) (`roles/bigtable.admin`) IAM role on the underlying table . For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to perform administrative operations on an authorized view . To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform administrative operations on an authorized view :

  * `bigtable.authorizedViews.get`
  * `bigtable.authorizedViews.list`
  * `bigtable.authorizedViews.create`
  * `bigtable.authorizedViews.update`
  * `bigtable.authorizedViews.delete`
  * `bigtable.authorizedViews.getIamPolicy`
  * `bigtable.authorizedViews.setIamPolicy`
  * `bigtable.authorizedViews.readRows`
  * `bigtable.authorizedViews.sampleRowKeys`
  * `bigtable.authorizedViews.mutateRows`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To learn how to manage Bigtable IAM roles at the authorized-view level, see [authorized view-level IAM management](https://docs.cloud.google.com/bigtable/docs/access-control#iam-management-view).

**Note:** If you want to perform an authorized views operation using the Google Cloud console, open the Cloud Shell and run the gcloud CLI command for the operation.

## Create an authorized view

When you create an authorized view, consider the queries that will be run against it. **Read, write, and delete requests that are sent to an authorized view must reference only data that is in the authorized view.** This means, for example, that if you attempt to read, write to, or delete a row that has columns in the table that are not in your authorized view, the request fails.

To avoid a situation where data requests to an authorized view fail because columns have been added to the table that aren't in the authorized view, you can specify an empty column qualifier prefix "" for a column family.

You can specify up to 100 definition parameters per authorized view.

### Console

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the table that you want an authorized view of.

  3. In the navigation pane, click **Bigtable Studio.**

  4. Click **Builder** to open the query builder.

  5. Choose the table that you want an authorized view of.

  6. Add clauses to build a query that returns only data that you want the authorized view users to have access to.

     * Acceptable clauses for an authorized view are **row key prefix** and **columns** (column qualifiers).
     * To specify a column qualifier prefix, add an asterisk after the prefix. For example, to include all columns that start with "data", enter `data*` in the **Columns** field after the column family name.
     * The **Limit** clause is ignored when the authorized view is saved.
     * For more information on using the query builder, see [Build queries in the console](https://docs.cloud.google.com/bigtable/docs/query-builder).
  7. Click **Run**.

  8. After you've verified that the results pane shows data that should be included in the authorized view, click **Save as view**.

  9. Enter a permanent identifier for the authorized view that is not already in use for the table.

  10. Optional: To save without granting access, click **Save**.

  11. Optional: To save the authorized view and then configure access for it, click **Save & grant access**. For more information about access control, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

     1. Add at least one principal and select the role to which that principal or group of principals should be assigned.
     2. Optional: To grant access for additional roles, click **Add another role** and then enter the principal and role for each additional role.
     3. Click **Save**.



### gcloud

Run the `bigtable authorized-views create` command. For more information, see the reference documentation at [gcloud bigtable authorized-views create](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/create).
    
    
    gcloud bigtable authorized-views create AUTHORIZED_VIEW_ID \
      --instance=INSTANCE_ID \
      --table=TABLE_ID \
      --definition-file=DEFINITION_FILE_PATH
    

Replace the following:

  * `AUTHORIZED_VIEW_ID`: a permanent identifier for the authorized view that is not already in use for the table
  * `INSTANCE_ID`: the permanent identifier for the instance that contains the table
  * `TABLE_ID`: the permanent identifier of that table you are creating an authorized view of
  * `DEFINITION_FILE_PATH`: the path to a valid JSON formatted representation of an authorized view. For examples of correctly formatted definition files, see [Definition file examples](https://docs.cloud.google.com/bigtable/docs/authorized-views#definition-file-examples).



You can also run the command without supplying the definition file. In this case, the gcloud CLI opens an editor and prompts you for values.

To confirm that the authorized view has been created, get a list of authorized views for the table.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    try {
      AuthorizedView.SubsetView subsetView =
          AuthorizedView.SubsetView.newBuilder()
              .addRowPrefixes(ByteString.EMPTY)
              .putFamilySubsets(
                  COLUMN_FAMILY,
                  AuthorizedView.FamilySubsets.newBuilder()
                      .addQualifierPrefixes(ByteString.copyFromUtf8(COLUMN_QUALIFIER_NAME))
                      .build())
              .build();
      AuthorizedView authorizedViewObj =
          AuthorizedView.newBuilder().setSubsetView(subsetView).build();
      CreateAuthorizedViewRequest request =
          CreateAuthorizedViewRequest.newBuilder()
              .setParent(
                  "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId)
              .setAuthorizedViewId(authorizedViewId)
              .setAuthorizedView(authorizedViewObj)
              .build();
      AuthorizedView authorizedView = adminClient.createAuthorizedViewAsync(request).get();
      System.out.printf("AuthorizedView: %s created successfully%n", authorizedView.getName());
    } catch (Exception e) {
      System.err.println("Failed to create an authorized view: " + e.getMessage());
    }

## Modify an authorized view

### Console

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the authorized view.

  3. In the navigation pane, click **Bigtable Studio.**

  4. In the explorer, expand the table and **Authorized views**.

  5. Next to the authorized view that you want to modify, click the more_vert action menu, and then click **Open**.

  6. Modify or add clauses to build a query that returns only data that you want the authorized view users to have access to.

     * Acceptable clauses for an authorized view are **row key prefix** and **columns** (column qualifiers).
     * To specify a column qualifier prefix, add an asterisk after the prefix. For example, to include all columns that start with "data", enter `data*` in the **Columns** field after the column family name.
     * The **Limit** clause is ignored when the authorized view is saved.
     * For more information on using the query builder, see [Build queries in the console](https://docs.cloud.google.com/bigtable/docs/query-builder).
  7. Click **Run**.

  8. After you've verified that the results pane shows data that should be included in the authorized view, click **Save as view**.

  9. In the dialog, enter the ID of the authorized view that you modified.

The dialog displays a message warning you that you are overwriting the existing authorized view.

  10. Optional: To save without granting access, click **Save**.

**Important:** If you don't reconfigure access for the authorized view after modifying the query it's based on, the previous access control settings are overwritten and the authorized view inherits permissions from the table.
  11. Optional: To save the authorized view and then configure access for it, click **Save & grant access**. For more information about access control, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

     1. Add at least one principal and select the role to which that principal or group of principals should be assigned.
     2. Optional: To grant access for additional roles, click **Add another role** and then enter the principal and role for each additional role.
     3. Click **Save**.



### gcloud

Modify an authorized view using the `bigtable authorized-views update` command. For more information, see the reference documentation at [gcloud bigtable authorized-views update](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/update).
    
    
    gcloud bigtable authorized-views update AUTHORIZED_VIEW_ID \
      --instance=INSTANCE_ID \
      --table=TABLE_ID \
      --definition-file=DEFINITION_FILE_PATH
    

Replace the following:

  * `AUTHORIZED_VIEW_ID`: the permanent identifier for the authorized view
  * `INSTANCE_ID`: the permanent identifier for the instance
  * `TABLE_ID`: the permanent identifier of the source table
  * `DEFINITION_FILE_PATH`: the path to a valid JSON formatted representation of an authorized view. For examples of correctly formatted definition files, see [Definition file examples](https://docs.cloud.google.com/bigtable/docs/authorized-views#definition-file-examples).



You can also run the command without supplying the definition file. In this case, the gcloud CLI opens an editor and prompts you for values.

Optional: To prevent the gcloud CLI from displaying a confirmation prompt showing the difference between the current authorized view structure and after the update is committed, append the `--no-interactive` flag to the command.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    try {
      // Update to an authorized view permitting everything.
      AuthorizedView.SubsetView subsetView =
          AuthorizedView.SubsetView.newBuilder()
              .addRowPrefixes(ByteString.EMPTY)
              .putFamilySubsets(
                  COLUMN_FAMILY,
                  AuthorizedView.FamilySubsets.newBuilder()
                      .addQualifierPrefixes(ByteString.EMPTY)
                      .build())
              .build();
      AuthorizedView authorizedViewObj =
          AuthorizedView.newBuilder()
              .setSubsetView(subsetView)
              .setName(
                  "projects/"
                      + projectId
                      + "/instances/"
                      + instanceId
                      + "/tables/"
                      + tableId
                      + "/authorizedViews/"
                      + authorizedViewId)
              .build();
      UpdateAuthorizedViewRequest request =
          UpdateAuthorizedViewRequest.newBuilder()
              .setAuthorizedView(authorizedViewObj)
              .setUpdateMask(FieldMask.newBuilder().addPaths("subset_view").build())
              .build();
      AuthorizedView authorizedView = adminClient.updateAuthorizedViewAsync(request).get();
      System.out.printf("AuthorizedView: %s updated successfully%n", authorizedView.getName());
    } catch (Exception e) {
      System.err.println("Failed to modify authorized view: " + e.getMessage());
    }

### Enable or disable deletion protection

To enable deletion protection for an authorized view, modify the JSON file that defines your authorized view by setting the `deletionProtection` flag to `true`.

To disable deletion protection, modify the JSON file that defines your authorized view by setting the `deletionProtection` flag to `false`.

Finalize changes to your authorized view by running the `bigtable authorized-views update` command with the name of the updated JSON file. For more information, see the reference documentation at [gcloud bigtable authorized-views update](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/update).

## Delete an authorized view

If you delete a table, all authorized views of the table are also deleted.

If you delete an authorized view, you can't undelete it. However, if you delete a table and then undelete the table, all authorized views of the table are restored along with the table. Then you must reconfigure IAM for the authorized views as well as for the tables. For more information, see [Undelete a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#undelete-table).

### Console

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the authorized view.

  3. In the navigation pane, click **Bigtable Studio.**

  4. In the explorer, expand the table and **Authorized views**.

  5. Next to the authorized view that you want to delete, click the more_vert action menu, and then click **Delete**.




### gcloud

Delete an authorized view using the `bigtable instances tables authorized-views delete` command. For more information, see the reference documentation at [gcloud bigtable authorized-views delete](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/delete).
    
    
    gcloud bigtable authorized-views delete AUTHORIZED_VIEW_ID \
      --instance=INSTANCE_ID \
      --table=TABLE_ID
    

Replace the following:

  * `AUTHORIZED_VIEW_ID`: the permanent identifier for the authorized view
  * `INSTANCE_ID`: the permanent identifier for the instance
  * `TABLE_ID`: the permanent identifier of the source table



Optional: To prevent the gcloud CLI from displaying a confirmation prompt requiring you to confirm or cancel the deletion, append the `--nointeractive` flag to the command.

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    try {
      adminClient.deleteAuthorizedView(
          "projects/"
              + projectId
              + "/instances/"
              + instanceId
              + "/tables/"
              + tableId
              + "/authorizedViews/"
              + authorizedViewId);
      System.out.printf("AuthorizedView: %s deleted successfully%n", authorizedViewId);
    } catch (NotFoundException e) {
      System.err.println("Failed to delete a non-existent authorized view: " + e.getMessage());
    }

## Get a list of authorized views for a table

### Console

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the authorized view.

  3. In the navigation pane, click **Bigtable Studio.**

  4. In the explorer, expand the table and **Authorized views**.




### gcloud

Run the `bigtable authorized-views list` command. For more information, see the reference documentation at [gcloud bigtable authorized-views list](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/list).
    
    
    gcloud bigtable authorized-views list \
      --instance=INSTANCE_ID \
      --table=TABLE_ID
    

Replace the following:

  * `INSTANCE_ID`: the permanent identifier for the instance
  * `TABLE_ID`: the permanent identifier for the table



### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    List<String> authorizedViewIds = new ArrayList<>();
    try {
      ListAuthorizedViewsRequest request =
          ListAuthorizedViewsRequest.newBuilder()
              .setParent(
                  "projects/" + projectId + "/instances/" + instanceId + "/tables/" + tableId)
              .build();
      for (AuthorizedView view : adminClient.listAuthorizedViews(request).iterateAll()) {
        String id = AuthorizedViewName.parse(view.getName()).getAuthorizedView();
        System.out.println(id);
        authorizedViewIds.add(id);
      }
    } catch (NotFoundException e) {
      System.err.println(
          "Failed to list authorized views from a non-existent table: " + e.getMessage());
    }

## View details about an authorized view

### Console

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the authorized view.

  3. In the navigation pane, click **Bigtable Studio.**

  4. In the explorer, expand the table and **Authorized views**.

  5. Next to the authorized view that you want to view, click the more_vert action menu, and then click **Open**.




### gcloud

To get details about an authorized view, run the `bigtable instances tables authorized-views describe` command. For more information, see the reference documentation at [gcloud bigtable authorized-views describe](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/describe).
    
    
    gcloud bigtable authorized-views describe \
    –-instance=INSTANCE_ID \
    –-table=TABLE_ID \
    AUTHORIZED_VIEW_ID
    

Replace the following:

  * `INSTANCE_ID`: the permanent identifier for the instance
  * `TABLE_ID`: the permanent identifier for the table
  * `AUTHORIZED_VIEW_ID`: the permanent identifier for the authorized view



### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/bigtable/docs/authentication#client-libs). 
    
    
    AuthorizedView authorizedView = null;
    try {
      authorizedView =
          adminClient.getAuthorizedView(
              "projects/"
                  + projectId
                  + "/instances/"
                  + instanceId
                  + "/tables/"
                  + tableId
                  + "/authorizedViews/"
                  + authorizedViewId);
      AuthorizedView.SubsetView subsetView = authorizedView.getSubsetView();
    
      for (ByteString rowPrefix : subsetView.getRowPrefixesList()) {
        System.out.printf("Row Prefix: %s%n", rowPrefix.toStringUtf8());
      }
      for (Map.Entry<String, AuthorizedView.FamilySubsets> entry :
          subsetView.getFamilySubsetsMap().entrySet()) {
        for (ByteString qualifierPrefix : entry.getValue().getQualifierPrefixesList()) {
          System.out.printf(
              "Column Family: %s, Qualifier Prefix: %s%n",
              entry.getKey(), qualifierPrefix.toStringUtf8());
        }
        for (ByteString qualifier : entry.getValue().getQualifiersList()) {
          System.out.printf(
              "Column Family: %s, Qualifier: %s%n", entry.getKey(), qualifier.toStringUtf8());
        }
      }
    } catch (NotFoundException e) {
      System.err.println(
          "Failed to retrieve metadata from a non-existent authorized view: " + e.getMessage());
    }

## Grant access to an authorized view

For more information about access control, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

### Console

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that contains the authorized view.

  3. In the navigation pane, click **Bigtable Studio.**

  4. In the explorer pane, expand the table and **Authorized views**.

  5. Next to the authorized view name, click the more_vert action menu, and then click **Grant access**.

  6. Add at least one principal and select the role to which that principal or group of principals should be assigned.

  7. Optional: To grant access for additional roles, click **Add another role** and then enter the principal and role for each additional role.

  8. Click **Save**.




### gcloud

To grant access to an authorized view, use the `bigtable authorized-views add-iam-policy-binding` command. For more information, see the reference documentation at [gcloud bigtable authorized-views add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/authorized-views/add-iam-policy-binding).
    
    
    gcloud bigtable authorized-views add-iam-policy-binding AUTH_VIEW_ID \
    --instance=INSTANCE_ID --table=TABLE_ID \
    --member=PRINCIPAL --role=ROLE
    

Replace the following:

  * `AUTH_VIEW_ID`: the ID for the authorized view
  * `TABLE_ID`: the ID for the table that the authorized view is of
  * `INSTANCE_ID`: the instance that contains the table
  * `PRINCIPAL`: the principal (user) to whom you want to grant access, such as `user:222larabrown@gmail.com`
  * `ROLE`: the role that you are granting, such as `roles/bigtable.reader`.



## What's next

  * [Encrypt data by using CMEK.](https://docs.cloud.google.com/bigtable/docs/use-cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
