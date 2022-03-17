cmake_minimum_required(VERSION 3.19)
project(cuda_tutorial LANGUAGES C CXX CUDA)

add_library(cuda_tutorial
        SHARED
        lltm-extension/lltm.cpp
        lltm-extension/lltm_cuda.cpp
        lltm-extension/lltm_cuda_kernel.cu)

target_include_directories(cuda_tutorial PRIVATE CMAKE_CUDA_TOOLKIT_INCLUDE_DIRECTORIES)
list(APPEND CMAKE_PREFIX_PATH "/home/ubuntu/miniconda3/envs/py37/lib/python3.7/site-packages/torch")

find_package(Torch REQUIRED)
target_include_directories(cuda_tutorial PRIVATE 
${TORCH_INCLUDE_DIRS}
/home/ubuntu/miniconda3/envs/py37/include/python3.7m
)
