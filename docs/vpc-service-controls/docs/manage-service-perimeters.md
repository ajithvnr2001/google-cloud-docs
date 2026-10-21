---
url: https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters/
title: Manage service perimeters \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:39.918757+00:00
---

# Manage service perimeters  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Manage service perimeters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can manage service perimeters in VPC Service Controls. For details on creating new service perimeters, see [Creating service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

This page includes the following sections:

  * Before you begin

  * List and describe service perimeters

  * List service perimeters (formatted)

  * Updating a service perimeter

  * Adding an access level to an existing perimeter

  * Deleting a perimeter

  * Limit access to services inside a perimeter with VPC accessible services




## Before you begin

  * Read [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

  * Read [Service perimeter configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#stages).

  * [Set your default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default) for using the `gcloud` command-line tool.

_-or-_

[Get the name of your policy.](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#get_the_name_of_an_access_policy) The policy name is required for commands using the `gcloud` command-line tool and making API calls. If you set a default access policy, you don't need to specify the policy for the `gcloud` command-line tool.




## List and describe service perimeters

List all service perimeters in an organization:

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to view.




### gcloud

To list your organization's service perimeters, use the [`list` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/list):
    
    
    gcloud access-context-manager perimeters list
    

You should see a list of the perimeters for your organization. For example:
    
    
    NAME           TITLE                 ETAG
    ProdPerimeter  Production Perimeter  abcdefg123456789
    

To view details about a service perimeter, use the [`describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/describe):
    
    
    gcloud access-context-manager perimeters \
      describe PERIMETER_ID
    

Replace the following:

  * PERIMETER_ID is the ID of the service perimeter that you want to obtain details about.



You should see the details about the perimeter. For example:
    
    
    etag: abcdefg123456789
    name: accessPolicies/626111171578/servicePerimeters/ProdPerimeter
    status:
      accessLevels:
      - accessPolicies/626111171578/accessLevels/corpAccess
      resources:
      - projects/111584792408
      restrictedServices:
      - bigquery.googleapis.com
      - storage.googleapis.com
    title: Production Perimeter
    

## List service perimeters (formatted)

Using the `gcloud` command-line tool, you can obtain a list of your service perimeters in YAML or json format.

To get a formatted list of perimeters, use the [`list` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/list):
    
    
    gcloud access-context-manager perimeters list \
      --format=FORMAT

Replace the following:

  * FORMAT is one of the following values:

    * `list` (YAML format)

    * `json` (JSON format)




The following output is an example list in YAML format:
    
    
    - etag: abcdefg123456789
      name: accessPolicies/165717541651/servicePerimeters/On_Prem
      status: {'resources': ['projects/167410821371'], 'restrictedServices': ['bigquery.googleapis.com', 'storage.googleapis.com']}
      title: On Prem
    - etag: hijklmn987654321
      name: accessPolicies/165717541651/servicePerimeters/Private
      spec: {'resources': ['projects/136109111311'], 'restrictedServices': ['bigquery.googleapis.com', 'storage.googleapis.com', 'logging.googleapis.com']}
      status: {'resources': ['projects/136109111311', 'projects/401921913171'], 'restrictedServices': ['bigquery.googleapis.com']}
      title: Private
      useExplicitDryRunSpec: True
    - etag: pqrstuv123456789
      name: accessPolicies/165717541651/servicePerimeters/OnpremBridge
      perimeterType: PERIMETER_TYPE_BRIDGE
      status: {'resources': ['projects/167410821371']}
      title: OnpremBridge

The following output is an example list in JSON format:
    
    
    [
      {
        "etag": "abcdefg123456789",
        "name": "accessPolicies/165717541651/servicePerimeters/On_Prem",
        "status": {
          "resources": [
            "projects/167410821371"
          ],
          "restrictedServices": [
            "bigquery.googleapis.com",
            "storage.googleapis.com"
          ]
        },
        "title": "On Prem"
      },
      {
        "etag": "hijklmn987654321",
        "name": "accessPolicies/165717541651/servicePerimeters/Private",
        "spec": {
          "resources": [
            "projects/136109111311"
          ],
          "restrictedServices": [
            "bigquery.googleapis.com",
            "storage.googleapis.com",
            "logging.googleapis.com"
          ]
        },
        "status": {
          "resources": [
            "projects/136109111311",
            "projects/401921913171"
          ],
          "restrictedServices": [
            "bigquery.googleapis.com"
          ]
        },
        "title": "Private",
        "useExplicitDryRunSpec": true
      },
      {
        "etag": "pqrstuv123456789",
        "name": "accessPolicies/165717541651/servicePerimeters/OnpremBridge",
        "perimeterType": "PERIMETER_TYPE_BRIDGE",
        "status": {
          "resources": [
            "projects/167410821371"
          ]
        },
        "title": "OnpremBridge"
      }
    ]

## Update a service perimeter

This section describes how to update individual service perimeters. To update all of your organization's service perimeters in one operation, see [Making bulk changes to service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/bulk-operations).

You can perform the following tasks to update a service perimeter:

  * Add new Google Cloud projects or remove projects from a service perimeter.
  * Change the list of restricted Google Cloud services. You can also change the title and description for a service perimeter.
  * Enable, add, remove, or disable VPC accessible services.
  * [Update the ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#updating).



After you update a service perimeter, it can take up to 30 minutes for the changes to propagate and take effect. During this time, the perimeter might block requests with the following error message: `Error 403: Request is prohibited by organization's policy.`

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. On the **Service perimeter details** page, click **Edit**.

  4. On the **Edit service perimeter** page, update the service perimeter.

  5. Click **Save**.




### gcloud

To add new resources to a perimeter, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update) and specify the resources to add:
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
      --add-resources=RESOURCES
    

Replace the following:

  * PERIMETER_ID is the ID of the service perimeter that you want to obtain details about.

  * RESOURCES is a comma-separated list of one or more project numbers or VPC network names. For example: `projects/12345` or `//compute.googleapis.com/projects/my-project/global/networks/vpc1`. Only projects and VPC networks are allowed. Project format: `projects/project_number`. VPC format: `//compute.googleapis.com/projects/project-id/global/networks/network_name`.




To update the list of restricted services, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update) and specify the services to add as a comma-delimited list:
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
      --add-restricted-services=SERVICES
    

Replace the following:

  * PERIMETER_ID is the ID of the service perimeter that you want to obtain details about.

  * SERVICES is a comma-delimited list of one or more services. For example: `storage.googleapis.com` or `storage.googleapis.com,bigquery.googleapis.com`.




## Add an access level to an existing perimeter

Once you have [created an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level), you can apply it to a service perimeter to control access.

After you update a service perimeter, it can take up to 30 minutes for the changes to propagate and take effect. During this time, the perimeter might block requests with the following error message: `Error 403: Request is prohibited by organization's policy.`

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. On the **Service perimeter details** page, click **Edit**.

  4. On the **Edit service perimeter** page, click **Access levels**.

  5. Click **Add access levels**.

  6. In the **Add access levels** pane, select the checkboxes corresponding to the access levels that you want to apply to the service perimeter.

  7. Click **Add selected access levels**.

  8. Click **Save**.




### gcloud

To add an access level to an existing service perimeter, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update):
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
      --add-access-levels=LEVEL_NAME
    

Replace the following:

  * PERIMETER_ID is the ID of your service perimeter.

  * LEVEL_NAME is the name of the access level that you want to add to the perimeter.




For more information about using access levels with a perimeter, see [Allow access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

## Delete a service perimeter

When you delete a service perimeter, the security controls associated with the perimeter no longer apply to the associated Google Cloud projects. There isn't any other impact to the member Google Cloud projects or associated resources.

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table row corresponding to the perimeter that you want to delete, click _delete_.




### gcloud

To delete a service perimeter, use the [`delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/delete):
    
    
    gcloud access-context-manager perimeters delete PERIMETER_ID
    

Replace the following:

  * PERIMETER_ID is the ID of your service perimeter.



## Limit access to Google APIs inside a perimeter

This section describes configuration settings that limit access to Google APIs from network endpoints inside a service perimeter.

You can restrict access in the following ways:

  * Configure VPC accessible services: limit the set of supported Google APIs that are accessible from network endpoints _inside_ your service perimeter.
  * Configure service patterns: limit the set of unsupported Google APIs that can be accessed from network endpoints _inside_ your service perimeter.



### Limit access by using VPC accessible services

You can use the VPC accessible services feature to limit the set of services that are accessible from network endpoints _inside_ your service perimeter. You can add VPC accessible services to service perimeters but not to perimeter bridges.

To learn more about the VPC accessible services feature, read about [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).

#### Enable VPC accessible services

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. On the **Service perimeter details** page, click edit **Edit**.

  4. In the **VPC accessible services** pane, select one of the following options:

     * **All restricted services** : Restricts access to only the services protected by this service perimeter.
     * **Selected services** : Restricts access to a custom list of services.
     * **No services** : Blocks access to all services.
  5. Click **Save** , and then click **Confirm**.




### gcloud

To enable VPC accessible services for your service perimeter, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update):
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
      --enable-vpc-accessible-services \
      --add-vpc-allowed-services=SERVICES
    

Replace the following:

  * PERIMETER_ID is the ID of your service perimeter.

  * SERVICES is a comma-separated list of one or more services that you want to _allow_ networks _inside_ your perimeter to access. Access to any services that are _not included_ in this list are prevented.

To quickly include the services protected by the perimeter, add `RESTRICTED-SERVICES` to the list for SERVICES. You can include other services in addition to `RESTRICTED-SERVICES`.




For example, to ensure that the VPC networks in your perimeter have access only to the Logging and Cloud Storage services, use the following command:
    
    
    gcloud access-context-manager perimeters update example_perimeter \
      --enable-vpc-accessible-services \
      --add-vpc-allowed-services=\
    RESTRICTED-SERVICES,logging.googleapis.com,storage.googleapis.com \
      --policy=11271009391
    

#### Add a service to the VPC accessible services

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. On the **Service perimeter details** page, click edit **Edit**.

  4. In the **VPC accessible services** pane, select **Selected services**.

  5. Click **Add services**.

  6. In the **Add services** pane, select the checkboxes for the services that you want to allow.

  7. Click **Add selected services**.

  8. Optional: To automatically include all services protected by the perimeter, click the **Include all restricted services** toggle to the on position.

  9. Click **Save** , and then click **Confirm**.




### gcloud

To add additional services to the VPC accessible services for your perimeter, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update):
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
      --add-vpc-allowed-services=SERVICES
    

Replace the following:

  * PERIMETER_ID is the ID of your service perimeter.

  * SERVICES is a comma-separated list of one or more services that you want to _allow_ networks _inside_ your perimeter to access.

To quickly include the services protected by the perimeter, add `RESTRICTED-SERVICES` to the list for SERVICES. You can include separate services in addition to `RESTRICTED-SERVICES`.




For example, if you enable VPC accessible services and require that the VPC networks in your perimeter have access to the Pub/Sub service, use the following command:
    
    
    gcloud access-context-manager perimeters update example_perimeter \
      --add-vpc-allowed-services=RESTRICTED-SERVICES,pubsub.googleapis.com \
      --policy=11271009391
    

#### Remove a service from the VPC accessible services

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. On the **Service perimeter details** page, click edit **Edit**.

  4. In the **VPC accessible services** pane, make sure that the option is set to **Selected services**.

  5. In the list of allowed services, locate the service that you want to remove, and click delete **Delete** next to the service name.

  6. Click **Save** , and then click **Confirm**.




### gcloud

To remove services from the VPC accessible services for your service perimeter, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update):
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
      --remove-vpc-allowed-services=SERVICES
    

Replace the following:

  * PERIMETER_ID is the ID of your service perimeter.

  * SERVICES is a comma-separated list of one or more services that you want to remove from the list of services that networks _inside_ your service perimeter are permitted to access.




For example, if you enable VPC accessible services and you no longer want the VPC networks in your perimeter to have access to the Cloud Storage service, use the following command:
    
    
    gcloud access-context-manager perimeters update example_perimeter \
      --remove-vpc-allowed-services=storage.googleapis.com \
      --policy=11271009391
    

#### Disable VPC accessible services

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. On the **Service perimeter details** page, click edit **Edit**.

  4. In the **VPC accessible services** pane, select **All services**.

  5. Click **Save** , and then click **Confirm**.




### gcloud

To disable VPC service restrictions for your service perimeter, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update):
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
      --no-enable-vpc-accessible-services \
      --clear-vpc-allowed-services
    

Replace the following:

  * PERIMETER_ID is the ID of your service perimeter.



For example, to disable VPC service restrictions for `example_perimeter`, use the following command:
    
    
    gcloud access-context-manager perimeters update example_perimeter \
      --no-enable-vpc-accessible-services \
      --clear-vpc-allowed-services \
      --policy=11271009391
    

### Limit access by using service patterns

You can use VPC Service Controls [service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services#service-patterns) to specify which Google APIs, including unsupported services, can be accessed from networks inside a service perimeter.

While VPC accessible services require using the [restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity), service patterns are designed for networks that use the [private VIP](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-options) (`private.googleapis.com`) or a Private Service Connect endpoint with the `all-apis` bundle.

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. On the **Service perimeter details** page, click edit **Edit**.

  4. In the **VPC accessible services** pane, select **Select services and patterns**.

  5. To add a supported service or an unsupported service pattern, click add **Add**.

     * To add a supported Google API: 
       1. Select the **Services** option.
       2. Select the checkbox next to each service name that you want to allow.
       3. Click **Add selected services**.
     * To add an unsupported Google API using a custom URL pattern: 
       1. Select the **Patterns** option.
       2. Click **Add pattern** or enter a URL pattern in the **Pattern** field (for example, `maps.googleapis.com/*`).
       3. Optional: Add custom HTTP request headers. Click **Add request header** , choose a header key from the **Key** list, and specify the value.
       4. Click **Add service patterns**.
  6. In the **Service patterns enforcement scopes** drop-down list, select **Google APIs via Private Path**.

  7. Click **Save** , and then click **Confirm**.




### gcloud

To configure service patterns, you must specify the VPC accessible services configuration in a YAML file.
    
    
    enableRestriction: true
    servicePatternsEnforcementScopes:
    - GOOGLE_APIS_VIA_PRIVATE_PATH
    allowedServicePatterns:
    - service: 'RESTRICTED-SERVICES'
    - service: 'logging.googleapis.com'
    - pattern: 'maps.googleapis.com/*'
    - pattern: 'www.googleapis.com/drive/*'
    

The YAML file contains the following fields:

  * **`enableRestriction`** : Set to `true` to enable limits on accessible services.
  * **`servicePatternsEnforcementScopes`** : Set this to `GOOGLE_APIS_VIA_PRIVATE_PATH` to enforce service patterns on Google APIs accessed through the private VIP.
  * **`allowedServicePatterns`** : The list of allowed services and URL patterns, which represent Google API hostnames and URL path patterns, corresponding to the HTTP `Host` headers of the requests. 
    * Use the `service` field for supported services (for example, `logging.googleapis.com`). You can also specify the `RESTRICTED-SERVICES` value, which expands to all services protected by the service perimeter.
    * Use the `pattern` field for unsupported URL patterns (for example, `maps.googleapis.com/*`).



**Create or update perimeters with service patterns**

To create a service perimeter with service patterns, use the [`create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/create) command. Specify the YAML configuration file that you set up in Limit access by using service patterns:
    
    
    gcloud access-context-manager perimeters \
      create PERIMETER_ID \
      --title="TITLE" \
      --resources="projects/PROJECT_ID" \
      --restricted-services=SERVICES \
      --vpc-accessible-services=vpc_accessible_services.yaml \
      --policy=POLICY_ID
    

To update an existing service perimeter to use service patterns, use the [`update`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update) command. Specify the YAML configuration file that you set up in Limit access by using service patterns:
    
    
    gcloud access-context-manager perimeters \
      update PERIMETER_ID \
      --set-vpc-accessible-services=vpc_accessible_services.yaml \
      --policy=POLICY_ID
    

Replace the following:

  * PERIMETER_ID: The ID of your service perimeter.

  * TITLE: The title of the service perimeter.

  * PROJECT_ID: The ID of the project to add to the perimeter.

  * SERVICES: A comma-separated list of one or more services.

  * POLICY_ID: The ID of your access policy.

  * `vpc_accessible_services.yaml` is the path to the YAML configuration file that you set up in [Limit access by using service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#gcloud_8).




#### Attach headers to requests for unsupported APIs

You can attach HTTP headers (such as `X-Goog-Allowed-Resources`) to requests for unsupported APIs. Add `modifiers` in the `allowedServicePatterns` section of your configuration YAML file:
    
    
    enableRestriction: true
    servicePatternsEnforcementScopes:
    - GOOGLE_APIS_VIA_PRIVATE_PATH
    allowedServicePatterns:
    - pattern: 'appengine.googleapis.com/*'
      modifiers:
      - addRequestHeader:
          key: 'X-Goog-Allowed-Resources'
          value: 'YOUR_ORGANIZATION_RESTRICTIONS_HEADER'
    

The `addRequestHeader` section contains the following fields to specify the HTTP request headers:

  * **`key`** : The name of the HTTP request header to add. The supported keys are `X-Goog-Allowed-Resources` and `X-GoogApps-Allowed-Domains`.
  * **`value`** : The value for the specified HTTP request header.



Replace YOUR_ORGANIZATION_RESTRICTIONS_HEADER with the web-safe base64-encoded JSON string that specifies the allowed Google Cloud Organization IDs. For details on how to format this header value, see [Configure organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/configure-organization-restrictions).

#### Test with dry-run mode

### Console

To verify the impact of service patterns before enforcing them, configure the service patterns in the dry-run mode of your perimeter:

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, click the **Dry run mode** tab.

  3. In the list of service perimeters, click the name of the service perimeter that you want to modify.

  4. On the **Service perimeter details** page, click edit **Edit**.

  5. On the **Edit service perimeter** page, make changes to the dry run configuration (as described in Limit access by using service patterns).

  6. Click **Save** , and then click **Confirm**.

  7. Observe the audit logs to check for violations. For details, see [Identifying blocked requests](https://docs.cloud.google.com/vpc-service-controls/docs/manage-dry-run-configurations#identifying_blocked_requests).

  8. On the **Service perimeter details** page, click **Enforce config**.

  9. When you are asked to confirm that you want to overwrite your existing enforced configuration, click **Confirm**.




### gcloud

To verify the impact of service patterns before enforcing them, configure the service patterns in the dry-run mode of your perimeter:

  1. Create a dry-run perimeter containing your configuration file.
         
         gcloud access-context-manager perimeters dry-run \
           create PERIMETER_ID \
           --perimeter-title="TITLE" \
           --perimeter-resources="projects/PROJECT_ID" \
           --perimeter-restricted-services=SERVICES \
           --perimeter-vpc-accessible-services=vpc_accessible_services.yaml \
           --policy=POLICY_ID
         

  2. Observe the audit logs to check for violations.

  3. Enforce the configuration by replacing the perimeter's main configuration.
         
         gcloud access-context-manager perimeters dry-run \
           enforce PERIMETER_ID \
           --policy=POLICY_ID
         




#### Migrate from restricted VIP to private VIP

If you are already using VPC accessible services with the [restricted VIP](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity), you can migrate to service patterns on the [private VIP](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-options):

  1. Update the perimeter configuration to use service patterns using a YAML file:
         
         gcloud access-context-manager perimeters \
           update PERIMETER_ID \
           --set-vpc-accessible-services=vpc_accessible_services.yaml \
           --policy=POLICY_ID
         

Ensure that `servicePatternsEnforcementScopes` is set to `GOOGLE_APIS_VIA_PRIVATE_PATH`.

  2. Update the DNS, routing, and firewall configurations in your VPC network to point to the private VIP (`private.googleapis.com`) or update the Private Service Connect endpoint to use the `all-apis` bundle.

**Note:** Update the perimeter configuration before switching to the private VIP to ensure exfiltration paths remain blocked.



#### Limitations

  * Enforcement only applies to the private VIP path (`private.googleapis.com` or Private Service Connect `all-apis` endpoint).
  * The following URL pattern formats are supported: 
    * `API_NAME.googleapis.com/*`
    * `www.googleapis.com/API_NAME/*`
    * `*.appspot.com/*`
  * Only `X-Goog-Allowed-Resources` and `X-GoogApps-Allowed-Domains` are supported.
  * Headers are inserted only for requests to unsupported services.
  * Modifiers and `addRequestHeader` don't insert headers when configured in dry-run mode.
  * Violation logs triggered by requests to unsupported APIs contain limited metadata. For details, see [Audit logging limitations](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging#limitations).
  * VPC Service Controls violation analyzer does not support troubleshooting violations for unsupported services. Refer to the audit logs using the violation ID.



### VPC accessible services and the Access Context Manager API

You can also use the Access Context Manager API to manage VPC accessible services. When you create or modify a service perimeter, use the [`ServicePerimeterConfig` object](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1beta/accessPolicies.servicePerimeters#ServicePerimeterConfig) in the response body to configure your VPC accessible services.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
