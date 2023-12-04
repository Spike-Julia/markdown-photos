# CentOS 7网络连接不上

**学完韩顺平`shell`,备份完数据库后,`MobaXterm`可能错误断开远程的`ssh`连接.注:虚拟机并未关机**

**1.先导致不能`ssh`远程连接，回到之前保存的快照，发现仍然不能远程`ssh`登录。**

**至此可以排除昨晚备份MySQL的嫌疑.但是之前并没有关闭`sshd`服务，试过`ping`虚拟机，`powershell`的`telnet ip:22`也连接不上**

**2.关闭虚拟机，再关闭`VMware`，重启`Windows`主机后，再打开`VMware`，提示【该虚拟机似乎正在使用中】,如图    [VMware提示【该虚拟机似乎正在使用中】的解决方案-CSDN博客](https://blog.csdn.net/weixin_43455581/article/details/119560058)**

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/26db1e812f6547609f46ba8dcb3bfda6.png?raw=true)

<img src="https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/8b126d662f644b69aff21961b05ea2d1.png?raw=true"  />

* 首先关闭`VMware`软件，然后在虚拟机目录下`.lck`后缀的文件夹改名为`.lck.backup`即可解决！

<img src="https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/49af88dec8b64c7f938e50f3bba00c8e.png?raw=true" style="zoom:67%;" />

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/69d1390dad7d4255b712b5839ae14bee.png?raw=true)

* 这样可以进入了

  

**3.仍然不能`ssh`连接，先网络冲浪搜索解决方法，参考下面文章 **

**[SSH远程连接不了服务器的故障及排查故障的步骤-叶宇梵-博客园 (cnblogs.com)](https://www.cnblogs.com/guobaiwang/articles/12610439.html)**

**"不能ping通，可以看一下network的服务状态",这句话起到帮助，果真是network服务failed**

**如图：**

* 这是最开始的`status`状态检测

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/Snipaste_2023-12-04_13-17-27.png?raw=true)

* 第一想法就是`restart`重启或者`start`开启一下，但是结果好像失败了

[解决Linux网络“Job for network.service failed because the control process exite”问题CSDN](https://blog.csdn.net/VariatioZbw/article/details/107482739)

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/Snipaste_2023-12-04_13-22-48.png?raw=true)

* 不管怎样先看一下状态。这是`restart`后`status`检测，果然失败了，界面与之前稍有不同`RTNETLINK`

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/Snipaste_2023-12-04_13-17-26.png?raw=true)

#### **解决方案**

```shell
## 1、和 NetworkManager 服务有冲突，直接关闭 NetworkManger 服务就好了
service NetworkManager stop

## 禁止开机启动
chkconfig NetworkManager off 

## 重启网络
service network restart

```

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/Snipaste_2023-12-04_13-28-07.png?raw=true)

* 再状态检测一下，发现OK了`active`被激活

![](https://github.com/Spike-Julia/markdown-photos/blob/main/Spike-Julia/Linux/CentOS-network/Snipaste_2023-12-04_13-30-39.png?raw=true)
