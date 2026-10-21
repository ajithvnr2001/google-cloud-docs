---
url: https://docs.cloud.google.com/compute/docs/labeling-resources/
title: Organize resources using labels \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:42.438091+00:00
---

# Organize resources using labels  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/labeling-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Organize resources using labels Stay organized with collections  Save and categorize content based on your preferences. 

Labels are key-value pairs that can be used on Google Cloud to group related or associated resources. For example, on Compute Engine, you can use labels to group VMs in categories such as production, staging, or development so that you can search for resources that belong to each development stage.

After adding labels to your resources, you can take advantage of the nested filtering feature to perform more precise searches for your resources using labels.

## Before you begin

  * Read the [persistent disks](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) documentation.
  * Read the [images](https://docs.cloud.google.com/compute/docs/images) documentation.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## What are labels?

A label is a key-value pair that you can assign to Google Cloud instances. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

## Requirements for labels

The labels applied to a resource must meet the following requirements:

  * Each resource can have up to 64 labels.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters, and cannot be empty. Values can be empty, and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. Keys must start with a lowercase letter or international character.
  * The key portion of a label must be unique within a single resource. However, you can use the same key with multiple resources.



These limits apply to the key and value for each label, and to the individual Google Cloud resources that have labels. There is no limit on how many labels you can apply across all resources within a project.

## Common uses of labels

Here are some common use cases for labels:

  * **Team or cost center labels** : Add labels based on team or cost center to distinguish instances owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage labels** : For example, `environment:production` and `environment:test`.

  * **State labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




  * **Virtual machine labels** : A label can be attached to a virtual machine. Virtual machine tags that you defined in the past appear as a label without a value.

**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Use labels on Compute Engine

You can apply labels to the following Compute Engine resources:

  * Virtual machine (VM) instances
  * Images
  * Persistent disks
  * Persistent disk snapshots



You can also use labels on related Google Cloud components such as the following:

  * [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/using-bucket-labels)
  * Networking resources: 
    * Forwarding rules used with internal Application Load Balancers (other load balancer forwarding rules aren't supported)
    * VPN tunnels
    * Static external IP addresses



For example, you can add the following labels as key-value pairs to your resources:
    
    
    {
     "labels": {
        "vmrole": "webserver",
        "environment": "production",
        "location": "west",...
        }
     }
    

## Create resources with labels

When creating a new resource, you can apply labels to the resource.

**Note:** You can't add labels to forwarding rules, static external IP addresses, and VPN tunnels when creating these resources. You can only add labels to these networking resources when you're updating the resource. For instructions on adding labels during an update, see Add or update labels to existing resources in this document.

###  Console 

  1. Go to the resource page that you want to create.

     * For VM instances, go to [**Create an instance**](https://console.cloud.google.com/compute/instances).
     * For disks, go to [**Create a disk**](https://console.cloud.google.com/compute/disks).
     * For snapshots, go to [**Create a snapshot**](https://console.cloud.google.com/compute/snapshots).
     * For images, go to [**Create an image**](https://console.cloud.google.com/compute/images).
  2. Under **Labels** , click add**Add label**.

  3. Continue with the creation process.




###  gcloud 

To add a label, use the `create` sub-command with the `--labels` flag. You can add labels to the Compute Engine resources by using the following `gcloud` commands:

  * For VM instances, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
  * For snapshots, use the [`gcloud compute disks snapshot` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot).
  * For images, use the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create).
  * For disks, use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create).



**Example**
    
    
    gcloud compute instances create ... \
        --labels webserver=backend,media=images
    

###  REST 

In the API, during the `POST` request to add a new resource, add the `labels` property in the request body to apply labels to the new resource.

  * For VM instances, use the [`instances.insert()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
  * For snapshots, use the [`disks.createSnapshot()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot).
  * For images, use the [`images.insert()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert).
  * For disks, use the [`disks.insert()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert).



For example, the following snippet makes a `POST` request to create a VM instance with the labels `webserver:backend` and `media:images`:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances
    
    {
     "name": "myVM",
     "machineType": "zones/us-central1-f/machineTypes/custom-2-15360-ext",
      ...,
     "labels": {
       "webserver": "backend",
       "media": "images"
      }
    }
    

## Add or update labels to existing resources

You can add labels or update existing labels on resources by using the Google Cloud console, the gcloud CLI, or the Compute Engine API. To add or update labels for forwarding rules, use the gcloud CLI or the Compute Engine API.

###  Console 

  1. Go to the resource page for which you want to add labels.

     * For VM instances, go to [**VM instances**](https://console.cloud.google.com/compute/instances).
     * For snapshots, go to [**Snapshots**](https://console.cloud.google.com/compute/snapshots).
     * For images, go to [**Images**](https://console.cloud.google.com/compute/images).
     * For disks, go to [**Disks**](https://console.cloud.google.com/compute/disks).
     * For static external IP addresses, go to [**External IP addresses**](https://console.cloud.google.com/networking/addresses).
     * For VPN tunnels, go to [**VPN**](https://console.cloud.google.com/hybrid/vpn/list).
  2. Select the checkboxes next to the resources you want to label.

  3. To expand the labels column, click **Show info panel**.

  4. In the panel, select **Labels**.

  5. To add labels, click add**Add label** and add the key-value pair.

  6. To update labels, select the existing labels and modify their values.

  7. Save your changes.




###  gcloud 

To add or change a label, use the `update` sub-command with the `--update-labels` flag. You can update labels for the Compute Engine resources by using the following `gcloud` commands:

  * For VM instances, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update).
  * For snapshots, use the [`gcloud compute snapshots update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/update).
  * For images, use the [`gcloud compute images update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/update).
  * For disks, use the [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update).
  * For forwarding rules, use the [`gcloud compute forwarding-rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update).
  * For static external IP addresses, use the [`gcloud beta compute addresses update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/addresses/update).
  * For VPN tunnels, use the [`gcloud beta compute vpn-tunnels update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/vpn-tunnels/update).



**Example**
    
    
    gcloud compute disks update example-disk \
        --update-labels backend=webserver,media=images
    

If you provide a label key that already exists, the Google Cloud CLI updates the existing key with the new label value. If you provide a new key, the tool adds the new key to the list of labels.

###  REST 

To add or update labels, make a `POST` request to the `setLabels` method of the resource with the latest fingerprint and a full list of labels to apply:

  * For VM instances, use the [`instances.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setLabels).
  * For snapshots, use the [`snapshots.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/latest/snapshots/setLabels).
  * For images, use the [`images.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/latest/images/setLabels).
  * For disks, use the [`disks.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/latest/disks/setLabels).
  * For forwarding rules, use the [`forwardingRules.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/setLabels).
  * For regional static external IP addresses, use the [ beta `addresses.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/addresses/setLabels).
  * For global static external IP addresses, use the [ beta `globalAddresses.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalAddresses/setLabels).
  * For VPN tunnels, use the [beta `vpnTunnels.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/vpnTunnels/setLabels).



Similar to metadata and tags, if the resource has existing labels you want to keep, you must include those labels in the request, along with any new labels that you want to add.

For example, the following snippet makes a `POST` request to a VM instance to set labels `environment:test` and `an-existing-tag:yes`:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances/example-instance/setLabels
    
    {
     "labels": {
      "environment": "test",
      "an-existing-tag": "yes"
     },
     "labelFingerprint": "42WmSpB8rSM="
    }
    

## View labels

You can view labels for resources by using the Google Cloud console, the gcloud CLI, or the Compute Engine API. To view labels for forwarding rules, use the gcloud CLI or the Compute Engine API.

###  Console 

  1. Go to the resource page.

     * For VM instances, go to [**VM instances**](https://console.cloud.google.com/compute/instances).
     * For snapshots, go to [**Snapshots**](https://console.cloud.google.com/compute/snapshots).
     * For images, go to [**Images**](https://console.cloud.google.com/compute/images).
     * For disks, go to [**Disks**](https://console.cloud.google.com/compute/disks).
     * For static external IP addresses, go to [**External IP addresses**](https://console.cloud.google.com/networking/addresses).
     * For VPN tunnels, go to [**VPN**](https://console.cloud.google.com/hybrid/vpn/list).
  2. Click the resource to view its details.

  3. Locate **Labels**.




###  gcloud 

To view labels, use the `describe` sub-command. You can view labels for the Compute Engine resources by using the following `gcloud` commands:

  * For VM instances, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe).
  * For snapshots, use the [`gcloud compute snapshots describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/describe).
  * For images, use the [`gcloud compute images describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe).
  * For disks, use the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe).
  * For forwarding rules, use the [`gcloud compute forwarding-rules describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/describe).
  * For static external IP addresses, use the [`gcloud beta compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/addresses/describe).
  * For VPN tunnels. use the [`gcloud beta compute vpn-gateways describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/vpn-gateways/describe).



**Example**
    
    
    gcloud compute disks describe example-disk
    

The output contains the labels:
    
    
    ...
    id: '5047929990219134234'
    kind: compute#disk
    labelFingerprint: GHZ1Un209U=0
    labels:
      environment: dev
      department: finance
    ...
    

###  REST 

To retrieve labels, make a `GET` request to the following resource:

  * For VM instances, use the [`instances.get()` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/get).
  * For snapshots, use the [`snapshots.get()` method](https://docs.cloud.google.com/compute/docs/reference/latest/snapshots/get).
  * For images, use the [`images.get()` method](https://docs.cloud.google.com/compute/docs/reference/latest/images/get).
  * For disks, use the [`disks.get()` method](https://docs.cloud.google.com/compute/docs/reference/latest/disks/get).
  * For forwarding rules, use the [`forwardingRules.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/get).
  * For regional static external IP addresses, use the [beta `addresses.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/addresses/get).
  * For global static external IP addresses, use the [beta `globalAddresses.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalAddresses/get).
  * For VPN tunnels, use the [beta `vpnTunnels.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/vpnTunnels/get).



For example, the following snippet makes a `GET` request to retrieve labels for a VM instance:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
    

Replace the following:

  * PROJECT_ID: the project ID
  * ZONE: the zone of the VM
  * VM_NAME: the name of the VM



## Get a label fingerprint for API requests

When updating or adding labels in the API, you need to provide the latest labels fingerprint with your request, to prevent any conflicts with other requests. A fingerprint is only required for API requests; the [Google Cloud console](https://console.cloud.google.com/) and the Google Cloud CLI tool do not require a fingerprint.

**Note:** You can get the label fingerprint only by making a query directly to the API.

To get the latest `labelsFingerprint`, make a `GET` request to the following resources:

  * For VM instances, use the [`instances.get()` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/get).
  * For snapshots, use the [`snapshots.get()` method](https://docs.cloud.google.com/compute/docs/reference/latest/snapshots/get).
  * For images, use the [`images.get()` method](https://docs.cloud.google.com/compute/docs/reference/latest/images/get).
  * For disks, use the [`disks.get()` method](https://docs.cloud.google.com/compute/docs/reference/latest/disks/get).
  * For forwarding rules, use the [`forwardingRules.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/get).
  * For regional static external IP addresses, use the [beta `addresses.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/addresses/get).
  * For global static external IP addresses, use the [beta `globalAddresses.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalAddresses/get).
  * For VPN tunnels, use the [beta `vpnTunnels.get()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/vpnTunnels/get).



For example, the following snippet gets a `labelsFingerprint` for a VM instance:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances/example-instance
    

The response contains the `labelFingerprint` property:
    
    
    200 OK
    
    {
     "kind": "compute#instance",
     "id": "4392196237934605253",
     "creationTimestamp": "2015-09-15T14:05:16.475-07:00",
     "zone": "https://content.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f",
     "status": "RUNNING",
     ...
     "labels": {
      "environment": "test"
     },
     "labelFingerprint": "p1ty_9HoBk0="
    }

## Remove a label

You can remove labels from resources by using the Google Cloud console, the gcloud CLI, or the Compute Engine API. To remove labels for forwarding rules, use the gcloud CLI or the Compute Engine API.

###  Console 

  1. Go to the resource page for which you want to remove labels.

     * For VM instances, go to [**VM instances**](https://console.cloud.google.com/compute/instances).
     * For snapshots, go to [**Snapshots**](https://console.cloud.google.com/compute/snapshots).
     * For images, go to [**Images**](https://console.cloud.google.com/compute/images).
     * For disks, go to [**Disks**](https://console.cloud.google.com/compute/disks).
     * For static external IP addresses, go to [**External IP addresses**](https://console.cloud.google.com/networking/addresses).
     * For VPN tunnels, go to [**VPN**](https://console.cloud.google.com/hybrid/vpn/list).
  2. Select the checkboxes next to the resources for which you want to remove labels.

  3. To expand the labels column, click **Show info panel**.

  4. To delete a label, click delete **Delete**.

  5. Save your changes.




###  gcloud 

To add or change a label, use the `update` sub-command with the `--remove-labels` flag. You can remove labels for the Compute Engine resources by using the following `gcloud` commands:

  * For VM instances, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update).
  * For snapshots, use the [`gcloud compute snapshots update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/update).
  * For images, use the [`gcloud compute images update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/update).
  * For disks, use the [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update).
  * For forwarding rules, use the [`gcloud compute forwarding-rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update).
  * For static external IP addresses, use the [`gcloud beta compute addresses update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/addresses/update).
  * For VPN tunnels, use the [`gcloud beta compute vpn-tunnels update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/vpn-tunnels/update).



**Example**
    
    
    gcloud compute disks update example-disk \
        --remove-labels backend,media
    

###  REST 

To remove labels, make a `POST` request to the `setLabels` method of the following resource with the latest fingerprint and a full list of labels to apply:

  * For VM instances, use the [`instances.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setLabels).
  * For snapshots, use the [`snapshots.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/latest/snapshots/setLabels).
  * For images, use the [`images.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/latest/images/setLabels).
  * For disks, use the [`disks.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/latest/disks/setLabels).
  * For forwarding rules, use the [`forwardingRules.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/setLabels).
  * For regional static external IP addresses, use the [beta `addresses.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/addresses/setLabels).
  * For global static external IP addresses, use the [beta `globalAddresses.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalAddresses/setLabels).
  * For VPN tunnels, use the [beta `vpnTunnels.setLabels()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/vpnTunnels/setLabels).



Provide the current `labelsFingerprint` and an empty list of labels to remove all labels, or provide a list of labels you want to keep (omitting the labels you want to remove). For example, the following snippet removes all labels from the VM:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances/example-instance/setLabels
    
    {
     "labels": { },
     "labelFingerprint": "42WmSpB8rSM="
    }
    

## Filter searches using labels

You can search your resources and filter results by labels by using the Google Cloud console, the gcloud CLI, or the Compute Engine API. To filter forwarding rules by labels, use the gcloud CLI or the Compute Engine API.

###  Console 

  1. Go to the resource page for which you want to get a filtered list of resources.

     * For VM instances, go to [**VM instances**](https://console.cloud.google.com/compute/instances).
     * For snapshots, go to [**Snapshots**](https://console.cloud.google.com/compute/snapshots).
     * For images, go to [**Images**](https://console.cloud.google.com/compute/images).
     * For disks, go to [**Disks**](https://console.cloud.google.com/compute/disks).
     * For static external IP addresses, go to [**External IP addresses**](https://console.cloud.google.com/networking/addresses).
     * For VPN tunnels, go to [**VPN**](https://console.cloud.google.com/hybrid/vpn/list).
  2. If prompted, select your project and click **Continue**.

  3. In the search bar, enter your key, value, or key-value pair. Your results include any partial matches.

For example, to show only resources with the label `env:dev`, you can enter any of the following:

     * Enter the key: `env`
     * Enter the value: `dev`
     * Enter the key-value pair: `env:dev`



###  gcloud 

To filter based on labels, use the `list` sub-command of the following resources with the `--filter` flag:

  * For VM instances, use the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list).
  * For snapshots, use the [`gcloud compute snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/list).
  * For images, use the [`gcloud compute images list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list).
  * For disks, use the [`gcloud compute disks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list).
  * For forwarding rules, use the [`gcloud compute forwarding-rules list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/list).
  * For static external IP addresses, use the [`gcloud beta compute addresses list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/addresses/list).
  * For VPN tunnels, use the [`gcloud beta compute vpn-tunnels list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/vpn-tunnels/list).



The value of `--filter` flag must be in the `labels.KEY=VALUE` format. For example, if you wanted to filter on a label with `env` as the key and `dev` as the value, you can run this command:
    
    
    gcloud compute instances list \
        --filter labels.env=dev
    

For more information about the filter syntax in the gcloud CLI, see the [`gcloud topic filters` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

###  REST 

To filter resources, make a `GET` request to the `list` method of the following resources and include the filter field:

  * For VM instances, use the [`instances.list()` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/list).
  * For snapshots, use the [`snapshots.list()` method](https://docs.cloud.google.com/compute/docs/reference/latest/snapshots/list).
  * For images, use the [`images.list()` method](https://docs.cloud.google.com/compute/docs/reference/latest/images/list).
  * For disks, use the [`disks.list()` method](https://docs.cloud.google.com/compute/docs/reference/latest/disks/list).
  * For forwarding rules, use the [`forwardingRules.list()` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/list).
  * For regional static external IP addresses, use the [beta `addresses.list()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/addresses/list).
  * For global static external IP addresses, use the [beta `globalAddresses.list()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalAddresses/list).
  * For VPN tunnels, use the [beta `vpnTunnels.list()` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/vpnTunnels/list).



For example, to list all the VMs in the project `myproject` and zone `us-central1-a` with a label that has a key-value pair of `env:dev`, set the filter field to `labels.env:dev` in your `list` request. If you include the filter field as a query string parameter, use a URL-encoded parameter value, `filter=labels.env%3Adev`:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-a/instances?filter=labels.env%3Adev
    

For more information, read the [`filter` documentation](https://docs.cloud.google.com/compute/docs/reference/latest/instances/list#filter) in the Compute Engine API reference.

## Relationship between VM labels and tags

In the past, labels and tags were related. For example, if you added a `webserver:test` label to a VM, Compute Engine automatically added a `webserver` tag to the VM.

Now, labels and tags are separate. If you create a label on a VM, Compute Engine does not create a tag for the VM. If you need to create a tag on a VM, you must create the tag manually.

To learn more about tags and their uses, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## What's next

  * Learn how to [compare Tags and network tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#differences).
  * Learn how to [manage tags for Compute Engine resources](https://docs.cloud.google.com/compute/docs/tag-resources).
  * Review the `filter` query parameter to learn about [filtering](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list#:%7E:text=A%20filter%20expression).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
