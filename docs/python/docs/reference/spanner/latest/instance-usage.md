---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/instance-usage/
title: Instance Admin Usage \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:48.739355+00:00
---

# Instance Admin Usage  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/instance-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Instance Admin Usage Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

After creating a [`Client`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/client#google.cloud.spanner_v1.client.Client), you can interact with individual instances for a project.

## Instance Configurations

Each instance within a project maps to a named “instance configuration”, specifying the location and other parameters for a set of instances. These configurations are defined by the server, and cannot be changed.

To iterate over all instance configurations available to your project, use the [`list_instance_configs()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/client#google.cloud.spanner_v1.client.Client.list_instance_configs) method of the client:
    
    
    for config in client.list_instance_configs():
        # `config` is an instance of `InstanceConfig`
    

To fetch a single instance configuration, use the `get_instance_configuration()` method of the client:
    
    
    config = client.get_instance_configuration('config-name')
    

Each of these methods provide [`InstanceConfig`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_admin_instance_v1/types_#google.cloud.spanner_admin_instance_v1.types.InstanceConfig) objects.

## List Instances

If you want a comprehensive list of all existing instances, iterate over the [`list_instances()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/client#google.cloud.spanner_v1.client.Client.list_instances) method of the client:
    
    
    for instance in client.list_instances():
        # `instance` is an instance of `Instance`
    

This iterator yields [`Instance`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_admin_instance_v1/types_#google.cloud.spanner_admin_instance_v1.types.Instance) objects.

## Instance Factory

To create a [`Instance`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance) object:
    
    
    config = configs[0]
    instance = client.instance(instance_id,
                               configuration_name=config.name,
                               node_count=10,
                               display_name='My Instance')
    

  * `configuration_name` is the name of the instance configuration to which the instance will be bound. It must be one of the names configured for your project, discoverable via [`list_instance_configs()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/client#google.cloud.spanner_v1.client.Client.list_instance_configs).

  * `node_count` is a postitive integral count of the number of nodes used by the instance. More nodes allows for higher performance, but at a higher billing cost.

  * `display_name` is optional. When not provided, `display_name` defaults to the `instance_id` value.




You can also use `Client.instance()` to create a local wrapper for an instance that has already been created:
    
    
    instance = client.instance(existing_instance_id)
    instance.reload()
    

## Create a new Instance

After creating the instance object, use its [`create()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance.create) method to trigger its creation on the server:
    
    
    instance.display_name = 'My very own instance'
    operation = instance.create()
    

**NOTE** : Creating an instance triggers a “long-running operation” and returns an `google.cloud.spanner_v1.instance.Operation` object. See Resolve Current Instance Operation for polling to find out if the operation is completed.

## Refresh metadata for an existing Instance

After creating the instance object, reload its server-side configuration using its [`reload()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance.reload) method:
    
    
    instance.reload()
    

This will load `display_name`, `config_name`, and `node_count` for the existing `instance` object from the back-end.

## Update an existing Instance

After creating the instance object, you can update its metadata via its [`update()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance.update) method:
    
    
    client.display_name = 'New display_name'
    operation = instance.update()
    

**NOTE** : Update an instance triggers a “long-running operation” and returns a `google.cloud.spanner_v1.instance.Operation` object. See Resolve Current Instance Operation for polling to find out if the operation is completed.

## Delete an existing Instance

Delete an instance using its [`delete()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance.delete) method:
    
    
    instance.delete()
    

## Resolve Current Instance Operation

The [`create()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance.create) and [`update()`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance.update) methods of instance object trigger long-running operations on the server, and return instances of the `Operation` class.

If you want to block on the completion of those operations, use the `result` method on the returned objects:
    
    
    >>> operation = instance.create()
    >>> result = operation.result()
    

This method will raise an exception if the operation fails.

## Next Step

Now we go down the hierarchy from [`Instance`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/instance#google.cloud.spanner_v1.instance.Instance) to a [`Database`](https://docs.cloud.google.com/python/docs/reference/spanner/latest/spanner_v1/database#google.cloud.spanner_v1.database.Database).

Next, learn about the [Database Admin Usage](https://docs.cloud.google.com/python/docs/reference/spanner/latest/database-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
