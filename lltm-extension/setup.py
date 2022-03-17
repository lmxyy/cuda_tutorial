from setuptools import setup
from torch.utils import cpp_extension

setup(name='lltm',
      ext_modules=[cpp_extension.CUDAExtension('lltm_cuda', ['lltm_cuda.cpp', 'lltm_cuda_kernel.cu'])],
      cmdclass={'build_ext': cpp_extension.BuildExtension})
