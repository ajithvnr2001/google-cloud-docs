---
url: https://docs.cloud.google.com/compute/docs/instances/view-future-reservations/
title: View reservations or future reservation requests \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:20.846606+00:00
---

# View reservations or future reservation requests  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-future-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View reservations or future reservation requests Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to view your reservations, future reservation requests, and reservation consumption. To learn more about reservations, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

When you view your reservations, future reservation requests, or reservation consumption, you can do the following:

  * **View reservation settings**. This review helps you verify the details of your reservations, ensure that they meet your needs, and plan for capacity.

  * **Determine the number of consumable instances**. This check helps you determine how many Compute Engine instances can consume your reserved capacity.

  * **View reservation consumption**. This review lets you verify which reservation a specific Compute Engine instance is consuming, or list all instances that are consuming a particular reservation within a project.




## Limitations

You can only view a shared reservation or shared future reservation request in the project where you created it.

## Before you begin

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

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to view reservations or future reservation requests, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view reservations or future reservation requests. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view reservations or future reservation requests:

  * To view a list of reservations: `compute.reservations.list` on the project 
  * To view a list of future reservation requests: `compute.futureReservations.list` on the project 
  * To view the details of a reservation: `compute.reservations.get` on the project 
  * To view the details of a future reservation request: `compute.futureReservations.get` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View reservation settings

The following sections explain how to view the settings of your reservations or future reservation requests.

### View reservations

To view the settings of one or more reservations, use one of the following methods described in this section:

  * To view an overview of all reservations in your project, view a list of your reservations.

  * To view the full details of a single reservation, view the details of the reservation.




To view the `deleteAtTime` and `reservationSharingPolicy` fields ([Preview](https://cloud.google.com/products#product-launch-stages)) in a reservation, view the details of a reservation using the Google Cloud CLI, or view reservations using the REST API. If you don't require these fields, then view reservations by selecting any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

On the **On-demand reservations** tab (default), the table lists each reservation, and each table column describes a property.

  2. Optional: In the **On-demand reservations** table, do one or both of the following:

     * To display the assured count of your reservations, click view_column **Column display options...** , select the **Assured count** checkbox, and then click **OK**.

     * To refine your list of reservations, in the filter_list **Filter** field, select the properties that you want to filter the reservations by.

  3. To view the details of a reservation, in the **Name** column, click the name of the reservation. A page that gives the details of the reservation opens.




###  gcloud 

  * To view a list of your reservations, use the [`gcloud compute reservations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/list):
        
        gcloud compute reservations list
        

The output is similar to the following example:
        
        NAME: r-01
        IN_USE_COUNT: 0
        COUNT: 5
        ZONE: us-central1-a
        SHARE_TYPE: LOCAL
        
        NAME: r-02
        IN_USE_COUNT: 3
        COUNT: 10
        ZONE: us-central1-f
        SHARE_TYPE: LOCAL
        

Optionally, to refine a list of reservations using a [filter expression](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters#Filter-Expressions), include the `--filter` flag:
        
        gcloud compute reservations list \
            --filter="FILTER_EXPRESSION"
        

Replace `FILTER_EXPRESSION` with a filter expression.

  * To view the details of a reservation, use the [`gcloud compute reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/describe):

**Note:** To view the `deleteAtTime` and `reservationSharingPolicy` fields in a reservation, use the [`gcloud beta compute reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/describe).
        
        gcloud compute reservations describe RESERVATION_NAME \
            --zone=ZONE
        

Replace the following:

    * `RESERVATION_NAME`: the name of an existing reservation.

    * `ZONE`: the zone where the reservation exists.

The output is similar to the following example:
    
    creationTimestamp: '2024-10-11T03:25:23.192-07:00'
    id: '4488228526648280060'
    kind: compute#reservation
    name: r-01
    selfLink: https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/reservations/r-01
    shareSettings:
      shareType: LOCAL
    specificReservation:
      assuredCount: '50'
      count: '50'
      inUseCount: '25'
      instanceProperties:
        machineType: n2-standard-2
    specificReservationRequired: false
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a
    




###  Go 

  * To view a list of your reservations, use the following code sample:
        
        // Copyright 2024 Google LLC
        //
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
        
        package snippets
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	compute "cloud.google.com/go/compute/apiv1"
        	computepb "cloud.google.com/go/compute/apiv1/computepb"
        	"google.golang.org/api/iterator"
        )
        
        // Get list of reservations for given project in particular zone
        func listReservations(w io.Writer, projectID, zone string) error {
        	// projectID := "your_project_id"
        	// zone := "us-west3-a"
        
        	ctx := context.Background()
        	reservationsClient, err := compute.[NewReservationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ReservationsClient_NewReservationsRESTClient)(ctx)
        	if err != nil {
        		return err
        	}
        	defer reservationsClient.Close()
        
        	req := &computepb.ListReservationsRequest{
        		Project: projectID,
        		Zone:    zone,
        	}
        
        	it := reservationsClient.List(ctx, req)
        	fmt.Fprintf(w, "Instances found in zone %s:\n", zone)
        	for {
        		instance, err := it.Next()
        		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
        			break
        		}
        		if err != nil {
        			return err
        		}
        		fmt.Fprintf(w, "- %s %d\n", instance.GetName(), instance.GetSpecificReservation().GetCount())
        	}
        
        	return nil
        }
        
        

  * To view the details of a reservation, use the following code sample:
        
        // Copyright 2024 Google LLC
        //
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
        
        package snippets
        
        import (
        	"context"
        	"fmt"
        	"io"
        
        	compute "cloud.google.com/go/compute/apiv1"
        	computepb "cloud.google.com/go/compute/apiv1/computepb"
        )
        
        // Get certain reservation for given project and zone
        func getReservation(w io.Writer, projectID, zone, reservationName string) (*computepb.Reservation, error) {
        	// projectID := "your_project_id"
        	// zone := "us-west3-a"
        	// reservationName := "your_reservation_name"
        
        	ctx := context.Background()
        	reservationsClient, err := compute.[NewReservationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ReservationsClient_NewReservationsRESTClient)(ctx)
        	if err != nil {
        		return nil, err
        	}
        	defer reservationsClient.Close()
        
        	req := &computepb.GetReservationRequest{
        		Project:     projectID,
        		Reservation: reservationName,
        		Zone:        zone,
        	}
        
        	reservation, err := reservationsClient.Get(ctx, req)
        	if err != nil {
        		return nil, fmt.Errorf("unable to delete reservation: %w", err)
        	}
        
        	fmt.Fprintf(w, "Reservation: %s\n", reservation.GetName())
        
        	return reservation, nil
        }
        
        




###  Java 

  * To view a list of your reservations, use the following code sample:
        
        /*
         * Copyright 2024 Google LLC
         *
         * Licensed under the Apache License, Version 2.0 (the "License");
         * you may not use this file except in compliance with the License.
         * You may obtain a copy of the License at
         *
         *   http://www.apache.org/licenses/LICENSE-2.0
         *
         * Unless required by applicable law or agreed to in writing, software
         * distributed under the License is distributed on an "AS IS" BASIS,
         * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         * See the License for the specific language governing permissions and
         * limitations under the License.
         */
        
        package compute.reservation;
        
        import com.google.cloud.compute.v1.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html);
        import com.google.cloud.compute.v1.[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html);
        import java.io.IOException;
        import java.util.ArrayList;
        import java.util.List;
        
        public class ListReservations {
        
          public static void main(String[] args) throws IOException {
            // TODO(developer): Replace these variables before running the sample.
            // Project ID or project number of the Cloud project you want to use.
            String project = "YOUR_PROJECT_ID";
            // Zone in which reservations are located.
            String zone = "us-central1-a";
        
            listReservations(project, zone);
          }
        
          // List all reservations in the given project and zone.
          public static List<Reservation> listReservations(String project, String zone) throws IOException {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            List<Reservation> listOfReservations = new ArrayList<>();
        
            try ([ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html) reservationsClient = [ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html).create()) {
              for ([Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html) reservation : reservationsClient.list(project, zone).iterateAll()) {
                listOfReservations.add(reservation);
                System.out.println("Reservation: " + reservation.getName());
              }
            }
            return listOfReservations;
          }
        }

  * To view the details of a reservation, use the following code sample:
        
        /*
         * Copyright 2024 Google LLC
         *
         * Licensed under the Apache License, Version 2.0 (the "License");
         * you may not use this file except in compliance with the License.
         * You may obtain a copy of the License at
         *
         * http://www.apache.org/licenses/LICENSE-2.0
         *
         * Unless required by applicable law or agreed to in writing, software
         * distributed under the License is distributed on an "AS IS" BASIS,
         * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         * See the License for the specific language governing permissions and
         * limitations under the License.
         */
        
        package compute.reservation;
        
        import com.google.cloud.compute.v1.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html);
        import com.google.cloud.compute.v1.[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html);
        import java.io.IOException;
        import java.util.concurrent.ExecutionException;
        import java.util.concurrent.TimeoutException;
        
        public class GetReservation {
        
          public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
            // TODO(developer): Replace these variables before running the sample.
            // Project ID or project number of the Cloud project you want to use.
            String projectId = "YOUR_PROJECT_ID";
            // Name of the zone in which you want to create the reservation.
            String zone = "us-central1-a";
            // Name of the reservation you want to create.
            String reservationName = "test-reservation-name";
        
            getReservation(projectId, reservationName, zone);
          }
        
          // Retrieve a reservation with the given name in the given zone.
          public static [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html) getReservation(
              String projectId, String reservationName, String zone)
              throws IOException {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            try ([ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html) reservationsClient = [ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html).create()) {
        
              // Get the reservation.
              [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html) reservation = reservationsClient.get(projectId, zone, reservationName);
        
              System.out.println("Reservation: " + reservation.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html#com_google_cloud_compute_v1_Reservation_getName__)());
              return reservation;
            }
          }
        }




###  Node.js 

  * To view a list of your reservations, use the following code sample:
        
        /*
         * Copyright 2024 Google LLC
         *
         * Licensed under the Apache License, Version 2.0 (the "License");
         * you may not use this file except in compliance with the License.
         * You may obtain a copy of the License at
         *
         *     https://www.apache.org/licenses/LICENSE-2.0
         *
         * Unless required by applicable law or agreed to in writing, software
         * distributed under the License is distributed on an "AS IS" BASIS,
         * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         * See the License for the specific language governing permissions and
         * limitations under the License.
         */
        
        'use strict';
        
        async function main() {
          // Import the Compute library
          const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
        
          // Instantiate a reservationsClient
          const reservationsClient = new computeLib.[ReservationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
        
          /**
           * TODO(developer): Update these variables before running the sample.
           */
          // The ID of the project where your reservations are located.
          const projectId = await reservationsClient.getProjectId();
          // The zone where your reservations are located.
          const zone = 'us-central1-a';
        
          async function callGetReservations() {
            const reservations = (
              await reservationsClient.list({
                project: projectId,
                zone,
              })
            )[0];
        
            console.log(JSON.stringify(reservations));
          }
        
          await callGetReservations();
        }
        
        main().catch(err => {
          console.error(err);
          process.exitCode = 1;
        });
        

  * To view the details of a reservation, use the following code sample:
        
        /*
         * Copyright 2024 Google LLC
         *
         * Licensed under the Apache License, Version 2.0 (the "License");
         * you may not use this file except in compliance with the License.
         * You may obtain a copy of the License at
         *
         *     https://www.apache.org/licenses/LICENSE-2.0
         *
         * Unless required by applicable law or agreed to in writing, software
         * distributed under the License is distributed on an "AS IS" BASIS,
         * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
         * See the License for the specific language governing permissions and
         * limitations under the License.
         */
        
        'use strict';
        
        async function main(reservationName) {
          // Import the Compute library
          const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
        
          // Instantiate a reservationsClient
          const reservationsClient = new computeLib.[ReservationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
        
          /**
           * TODO(developer): Update/uncomment these variables before running the sample.
           */
          // The ID of the project where your reservation is located.
          const projectId = await reservationsClient.getProjectId();
          // The zone where your reservation is located.
          const zone = 'us-central1-a';
          // The name of the reservation to return.
          // reservationName = 'reservation-01';
        
          async function callGetReservation() {
            const requestedReservation = (
              await reservationsClient.get({
                project: projectId,
                zone,
                reservation: reservationName,
              })
            )[0];
        
            console.log(JSON.stringify(requestedReservation));
          }
        
          await callGetReservation();
        }
        
        main(...process.argv.slice(2)).catch(err => {
          console.error(err);
          process.exitCode = 1;
        });
        




###  Python 

  * To view a list of your reservations, use the following code sample:
        
        # Copyright 2024 Google LLC
        #
        # Licensed under the Apache License, Version 2.0 (the "License");
        # you may not use this file except in compliance with the License.
        # You may obtain a copy of the License at
        #
        #    https://www.apache.org/licenses/LICENSE-2.0
        #
        # Unless required by applicable law or agreed to in writing, software
        # distributed under the License is distributed on an "AS IS" BASIS,
        # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        # See the License for the specific language governing permissions and
        # limitations under the License.
        
        
        # This file is automatically generated. Please do not modify it directly.
        # Find the relevant recipe file in the samples/recipes or samples/ingredients
        # directory and apply your changes there.
        
        
        from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
        from google.cloud.compute_v1.services.reservations.pagers import ListPager
        
        
        def list_compute_reservation(project_id: str, zone: str = "us-central1-a") -> ListPager:
            """
            Lists all compute reservations in a specified Google Cloud project and zone.
            Args:
                project_id (str): The ID of the Google Cloud project.
                zone (str): The zone of the reservations.
            Returns:
                ListPager: A pager object containing the list of reservations.
            """
        
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ReservationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html)()
        
            reservations_list = client.[list](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html#google_cloud_compute_v1_services_reservations_ReservationsClient_list)(
                project=project_id,
                zone=zone,
            )
        
            for reservation in reservations_list:
                print("Name: ", reservation.name)
                print(
                    "Machine type: ",
                    reservation.specific_reservation.instance_properties.machine_type,
                )
            # Example response:
            # Name:  my-reservation_1
            # Machine type:  n1-standard-1
            # Name:  my-reservation_2
            # Machine type:  n1-standard-1
        
            return reservations_list
        
        
        

  * To view the details of a reservation, use the following code sample:
        
        # Copyright 2024 Google LLC
        #
        # Licensed under the Apache License, Version 2.0 (the "License");
        # you may not use this file except in compliance with the License.
        # You may obtain a copy of the License at
        #
        #    https://www.apache.org/licenses/LICENSE-2.0
        #
        # Unless required by applicable law or agreed to in writing, software
        # distributed under the License is distributed on an "AS IS" BASIS,
        # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
        # See the License for the specific language governing permissions and
        # limitations under the License.
        
        
        # This file is automatically generated. Please do not modify it directly.
        # Find the relevant recipe file in the samples/recipes or samples/ingredients
        # directory and apply your changes there.
        
        
        from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
        from google.cloud.compute_v1.types import compute
        
        
        def get_compute_reservation(
            project_id: str,
            zone: str = "us-central1-a",
            reservation_name="your-reservation-name",
        ) -> compute.Reservation:
            """
            Retrieves a compute reservation from GCP.
            Args:
                project_id (str): The ID of the Google Cloud project.
                zone (str): The zone of the reservation.
                reservation_name (str): The name of the reservation to retrieve.
            Returns:
                compute.Reservation: The reservation object retrieved from Google Cloud.
            """
        
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ReservationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html)()
        
            reservation = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html#google_cloud_compute_v1_services_reservations_ReservationsClient_get)(
                project=project_id,
                zone=zone,
                reservation=reservation_name,
            )
        
            print("Name: ", reservation.name)
            print("STATUS: ", reservation.status)
            print(reservation.specific_reservation)
            # Example response:
            # Name:  your-reservation-name
            # STATUS:  READY
            # count: 3
            # instance_properties {
            #   machine_type: "n1-standard-1"
            #   local_ssds {
            #     disk_size_gb: 375
            #     interface: "NVME"
            #   }
            # ...
        
            return reservation
        
        
        




###  REST 

  * To view a list of your reservations, make a `GET` request to the [`reservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/list):

**Note:** To view the `deleteAtTime` and `reservationSharingPolicy` fields in your reservations, make a `GET` request to the [beta `reservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/list).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you created your reservations.

    * `ZONE`: the zone where your reservations exist.

The output is similar to the following example:
    
    {
      "kind": "compute#reservation",
      "id": "4100668622331754141",
      "creationTimestamp": "2019-09-27T08:21:14.707-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/reservations/reservation-05",
      "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a",
      "name": "reservation-05",
      "specificReservation": {
        "instanceProperties": {
          "machineType": "n1-standard-2"
        },
        "count": "100",
        "inUseCount": "0",
        "assuredCount": "100"
      },
      "specificReservationRequired": false,
      "status": "READY",
      "shareSettings": {
        "shareType": "LOCAL"
      }
    },
    {
      "kind": "compute#reservation",
      "id": "2533514314332214789",
      "creationTimestamp": "2019-09-27T08:21:14.707-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/reservations/reservation-04",
      "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a",
      "name": "reservation-04",
      "specificReservation": {
        "instanceProperties": {
          "machineType": "n1-standard-2",
          "guestAccelerators": [
            {
              "acceleratorType": "nvidia-tesla-t4",
              "acceleratorCount": 1
            }
          ],
          "localSsds": [
            {
              "diskSizeGb": "375",
              "interface": "SCSI"
            }
          ]
        },
        "count": "50",
        "inUseCount": "25",
        "assuredCount": "50"
      },
      "specificReservationRequired": false,
      "status": "READY",
      "shareSettings": {
        "shareType": "LOCAL"
      }
    }
    

Optionally, to refine a list of reservations using a [filter expression](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/list#body.QUERY_PARAMETERS.filter), include the `filter` query parameter:
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations**?filter= FILTER_EXPRESSION**
    

Replace `FILTER_EXPRESSION` with a filter expression that uses [URL-encoded values](https://en.wikipedia.org/wiki/URL_encoding).

  * To view the details of a reservation, make a `GET` request to the [`reservations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/get).

**Note:** To view the `deleteAtTime` and `reservationSharingPolicy` fields in a reservation, make a `GET` request to the [`beta.reservations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/get).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you created the reservation.

    * `ZONE`: the zone where the reservation exists.

    * `RESERVATION_NAME`: the name of an existing reservation.

The output is similar to the following example:
    
    {
      "kind": "compute#reservation",
      "id": "4488228526648280060",
      "creationTimestamp": "2024-10-11T03:25:23.192-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/davide-experimental/zones/us-central1-a/reservations/r-01",
      "zone": "https://www.googleapis.com/compute/v1/projects/davide-experimental/zones/us-central1-a",
      "name": "r-01",
      "specificReservation": {
        "instanceProperties": {
          "machineType": "n2-standard-2"
        },
        "count": "50",
        "inUseCount": "25",
        "assuredCount": "50"
      },
      "specificReservationRequired": false,
      "status": "READY",
      "shareSettings": {
        "shareType": "LOCAL"
      }
    }
    




### View future reservation requests

To view the settings of one or more future reservation requests, use one of the following methods described in this section:

  * To view an overview of all future reservation requests in your project, view a list of your requests.

  * To view the full details of a single future reservation request, view the details of the request.




To view future reservation requests, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

The table lists each future reservation request, and each table column describes a property.

  3. Optional: To refine your list of requests, in the filter_list **Filter** field, select the properties that you want to filter the requests by.

  4. To view the details of a request, in the **Name** column, click the name of the request. A page that gives the details of the future reservation request opens.




###  gcloud 

  * To view a list of your future reservation requests, use the [`gcloud compute future-reservations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/list):
        
        gcloud compute future-reservations list
        

The output is similar to the following example:
        
        NAME: fr-04
        TOTAL_COUNT: 100
        START_TIME: 2025-07-20T07:00:00Z
        END_TIME: 2025-08-05T07:00:00Z
        PROCUREMENT_STATUS: FULFILLED
        ZONE: us-east1-a
        
        NAME: fr-05
        TOTAL_COUNT: 10
        START_TIME: 2025-07-20T07:00:00Z
        END_TIME: 2025-12-01T00:00:00Z
        PROCUREMENT_STATUS: PENDING_APPROVAL
        ZONE: us-west1-c
        

Optionally, to refine a list of future reservation requests using a [filter expression](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters#Filter-Expressions), include the `--filter` flag:
        
        gcloud compute future-reservations list \
            --filter="FILTER_EXPRESSION"
        

Replace `FILTER_EXPRESSION` with a filter expression.

  * To view the details of a future reservation request, use the [`gcloud compute future-reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/describe):
        
        gcloud compute future-reservations describe FUTURE_RESERVATION_NAME \
            --zone=ZONE
        

Replace the following:

    * `FUTURE_RESERVATION_NAME`: the name of an existing future reservation request.

    * `ZONE`: the zone where the future reservation request exists.

The output is similar to the following example:
    
    autoCreatedReservationsDeleteTime: '2025-05-02T01:00:00Z'
    creationTimestamp: '2025-03-23T10:08:31.613-07:00'
    id: '5212276518668495076'
    kind: compute#futureReservation
    name: fr-01
    planningStatus: SUBMITTED
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/futureReservations/fr-01
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/futureReservations/5212276518668495076
    shareSettings:
      shareType: LOCAL
    specificSkuProperties:
      instanceProperties:
        machineType: n1-standard-64
      totalCount: '800'
    status:
      existingMatchingUsageInfo:
        count: '3'
        timestamp: '2025-03-30T01:00:00Z'
      lockTime: '2025-03-30T17:09:59.297799Z'
      procurementStatus: APPROVED
    timeWindow:
      endTime: '2025-05-02T01:00:00Z'
      startTime: '2025-04-30T17:30:00Z'
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a
    




###  REST 

  * To view a list of your future reservation requests, make a `GET` request to the [`futureReservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/list):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you created your future reservation requests.

    * `ZONE`: the zone where your future reservation requests exist.

The output is similar to the following example:
    
    {
      "id": "projects/my-project/zones/us-east1-a/futureReservations",
      "items": [
        {
          "id": "743865190848184978",
          "creationTimestamp": "2025-03-23T18:16:45.274-07:00",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-east1-a/futureReservations/fr-base",
          "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-east1-a/futureReservations/743865190848184978",
          "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-east1-a",
          "name": "fr-base",
          "specificSkuProperties": {
            "instanceProperties": {
              "machineType": "n1-standard-1"
            },
            "totalCount": "100"
          },
          "planningStatus": "SUBMITTED",
          "timeWindow": {
            "endTime": "2025-05-02T01:00:00Z",
            "startTime": "2025-04-30T17:30:00Z"
          },
          "status": {
            "procurementStatus": "FULFILLED",
            "lockTime": "2025-03-30T07:00:00Z",
            "existingMatchingUsageInfo": {
              "count": "3",
              "timestamp": "2025-03-30T01:00:00Z"
            }
          },
          "kind": "compute#futureReservation"
        },
        ...
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-east1-a/futureReservations",
      "etag": "AnzKY34l-cvvV-JnniESJ0dtQvQ=/hvc4jaHpxFAZmOt1FVtKNgzZu-M=",
      "kind": "compute#futureReservationsListResponse"
    }
    

Optionally, to refine a list of future reservation requests using a [filter expression](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/list#body.QUERY_PARAMETERS.filter), include the `filter` query parameter:
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/futureReservations**?filter= FILTER_EXPRESSION**
    

Replace `FILTER_EXPRESSION` with a filter expression that uses [URL-encoded values](https://en.wikipedia.org/wiki/URL_encoding).

  * To view the details of a future reservation request, make a `GET` request to the [`futureReservations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/get):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME
        

Replace the following:

    * `PROJECT_ID`: the ID of the project where you created the future reservation request.

    * `ZONE`: the zone where the future reservation request exists.

    * `FUTURE_RESERVATION_NAME`: the name of an existing future reservation request.

The output is similar to the following:
    
    {
      "autoCreatedReservationsDeleteTime": "2025-05-02T01:00:00Z",
      "creationTimestamp": "2025-03-23T10:08:31.613-07:00",
      "id": "5212276518668495076",
      "kind": "compute#futureReservation",
      "name": "fr-01",
      "planningStatus": "SUBMITTED",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/futureReservations/fr-01",
      "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/futureReservations/5212276518668495076",
      "shareSettings": {
        "shareType": "LOCAL"
      },
      "specificSkuProperties": {
        "instanceProperties": {
          "machineType": "n1-standard-64"
        },
        "totalCount": "800"
      },
      "status": {
        "lockTime": "2025-03-30T17:09:59.297799Z",
        "procurementStatus": "APPROVED",
        "existingMatchingUsageInfo": {
          "count": "3",
          "timestamp": "2025-03-30T01:00:00Z"
        }
      },
      "timeWindow": {
        "endTime": "2025-05-02T01:00:00Z",
        "startTime": "2025-04-30T17:30:00Z"
      },
      "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a"
    }
    




## Determine the number of consumable instances

To determine the number of compute instances that can consume your reserved capacity, do one of the following:

  * To view the maximum number of instances that can consume a reservation, see Consumable instances in a reservation.

  * To view the number of instances that Compute Engine is set to reserve for a future reservation request at the request start time, see Consumable instances in a future reservation request.

  * To view the number of instances that Compute Engine is set to reserve for a future reservation request in calendar mode at the request start time, see Consumable instances in a future reservation request in calendar mode.




### Consumable instances in a reservation

When you view the details of a reservation, you can view how many compute instances are consuming the reservation, and how many instances can consume it, by checking the following fields:

  * **Assured count (`assuredCount`)**: the number of instances that are physically reserved within the zone of the reservation. This number includes the instances reserved for your project, and for any project a shared reservation is shared with.

  * **Total count (`count`)**: the number of reserved instances specified in the reservation. This number should match the assured count.

**Caution:** If the assured count is lower than the total count, then fewer instances than expected are reserved. To troubleshoot this issue, see [Fewer VMs available for consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption#fewer-vms-available).
  * **Machines in use (`inUseCount`)**: the number of running instances in your project, or a project a shared reservation is shared with, that are consuming the reservation.




For example, if the assured count (`assuredCount`) and total count (`count`) are both 50, and the number of instances consuming the reservation (`inUseCount`) is 25, then 25 more instances can consume the reservation before it's fully consumed.

### Consumable instances in a future reservation request

You can determine the number of compute instances for which Compute Engine creates a reservation at a future reservation request start time. For a draft, pending approval, or approved request, you can determine this number as follows:

  1. View how many running instances and unused reservations in your project, and in any project the request is shared with, match the request properties.

  2. Subtract the number of matching running instances and unused reservations from the [total count](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#total-count) in the request.




You can determine the number of consumable instances for single or multiple requests at once. For multiple requests, use the Google Cloud console or REST API. For single requests, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

The table lists each future reservation request, and each table column describes a property.

  3. To determine the number of instances that Compute Engine plans to reserve for a request at its start time, subtract the **Matching count** column from the **Total count** column.

The **Matching count** column shows one of the following warnings:

     * **Matching count is zero** : there are no matching running instances or unused reservations in your project, or in any project that your request is shared with.

     * **Matching count equals Total count** : Compute Engine won't reserve any instances for your request at its star time.

If you [modify a request](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations), or create new instances or reservations that match the request, then Compute Engine updates the **Matching count** column within 30 minutes.

  4. Optional: To check when the **Matching count** column was last updated in a request, do the following:

     1. In the **Name** column, click the name of the request. A page that gives the details of the future reservation request opens.

     2. In the **Resource details** section, check the **Last matching usage evaluation time** field.




###  gcloud 

  1. To view the details of a future reservation request, use the [`gcloud compute future-reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/describe):
         
         gcloud compute future-reservations describe FUTURE_RESERVATION_NAME \
             --zone=ZONE
         

Replace the following:

     * `FUTURE_RESERVATION_NAME`: the name of an existing future reservation request.

     * `ZONE`: the zone where the future reservation request exists.

In the output, find the `count` and `totalCount` fields:
    
    ...
    specificSkuProperties:
      ...
      **totalCount: '100'**
    status:
      existingMatchingUsageInfo:
        **count: '50'**
        timestamp: '2025-03-30T01:00:00Z'
      ...
      procurementStatus: DRAFTING
    ...
    

  2. Subtract the value of `count` from `totalCount`. For example, if `count` is 50 and `totalCount` is 100, then Compute Engine automatically creates a reservation for 50 instances at the request start time.

If you [modify the request](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations), or create new instances or reservations that match the request, then Compute Engine updates the `existingMatchingUsageInfo` field within 30 minutes. To verify when this field was last updated, check the value of `existingMatchingUsageInfo.timestamp`.




###  REST 

  1. To view a list of your future reservation requests, make a `GET` request to the [`futureReservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/list). In the request URL, include the `filter` query parameter and specify to show only the `name`, `specificSkuProperties`, and `status` fields:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations?fields=items.name,items.specificSkuProperties,items.status
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where you created your future reservation requests.

     * `ZONE`: the zone where the future reservation request exists.

In the output, find the `count` and `totalCount` fields for each draft, pending approval, or approved request:
    
    {
      "items": [
        {
          "specificSkuProperties": {
            ...
            **totalCount: "100"**
          },
          "name": "fr-01",
          "status": {
            "procurementStatus": "APPROVED",
            ...
            existingMatchingUsageInfo: {
              **count: "50"** ,
              "timestamp": "2025-01-22T07:54:26.295Z"
            }
          }
        },
        {
          "specificSkuProperties": {
            ...
            **totalCount: "20"**
          },
          "name": "fr-02",
          "status": {
            "procurementStatus": "DRAFTING",
            ...
            existingMatchingUsageInfo: {
              **"count": "2"** ,
              "timestamp": "2025-01-22T07:54:26.295Z"
            }
          }
        }
      ]
    }
    

  2. For each request, subtract the value of `count` from `totalCount`. For example, if `count` is 50 and `totalCount` is 100, then Compute Engine automatically creates a reservation for 50 instances at the request start time.

If you [modify a request](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations), or create new instances or reservations that match the request, then Compute Engine updates the `existingMatchingUsageInfo` field within 30 minutes. To verify when this field was last updated, check the value of `existingMatchingUsageInfo.timestamp`.




### Consumable instances in a future reservation request in calendar mode

When you view the details of a future reservation request, you can see how many compute instances Compute Engine plans to provision at the request start time. Compute Engine creates the number of instances specified in the request, regardless of the number of matching instances in your project or in any project that the request is shared with.

## View reservation consumption

Whenever a compute instance consumes a reservation, you can view the following:

  * View the reservation that an instance is consuming
  * View a list of instances that are consuming a reservation



### View the reservation that an instance is consuming

To view the reservation that an instance is consuming, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance that is consuming a reservation that you want to view.

  3. In the **Basic information** section, the **Consumed reservation** field shows the name of the reservation that the instance is consuming.




###  gcloud 

To view the reservation that an instance is consuming, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) with the `--flatten=resourceStatus.reservationConsumptionInfo` flag:
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --flatten=resourceStatus.reservationConsumptionInfo \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `ZONE`: the zone where the instance exists.



You see an output that is similar to the following:
    
    
    consumedReservation: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-c/reservations/example-reservation
    

###  REST 

To view the reservation that an instance is consuming, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get). In the request URL, include the `fields` query parameter set to `resourceStatus.reservationConsumptionInfo`:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?fields=resourceStatus.reservationConsumptionInfo
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which the instance exists.
  * `ZONE`: the zone where the instance exists.
  * `INSTANCE_NAME`: the name of the instance.



You see a response that is similar to the following:
    
    
    {
      "resourceStatus": {
        "reservationConsumptionInfo": {
          "consumedReservation": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-reservation"
        }
      }
    }
    

### View a list of instances that are consuming a reservation

You can view a list of instances consuming a reservation within a single project. For [shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-shared-reservations-work), this method returns only the instances in the project that you specify; it doesn't include instances from other consumer projects that are consuming the same reservation.

To view the instances that are consuming a reservation, select one of the following options:

###  gcloud 

To view the instances that are consuming a reservation, use the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) with the `--filter` flag set to the reservation that you want to view:
    
    
    gcloud compute instances list \
        --project=CONSUMER_PROJECT_ID \
        --zones=ZONE \
        --filter="resourceStatus.reservationConsumptionInfo.consumedReservation:https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME"
    

Replace the following:

  * `CONSUMER_PROJECT_ID`: the ID of the project consuming the reservation.
  * `ZONE`: the zone where the reservation and the instances are located.
  * `HOST_PROJECT_ID`: the ID of the project where the reservation was created (if different from the consumer project).
  * `RESERVATION_NAME`: the name of the reservation.



You see an output that is similar to the following:
    
    
    NAME               ZONE           MACHINE_TYPE  PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP     STATUS
    my-e2-instance     us-central1-c  e2-medium                  10.128.0.61  35.239.208.172  RUNNING
    my-e2-instance-02  us-central1-c  e2-medium                  10.128.0.62  104.154.31.123  RUNNING
    my-e2-instance-03  us-central1-c  e2-medium                  10.128.0.63  34.171.90.254   RUNNING
    

###  REST 

To view the instances that are consuming a reservation, make a `GET` request to the [`instances.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/list). In the request URL, include the `filter` query parameter set to the name of the reservation that you want to view:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/CONSUMER_PROJECT_ID/zones/ZONE/instances?filter=resourceStatus.reservationConsumptionInfo.consumedReservation%3D%22.*%2Fprojects%2FHOST_PROJECT_ID%2Fzones%2FZONE%2Freservations%2FRESERVATION_NAME%22
    

Replace the following:

  * `CONSUMER_PROJECT_ID`: the ID of the project consuming the reservation.
  * `ZONE`: the zone where the reservation and the instances are located.
  * `HOST_PROJECT_ID`: the ID of the project where the reservation was created (if different from the consumer project).
  * `RESERVATION_NAME`: the name of the reservation.



You see a response that is similar to the following:
    
    
    {
      "kind": "compute#instanceList",
      "id": "projects/example-project/zones/us-central1-a/instances",
      "items": [
        {
          ...
          "name": "example-instance-01",
          ...
          "resourceStatus": {
            "scheduling": {},
            "reservationConsumptionInfo": {
              "consumedReservation": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-reservation"
            }
          }
        },
        {
          ...
          "name": "example-instance-02",
          ...
          "resourceStatus": {
            "scheduling": {},
            "reservationConsumptionInfo": {
              "consumedReservation": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-reservation"
            }
          },
          ...
        }
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances"
    }
    

## What's next

  * Learn how to [attach reservations to commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments).

  * Learn how to [consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume).

  * Learn how to [modify reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify).

  * Learn how to [delete reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-delete).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
