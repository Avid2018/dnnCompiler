# Copyright 2018 The DNNC Authors. All Rights Reserved.
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
#
include Makefile.common

all:FORMAT SRC DEEPC TEST

FORMAT:
	@echo $(UNAME_M)
	@echo "formatting code ..."
	-find include src -name \*.h -print0 -o -name \*.cpp -print0 | xargs -0 -P8 -n1 clang-format -i

TEST:
	@echo "running unit tests ..."
	$(shell $(LN_S) -f $(abspath ./include) $(abspath ./deepC))
	$(shell $(LN_S) -f $(abspath ./packages) $(abspath ./deepC))
	(cd test &&  $(PYTHON) ./run_all.py) || (echo "TEST failed."; exit 1)


DEEPC: SRC
	$(MAKE) -C deepC

SRC:
	$(MAKE) -C src

clean:
	$(MAKE) -C deepC clean
	$(MAKE) -C src  clean
	@$(RM) $(wildcard test/parser/unit_operators/testcases/*/*.cpp) &>/dev/null

.PHONY: print_vars

print_vars:
	@echo
