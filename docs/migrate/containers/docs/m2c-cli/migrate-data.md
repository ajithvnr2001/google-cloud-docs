---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/migrate-data/
title: Migrate data \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:32.641550+00:00
---

# Migrate data  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/migrate-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate data

This page describes how to run a data migration that copies files from the local machine to a persistent volume claim (PVC) in the target cluster.

This is an optional step.

## Customize your data migration configuration

When you [complete an analysis](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan), Migrate to Containers CLI might create a data configuration file named `dataConfig.yaml` in the specified analysis output directory. This indicates that to complete the migration, you need to perform data migration.

You can also create this data configuration file manually for data migration, and provide information about your target data volume or data claim.

Following is an example of a data configuration file:
    
    
    volumes:
    - deploymentPvcName: my-pvc1
      existingPvc:
        name: my-pvc1
      folders:
      - /bin
      - /opt
    - deploymentPvcName: my-pvc2
      newPvc:
       spec:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 10G
      folders:
      - /bin
      - /opt
    

Where:

  * `deploymentPvcName`: The PVC name to be used by Migrate to Containers in your deployed workload to access this volume.

**Note:** In case you've already [executed the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan), if you change this PVC name in the data configuration file, ensure that you make the same change in the other migration artifacts, or execute the migration again to update the generated artifacts.
  * `existingPvc`:

    * `name`: Name of an existing persistent volume claim (PVC). Define if you want to migrate data volumes to an existing PVC.
  * `newPvc`: Define if you want to migrate your data volumes to a new PVC. You can define your PVC using the standard PVC spec syntax.

For more information about Kubernetes PVC spec, see the [Kubernetes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) documentation.

**Note:** You can migrate a data volume to either an existing PVC or a new PVC. Therefore, you must only define one of the two parameters, `existingPvc` or `newPvc`, per volume.
  * `folders`: the folder you want to migrate from the VM to PVC. These folders are copied to the PVC in the same path.




You can edit your data configuration file for several data migration use cases, including:

  * Using an existing PVC
  * Creating new volumes on your migrated VM
  * Migrating multiple PVCs with multiple file paths



### Use an existing PVC

If you've already allocated the storage for your migrated data, and have a PVC to store your data, you can migrate your data using an existing PVC.

Define an existing PVC in your data configuration file `dataConfig.yaml` by passing your existing volume in the `existingPvc` field. In this case, your data configuration file would look like this:
    
    
    volumes:
    - deploymentPvcName: my-pvc
      existingPvc:
        name: my-pvc
        subpath: /subpath
      folders:
      - /bin
      - /opt
    

In the previous sample, the `existingPvc` entry can contain an optional `subPath` to migrate data to the subpath of the PVC, as shown.

**Note:** The PVC has to be in the same namespace as the target namespace on the deployment cluster.

### Create new data volumes on your migrated VMs

If you've not allocated storage ahead of time, and you want your storage to be created during the migration process, you can pass an empty `existingPvc` field and specify the storage you would like to be created in the `newPvc` field:
    
    
    volumes:
    - deploymentPvcName: my-pvc
      newPvc:
        spec:
          accessModes:
          - ReadWriteOnce
          resources:
            requests:
              storage: 10G
      folders:
      - /bin
      - /opt
    

**Note:** If you don't want to worry about the specifics of your backing storage, use an empty string for the storage class, as shown in the preceding yaml.

### Migrate multiple PVCs with multiple file paths

You can specify the set of directories under the `folders` list field of each entry in the `volume` list for each PVC listed in your data configuration file `dataConfig.yaml`:
    
    
    volumes:
    - deploymentPvcName: my-pvc1
      existingPvc:
        name: my-pvc1
      folders:
      - /bin
      - /opt
    - deploymentPvcName: my-pvc2
      newPvc:
       spec:
        accessModes:
        - ReadWriteOnce
        resources:
         requests:
           storage: 10G
      folders:
      - /bin
      - /opt
    

The paths you list under `folders` in the data configuration file are copied to the same paths in the target PVCs.

## Execute the data migration

After you've customized your data configuration file `dataConfig.yaml`, to migrate the data volumes to a PVC in the target cluster, run the following command:
    
    
    ./m2c migrate-data  -i ANALYSIS_OUTPUT_PATH -n NAMESPACE
    

Replace the following:

  * ANALYSIS_OUTPUT_PATH: the path where you saved the [analysis output](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan) that contains the file `dataConfig.yaml`
  * NAMESPACE: the target Kubernetes cluster namespace of the deployed network



## What's next

  * Learn how to [clean up your local machine](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/clean-up).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
