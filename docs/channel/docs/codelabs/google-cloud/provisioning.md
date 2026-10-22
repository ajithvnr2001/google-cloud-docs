---
url: https://docs.cloud.google.com/channel/docs/codelabs/google-cloud/provisioning/
title: Codelab: Provisioning Google Cloud entitlements \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:44.538452+00:00
---

# Codelab: Provisioning Google Cloud entitlements  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/codelabs/google-cloud/provisioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  Codelab: Provisioning Google Cloud entitlements Stay organized with collections  Save and categorize content based on your preferences. 

## Before you begin

  * Make sure you complete the [API setup codelab](https://docs.cloud.google.com/channel/docs/codelabs/setup) to set up a Google Cloud project and create a service account to call the Cloud Channel API. 

  * Read about the [Channel Services operations](https://docs.cloud.google.com/channel/docs/concepts#operations). 




## Overview

Provisioning a customer with a Google Cloud entitlement involves several API calls. The following diagram shows the high-level steps to provision your customer.

![Steps to provision Google Cloud entitlements via Cloud Channel API](https://docs.cloud.google.com/static/channel/docs/images/gcp-provisioning-iam.png)

## Step 1: Create service objects with authenticated credentials

### Using a client library

This codelab assumes you're using one of the client libraries for Cloud Channel API.

We recommend using a Google client library for your integration. These libraries provide a natural and language-specific interface, offer better performance by using RPC instead of HTTP, and set default values for fields.

To install the library:

###  C++ 

To install the C++ client library, see [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup).

###  C# 

If you are using Visual Studio 2017 or higher, open nuget package manager window and type the following:
    
    
    Install-Package Google.Cloud.Channel.V1
    

If you are using .NET Core command-line interface tools to install your dependencies, run the following command:
    
    
    dotnet add package Google.Cloud.Channel.V1
    

###  Go 
    
    
    go mod init YOUR_MODULE_NAME
    go get cloud.google.com/go/channel/apiv1
    

###  Java 

If use use Maven, add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://github.com/GoogleCloudPlatform/cloud-opensource-java/wiki/The-Google-Cloud-Platform-Libraries-BOM).
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>20.9.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-channel</artifactId>
        <version>2.3.0</version>
      </dependency>
    

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation group: 'com.google.cloud', name: 'google-cloud-channel', version: '2.3.0'
    

If you're using VS Code, IntelliJ, or Eclipse, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

###  Node.js 
    
    
    npm install @google-cloud/channel
    

###  PHP 
    
    
    composer require google/cloud-channel
    

###  Python 
    
    
    pip install google-cloud-channel
    

###  Ruby 
    
    
    gem install google-cloud-channel
    

If you choose not to use a client library, we recommend checking for a smaller client library to handle authentication. We do not recommend rewriting the authentication layer from scratch.

### Set up credentials for authentication

The Cloud Channel API uses a type of authentication that requires:

  1. A service account and its corresponding JSON key file.
  2. A reseller domain super admin to impersonate using domain-wide delegation on the service account's client.



Follow the [API setup codelab](https://docs.cloud.google.com/channel/docs/codelabs/setup) if you're missing any prerequisites. For more information, see [OAuth 2.0 for service accounts](https://developers.google.com/identity/protocols/oauth2/service-account).

In the code below, fill in these variables using your information:

  * `jsonKeyFile`: The path to the JSON key file generated when you [created a service account](https://docs.cloud.google.com/channel/docs/codelabs/setup#create-service-account).
  * `resellerAdminUser`: The email address of a reseller domain super admin.
  * `accountId`: Your Account ID, found in the Settings page of your Partner Sales Console.
  * `customerDomain`: The end customer's domain. 

**Note:** for a production deployment, we recommend setting those variables as environment variables, as described in the [client libraries](https://docs.cloud.google.com/channel/docs/reference/libraries) page.

###  C# 
    
    
    using Google.Apis.Auth.OAuth2;
    using Google.Api.Gax;
    using Google.Cloud.Billing.V1; // optional
    using Google.Cloud.Channel.V1;
    using Google.Cloud.Iam.V1; // optional
    using Google.Type;
    using Newtonsoft.Json;
    using System;
    using System.Linq;
    
    namespace Codelab {
    
      class Program {
    
        /***************** REPLACE WITH YOUR OWN VALUES ********************************/
        private static readonly string jsonKeyFile = "path/to/json_key_file.json";
        private static readonly string resellerAdminUser = "admin@yourresellerdomain.com";
        private static readonly string accountId = "C012345";
        private static readonly string customerDomain = "example.com";
        /*******************************************************************************/
    
        private static readonly string accountName = "accounts/" + accountId;
    
        private static CloudChannelServiceClient client;
    
        static void Main(string[] args) {
          // Set up credentials with user impersonation
          ICredential credential = GoogleCredential.FromFile(jsonKeyFile)
                                       .CreateScoped(CloudChannelServiceClient.DefaultScopes)
                                       .CreateWithUser(resellerAdminUser);
    
          // Create the API client
          client = new CloudChannelServiceClientBuilder {
            TokenAccessMethod = credential.GetAccessTokenForRequestAsync
          }.Build();

###  Go 
    
    
    package main
    
    import (
    	"context"
    	"fmt"
    	"io/ioutil"
    
    	billing "cloud.google.com/go/billing/apiv1" // optional
    	channel "cloud.google.com/go/channel/apiv1"
    	"golang.org/x/oauth2/google"
    	"google.golang.org/api/iterator"
    	"google.golang.org/api/option"
    	channelpb "google.golang.org/genproto/googleapis/cloud/channel/v1"
    	iampb "google.golang.org/genproto/googleapis/iam/v1" // optional
    	"google.golang.org/genproto/googleapis/type/postaladdress"
    	"google.golang.org/protobuf/encoding/protojson"
    )
    
    // ############## REPLACE WITH YOUR OWN VALUES ####################
    const jsonKeyFile = "path/to/json_key_file.json"
    const resellerAdminUser = "admin@yourresellerdomain.com"
    const accountID = "C012345"
    const customerDomain = "example.com"
    
    // ################################################################
    
    const accountName = "accounts/" + accountID
    
    func main() {
    	ctx := context.Background()
    
    	// set up credentials with user impersonation
    	jsonKey, _ := ioutil.ReadFile(jsonKeyFile)
    	jwt, _ := google.JWTConfigFromJSON(jsonKey, "https://www.googleapis.com/auth/apps.order")
    	jwt.Subject = resellerAdminUser
    	tokenSource := jwt.TokenSource(ctx)
    	// create the API client
    	client, _ := channel.NewCloudChannelClient(ctx, option.WithTokenSource(tokenSource))

###  Java 
    
    
    import com.google.api.gax.core.FixedCredentialsProvider;
    import com.google.api.gax.longrunning.OperationFuture;
    import com.google.auth.oauth2.GoogleCredentials;
    import com.google.auth.oauth2.ServiceAccountCredentials;
    import com.google.cloud.channel.v1.CloudChannelServiceClient;
    import com.google.cloud.channel.v1.CloudChannelServiceSettings;
    import com.google.cloud.channel.v1.CreateCustomerRequest;
    import com.google.cloud.channel.v1.CreateEntitlementRequest;
    import com.google.cloud.channel.v1.Customer;
    import com.google.cloud.channel.v1.Entitlement;
    import com.google.cloud.channel.v1.ListOffersRequest;
    import com.google.cloud.channel.v1.Offer;
    import com.google.cloud.channel.v1.OperationMetadata;
    import com.google.cloud.channel.v1.Parameter;
    import com.google.cloud.channel.v1.Value;
    import com.google.gson.Gson;
    import com.google.type.PostalAddress;
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.Iterator;
    import java.util.concurrent.ExecutionException;
    
    // optional
    import java.util.ArrayList;
    import java.util.List;
    import com.google.cloud.billing.v1.CloudBillingClient;
    import com.google.cloud.billing.v1.CloudBillingSettings;
    import com.google.iam.v1.Binding;
    import com.google.iam.v1.Policy;
    
    // ...
    
    public class Codelab {
    
      /***************** REPLACE WITH YOUR OWN VALUES ********************************/
      public static final String JSON_KEY_FILE = "path/to/json_key_file.json";
      public static final String RESELLER_ADMIN_USER = "admin@yourresellerdomain.com";
      public static final String ACCOUNT_ID = "C012345";
      public static final String CUSTOMER_DOMAIN = "example.com";
      /*******************************************************************************/
    
      public static final String ACCOUNT_NAME = "accounts/" + ACCOUNT_ID;
    
      private static CloudChannelServiceClient client;
      private static final Gson gson = new Gson();
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
    
        // Set up credentials with user impersonation
        FileInputStream jsonKeyFileSteam = new FileInputStream(JSON_KEY_FILE);
        GoogleCredentials credentials = ServiceAccountCredentials.fromStream(jsonKeyFileSteam)
                                            .createScoped("https://www.googleapis.com/auth/apps.order")
                                            .createDelegated(RESELLER_ADMIN_USER);
    
        CloudChannelServiceSettings clientSettings =
            CloudChannelServiceSettings.newBuilder()
                .setCredentialsProvider(FixedCredentialsProvider.create(credentials))
                .build();
    
        // Create the API client
        client = CloudChannelServiceClient.create(clientSettings);

###  Node.js 
    
    
    const {JWT} = require('google-auth-library');
    const {grpc} = require('google-gax');
    const {CloudChannelServiceClient} = require('@google-cloud/channel');
    
    // ############## REPLACE WITH YOUR OWN VALUES ####################
    const jsonKeyFile = 'path/to/json_key_file.json';
    const resellerAdminUser = 'admin@yourresellerdomain.com';
    const accountId = 'C012345';
    const customerDomain = 'example.com';
    // ################################################################
    const accountName = `accounts/${accountId}`;
    
    // Set up credentials with user impersonation
    const authClient = new JWT({
      keyFile: jsonKeyFile,
      scopes: ['https://www.googleapis.com/auth/apps.order'],
      subject: resellerAdminUser,
    });
    const sslCreds = grpc.credentials.combineChannelCredentials(
      grpc.credentials.createSsl(),
      grpc.credentials.createFromGoogleCredential(authClient)
    );
    // Create the API client
    const client = new CloudChannelServiceClient({sslCreds});

###  PHP 
    
    
    require 'vendor/autoload.php';
    
    use Google\Auth\Credentials\ServiceAccountCredentials;
    use Google\Cloud\Channel;
    
    // ############## REPLACE WITH YOUR OWN VALUES ####################
    $JSON_KEY_FILE = 'path/to/json_key_file.json';
    $RESELLER_ADMIN_USER = 'admin@yourresellerdomain.com';
    $ACCOUNT_ID = 'C012345';
    $CUSTOMER_DOMAIN = 'example.com';
    // ################################################################
    
    $ACCOUNT_NAME = 'accounts/' . $ACCOUNT_ID;
    
    // Set up credentials with user impersonation
    $credentials = new ServiceAccountCredentials(
      'https://www.googleapis.com/auth/apps.order', /* $scope */
      $JSON_KEY_FILE, /* $keyFile */
      $RESELLER_ADMIN_USER /* $sub */
    );
    
    // Create the API client
    $client = new Channel\V1\CloudChannelServiceClient([
      'credentials' => $credentials
    ]);

###  Python 
    
    
    from google.cloud import channel
    from google.oauth2 import service_account
    # optional
    from google.cloud import billing
    from google.iam.v1 import policy_pb2
    
    ############## REPLACE WITH YOUR OWN VALUES ####################
    JSON_KEY_FILE = "path/to/json_key_file.json"
    RESELLER_ADMIN_USER = "admin@yourresellerdomain.com"
    ACCOUNT_ID = "C012345"
    CUSTOMER_DOMAIN = "example.com"
    ################################################################
    
    ACCOUNT_NAME = "accounts/" + ACCOUNT_ID
    
    # Set up credentials with user impersonation
    credentials = service_account.Credentials.from_service_account_file(
        JSON_KEY_FILE, scopes=["https://www.googleapis.com/auth/apps.order"])
    credentials_delegated = credentials.with_subject(RESELLER_ADMIN_USER)
    
    # Create the API client
    client = channel.CloudChannelServiceClient(credentials=credentials_delegated)

###  Ruby 
    
    
    require 'google-cloud-channel'
    require 'google-cloud-billing' # Optional
    require 'google/iam/v1/policy_pb' # Optional
    
    ################## REPLACE WITH YOUR OWN VALUES ################################
    JSON_PRIVATE_KEY_FILE = 'path/to/json_key_file.json'
    RESELLER_ADMIN_USER = 'admin@yourresellerdomain.com'
    ACCOUNT_ID = 'C012345'
    CUSTOMER_DOMAIN = 'example.com'
    ################################################################################
    
    ACCOUNT_NAME = "accounts/#{ACCOUNT_ID}"
    
    # Set up credentials with user impersonation
    credentials = Google::Auth::ServiceAccountCredentials.make_creds(
      json_key_io: File.open(JSON_PRIVATE_KEY_FILE),
      scope: 'https://www.googleapis.com/auth/apps.order')
    credentials.sub = RESELLER_ADMIN_USER
    
    # Create the API client
    CLIENT = Google::Cloud::Channel::cloud_channel_service do |config|
      config.credentials = credentials
    end

## Step 2: Select an offer from your list of offers

The sample code below selects the first offer for `Google Cloud Platform`. If you want to select the offer for a specific Cloud Billing account ID (in the form of `billingAccounts/...`), you can filter offers with their `plan.billingAccount` field.

###  C# 
    
    
    PagedEnumerable<ListOffersResponse, Offer> offers =
        client.ListOffers(new ListOffersRequest { Parent = accountName });
    
    // For the purpose of this codelab, the code lists all offers and selects
    // the first offer for Google Cloud Platform.
    // This is needed because offerIds vary from one account to another,
    // but this is not a recommended model for your production integration
    Offer selectedOffer = offers.FirstOrDefault(
      o => o.Sku.MarketingInfo.DisplayName == "Google Cloud Platform");
    
    Console.WriteLine("=== Selected offer");
    Console.WriteLine(JsonConvert.SerializeObject(selectedOffer));

###  Go 
    
    
    var selectedOffer *channelpb.Offer
    req := &channelpb.ListOffersRequest{
    	Parent: accountName,
    }
    it := client.ListOffers(ctx, req)
    
    // For the purpose of this codelab, the code lists all offers and selects
    // the first offer for Google Cloud Platform.
    // This is needed because offerIds vary from one account to another and
    // is not a recommended model for your production integration.
    for {
    	offer, err := it.Next()
    	if err == iterator.Done {
    		break
    	}
    	if offer.Sku.MarketingInfo.DisplayName == "Google Cloud Platform" {
    		selectedOffer = offer
    		break
    	}
    }
    
    fmt.Println("=== Selected offer")
    fmt.Println(protojson.Format(selectedOffer))

###  Java 
    
    
    ListOffersRequest request =
        ListOffersRequest.newBuilder().setParent(ACCOUNT_NAME).build();
    
    // For the purpose of this codelab, the code lists all offers and selects
    // the first offer for Google Cloud Platform.
    // This is needed because offerIds vary from one account to another,
    // but this is not a recommended model for your production integration
    CloudChannelServiceClient.ListOffersPagedResponse response = client.listOffers(request);
    Offer selectedOffer = Offer.newBuilder().build();
    Iterator<Offer> iterator = response.iterateAll().iterator();
    while (iterator.hasNext()) {
      Offer offer = iterator.next();
      String skuName = offer.getSku().getMarketingInfo().getDisplayName();
      if (skuName.equals("Google Cloud Platform")) {
        selectedOffer = offer;
        break;
      }
    }
    
    System.out.println("=== Selected offer");
    System.out.println(gson.toJson(selectedOffer));

###  Node.js 
    
    
    const [offers] = await client.listOffers({
      parent: accountName,
    });
    
    // For the purpose of this codelab, the code lists all offers and selects
    // the first offer for the Google Cloud Platform.
    // This is needed because offerIds vary from one account to another,
    // but this is not a recommended model for your production integration
    const selectedOffer = offers.find(o => {
      return o.sku.marketingInfo.displayName === 'Google Cloud Platform';
    });
    
    console.log('=== Selected offer');
    console.info(selectedOffer);

###  PHP 
    
    
    $offers = $client->listOffers($ACCOUNT_NAME /* parent */);
    
    // For the purpose of this codelab, the code lists all offers and selects
    // the first offer for the Google Cloud Platform.
    // This is needed because offerIds vary from one account to another,
    // but this is not a recommended model for your production integration
    $sampleSku = 'Google Cloud Platform';
    foreach ($offers as $offer) {
      if ($offer->getSku()->getMarketingInfo()->getDisplayName() == $sampleSku) {
        $selectedOffer = $offer;
        break;
      }
    }
    
    print '=== Selected offer' . PHP_EOL;
    print $selectedOffer->serializeToJsonString() . PHP_EOL;

###  Python 
    
    
    request = channel.ListOffersRequest(parent=ACCOUNT_NAME)
    offers = client.list_offers(request)
    
    # For the purpose of this codelab, the code lists all offers and selects
    # the first offer for Google Cloud Platform.
    # This is needed because offerIds vary from one account to another,
    # but this is not a recommended model for your production integration
    selected_offer = None
    for offer in offers:
      if offer.sku.marketing_info.display_name == "Google Cloud Platform":
        selected_offer = offer
        break
    
    print("=== Selected offer")
    print(selected_offer)

###  Ruby 
    
    
    # For the purpose of this codelab, the code lists all offers and selects
    # the first offer for Google Cloud Platform.
    # This is needed because offerIds vary from one account to another,
    # but this is not a recommended model for your production integration
    
    request = Google::Cloud::Channel::V1::ListOffersRequest.new({ parent: ACCOUNT_NAME })
    offers = CLIENT.list_offers(request)
    sample_offer = 'Google Cloud Platform'
    
    offer = offers.detect { |offer| offer.sku.marketing_info.display_name == sample_offer }
    puts('=== Selected offer')
    puts(offer.inspect)

## Step 3: Create a Customer

Before you can create entitlements, you must create a Channel Services [customer](https://docs.cloud.google.com/channel/docs/concepts#customers) for your resold customer.

###  C# 
    
    
    // Create the Customer resource
    CreateCustomerRequest request = new CreateCustomerRequest {
      Parent = accountName,
      Customer = new Customer { OrgDisplayName = "Acme Corp",
                                OrgPostalAddress = new PostalAddress {
                                      AddressLines = { "1800 Amphibious Blvd" },
                                      PostalCode = "94045",
                                      RegionCode = "US" },
                                Domain = customerDomain,
                                // Optional. Add the CRM ID for this customer.
                                CorrelationId = "CRMID012345" }
    };
    
    Customer customer = client.CreateCustomer(request);
    Console.WriteLine("=== Created customer with id " + customer.Name);
    Console.WriteLine(JsonConvert.SerializeObject(customer));

###  Go 
    
    
    // Create the Customer resource
    req := &channelpb.CreateCustomerRequest{
    	Parent: accountName,
    	Customer: &channelpb.Customer{
    		OrgDisplayName: "Acme Corp",
    		OrgPostalAddress: &postaladdress.PostalAddress{
    			AddressLines: []string{"1800 Amphibious Blvd"},
    			PostalCode:   "94045",
    			RegionCode:   "US",
    		},
    		Domain: customerDomain,
    		// Optional. Add the CRM ID for this customer.
    		CorrelationId: "CRMID012345",
    		// Distributors need to pass the following value
    		// ChannelPartnerId: channelPartnerLinkId
    	},
    }
    customer, _ := client.CreateCustomer(ctx, req)
    fmt.Println("=== Created customer with id " + customer.Name)
    fmt.Println(protojson.Format(customer))

###  Java 
    
    
    // Create the Customer resource
    PostalAddress postalAddress =
        PostalAddress.newBuilder()
            .addAddressLines("1800 Amphibious Blvd")
            .setPostalCode("94045")
            .setRegionCode("US")
            .build();
    
    CreateCustomerRequest request =
        CreateCustomerRequest.newBuilder()
            .setParent(ACCOUNT_NAME)
            .setCustomer(
                Customer.newBuilder()
                    .setOrgDisplayName("Acme Corp")
                    .setOrgPostalAddress(postalAddress)
                    .setDomain(CUSTOMER_DOMAIN)
                    // Optional. Add the CRM ID for this customer.
                    .setCorrelationId("CRMID012345")
                    // Distributors need to pass the following field
                    // .setChannelPartnerId(channelPartnerLinkId)
                    .build())
            .build();
    
    Customer customer = client.createCustomer(request);
    
    System.out.println("=== Created customer with id " + customer.getName());
    System.out.println(gson.toJson(customer));

###  Node.js 
    
    
    // Create the Customer resource
    const [customer] = await client.createCustomer({
      parent: accountName,
      customer: {
        orgDisplayName: 'Acme Corp',
        orgPostalAddress: {
          addressLines: ['1800 Amphibious Blvd'],
          postalCode: '94045',
          regionCode: 'US',
        },
        domain: customerDomain,
        // Optional. Add the CRM ID for this customer.
        correlationId: "CRMID012345",
        // Distributors need to pass the following field
        // channelPartnerId: channelPartnerLinkId
      },
    });
    console.log(`=== Created customer with id ${customer.name}`);
    console.info(customer);

###  PHP 
    
    
    // Create the Customer resource
    $customer = $client->createCustomer(
      $ACCOUNT_NAME  /* parent */,
      new Channel\V1\Customer([
        'org_display_name' => 'Acme Corp',
        'org_postal_address' => new Google\Type\PostalAddress([
          'address_lines' => ['1800 Amphibious Blvd'],
          'postal_code' => '94045',
          'region_code' => 'US',
        ]),
        'domain' => $CUSTOMER_DOMAIN,
        // Optional. Add the CRM ID for this customer.
        'correlation_id' => 'CRMID012345',
        // Distributors need to pass the following field
        // 'channel_partner_id' => $channelPartnerLinkId
      ])
    );
    
    print '=== Created customer with id ' . $customer->getName() . PHP_EOL;
    print $customer->serializeToJsonString() . PHP_EOL;

###  Python 
    
    
    # Create the Customer resource
    request = channel.CreateCustomerRequest(
        parent=ACCOUNT_NAME,
        customer={
            "org_display_name": "Acme Corp",
            "domain": CUSTOMER_DOMAIN,
            "org_postal_address": {
                "address_lines": ["1800 Amphibious Blvd"],
                "postal_code": "94045",
                "region_code": "US"
            },
            # Optional. Add the CRM ID for this customer.
            "correlation_id": "CRMID012345"
        })
    # Distributors need to also pass the following field for the `customer`
    # "channel_partner_id": channel_partner_link_id
    
    customer = client.create_customer(request)
    
    print("=== Created customer with id ", customer.name)
    print(customer)

###  Ruby 
    
    
    # Create the Customer resource
    request = Google::Cloud::Channel::V1::CreateCustomerRequest.new(
      parent: ACCOUNT_NAME,
      customer: {
        'org_display_name': 'Acme Corp',
        'domain': CUSTOMER_DOMAIN,
        'org_postal_address': {
          'address_lines': ['1800 Amphibious Blvd'],
          'postal_code': '94045',
          'region_code': 'US'
        },
        # Optional. Add the CRM ID for this customer.
        'correlation_id': 'CRMID012345'
      })
      # Distributors need to also pass the following field for the `customer`
      # "channel_partner_id": channel_partner_link_id
    
    customer = CLIENT.create_customer(request)
    
    puts("=== Created customer with id " + customer.name)
    puts(customer.inspect)

## Step 4: Create the entitlement

After creating the customer, you can now provision the entitlement.

###  C# 
    
    
    // This display name shows on the Google Cloud console when a customer
    // links the account to their project.
    // Recommended format: "[Reseller name] - [Customer name]"
    string displayName = "Reseller XYZ - Acme corp";
    
    CreateEntitlementRequest request = new CreateEntitlementRequest {
      Parent = customer.Name,
      Entitlement = new Entitlement {
          Offer = selectedOffer.Name,
          Parameters = { new Parameter { Name = "display_name",
                                         Value = new Value {
                                              StringValue = displayName } } },
          // A string of up to 80 characters.
          // We recommend using an internal transaction ID or
          // identifier for the customer in this field.
          PurchaseOrderId = "A codelab test"
        }
    };
    
    // This call returns a long-running operation.
    var operation = client.CreateEntitlement(request);
    
    // Wait for the long-running operation and get the result.
    Entitlement entitlement = operation.PollUntilCompleted().Result;
    Console.WriteLine("=== Created entitlement");
    Console.WriteLine(JsonConvert.SerializeObject(entitlement));

###  Go 
    
    
    // This display name shows on the Google Cloud console when a customer
    // links the account to their project.
    // Recommended format: "[Reseller name] - [Customer name]"
    const displayName = "Reseller XYZ - Acme corp"
    
    // This endpoint returns a long-running operation.
    req := &channelpb.CreateEntitlementRequest{
    	Parent: customer.Name,
    	Entitlement: &channelpb.Entitlement{
    		Offer: selectedOffer.Name,
    		Parameters: []*channelpb.Parameter{
    			{
    				Name: "display_name",
    				Value: &channelpb.Value{
    					Kind: &channelpb.Value_StringValue{StringValue: displayName},
    				},
    			},
    		},
    		// A string of up to 80 characters.
    		// We recommend using an internal transaction ID or
    		// identifier for the customer in this field.
    		PurchaseOrderId: "A codelab test",
    	},
    }
    // This endpoint returns a long-running operation.
    op, _ := client.CreateEntitlement(ctx, req)
    
    // Wait for the long-running operation and get the result.
    entitlement, _ := op.Wait(ctx)
    
    fmt.Println("=== Created entitlement")
    fmt.Println(protojson.Format(entitlement))

###  Java 
    
    
    // This display name shows on the Google Cloud console when a customer
    // links the account to their project.
    // Recommended format: "[Reseller name] - [Customer name]"
    String displayName = "Reseller XYZ - Acme corp";
    
    Entitlement entitlement =
        Entitlement.newBuilder()
            .setOffer(selectedOffer.getName())
            .addParameters(
                Parameter.newBuilder()
                    .setName("display_name")
                    .setValue(Value.newBuilder().setStringValue(displayName).build())
                    .build())
            // A string of up to 80 characters.
            // We recommend using an internal transaction ID or
            // identifier for the customer in this field.
            .setPurchaseOrderId("A codelab test")
            .build();
    
    CreateEntitlementRequest request =
        CreateEntitlementRequest.newBuilder()
            .setParent(customer.getName())
            .setEntitlement(entitlement)
            .build();
    
    // This call returns a long-running operation.
    OperationFuture<Entitlement, OperationMetadata> operation =
        client.createEntitlementAsync(request);
    
    // Wait for the long-running operation and get the result.
    entitlement = operation.get();
    System.out.println("=== Created entitlement");
    System.out.println(gson.toJson(entitlement));

###  Node.js 
    
    
    // This display name shows on the Google Cloud console when a customer
    // links the account to their project.
    // Recommended format: "[Reseller name] - [Customer name]"
    const displayName = 'Reseller XYZ - Acme corp';
    
    // This call returns a long-running operation.
    const [operation] = await client.createEntitlement({
      parent: customer.name,
      entitlement: {
        offer: selectedOffer.name,
        parameters: [
          {
            name: 'display_name',
            value: {
              stringValue: displayName,
            },
          },
        ],
        // A string of up to 80 characters.
        // We recommend using an internal transaction ID or
        // identifier for the customer in this field.
        purchaseOrderId: 'A codelab test',
      },
    });
    
    // Wait for the long-running operation and get the result.
    const [entitlement] = await operation.promise();
    console.log('=== Created entitlement');
    console.info(entitlement);

###  PHP 
    
    
    // This display name shows on the Google Cloud console when a customer
    // links the account to their project.
    // Recommended format: "[Reseller name] - [Customer name]"
    $displayName = 'Reseller XYZ - Acme corp';
    
    // This call returns a long-running operation.
    $operation = $client->createEntitlement(
      $customer->getName() /* parent */,
      new Channel\V1\Entitlement([
        'offer' => $selectedOffer->getName(),
        'parameters' => [
          new Channel\V1\Parameter([
            'name' => 'display_name',
            'value' => new Channel\V1\Value([
              'string_value' => $displayName,
            ])
          ]),
        ],
        // A string of up to 80 characters.
        // We recommend using an internal transaction ID or
        // identifier for the customer in this field.
        'purchase_order_id' => 'A codelab test'
      ])
    );
    
    // Wait for the long-running operation and get the result.
    $operation->pollUntilComplete();
    $entitlement = $operation->getResult();
    print '=== Created entitlement' . PHP_EOL;
    print $entitlement->serializeToJsonString() . PHP_EOL;

###  Python 
    
    
    # This display name shows on the Google Cloud console when a customer
    # links the account to their project.
    # Recommended format: "[Reseller name] - [Customer name]"
    display_name = "Reseller XYZ - Acme corp"
    
    request = channel.CreateEntitlementRequest(
        parent=customer.name,
        entitlement={
            "offer": selected_offer.name,
            "parameters": [{
                "name": "display_name",
                "value": {
                    "string_value": display_name
                }
            }],
            # A string of up to 80 characters.
            # We recommend an internal transaction ID or
            # identifier for this customer in this field.
            "purchase_order_id": "A codelab test"
        })
    
    # This call returns a long-running operation.
    operation = client.create_entitlement(request)
    
    # Wait for the long-running operation and get the result.
    entitlement = operation.result()
    
    print("=== Created entitlement")
    print(entitlement)

###  Ruby 
    
    
    # This display name shows on the Google Cloud console when a customer
    # links the account to their project.
    # Recommended format: "[Reseller name] - [Customer name]"
    display_name = 'Reseller XYZ - Acme Corp'
    
    request = Google::Cloud::Channel::V1::CreateEntitlementRequest.new(
      parent: customer.name,
      entitlement: {
        offer: selected_offer.name,
        # Setting 5 seats for this Annual offer
        parameters: [{
                       name: 'display_name',
                       value: {
                         string_value: display_name
                       }
                     }],
        # A string of up to 80 characters.
        # We recommend an internal transaction ID or
        # identifier for this customer in this field.
        purchase_order_id: 'A codelab test'
      })
    
    # This call returns a long-running operation.
    operation = CLIENT.create_entitlement(request)
    
    # Wait for the long-running operation and get the result.
    CLIENT.operations_client.wait_operation(Google::Longrunning::WaitOperationRequest
                                            .new({ name: operation.name }))
    operation = CLIENT.operations_client.get_operation(Google::Longrunning::GetOperationRequest
                                                       .new({ name: operation.name }))
    entitlement = operation.response
    
    puts("=== Created entitlement")
    puts(entitlement)

## Optional: Update IAM policy on the customer billing account

Creating the entitlement provisions a customer billing account. You may want to give your customer explicit access to this account.

This can be done programmatically via the Cloud Billing API. To do so:

  * Navigate to the [API Library](https://console.cloud.google.com/apis/library) in the Google Cloud console and enable the Cloud Billing API.
  * Grant your service account the Cloud Billing IAM role on your parent billing account. Granting Billing Account Administrator (`roles/billing.admin`) is a good option for the purpose of this codelab, but you may want to use more granular privileges in your production integration. For more information on granting access, see the [Cloud Billing API access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access) page.

**Caution:** You will receive 403 errors if there are no IAM roles on the service account.

First, install the library:

###  C# 

If you are using Visual Studio 2017 or higher, open nuget package manager window and type the following:
    
    
    Install-Package Google.Cloud.Billing.V1
    

If you are using .NET Core command-line interface tools to install your dependencies, run the following command:
    
    
    dotnet add package Google.Cloud.Billing.v1
    

###  Go 
    
    
    go get cloud.google.com/go/billing/apiv1
    

###  Java 

Refer to the [Maven repository](https://mvnrepository.com/artifact/com.google.cloud/google-cloud-billing) for instructions on how to install. The following code has been tested with version `1.1.12`.

###  Node.js 
    
    
    npm install @google-cloud/nodejs-billing
    

###  PHP 
    
    
    composer require google/cloud-billing
    

###  Python 
    
    
    pip install google-cloud-billing
    

###  Ruby 
    
    
    gem install google-cloud-billing
    

Then you can instantiate the client and update the IAM policy.

**Note:** We do not recommend using user impersonation with Cloud Billing API. The following code creates a new `credentials` object specifically for the Cloud Billing API calls.

###  C# 
    
    
    // Get the name of the customer's billing account from the entitlement
    String billingAccount = entitlement.ProvisionedService.ProvisioningId;
    
    // Create a Cloud Billing API client
    CloudBillingClient billingClient = new CloudBillingClientBuilder {
      CredentialsPath = jsonKeyFile
    }.Build();
    
    // For the purpose of this codelab, we'll grant an IAM role to the reseller
    // admin user, but this is not a requirement for a production integration.
    Policy policy = billingClient.GetIamPolicy(billingAccount);
    
    string role = "roles/billing.user";
    string member = "user:" + resellerAdminUser;
    var binding = policy.Bindings.FirstOrDefault(b => b.Role == role);
    
    // If the binding already exists, add the user to it, else add a new binding
    if (binding != null) {
      binding.Members.Add(member);
    } else {
      binding = new Binding { Role = role };
      binding.Members.Add(member);
      policy.Bindings.Add(binding);
    }
    
    // Update the IAM policy
    SetIamPolicyRequest request = new SetIamPolicyRequest {
      Resource = billingAccount,
      Policy = policy
    };
    billingClient.SetIamPolicy(request);
    
    Console.WriteLine("=== Set IAM policy");
    Console.WriteLine(JsonConvert.SerializeObject(policy));

###  Go 
    
    
    // Get the name of the customer's billing account from the entitlement
    billingAccount := entitlement.ProvisionedService.ProvisioningId
    
    // Create a Cloud Billing API client
    client, _ := billing.NewCloudBillingClient(ctx, option.WithCredentialsFile(jsonKeyFile))
    
    // For the purpose of this codelab, we'll grant an IAM role to the reseller
    // admin user, but this is not a requirement for a production integration.
    getPolicyReq := &iampb.GetIamPolicyRequest{Resource: billingAccount}
    policy, _ := client.GetIamPolicy(ctx, getPolicyReq)
    
    var binding *iampb.Binding
    const role = "roles/billing.user"
    const member = "user:" + resellerAdminUser
    for _, b := range policy.Bindings {
    	if b.Role == role {
    		binding = b
    		break
    	}
    }
    // If the binding already exists, add the user to it, else add a new binding
    if binding != nil {
    	binding.Members = append(binding.Members, member)
    } else {
    	binding = &iampb.Binding{
    		Role:    role,
    		Members: []string{member},
    	}
    	policy.Bindings = append(policy.Bindings, binding)
    }
    
    // Update the IAM policy
    setPolicyReq := &iampb.SetIamPolicyRequest{
    	Resource: billingAccount,
    	Policy:   policy,
    }
    client.SetIamPolicy(ctx, setPolicyReq)
    fmt.Println("=== Set IAM policy")
    fmt.Println(protojson.Format(policy))

###  Java 
    
    
    // Get the name of the customer's billing account from the entitlement
    String billingAccount = entitlement.getProvisionedService().getProvisioningId();
    
    // Create a Cloud Billing API client
    FileInputStream jsonKeyFileSteam = new FileInputStream(JSON_KEY_FILE);
    GoogleCredentials credentials = ServiceAccountCredentials.fromStream(jsonKeyFileSteam);
    CloudBillingSettings clientSettings =
        CloudBillingSettings.newBuilder()
            .setCredentialsProvider(FixedCredentialsProvider.create(credentials))
            .build();
    CloudBillingClient client = CloudBillingClient.create(clientSettings);
    
    // For the purpose of this codelab, we'll grant an IAM role to the reseller
    // admin user, but this is not a requirement for a production integration.
    Policy policy = client.getIamPolicy(billingAccount);
    
    Binding binding = null;
    int bindingIndex = 0;
    String role = "roles/billing.user";
    String member = "user:" + RESELLER_ADMIN_USER;
    // getBindingsList() returns an ImmutableList and copying over to an ArrayList so it's mutable.
    List<Binding> bindings = new ArrayList(policy.getBindingsList());
    for (int index = 0; index < bindings.size(); index++) {
      Binding b = bindings.get(index);
      if (b.getRole().equals(role)) {
        binding = b;
        bindingIndex = index;
        break;
      }
    }
    
    // If the binding already exists, add the user to it, else add a new binding
    Policy.Builder newPolicyBuilder = policy.toBuilder();
    if (binding != null) {
      newPolicyBuilder.setBindings(bindingIndex, binding.toBuilder().addMembers(member).build());
    } else {
      binding = Binding.newBuilder()
                  .setRole(role)
                  .addMembers(member)
                  .build();
      newPolicyBuilder.addBindings(binding);
    }
    
    // Update the IAM policy
    Policy newPolicy = newPolicyBuilder.build();
    client.setIamPolicy(billingAccount, newPolicy);
    System.out.println("=== Set IAM policy");
    System.out.println(gson.toJson(newPolicy));

###  Node.js 
    
    
    // Get the name of the customer's billing account from the entitlement
    const billingAccount = entitlement.provisionedService.provisioningId;
    
    // Create a Cloud Billing API client
    const {CloudBillingClient} = require('@google-cloud/billing');
    const billingClient = new CloudBillingClient({keyFile: jsonKeyFile});
    
    // For the purpose of this codelab, we'll grant an IAM role to the reseller
    // admin user, but this is not a requirement for a production integration.
    const [policy] = await billingClient.getIamPolicy({
      resource: billingAccount,
    });
    
    const role = 'roles/billing.user';
    const member = `user:${resellerAdminUser}`;
    const binding = policy.bindings.find(binding => {
      return binding.role === role;
    });
    // If the binding already exists, add the user to it, else add a new binding
    if (binding) {
      binding.members.push(member);
    } else {
      policy.bindings.push({
        role,
        members: [member],
      });
    }
    
    // Update the IAM policy
    await billingClient.setIamPolicy({
      resource: billingAccount,
      policy,
    });
    console.log('=== Set IAM policy');
    console.info(policy);

###  PHP 
    
    
    // Get the name of the customer's billing account from the entitlement
    $billingAccount = $entitlement->getProvisionedService()->getProvisioningId();
    
    // Create a Cloud Billing API client
    $billingClient = new Google\Cloud\Billing\V1\CloudBillingClient([
      'credentials' => $JSON_KEY_FILE
    ]);
    
    // For the purpose of this codelab, we'll grant an IAM role to the reseller
    // admin user, but this is not a requirement for a production integration.
    $policy = $billingClient->getIamPolicy($billingAccount /* $resource */);
    
    $role = 'roles/billing.user';
    $member = 'user:' . $RESELLER_ADMIN_USER;
    $binding = null;
    foreach($policy->getBindings() as $b) {
      if ($b->getRole() == $role) {
        $binding = $b;
        break;
      }
    }
    // If the binding already exists, add the user to it, else add a new binding
    if ($binding) {
      $binding->getMembers()[] = $member;
    } else {
      $binding = new \Google\Cloud\Iam\V1\Binding([
        'role' => $role,
        'members' => [ $member ],
      ]);
      $policy->getBindings()[] = $binding;
    }
    
    // Update the IAM policy
    $billingClient->setIamPolicy(
      $billingAccount /* $resource */,
      $policy
    );
    print '=== Set IAM policy' . PHP_EOL;
    print $policy->serializeToJsonString() . PHP_EOL;

###  Python 
    
    
    # Get the name of the customer's billing account from the entitlement
    billing_account = entitlement.provisioned_service.provisioning_id
    
    # Create a Cloud Billing API client
    billing_credentials = service_account.Credentials.from_service_account_file(
        JSON_KEY_FILE)
    billing_client = billing.CloudBillingClient(credentials=billing_credentials)
    
    # For the purpose of this codelab, we'll grant an IAM role to the reseller
    # admin user, but this is not a requirement for a production integration.
    policy = billing_client.get_iam_policy(resource=billing_account)
    
    role = "roles/billing.user"
    member = "user:" + RESELLER_ADMIN_USER
    binding = None
    for b in policy.bindings:
      if b.role == role:
        binding = b
        break
    # If the binding already exists, add the user to it, else add a new binding
    if binding is not None:
      binding.members.append(member)
    else:
      binding = policy_pb2.Binding(role=role, members=[member])
      policy.bindings.append(binding)
    
    # Update the IAM policy
    billing_client.set_iam_policy(request={
        "resource": billing_account,
        "policy": policy
    })
    print("=== Set IAM policy")
    print(policy)

###  Ruby 
    
    
    # Get the name of the customer's billing account from the entitlement
    billing_account = entitlement.provisioned_service.provisioning_id
    
    # Create a Cloud Billing API client
    billing_client = Google::Cloud::Billing::cloud_billing_service do |config|
      config.credentials = JSON_PRIVATE_KEY_FILE
    end
    
    # For the purpose of this codelab, we'll grant an IAM role to the reseller
    # admin user, but this is not a requirement for a production integration.
    iam_request = Google::Iam::V1::GetIamPolicyRequest.new do |config|
      config.billing_account = billing_account
    end
    
    policy = billing_client.get_iam_policy({ resource: billing_account })
    role = 'roles/billing.user'
    member = "user:#{RESELLER_ADMIN_USER}"
    binding = policy.bindings.detect { |b| b.role == role }
    
    # If the binding already exists, add the user to it, else add a new binding
    if (binding != nil)
      binding.members.add(member)
    else
      binding = Google::Iam::V1::Binding.new
      binding.role = role
      binding.members.push(member)
      policy.bindings.push(binding)
    end
    
    request = Google::Iam::V1::SetIamPolicyRequest.new do |config|
      config.policy = policy
    end
    
    # Update the IAM policy
    billing_client.set_iam_policy({ resource: billing_account, policy: policy })
    
    puts('=== Set IAM policy')
    puts(policy.inspect)

## Putting it all together

The full code example for provisioning a customer with a Google Cloud (formerly Google Cloud Platform) entitlement:

###  C# 
    
    
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    
    // Instructions for this codelab can be found on this page
    // https://cloud.google.com/channel/docs/codelabs/gcp/provisioning
    
    using Google.Apis.Auth.OAuth2;
    using Google.Api.Gax;
    using Google.Cloud.Billing.V1; // optional
    using Google.Cloud.Channel.V1;
    using Google.Cloud.Iam.V1; // optional
    using Google.Type;
    using Newtonsoft.Json;
    using System;
    using System.Linq;
    
    namespace Codelab {
    
      class Program {
    
        /***************** REPLACE WITH YOUR OWN VALUES ********************************/
        private static readonly string jsonKeyFile = "path/to/json_key_file.json";
        private static readonly string resellerAdminUser = "admin@yourresellerdomain.com";
        private static readonly string accountId = "C012345";
        private static readonly string customerDomain = "example.com";
        /*******************************************************************************/
    
        private static readonly string accountName = "accounts/" + accountId;
    
        private static CloudChannelServiceClient client;
    
        static void Main(string[] args) {
          // Set up credentials with user impersonation
          ICredential credential = GoogleCredential.FromFile(jsonKeyFile)
                                       .CreateScoped(CloudChannelServiceClient.DefaultScopes)
                                       .CreateWithUser(resellerAdminUser);
    
          // Create the API client
          client = new CloudChannelServiceClientBuilder {
            TokenAccessMethod = credential.GetAccessTokenForRequestAsync
          }.Build();
    
          Offer selectedOffer = SelectOffer();
    
          Customer customer = CreateCustomer();
    
          Entitlement entitlement = CreateEntitlement(customer, selectedOffer);
    
          SetIamPolicy(entitlement);
        }
    
        static Offer SelectOffer() {
          PagedEnumerable<ListOffersResponse, Offer> offers =
              client.ListOffers(new ListOffersRequest { Parent = accountName });
    
          // For the purpose of this codelab, the code lists all offers and selects
          // the first offer for Google Cloud Platform.
          // This is needed because offerIds vary from one account to another,
          // but this is not a recommended model for your production integration
          Offer selectedOffer = offers.FirstOrDefault(
            o => o.Sku.MarketingInfo.DisplayName == "Google Cloud Platform");
    
          Console.WriteLine("=== Selected offer");
          Console.WriteLine(JsonConvert.SerializeObject(selectedOffer));
    
          return selectedOffer;
        }
    
        static Customer CreateCustomer() {
          // Create the Customer resource
          CreateCustomerRequest request = new CreateCustomerRequest {
            Parent = accountName,
            Customer = new Customer { OrgDisplayName = "Acme Corp",
                                      OrgPostalAddress = new PostalAddress {
                                            AddressLines = { "1800 Amphibious Blvd" },
                                            PostalCode = "94045",
                                            RegionCode = "US" },
                                      Domain = customerDomain,
                                      // Optional. Add the CRM ID for this customer.
                                      CorrelationId = "CRMID012345" }
          };
    
          Customer customer = client.CreateCustomer(request);
          Console.WriteLine("=== Created customer with id " + customer.Name);
          Console.WriteLine(JsonConvert.SerializeObject(customer));
    
          return customer;
        }
    
        static Entitlement CreateEntitlement(Customer customer, Offer selectedOffer) {
          // This display name shows on the Google Cloud console when a customer
          // links the account to their project.
          // Recommended format: "[Reseller name] - [Customer name]"
          string displayName = "Reseller XYZ - Acme corp";
    
          CreateEntitlementRequest request = new CreateEntitlementRequest {
            Parent = customer.Name,
            Entitlement = new Entitlement {
                Offer = selectedOffer.Name,
                Parameters = { new Parameter { Name = "display_name",
                                               Value = new Value {
                                                    StringValue = displayName } } },
                // A string of up to 80 characters.
                // We recommend using an internal transaction ID or
                // identifier for the customer in this field.
                PurchaseOrderId = "A codelab test"
              }
          };
    
          // This call returns a long-running operation.
          var operation = client.CreateEntitlement(request);
    
          // Wait for the long-running operation and get the result.
          Entitlement entitlement = operation.PollUntilCompleted().Result;
          Console.WriteLine("=== Created entitlement");
          Console.WriteLine(JsonConvert.SerializeObject(entitlement));
    
          return entitlement;
        }
    
        static void SetIamPolicy(Entitlement entitlement) {
          // Get the name of the customer's billing account from the entitlement
          String billingAccount = entitlement.ProvisionedService.ProvisioningId;
    
          // Create a Cloud Billing API client
          CloudBillingClient billingClient = new CloudBillingClientBuilder {
            CredentialsPath = jsonKeyFile
          }.Build();
    
          // For the purpose of this codelab, we'll grant an IAM role to the reseller
          // admin user, but this is not a requirement for a production integration.
          Policy policy = billingClient.GetIamPolicy(billingAccount);
    
          string role = "roles/billing.user";
          string member = "user:" + resellerAdminUser;
          var binding = policy.Bindings.FirstOrDefault(b => b.Role == role);
    
          // If the binding already exists, add the user to it, else add a new binding
          if (binding != null) {
            binding.Members.Add(member);
          } else {
            binding = new Binding { Role = role };
            binding.Members.Add(member);
            policy.Bindings.Add(binding);
          }
    
          // Update the IAM policy
          SetIamPolicyRequest request = new SetIamPolicyRequest {
            Resource = billingAccount,
            Policy = policy
          };
          billingClient.SetIamPolicy(request);
    
          Console.WriteLine("=== Set IAM policy");
          Console.WriteLine(JsonConvert.SerializeObject(policy));
        }
      }
    }

###  Go 
    
    
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    
    // Instructions for this codelab can be found on this page
    // https://cloud.google.com/channel/docs/codelabs/gcp/provisioning
    
    package main
    
    import (
    	"context"
    	"fmt"
    	"io/ioutil"
    
    	billing "cloud.google.com/go/billing/apiv1" // optional
    	channel "cloud.google.com/go/channel/apiv1"
    	"golang.org/x/oauth2/google"
    	"google.golang.org/api/iterator"
    	"google.golang.org/api/option"
    	channelpb "google.golang.org/genproto/googleapis/cloud/channel/v1"
    	iampb "google.golang.org/genproto/googleapis/iam/v1" // optional
    	"google.golang.org/genproto/googleapis/type/postaladdress"
    	"google.golang.org/protobuf/encoding/protojson"
    )
    
    // ############## REPLACE WITH YOUR OWN VALUES ####################
    const jsonKeyFile = "path/to/json_key_file.json"
    const resellerAdminUser = "admin@yourresellerdomain.com"
    const accountID = "C012345"
    const customerDomain = "example.com"
    
    // ################################################################
    
    const accountName = "accounts/" + accountID
    
    func main() {
    	ctx := context.Background()
    
    	// set up credentials with user impersonation
    	jsonKey, _ := ioutil.ReadFile(jsonKeyFile)
    	jwt, _ := google.JWTConfigFromJSON(jsonKey, "https://www.googleapis.com/auth/apps.order")
    	jwt.Subject = resellerAdminUser
    	tokenSource := jwt.TokenSource(ctx)
    	// create the API client
    	client, _ := channel.NewCloudChannelClient(ctx, option.WithTokenSource(tokenSource))
    
    	selectedOffer := selectOffer(ctx, client)
    
    	customer := createCustomer(ctx, client)
    
    	entitlement := createEntitlement(ctx, client, customer, selectedOffer)
    
    	setIamPolicy(ctx, entitlement)
    }
    
    func selectOffer(ctx context.Context, client *channel.CloudChannelClient) *channelpb.Offer {
    	var selectedOffer *channelpb.Offer
    	req := &channelpb.ListOffersRequest{
    		Parent: accountName,
    	}
    	it := client.ListOffers(ctx, req)
    
    	// For the purpose of this codelab, the code lists all offers and selects
    	// the first offer for Google Cloud Platform.
    	// This is needed because offerIds vary from one account to another and
    	// is not a recommended model for your production integration.
    	for {
    		offer, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if offer.Sku.MarketingInfo.DisplayName == "Google Cloud Platform" {
    			selectedOffer = offer
    			break
    		}
    	}
    
    	fmt.Println("=== Selected offer")
    	fmt.Println(protojson.Format(selectedOffer))
    
    	return selectedOffer
    }
    
    func createCustomer(ctx context.Context, client *channel.CloudChannelClient) *channelpb.Customer {
    	// Create the Customer resource
    	req := &channelpb.CreateCustomerRequest{
    		Parent: accountName,
    		Customer: &channelpb.Customer{
    			OrgDisplayName: "Acme Corp",
    			OrgPostalAddress: &postaladdress.PostalAddress{
    				AddressLines: []string{"1800 Amphibious Blvd"},
    				PostalCode:   "94045",
    				RegionCode:   "US",
    			},
    			Domain: customerDomain,
    			// Optional. Add the CRM ID for this customer.
    			CorrelationId: "CRMID012345",
    			// Distributors need to pass the following value
    			// ChannelPartnerId: channelPartnerLinkId
    		},
    	}
    	customer, _ := client.CreateCustomer(ctx, req)
    	fmt.Println("=== Created customer with id " + customer.Name)
    	fmt.Println(protojson.Format(customer))
    
    	return customer
    }
    
    func createEntitlement(ctx context.Context, client *channel.CloudChannelClient,
    	customer *channelpb.Customer, selectedOffer *channelpb.Offer) *channelpb.Entitlement {
    	// This display name shows on the Google Cloud console when a customer
    	// links the account to their project.
    	// Recommended format: "[Reseller name] - [Customer name]"
    	const displayName = "Reseller XYZ - Acme corp"
    
    	// This endpoint returns a long-running operation.
    	req := &channelpb.CreateEntitlementRequest{
    		Parent: customer.Name,
    		Entitlement: &channelpb.Entitlement{
    			Offer: selectedOffer.Name,
    			Parameters: []*channelpb.Parameter{
    				{
    					Name: "display_name",
    					Value: &channelpb.Value{
    						Kind: &channelpb.Value_StringValue{StringValue: displayName},
    					},
    				},
    			},
    			// A string of up to 80 characters.
    			// We recommend using an internal transaction ID or
    			// identifier for the customer in this field.
    			PurchaseOrderId: "A codelab test",
    		},
    	}
    	// This endpoint returns a long-running operation.
    	op, _ := client.CreateEntitlement(ctx, req)
    
    	// Wait for the long-running operation and get the result.
    	entitlement, _ := op.Wait(ctx)
    
    	fmt.Println("=== Created entitlement")
    	fmt.Println(protojson.Format(entitlement))
    
    	return entitlement
    }
    
    func setIamPolicy(ctx context.Context, entitlement *channelpb.Entitlement) {
    	// Get the name of the customer's billing account from the entitlement
    	billingAccount := entitlement.ProvisionedService.ProvisioningId
    
    	// Create a Cloud Billing API client
    	client, _ := billing.NewCloudBillingClient(ctx, option.WithCredentialsFile(jsonKeyFile))
    
    	// For the purpose of this codelab, we'll grant an IAM role to the reseller
    	// admin user, but this is not a requirement for a production integration.
    	getPolicyReq := &iampb.GetIamPolicyRequest{Resource: billingAccount}
    	policy, _ := client.GetIamPolicy(ctx, getPolicyReq)
    
    	var binding *iampb.Binding
    	const role = "roles/billing.user"
    	const member = "user:" + resellerAdminUser
    	for _, b := range policy.Bindings {
    		if b.Role == role {
    			binding = b
    			break
    		}
    	}
    	// If the binding already exists, add the user to it, else add a new binding
    	if binding != nil {
    		binding.Members = append(binding.Members, member)
    	} else {
    		binding = &iampb.Binding{
    			Role:    role,
    			Members: []string{member},
    		}
    		policy.Bindings = append(policy.Bindings, binding)
    	}
    
    	// Update the IAM policy
    	setPolicyReq := &iampb.SetIamPolicyRequest{
    		Resource: billingAccount,
    		Policy:   policy,
    	}
    	client.SetIamPolicy(ctx, setPolicyReq)
    	fmt.Println("=== Set IAM policy")
    	fmt.Println(protojson.Format(policy))
    }

###  Java 
    
    
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    // Instructions for this codelab can be found on this page
    // https://cloud.google.com/channel/docs/codelabs/gcp/provisioning
    
    import com.google.api.gax.core.FixedCredentialsProvider;
    import com.google.api.gax.longrunning.OperationFuture;
    import com.google.auth.oauth2.GoogleCredentials;
    import com.google.auth.oauth2.ServiceAccountCredentials;
    import com.google.cloud.channel.v1.CloudChannelServiceClient;
    import com.google.cloud.channel.v1.CloudChannelServiceSettings;
    import com.google.cloud.channel.v1.CreateCustomerRequest;
    import com.google.cloud.channel.v1.CreateEntitlementRequest;
    import com.google.cloud.channel.v1.Customer;
    import com.google.cloud.channel.v1.Entitlement;
    import com.google.cloud.channel.v1.ListOffersRequest;
    import com.google.cloud.channel.v1.Offer;
    import com.google.cloud.channel.v1.OperationMetadata;
    import com.google.cloud.channel.v1.Parameter;
    import com.google.cloud.channel.v1.Value;
    import com.google.gson.Gson;
    import com.google.type.PostalAddress;
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.Iterator;
    import java.util.concurrent.ExecutionException;
    
    // optional
    import java.util.ArrayList;
    import java.util.List;
    import com.google.cloud.billing.v1.CloudBillingClient;
    import com.google.cloud.billing.v1.CloudBillingSettings;
    import com.google.iam.v1.Binding;
    import com.google.iam.v1.Policy;
    
    /**
    * This is a basic example of provisioning a GCP customer.
    */
    
    public class Codelab {
    
      /***************** REPLACE WITH YOUR OWN VALUES ********************************/
      public static final String JSON_KEY_FILE = "path/to/json_key_file.json";
      public static final String RESELLER_ADMIN_USER = "admin@yourresellerdomain.com";
      public static final String ACCOUNT_ID = "C012345";
      public static final String CUSTOMER_DOMAIN = "example.com";
      /*******************************************************************************/
    
      public static final String ACCOUNT_NAME = "accounts/" + ACCOUNT_ID;
    
      private static CloudChannelServiceClient client;
      private static final Gson gson = new Gson();
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
    
        // Set up credentials with user impersonation
        FileInputStream jsonKeyFileSteam = new FileInputStream(JSON_KEY_FILE);
        GoogleCredentials credentials = ServiceAccountCredentials.fromStream(jsonKeyFileSteam)
                                            .createScoped("https://www.googleapis.com/auth/apps.order")
                                            .createDelegated(RESELLER_ADMIN_USER);
    
        CloudChannelServiceSettings clientSettings =
            CloudChannelServiceSettings.newBuilder()
                .setCredentialsProvider(FixedCredentialsProvider.create(credentials))
                .build();
    
        // Create the API client
        client = CloudChannelServiceClient.create(clientSettings);
    
        Offer selectedOffer = selectOffer();
    
        Customer customer = createCustomer();
    
        Entitlement entitlement = createEntitlement(customer, selectedOffer);
    
        setIamPolicy(entitlement);
      }
    
      private static Offer selectOffer() {
        ListOffersRequest request =
            ListOffersRequest.newBuilder().setParent(ACCOUNT_NAME).build();
    
        // For the purpose of this codelab, the code lists all offers and selects
        // the first offer for Google Cloud Platform.
        // This is needed because offerIds vary from one account to another,
        // but this is not a recommended model for your production integration
        CloudChannelServiceClient.ListOffersPagedResponse response = client.listOffers(request);
        Offer selectedOffer = Offer.newBuilder().build();
        Iterator<Offer> iterator = response.iterateAll().iterator();
        while (iterator.hasNext()) {
          Offer offer = iterator.next();
          String skuName = offer.getSku().getMarketingInfo().getDisplayName();
          if (skuName.equals("Google Cloud Platform")) {
            selectedOffer = offer;
            break;
          }
        }
    
        System.out.println("=== Selected offer");
        System.out.println(gson.toJson(selectedOffer));
    
        return selectedOffer;
      }
    
      private static Customer createCustomer() throws InterruptedException, ExecutionException {
        // Create the Customer resource
        PostalAddress postalAddress =
            PostalAddress.newBuilder()
                .addAddressLines("1800 Amphibious Blvd")
                .setPostalCode("94045")
                .setRegionCode("US")
                .build();
    
        CreateCustomerRequest request =
            CreateCustomerRequest.newBuilder()
                .setParent(ACCOUNT_NAME)
                .setCustomer(
                    Customer.newBuilder()
                        .setOrgDisplayName("Acme Corp")
                        .setOrgPostalAddress(postalAddress)
                        .setDomain(CUSTOMER_DOMAIN)
                        // Optional. Add the CRM ID for this customer.
                        .setCorrelationId("CRMID012345")
                        // Distributors need to pass the following field
                        // .setChannelPartnerId(channelPartnerLinkId)
                        .build())
                .build();
    
        Customer customer = client.createCustomer(request);
    
        System.out.println("=== Created customer with id " + customer.getName());
        System.out.println(gson.toJson(customer));
    
        return customer;
      }
    
      private static Entitlement createEntitlement(Customer customer, Offer selectedOffer)
          throws InterruptedException, ExecutionException {
        // This display name shows on the Google Cloud console when a customer
        // links the account to their project.
        // Recommended format: "[Reseller name] - [Customer name]"
        String displayName = "Reseller XYZ - Acme corp";
    
        Entitlement entitlement =
            Entitlement.newBuilder()
                .setOffer(selectedOffer.getName())
                .addParameters(
                    Parameter.newBuilder()
                        .setName("display_name")
                        .setValue(Value.newBuilder().setStringValue(displayName).build())
                        .build())
                // A string of up to 80 characters.
                // We recommend using an internal transaction ID or
                // identifier for the customer in this field.
                .setPurchaseOrderId("A codelab test")
                .build();
    
        CreateEntitlementRequest request =
            CreateEntitlementRequest.newBuilder()
                .setParent(customer.getName())
                .setEntitlement(entitlement)
                .build();
    
        // This call returns a long-running operation.
        OperationFuture<Entitlement, OperationMetadata> operation =
            client.createEntitlementAsync(request);
    
        // Wait for the long-running operation and get the result.
        entitlement = operation.get();
        System.out.println("=== Created entitlement");
        System.out.println(gson.toJson(entitlement));
    
        return entitlement;
      }
    
      private static void setIamPolicy(Entitlement entitlement) throws IOException {
        // Get the name of the customer's billing account from the entitlement
        String billingAccount = entitlement.getProvisionedService().getProvisioningId();
    
        // Create a Cloud Billing API client
        FileInputStream jsonKeyFileSteam = new FileInputStream(JSON_KEY_FILE);
        GoogleCredentials credentials = ServiceAccountCredentials.fromStream(jsonKeyFileSteam);
        CloudBillingSettings clientSettings =
            CloudBillingSettings.newBuilder()
                .setCredentialsProvider(FixedCredentialsProvider.create(credentials))
                .build();
        CloudBillingClient client = CloudBillingClient.create(clientSettings);
    
        // For the purpose of this codelab, we'll grant an IAM role to the reseller
        // admin user, but this is not a requirement for a production integration.
        Policy policy = client.getIamPolicy(billingAccount);
    
        Binding binding = null;
        int bindingIndex = 0;
        String role = "roles/billing.user";
        String member = "user:" + RESELLER_ADMIN_USER;
        // getBindingsList() returns an ImmutableList and copying over to an ArrayList so it's mutable.
        List<Binding> bindings = new ArrayList(policy.getBindingsList());
        for (int index = 0; index < bindings.size(); index++) {
          Binding b = bindings.get(index);
          if (b.getRole().equals(role)) {
            binding = b;
            bindingIndex = index;
            break;
          }
        }
    
        // If the binding already exists, add the user to it, else add a new binding
        Policy.Builder newPolicyBuilder = policy.toBuilder();
        if (binding != null) {
          newPolicyBuilder.setBindings(bindingIndex, binding.toBuilder().addMembers(member).build());
        } else {
          binding = Binding.newBuilder()
                      .setRole(role)
                      .addMembers(member)
                      .build();
          newPolicyBuilder.addBindings(binding);
        }
    
        // Update the IAM policy
        Policy newPolicy = newPolicyBuilder.build();
        client.setIamPolicy(billingAccount, newPolicy);
        System.out.println("=== Set IAM policy");
        System.out.println(gson.toJson(newPolicy));
      }
    }

###  Node.js 
    
    
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    
    // Instructions for this codelab can be found on this page
    // https://cloud.google.com/channel/docs/codelabs/gcp/provisioning
    
    const {JWT} = require('google-auth-library');
    const {grpc} = require('google-gax');
    const {CloudChannelServiceClient} = require('@google-cloud/channel');
    
    // ############## REPLACE WITH YOUR OWN VALUES ####################
    const jsonKeyFile = 'path/to/json_key_file.json';
    const resellerAdminUser = 'admin@yourresellerdomain.com';
    const accountId = 'C012345';
    const customerDomain = 'example.com';
    // ################################################################
    const accountName = `accounts/${accountId}`;
    
    // Set up credentials with user impersonation
    const authClient = new JWT({
      keyFile: jsonKeyFile,
      scopes: ['https://www.googleapis.com/auth/apps.order'],
      subject: resellerAdminUser,
    });
    const sslCreds = grpc.credentials.combineChannelCredentials(
      grpc.credentials.createSsl(),
      grpc.credentials.createFromGoogleCredential(authClient)
    );
    // Create the API client
    const client = new CloudChannelServiceClient({sslCreds});
    
    async function main() {
      const selectedOffer = await selectOffer();
    
      const customer = await createCustomer();
    
      const entitlement = await createEntitlement(customer, selectedOffer);
    
      await setIamPolicy(entitlement);
    }
    
    async function selectOffer() {
      const [offers] = await client.listOffers({
        parent: accountName,
      });
    
      // For the purpose of this codelab, the code lists all offers and selects
      // the first offer for the Google Cloud Platform.
      // This is needed because offerIds vary from one account to another,
      // but this is not a recommended model for your production integration
      const selectedOffer = offers.find(o => {
        return o.sku.marketingInfo.displayName === 'Google Cloud Platform';
      });
    
      console.log('=== Selected offer');
      console.info(selectedOffer);
    
      return selectedOffer;
    }
    
    async function createCustomer() {
      // Create the Customer resource
      const [customer] = await client.createCustomer({
        parent: accountName,
        customer: {
          orgDisplayName: 'Acme Corp',
          orgPostalAddress: {
            addressLines: ['1800 Amphibious Blvd'],
            postalCode: '94045',
            regionCode: 'US',
          },
          domain: customerDomain,
          // Optional. Add the CRM ID for this customer.
          correlationId: "CRMID012345",
          // Distributors need to pass the following field
          // channelPartnerId: channelPartnerLinkId
        },
      });
      console.log(`=== Created customer with id ${customer.name}`);
      console.info(customer);
    
      return customer;
    }
    
    async function createEntitlement(customer, selectedOffer) {
      // This display name shows on the Google Cloud console when a customer
      // links the account to their project.
      // Recommended format: "[Reseller name] - [Customer name]"
      const displayName = 'Reseller XYZ - Acme corp';
    
      // This call returns a long-running operation.
      const [operation] = await client.createEntitlement({
        parent: customer.name,
        entitlement: {
          offer: selectedOffer.name,
          parameters: [
            {
              name: 'display_name',
              value: {
                stringValue: displayName,
              },
            },
          ],
          // A string of up to 80 characters.
          // We recommend using an internal transaction ID or
          // identifier for the customer in this field.
          purchaseOrderId: 'A codelab test',
        },
      });
    
      // Wait for the long-running operation and get the result.
      const [entitlement] = await operation.promise();
      console.log('=== Created entitlement');
      console.info(entitlement);
    
      return entitlement;
    }
    
    async function setIamPolicy(entitlement) {
      // Get the name of the customer's billing account from the entitlement
      const billingAccount = entitlement.provisionedService.provisioningId;
    
      // Create a Cloud Billing API client
      const {CloudBillingClient} = require('@google-cloud/billing');
      const billingClient = new CloudBillingClient({keyFile: jsonKeyFile});
    
      // For the purpose of this codelab, we'll grant an IAM role to the reseller
      // admin user, but this is not a requirement for a production integration.
      const [policy] = await billingClient.getIamPolicy({
        resource: billingAccount,
      });
    
      const role = 'roles/billing.user';
      const member = `user:${resellerAdminUser}`;
      const binding = policy.bindings.find(binding => {
        return binding.role === role;
      });
      // If the binding already exists, add the user to it, else add a new binding
      if (binding) {
        binding.members.push(member);
      } else {
        policy.bindings.push({
          role,
          members: [member],
        });
      }
    
      // Update the IAM policy
      await billingClient.setIamPolicy({
        resource: billingAccount,
        policy,
      });
      console.log('=== Set IAM policy');
      console.info(policy);
    }
    
    main().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    process.on('unhandledRejection', err => {
      console.error(err.message);
      process.exitCode = 1;
    });

###  PHP 
    
    
    <?php
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    
    // Instructions for this codelab can be found on this page
    // https://cloud.google.com/channel/docs/codelabs/gcp/provisioning
    
    require 'vendor/autoload.php';
    
    use Google\Auth\Credentials\ServiceAccountCredentials;
    use Google\Cloud\Channel;
    
    // ############## REPLACE WITH YOUR OWN VALUES ####################
    $JSON_KEY_FILE = 'path/to/json_key_file.json';
    $RESELLER_ADMIN_USER = 'admin@yourresellerdomain.com';
    $ACCOUNT_ID = 'C012345';
    $CUSTOMER_DOMAIN = 'example.com';
    // ################################################################
    
    $ACCOUNT_NAME = 'accounts/' . $ACCOUNT_ID;
    
    // Set up credentials with user impersonation
    $credentials = new ServiceAccountCredentials(
      'https://www.googleapis.com/auth/apps.order', /* $scope */
      $JSON_KEY_FILE, /* $keyFile */
      $RESELLER_ADMIN_USER /* $sub */
    );
    
    // Create the API client
    $client = new Channel\V1\CloudChannelServiceClient([
      'credentials' => $credentials
    ]);
    
    $selectedOffer = selectOffer();
    
    $customer = createCustomer();
    
    $entitlement = createEntitlement($customer, $selectedOffer);
    
    setIamPolicy($entitlement);
    
    function selectOffer() {
      global $client, $ACCOUNT_NAME;
    
      $offers = $client->listOffers($ACCOUNT_NAME /* parent */);
    
      // For the purpose of this codelab, the code lists all offers and selects
      // the first offer for the Google Cloud Platform.
      // This is needed because offerIds vary from one account to another,
      // but this is not a recommended model for your production integration
      $sampleSku = 'Google Cloud Platform';
      foreach ($offers as $offer) {
        if ($offer->getSku()->getMarketingInfo()->getDisplayName() == $sampleSku) {
          $selectedOffer = $offer;
          break;
        }
      }
    
      print '=== Selected offer' . PHP_EOL;
      print $selectedOffer->serializeToJsonString() . PHP_EOL;
    
      return $selectedOffer;
    }
    
    function createCustomer() {
      global $client, $ACCOUNT_NAME, $CUSTOMER_DOMAIN;
    
      // Create the Customer resource
      $customer = $client->createCustomer(
        $ACCOUNT_NAME  /* parent */,
        new Channel\V1\Customer([
          'org_display_name' => 'Acme Corp',
          'org_postal_address' => new Google\Type\PostalAddress([
            'address_lines' => ['1800 Amphibious Blvd'],
            'postal_code' => '94045',
            'region_code' => 'US',
          ]),
          'domain' => $CUSTOMER_DOMAIN,
          // Optional. Add the CRM ID for this customer.
          'correlation_id' => 'CRMID012345',
          // Distributors need to pass the following field
          // 'channel_partner_id' => $channelPartnerLinkId
        ])
      );
    
      print '=== Created customer with id ' . $customer->getName() . PHP_EOL;
      print $customer->serializeToJsonString() . PHP_EOL;
    
      return $customer;
    }
    
    function createEntitlement($customer, $selectedOffer) {
      global $client;
    
      // This display name shows on the Google Cloud console when a customer
      // links the account to their project.
      // Recommended format: "[Reseller name] - [Customer name]"
      $displayName = 'Reseller XYZ - Acme corp';
    
      // This call returns a long-running operation.
      $operation = $client->createEntitlement(
        $customer->getName() /* parent */,
        new Channel\V1\Entitlement([
          'offer' => $selectedOffer->getName(),
          'parameters' => [
            new Channel\V1\Parameter([
              'name' => 'display_name',
              'value' => new Channel\V1\Value([
                'string_value' => $displayName,
              ])
            ]),
          ],
          // A string of up to 80 characters.
          // We recommend using an internal transaction ID or
          // identifier for the customer in this field.
          'purchase_order_id' => 'A codelab test'
        ])
      );
    
      // Wait for the long-running operation and get the result.
      $operation->pollUntilComplete();
      $entitlement = $operation->getResult();
      print '=== Created entitlement' . PHP_EOL;
      print $entitlement->serializeToJsonString() . PHP_EOL;
    
      return $entitlement;
    }
    
    function setIamPolicy($entitlement) {
      global $JSON_KEY_FILE, $RESELLER_ADMIN_USER;
    
      // Get the name of the customer's billing account from the entitlement
      $billingAccount = $entitlement->getProvisionedService()->getProvisioningId();
    
      // Create a Cloud Billing API client
      $billingClient = new Google\Cloud\Billing\V1\CloudBillingClient([
        'credentials' => $JSON_KEY_FILE
      ]);
    
      // For the purpose of this codelab, we'll grant an IAM role to the reseller
      // admin user, but this is not a requirement for a production integration.
      $policy = $billingClient->getIamPolicy($billingAccount /* $resource */);
    
      $role = 'roles/billing.user';
      $member = 'user:' . $RESELLER_ADMIN_USER;
      $binding = null;
      foreach($policy->getBindings() as $b) {
        if ($b->getRole() == $role) {
          $binding = $b;
          break;
        }
      }
      // If the binding already exists, add the user to it, else add a new binding
      if ($binding) {
        $binding->getMembers()[] = $member;
      } else {
        $binding = new \Google\Cloud\Iam\V1\Binding([
          'role' => $role,
          'members' => [ $member ],
        ]);
        $policy->getBindings()[] = $binding;
      }
    
      // Update the IAM policy
      $billingClient->setIamPolicy(
        $billingAccount /* $resource */,
        $policy
      );
      print '=== Set IAM policy' . PHP_EOL;
      print $policy->serializeToJsonString() . PHP_EOL;
    }

###  Python 
    
    
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    
    """GCP Provisioning codelab.
    
    Instructions for this codelab can be found on this page:
    https://cloud.google.com/channel/docs/codelabs/gcp/provisioning
    """
    
    from google.cloud import channel
    from google.oauth2 import service_account
    # optional
    from google.cloud import billing
    from google.iam.v1 import policy_pb2
    
    ############## REPLACE WITH YOUR OWN VALUES ####################
    JSON_KEY_FILE = "path/to/json_key_file.json"
    RESELLER_ADMIN_USER = "admin@yourresellerdomain.com"
    ACCOUNT_ID = "C012345"
    CUSTOMER_DOMAIN = "example.com"
    ################################################################
    
    ACCOUNT_NAME = "accounts/" + ACCOUNT_ID
    
    # Set up credentials with user impersonation
    credentials = service_account.Credentials.from_service_account_file(
        JSON_KEY_FILE, scopes=["https://www.googleapis.com/auth/apps.order"])
    credentials_delegated = credentials.with_subject(RESELLER_ADMIN_USER)
    
    # Create the API client
    client = channel.CloudChannelServiceClient(credentials=credentials_delegated)
    
    
    def main():
      offer = select_offer()
    
      customer = create_customer()
    
      entitlement = create_entitlement(customer, offer)
    
      set_iam_policy(entitlement)
    
    
    def select_offer():
      """Selects a GCP offer.
    
      Returns:
        A Channel API Offer for GCP
      """
      request = channel.ListOffersRequest(parent=ACCOUNT_NAME)
      offers = client.list_offers(request)
    
      # For the purpose of this codelab, the code lists all offers and selects
      # the first offer for Google Cloud Platform.
      # This is needed because offerIds vary from one account to another,
      # but this is not a recommended model for your production integration
      selected_offer = None
      for offer in offers:
        if offer.sku.marketing_info.display_name == "Google Cloud Platform":
          selected_offer = offer
          break
    
      print("=== Selected offer")
      print(selected_offer)
    
      return selected_offer
    
    
    def create_customer():
      """Create the Customer resource, with a cloud identity.
    
      Returns:
        The created Channel API Customer
      """
      # Create the Customer resource
      request = channel.CreateCustomerRequest(
          parent=ACCOUNT_NAME,
          customer={
              "org_display_name": "Acme Corp",
              "domain": CUSTOMER_DOMAIN,
              "org_postal_address": {
                  "address_lines": ["1800 Amphibious Blvd"],
                  "postal_code": "94045",
                  "region_code": "US"
              },
              # Optional. Add the CRM ID for this customer.
              "correlation_id": "CRMID012345"
          })
      # Distributors need to also pass the following field for the `customer`
      # "channel_partner_id": channel_partner_link_id
    
      customer = client.create_customer(request)
    
      print("=== Created customer with id ", customer.name)
      print(customer)
    
      return customer
    
    
    def create_entitlement(customer, selected_offer):
      """Create the Entitlement.
    
      Args:
        customer: a Customer resource
        selected_offer: an Offer
    
      Returns:
        The created Channel API Entitlement
      """
      # This display name shows on the Google Cloud console when a customer
      # links the account to their project.
      # Recommended format: "[Reseller name] - [Customer name]"
      display_name = "Reseller XYZ - Acme corp"
    
      request = channel.CreateEntitlementRequest(
          parent=customer.name,
          entitlement={
              "offer": selected_offer.name,
              "parameters": [{
                  "name": "display_name",
                  "value": {
                      "string_value": display_name
                  }
              }],
              # A string of up to 80 characters.
              # We recommend an internal transaction ID or
              # identifier for this customer in this field.
              "purchase_order_id": "A codelab test"
          })
    
      # This call returns a long-running operation.
      operation = client.create_entitlement(request)
    
      # Wait for the long-running operation and get the result.
      entitlement = operation.result()
    
      print("=== Created entitlement")
      print(entitlement)
    
      return entitlement
    
    
    def set_iam_policy(entitlement):
      """Sets IAM Policy on the created entitlement.
    
      Args:
        entitlement: a GCP Entitlement
      """
      # Get the name of the customer's billing account from the entitlement
      billing_account = entitlement.provisioned_service.provisioning_id
    
      # Create a Cloud Billing API client
      billing_credentials = service_account.Credentials.from_service_account_file(
          JSON_KEY_FILE)
      billing_client = billing.CloudBillingClient(credentials=billing_credentials)
    
      # For the purpose of this codelab, we'll grant an IAM role to the reseller
      # admin user, but this is not a requirement for a production integration.
      policy = billing_client.get_iam_policy(resource=billing_account)
    
      role = "roles/billing.user"
      member = "user:" + RESELLER_ADMIN_USER
      binding = None
      for b in policy.bindings:
        if b.role == role:
          binding = b
          break
      # If the binding already exists, add the user to it, else add a new binding
      if binding is not None:
        binding.members.append(member)
      else:
        binding = policy_pb2.Binding(role=role, members=[member])
        policy.bindings.append(binding)
    
      # Update the IAM policy
      billing_client.set_iam_policy(request={
          "resource": billing_account,
          "policy": policy
      })
      print("=== Set IAM policy")
      print(policy)
    
    
    if __name__ == "__main__":
      main()

###  Ruby 
    
    
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    
    # GCP Provisioning codelab.
    
    # Instructions for this codelab can be found on this page:
    # https://cloud.google.com/channel/docs/codelabs/gcp/provisioning
    
    require 'google-cloud-channel'
    require 'google-cloud-billing' # Optional
    require 'google/iam/v1/policy_pb' # Optional
    
    ################## REPLACE WITH YOUR OWN VALUES ################################
    JSON_PRIVATE_KEY_FILE = 'path/to/json_key_file.json'
    RESELLER_ADMIN_USER = 'admin@yourresellerdomain.com'
    ACCOUNT_ID = 'C012345'
    CUSTOMER_DOMAIN = 'example.com'
    ################################################################################
    
    ACCOUNT_NAME = "accounts/#{ACCOUNT_ID}"
    
    # Set up credentials with user impersonation
    credentials = Google::Auth::ServiceAccountCredentials.make_creds(
      json_key_io: File.open(JSON_PRIVATE_KEY_FILE),
      scope: 'https://www.googleapis.com/auth/apps.order')
    credentials.sub = RESELLER_ADMIN_USER
    
    # Create the API client
    CLIENT = Google::Cloud::Channel::cloud_channel_service do |config|
      config.credentials = credentials
    end
    
    def main
      offer = select_offer
      customer = create_customer
      entitlement = create_entitlement(customer, offer)
      set_iam_policy(entitlement)
    end
    
    def select_offer
      # For the purpose of this codelab, the code lists all offers and selects
      # the first offer for Google Cloud Platform.
      # This is needed because offerIds vary from one account to another,
      # but this is not a recommended model for your production integration
    
      request = Google::Cloud::Channel::V1::ListOffersRequest.new({ parent: ACCOUNT_NAME })
      offers = CLIENT.list_offers(request)
      sample_offer = 'Google Cloud Platform'
    
      offer = offers.detect { |offer| offer.sku.marketing_info.display_name == sample_offer }
      puts('=== Selected offer')
      puts(offer.inspect)
      offer
    end
    
    def create_customer
      # Create the Customer resource
      request = Google::Cloud::Channel::V1::CreateCustomerRequest.new(
        parent: ACCOUNT_NAME,
        customer: {
          'org_display_name': 'Acme Corp',
          'domain': CUSTOMER_DOMAIN,
          'org_postal_address': {
            'address_lines': ['1800 Amphibious Blvd'],
            'postal_code': '94045',
            'region_code': 'US'
          },
          # Optional. Add the CRM ID for this customer.
          'correlation_id': 'CRMID012345'
        })
        # Distributors need to also pass the following field for the `customer`
        # "channel_partner_id": channel_partner_link_id
    
      customer = CLIENT.create_customer(request)
    
      puts("=== Created customer with id " + customer.name)
      puts(customer.inspect)
      customer
    end
    
    def create_entitlement(customer, selected_offer)
      # This display name shows on the Google Cloud console when a customer
      # links the account to their project.
      # Recommended format: "[Reseller name] - [Customer name]"
      display_name = 'Reseller XYZ - Acme Corp'
    
      request = Google::Cloud::Channel::V1::CreateEntitlementRequest.new(
        parent: customer.name,
        entitlement: {
          offer: selected_offer.name,
          # Setting 5 seats for this Annual offer
          parameters: [{
                         name: 'display_name',
                         value: {
                           string_value: display_name
                         }
                       }],
          # A string of up to 80 characters.
          # We recommend an internal transaction ID or
          # identifier for this customer in this field.
          purchase_order_id: 'A codelab test'
        })
    
      # This call returns a long-running operation.
      operation = CLIENT.create_entitlement(request)
    
      # Wait for the long-running operation and get the result.
      CLIENT.operations_client.wait_operation(Google::Longrunning::WaitOperationRequest
                                              .new({ name: operation.name }))
      operation = CLIENT.operations_client.get_operation(Google::Longrunning::GetOperationRequest
                                                         .new({ name: operation.name }))
      entitlement = operation.response
    
      puts("=== Created entitlement")
      puts(entitlement)
    
      entitlement
    end
    
    def set_iam_policy(entitlement)
      # Get the name of the customer's billing account from the entitlement
      billing_account = entitlement.provisioned_service.provisioning_id
    
      # Create a Cloud Billing API client
      billing_client = Google::Cloud::Billing::cloud_billing_service do |config|
        config.credentials = JSON_PRIVATE_KEY_FILE
      end
    
      # For the purpose of this codelab, we'll grant an IAM role to the reseller
      # admin user, but this is not a requirement for a production integration.
      iam_request = Google::Iam::V1::GetIamPolicyRequest.new do |config|
        config.billing_account = billing_account
      end
    
      policy = billing_client.get_iam_policy({ resource: billing_account })
      role = 'roles/billing.user'
      member = "user:#{RESELLER_ADMIN_USER}"
      binding = policy.bindings.detect { |b| b.role == role }
    
      # If the binding already exists, add the user to it, else add a new binding
      if (binding != nil)
        binding.members.add(member)
      else
        binding = Google::Iam::V1::Binding.new
        binding.role = role
        binding.members.push(member)
        policy.bindings.push(binding)
      end
    
      request = Google::Iam::V1::SetIamPolicyRequest.new do |config|
        config.policy = policy
      end
    
      # Update the IAM policy
      billing_client.set_iam_policy({ resource: billing_account, policy: policy })
    
      puts('=== Set IAM policy')
      puts(policy.inspect)
    end
    
    main()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
