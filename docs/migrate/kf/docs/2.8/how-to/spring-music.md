---
url: https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/spring-music/
title: Deploy Spring Music \u00a0|\u00a0 Kf 2.8 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:42.774869+00:00
---

# Deploy Spring Music  |  Kf 2.8  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/spring-music/

Version 2.8

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
  * [ 2.8 ](https://docs.cloud.google.com/migrate/kf/docs/2.8)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.8/getting-started)



Send feedback 

#  Deploy Spring Music Stay organized with collections  Save and categorize content based on your preferences. 

These instructions will walk you through deploying the [Cloud Foundry Spring Music](https://github.com/cloudfoundry-samples/spring-music) reference App using the Kf Cloud Service Broker for Google Cloud.

  1. **Building Java Apps from source** : The Spring Music source will be built on the cluster, not locally.

  2. **Service broker integration** : You will create a database using the Kf Cloud Service Broker and bind the Spring Music App to it.

  3. **Spring Cloud Connectors** : [Spring Cloud Connectors](https://cloud.spring.io/spring-cloud-connectors/) are used by the Spring Music App to detect things like bound CF services. They work seamlessly with Kf.

  4. **Configuring the Java version** : You will specify the version of Java you want the buildpack to use.




## Prerequisites

[Install and configure Kf Cloud Service Broker](https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/deploying-cloud-sb).

## Deploy Spring Music

### Clone source

  1. Clone the [Spring Music repo](https://github.com/cloudfoundry-samples/spring-music).
         
         git clone https://github.com/cloudfoundry-samples/spring-music.git spring-music
         cd spring-music

  2. Edit `manifest.yml`, and replace `path: build/libs/spring-music-1.0.jar` with `stack: org.cloudfoundry.stacks.cflinuxfs3`. This instructs Kf to build from source using [cloud native buildpacks](https://cloud.google.com/blog/products/containers-kubernetes/google-cloud-now-supports-buildpacks) so you don't have to compile locally.
         
         ---
         applications:
         - name: spring-music
           memory: 1G
           random-route: true
           stack: org.cloudfoundry.stacks.cflinuxfs3
           env:
             JBP_CONFIG_SPRING_AUTO_RECONFIGURATION: '{enabled: false}'
         #    JBP_CONFIG_OPEN_JDK_JRE: '{ jre: { version: 11.+ } }'




### Push Spring Music with no bindings

  1. Create and target a Space.
         
         kf create-space test
         kf target -s test

  2. Deploy Spring Music.
         
         kf push spring-music

  3. Use the proxy feature to access the deployed App.

     1. Start the proxy:
            
            kf proxy spring-music

     2. Open `http://localhost:8080` in your browser:

![](https://docs.cloud.google.com/migrate/kf/docs/2.8/images/sm1.png)

The deployed App includes a UI element showing which (if any) Spring profile is being used. No profile is being used here, indicating an in-memory database is in use.




### Create and bind a database

  1. Create a PostgresSQL database from the marketplace.

**Note:** You must set the `COMPUTE_REGION` and `VPC_NAME` variables so Kf Cloud Service Broker knows where to provision your instance, and authorize the VPC Kf Apps run on to access it.
         
         kf create-service csb-google-postgres small spring-music-postgres-db -c '{"region":"COMPUTE_REGION","authorized_network":"VPC_NAME"}'

  2. Bind the Service with the App.
         
         kf bind-service spring-music spring-music-postgres-db

  3. Restart the App to make the service binding available via the VCAP_SERVICES environment variable.
         
         kf restart spring-music

  4. (Optional) View the binding details.
         
         kf bindings

  5. Verify the App is using the new binding.

     1. Start the proxy:
            
            kf proxy spring-music

     2. Open `http://localhost:8080` in your browser:

![](https://docs.cloud.google.com/migrate/kf/docs/2.8/images/sm2.png)

You now see the Postgres profile is being used, and we see the name of our Service we bound the App to.




## Clean up

  1. Unbind and delete the PostgreSQL service:
         
         kf unbind-service spring-music spring-music-db
         kf delete-service spring-music-db

  2. Delete the App:
         
         kf delete spring-music




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
