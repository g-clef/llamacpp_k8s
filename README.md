# llamacpp_k8s
A simple Docker/FastAPI wrapper around Llama.cpp to run it in a k8s container.
It is building off of the `llama-cpp-python` library, with mostly changes around the dockerfiles
including the command line options used to launch the llama server. 

It's tailored to my home lab, so the system is designed to run on a Raspberry PI 4 that is part 
of a kubernetes cluster. The model is stored in an external SMB share, which the 
deployment will need a username/password to. It is exposed outside the cluster using MetalLB.

I'm using the mistral-7b-instruct-v0.1.Q4_K_M model, 
as it seems to give the best results so far. 