// Copyright 2018 The AITS DNNC Authors.All Rights Reserved.
//
// Licensed to the Apache Software Foundation(ASF) under one
// or more contributor license agreements.See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.See the License for the
// specific language governing permissionsand limitations
// under the License.
//
// This file is part of AITS DNN compiler maintained at
// https://github.com/ai-techsystems/dnnCompiler
//

#pragma once
#include "operators/baseOperator.h"
#include <string>

using namespace Eigen;

namespace dnnc {

/*! Floor takes one input data (Tensor) and produces one output data (Tensor)
 where the floor is, \f$y = floor(x)\f$ The function is applied to the tensor
 elementwise.*/

template <typename T> class Floor : public baseOperator<T, T, T> {
public:
  Floor(std::string name = "opFloor") : baseOperator<T, T, T>(opFloor, name) {}

  tensor<T> compute(tensor<T> &a /*!<[float,double]: ND tensor*/) {

    if (!(this->template type_check<float, double>(typeid(T)))){
      LOG_F(ERROR, "Constrain input and output types to float or double tensors.");
      return a;
    }

    tensor<T> result(a.shape(), a.name());

    DNNC_EIGEN_ARRAY_MAP(eigenVector, T, a);
    DNNC_EIGEN_VECTOR_CTOR(T) eResult;

    eResult.array() = floor(eigenVector.array());

    result.load(eResult.data());
    return result;
  }
  /*!<
  \return The output tensor of the same shape and type as input.
  */
};
} // namespace dnnc