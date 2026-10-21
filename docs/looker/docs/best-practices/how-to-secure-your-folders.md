---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-secure-your-folders/
title: Best practice: Secure your folders! A content access walk-through \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:32.491455+00:00
---

# Best practice: Secure your folders! A content access walk-through  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-secure-your-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Best practice: Secure your folders! A content access walk-through Stay organized with collections  Save and categorize content based on your preferences. 

_These best practices reflect recommendations shared by a cross-functional team of seasoned Lookers. These insights come from years of experience working with Looker customers from implementation to long-term success. The practices are written to work for most users and situations, but as always use best judgment when implementing._

This page provides administrators of Looker instances with a guided example of setting up [content access controls](https://docs.cloud.google.com/looker/docs/access-levels). We will walk through the implementation process, starting with a new project and continuing over models, model sets, permission sets, groups, roles, and user attributes. 

First, an analogy to understand the primary Looker features in this context: 

A [**project**](https://docs.cloud.google.com/looker/docs/how-project-works) is like a home. 

A [**model**](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) is a room in the home that is filled with specific content. 

A [**model set**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) is a group of rooms or a single room (bedrooms, kitchen). 

A [**permission set**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets) is an activity checklist, specifying what people can do in a room (eat, play, sleep). 

A [**group**](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) is a way to combine people with shared characteristics (adults, kids, guests). 

A [**role**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) is how to give groups of people their activity checklists in different sets of rooms. 

A [**user attribute**](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) is a key that opens up special items in the house (teapot, power tools). 

## Scenario

The following is an example of a startup with finance, sales, and product teams. The CEO is our only admin, and she wants each team to see only the content that is relevant to them, with the exception that each team's VP should have access to all teams' content. She wants different feature access for standard employees, managers, and VPs. 

  * **Standard employees** should be able to view and explore data in their own models.
  * **Managers** should have standard access and also be able to download and schedule content.
  * **VPs** should have _almost_ all privileges, except for a few reserved for just the CEO.



The CEO wants salespeople to be able to view the data for their their own activities, but not be able to view another salesperson's individual sales numbers. However, sales managers should be able to view every salesperson's numbers. And finally, there are some finance fields with sensitive information that she wants masked for the standard employees using that model. 

Here is the organizational chart: 

![Organizational chart for the startup in this example.](https://docs.cloud.google.com/static/looker/docs/images/hc-secure-folders-example-org-chart-2210.png)

This chart reveals the following organizational structure for our example startup: 

  * CEO
    * VP of Finance
      * Finance Manager
        * Accountant
    * VP of Sales
      * Sales Manager West
        * Salesperson West
      * Sales Manager East
        * Salesperson East
    * VP of Product
      * Product Manager
        * Engineer



Implementing the desired access controls will involve the following steps: 

  1. **Create a project:** A project is the structural link between a database connection and data models.
  2. **Add models:** Decide what data will be revealed to which users.
  3. **Create model sets:** Group relevant models together.
  4. **Create permission sets:** Explicitly define the actions users can take within a model set.
  5. **Create groups:** Bucket similar users together.
  6. **Create roles:** Create the connections between model sets, permission sets, and groups.
  7. **Edit content access:** Manage which dashboards and Looks users can view via folders.
  8. **Add data filters:** Further filter the data that specific users can access within a model.



## 1\. Create a project

The first thing we need is a [project](https://docs.cloud.google.com/looker/docs/how-project-works), which is a container for one or more [models](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files). If you already have a project set up, you can skip this step. Otherwise, you can navigate to the **LookML Projects** page by selecting **Projects** in the **Develop** section of Looker and selecting **New LookML Project** to create a new project. For more detailed instructions on creating a new project, see the [Generating a model](https://docs.cloud.google.com/looker/docs/generating-a-model) documentation page. 

On the **New Project** page, we'll create a project with the following settings: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-new-project-2210.png)

  * In the **Name** section, we give the project a name.
  * In the **Starting Point** section, we select **Generate Model from Database Schema**.
  * In the **Connection** drop-down menu, we select the name of our database connection.
  * In the **Build Views From** section, for this example, we select the **All Tables** option so that the LookML generator creates a view file for each table in your database.



Once the desired settings for the new project have been configured, we select **Create Project**. 

Upon creating a project, you'll be brought to the project's auto-generated LookML model. At this point, you'll need to use the **Configure Git** button to set up version control for the project. Detailed instructions on setting up version control are on the [Setting up and testing a Git connection](https://docs.cloud.google.com/looker/docs/setting-up-git-connection) documentation page. 

## 2\. Add models

A data [model](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) is like a customizable portal into the database. Each model may expose different data to users. In our example, our salespeople need different data than our engineers do, so we'll add separate models to expose the appropriate information from the database to each kind of user. 

In our LookML project, we'll [add new LookML model files](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) with the names of each of our desired models (`finance`, `sales`, and `product`). Make sure to define at least one [Explore](https://docs.cloud.google.com/looker/docs/reference/param-explore-explore) in each model file; this will allow us to select the model when creating model sets (otherwise, they won't show up in the selection). For additional reference on how to use the `explore` parameter in your model file, see the [Understanding model and view files](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) documentation page. 

Once we have successfully added the models, we will still need to configure them. To [ configure the models](https://docs.cloud.google.com/looker/docs/generating-a-model#when_you_need_to_configure_models), we'll go back to the **Projects** page in the **Develop** section, which should now show red text reading "Configuration required for use" inline with each model name. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-config-required-2210.png)

Next to each model, select **Configure**. We will make sure our project name is correct, along with the connections we will allow this model to use, then save. 

![The Configure a Model page lets you check the model name, the project, and the allowed connections for the model.](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-check-config-2210.png)

After all the models are configured correctly, the red configuration issue messages we encountered previously will no longer appear. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-config-correct-2210.png)

Remember that in Looker, granting a user the [`see_lookml`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml) or [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permission on one model grants them that permission for all models in that project. Therefore, you should make separate projects if you want to partition permission to view or develop LookML. Otherwise, you should just create a new model. Model permissions are sufficient to ensure that only certain people can query certain data. 

For more on permissions, check out our documentation on [roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles). 

## 3\. Create model sets

Now that the data models for each department have been configured, we'll add the corresponding model for each department into the [model sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) we build. To create new model sets, we'll navigate to the **Roles** page in the **Admin** panel and select **New Model Set**. For further instructions on creating new model sets, see the [Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#creating_a_model_set) documentation page. 

Once the new model sets have been created, they will be displayed in the **Model Sets** section of the **Roles** page, as in the following example screenshot: 

![The finance, product, and sales models correspond to the Finance, Product, and Sales model sets on the Model Sets page.](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-example-model-sets-2210.png)

## 4\. Create permission sets

Next, we will create [permission sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets) using the model sets we have just made. As mentioned when we set up the scenario, we want four tiers of permissions corresponding with the four hierarchical levels in the organization chart, and higher tiers should include the permissions for the tiers below. In our scenario we'll identify the permission sets as follows: 

  * The CEO has the **Admin** permission set.
  * VPs have the **Limited Admin** permission set.
  * Managers have the **Download and Share** permission set.
  * Standard employees have the **View and Explore** permission set.



To create new permission sets, we'll navigate to the **Roles** page in the **Admin** panel and select **New Permission Set**. For each permission tier, we'll select the appropriate permissions. In general, permission sets should overlap as little as possible, with each set adding only the specific permissions we want the users with this permission set to have. This is because we will be giving some users multiple permission sets, and we want to know exactly what each permission set allows. However, because of the tree structure, some overlap is often necessary. 

In our example, we want the **View and Explore** permission set to allow users to view content, ask questions, and save useful tiles. So, we'll give them permissions associated with seeing content (such as `see_looks` and `see_user_dashboards`), the `explore` permission, and the `save_content` permission. The notable exceptions here are `see_lookml` which we may only want for developers, and `see_sql`, which we reserve for those who both understand SQL and are trusted to view the database structure. All of these permissions are strictly under the `access_data` branch. We are not giving any of the `see` permissions at the bottom of the tree, because they are administrative permissions. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-view-and-explore-permissions-2210.png)

For the **Download and Share** permission set, we'll add the permissions associated with downloading, scheduling, sharing, creating public Looks (which allows sharing of Looks to non-Looker users), and `see_schedules` (because they can create schedules, it's logical that they can also view them in the Admin panel). 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-download-and-share-permissions-2210.png)

The only fields that have been selected when configuring both the **View and Explore** and the **Download and Share** permission sets are the parent permissions required to select the added child permissions under the `access_data` branch. Therefore, since users with the **Download and Share** permission set will also have the **View and Explore** permission set, it is not necessary to include permissions like `see_lookml_dashboards`, `see_user_dashboards`, and `explore` in the **Download and Share** permission set, since these permissions do not contain any child permissions that are needed for the **Download and Share** permission set. 

Finally, for our **Limited Admin** permission set, we'll add most of the administrative permissions at the bottom of the tree, excluding the `manage_models` and `sudo` privileges that the CEO wants only for herself. That looks like this: 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-limited-admin-permissions-2210.png)

When it's all done, the permission sets will include the following permissions: 

  * **Admin** : The **Admin** permission set, which is reserved for the CEO of our example company, includes all permissions.
  * **Limited Admin** : The **Limited Admin** permission set includes the `create_prefetches`, `login_special_email`, `manage_homepage`, `manage_spaces`, `see_alerts`, `see_datagroups`, `see_logs`, `see_pdts`, `see_queries`, `see_users`, and `update_datagroups` permissions.
  * **Download and Share** : The **Download and Share** permission set includes the `access_data`, `create_public_looks`, `download_with_limit`, `download_without_limit`, `save_content`, `schedule_external_look_emails`, `schedule_look_emails`, `see_looks`, `see_schedules`, `send_outgoing_webhook`, `send_to_s3`, and `send_to_sftp` permissions.
  * **View and Explore** : The **View and Explore** permission set includes the `access_data`, `create_table_calculations`, `explore`, `save_content`, `see_drill_overlay`, `see_lookml_dashboards`, `see_looks`, and `see_user_dashboards` permissions. 



You can view the permissions that belong to an existing permission set by navigating to the **Permission Sets** section of the **Roles** admin page. 

## 5\. Create groups

The next step is to create the [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) and bucket our users. We will create groups for both standard employees and managers in each department, because these will eventually match the different roles we later create. VPs will be in their own group and the CEO doesn't need a group. When completed, the **Groups** page should list the following groups and their corresponding group IDs, which are automatically generated by Looker. For example: 

ID | Name  
---|---  
1 | All Users  
3 | Finance  
4 | Sales  
5 | Product  
7 | Sales Manager  
8 | Product Manager  
9 | Finance Manager  
10 | VPs  
  
With the groups created, we'll need to add users into those groups. For instructions on adding users to groups, see the [Groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#editing_groups) documentation page. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-limited-admin-permissions-2210.png)

When adding users to the groups we have created, remember that because of the way we have structured permissions, the higher-tier groups may be included in the lower-tier groups. For example, we want the VPs in the **Finance** group, but we do not want the Sales Managers in the **Product** group. An efficient way to approach this is to start by adding users to the higher-tier groups (like VPs), so we can add them as a group to the lower tiers. 

## 6\. Create roles

Now that we have our model sets, permission sets, and groups in place, we can put them all together using [roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#roles). Every role will have a single permission set and a single model set, and may include one or more groups. Because roles must include a model set, we'll again create roles both for standard employees and for managers for each department. 

  * **Standard roles** : Standard roles will include the **View and Explore** permission set, along with the corresponding model set. Assign standard roles to the standard and manager groups for that department, and to the VP. For example, assign the **Standard Finance** role to the **Finance** and **Finance Manager** groups, and to the VP of Finance.
  * **Manager roles** :Manager roles will have the **Download and Share** permission set, along with the corresponding model set. These roles should be assigned to the manager group for the corresponding department, and to the department's VP.
  * **Manager roles** :Manager roles will have the **Download and Share** permission set, along with the corresponding model set. These roles should be assigned to the manager group for the corresponding department, and to the department's VP.
  * **VP role** : The VP role will have the **Limited Admin** permission set and the **All** model set. This role will be assigned to the **VPs** group.



## 7\. Edit content access

The next step is to organize our folder access permissions so that each group has access to their own (and only their own) content. Here is the layout of folders in our example instance, which can be viewed by navigating to the **Content Access** page in the Admin panel: 

![The Shared folder contains Finance, Product, and Sales folders, which contain folders for their departments' use.](https://docs.cloud.google.com/static/looker/docs/images/hc-content-access-folder-structure-2210.png)

Access to folders follows the rules of hierarchical inheritance. For more information on how this works, check out our documentation on [access levels](https://docs.cloud.google.com/looker/docs/access-levels) and on [access control and permission management](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management). 

Following the [rules for folder access](https://docs.cloud.google.com/looker/docs/access-levels#types_of_access_to_folders), we want to give **View** access to all users in the **Shared** folder. We'll give each group **View** access to the parent folders in the tree above the folders that the group will have access to. This way, as we traverse down the tree, if we don't want a group to see a folder, we won't include that group when giving access. 

We can give the **Manage Access, Edit** access level to groups in a folder where we want to control who sees that folder. In our example, we only want the CEO and VPs to have those permissions; everyone else will only have **View** access to the folders they need. 

## 8\. Add data access restrictions with user attributes

This section shows methods for preventing specific users from accessing particular rows or columns of data from a model they have access to. Remember, our CEO wants salespeople to be able to view the data for their own individual activities, but not others' activities. Sales managers, however, should be able to view every salesperson's numbers. To do this, we'll leverage [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) and the [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) parameter. 

### Create user attributes

First, we will create a new user attribute called `access_level` that is hidden from users. This will allow us to define access tiers for the different groups we have. We will set the following values when [creating our user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#creating_user_attributes): 

  * **Name** : `access_level`
  * **Label** : Access Level
  * **Data Type** : String
  * **User Access** : Edit
  * **Hide Values** : No



In our example, we'll leave the **Set a default value** box unchecked. 

While creating the field, we'll configure three levels of access: **Basic** , **Premium** , and **Full**. We'll assign those levels to the standard, manager, and VP groups, respectively. This is done under the **Group Values** tab in the same section. See the [Assigning values to user groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups) section of the **User attributes** documentation for more details. 

Because the order of these rules matters, we want to place the highest access values at the top of the list, to override the lower access values toward the bottom. This behavior is further explained on our [User attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups) documentation page. 

### Filtering row data with user attributes

We will imagine that there is already an Explore being built with all the sales information in it. We will check the access level of the user querying the Explore; if the access level is **Basic** (which we've given to all our standard salespeople) then we'll always filter the Explore on the user's name, so only each salesperson's own rows are accessible to them. If the access level is **Premium** or **Full** , then the query will not get filtered. By default, we have a user attribute called **Name** which is the name of the Looker user. The LookML for the Explore will look like this: 
    
    
    explore: sales_info {
      sql_always_where: {% if {{_user_attributes['access_level']}} == "Basic" %}
        ${sales_info.name} = "{{_user_attributes['name']}}"
        % endif %
      ;;
    }
    

### Filtering column data with user attributes

Lastly, there are some PII (personally identifiable information) columns in the finance model that we want to hide from some of our users as well. To do this, we can use the user attributes we've created, along with the instructions for applying database-level permissions in Looker on the [User attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#use_case:_applying_database-level_permissions_in_looker) documentation page, to give only users with the **Full** access level the ability to see the PII fields. 

And we are done! We have finished setting up our content and data access controls and all of our users are free to explore Looker. By doing this we can be assured that they'll only see the content that we've allowed them to see. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
