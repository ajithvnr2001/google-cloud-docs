---
url: https://docs.cloud.google.com/nodejs/docs/reference/game-servers/latest/
title: Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:54:46.812911+00:00
---

# Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/game-servers/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.2.2 (latest) ](https://docs.cloud.google.com/nodejs/docs/reference/game-servers/latest/)
  * [ 3.2.1 ](https://docs.cloud.google.com/nodejs/docs/reference/game-servers/3.2.1/)
  * [ 3.1.3 ](https://docs.cloud.google.com/nodejs/docs/reference/game-servers/3.1.3/)
  * [ 2.5.0 ](https://docs.cloud.google.com/nodejs/docs/reference/game-servers/2.5.0/)
  * [ 2.4.0 ](https://docs.cloud.google.com/nodejs/docs/reference/game-servers/2.4.0/)
  * [ 2.3.8 ](https://docs.cloud.google.com/nodejs/docs/reference/game-servers/2.3.8/)



# [Google Cloud Game Servers: Node.js Client](https://github.com/googleapis/google-cloud-node)

[![release level](https://img.shields.io/badge/release%20level-stable-brightgreen.svg?style=flat)](https://cloud.google.com/terms/launch-stages) [![npm version](https://img.shields.io/npm/v/@google-cloud/game-servers.svg)](https://www.npmjs.org/package/@google-cloud/game-servers)

Game service client for Node.js

A comprehensive list of changes in each version may be found in [the CHANGELOG](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-gaming/CHANGELOG.md).

  * [Google Cloud Game Servers Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/game-servers/latest)
  * [Google Cloud Game Servers Documentation](https://cloud.google.com/game-servers/)
  * [github.com/googleapis/google-cloud-node/packages/google-cloud-gaming](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-gaming)



Read more about the client libraries for Cloud APIs, including the older Google APIs Client Libraries, in [Client Libraries Explained](https://cloud.google.com/apis/docs/client-libraries-explained).

**Table of contents:**

  * Quickstart
    * Before you begin
    * Installing the client library
    * Using the client library
  * Samples
  * Versioning
  * Contributing
  * License



## Quickstart

### Before you begin

  1. [Select or create a Cloud Platform project](https://console.cloud.google.com/project).
  2. [Enable billing for your project](https://support.google.com/cloud/answer/6293499#enable-billing).
  3. [Enable the Google Cloud Game Servers API](https://console.cloud.google.com/flows/enableapi?apiid=gameservices.googleapis.com).
  4. [Set up authentication with a service account](https://cloud.google.com/docs/authentication/getting-started) so you can access the API from your local workstation.



### Installing the client library
    
    
    npm install @google-cloud/game-servers
    

### Using the client library
    
    
    const {RealmsServiceClient} = require('[@google-cloud/game-servers](https://docs.cloud.google.com/nodejs/docs/reference/game-servers/latest/overview.html)');
    
    async function quickstart() {
      const client = new [RealmsServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/game-servers/latest/overview.html)();
    
      // TODO(developer): uncomment the following section, and add values
      // const projectId = 'YOUR_PROJECT_ID';
      // const location = 'us-central1;
      // const realmId = 'DESIRED_REALM_ID';
    
      const request = {
        parent: `projects/${projectId}/locations/${location}`,
        realmId,
        realm: {
          // Must use a valid support time zone.
          // See https://cloud.google.com/dataprep/docs/html/Supported-Time-Zone-Values_66194188
          timeZone: 'US/Pacific',
          description: 'My Game Server realm',
        },
      };
    
      const [operation] = await client.createRealm(request);
      const results = await operation.promise();
      const [realm] = results;
    
      console.log('Realm created:');
    
      console.log(`\tRealm name: ${realm.name}`);
      console.log(`\tRealm description: ${realm.description}`);
      console.log(`\tRealm time zone: ${realm.timeZone}`);
    }
    quickstart();
    

## Samples

Samples are in the [`samples/`](https://github.com/googleapis/google-cloud-node/tree/main/samples) directory. Each sample's `README.md` has instructions for running its sample.

Sample | Source Code | Try it  
---|---|---  
Game_server_clusters_service.create_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.create_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.create_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.delete_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.delete_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.delete_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.get_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.get_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.get_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.list_game_server_clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.list_game_server_clusters.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.list_game_server_clusters.js,samples/README.md)  
Game_server_clusters_service.preview_create_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.preview_create_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.preview_create_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.preview_delete_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.preview_delete_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.preview_delete_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.preview_update_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.preview_update_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.preview_update_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.update_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.update_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_clusters_service.update_game_server_cluster.js,samples/README.md)  
Game_server_configs_service.create_game_server_config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_configs_service.create_game_server_config.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_configs_service.create_game_server_config.js,samples/README.md)  
Game_server_configs_service.delete_game_server_config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_configs_service.delete_game_server_config.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_configs_service.delete_game_server_config.js,samples/README.md)  
Game_server_configs_service.get_game_server_config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_configs_service.get_game_server_config.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_configs_service.get_game_server_config.js,samples/README.md)  
Game_server_configs_service.list_game_server_configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_configs_service.list_game_server_configs.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_configs_service.list_game_server_configs.js,samples/README.md)  
Game_server_deployments_service.create_game_server_deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.create_game_server_deployment.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.create_game_server_deployment.js,samples/README.md)  
Game_server_deployments_service.delete_game_server_deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.delete_game_server_deployment.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.delete_game_server_deployment.js,samples/README.md)  
Game_server_deployments_service.fetch_deployment_state | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.fetch_deployment_state.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.fetch_deployment_state.js,samples/README.md)  
Game_server_deployments_service.get_game_server_deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.get_game_server_deployment.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.get_game_server_deployment.js,samples/README.md)  
Game_server_deployments_service.get_game_server_deployment_rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.get_game_server_deployment_rollout.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.get_game_server_deployment_rollout.js,samples/README.md)  
Game_server_deployments_service.list_game_server_deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.list_game_server_deployments.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.list_game_server_deployments.js,samples/README.md)  
Game_server_deployments_service.preview_game_server_deployment_rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.preview_game_server_deployment_rollout.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.preview_game_server_deployment_rollout.js,samples/README.md)  
Game_server_deployments_service.update_game_server_deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.update_game_server_deployment.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.update_game_server_deployment.js,samples/README.md)  
Game_server_deployments_service.update_game_server_deployment_rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.update_game_server_deployment_rollout.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/game_server_deployments_service.update_game_server_deployment_rollout.js,samples/README.md)  
Realms_service.create_realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/realms_service.create_realm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/realms_service.create_realm.js,samples/README.md)  
Realms_service.delete_realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/realms_service.delete_realm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/realms_service.delete_realm.js,samples/README.md)  
Realms_service.get_realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/realms_service.get_realm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/realms_service.get_realm.js,samples/README.md)  
Realms_service.list_realms | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/realms_service.list_realms.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/realms_service.list_realms.js,samples/README.md)  
Realms_service.preview_realm_update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/realms_service.preview_realm_update.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/realms_service.preview_realm_update.js,samples/README.md)  
Realms_service.update_realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1/realms_service.update_realm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1/realms_service.update_realm.js,samples/README.md)  
Game_server_clusters_service.create_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.create_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.create_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.delete_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.delete_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.delete_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.get_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.get_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.get_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.list_game_server_clusters | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.list_game_server_clusters.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.list_game_server_clusters.js,samples/README.md)  
Game_server_clusters_service.preview_create_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.preview_create_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.preview_create_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.preview_delete_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.preview_delete_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.preview_delete_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.preview_update_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.preview_update_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.preview_update_game_server_cluster.js,samples/README.md)  
Game_server_clusters_service.update_game_server_cluster | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.update_game_server_cluster.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_clusters_service.update_game_server_cluster.js,samples/README.md)  
Game_server_configs_service.create_game_server_config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_configs_service.create_game_server_config.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_configs_service.create_game_server_config.js,samples/README.md)  
Game_server_configs_service.delete_game_server_config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_configs_service.delete_game_server_config.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_configs_service.delete_game_server_config.js,samples/README.md)  
Game_server_configs_service.get_game_server_config | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_configs_service.get_game_server_config.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_configs_service.get_game_server_config.js,samples/README.md)  
Game_server_configs_service.list_game_server_configs | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_configs_service.list_game_server_configs.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_configs_service.list_game_server_configs.js,samples/README.md)  
Game_server_deployments_service.create_game_server_deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.create_game_server_deployment.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.create_game_server_deployment.js,samples/README.md)  
Game_server_deployments_service.delete_game_server_deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.delete_game_server_deployment.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.delete_game_server_deployment.js,samples/README.md)  
Game_server_deployments_service.fetch_deployment_state | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.fetch_deployment_state.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.fetch_deployment_state.js,samples/README.md)  
Game_server_deployments_service.get_game_server_deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.get_game_server_deployment.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.get_game_server_deployment.js,samples/README.md)  
Game_server_deployments_service.get_game_server_deployment_rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.get_game_server_deployment_rollout.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.get_game_server_deployment_rollout.js,samples/README.md)  
Game_server_deployments_service.list_game_server_deployments | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.list_game_server_deployments.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.list_game_server_deployments.js,samples/README.md)  
Game_server_deployments_service.preview_game_server_deployment_rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.preview_game_server_deployment_rollout.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.preview_game_server_deployment_rollout.js,samples/README.md)  
Game_server_deployments_service.update_game_server_deployment | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.update_game_server_deployment.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.update_game_server_deployment.js,samples/README.md)  
Game_server_deployments_service.update_game_server_deployment_rollout | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.update_game_server_deployment_rollout.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/game_server_deployments_service.update_game_server_deployment_rollout.js,samples/README.md)  
Realms_service.create_realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/realms_service.create_realm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/realms_service.create_realm.js,samples/README.md)  
Realms_service.delete_realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/realms_service.delete_realm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/realms_service.delete_realm.js,samples/README.md)  
Realms_service.get_realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/realms_service.get_realm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/realms_service.get_realm.js,samples/README.md)  
Realms_service.list_realms | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/realms_service.list_realms.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/realms_service.list_realms.js,samples/README.md)  
Realms_service.preview_realm_update | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/realms_service.preview_realm_update.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/realms_service.preview_realm_update.js,samples/README.md)  
Realms_service.update_realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/generated/v1beta/realms_service.update_realm.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/generated/v1beta/realms_service.update_realm.js,samples/README.md)  
Create Game Server Realm | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/quickstart.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/quickstart.js,samples/README.md)  
Quickstart.test | [source code](https://github.com/googleapis/google-cloud-node/blob/main/packages/google-cloud-gaming/samples/test/quickstart.test.js) | [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.png)](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/googleapis/google-cloud-node&page=editor&open_in_editor=packages/google-cloud-gaming/samples/test/quickstart.test.js,samples/README.md)  
  
The [Google Cloud Game Servers Node.js Client API Reference](https://cloud.google.com/nodejs/docs/reference/game-servers/latest) documentation also contains samples.

## Supported Node.js Versions

Our client libraries follow the [Node.js release schedule](https://nodejs.org/en/about/releases/). Libraries are compatible with all current _active_ and _maintenance_ versions of Node.js. If you are using an end-of-life version of Node.js, we recommend that you update as soon as possible to an actively supported LTS version.

Google's client libraries support legacy versions of Node.js runtimes on a best-efforts basis with the following warnings:

  * Legacy versions are not tested in continuous integration.
  * Some security patches and features cannot be backported.
  * Dependencies cannot be kept up-to-date.



Client libraries targeting some end-of-life versions of Node.js are available, and can be installed through npm [dist-tags](https://docs.npmjs.com/cli/dist-tag). The dist-tags follow the naming convention `legacy-(version)`. For example, `npm install @google-cloud/game-servers@legacy-8` installs client libraries for versions compatible with Node.js 8.

## Versioning

This library follows [Semantic Versioning](http://semver.org/).

This library is considered to be **stable**. The code surface will not change in backwards-incompatible ways unless absolutely necessary (e.g. because of critical security issues) or with an extensive deprecation period. Issues and requests against **stable** libraries are addressed with the highest priority.

More Information: [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages)

## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/googleapis/google-cloud-node/blob/main/CONTRIBUTING.md).

Please note that this `README.md`, the `samples/README.md`, and a variety of configuration files in this repository (including `.nycrc` and `tsconfig.json`) are generated from a central template. To edit one of these files, make an edit to its templates in [directory](https://github.com/googleapis/synthtool).

## License

Apache Version 2.0

See [LICENSE](https://github.com/googleapis/google-cloud-node/blob/main/LICENSE)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
