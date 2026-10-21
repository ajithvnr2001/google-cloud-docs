---
url: https://docs.cloud.google.com/migrate/kf/docs/2.10/how-to/managed-services/
title: Provision managed services \u00a0|\u00a0 Kf 2.10 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:50:27.667771+00:00
---

# Provision managed services  |  Kf 2.10  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.10/how-to/managed-services/

Version 2.10

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
  * [ 2.10 ](https://docs.cloud.google.com/migrate/kf/docs/2.10)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.10/getting-started)



Send feedback 

#  Provision managed services Stay organized with collections  Save and categorize content based on your preferences. 

## Find a service

Use the `kf marketplace` command to find a service you want to use in your App. Running the command without arguments will show all the service classes available. A **service class** represents a specific type of service e.g. a MySQL database or a Postfix SMTP relay.
    
    
    $ kf marketplace
    5 services can be used in Space "test", use the --service flag to list the plans for a service
    
    Broker      Name        Space      Status  Description
    minibroker  mariadb                Active  Helm Chart for mariadb
    minibroker  mongodb                Active  Helm Chart for mongodb
    minibroker  mysql                  Active  Helm Chart for mysql
    minibroker  postgresql             Active  Helm Chart for postgresql
    minibroker  redis                  Active  Helm Chart for redis
    

Service classes can have multiple plans available. A **service plan** generally corresponds to a version or pricing tier of the software. You can view the plans for a specific service by supplying the service name with the marketplace command:
    
    
    $ kf marketplace --service mysql
    Name    Free  Status  Description
    5-7-14  true  Active  Fast, reliable, scalable, and easy to use open-source relational database system.
    5-7-27  true  Active  Fast, reliable, scalable, and easy to use open-source relational database system.
    5-7-28  true  Active  Fast, reliable, scalable, and easy to use open-source relational database system.
    

## Provision a service

Once you have identified a service class and plan to provision, you can create an instance of the service using `kf create-service`:
    
    
    $ kf create-service mysql 5-7-28 my-db
    Creating service instance "my-db" in Space "test"
    Waiting for service instance to become ready...
    Success
    

Services are provisioned into a single Space. You can see the services in the current Space by running `kf services`:
    
    
    $ kf services
    Listing services in Space: "test"
    Name   ClassName  PlanName  Age   Ready  Reason
    my-db  mysql      5-7-28    111s  True   <nil>
    

You can delete a service using `kf delete-service`:
    
    
    $ kf delete-service my-db
    

## Bind a service

Once a service has been created, you can **bind** it to an App, which will inject credentials into the App so the service can be used. You can create the binding using `kf bind-service`:
    
    
    $ kf bind-service my-app my-db
    Creating service instance binding "binding-my-app-my-db" in Space "test"
    Waiting for service instance binding to become ready...
    Success
    

You can list all bindings in a Space using the `kf bindings` command:
    
    
    $ kf bindings
    Listing bindings in Space: "test"
    Name                  App     Service  Age  Ready
    binding-my-app-my-db  my-app  my-db    82s  True
    

Once a service is bound, restart the App using `kf restart` and the credentials will be in the [`VCAP_SERVICES`](https://docs.cloud.google.com/migrate/kf/docs/2.10/how-to/app-runtime#vcapservices) environment variable.

You can delete a service binding with the `kf unbind-service` command:
    
    
    $ kf unbind-service my-app my-db
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
