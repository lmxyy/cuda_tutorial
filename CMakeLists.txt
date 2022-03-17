cmake_minimum_required(VERSION 3.19)
project(cuda_tutorial LANGUAGES C CXX CUDA)

add_library(cuda_tutorial
        SHARED
        lltm-extension/lltm.cpp
        lltm-extension/lltm_cuda.cpp
        lltm-extension/lltm_cuda_kernel.cu)

target_include_directories(cuda_tutorial PRIVATE
        3rdparty/pytorch
        3rdparty/pytorch/torch/csrc/api/include)
