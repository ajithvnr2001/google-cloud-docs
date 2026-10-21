---
url: https://docs.cloud.google.com/tpu/docs/tensorflow-ops/
title: Available TensorFlow Ops \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:26.165390+00:00
---

# Available TensorFlow Ops  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tensorflow-ops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Reference ](https://docs.cloud.google.com/tpu/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Available TensorFlow Ops

This page lists the TensorFlow Python APIs and graph operators available on Cloud TPU.

## Available Python APIs

The list below is a guide to the set of available TensorFlow Python APIs. This list is not exhaustive. Library functions not on this list may work if they are composed of available primitives.

See the [performance guide](https://cloud.google.com/tpu/docs/performance-guide) for recommendations about specific operators.

Module | Available Python API | Comments  
---|---|---  
`tf` | `tf.abs` |   
| `tf.acosh` |   
| `tf.add` |   
| `tf.add_n` |   
| `tf.angle` |   
| `tf.arg_max` | `dimension` argument must be a compile-time constant.  
| `tf.arg_min` | `dimension` argument must be a compile-time constant.  
| `tf.asinh` |   
| `tf.assign` | Available only for resource variable.  
| `tf.assign_add` | Available only for resource variable.  
| `tf.assign_sub` | Available only for resource variable.  
| `tf.atan` |   
| `tf.atan2` |   
| `tf.atanh` |   
| `tf.batch_to_space` | `crops` and `block_shape` arguments must be compile-time constant.  
| `tf.batch_to_space_nd` | `crops` argument must be a compile-time constant.  
| `tf.broadcast_dynamic_shape` |   
| `tf.broadcast_static_shape` |   
| `tf.case` | Experimental (control-flow). May not work reliably yet.  
| `tf.cast` |   
| `tf.ceil` |   
| `tf.cholesky` | Experimental. May have issues with numerical precision.  
| `tf.cholesky_solve` | Experimental. May have issues with numerical precision.  
| `tf.clip_by_average_norm` |   
| `tf.clip_by_global_norm` |   
| `tf.clip_by_norm` |   
| `tf.clip_by_value` |   
| `tf.complex` |   
| `tf.concat` | `concat_dim` must be a compile-time constant.  
| `tf.cond` | Experimental (control-flow). May not work reliably yet.  
| `tf.conj` |   
| `tf.constant` |   
| `tf.convert_to_tensor` |   
| `tf.cos` |   
| `tf.cosh` |   
| `tf.cross` |   
| `tf.cumprod` | `axis` must be a compile-time constant.  
| `tf.cumsum` | `axis` must be a compile-time constant.  
| `tf.depth_to_space` |   
| `tf.diag` |   
| `tf.diag_part` |   
| `tf.div` | `int32` division is slower than other types.  
| `tf.divide` | `int32` division is slower than other types.  
| `tf.dynamic_stitch` | `indices` must be a compile-time constant.  
| `tf.einsum` |   
| `tf.equal` |   
| `tf.erf` |   
| `tf.erfc` |   
| `tf.exp` |   
| `tf.expand_dims` | `dims` must be a compile-time constant.  
| `tf.expm1` |   
| `tf.extract_image_patches` |   
| `tf.eye` |   
| `tf.fake_quant_with_min_max_args` |   
| `tf.fake_quant_with_min_max_args_gradient` |   
| `tf.fake_quant_with_min_max_vars` |   
| `tf.fake_quant_with_min_max_vars_gradient` |   
| `tf.fft` |   
| `tf.fft2d` |   
| `tf.fft3d` |   
| `tf.fill` | `dims` argument must be a compile-time constant.  
| `tf.floor` |   
| `tf.floordiv` |   
| `tf.floormod` |   
| `tf.foldl` | Experimental (control-flow).  
| `tf.foldr` | Experimental (control-flow).  
| `tf.gather` | `axis` must be a compile-time constant.  
| `tf.gather_nd` |   
| `tf.greater` |   
| `tf.greater_equal` |   
| `tf.hessians` | Experimental (control-flow.  
| `tf.identity` |   
| `tf.identity_n` |   
| `tf.ifft` |   
| `tf.ifft2d` |   
| `tf.ifft3d` |   
| `tf.imag` |   
| `tf.invert_permutation` | `x` argument must be a compile-time constant.  
| `tf.is_finite` |   
| `tf.is_inf` |   
| `tf.is_nan` |   
| `tf.is_non_decreasing` |   
| `tf.is_strictly_increasing` |   
| `tf.less` |   
| `tf.less_equal` |   
| `tf.linspace` | `start`, `stop` and `num` arguments must be compile-time constants.  
| `tf.log` |   
| `tf.log1p` |   
| `tf.log_sigmoid` |   
| `tf.logical_and` |   
| `tf.logical_or` |   
| `tf.logical_not` |   
| `tf.logical_xor` |   
| `tf.matmul` | Uses a `bfloat16` matmul with `float32` accumulation.  
| `tf.matrix_band_part` |   
| `tf.matrix_diag` |   
| `tf.matrix_diag_part` |   
| `tf.matrix_set_diag` |   
| `tf.matrix_triangular_solve` | Experimental. May have issues with numerical precision.  
| `tf.maximum` |   
| `tf.meshgrid` |   
| `tf.minimum` |   
| `tf.mod` |   
| `tf.multinomial` | `num_samples` argument must be a compile-time constant.  
| `tf.multiply` |   
| `tf.negative` |   
| `tf.no_op` |   
| `tf.norm` |   
| `tf.not_equal` |   
| `tf.one_hot` | `depth` must be a compile-time constant.  
| `tf.ones` |   
| `tf.ones_like` |   
| `tf.pad` | `paddings` argument must be a compile-time constant. Gradient of `REFLECT` padding is not yet available.  
| `tf.pow` |   
| `tf.random_normal` | `shape` must be a compile-time constant.  
| `tf.random_uniform` | `shape` must be a compile-time constant.  
| `tf.range` | `start`, `limit` and `delta` arguments must be compile-time constants.  
| `tf.rank` |   
| `tf.real` |   
| `tf.realdiv` |   
| `tf.reciprocal` |   
| `tf.reduce_all` | `axis` must be a compile-time constant.  
| `tf.reduce_any` | `axis` must be a compile-time constant.  
| `tf.reduce_logsumexp` |   
| `tf.reduce_max` | `axis` must be a compile-time constant.  
| `tf.reduce_min` | `axis` must be a compile-time constant.  
| `tf.reduce_prod` | `axis` must be a compile-time constant.  
| `tf.reduce_sum` | `axis` must be a compile-time constant.  
| `tf.reshape` | `shape` argument must be a compile-time constant.  
| `tf.reverse` | `dims` argument must be a compile-time constant.  
| `tf.reverse_sequence` |   
| `tf.reverse_v2` | `axis` argument must be a compile-time constant.  
| `tf.rint` |   
| `tf.round` |   
| `tf.rsqrt` |   
| `tf.saturate_cast` |   
| `tf.scalar_mul` |   
| `tf.scan` | Experimental (control-flow).  
| `tf.scatter_nd` |   
| `tf.sequence_mask` |   
| `tf.shape` |   
| `tf.shape_n` |   
| `tf.sigmoid` |   
| `tf.sign` |   
| `tf.sin` |   
| `tf.sinh` |   
| `tf.size` |   
| `tf.slice` | `size` must be a compile-time constant. In addition, either `begin` must be a compile-time constant or `size` must be non-negative. Backpropagation is only supported if `begin` and `size` are compile-time constants.  
| `tf.space_to_batch` | `paddings` and `block_shape` must be compile-time constants.  
| `tf.space_to_batch_nd` | `paddings` must be a compile-time constant.  
| `tf.space_to_depth` |   
| `tf.split` | `axis` must be a compile-time constant.  
| `tf.sqrt` |   
| `tf.square` |   
| `tf.squared_difference` |   
| `tf.squeeze` |   
| `tf.stack` |   
| `tf.stop_gradient` |   
| `tf.strided_slice` |   
| `tf.tan` |   
| `tf.tanh` |   
| `tf.tensordot` |   
| `tf.tile` | `multiples` argument must be a compile-time constant.  
| `tf.to_bfloat16` |   
| `tf.to_float` |   
| `tf.to_int32` |   
| `tf.to_int64` | `int64` support is limited.  
| `tf.trace` |   
| `tf.transpose` | `perm` argument must be a compile-time constant.  
| `tf.truediv` |   
| `tf.truncated_normal` | `shape` must be a compile-time constant.  
| `tf.truncatediv` |   
| `tf.truncatemod` |   
| `tf.unsorted_segment_sum` |   
| `tf.unstack` |   
| `tf.where` | Both `x` and `y` must be non-`None`. If both `x` and `y` are `None`, the operator would not have a static shape.  
| `tf.while_loop` | Computing the gradient of a while loop requires that the `maximum_iterations` argument is passed.  
| `tf.zeros` |   
| `tf.zeros_like` |   
| `tf.Tensor.__getitem__` | The start, end, and strides of a slice must be compile-time constants.  
`tf.bitwise` | `tf.bitwise_and` |   
| `tf.bitwise_or` |   
| `tf.bitwise_invert` |   
`tf.contrib.stateless` | `tf.contrib.stateless.stateless_random_normal` |   
| `tf.contrib.stateless.stateless_random_uniform` |   
`tf.image` | `tf.image.adjust_brightness` |   
| `tf.image.adjust_contrast` |   
| `tf.image.adjust_gamma` |   
| `tf.image.adjust_hue` |   
| `tf.image.adjust_saturation` |   
| `tf.image.central_crop` | Crop factor must be a compile-time constant.  
| `tf.image.convert_image_dtype` |   
| `tf.image.flip_left_right` |   
| `tf.image.flip_up_down` |   
| `tf.image.grayscale_to_rgb` |   
| `tf.image.hsv_to_rgb` |   
| `tf.image.resize_bilinear` | Only `align_corners=True` is available. `size` must be a compile-time constant.  
| `tf.image.random_brightness` |   
| `tf.image.random_contrast` |   
| `tf.image.random_flip_left_right` |   
| `tf.image.random_flip_up_down` |   
| `tf.image.random_hue` |   
| `tf.image.random_saturation` |   
| `tf.image.rgb_to_hsv` |   
| `tf.image.rgb_to_grayscale` |   
| `tf.image.rot90` |   
| `tf.image.total_variation` |   
| `tf.image.transpose_image` |   
`tf.layers` | `tf.layers.average_pooling1d` |   
| `tf.layers.average_pooling2d` |   
| `tf.layers.average_pooling1d` |   
| `tf.layers.batch_normalization` |   
| `tf.layers.conv1d` |   
| `tf.layers.conv2d` |   
| `tf.layers.conv2d_transpose` |   
| `tf.layers.conv3d` |   
| `tf.layers.conv3d_transpose` |   
| `tf.layers.dense` |   
| `tf.layers.dropout` |   
| `tf.layers.flatten` |   
| `tf.layers.max_pooling1d` |   
| `tf.layers.max_pooling2d` |   
| `tf.layers.max_pooling3d` |   
| `tf.layers.separable_conv2d` |   
`tf.nn` | `tf.nn.atrous_conv2d` |   
| `tf.nn.atrous_conv2d_transpose` |   
| `tf.nn.avg_pool` |   
| `tf.nn.avg_pool3d` |   
| `tf.nn.batch_normalization` |   
| `tf.nn.bias_add` |   
| `tf.nn.conv1d` |   
| `tf.nn.conv2d` |   
| `tf.nn.conv2d_backprop_filter` |   
| `tf.nn.conv2d_backprop_input` |   
| `tf.nn.conv2d_transpose` |   
| `tf.nn.conv3d` |   
| `tf.nn.conv3d_backprop_filter` |   
| `tf.nn.conv3d_backprop_input` |   
| `tf.nn.conv3d_transpose` |   
| `tf.nn.convolution` |   
| `tf.nn.crelu` |   
| `tf.nn.depthwise_conv2d` |   
| `tf.nn.depthwise_conv2d_native` |   
| `tf.nn.depthwise_conv2d_native_backprop_filter` |   
| `tf.nn.depthwise_conv2d_native_backprop_input` |   
| `tf.nn.dropout` |   
| `tf.nn.dynamic_rnn` | Experimental.  
| `tf.nn.elu` |   
| `tf.nn.fused_batch_norm` |   
| `tf.nn.l2_loss` |   
| `tf.nn.l2_normalize` |   
| `tf.nn.leaky_relu` |   
| `tf.nn.local_response_normalization` |   
| `tf.nn.log_poisson_loss` |   
| `tf.nn.log_softmax` |   
| `tf.nn.max_pool` |   
| `tf.nn.max_pool3d` |   
| `tf.nn.moments` |   
| `tf.nn.normalize_moments` |   
| `tf.nn.pool` |   
| `tf.nn.relu` |   
| `tf.nn.relu6` |   
| `tf.nn.relu_layer` |   
| `tf.nn.selu` |   
| `tf.nn.separable_conv2d` |   
| `tf.nn.sigmoid_cross_entropy_with_logits` |   
| `tf.nn.softmax` |   
| `tf.nn.softmax_cross_entropy_with_logits` |   
| `tf.nn.softplus` |   
| `tf.nn.softsign` |   
| `tf.nn.sparse_softmax_cross_entropy_with_logits` |   
| `tf.nn.static_bidirectional_rnn` | Experimental.  
| `tf.nn.static_rnn` | Experimental.  
| `tf.nn.weighted_cross_entropy_with_logits` | Experimental.  
| `tf.nn.weighted_moments` |   
| `tf.nn.with_space_to_batch` |   
| `tf.nn.xw_plus_b` |   
| `tf.nn.zero_fraction` |   
`tf.spectral` | `tf.spectral.fft` |   
| `tf.spectral.fft2d` |   
| `tf.spectral.fft3d` |   
| `tf.spectral.ifft` |   
| `tf.spectral.ifft2d` |   
| `tf.spectral.ifft3d` |   
| `tf.spectral.irfft` | `fft_length` must be a compile-time constant.  
| `tf.spectral.irfft2d` | `fft_length` must be a compile-time constant.  
| `tf.spectral.irfft3d` | `fft_length` must be a compile-time constant.  
| `tf.spectral.rfft` | `fft_length` must be a compile-time constant.  
| `tf.spectral.rfft2d` | `fft_length` must be a compile-time constant.  
| `tf.spectral.rfft3d` | `fft_length` must be a compile-time constant.  
  
## Unavailable Python APIs

This list is not exhaustive. Ops that are not available on Cloud TPU include the following:

Module | Unavailable Python API | Comments  
---|---|---  
`tf` | `tf.accumulate_n` | Uses Ref variables.  
| `tf.acos` |   
| `tf.asin` |   
| `tf.betainc` |   
| `tf.bitcast` |   
| `tf.add_check_numerics_ops` | Programs containing check numerics operators should run, but the check numerics operator is currently ignored.  
| `tf.assert_...` | Programs containing assertions should run, but the assertions are ignored.  
| `tf.check_numerics` | Programs containing check numerics operators should run, but the check numerics operator is currently ignored.  
| `tf.confusion_matrix` |   
| `tf.count_nonzero` | Uses `int64` reduction.  
| `tf.count_up_to` |   
| `tf.create_partitioned_variables` |   
| `tf.dequantize` |   
| `tf.digamma` |   
| `tf.dynamic_partition` |   
| `tf.edit_distance` |   
| `tf.fake_quant_with_min_max_vars_per_channel` |   
| `tf.fake_quant_with_min_max_vars_per_channel_gradient` |   
| `tf.histogram_fixed_width` |   
| `tf.igamma` |   
| `tf.igammac` |   
| `tf.lbeta` |   
| `tf.lgamma` |   
| `tf.matrix_determinant` |   
| `tf.matrix_inverse` |   
| `tf.matrix_solve` |   
| `tf.matrix_solve_ls` |   
| `tf.polygamma` |   
| `tf.py_func` |   
| `tf.qr` |   
| `tf.quantize_v2` |   
| `tf.quantized_concat` |   
| `tf.random_crop` |   
| `tf.random_gamma` |   
| `tf.random_poisson` |   
| `tf.random_shuffle` |   
| `tf.scatter_add` |   
| `tf.scatter_div` |   
| `tf.scatter_mul` |   
| `tf.scatter_nd_add` |   
| `tf.scatter_nd_sub` |   
| `tf.scatter_nd_update` |   
| `tf.segment_mean` |   
| `tf.segment_max` |   
| `tf.segment_min` |   
| `tf.segment_prod` |   
| `tf.segment_sum` |   
| `tf.self_adjoint_eig` |   
| `tf.self_adjoint_eigvals` |   
| `tf.setdiff1d` |   
| `tf.sparse_...` |   
| `tf.string_...` |   
| `tf.substr` |   
| `tf.svd` |   
| `tf.to_double` |   
| `tf.unique` |   
| `tf.unsorted_segment_max` |   
| `tf.zeta` |   
| `tf.bitwise.bitwise_xor` |   
| `tf.contrib.stateless.stateless_truncated_normal` |   
  
## Available graph operators

Operator | Type Constraint  
---|---  
`Abs` | `T={bfloat16,float,int32,int64}`  
`Acos` | `T={bfloat16,complex64,float,int32,int64}`  
`Acosh` | `T={bfloat16,complex64,float}`  
`Add` | `T={bfloat16,complex64,float,int32,int64}`  
`AddN` | `T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`AdjustContrastv2` | `T={float}`  
`AdjustHue` | `T={float}`  
`AdjustSaturation` | `T={float}`  
`All` | `Tidx={int32,int64}`  
`AllToAll` | `T={bfloat16,float}`  
`Angle` | `Tout={float}`  
`T={complex64}`  
`Any` | `Tidx={int32,int64}`  
`ApproximateEqual` | `T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`ArgMax` | `Tidx={int32,int64}`  
`output_type={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`ArgMin` | `Tidx={int32,int64}`  
`output_type={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`Asin` | `T={bfloat16,complex64,float,int32,int64}`  
`Asinh` | `T={bfloat16,complex64,float}`  
`Assert` | `T={bfloat16,bool,complex64,float,int32,int64,string,uint32,uint64}`  
`AssignAddVariableOp` | `dtype={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`AssignSubVariableOp` | `dtype={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`AssignVariableOp` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Atan` | `T={bfloat16,complex64,float,int32,int64}`  
`Atan2` | `T={bfloat16,float}`  
`Atanh` | `T={bfloat16,complex64,float}`  
`AvgPool` | `T={bfloat16,float}`  
`AvgPool3D` | `T={bfloat16,float}`  
`AvgPool3DGrad` | `T={bfloat16,float}`  
`AvgPoolGrad` | `T={bfloat16,float}`  
`BatchMatMul` | `T={bfloat16,complex64,float,int32,int64}`  
`BatchToSpace` | `Tidx={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`BatchToSpaceND` | `Tcrops={int32,int64}`  
`Tblock_shape={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`BiasAdd` | `T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`BiasAddGrad` | `T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`BiasAddV1` | `T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`Bitcast` | `type={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`BitwiseAnd` | `T={int32,int64,uint32,uint64}`  
`BitwiseOr` | `T={int32,int64,uint32,uint64}`  
`BitwiseXor` | `T={int32,int64,uint32,uint64}`  
`BroadcastArgs` | `T={int32,int64}`  
`BroadcastGradientArgs` | `T={int32,int64}`  
`BroadcastTo` | `Tidx={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Bucketize` | `T={float,int32,int64}`  
`Cast` | `DstT={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`SrcT={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Ceil` | `T={bfloat16,float}`  
`CheckNumerics` | `T={bfloat16,float}`  
`Cholesky` | `T={float}`  
`ClipByValue` | `T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`CollectivePermute` | `T={bfloat16,float}`  
`Complex` | `Tout={complex64}`  
`T={float}`  
`ComplexAbs` | `Tout={float}`  
`T={complex64}`  
`Concat` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ConcatOffset` |   
`ConcatV2` | `Tidx={int32}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Conj` | `T={complex64}`  
`ConjugateTranspose` | `Tperm={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Const` | `dtype={bfloat16,bool,complex64,float,int32,int64,string,uint32,uint64}`  
`ControlTrigger` |   
`Conv2D` | `T={bfloat16,float}`  
`Conv2DBackpropFilter` | `T={bfloat16,float}`  
`Conv2DBackpropInput` | `T={bfloat16,float}`  
`Conv3D` | `T={bfloat16,float}`  
`Conv3DBackpropFilterV2` | `T={bfloat16,float}`  
`Conv3DBackpropInputV2` | `Tshape={int32,int64}`  
`T={bfloat16,float}`  
`Cos` | `T={bfloat16,complex64,float}`  
`Cosh` | `T={bfloat16,complex64,float}`  
`Cross` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`CrossReplicaSum` | `T={bfloat16,float}`  
`Cumprod` | `Tidx={int32,int64}`  
`T={bfloat16,float,int32}`  
`Cumsum` | `Tidx={int32,int64}`  
`T={bfloat16,float,int32}`  
`DataFormatVecPermute` | `T={int32,int64}`  
`DepthToSpace` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`DepthwiseConv2dNative` | `T={bfloat16,float}`  
`DepthwiseConv2dNativeBackpropFilter` | `T={bfloat16,float}`  
`DepthwiseConv2dNativeBackpropInput` | `T={bfloat16,float}`  
`Diag` | `T={bfloat16,complex64,float,int32,int64}`  
`DiagPart` | `T={bfloat16,complex64,float,int32,int64}`  
`Digamma` | `T={bfloat16,float}`  
`Div` | `T={bfloat16,complex64,float,int32,int64}`  
`DivNoNan` | `T={float}`  
`DynamicStitch` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Elu` | `T={bfloat16,float}`  
`EluGrad` | `T={bfloat16,float}`  
`Empty` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`EmptyTensorList` | `shape_type={int32,int64}`  
`element_dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Equal` | `T={bfloat16,bool,complex64,float,int32,int64}`  
`Erf` | `T={bfloat16,float}`  
`Erfc` | `T={bfloat16,float}`  
`Exp` | `T={bfloat16,complex64,float}`  
`ExpandDims` | `Tdim={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Expm1` | `T={bfloat16,complex64,float}`  
`ExtractImagePatches` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`FFT` | `Tcomplex={complex64}`  
`FFT2D` | `Tcomplex={complex64}`  
`FFT3D` | `Tcomplex={complex64}`  
`FakeParam` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`FakeQuantWithMinMaxArgs` |   
`FakeQuantWithMinMaxArgsGradient` |   
`FakeQuantWithMinMaxVars` |   
`FakeQuantWithMinMaxVarsGradient` |   
`Fill` | `index_type={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Floor` | `T={bfloat16,float}`  
`FloorDiv` | `T={bfloat16,complex64,float,int32,int64}`  
`FloorMod` | `T={bfloat16,float,int32,int64}`  
`FusedBatchNorm` | `T={float}`  
`FusedBatchNormGrad` | `T={float}`  
`FusedBatchNormGradV2` | `U={float}`  
`T={bfloat16,float}`  
`FusedBatchNormV2` | `U={float}`  
`T={bfloat16,float}`  
`Gather` | `Tindices={int32,int64}`  
`Tparams={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`GatherNd` | `Tindices={int32,int64}`  
`Tparams={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`GatherV2` | `Taxis={int32,int64}`  
`Tindices={int32,int64}`  
`Tparams={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`GetItem` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Greater` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`GreaterEqual` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`HSVToRGB` | `T={bfloat16,float}`  
`IFFT` | `Tcomplex={complex64}`  
`IFFT2D` | `Tcomplex={complex64}`  
`IFFT3D` | `Tcomplex={complex64}`  
`IRFFT` |   
`IRFFT2D` |   
`IRFFT3D` |   
`Identity` | `T={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`IdentityN` | `T={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`If` | `Tout={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Tin={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Tcond={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Imag` | `Tout={float}`  
`T={complex64}`  
`InfeedDequeue` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`InfeedDequeueTuple` | `dtypes={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`InplaceAdd` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`InplaceUpdate` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Inv` | `T={bfloat16,complex64,float,int32,int64}`  
`Invert` | `T={int32,int64,uint32,uint64}`  
`InvertPermutation` | `T={int32}`  
`IsFinite` | `T={bfloat16,float}`  
`IsInf` | `T={bfloat16,float}`  
`IsNan` | `T={bfloat16,float}`  
`L2Loss` | `T={bfloat16,float}`  
`LRN` | `T={bfloat16,float}`  
`LRNGrad` | `T={bfloat16,float}`  
`LeakyRelu` | `T={bfloat16,float}`  
`LeakyReluGrad` | `T={bfloat16,float}`  
`LeftShift` | `T={int32,int64,uint32,uint64}`  
`Less` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`LessEqual` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`Lgamma` | `T={bfloat16,float}`  
`LinSpace` | `Tidx={int32,int64}`  
`T={bfloat16,float}`  
`ListDiff` | `out_idx={int32,int64}`  
`T={int32,int64}`  
`Log` | `T={bfloat16,complex64,float}`  
`Log1p` | `T={bfloat16,complex64,float}`  
`LogSoftmax` | `T={bfloat16,float}`  
`LogicalAnd` |   
`LogicalNot` |   
`LogicalOr` |   
`MatMul` | `T={bfloat16,complex64,float}`  
`MatrixBandPart` | `Tindex={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`MatrixDiag` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`MatrixDiagPart` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`MatrixSetDiag` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`MatrixTriangularSolve` | `T={complex64,float}`  
`Max` | `Tidx={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`MaxPool` | `T={bfloat16,float,int32,int64}`  
`MaxPool3D` | `T={bfloat16,float}`  
`MaxPool3DGrad` | `TInput={bfloat16,float}`  
`T={bfloat16,float}`  
`MaxPool3DGradGrad` | `T={float}`  
`MaxPoolGrad` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`MaxPoolGradGrad` | `T={float}`  
`MaxPoolGradGradV2` | `T={float}`  
`MaxPoolGradV2` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`MaxPoolV2` | `T={bfloat16,float,int32,int64}`  
`Maximum` | `T={bfloat16,float,int32,int64}`  
`Mean` | `Tidx={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`Min` | `Tidx={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`Minimum` | `T={bfloat16,float,int32,int64}`  
`MirrorPad` | `Tpaddings={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Mod` | `T={bfloat16,float,int32,int64}`  
`Mul` | `T={bfloat16,complex64,float,int32,int64}`  
`Multinomial` | `output_dtype={int32,int64}`  
`T={bfloat16,float,int32,int64,uint32,uint64}`  
`Neg` | `T={bfloat16,complex64,float,int32,int64}`  
`NoOp` |   
`NonMaxSuppressionV4` | `T={float}`  
`NotEqual` | `T={bfloat16,bool,complex64,float,int32,int64}`  
`OneHot` | `TI={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`OnesLike` | `T={bfloat16,bool,complex64,float,int32,int64}`  
`OutfeedEnqueue` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`OutfeedEnqueueTuple` | `dtypes={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Pack` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Pad` | `Tpaddings={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`PadV2` | `Tpaddings={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ParallelDynamicStitch` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`PlaceholderWithDefault` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Pow` | `T={bfloat16,complex64,float,int32,int64}`  
`PreventGradient` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Prod` | `Tidx={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`Qr` | `T={float}`  
`QuantizeAndDequantizeV2` | `T={bfloat16,float}`  
`QuantizeAndDequantizeV3` | `T={bfloat16,float}`  
`RFFT` |   
`RFFT2D` |   
`RFFT3D` |   
`RGBToHSV` | `T={bfloat16,float}`  
`RandomShuffle` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`RandomStandardNormal` | `T={int32,int64}`  
`dtype={bfloat16,float}`  
`RandomUniform` | `T={int32,int64}`  
`dtype={bfloat16,float}`  
`RandomUniformInt` | `T={int32,int64}`  
`Tout={int32,int64}`  
`Range` | `Tidx={bfloat16,float,int32,int64}`  
`Rank` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ReadVariableOp` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Real` | `Tout={float}`  
`T={complex64}`  
`RealDiv` | `T={bfloat16,complex64,float,int32,int64}`  
`Reciprocal` | `T={bfloat16,complex64,float,int32,int64}`  
`ReciprocalGrad` | `T={bfloat16,complex64,float}`  
`RecvTPUEmbeddingActivations` |   
`Relu` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`Relu6` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`Relu6Grad` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`ReluGrad` | `T={bfloat16,float,int32,int64,uint32,uint64}`  
`Reshape` | `Tshape={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ResizeBilinear` | `T={bfloat16,float,int32,int64}`  
`ResizeBilinearGrad` | `T={bfloat16,float}`  
`ResizeNearestNeighbor` | `T={float,int32,int64}`  
`ResourceApplyAdaMax` | `T={bfloat16,float}`  
`ResourceApplyAdadelta` | `T={bfloat16,float}`  
`ResourceApplyAdagrad` | `T={bfloat16,float}`  
`ResourceApplyAdagradDA` | `T={bfloat16,float}`  
`ResourceApplyAdam` | `T={bfloat16,float}`  
`ResourceApplyAddSign` | `T={bfloat16,float}`  
`ResourceApplyCenteredRMSProp` | `T={bfloat16,float}`  
`ResourceApplyFtrl` | `T={bfloat16,float}`  
`ResourceApplyFtrlV2` | `T={bfloat16,float}`  
`ResourceApplyGradientDescent` | `T={bfloat16,float}`  
`ResourceApplyKerasMomentum` | `T={bfloat16,float}`  
`ResourceApplyMomentum` | `T={bfloat16,float}`  
`ResourceApplyPowerSign` | `T={bfloat16,float}`  
`ResourceApplyProximalAdagrad` | `T={bfloat16,float}`  
`ResourceApplyProximalGradientDescent` | `T={bfloat16,float}`  
`ResourceApplyRMSProp` | `T={bfloat16,float}`  
`ResourceGather` | `Tindices={int32,int64}`  
`dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterAdd` | `Tindices={int32,int64}`  
`dtype={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterDiv` | `Tindices={int32,int64}`  
`dtype={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterMax` | `Tindices={int32,int64}`  
`dtype={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterMin` | `Tindices={int32,int64}`  
`dtype={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterMul` | `Tindices={int32,int64}`  
`dtype={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterNdAdd` | `Tindices={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterNdSub` | `Tindices={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterNdUpdate` | `Tindices={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterSub` | `Tindices={int32,int64}`  
`dtype={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`ResourceScatterUpdate` | `Tindices={int32,int64}`  
`dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ResourceStridedSliceAssign` | `Index={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Reverse` | `T={bool,complex64,float,int32,int64}`  
`ReverseSequence` | `Tlen={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ReverseV2` | `T={bfloat16,bool,complex64,float,int32,int64}`  
`Tidx={int32,int64}`  
`RightShift` | `T={int32,int64,uint32,uint64}`  
`Rint` | `T={bfloat16,float}`  
`Round` | `T={bfloat16,complex64,float,int32,int64}`  
`Rsqrt` | `T={bfloat16,complex64,float}`  
`RsqrtGrad` | `T={bfloat16,complex64,float}`  
`ScatterNd` | `Tindices={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Select` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Selu` | `T={bfloat16,float}`  
`SeluGrad` | `T={bfloat16,float}`  
`SendTPUEmbeddingGradients` |   
`Shape` | `out_type={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`ShapeN` | `out_type={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Sigmoid` | `T={bfloat16,complex64,float}`  
`SigmoidGrad` | `T={bfloat16,complex64,float}`  
`Sign` | `T={bfloat16,complex64,float,int32,int64}`  
`Sin` | `T={bfloat16,complex64,float}`  
`Sinh` | `T={bfloat16,complex64,float}`  
`Size` | `out_type={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Slice` | `Index={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Snapshot` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Softmax` | `T={bfloat16,float}`  
`SoftmaxCrossEntropyWithLogits` | `T={bfloat16,float}`  
`Softplus` | `T={bfloat16,float}`  
`SoftplusGrad` | `T={bfloat16,float}`  
`Softsign` | `T={bfloat16,float}`  
`SoftsignGrad` | `T={bfloat16,float}`  
`SpaceToBatch` | `Tpaddings={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`SpaceToBatchND` | `Tblock_shape={int32,int64}`  
`Tpaddings={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`SpaceToDepth` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`SparseMatMul` | `Tb={bfloat16,float}`  
`Ta={bfloat16,float}`  
`SparseSoftmaxCrossEntropyWithLogits` | `Tlabels={int32,int64}`  
`T={bfloat16,float}`  
`SparseToDense` | `Tindices={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Split` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`SplitV` | `Tlen={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Sqrt` | `T={bfloat16,complex64,float}`  
`SqrtGrad` | `T={bfloat16,complex64,float}`  
`Square` | `T={bfloat16,complex64,float,int32,int64}`  
`SquaredDifference` | `T={bfloat16,complex64,float,int32,int64}`  
`Squeeze` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`StackCloseV2` |   
`StackPopV2` | `elem_type={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`StackPushV2` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`StackV2` | `elem_type={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`StatelessIf` | `Tout={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Tin={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Tcond={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`StatelessMultinomial` | `output_dtype={int32,int64}`  
`Tseed={int32}`  
`T={bfloat16,float}`  
`StatelessRandomNormal` | `Tseed={int32}`  
`T={int32,int64}`  
`dtype={bfloat16,float}`  
`StatelessRandomUniform` | `Tseed={int32}`  
`T={int32,int64}`  
`dtype={bfloat16,float}`  
`StatelessRandomUniformInt` | `Tseed={int32}`  
`T={int32,int64}`  
`dtype={int32,int64}`  
`StatelessTruncatedNormal` | `Tseed={int32}`  
`T={int32,int64}`  
`dtype={bfloat16,float}`  
`StatelessWhile` | `T={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`StopGradient` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`StridedSlice` | `Index={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`StridedSliceGrad` | `Index={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Sub` | `T={bfloat16,complex64,float,int32,int64}`  
`Sum` | `Tidx={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`SymbolicGradient` | `Tout={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Tin={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TPUEmbeddingActivations` |   
`Tan` | `T={bfloat16,complex64,float,int32,int64}`  
`Tanh` | `T={bfloat16,complex64,float}`  
`TanhGrad` | `T={bfloat16,complex64,float}`  
`TensorArrayCloseV3` |   
`TensorArrayConcatV3` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorArrayGatherV3` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorArrayGradV3` |   
`TensorArrayReadV3` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorArrayScatterV3` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorArraySizeV3` |   
`TensorArraySplitV3` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorArrayV3` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorArrayWriteV3` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorListElementShape` | `shape_type={int32,int64}`  
`TensorListPopBack` | `element_dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorListPushBack` | `element_dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TensorListReserve` | `shape_type={int32,int64}`  
`element_dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Tile` | `Tmultiples={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TopKV2` | `T={bfloat16,float,int32,uint32}`  
`Transpose` | `Tperm={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`TruncateDiv` | `T={bfloat16,complex64,float,int32,int64}`  
`TruncateMod` | `T={bfloat16,float,int32,int64}`  
`TruncatedNormal` | `T={int32,int64}`  
`dtype={float}`  
`Unpack` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`UnsortedSegmentMax` | `Tnumsegments={int32,int64}`  
`Tindices={int32,int64}`  
`T={bfloat16,float,int32,int64,uint32,uint64}`  
`UnsortedSegmentMin` | `Tnumsegments={int32,int64}`  
`Tindices={int32,int64}`  
`T={bfloat16,float,int32,int64,uint32,uint64}`  
`UnsortedSegmentProd` | `Tnumsegments={int32,int64}`  
`Tindices={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`UnsortedSegmentSum` | `Tnumsegments={int32,int64}`  
`Tindices={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`VarIsInitializedOp` |   
`VariableShape` | `out_type={int32,int64}`  
`While` | `T={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Xdivy` | `T={complex64,float}`  
`XlaBroadcastHelper` | `Tindices={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`XlaConv` | `Tindices={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`XlaDequantize` |   
`XlaDot` | `T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`XlaDynamicSlice` | `Tindices={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaDynamicUpdateSlice` | `Tindices={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaHostCompute` | `Toutputs={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Tinputs={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaIf` | `Tout={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Tin={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Tcond={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`XlaKeyValueSort` | `V={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`K={bfloat16,float,int32,int64,uint32,uint64}`  
`XlaPad` | `Tindices={int32,int64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaRecv` | `dtype={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaRecvFromHost` | `Toutput={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaReduce` | `T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`XlaReduceWindow` | `Tindices={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`XlaSelectAndScatter` | `Tindices={int32,int64}`  
`T={bfloat16,complex64,float,int32,int64,uint32,uint64}`  
`XlaSend` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaSendToHost` | `Tinput={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaSort` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`XlaWhile` | `T={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`Xlogy` | `T={complex64,float}`  
`ZerosLike` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`_Arg` | `T={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
`_ArrayToList` | `out_types={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`_ListToArray` | `T={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`Tin={bfloat16,bool,complex64,float,int32,int64,uint32,uint64}`  
`_Retval` | `T={bfloat16,bool,complex64,float,int32,int64,resource,uint32,uint64}`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
