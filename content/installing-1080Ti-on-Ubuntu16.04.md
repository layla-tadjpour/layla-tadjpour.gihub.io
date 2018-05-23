Title: Installing GTX 1080Ti Drivers / CUDA-8.0 on Ubuntu 16.04
Date: 2018-05-23 
Modified: 2018-05-23 
Category: General
Tags: 
Slug: Installing GTX 1080Ti Drivers on Ubuntu 16.04
Authors: Layla Tadjpour
Summary: Installing GTX 1080Ti Drivers on Ubuntu 16.04

Update: This tutorial should also work with CUDA 9.0 and NVIDIA Driver 390.12 with minor tweaks.

[Nelson Liu's blog](http://blog.nelsonliu.me/2017/04/29/installing-and-updating-gtx-1080-ti-cuda-drivers-on-ubuntu/) 
has an excellent post about installing GTX 1080 Ti Drivers with Cuda 8.0 on Ubuntu 16.04.  
I used his blog and other online material to set up the NVIDIA’s new GTX 1080Ti graphics card for use with CUDA-enabled machine learning libraries, e.g. Keras, Tensorflow and Pytorch;
Since the card (as of this writing) was relatively new, the process was a bit cumbersome. I had to reinstall ubuntu 2 times to make it work. There are not many online resources for GTX 1080Ti and a few that I found did not work for my setup. I thought to write about my experience here.
I recommend that you start with a fresh install of Ubuntu.

## Install CUDA without the driver
For CUDA install without drive, [Abhijeet Kislay's blog](https://kislayabhi.github.io/Installing_CUDA_with_Ubuntu/)
helped me a lot. Although his is for CUDA 7.5 ,  I was able to make it work with CUDA 8.0 with some minor changes. So here I repeat most of his instructions with minor changes that I made to make it work for my own setup.

Note that you can not just install CUDA 8.0 by apt-get  because it comes with a driver version (375.26) that doesn't support the GTX 1080 Ti.  Thus, you have to install with the [runfile](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#runfile), to opt-out of installing the driver. The runfile documentation was not 
that helpful. So here is step-to-step guide: 

Go to [this address](https://developer.nvidia.com/cuda-downloads) and download CUDA toolkit 8.0 for Ubuntu 16.04 and select runfile local as your installer type. I have tested the 64 bit version but I think the 32 bit will work too if your machine is 32 bit.

Open up a terminal and extract the separate installers via:

*mkdir ~/Downloads/nvidia_installers*

*cd ~/Downloads*

*./cuda_8.0.61_linux.run -extract=~/Downloads/nvidia_installers*

It is better to start with a fresh OS install otherwise completely uninstall anything in the ubuntu repositories with nvidia. I used synaptic and did a purge, i.e., completely uninstall programs and configuration by running

*sudo apt-get --purge remove nvidia*

Create the /etc/modprobe.d/blacklist-nouveau.conf file with the 2 following lines:

*blacklist nouveau*

*options nouveau modeset=0*

Then do a

*sudo update-initramfs -u*

Reboot computer. Nothing should have changed in loading up menu. You should be taken to the login screen. Once there type: Ctrl + Alt + F1, and login to your user. Keep the next commands handy in another machine since now you are in tty.

In tty mode:

*cd ~/Downloads/nvidia_installers*

*sudo /etc/init.d/lightdm stop*

I initially ran "*sudo service lightdm stop*" but for some reason, it caused my screen to go blank.

Now, install the toolkit. Note that you don’t want to install the drivers 375 that comes with the cuda-8.0. [Nvidia documentation](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#runfile) manual states that to run "sudo sh cuda_<version>_linux.run"
and the installer will prompt for the following:

*EULA Acceptance*

*CUDA Driver installation*

*CUDA Toolkit installation, location, and /usr/local/cuda symbolic link*

*CUDA Samples installation and location*

You are supposed to ignore the driver installation. However, 
the "-sudo sh cuda_<version>_linux.run-" did not work for me. Instead I ran the following commands:

*sudo ./cuda-linux64-rel-6.0.37-18176142.run*

*sudo ./cuda-samples-linux-6.0.37-18176142.run*

Moreover, I was not prompted for the driver installation; only EULA acceptance and the directory location for cuda.

Set Environment path variables in *.bashrc*:

*export PATH=/usr/local/cuda-8.0/bin:$PATH*

*export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH*

Check CUDA driver version:

*nvcc -V*

At this point you can switch the lightdm back on again by doing:

*sudo /etc/init.d/lightdm start*

## Installing the driver with apt-get
[This Nelson Liu's blog post](http://blog.nelsonliu.me/2017/04/29/installing-and-updating-gtx-1080-ti-cuda-drivers-on-ubuntu/) has more details on how to install the driver with apt-get. I repost them here for the sake of completeness. To install the driver with apt-get, I used the Ubuntu graphics-drivers PPA. This method isn't officially supported by NVIDIA, 
but it seems to work. Also, make sure that PPA supports the version of NVIDIA driver you are using.
Add the PPA to apt-get and update the index by running:

*sudo add-apt-repository ppa:graphics-drivers/ppa*  

*sudo apt-get update*

Now, we use it to install the desired driver versions (as of this writing):
For 1080 Ti: 

*Major version 378:*

*sudo apt-get install nvidia-378*

Reboot your computer, and the GPU should run on the new driver. To verify, run nvidia-smi and confirm that the Driver Version at the top of the output is what you expect.

## Verifying the installation worked
### CUDA
To test the CUDA installation, you can run the deviceQuery example bundled with CUDA. 
If you navigate to the CUDA samples folder (*/usr/local/cuda#.#/samples* or *~/NVIDIA_CUDA-#.#_Samples* by default), you can find the deviceQuery example in *<samples_dir>/1_Utilities/deviceQuery*.

Running sudo makein this directory should compile the CUDA source file to produce a binary file and then run
./deviceQuery.o will produce a variety of statistics about your GPU and run some test on it. Here are some of the outputs:

*CUDA Device Query (Runtime API) version (CUDART static linking)*

*Detected 1 CUDA Capable device(s)*

*Device 0: “Graphics Device”*

*CUDA Driver Version / Runtime Version 8.0 / 8.0*

*CUDA Capability Major/Minor version number: 6.1*

...

*deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 8.0, CUDA Runtime Version = 8.0*

*NumDevs = 1, Device0 = Graphics Device*

*Result = PASS*

### Drivers
If the driver installation went properly, you should be able to run nvidia-smi and you should get an output detailing the memory usage and temp/ fan/GPU utilization.

