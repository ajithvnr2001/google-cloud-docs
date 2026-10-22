---
url: https://docs.cloud.google.com/channel/docs/codelabs/workspace/provisioning/
title: Codelab: Provisioning Google Workspace \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:31.294732+00:00
---

# Codelab: Provisioning Google Workspace  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/codelabs/workspace/provisioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  Codelab: Provisioning Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

## Before you begin

  * Make sure you complete the [API setup codelab](https://docs.cloud.google.com/channel/docs/codelabs/setup) to set up a Google Cloud project and create a service account to call the Cloud Channel API. 

  * Read about the [Channel Services operations](https://docs.cloud.google.com/channel/docs/concepts#operations). 

  * We recommend using your Test Partner Sales Console for this codelab. 




## Overview

Provisioning a customer with a Google Workspace entitlement involves several API calls. The following diagram shows the high-level steps to provision your customer.

![Steps to provision Google Workspace via Cloud Channel API](https://docs.cloud.google.com/static/channel/docs/images/workspace-provisioning.png)

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
  * `resellerAdminUser`: The email address of a reseller domain super admin(preferably of your Test Partner Sales Console).
  * `accountId`: Your Account ID, found in the Settings page of your Partner Sales Console.
  * `customerDomain`: The end customer's domain. If you run this codelab on your Test Partner Sales Console, make sure the domain follows domain naming conventions. 

**Note:** for a production deployment, we recommend setting those variables as environment variables, as described in the [client libraries](https://docs.cloud.google.com/channel/docs/reference/libraries) page.

###  C# 
    
    
    using Google.Apis.Auth.OAuth2;
    using Google.Api.Gax;
    using Google.Cloud.Channel.V1;
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
    	"log"
    
    	channel "cloud.google.com/go/channel/apiv1"
    	"golang.org/x/oauth2/google"
    	"google.golang.org/api/iterator"
    	"google.golang.org/api/option"
    	channelpb "google.golang.org/genproto/googleapis/cloud/channel/v1"
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
    	// Set up credentials with user impersonation
    	jsonKey, _ := ioutil.ReadFile(jsonKeyFile)
    	jwt, _ := google.JWTConfigFromJSON(jsonKey, "https://www.googleapis.com/auth/apps.order")
    	jwt.Subject = resellerAdminUser
    	tokenSource := jwt.TokenSource(ctx)
    	// Create the API client
    	client, _ := channel.NewCloudChannelClient(ctx, option.WithTokenSource(tokenSource))

###  Java 
    
    
    import com.google.api.gax.core.FixedCredentialsProvider;
    import com.google.api.gax.longrunning.OperationFuture;
    import com.google.auth.oauth2.GoogleCredentials;
    import com.google.auth.oauth2.ServiceAccountCredentials;
    import com.google.cloud.channel.v1.AdminUser;
    import com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistRequest;
    import com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse;
    import com.google.cloud.channel.v1.CloudChannelServiceClient;
    import com.google.cloud.channel.v1.CloudChannelServiceSettings;
    import com.google.cloud.channel.v1.CloudIdentityInfo;
    import com.google.cloud.channel.v1.CommitmentSettings;
    import com.google.cloud.channel.v1.CreateCustomerRequest;
    import com.google.cloud.channel.v1.CreateEntitlementRequest;
    import com.google.cloud.channel.v1.Customer;
    import com.google.cloud.channel.v1.Entitlement;
    import com.google.cloud.channel.v1.ListOffersRequest;
    import com.google.cloud.channel.v1.Offer;
    import com.google.cloud.channel.v1.OperationMetadata;
    import com.google.cloud.channel.v1.Parameter;
    import com.google.cloud.channel.v1.PaymentPlan;
    import com.google.cloud.channel.v1.Period;
    import com.google.cloud.channel.v1.PeriodType;
    import com.google.cloud.channel.v1.ProvisionCloudIdentityRequest;
    import com.google.cloud.channel.v1.RenewalSettings;
    import com.google.cloud.channel.v1.Value;
    import com.google.gson.Gson;
    import com.google.type.PostalAddress;
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.Iterator;
    import java.util.concurrent.ExecutionException;
    
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
          throws Exception, IOException, ExecutionException, InterruptedException {
    
        // Set up credentials with user impersonation
        FileInputStream jsonKeyFileStream = new FileInputStream(JSON_KEY_FILE);
        GoogleCredentials  credentials = ServiceAccountCredentials.fromStream(jsonKeyFileStream)
                                            .createScoped("https://www.googleapis.com/auth/apps.order")
                                            .createDelegated(RESELLER_ADMIN_USER);
        // Create the API client
        CloudChannelServiceSettings serviceSettings =
            CloudChannelServiceSettings.newBuilder()
                .setCredentialsProvider(FixedCredentialsProvider.create(credentials))
                .build();
        client = CloudChannelServiceClient.create(serviceSettings);

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
    $client = new Channel\V1\Client\CloudChannelServiceClient([
      'credentials' => $credentials
    ]);

###  Python 
    
    
    from google.cloud import channel
    from google.oauth2 import service_account
    
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
      scope: 'https://www.googleapis.com/auth/apps.order'
    )
    credentials.sub = RESELLER_ADMIN_USER
    
    # Create the API client
    CLIENT = Google::Cloud::Channel::cloud_channel_service do |config|
      config.credentials = credentials
    end

## Step 2: Pick an offer from your list of offers

###  C# 
    
    
    PagedEnumerable<ListOffersResponse, Offer> offers =
        client.ListOffers(new ListOffersRequest { Parent = accountName });
    
    // For the purpose of this codelab, the code lists all offers and selects
    // the first offer for Google Workspace Business Standard on an Annual
    // plan. This is needed because offerIds vary from one account to another,
    // but this is not a recommended model for your production integration
    string sampleOffer = "Google Workspace Business Standard";
    PaymentPlan samplePlan = PaymentPlan.Commitment;
    
    Offer selectedOffer = offers.FirstOrDefault(
      o => o.Sku.MarketingInfo.DisplayName == sampleOffer && o.Plan.PaymentPlan == samplePlan);
    
    Console.WriteLine("=== Selected offer");
    Console.WriteLine(JsonConvert.SerializeObject(selectedOffer));

###  Go 
    
    
    var selectedOffer *channelpb.Offer
    req := &channelpb.ListOffersRequest{
    	Parent: accountName,
    }
    it := client.ListOffers(ctx, req)
    
    // For the purpose of this codelab, the code lists all offers and selects
    // the first offer for Google Workspace Business Standard on an Annual
    // plan. This is needed because offerIds vary from one account to another and
    // is not a recommended model for your production integration.
    for {
    	offer, err := it.Next()
    	if err == iterator.Done {
    		break
    	}
    	if offer.Sku.MarketingInfo.DisplayName == "Google Workspace Business Standard" &&
    		offer.Plan.PaymentPlan == channelpb.PaymentPlan_COMMITMENT {
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
    // the first offer for Google Workspace Business Standard on an Annual
    // plan. This is needed because offerIds vary from one account to another,
    // but this is not a recommended model for your production integration
    String sampleSkuName = "Google Workspace Business Standard";
    String samplePlan = "COMMITMENT";
    
    CloudChannelServiceClient.ListOffersPagedResponse response = client.listOffers(request);
    Offer selectedOffer = Offer.newBuilder().build();
    Iterator<Offer> iterator = response.iterateAll().iterator();
    while (iterator.hasNext()) {
      Offer offer = iterator.next();
      String skuName = offer.getSku().getMarketingInfo().getDisplayName();
      String offerPlan = offer.getPlan().getPaymentPlan().name();
      if (skuName.equals(sampleSkuName) && offerPlan.equals(samplePlan)) {
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
    // the first offer for Google Workspace Business Standard on an Annual
    // plan. This is needed because offerIds vary from one account to another,
    // but this is not a recommended model for your production integration
    const selectedOffer = offers.find(o => {
      return (
        o.sku.marketingInfo.displayName ===
          'Google Workspace Business Standard' &&
        o.plan.paymentPlan === 'COMMITMENT'
      );
    });
    
    console.log('=== Selected offer');
    console.info(selectedOffer);

###  PHP 
    
    
    $request = new Channel\V1\ListOffersRequest(['parent' => $ACCOUNT_NAME]);
    $offers = $client->listOffers($request);
    
    // For the purpose of this codelab, the code lists all offers and selects
    // the first offer for Google Workspace Business Standard on an Annual
    // plan. This is needed because offerIds vary from one account to another,
    // but this is not a recommended model for your production integration
    $sampleSku = 'Google Workspace Business Standard';
    $samplePlan = Channel\V1\PaymentPlan::COMMITMENT;
    foreach ($offers as $offer) {
      if ($offer->getSku()->getMarketingInfo()->getDisplayName() == $sampleSku
      && $offer->getPlan()->getPaymentPlan() == $samplePlan) {
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
    # the first offer for Google Workspace Business Standard on an Annual
    # plan. This is needed because offerIds vary from one account to another,
    # but this is not a recommended model for your production integration
    sample_offer = "Google Workspace Business Standard"
    sample_plan = "PaymentPlan.COMMITMENT"
    selected_offer = None
    for offer in offers:
      if offer.sku.marketing_info.display_name == sample_offer and \
          str(offer.plan.payment_plan) == sample_plan:
        selected_offer = offer
        break
    
    print("=== Selected offer")
    print(selected_offer)

###  Ruby 
    
    
    # For the purpose of this codelab, the code lists all offers and selects
    # the first offer for Google Workspace Business Standard on an Annual
    # plan. This is needed because offerIds vary from one account to another,
    # but this is not a recommended model for your production integration
    
    request = Google::Cloud::Channel::V1::ListOffersRequest.new({ parent: ACCOUNT_NAME })
    offers = CLIENT.list_offers(request)
    sample_offer = 'Google Workspace Business Standard'
    sample_plan = :COMMITMENT
    
    offer = offers.detect { |offer| offer.sku.marketing_info.display_name == sample_offer
      && offer.plan.payment_plan == sample_plan }
    puts("=== Selected offer")
    puts(offer.inspect)

## Step 3: Create a Customer for Google Workspace

### Find out if the customer has a cloud identity

You can only provision Google Workspace products for a customer if they do not have an existing [cloud identity](https://docs.cloud.google.com/channel/docs/concepts#cloud_identity) or if you already resell for them.

If the customer has a cloud identity, you must [transfer the customer and their entitlements](https://support.google.com/channelservices/answer/9547629).

Use the [`accounts.checkCloudIdentityAccountsExist`](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/checkCloudIdentityAccountsExist) endpoint to see if you can provision them as a new customer. If the endpoint returns a list of existing cloud identities, you must transfer the customer instead.

###  C# 
    
    
    // Determine if customer already has a cloud identity
    CheckCloudIdentityAccountsExistRequest request =
        new CheckCloudIdentityAccountsExistRequest { Parent = accountName,
                                                     Domain = customerDomain };
    
    CheckCloudIdentityAccountsExistResponse response =
        client.CheckCloudIdentityAccountsExist(request);
    
    if (response.CloudIdentityAccounts.Count > 0) {
      throw new Exception(@"Cloud identity already exists. Customer must be transferred.
      Out of scope for this codelab");
    }

###  Go 
    
    
    // Determine if customer already has a cloud identity
    req := &channelpb.CheckCloudIdentityAccountsExistRequest{
    	Parent: accountName,
    	Domain: customerDomain,
    }
    res, _ := client.CheckCloudIdentityAccountsExist(ctx, req)
    // checkCloudIdentityAccountsExist always returns an array
    if len(res.CloudIdentityAccounts) > 0 {
    	log.Fatal(`Cloud identity already exists;
    		customer must be transferred
    		[out-of-scope of this codelab]`)
    }

###  Java 
    
    
    // Determine if customer already has a cloud identity
    CheckCloudIdentityAccountsExistRequest request =
        CheckCloudIdentityAccountsExistRequest.newBuilder()
            .setParent(ACCOUNT_NAME)
            .setDomain(CUSTOMER_DOMAIN)
            .build();
    CheckCloudIdentityAccountsExistResponse response =
        client.checkCloudIdentityAccountsExist(request);
    
    if (response.getCloudIdentityAccountsCount() > 0) {
      throw new Exception(
          "Cloud identity already exists. "
          + "Customer must be transferred. "
          + "Out of scope for this codelab");
    }

###  Node.js 
    
    
    // Determine if customer already has a cloud identity
    const [
      cloudIdentityAccounts,
    ] = await client.checkCloudIdentityAccountsExist({
      parent: accountName,
      domain: customerDomain,
    });
    
    if (cloudIdentityAccounts.length > 0) {
      throw new Error(
        'Cloud identity already exists; ' +
          'customer must be transferred ' +
          '[out-of-scope of this codelab]'
      );
    }

###  PHP 
    
    
    // Determine if customer already has a cloud identity
    $request = new Channel\V1\CheckCloudIdentityAccountsExistsRequest([
      'parent' => $ACCOUNT_NAME,
      'domain' => $CUSTOMER_DOMAIN,
    ]);
    $response = $client->checkCloudIdentityAccountsExist($request);
    
    if (count($response->getCloudIdentityAccounts()) > 0) {
      throw new Error('Cloud identity already exists; \
        customer must be transferred \
        [out-of-scope of this codelab]'
      );
    }

###  Python 
    
    
    # Determine if customer already has a cloud identity
    request = channel.CheckCloudIdentityAccountsExistRequest(
        parent=ACCOUNT_NAME, domain=CUSTOMER_DOMAIN)
    
    response = client.check_cloud_identity_accounts_exist(request)
    
    if response.cloud_identity_accounts:
      raise Exception(
          "Cloud identity already exists. Customer must be transferred." +
          "Out of scope for this codelab")

###  Ruby 
    
    
    # Determine if customer already has a cloud identity
    request = Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest
    .new({ parent: ACCOUNT_NAME, domain: CUSTOMER_DOMAIN })
    response = CLIENT.check_cloud_identity_accounts_exist(request)
    
    if response.cloud_identity_accounts.count > 0
      raise 'Cloud identity already exists. Customer must be transferred.'\
        'Out of scope for this codelab'
    end

### Create a Channel Services customer

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
    let [customer] = await client.createCustomer({
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
    $request = new Channel\V1\CreateCustomerRequest([
      'parent' => $ACCOUNT_NAME,
      'customer' => new Channel\V1\Customer([
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
    ]);
    $customer = $client->createCustomer($request);
    
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

### Provision a cloud identity

After you have a customer, you need to attach a [cloud identity](https://docs.cloud.google.com/channel/docs/concepts#cloud_identity) with the required information to provision Google Workspace products.

**Important:** `alternateEmail` must be on a different domain from the `Customer.domain`.

###  C# 
    
    
    CloudIdentityInfo cloudIdentityInfo =
        new CloudIdentityInfo { AlternateEmail = "john.doe@gmail.com", LanguageCode = "en-US" };
    
    AdminUser adminUser = new AdminUser { GivenName = "John", FamilyName = "Doe",
                                          Email = "admin@" + customerDomain };
    
    ProvisionCloudIdentityRequest cloudIdentityRequest = new ProvisionCloudIdentityRequest {
      Customer = customer.Name, CloudIdentityInfo = cloudIdentityInfo, User = adminUser
    };
    
    // This call returns a long-running operation.
    var operation = client.ProvisionCloudIdentity(cloudIdentityRequest);
    
    // Wait for the long-running operation and get the result.
    customer = operation.PollUntilCompleted().Result;
    Console.WriteLine("=== Provisioned cloud identity");

###  Go 
    
    
    cireq := &channelpb.ProvisionCloudIdentityRequest{
    	Customer: customer.Name,
    	CloudIdentityInfo: &channelpb.CloudIdentityInfo{
    		AlternateEmail: "john.doe@gmail.com",
    		LanguageCode:   "en-US",
    	},
    	User: &channelpb.AdminUser{
    		GivenName:  "John",
    		FamilyName: "Doe",
    		Email:      "admin@" + customerDomain,
    	},
    }
    // This endpoint returns a long-running operation.
    op, _ := client.ProvisionCloudIdentity(ctx, cireq)
    
    // Wait for the long-running operation and get the result.
    customer, _ = op.Wait(ctx)
    fmt.Println("=== Provisioned cloud identity")

###  Java 
    
    
    CloudIdentityInfo cloudIdentityInfo =
        CloudIdentityInfo.newBuilder()
            .setAlternateEmail("john.doe@gmail.com")
            .setLanguageCode("en-US")
            .build();
    
    AdminUser adminUser =
        AdminUser.newBuilder()
            .setGivenName("John")
            .setFamilyName("Doe")
            .setEmail("admin@" + CUSTOMER_DOMAIN)
            .build();
    
    ProvisionCloudIdentityRequest cloudIdentityRequest =
        ProvisionCloudIdentityRequest.newBuilder()
            .setCustomer(customer.getName())
            .setCloudIdentityInfo(cloudIdentityInfo)
            .setUser(adminUser)
            .build();
    
    // This call returns a long-running operation.
    OperationFuture<Customer, OperationMetadata> operation =
        client.provisionCloudIdentityAsync(cloudIdentityRequest);
    
    // Wait for the long-running operation and get the result.
    customer = operation.get();
    System.out.println("=== Provisioned cloud identity");

###  Node.js 
    
    
    // This endpoint returns a long-running operation.
    // For other ways to get operation results, see
    // https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations
    const [operation] = await client.provisionCloudIdentity({
      customer: customer.name,
      cloudIdentityInfo: {
        alternateEmail: 'john.doe@gmail.com',
        languageCode: 'en-US',
      },
      user: {
        givenName: 'John',
        familyName: 'Doe',
        email: `admin@${customerDomain}`,
      },
    });
    
    // Wait for the long-running operation and get the result.
    [customer] = await operation.promise();
    console.log('=== Provisioned cloud identity');

###  PHP 
    
    
    // This endpoint returns a long-running operation.
    $request = new Channel\V1\ProvisionCloudIdentityRequest([
      'customer' => $customer->getName() /* customer */,
      'cloud_identity_info' => new Channel\V1\CloudIdentityInfo([
        'alternate_email' => 'john.doe@gmail.com',
        'language_code' => 'en-US',
      ]),
      'user' => new Channel\V1\AdminUser([
        'given_name' => 'John',
        'family_name' => 'Doe',
        'email' => 'admin@' . $CUSTOMER_DOMAIN,
      ])
    ]);
    $operation = $client->provisionCloudIdentity($request);
    
    // Wait for the long-running operation and get the result.
    $operation->pollUntilComplete();
    $customer = $operation->getResult();
    print '=== Provisioned cloud identity' . PHP_EOL;

###  Python 
    
    
    cloud_identity_info = channel.CloudIdentityInfo(
        alternate_email="john.doe@gmail.com", language_code="en-US")
    
    admin_user = channel.AdminUser(
        given_name="John", family_name="Doe", email="admin@" + CUSTOMER_DOMAIN)
    
    cloud_identity_request = channel.ProvisionCloudIdentityRequest(
        customer=customer.name,
        cloud_identity_info=cloud_identity_info,
        user=admin_user)
    
    # This call returns a long-running operation.
    operation = client.provision_cloud_identity(cloud_identity_request)
    
    # Wait for the long-running operation and get the result.
    customer = operation.result()
    
    print("=== Provisioned cloud identity")

###  Ruby 
    
    
    cloud_identity_info = Google::Cloud::Channel::V1::CloudIdentityInfo.new(
      alternate_email: 'john.doe@gmail.com', language_code: 'en-US'
    )
    
    admin_user = Google::Cloud::Channel::V1::AdminUser.new(
      given_name: 'John', family_name: 'Doe', email: "admin@#{CUSTOMER_DOMAIN}"
    )
    
    cloud_identity_request = Google::Cloud::Channel::V1::ProvisionCloudIdentityRequest.new(
      customer: customer.name,
      cloud_identity_info: cloud_identity_info,
      user: admin_user
    )
    
    # This call returns a long-running operation.
    operation = CLIENT.provision_cloud_identity(cloud_identity_request)
    
    # Wait for the long-running operation and get the result.
    CLIENT.operations_client.wait_operation(Google::Longrunning::WaitOperationRequest
      .new({ name: operation.name }))
    operation = CLIENT.operations_client.get_operation(Google::Longrunning::GetOperationRequest
      .new({ name: operation.name }))
    customer = operation.response
    puts("=== Provisioned cloud identity")

This call will create the cloud identity, including the customer's first super admin.

## Step 4: Create a Google Workspace entitlement

After creating the customer and their cloud identity, you can now provision a Google Workspace entitlement.

###  C# 
    
    
    RenewalSettings renewalSettings = new RenewalSettings {
      // Setting renewal settings to auto renew
      EnableRenewal = true,
      PaymentPlan = PaymentPlan.Commitment,
      PaymentCycle = new Period {
        PeriodType = PeriodType.Year,
        Duration = 1
      }
    };
    
    CreateEntitlementRequest request = new CreateEntitlementRequest {
      Parent = customer.Name,
      Entitlement = new Entitlement {
          Offer = selectedOffer.Name,
          // Setting 5 seats for this Annual offer
          Parameters = { new Parameter { Name = "num_units",
                                         Value = new Value { Int64Value = 5 } } },
          CommitmentSettings = new CommitmentSettings { RenewalSettings = renewalSettings },
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
    
    
    // This endpoint returns a long-running operation.
    req := &channelpb.CreateEntitlementRequest{
    	Parent: customer.Name,
    	Entitlement: &channelpb.Entitlement{
    		Offer: selectedOffer.Name,
    		// Setting 5 seats for this Annual offer
    		Parameters: []*channelpb.Parameter{
    			{
    				Name: "num_units",
    				Value: &channelpb.Value{
    					Kind: &channelpb.Value_Int64Value{Int64Value: 5},
    				},
    			},
    		},
    		// Setting renewal settings to auto renew
    		CommitmentSettings: &channelpb.CommitmentSettings{
    			RenewalSettings: &channelpb.RenewalSettings{
    				EnableRenewal: true,
    				PaymentPlan:   channelpb.PaymentPlan_COMMITMENT,
    				PaymentCycle: &channelpb.Period{
    					Duration:   1,
    					PeriodType: channelpb.PeriodType_YEAR,
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
    
    
    RenewalSettings renewalSettings =
        RenewalSettings.newBuilder()
            // Setting renewal settings to auto renew
            .setEnableRenewal(true)
            .setPaymentPlan(PaymentPlan.COMMITMENT)
            .setPaymentCycle(
                Period.newBuilder().setPeriodType(PeriodType.YEAR).setDuration(1).build())
            .build();
    
    CommitmentSettings commitmentSettings =
        CommitmentSettings.newBuilder().setRenewalSettings(renewalSettings).build();
    
    Entitlement entitlement =
        Entitlement.newBuilder()
            .setOffer(selectedOffer.getName())
            // Setting 5 seats for this Annual offer
            .addParameters(
                Parameter.newBuilder()
                    .setName("num_units")
                    .setValue(Value.newBuilder().setInt64Value(5).build())
                    .build())
            .setCommitmentSettings(commitmentSettings)
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
    
    
    // This call returns a long-running operation.
    const [operation] = await client.createEntitlement({
      parent: customer.name,
      entitlement: {
        offer: selectedOffer.name,
        parameters: [
          // Setting 5 seats for this Annual offer
          {
            name: 'num_units',
            value: {
              int64Value: 5,
            },
          },
        ],
        commitmentSettings: {
          // Setting renewal settings to auto renew
          renewalSettings: {
            enableRenewal: true,
            paymentPlan: 'COMMITMENT',
            paymentCycle: {
              duration: 1,
              periodType: 'YEAR',
            },
          },
        },
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
    
    
    // This call returns a long-running operation.
    $request = new Channel\V1\CreateEntitlementRequest([
      'parent' => $customer->getName(),
      'entitlement' => new Channel\V1\Entitlement([
        'offer' => $selectedOffer->getName(),
        'parameters' => [
          new Channel\V1\Parameter([
            // Setting 5 seats for this Annual offer
            'name' => 'num_units',
            'value' => new Channel\V1\Value([
              'int64_value' => 5,
            ])
          ]),
        ],
        'commitment_settings' => new Channel\V1\CommitmentSettings([
          // Setting renewal settings to auto renew
          'renewal_settings' => new Channel\V1\RenewalSettings([
            'enable_renewal' => true,
            'payment_plan' => Channel\V1\PaymentPlan::COMMITMENT,
            'payment_cycle' => new Channel\V1\Period([
              'duration' => 1,
              'period_type' => Channel\V1\PeriodType::YEAR,
            ]),
          ]),
        ]),
        // A string of up to 80 characters.
        // We recommend using an internal transaction ID or
        // identifier for the customer in this field.
        'purchase_order_id' => 'A codelab test'
      ])
    ]);
    $operation = $client->createEntitlement($request);
    
    // Wait for the long-running operation and get the result.
    $operation->pollUntilComplete();
    $entitlement = $operation->getResult();
    print '=== Created entitlement' . PHP_EOL;
    print $entitlement->serializeToJsonString() . PHP_EOL;

###  Python 
    
    
    request = channel.CreateEntitlementRequest(
        parent=customer.name,
        entitlement={
            "offer": selected_offer.name,
            # Setting 5 seats for this Annual offer
            "parameters": [{
                "name": "num_units",
                "value": {
                    "int64_value": 5
                }
            }],
            "commitment_settings": {
                "renewal_settings": {
                    # Setting renewal settings to auto renew
                    "enable_renewal": True,
                    "payment_plan": "COMMITMENT",
                    "payment_cycle": {
                        "period_type": "YEAR",
                        "duration": 1
                    }
                }
            },
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
    
    
    request = Google::Cloud::Channel::V1::CreateEntitlementRequest.new(
      parent: customer.name,
      entitlement: {
        offer: selected_offer.name,
        # Setting 5 seats for this Annual offer
        parameters: [{
                       name: 'num_units',
                       value: {
                         int64_value: 5
                       }
                     }],
        commitment_settings: {
          renewal_settings: {
            # Setting renewal settings to auto renew
            enable_renewal: true,
            payment_plan: 'COMMITMENT',
            payment_cycle: {
              period_type: 'YEAR',
              duration: 1
            }
          }
        },
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

**Key Point:** Google Workspace entitlements are suspended until a customer super admin logs in and accepts the Terms of Service. Customer super admins are redirected to the Terms of Service on their first login when accessing any Google property (for example, Gmail or Drive).

## Optional: Integrate with Workspace Admin SDK

If you plan to integrate with the [Workspace Admin SDK](https://developers.google.com/admin-sdk), its APIs require a Google Workspace `customerId`. The Cloud Channel API returns this as the `cloudIdentityId` on the `Customer` resource.

###  C# 
    
    
    string customerId = customer.CloudIdentityId;
    Console.WriteLine(customerId);

###  Go 
    
    
    customerID := customer.CloudIdentityId
    fmt.Println(customerID)

###  Java 
    
    
    String adminSDKCustomerId = customer.getCloudIdentityId();
    System.out.println(adminSDKCustomerId);

###  Node.js 
    
    
    const customerId = customer.cloudIdentityId;
    console.log(customerId);

###  PHP 
    
    
    $customerId = $customer->getCloudIdentityId();
    print $customerId . PHP_EOL;

###  Python 
    
    
    customer_id = customer.cloud_identity_id
    print(customer_id)

###  Ruby 
    
    
    customer_id = customer.cloud_identity_id
    puts(customer_id)

## Putting it all together

The full code example for provisioning a customer with a Google Workspace entitlement:

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
    // https://cloud.google.com/channel/docs/codelabs/workspace/provisioning
    
    using Google.Apis.Auth.OAuth2;
    using Google.Api.Gax;
    using Google.Cloud.Channel.V1;
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
    
          CheckExists();
    
          Customer customer = CreateCustomer();
    
          Entitlement entitlement = CreateEntitlement(customer, selectedOffer);
    
          string customerId = customer.CloudIdentityId;
          Console.WriteLine(customerId);
        }
    
        static Offer SelectOffer() {
          PagedEnumerable<ListOffersResponse, Offer> offers =
              client.ListOffers(new ListOffersRequest { Parent = accountName });
    
          // For the purpose of this codelab, the code lists all offers and selects
          // the first offer for Google Workspace Business Standard on an Annual
          // plan. This is needed because offerIds vary from one account to another,
          // but this is not a recommended model for your production integration
          string sampleOffer = "Google Workspace Business Standard";
          PaymentPlan samplePlan = PaymentPlan.Commitment;
    
          Offer selectedOffer = offers.FirstOrDefault(
            o => o.Sku.MarketingInfo.DisplayName == sampleOffer && o.Plan.PaymentPlan == samplePlan);
    
          Console.WriteLine("=== Selected offer");
          Console.WriteLine(JsonConvert.SerializeObject(selectedOffer));
    
          return selectedOffer;
        }
    
        static void CheckExists() {
          // Determine if customer already has a cloud identity
          CheckCloudIdentityAccountsExistRequest request =
              new CheckCloudIdentityAccountsExistRequest { Parent = accountName,
                                                           Domain = customerDomain };
    
          CheckCloudIdentityAccountsExistResponse response =
              client.CheckCloudIdentityAccountsExist(request);
    
          if (response.CloudIdentityAccounts.Count > 0) {
            throw new Exception(@"Cloud identity already exists. Customer must be transferred.
            Out of scope for this codelab");
          }
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
    
          CloudIdentityInfo cloudIdentityInfo =
              new CloudIdentityInfo { AlternateEmail = "john.doe@gmail.com", LanguageCode = "en-US" };
    
          AdminUser adminUser = new AdminUser { GivenName = "John", FamilyName = "Doe",
                                                Email = "admin@" + customerDomain };
    
          ProvisionCloudIdentityRequest cloudIdentityRequest = new ProvisionCloudIdentityRequest {
            Customer = customer.Name, CloudIdentityInfo = cloudIdentityInfo, User = adminUser
          };
    
          // This call returns a long-running operation.
          var operation = client.ProvisionCloudIdentity(cloudIdentityRequest);
    
          // Wait for the long-running operation and get the result.
          customer = operation.PollUntilCompleted().Result;
          Console.WriteLine("=== Provisioned cloud identity");
    
          return customer;
        }
    
        static Entitlement CreateEntitlement(Customer customer, Offer selectedOffer) {
          RenewalSettings renewalSettings = new RenewalSettings {
            // Setting renewal settings to auto renew
            EnableRenewal = true,
            PaymentPlan = PaymentPlan.Commitment,
            PaymentCycle = new Period {
              PeriodType = PeriodType.Year,
              Duration = 1
            }
          };
    
          CreateEntitlementRequest request = new CreateEntitlementRequest {
            Parent = customer.Name,
            Entitlement = new Entitlement {
                Offer = selectedOffer.Name,
                // Setting 5 seats for this Annual offer
                Parameters = { new Parameter { Name = "num_units",
                                               Value = new Value { Int64Value = 5 } } },
                CommitmentSettings = new CommitmentSettings { RenewalSettings = renewalSettings },
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
    // https://cloud.google.com/channel/docs/codelabs/workspace/provisioning
    
    package main
    
    import (
    	"context"
    	"fmt"
    	"io/ioutil"
    	"log"
    
    	channel "cloud.google.com/go/channel/apiv1"
    	"golang.org/x/oauth2/google"
    	"google.golang.org/api/iterator"
    	"google.golang.org/api/option"
    	channelpb "google.golang.org/genproto/googleapis/cloud/channel/v1"
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
    	// Set up credentials with user impersonation
    	jsonKey, _ := ioutil.ReadFile(jsonKeyFile)
    	jwt, _ := google.JWTConfigFromJSON(jsonKey, "https://www.googleapis.com/auth/apps.order")
    	jwt.Subject = resellerAdminUser
    	tokenSource := jwt.TokenSource(ctx)
    	// Create the API client
    	client, _ := channel.NewCloudChannelClient(ctx, option.WithTokenSource(tokenSource))
    
    	selectedOffer := selectOffer(ctx, client)
    
    	checkExists(ctx, client)
    
    	customer := createCustomer(ctx, client)
    
    	_ /* entitlement */ = createEntitlement(ctx, client, customer, selectedOffer)
    
    	customerID := customer.CloudIdentityId
    	fmt.Println(customerID)
    }
    
    func selectOffer(ctx context.Context, client *channel.CloudChannelClient) *channelpb.Offer {
    	var selectedOffer *channelpb.Offer
    	req := &channelpb.ListOffersRequest{
    		Parent: accountName,
    	}
    	it := client.ListOffers(ctx, req)
    
    	// For the purpose of this codelab, the code lists all offers and selects
    	// the first offer for Google Workspace Business Standard on an Annual
    	// plan. This is needed because offerIds vary from one account to another and
    	// is not a recommended model for your production integration.
    	for {
    		offer, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if offer.Sku.MarketingInfo.DisplayName == "Google Workspace Business Standard" &&
    			offer.Plan.PaymentPlan == channelpb.PaymentPlan_COMMITMENT {
    			selectedOffer = offer
    			break
    		}
    	}
    
    	fmt.Println("=== Selected offer")
    	fmt.Println(protojson.Format(selectedOffer))
    
    	return selectedOffer
    }
    
    func checkExists(ctx context.Context, client *channel.CloudChannelClient) {
    	// Determine if customer already has a cloud identity
    	req := &channelpb.CheckCloudIdentityAccountsExistRequest{
    		Parent: accountName,
    		Domain: customerDomain,
    	}
    	res, _ := client.CheckCloudIdentityAccountsExist(ctx, req)
    	// checkCloudIdentityAccountsExist always returns an array
    	if len(res.CloudIdentityAccounts) > 0 {
    		log.Fatal(`Cloud identity already exists;
    			customer must be transferred
    			[out-of-scope of this codelab]`)
    	}
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
    
    	cireq := &channelpb.ProvisionCloudIdentityRequest{
    		Customer: customer.Name,
    		CloudIdentityInfo: &channelpb.CloudIdentityInfo{
    			AlternateEmail: "john.doe@gmail.com",
    			LanguageCode:   "en-US",
    		},
    		User: &channelpb.AdminUser{
    			GivenName:  "John",
    			FamilyName: "Doe",
    			Email:      "admin@" + customerDomain,
    		},
    	}
    	// This endpoint returns a long-running operation.
    	op, _ := client.ProvisionCloudIdentity(ctx, cireq)
    
    	// Wait for the long-running operation and get the result.
    	customer, _ = op.Wait(ctx)
    	fmt.Println("=== Provisioned cloud identity")
    
    	return customer
    }
    
    func createEntitlement(ctx context.Context, client *channel.CloudChannelClient,
    	customer *channelpb.Customer, selectedOffer *channelpb.Offer) *channelpb.Entitlement {
    	// This endpoint returns a long-running operation.
    	req := &channelpb.CreateEntitlementRequest{
    		Parent: customer.Name,
    		Entitlement: &channelpb.Entitlement{
    			Offer: selectedOffer.Name,
    			// Setting 5 seats for this Annual offer
    			Parameters: []*channelpb.Parameter{
    				{
    					Name: "num_units",
    					Value: &channelpb.Value{
    						Kind: &channelpb.Value_Int64Value{Int64Value: 5},
    					},
    				},
    			},
    			// Setting renewal settings to auto renew
    			CommitmentSettings: &channelpb.CommitmentSettings{
    				RenewalSettings: &channelpb.RenewalSettings{
    					EnableRenewal: true,
    					PaymentPlan:   channelpb.PaymentPlan_COMMITMENT,
    					PaymentCycle: &channelpb.Period{
    						Duration:   1,
    						PeriodType: channelpb.PeriodType_YEAR,
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
    // https://cloud.google.com/channel/docs/codelabs/workspace/provisioning
    
    import com.google.api.gax.core.FixedCredentialsProvider;
    import com.google.api.gax.longrunning.OperationFuture;
    import com.google.auth.oauth2.GoogleCredentials;
    import com.google.auth.oauth2.ServiceAccountCredentials;
    import com.google.cloud.channel.v1.AdminUser;
    import com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistRequest;
    import com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse;
    import com.google.cloud.channel.v1.CloudChannelServiceClient;
    import com.google.cloud.channel.v1.CloudChannelServiceSettings;
    import com.google.cloud.channel.v1.CloudIdentityInfo;
    import com.google.cloud.channel.v1.CommitmentSettings;
    import com.google.cloud.channel.v1.CreateCustomerRequest;
    import com.google.cloud.channel.v1.CreateEntitlementRequest;
    import com.google.cloud.channel.v1.Customer;
    import com.google.cloud.channel.v1.Entitlement;
    import com.google.cloud.channel.v1.ListOffersRequest;
    import com.google.cloud.channel.v1.Offer;
    import com.google.cloud.channel.v1.OperationMetadata;
    import com.google.cloud.channel.v1.Parameter;
    import com.google.cloud.channel.v1.PaymentPlan;
    import com.google.cloud.channel.v1.Period;
    import com.google.cloud.channel.v1.PeriodType;
    import com.google.cloud.channel.v1.ProvisionCloudIdentityRequest;
    import com.google.cloud.channel.v1.RenewalSettings;
    import com.google.cloud.channel.v1.Value;
    import com.google.gson.Gson;
    import com.google.type.PostalAddress;
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.Iterator;
    import java.util.concurrent.ExecutionException;
    
    /**
    * This is a basic example of provisioning a Google Workspace customer.
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
          throws Exception, IOException, ExecutionException, InterruptedException {
    
        // Set up credentials with user impersonation
        FileInputStream jsonKeyFileStream = new FileInputStream(JSON_KEY_FILE);
        GoogleCredentials  credentials = ServiceAccountCredentials.fromStream(jsonKeyFileStream)
                                            .createScoped("https://www.googleapis.com/auth/apps.order")
                                            .createDelegated(RESELLER_ADMIN_USER);
        // Create the API client
        CloudChannelServiceSettings serviceSettings =
            CloudChannelServiceSettings.newBuilder()
                .setCredentialsProvider(FixedCredentialsProvider.create(credentials))
                .build();
        client = CloudChannelServiceClient.create(serviceSettings);
    
        Offer selectedOffer = selectOffer();
    
        checkExists();
    
        Customer customer = createCustomer();
    
        Entitlement entitlement = createEntitlement(customer, selectedOffer);
    
        String adminSDKCustomerId = customer.getCloudIdentityId();
        System.out.println(adminSDKCustomerId);
      }
    
      private static Offer selectOffer() {
        ListOffersRequest request =
            ListOffersRequest.newBuilder().setParent(ACCOUNT_NAME).build();
    
        // For the purpose of this codelab, the code lists all offers and selects
        // the first offer for Google Workspace Business Standard on an Annual
        // plan. This is needed because offerIds vary from one account to another,
        // but this is not a recommended model for your production integration
        String sampleSkuName = "Google Workspace Business Standard";
        String samplePlan = "COMMITMENT";
    
        CloudChannelServiceClient.ListOffersPagedResponse response = client.listOffers(request);
        Offer selectedOffer = Offer.newBuilder().build();
        Iterator<Offer> iterator = response.iterateAll().iterator();
        while (iterator.hasNext()) {
          Offer offer = iterator.next();
          String skuName = offer.getSku().getMarketingInfo().getDisplayName();
          String offerPlan = offer.getPlan().getPaymentPlan().name();
          if (skuName.equals(sampleSkuName) && offerPlan.equals(samplePlan)) {
            selectedOffer = offer;
            break;
          }
        }
    
        System.out.println("=== Selected offer");
        System.out.println(gson.toJson(selectedOffer));
    
        return selectedOffer;
      }
    
      private static void checkExists() throws Exception {
        // Determine if customer already has a cloud identity
        CheckCloudIdentityAccountsExistRequest request =
            CheckCloudIdentityAccountsExistRequest.newBuilder()
                .setParent(ACCOUNT_NAME)
                .setDomain(CUSTOMER_DOMAIN)
                .build();
        CheckCloudIdentityAccountsExistResponse response =
            client.checkCloudIdentityAccountsExist(request);
    
        if (response.getCloudIdentityAccountsCount() > 0) {
          throw new Exception(
              "Cloud identity already exists. "
              + "Customer must be transferred. "
              + "Out of scope for this codelab");
        }
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
    
        CloudIdentityInfo cloudIdentityInfo =
            CloudIdentityInfo.newBuilder()
                .setAlternateEmail("john.doe@gmail.com")
                .setLanguageCode("en-US")
                .build();
    
        AdminUser adminUser =
            AdminUser.newBuilder()
                .setGivenName("John")
                .setFamilyName("Doe")
                .setEmail("admin@" + CUSTOMER_DOMAIN)
                .build();
    
        ProvisionCloudIdentityRequest cloudIdentityRequest =
            ProvisionCloudIdentityRequest.newBuilder()
                .setCustomer(customer.getName())
                .setCloudIdentityInfo(cloudIdentityInfo)
                .setUser(adminUser)
                .build();
    
        // This call returns a long-running operation.
        OperationFuture<Customer, OperationMetadata> operation =
            client.provisionCloudIdentityAsync(cloudIdentityRequest);
    
        // Wait for the long-running operation and get the result.
        customer = operation.get();
        System.out.println("=== Provisioned cloud identity");
    
        return customer;
      }
    
      private static Entitlement createEntitlement(Customer customer, Offer selectedOffer)
          throws InterruptedException, ExecutionException {
        RenewalSettings renewalSettings =
            RenewalSettings.newBuilder()
                // Setting renewal settings to auto renew
                .setEnableRenewal(true)
                .setPaymentPlan(PaymentPlan.COMMITMENT)
                .setPaymentCycle(
                    Period.newBuilder().setPeriodType(PeriodType.YEAR).setDuration(1).build())
                .build();
    
        CommitmentSettings commitmentSettings =
            CommitmentSettings.newBuilder().setRenewalSettings(renewalSettings).build();
    
        Entitlement entitlement =
            Entitlement.newBuilder()
                .setOffer(selectedOffer.getName())
                // Setting 5 seats for this Annual offer
                .addParameters(
                    Parameter.newBuilder()
                        .setName("num_units")
                        .setValue(Value.newBuilder().setInt64Value(5).build())
                        .build())
                .setCommitmentSettings(commitmentSettings)
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
    // https://cloud.google.com/channel/docs/codelabs/workspace/provisioning
    
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
    
      await checkExists();
    
      const customer = await createCustomer();
    
      const entitlement = await createEntitlement(customer, selectedOffer);
    
      const customerId = customer.cloudIdentityId;
      console.log(customerId);
    }
    
    async function selectOffer() {
      const [offers] = await client.listOffers({
        parent: accountName,
      });
    
      // For the purpose of this codelab, the code lists all offers and selects
      // the first offer for Google Workspace Business Standard on an Annual
      // plan. This is needed because offerIds vary from one account to another,
      // but this is not a recommended model for your production integration
      const selectedOffer = offers.find(o => {
        return (
          o.sku.marketingInfo.displayName ===
            'Google Workspace Business Standard' &&
          o.plan.paymentPlan === 'COMMITMENT'
        );
      });
    
      console.log('=== Selected offer');
      console.info(selectedOffer);
    
      return selectedOffer;
    }
    
    async function checkExists() {
      // Determine if customer already has a cloud identity
      const [
        cloudIdentityAccounts,
      ] = await client.checkCloudIdentityAccountsExist({
        parent: accountName,
        domain: customerDomain,
      });
    
      if (cloudIdentityAccounts.length > 0) {
        throw new Error(
          'Cloud identity already exists; ' +
            'customer must be transferred ' +
            '[out-of-scope of this codelab]'
        );
      }
    }
    
    async function createCustomer() {
      // Create the Customer resource
      let [customer] = await client.createCustomer({
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
    
      // This endpoint returns a long-running operation.
      // For other ways to get operation results, see
      // https://github.com/googleapis/gax-nodejs/blob/master/client-libraries.md#long-running-operations
      const [operation] = await client.provisionCloudIdentity({
        customer: customer.name,
        cloudIdentityInfo: {
          alternateEmail: 'john.doe@gmail.com',
          languageCode: 'en-US',
        },
        user: {
          givenName: 'John',
          familyName: 'Doe',
          email: `admin@${customerDomain}`,
        },
      });
    
      // Wait for the long-running operation and get the result.
      [customer] = await operation.promise();
      console.log('=== Provisioned cloud identity');
    
      return customer;
    }
    
    async function createEntitlement(customer, selectedOffer) {
      // This call returns a long-running operation.
      const [operation] = await client.createEntitlement({
        parent: customer.name,
        entitlement: {
          offer: selectedOffer.name,
          parameters: [
            // Setting 5 seats for this Annual offer
            {
              name: 'num_units',
              value: {
                int64Value: 5,
              },
            },
          ],
          commitmentSettings: {
            // Setting renewal settings to auto renew
            renewalSettings: {
              enableRenewal: true,
              paymentPlan: 'COMMITMENT',
              paymentCycle: {
                duration: 1,
                periodType: 'YEAR',
              },
            },
          },
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
    // https://cloud.google.com/channel/docs/codelabs/workspace/provisioning
    
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
    $client = new Channel\V1\Client\CloudChannelServiceClient([
      'credentials' => $credentials
    ]);
    
    $selectedOffer = selectOffer();
    
    checkExists();
    
    $customer = createCustomer();
    
    $entitlement = createEntitlement($customer, $selectedOffer);
    
    $customerId = $customer->getCloudIdentityId();
    print $customerId . PHP_EOL;
    
    function selectOffer() {
      global $client, $ACCOUNT_NAME;
    
      $request = new Channel\V1\ListOffersRequest(['parent' => $ACCOUNT_NAME]);
      $offers = $client->listOffers($request);
    
      // For the purpose of this codelab, the code lists all offers and selects
      // the first offer for Google Workspace Business Standard on an Annual
      // plan. This is needed because offerIds vary from one account to another,
      // but this is not a recommended model for your production integration
      $sampleSku = 'Google Workspace Business Standard';
      $samplePlan = Channel\V1\PaymentPlan::COMMITMENT;
      foreach ($offers as $offer) {
        if ($offer->getSku()->getMarketingInfo()->getDisplayName() == $sampleSku
        && $offer->getPlan()->getPaymentPlan() == $samplePlan) {
          $selectedOffer = $offer;
          break;
        }
      }
    
      print '=== Selected offer' . PHP_EOL;
      print $selectedOffer->serializeToJsonString() . PHP_EOL;
    
      return $selectedOffer;
    }
    
    function checkExists () {
      global $client, $ACCOUNT_NAME, $CUSTOMER_DOMAIN;
    
      // Determine if customer already has a cloud identity
      $request = new Channel\V1\CheckCloudIdentityAccountsExistsRequest([
        'parent' => $ACCOUNT_NAME,
        'domain' => $CUSTOMER_DOMAIN,
      ]);
      $response = $client->checkCloudIdentityAccountsExist($request);
    
      if (count($response->getCloudIdentityAccounts()) > 0) {
        throw new Error('Cloud identity already exists; \
          customer must be transferred \
          [out-of-scope of this codelab]'
        );
      }
    }
    
    function createCustomer() {
      global $client, $ACCOUNT_NAME, $CUSTOMER_DOMAIN;
    
      // Create the Customer resource
      $request = new Channel\V1\CreateCustomerRequest([
        'parent' => $ACCOUNT_NAME,
        'customer' => new Channel\V1\Customer([
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
      ]);
      $customer = $client->createCustomer($request);
    
      print '=== Created customer with id ' . $customer->getName() . PHP_EOL;
      print $customer->serializeToJsonString() . PHP_EOL;
    
    
      // This endpoint returns a long-running operation.
      $request = new Channel\V1\ProvisionCloudIdentityRequest([
        'customer' => $customer->getName() /* customer */,
        'cloud_identity_info' => new Channel\V1\CloudIdentityInfo([
          'alternate_email' => 'john.doe@gmail.com',
          'language_code' => 'en-US',
        ]),
        'user' => new Channel\V1\AdminUser([
          'given_name' => 'John',
          'family_name' => 'Doe',
          'email' => 'admin@' . $CUSTOMER_DOMAIN,
        ])
      ]);
      $operation = $client->provisionCloudIdentity($request);
    
      // Wait for the long-running operation and get the result.
      $operation->pollUntilComplete();
      $customer = $operation->getResult();
      print '=== Provisioned cloud identity' . PHP_EOL;
    
      return $customer;
    }
    
    function createEntitlement($customer, $selectedOffer) {
      global $client;
    
      // This call returns a long-running operation.
      $request = new Channel\V1\CreateEntitlementRequest([
        'parent' => $customer->getName(),
        'entitlement' => new Channel\V1\Entitlement([
          'offer' => $selectedOffer->getName(),
          'parameters' => [
            new Channel\V1\Parameter([
              // Setting 5 seats for this Annual offer
              'name' => 'num_units',
              'value' => new Channel\V1\Value([
                'int64_value' => 5,
              ])
            ]),
          ],
          'commitment_settings' => new Channel\V1\CommitmentSettings([
            // Setting renewal settings to auto renew
            'renewal_settings' => new Channel\V1\RenewalSettings([
              'enable_renewal' => true,
              'payment_plan' => Channel\V1\PaymentPlan::COMMITMENT,
              'payment_cycle' => new Channel\V1\Period([
                'duration' => 1,
                'period_type' => Channel\V1\PeriodType::YEAR,
              ]),
            ]),
          ]),
          // A string of up to 80 characters.
          // We recommend using an internal transaction ID or
          // identifier for the customer in this field.
          'purchase_order_id' => 'A codelab test'
        ])
      ]);
      $operation = $client->createEntitlement($request);
    
      // Wait for the long-running operation and get the result.
      $operation->pollUntilComplete();
      $entitlement = $operation->getResult();
      print '=== Created entitlement' . PHP_EOL;
      print $entitlement->serializeToJsonString() . PHP_EOL;
    
      return $entitlement;
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
    
    """Google Workspace Provisioning codelab.
    
    Instructions for this codelab can be found on this page:
    https://cloud.google.com/channel/docs/codelabs/workspace/provisioning
    """
    
    from google.cloud import channel
    from google.oauth2 import service_account
    
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
    
      check_exists()
    
      customer = create_customer()
    
      _ = create_entitlement(customer, offer)
    
      customer_id = customer.cloud_identity_id
      print(customer_id)
    
    
    def select_offer():
      """Selects a Workspace offer.
    
      Returns:
        A Channel API Offer for Workspace
      """
      request = channel.ListOffersRequest(parent=ACCOUNT_NAME)
      offers = client.list_offers(request)
    
      # For the purpose of this codelab, the code lists all offers and selects
      # the first offer for Google Workspace Business Standard on an Annual
      # plan. This is needed because offerIds vary from one account to another,
      # but this is not a recommended model for your production integration
      sample_offer = "Google Workspace Business Standard"
      sample_plan = "PaymentPlan.COMMITMENT"
      selected_offer = None
      for offer in offers:
        if offer.sku.marketing_info.display_name == sample_offer and \
            str(offer.plan.payment_plan) == sample_plan:
          selected_offer = offer
          break
    
      print("=== Selected offer")
      print(selected_offer)
    
      return selected_offer
    
    
    def check_exists():
      """Determine if customer already has a cloud identity.
    
      Raises:
        Exception: if the domain is already in use
      """
      # Determine if customer already has a cloud identity
      request = channel.CheckCloudIdentityAccountsExistRequest(
          parent=ACCOUNT_NAME, domain=CUSTOMER_DOMAIN)
    
      response = client.check_cloud_identity_accounts_exist(request)
    
      if response.cloud_identity_accounts:
        raise Exception(
            "Cloud identity already exists. Customer must be transferred." +
            "Out of scope for this codelab")
    
    
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
    
      cloud_identity_info = channel.CloudIdentityInfo(
          alternate_email="john.doe@gmail.com", language_code="en-US")
    
      admin_user = channel.AdminUser(
          given_name="John", family_name="Doe", email="admin@" + CUSTOMER_DOMAIN)
    
      cloud_identity_request = channel.ProvisionCloudIdentityRequest(
          customer=customer.name,
          cloud_identity_info=cloud_identity_info,
          user=admin_user)
    
      # This call returns a long-running operation.
      operation = client.provision_cloud_identity(cloud_identity_request)
    
      # Wait for the long-running operation and get the result.
      customer = operation.result()
    
      print("=== Provisioned cloud identity")
    
      return customer
    
    
    def create_entitlement(customer, selected_offer):
      """Create the Entitlement.
    
      Args:
        customer: a Customer resource
        selected_offer: an Offer
    
      Returns:
        The created Channel API Entitlement
      """
      request = channel.CreateEntitlementRequest(
          parent=customer.name,
          entitlement={
              "offer": selected_offer.name,
              # Setting 5 seats for this Annual offer
              "parameters": [{
                  "name": "num_units",
                  "value": {
                      "int64_value": 5
                  }
              }],
              "commitment_settings": {
                  "renewal_settings": {
                      # Setting renewal settings to auto renew
                      "enable_renewal": True,
                      "payment_plan": "COMMITMENT",
                      "payment_cycle": {
                          "period_type": "YEAR",
                          "duration": 1
                      }
                  }
              },
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
    
    # Instructions for this codelab can be found on this page
    # https://cloud.google.com/channel/docs/codelabs/workspace/provisioning
    
    require 'google-cloud-channel'
    
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
      scope: 'https://www.googleapis.com/auth/apps.order'
    )
    credentials.sub = RESELLER_ADMIN_USER
    
    # Create the API client
    CLIENT = Google::Cloud::Channel::cloud_channel_service do |config|
      config.credentials = credentials
    end
    
    def main
      offer = select_offer
      check_exists
      customer = create_customer
      create_entitlement(customer, offer)
      customer_id = customer.cloud_identity_id
      puts(customer_id)
    end
    
    def select_offer
      # For the purpose of this codelab, the code lists all offers and selects
      # the first offer for Google Workspace Business Standard on an Annual
      # plan. This is needed because offerIds vary from one account to another,
      # but this is not a recommended model for your production integration
    
      request = Google::Cloud::Channel::V1::ListOffersRequest.new({ parent: ACCOUNT_NAME })
      offers = CLIENT.list_offers(request)
      sample_offer = 'Google Workspace Business Standard'
      sample_plan = :COMMITMENT
    
      offer = offers.detect { |offer| offer.sku.marketing_info.display_name == sample_offer
        && offer.plan.payment_plan == sample_plan }
      puts("=== Selected offer")
      puts(offer.inspect)
      offer
    end
    
    def check_exists
      # Determine if customer already has a cloud identity
      request = Google::Cloud::Channel::V1::CheckCloudIdentityAccountsExistRequest
      .new({ parent: ACCOUNT_NAME, domain: CUSTOMER_DOMAIN })
      response = CLIENT.check_cloud_identity_accounts_exist(request)
    
      if response.cloud_identity_accounts.count > 0
        raise 'Cloud identity already exists. Customer must be transferred.'\
          'Out of scope for this codelab'
      end
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
    
      cloud_identity_info = Google::Cloud::Channel::V1::CloudIdentityInfo.new(
        alternate_email: 'john.doe@gmail.com', language_code: 'en-US'
      )
    
      admin_user = Google::Cloud::Channel::V1::AdminUser.new(
        given_name: 'John', family_name: 'Doe', email: "admin@#{CUSTOMER_DOMAIN}"
      )
    
      cloud_identity_request = Google::Cloud::Channel::V1::ProvisionCloudIdentityRequest.new(
        customer: customer.name,
        cloud_identity_info: cloud_identity_info,
        user: admin_user
      )
    
      # This call returns a long-running operation.
      operation = CLIENT.provision_cloud_identity(cloud_identity_request)
    
      # Wait for the long-running operation and get the result.
      CLIENT.operations_client.wait_operation(Google::Longrunning::WaitOperationRequest
        .new({ name: operation.name }))
      operation = CLIENT.operations_client.get_operation(Google::Longrunning::GetOperationRequest
        .new({ name: operation.name }))
      customer = operation.response
      puts("=== Provisioned cloud identity")
    
      customer
    end
    
    def create_entitlement(customer, selected_offer)
      request = Google::Cloud::Channel::V1::CreateEntitlementRequest.new(
        parent: customer.name,
        entitlement: {
          offer: selected_offer.name,
          # Setting 5 seats for this Annual offer
          parameters: [{
                         name: 'num_units',
                         value: {
                           int64_value: 5
                         }
                       }],
          commitment_settings: {
            renewal_settings: {
              # Setting renewal settings to auto renew
              enable_renewal: true,
              payment_plan: 'COMMITMENT',
              payment_cycle: {
                period_type: 'YEAR',
                duration: 1
              }
            }
          },
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
    
    main

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
