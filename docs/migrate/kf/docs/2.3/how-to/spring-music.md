---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/spring-music/
title: Deploy Spring Music \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:28.880417+00:00
---

# Deploy Spring Music  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/spring-music/

Version 2.3

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.3/getting-started)



Send feedback 

#  Deploy Spring Music Stay organized with collections  Save and categorize content based on your preferences. 

These instructions will walk you through deploying the [Cloud Foundry Spring Music](https://github.com/cloudfoundry-samples/spring-music) reference App with Kf, demonstrating a few things along the way:

  1. **Building Java Apps from source** : The Spring Music source will be built on the cluster, not locally.

  2. **Service broker integration** : You will create and bind a PostgreSQL database to the Spring Music App.

  3. **Spring Cloud Connectors** : [Spring Cloud Connectors](https://cloud.spring.io/spring-cloud-connectors/) are used by the Spring Music App to detect things like bound CF services. They work seamlessly with Kf.

  4. **Configuring the Java version** : You will specify the version of Java you want the buildpack to use.




## Prerequisites

### Option 1: Minibroker

The cluster administrator should follow [these instructions](https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/minibroker) to install the Minibroker service broker into your cluster. Minibroker will allow you to provision a PostgreSQL database and configure your App to use it.

To confirm that Minibroker is installed and available to your cluster, run `kf marketplace` and you should see output similar to:
    
    
    $ kf marketplace
    5 services can be used in Space "demo", use the --service flag to list the plans for a service
    
    Broker      Name        Space      Status  Description
    minibroker  mariadb                Active  Helm Chart for mariadb
    minibroker  mongodb                Active  Helm Chart for mongodb
    minibroker  mysql                  Active  Helm Chart for mysql
    minibroker  postgresql             Active  Helm Chart for postgresql
    minibroker  redis                  Active  Helm Chart for redis
    

### Option 2: Other Service Broker

You can use a different service broker that's installed as long as it supports creating PostgreSQL services. For example, the [gcp-service-broker](https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/spring-music/).

## Deploy

### Clone source

  1. Clone the [Spring Music repo](https://github.com/cloudfoundry-samples/spring-music).
         
         git clone https://github.com/cloudfoundry-samples/spring-music.git spring-music
         cd spring-music

  2. Edit `manifest.yml`, and replace the contents with the following:
         
         ---
         applications:
         - name: spring-music
           memory: 1G
           random-route: true
           stack: org.cloudfoundry.stacks.cflinuxfs3
           env:
             BP_AUTO_RECONFIGURATION_ENABLED: false
         




### Push App

  1. Deploy (this assumes you've already `kf target`ed a Space; see [these docs](https://docs.cloud.google.com/migrate/kf/docs/2.3/quickstart#prepare_space) for more detail):
         
         kf push spring-music
         

  2. Use the proxy feature to access the deployed App, then load `http://localhost:8080` in your browser:
         
         kf proxy spring-music
         

![](https://docs.cloud.google.com/migrate/kf/docs/2.3/images/sm1.png)

> The deployed App includes a UI element showing which (if any) Spring profile is being used. No profile is being used here, indicating an in-memory database is in use.




### Create and bind database

  1. Create a PostgreSQL service via the broker installed in the marketplace:
         
         kf create-service postgresql 11-7-0 spring-music-db -c '{"postgresqlDatabase":"smdb", "postgresDatabase":"smdb"}'
         

  2. Bind the service instance to the Spring Music App:
         
         kf bind-service spring-music spring-music-db -c '{"postgresqlDatabase":"smdb", "postgresDatabase":"smdb"}'
         

  3. Restart the App to make the service binding available via the `VCAP_SERVICES` environment variable:
         
         kf restart spring-music
         

  4. (Optional) View the binding details:
         
         kf bindings
         

  5. `kf proxy` to the App again and view it in your web browser. The Spring profile should be shown, indicating the PostgreSQL service you created and bound is being used:

![](https://docs.cloud.google.com/migrate/kf/docs/2.3/images/sm2.png)




## Destroy

  1. Unbind and delete the PostgreSQL service:
         
         kf unbind-service spring-music spring-music-db
         kf delete-service spring-music-db
         

  2. Delete the App:
         
         kf delete spring-music
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
