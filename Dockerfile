FROM python:3-slim-bullseye
# It's not at all clear why the image published by the llama-cpp-python author doesn't work,
# but it can't find the llama libraries, soI had to re-build the docker container
# We need to set the host to 0.0.0.0 to allow outside access
ENV HOST 0.0.0.0

COPY . .

# Install the package
RUN apt update && apt install -y libopenblas-dev ninja-build build-essential pkg-config
RUN python -m pip install --upgrade pip pytest cmake scikit-build setuptools fastapi uvicorn sse-starlette pydantic-settings starlette-context

RUN CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama_cpp_python --verbose

# Run the server
CMD python3 -m llama_cpp.server --model $MODEL --n_gpu_layers $N_GPU_LAYERS --n_batch $N_BATCH