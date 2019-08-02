
# Copyright 2018 The AITS DNNC Authors. All Rights Reserved.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=invalid-name, unused-argument
#
# This file is part of DNN compiler maintained at 
# https://github.com/ai-techsystems/dnnCompiler

from generate_output import *

operators = {}
'''
operators['Constant'] = {
	'nodes':['helper.make_node("Constant", [], ["1"], value = onnx.helper.make_tensor(name="const_tensor", data_type=onnx.TensorProto.FLOAT, dims=values.shape, vals=values.flatten().astype(float)))'],
	'inputs':'[]',
	'outputs':'[helper.make_tensor_value_info("1", TensorProto.FLOAT, (5,5))]',
	'declarations':['values=np.random.randn(5, 5).astype(np.float32)']
}
'''
operators['BitShift'] = {
	'nodes':['helper.make_node("BitShift", ["A","B"], ["C"], direction="LEFT")'],
	'inputs':'[helper.make_tensor_value_info("A", TensorProto.INT64, (2, 3, 4)),helper.make_tensor_value_info("B", TensorProto.INT64, (2, 3, 4))]',
	'outputs':'[helper.make_tensor_value_info("C", TensorProto.INT64, (2, 3, 4))]'
}

for operator in operators.keys():
	operator_info = operators[operator]
	declarations = []
	if 'declarations' in operators[operator].keys():
		declarations = operators[operator]['declarations']
	node_params = []
	if 'node_params' in operators[operator].keys():
		node_params = operators[operator]['node_params']
	create_testcase(operator, operator_info['inputs'], operator_info['outputs'], operator_info['nodes'], declarations)
