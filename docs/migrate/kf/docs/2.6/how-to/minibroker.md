---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/how-to/minibroker/
title: Install the Minibroker Service Broker \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:36:49.184788+00:00
---

# Install the Minibroker Service Broker  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/how-to/minibroker/

Version 2.6

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
  * [ 2.6 ](https://docs.cloud.google.com/migrate/kf/docs/2.6)



Send feedback 

#  Install the Minibroker Service Broker Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Minibroker is not an officially supported part of Kf.

The following steps will guide you through installing a service broker called [Minibroker](https://github.com/kubernetes-sigs/minibroker). Minibroker adapts Helm charts into brokered services. When a service is provisioned, the Helm chart is applied to the same namespace as the apps it will be bound to.

Minibroker provides the following services by default:

  * MariaDB
  * MongoDB
  * MySQL
  * PostgreSQL
  * Redis



## Before you begin

You will need a cluster with Kf installed and access to the Kf CLI.

Additionally, you will need the following software:

  * **`helm`** : Follow [these instructions](https://helm.sh/docs/intro/install/) to install the `helm` CLI.



## Install Minibroker

  1. Check that Helm is at least version 3 by running:
         
         helm version

The output should look similar to the following:
         
         version.BuildInfo{Version:"v3.0.0", GitCommit:"e29ce2a54e96cd02ccfce88bee4f58bb6e2a28b6", GitTreeState:"clean", GoVersion:"go1.13.4"}
         

  2. Add the Minibroker Helm chart repository:
         
         helm repo add minibroker "https://minibroker.blob.core.windows.net/charts"

Helm will report that the repository was added:
         
         "minibroker" has been added to your repositories
         

  3. Create a Kubernetes namespace for the broker:
         
         kubectl create namespace minibroker

  4. Install Minibroker into the Kubernetes cluster:
         
         helm install minibroker minibroker/minibroker \
           --namespace minibroker \
           --set "deployServiceCatalog=false"

  5. Register the broker with Kf:
         
         kf create-service-broker minibroker \
           "user" \
           "pass" \
           "http://minibroker-minibroker.minibroker.svc.cluster.local"

**Note:** It may take several minutes for the broker to be reachable.



## Confirm broker installation

Run `kf marketplace`. You should see output similar to:
    
    
    $ kf marketplace
    
    5 services can be used in Space "default", use the --service flag to list the plans for a service
    
    Broker      Name        Space      Status  Description
    minibroker  mariadb                Active  Helm Chart for mariadb
    minibroker  mongodb                Active  Helm Chart for mongodb
    minibroker  mysql                  Active  Helm Chart for mysql
    minibroker  postgresql             Active  Helm Chart for postgresql
    minibroker  redis                  Active  Helm Chart for redis
    

## Removal

Run the following to remove Minibroker:
    
    
    kf delete-service-broker minibroker
    helm uninstall minibroker --namespace minibroker
    kubectl delete namespace minibroker

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
