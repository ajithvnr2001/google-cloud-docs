---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/websphere/websphere-customizing-a-migration/
title: Customize migration plan for WebSphere workloads \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:31.940467+00:00
---

# Customize migration plan for WebSphere workloads  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/websphere/websphere-customizing-a-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Customize migration plan for WebSphere workloads

## Before you begin

This document assumes that you've already [created a migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan) and have the migration plan file.

## Edit the migration plan

After you have copied the file system and analyzed it, you can find the migration plan in the new directory that is created in the specified output path: ANALYSIS_OUTPUT_PATH/`config.yaml`.

Edit the migration plan as necessary and save the changes.

Review your migration plan details and guiding comments to add information as needed.

Specifically, consider edits around the following sections.

## Migration plan structure

The migration plan for WebSphere workloads has the following structure, which you can customize as described in the following sections.
    
    
    # List of discovered WebSphere application servers and how to migrate their
    # hosted applications to containers.
    webSphereApplicationServers:
    # The application server installation path.
    - home: /opt/ibm/wlp
      applicationServerInfo:
        name: WebSphere Application Server
        profile: Liberty
        version: 23.0.0.4
        edition: Base
        # List of Java installations available to the application server.
        javaDevelopmentKits:
        - home: /opt/ibm/java
          vendor: IBM Corporation
          version:
            jdk: java version 1.8.0_361
            jre: Java(TM) SE Runtime Environment
            jvm: IBM J9 VM
      # List of hosted applications and how to migrate them to containers.
      applications:
      - path: /opt/ibm/wlp/usr/servers/defaultServer/apps/app.war
        # Application archives to be migrated into the target container.
        archives:
        - /opt/ibm/wlp/usr/servers/defaultServer/apps/app.war
        # Application configuration files to be migrated into the target container.
        configurations:
          serverXML: /opt/ibm/wlp/usr/servers/defaultServer/server.xml
          serverEnv:
          - /opt/ibm/wlp/usr/servers/defaultServer/server.env
          bootstrapProperties:
          - /opt/ibm/wlp/usr/servers/defaultServer/bootstrap.properties
          variableProperties:
          - /opt/ibm/wlp/usr/servers/defaultServer/variables/variable.properties
          jvmOptions:
          - /opt/ibm/wlp/usr/servers/defaultServer/jvm.options
        # Application resource files to be migrated into the target container.
        resources:
          locations:
          - /opt/ibm/wlp/usr/servers/defaultServer/resources/ports.xml
          libraries:
          - /opt/ibm/wlp/usr/servers/defaultServer/resources/postgresql.jar
          keystores:
          - /opt/ibm/wlp/output/defaultServer/resources/security/key.p12
          sharedResources:
            - /opt/ibm/wlp/usr/shared/resources/jdbc.jar
          additionalResources:
          - /opt/ibm/wlp/output/defaultServer/resources/mongodb.jar
        javaRuntime:
          se: SE8
          ee: EE7
          vendor: IBM Corporation
        targetJavaRuntime:
          se: SE8
          ee: EE7
          vendor: IBM Corporation
        targetApplicationServer:
          profile: Liberty
          version: 23.0.0.4
          edition: Base
        targetContainer:
          # The target container base image name.
          baseImage: ibmcom/websphere-liberty:full-java8-ibmjava-ubi
          # The application server installation path within the target container
          # base image.
          home: /opt/ibm/wlp
          # The application server default server name.
          server: defaultServer
          # The UID or name of the user configured within the target container
          # base image. Defaults to 1001 for Liberty profile.
          user: "1001"
          # The GID or name of the group configured within the target container
          # base image. Defaults to 0 for Liberty profile.
          group: "0"
          # Application ports to be exposed in Kubernetes artifacts.
          ports:
          - name: http-tcp-9080
            port: 9080
            protocol: TCP
          - name: https-tcp-9443
            port: 9443
            protocol: TCP
          # Specify whether discovered keystores are automatically converted to
          # Kubernetes secrets. Defaults to true.
          enableSecrets: true
    

### Exclude applications

To exclude applications from the migration, remove them from the `applications` list.
    
    
      applications:
      # Exclude app1.war:
      # - path: app1.war
      #  ...
      - path: app2.war
    

### Control application files

To control which application files are included or excluded from the migration, update the `configurations` and `resources` fields.
    
    
      applications:
      - path: app.war
        resources:
          keystores:
          # Exclude key1.p12:
          # - key1.p12
          # Include key2.p12:
          - key2.p12
          additionalResources:
          # Exclude resource1.xml:
          # - resource1.xml
          # Include resource2.xml:
          - resource2.xml
    

### Customize the target Java runtime

To customize the target Java runtime for the application, update the `targetJavaRuntime` field.
    
    
      applications:
      - path: app.war
        targetJavaRuntime:
          se: SE
          ee: EE
          vendor: VENDOR
    

Replace the following:

  * SE: the Java SE version. Format: [SE8|SE11|SE17].
  * EE: the Java EE or Jakarta EE version. Format: [EE7|EE8|EE9|EE10].
  * VENDOR: the Java vendor. Format: [IBM Corporation|Oracle Corporation].



### Customize the target application server

To customize the target application server for the application, update the `targetApplicationServer` field.
    
    
      applications:
      - path: app.war
        targetApplicationServer:
          profile: PROFILE
          version: VERSION
          edition: EDITION
    

Replace the following:

  * PROFILE: the WebSphere profile. Format: [Liberty|Traditional].
  * TARGET_VERSION: the WebSphere version.
  * TARGET_EDITION: the WebSphere edition. Format: [Base|Core|Open|ND].



### Customize the target container

To customize the target container to be used for the application, update the `targetContainer` field.
    
    
      applications:
      - path: app.war
        targetContainer:
          baseImage: BASE_IMAGE
          home: HOME
          server: SERVER
          user: USER
          group: GROUP
    

### Customize Kubernetes secrets

By default, files listed under the `keystores` field are migrated to Kubernetes secrets. To migrate these files as is, you can disable this feature.
    
    
      applications:
      - path: app.war
        resources:
          keystores:
          - key.p12
        targetContainer:
          # Do not migrate keystores to Kubernetes secrets:
          enableSecrets: false
    

### Customize Kubernetes ports

To control which ports are exposed by Kubernetes Pods and Services, update the `ports` field.
    
    
      applications:
      - path: app.war
        targetContainer:
          ports:
          # Exclude http-tcp-9080:
          # - name: http-tcp-9080
          #   port: 9080
          #   protocol: TCP
          # Include https-tcp-9443:
          - name: https-tcp-9443
            port: 9443
            protocol: TCP
    

## What's next

  * Learn how to [execute the migration](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/execute-the-migration-plan).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
