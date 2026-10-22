---
url: https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters/
title: View clusters \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:00.926521+00:00
---

# View clusters  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  View clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view a list of clusters in your project, or the details of a single cluster.

After you create one or more clusters in Cluster Director, you can view the clusters to review their configuration details, status, and the Compute Engine instances that make up those clusters. Viewing clusters helps you optimize the workloads that run in your clusters and plan for future capacity needs.

To learn more about the states that nodes enter during their lifecycle, see [Node lifecycle](https://docs.cloud.google.com/cluster-director/docs/manage/node-lifecycle).

## Limitations

You can only view the state of a cluster or node by using the Google Cloud console.

## Before you begin

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

### Required roles

To get the permissions that you need to view clusters, ask your administrator to grant you the [Cluster Director Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.viewer) (`roles/hypercomputecluster.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view clusters. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view clusters:

  * To view a list of clusters: `hypercomputecluster.clusters.list`
  * To view the details of a single cluster: `hypercomputecluster.clusters.describe`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View clusters

To view the clusters in your project, use one of the following methods:

  * View a list of clusters

  * View the details of a single cluster




### View a list of clusters

To view a list of clusters across multiple regions, use the Google Cloud console. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director/overview)

  2. In the navigation menu, click **Clusters**. The **Clusters** page appears. The table lists each cluster, and each table column describes a property.

  3. Optional: To refine your list of clusters, in the filter_list **Filter** field, select the properties that you want to filter the clusters by.




###  gcloud 

To view a list of clusters, use the [`gcloud alpha cluster-director clusters list` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/list).

To run the command, select one of the following options:

###  Bash 
    
    
    gcloud alpha cluster-director clusters list \
        --location=REGION
    

###  Powershell 
    
    
    gcloud alpha cluster-director clusters list `
        --location=REGION
    

###  cmd.exe 
    
    
    gcloud alpha cluster-director clusters list ^
        --location=REGION
    

Replace `REGION` with the region where one or more of your clusters exist.

The output is similar to the following:
    
    
    ---
    compute:
      resourceRequests:
      - disks:
        - boot: true
          sizeGb: '100'
          type: pd-balanced
        id: cluster000-rr1
        machineType: n2-standard-2
        provisioningModel: PROVISIONING_MODEL_STANDARD
        zone: us-central1-a
    computeResources:
      cluster000-rr1:
        config:
          newOnDemandInstances:
            bootDisk:
              boot: true
              sizeGb: '100'
              type: pd-balanced
            machineType: n2-standard-2
            zone: us-central1-a
    createTime: '2025-10-08T12:53:48.764581437Z'
    description: An optional description for your cluster
    name: projects/example-project/locations/us-central1/clusters/cluster000
    networkResources:
      net-cluster000-net:
        config:
          newNetwork:
            network: projects/example-project/global/networks/cluster000-net
    networks:
    - initializeParams:
        network: projects/example-project/global/networks/cluster000-net
      network: projects/example-project/global/networks/cluster000-net
      subnetwork: projects/example-project/global/networks/cluster000-net
    orchestrator:
      slurm:
        defaultPartition: part1
        loginNodes:
          bootDisk:
            sizeGb: '100'
            type: pd-balanced
          count: '2'
          disks:
          - boot: true
            sizeGb: '100'
            type: pd-balanced
          enableOsLogin: true
          enablePublicIps: true
          instances:
          - instance: projects/example-project/zones/us-central1-a/instances/cluster000-login-001
          machineType: n2-standard-2
          storageConfigs:
          - id: filestore-id-1
            localMount: /home
          zone: us-central1-a
        nodeSets:
        - bootDisk:
            boot: true
            sizeGb: '100'
            type: pd-balanced
          computeId: cluster000-rr1
          computeInstance:
            bootDisk:
              sizeGb: '100'
              type: pd-balanced
          id: nodeset1
          resourceRequestId: cluster000-rr1
          staticNodeCount: '4'
          storageConfigs:
          - id: filestore-id-1
            localMount: /home
        partitions:
        - id: part1
          nodeSetIds:
          - nodeset1
    reconciling: false
    storageResources:
      filestore-id-1:
        config:
          newFilestore:
            fileShares:
            - capacityGb: '5120'
              fileShare: nfsshare
            filestore: projects/example-project/locations/us-central1-a/instances/cluster000
            protocol: NFSV3
            tier: ZONAL
    storages:
    - id: filestore-id-1
      initializeParams:
        filestore:
          fileShares:
          - capacityGb: '5120'
            fileShare: nfsshare
          filestore: projects/example-project/locations/us-central1-a/instances/cluster000
          protocol: PROTOCOL_NFSV3
          tier: TIER_ZONAL
      storage: projects/example-project/locations/us-central1-a/instances/cluster000
    updateTime: '2025-10-08T21:14:18.952183479Z'
    ---
    ...
    

If you want to refine your list of clusters, then use the same command with the [`--filter` flag](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/list#--filter).

###  REST 

To view a list of clusters in your project, make a `GET` request to the [`clusters.list` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/list).

Your request must include the following HTTP method and request URL:
    
    
    GET https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `REGION`: the region where your clusters exist.




To send your request, select one of the following options:

###  curl (Bash) 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters"
    

###  Powershell 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method GET `
        -Headers $headers `
        -Uri "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters" | Select-Object -Expand Content
    

###  curl (cmd.exe) 
    
    
    curl -X GET ^
         -H "Authorization: Bearer $(gcloud auth print-access-token)" ^
         "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters"
    

The response is similar to the following:
    
    
    [
      {
        "computeResources": {
          "cluster000-rr1": {
            "config": {
              "newOnDemandInstances": {
                "bootDisk": {
                  "sizeGb": "100",
                  "type": "pd-balanced"
                },
                "machineType": "n2-standard-2",
                "zone": "us-central1-a"
              }
            }
          }
        },
        "createTime": "2025-10-08T12:53:48.764581437Z",
        "description": "An optional description for your cluster",
        "name": "projects/example-project/locations/us-central1/clusters/cluster000",
        "networkResources": {
          "net-cluster000-net": {
            "config": {
              "newNetwork": {
                "network": "projects/example-project/global/networks/cluster000-net"
              }
            }
          }
        },
        "orchestrator": {
          "slurm": {
            "defaultPartition": "part1",
            "loginNodes": {
              "bootDisk": {
                "sizeGb": "100",
                "type": "pd-balanced"
              },
              "count": "2",
              "enableOsLogin": true,
              "enablePublicIps": true,
              "instances": [
                {
                  "instance": "projects/example-project/zones/us-central1-a/instances/cluster000-login-001"
                }
              ],
              "machineType": "n2-standard-2",
              "storageConfigs": [
                {
                  "id": "filestore-id-1",
                  "localMount": "/home"
                }
              ],
              "zone": "us-central1-a"
            },
            "nodeSets": [
              {
                "computeId": "cluster000-rr1",
                "computeInstance": {
                  "bootDisk": {
                    "sizeGb": "100",
                    "type": "pd-balanced"
                  }
                },
                "id": "nodeset1",
                "staticNodeCount": "4",
                "storageConfigs": [
                  {
                    "id": "filestore-id-1",
                    "localMount": "/home"
                  }
                ]
              }
            ],
            "partitions": [
              {
                "id": "part1",
                "nodeSetIds": [
                  "nodeset1"
                ]
              }
            ]
          }
        },
        "reconciling": false,
        "storageResources": {
          "filestore-id-1": {
            "config": {
              "newFilestore": {
                "fileShares": [
                  {
                    "capacityGb": "5120",
                    "fileShare": "nfsshare"
                  }
                ],
                "filestore": "projects/example-project/locations/us-central1-a/instances/cluster000fs1",
                "protocol": "NFSV3",
                "tier": "ZONAL"
              }
            }
          }
        },
        "updateTime": "2025-10-08T21:14:18.952183479Z"
      },
      ...
    ]
    

If you want to refine your list of reservations, then make the same request and, in the request URL, include the [`filter` query parameter](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/list#body.QUERY_PARAMETERS.filter).

### View the details of a cluster

For the most detailed view of your cluster, including the cluster or node states, Cloud Monitoring dashboards, and a topology view, use the Google Cloud console. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director)

  2. In the navigation menu, click **Clusters**. The **Clusters** page appears.

  3. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to view the details of. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  4. Based on the tab that you click, you can view the following details of the cluster:

     * **Details** : the attributes of the cluster, such as its name, region, state, as well as the configured compute, network, and storage resources.

     * **Nodes** : the name, state, and properties of the login nodes and compute node in your cluster.

     * **Observability** : a set of prebuilt Monitoring dashboards that show resource vCPU, memory, and GPU usage across your cluster. For more information, see [Monitor cluster performance with prebuilt dashboards](https://docs.cloud.google.com/cluster-director/docs/monitor/dashboards).

     * **Topology** : a view of the topology of the compute instances in your cluster, including health data, CPU usage, and maintenance information. For more information, see [View cluster topology](https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology).




###  gcloud 

To view the details of a single cluster, use the [`gcloud alpha cluster-director clusters describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/describe).

To run the command, select one of the following options:

###  Bash 
    
    
    gcloud alpha cluster-director clusters describe CLUSTER_NAME \
        --location=REGION
    

###  Powershell 
    
    
    gcloud alpha cluster-director clusters describe CLUSTER_NAME `
        --location=REGION
    

###  cmd.exe 
    
    
    gcloud alpha cluster-director clusters describe CLUSTER_NAME ^
        --location=REGION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.

  * `REGION`: the region where your cluster exists.




The output is similar to the following:
    
    
    compute:
      resourceRequests:
      - disks:
        - boot: true
          sizeGb: '100'
          type: pd-balanced
        id: cluster000-rr1
        machineType: n2-standard-2
        provisioningModel: PROVISIONING_MODEL_STANDARD
        zone: us-central1-a
    computeResources:
      cluster000-rr1:
        config:
          newOnDemandInstances:
            bootDisk:
              boot: true
              sizeGb: '100'
              type: pd-balanced
            machineType: n2-standard-2
            zone: us-central1-a
    createTime: '2025-10-08T12:53:48.764581437Z'
    description: An optional description for your cluster
    name: projects/example-project/locations/us-central1/clusters/cluster000
    networkResources:
      net-cluster000-net:
        config:
          newNetwork:
            network: projects/example-project/global/networks/cluster000-net
    networks:
    - initializeParams:
        network: projects/example-project/global/networks/cluster000-net
      network: projects/example-project/global/networks/cluster000-net
      subnetwork: projects/example-project/global/networks/cluster000-net
    orchestrator:
      slurm:
        defaultPartition: part1
        loginNodes:
          bootDisk:
            sizeGb: '100'
            type: pd-balanced
          count: '2'
          disks:
          - boot: true
            sizeGb: '100'
            type: pd-balanced
          enableOsLogin: true
          enablePublicIps: true
          instances:
          - instance: projects/example-project/zones/us-central1-a/instances/cluster000-login-001
          machineType: n2-standard-2
          storageConfigs:
          - id: filestore-id-1
            localMount: /home
          zone: us-central1-a
        nodeSets:
        - bootDisk:
            boot: true
            sizeGb: '100'
            type: pd-balanced
          computeId: cluster000-rr1
          computeInstance:
            bootDisk:
              sizeGb: '100'
              type: pd-balanced
          id: nodeset1
          resourceRequestId: cluster000-rr1
          staticNodeCount: '4'
          storageConfigs:
          - id: filestore-id-1
            localMount: /home
        partitions:
        - id: part1
          nodeSetIds:
          - nodeset1
    reconciling: false
    storageResources:
      filestore-id-1:
        config:
          newFilestore:
            fileShares:
            - capacityGb: '5120'
              fileShare: nfsshare
            filestore: projects/example-project/locations/us-central1-a/instances/cluster000
            protocol: NFSV3
            tier: ZONAL
    storages:
    - id: filestore-id-1
      initializeParams:
        filestore:
          fileShares:
          - capacityGb: '5120'
            fileShare: nfsshare
          filestore: projects/example-project/locations/us-central1-a/instances/cluster000
          protocol: PROTOCOL_NFSV3
          tier: TIER_ZONAL
      storage: projects/example-project/locations/us-central1-a/instances/cluster000
    updateTime: '2025-10-08T21:14:18.952183479Z'
    

###  REST 

To view the details of a single cluster, make a `GET` request to the [`clusters.get` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/get).

Your request must include the following HTTP method and request URL:
    
    
    GET https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `REGION`: the region where your cluster exists.

  * `CLUSTER_NAME`: the name of the cluster that you want to view.




To send your request, select one of the following options:

###  curl (Bash) 
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME"
    

###  Powershell 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method GET `
        -Headers $headers `
        -Uri "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME" | Select-Object -Expand Content
    

###  curl (cmd.exe) 
    
    
    curl -X GET ^
         -H "Authorization: Bearer $(gcloud auth print-access-token)" ^
            "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME"
    

The response is similar to the following:
    
    
    {
      "computeResources": {
        "cluster000-rr1": {
          "config": {
            "newOnDemandInstances": {
              "bootDisk": {
                "sizeGb": "100",
                "type": "pd-balanced"
              },
              "machineType": "n2-standard-2",
              "zone": "us-central1-a"
            }
          }
        }
      },
      "createTime": "2025-10-08T12:53:48.764581437Z",
      "description": "An optional description for your cluster",
      "name": "projects/example-project/locations/us-central1/clusters/cluster000",
      "networkResources": {
        "net-cluster000-net": {
          "config": {
            "newNetwork": {
              "network": "projects/example-project/global/networks/cluster000-net"
            }
          }
        }
      },
      "orchestrator": {
        "slurm": {
          "defaultPartition": "part1",
          "loginNodes": {
            "bootDisk": {
              "sizeGb": "100",
              "type": "pd-balanced"
            },
            "count": "2",
            "enableOsLogin": true,
            "enablePublicIps": true,
            "instances": [
              {
                "instance": "projects/example-project/zones/us-central1-a/instances/cluster000-login-001"
              }
            ],
            "machineType": "n2-standard-2",
            "storageConfigs": [
              {
                "id": "filestore-id-1",
                "localMount": "/home"
              }
            ],
            "zone": "us-central1-a"
          },
          "nodeSets": [
            {
              "computeId": "cluster000-rr1",
              "computeInstance": {
                "bootDisk": {
                  "sizeGb": "100",
                  "type": "pd-balanced"
                }
              },
              "id": "nodeset1",
              "staticNodeCount": "4",
              "storageConfigs": [
                {
                  "id": "filestore-id-1",
                  "localMount": "/home"
                }
              ]
            }
          ],
          "partitions": [
            {
              "id": "part1",
              "nodeSetIds": [
                "nodeset1"
              ]
            }
          ]
        }
      },
      "reconciling": false,
      "storageResources": {
        "filestore-id-1": {
          "config": {
            "newFilestore": {
              "fileShares": [
                {
                  "capacityGb": "5120",
                  "fileShare": "nfsshare"
                }
              ],
              "filestore": "projects/example-project/locations/us-central1-a/instances/cluster000fs1",
              "protocol": "NFSV3",
              "tier": "ZONAL"
            }
          }
        }
      },
      "updateTime": "2025-10-08T21:14:18.952183479Z"
    }
    

## What's next

  * [Connect to a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster)

  * [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)

  * [Delete a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/delete-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
