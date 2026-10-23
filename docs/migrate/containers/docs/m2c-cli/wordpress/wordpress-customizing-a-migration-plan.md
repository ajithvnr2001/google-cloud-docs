---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/wordpress/wordpress-customizing-a-migration-plan/
title: Customize migration plan for WordPress sites \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:44.690054+00:00
---

# Customize migration plan for WordPress sites  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/wordpress/wordpress-customizing-a-migration-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customize migration plan for WordPress sites

You should review the migration plan file that resulted from creating a migration. Customize the file before executing the migration. The details of your migration plan are used to extract the workload container artifacts from the source.

This section describes the contents of the migration and the kinds of customizations you might consider before you execute the migration and generate deployment artifacts.

## Before you begin

  * Ensure that you've already [created a migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan) and have the migration plan file.

  * If your WordPress site relies on a database connection, then ensure that the [database is accessible](https://docs.cloud.google.com/migrate/containers/docs/planning-best-practices#ensure_databases_are_accessible) from the target cluster as Migrate to Containers doesn't automatically migrate it.


**Note:** To change the site's URL as part of the migration, you need to [update the database contents](https://wordpress.org/documentation/article/changing-the-site-url/).

## Edit the migration plan

After you have copied the file system and analyzed it, you can find the migration plan in the new directory that is created in the specified output path: ANALYSIS_OUTPUT_PATH/`config.yaml`.

Edit the migration plan as necessary and save the changes.

Review your migration plan details and guiding comments to add information as needed. Specifically, consider edits around the following sections.

## Migration plan structure

The migration plan for a WordPress workload has the following structure, which you can customize as described in the following sections.
    
    
    sites:
    - # Image name. Edit this to change the artifacts naming.
      imageName: wordpress
      # Parent WordPress image for the generated container image.
      fromImage: wordpress:6.1-php7.4-apache
      # WordPress root directory.
      rootDirectory: /var/www/html/
      # Database connection values.
      databaseValues:
      - name: DB_NAME
        value: database_name_here
      - name: DB_USER
        value: username_here
      - name: DB_PASSWORD
        value: password_here
      - name: DB_HOST
        value: host_here
    

To add information as needed, review your migration plan details and guiding comments.

Specifically, consider edits around the following sections.

### Specify the Docker image

In the migration plan, generate a Docker community image tag based on the WordPress version.

If you want to change the Docker community image, or provide your own docker image, you can modify the `fromImage` tag in your migration plan using the following format:
    
    
    # Parent WordPress image for the generated container image.
      fromImage: wordpress:6.1-php7.4-apache

### Specify the database connection configuration

The `databaseValues` section contains the database connection configuration extracted from the VM. Modify these values to change the database connection.

These values are passed to the migrated pod.

## Data migration plan structure

The data migration plan for a WordPress workload has the following structure:
    
    
    volumes:
    - deploymentPvcName: wordpress-pvc
      folders:
      - /var/www/html/wp-content
      newPvc:
        spec:
          accessModes:
          - ReadWriteOnce
          resources:
            requests:
              storage: 10G
    

The uploaded content, plugins, and themes that reside in the `wp-content` folder in your WordPress VM are exported to a persistent volume claim (PVC). The PVC is attached and mounted to the migrated pod.

## What's next

  * Learn how to [execute the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
