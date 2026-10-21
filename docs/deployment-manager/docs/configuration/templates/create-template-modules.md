---
url: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-template-modules/
title: Using Template Modules \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:58.900961+00:00
---

# Using Template Modules  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-template-modules/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Using Template Modules Stay organized with collections  Save and categorize content based on your preferences. 

Template modules are helper files that perform specific functions that can make your templates more efficient. For example, you can have a module that generates unique names for your resources. Deployment Manager can execute any module written in Python or Jinja.

## Before you begin

  * If you want to use the command-line examples in this guide, install the [`gcloud` command-line tool](https://docs.cloud.google.com/sdk).
  * If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/deployment-manager/docs/reference/latest).
  * Understand how to [create a basic template](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template). 
  * Understand how to [create a configuration](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-basic-configuration)



## Creating a template module

A template module is treated as a regular template file and can be written in Jinja or Python.

For example, the following is a helper template that generates a name given a prefix and suffix.

###  Jinja 

  
In Jinja, this helper template (in this example, named helpers/common.jinja) would look like the following:
    
    
    
    {%- macro GenerateMachineName(prefix='', suffix='') -%}
        {{ prefix + "-" + suffix }}
    {%- endmacro %}
    

You can then import this template and use it as a module. In your Jinja template, you could use the module like so:
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    
    {% import 'helpers/common.jinja' as common %}
    
    resources:
    - name: {{ common.GenerateMachineName("myfrontend", "prod") }}
      type: compute.v1.instance
      properties:
        zone: us-central1-f
        machineType: https://www.googleapis.com/compute/v1/projects/{{ env['project'] }}/zones/us-central1-f/machineTypes/f1-micro
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/family/debian-11
        networkInterfaces:
        - network: https://www.googleapis.com/compute/v1/projects/{{ env['project'] }}/global/networks/default
          accessConfigs:
          - name: External NAT
            type: ONE_TO_ONE_NAT
    

The configuration must then import both files (including the `helpers/common.jinja` file):
    
    
    # Copyright 2015 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    imports:
    - path: helpers/common.jinja
    - path: vm-instance-example.jinja
    
    resources:
    - name: my-vm
      type: vm-instance-example.jinja
    

The Deployment Manager service will expand the configuration and the final configuration looks like this:
    
    
    resources:
    - name: myfrontend-prod
      type: compute.v1.instance
      properties:
        zone: us-central1-f
        machineType: https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/machineTypes/f1-micro
        disks:
        - deviceName: boot
          type: PERSISTENT
          boot: true
          autoDelete: true
          initializeParams:
            sourceImage: https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/family/debian-9
        networkInterfaces:
        - network: https://www.googleapis.com/compute/v1/projects/myproject/global/networks/default
          accessConfigs:
          - name: External NAT
            type: ONE_TO_ONE_NAT
    

###  Python 

  
In Python, the helper template (in this example, named helpers/common.py) would look like this:
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    """Generates name of a VM."""
    
    
    def GenerateMachineName(prefix, suffix):
      return prefix + "-" + suffix
    

To use it in your Python template:
    
    
    # Copyright 2016 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    """Constructs a VM with imported module."""
    from helpers import common
    
    COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'
    
    
    def GenerateConfig(context):
      """Generates configuration of a VM."""
      resources = [{
          'name': common.GenerateMachineName('myfrontend', 'prod'),
          'type': 'compute.v1.instance',
          'properties': {
              'zone': 'us-central1-f',
              'machineType': COMPUTE_URL_BASE + 'projects/' + context.env['project']
                             + '/zones/us-central1-f/machineTypes/f1-micro',
              'disks': [{
                  'deviceName': 'boot',
                  'type': 'PERSISTENT',
                  'boot': True,
                  'autoDelete': True,
                  'initializeParams': {
                      'sourceImage': COMPUTE_URL_BASE + 'projects/'
                                     'debian-cloud/global/images/family/debian-11'}
              }],
              'networkInterfaces': [{
                  'network': COMPUTE_URL_BASE + 'projects/' + context.env['project']
                             + '/global/networks/default',
                  'accessConfigs': [{
                      'name': 'External NAT',
                      'type': 'ONE_TO_ONE_NAT'
                  }]
              }]
          }
      }]
      return {'resources': resources}
    

The configuration must then import both files (including the `helpers/common.py` file):
    
    
    # Copyright 2015 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    imports:
    - path: helpers/common.py
    - path: vm-instance-example.py
    
    resources:
    - name: my-vm
      type: vm-instance-example.py
    

Here is a more complicated helper module:
    
    
    # Copyright 2015 Google Inc. All rights reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    """Helper methods for working with containers in config."""
    import common
    import default
    import yaml
    
    # Specific properties for this component, also see container_instance
    DCKRENV = default.DCKRENV
    DCKRIMAGE = default.DCKRIMAGE
    
    MANIFEST = """
    version: v1beta2
    containers:
      - name: %(name)s
        image: %(dockerImage)s
        ports:
          - name: %(name)s-port
            hostPort: %(port)i
            containerPort: %(port)i
        %(env)s
    """
    
    
    def GenerateManifest(context):
      """Generates a Container Manifest given a Template context.
    
      Args:
        context: Template context, which must contain dockerImage and port
            properties, and an optional dockerEnv property.
    
      Returns:
        A Container Manifest as a YAML string.
      """
      env = ""
      env_list = []
      if DCKRENV in context.properties:
        for key, value in context.properties[DCKRENV].iteritems():
          env_list.append({"name": key, "value": value})
      if env_list:
        env = "env: " + yaml.dump(env_list, default_flow_style=True)
    
      manifest_yaml_string = MANIFEST % {
          "name": context.env["name"],
          "dockerImage": context.properties[DCKRIMAGE],
          "port": context.properties[default.PORT],
          "env": env
      }
      return common.GenerateEmbeddableYaml(manifest_yaml_string)
    

## What's next

  * Use [template properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties) to abstract your content.
  * Populate information about your projects and deployments using [environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables).
  * Add a template permanently to your project as a [composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
