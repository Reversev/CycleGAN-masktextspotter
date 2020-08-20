该项目主要借鉴了CycleGAN的网络模型实现模具数据的生成，整个项目大部分的代码都是采用了CycleGAN的网络模型，
具体可以看原来的github：https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
在原作者的基础上，进行了参数的调整和优化，在预处理和后处理都做了一些工作，最后在masktextspotter（https://github.com/lvpengyuan/masktextspotter.caffe2）
上实验证明该实验方法具有一定的可行性，除去原来GAN的代码外，该项目加入的文件夹都在对应的文件夹下加入了readme.txt文件进行了说明。


备注：环境所需要的包见environment.yml