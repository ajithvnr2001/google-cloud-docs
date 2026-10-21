---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management/
title: Configure advanced traffic management with proxyless gRPC services \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:45.348227+00:00
---

# Configure advanced traffic management with proxyless gRPC services  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure advanced traffic management with proxyless gRPC services

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This configuration is supported for Preview customers but we don't recommended it for new Cloud Service Mesh users. For more information, see the [Cloud Service Mesh service routing overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview).

This document provides instructions for configuring Cloud Service Mesh with the following traffic management features:

  * Route matching
  * Traffic splitting
  * Circuit breaking
  * Fault injection
  * Max stream duration
  * Retry
  * Session affinity
  * Outlier detection
  * Locality load balancing



While this document focuses on setting up advanced traffic management with proxyless gRPC on Compute Engine, advanced traffic management is also supported when you use proxyless gRPC on Google Kubernetes Engine (GKE).

## Before you begin

Before you configure advanced traffic management, review the requirements in [Prepare to set up Cloud Service Mesh with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/docs/service-routing/prepare-proxyless-grpc). You can't configure advanced traffic management unless all the requirements are met.

For conceptual information about these features, see [Advanced traffic management](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management).

## About the gRPC Wallet example

To illustrate these features, you deploy a gRPC Wallet example. In this example there are three gRPC services, `grpc.examples.wallet.Wallet`, `grpc.examples.wallet.stats.Stats`, and `grpc.examples.wallet.account.Account`, that are deployed as three separate applications.

As shown in the following diagram, you create a gRPC client that calls the `Wallet` service to get the balance of an account and calls the `Stats` service to get the price of a coin. The `Wallet` service calls the `Stats` and the `Account` services to calculate the balance. The `Stats` service also calls the `Account` service to get user information.

[ ![Example gRPC Wallet traffic routing configuration.](https://docs.cloud.google.com/static/service-mesh/docs/images/proxyless-traffic-example.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/proxyless-traffic-example.svg) Example gRPC Wallet traffic routing configuration (click to enlarge)

In the example, you deploy two versions of the `Wallet` and `Stats` implementations to illustrate request routing based on rules that you configure. To simulate building and deploying different versions of a service, you use server flags to change the behavior of binaries that you build only once.

  * The `--port` flag specifies the port on which the service on a VM instance listens.
  * The `--hostname_suffix` flag specifies a value that is appended to the hostname of the VM instance that responds to a request. The resulting value is added as the `hostname` metadata in the response. This helps you identify which instance in an instance group responded to the client request.
  * The `--premium_only` flag with the value `true` specifies that the service is a premium version of the `stats` service.
  * The `--v1_behavior` flag with the value `true` specifies that the wallet binary behaves as a v1 version.



The following table shows the values of these flags for each VM instance that is running one of the gRPC services, the number of instances in an instance group, and the backend services that these instance groups belong to.

**Note:** For brevity, the common prefix and suffix in the names of the backend services and instance groups are not shown. For example, `grpcwallet-wallet-v1-service` backend service is shown as `wallet-v1`.Backend service | Instance group | Instances | Server flags  
---|---|---|---  
`account` | `account` | 2 | `--port=50053`  
`--hostname_suffix="account"`  
`stats` | `stats` | 2 | `--port=50052`  
`--hostname_suffix="stats"`  
`--account_server="xds:///account.grpcwallet.io"`  
`stats-premium` | `stats-premium` | 2 | `--port=50052`  
`--hostname_suffix="stats_premium"`  
`--account_server="xds:///account.grpcwallet.io"`  
`--premium_only=true`  
`wallet-v1`  
`wallet-v1-affinity` | `wallet-v1` | 2 | `--port=50051`  
`--hostname_suffix="wallet_v1"`  
`--v1_behavior=true`  
`--account_server="xds:///account.grpcwallet.io"`  
`--stats_server="xds:///stats.grpcwallet.io"`  
`wallet-v2` | `wallet-v2` | 1 | `--port=50051`  
`--hostname_suffix "wallet_v2"`  
`--account_server="xds:///account.grpcwallet.io"`  
`--stats_server="xds:///stats.grpcwallet.io"`  
  
After you deploy these services, you configure Cloud Service Mesh to route requests to these backend services from a test client, based on the routing rules in the following table. The client connects to the virtual hostname of a service, as shown in the Host column.

**Note:** The HTTP/2 `:path` pseudo-header in a gRPC request is of the format `/ServiceName/MethodName` where `ServiceName` is the name of the gRPC service being called in the gRPC request and `MethodName` is the method in that service.Host | Match rules | Route action  
---|---|---  
`wallet.grpcwallet.io` | Path prefix: `"/"`  
Header present: `"session_id"` | Route to `wallet-v1-affinity`  
| Path prefix: `"/"`  
Header: `{"route": "timeout"}` | Set 5-second timeout and  
route to `wallet-v2`  
| Path prefix: `"/"`  
Header: `{"route": "fault"}` | Fail 50% requests and  
route the rest to `wallet-v2`  
| Path prefix: `"/"`  
Header: `{"membership": "premium"}` | Route to `wallet-v1` and  
retry up to 3 times on failure   
| Full path: `/grpc.examples.wallet.Wallet/FetchBalance` | Route to:  
`wallet-v1`: 70%  
`wallet-v2`: 30%   
| Default | Route to `wallet-v1`  
`stats.grpcwallet.io` | Path prefix: `"/"`  
Header: `{"membership": "premium"}` | Route to `stats-premium`  
| Default | Route to `stats`  
`account.grpcwallet.io` | Path prefix: `"/"`  
Header: `{"route": "account-fault"}` | Fail 30% requests and  
route the rest to `account`  
| Default | `account`  
  
This example uses a 70/30 traffic split between two existing services. If you are splitting traffic to a new service that has not been referenced by the URL map before, first add the new service to `weightedBackendServices` and give it a weight of `0`. Then, gradually increase the weight assigned to that service.

The test client has the following options that allow you to generate appropriate requests to demonstrate the traffic management features.

Option | Description  
---|---  
`--watch=true` | Call streaming methods to watch balance/price  
`--unary_watch=true` | Call unary methods repeatedly to watch balance/price  
`--user=Alice` | Inject header `{"membership": "premium"}`  
`--user=Bob` | Inject header `{"membership": "normal"}`  
`--route=_value_` | Inject header `{"route": "_value_ "}`  
`--affinity=true` | Inject header `{"session_id": "_value_ "}`  
  
## Prepare your local environment

To set up the local environment for these examples, run the following commands:

  1. Update the `gcloud` binary to ensure that you have the latest version:
         
         gcloud components update
         

  2. Download the examples repository:
         
         sudo apt-get install git -y
         

  3. Clone the correct repository for the example:
         
         export EXAMPLES_VERSION=v1.1.x
         git clone -b $EXAMPLES_VERSION --single-branch --depth=1 \
           https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples.git
         




## Create and configure Cloud Router instances

In this section, you create Cloud Router instances in each region and configure them for Cloud NAT. The VMs created by this example don't have external IP addresses, but they need to have access to the internet. Configuring Cloud Router with Cloud NAT provides the required access.

###  gcloud 

  1. Create the Cloud Router instances:
         
         gcloud compute routers create nat-router-us-central1 \
             --network=default \
             --region=us-central1
         

  2. Configure the routers for Cloud NAT:
         
         gcloud compute routers nats create nat-config \
             --router-region=us-central1 \
             --router=nat-router-us-central1 \
             --nat-all-subnet-ip-ranges \
             --auto-allocate-nat-external-ips
         




## Create the gRPC health check and firewall rule

In this section, you create a gRPC health check and a firewall rule to allow gRPC health check requests to reach your network. Later, the gRPC health check is associated with backend services so that it can check the health of the backend instances of those backend services.

###  gcloud 

  1. Create the health check:
         
         gcloud compute health-checks create grpc grpcwallet-health-check \
             --use-serving-port
         

  2. Create the firewall rule for the health check:
         
         gcloud compute firewall-rules create grpcwallet-allow-health-checks \
             --network default --action allow --direction INGRESS \
             --source-ranges 35.191.0.0/16,130.211.0.0/22 \
             --target-tags allow-health-checks \
             --rules tcp:50051-50053
         




## Create the instance template

In this section, you create an instance template to deploy the `account` gRPC service that is exposed on port `50053`.

###  gcloud 

  * Create the instance template:
        
        gcloud compute instance-templates create grpcwallet-account-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=allow-health-checks \
           --network-interface=no-address \
           --image-family=debian-10 \
           --image-project=debian-cloud \
           --metadata-from-file=startup-script=<(echo "#! /bin/bash
        set -ex
        cd /root
        export HOME=/root
        sudo apt-get update -y
        pushd \$(mktemp -d)
        sudo apt-get install -y wget git
        wget https://dl.google.com/go/go1.16.5.linux-amd64.tar.gz
        sudo tar -C /usr/local -xvf go1.16.5.linux-amd64.tar.gz
        sudo cp /usr/local/go/bin/go /usr/bin/go
        popd
        git clone -b $EXAMPLES_VERSION --single-branch --depth=1 https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples.git
        cd traffic-director-grpc-examples/go/account_server/
        go build .
        sudo systemd-run ./account_server --port 50053 --hostname_suffix account")
        




## Create the managed instance group

Managed instance groups (MIGs) use autoscaling to create new VM instances as needed. In this section, you create a MIG by using the instance template that you created in the previous section.

###  gcloud 

  * Create the instance group:
        
        gcloud compute instance-groups managed create grpcwallet-account-mig-us-central1 \
           --zone=us-central1-a \
           --size=2 \
           --template=grpcwallet-account-template
        




## Configure the named port

In this section, you configure the named port for the gRPC service. The named port is the port on which the gRPC service listens for requests. In this example, the named port is port `50053`.

###  gcloud 

  * Create the named port:
        
        gcloud compute instance-groups set-named-ports grpcwallet-account-mig-us-central1 \
           --named-ports=grpcwallet-account-port:50053 \
           --zone=us-central1-a
        




## Create the backend service

In this section, you create a global [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load-balancing scheme of `INTERNAL_SELF_MANAGED` and protocol `GRPC`. You then associate the health check and instance group with the backend service. In this example, you use the MIG that you created in Create the managed instance group. This MIG runs the `account` gRPC service. The port in the `--port-name` flag is the named port that you created in Configure the named port.

###  gcloud 

  1. Create the backend service, and then associate the health check with the new backend service:
         
         gcloud compute backend-services create grpcwallet-account-service \
             --global \
             --load-balancing-scheme=INTERNAL_SELF_MANAGED \
             --protocol=GRPC \
             --port-name=grpcwallet-account-port \
             --health-checks=grpcwallet-health-check
         

  2. Add the managed instance group as the backend:
         
         gcloud compute backend-services add-backend grpcwallet-account-service \
             --instance-group=grpcwallet-account-mig-us-central1 \
             --instance-group-zone=us-central1-a \
             --global
         




The steps to create the remaining backend services used in the gRPC Wallet example are similar to the preceding steps. You create the remaining services by running a shell script. The script deploys the following backend services:

  * `stats`
  * `stats-premium`
  * `wallet-v1`
  * `wallet-v1-affinity`
  * `wallet-v2`



Run the shell script that creates the additional backend services:
    
    
    traffic-director-grpc-examples/scripts/create_service.sh go stats 50052 stats '--account_server="xds:///account.grpcwallet.io"'
    
    traffic-director-grpc-examples/scripts/create_service.sh go stats 50052 stats-premium '--account_server="xds:///account.grpcwallet.io" --premium_only=true'
    
    # This command creates wallet-v1 and wallet-v1-affinity backend services.
    traffic-director-grpc-examples/scripts/create_service.sh java wallet 50051 wallet-v1 '--account_server="xds:///account.grpcwallet.io" --stats_server="xds:///stats.grpcwallet.io" --v1_behavior=true'
    
    traffic-director-grpc-examples/scripts/create_service.sh java wallet 50051 wallet-v2 '--account_server="xds:///account.grpcwallet.io" --stats_server="xds:///stats.grpcwallet.io"'
    

## Create the routing rules

In this section, you create a URL map that is used to demonstrate various traffic management features. The URL map specifies the virtual hostnames of the services in this example and the associated routing rules. For more information, see [Routing rule maps](https://docs.cloud.google.com/service-mesh/docs/service-routing/routing-rule-maps).

In the URL map, the `hostRules` specify the virtual hostnames of the services in the example. These are the names that a client uses in the channel URI to connect to a specific service. For example, to send a request to the `account` service, a client uses `xds:///account.grpcwallet.io` in the channel URI. In the `hostRules`, configure a `hosts` entry with the value `account.grpcwallet.io`.

The `pathMatcher` associated with a `hosts` entry specifies the name of a `pathMatcher` that contains all the routing rules for that virtual host. A `pathMatcher` configuration consists of matching rules and corresponding action rules as described in About the gRPC Wallet example.

###  gcloud 

Create the URL map:
    
    
    export PROJECT_ID=$(gcloud config list --format 'value(core.project)')
    export BS_PREFIX=projects/$PROJECT_ID/global/backendServices/grpcwallet
    
    gcloud compute url-maps import grpcwallet-url-map << EOF
    name: grpcwallet-url-map
    defaultService: $BS_PREFIX-account-service
    
    hostRules:
    - hosts:
      - account.grpcwallet.io
      pathMatcher: grpcwallet-account-path-matcher
    - hosts:
      - stats.grpcwallet.io
      pathMatcher: grpcwallet-stats-path-matcher
    - hosts:
      - wallet.grpcwallet.io
      pathMatcher: grpcwallet-wallet-path-matcher
    
    pathMatchers:
    - name: grpcwallet-account-path-matcher
      defaultService: $BS_PREFIX-account-service
      routeRules:
      - matchRules:
        - prefixMatch: /
          headerMatches:
          - headerName: route
            exactMatch: account-fault
        priority: 0
        routeAction:
          weightedBackendServices:
          - backendService: $BS_PREFIX-account-service
            weight: 100
          faultInjectionPolicy:
            abort:
              httpStatus: 503
              percentage: 30
    
    - name: grpcwallet-stats-path-matcher
      defaultService: $BS_PREFIX-stats-service
      routeRules:
      - matchRules:
        - prefixMatch: /
          headerMatches:
          - headerName: membership
            exactMatch: premium
        priority: 0
        service: $BS_PREFIX-stats-premium-service
    
    - name: grpcwallet-wallet-path-matcher
      defaultService: $BS_PREFIX-wallet-v1-service
      routeRules:
      - matchRules:
        - prefixMatch: /
          headerMatches:
          - headerName: session_id
            presentMatch: true
        priority: 0
        routeAction:
          weightedBackendServices:
          - backendService: $BS_PREFIX-wallet-v1-affinity-service
            weight: 100
    
      - matchRules:
        - prefixMatch: /
          headerMatches:
          - headerName: route
            exactMatch: timeout
        priority: 1
        routeAction:
          weightedBackendServices:
          - backendService: $BS_PREFIX-wallet-v2-service
            weight: 100
          maxStreamDuration:
            seconds: 5
    
      - matchRules:
        - prefixMatch: /
          headerMatches:
          - headerName: route
            exactMatch: fault
        priority: 2
        routeAction:
          weightedBackendServices:
          - backendService: $BS_PREFIX-wallet-v2-service
            weight: 100
          faultInjectionPolicy:
            abort:
              httpStatus: 503
              percentage: 50
    
      - matchRules:
        - prefixMatch: /
          headerMatches:
          - headerName: membership
            exactMatch: premium
        priority: 3
        routeAction:
          weightedBackendServices:
          - backendService: $BS_PREFIX-wallet-v1-service
            weight: 100
          retryPolicy:
            retryConditions:
              - unavailable
            numRetries: 3
    
      - matchRules:
        - fullPathMatch: /grpc.examples.wallet.Wallet/FetchBalance
        priority: 4
        routeAction:
          weightedBackendServices:
          - backendService: $BS_PREFIX-wallet-v1-service
            weight: 70
          - backendService: $BS_PREFIX-wallet-v2-service
            weight: 30
    
      - matchRules:
        - prefixMatch: /grpc.examples.wallet.Wallet/
        priority: 5
        routeAction:
          weightedBackendServices:
          - backendService: $BS_PREFIX-wallet-v2-service
            weight: 100
    EOF
    

## Create the target proxy and forwarding rule

In this section, you create the target gRPC proxy and a forwarding rule.

The target gRPC proxy references the URL map that you created in the previous step. The flag `--validate-for-proxyless` enables configuration checks so that you don't accidentally enable a feature that is not compatible with proxyless gRPC deployments.

###  gcloud 

  * Create the target gRPC proxy:
        
        gcloud compute target-grpc-proxies create grpcwallet-proxy \
           --url-map=grpcwallet-url-map \
           --validate-for-proxyless
        




The forwarding rule references the target gRPC proxy that you created. The load-balancing scheme is set to `INTERNAL_SELF_MANAGED` to indicate that this forwarding rule is used by Cloud Service Mesh. It must be a global forwarding rule. The IP address is set to `0.0.0.0` because a proxyless gRPC client resolves the `hostname:port` in the target URI by sending an [LDS](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/lds) request to Cloud Service Mesh instead of doing a DNS lookup. For more information, see [Name resolution scheme](https://docs.cloud.google.com/service-mesh/docs/service-routing/proxyless-overview#name_resolution_scheme).

When a port is not specified in the target URI, the default value is `80`. For example, a target URI `xds:///foo.myservice:8080` matches a forwarding rule that is configured with port `8080`. In this example, the forwarding rule is configured with port `80`.

###  gcloud 

  * Create the forwarding rule:
        
        gcloud compute forwarding-rules create grpcwallet-forwarding-rule \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --address=0.0.0.0 \
           --address-region=us-central1 \
           --target-grpc-proxy=grpcwallet-proxy \
           --ports=80 \
           --network=default
        




## Verify the configuration

When the configuration process is complete, verify that the backend services that you configured are available by checking the [Cloud Service Mesh page in the Google Cloud console](https://console.cloud.google.com/net-services/trafficdirector/services/list?_ga=2.16860793.1925980301.1594086051-345140609.1594076710). Confirm that the backend services and associated backends are reported as healthy. This may take several minutes.

### Verify the routing configuration

In this section, you verify that the routing configuration is working correctly. You use the `grpcurl` tool to test the configuration.

###  gcloud 

  1. Create a client VM on which you run the clients to test the service. You can optionally include the `--network-interface=no-address` flag.
         
         gcloud compute instances create grpc-wallet-client \
             --zone=us-central1-a \
             --scopes=https://www.googleapis.com/auth/cloud-platform \
             --image-family=debian-10 \
             --image-project=debian-cloud \
             --metadata-from-file=startup-script=<(echo '#! /bin/bash
         set -e
         export GRPC_XDS_BOOTSTRAP=/run/td-grpc-bootstrap.json
         # Expose bootstrap variable to SSH connections
         echo export GRPC_XDS_BOOTSTRAP=$GRPC_XDS_BOOTSTRAP | sudo tee /etc/profile.d/grpc-xds-bootstrap.sh
         # Create the bootstrap file
         curl -L https://storage.googleapis.com/traffic-director/td-grpc-bootstrap-0.19.0.tar.gz | tar -xz
         ./td-grpc-bootstrap-0.19.0/td-grpc-bootstrap | sudo tee $GRPC_XDS_BOOTSTRAP')
         

  2. Access the VM using SSH and run the following commands to prepare the VM:
         
         export EXAMPLES_VERSION=v1.1.x
         sudo apt-get update
         sudo apt-get install git -y
         

  3. Run the following commands:
         
         git clone -b $EXAMPLES_VERSION --single-branch --depth=1 \
            https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples.git
         curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.6.1/grpcurl_1.6.1_linux_x86_64.tar.gz | tar -xz
         chmod +x grpcurl
         




To access the services without a sidecar proxy, the gRPC client needs to use the `xds` name resolution scheme. This scheme tells the gRPC library used in the client to use an xDS server to resolve the hostname. To do this, a bootstrap configuration is required.

The startup script in the previous section sets the `GRPC_XDS_BOOTSTRAP` environment variable and uses a helper script to generate the bootstrap file. The values for `TRAFFICDIRECTOR_GCP_PROJECT_NUMBER`, `TRAFFICDIRECTOR_NETWORK_NAME`, and zone in the generated bootstrap file are obtained from the metadata server that knows these details about your Compute Engine VM instances. You can provide these values to the helper script manually by using the `-gcp-project-number` and `-vpc-network-name` options.

**Note:** Per policy, we encourage users to check for updates of the TD gRPC bootstrap generator yearly.

### Verify the configuration using the `grpcurl` tool

Run the following commands in the SSH shell to verify that the `wallet-service`, `stats-service`, and `account-service` are running:
    
    
    ./grpcurl -plaintext xds:///account.grpcwallet.io list
    ./grpcurl -plaintext -d '{"token": "2bd806c9"}' xds:///account.grpcwallet.io grpc.examples.wallet.account.Account/GetUserInfo
    ./grpcurl -plaintext -H 'authorization:2bd806c9' -H 'membership:premium' xds:///stats.grpcwallet.io grpc.examples.wallet.stats.Stats/FetchPrice
    ./grpcurl -plaintext -H 'authorization:2bd806c9' -H 'membership:premium' -d '{"include_balance_per_address": true}' xds:///wallet.grpcwallet.io grpc.examples.wallet.Wallet/FetchBalance
    

You see the following results:
    
    
    grpc.examples.wallet.account.Account
    grpc.health.v1.Health
    grpc.reflection.v1alpha.ServerReflection
    
    {
      "name": "Alice",
      "membership": "PREMIUM"
    }
    
    {
      "price": "10295"
    }
    
    {
      "balance": "5089953"
    }
    

### Verify with `grpc-wallet` clients

Use the following language-specific instructions to verify the configuration. The commands send multiple RPCs, some with extra metadata, to show that requests are routed to backend services based on the matching rules from the URL map. The command also prints the hostname of the VM instance for each response to show which VM instance the request was routed to.

###  Java 

  1. To verify the service with a gRPC Java client, run the following:
         
         sudo apt-get install -y openjdk-11-jdk-headless
         

  2. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/java
         ./gradlew installDist
         
         # This command calls 'FetchBalance' from 'wallet-service' in a loop,
         # to demonstrate that 'FetchBalance' gets responses from 'wallet-v1' (70%)
         # and 'wallet-v2' (30%).
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Bob
         
         # This command calls the streaming RPC 'WatchBalance' from 'wallet-service'.
         # The RPC path matches the service prefix, so all requests are
         # sent to 'wallet-v2'.
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob
         
         # This command calls 'WatchPrice' from 'stats-service'. It sends the
         # user's membership (premium or not) in metadata. Premium requests are
         # all sent to 'stats-premium' and get faster responses. Alice's requests
         # always go to premium and Bob's go to regular.
         ./build/install/wallet/bin/client price --stats_server="xds:///stats.grpcwallet.io" --watch=true --user=Bob
         ./build/install/wallet/bin/client price --stats_server="xds:///stats.grpcwallet.io" --watch=true --user=Alice
         




###  Go 

  1. To verify the service with a gRPC Go client, install golang or follow [the official instructions](https://golang.org/doc/install):
         
         sudo apt-get install -y wget
         wget https://dl.google.com/go/go1.16.5.linux-amd64.tar.gz
         sudo tar -C /usr/local -xvf go1.16.5.linux-amd64.tar.gz
         sudo ln -s /usr/local/go/bin/go /usr/bin/go
         

  2. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/go/wallet_client
         go build
         
         # This command calls 'FetchBalance' from 'wallet-service' in a loop,
         # to demonstrate that 'FetchBalance' gets responses from 'wallet-v1' (70%)
         # and 'wallet-v2' (30%).
         ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch --user=Bob
         
         # This command calls the streaming RPC 'WatchBalance' from 'wallet-service'.
         # The RPC path matches the service prefix, so all requests
         # are sent to 'wallet-v2'.
         ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch --user=Bob
         
         # This command calls 'WatchPrice' from 'stats-service'. It sends the
         # user's membership (premium or not) in metadata. Premium requests are
         # all sent to 'stats-premium' and get faster responses. Alice's requests
         # always go to premium and Bob's go to regular.
         ./wallet_client price --stats_server="xds:///stats.grpcwallet.io" --watch --user=Bob
         ./wallet_client price --stats_server="xds:///stats.grpcwallet.io" --watch --user=Alice
         




###  C++ 

  1. To verify the service with a gRPC C++ client, run the following:
         
         sudo apt-get install -y build-essential
         

  2. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/cpp
         ../tools/bazel build :client
         
         # This command calls 'FetchBalance' from 'wallet-service' in a loop,
         # to demonstrate that 'FetchBalance' gets responses from 'wallet-v1' (70%)
         # and 'wallet-v2' (30%).
         ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Bob
         
         # This command calls the streaming RPC 'WatchBalance'  from 'wallet-service'.
         # The RPC path matches the service prefix, so all requests are sent to 'wallet-v2'.
         ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob
         
         # This command calls 'WatchPrice' from 'stats-service'. It sends the
         # user's membership (premium or not) in metadata. Premium requests are
         # all sent to 'stats-premium' and get faster responses. Alice's requests
         # always go to premium, and Bob's go to regular.
         ../bazel-bin/cpp/client price --stats_server="xds:///stats.grpcwallet.io" --watch=true --user=Bob
         ../bazel-bin/cpp/client price --stats_server="xds:///stats.grpcwallet.io" --watch=true --user=Alice
         




## Configure more advanced options

You can configure additional advanced traffic routing options by using the instructions in the following sections.

### Circuit breaking

Circuit breaking lets you set failure thresholds to prevent client requests from overloading your backend services. After the number of outstanding requests reach a limit that you set, the client stops sending additional requests, giving your backend services time to recover.

Circuit breaking prevents cascading failures by returning an error to the client rather than overloading a backend service. This allows some traffic to be served while providing time for managing the overload situation, such as handling a traffic spike by increasing capacity through autoscaling.

When you create the backend service for the `stats-service`, the `create_service.sh` script includes the following lines in its configuration:
    
    
    circuitBreakers:
      maxRequests: 1
    

This setting limits clients to one pending request to the `stats-service` at a time. Because there is only one `wallet-v2` service, running two concurrent wallet client `WatchBalance` operations exhibits failures from the second instance.

###  Java 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/java
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob  2>/dev/null 1>/dev/null &
         
         sleep 10 # Wait a few seconds to allow the watch to begin.
         
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob
         

  2. The output looks like the following:
         
         io.grpc.examples.wallet.Client run
         INFO: Will try to run balance
         io.grpc.examples.wallet.Client run
         WARNING: RPC failed: Status{code=INTERNAL, description=RPC to stats server failed: UNAVAILABLE: Cluster max concurrent requests limit exceeded, cause=null}
         

  3. Issue the `kill` command:
         
         kill %%
         




###  Go 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/go/wallet_client
         ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch --user=Bob 2> /dev/null 1> /dev/null &
         
         sleep 10 # Wait a few seconds to allow the watch to begin.
         
         ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch --user=Bob
         

  2. The output looks like the following:
         
         server host: error: no hostname
         failed to fetch balance: rpc error: code = Internal desc = RPC to stats server failed:
         UNAVAILABLE: Cluster max concurrent requests limit exceeded
         

  3. Issue the `kill` command:
         
         kill %%
         




###  C++ 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/cpp
         ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob 2>/dev/null 1>/dev/null &
         
         sleep 10 # Wait a few seconds to allow the watch to begin.
         
         ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob
         

  2. The output looks like the following:
         
         Client arguments: command: balance, wallet_server: xds:///wallet.grpcwallet.io, stats_server:
         localhost:18882, user: Bob, watch: 1 ,unary_watch: 0, observability_project: , route:
         13: RPC to stats server failed: UNAVAILABLE: Cluster max concurrent requests limit exceeded
         

  3. Issue the `kill` command:
         
         kill %%
         




### Fault injection

Fault injection introduces errors when servicing requests to simulate failures, including high latency, service overload, service failures, and network partitioning. This feature is useful for testing the resiliency of a service to simulated faults.

When you created the URL map previously, you set the fault injection policy to fail 50% of the RPCs sent to `wallet.grpcwallet.io` with the `route=fault` header.

To demonstrate fault injection, use the code in the following languages.

###  Java 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/java
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Bob --route=fault
         

  2. The output looks like the following:
         
         server host: grpcwallet-wallet-v2-mig-us-central1-zznc
         total balance: 10340491
         - address: 148de9c5, balance: 2549839
         - address: 2e7d2c03, balance: 7790652
         io.grpc.examples.wallet.Client run
         WARNING: RPC failed: Status{code=UNAVAILABLE, description=RPC terminated due to fault injection: HTTP status code 503, cause=null}
         




###  Go 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/go/wallet_client
         ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch --user=Bob --route=fault
         

  2. The output looks like the following:
         
         server host: grpcwallet-wallet-v1-mig-us-central1-bm1t_wallet-v1
          user: Bob, total grpc-coin balance: 10452589.
           - address: 2e7d2c03, balance: 7875108.
           - address: 148de9c5, balance: 2577481.
          failed to fetch balance: rpc error: code = Unavailable desc = RPC terminated due to fault injection
         




###  C++ 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/cpp
         ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Bob --route=fault
         

  2. The output looks like the following:
         
         Client arguments: command: balance, wallet_server: xds:///wallet.grpcwallet.io,
         stats_server: localhost:18882, user: Bob, watch: 0 ,unary_watch: 1, observability_project: ,
         route: fault server host: grpcwallet-wallet-v2-mig-us-central1-1lm6
         user: Bob total grpc-coin balance: 10211908
          - address: 148de9c5, balance: 2518132
          - address: 2e7d2c03, balance: 7693776
         14: Fault injected
         




### Max stream duration

Max stream duration allows a maximum timeout to be applied to all RPCs. This prevents clients that forget to set a deadline, or that set an excessive deadline, from wasting server resources.

When you created the URL map previously, you set a max stream duration of 5 seconds for RPCs sent to `wallet.grpcwallet.io` with the `route=timeout` header.

To demonstrate timeouts, we first stop the `wallet-v2` service.

###  gcloud 
    
    
    gcloud compute instance-groups managed resize \
        --size=0 grpcwallet-wallet-v2-mig-us-central1 \
        --zone=us-central1-a
    

The following command would be stuck forever, because there is no backend service to handle it, and the application does not set a deadline.

###  Java 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/java
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob
         

  2. The command stops responding. Press ^C to interrupt the command.




###  Go 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/go/wallet_client
         ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch --user=Bob
         

  2. The command stops responding. Press ^C to interrupt the command.




###  C++ 

  1. Run the following commands:
         
         cd ~/traffic-director-grpc-examples/cpp
         ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob
         

  2. The command stops responding. Press ^C to interrupt the command.




However, the following command using the `timeout` route fails after 5 seconds because of the `maxStreamDuration` setting.

###  Java 

  1. Run the following command:
         
         cd ~/traffic-director-grpc-examples/java
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob --route=timeout
         

  2. The output looks like the following:
         
         io.grpc.examples.wallet.Client run
         WARNING: RPC failed: Status{code=DEADLINE_EXCEEDED, description=deadline exceeded after 4.999594070s.         [wait_for_ready, buffered_nanos=5000553401, waiting_for_connection], cause=null}
         




###  Go 

  1. Run the following command:
         
         cd ~/traffic-director-grpc-examples/go/wallet_client
         ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch --user=Bob --route=timeout
         

  2. The output looks like the following:
         
         failed to create stream: rpc error: code = DeadlineExceeded desc = context deadline exceeded.
         




###  C++ 

  1. Run the following command:
         
         cd ~/traffic-director-grpc-examples/cpp
         ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob --route=timeout
         

  2. The output looks like the following:
         
         Client arguments: command: balance, wallet_server: xds:///wallet.grpcwallet.io, stats_server:
         localhost:18882, user: Bob, watch: 1 ,unary_watch: 0, observability_project: , route: timeout
         4: Deadline Exceeded
         




Restart the `wallet-v2` service.

###  gcloud 
    
    
    gcloud compute instance-groups managed resize \
        --size=1 grpcwallet-wallet-v2-mig-us-central1 \
        --zone=us-central1-a
    

### Retry

Retries help you improve service availability by enabling your gRPC applications to retry outbound requests according to a retry policy. In a retry policy, you can configure the conditions under which a failed request should be retried and the maximum number of retry attempts—for example, when a request fails with a particular response code.

When you created the URL map previously, you set a retry policy for RPCs to the `FetchBalance` method with the `membership=premium` header. This policy retries RPCs that fail with status code `unavailable` up to a maximum of 3 times. You also set a fault injection policy for RPCs to `account.grpcwallet.io` with the `route=account-fault` header that fails 30% of the RPCs from the `Wallet` service to the `Account` service. As a result, 30% of the RPCs from the test client with `membership=normal` header fail, whereas the failure rate for the RPCs with `membership=premium` header is less than 1%.

To demonstrate retries, use the code in the following languages.

###  Java 

Run the following commands:
    
    
    cd ~/traffic-director-grpc-examples/java
    # 30% of the requests fail because Bob is a normal user.
    ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Bob --route=account-fault
    # Less than 1% of the requests fail because Alice is a premium user.
    ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice --route=account-fault
    

###  Go 

Run the following commands:
    
    
    cd ~/traffic-director-grpc-examples/go/wallet_client
    # 30% of the requests fail because Bob is a normal user.
    ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Bob --route=account-fault
    # Less than 1% of the requests fail because Alice is a premium user.
    ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice --route=account-fault
    

###  C++ 

Run the following commands:
    
    
    cd ~/traffic-director-grpc-examples/cpp
    # 30% of the requests fail because Bob is a normal user.
    ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Bob --route=account-fault
    # Less than 1% of the requests fail because Alice is a premium user.
    ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice --route=account-fault
    

### Session affinity

Session affinity provides a best-effort attempt to send requests with particular characteristics (HTTP headers) to the same instance for as long as the instance is healthy and has capacity. This is useful for stateful application servers that benefit from improved performance and efficiency when requests from a particular client are sent to the same instance instead of, for example, round-robin distribution to different instances.

**Note:** A gRPC client that does not support RING_HASH load balancing policy will negative acknowledge the configuration from Cloud Service Mesh when a URL map references a backend service with `localityLbPolicy=RING_HASH`. This will cause the client channel to go into a transient error state until the configuration is fixed. See [Backend service limitation](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/limitations-proxyless#backend-service-limitations) for more details.

When you created the backend service `grpcwallet-wallet-v1-affinity-service`, in the `create_service.sh` script, the `localityLbPolicy` was set to `ROUND_ROBIN`. In this example, you will apply the following configuration to change the `localityLbPolicy` to `RING_HASH`.
    
    
    sessionAffinity: HEADER_FIELD
    localityLbPolicy: RING_HASH
    consistentHash:
      httpHeaderName: "session_id"
    

###  gcloud 

  1. Save the configuration of the backend service `grpcwallet-wallet-v1-affinity-service`:
         
         gcloud compute backend-services export grpcwallet-wallet-v1-affinity-service \
          --destination=bs_config.yaml \
          --global
         

  2. Update the backend service `grpcwallet-wallet-v1-affinity-service`:
         
         project_id="$(gcloud config list --format 'value(core.project)')"
         backend_config="
         backends:
         - balancingMode: UTILIZATION
           capacityScaler: 1.0
           group: projects/${project_id}/zones/us-central1-a/instanceGroups/grpcwallet-wallet-v1-mig-us-central1
         connectionDraining:
           drainingTimeoutSec: 0
         healthChecks:
         - projects/${project_id}/global/healthChecks/grpcwallet-health-check
         loadBalancingScheme: INTERNAL_SELF_MANAGED
         name: grpcwallet-wallet-v1-affinity-service
         portName: grpcwallet-wallet-port
         protocol: GRPC
         sessionAffinity: HEADER_FIELD
         localityLbPolicy: RING_HASH
         consistentHash:
           httpHeaderName: session_id"
         gcloud compute backend-services import grpcwallet-wallet-v1-affinity-service --global <<< "${backend_config}"
         




**Note:** The backend service update may take several minutes to propagate to the clients.

To demonstrate session affinity, use the code in the following languages. With the flag `--affinity=true`, the client inserts a header `session-id` with a unique value for each user. A hash of this value is used to send the request to a particular instance in the instance group of the backend service `grpcwallet-wallet-v1-affinity-service`.

###  Java 

Run the following commands:
    
    
    cd ~/traffic-director-grpc-examples/java
    # Without affinity, requests are sent to both instances.
    ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice
    # With affinity, requests are sent to only one instance.
    ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice --affinity=true
    

###  Go 

Run the following commands:
    
    
    cd ~/traffic-director-grpc-examples/go/wallet_client
    # Without affinity, requests are sent to both instances.
    ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice
    # With affinity, requests are sent to only one instance.
    ./wallet_client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice --affinity=true
    

###  C++ 

Run the following commands:
    
    
    cd ~/traffic-director-grpc-examples/cpp
    # Without affinity, requests are sent to both instances.
    ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice
    # With affinity, requests are sent to only one instance.
    ../bazel-bin/cpp/client balance --wallet_server="xds:///wallet.grpcwallet.io" --unary_watch=true --user=Alice --affinity=true
    

Restore the configuration of the backend service `grpcwallet-wallet-v1-affinity-service`.

###  gcloud 
    
    
    gcloud compute backend-services import grpcwallet-wallet-v1-affinity-service \
      --source=bs_config.yaml \
      --global
    

### Outlier detection

To improve service availability, configure outlier detection. This feature lets you identify and temporarily eject unhealthy hosts from the load-balancing pool. These unhealthy hosts are called _outliers_.

gRPC evaluates hosts based on success rate—the frequency with which a host successfully handles requests. The rate is affected by failures such as gRPC errors, HTTP errors, timeouts, and other problems.

When you configure outlier detection through Cloud Service Mesh, you can fine-tune how gRPC assesses hosts and how it handles outliers. For example, you can specify criteria such as the following:

  * The number of requests that a host must receive before gRPC analyzes it for possible outlier status.

  * The extent to which a host can deviate from the mean success rate before it's considered an outlier.

  * The maximum percentage of hosts that can be ejected at any one time from the load-balancing pool.

  * The amount of time for which an outlier is excluded from the load-balancing pool.




For more information about the available parameters, see the [`REST Resource: backendServices`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) reference. However, some limitations exist for gRPC, as described in the following section.

#### Limitations

The following fields are not supported for gRPC clients:

  * `outlierDetection.consecutiveErrors`

  * `outlierDetection.enforcingConsecutiveErrors`

  * `outlierDetection.consecutiveGatewayFailure`

  * `outlierDetection.enforcingConsecutiveGatewayFailure`




#### Set up outlier detection

The following procedure shows how to configure outlier detection for a service that uses one instance group as its backend. This procedure establishes the following configuration:

  * Outlier-detection analysis runs every second. You configure this behavior by using the `interval` field.
  * Outliers are ejected from the load-balancing pool for increments of 30 seconds, as follows: 
    * If a host has never been previously ejected, it's ejected for only 30 seconds.
    * If a host has been previously ejected, the time increases by 30 seconds for each previous ejection. For example, when a host is ejected for a third time, it's ejected for 90 seconds. You configure this behavior by using the `baseEjectionTime` field.
  * A host is considered unhealthy if its success rate is one standard deviation under average during the selected time interval (in this case, 1 second). You configure the maximum standard deviation by using the `successRateStdevFactor` field.



To configure outlier detection in this way, use the following steps.

###  gcloud 

  1. Export the `grpcwallet-wallet-v2-service` backend service configuration file by using the [`gcloud compute backend-services export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/export) command:
         
         gcloud compute backend-services export grpcwallet-wallet-v2-service \
          --destination=bs_config.yaml \
          --global
         

  2. In the `bs_config.yaml` file, update the `grpcwallet-wallet-v2-service` configuration to include the outlier detection fields:
         
         outlierDetection:
          interval:
            seconds: 1
            nanos: 0
          baseEjectionTime:
            seconds: 30
            nanos: 0
          successRateStdevFactor: 1000
         

  3. Import the updated file by using the [`gcloud compute backend-services import`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/import) command:
         
         gcloud compute backend-services import grpcwallet-wallet-v2-service \
          --source=bs_config.yaml \
          --global




**Note:** The Wallet example is not designed to include unhealthy hosts. For that reason, `grpcwallet-wallet-v2-service` hosts typically are not removed, even if you configure outlier detection correctly.

### Locality load balancing

To make the most efficient use of your resources, configure locality load balancing. This feature helps you conserve resources by evenly distributing client requests across your backends.

When you configure locality load balancing, you can use the options described in the following table. All options require you to configure the [`backendServices`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) resource.

Option | Available for | Relevant configuration field  
---|---|---  
Use a built-in policy | All gRPC clients | `localityLbPolicy`  
Use a custom policy | Java clients that use gRPC version 1.47 or later, in a mesh that includes only gRPC clients  | `localityLbPolicies`  
Define a list of preferred policies | Java clients that use gRPC version 1.47 or later, in a mesh that includes only gRPC clients  | `localityLbPolicies`  
  
You can use any combination of the preceding options. However, if you configure both `localityLbPolicy` and `localityLbPolicies`, gRPC first tries to use your `localityLbPolicies` configuration.

If you don't configure locality load balancing, Cloud Service Mesh uses the `ROUND_ROBIN` policy.

For information about `ROUND_ROBIN` and other built-in policies, see the description of `localityLbPolicy` on the [`backendServices`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) page.

#### Use a built-in policy

If you want all of your clients to use a single built-in policy, you can select it by configuring the `localityLbPolicy` field.

When you configure this field, you can choose from the following policies:

  * `LEAST_REQUEST` (Java clients only)
  * `RING_HASH`
  * `ROUND_ROBIN`



If not all of your clients can use the same policy, see Define a list of preferred policies.

###  gcloud 

  1. Export the `grpcwallet-wallet-v2-service` backend service configuration file by using the [`gcloud compute backend-services export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/export) command:
         
         gcloud compute backend-services export grpcwallet-wallet-v2-service \
         --destination=bs_config.yaml \
         --global
         

  2. Update the exported `bs_config.yaml` file to include the following lines:
         
         localityLbPolicy:
          -- policy
             name: RING_HASH
         

  3. Import the updated file by using the [gcloud compute backend-services import](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/import) command:
         
         gcloud compute backend-services import grpcwallet-wallet-v2-service --source=bs_config.yaml --global
         




#### Use a custom policy

If appropriate, you can use a custom load-balancing policy that you created and deployed with gRPC. This feature is available for Java clients that use gRPC version 1.47 or later. Use it only in a mesh that includes all gRPC clients.

When creating a custom policy, the following documentation might be helpful:

  * To make your custom policy more sophisticated, you can use the Open Request Cost Aggregation (ORCA) APIs. These APIs let you capture metrics about query cost and server utilization. Using these APIs requires gRPC version 1.48.1 or later. For more information, see [gRPC ORCA Example](https://github.com/grpc/grpc-java/tree/v1.48.1/examples/example-orca).

  * For information about how custom load-balancing configurations are delivered to gRPC by xDS, see [gRPC xDS Custom Load Balancer Configuration](https://github.com/grpc/proposal/blob/master/A52-xds-custom-lb-policies.md).




To configure Cloud Service Mesh to use your custom policy, identify the policy by using the `localityLbPolicies` field.

The following steps demonstrate this process. In this procedure, you update the configuration of the `grpcwallet-wallet-v2-service` backend service so that clients connecting to it use a custom policy called [`example.ExampleLoadBalancer`](https://github.com/GoogleCloudPlatform/traffic-director-grpc-examples/blob/master/java/src/main/java/io/grpc/examples/wallet/ExampleLoadBalancerProvider.java).

**Caution:** This feature is intended for use in a service mesh that includes gRPC clients only. Envoy proxies can't use backend services that have this configuration.

###  gcloud 

  1. Export the `grpcwallet-wallet-v2-service` backend service configuration file by using the [`gcloud compute backend-services export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/export) command:
         
         gcloud compute backend-services export grpcwallet-wallet-v2-service \
         --destination=bs_config.yaml \
         --global
         

  2. Update the exported `bs_config.yaml` file to reference the `example.ExampleLoadBalancer` policy. Include the following lines:
         
         localityLbPolicies:
           - customPolicy:
               name: example.ExampleLoadBalancer
               data: '{ "message": "Hello load-balancing world!" }'
         

  3. Import the updated file by using the [gcloud compute backend-services import](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/import) command:
         
         gcloud compute backend-services import grpcwallet-wallet-v2-service --source=bs_config.yaml --global
         

  4. Optional: Test the load-balancing configuration:

###  Java 
         
         cd ~/traffic-director-grpc-examples/java
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob
         

If you configured the custom load-balancing policy correctly, you see the message that you included in the configuration ("Hello load-balancing world!").




#### Define a list of preferred policies

If you have multiple clients that don't all support a single load-balancing policy, create a list of policies that your clients can use. With this option, if your first preferred policy can't be used by a particular client, gRPC falls back to the next policy on the list.

When you create a list of preferred policies, valid options include custom policies, and, for Java clients, `ROUND_ROBIN`. You can list up to 10 policies.

This feature is available only for Java clients that use gRPC version 1.47 or later. Use it only in a mesh that includes all gRPC clients.

**Caution:** This feature is intended for use in a service mesh that includes gRPC clients only. Envoy proxies can't use backend services that have this configuration.

###  gcloud 

  1. Export the `grpcwallet-wallet-v2-service` backend service configuration file by using the [`gcloud compute backend-services export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/export) command:


    
    
    gcloud compute backend-services export grpcwallet-wallet-v2-service \
      --destination=bs_config.yaml \
      --global
    

  1. Update the exported `bs_config.yaml` file to include the `localityLbPolicies` field. Populate it with entries that represent the following policies:

     * An invalid custom policy (`example.InvalidLoadBalancer`)
     * A valid custom policy (`example.ExampleLoadBalancer`)
     * A supported built-in policy (`LEAST_REQUEST`)
    
    localityLbPolicies:
      - customPolicy:
          name: example.InvalidLoadBalancer
          data: '{ "message": "This load-balancing policy doesn't work!" }'
      - customPolicy:
          name: example.ExampleLoadBalancer
          data: '{ "message": "Hello load-balancing world!" }'
      - policy:
          name: LEAST_REQUEST
    

  2. Import the updated file by using the [gcloud compute backend-services import](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/import) command:
         
         gcloud compute backend-services import grpcwallet-wallet-v2-service --source=bs_config.yaml --global
         

  3. Optional: Test the load-balancing configuration:

###  Java 
         
         cd ~/traffic-director-grpc-examples/java
         ./build/install/wallet/bin/client balance --wallet_server="xds:///wallet.grpcwallet.io" --watch=true --user=Bob
         

In response, gRPC tries and fails to find `example.InvalidLoadBalancer`. Afterward, it falls back to using `example.ExampleLoadBalancer`, and you see the message that you included in the configuration ("Hello load-balancing world!"). The gRPC logging on the client includes a message stating that `example.InvalidLoadBalancer` was not found.




## Clean up the resources

To clean up the resources, run the following command from your local system:
    
    
    traffic-director-grpc-examples/scripts/cleanup.sh
    

## Block traffic between services

If you want to block traffic between Service A and Service B, and your deployment is on GKE, set up service security and use an authorization policy to block traffic between services. For complete instructions, see [Cloud Service Mesh service security](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-overview-legacy) and the setup instructions with [Envoy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-envoy-setup-legacy) and [proxyless gRPC](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-proxyless-setup-legacy).

## What's next

  * To help you resolve Cloud Service Mesh configuration issues, see [Troubleshooting deployments that use proxyless gRPC](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
