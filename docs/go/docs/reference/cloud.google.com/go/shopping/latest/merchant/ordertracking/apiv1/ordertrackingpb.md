---
url: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/ordertracking/apiv1/ordertrackingpb/
title: Shopping Merchant Order Tracking API v1 - Package cloud.google.com/go/shopping/merchant/ordertracking/apiv1/ordertrackingpb (v1.17.0) \u00a0|\u00a0 Go client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:20.689927+00:00
---

# Shopping Merchant Order Tracking API v1 - Package cloud.google.com/go/shopping/merchant/ordertracking/apiv1/ordertrackingpb (v1.17.0)  |  Go client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/merchant/ordertracking/apiv1/ordertrackingpb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Go ](https://docs.cloud.google.com/go/docs)
  * [ Client libraries ](https://docs.cloud.google.com/go/docs/reference)



Send feedback 

#  Shopping Merchant Order Tracking API v1 - Package cloud.google.com/go/shopping/merchant/ordertracking/apiv1/ordertrackingpb (v1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.25.0  0.24.1  0.23.0  0.22.0  0.21.0  0.20.0  0.19.1  0.18.1  0.17.1  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.1  0.10.0  0.9.2  0.8.7  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/cloud.google.com/go/shopping/merchant/ordertracking/apiv1/ordertrackingpb). 

##  Constants 

### OrderTrackingSignalsService_CreateOrderTrackingSignal_FullMethodName
    
    
    const (
    	OrderTrackingSignalsService_CreateOrderTrackingSignal_FullMethodName = "/google.shopping.merchant.ordertracking.v1.OrderTrackingSignalsService/CreateOrderTrackingSignal"
    )

## Variables 

### OrderTrackingSignal_ShippingInfo_ShippingState_name, OrderTrackingSignal_ShippingInfo_ShippingState_value
    
    
    var (
    	OrderTrackingSignal_ShippingInfo_ShippingState_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){
    		0: "SHIPPING_STATE_UNSPECIFIED",
    		1: "SHIPPED",
    		2: "DELIVERED",
    	}
    	OrderTrackingSignal_ShippingInfo_ShippingState_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){
    		"SHIPPING_STATE_UNSPECIFIED": 0,
    		"SHIPPED":                    1,
    		"DELIVERED":                  2,
    	}
    )

Enum value maps for OrderTrackingSignal_ShippingInfo_ShippingState.

### File_google_shopping_merchant_ordertracking_v1_order_tracking_signals_proto
    
    
    var File_google_shopping_merchant_ordertracking_v1_order_tracking_signals_proto protoreflect.FileDescriptor

### OrderTrackingSignalsService_ServiceDesc
    
    
    var OrderTrackingSignalsService_ServiceDesc = grpc.ServiceDesc{
    	ServiceName: "google.shopping.merchant.ordertracking.v1.OrderTrackingSignalsService",
    	HandlerType: (*OrderTrackingSignalsServiceServer)([nil](https://pkg.go.dev/builtin#nil)),
    	Methods: []grpc.MethodDesc{
    		{
    			MethodName: "CreateOrderTrackingSignal",
    			Handler:    _OrderTrackingSignalsService_CreateOrderTrackingSignal_Handler,
    		},
    	},
    	Streams:  []grpc.StreamDesc{},
    	Metadata: "google/shopping/merchant/ordertracking/v1/order_tracking_signals.proto",
    }

OrderTrackingSignalsService_ServiceDesc is the grpc.ServiceDesc for OrderTrackingSignalsService service. It's only intended for direct use with grpc.RegisterService, and not to be introspected or modified (even as a copy)

## Functions 

### func RegisterOrderTrackingSignalsServiceServer 
    
    
    func RegisterOrderTrackingSignalsServiceServer(s [grpc](https://pkg.go.dev/google.golang.org/grpc).[ServiceRegistrar](https://pkg.go.dev/google.golang.org/grpc#ServiceRegistrar), srv OrderTrackingSignalsServiceServer)

## CreateOrderTrackingSignalRequest
    
    
    type CreateOrderTrackingSignalRequest struct {
    
    	// Required. The account of the business for which the order signal is
    	// created. Format: accounts/{account}
    	Parent [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=parent,proto3" json:"parent,omitempty"`
    	// Output only. The ID that uniquely identifies this order tracking signal.
    	OrderTrackingSignalId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=order_tracking_signal_id,json=orderTrackingSignalId,proto3" json:"order_tracking_signal_id,omitempty"`
    	// Required. The order signal to be created.
    	OrderTrackingSignal *OrderTrackingSignal `protobuf:"bytes,3,opt,name=order_tracking_signal,json=orderTrackingSignal,proto3" json:"order_tracking_signal,omitempty"`
    	// contains filtered or unexported fields
    }

Signals only can be created but not updated. Businesses need to call this API only when the order is completely shipped. Creates new order signal.

### func (*CreateOrderTrackingSignalRequest) Descriptor 
    
    
    func (*CreateOrderTrackingSignalRequest) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use CreateOrderTrackingSignalRequest.ProtoReflect.Descriptor instead.

### func (*CreateOrderTrackingSignalRequest) GetOrderTrackingSignal 
    
    
    func (x *CreateOrderTrackingSignalRequest) GetOrderTrackingSignal() *OrderTrackingSignal

### func (*CreateOrderTrackingSignalRequest) GetOrderTrackingSignalId 
    
    
    func (x *CreateOrderTrackingSignalRequest) GetOrderTrackingSignalId() [string](https://pkg.go.dev/builtin#string)

### func (*CreateOrderTrackingSignalRequest) GetParent 
    
    
    func (x *CreateOrderTrackingSignalRequest) GetParent() [string](https://pkg.go.dev/builtin#string)

### func (*CreateOrderTrackingSignalRequest) ProtoMessage 
    
    
    func (*CreateOrderTrackingSignalRequest) ProtoMessage()

### func (*CreateOrderTrackingSignalRequest) ProtoReflect 
    
    
    func (x *CreateOrderTrackingSignalRequest) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*CreateOrderTrackingSignalRequest) Reset 
    
    
    func (x *CreateOrderTrackingSignalRequest) Reset()

### func (*CreateOrderTrackingSignalRequest) String 
    
    
    func (x *CreateOrderTrackingSignalRequest) String() [string](https://pkg.go.dev/builtin#string)

## OrderTrackingSignal
    
    
    type OrderTrackingSignal struct {
    
    	// Output only. The ID that uniquely identifies this order tracking signal.
    	OrderTrackingSignalId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,11,opt,name=order_tracking_signal_id,json=orderTrackingSignalId,proto3" json:"order_tracking_signal_id,omitempty"`
    	// Optional. The Google Merchant Center ID of this order tracking signal. This
    	// value is optional. If left unset, the caller's Merchant Center ID is used.
    	// You must request access in order to provide data on behalf of another
    	// business. For more information, see [Submitting Order Tracking
    	// Signals](/shopping-content/guides/order-tracking-signals).
    	MerchantId [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,12,opt,name=merchant_id,json=merchantId,proto3" json:"merchant_id,omitempty"`
    	// Required. The time when the order was created on the businesses side.
    	// Include the year and timezone string, if available.
    	OrderCreatedTime *datetime.DateTime `protobuf:"bytes,1,opt,name=order_created_time,json=orderCreatedTime,proto3" json:"order_created_time,omitempty"`
    	// Required. The ID of the order on the businesses side. This field will be
    	// hashed in returned OrderTrackingSignal creation response.
    	OrderId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=order_id,json=orderId,proto3" json:"order_id,omitempty"`
    	// Required. The shipping information for the order.
    	ShippingInfo []*OrderTrackingSignal_ShippingInfo `protobuf:"bytes,3,rep,name=shipping_info,json=shippingInfo,proto3" json:"shipping_info,omitempty"`
    	// Required. Information about line items in the order.
    	LineItems []*OrderTrackingSignal_LineItemDetails `protobuf:"bytes,4,rep,name=line_items,json=lineItems,proto3" json:"line_items,omitempty"`
    	// Optional. The mapping of the line items to the shipment information.
    	ShipmentLineItemMapping []*OrderTrackingSignal_ShipmentLineItemMapping `protobuf:"bytes,5,rep,name=shipment_line_item_mapping,json=shipmentLineItemMapping,proto3" json:"shipment_line_item_mapping,omitempty"`
    	// Optional. The shipping fee of the order;
    	// this value should be set to zero in the case of free shipping.
    	CustomerShippingFee *typepb.Price `protobuf:"bytes,6,opt,name=customer_shipping_fee,json=customerShippingFee,proto3,oneof" json:"customer_shipping_fee,omitempty"`
    	// Optional. The delivery postal code, as a continuous string without spaces
    	// or dashes, for example "95016". This field will be anonymized in returned
    	// OrderTrackingSignal creation response.
    	DeliveryPostalCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,9,opt,name=delivery_postal_code,json=deliveryPostalCode,proto3" json:"delivery_postal_code,omitempty"`
    	// Optional. The [CLDR territory code]
    	// (http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) for
    	// the shipping destination.
    	DeliveryRegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,10,opt,name=delivery_region_code,json=deliveryRegionCode,proto3" json:"delivery_region_code,omitempty"`
    	// contains filtered or unexported fields
    }

Represents a business trade from which signals are extracted, such as shipping.

### func (*OrderTrackingSignal) Descriptor 
    
    
    func (*OrderTrackingSignal) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OrderTrackingSignal.ProtoReflect.Descriptor instead.

### func (*OrderTrackingSignal) GetCustomerShippingFee 
    
    
    func (x *OrderTrackingSignal) GetCustomerShippingFee() *[typepb](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb).[Price](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/shopping/latest/type/typepb#cloud_google_com_go_shopping_type_typepb_Price)

### func (*OrderTrackingSignal) GetDeliveryPostalCode 
    
    
    func (x *OrderTrackingSignal) GetDeliveryPostalCode() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal) GetDeliveryRegionCode 
    
    
    func (x *OrderTrackingSignal) GetDeliveryRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal) GetLineItems 
    
    
    func (x *OrderTrackingSignal) GetLineItems() []*OrderTrackingSignal_LineItemDetails

### func (*OrderTrackingSignal) GetMerchantId 
    
    
    func (x *OrderTrackingSignal) GetMerchantId() [int64](https://pkg.go.dev/builtin#int64)

### func (*OrderTrackingSignal) GetOrderCreatedTime 
    
    
    func (x *OrderTrackingSignal) GetOrderCreatedTime() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[DateTime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#DateTime)

### func (*OrderTrackingSignal) GetOrderId 
    
    
    func (x *OrderTrackingSignal) GetOrderId() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal) GetOrderTrackingSignalId 
    
    
    func (x *OrderTrackingSignal) GetOrderTrackingSignalId() [int64](https://pkg.go.dev/builtin#int64)

### func (*OrderTrackingSignal) GetShipmentLineItemMapping 
    
    
    func (x *OrderTrackingSignal) GetShipmentLineItemMapping() []*OrderTrackingSignal_ShipmentLineItemMapping

### func (*OrderTrackingSignal) GetShippingInfo 
    
    
    func (x *OrderTrackingSignal) GetShippingInfo() []*OrderTrackingSignal_ShippingInfo

### func (*OrderTrackingSignal) ProtoMessage 
    
    
    func (*OrderTrackingSignal) ProtoMessage()

### func (*OrderTrackingSignal) ProtoReflect 
    
    
    func (x *OrderTrackingSignal) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OrderTrackingSignal) Reset 
    
    
    func (x *OrderTrackingSignal) Reset()

### func (*OrderTrackingSignal) String 
    
    
    func (x *OrderTrackingSignal) String() [string](https://pkg.go.dev/builtin#string)

## OrderTrackingSignal_LineItemDetails
    
    
    type OrderTrackingSignal_LineItemDetails struct {
    
    	// Required. The ID for this line item.
    	LineItemId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=line_item_id,json=lineItemId,proto3" json:"line_item_id,omitempty"`
    	// Required. The Content API REST ID of the product, in the
    	// form channel:contentLanguage:targetCountry:offerId.
    	ProductId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=product_id,json=productId,proto3" json:"product_id,omitempty"`
    	// Optional. The Global Trade Item Numbers.
    	Gtins [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,rep,name=gtins,proto3" json:"gtins,omitempty"`
    	// Optional. The manufacturer part number.
    	Mpn [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=mpn,proto3" json:"mpn,omitempty"`
    	// Optional. Plain text title of this product.
    	ProductTitle *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=product_title,json=productTitle,proto3,oneof" json:"product_title,omitempty"`
    	// Optional. Brand of the product.
    	Brand *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,6,opt,name=brand,proto3,oneof" json:"brand,omitempty"`
    	// Required. The quantity of the line item in the order.
    	Quantity [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,7,opt,name=quantity,proto3" json:"quantity,omitempty"`
    	// contains filtered or unexported fields
    }

The line items of the order.

### func (*OrderTrackingSignal_LineItemDetails) Descriptor 
    
    
    func (*OrderTrackingSignal_LineItemDetails) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OrderTrackingSignal_LineItemDetails.ProtoReflect.Descriptor instead.

### func (*OrderTrackingSignal_LineItemDetails) GetBrand 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) GetBrand() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_LineItemDetails) GetGtins 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) GetGtins() [][string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_LineItemDetails) GetLineItemId 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) GetLineItemId() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_LineItemDetails) GetMpn 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) GetMpn() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_LineItemDetails) GetProductId 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) GetProductId() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_LineItemDetails) GetProductTitle 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) GetProductTitle() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_LineItemDetails) GetQuantity 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) GetQuantity() [int64](https://pkg.go.dev/builtin#int64)

### func (*OrderTrackingSignal_LineItemDetails) ProtoMessage 
    
    
    func (*OrderTrackingSignal_LineItemDetails) ProtoMessage()

### func (*OrderTrackingSignal_LineItemDetails) ProtoReflect 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OrderTrackingSignal_LineItemDetails) Reset 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) Reset()

### func (*OrderTrackingSignal_LineItemDetails) String 
    
    
    func (x *OrderTrackingSignal_LineItemDetails) String() [string](https://pkg.go.dev/builtin#string)

## OrderTrackingSignal_ShipmentLineItemMapping
    
    
    type OrderTrackingSignal_ShipmentLineItemMapping struct {
    
    	// Required. The shipment ID. This field will be hashed in returned
    	// OrderTrackingSignal creation response.
    	ShipmentId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=shipment_id,json=shipmentId,proto3" json:"shipment_id,omitempty"`
    	// Required. The line item ID.
    	LineItemId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=line_item_id,json=lineItemId,proto3" json:"line_item_id,omitempty"`
    	// Required. The line item quantity in the shipment.
    	Quantity [int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=quantity,proto3" json:"quantity,omitempty"`
    	// contains filtered or unexported fields
    }

Represents how many items are in the shipment for the given shipment_id and line_item_id.

### func (*OrderTrackingSignal_ShipmentLineItemMapping) Descriptor 
    
    
    func (*OrderTrackingSignal_ShipmentLineItemMapping) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OrderTrackingSignal_ShipmentLineItemMapping.ProtoReflect.Descriptor instead.

### func (*OrderTrackingSignal_ShipmentLineItemMapping) GetLineItemId 
    
    
    func (x *OrderTrackingSignal_ShipmentLineItemMapping) GetLineItemId() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_ShipmentLineItemMapping) GetQuantity 
    
    
    func (x *OrderTrackingSignal_ShipmentLineItemMapping) GetQuantity() [int64](https://pkg.go.dev/builtin#int64)

### func (*OrderTrackingSignal_ShipmentLineItemMapping) GetShipmentId 
    
    
    func (x *OrderTrackingSignal_ShipmentLineItemMapping) GetShipmentId() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_ShipmentLineItemMapping) ProtoMessage 
    
    
    func (*OrderTrackingSignal_ShipmentLineItemMapping) ProtoMessage()

### func (*OrderTrackingSignal_ShipmentLineItemMapping) ProtoReflect 
    
    
    func (x *OrderTrackingSignal_ShipmentLineItemMapping) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OrderTrackingSignal_ShipmentLineItemMapping) Reset 
    
    
    func (x *OrderTrackingSignal_ShipmentLineItemMapping) Reset()

### func (*OrderTrackingSignal_ShipmentLineItemMapping) String 
    
    
    func (x *OrderTrackingSignal_ShipmentLineItemMapping) String() [string](https://pkg.go.dev/builtin#string)

## OrderTrackingSignal_ShippingInfo
    
    
    type OrderTrackingSignal_ShippingInfo struct {
    
    	// Required. The shipment ID. This field will be hashed in returned
    	// OrderTrackingSignal creation response.
    	ShipmentId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=shipment_id,json=shipmentId,proto3" json:"shipment_id,omitempty"`
    	// Optional. The tracking ID of the shipment. This field is required if one
    	// of the following fields is absent: earliest_delivery_promise_time,
    	// latest_delivery_promise_time, and actual_delivery_time.
    	TrackingId [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=tracking_id,json=trackingId,proto3" json:"tracking_id,omitempty"`
    	// Optional. The name of the shipping carrier for the delivery. This field
    	// is required if one of the following fields is absent:
    	// earliest_delivery_promise_time, latest_delivery_promise_time,
    	// and actual_delivery_time.
    	Carrier [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=carrier,proto3" json:"carrier,omitempty"`
    	// Optional. The service type for fulfillment, such as GROUND, FIRST_CLASS,
    	// etc.
    	CarrierService [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=carrier_service,json=carrierService,proto3" json:"carrier_service,omitempty"`
    	// Optional. The time when the shipment was shipped.
    	// Include the year and timezone string, if available.
    	ShippedTime *datetime.DateTime `protobuf:"bytes,5,opt,name=shipped_time,json=shippedTime,proto3" json:"shipped_time,omitempty"`
    	// Optional. The earliest delivery promised time.
    	// Include the year and timezone string, if available.
    	// This field is required, if one of the following fields is absent:
    	// tracking_id or carrier_name.
    	EarliestDeliveryPromiseTime *datetime.DateTime `protobuf:"bytes,6,opt,name=earliest_delivery_promise_time,json=earliestDeliveryPromiseTime,proto3" json:"earliest_delivery_promise_time,omitempty"`
    	// Optional. The latest delivery promised time.
    	// Include the year and timezone string, if available.
    	// This field is required, if one of the following fields is absent:
    	// tracking_id or carrier_name.
    	LatestDeliveryPromiseTime *datetime.DateTime `protobuf:"bytes,7,opt,name=latest_delivery_promise_time,json=latestDeliveryPromiseTime,proto3" json:"latest_delivery_promise_time,omitempty"`
    	// Optional. The time when the shipment was actually delivered.
    	// Include the year and timezone string, if available.
    	// This field is required, if one of the following fields is absent:
    	// tracking_id or carrier_name.
    	ActualDeliveryTime *datetime.DateTime `protobuf:"bytes,8,opt,name=actual_delivery_time,json=actualDeliveryTime,proto3" json:"actual_delivery_time,omitempty"`
    	// Required. The status of the shipment.
    	ShippingStatus OrderTrackingSignal_ShippingInfo_ShippingState `protobuf:"varint,9,opt,name=shipping_status,json=shippingStatus,proto3,enum=google.shopping.merchant.ordertracking.v1.OrderTrackingSignal_ShippingInfo_ShippingState" json:"shipping_status,omitempty"`
    	// Required. The origin postal code, as a continuous string without spaces
    	// or dashes, for example "95016". This field will be anonymized in returned
    	// OrderTrackingSignal creation response.
    	OriginPostalCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,10,opt,name=origin_postal_code,json=originPostalCode,proto3" json:"origin_postal_code,omitempty"`
    	// Required. The [CLDR territory code]
    	// (http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) for
    	// the shipping origin.
    	OriginRegionCode [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,11,opt,name=origin_region_code,json=originRegionCode,proto3" json:"origin_region_code,omitempty"`
    	// contains filtered or unexported fields
    }

The shipping information for the order.

### func (*OrderTrackingSignal_ShippingInfo) Descriptor 
    
    
    func (*OrderTrackingSignal_ShippingInfo) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OrderTrackingSignal_ShippingInfo.ProtoReflect.Descriptor instead.

### func (*OrderTrackingSignal_ShippingInfo) GetActualDeliveryTime 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetActualDeliveryTime() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[DateTime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#DateTime)

### func (*OrderTrackingSignal_ShippingInfo) GetCarrier 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetCarrier() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_ShippingInfo) GetCarrierService 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetCarrierService() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_ShippingInfo) GetEarliestDeliveryPromiseTime 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetEarliestDeliveryPromiseTime() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[DateTime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#DateTime)

### func (*OrderTrackingSignal_ShippingInfo) GetLatestDeliveryPromiseTime 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetLatestDeliveryPromiseTime() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[DateTime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#DateTime)

### func (*OrderTrackingSignal_ShippingInfo) GetOriginPostalCode 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetOriginPostalCode() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_ShippingInfo) GetOriginRegionCode 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetOriginRegionCode() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_ShippingInfo) GetShipmentId 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetShipmentId() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_ShippingInfo) GetShippedTime 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetShippedTime() *[datetime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime).[DateTime](https://pkg.go.dev/google.golang.org/genproto/googleapis/type/datetime#DateTime)

### func (*OrderTrackingSignal_ShippingInfo) GetShippingStatus 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetShippingStatus() OrderTrackingSignal_ShippingInfo_ShippingState

### func (*OrderTrackingSignal_ShippingInfo) GetTrackingId 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) GetTrackingId() [string](https://pkg.go.dev/builtin#string)

### func (*OrderTrackingSignal_ShippingInfo) ProtoMessage 
    
    
    func (*OrderTrackingSignal_ShippingInfo) ProtoMessage()

### func (*OrderTrackingSignal_ShippingInfo) ProtoReflect 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) ProtoReflect() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[Message](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#Message)

### func (*OrderTrackingSignal_ShippingInfo) Reset 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) Reset()

### func (*OrderTrackingSignal_ShippingInfo) String 
    
    
    func (x *OrderTrackingSignal_ShippingInfo) String() [string](https://pkg.go.dev/builtin#string)

## OrderTrackingSignal_ShippingInfo_ShippingState
    
    
    type OrderTrackingSignal_ShippingInfo_ShippingState [int32](https://pkg.go.dev/builtin#int32)

The current status of the shipments.

### OrderTrackingSignal_ShippingInfo_SHIPPING_STATE_UNSPECIFIED, OrderTrackingSignal_ShippingInfo_SHIPPED, OrderTrackingSignal_ShippingInfo_DELIVERED
    
    
    const (
    	// The shipping status is not known to business.
    	OrderTrackingSignal_ShippingInfo_SHIPPING_STATE_UNSPECIFIED OrderTrackingSignal_ShippingInfo_ShippingState = 0
    	// All items are shipped.
    	OrderTrackingSignal_ShippingInfo_SHIPPED OrderTrackingSignal_ShippingInfo_ShippingState = 1
    	// The shipment is already delivered.
    	OrderTrackingSignal_ShippingInfo_DELIVERED OrderTrackingSignal_ShippingInfo_ShippingState = 2
    )

### func (OrderTrackingSignal_ShippingInfo_ShippingState) Descriptor 
    
    
    func (OrderTrackingSignal_ShippingInfo_ShippingState) Descriptor() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumDescriptor](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumDescriptor)

### func (OrderTrackingSignal_ShippingInfo_ShippingState) Enum 
    
    
    func (x OrderTrackingSignal_ShippingInfo_ShippingState) Enum() *OrderTrackingSignal_ShippingInfo_ShippingState

### func (OrderTrackingSignal_ShippingInfo_ShippingState) EnumDescriptor 
    
    
    func (OrderTrackingSignal_ShippingInfo_ShippingState) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use OrderTrackingSignal_ShippingInfo_ShippingState.Descriptor instead.

### func (OrderTrackingSignal_ShippingInfo_ShippingState) Number 
    
    
    func (x OrderTrackingSignal_ShippingInfo_ShippingState) Number() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumNumber](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumNumber)

### func (OrderTrackingSignal_ShippingInfo_ShippingState) String 
    
    
    func (x OrderTrackingSignal_ShippingInfo_ShippingState) String() [string](https://pkg.go.dev/builtin#string)

### func (OrderTrackingSignal_ShippingInfo_ShippingState) Type 
    
    
    func (OrderTrackingSignal_ShippingInfo_ShippingState) Type() [protoreflect](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect).[EnumType](https://pkg.go.dev/google.golang.org/protobuf/reflect/protoreflect#EnumType)

## OrderTrackingSignalsServiceClient
    
    
    type OrderTrackingSignalsServiceClient interface {
    	// Creates new order tracking signal.
    	CreateOrderTrackingSignal(ctx context.Context, in *CreateOrderTrackingSignalRequest, opts ...grpc.CallOption) (*OrderTrackingSignal, [error](https://pkg.go.dev/builtin#error))
    }

OrderTrackingSignalsServiceClient is the client API for OrderTrackingSignalsService service.

For semantics around ctx use and closing/ending streaming RPCs, please refer to <https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream>.

### func NewOrderTrackingSignalsServiceClient 
    
    
    func NewOrderTrackingSignalsServiceClient(cc [grpc](https://pkg.go.dev/google.golang.org/grpc).[ClientConnInterface](https://pkg.go.dev/google.golang.org/grpc#ClientConnInterface)) OrderTrackingSignalsServiceClient

## OrderTrackingSignalsServiceServer
    
    
    type OrderTrackingSignalsServiceServer interface {
    	// Creates new order tracking signal.
    	CreateOrderTrackingSignal(context.Context, *CreateOrderTrackingSignalRequest) (*OrderTrackingSignal, [error](https://pkg.go.dev/builtin#error))
    }

OrderTrackingSignalsServiceServer is the server API for OrderTrackingSignalsService service. All implementations should embed UnimplementedOrderTrackingSignalsServiceServer for forward compatibility

## UnimplementedOrderTrackingSignalsServiceServer
    
    
    type UnimplementedOrderTrackingSignalsServiceServer struct {
    }

UnimplementedOrderTrackingSignalsServiceServer should be embedded to have forward compatible implementations.

### func (UnimplementedOrderTrackingSignalsServiceServer) CreateOrderTrackingSignal 
    
    
    func (UnimplementedOrderTrackingSignalsServiceServer) CreateOrderTrackingSignal([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *CreateOrderTrackingSignalRequest) (*OrderTrackingSignal, [error](https://pkg.go.dev/builtin#error))

## UnsafeOrderTrackingSignalsServiceServer
    
    
    type UnsafeOrderTrackingSignalsServiceServer interface {
    	// contains filtered or unexported methods
    }

UnsafeOrderTrackingSignalsServiceServer may be embedded to opt out of forward compatibility for this service. Use of this interface is not recommended, as added methods to OrderTrackingSignalsServiceServer will result in compilation errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
