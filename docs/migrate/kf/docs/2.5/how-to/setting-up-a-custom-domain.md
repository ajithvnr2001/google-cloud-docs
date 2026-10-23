---
url: https://docs.cloud.google.com/migrate/kf/docs/2.5/how-to/setting-up-a-custom-domain/
title: Setting up a Custom Domain \u00a0|\u00a0 Kf 2.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:00.206112+00:00
---

# Setting up a Custom Domain  |  Kf 2.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.5/how-to/setting-up-a-custom-domain/

Version 2.5

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
  * [ 2.5 ](https://docs.cloud.google.com/migrate/kf/docs/2.5)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.5/documentation)



Send feedback 

#  Setting up a Custom Domain Stay organized with collections  Save and categorize content based on your preferences. 

All Kf Apps that serve HTTP traffic to users or applications outside of the cluster must be associated with a domain name.

Kf has three locations where domains can be configured. Ordered by precedence, they are:

  1. Apps
  2. Spaces
  3. The `config-defaults` ConfigMap in the `kf` Namespace



## The `config-defaults` ConfigMap

The `config-defaults` ConfigMap holds cluster-wide settings for Kf and can be edited by cluster administrators. The values in the ConfigMap are read by the Spaces controller and modify their configuration. Domain values are reflected in the Space's `status.networkConfig.domains` field.

To modify Kf cluster's domain, edit the `config-defaults` ConfigMap in the `kf` Namespace:
    
    
    kubectl edit configmap config-defaults -n kf

Add or update the entry for the `spaceClusterDomain` key like the following:
    
    
    spaceClusterDomain: my-domain.com
    

To validate the configuration was updated correctly, check the domain value in a space:
    
    
    kf space SPACE_NAME -o "jsonpath={.status.networkConfig.domains[]['domain']}"

The output will look similar to:
    
    
    Getting Space some-space
    some-space.my-domain.com
    

Each Space prefixes the cluster domains with its own name. This prevents conflicts between Apps.

**Warning:** Updating the `spaceClusterDomain` in `config-defaults` will immediately be reflected on all Spaces and Apps that haven't overridden the domain.

## Space domains

Spaces are the authoritative location for domain configuration. You can assign domains and sub-domains to each space for developers to use. The field for configuring domains is `spec.networkConfig.domains`.

Use `kf space` to view the domains assigned to a Space:
    
    
    kf space SPACE_NAME

In the output, the `Spec` field contains specific configuration for the Space and the `Status` field reflects configuration for the Space with cluster-wide defaults appended to the end:
    
    
    ...
    Spec:
      Network Config:
        Domains:
          Domain: my-space.mycompany.com
    ...
    Status:
      Network Config:
        Domains:
          Domain: my-space.mycompany.com
          Domain: my-space.prod.us-east1.kf.mycompany.com
    

**Note:** Apps will use the **first** domain the status if developers don't specify a domain.

### Configuration with the CLI

The `kf` CLI supports mutations on Space domains. Each command outputs a diff between the old and new configurations.

Add a new domain with `kf configure-space append-domain`:
    
    
    kf configure-space append-domain SPACE_NAME myspace.mycompany.com

Add or make an existing domain the default with `kf configure-space set-default-domain`:
    
    
    kf configure-space set-default-domain SPACE_NAME myspace.mycompany.com

And finally, remove a domain:
    
    
    kf configure-space remove-domain SPACE_NAME myspace.mycompany.com

**Note:** You can override a cluster domains by inserting a new domain on the `spec` with the same `domain`. This ensures the space won't be updated if the cluster domain changes.

## Apps

Apps can specify domains as part of their configuration. Routes are mapped to Apps during `kf push` using the following logic:
    
    
    let current_routes  = The set of routes already on the app
    let manifest_routes = The set of routes defined by the manifest
    let flag_routes     = The set of routes supplied by the --route flag(s)
    let no_route        = Whether the manifest has no-route:true or --no-route is set
    let random_route    = Whether the manifest has random-route:true or --random-route is set
    
    let new_routes = Union(current_routes, manifest_routes, flag_routes)
    
    if new_routes.IsEmpty() then
      if random_route then
        new_routes.Add(CreateRandomRoute())
      else
        new_routes.Add(CreateDefaultRoute())
      end
    end
    
    if no_route then
      new_routes.RemoveAll()
    end
    
    return new_routes
    

If an App doesn't specify a Route, or requests a random Route, the first domain on the Space will be used. If the first domain on a Space changes, all Apps in the space using the default domain will be updated to reflect it.

## Domain templates

Kf supports variable substitution in domains. Substitution allows a single cluster-wide domain to be customized per-Space and to react to changes to the ingress IP. Substitution is performed on variables with the syntax `$(VARIABLE_NAME)` that occur in a domain.

Variable | Description  
---|---  
`CLUSTER_INGRESS_IP` | The IPV4 address of the cluster ingress.  
`SPACE_NAME` | The name of the Space.  
**Note:** Use the `SPACE_NAME` variable in domains to allow developers in different Spaces to avoid DNS conflicts if they push Apps with the same name.

### Examples

The following examples demonstrate how domain variables can be used to support a variety of different organizational structures and cluster patterns.

  * Using a wildcard DNS service like [nip.io](https://nip.io/):
        
        **$(SPACE_NAME)**.**$(CLUSTER_INGRESS_IP)**.nip.io
        

  * Domain for an organization with centrally managed DNS:
        
        **$(SPACE_NAME)**.cluster-name.example.com
        

  * Domain for teams who manage their own DNS:
        
        cluster-name.**$(SPACE_NAME)**.example.com
        

  * Domain for a cluster with warm failover and external circuit breaker:
        
        **$(SPACE_NAME)** -failover.cluster-name.example.com
        




## Differences between Kf and CF

  * Kf Spaces prefix the cluster-wide domain with the Space name.
  * Kf does not check for domain conflicts on user-specified routes.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
