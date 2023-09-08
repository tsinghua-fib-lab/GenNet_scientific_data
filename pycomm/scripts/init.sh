#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
PROJECT_DIR="$(dirname "${SCRIPT_DIR}")"

echo "Project Directory: ${PROJECT_DIR}"
echo "Generate proto and grpc python package"

OUTPUT_PATH_PYCOMM=${PROJECT_DIR}/pycomm/protos

INCLUDE_PATH=${PROJECT_DIR}/submodules/protos
WOLONG_PREFIX=${PROJECT_DIR}/submodules/protos/wolong
# 请修改待生成_pb2.py文件的proto文件列表
FILES="\
    ${WOLONG_PREFIX}/geo/v2/geo.proto \
    ${WOLONG_PREFIX}/comm/input/v1/config.proto \
    ${WOLONG_PREFIX}/config/v1/config.proto \
    ${WOLONG_PREFIX}/comm/interaction/optimize/v1/optimize_service.proto \
    ${WOLONG_PREFIX}/comm/interaction/sim/v1/dynamic.proto \
    ${WOLONG_PREFIX}/comm/interaction/sim/v1/coverage.proto \
    ${WOLONG_PREFIX}/comm/interaction/sim/v1/energy.proto \
    ${WOLONG_PREFIX}/comm/interaction/sim/v1/sim_service.proto \
    ${WOLONG_PREFIX}/sync/v1/sync_service.proto \
"

rm -r ${OUTPUT_PATH_PYCOMM} 2>/dev/null || true
mkdir -p ${OUTPUT_PATH_PYCOMM}

protoc --python_out=${OUTPUT_PATH_PYCOMM} -I ${INCLUDE_PATH} ${FILES}
python3 -m grpc_tools.protoc \
    -I ${INCLUDE_PATH} --grpc_python_out=${OUTPUT_PATH_PYCOMM} ${FILES}
protol --create-package --in-place --python-out ${OUTPUT_PATH_PYCOMM} \
    protoc --proto-path=${INCLUDE_PATH} ${FILES}

